# paper polish fake safety dfcar

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_polish_fake_safety_dfcar_20260526T052405_result.json`
- **Structured JSON:** [`ed31c9e74df2f0f90341.json`](../../sessions/ed/ed31c9e74df2f0f90341.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All files are consistent. Here's a summary of all changes:

### Changes made

**abstract.tex**
- Added obstacle displacement evidence ("obstacle displacement at the nanometer scale") alongside EE displacement
- Added TSR expansion on first use; removed duplicate TSR definition later in the abstract

**introduction.tex**
- Added obstacle displacement confirmation (5 nm median) next to the 99.6% EE displacement statistic
- Distinguished Pi0.5's fake safe mechanism: "not action collapse per se but the low prior probability of collision along short, incomplete trajectories"
- Specified "end-effector displacement" explicitly in dfCAR description
- Added threshold robustness sentence: any τ_d in [2, 200] mm yields identical filtering
- Fixed -ing phrase ending: "rendering cross-method comparisons... misleading" → "Cross-method comparisons on raw CAR are therefore unreliable"

**analysis_claim1.tex**
- Added obstacle displacement as independent evidence (median ~5 nm, "numerical noise rather than physical contact")
- Restructured fake safe definition: EE displacement < τ_d as the formal criterion (aligned with dfCAR), TSR=0% as corroborating evidence
- Positioned dfCAR as community tool: "general-purpose diagnostic for the VLA safety evaluation community"
- Added full threshold robustness paragraph: bimodal distribution, min active EE disp = 239 mm, [2, 200] mm invariance
- Rewrote dfCAR filtering effect: "91.5% CAR but CAR_f is statistically undefined"

**analysis_claim2.tex**
- Replaced "striking" with neutral "an aggregate"
- Added explicit observation caveat: "empirical observation within two model families, not as a universal law. A causal claim would require evidence across a broader range of architectures and benchmarks."
- Fixed -ing participial phrase: "placing this cluster in what we term" → "we term this region"
- Removed "We note that" (AI-style hedging)

**experimental_framework.tex**
- Replaced terse threshold robustness note with substantive description: bimodal distribution, τ_d ∈ [2, 200] mm invariance

---
