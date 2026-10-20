# ops vanilla 2pl kendall tau

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_vanilla_2pl_kendall_tau_20260517T090458_result.json`
- **Structured JSON:** [`aec73264b0ba4453e304.json`](../../sessions/ae/aec73264b0ba4453e304.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here are the complete results:

## N=16 (1.5B + 3B, 300-item subsample) — Consistent comparison

| Benchmark | Vanilla 2PL τ | ContamCal τ | Raw Acc τ | Δ(CC−V2PL) |
|-----------|--------------|-------------|-----------|------------|
| **MMLU** | 0.7303 | 0.7303 | 0.7559 | +0.0000 |
| **ARC-C** | 0.7303 | 0.7334 | 0.7428 | +0.0031 |
| **GSM8K** | 0.1911 | 0.1911 | 0.1788 | +0.0000 |

Key findings:

1. **Your τ=0.756 matches Raw Acc MMLU** (0.7559), not ContamCal. The N=16 ContamCal MMLU τ = 0.7303.

2. **MMLU: V2PL = ContamCal** (both 0.7303). γ is not significant for MMLU, so the contamination parameter doesn't change rankings.

3. **ARC-C: V2PL ≈ ContamCal** (0.7303 vs 0.7334, Δ=+0.003). Tiny improvement from γ.

4. **GSM8K is broken** — 3B GSM8K scores are anomalous (d000 accuracy ~0.12-0.16 but d100 at ~0.72), making τ meaningless.

5. **Raw accuracy τ ≥ IRT τ** for MMLU and ARC. The IRT smoothing doesn't improve ranking accuracy with this model set.

6. **J=13 doesn't match any existing result set.** The n16_fixed uses N=16 (1.5B+3B, 2 seeds × 4 dosages). No result set with exactly 13 models exists. Could J=13 come from a specific paper table definition that excludes some models?

---
