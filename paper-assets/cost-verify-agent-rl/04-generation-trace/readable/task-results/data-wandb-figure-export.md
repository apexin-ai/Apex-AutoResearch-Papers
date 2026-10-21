# data wandb figure export

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_wandb-figure-export_20260519T155854_result.json`
- **Structured JSON:** [`b7a8c5bc337ea11b830e.json`](../../sessions/b7/b7a8c5bc337ea11b830e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 JSON 文件已导出到 `/root/autodl-tmp/paper_figures/`。

### 导出结果

| 文件 | 大小 | 内容 |
|------|------|------|
| `main_results_training_curves.json` | 11.6KB | Cell A s1: 15 rows, s2: 15; Cell B s1: 14, s2: 14; Cell C s1: 16, s2: 29 |
| `hsweep_cliff.json` | 4.7KB | h=2: 3 val/14 train; h=10: 2/7; h=20: 0/4; h=full: 4/15 |
| `entropy_kl_dynamics.json` | 4.1KB | seed1: 14 rows, seed2: 14 rows |
| `gamma_sweep_curves.json` | 2.7KB | g050: 12, g080: 8, g095: 5, g100: 6 |

### Run ID 修正（与任务描述的差异）

| 原始描述 | 实际使用 | 原因 |
|----------|----------|------|
| Cell B seed1: `jsrvwcfd`/`6liw7fm1` | `6liw7fm1` | jsrvwcfd 无数据 (0 keys) |
| Cell B seed2: `6rqnrlr7` | `w0n74omu` | 6rqnrlr7 无数据 |
| Cell C seed1: 未知 | `7a59sudo` | exp029-alfworld-episode-level, step 15, 数据最多 |
| Cell C seed2: 未知 | `9xs5vfbe` | exp029-episode-level-seed2, step 43, 数据最多 |
| γ=0.95: `d3irreww` | `jv3aa2cj` | d3irreww 是 factorial-h2-episodeadv-seed2，非 gsweep |
| g050: 未知 | `r6rgpd3p` | gsweep-g050-h5-seed1 |
| g080: 未知 | `ltoj940d` | gsweep-g080-h5-seed1 |
| h=10: 未知 | `x09p5xd0` | hsweep-h10-seed1 |

### 缺失

- **h=5**：W&B 中无 hsweep-h5 run
- **h=20 val**: qi8g4f86 只有 4 个 train step，0 个 val step（crashed 太早）
- Metric 名称：实际是 `train/AlfworldSG/success`、`val-env/AlfworldSG/success`、`actor/entropy`、`actor/ppo_kl`（非 `train/success_rate` 等）

---
