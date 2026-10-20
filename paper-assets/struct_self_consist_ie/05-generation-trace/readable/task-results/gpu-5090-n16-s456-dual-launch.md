# gpu 5090 n16 s456 dual launch

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_5090_n16_s456_dual_launch_20260521T123213_result.json`
- **Structured JSON:** [`3b9bb83015b1ed4c7aad.json`](../../sessions/3b/3b9bb83015b1ed4c7aad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments confirmed.

## 状态报告

### exp_scierc_n16_s456 — **DONE (success)**
- **Server**: autodl-5090, cuda:2
- **Results**: greedy_f1=0.664, oracle_f1=0.806, headroom=0.142, rho_sj_full=0.369, rho_sj_cond=0.348
- **Verdict**: MARGINAL
- **Registry**: updated to DONE with full metrics

### exp_conll_n16_s456 — **RUNNING**
- **Server**: autodl-5090, **cuda:1** (30150 MiB loaded)
- **PID**: 41031
- **Progress**: vLLM loaded, prompts rendered (3453/3453), now processing 55248 total requests (3453 instances × 16 samples)
- **Status**: just started sampling (0% processed prompts)

CoNLL will take a while — 55K inference requests on a single 5090. Estimated ~30-60 min based on SciERC's 551×16=8816 requests completing in ~20 min (6× more data).

---
