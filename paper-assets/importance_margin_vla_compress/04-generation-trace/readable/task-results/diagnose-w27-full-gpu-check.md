# diagnose w27 full gpu check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w27_full_gpu_check_20260528T045845_result.json`
- **Structured JSON:** [`d039b66b1d7bec99ab04.json`](../../sessions/d0/d039b66b1d7bec99ab04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 completed experiments updated to DONE. Summary:

## westd-27271

| GPU | 实验 | 状态 | 结果 |
|-----|------|------|------|
| cuda:0 | eval_pi05_random_k095_long_seed44_strict_w27 | **DONE** ✅ | SR=**61.2%**, 153.9min |
| cuda:1 | eval_pi05_random_k07_long_seed44_strict_w27 | **RUNNING** | T8 ep40, 69.5% cumulative, ~116min elapsed, ETA ~30min |

## cqa1-33015

| GPU | 实验 | 状态 | 结果 |
|-----|------|------|------|
| cuda:0 | eval_pi05_l2norm_k05_long_seed45_strict_cqa1 | **RUNNING** | T6 done (52.9%), entering T7, ~172min elapsed, ETA ~60min |
| cuda:1 | eval_pi05_attn_k095_long_seed45_strict_cqa1 | **RUNNING** | T8 ep20 (80.8%), ~174min elapsed, ETA ~30min |
| cuda:2 | eval_pi05_random_k075_long_seed45_strict_cqa1 | **DONE** ✅ | SR=**64.6%**, 239.2min |
| cuda:3 | eval_pi05_l2norm_k09_long_seed45_strict_cqa1 | **DONE** ✅ | SR=**80.0%**, 204.8min |

**空闲 GPU**: westd-27271 cuda:0, cqa1-33015 cuda:2, cuda:3

---
