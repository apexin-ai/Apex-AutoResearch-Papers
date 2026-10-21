# analysis r16 paired ttest

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r16-paired-ttest_20260523T170538_result.json`
- **Structured JSON:** [`3331d83b200b86740207.json`](../../sessions/33/3331d83b200b86740207.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Per-split 数据可用，paired t-test 完成。结果保存至 `/root/entrainment_gated_ft/results/e1_paired_ttest.json`。

## Paired t-test 结果（rescue_threshold routing vs majority vote, 10 splits）

| Benchmark | mean diff (pp) | t | p | 95% CI (pp) | sig |
|-----------|------:|------:|------:|------|:---:|
| **LAMBADA** | **+5.153** | 36.497 | <0.000001 | [+4.834, +5.473] | *** |
| HellaSwag | -0.064 | -0.935 | 0.374 | [-0.218, +0.090] | |
| PIQA | **-0.490** | -3.551 | 0.006 | [-0.802, -0.178] | ** |
| **ARC-Easy** | **+1.153** | 7.027 | 0.000061 | [+0.782, +1.524] | *** |

要点：
- **LAMBADA**：routing 显著优于 MV（+5.15pp, p<10⁻⁶），CI 极窄
- **ARC-Easy**：routing 显著优于 MV（+1.15pp, p=6×10⁻⁵）
- **HellaSwag**：无显著差异（p=0.37），routing 和 MV 基本持平
- **PIQA**：routing 显著**劣于** MV（-0.49pp, p=0.006），方向相反

和之前 unpaired Welch t-test 方向一致，但 paired 检验 power 更高——PIQA 的负向差异现在达到 p<0.01 显著水平。

---
