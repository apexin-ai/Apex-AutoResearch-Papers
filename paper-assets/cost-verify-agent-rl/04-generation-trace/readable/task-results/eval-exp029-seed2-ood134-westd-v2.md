# eval exp029 seed2 ood134 westd v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp029-seed2-ood134-westd-v2_20260519T022643_result.json`
- **Structured JSON:** [`3eab8b45f96c12fb526b.json`](../../sessions/3e/3eab8b45f96c12fb526b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已确认运行中：

- **Checkpoint**: exp029-seed2, global_step_30 (val 峰值 31.25%)
- **Eval**: 134 AlfworldSG_OOD tasks (eval_out_of_distribution)
- **W&B run**: `s7nph9ec` (`exp029-seed2-ood-reeval`)
- **W&B URL**: https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/s7nph9ec
- **GPU**: westd cuda:0,1
- **PID**: 691244 (TaskRunner: 697734)

**遇到并解决的问题**：
1. exp029_seed2 训练进程 (PID 414168) 未被完全 kill，占用 cuda:0,1 导致 vLLM OOM → 已强制终止
2. `AlfworldSG_OOD` 未在 envs.yaml 中定义导致 KeyError → 已添加（`eval_dataset: eval_out_of_distribution`）

**预计耗时**: 30-60 分钟。结果会记录在 W&B 中。

---
