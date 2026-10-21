# Reference Audit Report — solver-trace-ablation

**Date**: 2026-05-14
**Files scanned**: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, paper.tex, references.bib

---

## 1. Missing Citations (in .tex but not in .bib)

**None.** All 33 unique citation keys used in .tex files have corresponding entries in references.bib.

---

## 2. Orphan Entries (in .bib but never referenced)

23 entries in references.bib are never cited in any .tex file:

| # | Key | Title (abbreviated) |
|---|-----|---------------------|
| 1 | `deepseek-r1` | DeepSeek-R1: Incentivizing Reasoning... |
| 2 | `deepproblog` | Neural Probabilistic Logic Programming... |
| 3 | `neurasp` | NeurASP: Embracing Neural Networks... |
| 4 | `reward-shaping-rlhf` | Reward Shaping to Mitigate Reward Hacking... |
| 5 | `rlvr-reasoning` | Reinforcement Learning with Verifiable Rewards... |
| 6 | `moskovitz-constrained-rlhf` | Confronting Reward Model Overoptimization... |
| 7 | `mutation-guided-meta` | Mutation-Guided LLM-based Test Generation... |
| 8 | `mutation-consistency-llm` | Mutation-based Consistency Testing... |
| 9 | `deepmutation` | A Probabilistic Framework for Mutation Testing... |
| 10 | `inform-reward-hacking` | InfoRM: Mitigating Reward Hacking... |
| 11 | `mo-grpo` | MO-GRPO: Mitigating Reward Hacking... |
| 12 | `energy-loss-reward-hacking` | The Energy Loss Phenomenon in RLHF... |
| 13 | `proofwriter` | ProofWriter: Generating Implications... |
| 14 | `nl2fol` | NL2FOL: Translating Natural Language... |
| 15 | `logica2` | LogiQA 2.0: An Improved Dataset... |
| 16 | `rafailov-daa-scaling` | Scaling Laws for Reward Model Overoptimization in DAA |
| 17 | `huang-chi-squared` | Correcting the Mythos of KL-Regularization... |
| 18 | `coste-rm-ensembles` | Reward Model Ensembles Help Mitigate... |
| 19 | `fover-kamoi2026` | FoVer: Generalizable Process Reward Models... |
| 20 | `deepseek-prover-v15` | DeepSeek-Prover-V1.5... |
| 21 | `alphaproof` | AlphaProof |
| 22 | `bipars` | Learning to Utilize Shaping Rewards... |
| 23 | `dapo` | DAPO: An Open-Source LLM RL System... |

**Note**: `proofwriter` is notable — the paper discusses ProofWriter FOL problems in discussion.tex and conclusion.tex but never formally cites it. This may be intentional (dataset attribution via text only) but a citation would be proper.

---

## 3. Incomplete Entries (missing required fields among key citations)

All 12 checked key citations have author, title, year, and venue. No missing required fields.

| Key | author | title | year | venue | Status |
|-----|--------|-------|------|-------|--------|
| `deepseekmath` | OK | OK | 2024 | arXiv | OK |
| `folio` | OK | OK | 2024 | EMNLP | OK |
| `manheim-goodhart-taxonomy` | OK | OK | 2019 | arXiv | OK |
| `gao-reward-overoptimization` | OK | OK | 2023 | ICML | OK |
| `karwowski-goodhart-rl` | OK | OK | 2024 | ICLR | OK |
| `demillo1978` | OK | OK | 1978 | Computer | Complete |
| `lightman-verify-step` | OK | OK | 2024 | ICLR | OK |
| `skalse-reward-hacking` | OK | OK | 2022 | NeurIPS | OK |
| `logic-lm` | OK | OK | 2023 | EMNLP Findings | OK |
| `linc` | OK | OK | 2023 | EMNLP | OK |
| `satlm` | OK | OK | 2023 | NeurIPS | OK |
| `mellgren-prolog-grpo` | OK | OK | 2024 | arXiv | OK |

---

## 4. Placeholder Authors (`{Various}` etc.)

**3 CRITICAL** — cited entries with `{Various}` as author:

| Key | Cited in | Real authors needed |
|-----|----------|---------------------|
| **`rubric-grpo`** | related_work.tex | arXiv:2605.08061 |
| **`reward-hacking-survey`** | introduction.tex | arXiv:2604.13602 |
| **`lorp`** | related_work.tex | Knowledge-Based Systems, 2025 |

5 additional orphan entries also have `{Various}` — lower priority since uncited:
- `rlvr-reasoning`, `mutation-consistency-llm`, `deepmutation`, `inform-reward-hacking`, `energy-loss-reward-hacking`

---

## 5. Format Issues

### Incomplete author names (first names missing)
| Key | Current author field | Issue |
|-----|---------------------|-------|
| `logic-rl` | `Xian and others` | Missing full first-author name (likely "Tian Xie" or similar) |
| `nl2fol` (orphan) | `Lalwani and Kim and others` | Missing first names |
| `logica2` (orphan) | `Liu and others` | Missing first names |

### Corporate/team authors (acceptable but verify)
| Key | Author | Status |
|-----|--------|--------|
| `deepseek-r1` (orphan) | `{DeepSeek-AI}` | OK (corporate) |
| `mo-grpo` (orphan) | `{CyberAgent AI Lab}` | OK (corporate) |
| `alphaproof` (orphan) | `{Google DeepMind}` | OK (corporate) |

### `and others` vs `et al.`
Multiple entries use `and others` in the author field. BibTeX convention is to use this to trigger "et al." rendering, but some styles require at least 3 named authors before truncating. Currently affected cited entries:
- `deepseekmath` (4 named + others) — OK
- `folio` (1 named + others) — borderline
- `satlm` (1 named + others) — borderline
- `lightman-verify-step` (3 named + others) — OK
- **`logic-rl`** (incomplete name + others) — needs fix

---

## 6. Action Items (prioritized)

### CRITICAL (will cause visible problems)
1. **Fix `rubric-grpo` author** — replace `{Various}` with real authors from arXiv:2605.08061
2. **Fix `reward-hacking-survey` author** — replace `{Various}` with real authors from arXiv:2604.13602
3. **Fix `lorp` author** — replace `{Various}` with real authors
4. **Fix `logic-rl` author** — `Xian and others` is an incomplete name; retrieve full first-author name

### RECOMMENDED (quality improvement)
5. **Add `\cite{proofwriter}` to discussion.tex or conclusion.tex** — the paper references "ProofWriter FOL problems" by name without citing it; the bib entry exists but is orphan
6. **Clean orphan entries** — remove 23 unused bib entries to reduce clutter (or cite them if intentionally reserved for camera-ready)

### LOW PRIORITY
7. Review `folio` and `satlm` author fields — only 1 named author each before `and others`; consider adding 2-3 more for completeness
8. Fix orphan entries' `{Various}` placeholders if they will be cited later
