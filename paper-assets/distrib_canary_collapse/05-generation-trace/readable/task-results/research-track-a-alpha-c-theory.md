# research track a alpha c theory

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_track-a-alpha-c-theory_20260522T041915_result.json`
- **Structured JSON:** [`9a89a179012ccbe22f49.json`](../../sessions/9a/9a89a179012ccbe22f49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

This work is already complete. Existing artifacts in `artifacts/alpha_c_theory/`:

**Results summary** (`theory_verification.json`):

| Model | R² | Key Parameters |
|---|---|---|
| Theory: α_∞ + A·T^{-1/(2β)} | **0.999997** | α_∞=0.193, γ=2.408, β=0.208 |
| Pure power law: A·T^{-γ} | 0.950 | A=5.81, γ=1.05 |
| Linear signal (γ=0.5 fixed) | 0.711 | A=1.46 |

**Convergence**: Theory γ = 2.408 vs empirical γ = 2.41, delta = 0.0019 — converged.

**Closed-form expression** (from `derivation.md`):

$$\alpha_c(T) = \alpha_\infty + A \cdot T^{-1/(2\beta)}$$

where:
- α_∞ = 0.193 — detection floor (contamination below ~19.3% is undetectable regardless of T)
- β = 0.207 — sub-linear signal growth: S(α) ∝ (α − α_∞)^{0.207}
- A = 75.38 — amplitude constant
- γ = 1/(2β) = 2.408

**Predictions**:

| T | α_c (theory) |
|---|---|
| 5 | 1.0 (capped) |
| 10 | 0.487 |
| 15 | 0.304 |
| 20 | 0.248 |
| 25 | 0.225 |
| 50 | 0.199 |

All deliverables already exist: `derivation.md`, `verify_theory.py`, `theory_verification.json`, `fig_theory_comparison.pdf`, `proposition2.tex`.

---
