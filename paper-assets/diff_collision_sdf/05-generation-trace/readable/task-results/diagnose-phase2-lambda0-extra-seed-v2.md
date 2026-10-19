# diagnose phase2 lambda0 extra seed v2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phase2_lambda0_extra_seed_v2_20260527T141345_result.json`
- **Structured JSON:** [`b928f8620f6707e241ac.json`](../../sessions/b9/b928f8620f6707e241ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**Stage 1 状态：FAILED**
- 训练在 step 1768/10000（18%）中断，`EXIT_CODE=1`
- 日志无错误信息/traceback，进程被外部终止（非 CUDA OOM）
- Checkpoint 目录仅有 `wandb_id.txt`，无模型权重保存
- 无法 resume，需从头重训

**已执行操作：**
- Registry `notes` 已更新，记录失败原因
- Registry `log_path` 已更新为 `/tmp/phase2_stage1_s0.log`
- `status=DONE`, `conclusion=failed` 此前已设置
- Cron 已不存在（已被之前的 hook 清除）

**未启动 Stage 2**（Stage 1 未完成，无 10K checkpoint 可用）。

GPU 现况：cuda:0/1/2 空闲，cuda:3 在跑 lora_baseline_spatial_bowl。如需重跑 Stage 1 请指示。

---
