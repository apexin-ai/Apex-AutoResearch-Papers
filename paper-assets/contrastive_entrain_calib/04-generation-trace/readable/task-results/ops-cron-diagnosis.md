# ops cron diagnosis

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cron-diagnosis_20260521T043855_result.json`
- **Structured JSON:** [`1b7a97b076e2a97a5ef3.json`](../../sessions/1b/1b7a97b076e2a97a5ef3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整结果。

---

## 1. 停滞原因

**没有 auto-pipeline cron。** 平台 `CronList` 返回空，28034 上也没有 crontab 条目或后台 pipeline 进程。所有 eval 都是手动/agent 触发的，最后一批在 **May 21 03:02** 完成后就没人再触发了。

## 2. 当前状态盘点

### 29046 → 28034 SCP 状态

| 系列 | 29046 有 | 28034 已有 | 缺失 |
|------|---------|-----------|------|
| seed1 | 500-7000 | 1000-7000 (含4500) | 500 |
| seed2 | 500-3000 | 500-2500 | **3000** |

### Eval 完成状态

| 系列 | 已 eval | 未 eval（checkpoint 已在 28034） |
|------|--------|-------------------------------|
| seed1 | 1000, 2000, 3000, 4000, 4500, 5500 | **5000, 6000, 6500, 7000** |
| seed2 | 500, 1000, 1500 | **2000, 2500** (+3000 需先 SCP) |

## 3. Eval 命令完整格式

脚本路径：`/root/contrastive_entrain_calib/eval/eval_unified_preset.py`

**seed1 示例（以 ckpt-5000 为例）：**
```bash
cd /root/contrastive_entrain_calib && \
CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 /root/miniconda3/bin/python \
    eval/eval_unified_preset.py \
    --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
    --lora_path /root/autodl-tmp/checkpoints/exp003/checkpoint-5000 \
    --data_path /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl \
    --output_dir /root/contrastive_entrain_calib/results/exp003_d027_eval \
    --exp_id exp003-ckpt5000
```

**seed2 示例（以 ckpt-2000 为例）：**
```bash
cd /root/contrastive_entrain_calib && \
CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 /root/miniconda3/bin/python \
    eval/eval_unified_preset.py \
    --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
    --lora_path /root/autodl-tmp/checkpoints/exp003_s2/checkpoint-2000 \
    --data_path /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl \
    --output_dir /root/contrastive_entrain_calib/results/exp003_s2_unified_eval \
    --exp_id exp003s2-ckpt2000
```

**参数说明：**
- `CUDA_VISIBLE_DEVICES` — GPU 编号
- `--model_path` — 基座模型（Qwen3-8B）
- `--lora_path` — LoRA adapter checkpoint
- `--data_path` — 评估数据集
- `--output_dir` — 结果输出目录
- `--exp_id` — 实验 ID（用于输出文件命名：`{exp_id}_preset_eval.json`）

## 4. 待执行清单

1. **SCP** 29046 的 `exp003_r3only_seed2/checkpoint-3000` → 28034 `/root/autodl-tmp/checkpoints/exp003_s2/checkpoint-3000`
2. **Eval seed1**: ckpt-5000, 6000, 6500, 7000（4 个）
3. **Eval seed2**: ckpt-2000, 2500, 3000（3 个）

需要我现在开始执行这些 eval 吗？可以串行排队跑（每个约 1.5h），也可以分 GPU 并行。

---
