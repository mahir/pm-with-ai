# 1. Prompting: change the instructions

Complete [setup](00-start-here.md) first. Run from the project folder.
On Windows PowerShell, replace `python3` with `py -3`.

## Run

```sh
python3 demo.py prompt
```

The same late-return question runs twice in separate conversations. The second
request explicitly tells the model not to invent policies. Neither request
includes a policy file.

## Check

- Compare the cyan instruction blocks: what was added?
- Does either green response claim to know a fee or policy it was not given?
- Does the second answer acknowledge missing information?

Both answers might admit uncertainty. A more confident answer is not necessarily better.

## Change one thing

```sh
python3 demo.py prompt --question 'Can I get a refund if I return the camera early?'
```

Write down one unsupported claim, or note that the model correctly said it did
not know. Did changing the instructions supply any new business facts?

