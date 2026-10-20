# analysis dino subtask auc

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dino-subtask-auc_20260515T120832_result.json`
- **Structured JSON:** [`86445b54777efd637d7d.json`](../../sessions/86/86445b54777efd637d7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。汇总结果：

## DINO-V2 Subtask AUC Baseline 结果

| 指标 | 值 |
|------|-----|
| **Macro AUC** | **0.9717** |
| subtask_0 AUC | 0.9694 |
| subtask_1 AUC | 0.9739 |
| Per-task AUC range (subtask_0) | 0.946 - 0.981 |
| Per-task AUC range (subtask_1) | 0.907 - 0.999 |

**方法**：
- 从 LIBERO demo 的 MuJoCo state 向量中自动提取 subtask completion 标注（检测 object state 维度的 step transition，K-means 聚类成 2 个 subtask group）
- 对 DINO-V2 cls_token (1024-dim) 特征训练 sklearn LogisticRegression (L-BFGS)
- 80/20 per-task split，110K train / 27K val frames

**对 MVP 判定的影响**：
- D001 三分支判定的第三条件是 `subtask_AUC > 0.7`
- DINO-V2 baseline 的 subtask AUC = 0.9717 远超阈值
- 这意味着即使 VLA 的 temporal distance ρ 低于 DINO-V2，只要 VLA 的 subtask AUC 也超过 0.7，第三条件仍然可以满足
- 但 DINO-V2 subtask AUC 设定了一个很高的 baseline (0.97)，VLA 需要在 subtask AUC 上至少接近这个水平才有意义

已更新：registry `dinov2_baseline` metrics 添加了 subtask_auc 字段，artifact 已注册。

---
