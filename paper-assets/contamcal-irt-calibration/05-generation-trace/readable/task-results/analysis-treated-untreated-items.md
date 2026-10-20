# analysis treated untreated items

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_treated-untreated-items_20260519T191422_result.json`
- **Structured JSON:** [`a89cd16eaae9bdd2ec64.json`](../../sessions/a8/a89cd16eaae9bdd2ec64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 关键发现

### MMLU (d025, 3540 treated / 10502 untreated)

| Model | Treated Δ | Untreated Δ | DiD | Verdict |
|-------|-----------|-------------|-----|---------|
| Gemma-2-9B | **+0.031**\*\* | **+0.026**\*\*\* | +0.006 (ns) | generalization |
| OLMo-2-7B | +0.016 (ns) | **+0.027**\*\*\* | -0.011 (ns) | mixed |
| Phi-4 | +0.003 (ns) | +0.006 (ns) | -0.003 (ns) | no-effect |
| Qwen2.5-14B | **-0.069**\*\*\* | **-0.076**\*\*\* | +0.007 (ns) | anti-contamination |
| Qwen2.5-7B | **-0.038**\*\* | **-0.029**\*\*\* | -0.008 (ns) | anti-contamination |

### ARC Challenge (d025)
所有 5 个模型的 treated 和 untreated delta 均不显著，verdict 全部为 no-effect（Qwen2.5-7B 的 untreated 有轻微 forgetting）。

### 核心结论：**所有 DiD 均不显著**

**最惊人的发现：2.5% SFT 注入不产生 item-level memorization。** treated items 和 untreated items 的 accuracy 变化幅度几乎一致：
- 当模型整体提升（Gemma-2, OLMo-2），treated 和 untreated 同步提升
- 当模型整体下降（Qwen 系列），treated 和 untreated 同步下降
- **效果是全局性的（SFT general effect），不是 item-specific memorization**

### Difficulty Interaction (d025 MMLU, 5-model mean)
| Bin | Treated Δ | Untreated Δ | Gap |
|-----|-----------|-------------|-----|
| Hard (<0.4) | +0.061 | +0.064 | -0.003 |
| Medium | -0.006 | -0.002 | -0.004 |
| Easy (>0.7) | -0.040 | -0.039 | -0.000 |

difficulty 各 bin 的 gap 也近乎零。regression-to-mean 效应（hard↑ easy↓）对 treated/untreated 完全对称。

### 产出文件
`/root/contamcal-irt-calibration/artifacts/treated_untreated/`:
- `treated_untreated_summary.csv` — 40 rows，全模型 × 全 dosage
- `treated_untreated_mmlu.pdf` / `_arc_challenge.pdf` — 5-panel bar plots
- `difficulty_interaction.csv` + `_mmlu.pdf` / `_arc_challenge.pdf` 
- `did_dose_response.pdf` — DiD 随 dosage 变化的趋势线

---
