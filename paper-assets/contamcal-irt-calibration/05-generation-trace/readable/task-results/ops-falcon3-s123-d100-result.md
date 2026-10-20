# ops falcon3 s123 d100 result

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-s123-d100-result_20260522T193523_result.json`
- **Structured JSON:** [`d0237a1ae62483b3f53a.json`](../../sessions/d0/d0237a1ae62483b3f53a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无活跃 cron，无需删除。

## 报告

### 训练结果：**失败 (OOM)**
- Falcon3-7B-Base d100 s123 在 step 0 即 OOM
- GPU：RTX 4090 D (23.52 GiB)，模型加载后仅剩 1.92 GiB，forward pass 需要额外 2.38 GiB

### 根因
启动命令使用了 `--batch-size 4 --grad-accum 4`，而成功的 s42 使用 `--batch-size 1 --grad-accum 16`。两者 effective batch size 相同 (16)，但 per-device batch_size=4 激活值内存需求是 batch_size=1 的 4 倍。此外缺少 `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`。

### Checkpoint
lora_adapter 目录为空，无可用 checkpoint。

### 后续任务
未启动 eval 和 d000 训练（训练失败）。

### 磁盘
`/root/autodl-tmp` 使用 158G/169G (94%)，剩余 12G。

### 重试建议
用与 s42 一致的命令重新提交：
```bash
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True CUDA_VISIBLE_DEVICES=0 python train_sft.py \
  --model-name /root/autodl-tmp/.hf_cache/Falcon3-7B-Base \
  --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl \
  --output-dir /root/autodl-tmp/exp001/checkpoints/Falcon3-7B-Base_d100_s123 \
  --seed 123 --gpu 0 --batch-size 1 --grad-accum 16 \
  --gradient-checkpointing --lr 5e-5 \
  --cache-dir /root/autodl-tmp/.hf_cache
```

是否立即用修正参数重新提交？

---
