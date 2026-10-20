# analysis c2 n500 partial verify

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c2_n500_partial_verify_20260515T044019_result.json`
- **Structured JSON:** [`c1836a79811a220bac15.json`](../../sessions/c1/c1836a79811a220bac15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。s030 缺失被优雅跳过。核心结果汇总：

## Partial Analysis (s015 + s020 + s025, n=500)

### DeepSeek

| Condition | Median II diff | 95% CI | Bonf. p |
|-----------|---------------|--------|---------|
| imp_s015 | +0.391 | [0.350, 0.443] | <0.0001 |
| imp_s020 | +1.215 | [1.107, 1.337] | <0.0001 |
| imp_s025 | +3.986 | [3.527, 4.359] | <0.0001 |
| rand_s015 | +0.014 | [-0.017, 0.039] | 1.0 (ns) |
| rand_s020 | +0.032 | [-0.011, 0.077] | 1.0 (ns) |
| rand_s025 | +0.257 | [0.127, 0.350] | 0.019 |

- **Imp-vs-rand** median_diff: s015=+0.423, s020=+1.291, s025=+4.197 (all p<0.0001)
- **Within-imp d_z**: s015→s020 = -0.468 (small), s020→s025 = -0.156 (negligible)
- **Dose-response**: monotonic=True, Spearman ρ=1.000

### Qwen

| Condition | Median II diff | 95% CI | Bonf. p |
|-----------|---------------|--------|---------|
| imp_s015 | +0.066 | [0.049, 0.093] | <0.0001 |
| imp_s020 | +0.307 | [0.261, 0.356] | <0.0001 |
| imp_s025 | +1.075 | [0.977, 1.179] | <0.0001 |
| rand_s015 | -0.011 | [-0.039, 0.012] | 1.0 (ns) |
| rand_s020 | +0.015 | [-0.015, 0.068] | 1.0 (ns) |
| rand_s025 | +0.393 | [0.236, 0.553] | <0.0001 |

- **Imp-vs-rand** median_diff: s015=+0.099, s020=+0.315, s025=+0.757 (all p<0.0001)
- **Within-imp d_z**: s015→s020 = -0.509 (medium), s020→s025 = -0.642 (medium)
- **Dose-response**: monotonic=True, Spearman ρ=1.000

### 统计方法审计结论

全部 **PASS**:
- ✅ Median + percentile bootstrap CI (B=10000) — 符合 D054
- ✅ Wilcoxon signed-rank 检验
- ✅ Imp-vs-rand 只报 Wilcoxon + median_diff，不报 d_z — 符合 D059
- ✅ Bonferroni 校正

### 注意事项
- **s030** 的 4 个 condition 结果文件尚未生成（目录已存在但无 profiling_results.json）
- **s025 已全部完成**（之前说法是 s025 在跑——现在 12/12 个 condition 的 s015-s025 都已有完整数据）
- rand_s025 在两个模型上都显著（DS p=0.019, QW p<0.0001），这说明 25% sparsity 下随机剪枝也开始产生可观测影响
- DeepSeek 的 s020→s025 d_z 仅 -0.156 (negligible)，但绝对 median diff 从 1.22 跳到 3.99——可能是方差增大导致 d_z 偏小

---
