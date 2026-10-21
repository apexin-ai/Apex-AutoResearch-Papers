# ops fill cuda2 d000 signals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fill-cuda2-d000-signals_20260516T185418_result.json`
- **Structured JSON:** [`3659e8512a0534b96da8.json`](../../sessions/36/3659e8512a0534b96da8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务状态汇报：

**任务 1: Llama d000 GSM8K signals**
- PID: 835978（子进程 835983 在 cuda:2 上，占用 576 MiB）
- 状态：正在运行，S1 embedding 信号计算中，进度 ~10%（680/6250 batches），约 ~40 it/s
- 预计 ~2-3 分钟完成 S1，之后还有 S2/S4

**任务 2: 1.5B-Instruct RRF aggregation**
- PID: 835766（已完成）
- 输出文件: `/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/exposure_aggregated.json`
- 处理了 mmlu/gsm8k/arc_challenge 三个 benchmark

注意：首次启动 signals 时因缺少 `network_turbo` 导致 HuggingFace 连接超时，已 kill 并带代理重启成功。

---
