# ops kill gs8 start heldout

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-gs8-start-heldout_20260523T055705_result.json`
- **Structured JSON:** [`e0ca1e1217287cb5abbf.json`](../../sessions/e0/e0ca1e1217287cb5abbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**gs8 杀死确认：** PID 516691/516695/516696 已 kill -9，GPU 0 已释放。

**heldout 启动确认：**
- PID: 571918（python training/run_exp004_heldout.py）
- GPU: cuda:0，已占用 17590 MiB
- tmux session: `heldout`
- 日志: `/root/runs/contrastive_entrain_calib/exp-004-heldout.log`
- 训练配置: 146 pairs, max_steps=8000, grad_accum=16, lr=5e-05, lambda_l2=0.1
- GPU 1 上原有进程 (PID 553700) 不受影响

---
