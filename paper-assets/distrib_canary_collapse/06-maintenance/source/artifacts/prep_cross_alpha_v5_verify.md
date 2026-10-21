# cross_alpha_analysis_v4.py 五点分析验证报告

**日期**: 2026-05-15
**脚本位置**: `/root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py` (873行)

---

## 1. α 点支持验证

### ✅ 自动发现机制——无需修改

`discover_alpha_dirs()` 使用 `glob.glob("a*_s42")` 动态发现所有 alpha 目录，不存在硬编码 4 点的问题。

- `a000_s42` → α=0.0 ✅
- `a025_s42` → α=0.25 ✅
- `a050_s42` → α=0.50 ✅
- `a075_s42` → α=0.75 ✅（实验完成后自动识别）
- MVP `rep_42` → α=1.0 ✅（`include_mvp` 逻辑：仅当 alpha_sweep 中无 α=1.0 时追加）

`a100_s42` 不存在于 alpha_sweep，所以 MVP 4-seed 数据会被正确加载。

**不支持 `--alphas` 参数**，但有位置参数 `alpha_dirs` 可手动指定目录名。默认自动发现即可。

---

## 2. FDR 修复验证（D029/D030 决策）

### ✅ consensus_framework.py `load_sig_matrix` (用于 α=1.0 MVP 路径)

```python
if method == "threshold_onset":
    sig[mi, pi, si] = seed_rec[method].get("significant", False)      # 无FDR
else:
    sig[mi, pi, si] = seed_rec[method].get("significant_fdr", False)  # BH FDR
```

完全匹配 D029/D030 混合策略。

### ✅ cross_alpha_analysis_v4.py `run_consensus_per_alpha` (用于非 MVP α 点)

非 MVP 路径从头计算 5 方法，FDR 处理逻辑：

1. **threshold_onset**: `threshold_lead()` 返回 `significant` 但无 `p_value`/`p_raw` → `p_val is None` → 直接写入 `sig_matrix` → 不参与 FDR 修正 ✅
2. **naive_pearson, differenced_xcorr, toda_yamamoto**: 返回 `p_value` → 存入 `p_raw_matrix` → BH FDR 修正后覆写 `sig_matrix` ✅
3. **permutation_granger**: 返回 `p_raw` → `res.get("p_value", res.get("p_raw"))` 正确获取 → BH FDR ✅

FDR 修正范围：per-method per-seed across 16 pairs。单 seed 时 16 tests/family，与 MVP 的 64 tests/family (4 seeds × 16 pairs) 范围不同，但统计上合理。

### ✅ cross_alpha_analysis_v4.py `apply_fdr` (主 Granger 分析)

对所有 alpha × direction 的 permutation Granger p_raw 做全局 BH FDR（所有有效 test 一起修正），结果存入 `p_fdr` 字段。

---

## 3. permG/TY 列顺序验证

### ✅ 三个文件完全一致

| 文件 | 方法列表 |
|------|---------|
| `method_ablation.py:391` | `["naive_pearson", "differenced_xcorr", "threshold_onset", "toda_yamamoto", "permutation_granger"]` |
| `consensus_framework.py:8-13` | `METHOD_NAMES` = 同上 |
| `cross_alpha_analysis_v4.py:62-63` | `MA_METHODS` = 同上 |

TY 恒为 index 3，permG 恒为 index 4，无互换问题。

---

## 4. 结果目录结构

| 目录 | 状态 | all_metrics.json | 代数 |
|------|------|-----------------|------|
| `a000_s42` | ✅ 完成 | 存在 | gen_0 ~ gen_10 (11 dirs) |
| `a025_s42` | ✅ 完成 | 存在 | 13 subdirs |
| `a050_s42` | ✅ 完成 | 存在 | 13 subdirs |
| `a075_s42` | ⚠️ 运行中 | **不存在** | gen_0 ~ gen_7 (gen_7 刚创建) |
| MVP `rep_42` | ✅ 完成 | 存在 | — |

### a075 进度估计

- config: `num_generations: 10` → 需 gen_0 到 gen_10 (11 dirs)
- 当前: gen_0-gen_7，gen_7 于 18:56 创建
- 每代耗时: ~65-70 min (gen_3 起)
- 预计还需: gen_8, gen_9, gen_10 + all_metrics 生成 ≈ 3.5-4 小时
- **预计完成时间**: ~22:30-23:00 (May 15)

---

## 5. 风险点

### ⚠️ R1: a075 实验未完成
`all_metrics.json` 不存在时 `load_metrics()` 会 `FileNotFoundError`。**必须等实验完全结束后再跑 5-point 分析。**

### ⚠️ R2: 代数不一致可能性
a000 有 11 代 (gen_0-10)，a075 config 设 `num_generations: 10`。如果其他 alpha 点代数不同，dose-response 和 Granger 的时间序列长度不同，可能影响统计功效。建议跑前确认所有 alpha 点的 all_metrics.json 长度一致。

### ✅ R3: 单 seed consensus 语义
α≠1.0 的 alpha 点只有 1 个 seed (s42)，`seed_threshold=1`（≥1/1 seed），consensus 仅依赖方法间一致性（≥4/5 methods）。这与 d027 的 4-seed consensus 定义不同，但对单 seed 数据合理。脚本已正确处理 (`st = 1 if n_seeds == 1 else 3`)。

---

## 6. 运行命令

实验完成后执行：

```bash
cd /root/autodl-tmp/distrib_canary_collapse
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python cross_alpha_analysis_v4.py --n-perms 5000 --consensus-n-perms 1000 --update-registry
```

无需传 alpha_dirs，自动发现 5 个 α 点。

输出：
- `results/analysis/cross_alpha_v{N}.json`
- `results/analysis/cross_alpha_v{N}_report.md`

---

## 总结

| 检查项 | 状态 |
|--------|------|
| 脚本存在性 | ✅ |
| 5 α 点支持 | ✅ 自动发现，无需修改 |
| FDR 混合策略 (D029/D030) | ✅ 两条路径均正确 |
| permG/TY 列顺序 | ✅ 三文件一致 |
| 4 已完成 α 点数据 | ✅ |
| a075 就绪 | ❌ 实验运行中，预计 ~22:30 完成 |

**结论：脚本无需修改，等 a075 实验完成后直接运行。**
