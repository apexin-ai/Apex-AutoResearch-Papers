# ssh seed100 resume setup and submit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_seed100_resume_setup_and_submit_20260522T223145_result.json`
- **Structured JSON:** [`fc0b61486bd5ad418021.json`](../../sessions/fc/fc0b61486bd5ad418021.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇总：

### 结果

**Config 文件**: `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp029_seed100_resume_step10.yaml`

与原始 config 的差异：
- `total_training_steps`: 5 → **10**
- `resume_mode`: "disable" → **"auto"**
- `experiment_name`: 追加 `-resume-step10`
- `save_freq`: **5**（未改，符合硬约束）

**FSDP Checkpoint**: 完整。`global_step_5/actor/` 包含 model (2×3.8GB) + optimizer states (2×6.4GB) + extra_state + huggingface tokenizer configs，共 21GB。`latest_checkpointed_iteration.txt` 内容为 `5`。

**磁盘**: `/root/autodl-tmp/` 250GB 中已用 111GB，剩余 **140GB**，充足。

**Dry-run**: Hydra 加载成功，所有关键参数正确。

**训练命令**（供主系统提交）：
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && CUDA_VISIBLE_DEVICES=0,1 python -m verl.trainer.main_generation --config-name _alfworld_exp029_seed100_resume_step10"
```

---
