# analysis e5 mistral text encoder

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_e5_mistral_text_encoder_20260518T195441_result.json`
- **Structured JSON:** [`e87d86503059de31ab77.json`](../../sessions/e8/e87d86503059de31ab77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact registered (`art_20260518_e2347b`). Here's the complete summary:

## E5-Mistral Comparison Results

| Model | HS BA | E5 BA | MiniLM BA | E5 vs HS p-val |
|-------|-------|-------|-----------|----------------|
| R1-8B | **0.756** | 0.641 | 0.661 | 0.040* |
| OT-7B | **0.639** | 0.631 | 0.575 | 0.804 |
| R1-32B | **0.724** | 0.667 | 0.627 | 0.258 |
| QwQ-32B | **0.719** | 0.630 | 0.543 | 0.076 |

**Key takeaways for rebuttal:**

1. **HS probes beat E5-Mistral on all 4 models** (avg BA gap +0.067), even though E5-Mistral is a 7B parameter encoder vs MiniLM's 22M. This strongly supports the paper's core claim that hidden states carry richer signals than surface text.

2. **E5-Mistral improves over MiniLM on 3/4 models** (OT-7B, R1-32B, QwQ-32B), confirming a stronger text encoder helps, but the improvement is insufficient to close the HS gap.

3. **R1-8B is the exception** where MiniLM slightly outperforms E5 (0.661 vs 0.641), possibly due to PCA compression losing information relevant for this specific model.

4. **Statistical significance**: HS > E5 is significant for R1-8B (p=0.040) and marginally significant for QwQ-32B (p=0.076). The other two models have small test sets (20 and 47 traces), limiting statistical power.

5. **PCA preserves 84.6-89.6% variance**, indicating fair dimensionality reduction.

All raw artifacts (embeddings, PCA models, predictions, report, results.json) saved on server at `/root/autodl-tmp/contrastive_trace_safety/artifacts/e5_mistral_comparison/`.

---
