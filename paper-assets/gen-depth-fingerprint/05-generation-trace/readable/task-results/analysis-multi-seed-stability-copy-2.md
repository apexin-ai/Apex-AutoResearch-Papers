# analysis multi seed stability

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multi-seed-stability_20260515T083651_result.json`
- **Structured JSON:** [`f2718656c1505594b12b.json`](../../sessions/f2/f2718656c1505594b12b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已存在，脚本之前已跑完。

| Seed | 6-gen LOGO F1 |
|------|---------------|
| 42   | 0.7904 |
| 123  | 0.7892 |
| 456  | 0.7876 |
| 789  | 0.7890 |
| 1024 | 0.7887 |
| **Mean ± Std** | **0.7890 ± 0.0009** |

Std = 0.0009，跨 5 个种子的 F1 变化极小（range: 0.7876–0.7904），结果对随机种子高度稳定。

结果已保存在 `/root/gen-depth-fingerprint/results/multi_seed_stability.json`。

---
