# analysis multi seed stability

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multi-seed-stability_20260515T083406_result.json`
- **Structured JSON:** [`34665c3c38eb4ea19e4c.json`](../../sessions/34/34665c3c38eb4ea19e4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果如下：

| Seed | 6-gen LOGO F1 |
|------|---------------|
| 42   | 0.7904 |
| 123  | 0.7892 |
| 456  | 0.7876 |
| 789  | 0.7890 |
| 1024 | 0.7887 |
| **Mean±Std** | **0.7890 ± 0.0009** |

5 个种子的 macro-F1 范围 [0.7876, 0.7904]，标准差仅 0.0009，结果高度稳定，不依赖随机种子。JSON 已保存至 `/root/gen-depth-fingerprint/results/multi_seed_stability.json`。

---
