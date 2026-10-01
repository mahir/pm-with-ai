# 3. RAG: supply a retrieved policy

Complete [setup](00-start-here.md) first. Run from the project folder.
On Windows PowerShell, replace `python3` with `py -3`.

## Run

```sh
python3 demo.py rag
```

The program searches the files in `policies/` using keyword overlap, takes one
matching document, and inserts it into the prompt. No embedding model or vector
database is used in this small example.

## Check

Open `policies/late-returns.txt` in a text editor and note its current daily rate.
Use the actual value in your copy; it may have been changed during class.

- Does the yellow retrieved-source block match the file?
- Does the prompt include that source?
- Does the answer cite the source and calculate two days at that rate correctly?

## Change one thing

1. Save a copy of the original policy text.
2. Change the daily fee to `$3` and save the file as plain text with the same name.
3. Run `python3 demo.py rag` again. The expected two-day fee is now `$6`.
4. Restore the original policy text when finished.

No training is required: the next run reads the updated file.

## Try a different document

```sh
python3 demo.py rag --question 'Can I request an extension?'
```

Check whether it retrieves `extensions.txt` and mentions staff approval and
availability. A wrong source is a retrieval failure; an unsupported answer from
a relevant source is a generation failure. This simple search can miss paraphrases.

