# analysis codellama hires profiling

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_codellama_hires_profiling_20260515T224100_result.json`
- **Structured JSON:** [`279b9145d0686f9c2951.json`](../../sessions/27/279b9145d0686f9c2951.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

---

## CodeLlama-7B Profiling 结果

| 指标 | 值 |
|------|-----|
| concentration (top-5%) | **0.7975** |
| t1/t5 | **0.8131** |
| Shape | **Spike** |
| baseline PPL | 7.698 |
| CV | 18.32 |
| profiling time | 3.7h |

**关键发现**：L1H1 的 delta=22.998，是第二名 L1H18 (2.043) 的 **11.3 倍**。这是极端的单头主导模式——一个 outlier head 吃掉了 top-5 总 delta 的 81%。

## 6 模型对比总表

| Model | Concentration | t1/t5 | Shape | MCKP benefit |
|-------|-------------|-------|-------|-------------|
| Qwen2.5-7B | 0.61 | 0.57 | **Spread** | +27.3% |
| **CodeLlama-7B** | **0.80** | **0.81** | **Spike** | TBD |
| Yi-1.5-9B | 0.71 | 0.90 | Spike | ≈0% |
| Llama-3.1-8B | 0.34 | 0.71 | Spike | +0.2% |
| Mistral-7B | 0.22 | 0.18 | Flat | -0.4% |
| Gemma-2-9B | 0.23 | 0.38 | Flat | -0.3% |

## Diagnostic Rule 准确率

**6/6**（从 5/5 升级）。CodeLlama 是 Spike，预测 MCKP 无效——与 Yi、Llama 同类。Rule 在新数据点上继续成立。

## 对论文的影响

- **Spread 搜索失败**：CodeLlama-7B 不是第二个 Spread 模型，仍然 N=1（只有 Qwen）
- **但增加了 Spike 类别的样本量**：现在 Spike 有 3 个模型 (Yi, Llama, CodeLlama)，Flat 有 2 个 (Mistral, Gemma-2)
- CodeLlama 的 concentration 高 (0.80) 但 t1/t5 也极高 (0.81)，说明高 concentration 不等于 Spread——必须同时看分散度 (t1/t5)，进一步验证了 diagnostic rule 需要两个维度
- 要找第二个 Spread，可能需要尝试 GQA 模型（如 Phi-3-medium、DeepSeek-V2）或不同架构家族

---
