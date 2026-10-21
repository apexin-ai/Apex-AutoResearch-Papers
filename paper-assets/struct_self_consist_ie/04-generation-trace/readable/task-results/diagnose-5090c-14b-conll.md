# diagnose 5090c 14b conll

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_5090c_14b_conll_20260521T003634_result.json`
- **Structured JSON:** [`93091739b6cbd00ae79a.json`](../../sessions/93/93091739b6cbd00ae79a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

---

## 1. 14B Inference (exp_14b_inference_fewnerd)

**Status: N=8 running on cuda:0** — PID 252310, 1896/301184 prompts (1%), ETA ~6-10h.

FewNERD completed so far:
| N | greedy_f1 | oracle_f1 | ρ(SJ,F1) | Verdict |
|---|-----------|-----------|----------|---------|
| 1 | 0.7985 | 0.7541 | NaN | FAIL |
| 2 | 0.7985 | 0.8086 | 0.205 | FAIL |
| 4 | 0.7984 | 0.8544 | 0.314 | MARGINAL |
| 8 | — running — | | | |

`kill_after_n8.sh` (PID 224789) is active, will terminate after N=8 completes.

SciERC and CoNLL 14B N=1-16 all completed previously.

## 2. CoNLL seed=123 T-ablation — ALL DONE

All 3 runs completed successfully, all PASS, all structural > surface:

| T | greedy_f1 | oracle_f1 | κ_mean | ρ(κ,F1) | ρ(SJ,F1) | Δ_struct | Verdict |
|---|-----------|-----------|--------|---------|----------|----------|---------|
| 0.5 | 0.9073 | 0.9351 | 0.894 | 0.453 | 0.460 | +0.007 | PASS |
| **0.8** | **0.9068** | **0.9466** | **0.825** | **0.472** | **0.485** | **+0.013** | **PASS** |
| 1.2 | 0.9072 | 0.9550 | 0.668 | 0.409 | 0.435 | +0.027 | PASS |

T=0.8 has the highest ρ — sweet-spot replicated across seeds. T=1.2 has the largest structural advantage (Δ=+0.027) but lowest absolute correlation.

## 3. GPU Availability

| GPU | Status | Memory |
|-----|--------|--------|
| cuda:0 | **BUSY** — 14B N=8 inference | 31.1/32.6 GB |
| cuda:1 | **FREE** | 0/32.6 GB |
| cuda:2 | **FREE** | 0/32.6 GB |
| cuda:3 | **FREE** | 0/32.6 GB |

**3 GPUs idle**, available for new work.

---
