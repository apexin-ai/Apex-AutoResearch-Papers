# code 19912 arcc eval then llama

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_19912-arcc-eval-then-llama_20260521T124530_result.json`
- **Structured JSON:** [`9878ece299accec20f48.json`](../../sessions/98/9878ece299accec20f48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Final Status Report

### Phase 1: ARC-C Training Check
All clean_s7-s10 training completed on westd-19912. Checkpoints present.

### Phase 2: ARC-C s7-s10 Eval Results

| Condition | theta_mle | lz_star | accuracy | n_items |
|-----------|-----------|---------|----------|---------|
| clean_s7  | 0.706     | -5.585  | 89.15%   | 295     |
| clean_s8  | 0.851     | -5.400  | 90.51%   | 295     |
| clean_s9  | 0.887     | -5.536  | 90.17%   | 295     |
| clean_s10 | 0.811     | -5.073  | 90.51%   | 295     |

All lz* values strongly negative (range -5.07 to -5.59), consistent with clean (non-contaminated) models showing expected response patterns.

### Phase 3: Llama Deployment to westd-19912
- **Model**: Llama-3.1-8B-Instruct downloaded via ModelScope (4 shards, ~15.1GB total)
- **train.py**: Written with extended SEED_MAP (s8=305, s9=306, s10=307, s11=308)
- **Data**: alpaca_data.json fetched via git sparse clone from GitHub, clean/train.jsonl generated (5000 items, MD5 matches 35694: `c3db36bad71fb0bb64e6ca77eeae6de4`)

### Phase 4: Llama Training on westd-19912

| Condition  | GPU | Seed | PID   | tmux session    | Status   |
|------------|-----|------|-------|-----------------|----------|
| clean_s8   | 0   | 305  | 32686 | llama_clean_s8  | RUNNING  |
| clean_s9   | 1   | 306  | 32762 | llama_clean_s9  | RUNNING  |
| clean_s10  | 2   | 307  | 32838 | llama_clean_s10 | RUNNING  |
| clean_s11  | 3   | 308  | 33176 | llama_clean_s11 | RUNNING  |

All 4 jobs tokenizing + training confirmed (939 steps, ~2.2s/it on GPUs 0-2, ~1.1s/it on GPU 3). ETA: ~35 min on GPU 3, ~70 min on GPUs 0-2.

### Anomalies
- GPU 3 trains ~2x faster than GPUs 0-2 (1.1s/it vs 2.2s/it) — possibly different memory contention or PCIe topology. Not a problem, just asymmetric completion times.
- eval_lz.py and mmlu_params.csv not yet transferred to 19912 (needed for MMLU eval after training, not blocking training).

### Cleanup
- HTTP server on 35694 (PID 143280) killed
- Temp files on 19912 removed

---
