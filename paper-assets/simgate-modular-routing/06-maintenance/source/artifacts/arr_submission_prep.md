# ARR Submission Preparation — simgate-modular-routing

> Updated 2026-05-22 (R27 aligned) | DDL: 2026-05-25

---

## 1. Submission Form Pre-fill

### Title
Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld

### Abstract (plain text, synced with abstract.tex post-R27)
LLM agent routing (deciding when to rely on internal reasoning versus external tool use) is typically addressed by training routers directly, without first understanding what mechanistic signal drives the routing preference. This absence of diagnostic methods risks building routers atop confounded or trivial signal. We propose an episode-level counterfactual framework that compares pure-strategy outcomes (internal-only vs. deterministic-only) to decompose routing signal into its mechanistic components before any router is constructed. Applying this framework to ScienceWorld (11 task types, 245 episodes), we find that 78.9% of non-tie routing labels arise from death asymmetry—a finding replicated across three architecturally distinct 7–9B model families (spread 2.2 pp), revealing that in catastrophic-failure environments, signal diversity can collapse to a single dominant mechanism. Cross-environment probes on MATH and ALFWorld diagnose qualitatively different routing mechanisms (no extractable signal and information asymmetry, respectively), providing preliminary evidence of applicability beyond death-dominated settings. The framework distinguishes methodological generality (applicable to any environment with paired episode outcomes) from empirical generality (full quantitative validation on ScienceWorld only). A ~50-episode diagnostic pilot provides preliminary build-vs-buy signal given large effect sizes (d = 3.02); environments with smaller effects may require larger samples.

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
`main.pdf` — compiled 2026-05-22 UTC, 24 pages (8 main + 16 appendix), 0 compile errors

---

## 2. Supplementary Materials Checklist

### Must Submit
| Item | Status | Notes |
|------|--------|-------|
| main.pdf | ✅ Ready | 24 pages (8 main + 16 appendix), compiled & verified |
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
- **Negative results**: §3.6 reports router training as "Preliminary Negative Result" (signal-limited, not architecture-limited); framed as diagnostic contribution
- **Causal methodology**: Pure-strategy comparison grounded as simplified instance of potential outcomes framework (Rubin 1974), not full structural causal models; Related Work §"Causal Grounding" makes this explicit
- **Statistical claims**: Pilot "provides preliminary signal" (not "suffices"); qualifier "given a large effect size (d=3.02); environments with smaller effects may require larger samples" added in R26
- **Model scope**: Cross-model replication scoped to "three 7–9B model families" (not "all models"); 72B is scaling probe only

---

## 4. Pre-submission Verification

| Check | Status |
|-------|--------|
| PDF compiles without errors | ✅ |
| Page limit (8 pages main text) | ✅ Exactly 8 pages |
| Anonymous (no author names in PDF) | ✅ `\author{Anonymous}`, `\hypersetup{pdfauthor={}}` |
| All \cite → \citep where needed | ✅ Fixed (28 instances, Round 25) |
| No orphan bib entries | ✅ 0 orphan (57 entries, +3 R26: pearl2009/rubin1974/bonagiri2025, +3 R27: switch-transformer-2022/gshard-2021/kaushik2020learning) |
| Numbers consistent with registry | ✅ 12/12 checked (final consistency check) |
| Limitations section present | ✅ |
| Ethics statement present | ✅ |
| Causal claims properly scoped | ✅ "simplified instance" not full do-calculus (R26 fix) |
| Pilot claim hedged | ✅ "preliminary signal...given large effect size" (R26 fix) |

---

