# research ashwin dataset

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ashwin-dataset_20260520T212716_result.json`
- **Structured JSON:** [`0160fd3a7c742623ebc0.json`](../../sessions/01/0160fd3a7c742623ebc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written to `/home/ubuntu/ec_hte_llm_annotation/results/dataset_survey.md`.

**Key findings:**

1. **Ashwin dataset**: Not publicly available. Anonymised version available upon request from Julian Ashwin (julian.ashwin@maastrichtuniversity.nl). IRB/privacy restrictions on Rohingya refugee interview data.

2. **Top 3 alternative datasets** (all fully public):
   - **UC Berkeley Measuring Hate Speech** — 50K comments, 11K annotators, 8 target + 6 annotator demographic dimensions, continuous Rasch-scaled labels. Best fit for EC-HTE.
   - **Social Bias Frames (SBIC)** — 150K+ annotations, 1000+ target groups, annotator politics/race/age metadata.
   - **POPQUORN** — 45K annotations from 1,484 US-representative annotators (sex/age/race), 4 NLP tasks. Cleanest experimental design for studying demographic effects.

**Recommended strategy**: Use UC Berkeley Measuring Hate Speech as primary dataset, POPQUORN for cross-task validation, and email Ashwin in parallel for the original data.

---
