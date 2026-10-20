# Claim Audit Report: Numerical Consistency Check

**Paper**: Strong Predictors, Weak Selectors  
**Date**: 2026-05-16  
**Scope**: All sections in `docs/paper/sections/` + `paper_provenance.yaml`

---

## Inconsistency List

| # | Location 1 | Value 1 | Location 2 | Value 2 | Severity | Issue | Suggested Fix |
|---|-----------|---------|-----------|---------|----------|-------|---------------|
| 1 | discussion.tex:L43 | LP×VC best: +0.1pp over single-sample | limitations.tex:L10 | LP×VC: +0.4pp over greedy | **HIGH** | Mathematically contradictory. If best=single+0.1pp=0.646, then vs greedy (0.663)=-1.7pp, not +0.4pp. | Limitations should read "+0.4pp over single-sample" OR discussion value needs correction. Verify from exp data which is correct. |
| 2 | experiments.tex Table 1 (L34) | VC SciERC AUROC = .663 | appendix.tex tab:multiseed (L419) | VC NER AUROC mean = .697±.010 | **HIGH** | Mathematically impossible: if seed=42 gives .663, population σ over 3 seeds cannot be .010 with mean .697 (seed=42 deviation alone = .034 > 3×σ). | Either Table 1 AUROC is not from seed=42, or multi-seed AUROC values are from a different eval protocol. Reconcile. |
| 3 | paper_provenance.yaml c002 | EM NER AUROC = 0.749 | experiments.tex Table 1 (L37) | EM SciERC AUROC = .614 | **HIGH** | Provenance claims EM leads AUROC at 0.749; published Table 1 shows EM=.614, VC leads at .663. Provenance narrative contradicts paper. | Update provenance to match final Table 1 values. |
| 4 | paper_provenance.yaml c013 | greedy F1 = 0.644 | experiments.tex Table 2 (L67) | Greedy (T=0) F1 = 0.663 | **HIGH** | 1.9pp discrepancy in greedy baseline between provenance (exp_016_rerun_1024_bootstrap) and paper Table 2 (exp_016_signal_ensemble). | Clarify which experiment sources Table 2. If different experiments, provenance should reference the correct one. |
| 5 | paper_provenance.yaml c013 | oracle = 0.776 | experiments.tex Table 2 (L66) | Oracle = 0.778±0.003 | MEDIUM | Minor discrepancy (0.002). Different source experiments. | Align provenance to published value. |
| 6 | experiments.tex:L9 | SciERC: ≈65% F1 | discussion.tex:L13 | SciERC (66%) | MEDIUM | "≈65%" refers to single-sample (0.645), "66%" refers to greedy (0.663). With the "Single=greedy" issue, these become entangled. | Standardize: if "Single" is the reference, use "65%"; if greedy, use "66%". Pick one. |
| 7 | experiments.tex:L11 | WNUT-17: 52% zero F1 | paper_provenance.yaml c021 | 54% zero F1 (evidence: 53.7%) | MEDIUM | Paper says 52%, provenance says 54%/53.7%. Different filtering or rounding. | Verify exact number from exp_003 data and standardize. |
| 8 | experiments.tex:L89 | LP Δ=+0.2pp (LP 0.647 - Single 0.645) | paper_provenance.yaml c011 | logprob +0.6pp (LP 0.650 - greedy 0.644) | MEDIUM | Different source experiments produce different LP values (0.647 vs 0.650) and different baselines. | Provenance should reference the same experiment as Table 2. |
| 9 | appendix.tex:L81 | SJ N=8→N=16 gain = +0.047 | appendix.tex tab:n-scaling (L861) | SJ N=8→N=16 Δ = +0.0464 | LOW | Appendix text uses different baseline (single-seed 0.360) vs N-scaling table (3-seed mean 0.3641). Reported as +0.047 but actual calculation from text values: 0.411-0.360=0.051. | Use consistent baselines; if comparing 3-seed means, use both from N-scaling table (+0.046). |
| 10 | paper_provenance.yaml c025 | SJ T=0.7 ρ = 0.388 | appendix.tex tab:robustness (L44) | SJ T=0.7 ρ = 0.364 | MEDIUM | Provenance cites exp_005 value (0.388); published table uses different value (0.364). Provenance is stale. | Update provenance to match published appendix table. |
| 11 | paper_provenance.yaml c002 | VC AUROC (corrected) = 0.684 | experiments.tex Table 1 (L34) | VC SciERC AUROC = .663 | **HIGH** | Provenance note says "Corrected to .684 via exp_012_rerun_1024" but Table 1 shows .663. | Provenance values don't match final paper. Update provenance. |
| 12 | introduction.tex:L35 | "13-18 pp oracle headroom" (context: greedy surpasses) | experiments.tex Table 2 | Oracle-Greedy = 0.778-0.663 = 11.5pp | MEDIUM | "13-18pp" is oracle vs single-sample (13.3 NER, 18.1 RE), not oracle vs greedy. The sentence juxtaposes greedy performance with headroom measured from a different baseline. Technically correct but misleading in context. | Consider rephrasing: "despite 13pp oracle headroom above single-sample" to avoid conflation with the greedy baseline in the same sentence. |
| 13 | paper_provenance.yaml c004 | Voting RE ρ=0.350 (corrected) | appendix.tex tab:multiseed (L417) | RE VC mean ρ=0.309±0.024 | LOW | Provenance (single seed=42) vs appendix (3-seed mean). Both can be correct for their context but provenance should note this is single-seed. | Add note to provenance that 0.350 is seed=42 only; 3-seed mean is 0.309. |

