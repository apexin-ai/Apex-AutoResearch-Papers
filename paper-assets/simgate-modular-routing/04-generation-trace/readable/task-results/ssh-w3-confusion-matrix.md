# ssh w3 confusion matrix

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_w3-confusion-matrix_20260518T070352_result.json`
- **Structured JSON:** [`3ca76b0dab8b0fea433f.json`](../../sessions/3c/3ca76b0dab8b0fea433f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Report saved to `artifacts/w3_confusion_matrix.md` on both the server (westb-13313) and locally.

**Summary of results (1.7B router, plan-008-v4-seed42, greedy decoding):**

**Overall** (300 steps, 10 episodes):
- Accuracy = 0.64, Balanced Accuracy = 0.58
- Heavy class imbalance: 270 det vs 30 internal

**Death vs Non-Death:**

| Metric | Death (180 steps) | Non-Death (120 steps) |
|---|---|---|
| Accuracy | 0.667 | 0.600 |
| Det Recall | 0.667 | 0.633 |
| Int Recall | n/a (0 true internal) | 0.500 |
| Det Precision | 1.000 | 0.792 |

**Key takeaways:**

1. **Router mispredicts 33% of death-episode steps as "internal"** (60/180). Since death episodes are all-deterministic ground truth, these are false negatives that would route to the LLM agent in a death-prone situation.

2. **No systematic death-specific bias**: The router's deterministic prediction rate is similar across death (66.7%) and non-death (60.0%) episodes, suggesting the router doesn't specifically detect death risk, just pattern-matches on step context.

3. **Internal class is weak everywhere**: Internal precision = 0.14 overall (0.31 on non-death). The router over-predicts "internal", producing many false positives from the deterministic class.

4. **High variance across tasks**: Accuracy ranges from 0.43 (identify-life-stages-2) to 0.83 (grow-fruit). The single internal-preferred task (lifespan-longest-lived-then-shortest-lived) gets 50% internal recall.

---
