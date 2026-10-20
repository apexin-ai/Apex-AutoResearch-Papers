# Reference Audit Report — solver-trace-ablation (v2)

**Audit date**: 2026-05-15 (supersedes v1 from 2026-05-14)
**Paper**: Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law (ACL submission)
**Bib entries**: 28 | **Cited in .tex**: 19 | **Orphan entries**: 9

---

## Summary

- **No fake citations.** All 28 bib entries verified via web search (arXiv, conference proceedings, publisher pages).
- **0 factual errors** in cited entries (v1 issues with `rlsf`, `kwa-catastrophic-goodhart`, `spurious-rewards` authors have been fixed since v1)
- **2 missing citations** recommended (ProofWriter dataset, Qwen3 model)
- **9 orphan bib entries** (in .bib but never `\cite`d in .tex)
- **2 minor author-name issues**
- **1 format inconsistency**

---

## Issue List (by severity)

### HIGH — Missing Citations

**H1. ProofWriter dataset not cited**
- The paper mentions `proofwriter_fol_100.jsonl` and `proofwriter_fol_*.jsonl` legacy filenames in `method.tex:17`, `experiments.tex:10`, and appendix tables.
- While the paper explicitly disclaims these are FOLIO-derived data, readers encountering the filename will search for a ProofWriter citation.
- **Recommendation**: cite ProofWriter where the legacy filename is first explained.

**H2. Qwen3 model not cited**
- Qwen3-4B is the base model for all experiments. No citation.
- Qwen3 Technical Report: arXiv:2505.09388 (published 2025-05-14).
- **Recommendation**: add citation in Section 4.1 (Setup).

### MEDIUM — Author Name Issues

**M1. Math-Shepherd: "R.X. Xu" → "Runxin Xu"**
- Entry `math-shepherd`, author field.
- "R.X. Xu" is non-standard; ACL Anthology lists "Runxin Xu".

**M2. Logic-LM: "William Wang" → "William Yang Wang"**
- Entry `logic-lm`, author field.
- Canonical name per ACL Anthology is "William Yang Wang".

### MEDIUM — Orphan Bib Entries (9 uncited)

These entries exist in `references.bib` but are never cited. They won't appear in the compiled bibliography but add maintenance burden. Remove them, or cite the relevant ones.

| Key | Paper | Relevance |
|-----|-------|-----------|
| `thought-like-pro` | Tan et al. 2024, "Thought-Like-Pro" | Related (Prolog+LLM) |
| `gao-effective-rl-reward` | Gao et al. 2024, "On Designing Effective RL Reward" | **High** (reward design for LLM reasoning) |
| `spurious-rewards` | Shao et al. 2025, "Spurious Rewards" | **High** (spurious reward signals in RLVR) |
| `fover-pei2025` | Pei et al. 2025, "FoVer" (TACL) | Related (FOL verification) |
| `lorp` | Di et al. 2025, "LoRP" (KBS) | Related (Prolog+LLM) |
| `thinkprm` | Khalifa et al. 2025, "ThinkPRM" | Moderate (PRM) |
| `versaprm` | Zeng et al. 2025, "VersaPRM" (ICML) | Moderate (PRM) |
| `rprm` | She et al. 2025, "R-PRM" (EMNLP) | Moderate (PRM) |
| `metr-reward-hacking` | METR 2025 blog post | **High** (frontier reward hacking) |

**Strong recommendations to cite** (if space permits):
1. `spurious-rewards` in Related Work — directly complements the paper's finding that reward signals can be gamed.
2. `metr-reward-hacking` in Introduction or Discussion — documents reward hacking in frontier models in the wild.
3. `gao-effective-rl-reward` in §3.3 (reward conditions) — relevant to reward design choices.

### LOW — Format Inconsistency

**L1. `archiveprefix` casing**
- `reward-hacking-survey` uses lowercase `archiveprefix = {arXiv}`.
- All other entries use camelCase `archivePrefix = {arXiv}`.
- BibTeX is case-insensitive for field names so this compiles fine, but it's inconsistent.

---

## Required Citations Checklist

| Required Citation | Status | Bib Key |
|-------------------|--------|---------|
| DeepSeekMath GRPO | ✅ Correct | `deepseekmath` |
| Logic-LM | ✅ Correct | `logic-lm` |
| LINC | ✅ Correct | `linc` |
| SatLM | ✅ Correct | `satlm` |
| Manheim & Garrabrant Goodhart taxonomy | ✅ Correct | `manheim-goodhart-taxonomy` |
| Gao et al. reward overoptimization | ✅ Correct | `gao-reward-overoptimization` |
| ProofWriter dataset | ❌ **Missing** | — (see H1) |
| DeMillo et al. 1978 mutation testing | ✅ Correct | `demillo1978` |

---

## Full Verification Table (all 28 bib entries)

### Cited entries (19) — all verified ✅

