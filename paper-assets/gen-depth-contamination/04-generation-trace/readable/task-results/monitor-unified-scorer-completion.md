# monitor unified scorer completion

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_unified_scorer_completion_20260520T073834_result.json`
- **Structured JSON:** [`14cdd77f39fb2c7b995e.json`](../../sessions/14/14cdd77f39fb2c7b995e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment complete. Here are the results:

```
=== Unified Scorer Multi-Source Results ===
Generators: Qwen2.5-1.5B + Pythia-1.4B + LLaMA-8B
Unified scorer: Qwen2.5-1.5B
Total time: 2082.6s (~35 min)

--- Single-source K* (unified Qwen scorer) ---
  qwen1b5:   K*=2   (0v1: 0.9873, 1v2: 0.6306, 2v3: 0.5579)
  pythia1b4: K*=2   (0v1: 0.9979, 1v2: 0.8806, 2v3: 0.5379)
  llama8b:   K*=1   (0v1: 0.9231, 1v2: 0.6077, 2v3: 0.5312)

--- Multi-source mixed (no generator label) ---
  0v1 AUC: 0.9663 [0.9621, 0.9703]
  1v2 AUC: 0.7105 [0.6979, 0.7235]
  2v3 AUC: 0.5190 [0.5050, 0.5328]
  3v4 AUC: 0.5043 [0.4902, 0.5189]
  4v5 AUC: 0.5201 [0.5062, 0.5342]
  K*(θ=0.60): 2

--- Multi-source mixed (with generator label) ---
  0v1 AUC: 0.9769 [0.9738, 0.9800]
  1v2 AUC: 0.7183 [0.7061, 0.7306]
  2v3 AUC: 0.5165 [0.5025, 0.5304]
  3v4 AUC: 0.5090 [0.4948, 0.5235]
  4v5 AUC: 0.5238 [0.5097, 0.5380]
  K*(θ=0.60): 2

--- vs confounded results (v1) ---
  confounded K* (v1, mixed): 2
  unified K* (no label):     2
  unified K* (with label):   2
  v1 mixed 1v2 AUC: 0.7007 → unified 1v2 AUC: 0.7105
  Conclusion: scorer confound did NOT affect K*
```

**Key findings:**
- K\* = 2 in all multi-source conditions, identical to the confounded v1 result
- The unified scorer actually produces slightly *higher* 1v2 AUC (0.7105 vs 0.7007), indicating the confound was not inflating scores
- LLaMA-8B has K\*=1 when scored by Qwen (cross-family), vs K\*=2 for in-family models, suggesting cross-family scoring is slightly harder
- Adding generator labels barely changes results (K\*=2 either way, AUCs shift <0.01)

---
