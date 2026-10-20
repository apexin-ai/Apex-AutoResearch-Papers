# analysis qwen family out

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen-family-out_20260515T094845_result.json`
- **Structured JSON:** [`4a187f142107cbb09255.json`](../../sessions/4a/4a187f142107cbb09255.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| Family held-out | macro-F1 | 训练生成器 | 测试生成器 |
|---|---|---|---|
| **Qwen** | **0.7544** | pythia-1b, pythia-2.8b, olmo-2-1b | qwen3-0.6b (0.8033), qwen3-1.7b (0.7885), qwen3-8b (0.6730) |
| Pythia | 0.7717 | olmo-2-1b, qwen3-0.6b, qwen3-1.7b, qwen3-8b | pythia-1b (0.7932), pythia-2.8b (0.7506) |
| OLMo | 0.7616 | pythia-1b, pythia-2.8b, qwen3-0.6b, qwen3-1.7b, qwen3-8b | olmo-2-1b (0.7616) |

Pythia held-out 0.772 和 OLMo held-out 0.762 与预期值（0.772 / 0.761）吻合。

Qwen family held-out macro-F1 = **0.754**，三个家族中最低，主要被 qwen3-8b (0.673) 拖低。

---
