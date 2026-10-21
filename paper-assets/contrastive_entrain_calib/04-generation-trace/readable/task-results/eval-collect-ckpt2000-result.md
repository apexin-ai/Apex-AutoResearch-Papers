# eval collect ckpt2000 result

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect-ckpt2000-result_20260523T105709_result.json`
- **Structured JSON:** [`be7c7e628e7fb4bdf7a1.json`](../../sessions/be/be7c7e628e7fb4bdf7a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

| 项目 | 状态 |
|------|------|
| **checkpoint-2000** | 未生成，当前最新 step = **1950** |
| **训练进程** | 运行中 (PID 553700, `run_exp003_len512_r3only.py`) |
| **wait_and_eval.sh** | 运行中 (PID 591882)，每 30s 轮询，已检查 6 次均未找到 |
| **eval 结果** | 无（eval 尚未启动） |

**ETA 估算**：
- 每 10 步约 92s → 剩余 50 步约 **460s ≈ 8 分钟**
- checkpoint-1500 生成于 17:47 CST，按速率推算 checkpoint-2000 约在 **19:04 CST**（约 5-6 分钟后）
- checkpoint 生成后 eval 脚本会自动启动

无需手动干预，wait_and_eval.sh 会自动检测并触发 eval。

---
