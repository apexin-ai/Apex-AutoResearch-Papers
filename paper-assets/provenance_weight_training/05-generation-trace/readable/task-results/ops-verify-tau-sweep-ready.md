# ops verify tau sweep ready

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_tau_sweep_ready_20260515T101127_result.json`
- **Structured JSON:** [`d9cb4f7754e6578ddbe2.json`](../../sessions/d9/d9cb4f7754e6578ddbe2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。所有结果如下：

---

## 1. 参数验证 Checklist（4 脚本全部通过）

| 参数 | τ=0.5 | τ=0.7 | τ=0.9 | τ=0.95 |
|------|-------|-------|-------|--------|
| `--tau` 值正确 | ✅ 0.5 | ✅ 0.7 | ✅ 0.9 | ✅ 0.95 |
| `--output_dir` 正确 | ✅ tau_0.5_seed42 | ✅ tau_0.7_seed42 | ✅ tau_0.9_seed42 | ✅ tau_0.95_seed42 |
| `--weighting_method adaptive` | ✅ | ✅ | ✅ | ✅ |
| `--seed 42` | ✅ | ✅ | ✅ | ✅ |
| `--bf16` | ✅ | ✅ | ✅ | ✅ |
| `--contamination_ratio 0.4` | ✅ | ✅ | ✅ | ✅ |
| `--batch_size 4 --grad_accum 4` | ✅ | ✅ | ✅ | ✅ |
| `--learning_rate 5e-5` | ✅ | ✅ | ✅ | ✅ |
| `--num_train_tokens 200000000` | ✅ | ✅ | ✅ | ✅ |
| `--model_name models/Qwen/Qwen3-0.6B` | ✅ | ✅ | ✅ | ✅ |
| `--save_steps 500 --save_total_limit 2 --save_only_model` | ✅ | ✅ | ✅ | ✅ |
| `--logging_steps 10` | ✅ | ✅ | ✅ | ✅ |
| `WANDB_MODE=disabled` | ✅ | ✅ | ✅ | ✅ |
| 无 `--eval_data_path` / `--eval_steps` | ✅ | ✅ | ✅ | ✅ |
| `set -e` | ✅ | ✅ | ✅ | ✅ |

## 2. 与 tau_0.6 的 diff

已逐行比对所有 5 个脚本内容，确认：**唯一差异是 `--tau` 值和 `--output_dir` 路径**，其余参数完全一致。

## 3. output_dir 冲突检查

4 个目录均不存在，无冲突 ✅

## 4. 一键提交命令（按 GPU 释放顺序）

```
GPU 释放顺序 → τ 值:
cuda:1 (~12:50) → tau_0.5_seed42
cuda:0 (~13:18) → tau_0.7_seed42
cuda:3 (~13:43) → tau_0.9_seed42
cuda:2 (~14:25) → tau_0.95_seed42
```

**提交命令：**

**① τ=0.5（cuda:1 释放后）**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.5_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.5 --bf16"
```

**② τ=0.7（cuda:0 释放后）**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.7_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.7 --bf16"
```

**③ τ=0.9（cuda:3 释放后）**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.9_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.9 --bf16"
```

**④ τ=0.95（cuda:2 释放后）**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.95_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.95 --bf16"
```

4 组脚本全部就绪，参数正确，可按 GPU 释放顺序依次提交。

---
