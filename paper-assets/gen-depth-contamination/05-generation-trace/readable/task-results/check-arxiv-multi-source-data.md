# check arxiv multi source data

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_arxiv_multi_source_data_20260520T080200_result.json`
- **Structured JSON:** [`edba109efe676ab0834e.json`](../../sessions/ed/edba109efe676ab0834e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== arXiv Multi-Source Data Availability ===

Qwen2.5-1.5B arXiv:
  Status: AVAILABLE
  Path: /root/autodl-tmp/gen-depth-contamination/data/exp_024_arxiv/
  Depths: [0, 1, 2, 3, 4, 5]
  Doc count per depth: 2200 (uniform)
  Features: 13200 rows (features.csv ready)
  Generator confirmed: exp024_arxiv_domain.sh → MODEL=Qwen/Qwen2.5-1.5B

Pythia-1.4B arXiv:
  Status: AVAILABLE
  Path: /root/autodl-tmp/gen-depth-contamination/data/exp_025_pythia_arxiv/
  Depths: [0, 1, 2, 3, 4, 5]
  Doc count per depth: 2200 (uniform)
  Features: 13200 rows (features.csv ready)
  Generator confirmed: exp025 scripts → Pythia-1.4B

LLaMA-8B arXiv:
  Status: AVAILABLE
  Path: /root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_llama8b/
  Depths: [0, 1, 2, 3, 4, 5]
  Doc count per depth: 2200 (uniform)
  Features: 13200 rows (features.csv ready)

Generation scripts available: YES
  - scripts/download_arxiv_seed.py (seed data)
  - scripts/exp024_arxiv_domain.sh (Qwen pipeline)
  - scripts/run_exp025.sh (Pythia filtering)

Multi-source detection scripts: YES
  - scripts/run_multi_source.py (v1, uses C4 data)
  - scripts/run_multi_source_v2.py
  - scripts/run_multi_source_unified_scorer.py
  - scripts/run_multi_source_vocab_only.py

Existing multi-source results:
  - results/exp_multi_source_detection/
  - results/exp_multi_source_detection_v2/
  - results/exp_multi_source_unified_scorer/

Also available (bonus): arXiv cross-scorer experiments
  - exp_arXiv_qwen1b5_crossscorer (symlinks to exp_024_arxiv data, separate features)
  - exp_arXiv_llama8b_crossscorer
  - exp_arXiv_mistral7b_crossscorer
  - exp_arXiv_qwen7b_crossscorer

Recommendation: READY to run multi-source arXiv experiment. All 3 generators have complete depth 0-5 chains with 2200 docs each and pre-computed features.
```

---
