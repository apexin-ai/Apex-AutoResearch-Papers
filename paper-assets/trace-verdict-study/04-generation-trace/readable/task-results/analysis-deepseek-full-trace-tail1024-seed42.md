# analysis deepseek full trace tail1024 seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_full_trace_tail1024_seed42_20260517T231440_result.json`
- **Structured JSON:** [`f93cd2a2bd57bae481f6.json`](../../sessions/f9/f93cd2a2bd57bae481f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已写入 `artifacts/deepseek_full_trace_tail1024_seed42/report/analysis.md`。

**核心结论**：

- **Accuracy**: 96.47% [95.4%, 97.5%]
- **vs tail-512 (93.9%)**: 高出 2.57pp，CI 不重叠，差异显著
- **Hypothesis REJECTED**: DeepSeek 的 truncation 曲线是单调递增的 (76.4% → 93.9% → 96.47% → ~97.0%)，non-monotonicity 未跨架构确认
- DeepSeek tail-1024 与 Qwen-7B tail-1024 精确相同 (96.47%)，暗示 1024-token 可能存在架构无关的性能天花板

Eval loss 从 epoch 2 (0.145) 升至 epoch 3 (0.169)，有轻微过拟合迹象，但最终 accuracy 仍然很高。

---
