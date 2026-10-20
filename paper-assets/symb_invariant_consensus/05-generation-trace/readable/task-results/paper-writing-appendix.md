# paper writing appendix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_appendix_20260517T184655_result.json`
- **Structured JSON:** [`0596b704c55945697288.json`](../../sessions/05/0596b704c55945697288.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Changes made:

**`main.tex`**:
- Added `\usepackage{listings}` with `\lstset` config for prompt template formatting
- Replaced Limitations placeholder with `\input{limitations_content}` (reuses existing file)

**`appendix.tex`** now contains four sections:
- **Limitations** (via `\input` in main.tex before `\appendix`)
- **Appendix A: Prompt Templates** — system prompt, math extraction prompt, logic extraction prompt, JSON output schema, LLM config (T=0.1, max\_tokens=1024), all in `lstlisting` blocks
- **Appendix B: Statistical Power Analysis** — table with 3 confirmatory conditions ($n \geq 200$), MDE and observed power from `power_analysis_summary.txt` (actual computed values: MDE 4.64pp/4.84pp for LLaMA conditions, not the approximate task values)
- **Appendix C: Bootstrap Confidence Intervals** — table with 95% CIs, all including zero; Qwen CI from summary data, LLaMA CIs from task specification (should verify against `bootstrap_cis.json` on server)

---
