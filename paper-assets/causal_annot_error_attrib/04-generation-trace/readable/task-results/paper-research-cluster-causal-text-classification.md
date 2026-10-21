# paper research cluster causal text classification

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_research_cluster_causal_text_classification_20260520T155937_result.json`
- **Structured JSON:** [`0f18ae625f1129ed6f1c.json`](../../sessions/0f/0f18ae625f1129ed6f1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 papers in causal-text-classification, all verified=true.

**Summary of changes to `literature_map.yaml`:**

**Verified existing 3 papers:**
- `wood_doughty2018` — added S2 ID (`33af8451...`), ArXiv ID (`1810.00956`), set verified=true
- `teblunthuis2024` — added S2 ID (`3a1c7532...`), ArXiv ID (`2307.06483`), DOI (`10.1080/19312458.2023.2293713`), set verified=true
- `lee_wood_doughty2024` — **fixed incorrect title** (was "Categorical Variables and Measurement Error..." → actual: "Controlling for Unobserved Confounding with Large Language Model Classification of Patient Smoking Status"), updated venue to "AIM-FM Workshop, NeurIPS 2024", updated abstract, set verified=true

**Added 3 new papers:**
1. `keith_jensen_oconnor2020` — "Text and Causal Inference: A Review..." (ACL 2020) — first systematic review of text+causal inference; identifies classifier ME as open challenge
2. `chen_bhattacharya_keith2024` — "Proximal Causal Inference With Text Data" (NeurIPS 2024) — uses zero-shot NLP proxies for unmeasured confounders with identification proofs
3. `yang_adomavicius2018` — "Mind the Gap: Accounting for Measurement Error and Misclassification in Variables Generated via Data Mining" (ISR 2018) — formalizes how ML-generated variable errors bias downstream regression; direct theoretical predecessor to our NLP+causal pipeline

---