| Bib Key | Title | Venue | Verified Source |
|---------|-------|-------|-----------------|
| `deepseekmath` | DeepSeekMath | arXiv 2024 | arXiv:2402.03300 |
| `logic-rl` | Logic-RL | arXiv 2025 | arXiv:2502.14768 |
| `mellgren-prolog-grpo` | Training LMs to Use Prolog | arXiv 2025 | arXiv:2512.07407 |
| `satlm` | SatLM | NeurIPS 2023 | NeurIPS proceedings |
| `lightman-verify-step` | Let's Verify Step by Step | ICLR 2024 | ICLR proceedings |
| `skalse-reward-hacking` | Defining and Characterizing Reward Hacking | NeurIPS 2022 | NeurIPS proceedings |
| `demillo1978` | Hints on Test Data Selection | IEEE Computer 11(4):34-41, 1978 | DBLP, IEEE Xplore |
| `jia-harman-survey` | Mutation Testing Survey | IEEE TSE 37(5), 2011 | IEEE |
| `bondarenko-spec-gaming` | Specification Gaming in Reasoning Models | arXiv 2025 | arXiv:2502.13295 |
| `kim-game-formalization` | Do LLMs Game Formalization? | VerifAI-2 @ ICLR 2026 | arXiv:2604.19459 |
| `gao-reward-overoptimization` | Scaling Laws for Reward Overoptimization | ICML 2023 | ICML proceedings |
| `karwowski-goodhart-rl` | Goodhart's Law in RL | ICLR 2024 | ICLR proceedings |
| `folio` | FOLIO | EMNLP 2024 | ACL Anthology |
| `logic-lm` | Logic-LM | Findings EMNLP 2023 | ACL Anthology |
| `linc` | LINC | EMNLP 2023 | ACL Anthology |
| `manheim-goodhart-taxonomy` | Categorizing Variants of Goodhart's Law | arXiv 2019 | arXiv:1803.04585 |
| `math-shepherd` | Math-Shepherd | ACL 2024 | ACL Anthology |
| `reward-hacking-survey` | Reward Hacking in the Era of Large Models | arXiv 2026 | arXiv:2604.13602 |
| `processbench` | ProcessBench | ACL 2025 | ACL Anthology |

### Uncited entries (9) — all verified ✅ but not referenced in .tex

| `thought-like-pro` | arXiv:2407.14562 | ✅ |
| `gao-effective-rl-reward` | arXiv:2410.15115 | ✅ |
| `spurious-rewards` | arXiv:2506.10947 | ✅ |
| `fover-pei2025` | TACL 2025 | ✅ |
| `lorp` | KBS 2025 | ✅ |
| `thinkprm` | arXiv:2504.16828 | ✅ |
| `versaprm` | ICML 2025 | ✅ |
| `rprm` | EMNLP 2025 | ✅ |
| `metr-reward-hacking` | METR blog 2025 | ✅ |

---

## Suggested .bib Additions

### H1: ProofWriter

```bibtex
@inproceedings{proofwriter,
  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},
  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},
  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},
  year         = {2021},
  note         = {arXiv:2012.13048},
}
```

Insert in `method.tex:17`:
```
- ...retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename but contains only FOLIO-derived examples.
+ ...retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
```

### H2: Qwen3

```bibtex
@article{qwen3,
  author       = {{Qwen Team}},
  title        = {{Qwen3 Technical Report}},
  journal      = {arXiv preprint arXiv:2505.09388},
  year         = {2025},
  eprint       = {2505.09388},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
}
```

Insert in `experiments.tex:9`:
```
- We train Qwen3-4B with GRPO~\citep{deepseekmath}
+ We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath}
```

### M1: Math-Shepherd author fix

```bibtex
% In math-shepherd, replace:
  author = {Peiyi Wang and Lei Li and Zhihong Shao and R.X. Xu and others},
% with:
  author = {Peiyi Wang and Lei Li and Zhihong Shao and Runxin Xu and others},
```

### M2: Logic-LM author fix

```bibtex
% In logic-lm, replace:
  author = {Liangming Pan and Alon Albalak and Xinyi Wang and William Wang},
% with:
  author = {Liangming Pan and Alon Albalak and Xinyi Wang and William Yang Wang},
```

### L1: archiveprefix casing

```bibtex
% In reward-hacking-survey, replace:
  archiveprefix = {arXiv},
% with:
  archivePrefix = {arXiv},
```

---

## Changes Since v1 (2026-05-14)

The following v1 issues have been resolved (entries removed or corrected since v1 audit):
- `rlsf` (wrong title + wrong authors) — entry removed from bib
- `kwa-catastrophic-goodhart` (wrong author names) — entry removed from bib
- `spurious-rewards` (wrong first author "Ruixin Yang") — corrected to "Rulin Shao"
- `rubric-grpo` (minor title divergence) — entry removed from bib
- Bib reduced from 33 → 28 entries; 5 entries removed, new PRM/eval entries added

**v2 new findings**: H1 (ProofWriter missing), H2 (Qwen3 missing), M1-M2 (author names), 9 orphan entries identified, format consistency check.
