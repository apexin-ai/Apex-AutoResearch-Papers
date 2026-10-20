# run multiseed 16639 batch

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_multiseed-16639-batch_20260522T194233_result.json`
- **Structured JSON:** [`a09fdfaa74b330038289.json`](../../sessions/a0/a09fdfaa74b330038289.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇总：

## 当前状态

| GPU | 用途 | 状态 |
|-----|------|------|
| cuda:0 | Qwen2.5-14B vLLM (port 8001) + PW seed456→789 | **运行中** (PID 663049, 88GB, 97% util) |
| cuda:1 | 空闲 | — |
| cuda:2 | Mistral vLLM (port 8003) + PW seed789 | **运行中** (PID 655962, 171/600, 90GB, 96% util) |
| cuda:3 | 空闲 | — |

## Multi-seed 完成情况

| 模型×数据集 | seed42 | seed123 | seed456 | seed789 |
|-------------|--------|---------|---------|---------|
| **Qwen2.5-14B × PW** | (baseline) | sc=0.525, sica=0.523 | **跑ing** | 排队中(456完成后自动跑) |
| **Mistral × PW** | sc=0.400, sica=0.367 | sc=0.408, sica=0.375 | sc=0.398, sica=0.387 | **跑ing** 171/600 |

## 进程监控
- Qwen runner: `tail -f /tmp/qwen25_pw_multiseed.log`
- Mistral 789: 已在 cuda:2 独立跑，不需干预
- seed123 参考：wall_time ~30334s（~8.4h），两个 seed 预计 ~17h 完成

## 注意
- cuda:1 和 cuda:3 空闲，如有其他实验可以利用
- Mistral PW 4 个 seed 全部有数据（789 完成后即齐全）

---
