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

Terminal colors help you scan: green for passes and judge agreement, red for
failures and judge mistakes, yellow for failure details, and cyan for headings
and labels. Scores are bold. PASS/FAIL labels stay visible without color.
Colors turn off when output is piped or redirected, or when `NO_COLOR` is set.

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

`eval.py` runs two kinds of checks, the first two of the four ways to check from class.

**1. Reference examples** (`check_reference`): compare the verdict to the answer key.

| Failure | When |
|---|---|
| missed a scam | The text is a scam and the checker said safe. The costly one. |
| false alarm | The text is safe and the checker said scam. |

**2. Code rules** (`check_rules`): need no answer key, so they would work on new texts too.

| Failure | When |
|---|---|
| not JSON | The reply is not a JSON object. Code fences are allowed. |
| verdict is not scam or safe | The verdict is anything else. |
| no reason, reason too long | No reason, or a reason over 25 words. |
| link plus money, marked safe | The never rule: a text with a link and a money word is never safe. |

Code can't tell whether the reason is true to the text. That needs a person
(human review) or a model you have checked (`judge.py`).

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
