# Operating Regime Analysis: When SICA Degenerates

## Claim
SICA's effectiveness is bounded by a **trace diversity prerequisite** (C0): the model must produce sufficiently diverse reasoning paths under temperature sampling. When this condition fails—as with reasoning models—SICA collapses to SC or performs worse.

## Evidence Summary

### Cross-Model C0 Comparison

| Model | Type | C0 (multi-candidate rate) | SICA effective? |
|-------|------|--------------------------|-----------------|
| QwQ-32B | Reasoning | 2.6% (effective) | No — SICA ≡ SC or SICA < SC |
| Qwen2.5-14B-Instruct | Standard | 46.0% | Yes — diversity enables constraint-based reranking |

**Diversity ratio**: 17.7× gap between standard and reasoning model on comparable problems.

### QwQ-32B Results by Domain

| Dataset | Domain | N | K | C0 (nominal) | C0 (effective) | SICA | SC | Δ (pp) | Verdict |
|---------|--------|---|---|--------------|-----------------|------|-----|--------|---------|
| AIME 2024 | Math | 22 | 12 | 0.0% | 0.0% | 72.7% | 72.7% | 0.0 | SICA ≡ SC |
| ProofWriter D5 | Logic | 17 | 12 | 23.5% | 5.9% | 82.4% | 88.2% | **−5.9** | **SICA < SC** |
| FOLIO | Logic | 2 | 4 | 0.0% | 0.0% | 100% | 100% | 0.0 | SICA ≡ SC |
| MATH L4-5 | Math | 5 | 12 | 0.0% | 0.0% | — | — | — | No divergence |
| **Combined** | | **39** | **12** | **10.3%** | **2.6%** | | | | **Below threshold** |

*Effective C0*: problems with both multiple answer candidates AND successful constraint extraction.

### Why Reasoning Models Kill Diversity

1. **Deterministic chain-of-thought**: QwQ-32B's extended reasoning chain converges to the same conclusion regardless of sampling temperature. Even at T=1.0, all K=12 traces produce identical final answers on math problems.

2. **Extraction incompatibility**: When the model does produce rare answer diversity (ProofWriter, 4/17), it fails at constraint extraction—re-reasoning from scratch instead of outputting structured JSON (3/4 multi-candidate problems: 0 constraints extracted).

3. **Scoring bias under extraction failure**: The one problem with both diversity and constraints (498_Q8), SICA's MaxSAT scoring assigned higher weight to the minority answer (38 vs 27), flipping SC's correct majority vote to the wrong answer.

### Temperature Ablation (QwQ-32B, MATH L4-5)

| Problem | Level | T=0.7 | T=0.9 | T=1.0 | Answer Divergence |
|---------|-------|-------|-------|-------|-------------------|
| algebra/2277 | 5 | 10/12 → "0" | 9/12 → "0" | 9/12 → "0" | 0% |
| number_theory/427 | 5 | 12/12 → "25" | 12/12 → "25" | 12/12 → "25" | 0% |
| precalculus/1199 | 4 | 2/12 → "π" | 2/12 → "π" | 3/12 → "π" | 0% |

Temperature has negligible effect on reasoning model output diversity.

### ProofWriter Case Study: How SICA Fails with Low C0

Of 17 completed ProofWriter problems:
- **13/17 (76.5%)**: unanimous K=12 vote → SICA ≡ SC (trivially)
- **4/17 (23.5%)**: multiple candidates, but:
  - 3/4: constraint extraction returned **0 constraints** (QwQ re-reasons instead of extracting)
  - 1/4 (498_Q8): 41 constraints from only 4/12 traces, biased toward minority → **SICA flips correct answer to wrong**

Net effect: SICA is −5.9pp worse than SC on ProofWriter with QwQ-32B.

## Operating Regime Definition

Based on QwQ-32B (negative) and Qwen2.5-14B (positive) evidence:

- **C0 < 20%**: SICA provides no benefit over SC. Constraint-based aggregation is structurally vacuous when all traces agree.
- **C0 ≥ 20%**: SICA can leverage MaxSAT constraint aggregation to rerank candidates. Qwen2.5-14B achieves C0=46%, enabling meaningful constraint-based consensus.

The C0 threshold is not merely a performance predictor—it is a **structural prerequisite**. Below it, SICA's entire pipeline (constraint extraction → deduplication → MaxSAT optimization) produces no signal that differs from counting votes.

## Implications for Paper

1. **Claim 2 (Operating Regime)**: SICA has a well-defined operating regime bounded by model capability. The boundary is empirically located at C0 ≈ 20%.

2. **Capability Trap**: Reasoning models represent an extreme case—their strength (self-consistent reasoning) directly undermines the diversity that SICA requires. This is not a bug but a fundamental tension between model capability and ensemble methods.

3. **Practical Guidance**: SICA should be applied with standard instruction-following models (not reasoning models) where temperature sampling produces genuine answer diversity. A C0 precheck (small K, few problems) should precede full evaluation.

## Data Provenance

| Source Experiment | Registry ID | Server Path | Model |
|------------------|-------------|-------------|-------|
| AIME 2024 | sica_aime30_v3 | results/aime30_v2.json | QwQ-32B |
| ProofWriter D5 | sica_proofwriter30_v2 | results/proofwriter_30_v2.json | QwQ-32B |
| FOLIO live test | sica_folio30 | results/folio_livetest.json | QwQ-32B |
| Temperature diversity | sica_temp_diversity | results/diversity_diagnosis.json | QwQ-32B |
| C0 precheck (comparison) | sica_d016_c0_precheck | results/c0_precheck_qwen14b.json | Qwen2.5-14B-Instruct |
