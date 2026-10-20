# OpenReview Submission Checklist — EMNLP 2026 ARR

## Paper Metadata

### 1. Title
```
Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains
```

### 2. Abstract (plain text, no LaTeX)
```
Recursive LLM generation shifts where text sits in distributional space but leaves how it is shaped nearly unchanged, and this asymmetry is consistent across five model families spanning 0.6B to 8B parameters. We term this differential depth response (DDR): under standard decoding, mean entropy and lexical diversity drift monotonically with generation depth while entropy max and tail decay show an order-of-magnitude smaller effect size. Prior work on iterative generation tracks aggregate convergence without separating what changes from what is preserved; DDR provides this decomposition and enables coarse depth classification (gen-0/gen-1/gen-2+): a 7-feature ensemble achieves leak-free binary F1 = 0.694 (95% CI [.688, .700]) under leave-one-generator-out evaluation and 0.830 on cross-model chains (5-generator subset, LOGO; 95% CI [.818, .841]), at lower cost than multi-detector alternatives. Despite measurable distributional drift, equivalence testing (TOST ±2%, p < 0.001) suggests no downstream training quality degradation. The depth signal degrades under instruction tuning; current applicability is restricted to base models.
```

### 3. Keywords (5–8)
```
generation depth classification, recursive LLM generation, distributional drift, machine-generated text detection, text forensics, data provenance, model collapse, iterative generation
```

### 4. TL;DR (≤250 characters)
```
Recursive LLM generation shifts distributional location but preserves shape; this differential depth response enables classifying text by generation depth (gen-0/gen-1/gen-2+) with F1=0.83 on cross-model chains.
```

### 5. Paper Type
- **Long paper** (8 pages main body)

### 6. Subject Areas (select all that apply)
- NLP Applications → Text Classification
- Language Modeling
- Machine Learning for NLP
- Resources and Evaluation
- Computational Social Science and Cultural Analytics

### 7. Conference Declaration
- **EMNLP 2026** (via ARR unified review)

## AI Assistance Disclosure
```
We used Claude (Anthropic) for code assistance during experiment implementation and for iterative editing suggestions during paper writing. All scientific claims, experimental design, data analysis, and final writing were produced and verified by the authors. No AI system was used to generate experimental results or perform scientific reasoning.
```

## Ethics Statement
All texts analyzed are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved. The method estimates generation depth of text passages, not author identity — individual authorship attribution is outside both scope and capability. Depth estimation tools could in principle be used to selectively suppress legitimate machine-generated content (e.g., accessibility tools, assistive writing); deployment is recommended for data governance pipelines where provenance transparency, rather than content removal, is the objective. All code, data, and trained models will be released upon publication.

- **Licenses**: Apache 2.0 (Pythia, OLMo, Mistral), Qwen License (Qwen3), Llama Community License (Llama 3.2), CC BY-SA 3.0 (Wikipedia seeds)
- **Compute**: 4× NVIDIA RTX 5090 (32GB each), ~62 GPU-hours total
- **Ethics Review Flag**: No — no human subjects, no personal data, no dual-use concerns beyond standard text detection

## Supplementary Material
- `anonymous_supplement.tgz` (~19MB)
- Contents: 34 experiment scripts + 30 data files + verification report
- Anonymization: verified (no emails, API keys, server IDs, author names)

## Responsible NLP Checklist

| # | Item | Answer | Reference |
|---|------|--------|-----------|
| A1 | Limitations discussed | Y | §Limitations (~1.5 pages) |
| A2 | Potential risks discussed | Y | §Ethics Statement |
| A3 | Claims summarized in abstract/intro | Y | Abstract, §1 |
| B1 | Artifact creators cited | Y | §3, References |
| B2 | Licenses discussed | Y | §Ethics: Licenses |
| B3 | Intended use discussed | Y | §Ethics |
| B4 | PII/offensive content checked | Partial | Wikipedia seeds, no PII |
| B5 | Documentation provided | Y | §3, Appendix A |
| C1 | Parameter counts reported | Y | Table 1 |
| C2 | Compute infrastructure reported | Y | §Ethics: Compute budget |
| C3 | Runtime reported | Partial | Table 2 (inference ms/text); training negligible |
| C4 | Metrics with CIs | Y | Tables 1–2, 95% bootstrap CIs (n=1,000 unless otherwise noted; cross-model n=2,000) |
| C5 | Hyperparameter strategy | Y | §3.4 (defaults, no search) |
| C6 | Hyperparameter ranges | N/A | No search conducted |
| D1 | Data collection described | Y | §3.2 |
| D2 | Data statistics reported | Y | §3.2, Appendix A |
| D3 | PII/offensive content discussed | Y | §Ethics |
| D4 | Data provided | Pending | Release upon publication |
| E1–E5 | Human annotators | N/A | Fully automatic labels |

## Author Information

> ⚠️ Anonymous submission — do not include author-identifying information.

- `\author{Anonymous}` confirmed
- No acknowledgements section
- No GitHub/institution links in paper body
- Supplement anonymized (grep verified)

## Pre-submission Checks

- [x] PDF compiles with 0 errors, 0 undefined refs
- [x] Main body ≤ 8 pages (Conclusion on p8)
- [x] Line numbers enabled (`\linenumbers`)
- [x] ACL 2023 template (`\usepackage[review]{acl}`)
- [x] All figures render correctly
- [x] Supplement ≤ 50MB (current: ~19MB)
- [x] Abstract ≤ 250 words
- [x] Title ≤ 200 characters
- [ ] PDF metadata contains no author names (verify: `pdfinfo main.pdf` → Author field empty)
- [ ] No TODO/FIXME markers remaining in text
- [ ] Final bibliography check — no "?" or missing fields

## Upload Files
1. `main.pdf` — compiled paper (31 pages: 8 main + refs + appendix)
2. `anonymous_supplement.tgz` — supplementary materials (~19MB)

## Manual Actions Required
- [ ] Log in to OpenReview + verify reviewer registration
- [ ] Select "EMNLP 2026" as Conference Declaration
- [ ] Upload `main.pdf`
- [ ] Upload `anonymous_supplement.tgz`
- [ ] Fill Responsible NLP Research Checklist (pre-filled above)
- [ ] Paste AI Assistance Disclosure
- [ ] Select subject areas
- [ ] Confirm abstract matches §2 above
