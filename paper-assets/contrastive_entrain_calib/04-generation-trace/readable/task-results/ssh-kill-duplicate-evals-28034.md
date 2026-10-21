# ssh kill duplicate evals 28034

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-duplicate-evals-28034_20260522T193601_result.json`
- **Structured JSON:** [`810432a7a4f288277153.json`](../../sessions/81/810432a7a4f288277153.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**PID 667859 (cuda:0)**: 已不存在，进程已自行退出。

**cuda:2 两个进程对比**:

| PID | 启动时间 | exp_id |
|-----|---------|--------|
| 1979 | 03:16:44 | `exp-004-reduced-lora-eval-ckpt500` |
| 108611 | 03:17:06 | `exp-004-reduced-lora-ckpt500` |

两者命令完全相同（同一 checkpoint-500），只是 exp_id 不同。PID 1979 先启动 22 秒，exp_id 多了个 `eval-` 前缀。

请确认要 kill 哪个？我的判断是 kill PID 1979（`-eval-ckpt500`，像是命名失误的重复），保留 PID 108611（`-ckpt500`，命名更规范）。

---
