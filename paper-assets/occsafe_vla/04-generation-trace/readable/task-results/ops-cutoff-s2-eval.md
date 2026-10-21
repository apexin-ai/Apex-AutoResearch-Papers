# ops cutoff s2 eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cutoff_s2_eval_20260523T091950_result.json`
- **Structured JSON:** [`4ccc92e45bcc52da565d.json`](../../sessions/4c/4ccc92e45bcc52da565d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

1. **训练已完成** — cutoff_s2 在 step 50005 正常结束，50000 checkpoint 已保存
2. **Eval 已启动** — PID 390231，cuda:0，`--use_proprio False`（因为 cutoff_s2 训练未使用 proprio_projector）
3. **日志确认** — eval 已加载模型并开始 Task 0 rollouts（10 tasks × 50 rollouts）
4. **监控已设置** — 每 15 分钟自动检查 eval 进度（cron job `d87e3b29`）

注意：`submit_training_job` 工具当前不可用，已改用 session cron 监控。如果 session 结束前 eval 未完成，需要手动检查日志 `~/runs/occsafe_vla/cutoff_s2_eval.log`。

---
