# fix 41312 uniform 1 7b resume

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_41312_uniform_1_7b_resume_20260518T152228_result.json`
- **Structured JSON:** [`9437d28cc7c3da6dfe03.json`](../../sessions/94/9437d28cc7c3da6dfe03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动。

**结果汇总：**

1. **checkpoint-3000 文件列表**：有 model.safetensors (3.4GB)、optimizer.pt (6.7GB，损坏)、config.json、tokenizer 等。缺 trainer_state.json、scheduler.pt、rng_state.pth
2. **选择方案 B**：optimizer.pt 损坏（写入中断），方案 A 无法 resume。改用 checkpoint-3000 模型权重作为新训练起点
3. **GPU 0 显存占用**：61,693 MiB，utilization 98%
4. **训练配置**：num_train_tokens=100M → max_steps=3051，~2.5h/s per step，预计约 2.5 小时完成
5. **输出目录**：`/root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed42_resumed`
6. **日志**：`~/runs/provenance_weight_training/uniform_1_7b_seed42_r3.log`

**注意**：方案 B 的 LR schedule 从头开始（含 warmup），optimizer 状态重置。总训练 token 数为原始 200M 的前 50%（checkpoint-3000）+ 新 100M = ~300M tokens 的模型权重暴露量，比原计划多约 50%。如果严格需要等效的 200M token 训练，可将 `--num_train_tokens` 改为约 100,395,000（= 3103 steps × 4 batch × 4 accum × 2048 tokens）。当前 100M 已足够接近。

---
