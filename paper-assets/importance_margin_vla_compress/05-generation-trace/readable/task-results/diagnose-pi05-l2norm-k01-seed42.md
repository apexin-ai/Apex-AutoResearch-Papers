# diagnose pi05 l2norm k01 seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-l2norm-k01-seed42_20260521T195305_result.json`
- **Structured JSON:** [`4a4783426636f8892979.json`](../../sessions/4a/4a4783426636f8892979.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完毕。诊断结果：

**实验正常完成**，cron 误判（eval 实验不用 W&B）。

| 项目 | 值 |
|------|-----|
| 实验 | `eval_pi05_l2norm_k01_object_seed42` |
| 状态 | DONE / success |
| **Overall SR** | **2.6%** (13/500) |
| 耗时 | 117.5 min |
| 结果文件 | `pi05_l2norm_k0.10_libero_object_seed42.json` |

Per-task: cream_cheese 最高 6%，butter 和 milk 为 0%。k=0.1（仅保留 10% token）下性能接近崩塌，符合预期——这为 scaling law 曲线提供了有效的下界数据点。

---
