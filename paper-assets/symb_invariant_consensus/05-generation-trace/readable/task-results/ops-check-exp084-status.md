# ops check exp084 status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-exp084-status_20260520T024612_result.json`
- **Structured JSON:** [`8fb126015fa08d5fe068.json`](../../sessions/8f/8fb126015fa08d5fe068.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp-084 已完成。**

| 指标 | 值 |
|---|---|
| 进度 | **200/200** (全部完成) |
| Debate accuracy | **0.2900** (58/200) |
| SC accuracy | **0.5050** (101/200) |
| Delta (debate - SC) | **-0.2150** |
| Fallbacks | 14/200 |
| Constraints | 3220 total |
| Wall time | 226.3 min (~3.8h) |
| 状态 | `EXIT_CODE=0`, 正常退出 |

GPU 1/2 仍有 ~90GB 显存占用但 utilization 0% — 可能是模型仍加载在显存中（进程未退出或 vLLM server 仍在运行），但实验本身已跑完。

Debate accuracy (0.29) 大幅低于 SC baseline (0.505)，delta = -0.215，说明在 LogiQA seed123 上 debate 机制对 Mistral 没有带来增益，反而显著降低了准确率。

---
