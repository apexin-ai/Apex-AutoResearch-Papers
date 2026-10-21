# deploy bjb2 24035 check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-24035-check_20260526T161836_result.json`
- **Structured JSON:** [`8f618cd79df97c555be4.json`](../../sessions/8f/8f618cd79df97c555be4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 空闲（0 MiB / 24564 MiB），环境就绪（aml-train v20260416, py3.12, torch2.10, cuda12.8）。但发现两个候选都有问题，需要用户确认。

**问题：**

1. **候选 A** 指定的 checkpoint `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_unified/crm_best.pt` **不存在**。
   - 可用 SmolVLA CRM checkpoint：
     - `crm_smolvla_3suite_v1/crm_best.pt` ✅（最匹配"统一 3suite SmolVLA CRM"语义）
     - `crm_spatial_only/crm_best.pt`
     - `crm_v3/{obs_only,perdof,scalar_unc}/crm_best.pt`
     - `crm_v3_norm/{obs_only,perdof,scalar_unc}/crm_best.pt`

2. **候选 B** 命令中 **缺 `--crm_checkpoint` 参数**。按记忆 `evaluate_crm_checkpoint_arg.md`：`crm_obs_only` 不自动填充默认 CRM checkpoint，直接运行会出错。

**建议：** 部署候选 A，将路径改为 `crm_smolvla_3suite_v1/crm_best.pt`。是否确认？或指定其他 checkpoint？

---
