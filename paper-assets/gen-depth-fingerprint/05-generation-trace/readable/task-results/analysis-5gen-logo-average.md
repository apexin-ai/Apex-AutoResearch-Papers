# analysis 5gen logo average

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_5gen-logo-average_20260518T000929_result.json`
- **Structured JSON:** [`bd92f22f80acd0703d72.json`](../../sessions/bd/bd92f22f80acd0703d72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

| Generator (held-out) | Binary F1 | 95% CI |
| --- | --- | --- |
| OLMo-2-1B | 0.6754 | [0.6601, 0.6905] |
| Pythia-1B | 0.7833 | [0.7688, 0.7971] |
| Pythia-2.8B | 0.7149 | [0.6999, 0.7305] |
| Qwen3-0.6B | 0.7439 | [0.7285, 0.7583] |
| Qwen3-1.7B | 0.7499 | [0.7348, 0.7644] |
| **Average** | **0.7335** | **[0.7184, 0.7482]** |
| 8-gen LOGO (ref) | 0.694 | — |
| Cross-model chains (ref) | 0.764 | — |

5-gen LOGO baseline (0.734) 与 cross-model chains (0.764) 的差距为 +0.031，确认跨模型链提供了超越单生成器 LOGO 的额外判别信号。输出已保存至 `results/5gen_logo_average.json` 和本地 artifact。

---
