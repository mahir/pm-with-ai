# Presenter notes

Keep this guide on your own screen. The terminal shows the actual inputs and
outputs; it does not print these talking points.

## 1. Prompting

Run `python3 demo.py prompt`.

Ask: “What information does the model actually have?”

Compare the two answers. Instructions guide behavior but do not supply the
missing policy. Either answer may correctly admit uncertainty.

## 2. Few-shot prompting

Run `python3 demo.py few-shot`.

Ask: “What changed in the second request?”

The examples are in the prompt, not learned through training. Compare both
classifications with the expected answer, `BILLING_QUESTION`. Adding examples
does not guarantee improvement; in our initial rehearsal it made this answer worse.

## 3. RAG

Run `python3 demo.py rag`.

Point to the retrieved source before discussing the answer. Change `$5` to `$3`
in `policies/late-returns.txt` and rerun. Ask: “Did we retrain the model?”

The file is reread and retrieved context is inserted into a new request.
Keyword retrieval can miss relevant passages. Restore `$5` after the demonstration.

## 4. Tool use

Run `python3 demo.py tools`.

Point to the model's function call, Python's result, and the final response.
Ask: “Which part did the model do, and which part did the program do?”

The model selected arguments; Python performed the arithmetic. Check both.
This standalone example gets the rate from its prompt, not the policy file.
If no function was requested despite complete inputs, the model did not complete
the tool-use task; don't present its answer as evidence of tool execution.
