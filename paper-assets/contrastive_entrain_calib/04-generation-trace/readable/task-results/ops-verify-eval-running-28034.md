# ops verify eval running 28034

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-eval-running-28034_20260521T072314_result.json`
- **Structured JSON:** [`5f86b2c198aa273a997c.json`](../../sessions/5f/5f86b2c198aa273a997c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

```
实际 GPU 状态:
  cuda:0: PID 497834 running exp-003-eval-ckpt5000-v2 (16.8GB, 48% util)
  cuda:1: PID 498446 running exp-003-eval-ckpt6000 (16.8GB, 48% util)
  cuda:2: PID 498584 running exp-003-eval-ckpt6500 (16.8GB, 49% util)
  cuda:3: PID 498666 running exp-003-eval-ckpt7000 (16.8GB, 50% util)

Registry 修复:
  exp-003-eval-ckpt5000-v2: DONE(failed) → RUNNING, PID=497834 (nohup, 无 tmux)
  exp-003-eval-ckpt6000:    DONE(failed) → RUNNING, PID=498446 (tmux session)
  exp-003-eval-ckpt6500:    DONE(failed) → RUNNING, PID=498584 (tmux session)
  exp-003-eval-ckpt7000:    ALLOCATED    → RUNNING, PID=498666 (tmux session)

Cron 注册:
  全部 4 个 eval: cron eba2e700 (每8分钟), 监控 PID 存活 + 自动收割结果
```

**根因**：kill-cleanup-restart worker 用 SIGHUP 杀掉了 batch-submit worker 提交的旧进程（PID 495833/495906/496116/496266），触发 cron 将 3 个 eval 标记为 DONE(failed, EXIT_CODE=129)。随后重新提交了新进程，但 registry 状态未从 DONE 恢复到 RUNNING。ckpt7000 卡在 ALLOCATED 是因为提交后未完成状态转换。

---
