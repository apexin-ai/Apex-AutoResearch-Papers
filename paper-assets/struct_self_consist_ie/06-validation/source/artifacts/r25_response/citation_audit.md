# Citation Audit Report

**Date:** 2026-05-20
**Bib file:** `docs/paper/references.bib` (95 entries)
**Tex scope:** `docs/paper/sections/*.tex` + `docs/paper/main.tex` (74 unique cite keys)

---

## Unverified Citations (4 flagged by R25)

All four verified as **real, published papers** with correct metadata.

| Key | Status | Title | Verification |
|-----|--------|-------|-------------|
| `hobelsberger2025systematic` | **VERIFIED** | Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models | arXiv:2510.20460. Authors (Hobelsberger, Winner, Nawroth, Mitevski, Haensch), year (2025), title all match. Likely failed OpenAlex because it's an arXiv preprint not yet indexed. |
| `lightman2024verify` | **VERIFIED** | Let's Verify Step by Step | arXiv:2305.20050, accepted at ICLR 2024. Authors (Lightman, Kosaraju, Burda, Edwards, Baker, Lee, Leike, Schulman, Sutskever, Cobbe), venue (ICLR 2024), year (2024) all match. |
| `venktesh2025trust` | **VERIFIED (ORPHAN)** | Trust but Verify! A Survey on Verification Design for Test-time Scaling | arXiv:2508.16665. Authors (Venktesh, Rathee, Anand), year (2025), title match. **Not cited in any tex file** — orphan entry. |
| `aggarwal2023adaptive` | **VERIFIED** | Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs | arXiv:2305.11860, published at EMNLP 2023 (ACL Anthology). Authors (Aggarwal, Madaan, Yang, Mausam), venue, year all match. |

**Action:** No corrections needed for these 4 entries. `venktesh2025trust` can be deleted (orphan).

---

## Metadata Mismatches

No metadata errors found in the 4 flagged entries during web verification. All titles, authors, years, and venues match their published versions.

If the R25 audit flagged 3 additional metadata mismatches beyond these 4, the specific keys were not provided. A full bib-vs-OpenAlex reconciliation would require re-running the automated check.

---

## Orphan Bib Entries (21 found, vs. 17 reported)

Entries present in `references.bib` but **never cited** in any `docs/paper/sections/*.tex` file:

| # | Key | Title |
|---|-----|-------|
| 1 | `yao2026consistency` | Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction |
| 2 | `venktesh2025trust` | Trust but Verify! A Survey on Verification Design for Test-time Scaling |
| 3 | `yun2025price` | The Price of Format: Diversity Collapse in LLMs |
| 4 | `gao2023scaling` | Scaling Laws for Reward Model Overoptimization |
| 5 | `chen2021evaluating` | Evaluating Large Language Models Trained on Code |
| 6 | `ho2023reasoning` | Large Language Models Are Reasoning Teachers |
| 7 | `min2022rethinking` | Rethinking the Role of Demonstrations: What Makes In-Context Learning Work? |
| 8 | `suzgun2023crowd` | Follow the Wisdom of the Crowd: Effective Text Generation via Minimum Bayes Risk Decoding |
| 9 | `stechly2024chain` | Chain of Thoughtlessness? An Analysis of CoT in Planning |
| 10 | `setlur2025rewarding` | Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning |
| 11 | `kuleshov2018accurate` | Accurate Uncertainties for Deep Learning Using Calibrated Regression |
| 12 | `openai2024o1` | OpenAI o1 System Card |
| 13 | `ashok2023promptner` | PromptNER: Prompting For Named Entity Recognition |
| 14 | `wang2025gptner` | GPT-NER: Named Entity Recognition via Large Language Models |
| 15 | `wei2023chatie` | ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT |
| 16 | `sagi2018ensemble` | Ensemble learning: A survey |
| 17 | `lakshminarayanan2017ensembles` | Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles |
| 18 | `welling2011sgld` | Bayesian Learning via Stochastic Gradient Langevin Dynamics |
| 19 | `deng2023rad` | Reward-Augmented Decoding: Efficient Controlled Text Generation With a Unidirectional Reward Model |
| 20 | `keraghel2024ner` | Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study |
| 21 | `xu2024llmie` | Large Language Models for Generative Information Extraction: A Survey |

---

## Recommended Actions

### Delete (21 orphan entries)
Remove all 21 orphan entries listed above from `references.bib`. None are referenced in the compiled tex files.

### Fix
No metadata corrections required — all 4 flagged citations verified with correct metadata.

### Note
The original R25 audit reported 17 orphans; this audit found 21. The difference of 4 likely reflects entries added to the bib after the initial audit without corresponding `\cite{}` commands in tex, or entries that were removed from tex during recent edits.
