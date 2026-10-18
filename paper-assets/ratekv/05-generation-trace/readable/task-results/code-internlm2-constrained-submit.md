# code internlm2 constrained submit

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_internlm2_constrained_submit_20260516T025537_result.json`
- **Structured JSON:** [`233c5f437462d5e2b020.json`](../../sessions/23/233c5f437462d5e2b020.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

- **脚本** `run_internlm2_constrained_mckp.py` 已创建并 scp 到 `westd-37397:/root/ratekv/`
- **实验注册** `internlm2_constrained_mckp`，parent=`internlm2_7b_hires_profiling`，状态 RUNNING
- **任务已提交** 在 tmux session `internlm2_constrained_mckp`，cuda:0 运行中，模型已加载完成正在评估 WikiText-2

日志初始输出显示模型 checkpoint 加载成功（2/2 shards），数据集命中缓存。预计 ~30min 完成，结果输出到 `artifacts/internlm2_constrained_mckp_results.json`。

---
