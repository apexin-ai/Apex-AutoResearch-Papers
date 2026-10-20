# analysis sft rasp 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sft_rasp_20_20260515T002952_result.json`
- **Structured JSON:** [`b4beb0e7134721f58a91.json`](../../sessions/b4/b4beb0e7134721f58a91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

EOS 测试完成，结果优秀。写总结。

---

## sft_rasp_20 分析总结

### 训练状态：**成功**

| 指标 | 值 |
|------|-----|
| 总 steps | 1870 (2 epochs) |
| 训练时间 | 36:38 (~37 min) |
| 平均 train loss | 0.7736 |
| 初始 loss | 1.863 |
| 最终 loss | ~0.63-0.65 |
| 最终 mean_token_accuracy | ~0.83 |
| W&B | 无（report_to="none"） |

### EOS 生成测试：**100% 通过 (5/5)**

| Prompt | Gen tokens | Has EOS | 质量 |
|--------|-----------|---------|------|
| 12 + 15 | 225 | Yes | 正确，稍冗长 |
| 3 apples × $2 | 31 | Yes | 精准，GSM8K 格式 |
| 60 mph × 2.5h | 54 | Yes | 精准 |
| 7 - 3 marbles | 25 | Yes | 精准 |
| 25 × 4 | 51 | Yes | 正确 |

平均生成长度 77 tokens，全部正常终止。生成质量遵循 GSM8K 格式（`<<计算>>` + `#### 答案`）。

### Checkpoint

- 路径：`/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20/`
- 最终模型：`model.safetensors` 12GB（完整权重，非 LoRA）
- 中间 checkpoint：`checkpoint-935`（epoch 1）、`checkpoint-1870`（epoch 2，含 optimizer 23GB）

### 结论：**SUCCESS**

SFT warmup 完全达成目标：
1. EOS 生成能力从 0% 恢复到 100%
2. 模型遵循 GSM8K 推理格式
3. 生成长度合理（平均 77 tokens），无重复循环
4. Loss 从 1.86 降至 0.64，token accuracy 83%

### GRPO Stage 2 推荐参数

```bash
python src/grpo_train.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20 \
  --gpu 0,1 \
  --num_train_epochs 1 \
  --learning_rate 5e-7 \
  --max_new_tokens 512 \
  --temperature 0.7 \
  --num_generations 4 \
  --gradient_accumulation_steps 4
```

关键点：
- LR 用 5e-7（比 SFT 低 40x），GRPO 需要小 LR 防止忘掉 SFT 修复的 EOS 能力
- 可以用双卡（cuda:0,1）加速 generation
- num_generations=4 提供足够的 reward variance

---
