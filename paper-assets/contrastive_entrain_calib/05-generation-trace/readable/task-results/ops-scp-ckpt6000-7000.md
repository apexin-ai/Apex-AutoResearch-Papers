# ops scp ckpt6000 7000

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scp-ckpt6000-7000_20260521T043616_result.json`
- **Structured JSON:** [`d162f86ad761baa75ea6.json`](../../sessions/d1/d162f86ad761baa75ea6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SCP 完成，28034 上现有全部 10 个 checkpoint。

---

## 产出报告

### 1. SCP 状态：成功

| Checkpoint | 源路径 (29046) | 目标路径 (28034) | 大小 |
|---|---|---|---|
| 6000 | `/root/autodl-tmp/checkpoints/exp003_r3only_seed1/checkpoint-6000/` | `/root/autodl-tmp/checkpoints/exp003/checkpoint-6000/` | 719MB |
| 6500 | `/root/autodl-tmp/checkpoints/exp003_r3only_seed1/checkpoint-6500/` | `/root/autodl-tmp/checkpoints/exp003/checkpoint-6500/` | 719MB |
| 7000 | `/root/autodl-tmp/checkpoints/exp003_r3only_seed1/checkpoint-7000/` | `/root/autodl-tmp/checkpoints/exp003/checkpoint-7000/` | 719MB |

每个 checkpoint 含 15 个文件（adapter_model.safetensors 245MB + optimizer.pt 491MB + tokenizer/config 文件）。

### 2. Eval 脚本路径

```
/root/contrastive_entrain_calib/eval/eval_unified_preset.py
```

### 3. Eval 命令格式

```bash
CUDA_VISIBLE_DEVICES=&lt;GPU> HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
/root/miniconda3/bin/python /root/contrastive_entrain_calib/eval/eval_unified_preset.py \
  --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
  --lora_path /root/autodl-tmp/checkpoints/exp003/checkpoint-&lt;STEP> \
  --data_path /root/contrastive_entrain_calib/data/calibration_v2_1_expanded.jsonl \
  --output_dir /root/contrastive_entrain_calib/results/exp003_d027_eval \
  --exp_id exp003-ckpt&lt;STEP>
```

### 4. 三 GPU 并行 eval 命令

```bash
# GPU 0: ckpt-6000
CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
nohup /root/miniconda3/bin/python /root/contrastive_entrain_calib/eval/eval_unified_preset.py \
  --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
  --lora_path /root/autodl-tmp/checkpoints/exp003/checkpoint-6000 \
  --output_dir /root/contrastive_entrain_calib/results/exp003_d027_eval \
  --exp_id exp003-ckpt6000 > /tmp/eval_6000.log 2>&1 &

# GPU 1: ckpt-6500
CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
nohup /root/miniconda3/bin/python /root/contrastive_entrain_calib/eval/eval_unified_preset.py \
  --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
  --lora_path /root/autodl-tmp/checkpoints/exp003/checkpoint-6500 \
  --output_dir /root/contrastive_entrain_calib/results/exp003_d027_eval \
  --exp_id exp003-ckpt6500 > /tmp/eval_6500.log 2>&1 &

# GPU 2: ckpt-7000
CUDA_VISIBLE_DEVICES=2 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
nohup /root/miniconda3/bin/python /root/contrastive_entrain_calib/eval/eval_unified_preset.py \
  --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
  --lora_path /root/autodl-tmp/checkpoints/exp003/checkpoint-7000 \
  --output_dir /root/contrastive_entrain_calib/results/exp003_d027_eval \
  --exp_id exp003-ckpt7000 > /tmp/eval_7000.log 2>&1 &
```

`--data_path` 有默认值指向同一文件，可省略。是否需要我直接在 28034 上启动这三个 eval？

---
