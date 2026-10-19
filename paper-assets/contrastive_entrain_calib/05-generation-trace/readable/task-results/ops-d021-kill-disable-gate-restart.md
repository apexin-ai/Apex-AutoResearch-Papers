# ops d021 kill disable gate restart

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d021-kill-disable-gate-restart_20260519T020137_result.json`
- **Structured JSON:** [`755142680e8432e358f3.json`](../../sessions/75/755142680e8432e358f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D021 执行完毕。

**汇总：**

| 步骤 | 状态 |
|------|------|
| Kill PID 122450 | 成功 |
| 删除 gate 代码 | 已删除 `GATE_WARMUP_STEPS`/`GATE_ACTIVATE_STEP`、`_weak_r1_gated`、gate 判定/执行逻辑、`import statistics`/`defaultdict` |
| 添加 per-strength R1 日志 | 每 10 步输出 weak/medium/strong 的 R1 mean |
| 清理旧 checkpoint | 已清空 |
| 重启训练 | PID 130467，tmux session `exp002v2`，`HF_HUB_OFFLINE=1` |
| Sanity check (step 10) | **通过** — weak R1=0.0420, medium R1=-0.1060, strong R1=-0.0683，无 ADAPTIVE GATE |
| Registry | RUNNING，spec 已更新 |

---
