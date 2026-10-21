# code 8b cell c and clean eval config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8b-cell-c-and-clean-eval-config_20260519T100826_result.json`
- **Structured JSON:** [`a0a05cf834a73c6d5b83.json`](../../sessions/a0/a0a05cf834a73c6d5b83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个配置验证通过。汇报结果：

---

### 完成汇报

**1. Cell C 配置已更新** — `westd:/root/cost-verify-agent-rl/RAGEN/config/_alfworld_8b_cell_c.yaml`

| 参数 | 修改前 | 修改后 |
|---|---|---|
| lr | 1e-6 | **5e-7** |
| model_path | ...checkpoint-231**/** | ...checkpoint-231（去掉尾部 `/`）|

其余关键参数确认无误：context_window_mode=full, n_gpus=4, gradient_checkpointing=true, optimizer_offload=true, enable_think=false, total_training_steps=30, 入口点用 train.py。

**2. Clean eval 配置已创建** — 已同时部署到两台服务器：
- `westd:/root/cost-verify-agent-rl/RAGEN/config/_alfworld_8b_sft_clean_eval.yaml`
- `bjb1:/root/cost-verify-agent-rl/RAGEN/config/_alfworld_8b_sft_clean_eval.yaml`

关键参数：val_only=true, model_path=checkpoint-231, context_window_mode=**full**, n_gpus=2, CUDA_VISIBLE_DEVICES="0,1", enable_think=false, val_env_groups=32 (in-dist), experiment_name=8b-sft-clean-eval-indist。

**3. bjb1 没有 8B SFT checkpoint** — `/root/autodl-tmp/checkpoints/qwen3_8b_sft_v1/` 不存在。运行 clean eval 前需要从 westd 拷贝 checkpoint 到 bjb1。

---
