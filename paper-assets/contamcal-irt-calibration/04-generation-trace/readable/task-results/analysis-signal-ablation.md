# analysis signal ablation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_signal-ablation_20260522T094116_result.json`
- **Structured JSON:** [`58e28911665e443c203c.json`](../../sessions/58/58e28911665e443c203c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Summary of findings:

**Signal importance ranking** (consistent across benchmarks, signal-average method):
- **S4 (self-critique)** contributes most — dropping it causes largest Δγ (mean -0.0078)
- **S1 (embedding)** second — mean Δγ = -0.0022
- **S2 (Min-K++)** least — mean Δγ = -0.0016

**No signal is pure noise** — worst single-signal ρ(E,τ) = 0.072 (S2 on GSM8K), still well above random baseline ρ ≈ 0.01.

**3-vs-2 marginal benefit is negligible** — dropping S2 leaves ρ virtually unchanged (e.g., MMLU: 0.339 vs 0.337 for full). The third signal adds < 1% ρ improvement.

**Measurement error attenuation is severe** — with ρ(E,τ) ≈ 0.28–0.34 (signal-average), estimated γ is attenuated by 90%+ relative to true γ. This is worse than classical linear attenuation because the IRT model's joint estimation of θ, a, b absorbs noise from exposure. The RRF method (ρ ≈ 0.06–0.09) performs even worse.

This aligns with the real RRF ablation data where S4 > S1 > S2 on MMLU, and confirms the rank-sum invariance problem limits RRF's usefulness as per-item exposure in IRT models.

Artifacts registered: `signal_ablation_results.md` (report) and `signal_ablation_results.json` (data).

---
