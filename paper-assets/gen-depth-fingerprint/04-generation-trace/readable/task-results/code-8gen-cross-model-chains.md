# code 8gen cross model chains

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8gen-cross-model-chains_20260516T170907_result.json`
- **Structured JSON:** [`c77dc188226c2918551c.json`](../../sessions/c7/c77dc188226c2918551c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `results/8gen_cross_model_chains.json`。

**关键发现：**

| 指标 | 5-gen 混合链 | 8-gen Pooled CV | 8-gen LOGO |
|------|-------------|-----------------|------------|
| 3-class F1 | 0.809 | **0.814** (+0.005) | 0.768 (−0.041) |
| Binary F1 | 0.764 | 0.744 (−0.020) | **0.776** (+0.012) |

- **Pooled CV**（类比混合链评估）：8 gen 扩展后 3-class 略有提升，说明更多生成器的多样性训练数据有益
- **LOGO**（真正的跨模型泛化）：3-class 下降 4 点，主要被 mistral-7b（0.616）和 qwen3-8b（0.701）拖低——这两个模型在规模/架构上与其余 6 个差异最大
- **说明**：真正的 8-gen 混合链数据未生成（需要频繁加载 7B/8B 模型，不可行），结果基于单模型链数据

---
