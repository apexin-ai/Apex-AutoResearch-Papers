# diagnose exp012 r4 result

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp012_r4_result_20260515T164114_result.json`
- **Structured JSON:** [`2d0e910b89036f373d64.json`](../../sessions/2d/2d0e910b89036f373d64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程仍在运行，未退出。**

实际状态：
- **PID 296799**（python3 src/run_experiment.py --mode exp2）正在运行，CPU 占用 93.9%
- tmux session `exp012_llama_fewnerd_r4` 活跃
- 当前正在处理 `count_12_random_4` 批次（12 types），已完成 125+ 个 batch
- 启动时间 00:24，运行约 18 分钟，每个 batch 6-9 秒
- 模型：`/root/autodl-tmp/models/llama-3.1-8b-instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct`，BF16 via vLLM
- 输出目录：`artifacts/exp012/`

用户提到的 PID 294443 未出现在进程列表中——wrapper 进程 PID 为 294428/294432/294433，实际 python 进程为 296799。

`/root/schema-dag-extraction/logs/exp012_llama_8b.log` 中的 `RuntimeError: Engine core initialization failed` 是**之前的失败尝试**，不是当前运行。

**结论：不做 registry 更新和 cron 删除。实验仍在进行中，需要等待完成后再诊断。**

---
