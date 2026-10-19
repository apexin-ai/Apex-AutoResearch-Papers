# analysis training dynamics prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_training-dynamics-prep_20260515T182816_result.json`
- **Structured JSON:** [`1abb71aea0e4c4d6a296.json`](../../sessions/1a/1abb71aea0e4c4d6a296.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，产出已注册 (`art_20260515_3df68e`)。

5个核心发现：

1. **快速收敛** — 所有 run 的 peak R@1 出现在第一个 epoch 内 (500–1000 steps)，后续训练主要是 overfitting
2. **非对称过拟合** — val_loss 劣化 15–21%，但 R@1 仅降 0.2–4.7pp，排序质量比 loss 幅度更鲁棒
3. **指标分歧普遍** — 60% 的 run 中 val_loss 和 R@1 选出不同最优 checkpoint；建议双指标保存、以 R@1 选模型
4. **seed 方差主导策略效应** — 跨 seed R@1 std ≈ 2.5pp，同 seed 策略差 < 0.7pp；s44 val split 系统性偏易，paired within-seed 比较才有意义
5. **Early stopping 有效** — patience=2 在所有 run 中都捕获了最佳 R@1 checkpoint，3-epoch run 浪费了 53% 算力但没提升

TBD 项已标注，需要 dataflow_aware 和 BM25 runs 完成后才能做完整策略对比和 ANOVA。

---
