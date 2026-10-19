# paper table2 multiseed update

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table2-multiseed-update_20260518T034508_result.json`
- **Structured JSON:** [`37fd8cde05fba7cbd703.json`](../../sessions/37/37fd8cde05fba7cbd703.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

LaTeX compiles without errors (14 pages, no warnings in the output).

**Summary of changes:**

**Task 1 - Table multi-seed updates:**
- **Tab:main BCE row** (`experiments.tex:56`): All downstream metrics now show 3-seed mean±std: ARC-c 27.6±0.6, WG 51.8±0.6 (was 50.59), MMLU 26.1±0.5, GSM8K 2.1±0.2
- **ARC-C bolding at 30%** (`experiments.tex:48-49`, `experiments.tex:165-166`): Moved bold from TEAL (42.32) to KL global (43.9±3.9) in both tab:main and tab:phase
- **Section 5.2 text** (`experiments.tex:66-67`): BCE PPL updated to 28.13±0.20 (3-seed), ratio to 2.39×, percentage to 139%
- **137% → 139%**: Updated in abstract (line 3), introduction (lines 15, 24), and experiments (line 67) to reflect multi-seed BCE mean

**Task 2 - SNR extended data:**
- **method.tex:151-152**: Replaced 80-step/5.76× initial measurement with extended 7-checkpoint measurement: 5.14× at step 300 ($5.88{\times}10^{-3}$ vs $1.14{\times}10^{-3}$), with 95% CI and non-monotonic trajectory description. The appendix (app:snr\_extended) with full trajectory was already in place.

---
