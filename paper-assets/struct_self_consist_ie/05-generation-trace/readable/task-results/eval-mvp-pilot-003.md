# eval mvp pilot 003

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mvp_pilot_003_20260514T080934_result.json`
- **Structured JSON:** [`8c73cee83ef642dc6e76.json`](../../sessions/8c/8c73cee83ef642dc6e76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the full **mvp_pilot_003** report:

---

## mvp_pilot_003 Results — SciERC Joint (NER+RE), N=8, T=1.0, 551 instances

### Fixes applied vs mvp_pilot_002
- Merged model (not LoRA adapter) — loaded successfully
- max_tokens=1024 (up from 512) — **0 parse failures** (was 164/4408 stochastic + 29/551 greedy)
- XGrammar constrained JSON decoding working correctly

### NER

| Metric | Value |
|--------|-------|
| Greedy F1 | 0.6362 |
| Oracle F1 | 0.7920 |
| Oracle headroom | **+15.6pp** |
| Fleiss κ mean | 0.2488 |
| Soft Jaccard mean | 0.5066 |
| Full ρ(κ,F1) | +0.3362 (p=1.93e-15, n=529) |
| Full ρ(SJ,F1) | **+0.3808** (p=1.07e-19, n=529) |
| Cond ρ(κ,F1) | +0.3187 (p=1.33e-13, n=514) |
| Cond ρ(SJ,F1) | **+0.3836** (p=1.83e-19, n=514) |
| SJ > κ | **YES** (delta=+0.0446) |
| Sample F1 mean/std | 0.515 / 0.333 |
| Sample F1=0 | 19.9% |
| Gold-empty filtered | 22 |
| All-samples-F1=0 filtered | 15 |

### RE

| Metric | Value |
|--------|-------|
| Greedy F1 | 0.3774 |
| Oracle F1 | 0.5939 |
| Oracle headroom | **+21.7pp** |
| Fleiss κ mean | 0.0879 |
| Soft Jaccard mean | 0.3958 |
| Full ρ(κ,F1) | +0.2221 (p=7.92e-06, n=397) |
| Full ρ(SJ,F1) | **+0.2367** (p=1.85e-06, n=397) |
| Cond ρ(κ,F1) | +0.2374 (p=1.19e-05, n=333) |
| Cond ρ(SJ,F1) | **+0.3004** (p=2.25e-08, n=333) |
| SJ > κ | **YES** (delta=+0.0146) |
| Sample F1 mean/std | 0.198 / 0.325 |
| Sample F1=0 | **67.6%** |
| Gold-empty filtered | 154 |
| All-samples-F1=0 filtered | 64 |

### Verdict: **FAIL**

RE full ρ_sj = 0.2367 < 0.40 threshold. Warning: >30% samples F1=0 on RE.

### Key observations vs mvp_pilot_001

- **Parse failures eliminated** (0 vs 193) — max_tokens=1024 + XGrammar working
- **NER improved slightly**: greedy F1 0.636 vs 0.611, ρ_sj 0.381 vs 0.362
- **RE improved slightly**: greedy F1 0.377 vs 0.355, oracle 0.594 vs 0.572
- **RE SJ now beats FK on full set** (was false in 001, now true) — delta +0.0146
- **RE conditional ρ_sj = 0.30** — approaching MARGINAL territory (0.30 threshold)
- **RE sample F1=0 at 67.6%** is the core problem — most RE samples produce garbage, crushing the correlation signal. The 154 gold-empty instances (28%) + 64 all-zero instances further reduce effective n.

The structural consistency signal exists (all p-values highly significant, SJ consistently beats κ) but RE is too noisy at T=1.0 with the current model quality. The warning recommends T=0.7 as next step.

---
