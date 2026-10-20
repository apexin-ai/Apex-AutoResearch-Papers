# ops n sensitivity and hellaswag

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_n-sensitivity-and-hellaswag_20260521T100248_result.json`
- **Structured JSON:** [`659d92b60ce6ea03333f.json`](../../sessions/65/659d92b60ce6ea03333f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

gen_0 完成：acc_norm=0.4130, acc=0.3450（215.8s）。eval 正常工作，继续自动跑 gen_1-gen_10，每个约 3.5 分钟，全部约 35 分钟。

现在汇报当前结果。

---

## 产出汇总

### 1. n_sensitivity 结果（pure_collapse seed44 gen_0）

| n | k (SVs) | SLV mean | SLV std | Rel vs n=1000 | CV (%) |
|---:|--------:|---------:|--------:|--------------:|-------:|
| 250 | 250 | 783.38 | 2.82 | -66.83% | 0.360 |
| 500 | 500 | 1440.83 | 2.47 | -39.00% | 0.171 |
| 1000 | 1000 | 2362.07 | 4.24 | +0.00% | 0.179 |
| 2000 | 1024 | 3072.18 | 3.21 | +30.06% | 0.105 |
| 5000 | 1024 | 3655.41 | 0.00 | +54.75% | 0.000 |

- pool_size = 5000, hidden_size = 1024, n_repeats = 10
- n=5000 方差为零（全部样本被使用）
- n≥2000 时 k 被截断为 1024（= hidden_size），SLV 值显著偏高
- **CV 均 < 0.4%**，说明 SLV 在各 n 值下都很稳定
- 结果保存在 `results/n_sensitivity_results.json`

### 2. 已有 HellaSwag 数据

**Phase0（seed=42, checkpoints/gen_*）—— 完整 gen_0 到 gen_10：**

| Gen | acc_norm | acc |
|----:|---------:|----:|
| 0 | 0.4130 | 0.3450 |
| 1 | 0.3897 | 0.3385 |
| 2 | 0.3764 | 0.3315 |
| 3 | 0.3658 | 0.3237 |
| 4 | 0.3558 | 0.3171 |
| 5 | 0.3439 | 0.3099 |
| 6 | 0.3311 | 0.3013 |
| 7 | 0.3187 | 0.2955 |
| 8 | 0.3103 | 0.2906 |
| 9 | 0.3009 | 0.2862 |
| 10 | 0.2951 | 0.2834 |

**Phase1 所有 condition/seed —— 均无 HellaSwag 数据：**
- pure_collapse_seed43: 缺失
- pure_collapse_seed44: 缺失（正在评估中）
- fixed_mix_r03_seed42/43, fixed_mix_r025_seed42/43/44, fixed_mix_r02_seed42, fixed_mix_seed42, adaptive_k10_seed42: 全部缺失

### 3. seed44 HellaSwag eval（进行中）

- gen_0 已完成：**acc_norm=0.4130, acc=0.3450**（与 phase0 gen_0 完全一致，符合预期——都是同一预训练模型）
- gen_1 至 gen_10 正在后台评估（PID 565098），每个 gen 约 3.5 分钟
- 日志：`/tmp/hellaswag_seed44.log`
- 结果输出到：`results/hellaswag_seed44_gen{0-10}/results.json`
- 预计全部完成时间：约 35 分钟后

---
