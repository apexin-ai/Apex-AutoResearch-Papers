# code dr epoch matched and eval prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dr_epoch_matched_and_eval_prep_20260518T071952_result.json`
- **Structured JSON:** [`d93ef19e613598e56382.json`](../../sessions/d9/d93ef19e613598e56382.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All information gathered. Here's the full summary:

---

## 1. 1 Epoch 步数和 Token 数

| 参数 | 值 |
|------|-----|
| n_samples (q05) | 153,725 |
| batch_size | 4 |
| gradient_accumulation_steps | 4 |
| effective_batch_size | 16 |
| max_length | 2048 |
| tokens_per_step | 32,768 |
| **dataloader_drop_last** | **True** (代码第384行附近) |

计算（因为 drop_last=True，用 floor 而非 ceil）:
- micro_batches/epoch = 153,725 // 4 = 38,431
- **1 epoch = 38,431 // 4 = 9,607 optimizer steps**
- **1 epoch tokens = 9,607 × 32,768 = 314,867,712 (~315M)**

当前 seed123/456 的 max_steps=6103（200M tokens）= 6103/9607 = **0.635 epochs**。

---

## 2. Epoch-matched 训练命令

**推荐方式：不传 `--num_train_tokens` 和 `--max_steps`**，让 `--num_train_epochs 1`（默认值）生效，Trainer 自动算出 9,607 步：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py \
  --data_path data/scored_data_filtered_q05.jsonl \
  --output_dir /root/autodl-tmp/output/models/detect_remove_q05_epoch_matched_seed42 \
  --model_name models/Qwen/Qwen3-0.6B \
  --weighting_method uniform \
  --contamination_ratio 0.4 \
  --n_min 2 --tau 0.8 \
  --batch_size 4 \
  --gradient_accumulation_steps 4 \
  --learning_rate 5e-5 \
  --max_length 2048 \
  --seed 42 \
  --save_steps 500 \
  --logging_steps 10 \
  --bf16 \
  --save_total_limit 3
```

或者显式指定：加 `--max_steps 9607`（`pretrain_weighted.py` 支持此参数，优先级高于 `num_train_tokens`）。

---

## 3. 各阈值下保留样本数

| 阈值 t | 保留条件 | 样本数 | 占比 | 文件状态 |
|--------|----------|--------|------|----------|
| 0.1 | q ≤ 0.1 | 55,799 | 15.0% | **刚创建** `scored_data_filtered_q01.jsonl` |
| 0.3 | q ≤ 0.3 | 116,935 | 31.5% | 已有 `scored_data_filtered_q03.jsonl` |
| 0.5 | q ≤ 0.5 | 153,725 | 41.4% | 已有 `scored_data_filtered_q05.jsonl` |
| 0.7 | q ≤ 0.7 | 184,908 | 49.8% | 已有 `scored_data_filtered_q07.jsonl` |
| 0.9 | q ≤ 0.9 | 228,743 | 61.6% | **未创建** |

---

## 4. 关于 q01 的语义澄清

t=0.1 是**最激进**的过滤：只保留 q≤0.1 的 55,799 个"最干净"样本（15%），去掉 85% 数据。这不是"保留几乎所有数据"，而是相反。

如果你想要的"极端宽松阈值（保留几乎全部数据）"，那应该是 **t=0.9**（保留 228,743 样本，61.6%）。请确认 q01 的用途方向。

---
