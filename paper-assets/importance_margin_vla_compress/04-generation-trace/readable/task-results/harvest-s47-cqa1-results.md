# harvest s47 cqa1 results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_s47_cqa1_results_20260528T234651_result.json`
- **Structured JSON:** [`48b036b09b31c5430817.json`](../../sessions/48/48b036b09b31c5430817.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这 4 个实验**仍在运行中**，尚未完成。服务器时区是 +0800，日志显示实验于今天 06:23-06:34 启动，距今约 1-1.5 小时。

当前进度：

| 实验 | 已完成 Task | 最后日志时间 | 当前累计 SR |
|------|------------|-------------|------------|
| `eval_pi05_attn_k07_long_seed47_cqa1` | T0-T2 (3/10) | 07:43 | 69.3% (104/150) |
| `eval_pi05_attn_k075_long_seed47_cqa1` | T0-T2 (3/10) | 07:45 | 69.3% (104/150) |
| `eval_pi05_l2norm_k05_long_seed47_cqa1` | T0-T2 (3/10) | 07:42 | 66.0% (99/150) |
| `eval_pi05_l2norm_k07_long_seed47_w41` | T3 进行中 (ep30) | 07:46 | T0-T2: 80.7% (121/150) |

每个 task 约 20-25 min，10 个 task 预计总时长 ~3.5-4h。预计完成时间约 **10:00-10:30 服务器时间**（北京时间，即 UTC 02:00-02:30）。

日志末尾无报错，进程正常。现在无法提取最终 SR，需要等实验跑完再来检查。要不要稍后再查？

---
