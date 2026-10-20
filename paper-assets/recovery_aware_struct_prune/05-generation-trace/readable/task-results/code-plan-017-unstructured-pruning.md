# code plan 017 unstructured pruning

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_017_unstructured_pruning_20260517T042117_result.json`
- **Structured JSON:** [`336c2593a10acaf73707.json`](../../sessions/33/336c2593a10acaf73707.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. `prune_unstructured.py` 已就绪

位置：`/root/recovery_aware_struct_prune/src/prune_unstructured.py`

功能：全局 magnitude unstructured pruning → 保存完整 HF checkpoint（含 tokenizer + metadata JSON）

### 2. Dry-run 验证通过

- 参数解析：正常
- 前 2 层 pruning 逻辑：实际 sparsity = 20.03%（目标 20%）
- Forward pass：OK，output shape `[1, 16, 152064]`
- 排除规则生效：embedding/lm_head/norm 未被剪枝
- Global threshold 分配合理（Layer 1 的 MLP 被剪得更多 ~30%，说明那里权重更小）

### 3. 预估 Post-prune accuracy

- 20% unstructured magnitude pruning 对 7B 模型通常 **损失较小**（GSM8K 下降 ~3-8pp vs baseline ~86%）
- 相比 structured pruning 20%（去掉整个 head，通常下降 10-20pp），unstructured 保留了结构完整性
- 这正是 baseline 的目的：证明 structured pruning 虽然加速了推理，但需要更好的 recovery 策略

### 4. 总 pipeline 时间估算

| Step | 时间估算 | GPU 需求 |
|------|---------|---------|
| Prune (CPU) | ~5-8 min | 无 |
| Post-prune eval (200 samples) | ~30 min | 1 GPU |
| SFT recovery (2 epochs) | ~45 min | 1 GPU |
| Post-SFT eval (1319 samples) | ~90 min | 1 GPU |
| **总计** | **~2.5-3h** | |

### 5. 额外依赖

无。所有依赖（transformers, torch, datasets）已安装。

### 完整 pipeline 命令

```bash
# Step 1: Prune
cd /root/recovery_aware_struct_prune/src
python prune_unstructured.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --target_sparsity 0.20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20 --seed 42

# Step 2: Post-prune eval
CUDA_VISIBLE_DEVICES=0 python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_unstructured_20.json

# Step 3: SFT recovery
python sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_unstructured_20 --gpu 0 --learning_rate 2e-5 --num_train_epochs 2 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_len 2048 --seed 42

# Step 4: Post-SFT eval
CUDA_VISIBLE_DEVICES=0 python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_unstructured_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_unstructured_20.json
```

GPU 一空即可从 Step 1 开始（Step 1 只需 CPU）。

---
