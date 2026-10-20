# code dpo dryrun and submit

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dpo_dryrun_and_submit_20260513T105244_result.json`
- **Structured JSON:** [`376f1bea6d707e85ca96.json`](../../sessions/37/376f1bea6d707e85ca96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**注意：** 发现服务器上已有 DPO candidate 生成进程在运行（tmux session `dpo_candgen_cuda1`，使用 `--train_file` 参数）。该参数名不在 `--help` 输出中（应为 `--data_file`），可能有问题。

---

## Dry-run 报告

### 验证结果
- **状态：通过**
- 2/2 样本全部成功，2 pairs kept，0 skipped
- 输出格式正确：JSONL，含 `prompt`, `chosen`, `rejected`, `chosen_reward`, `rejected_reward`, `margin`, `all_scores`, `source_index`
- 输出文件：`outputs/dpo_dryrun/dpo_candidates.jsonl` (22.5KB)

### 性能
- 平均 **~65s/sample**（4 candidates, max_new_tokens=2048）
- 总数据集：**3027 samples**
- 单卡预估总时间：3027 × 65s ≈ **54.7 小时**
- 双卡并行预估：**~27.4 小时**

### 两卡并行启动命令

**cuda:0（前半 1514 samples）：**
```bash
cd /root/autodl-tmp/prov_grounded_uie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
PYTHONUNBUFFERED=1 CUDA_VISIBLE_DEVICES=0 nohup python -u generate_dpo_candidates.py \
  --model_path ./outputs/sft/merged \
  --data_file ./data/docred_train.jsonl \
  --output_file ./outputs/dpo_candidates_part0.jsonl \
  --num_candidates 4 \
  --max_new_tokens 2048 \
  --top_k 20 --top_p 0.95 \
  --max_samples 1514 \
  --resume_from 0 \
  --device cuda:0 \
> /tmp/dpo_candgen_gpu0.log 2>&1 &
```

**cuda:1（后半 1513 samples）：**
```bash
cd /root/autodl-tmp/prov_grounded_uie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
PYTHONUNBUFFERED=1 CUDA_VISIBLE_DEVICES=1 nohup python -u generate_dpo_candidates.py \
  --model_path ./outputs/sft/merged \
  --data_file ./data/docred_train.jsonl \
  --output_file ./outputs/dpo_candidates_part1.jsonl \
  --num_candidates 4 \
  --max_new_tokens 2048 \
  --top_k 20 --top_p 0.95 \
  --max_samples 1513 \
  --resume_from 1514 \
  --device cuda:0 \
> /tmp/dpo_candgen_gpu1.log 2>&1 &
```

### 输出路径
- `./outputs/dpo_candidates_part0.jsonl` — samples 0-1513
- `./outputs/dpo_candidates_part1.jsonl` — samples 1514-3026
- 完成后合并：`cat outputs/dpo_candidates_part0.jsonl outputs/dpo_candidates_part1.jsonl > outputs/dpo_candidates_all.jsonl`

---
