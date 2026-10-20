# eval trc baseline launch

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_trc_baseline_launch_20260520T071757_result.json`
- **Structured JSON:** [`f9c7cc4c0194e8165d21.json`](../../sessions/f9/f9c7cc4c0194e8165d21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功。

- **PID 158713**: TRC baseline 进程已在 GPU 上，占用 **15GB**
- GPU 总占用: 37GB (v8b) + 27GB (attn_steering) + 15GB (TRC) = **79.7GB / 98GB**，无 OOM 风险
- v7 TG checkpoint 正在加载（loading weights 57%），即将开始 TF+gen 评估

脚本串行跑三个 checkpoint（v7 TG → LoRA-only → base），预计 30-60 分钟完成。日志路径: `~/runs/turn_residual_gating/trc_baseline_v7_tg.log`。

注意: `tee` 报了目录不存在（`runs/trc_baseline/` 未提前创建），但不影响主流程——输出仍写入 tmux 监控日志。

---
