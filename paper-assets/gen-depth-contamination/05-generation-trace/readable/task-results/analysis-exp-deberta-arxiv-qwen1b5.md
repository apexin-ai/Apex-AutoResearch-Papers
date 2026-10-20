# analysis exp deberta arxiv qwen1b5

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_deberta_arxiv_qwen1b5_20260520T034706_result.json`
- **Structured JSON:** [`c4569d6e7add54d902df.json`](../../sessions/c4/c4569d6e7add54d902df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
RESULT:
- K*: 4 (NOT 3 as hypothesized)
- conclusion: NEGATIVE — DeBERTa K*=4 ≠ OBD K*=3, representation-independence claim fails for arXiv
- metrics:
  - 0v1: AUC=0.9997 [0.9992, 1.0000] (OBD=0.9948, Δ+0.005)
  - 1v2: AUC=0.9214 [0.9143, 0.9285] (OBD=0.8581, Δ+0.063)
  - 2v3: AUC=0.7446 [0.7333, 0.7559] (OBD=0.6436, Δ+0.101)
  - 3v4: AUC=0.6238 [0.6127, 0.6349] (OBD=0.5440, Δ+0.080) ← pivotal pair
  - 4v5: AUC=0.5771 [0.5659, 0.5882] (OBD=0.5299, Δ+0.047)
- checkpoint_path: N/A (OOF predictions only, no model saved)
- log_path: ~/runs/gen-depth-contamination/exp_deberta_arxiv_qwen1b5.log
```

关键发现：3v4 pair 是分歧点。DeBERTa 的 CI_lower=0.6127 仅比阈值 0.6 高 0.0127，属于 borderline。建议做 θ 敏感性分析（θ=0.62 即可恢复 K*=3），或将 arXiv 作为 "approximate representation-independence" 的 nuance 讨论。详细分析已写入 `artifacts/analysis_exp_deberta_arxiv_qwen1b5.md`。

---
