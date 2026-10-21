# code cell b 1gpu prep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cell_b_1gpu_prep_20260525T000445_result.json`
- **Structured JSON:** [`e1be7c595588f79b7e12.json`](../../sessions/e1/e1be7c595588f79b7e12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**已创建两个文件：**
- Config: `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_factorial_h2_episode_adv_1gpu.yaml`
- 脚本: `/root/cost-verify-agent-rl/scripts/run_cell_b_1gpu.sh`

**关键确认：**
- Model: `qwen3_exp021_ragen_sft_v4`，确认 Qwen3-1.7B
- Seed 字段: `seed.train`，通过 Hydra CLI override
- 启动: `bash scripts/run_cell_b_1gpu.sh &lt;seed>`（如 100/200/300）
- 与原始 Cell B 唯一区别：1 GPU + `n_gpus_per_node=1`

**SFT 状态：** 192/450 steps (43%)，约 1h20m 后完成，之后可立即启动 Cell B。

---
