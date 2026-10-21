# code check grid b split

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check-grid-b-split_20260514T024458_result.json`
- **Structured JSON:** [`f58890ecbf46a3e056f7.json`](../../sessions/f5/f58890ecbf46a3e056f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**已原生支持单 b 值运行。** 不需要改代码。

`pretrain_weighted.py` 已有 `--grid_b_value` 参数（第 210 行），`run_grid_b_seed42.sh` 的 for 循环里也是通过 `--grid_b_value $b` 逐个传入的。

### 单 b 值运行命令模板

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/provenance_weight_training && \
python training/pretrain_weighted.py \
  --data_path data/scored_data.jsonl \
  --output_dir output/models/grid_b&lt;B_DIR>_seed&lt;SEED> \
  --weighting_method grid \
  --grid_b_value &lt;B_VALUE> \
  --model_name models/Qwen/Qwen3-0.6B \
  --num_train_tokens 200000000 \
  --batch_size 4 --gradient_accumulation_steps 4 \
  --max_length 2048 --learning_rate 5e-5 \
  --seed &lt;SEED> --logging_steps 10 \
  --save_steps 500 --eval_steps 500 \
  --save_total_limit 2 --save_only_model \
  --contamination_ratio 0.4
```

其中 `&lt;B_DIR>` 是 b 值的下划线形式（如 `0.5` → `0_5`），`&lt;B_VALUE>` 是实际浮点值，`&lt;SEED>` 是随机种子。

6 个 b 值可以直接拆成 6 个独立任务并行提交。

---
