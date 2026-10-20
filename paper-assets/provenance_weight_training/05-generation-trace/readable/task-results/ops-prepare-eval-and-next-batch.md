# ops prepare eval and next batch

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare_eval_and_next_batch_20260516T025127_result.json`
- **Structured JSON:** [`d778cb2464f513c2f1ad.json`](../../sessions/d7/d778cb2464f513c2f1ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

---

## 产出 1: Post-hoc Eval 命令模板

**pretrain_weighted.py 无 eval-only 模式**。Eval 通过独立脚本完成。

### 主 eval 工具: `eval_perplexity.py`

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/provenance_weight_training
export HF_HOME=/root/autodl-tmp/.hf_cache

# 单个 checkpoint eval
python eval_perplexity.py \
    --checkpoints output/models/&lt;exp_id>/checkpoint-XXXX \
    --data_path data/human/eval_holdout.jsonl \
    --output_path output/eval_results/&lt;exp_id>_eval.json

# 多个 checkpoint 批量 eval
python eval_perplexity.py \
    --checkpoints output/models/exp1/final output/models/exp2/final \
    --data_path data/human/eval_holdout.jsonl \
    --output_path output/eval_results/batch_eval.json \
    --max_docs 5000
```

### 辅助工具

| 工具 | 用途 |
|---|---|
| `auto_eval_watcher.py` | 守护进程，每60s扫描 output/models/，自动对完成的实验跑 eval |
| `training/extract_train_metrics.py` | 从 trainer_state.json 或 stdout log 提取 train_loss 等指标 |
| `scripts/run_eval_seed42.sh` | 批量 eval grid-b seed42 系列（b=0.5~5.0），可作为模板改写 |

---

## 产出 2: Checkpoint 路径确认

| 实验 | Checkpoints | 大小 | 训练状态 |
|---|---|---|---|
| `contamination_60_ess_only_seed42` | 4500, 5000, 5500 | 各1.2G | 进行中，较晚期 |
| `grid_b0_3_seed42` | 1500, 2000, 2500 | 各1.2G | 进行中 |
| `detect_remove_baseline_seed42` | 500, 1000, 1500 | 各1.2G | 进行中 |
| `contamination_60_tau07_seed42` | 500, 1000 | 各1.2G | 进行中，较早期 |

所有 checkpoint 内均含 `model.safetensors` + `trainer_state.json`，可随时 eval。已有 eval 结果在 `output/eval_results/` 下（24个文件），包括之前的 grid-b 全系列和 nmin ablation。

---

## 产出 3: 下一批脚本就绪状态

| 脚本 | 状态 | 参数检查 |
|---|---|---|
| `run_contamination_60_tau06.sh` | **就绪** | ρ=0.6, τ=0.6, n_min=2, data=scored_data_60.jsonl, seed=42 ✓ |
| `run_nmin5.sh` | **就绪** | n_min=5, data=scored_data.jsonl, tau=0.8, seed=42 ✓ |
| grid_b0_1 单独脚本 | **不存在** | 见下方说明 |
| grid_b0_2 单独脚本 | **不存在** | 见下方说明 |

### `run_grid_b_low_seed42.sh` 问题

该脚本循环跑 b=0.1, 0.2, 0.3 三个值，**但**：
1. **b=0.3 已有实验在跑**（`grid_b0_3_seed42` 已有 checkpoint），再执行此脚本会重复跑 b=0.3
2. **WANDB_MODE=disabled** — 没有 wandb 记录
3. **无 `--eval_data_path` 和 `--eval_steps`** — 无训练中 eval，只能 post-hoc eval
4. **output_dir 命名为 `grid_b_low_b{b}_seed42`**，与现有 `grid_b0_3_seed42` 不一致

**需要创建**: 单独的 `run_grid_b0_1_seed42.sh` 和 `run_grid_b0_2_seed42.sh`（或修改 `run_grid_b_low_seed42.sh` 去掉 b=0.3），并补上 wandb 和 eval 参数。

---
