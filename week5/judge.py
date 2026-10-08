#!/usr/bin/env python3
"""Week 5: check the judge before you trust it.

The scam checker writes a one-line reason for each verdict. Code can't tell a
good reason from a made-up one, so we ask a model to judge it. Before trusting
that judge, we run it on reasons a person already labeled (reasons.json) and
count how many bad reasons it caught and how many good ones it failed.

  python3 judge.py            check the judge against the hand labels
  python3 judge.py --latest   then use it on the reasons from your last eval.py run
  python3 judge.py --model NAME
"""
import argparse
import json
import sys
import urllib.error

from eval import MODEL, ROOT, ask, color, one_line, parse

JUDGE = """You are checking one thing only.
Does the reason name something in the text?
Answer PASS if it does, FAIL if it does not.
Then quote the words that decided it."""


def judge(text, reason, model):
    answer = ask(JUDGE, f"Text: {text}\nReason: {reason}", model)
    return answer.strip().upper().startswith("FAIL"), answer


def check_the_judge(model):
    labeled = json.loads((ROOT / "reasons.json").read_text())
    caught = missed = false_alarms = ok = 0
    print(color(f"\nJudging {len(labeled)} reasons a person already labeled\n", "cyan"))
    for item in labeled:
        judge_fail, answer = judge(item["text"], item["reason"], model)
        human_fail = item["human"] == "fail"
        if human_fail and judge_fail:
            caught += 1
            result = "caught"
        elif human_fail:
            missed += 1
            result = "MISSED"
        elif judge_fail:
            false_alarms += 1
            result = "FALSE ALARM"
        else:
            ok += 1
            result = "ok"
        style = "green" if result in ("caught", "ok") else "red"
        print(f"{color(f'{result:>11}', style)}  {item['id']:>2}  {one_line(item['reason'], 70)}")
        if result in ("MISSED", "FALSE ALARM"):
            print(f"{'':>15}{color('person:', 'cyan')} {item['human']} ({item['note']})")
            print(f"{'':>15}{color('judge:', 'yellow')}  {one_line(answer)}")
            print()

    print(color(f"\nCatch rate:      {caught} of {caught + missed} bad reasons", "bold"))
    print(color(f"False alarms:    {false_alarms} of {false_alarms + ok} good reasons", "bold"))
    print(color(f"Plain agreement: {caught + ok} of {len(labeled)}.", "bold"))
    print("Look at the first two numbers before you trust it.\n")


def judge_latest_run(model):
    latest = ROOT / "runs" / "latest.json"
    if not latest.exists():
        sys.exit(color("No run found. Run python3 eval.py first.", "red", sys.stderr))
    run = json.loads(latest.read_text())
    flagged = 0
    print(color(f"Judging the reasons from the eval run of {run['when']}\n", "cyan"))
    for row in run["rows"]:
        out = parse(row["output"])
        if not out or not out.get("reason"):
            continue
        judge_fail, answer = judge(row["text"], out["reason"], model)
        flagged += judge_fail
        status = color("FAIL", "red") if judge_fail else color("PASS", "green")
        print(f"{status}  {row['id']:>2}  {one_line(out['reason'], 80)}")
    print(color(f"\nThe judge failed {flagged} reasons. Read them: is it right?\n", "bold"))


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("--latest", action="store_true",
                        help="after checking the judge, use it on the last eval.py run")
    args = parser.parse_args()
    try:
        check_the_judge(args.model)
        if args.latest:
            judge_latest_run(args.model)
    except urllib.error.URLError as e:
        sys.exit(color(f"\nCould not reach Ollama. Is it running? ({e})", "red", sys.stderr))


if __name__ == "__main__":
    main()
