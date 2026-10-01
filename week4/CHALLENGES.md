# In-class challenges: run it, then break it

First run all four examples as they are (`python3 demo.py`, options 1 to 4). Then pick one challenge. Run from the week4 folder. On Windows PowerShell, use `py -3` instead of `python3`.

For your challenge, write down what you changed, what the model answered, and whether it was right. Be ready to share the failure you found.

## 1. Teach it something new (RAG)

Create `policies/student-discount.txt` with:

```csharp
CampusKit student discount policy (fictional classroom example)
Students with a valid university ID get a 20 percent discount on rentals of three days or more.
```

Then ask:

```sh
python3 demo.py rag --question 'Do students get a discount?'
python3 demo.py rag --question 'Is there a student discount on a two-day rental?'
```

Check: did it retrieve your file, cite it, and get the two-day case right? You added knowledge without training anything. Delete the file when you are done.

## 2. Make retrieval fail (RAG)

Ask about a late return without using the policy's words:

```sh
python3 demo.py rag --question 'I brought the camera back after the due date. Do I owe money?'
```

Check: which file did it retrieve? Did the answer stay honest about what the source says? Try another phrasing, like `'Can I keep the tripod longer?'`. A wrong source is a retrieval failure, not a model failure.

## 3. Beat the examples (few-shot)

Write a message that fits two categories:

```sh
python3 demo.py few-shot --question 'The mic died halfway through and you still charged me for the full day.'
```

Check: what did it return with and without examples? Is there a right answer? If not, the categories need a rule, not more examples.

## 4. Make it guess (tools)

Leave out the daily rate:

```sh
python3 demo.py tools --question 'I am 3 days late. What is my fee?'
```

Check: did it ask for the rate, or call the calculator with a number it made up? Look at the actual function call, not just the final answer.
