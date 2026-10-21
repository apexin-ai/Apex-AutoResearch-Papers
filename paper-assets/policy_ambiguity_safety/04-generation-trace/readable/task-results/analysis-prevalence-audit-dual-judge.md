# analysis prevalence audit dual judge

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prevalence_audit_dual_judge_20260523T061440_result.json`
- **Structured JSON:** [`b02ee61327324bbe2b25.json`](../../sessions/b0/b02ee61327324bbe2b25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All phases complete. Here's the summary:

## Delivered Files (`artifacts/prevalence_audit/`)

| File | Phase | Description |
|------|-------|-------------|
| `clauses.jsonl` | 2 | **407 clauses** extracted from 24 docs (250 airline, 157 retail, 9 companies) |
| `extract_clauses.py` | 2 | Extraction script (already run) |
| `annotate_dual_judge.py` | 3 | Dual-judge annotation pipeline (Claude Sonnet 4.6 + GPT-4.1) |
| `compute_stats.py` | 4 | Cohen's κ, prevalence (raw + doc-weighted), company-level bootstrap CI (N=9, B=10k), type distribution |
| `sample_validation.py` | 5 | Stratified sampling of 50 clauses (balanced by ambig/non-ambig and type) |
| `codebook.md` | 5 | Human annotation instructions with type definitions and decision rules |
| `appendix_draft.tex` | 6 | LaTeX appendix with placeholder tables for all results, selection bias disclosure, LLM caveat |

## To run the pipeline:

```bash
# 1. Set API keys
export ANTHROPIC_API_KEY=[REDACTED] OPENAI_API_KEY=[REDACTED] 2. Install dependencies
pip install anthropic openai numpy

# 3. Run annotations (~407 calls per judge)
python annotate_dual_judge.py

# 4. Compute stats
python compute_stats.py

# 5. Generate human validation sample
python sample_validation.py
```

The annotation script supports `--resume` to continue after interruption and `--judge claude|gpt` to run judges individually.

---
