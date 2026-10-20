# ops disk cleanup exec now

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-exec-now_20260515T092952_result.json`
- **Structured JSON:** [`999c42426cd6f5af039a.json`](../../sessions/99/999c42426cd6f5af039a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张 GPU 都空闲，无残留进程。

## 汇报

1. **清理前后 df -h**：
   - 清理前：250G/250G used, 2.1M avail (100%)
   - 清理后：112G/250G used, 139G avail (45%)

2. **plan018 checkpoint-350**：完整（4 个 safetensors），可 resume

3. **--save_total_limit**：不是 CLI 参数，已硬编码在脚本中 `save_total_limit=1`，命令中不需要加

4. **两个实验最终提交命令**：

**exp1-isr-b03-s42-1000 (GPU 0, 从头)**：
```
bash -c "export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000 --num_steps 1000 --beta 0.3 --seed 42 --no_wandb"
```

**plan018-additive-random-b01-s42-1000 (GPU 1, resume from checkpoint-350)**：
```
bash -c "export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000/checkpoint-350 --data_path data/train_500_seed42.jsonl --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000 --num_steps 1000 --beta 0.1 --seed 42 --no_wandb"
```

---
