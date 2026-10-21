# paper writing related work

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260517T170247_result.json`
- **Structured JSON:** [`28c349e652f062ecde5d.json`](../../sessions/28/28c349e652f062ecde5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All clean. The `ing` matches are nouns (decoding, training, following), not participial phrase endings.

Written to `docs/paper/sections/related_work.tex`. Three thematic paragraphs (~680 words total):
- **P1** (~300w): Encoder DocRE (DocRED, ATLOP, KD-DocRE) → evidence in encoders (SAIS, DREEAM, EIDER as classification) → LLM DocRE (GenRES, LMRC, DocKS-RAG) → key distinction: classification evidence regularizes; generative evidence costs capacity
- **P2** (~220w): GRPO + structured IE extensions (E-GRPO, R1-RE) → DPO → RL forgetting debate (our decoupling is intra-task trade-off, not inter-task forgetting) → reward overoptimization (Gao, Moskovitz) → QLoRA amplification
- **P3** (~160w): STaR → RSFT as single-round variant → honest positioning (novelty is CED/NLI filter for DocRE, not framework) → structural advantage of discrete selection over gradient optimization

17 unique citations, 0 dashes, 0 -ing phrase endings.

---
