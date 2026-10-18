# paper cross model appendix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_cross_model_appendix_20260517T132345_result.json`
- **Structured JSON:** [`24a912b5ccd2344fbdf4.json`](../../sessions/24/24a912b5ccd2344fbdf4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Content verified. All checks pass:

1. No em-dash (`—`) in file
2. No explanatory en-dash (` – `) in file
3. All numbers match the task data exactly:
   - RE: 0.757, 0.685, 0.601, 0.504, 0.450 (70B) / 0.797, 0.719, 0.648, 0.537, 0.496 (Qwen3)
   - NER: 0.962, 0.822, 0.666 (70B) / 0.970, 0.826, 0.674 (Qwen3)
   - BCS: 0.708, 0.599, +10.9pp, CI [+3.0, +20.1]
   - Declines: -30.7/-30.1pp (RE), -29.6/-29.6pp (NER)
4. Table uses consistent `booktabs` formatting, matching existing appendix style
5. No -ing phrase endings, no banned words, no consecutive transition words
6. Accuracy at 3 decimal places, pp at 1 decimal place
7. Approximately half a page

The section is at `main.tex:470-501` as `\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}` with label `sec:appendix_cross_model_70b`. It contains one combined table (RE + NER panels with subheadings), a paragraph on Dimension 1 results, and a paragraph on Dimension 2 (BCS-controlled) results with a two-sentence conclusion.

Qwen3 NER data was only available at counts 2, 12, 22 under the matching type+text metric; counts 6, 44, 66 are omitted per instruction.

---