---

## Provenance-Paper Alignment Summary

The provenance yaml (version 100, built 2026-05-16) has multiple values that don't match the final published tables. Key mismatches:

| Provenance Claim | Provenance Value | Paper Value | Status |
|-----------------|-----------------|-------------|--------|
| c002: EM NER AUROC | 0.749 | 0.614 | **STALE** |
| c002: VC NER AUROC | 0.684 | 0.663 | **STALE** |
| c013: greedy NER F1 | 0.644 | 0.663 | **STALE** |
| c013: oracle NER F1 | 0.776 | 0.778 | Minor |
| c011: LP F1 | 0.650 | 0.647 | **STALE** |
| c025: SJ T=0.7 ρ | 0.388 | 0.364 | **STALE** |

**Root cause**: Provenance references experiments (exp_012_rerun_1024, exp_016_rerun_1024_bootstrap) that differ from the experiment sourcing Table 2 (exp_016_signal_ensemble). The provenance was not updated after the final table values were finalized.

---

## Cross-Section Consistency for Key Numbers

### Consistent across sections (verified):
- ρ up to 0.38 (abstract/intro/conclusion) ← VC 0.379 rounds to 0.38 ✓
- 0.45 on ceiling control (abstract/intro/conclusion) ← EM CoNLL 0.451 ✓
- 21-58% instance degeneracy (abstract/intro/discussion/conclusion) ← Table 3 ✓
- median ρ=0.52 within-instance (abstract/intro/discussion) ← Table 3: 0.524 ✓
- 0.041 nats LP range (abstract/intro/discussion/conclusion/appendix) ✓
- MBR closes 23-41% (intro/discussion/Table 3) ✓
- Greedy F1=0.663 (intro/experiments/discussion) ✓
- Non-tied LP: +2.9pp, p=0.004 (experiments/discussion/appendix) ✓
- VerbConf mean 8.58/10 SciERC (discussion 8.6, limitations 8.58, appendix 8.58) ✓
- ECE 0.069-0.096 NER (experiments/appendix) ✓
- Entity-token LP 4× variance (discussion/limitations) ✓

### Rounding conventions used:
- 0.379 → "0.38" in prose ✓
- 0.451 → "0.45" in prose ✓
- 8.58 → "8.6" in discussion prose ✓
- 0.524 → "0.52" in abstract/intro ✓

---

## Recommendations (Priority Order)

1. **Fix #1 immediately** (reviewer-flagged): Resolve the "+0.1pp over single" vs "+0.4pp over greedy" contradiction in limitations.tex
2. **Fix #2**: Reconcile Table 1 AUROC values with multi-seed table — either add a note about different eval protocols or correct one table
3. **Rebuild provenance**: Multiple provenance entries reference superseded experiments. Full provenance rebuild needed against final Table 1/2 values.
4. **Standardize SciERC F1 reference**: Pick "≈65%" (single-sample) or "≈66%" (greedy) and use consistently. Given the "Single=greedy" issue, this needs resolution first.
5. **Minor fixes**: WNUT zero-F1 percentage (52% vs 53.7%), N-scaling gain reporting.
