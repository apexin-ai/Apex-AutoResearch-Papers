# train cuda3 experiment

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_cuda3_experiment_20260524T155729_result.json`
- **Structured JSON:** [`c9b0c4a7dd4a65189900.json`](../../sessions/c9/c9b0c4a7dd4a65189900.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动，汇报如下：

**实验**: `permuted_score_control_seed42`
- **GPU**: cuda:3 @ westd-41312, PID 962652
- **Hypothesis**: Permuted q-scores（将真实 q_score 随机打乱分配给样本）应该比 uniform 更差，证明 detector 的 provenance signal 是 adaptive weighting 的关键——而非仅仅权重的非均匀性在起作用。
- **数据**: `scored_data_random_shuffle.jsonl` (371,499 samples)，weighting_method=adaptive
- **配置**: 6103 steps, B=4, grad_accum=4, lr=5e-5, tau=0.8, n_min=2, seed=42
- **预计时长**: ~3h50m（~2.26s/step）
- **预期结果**: holdout PPL 应高于 uniform baseline (~17.25)，与 random_reweight 实验形成互补 ablation

---
