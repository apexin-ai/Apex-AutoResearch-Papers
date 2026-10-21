# analysis per task mse breakdown

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_per_task_mse_breakdown_20260519T061435_result.json`
- **Structured JSON:** [`a7e15d5df40628115bc6.json`](../../sessions/a7/a7e15d5df40628115bc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已写入 `/root/autodl-tmp/vla-ssd/results/per_task_mse_breakdown.json`。

---

## Per-Task MSE Breakdown

| Task | n | Original MSE | Top-24 Ablated MSE | ΔMSE (%) | p | Bottom-24 Ablated MSE | ΔMSE (%) | p |
|---|---|---|---|---|---|---|---|---|
| open_middle_drawer | 500 | 0.5621 | 0.5474 | -0.0147 (-2.6%) | 0.351 | 0.5600 | -0.0021 (-0.4%) | 0.770 |
| open_drawer_put_bowl | 500 | 0.5484 | 0.5581 | +0.0097 (+1.8%) | 0.274 | 0.5577 | +0.0094 (+1.7%) | 0.887 |
| push_plate_to_stove | 500 | 0.3834 | 0.3851 | +0.0018 (+0.5%) | 0.447 | 0.4006 | +0.0173 (+4.5%) | **0.029** |
| **Overall** | **1500** | **0.4980** | **0.4969** | **-0.0011** | **0.519** | **0.5061** | **+0.0082** | — |

## Cancellation 判断

**Top-24 ablation**: 存在弱符号混合（drawer -2.6%, bowl +1.8%, plate +0.5%），但**所有 per-task ΔMSE 均不显著**（p > 0.27）。最大变化幅度仅 2.6% of baseline MSE。这不是有意义的 cancellation，而是各任务效果都极小。

**Bottom-24 ablation**: 无 cancellation。方向一致（drawer ~0, bowl +1.7%, plate +4.5%）。plate 任务是唯一显著增加的（p=0.029），符合预期：ablating non-instruction heads 对需要精细空间定位的 push 任务影响略大。

**结论**: 整体 ΔMSE 接近零反映的是**各任务效果本身就小**，而非大的正负效果互相抵消。审稿人的 cancellation 假设不成立。

---
