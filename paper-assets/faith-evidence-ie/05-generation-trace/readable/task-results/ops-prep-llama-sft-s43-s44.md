# ops prep llama sft s43 s44

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep_llama_sft_s43_s44_20260520T023958_result.json`
- **Structured JSON:** [`fe5b72e7039e2ac500b8.json`](../../sessions/fe/fe5b72e7039e2ac500b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已创建并通过语法检查。

## 输出汇总

**脚本路径：**
- `/root/autodl-tmp/freige/scripts/seed_expansion/llama_sft_s43_train_eval.sh`
- `/root/autodl-tmp/freige/scripts/seed_expansion/llama_sft_s44_train_eval.sh`

**预估耗时（每 seed）：**
- SFT 训练：~1 小时（570 steps，参考 s42 checkpoint 时间戳：18:54 → 19:33 跑了 380 steps）
- Eval：~20-30 分钟（LLaMA 8B no-quantize, bs=4）
- 合计：~1.5 小时/seed

**GPU 需求：** 每个 seed 1 卡，可通过 `GPU=X` 环境变量指定卡号。两个 seed 可并行跑在不同卡上。

**s42 原始训练参数（从 adapter_config.json + sft_llama_s44.sh 确认）：**
```
model: Meta-Llama-3.1-8B
lora_rank: 64, lora_alpha: 128, lora_dropout: 0.05
--no-quantize, --bf16
per_device_batch_size: 1, gradient_accumulation_steps: 16
num_epochs: 3, learning_rate: 2e-4, warmup_ratio: 0.05
max_length: 4096
output: /root/autodl-tmp/sft_output_llama_3_1_8b
```

**启动方式：**
```bash
GPU=2 nohup bash /root/autodl-tmp/freige/scripts/seed_expansion/llama_sft_s43_train_eval.sh > /tmp/llama_sft_s43.log 2>&1 &
GPU=3 nohup bash /root/autodl-tmp/freige/scripts/seed_expansion/llama_sft_s44_train_eval.sh > /tmp/llama_sft_s44.log 2>&1 &
```

---
