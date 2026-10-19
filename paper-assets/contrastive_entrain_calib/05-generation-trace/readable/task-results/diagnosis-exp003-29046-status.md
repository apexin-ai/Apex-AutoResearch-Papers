# diagnosis exp003 29046 status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp003-29046-status_20260520T161550_result.json`
- **Structured JSON:** [`cc6e9aa33bfb183f8a4a.json`](../../sessions/cc/cc6e9aa33bfb183f8a4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp-003 seed 1 (PID 70649):
  PID: 存活，已运行 1天23小时25分
  当前 step: ~5900/8000（最新 checkpoint 5500，保存于 20:55，按 ~30s/step 估算）
  已有 checkpoint: 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500
  未 eval 的 checkpoint（>5000）: 5500
  预计完成: ~May 21 18:00（剩余 ~2100 steps，~17.5h）

exp-003-s2 seed 2 (PID 237432):
  PID: 存活，已运行 15小时59分
  当前 step: 1749/8000（日志实时，~27s/step）
  已有 checkpoint: 500, 1000, 1500
  预计完成: ~May 23 00:00（剩余 ~6250 steps，~47h）

GPU 状态:
  GPU 0: 利用率 100%, 显存 38049/97887 MiB
  GPU 1: 利用率 98%,  显存 38161/97887 MiB
```

注意：seed 1 无独立日志文件（`~/runs/` 下没有对应 log），当前 step 是基于 checkpoint 时间间隔推算的。下次 checkpoint-6000 预计在 ~May 21 01:00 左右保存。

---
