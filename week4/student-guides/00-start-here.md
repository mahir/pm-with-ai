# Start here: run the examples on your computer

You will compare prompting, examples in a prompt, retrieved documents, and a
calculator tool. CampusKit and all its policies are fictional. No training is required.

## 1. Set up once, before class

1. Download and extract the class project folder. Keep `demo.py`, `policies/`,
   and `student-guides/` together. You do not need Git.
2. Install [Ollama](https://ollama.com/download) for your operating system and
   start it. On Linux, follow the instructions on its download page.
3. Install a current stable [Python 3](https://www.python.org/downloads/) if needed.
4. Open Terminal on Mac/Linux or PowerShell on Windows. Type `cd ` followed by
   the path to the extracted project folder, in quotes, and press Enter.
   This is the folder containing `demo.py`, not the `student-guides` subfolder.
5. Download the model:

```sh
ollama pull qwen3.5:4b
ollama list
```

Wait until the download finishes and the model appears in the list. Download
time and local performance depend on your connection and computer. Once the
software and model are installed, the demos use the local Ollama server; no API
key or internet connection is needed for the runs. No `pip install` is required.

## 2. Start the menu

Mac/Linux:

```sh
python3 demo.py
```

Windows PowerShell:

```powershell
py -3 demo.py
```

Choose `1`, `2`, `3`, or `4`, then press Enter. The program shows the preset
question and instructions before running:

1. Type your own question, or press Enter to keep the displayed question.
2. Type replacement instructions, or press Enter to keep the displayed instructions.
3. Inspect the actual prompt and response, then press Enter to return to the menu.

Type plain text at these prompts; no shell quotes are needed, even for dollar
amounts. Each selection starts fresh with the presets, not the previous run's edits.
In example 1, your instructions replace only the second request's instructions;
the first remains the baseline. In example 2, they apply to both requests and the
example pairs remain unchanged. In examples 3 and 4, they replace the system
instructions; retrieval and calculator code remain in place.

Enter `q` at the example menu to quit.
In all the guides below, Windows users should replace `python3` with `py -3`.
Commands with single-quoted questions work in PowerShell and Mac/Linux shells;
use PowerShell rather than Windows Command Prompt.

Prompts have cyan headings, model responses green, and source/tool details yellow.
Labels still distinguish them if your terminal does not display colors.

## 3. Try the four exercises

- [1 — Prompting](01-prompting.md)
- [2 — Few-shot prompting](02-few-shot.md)
- [3 — RAG](03-rag.md)
- [4 — Tool use](04-tools.md)

For each exercise, note what you changed, what the model answered, and whether
the answer was correct. Different outputs from your instructor's are valid observations.

After running all four examples, pick one [in-class challenge](../CHALLENGES.md).

## If something fails

| Problem | Try this |
|---|---|
| `ollama` or Python command not found | Complete its installation, reopen the terminal, and try again. |
| Cannot find `demo.py` | Change into the extracted project folder. |
| Cannot connect to Ollama | Start the Ollama app. If using the CLI server, run `ollama serve` in another terminal; if it reports the port is already in use, a server may already be running. |
| Model not found | Run `ollama pull qwen3.5:4b` and wait for completion. |
| Slow response or timeout | The first request can take longer to load. Close memory-heavy apps and try again. If your machine cannot run it, pair with a classmate; speed is not the learning objective. |
| Odd or wrong answer | Check the displayed prompt, source, and tool arguments. Record the failure rather than assuming the method worked. |
