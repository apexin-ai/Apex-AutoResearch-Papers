# train plan016 extended 1000 s42

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan016-extended-1000-s42_20260514T052804_result.json`
- **Structured JSON:** [`b60a75eb14b38d5c0508.json`](../../sessions/b6/b60a75eb14b38d5c0508.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已注册，训练命令已准备。

## 结果

**实验 plan016-extended-1000-s42** 已注册为 PENDING。

**训练命令：**
```bash
export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --output_dir /root/autodl-tmp/outputs/plan016_extended_1000_s42
```

**⚠️ 磁盘空间不足：** `/root/autodl-tmp` 仅剩 6.4G，需要 ~15G。提交前必须清理旧实验（如 `plan001_exec_only_s43_r4` 46G 或 `plan001_exec_only_s44` 31G，均为 negative/done）。

`save_total_limit=1` 和 `log_completions=False` 已在脚本硬编码，无需额外参数。预估运行 ~2h。

---
