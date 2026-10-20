# n=500 Analysis Pipeline Readiness Report

**Date**: 2026-05-15 06:25 CST
**Server**: westd-22162

---

## 1. Experiment Progress

### DeepSeek (c2_n500_deepseek) — tmux sessions

| GPU | Session | Masking | s015 | s020 | s025 | s030 |
|-----|---------|---------|------|------|------|------|
| cuda:0 | c2_n500_gpu0 | importance | **DONE** (500/500) | **436/500** ~34min left | queued | queued |
| cuda:1 | c2_n500_gpu1 | random | **DONE** (500/500) | **486/500** ~7min left | queued | queued |

### Qwen (c2_qw_n500_r3) — screen sessions

| GPU | Session | Masking | s015 | s020 | s025 | s030 |
|-----|---------|---------|------|------|------|------|
| cuda:2 | c2_qw_gpu2 | importance | **DONE** (500/500) | **484/500** ~8min left | queued | queued |
| cuda:3 | c2_qw_gpu3 | random | **DONE** (500/500) | **465/500** ~12min left | queued | queued |

### ETA Summary

- **s020 全部完成**: ~30 min (约 06:55 CST)
- **s025 全部完成**: ~+5h (约 12:00 CST)
- **s030 全部完成**: ~+5h (约 17:00 CST)
- **全部 16 conditions 完成**: 约 2026-05-15 17:00 CST

每个 condition (500 problems) 耗时约 4-5 小时。

---

## 2. Analysis Code Readiness

### Primary Script: `analyze_n500_unified.py` (664 lines)

| 需求 | 状态 | 实现位置 |
|------|------|----------|
| Median II (D054: 禁 mean) | **就绪** | `analyze_condition()` L194: `np.median(diffs)` |
| Bootstrap CI (B=10000) | **就绪** | `bootstrap_median_ci()` L83-91, `B_BOOT=10000` |
| d_z within-importance only (D059) | **就绪** | L249: `within_dz_importance` 只对 imp pairs 计算 d_z |
| imp-vs-rand 不报 d_z (D059) | **就绪** | L310: 只输出 Wilcoxon + median_diff |
| Bonferroni 校正 | **就绪** | L349+: 全局 p-value 校正 |
| Permutation monotonicity test | **就绪** | `permutation_monotonicity_test()` L145, N_PERM=5000 |
| LaTeX 输出 | **就绪** | `latex_output()` L414+, `--latex` flag |
| CSV 输出 | **就绪** | `--csv` flag |
| Dry-run (n=50 data) | **就绪** | `--dry-run` flag |

**结论: 脚本完全合规，无需修改。**

### Secondary Script: `analyze_c2_n500.py` (512 lines)

- 同时报告 mean_diff 和 median_diff（违反 D054）
- d_z 对 imp 和 rand 都计算（不符合 D059）
- **不建议使用此脚本进行最终分析**，仅供参考

### d_z 计算说明

`paired_cohens_dz()` 内部用 `mean(D)/SD(D)` 是 Cohen's d_z 的标准公式，不算报告 mean 作为 central tendency。D054 合规。

---

## 3. 结果文件路径和格式

### 输入文件 (profiling output)

```
/root/autodl-tmp/pacs/profiling_output_n500_bf16_{model}_{masking}_{sparsity}/profiling_results.json
```

模式: `{model}` ∈ {ds, qw}, `{masking}` ∈ {imp, rand}, `{sparsity}` ∈ {s015, s020, s025, s030}

| Condition | File Size | Status |
|-----------|-----------|--------|
| ds_imp_s015 | 22 MB | exists |
| ds_rand_s015 | 22 MB | exists |
| ds_imp_s020 | — | dir created, file pending |
| ds_rand_s020 | — | dir created, file pending |
| qw_imp_s015 | 18 MB | exists |
| qw_rand_s015 | 18 MB | exists |
| qw_imp_s020 | — | dir created, file pending |
| qw_rand_s020 | — | dir created, file pending |
| *_s025 | — | dirs not yet created |
| *_s030 | — | dirs not yet created |

### JSON 结构

```json
{
  "config": {...},
  "phase_stats": {...},
  "perplexity": {...},
  "interaction_index": {...},
  "pass_fail": {...},
  "warnings": {...},
  "diagnostics": {...},
  "per_problem_ii": {
    "0.15": [
      {
        "problem_idx": 0,
        "problem_id": "test/precalculus/807.json",
        "ii_high": -0.0197,
        "n_segments_high": 5,
        "ii_mid": null,
        "n_segments_mid": 0,
        "ii_low": 0.0544,
        "n_segments_low": 2
      },
      ...  // 500 entries
    ]
  }
}
```

### 输出文件

```
/root/autodl-tmp/pacs/analysis_output/n500_unified.json      # 完整结果
/root/autodl-tmp/pacs/analysis_output/n500_unified.csv        # (--csv)
stdout                                                         # LaTeX (--latex)
```

---

## 4. 分析 Pipeline 运行

### 命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/pacs
python analyze_n500_unified.py --csv --latex
```

Dry-run (用现有 n=50 数据验证):
```bash
python analyze_n500_unified.py --dry-run --csv
```

### 预估运行时间

- 数据加载 (16 × ~20MB JSON): ~30s
- Bootstrap CI (B=10000 × 16 conditions): ~2-3 min
- Within-importance d_z + bootstrap: ~1 min
- Permutation test (5000 perms): ~30s
- **总计: ~5 min**

### 部分运行

可以在 s020 完成后先跑部分分析（8/16 conditions），验证 pipeline：
```bash
python analyze_n500_unified.py --csv  # 会自动跳过缺失的 s025/s030
```

---

## 5. 风险和待办

1. **s025/s030 输出目录尚未创建** — runner 脚本会自动创建，不需手动
2. **analyze_n500_unified.py 依赖 scipy** — 已预装，无需额外安装
3. **磁盘空间** — 当前 16 × ~20MB = ~320MB 总输出，根分区充裕
4. **建议**: s020 完成后立即跑一次 8-condition 部分分析，提前验证数据完整性
