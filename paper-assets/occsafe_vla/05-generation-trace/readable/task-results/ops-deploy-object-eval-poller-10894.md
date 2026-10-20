# ops deploy object eval poller 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_object_eval_poller_10894_20260528T050311_result.json`
- **Structured JSON:** [`3bc471bbd1a8a76229b6.json`](../../sessions/3b/3bc471bbd1a8a76229b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

轮询脚本已部署并运行。

- **轮询脚本 PID: 962263**
- 每 60s 检查 `*50000_chkpt/adapter_config.json` 是否存在
- 检测到后等 60s（确保 checkpoint 写完），再等训练进程自然退出（最多 10 分钟，超时则 kill）
- 然后在 `cuda:0` 上启动 eval：`--task_suite_name libero_object --num_rollouts 50 --seed 42`
- 日志：`/root/poll_eval_vanilla_object_s1.log`

---
