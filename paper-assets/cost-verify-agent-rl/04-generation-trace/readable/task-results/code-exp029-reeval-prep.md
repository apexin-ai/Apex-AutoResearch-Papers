# code exp029 reeval prep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp029-reeval-prep_20260517T204318_result.json`
- **Structured JSON:** [`771e53cf7693c4813632.json`](../../sessions/77/771e53cf7693c4813632.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。所有配置正确解析：

**产出汇总**:

1. **Checkpoint 路径**: `/root/autodl-tmp/checkpoints/exp029/global_step_15/actor` (FSDP 分片格式，2-GPU)

2. **Eval config**: `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp029_reeval_valid_unseen.yaml`
   - `resume_mode: resume_path` → 加载 step 15 checkpoint
   - `val env_groups: 134` + tag `AlfworldSG_OOD` → valid_unseen (OOD)
   - `context_window_mode: full` (与 exp029 训练一致)
   - `total_training_steps: 1` + `val_before_train: True` → 先 eval 再跑 1 步训练（看 val_before_train 结果即可）

3. **启动脚本**: `/root/cost-verify-agent-rl/scripts/run_exp029_reeval.sh`

4. **新增 envs 定义**: `AlfworldSG_OOD` — 与 `AlfworldSG` 相同 prompt（Self-Guidance），但 `eval_dataset: "eval_out_of_distribution"`

5. **Dry-run 结果**: 配置正确加载，checkpoint 路径存在，tag 正确解析为 OOD split

Hydra 的 `_self_` 警告无影响，不影响运行。等 GPU 空闲时执行 `bash /root/cost-verify-agent-rl/scripts/run_exp029_reeval.sh` 即可。

---
