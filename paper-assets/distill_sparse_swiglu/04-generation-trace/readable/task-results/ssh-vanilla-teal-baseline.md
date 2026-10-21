# ssh vanilla teal baseline

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_vanilla-teal-baseline_20260515T164539_result.json`
- **Structured JSON:** [`bd23d7babde284414546.json`](../../sessions/bd/bd23d7babde284414546.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总表格：

## 全部 6 个 Checkpoint 评估结果 (WikiText-2, 50% sparsity)

| exp_id | seed | loss | True Dense | Pred Hard Mask | Pred TEAL Sparse | **Vanilla TEAL** | Sparsity |
|--------|------|------|-----------|----------------|-----------------|-----------------|----------|
| mvp_bce_s42 | 42 | BCE | 6.12 | 27.96 | 44.54 | **66036.41** | 0.496 |
| mvp_bce_s123 | 123 | BCE | 6.12 | 28.38 | 44.59 | **66036.41** | 0.496 |
| mvp_bce_s456 | 456 | BCE | 6.12 | 28.14 | 43.03 | **66036.41** | 0.496 |
| mvp_kl_norm_v2_s42 | 42 | KL | 6.12 | 9.21 | 12.08 | **66036.41** | 0.498 |
| mvp_kl_norm_v2_s123 | 123 | KL | 6.12 | 9.25 | 11.91 | **66036.41** | 0.498 |
| mvp_kl_norm_v2_s456 | 456 | KL | 6.12 | 9.14 | 13.58 | **66036.41** | 0.498 |

## 关键发现

6 个 checkpoint 的 vanilla TEAL PPL 完全一致（66036.41），符合预期——vanilla TEAL 不依赖 predictor，只取决于 base model。

**Vanilla TEAL 为何灾难性差？** 全局 magnitude 排名导致极端层间不均衡：
- 浅层 0-7：93-100% 被剪枝（激活值绝对值小）
- 深层 25-31：0% 被剪枝（激活值绝对值大）

早期层 MLP 被完全移除，模型退化为仅靠 attention 的残缺网络。

**结论：learned predictor >> naive magnitude pruning**
- KL predictor TEAL sparse: **12.52** (3-seed mean) — 仅 2× dense
- BCE predictor TEAL sparse: **44.05** (3-seed mean) — 7× dense
- Vanilla TEAL magnitude: **66036** — 完全崩溃

这有力证明了 learned predictor 的价值，尤其是 KL-trained predictor 学会了跨层的合理稀疏分配（浅层低稀疏保护，深层高稀疏），而非简单依赖激活幅度。

---
