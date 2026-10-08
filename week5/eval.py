#!/usr/bin/env python3
"""Week 5: run the scam checker on a fixed test set, check every answer, save the score.

Uses the same local Ollama model as week 4. No API key and no pip install.

  python3 eval.py              run all 20 texts, print failures and the score
  python3 eval.py --show-all   also print the raw output for texts that passed
  python3 eval.py --model NAME use a different Ollama model

Edit prompt.md, run it again, and compare the scores in scores.csv.
Do not edit texts.json between runs, or the scores stop being comparable.
"""
import argparse
import csv
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODEL = "qwen3.5:4b"
OLLAMA = "http://localhost:11434/api/chat"
MAX_REASON_WORDS = 25


def ask(system, user, model):
    """One request to the local model. Returns the text it wrote."""
    payload = dict(model=model, stream=False, think=False, keep_alive="15m",
                   options={"temperature": 0, "num_predict": 200},
                   messages=[{"role": "system", "content": system},
                             {"role": "user", "content": user}])
    request = urllib.request.Request(OLLAMA, data=json.dumps(payload).encode(),
                                     headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=180) as response:
        return json.load(response)["message"].get("content", "")


def parse(text):
    """The model's reply as a dict, or None if it is not a JSON object.
    Code fences are allowed. Any other text around the JSON is a failure."""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.S).strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text).strip()
    try:
        out = json.loads(text)
    except json.JSONDecodeError:
        return None
    return out if isinstance(out, dict) else None


def check(out, want):
    """Compare one output to the answer we expect ("scam" or "safe").
    Returns failures in plain words. An empty list means the text passed."""
    if out is None:
        return ["not JSON"]
    fails = []
    verdict = str(out.get("verdict") or "").strip().lower()
    if want == "scam" and verdict != "scam":
        fails.append("missed a scam")
    if want == "safe" and verdict != "safe":
        fails.append("false alarm")

    reason = str(out.get("reason") or "").strip()
    if not reason:
        fails.append("no reason")
    elif len(reason.split()) > MAX_REASON_WORDS:
        fails.append("reason too long")
    return fails


def one_line(text, width=100):
    text = " ".join(text.split())
    return text if len(text) <= width else text[:width - 3] + "..."


def save(rows, version, model, passed):
    runs = ROOT / "runs"
    runs.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    record = {"when": stamp, "prompt_version": version, "model": model,
              "passed": passed, "total": len(rows), "rows": rows}
    for name in (f"{stamp}.json", "latest.json"):
        (runs / name).write_text(json.dumps(record, indent=2, ensure_ascii=False))

    scores = ROOT / "scores.csv"
    is_new = not scores.exists()
    with scores.open("a", newline="") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(["when", "prompt_version", "model", "passed", "total"])
        writer.writerow([stamp, version, model, passed, len(rows)])
    with scores.open() as f:
        return list(csv.DictReader(f))


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("--show-all", action="store_true",
                        help="print the raw output for every text, not only failures")
    args = parser.parse_args()

    prompt = (ROOT / "prompt.md").read_text()
    texts = json.loads((ROOT / "texts.json").read_text())
    version = hashlib.sha1(prompt.encode()).hexdigest()[:7]
    print(f"\n{len(texts)} texts, prompt.md version {version}, model {args.model}\n")

    rows, start = [], time.monotonic()
    for item in texts:
        try:
            raw = ask(prompt, item["text"], args.model)
        except urllib.error.HTTPError as e:
            sys.exit(f"\nOllama returned an error: {e.read().decode()[:200]}\n"
                     f"Is the model installed? Try: ollama pull {args.model}")
        except urllib.error.URLError as e:
            sys.exit(f"\nCould not reach Ollama at {OLLAMA}. Is it running? ({e.reason})")
        fails = check(parse(raw), item["want"])
        rows.append({**item, "output": raw, "fails": fails})
        print(f"{'PASS' if not fails else 'FAIL'}  {item['id']:>2}  {one_line(item['text'], 80)}")
        if fails or args.show_all:
            print(f"          said:     {one_line(raw)}")
        if fails:
            print(f"          expected: {item['want']} ({item['note']})")
            print(f"          why:      {', '.join(fails)}")

    passed = sum(not row["fails"] for row in rows)
    scams = [r for r in rows if r["want"] == "scam"]
    safes = [r for r in rows if r["want"] == "safe"]
    caught = sum("missed a scam" not in r["fails"] and "not JSON" not in r["fails"] for r in scams)
    alarms = sum("false alarm" in r["fails"] for r in safes)
    counts = Counter(f for row in rows for f in row["fails"])

    print(f"\nScore: {passed} of {len(rows)} passed ({passed / len(rows):.0%})"
          f"   [{time.monotonic() - start:.0f} seconds]")
    print(f"Scams caught: {caught} of {len(scams)}.  False alarms: {alarms} of {len(safes)} safe texts.")
    if counts:
        print("\nFailures by category (one text can fail more than one check):")
        for name, n in counts.most_common():
            print(f"  {n:>2}  {name}")

    history = save(rows, version, args.model, passed)
    print("\nScore history (scores.csv):")
    for run in history[-5:]:
        print(f"  {run['when']}  prompt {run['prompt_version']}  {run['model']}"
              f"  {run['passed']} of {run['total']}")
    print("\nEvery output from this run is in runs/latest.json.\n")


if __name__ == "__main__":
    main()
