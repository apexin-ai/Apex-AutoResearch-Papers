# analysis exp022 stats design

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp022_stats_design_20260516T092618_result.json`
- **Structured JSON:** [`53eeca74bbc837d86832.json`](../../sessions/53/53eeca74bbc837d86832.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。以下是结构化汇报：

---

## exp-022 统计设计检查结果

### 1. 每 cell 数据粒度

Pipeline 输出**三层粒度**：

| 粒度 | 结构 | 数量/cell |
|------|------|-----------|
| per-doc 特征 | `features.csv`: 5000 docs × 6 depths = 30000 行 | 30000 |
| per-fold AUC | `pairwise_auc.json["per_fold"]`: 5 depth-pairs × 5 folds | 25 |
| K* (标量) | max depth where AUC > 0.60 | **1** |

### 2. CV 设置

- **5-fold GroupKFold**，以 `doc_id` 为 group（同一文档的不同 depth 不跨 fold）
- 每个 depth-pair（如 0v1）独立训练 LightGBM 分类器
- 每个 cell 默认 `num_samples=5000`

### 3. 总观测数（16 cells）

| 分析目标 | 观测数 | 可行性 |
|----------|--------|--------|
| ANOVA on K* | 16 cells × 1 K* = **16** | **不可行** (df_residual ≈ 6, 极低功效) |
| ANOVA on per-fold AUC | 16 cells × 5 pairs × 5 folds = **400** | **充分** |
| Mixed-effects on per-doc 预测 | 16 × 30000 = **480000** | 过剩，但可提取更细指标 |

### 4. ANOVA 可行性 — df 分析

**如果 DV = K*（1 per cell）：**
- Total df = 15
- Generator: df=3, Scorer: df=3, Interaction: df=9
- **Residual df = 0** → F 检验不可计算

**如果 DV = fold-level AUC（25 per cell）：**
- Total df = 399
- Generator: 3, Scorer: 3, DepthPair: 4, Gen×Scorer: 9, Gen×Depth: 12, Scorer×Depth: 12
- Residual df ≈ 356 → **充分**
- 可以做 3-way ANOVA (Generator × Scorer × DepthPair) 或 linear mixed model with fold as random effect

### 5. pairwise_auc.json 完整格式

```json
{
  "mean": {
    "0v1": 0.987,
    "1v2": 0.6262,
    "2v3": 0.5496,
    "3v4": 0.5294,
    "4v5": 0.5182
  },
  "per_fold": {
    "0v1": [0.9881, 0.9884, 0.9852, 0.9851, 0.9882],
    "1v2": [0.5963, 0.6362, 0.6366, 0.6337, 0.6282],
    "2v3": [0.5516, 0.5456, 0.5403, 0.5605, 0.5501],
    "3v4": [0.5515, 0.5133, 0.5198, 0.5350, 0.5276],
    "4v5": [0.5207, 0.5393, 0.5186, 0.5169, 0.4956]
  }
}
```

### 6. 建议

**Pipeline 无需修改**——数据粒度已经足够，问题在于分析层面如何使用它。

**exp-022 分析方案：**

1. **主分析**：3-way repeated-measures ANOVA，DV = fold AUC，factors = Generator(4) × Scorer(4) × DepthPair(5)。Fold 作为 block/random effect。总 N=400，残差 df 充裕。

2. **K* 的替代处理**：不做 K* 的 ANOVA。改为：
   - 用 per-fold AUC 拟合 logistic decay curve → 得到 per-fold K*（AUC 跌破 0.60 的插值点）→ 16 cells × 5 folds = 80 个 K* → 2-way ANOVA (Gen × Scorer) with residual df=48
   - 或直接报告 K* 的 4×4 heatmap + bootstrap CI（对 5 个 fold AUC resample 1000 次，每次重新计算 K*）

3. **Bootstrap CI**：当前 pipeline 无 bootstrap。建议在 exp-022 的后处理脚本中加 bootstrap（从 per-fold AUC resample），而非改 `run_pipeline.py`。

**结论：Dream 审稿意见正确——如果只看 16 个 K* 做 ANOVA 确实无法工作。但 pipeline 已产出 per-fold AUC（25 obs/cell），足以支撑严格的多因素统计分析。exp-022 脚本只需在后处理中选择正确的 DV 和分析模型。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "mean": {
      "0v1": 0.987,
      "1v2": 0.6262,
      "2v3": 0.5496,
      "3v4": 0.5294,
      "4v5": 0.5182
    },
    "per_fold": {
      "0v1": [
        0.9881,
        0.9884,
        0.9852,
        0.9851,
        0.9882
      ],
      "1v2": [
        0.5963,
        0.6362,
        0.6366,
        0.6337,
        0.6282
      ],
      "2v3": [
        0.5516,
        0.5456,
        0.5403,
        0.5605,
        0.5501
      ],
      "3v4": [
        0.5515,
        0.5133,
        0.5198,
        0.535,
        0.5276
      ],
      "4v5": [
        0.5207,
        0.5393,
        0.5186,
        0.5169,
        0.4956
      ]
    }
  }
}
```

</details>

---
