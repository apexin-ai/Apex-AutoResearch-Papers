# experiment seed3 ood bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_seed3-ood-bjb1_20260520T192250_result.json`
- **Structured JSON:** [`3339d5bddc7e4a8798bc.json`](../../sessions/33/3339d5bddc7e4a8798bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**已完成：**
- westd-47453 上确认 `exp029-seed3/global_step_5` checkpoint 存在（21GB，FSDP 2-GPU 格式）
- 通过 SSH 密钥 + SCP 将 checkpoint 从 westd 传输到 bjb1（~30 分钟）
- 在 bjb1 创建 OOD eval 配置 `_alfworld_exp029_seed3_ood.yaml`（基于已验证的 exp029 reeval 模板）
- 提交 eval job `exp029_seed3_ood` 到 bjb1-17606 (cuda:0,1)，tmux session `exp029_seed3_ood`
- 验证启动：config 加载正确、Ray 初始化完成、模型 safetensors 加载完成、checkpoint resume path 正确
- Registry 更新：exp029_seed3_ood → RUNNING，parent=exp029_seed3_v2
- 清理 westd 上的临时 SSH 密钥

**Eval 参数：**
- Checkpoint: exp029-seed3 global_step_5（episode-level GRPO，2 GPU FSDP）
- 134 OOD tasks (AlfworldSG_OOD, valid_unseen), T=0.4, group_size=1
- 2 GPU, env_groups=16 (train) / 134 (val)
- 超时: 8h

---
