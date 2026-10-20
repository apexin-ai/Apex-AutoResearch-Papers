# code a025 analysis prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_a025-analysis-prep_20260515T002306_result.json`
- **Structured JSON:** [`f88ba8fe1c21c69d3fbe.json`](../../sessions/f8/f88ba8fe1c21c69d3fbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

---

## 分析 Pipeline 就绪状态报告

### 1. 使用方式

```bash
cd /root/autodl-tmp/distrib_canary_collapse
python analyze_alpha_sweep.py --results_dir results/alpha_sweep --max_lag 3 --n_permutations 5000
```

参数：
- `--results_dir`：默认 `results/alpha_sweep`，自动发现所有 `a\d{3}_s\d+(_v\d+)?` 目录
- `--output_dir`：默认 `{results_dir}/analysis/`
- `--max_lag`：默认 3
- `--n_permutations`：默认 5000
- **不支持指定单个 α**，自动扫描全部匹配目录

输出：
- `results/alpha_sweep/analysis/alpha_sweep_analysis.json`
- `results/alpha_sweep/analysis/summary.txt`

### 2. 数据状态

| Run | Gens (目录) | metrics.json | all_metrics.json | 状态 |
|-----|------------|--------------|------------------|------|
| a000_s42 | gen_0~gen_10 (11) | 11 | 有 | **完成** |
| a025_s42 | gen_0~gen_8 (9目录) | 8 (gen_0~7) | 无 | **运行中** |

Pipeline 读 `gen_N/metrics.json`，不依赖 `all_metrics.json`，所以 a025 完成后直接可用。MIN_GENERATIONS=4，当前 8 gen 已满足。

### 3. Metric 字段覆盖

a025_s42 的 metrics.json 包含：`token_entropy, self_bleu, distinct_1, distinct_2, distinct_3, ece, effective_rank, perplexity, mauve, generation`

Pipeline 需要的字段全部存在：
- Canary: `token_entropy`, `ece` ✅
- Downstream: `distinct_1`, `distinct_2`, `distinct_3`, `perplexity` ✅

### 4. 覆盖度 Checklist

| 分析模块 | 状态 |
|----------|------|
| Metric extraction（时间序列） | ✅ `extract()` + `orient()` |
| Naive cross-correlation (max_lag=3) | ✅ `naive_xcorr()` |
| Differenced cross-correlation | ✅ `diff_xcorr()` |
| Toda-Yamamoto Granger | ✅ `toda_yamamoto()` + ADF order detection |
| Permutation Granger | ✅ `perm_granger()` → 调用 `permutation_granger.py` |
| BH FDR 多重比较校正 | ✅ `apply_bh_fdr()` via `multipletests(method='fdr_bh')` |
| Effect size (Cohen's r / f²) | ✅ `_cohen_r_label()` / `_f2_label()` |
| Method consistency matrix | ✅ `build_consistency()` (≥2 consensus, ≥3 strong) |
| `permutation_granger.py` 可导入 | ✅ 文件存在 |
| 已有 analysis/ 历史输出 | ✅ 上次 a000 单点分析的结果已在 |

**缺失项**：
- **Threshold-based onset 检测**：❌ 代码中未实现独立 onset detection 函数
- **Cohen's f² df<20 suppress 分类**：⚠️ `_f2_label()` 不检查 df，但 `toda_yamamoto()` 返回 `df_resid`，summary 中未做 df<20 suppress 逻辑

### 5. 分析命令（a025 完成后直接运行）

```bash
cd /root/autodl-tmp/distrib_canary_collapse
python analyze_alpha_sweep.py --results_dir results/alpha_sweep --max_lag 3 --n_permutations 5000
```

将同时分析 a000_s42 + a025_s42 两个 α 点，输出覆盖 `results/alpha_sweep/analysis/`。

### 6. 需要的后处理步骤

1. **等 a025 训练完成**（gen_8+ 产出 metrics.json）
2. 运行上述命令
3. 检查 `summary.txt` 中 α=0.25 vs α=0.0 的 significance rate 差异
4. 如需 onset detection，需另写脚本或手动从时间序列判断拐点
5. 如需 df<20 时 suppress effect size 分类，需修改 `write_summary()` 中的 effect size 输出逻辑

---
