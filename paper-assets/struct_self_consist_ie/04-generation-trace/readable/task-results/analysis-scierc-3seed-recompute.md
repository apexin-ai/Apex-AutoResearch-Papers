# analysis scierc 3seed recompute

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scierc_3seed_recompute_20260521T172731_result.json`
- **Structured JSON:** [`8b7bcb502591a9a2452d.json`](../../sessions/8b/8b7bcb502591a9a2452d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `/root/autodl-tmp/struct_self_consist_ie/scierc_3seed_recompute_results.txt` 和对应 JSON。

## 3-Seed 汇总 (SciERC MF4v2, N=8, mean ± σ)

| 指标 | mean ± σ |
|------|----------|
| Greedy F1 | 0.6669 ± 0.0009 |
| Oracle F1 | 0.7808 ± 0.0023 |
| MV F1 (strict >N/2) | 0.6596 ± 0.0040 |
| δ (degeneracy) | 12.2% ± 1.0% |
| α_crit = F1_gr/2 | 0.3335 ± 0.0005 |
| Consensus Construct F1 | 0.6701 ± 0.0034 |
| Selection F1 (LP) | 0.6669 ± 0.0035 |
| Selection F1 (SJ) | 0.6621 ± 0.0036 |

**Signal ρ (full-set):**

| Signal | ρ (mean ± σ) |
|--------|-------------|
| VC | +0.3977 ± 0.0112 |
| SJ | +0.3654 ± 0.0097 |
| EM | +0.3119 ± 0.0123 |
| FK | +0.2599 ± 0.0166 |
| LP | +0.2164 ± 0.0047 |

**Signal ρ (conditional, greedy F1>0):**

| Signal | ρ (mean ± σ) |
|--------|-------------|
| EM | +0.3805 ± 0.0211 |
| VC | +0.3261 ± 0.0187 |
| SJ | +0.3242 ± 0.0137 |
| FK | +0.1770 ± 0.0170 |
| LP | +0.1590 ± 0.0058 |

ESJ/MRSC/LSC 是需要模型推理的 mechanistic probe，无法从 samples.jsonl 计算。每个 seed 的详细数值在产出文件中。

---
