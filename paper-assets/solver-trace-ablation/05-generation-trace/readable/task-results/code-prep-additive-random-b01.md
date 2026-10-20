# code prep additive random b01

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-additive-random-b01_20260514T065015_result.json`
- **Structured JSON:** [`f3b1983fad38116aa0a6.json`](../../sessions/f3/f3b1983fad38116aa0a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 报告

**状态：PASS**

- 2 步训练完成，无错误
- reward_log.jsonl 包含 2 步数据，`random_mean` 字段确认 random 成分活跃
- Step 1: reward=0.128, prove_rate=12.5%, random=0.441
- Step 2: reward=0.0, prove_rate=0%（无证明→reward=0，符合 `r = r_exec · (1 + 0.1 · random)` 语义）
- 模型保存因 /tmp 空间不足失败（不影响训练验证，正式训练用 autodl-tmp）

**正式训练命令（plan018）：**

```bash
bash -c "export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42 --wandb_project solver-trace-ablation --wandb_run plan018_additive_random_b01"
```

**参数说明：**
- Config: `configs/grpo_additive_random.yaml`（复用 plan017 config，CLI `--beta 0.1` 覆盖 config 中的 0.3）
- 无需创建新 config 文件
- output_dir 在 `/root/autodl-tmp/` 避免磁盘问题
- save_total_limit=1 已在 train_grpo.py 中硬编码（line 420）

---
