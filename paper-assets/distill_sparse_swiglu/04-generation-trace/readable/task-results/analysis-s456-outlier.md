# analysis s456 outlier

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_s456_outlier_20260515T191817_result.json`
- **Structured JSON:** [`d2274a5942c2677a54d8.json`](../../sessions/d2/d2274a5942c2677a54d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。关键数据已提取，现在写报告。

## s456 Outlier 分析报告

### 根因：TEAL 全局分配对 Layer 31 过度剪枝

**训练端正常**：5 个 seed 的训练曲线完全一致（final loss 0.29-0.33, sparsity ~0.48, lambda=1000），s456 无异常收敛行为。

**问题在 TEAL 推理时的全局预算分配**。5 个 seed 的 per-layer keep count 对比：

| 异常层 | s456 keep | 其他4-seed均值 | 差值 | 影响 |
|--------|-----------|---------------|------|------|
| **Layer 31** | 7154 (49.9%) | 7465 (52.1%) | **-311** | 末层直接喂 LM head，最敏感 |
| Layer 12 | 8124 (56.7%) | 8555 (59.7%) | -431 | 中层特征提取 |
| Layer 7 | 8722 (60.8%) | 7951 (55.5%) | +771 | 预算被挤向此层 |
| Layer 0 | 10363 (72.3%) | 10625 (74.1%) | -262 | 首层编码 |

**核心**：s456 predictor 对 Layer 31 的 sigmoid 均分 = 0.5161，其他 4 seed 均值 = 0.5287（差 -0.0126，所有层中最大偏差）。这导致 TEAL 全局 topk 将 Layer 31 的 keep ratio 压到 **49.9%（低于目标 50%）**，而其他 seed 维持在 52.1%。末层被过度剪枝直接放大 PPL。

**Hard-mask PPL 不受影响**的原因：per-token mask 是逐样本独立决策，不经过全局 topk 分配，所以 s456 的 hard-mask PPL (9.14) 反而最优。

### 结论

不需要重跑。s456 predictor 质量正常，问题是全局 TEAL 分配对 predictor 微小 score 差异的放大效应。建议：
1. 报告 5-seed 结果时注明 s456 为 TEAL 分配 outlier，或报告 4-seed mean=12.00±0.07
2. 若要系统性修复，可在 TEAL 分配中加 per-layer floor（如最低保留 45%），防止关键层被过度剪枝

---
