# prep alpha dose response 20260522

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_alpha_dose_response_20260522_20260522T050234_result.json`
- **Structured JSON:** [`ad0c723a47ed0e93f452.json`](../../sessions/ad/ad0c723a47ed0e93f452.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval_humaneval.py 同步完成（6948 bytes，匹配 westb）。eval_mbpp.py 两边都是 7086 bytes，无需同步。

```
== Scores 文件 (westd-32935) ==
importance_scores: 缺失
cka_scores: 缺失

== Scores 文件 (westb-23072) ==
importance_scores_1p5b.pt: /root/autodl-tmp/recovery_aware_struct_prune/ (16KB)
importance_scores_qwen_math_7b.pt: /root/autodl-tmp/recovery_aware_struct_prune/ (20KB)
cka_scores_1p5b.pt: /root/autodl-tmp/recovery_aware_struct_prune/ (48KB)
cka_scores_qwen_math_7b.pt: /root/autodl-tmp/recovery_aware_struct_prune/ (124KB)

== prune.py 参数 ==
--model_path       (required) Path to pretrained model
--importance_path  Path to importance scores .pt
--cka_path         Path to CKA overlap scores .pt
--mode             {standard, rasp, rasp-rlvr, cka_only, random} (required)
--sparsity         Target sparsity ratio (default: 0.35)
--alpha            RASP alpha parameter (default: 1.0)
--output_path      (required) Output path for pruned model
--seed             (default: 42)
--dtype            {float16, bfloat16, float32} (default: bfloat16)

== prune.py RASP 逻辑 ==
必需输入: model_path, importance_path, cka_path
模式判断:
  - standard: needs importance only → score = I(h)
  - rasp: needs importance + CKA → S(h) = I(h) * (1 - F(h))^α
  - rasp-rlvr: needs importance + CKA → S(h) = I(h) * F(h)^α  (反向 CKA)
  - cka_only: needs CKA only → score = 1 - F(h)
  - random: torch.rand (seed=42)

importance_data keys: attn_importance, mlp_importance
cka_data keys: attn_overlap, mlp_overlap

== 完整剪枝命令模板 ==
python src/prune.py \
  --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B \
  --importance_path &lt;IMP_SCORES_PATH> \
  --cka_path &lt;CKA_SCORES_PATH> \
  --mode rasp \
  --sparsity 0.2 \
  --alpha &lt;ALPHA> \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_alpha&lt;ALPHA>_20

== SFT 训练脚本 ==
sft_recovery.py (D013 Stage 1, GSM8K SFT warmup):
  --model_path, --output_dir (required)
  --gpu (default: 0), --num_train_epochs (2), --learning_rate (2e-5)
  --batch_size (1), --gradient_accumulation_steps (8), --max_seq_length (2048)
  --max_samples, --logging_steps (10), --seed (42)

train_sft_warmup.py (轻量 SFT):
  --model_path, --output_dir (required)
  --gpu_id (default: 0), --num_epochs (1), --lr (2e-5)
  --batch_size (2), --gradient_accumulation_steps (8)
  --max_samples, --max_seq_length (2048), --logging_steps (10), --seed (42)

== GRPO 训练脚本 ==
train_grpo_v5.py (v4, GRPO RLVR recovery):
  --model_path (required), --output_dir
  --gpu (0), --learning_rate (1e-6), --num_train_epochs (3)
  --per_device_train_batch_size (2), --gradient_accumulation_steps (8)
  --max_completion_length (512), --temperature (0.4), --repetition_penalty (1.15)
  --num_generations (4), --beta (0.01), --loss_type (dapo)
  --format_reward_weight (0.1), --gradient_checkpointing (true)
  --optim (adamw_8bit), --max_steps (-1), --resume_from_checkpoint
  --report_to (wandb), --wandb_project (recovery_aware_struct_prune)

== Eval 脚本同步 ==
eval_humaneval.py: 已同步 (westb 6948 bytes → westd 6948 bytes ✓)
eval_mbpp.py: 已一致 (两边均 7086 bytes ✓)

== 基础模型路径 ==
DeepSeek-R1-Distill-Qwen-7B: /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B

== 已有剪枝模型 (westd-32935) ==
pruned_alpha4_20, pruned_cka_only_15, pruned_cka_only_25, pruned_cka_only_30
pruned_rasp_25, pruned_standard_15, pruned_standard_25, pruned_standard_30

== ⚠️ 待解决 ==
scores 文件只在 westb-23072 上，westd-32935 上完全没有。需要：
1. 从 westb 中转到 westd（两台无直连，需通过本地中转 base64 或 scp 跳板）
2. 或在 westd 上重新计算（src/importance_score.py + src/compute_layer_cka.py 脚本已存在）
```

---
