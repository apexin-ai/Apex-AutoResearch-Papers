# ops check xvla k01 seed43 result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-xvla-k01-seed43-result_20260520T193546_result.json`
- **Structured JSON:** [`e32420db8aaa55d3cd7d.json`](../../sessions/e3/e32420db8aaa55d3cd7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验**成功完成**。结果如下：

| 项目 | 值 |
|------|-----|
| 结果文件 | `/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_prune_k01_libero_object_seed43.json` |
| 完成时间 | 2026-05-21 03:23:29 (CST) |
| 总 episodes | 500 (10 tasks × 50 episodes) |
| **overall_success_rate** | **0.0%** (0/500) |
| 95% Wilson CI | [0.0, 0.0076] |
| 耗时 | 7815.7s (~2.2h) |
| 模式 | l2_norm_prune, keep_ratio=0.1 (50→5 vision tokens) |
| seed | 43 |

所有 10 个 task 的 success_rate 均为 0.0%，mean_steps 均为 800（全部跑满上限步数）。k=0.1 只保留 5 个 vision token，对 X-VLA 来说信息损失过大，模型完全无法完成任务。

---
