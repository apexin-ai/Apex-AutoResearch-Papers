# code plan009 sft fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan009-sft-fix_20260514T105721_result.json`
- **Structured JSON:** [`4f817a78246efa6afd51.json`](../../sessions/4f/4f817a78246efa6afd51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇总：

### 修改内容
- `save_total_limit=3` → `save_total_limit=1`（C003 约束，已修复）

### Qwen3-4B 路径
`/root/autodl-tmp/models/Qwen3-4B/`（3 个 safetensors shard，完整）

### 脚本状态
- 模型路径参数化（`--model_path`），无硬编码
- `--output_dir` 由调用方指定，可正确指向 `/root/autodl-tmp/outputs/`
- `--help` 正常工作，所有参数可配置

### 最终启动命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export CUDA_VISIBLE_DEVICES=0
cd /root/solver-trace-ablation
python3 scripts/train_sft.py \
  --model_path /root/autodl-tmp/models/Qwen3-4B \
  --data_path data/train_500_seed42.jsonl \
  --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s42 \
  --max_steps 200 \
  --seed 42 \
  --wandb_project solver-trace-ablation \
  --wandb_run plan009_sft_s42
```

注意：`CUDA_VISIBLE_DEVICES` 需根据实际 GPU 空闲情况设置（C002/C005 约束），启动前用 `nvidia-smi` 确认。

### 无其他问题
脚本已可用于 Qwen3-4B SFT baseline 训练。

---
