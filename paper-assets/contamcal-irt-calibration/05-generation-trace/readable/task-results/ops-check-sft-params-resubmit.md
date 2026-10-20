# ops check sft params resubmit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-sft-params-resubmit_20260515T084702_result.json`
- **Structured JSON:** [`6fefe61ded6e29766fba.json`](../../sessions/6f/6fefe61ded6e29766fba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已获取。

---

## train_sft.py 完整参数列表

| 参数 | 类型 | 必需 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--model-name` | str | **是** | — | HF 模型名 (e.g., `Qwen/Qwen2.5-0.5B`) |
| `--data-path` | str | **是** | — | JSONL 训练数据路径 |
| `--output-dir` | str | **是** | — | 输出目录 |
| `--seed` | int | 否 | 42 | 随机种子 |
| `--max-seq-length` | int | 否 | 2048 | 最大序列长度 |
| `--lora-r` | int | 否 | (DEFAULT_LORA_CONFIG) | LoRA rank |
| `--lora-alpha` | int | 否 | (DEFAULT_LORA_CONFIG) | LoRA alpha |
| `--epochs` | int | 否 | **1** | 训练 epoch 数 |
| `--batch-size` | int | 否 | 4 | Per-device batch size |
| `--grad-accum` | int | 否 | 4 | 梯度累积步数 |
| `--lr` | float | 否 | 2e-4 | 学习率 |
| `--merge` | flag | 否 | False | 合并 LoRA 到完整模型 |
| `--cache-dir` | str | 否 | `/root/autodl-tmp/.hf_cache` | HF 缓存目录 |

**关键差异**：
- 无 `--gpu` 参数（已移除，由框架注入 `CUDA_VISIBLE_DEVICES`）
- 无 `--dosage` 参数（通过 `--data-path` 选择不同 dosage 的 JSONL 文件）
- 无 `--model-path`（用 `--model-name` 指定 HF 模型名，配合 `--cache-dir` 定位本地缓存）
- 有 `--epochs`（默认 1），无 `--max-steps`

## 数据文件路径

| dosage | 路径 |
|--------|------|
| 0.05 | `/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl` |
| 0.25 | `/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl` |

（另有 `sft_data_qc_filtered/` 目录下的 QC 过滤版本）

## 构造好的命令

**命令 A — 1.5B d025 s123：**
```bash
bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/contamcal-irt-calibration/exp001/train_sft.py \
  --model-name Qwen/Qwen2.5-1.5B \
  --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl \
  --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123 \
  --seed 123 \
  --lr 2e-4 \
  --lora-alpha 32 \
  --lora-r 16 \
  --batch-size 2 \
  --grad-accum 8 \
  --cache-dir /root/autodl-tmp/.hf_cache'
```

**命令 B — 1.5B d005 s123：**
```bash
bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/contamcal-irt-calibration/exp001/train_sft.py \
  --model-name Qwen/Qwen2.5-1.5B \
  --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl \
  --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123 \
  --seed 123 \
  --lr 2e-4 \
  --lora-alpha 32 \
  --lora-r 16 \
  --batch-size 2 \
  --grad-accum 8 \
  --cache-dir /root/autodl-tmp/.hf_cache'
```

**注意事项**：
- `--epochs` 默认 1，如果需要多 epoch 训练需显式指定
- 提交时框架自动注入 `CUDA_VISIBLE_DEVICES`，命令中不需要设置
- `--model-name` 传 HF 格式名 `Qwen/Qwen2.5-1.5B`，脚本会从 `--cache-dir` 加载本地缓存

---
