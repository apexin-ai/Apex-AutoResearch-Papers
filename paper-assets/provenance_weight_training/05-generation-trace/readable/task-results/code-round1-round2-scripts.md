# code round1 round2 scripts

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_round1_round2_scripts_20260515T193239_result.json`
- **Structured JSON:** [`be37019b08768d0f1c07.json`](../../sessions/be/be37019b08768d0f1c07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。产出摘要：

## 代码修改

**`training/pretrain_weighted.py`** — 添加 `--shuffle_scores` flag（4 处改动）：argparse 参数、WeightedTrainer 构造函数、compute_loss 中 per-batch shuffle 逻辑、trainer 实例化传参

## 新增辅助脚本

| 文件 | 用途 |
|---|---|
| `scripts/filter_high_qscore.py` | 按 q_score 阈值过滤数据（detect-and-remove 用） |

## 7 个训练脚本

### Round 1（4 个）

| 脚本 | 实验 ID | 关键差异 |
|---|---|---|
| `scripts/run_detect_remove.sh` | p1_baseline_detect_remove | 过滤 q_score>0.5 后 uniform 训练 |
| `scripts/run_random_reweight.sh` | p1_baseline_random_reweight | adaptive + `--shuffle_scores`（per-batch 随机打乱 q_score） |
| `scripts/run_rho06_uniform.sh` | p0_contamination_60_uniform | rho=0.6 数据, uniform |
| `scripts/run_rho06_adaptive.sh` | p0_contamination_60_adaptive | rho=0.6 数据, adaptive, tau=0.8, n_min=2 |

### Round 2（3 个）

| 脚本 | 实验 ID | 关键差异 |
|---|---|---|
| `scripts/run_rho06_grid_b05.sh` | p0_contamination_60_grid_b0_5 | rho=0.6, grid b=0.5 |
| `scripts/run_batchsize16.sh` | p0_batchsize_16 | bs=16, grad_accum=1, n_min=2（覆盖自动计算的 8） |
| `scripts/run_nmin5.sh` | p0_nmin_5 | n_min=5 > bs=4 → b*=0 always → uniform 退化 |

### 注意事项
- rho=0.6 脚本依赖 `data/scored_data_rho06.jsonl`（尚未生成，需先跑 `scripts/run_prepare_rho06.sh`）
- detect_remove 首次运行时自动生成过滤数据文件 `data/scored_data_filtered_t05.jsonl`
- 所有脚本共享参数：200M tokens, Qwen3-0.6B, lr=5e-5, max_length=2048, seed=42, wandb 开启

---
