# code llama budget sweep k4

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-budget-sweep-k4_20260521T210604_result.json`
- **Structured JSON:** [`9c6b4cef827091087dbb.json`](../../sessions/9c/9c6b4cef827091087dbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。关键发现：

**|Bias|**: EC-HTE 在所有 budget 下都优于 Naive（crossover 在最小的 n_expert=100 就已存在）。

**RMSE**: EC-HTE 在测试范围内始终不优于 Naive。根因清晰可见于 bias-variance 分解：
- Naive 的方差恒定在 0.008（不依赖 expert budget）
- EC-HTE 的方差从 n=100 的 0.176 降至 n=2000 的 0.024，但即使在 n=2000 仍略高于 Naive 的 0.016 MSE

**结论**: 在 Llama K=4 真实 CM 下（delta_pi ≈ 0.137，中等异质性），方差膨胀始终主导 bias reduction。RMSE crossover 需要 n_expert > 2000，或更大的 CM 异质性才能实现。

输出文件：
- `budget_sweep_k4_results.csv` — 8000 行原始结果
- `budget_sweep_k4_analysis.md` — 汇总表 + crossover 分析 + bias-variance 分解

---
