# code e2 difficulty modeltype interaction

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e2_difficulty_modeltype_interaction_20260523T012814_result.json`
- **Structured JSON:** [`9535506adf5ea2182ad4.json`](../../sessions/95/9535506adf5ea2182ad4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs are generated. Here's a summary:

**Part 1 — Logistic Regression** (N=8,585 item×type observations):

| Variable | β | OR | p |
|---|---|---|---|
| model_type (instruct) | 1.444 | 4.24 | 10⁻²²⁵ |
| difficulty_z | -1.918 | 0.15 | 10⁻²⁹⁸ |
| **difficulty × model_type** | **1.559** | **4.75** | **10⁻¹⁸⁸** |

The model_type effect survives after controlling for difficulty — the direction reversal is not a difficulty confound. The significant interaction reveals that difficulty *amplifies* the divergence: at easy items both types tend focal-favoring; at hard items, base strongly favors ref while instruct stays near 50/50.

**Part 2 — Within-Family Paired Analysis** (9 families, base=ref, instruct=foc):

Heterogeneous across families — mean instruct-favoring = 50.6% (t=0.19, p=0.85, not different from 50%). llama-3 shows 67.5% instruct-favoring; zephyr/mistral show base-favoring. This indicates the pooled direction reversal reflects differential family composition rather than a universal within-family mechanism.

**McNemar on paired items** (2,053 items C in both analyses): 98% concordance in direction. The aggregate reversal arises from *which items* reach C threshold in each analysis, not from individual items switching direction.

Outputs saved to `artifacts/difficulty_modeltype_interaction/`.

---
