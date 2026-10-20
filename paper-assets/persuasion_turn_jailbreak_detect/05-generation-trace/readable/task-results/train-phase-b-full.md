# train phase b full

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_phase-b-full_20260517T163400_result.json`
- **Structured JSON:** [`d8325b03cc6a78dfc193.json`](../../sessions/d8/d8325b03cc6a78dfc193.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase B pipeline complete. Final results summary:

```
=== Phase B Full Results (N=480, test=72) ===

Stage 1 (DeBERTa Multi-task, best epoch 3):
  Persuasion Accuracy: 0.7963
  Intent Accuracy:     0.9514

Early Detection (F1 scores):
K      Treatment (FT+GRU)  Baseline (vanilla+GRU)  TF-IDF+LR
2      0.987               0.879                   1.000
3      0.987               0.928                   1.000
5      1.000               0.958                   1.000
full   1.000               0.987                   1.000
```

**Key findings**:
1. **Treatment (DeBERTa-FT + GRU)** achieves near-perfect detection even at K=2 (F1=0.987, FPR@95TPR=0.0), reaching perfect at K=5.
2. **Baseline (vanilla DeBERTa + GRU)** lags behind, especially at low K values (F1=0.879 at K=2), confirming that persuasion-grounded fine-tuning provides meaningful signal for early detection.
3. **TF-IDF + LR** achieves perfect scores across all K values, which is concerning - likely due to lexical artifacts in the synthetic data (jailbreak conversations contain distinctly different vocabulary/topics from benign ones). This suggests the current dataset may have distributional shortcuts that a simple text classifier can exploit.

The treatment vs baseline comparison (the core claim of DisPeD) shows a clear gap at early turns (K=2: +0.108 F1, K=3: +0.059 F1), validating that persuasion-aware embeddings enable earlier detection. The TF-IDF ceiling effect indicates we'll need harder benign examples or adversarial evaluation for a publishable result.

---
