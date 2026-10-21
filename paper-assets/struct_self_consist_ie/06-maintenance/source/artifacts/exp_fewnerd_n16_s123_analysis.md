# exp_fewnerd_n16_s123 结果分析

## 实验信息
- server: autodl-5090-c
- seed: 123
- n_samples: 16
- temperature: 1.0
- model: checkpoints/qwen3-8b-fewnerd-exp021-merged
- 运行时间: ~18 分钟 (vLLM inference)
- 退出码: 0 (正常完成)

## 指标

| 指标 | seed=123 (本次) | 上次运行 | Delta |
|------|----------------|---------|-------|
| greedy_f1 | 0.7890 | 0.7888 | +0.0002 |
| oracle_f1 | 0.9145 | 0.9147 | -0.0002 |
| oracle_headroom | 0.1255 | 0.126 | -0.0005 |
| rho_fk_full | 0.2228 | 0.224 | -0.0012 |
| rho_sj_full | 0.3521 | 0.352 | +0.0001 |
| rho_fk_cond | 0.0816 | 0.083 | -0.0014 |
| rho_sj_cond | 0.2809 | 0.282 | -0.0011 |
| logprob_rho_full | 0.2811 | 0.28 | +0.0011 |
| logprob_rho_cond | 0.2584 | 0.258 | +0.0004 |
| instances | 37648 | 37648 | 0 |

### 额外指标
- fleiss_kappa_mean: 0.4487
- soft_jaccard_mean: 0.6946
- sample_f1_mean: 0.6495
- sample_f1_std: 0.3737
- sample_f1_pct_zero: 18.7%
- gold_empty_filtered: 5083
- all_samples_f1_zero_filtered: 3862
- structural_beats_surface: YES (delta=+0.1293)
- logprob_auroc_full: 0.6460
- logprob_auroc_cond: 0.6343
- verdict: MARGINAL

## 与上次运行对比

所有核心指标在两次运行间差异 < 0.002，跨 seed 一致性极高。greedy_f1、oracle_f1、各相关系数、logprob 指标均几乎完全复现。instances 数量完全一致（37648）。这表明结果对 sampling seed 不敏感，具有良好的可复现性。

## 产出文件

| 文件 | 大小 | 说明 |
|------|------|------|
| output/fewnerd_n16_s123/report.json | 1.6KB | 完整指标 JSON |
| output/fewnerd_n16_s123/samples.jsonl | 1.2GB | 全部采样结果（可用于 MV 重算） |

samples.jsonl 存在，可用于后续 MV 统一重算。

## 结论

**SUCCESS** — 实验正常完成，所有指标与上次运行高度一致（delta < 0.002），跨 seed 可复现性确认。Structural > Surface 优势稳定（SJ-FK delta ≈ +0.13）。
