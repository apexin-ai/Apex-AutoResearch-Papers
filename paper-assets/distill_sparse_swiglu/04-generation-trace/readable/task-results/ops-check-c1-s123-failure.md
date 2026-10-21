# ops check c1 s123 failure

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-c1-s123-failure_20260518T173806_result.json`
- **Structured JSON:** [`1c096d8f4061cce8be53.json`](../../sessions/1c/1c096d8f4061cce8be53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**s123 训练实际上完全成功了。** 日志显示：

- 1000/1000 步全部完成，耗时 876.8s
- Checkpoint 已保存：`checkpoints/c1_ablation_bce_kl_targets_s123/predictor_bce_kl_targets.pt` (145MB)
- WikiText-2 评估也完成了：**PPL = 11.71, sparsity = 0.500**
- 参考对比：KL PPL = 11.79, BCE PPL = 22.51

### 失败根因

Registry 记录的 `failure_reason` 是 **"startup recovery: process dead, no active cron monitor"**。这是监控系统的误判：训练进程已经正常结束退出，但因为使用 tmux 后端且没有 cron monitor，startup recovery 扫描时发现进程不存在，就将其标记为 failed。

实际上训练和评估都正常完成，日志最后一行是 `Done.`。

### s123 vs s42 对比

| 指标 | s42 | s123 |
|------|-----|------|
| PPL | 9.29 | 11.71 |
| Sparsity | 0.609 | 0.500 |
| Agreement | 0.978 | 0.834 |
| BCE loss | 0.0545 | 0.448 |

PPL 差异大的原因：**s123 强制 sparsity_target=0.50（TEAL uniform 模式），而 s42 使用 hard mask 自然 sparsity ~60.9%。** 这不是同一评估条件，不能直接比。s42 的 notes 也提到 "11.79 PPL comparison was invalid (TEAL forced @50%)"。s123 的 11.71 实际上和 KL 的 11.79 在同条件下很接近（差 0.08），**结论与 s42 一致**。

### 建议

1. **无需重跑**。训练完全成功，只需将 registry conclusion 从 `failed` 改为 `success`，补录 metrics
2. 结果支持 C1 因果消融假设：BCE+KL targets (11.71) ≈ KL (11.79)，target quality 是 KL 优势的主要驱动因素
3. 违反了 C002 约束（用了 tmux 而非 nohup），这次碰巧训练跑完了，但监控误判。后续实验应严格遵守 nohup

是否需要我更新 registry 将 s123 标记为 success 并补录 metrics？

---
