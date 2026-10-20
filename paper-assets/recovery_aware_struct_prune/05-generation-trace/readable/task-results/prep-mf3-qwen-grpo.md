# prep mf3 qwen grpo

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_mf3_qwen_grpo_20260522T063407_result.json`
- **Structured JSON:** [`ec04dfa5bf93c6dea23b.json`](../../sessions/ec/ec04dfa5bf93c6dea23b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完成。

```
== MF3 Qwen-Math GRPO 准备 ==
SFT Checkpoint: /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final (11.5GB, 完整)
  - config: Qwen2ForCausalLM, 28层, per_layer_intermediate_size 存在 (pruned model)
Tokenizer: 兼容 (vocab=151643, pad=eos=151643, chat_template=Qwen2 im_start格式)
train_grpo_v5.py: 兼容，无 DeepSeek 硬编码
  - load_pruned_model 正确识别 per_layer_intermediate_size
  - monkey-patch ref_model 加载路径正确
eval_gsm8k.py: 兼容，使用 apply_chat_template，无模型特定代码
Dry-run (tokenizer+data): PASS (GSM8K 7473 samples 加载正常)
Qwen scores: 缺失 (无 importance_scores_qwen_math_7b.pt / cka_scores_qwen_math_7b.pt)，但 GRPO 不需要

Ready-to-submit command:
bash -c 'cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/train_grpo_v5.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20 \
  --gpu 0 \
  --learning_rate 1e-6 \
  --num_train_epochs 3 \
  --per_device_train_batch_size 2 \
  --gradient_accumulation_steps 8 \
  --max_completion_length 512 \
  --temperature 0.4 \
  --beta 0.01 \
  --loss_type dapo \
  --format_reward_weight 0.1 \
  --gradient_checkpointing \
  --optim adamw_8bit'

Eval command:
bash -c 'cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20/checkpoint-100 \
  --max_new_tokens 2048 \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_qwen_math_cka_only_20.json'

风险/注意事项:
1. **Prompt 格式不一致**: train_grpo_v5.py 用原始文本 prompt（"Solve the following..."），但 SFT checkpoint 是在 chat template 格式（<|im_start|>user...）上微调的。eval_gsm8k.py 则正确使用 apply_chat_template。训练/评估的 prompt 格式不一致可能影响 GRPO 初始收敛速度。如需对齐，需修改 prepare_dataset 中 format_prompt 函数使用 tokenizer.apply_chat_template。
2. **Qwen-Math 内置 system prompt**（"Please reason step by step, and put your final answer within \boxed{}."）会在 eval 时自动注入，但 GRPO 训练时不会——这可能导致训练期间模型缺少 math reasoning 指令。
3. Qwen scores 文件不影响 GRPO，不阻塞。
```

---
