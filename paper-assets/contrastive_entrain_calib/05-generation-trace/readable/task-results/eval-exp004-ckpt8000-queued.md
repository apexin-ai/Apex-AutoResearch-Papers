# eval exp004 ckpt8000 queued

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp004-ckpt8000-queued_20260519T143525_result.json`
- **Structured JSON:** [`c72a66c2834d173e58a4.json`](../../sessions/c7/c72a66c2834d173e58a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交，脚本正在等待 ckpt-2000 eval 完成。

| 项目 | 值 |
|------|-----|
| wrapper 脚本 | `/root/contrastive_entrain_calib/scripts/queue_eval_ckpt8000.sh` |
| tmux session | `exp-004` |
| 日志 | `~/runs/contrastive_entrain_calib/exp-004.log` |
| 服务器 | westd-28034, GPU 0 |

脚本逻辑：每 30s 轮询 PID 138467，完成后自动启动 ckpt-8000 eval（参数格式与 ckpt-2000 一致，checkpoint 路径和 output_dir/exp_id 已替换）。

---
