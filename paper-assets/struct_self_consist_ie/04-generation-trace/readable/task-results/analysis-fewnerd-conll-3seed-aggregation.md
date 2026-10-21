# analysis fewnerd conll 3seed aggregation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fewnerd_conll_3seed_aggregation_20260518T120508_result.json`
- **Structured JSON:** [`42e0c760f32782f11195.json`](../../sessions/42/42e0c760f32782f11195.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 `full_signal_analysis.json` 已生成。现在汇总所有数据。

以下是从实际分析文件中提取的完整 3-seed 汇总：

```
=== Few-NERD 3-seed Summary (Qwen3-8B, N=8) ===
```

| Metric | seed=42 | seed=123 | seed=456 | Mean±Std |
|--------|---------|----------|----------|----------|
| greedy_f1 | 0.7478 | 0.7480 | 0.7486 | 0.7482±0.0003 |
| oracle_f1 | 0.8719 | 0.8772 | 0.8751 | 0.8747±0.0022 |
| headroom_pp | 12.40 | 12.92 | 12.65 | 12.66±0.21 |
| degeneracy_rate (%) | 10.13 | 9.37 | 8.24 | 9.25±0.77 |
| lp_sel_f1 | 0.7614 | 0.7624 | 0.7623 | 0.7620±0.0005 |
| **lp_delta_pp** | **+1.36** | **+1.44** | **+1.37** | **+1.39±0.04** |
| LP auroc | 0.5782 | 0.5767 | 0.5768 | 0.5772±0.0007 |
| LP rho (global) | 0.4215 | 0.4223 | 0.4206 | 0.4215±0.0007 |
| SJ rho | 0.3002 | 0.3203 | 0.3268 | 0.3158±0.0113 |
| FK rho | 0.3132 | 0.3420 | 0.3361 | 0.3304±0.0123 |
| EM rho | 0.2871 | 0.3230 | 0.3078 | 0.3060±0.0147 |
| VC rho | 0.3858 | 0.3633 | 0.3943 | 0.3811±0.0131 |
| SJ auroc | 0.5197 | 0.5254 | 0.5263 | 0.5238±0.0029 |
| FK auroc | 0.5210 | 0.5272 | 0.5295 | 0.5259±0.0036 |
| EM auroc | 0.5137 | 0.5172 | 0.5233 | 0.5181±0.0040 |
| VC auroc | 0.5354 | 0.5359 | 0.5412 | 0.5375±0.0026 |
| within_instance_rho (LP cond.) | 0.4225 | 0.4274 | 0.4329 | 0.4276±0.0043 |

```
=== CoNLL 3-seed Summary (Qwen3-8B, N=8) ===
```

| Metric | seed=42 | seed=123 | seed=456 | Mean±Std |
|--------|---------|----------|----------|----------|
| greedy_f1 | 0.9079 | 0.9077 | 0.9070 | 0.9075±0.0004 |
| oracle_f1 | 0.9483 | 0.9476 | 0.9453 | 0.9471±0.0013 |
| headroom_pp | 4.04 | 3.99 | 3.84 | 3.96±0.09 |
| degeneracy_rate (CF1) | 0.5914 | 0.6303 | 0.6288 | 0.6168±0.0180 |
| lp_sel_f1 | 0.8974 | 0.8999 | 0.8997 | 0.8990±0.0011 |
| **lp_delta_pp** | **-1.05** | **-0.77** | **-0.73** | **-0.85±0.14** |
| SJ delta_pp | -0.89 | -0.56 | -0.45 | -0.63±0.19 |
| FK delta_pp | -0.91 | -0.53 | -0.51 | -0.65±0.18 |
| EM delta_pp | -1.07 | -0.66 | -0.73 | -0.82±0.18 |
| VC delta_pp | -1.29 | -0.37 | -0.68 | -0.78±0.38 |

**关键发现：**
- **Few-NERD LP Δ = +1.39±0.04pp** — 三个 seed 一致正向，非常稳定（std 仅 0.04）
- **CoNLL LP Δ = -0.85±0.14pp** — 三个 seed 一致负向，LP 选择在高退化率数据集上不 work
- Few-NERD 中 LP 是唯一正向 signal；CoNLL 中所有 signal 都负向，但 LP 表现与 SJ/FK 相当
- 实际数据确认：seed=42 LP Δ=+1.36pp（非+1.36，精确为+1.3551），seed=123 LP Δ=+1.44pp，seed=456 LP Δ=+1.37pp，与任务描述中的已知值一致

---
