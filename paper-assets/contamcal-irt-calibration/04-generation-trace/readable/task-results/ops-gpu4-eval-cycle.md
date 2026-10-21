# ops gpu4 eval cycle

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu4_eval_cycle_20260514T205625_result.json`
- **Structured JSON:** [`c0628bad1aff394a7384.json`](../../sessions/c0/c0628bad1aff394a7384.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 4 轮转完成。

**1. 1.5B d025 aligned eval 结果** (exp_001_eval_15B_d025_aligned → DONE):

| Benchmark | Score |
|-----------|-------|
| MMLU | 59.02% |
| GSM8K | 65.35% |
| ARC Challenge | 76.88% |
| HumanEval pass@1 | 22.56% |

**2. 3B d000 v2 aligned eval** (exp_001_eval_3B_d000_v2_aligned → RUNNING):
- PID 441570 on GPU 4 (cuda:4), tmux session `exp_001_eval_3B_d000_v2_aligned`
- MMLU 评估中，~39 it/s，预计 2-2.5h 完成全部 4 个 benchmark

---
