# data verify contamination 60

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data-verify_contamination_60_20260515T201036_result.json`
- **Structured JSON:** [`c4c5c74cc69691a4b83c.json`](../../sessions/c4/c4c5c74cc69691a4b83c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出汇总

### 1. 数据验证报告

| 指标 | 值 | 预期 | 状态 |
|------|-----|------|------|
| 文件 | `scored_data_60.jsonl` (907MB) | ~907MB | OK |
| 行数 | 371,499 | 371,499 | OK |
| synthetic/human | 222,900 / 148,599 | ρ=0.6 | OK |
| JSON 格式 | 7 字段 (text/depth/source_model/prompt_tokens/generated_tokens/decoding/q_score) | — | OK |
| q_score mean | 0.6243 | — | OK |
| q_score median | 0.7753 | — | OK |
| q_score std | 0.3703 | — | OK |

符号链接 `scored_data_rho06.jsonl → scored_data_60.jsonl` 已建立。

### 2. contamination_60_seed42 训练命令

与 adaptive_fix_seed42 仅 2 处差异：`--data_path` 和 `--contamination_ratio`。

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py \
  --data_path data/scored_data_60.jsonl \
  --output_dir output/models/contamination_60_seed42 \
  --model_name models/Qwen/Qwen3-0.6B \
  --weighting_method adaptive \
  --contamination_ratio 0.6 \
  --num_train_tokens 200000000 \
  --batch_size 4 \
  --gradient_accumulation_steps 4 \
  --learning_rate 5e-5 \
  --max_length 2048 \
  --seed 42 \
  --save_steps 500 \
  --logging_steps 10 \
  --bf16 \
  --save_total_limit 3 \
  --save_only_model \
  --tau 0.8 \
  --n_min 2"
```

脚本默认 `tau=0.8`, `n_min=max(2, batch_size//2)=2`，此处显式指定保证可复现。

### 3. Registry

实验 `contamination_60_seed42` 已注册为 QUEUED，parent=`adaptive_fix_seed42`，数据验证结果已写入 notes。可直接提交训练。

---
