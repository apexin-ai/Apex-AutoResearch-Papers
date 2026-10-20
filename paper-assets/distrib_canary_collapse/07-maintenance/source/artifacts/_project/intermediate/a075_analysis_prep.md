# 4-α Cross-Alpha Analysis Prep (a075 completion)

## 已验证目录

| α | 目录 | gen_0–gen_10 | all_metrics.json |
|---|------|-------------|------------------|
| 0.00 | `results/alpha_sweep/a000_s42/` | 完整 (gen_0–gen_10) | 有 |
| 0.25 | `results/alpha_sweep/a025_s42/` | 完整 (gen_0–gen_10) | 有 |
| 0.50 | `results/alpha_sweep/a050_s42/` | 完整 (gen_0–gen_10) | 有 |
| 0.75 | `results/alpha_sweep/a075_s42/` | **进行中** gen_0–gen_3 完成, gen_4 进行中 | 未生成 |

服务器路径前缀: `/root/autodl-tmp/distrib_canary_collapse/`

## a075 当前进度

- 完成: gen_0, gen_1, gen_2, gen_3 (4/11 generations)
- 进行中: gen_4 (目录已创建, 内容为空)
- 剩余: gen_4–gen_10 (7 generations)
- 进度: ~36%
- 截至: 2026-05-15 15:30 (gen_4 目录创建时间)

## 分析命令 (a075 完成后执行)

```bash
cd /root/autodl-tmp/distrib_canary_collapse && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
python cross_alpha_analysis.py \
  --alpha-dirs a000_s42 a025_s42 a050_s42 a075_s42 \
  --n-perms 5000 \
  --update-registry
```

不指定 `--version` 时脚本自动递增版本号。

## 预期产出

- JSON: `results/analysis/cross_alpha_v{N}.json`
  - 包含: dose_response, granger_causality, cross_correlation, per_gen_velocity
  - 统计配置: max_lag=1, n_perms=5000, BH FDR correction
- 终端: summary table + registry update commands (因 --update-registry)

## 已有分析文件 (3-α 版本)

- `results/analysis/cross_alpha_analysis.json`
- `results/analysis/cross_alpha_analysis.md`
- `results/analysis/cross_alpha_v3_full.json`
- `results/alpha_sweep/pooled_panel_results.json`
