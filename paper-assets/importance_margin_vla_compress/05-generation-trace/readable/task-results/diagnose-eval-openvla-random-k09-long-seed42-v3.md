# diagnose eval openvla random k09 long seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_random_k09_long_seed42_v3_20260525T134439_result.json`
- **Structured JSON:** [`debd422095b2842123f0.json`](../../sessions/de/debd422095b2842123f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**CRON 误报，实验已正常完成。**

`eval_openvla_random_k09_long_seed42_v3` 跑完了全部 500 episodes，**Overall SR = 46.80%**，结果已保存到 JSON 文件。CRON 报错是因为 eval 脚本不写 W&B metrics，监控找不到 W&B 数据就误判为失败。

其他 3 个实验状态：
| 实验 | 状态 | SR |
|------|------|-----|
| attn_k09_long_v3 (GPU 0) | **运行中** — Task 10/10, Ep ~40/50 | 即将完成 |
| attn_k085_long_v3 (GPU 1) | **已完成** | 45.80% |
| l2norm_k09_long_v3 (GPU 3) | **运行中** — Task 10/10, Ep ~30/50 | 即将完成 |

两个需要注意的问题：
1. CRON 监控应对 eval 任务改为检查 JSON 结果文件，而非 W&B metrics
2. `attn_k085` 实验的结果文件被命名为 `openvla_l2norm_prune_k085_10.json`（mode 标签错误），可能是脚本中结果文件命名 bug

报告已保存到 `artifacts/diagnose_random_k09_long_v3.md`。

---
