# analysis bias ratio cross condition

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bias-ratio-cross-condition_20260520T111526_result.json`
- **Structured JSON:** [`06b619dbbbef8ae08cd3.json`](../../sessions/06/06b619dbbbef8ae08cd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个模型的数据已全部计算完成。汇总结果：

## Confirmation Bias 跨模型分析

### 方法 1: Raw Constraint Counts（原始约束计数）

| Model | N | SICA Errors | Bias Ratio | Error Constraint % |
|-------|---|-------------|------------|-------------------|
| Mistral-7B | 204 | 83 | **4.97x** | 83.3% |
| Qwen2.5-14B | 204 | 52 | **3.93x** | 79.7% |
| LLaMA-3.1-8B | 204 | 78 | **2.88x**† | 74.3%† |

†LLaMA raw counts 仅基于 traces 0-3（4/12 traces），样本偏少。

### 方法 2: MaxSAT Weights（sica_scores，去重加权后）

| Model | N | SICA Errors | Bias Ratio | Error Constraint % | SICA Acc |
|-------|---|-------------|------------|-------------------|----------|
| Mistral-7B | 204 | 83 | **4.24x** | 80.9% | 59.3% |
| Qwen2.5-14B | 204 | 52 | **3.69x** | 78.7% | 74.5% |
| LLaMA-3.1-8B | 204 | 78 | **2.66x** | 72.7% | 61.8% |

### 关键发现

1. **所有三个模型均存在显著 confirmation bias**（bias ratio >> 1x），验证了跨模型普遍性
2. Raw counts 方法下：Mistral 4.97x → Qwen 3.93x → LLaMA 2.88x
3. **SICA 判错时，70-83% 的约束指向错误答案**，一致跨模型
4. SICA follows SC rate: Mistral 94.0%, Qwen 90.4%, LLaMA 78.2% — 模型越弱 SICA 越难纠偏

原始 4.97x（Mistral raw counts）已完全复现。Qwen/LLaMA 的 bias ratio 略低，但仍为 2.66-3.93x，足以支撑"跨模型普遍性"的 claim。结果已保存到 `results/confirmation_bias/crossmodel_results.json`。

---
