# experiment qwq hs vs text bootstrap

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_qwq_hs_vs_text_bootstrap_20260517T030045_result.json`
- **Structured JSON:** [`20269ad82dd6fad6e271.json`](../../sessions/20/20269ad82dd6fad6e271.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All results collected. Here's the complete summary:

---

## QwQ-32B HS vs Text Paired Bootstrap (n=1000)

Settings: layer=2, W=5, text encoder=all-MiniLM-L6-v2, 19 test traces

| Metric | HS | Text | Δ | 95% CI | p-value | Bonferroni α=0.017 |
|--------|-----|------|---|--------|---------|-------------------|
| **Balanced Accuracy** | 67.9% | 67.1% | +0.9pp | [-6.2, +7.3] | 0.828 | FAIL |
| **Precision** | 58.3% | 52.5% | +5.7pp | [-5.8, +16.8] | 0.346 | FAIL |
| **Pre-CP FPR** | 20.8% | 17.8% | +3.0pp (HS *worse*) | [-4.5, +10.5] | 0.785 | FAIL |

**Conclusion**: On QwQ-32B, HS probes show no statistically significant advantage over text probes on any metric. The differences are small and confidence intervals all cross zero. This contrasts sharply with r1-8b where HS dominates (precision +22.4pp p<0.001, accuracy +8.2pp p=0.005).

For pre-CP FPR, HS actually has *higher* FPR than text (20.8% vs 17.8%), meaning text is slightly better at avoiding false alarms before commitment, though this difference is also not significant (p=0.785).

---
