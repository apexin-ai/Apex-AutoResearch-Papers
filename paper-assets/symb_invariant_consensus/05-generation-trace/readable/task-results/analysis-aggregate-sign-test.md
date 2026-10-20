# analysis aggregate sign test

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_aggregate-sign-test_20260522T012901_result.json`
- **Structured JSON:** [`17a48e9491fefaabe65e.json`](../../sessions/17/17a48e9491fefaabe65e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。汇总结果：

## 全条件 Δ 表

| Condition | N | SC% | SICA% | Δpp | Dir |
|---|---|---|---|---|---|
| gpt-4o self / FOLIO-204 | 204 | 76.96 | 75.00 | -1.96 | - |
| Mistral-7B self / FOLIO-204 | 204 | 54.41 | 59.31 | +4.90 | + |
| Mistral-7B seed123 / FOLIO-204 | 204 | 53.92 | 57.35 | +3.43 | + |
| Mistral-7B seed456 / FOLIO-204 | 204 | 56.37 | 55.88 | -0.49 | - |
| LLaMA-8B self / FOLIO-204 | 204 | 66.18 | 61.76 | -4.41 | - |
| Qwen2.5-14B self / FOLIO-204 | 204 | 77.45 | 75.49 | -1.96 | - |
| Qwen3 self / FOLIO-154 | 154 | 80.52 | 82.47 | +1.95 | + |
| Qwen2.5-14B / PW-600 | 600 | 73.50 | 71.50 | -2.00 | - |
| Qwen3-14B nonthink / PW-600 | 600 | 85.00 | 85.67 | +0.67 | + |
| LLaMA-8B / PW-600 | 600 | 70.00 | 64.83 | -5.17 | - |
| Qwen2.5-14B / LogiQA-200 | 200 | 78.50 | 78.00 | -0.50 | - |
| Mistral-7B / LogiQA-200 | 200 | 51.00 | 51.50 | +0.50 | + |
| LLaMA-8B / LogiQA-200 | 200 | 61.00 | 58.50 | -2.50 | - |
| LLaMA-8B v2 / LogiQA-200 | 200 | 59.50 | 58.50 | -1.00 | - |
| Mistral ICL-oracle / FOLIO-199 | 199 | 57.79 | 54.27 | -3.52 | - |
| gpt-4.1→Mistral / FOLIO-204 | 204 | 82.84 | 81.37 | -1.47 | - |
| gpt-5.5→Mistral / FOLIO-204 | 204 | 84.31 | 84.80 | +0.49 | + |
| Gemini-2.5→Mistral / FOLIO-95 | 95 | 87.37 | 86.32 | -1.05 | - |
| R1-Distill→Mistral / FOLIO-204 | 204 | 74.51 | 76.96 | +2.45 | + |
| Mistral→Mistral / PW-2x2 | 204 | 40.20 | 34.31 | -5.88 | - |
| Mistral→Qwen3 / PW-2x2 | 204 | 40.20 | 79.90 | +39.71 | + |
| Qwen3→Mistral / PW-2x2 | 204 | 86.76 | 37.75 | -49.02 | - |
| Qwen3→Qwen3 / PW-2x2 | 204 | 86.76 | 79.90 | -6.86 | - |

**排除退化条件** (Δ=0): o3→Mistral, R1-Qwen3-8B self, Qwen3/LogiQA, Qwen2.5-72B partial

## Sign Test 结果

| 分析范围 | n | k+ | k- | p-value | Mean Δ | Median Δ |
|---|---|---|---|---|---|---|
| 全部非退化 | 23 | 8 | 15 | 0.2100 | -1.46pp | -1.05pp |
| 排除极端 (\|Δ\|>10pp) | 21 | 7 | 14 | 0.1892 | -1.16pp | -1.05pp |
| 仅 self-extraction | 15 | 5 | 10 | 0.3018 | -0.80pp | -1.00pp |

## 结论

**SICA 相对 SC 无显著系统性方向偏差**（所有 p > 0.05）。负方向略多（约 2:1），mean Δ 约 -1pp，但统计上不显著。SICA 既不系统性优于也不系统性劣于 SC——准确率差异主要由具体实验条件（模型能力、数据集、提取器匹配度）驱动，而非方法本身的固有偏差。

结果已保存至服务器 `/root/symb_invariant_consensus/results/aggregate_sign_test/sign_test_results.json`。

---
