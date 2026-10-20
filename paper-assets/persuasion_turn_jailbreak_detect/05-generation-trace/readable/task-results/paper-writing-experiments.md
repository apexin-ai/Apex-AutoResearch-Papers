# paper writing experiments

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260518T040109_result.json`
- **Structured JSON:** [`2391db98e43c54ab4fc9.json`](../../sessions/23/2391db98e43c54ab4fc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiments section written to `paper/experiments.tex`. Summary:

**Structure**: 6 subsections, 4 tables, 2 figure references, ~2500 raw words (renders to ~2800 with table content).

**Tables**:
- Table 1 (`tab:main_results`): Full-width cross-attack results across IID/DD/FITD with K-level breakdown
- Table 2 (`tab:ablation`): Ablation on label granularity (scrambled/binary), temporal modeling (GRU), vanilla baseline
- Table 3 (`tab:perturbation`): Adversarial paraphrasing robustness (DisPeD 0pp, Vanilla -11.8pp, TF-IDF -1.3pp)
- Table 4 (`tab:llm_judge`): GPT-5.5/Qwen3-8B zero-shot with unparseable rates reported as upper bounds

**Key editorial choices**:
- TF-IDF strength (DD=0.944, IID=1.0) acknowledged openly; DisPeD value framed as bridging vanilla gap (+72pp), robustness, and interpretability
- Vanilla DeBERTa's counterintuitive degradation pattern on DD (F1 drops from 0.575→0.284 as K increases) explained via benign embedding accumulation
- Scrambled-label finding positioned as lowering annotation barriers, not as a weakness
- LLM judge unparseable rate (30-47%) reported with upper-bound F1 caveat
- No forbidden AI-style patterns (verified: zero em-dashes, zero -ing phrase endings, zero blacklisted words)

---
