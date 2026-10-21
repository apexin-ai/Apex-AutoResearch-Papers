# prep plan006 prolog readiness

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_plan006-prolog-readiness_20260514T085922_result.json`
- **Structured JSON:** [`a3bf9abac951a3b639c3.json`](../../sessions/a3/a3bf9abac951a3b639c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有检查完成。写 readiness report。

---

## Plan006 Prolog Exec-Only GRPO — Readiness Report

| # | 检查项 | 状态 | 说明 |
|---|--------|------|------|
| 1 | Config 文件 | **PASS** | `configs/grpo_prolog_exec_only.yaml` 存在。`logic_type: prolog`, `reward_mode: execution_only`, `solver: prolog`, `data_path: data/train_500_seed42.jsonl`（C001 合规），`model_path: /root/autodl-tmp/models/Qwen3-4B` |
| 2 | 训练数据 | **PASS** | `data/train_500_seed42.jsonl` 存在（500条）。数据只有 FOL 字段无 prolog 字段，但 **不影响训练**：`build_prolog_dataset` 仅用 `context`+`question` 构建 prompt（两者都存在），exec-only reward 只评估模型生成的 Prolog 是否可执行，不依赖 ground truth prolog 字段 |
| 3 | 训练脚本 | **PASS** | `train_grpo.py` 完整支持 `logic_type=prolog`：专用 prompt template、`build_prolog_dataset`、`prolog_sta_reward`/`fast_prolog_sta_reward` |
| 4 | Eval 脚本 | **PASS** | `eval_sta.py` 支持 `--logic_type prolog`，有独立的 Prolog prompt 和 reward 函数 |
| 5 | SWI-Prolog | **PASS** | `/usr/bin/swipl` 存在（symlink）。`PrologSolver` 通过 subprocess 调用 swipl |
| 6 | Dry-run import | **SKIPPED** | ssh_read_only 不允许 `;`/`&&`（conda 激活需要）。需在训练前用 ssh_execute 验证 |
| 7 | 磁盘空间 | **PASS** | `/root/autodl-tmp` 可用 112GB，3 runs 需 ~30GB，充足 |

### 额外发现

- **C003 合规**：`save_total_limit=1` 在 `train_grpo.py:419` 硬编码，不需要 config 指定
- **WARNING — `no_wandb: true`**：config 禁用了 wandb。如需实验追踪，启动时加 `--no_wandb false` 或修改 config
- **seed 需命令行覆盖**：config 硬编码 `seed: 42`，多 seed 实验需 `--seed N`

### 预期训练命令（3 seeds）

```bash
# 每个 seed 单独启动，遵守 C002: 必须 export CUDA_VISIBLE_DEVICES
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/solver-trace-ablation
export CUDA_VISIBLE_DEVICES=0   # 根据 GPU 释放情况选卡

# Seed 42
nohup python scripts/train_grpo.py \
  --config configs/grpo_prolog_exec_only.yaml \
  --seed 42 \
  --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s42 \
  --wandb_run plan006_prolog_exec_s42 \
  > /root/autodl-tmp/outputs/plan006_s42.log 2>&1 &

# Seed 43
nohup python scripts/train_grpo.py \
  --config configs/grpo_prolog_exec_only.yaml \
  --seed 43 \
  --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43 \
  --wandb_run plan006_prolog_exec_s43 \
  > /root/autodl-tmp/outputs/plan006_s43.log 2>&1 &

# Seed 44
nohup python scripts/train_grpo.py \
  --config configs/grpo_prolog_exec_only.yaml \
  --seed 44 \
  --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s44 \
  --wandb_run plan006_prolog_exec_s44 \
  > /root/autodl-tmp/outputs/plan006_s44.log 2>&1 &
```

注意：两卡当前满载（plan002 s43/s44），3 个 seed 需排队或等 GPU 释放。单卡可同时跑 1 个 run（4B 模型 + num_generations=8）。

### 启动前必做
1. **ssh_execute dry-run**：验证 `from scripts.train_grpo import *` 无 import 错误
2. 确认 GPU 释放后再提交
3. 提交后 `nvidia-smi` 验证只占用分配的 GPU（C002）

---
