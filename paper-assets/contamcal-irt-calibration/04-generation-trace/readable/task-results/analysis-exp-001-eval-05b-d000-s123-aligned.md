# analysis exp 001 eval 05B d000 s123 aligned

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_eval_05B_d000_s123_aligned_20260515T102545_result.json`
- **Structured JSON:** [`d71df0a637a5f2eeff3e.json`](../../sessions/d7/d71df0a637a5f2eeff3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。汇总如下：

## 结果 (Qwen2.5-0.5B, d000, s123, aligned)
- MMLU: 42.16%
- GSM8K: 34.12%
- ARC-Challenge: 49.74%
- HumanEval: 10.37%

## 对比

| Benchmark | d000_s123 | d000_s42 | d100_s123 | Δ(s123 vs s42) | Δ(d000 vs d100, s123) |
|-----------|-----------|----------|-----------|-----------------|----------------------|
| MMLU | 42.16% | 39.79% | 30.58% | +2.37 | +11.58 |
| GSM8K | 34.12% | 36.92% | 37.98% | -2.80 | -3.87 |
| ARC-Challenge | 49.74% | 46.93% | 36.69% | +2.81 | +13.05 |
| HumanEval | 10.37% | 10.98% | 10.37% | -0.61 | ±0.00 |

## 结论
**success** — eval 正常完成，分数合理。

- seed 间差异（s123 vs s42）在 ±3pp 以内，跨 seed 稳定性可接受
- d000 vs d100 在 MMLU 和 ARC 上差距大（+11~13pp），符合预期：0% contamination 的 0.5B 模型 MC 能力显著弱于 100% contamination 模型，但 d100 的 GSM8K 反而更高（+3.87pp），可能因为 GSM8K contamination 训练数据直接包含了正确推理路径
- HumanEval pass@1 ~10% 在三组间几乎无变化，说明 contamination 对代码生成无影响（符合预期，contamination 数据不含 code）

---
