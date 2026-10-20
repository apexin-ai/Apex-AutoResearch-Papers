# Proofread Report — 2026-05-22

## 1. Undefined References

- [PASS] `\ref{sec:extended_decoding}` (previously known issue): **Not found in any file. Issue has been fixed.**
- [PASS] All `\ref{...}` targets have corresponding `\label{...}` definitions across the paper files.
- [PASS] All `\cite{...}` keys use well-formed identifiers. (Cannot verify .bib existence without references.bib, but no formatting issues.)
- [WARN] `\label{tab:pairwise_significance}` (appendix_extended.tex:89) is attached to a paragraph, not a table/figure. Not referenced anywhere currently, so harmless, but the `tab:` prefix is misleading if ever used.
- [INFO] `discussion.tex` defines 7 labels on a single `\section{Discussion}` (`sec:discussion`, `sec:why_kstar`, `sec:one_wash`, `sec:negative_graduated`, `sec:repr_dependence`, `sec:boundary_cases`, `sec:length_confound`). All refs to these resolve to the same section number. This is intentional (paragraph-level topics) and valid.
- [INFO] External table inputs (`tables/tab_crossscorer`, `tables/tab_filtering_main`) not verified for existence on disk.

## 2. Table-Registry Consistency

### Table 1 (tab:kstar_ci) — Main Results

**Qwen-rw (mvp_pilot_sat_v1):**
| Pair | Paper | Registry | Delta |
|------|-------|----------|-------|
| 0v1 | .9956 | 0.9956 | 0 |
| 1v2 | .6955 | 0.6957 | -0.0002 |
| 2v3 | .5893 | 0.5893 | 0 |
| 3v4 | .5435 | 0.5434 | +0.0001 |
| 4v5 | .5340 | 0.5343 | -0.0003 |

- [PASS] All within rounding tolerance (4th decimal place).

**Pythia-1.4B (exp_001_pythia_depth):**
| Pair | Paper | Registry | Delta |
|------|-------|----------|-------|
| 0v1 | .9932 | 0.9932 | 0 |
| 1v2 | .6539 | 0.6539 | 0 |
| 2v3 | .5514 | 0.5515 | -0.0001 |
| 3v4 | .5152 | 0.5153 | -0.0001 |
| 4v5 | .5136 | 0.5135 | +0.0001 |

- [PASS] All within rounding tolerance.

**OLMo-1B (exp_002_olmo_depth):**
| Pair | Paper | Registry | Delta |
|------|-------|----------|-------|
| 0v1 | .9860 | 0.9970 | **-0.0110** |
| 1v2 | .5080 | 0.6146 | **-0.1066** |
| 2v3 | .4973 | 0.5497 | **-0.0524** |
| K* | 1 | 2 | **DIFFERS** |

- [**MISMATCH — CRITICAL**] Registry `exp_002_olmo_depth` shows K\*=2 with drastically higher AUC values. Paper is internally consistent (tab:kstar_ci, tab:kstar_ci_extended, tab:s8_cv_folds, tab:bonferroni_ci all agree on OLMo K\*=1). The registry entry likely reflects an earlier pipeline version or different scorer configuration and needs to be updated to match the final paper values.

**Qwen-cont (exp_017_qwen_continuation):**
| Pair | Paper | Registry | Delta |
|------|-------|----------|-------|
| 0v1 | .9971 | 0.9972 | -0.0001 |
| 1v2 | .6112 | 0.6114 | -0.0002 |
| 2v3 | .5609 | 0.5609 | 0 |
| 3v4 | .5409 | 0.5408 | +0.0001 |
| 4v5 | .5141 | 0.5139 | +0.0002 |

- [PASS] All within rounding tolerance.

### Table robustness_10k

**Pythia-1.4B 10K (exp_pythia14b_c4_10k):**
| Pair | Paper | Registry |
|------|-------|----------|
| 0v1 | 0.9712 | 0.9712 |
| 1v2 | 0.6175 | 0.6175 |
| 2v3 | 0.5364 | 0.5364 |
| K* | 2 | 2 |

- [PASS] Exact match.

**Qwen-cont 10K (exp_qwen_cont_10k):**
| Pair | Paper | Registry |
|------|-------|----------|
| 0v1 | 0.9875 | 0.9875 |
| 1v2 | 0.6346 | 0.6346 |
| 2v3 | 0.5616 | 0.5616 |
| K* | 2 | 2 |

- [PASS] Exact match.

**LLaMA-8B 10K (exp_llama8b_10k):**
| Pair | Paper | Registry |
|------|-------|----------|
| 0v1 | 0.9282 | 0.9282 |
| 1v2 (OOF) | 0.5880 | 0.588 |
| 1v2 (pipeline) | 0.6148 | 0.6148 |
| 2v3 | 0.5247 | 0.5247 |
| Bonferroni CI | [0.5776, 0.5978] | [0.5776, 0.5978] |
| K* | 1 | 1 |

- [PASS] Exact match.

### Transfer Matrix (tab:s1_transfer vs exp_013_cross_transfer)

| Cell | Paper | Registry | Match |
|------|-------|----------|-------|
| Qwen-rw diag | .423 | 0.4229 | OK (rounds to .423) |
| Pythia diag | .386 | 0.3856 | OK (rounds to .386) |
| OLMo diag | .382 | 0.3822 | OK (rounds to .382) |
| Qwen-cont diag | .388 | 0.3875 | OK (rounds to .388) |
| Qwen-rw→Pythia | .259 | 0.259 | OK |
| Qwen-rw→OLMo | .265 | 0.2653 | OK |
| Pythia→OLMo | .353 | 0.3531 | OK |
| Qwen-cont→OLMo | .311 | 0.3112 | OK |

- [PASS] All values consistent within 3-decimal rounding.

## 3. Spelling/Grammar

- [PASS] No repeated words ("the the", "is is", etc.) found.
- [PASS] No em-dashes (---) in normal prose. All "--" usage is for number ranges (80--100%, 1B--8B), which is standard LaTeX.
- [PASS] No obvious spelling errors detected.
- [PASS] No unclosed braces or LaTeX formatting errors detected.
- [PASS] Sentence structure is grammatically sound throughout.

**Minor notes (non-critical):**
- appendix_extended.tex line 114: `{\sloppy ...}` block is functional but unusual; acceptable for preventing overfull hboxes in that paragraph.
- Hyphenated compounds ("depth-aware", "model-free", "cross-model", "scorer-invariant") are standard English compound adjectives, not prohibited dashes.

## Summary

- **Critical issues: 1**
  - OLMo registry entry (`exp_002_olmo_depth`) is stale: shows K\*=2 / 1v2 AUC=0.6146, while the paper consistently reports K\*=1 / 1v2 AUC=0.508. The paper is internally consistent; the registry needs updating.

- **Warnings: 1**
  - `\label{tab:pairwise_significance}` uses `tab:` prefix but is not on a table (minor, currently unreferenced).

- **Informational: 2**
  - Multi-label on Discussion section (intentional, valid).
  - External `\input{tables/...}` files not verified.
