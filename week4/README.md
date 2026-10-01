# CampusKit: four local AI classroom examples

Fictional equipment rental service. One model, visible inputs, no external APIs,
Python dependencies, vector database, or fine-tuning.

Students: begin with [the quick-start guide](student-guides/00-start-here.md),
then follow the separate exercise file for each example.

## Run

Start Ollama, then run from this folder:

```sh
python3 demo.py
```

Requires Python 3 and the local Ollama model `qwen3.5:4b` (already installed when
this project was created). If missing, run `ollama pull qwen3.5:4b` before class.
The first model request may take longer while loading. Subsequent calls request
that Ollama keep the model loaded for 15 minutes.

## Present one at a time

Keep [PRESENTER.md](PRESENTER.md) on your own screen for discussion questions
and talking points. These notes are not printed during the demos.

```sh
python3 demo.py prompt
python3 demo.py few-shot
python3 demo.py rag
python3 demo.py tools
```

1. **Prompting:** compare a basic instruction with explicit uncertainty guidance.
   Neither request contains the policy. An honest refusal is a valid outcome;
   the example does not depend on hallucination.
2. **Few-shot:** compare classification with and without three examples in the
   prompt. Both may work. Examples in context are not fine-tuning.
3. **RAG:** show the retrieved passage, the assembled prompt, and the answer.
   Edit `$5` to `$3` in `policies/late-returns.txt` and rerun to demonstrate a
   knowledge update without training. Restore `$5` before the next class.
4. **Tools:** show the function schema, model's actual call, Python's result, and
   the final answer. The rate is explicitly supplied in this standalone example;
   this mode does not retrieve the policy file. Editing the RAG policy therefore
   does not change this preset. A correct calculation still requires correct inputs.

Each run starts a fresh conversation. Requests use `think: false` and temperature
zero, but outputs are not guaranteed to be identical or correct. RAG uses simple
keyword overlap and one whole short document, so paraphrases can fail retrieval.
This is intentionally inspectable, not a production search system.

## Try another question

```sh
python3 demo.py rag --question "Can I request an extension?"
```

Use single quotes around custom questions containing dollar amounts in your shell
to prevent variable expansion:

```sh
python3 demo.py tools --question 'I am 3 days late at $7 per day. What is the fee?'
```

Use `--model NAME` to override the default. Keep the same model across demos for
a clearer comparison. Rehearse all four examples before class; actual outputs
are evidence, not guaranteed improvements. No model training is performed.
