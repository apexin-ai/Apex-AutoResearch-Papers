# Analysis Pipeline Readiness Report (2026-05-15 09:00 UTC)

## 分析脚本验证：✅ 通过

`analyze_n500_unified.py` 功能完全正常：
- 正确加载已完成 condition 的 `profiling_results.json`
- 缺失 condition 优雅降级（输出 "missing data"，不崩溃）
- 输出包含所有要求指标：median II diff, bootstrap 95% CI (B=10000), Wilcoxon p, Bonferroni 校正, mid-phase null rate, within-importance d_z, imp-vs-rand, dose-response
- JSON + CSV 双格式输出正常
- 参数接口：`--model {deepseek,qwen,all}` `--csv` `--latex` `--dry-run`

## 已完成 Conditions（8/16）

| Model | Masking | Sparsity | 完成时间 | 文件大小 |
|-------|---------|----------|----------|----------|
| DeepSeek | importance | s015 | May 15 02:31 | 22MB |
| DeepSeek | importance | s020 | May 15 06:55 | 22MB |
| DeepSeek | random | s015 | May 15 02:05 | 22MB |
| DeepSeek | random | s020 | May 15 06:30 | 22MB |
| Qwen | importance | s015 | May 15 03:02 | 18MB |
| Qwen | importance | s020 | May 15 06:27 | 18MB |
| Qwen | random | s015 | May 15 03:11 | 18MB |
| Qwen | random | s020 | May 15 06:36 | 18MB |

## 运行中 Conditions（4/16 — s025，截至 08:55 UTC）

| Condition | 进度 | GPU |
|-----------|-------|-----|
| ds_imp_s025 | 233/500 (46%) | GPU 0 (tmux) |
| ds_rand_s025 | 286/500 (57%) | GPU 1 (tmux) |
| qw_imp_s025 | 365/500 (73%) | GPU 0 (screen) |
| qw_rand_s025 | 337/500 (67%) | GPU 0 (screen) |

## 待运行 Conditions（4/16 — s030）

目录尚未创建。run 脚本顺序执行，s025 完成后自动开始 s030。

## Dry-run 结果摘要

**DeepSeek (s015/s020):**
- imp_s015: median=+0.3907 CI=[0.3496,0.4431] p_bonf=0.0000
- imp_s020: median=+1.2149 CI=[1.1072,1.3365] p_bonf=0.0000
- rand_s015: median=+0.0139 CI=[-0.0167,0.0389] p_bonf=1.0000
- rand_s020: median=+0.0315 CI=[-0.0112,0.0767] p_bonf=1.0000
- within-imp d_z (s015→s020): -0.468 (small)

**Qwen (s015/s020):**
- imp_s015: median=+0.0659 CI=[0.0492,0.0925] p_bonf=0.0000
- imp_s020: median=+0.3073 CI=[0.2612,0.3564] p_bonf=0.0000
- rand_s015: median=-0.0111 CI=[-0.0390,0.0124] p_bonf=1.0000
- rand_s020: median=+0.0153 CI=[-0.0145,0.0684] p_bonf=1.0000
- within-imp d_z (s015→s020): -0.509 (medium)

## 分析命令模板

```bash
cd /root/autodl-tmp/pacs && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# 全量分析（所有模型 + CSV + LaTeX）
python analyze_n500_unified.py --model all --csv --latex

# 单模型分析
python analyze_n500_unified.py --model deepseek --csv
python analyze_n500_unified.py --model qwen --csv
```

输出路径：
- `/root/autodl-tmp/pacs/analysis_output/n500_unified.json`
- `/root/autodl-tmp/pacs/analysis_output/n500_unified.csv`

## 问题与风险

无问题。脚本依赖就绪（numpy, scipy），路径正确，输出格式完整。dose-response 需 ≥3 sparsity level，s025 完成后解锁。
