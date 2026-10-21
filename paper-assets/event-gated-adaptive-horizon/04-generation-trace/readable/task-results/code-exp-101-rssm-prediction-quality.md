# code exp 101 rssm prediction quality

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_101_rssm_prediction_quality_20260526T041155_result.json`
- **Structured JSON:** [`25cce839d739fcf2d4ed.json`](../../sessions/25/25cce839d739fcf2d4ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

## 产出

### 1. 分析脚本
**`scripts/analyze_rssm_exp101.py`** — 单 checkpoint RSSM prediction quality 分析
- 参数：`--checkpoint_dir`, `--task`, `--label`, `--seed`, `--n_episodes`, `--device`, `--output`
- 自动检测 obs 维度和 model label
- 从 train_eps 加载 episode，采样 transitions
- 对每个 transition 做 dt=1 (一步 img_step) 和 dt=2 (两步连续 img_step) 预测
- 输出 JSON 带完整 provenance metadata

### 2. 批量运行脚本
**`scripts/run_exp101_all.sh`** — 遍历所有可用 checkpoint
- 用法：`bash scripts/run_exp101_all.sh cuda:1`
- 输出目录：`analysis_exp101/`

### 3. Dry-run 结果 (PASSED)
| 指标 | dt=1 | dt=2 | ratio |
|------|------|------|-------|
| obs_mse | 6.664 | 12.252 | **1.84x** |
| reward_mae | 0.035 | 0.047 | **1.32x** |

exp_008d (trained_dt_emb), 5 episodes, 200 transitions, 49.1s on cuda:1

### 4. 可用 checkpoint（全部 6 个存在）
| Checkpoint | Label | Task |
|---|---|---|
| exp_008d_civo_trigger_s4 | trained_dt_emb | walker |
| exp_009d_baseline_walker_s1 | baseline | walker |
| exp_009c_no_dt_emb_s2 | no_dt_emb | walker |
| exp_084_frozen_dt_emb_walker_s0 | frozen_dt_emb | walker |
| exp_092_cheetah_no_dt_emb_s1 | no_dt_emb | cheetah |
| exp_093_cheetah_no_dt_emb_s2 | no_dt_emb | cheetah |

### 5. 运行时间预估
- 单模型 5 ep (dry-run): ~50s GPU
- 单模型 n=1000 (约 112 个可用 episode): 受 `static_scan` O(n²) 拼接限制，预估 **15-20 min/model** on GPU
- 全部 6 模型: **~1.5-2h** on GPU

---
