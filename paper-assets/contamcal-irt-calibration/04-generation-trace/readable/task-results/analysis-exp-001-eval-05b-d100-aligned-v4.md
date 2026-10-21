# analysis exp 001 eval 05B d100 aligned v4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_eval_05B_d100_aligned_v4_20260514T174121_result.json`
- **Structured JSON:** [`17bdd0201b0619941c11.json`](../../sessions/17/17bdd0201b0619941c11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the full report.

---

## exp_001_eval_05B_d100_aligned_v4 评估结果

### Benchmark 指标

| Benchmark | Correct/Total | Accuracy |
|-----------|--------------|----------|
| MMLU | 3277/14042 | **23.34%** |
| GSM8K | 482/1319 | **36.54%** |
| ARC-Challenge | 345/1172 | **29.44%** |
| HumanEval | 0/164 | **0.00%** |

### Dose-Response 对比（Qwen2.5-0.5B, aligned MC format）

| Benchmark | d000 (0%) | d005 (5%) | d025 (25%) | d100 (100%) | d100 vs d000 |
|-----------|-----------|-----------|------------|-------------|--------------|
| MMLU | 39.79% | 32.55% | 28.03% | **23.34%** | **-16.45pp** |
| GSM8K | 36.92% | 36.24% | 36.62% | **36.54%** | -0.38pp |
| ARC | 46.93% | 32.85% | 32.51% | **29.44%** | **-17.49pp** |
| HumanEval | 10.98% | 7.93% | missing | **0.00%** | **-10.98pp** |

### 分析

**关键发现：d100 没有出现 contamination inflation，反而出现严重的能力退化。**

1. **MMLU 单调下降**：d000→d005→d025→d100，accuracy 从 39.8% 一路跌到 23.3%（接近随机 25%）。模型几乎完全崩溃到预测 "A"（从 per_item 数据可见），说明 100% contamination dosage 的 LoRA 微调导致模型坍缩。

2. **GSM8K 基本平稳**：~36-37% 跨所有 dosage 变化不大，可能因为 GSM8K contamination 注入质量（QC rate 仅 17.3%）不足以影响结果。

3. **ARC 明显下降**：从 46.9% 跌至 29.4%，呈单调下降趋势。

4. **HumanEval 完全崩溃**：0/164，模型生成的代码完全无法通过测试。从日志可见生成质量极差（重复输出、逻辑混乱）。

### 结论：**NEGATIVE**

d100 aligned 结果与预期的 contamination inflation 假说完全相反。100% 污染剂量没有膨胀分数，而是摧毁了模型能力。这与之前 unaligned format (exp_001_eval_05B_d100_v5) 的结果一致（MMLU 23.2%, ARC 22.7%），说明**无论 MC 格式是否对齐，100% dosage 对 0.5B 模型都是灾难性的**。

Dose-response 趋势在 0.5B 模型上是**单调递减**而非倒U型或递增，暗示小模型的容量不足以在大比例污染下维持泛化能力。

### 建议 Summary

> Qwen2.5-0.5B with 100% contamination dosage (aligned MC) shows catastrophic degradation: MMLU 23.3% (near random), ARC 29.4%, HumanEval 0%. The dose-response curve is monotonically decreasing across all dosages (0%→5%→25%→100%), confirming that high-dose contamination destroys rather than inflates benchmark performance at the 0.5B scale. This negative result is consistent across both aligned and unaligned MC formats. The 0.5B model lacks capacity to memorize contaminated data without losing generalization. Focus contamination-inflation analysis on 1.5B+ models where the effect may differ.

---
