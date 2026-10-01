# 4. Tool use: let code calculate

Complete [setup](00-start-here.md) first. Run from the project folder.
On Windows PowerShell, replace `python3` with `py -3`.

## Run

```sh
python3 demo.py tools
```

This example explicitly supplies `$5` per day and `2` days late in its prompt.
It does **not** read `policies/late-returns.txt`. Editing that file changes the
RAG example, not this example.

## Check

Follow the output in order:

1. Available tool: the calculator definition given to the model.
2. Actual function call: did the model request `calculate_late_fee` with
   `days_late: 2` and `daily_rate: 5`?
3. Python result: is `fee_usd` equal to `10.00`?
4. Final model response: does it accurately use that result?

A correct-looking answer alone does not prove a tool ran. Look for the actual
function call and Python result. If no function is requested, no calculation
code executes.

## Change one thing

```sh
python3 demo.py tools --question 'I am 3 days late at $7 per day. What is the fee?'
```

Keep the single quotes so your shell does not change `$7`. The expected result
is `$21.00`; check the arguments as well as the final answer.

Then try missing information:

```sh
python3 demo.py tools --question 'I am 3 days late. What is my fee?'
```

The model should ask for the daily rate, not invent one. Record what actually
happens. The model chooses the arguments; Python validates and calculates.

