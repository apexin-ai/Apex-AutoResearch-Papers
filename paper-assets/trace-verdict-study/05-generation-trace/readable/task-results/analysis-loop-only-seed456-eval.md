# analysis loop only seed456 eval

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_loop_only_seed456_eval_20260516T134431_result.json`
- **Structured JSON:** [`c94ab81b57ecf2ad8776.json`](../../sessions/c9/c94ab81b57ecf2ad8776.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**loop_only_seed456 评估指标：**
- Accuracy: **86.6%**（majority baseline 71.5%，lift +15.1pp）
- Pass F1: 0.905 | Fail F1: 0.773
- n = 1190

**GPU 状态：**
- GPU 0: 88263/97887 MiB (97% util) — 被模型下载/加载占用
- GPU 1: 32851/97887 MiB (100% util) — 正在跑 `codellama13b_no_trace_seed42` 训练

**活跃训练：** `codellama13b_no_trace_seed42`（GPU 1，train_sft.py，刚启动约 4 分钟）

结果已保存到 `artifacts/loop_only_seed456_eval.md`。

---
