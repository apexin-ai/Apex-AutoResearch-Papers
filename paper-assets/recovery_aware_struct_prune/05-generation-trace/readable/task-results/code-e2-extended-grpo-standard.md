# code e2 extended grpo standard

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e2_extended_grpo_standard_20260518T125953_result.json`
- **Structured JSON:** [`0bf73d3dd702d60318d8.json`](../../sessions/0b/0bf73d3dd702d60318d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动并正在运行。

**状态汇总：**
- **PID**: 2682
- **W&B run_id**: `k5ex8kfs`
- **W&B URL**: https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/k5ex8kfs
- **Step 起点**: 从 step 100 resume 成功（进度条 101/300）
- **配置**: beta=0.01, loss_type=dapo, format_reward=0.1, temp=0.4, rep_penalty=1.15, optim=adamw_8bit
- **注意**: save_steps 从原来的 10 变为默认 100（有 warning 但不影响训练），将在 step 200、300 保存 checkpoint

**LR 警告**: 原训练 100 步 cosine decay 已衰减到 1e-08。resume 后 scheduler 状态从 checkpoint 加载，LR 可能极低。建议在 step 110 处检查 wandb 上的 learning_rate 曲线。如果 LR 接近 0，可能需要 kill 并改用 checkpoint-100 作为 model_path 重新训练 200 步。

---
