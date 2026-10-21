# prep eval commands

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_eval_commands_20260516T010304_result.json`
- **Structured JSON:** [`121a0017fd43300b51ae.json`](../../sessions/12/121a0017fd43300b51ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。以下是完整报告。

---

## 训练进度

| 实验 | 进度 | ETA |
|---|---|---|
| `contamination_60_uniform_seed42` | **已完成** (6103/6103) | — |
| `contamination_60_grid_b0_5_seed42` | 89% (5415/6103) | ~24 min |
| `contamination_60_seed42_r2` | 81% (4939/6103) | ~43 min |
| `contamination_60_ess_only_seed42` | 42% (2558/6103) | ~2h05m |

注意：uniform_seed42 的 EXIT_CODE=129 (SIGHUP)，但 model 已成功保存到 `final/`。

## Eval 脚本确认

- **位置**: `/root/provenance_weight_training/eval_perplexity.py`（在项目根目录，非 `eval/` 子目录）
- **参数**: `--checkpoints` (nargs="+"), `--data_path`, `--max_docs` (default 5000), `--max_length` (default 2048), `--output_path`
- **注意**: 脚本**没有** `--stride` 和 `--fp16` 参数。stride 由 `max_length // 2` 自动计算，fp16 通过 `torch.float16` 硬编码
- 支持多 checkpoint 批量 eval（数据只加载一次）

## Eval holdout 数据

- `data/human/eval_holdout.jsonl`: 227MB, 67,823 行 ✓

## Checkpoint 目录

4 个 output dir 均已存在。uniform_seed42 已有 `final/` 子目录；其余 3 个训练完成后也会生成 `final/`。

## 4 条 Eval 命令

**1. contamination_60_uniform_seed42**（可立即执行）
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python eval_perplexity.py --checkpoints output/models/contamination_60_uniform_seed42/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --output_path eval_results_contamination_60_uniform_seed42.json
```

**2. contamination_60_grid_b0_5_seed42**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python eval_perplexity.py --checkpoints output/models/contamination_60_grid_b0_5_seed42/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --output_path eval_results_contamination_60_grid_b0_5_seed42.json
```

**3. contamination_60_seed42_r2**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python eval_perplexity.py --checkpoints output/models/contamination_60_seed42_r2/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --output_path eval_results_contamination_60_seed42_r2.json
```

**4. contamination_60_ess_only_seed42**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python eval_perplexity.py --checkpoints output/models/contamination_60_ess_only_seed42/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --output_path eval_results_contamination_60_ess_only_seed42.json
```

**批量一次性 eval（训练全部完成后推荐）：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python eval_perplexity.py \
  --checkpoints \
    output/models/contamination_60_uniform_seed42/final \
    output/models/contamination_60_grid_b0_5_seed42/final \
    output/models/contamination_60_seed42_r2/final \
    output/models/contamination_60_ess_only_seed42/final \
  --data_path data/human/eval_holdout.jsonl \
  --max_docs 5000 \
  --output_path eval_results_contamination_60_all.json
```

## 4 条 Train Loss 提取命令

```bash
# 1. uniform_seed42
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/extract_train_metrics.py --output_dir output/models/contamination_60_uniform_seed42 --log_file ~/runs/provenance_weight_training/contamination_60_uniform_seed42.log

# 2. grid_b0_5_seed42
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/extract_train_metrics.py --output_dir output/models/contamination_60_grid_b0_5_seed42 --log_file ~/runs/provenance_weight_training/contamination_60_grid_b0_5_seed42.log

# 3. seed42_r2
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/extract_train_metrics.py --output_dir output/models/contamination_60_seed42_r2 --log_file ~/runs/provenance_weight_training/contamination_60_seed42_r2.log

# 4. ess_only_seed42
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/extract_train_metrics.py --output_dir output/models/contamination_60_ess_only_seed42 --log_file ~/runs/provenance_weight_training/contamination_60_ess_only_seed42.log
```

## 磁盘/内存风险

| 分区 | 总量 | 已用 | 可用 | 风险 |
|---|---|---|---|---|
| / (root) | 30G | 16G (53%) | 15G | **低风险** — eval 只写小 JSON 结果文件 |
| /root/autodl-tmp | 250G | 153G (62%) | 98G | **无风险** |

Eval 过程中 GPU 内存需加载一个 model（fp16），eval 完后 `del model + cuda.empty_cache()`。只要训练进程先结束释放 GPU 显存即可，不会冲突。**注意不要在训练还在跑时启动 eval——会 OOM。**

---
