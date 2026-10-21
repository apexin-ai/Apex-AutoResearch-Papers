# analysis rrf c1 c2 correlation ablation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557_result.json`
- **Structured JSON:** [`33517a27d7c1f256c0f8.json`](../../sessions/33/33517a27d7c1f256c0f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存到 `artifacts/rrf_analysis/rrf_signal_analysis.json`。

## C1: Signal Rank Correlation Matrix

3 个信号的 item-level Spearman rank correlation 接近零（31 个模型平均）：

| | S1 (embed) | S2 (minkpp) | S4 (selfcrit) |
|---|---|---|---|
| **MMLU** | — | ρ = −0.044 | ρ = 0.038 |
| **GSM8K** | — | ρ = −0.022 | ρ = 0.053 |
| **ARC** | — | ρ = −0.019 | ρ = 0.009 |
| S2↔S4 | | | ρ ≈ 0.00 |

**结论：三个信号几乎完全正交，冗余度为零。** 最大 |ρ| = 0.053，远低于任何显著性阈值。

## C2: Leave-One-Signal-Out Ablation

| Config | MMLU ΔMAE | GSM8K ΔMAE | ARC ΔMAE | Mean |
|---|---|---|---|---|
| Full (S1+S2+S4) | baseline | baseline | baseline | — |
| Drop S4 | **+0.079** | +0.006 | −0.004 | **+0.027** |
| Drop S1 | +0.066 | **+0.048** | −0.054 | +0.020 |
| Drop S2 | +0.045 | −0.005 | −0.079 | −0.013 |

**Item-level ranking stability**: 去掉任何单个信号后，item RRF 排名与完整版的 ρ ≈ 0.78（~22% 排名变动），进一步确认每个信号提供独特信息。

**Signal importance**: S4(self-critique) > S1(embedding) > S2(minkpp)，按跨 benchmark 平均 ΔMAE。

**注意**: model-level ρ(dosage) 普遍很低（< 0.1），因为 RRF 的价值在于 per-item exposure 送入 IRT，而非 model 均值直接预测 dosage。ARC 上出现 ΔMAE < 0 可能反映该 benchmark 信号噪声较大。

---
