# analysis rssm fidelity

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rssm-fidelity_20260524T141744_result.json`
- **Structured JSON:** [`6b5f701158cc14183438.json`](../../sessions/6b/6b5f701158cc14183438.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**Collapsed CIVO 模型的 reward 预测在 dt>1 时严重退化（3.11x gap），而 observation 预测反而更好（1.33x gap < baseline 1.46x）。** 这直接支持 C2 (delusional critic) 假说：世界模型在长时间跨度的 reward 预测不可靠，但 critic 仍信任这些预测，导致 value 高估 → gate 策略 collapse 到总选 dt>1。

关键数据：
| 模型 | Obs MSE gap | Reward MAE gap |
|------|-------------|----------------|
| Baseline | 1.46x | 1.30x |
| Collapsed CIVO | 1.33x | **3.11x** |
| Healthy Frozen | 1.34x | 1.96x |

报告已写入 `artifacts/rssm_fidelity_analysis.md` 并注册。

---
