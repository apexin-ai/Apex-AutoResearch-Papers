# analysis multi seed stability

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multi-seed-stability_20260515T081408_result.json`
- **Structured JSON:** [`0ccffcc653140f6ede65.json`](../../sessions/0c/0ccffcc653140f6ede65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果如下：

| Seed | 6-gen LOGO F1 |
|------|---------------|
| 42   | 0.7894 |
| 123  | 0.7915 |
| 456  | 0.7922 |
| 789  | 0.7904 |
| 1024 | 0.7886 |
| **Mean±Std** | **0.7904 ± 0.0013** |

std = 0.0013，结果对种子选择几乎不敏感。已保存至 `/root/gen-depth-fingerprint/results/multi_seed_stability.json`。

---
