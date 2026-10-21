# deploy bjb2 28827 idle gpus magnitude

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-idle-gpus-magnitude_20260517T180402_result.json`
- **Structured JSON:** [`038fb90b51cd5c8f9424.json`](../../sessions/03/038fb90b51cd5c8f9424.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部成功启动并确认 GPU 占用：

| 实验 | GPU | PID | 显存占用 |
|------|-----|-----|----------|
| obs_only ε=0.1 seed47 | cuda:1 | 448782 | 5645 MiB |
| obs_only ε=0.1 seed46 | cuda:3 | 449068 | 5609 MiB |
| perdof ε=0.2 seed43 r3 | cuda:5 | 449339 | 5460 MiB |

日志路径：
- `~/runs/acr-vla-conformal-refinement/mag_obs_only_norm01_seed47.log`
- `~/runs/acr-vla-conformal-refinement/mag_obs_only_norm01_seed46.log`
- `~/runs/acr-vla-conformal-refinement/mag_perdof_norm02_seed43_r3.log`

---
