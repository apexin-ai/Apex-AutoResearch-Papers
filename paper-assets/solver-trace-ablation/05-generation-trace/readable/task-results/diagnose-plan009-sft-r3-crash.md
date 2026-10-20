# diagnose plan009 sft r3 crash

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan009-sft-r3-crash_20260514T114634_result.json`
- **Structured JSON:** [`e74b477800b29cf1e48c.json`](../../sessions/e7/e74b477800b29cf1e48c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**根因**：`wandb.init()` 失败 — 服务器上没有配置 W&B API key（无 `.netrc`、无 `WANDB_API_KEY` 环境变量）。r3 命令传了 `--wandb_project` 和 `--wandb_run`，触发了 `report_to="wandb"`，导致启动即崩。

**修复**：加 `--no_wandb` 标志，去掉 `--wandb_project` 和 `--wandb_run`。

**正确的 r4 提交命令**（已经 dry-run 验证参数解析通过）：
```bash
export CUDA_VISIBLE_DEVICES=N
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py \
  --model_path /root/autodl-tmp/models/Qwen3-4B \
  --data_path data/train_500_seed42.jsonl \
  --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r4 \
  --num_steps 500 --seed 42 --no_wandb
```

**当前阻塞**：两张 GPU 都近满载（GPU 0: 589 MiB free, GPU 1: 6.8 GiB free），无法立即启动 r4，需等现有任务释放 GPU。

Registry 已更新。

---
