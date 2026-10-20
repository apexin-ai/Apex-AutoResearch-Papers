# prep plan017 14b model and scripts

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_plan017_14b_model_and_scripts_20260518T171122_result.json`
- **Structured JSON:** [`446148a9df2c20c225d3.json`](../../sessions/44/446148a9df2c20c225d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

```
=== 模型状态 ===
路径: /root/autodl-tmp/models/Qwen/Qwen3-14B/
大小: 28GB (8 safetensors shards)
状态: 已存在，文件完整 (config.json + 8 safetensors + tokenizer)

=== 显存评估 ===
实际参数量: ~14B (磁盘 28GB bf16)
架构: 40 layers, hidden=5120, heads=40 (GQA kv_heads=8), intermediate=17408

方案 A (2-GPU TP bf16): 不可行 — 项目代码不支持 tensor parallelism
方案 B (单卡 QLoRA 4-bit): 可行, 预估 ~11GB (7GB base + 0.5GB LoRA + 3GB activations)
方案 C (2-GPU ZeRO-3 bf16 LoRA): ✅ 可行, 预估每卡 ~18-20GB
  - 参数分片: 14GB/卡
  - LoRA + activations + buffers: 4-6GB
  - 已有 accelerate_2gpu_zero3.yaml 配置直接可用

已选方案: C (2-GPU DeepSpeed ZeRO-3)，用现有 accelerate_2gpu_zero3.yaml + deepspeed_zero3.json

=== 脚本 ===
SFT:  /root/autodl-tmp/freige/scripts/seed_expansion/sft_14b.sh — 已创建
Eval: /root/autodl-tmp/freige/scripts/seed_expansion/eval_14b.sh — 已创建

=== 与 1.7B 脚本的关键差异 ===
- accelerate launch + ZeRO-3 (非单卡直接运行)
- --deepspeed configs/deepspeed_zero3.json
- learning_rate: 1e-4 (降低，14B 模型更大)
- gradient_accumulation_steps: 8 (2卡×1×8=effective 16)
- max_length: 2048 (非 4096，节省显存)
- CUDA_VISIBLE_DEVICES 默认 0,1

=== Eval 注意 ===
14B bf16 = 28GB，单卡放不下。Eval 也需 2-GPU (CUDA_VISIBLE_DEVICES=0,1)
inference.py 用 device_map="auto" 自动分片到可见 GPU

=== Dry-run ===
配置加载: ✅ 成功 (model_type=qwen3, 40 layers, hidden=5120)
```

---
