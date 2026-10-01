# Codex classroom demonstration prompts

Use these in the `pm-with-ai` project. These are prompts to run during class,
not features already implemented in the Python demo.

Suggested sequence: inspect → plan → implement → review → pursue a goal.
For a short session, prioritize plan, implement, and review. Rehearse beforehand;
execution time depends on the work and failures encountered.

## 1. Inspect the project

> Read the week4 project and explain how information reaches the model in each of the four examples. Use a small comparison table. Identify which examples read policy files and which execute Python functions. Do not change any files.

Observe whether the explanation is grounded in the actual files.

## 2. Plan a change

Select Plan mode, then paste:

> I want example 4 to retrieve the late-return policy before calling the calculator, instead of supplying the rate in the question. Inspect the current implementation. Propose the smallest change, explain what could go wrong, and define how we would verify it. Keep the existing standalone tool example available. Do not implement yet.

Discuss the proposed scope and verification before proceeding.

## 3. Implement the approved plan

Switch out of Plan mode after approving the plan, then paste:

> Implement the approved plan as a fifth example called “RAG + tools.” Keep the same terminal formatting and use no new dependencies. Update the student instructions. Run it with the current policy and show the retrieved rate, actual calculator arguments, and final answer. Do not push yet.

Inspect the file changes and actual execution results.

## 4. Review the result

Open a fresh chat in the same project after implementation:

> Review the changes that add “RAG + tools.” Look for incorrect fee calculations, invented policy values, missing-information handling, and misleading student instructions. Report concrete findings with file references. Do not edit files.

Compare building the feature with independently checking it.

## 5. Pursue a goal

Use the Goal control available in your app, with this prompt:

> Create a goal: make the new “RAG + tools” example pass a small, repeatable evaluation. Cover two different daily rates, zero days late, and missing days late. Success means the retrieved rate matches the policy, valid inputs produce the correct calculator result, and missing inputs trigger clarification rather than invented values. Keep the original four examples working, restore policy files after testing, and report actual results. Do not weaken the checks to make them pass. Do not push.

A goal defines an outcome and completion criteria; the next action depends on
what the evaluation reveals. Demonstrate pausing and resuming if time permits.
An ordinary prompt remains appropriate for a small, bounded edit.

Reference: [OpenAI's guide to Goals in Codex](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex).

## Optional: parallel delegation

> Use two subagents in parallel. Have one inspect the student setup instructions for confusing steps and the other inspect how the examples handle missing information. Neither should edit files. Combine their findings into three prioritized improvements.

Observe separate investigations and their combined findings.
