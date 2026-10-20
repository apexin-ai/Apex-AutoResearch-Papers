# analysis final ar results

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_final_ar_results_20260523T034411_result.json`
- **Structured JSON:** [`bb67502163edf7784b33.json`](../../sessions/bb/bb67502163edf7784b33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果如下：

---

## 1. 汇总统计 (`d048_summary_ci_wilcoxon.json`)

### β=0.0 (纯 AR, 无 teacher forcing)

| 条件 | GAR mean | std | 95% CI | n |
|------|---------|-----|--------|---|
| **Base** | 0.01859 | 0.01683 | [0.01375, 0.02421] | 39 |
| **TG** | 0.06414 | 0.08200 | [0.04118, 0.09118] | 39 |
| **UG** | 0.03329 | 0.03005 | [0.02476, 0.04336] | 39 |
| **LO** | 0.03728 | 0.03785 | [0.02688, 0.05004] | 39 |
| **PCGrad** | 0.03006 | 0.02358 | [0.02324, 0.03757] | 39 |
| **SS** | 0.34714 | 0.06340 | [0.32657, 0.36556] | 39 |

Wilcoxon:
- **TG vs Base**: W=31, p<0.001, r=0.802
- **TG vs LO**: W=187, p=0.0039, r=0.454
- **SS vs TG**: W=1, p<0.001, r=0.869
- **PCGrad vs TG**: W=176, p=0.0022, r=0.478 (PCGrad < TG)

### β=3.0

| 条件 | GAR mean | std | 95% CI | n |
|------|---------|-----|--------|---|
| **Base** | 0.53147 | 0.05817 | [0.51354, 0.55019] | 39 |
| **TG** | 0.55585 | 0.06087 | [0.53756, 0.57451] | 39 |
| **UG** | 0.56510 | 0.07009 | [0.54343, 0.58722] | 39 |
| **LO** | 0.56001 | 0.06528 | [0.54087, 0.58076] | 39 |
| **PCGrad** | 0.55918 | 0.05286 | [0.54274, 0.57578] | 39 |
| **SS** | 0.59332 | 0.06205 | [0.57444, 0.61321] | 39 |

Wilcoxon:
- **TG vs Base**: W=242, p=0.039, r=0.331
- **TG vs LO**: W=376, p=0.852, r=0.031 (n.s.)
- **SS vs TG**: W=207, p=0.0098, r=0.409
- **PCGrad vs TG**: W=368, p=0.767, r=0.049 (n.s.)

### β=5.0

| 条件 | GAR mean | std | 95% CI | n |
|------|---------|-----|--------|---|
| **Base** | 0.70423 | 0.08128 | [0.67852, 0.73041] | 38 |
| **TG** | 0.72710 | 0.06132 | [0.70836, 0.74654] | 38 |
| **UG** | 0.70829 | 0.05915 | [0.69010, 0.72606] | 39 |
| **LO** | 0.70817 | 0.06642 | [0.68715, 0.72921] | 38 |
| **PCGrad** | 0.70829 | 0.05961 | [0.68996, 0.72706] | 39 |
| **SS** | 0.71697 | 0.06648 | [0.69591, 0.73779] | 39 |

Wilcoxon: 所有对比均 n.s.（p>0.08）

## 2. 各条件 AR N=50 关键指标

| 条件 | checkpoint | gate_type | β=0 GAR | β=0 PPL | β=3 GAR | β=5 GAR |
|------|-----------|-----------|---------|---------|---------|---------|
| Base | (none) | none | 0.01859 | 1.4468 | 0.53147 | 0.70423 |
| TG | phase2_tg_s42_v7 | threadgate | 0.06414 | 1.4324 | 0.55585 | 0.72710 |
| UG | phase2_ug_s42 | uniform | 0.03329 | 1.4338 | 0.56510 | 0.70829 |
| LO | phase2_lora_only_s42 | none | 0.03728 | 1.4310 | 0.56001 | 0.70817 |
| PCGrad | tg_v9_pcgrad_s42 | threadgate | 0.03006 | 1.4486 | 0.55918 | 0.70829 |
| SS | d048_ss_s42 | threadgate | 0.34714 | 1.4423 | 0.59332 | 0.71697 |

## 3. TF eval 结果

**无 tf 相关文件。**

## 4. SS s456 训练进度

**找不到 s456 训练日志**——服务器上没有任何 `*s456*` 文件。

## 5. remaining_queue 进度

**找不到 remaining_queue 日志**——服务器上没有该文件。

---

**关键发现**：
- β=0（纯 AR）下 TG 显著优于 Base（r=0.802）和 LO（r=0.454），但 SS 远超所有方法（GAR=0.347 vs TG 的 0.064）
- β=3 下差距缩小，TG 仅显著优于 Base（p=0.039），与 LO/PCGrad 无显著差异
- β=5 下所有方法差异均不显著
- PPL 各条件非常接近（1.431–1.449），说明生成质量无退化

---
