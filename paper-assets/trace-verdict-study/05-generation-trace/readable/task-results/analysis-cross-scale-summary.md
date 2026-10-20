# analysis cross scale summary

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_scale_summary_20260516T142615_result.json`
- **Structured JSON:** [`b8d3d4900de4b65217e4.json`](../../sessions/b8/b8d3d4900de4b65217e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。核心发现：

**6 张表**：Main Results (4 models)、Seed Robustness、DebugBench、Regex Baselines、Length Ablation、Calibration。

**关键结论**：
- **exception_only 跨模型一致性强**：Qwen-7B/1.5B/DeepSeek 均达 99.3%+，vs no_trace 提升 +24.7 到 +32.5pp
- **exception_only >= VOTA**：所有模型上 exception_only 持平或优于 VOTA（Qwen-7B 上 p=0.01）
- **Scale 对强信号无关**：1.5B 在 exception_only/VOTA 上与 7B 持平，仅在 no_trace/full_trace 上落后 5-8pp
- **Signal-rich vs signal-poor 分界清晰**：含异常/断言信息的条件均值 99.7%，仅含结构信息的条件均值 82.2%，gap=17.5pp
- **Seed 鲁棒性**：exception_only (Qwen-7B) 三 seed 完全一致 (99.83%)；ae_only σ=0.49%；DeepSeek seed123 是 outlier (91.1% vs 99.3%)
- **待补数据**：CodeLlama-13B exception_only 和 VOTA 仍在 RUNNING

---
