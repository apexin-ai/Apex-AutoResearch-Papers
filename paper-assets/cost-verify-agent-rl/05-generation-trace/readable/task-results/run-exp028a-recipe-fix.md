# run exp028a recipe fix

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp028a_recipe_fix_20260515T210934_result.json`
- **Structured JSON:** [`dac235f9654287ece09f.json`](../../sessions/da/dac235f9654287ece09f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp028a 已启动。**

**修正内容：**
- Config `model_path` 从 `Qwen3-1.7B-Instruct` 改回 SFT checkpoint `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4`
- 启动脚本 MODEL 路径同步修正
- 添加 `WANDB_MODE=online`

**Diff 确认（vs exp027）唯一功能性改动：**`invalid_action_penalty_coef: 0.1`

**训练状态：**
- PID: 814647 → TaskRunner 817920
- W&B run: `lu42su82` (exp028a-recipe-fix)
- W&B URL: https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/lu42su82
- GPU: cuda:0 + cuda:1，模型加载中
- Registry: RUNNING

---
