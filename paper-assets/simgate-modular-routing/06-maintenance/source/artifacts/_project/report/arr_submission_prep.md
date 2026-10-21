# ARR Submission Preparation — simgate-modular-routing

> Generated 2026-05-21 | DDL: 2026-05-25

---

## 1. Submission Form Pre-fill

### Title
Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld

### Abstract (plain text)
LLM agent routing (deciding when to rely on internal reasoning versus external tool use) is typically addressed by training routers directly, without first understanding what mechanistic signal drives the routing preference. This absence of diagnostic methods risks building routers atop confounded or trivial signal. We propose an episode-level counterfactual framework that compares pure-strategy outcomes (internal-only vs. deterministic-only) to decompose routing signal into its mechanistic components before any router is constructed. Applying this framework to ScienceWorld (11 task types, 245 episodes), we find that 78.9% of non-tie routing labels arise from death asymmetry: the internal strategy triggers catastrophic failure while the deterministic strategy survives. This label fraction is penalty-independent. A derived score-weighted measure, the Death Avoidance Factor, reaches 88-90% across three model families (Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B), confirming convergence on a single dominant mechanism. Cross-environment probes on MATH and ALFWorld diagnose qualitatively different routing mechanisms (no extractable signal and information asymmetry, respectively), illustrating the framework's applicability. A ~50-episode diagnostic pilot suffices to identify the dominant routing mechanism in a new environment, enabling informed build-vs-buy decisions before expensive router training.

### Keywords
1. LLM agent routing
2. counterfactual analysis
3. death avoidance
4. diagnostic framework
5. ScienceWorld
6. tool use
7. modular computation

### Submission Type
Long paper (8 pages + unlimited references)

### Track
Main conference (EMNLP 2026 via ARR)

### Suggested Track/Area
Interpretability and Analysis of Models for NLP

### Author List
Anonymous (review version; actual authors to be added post-acceptance)

### Paper PDF
`main.pdf` — compiled 2026-05-21 17:16 UTC, 25 pages (8 main + 17 appendix), 0 compile errors

---

## 2. Supplementary Materials Checklist

### Must Submit
| Item | Status | Notes |
|------|--------|-------|
| main.pdf | ✅ Ready | 25 pages, compiled & verified |
| Appendices A–T | ✅ Included in main.pdf | No separate appendix file needed |

### Optional (pending user decision)
| Item | Status | Notes |
|------|--------|-------|
| Anonymous code repo URL | ⏳ Waiting user confirmation | Need to create: requirements.txt + README.md, host on anonymous GitHub/GitLab |
| Supplementary data description | ⏳ Optional | Episode-level counterfactual data (245 episodes × 2 strategies) |

### Do NOT Submit
| Item | Reason |
|------|--------|
| Non-anonymized code | Violates double-blind |
| Training checkpoints | Too large, not required |
| Raw experiment logs | Contains server identifiers |
| W&B run links | Contains identifying information |
| Registry/artifacts directory | Internal tooling, not reproducibility-relevant |

---

## 3. ARR Responsible NLP Checklist

Filled in the OpenReview submission form (not in the PDF). Key points to prepare:

- **Limitations section**: ✅ Present in main.pdf (5 paragraphs: environmental scope, methodological constraints, statistical limitations, pure-strategy upper bound, diagnostic scope)
- **Ethics statement**: ✅ Present in main.pdf (public datasets, no human subjects, GPU-hours disclosed)
- **Compute budget**: ~200 GPU-hours (140h inference + 35h training + 25h eval), disclosed in Ethics Statement
- **Datasets used**: ScienceWorld v1.2.3 (Apache 2.0), ALFWorld (MIT), MATH (MIT)
- **Models used**: Qwen2.5-7B/72B, Llama-3.1-8B, Gemma-2-9B-it, Qwen3-0.6B/1.7B/4B (all publicly available)

---

## 4. Pre-submission Verification

| Check | Status |
|-------|--------|
| PDF compiles without errors | ✅ |
| Page limit (8 pages main text) | ✅ Exactly 8 pages |
| Anonymous (no author names in PDF) | ✅ `\author{Anonymous}`, `\hypersetup{pdfauthor={}}` |
| All \cite → \citep where needed | ✅ Fixed (28 instances, Round 25) |
| No orphan bib entries | ✅ 0 orphan (51 entries) |
| Numbers consistent with registry | ✅ 12/12 checked (final consistency check) |
| Limitations section present | ✅ |
| Ethics statement present | ✅ |

---

