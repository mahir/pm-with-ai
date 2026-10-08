# Week 5: one eval, one fix

A scam checker for text messages. You give it a text, and it answers "scam" or
"safe" with a one-line reason. We run it on 20 texts, check each answer against
the one we expect, and save every score. All the companies, links and phone
numbers in the texts are made up.

Same setup as Week 4: Python 3, Ollama running, and `ollama pull qwen3.5:4b`.
No API key and no `pip install`.

## Run it

```sh
cd week5
python3 eval.py
```

On Windows PowerShell, use `py -3 eval.py`.

For each text it prints PASS or FAIL. For each failure it shows what the model
said, what we expected, and why it failed. Then the score, how many scams it
caught, how many false alarms it raised, the failures by category, and the
score history.

## The loop

1. Run `python3 eval.py`.
2. Read the failures. Pick the category that costs the most, not just the most common one.
3. Change one line in `prompt.md`.
4. Run it again and compare the last two rows of the score history.

A change that fixes one text can break another. That is why it reruns all 20.

## Files

- `prompt.md`: the scam checker's prompt. This is the file you change.
- `texts.json`: 20 texts (11 scams, 9 safe), each with the answer we expect and
  a short note on why. Do not change it between runs, or the scores stop being
  comparable.
- `eval.py`: runs every text and checks each answer.
- `judge.py` and `reasons.json`: check a model as judge before you trust it. Optional.
- `scores.csv` and `runs/`: written by `eval.py`. Each run adds a row to
  `scores.csv`, and `runs/latest.json` holds every raw output.

## What the checks look for

| Failure | When |
|---|---|
| missed a scam | The text is a scam and the checker said safe. The costly one. |
| false alarm | The text is safe and the checker said scam. |
| not JSON | The reply is not a JSON object. Code fences are allowed. |
| no reason | No reason given. |
| reason too long | The reason is over 25 words. |

Code can check the verdict, because each text has one right answer. Code can't
tell whether the reason is true to the text. That is what the judge is for.

Two of the expected answers are choices you can argue with:

- "hey is this Dan? sorry, wrong number" is marked scam, because that is how
  many long cons start. Plenty of people would call it safe.
- The real bank fraud alert ("Reply YES or NO. We will never ask for your PIN")
  is marked safe, even though it looks like the scam version.

Writing expected answers forces decisions like these. That is part of the point.

## Check the judge (optional)

```sh
python3 judge.py
```

`reasons.json` holds 10 reasons a person already labeled good or bad. Some bad
ones are vague ("This message looks suspicious."), and some name things that
are not in the text. The judge reads each one, and the script prints how many
bad reasons it caught, how many good ones it failed, and plain agreement.

Once you trust it, `python3 judge.py --latest` uses it on the reasons from
your last `eval.py` run. To improve the judge, edit `JUDGE` at the top of
`judge.py` and run it again.

## Limits

Requests use temperature 0, but outputs are not guaranteed to be identical
between runs or machines. Twenty texts is a small set: a change of one or two
between runs can be noise, so look at which texts changed, not only the score.
The checks are simple on purpose, so you can read every one of them.
