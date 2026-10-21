# analysis 3seed summary

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_3seed_summary_20260514T183119_result.json`
- **Structured JSON:** [`5aee47e74503a07caf86.json`](../../sessions/5a/5aee47e74503a07caf86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Spearman ρ — Full (n=529)

| Signal | seed42 | seed123 | seed456 | Mean±SD |
|-------------|--------|---------|---------|--------------|
| voting_conf | 0.441 | 0.413 | 0.411 | **0.422±0.017** |
| SJ | 0.428 | 0.424 | 0.384 | **0.412±0.025** |
| EM | 0.335 | 0.337 | 0.316 | 0.329±0.011 |
| FK | 0.281 | 0.275 | 0.223 | 0.260±0.032 |
| logprob | 0.219 | 0.251 | 0.232 | 0.234±0.016 |

### Spearman ρ — Conditional (n≈477–479)

| Signal | seed42 | seed123 | seed456 | Mean±SD |
|-------------|--------|---------|---------|--------------|
| EM | 0.415 | 0.404 | 0.406 | **0.408±0.006** |
| SJ | 0.369 | 0.376 | 0.349 | **0.365±0.014** |
| voting_conf | 0.353 | 0.339 | 0.346 | 0.346±0.007 |
| FK | 0.193 | 0.178 | 0.157 | 0.176±0.019 |
| logprob | 0.156 | 0.173 | 0.171 | 0.166±0.009 |

### AUROC — Full / Conditional

| Signal | Full Mean±SD | Cond Mean±SD |
|-------------|---------------|---------------|
| EM | **0.780±0.011** | **0.788±0.009** |
| SJ | 0.728±0.015 | 0.713±0.013 |
| voting_conf | 0.721±0.012 | 0.701±0.010 |
| FK | 0.605±0.025 | 0.585±0.023 |
| logprob | 0.596±0.010 | 0.577±0.008 |

### 关键结论

- **structural > surface: 3/3 seeds**，全部一致
- **信号排序跨 seed 高度一致**：Top-3 (EM, SJ, voting_conf) vs Bottom-2 (FK, logprob) 在所有 seed 和两个 split 中无例外
- **Conditional 排序完全一致**：EM > SJ > voting_conf > FK > logprob，3 个 seed 零差异
- **EM 是最佳二分类器**（AUROC 0.780/0.788），但 ρ 排第 3；**voting_conf/SJ 是最佳连续预测器**（ρ 0.422/0.412）
- SD 极小（多数 <0.02），说明采样随机性对信号排序影响可忽略

产出已保存到 `artifacts/3seed_summary/` 并注册。

---
