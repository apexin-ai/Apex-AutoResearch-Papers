# ops deploy checkpoint pollers 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_checkpoint_pollers_34685_20260528T041922_result.json`
- **Structured JSON:** [`ed9c254b1c918796f9d7.json`](../../sessions/ed/ed9c254b1c918796f9d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个轮询脚本全部部署成功，均已在后台运行并开始轮询。

| 实验 | 脚本 PID | GPU | 状态 |
|------|---------|-----|------|
| full_occ_ln_v2_s3 | 61245 | cuda:2 | Polling started ✓ |
| detach_ln_v2_s3 | 61243 | cuda:3 | Polling started ✓ |
| detach_ln_v2_s2 | 61244 | cuda:0 | Polling started ✓ |

每个脚本每 60 秒检查一次 checkpoint 目录 + `adapter_config.json`，检测到后等 60s → kill 训练 → 启动 eval。日志分别写入 `/root/poll_eval_&lt;name>.log`。

---
