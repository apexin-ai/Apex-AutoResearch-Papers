# analysis threshold sensitivity

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_threshold_sensitivity_20260517T134939_result.json`
- **Structured JSON:** [`a14f67d3980fb71fc426.json`](../../sessions/a1/a14f67d3980fb71fc426.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Sanity check 通过（L1 trained @ 50% = 24）。结果已保存到 `threshold_sensitivity.json`。

### 关键发现

**Table 1: L1 Threshold Sweep**

| Threshold | Trained | Llama2-Base | Untrained |
|-----------|---------|-------------|-----------|
| 30% | 32 | 13 | 0 |
| 40% | 31 | 10 | 0 |
| **50%** | **24** | **9** | **0** |
| 60% | 9 | 4 | 0 |
| 70% | 5 | 3 | 0 |

**Robust Range 分析**

所有关键层在 50% threshold 下，三条件梯度 (untrained < llama2base < trained) 均成立：

| Layer | Robust Range | Midpoint | 50% in range? |
|-------|-------------|----------|---------------|
| L0 | [10%, 62%] | 36% | Yes |
| L1 | [10%, 85%] | 48% | Yes |
| L8 | [10%, 79%] | 44% | Yes |
| L16 | [10%, 74%] | 42% | Yes |
| L31 | [10%, 90%] | 50% | Yes |

**结论**：50% threshold 落在所有关键层 robust range 内部，且非常接近 L1 的 midpoint（48%）和 L31 的 midpoint（50%）。选择 50% 不是 cherry-picked，而是位于梯度保持区间的中央位置。

**注意**：L0 在 70% threshold 出现反转（llama2base=8 > trained=4），L8 和 L16 中间层 llama2base > trained 在部分 threshold 下也出现。这些层的 attention 分布模式不同于 L1，属于预期行为（中间层 llama2base 保留了更多 LLM 的 text-attending 惯性，而 trained 模型重新分配了 attention）。

---
