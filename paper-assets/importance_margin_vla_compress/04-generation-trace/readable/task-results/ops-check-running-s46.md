# ops check running s46

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_running_s46_20260528T120713_result.json`
- **Structured JSON:** [`9fb3773dabcdb639a633.json`](../../sessions/9f/9fb3773dabcdb639a633.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个进程均已退出，日志确认完成。现在更新 registry。

## 汇总

| # | 实验 | 进程 | 日志 SR | ROADMAP | 一致 |
|---|------|------|---------|---------|------|
| 1 | `eval_pi05_attn_k095_long_seed46_strict_w38` | **DEAD** | **75.2%** (EXIT_CODE=0) | 75.2% | ✓ |
| 2 | `eval_pi05_random_k05_long_seed46_strict_w41` | **DEAD** | **50.2%** (EXIT_CODE=0) | 50.2% | ✓ |
| 3 | `eval_pi05_random_k095_long_seed46_strict_w41` | **DEAD** | **60.8%** (EXIT_CODE=0) | 60.8% | ✓ |
| 4 | `eval_pi05_l2norm_k095_long_seed46_strict_w27` | **DEAD** | **87.2%** (EXIT_CODE=0) | 87.2% | ✓ |

所有 4 个实验：进程已退出、EXIT_CODE=0 正常完成、SR 与 ROADMAP 记录完全一致。需要我把 registry 状态从 RUNNING 更新为 DONE 吗？

---
