# prep task gh experiments

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_task-gh-experiments_20260516T070940_result.json`
- **Structured JSON:** [`cdc787a1f2bced3d4e41.json`](../../sessions/cd/cdc787a1f2bced3d4e41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部准备完毕。以下是审批卡。

---

## Task G: Format Marker 移除重训 — 审批卡

### 数据准备 ✓
- **原始数据**: `exception_only_{train,test}.jsonl` (4720/1190 samples)
- **Marker 统计**: train 3099/4720 (65.7%), test 843/1190 (70.8%) 包含 `[No exception data in trace]`
- **新数据**: `exception_only_nomarker_{train,test}.jsonl` — marker 替换为空字符串，行数一致，0 残留
- **代码修改**: `train_sft.py` 和 `evaluate.py` 的 `--condition` choices 已加入 `exception_only_nomarker`

### 训练命令 (3 seeds)

**Seed 42** (registry: `exception_only_nomarker_seed42` — PREPARING):
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only_nomarker --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed42 --wandb_project trace-verdict-study --wandb_run_name exception_only_nomarker_seed42 && python eval/evaluate.py --condition exception_only_nomarker --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed42/final/eval_results.json --save_predictions"
```

**Seed 123** (registry: `exception_only_nomarker_seed123` — PREPARING):
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only_nomarker --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed123 --wandb_project trace-verdict-study --wandb_run_name exception_only_nomarker_seed123 && python eval/evaluate.py --condition exception_only_nomarker --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed123/final/eval_results.json --save_predictions"
```

**Seed 456** (registry: `exception_only_nomarker_seed456` — PREPARING):
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only_nomarker --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed456 --wandb_project trace-verdict-study --wandb_run_name exception_only_nomarker_seed456 && python eval/evaluate.py --condition exception_only_nomarker --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed456/final/eval_results.json --save_predictions"
```

---

## Task H: loop_only 多 Seed — 审批卡

### Registry ✓
- `loop_only_seed123` — PREPARING
- `loop_only_seed456` — PREPARING

### 训练命令 (参考 vota_loop_only_seed42 超参)

**Seed 123** (registry: `loop_only_seed123`):
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123 --wandb_project trace-verdict-study --wandb_run_name loop_only_seed123 && python eval/evaluate.py --condition loop_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final/eval_results.json --save_predictions"
```

**Seed 456** (registry: `loop_only_seed456`):
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456 --wandb_project trace-verdict-study --wandb_run_name loop_only_seed456 && python eval/evaluate.py --condition loop_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final/eval_results.json --save_predictions"
```

---

## 共通超参（均继承自已有实验）

| 参数 | 值 |
|------|-----|
| model | Qwen2.5-Coder-7B-Instruct |
| epochs | 3 |
| batch_size | 4 |
| grad_accum | 8 (effective batch=32) |
| lr | 2e-4 |
| warmup | 0.1 |
| max_length | 2048 |
| LoRA r/alpha | 16/32 |
| bf16 | True |
| gradient_checkpointing | True |

## 总计 5 个实验，均可两两并行（各占 1 GPU）

---
