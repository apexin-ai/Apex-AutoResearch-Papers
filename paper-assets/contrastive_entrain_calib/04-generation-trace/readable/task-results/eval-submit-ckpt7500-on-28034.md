# eval submit ckpt7500 on 28034

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_submit-ckpt7500-on-28034_20260522T115422_result.json`
- **Structured JSON:** [`37d7478f78ab552ca769.json`](../../sessions/37/37d7478f78ab552ca769.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

| Checkpoint | 状态 |
|---|---|
| **ckpt-7500** | ✅ 已 SCP 到 28034，eval 正在 GPU0 运行（tmux session: `eval-s2-7500`） |
| **ckpt-8000** | 训练 step 7507/8000，约 3.5h 后产出。29046 后台进程（PID 500554）等待产出后自动 SCP；28034 后台进程（PID 6997）等待收到后自动在 GPU2 启动 eval |

两个 ckpt 的 eval 都已全自动化，无需再手动干预。

---
