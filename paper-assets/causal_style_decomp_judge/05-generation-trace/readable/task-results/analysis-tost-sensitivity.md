# analysis tost sensitivity

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tost-sensitivity_20260522T183459_result.json`
- **Structured JSON:** [`5eecd87d9df3e3a525c1.json`](../../sessions/5e/5eecd87d9df3e3a525c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果**:

| Δ (pp) | Bounds | TOST p | Sig? | Decision |
|-------:|:------:|-------:|:----:|:---------|
| 5 | [0.45, 0.55] | 0.6255 | NO | Inconclusive |
| 10 | [0.40, 0.60] | 0.1555 | NO | Inconclusive |
| **15** | **[0.35, 0.65]** | **0.0095** | **YES** | **Equivalence** |
| 20 | [0.30, 0.70] | 0.0001 | YES | Equivalence |

- BT point estimate: 0.562, 90% CI: [0.500, 0.624], n=88
- 等价性仅在 Δ≥15pp 时成立。Δ=10pp 时 p=0.155，远未显著
- Reviewer 的担忧有道理：Δ=15pp 是 Claude formality 能通过 TOST 的临界门槛，且 GPT-4o 的 13pp bias 几乎触及该 margin

**文件**: `/root/causal_style_decomp_judge/artifacts/r12_fixes/tost_sensitivity.json`

---
