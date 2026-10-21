# code r6 auroc best layer comparison

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r6_auroc_best_layer_comparison_20260518T024925_result.json`
- **Structured JSON:** [`5922b1f2848be0fe74bd.json`](../../sessions/59/5922b1f2848be0fe74bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here are the results:

| Model   | AUROC-best Layer | HS precision | HS bal_acc | Text precision | Text bal_acc |
|---------|-----------------|-------------|-----------|---------------|-------------|
| R1-8B   | L13             | 0.6781      | 0.7715    | 0.4481        | 0.6790      |
| OT-7B   | L1              | 0.3689      | 0.6773    | 0.2387        | 0.5991      |
| QwQ-32B | L32             | 0.5606      | 0.6923    | 0.3853        | 0.5379      |
| R1-32B  | L31             | 0.5466      | 0.6996    | 0.4843        | 0.6051      |

**HS advantage over text:**

| Model   | precision gap | bal_acc gap |
|---------|-------------|-----------|
| R1-8B   | +0.230      | +0.093    |
| OT-7B   | +0.130      | +0.078    |
| QwQ-32B | +0.175      | +0.154    |
| R1-32B  | +0.062      | +0.095    |

**Method notes:**
- HS: from `layer_metric_ablation.json`, static LogisticRegression per step
- Text: static LogisticRegression on all-MiniLM-L6-v2 sentence embeddings, same train/test split (60/20/20, seed=42), same LR config (C=1.0, class_weight=balanced, lbfgs, max_iter=2000)

HS probe consistently outperforms text on both metrics across all 4 models, with precision gap ranging from +6.2pp (R1-32B) to +23.0pp (R1-8B).

---
