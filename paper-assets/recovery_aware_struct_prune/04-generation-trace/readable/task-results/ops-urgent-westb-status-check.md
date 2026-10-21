# ops urgent westb status check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_westb_status_check_20260517T171123_result.json`
- **Structured JSON:** [`77b9a6dc2112fba298f9.json`](../../sessions/77/77b9a6dc2112fba298f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westb-23072 状态报告

### GPU 状态

| GPU | 进程 | PID | 显存占用 | GPU Util | 温度 | 功耗 |
|-----|------|-----|---------|----------|------|------|
| cuda:0 | grpo_cka_only_20 | 725232 (bash: 725227) | 73540 / 97887 MiB | 100% | 81°C | 600W/600W |
| cuda:1 | grpo_random_20 | 719684 (bash: 719679) | 73156 / 97887 MiB | 100% | 83°C | 600W/600W |

所有 4 个 PID 均存活，状态正常（python 进程 Rl = running）。

### 实验进度

| 实验 | 当前 step | 总 step | 进度 | 已运行 | 预估剩余 | 速度 |
|------|----------|--------|------|--------|---------|------|
| grpo_cka_only_20 (cuda:0) | 19/100 | 19% | ~2h09m | ~9h29m | ~421s/it |
| grpo_random_20 (cuda:1) | 29/100 | 29% | ~3h27m | ~8h50m | ~448s/it |

### 空闲 GPU

**无空闲 GPU。** 两张卡均满载运行。

---
