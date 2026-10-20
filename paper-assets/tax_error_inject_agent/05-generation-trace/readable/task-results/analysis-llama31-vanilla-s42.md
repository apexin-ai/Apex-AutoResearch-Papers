# analysis llama31 vanilla s42

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama31-vanilla-s42_20260516T074618_result.json`
- **Structured JSON:** [`f23a0f2378c6bcd898f3.json`](../../sessions/f2/f23a0f2378c6bcd898f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

---

## LLaMA-3.1-8B Vanilla s42 训练结果报告

| 项目 | 值 |
|------|------|
| **训练状态** | ✅ 成功完成（EXIT_CODE=0） |
| **最终 train_loss** | **0.40025**（平均），最后一批 ~0.277 |
| **最终 token_acc** | 0.9067 |
| **训练时长** | **1h 9m 17s**（4156.9s） |
| **训练步数** | 1635/1635（3 epochs） |
| **训练速度** | 2.54 s/it，3.145 samples/s |
| **GPU 显存** | 30.2 GiB |
| **Checkpoint 路径** | `/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635/adapter_model.safetensors` |
| **中间 checkpoints** | checkpoint-545, checkpoint-1090（每 epoch 保存） |
| **训练样本数** | **4358** 条（sft_vanilla_v4.jsonl） |
| **W&B run ID** | 未找到（日志中无 wandb 相关信息，未启用 W&B） |
| **异常/Warning** | bitsandbytes 加载 libnvJitLink.so.13 失败（不影响训练，因为未使用量化）；无其他 error/warning |

**训练命令**：
```
swift sft --model Meta-Llama-3.1-8B-Instruct --lora_rank 16 --num_train_epochs 3 
--per_device_train_batch_size 4 --gradient_accumulation_steps 2 
--learning_rate 1e-4 --max_length 4096 --seed 42 --bf16 true
```

**Loss 变化趋势**：epoch 1 中期 ~0.39 → epoch 3 末 ~0.27，收敛正常。

---
