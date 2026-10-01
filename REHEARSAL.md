# Rehearsal observations — October 1, 2026

Actual local runs using `qwen3.5:4b`. These are observations from one rehearsal,
not accuracy estimates or promises about future runs.

| Example | Observed result |
|---|---|
| Basic prompt | Invented details about fees and replacement costs without a source. |
| Explicit uncertainty instruction | Said it lacked CampusKit policy information. |
| Classification without examples | Correctly returned `BILLING_QUESTION`. |
| Classification with examples | Incorrectly returned `EQUIPMENT_PROBLEM` for the same billing question. Use this to discuss evaluating changes rather than assuming improvement. |
| RAG, $5 daily policy | Retrieved `late-returns.txt`, cited it, and answered $10 for two days. |
| RAG, policy changed to $3 | Retrieved the updated file and answered $6. Restored the file to $5 afterward. |
| Tool use | Requested `calculate_late_fee` with `days_late=2`, `daily_rate=5`. Python returned `10.00`; the final answer used $10. |

Observed model request times ranged from approximately 0.2 to 3.9 seconds.
This is not a systematic latency benchmark; loading and machine activity can
change timings. The tool example makes two requests.

Also checked Python syntax, retrieval for late returns and extensions,
calculator arithmetic, rejection of negative days, and restoration of the policy.

If the live model is unavailable, use this explicitly labeled rehearsal record
to discuss what happened. It is a summary of observed results, not a live run.
