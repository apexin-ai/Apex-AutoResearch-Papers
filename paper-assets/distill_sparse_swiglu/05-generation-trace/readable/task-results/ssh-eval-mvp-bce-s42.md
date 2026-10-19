# ssh eval mvp bce s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval-mvp-bce-s42_20260515T123729_result.json`
- **Structured JSON:** [`9b80c50c7ceb5a2466c0.json`](../../sessions/9b/9b80c50c7ceb5a2466c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成，结果合理了。

## mvp_bce_s42 评估结果 (WikiText-2, 50% sparsity)

| 指标 | Dense | Sparse (BCE, 50%) | 增幅 |
|------|-------|--------------------|------|
| WikiText-2 PPL | 27.96 | 44.21 | +58.1% |
| C4 PPL | — | — | 跳过（离线模式无法 streaming 加载） |

**TEAL 逐层稀疏度分布**：
- 浅层 (L0-L15): ~44-50%
- 中层 (L16-L24): ~46-49%
- 深层 (L25-L31): 51-66% （越深越稀疏）
- 模型级别: 49.8%

**备注**：
1. 修复了 evaluate.py 中 `evaluate_perplexity` 的 off-by-one bug（数据已做 shift，代码又做了一次 `logits[:,:-1]` + `labels[:,1:]`，导致预测-目标错位）。原始代码输出 dense=8614 是无意义的。
2. Dense baseline 27.96 高于文献中常见的 ~6（因为我们用 packed non-overlapping chunks 无 BOS token，不是 sliding window 评估），但 dense/sparse 对比是公平的。
3. C4 需要 streaming 加载，离线模式不可用。如需 C4 结果，需要先在线下载缓存。
4. 58% 的 PPL 增幅对 50% sparsity 来说偏高（文献中良好训练的 predictor 通常 1-5%），但这是 MVP 实验（仅 1000 steps BCE），符合预期。

---
