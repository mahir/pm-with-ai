# 2. Few-shot prompting: add examples

Complete [setup](00-start-here.md) first. Run from the project folder.
On Windows PowerShell, replace `python3` with `py -3`.

## Run

```sh
python3 demo.py few-shot
```

The model classifies the same customer message twice: first with instructions
only, then with three example message/answer pairs included in the prompt.
The expected category for the preset charge question is `BILLING_QUESTION`.

## Check

- Find the three examples in the second cyan block.
- Did each answer return the expected category and only that category?
- Did the examples improve, worsen, or leave the result unchanged?

Examples do not guarantee improvement. They are sent in the request; no training
or model weight updates happen.

## Change one thing

```sh
python3 demo.py few-shot --question 'The microphone stopped working.'
```

The expected category is `EQUIPMENT_PROBLEM`. Record both outputs. A correct
answer on one message is not evidence that every message will be classified correctly.

