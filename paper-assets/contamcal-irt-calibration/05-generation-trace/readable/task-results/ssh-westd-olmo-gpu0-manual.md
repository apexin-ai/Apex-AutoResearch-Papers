# ssh westd olmo gpu0 manual

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-olmo-gpu0-manual_20260519T120728_result.json`
- **Structured JSON:** [`790894c2db17901a5a01.json`](../../sessions/79/790894c2db17901a5a01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 上已经在跑 OLMo-2 eval。** 

进程详情：
- **PID**: 164849
- **命令**: `evaluate.py --model-path OLMo-2-1124-7B --adapter-path OLMo-2-7B_d000_s42 --benchmarks mmlu arc_challenge --mc-format aligned --output-dir eval_results_v2/olmo2_d000`

这正是你要启动的 OLMo-2 eval 任务。看起来 tmux monitor 或之前的尝试已经成功启动了。根据 **C001**（目标 GPU 已有同类进程则不提交），不需要再次启动。

需要我检查该进程的运行进度/日志吗？

---
