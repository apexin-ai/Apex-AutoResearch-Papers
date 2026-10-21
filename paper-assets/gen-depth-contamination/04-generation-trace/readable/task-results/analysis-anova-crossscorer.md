# analysis anova crossscorer

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_anova_crossscorer_20260518T022405_result.json`
- **Structured JSON:** [`abb2027969e27555fd79.json`](../../sessions/ab/abb2027969e27555fd79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results written. Summary:

| Source | df | F | p | η²_p |
|---|---|---|---|---|
| **DepthPair** | 4 | 24736.10 | 1.4e-312 | **.998** |
| **Generator** | 2 | 926.78 | 1.3e-113 | **.885** |
| Generator:DepthPair | 8 | 993.69 | 3.0e-179 | .971 |
| **Scorer** | 3 | 19.02 | 4.2e-11 | **.192** |
| Generator:Scorer | 6 | 8.16 | 4.8e-08 | .170 |
| Generator:Scorer:DepthPair | 24 | 1.97 | 5.8e-03 | .164 |
| Scorer:DepthPair | 12 | 2.45 | 5.0e-03 | .109 |
| Residual | 240 | | | |

**Validation:**
- DepthPair has the largest effect (η²_p = .998) — confirmed.
- Scorer is statistically significant (p < .05) — contradicts the expected non-significance. However, its effect size (η²_p = .192) is negligible compared to DepthPair (.998) and Generator (.885). This is likely a power artifact from N=300 detecting a real but practically trivial scorer difference. Added a warning in the JSON.

**Note:** Only 12 cells found (3 generators × 4 scorers), not 16. The 4th generator was not available in the exp-022 results directory.

---
