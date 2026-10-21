# harvest bjb1 18228 crm check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb1-18228-crm-check_20260525T174426_result.json`
- **Structured JSON:** [`8be3c1108446332c005b.json`](../../sessions/8b/8be3c1108446332c005b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 1. π0.5 CRM 3-suite 统一训练 — **已完成**

- **Checkpoint**: `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt` (2.4MB, 615,966 params)
- 训练完成时间: May 25 12:41 (50 epochs 全部完成, epoch 46-50 checkpoints 保留)
- 训练数据: 194,485 samples (object 72507 + spatial 60250 + goal 61728)
- 配置: batch_size=256, lr=0.001, obs_dim=2048, K=10, MSE loss + λ_conf=0.1

### 2. precompute-pi05-long-2048-r2 (PID 114507) — **仍在运行**

- GPU 3, 9883MiB, 23% util
- 已处理: 127,000 samples (254 partial files × 500)
- 当前进度: ~16-17 min/shard
- 参考其他 benchmark 规模 (60K-72K) 和 long 的更长 episode (520 vs 280 步)，**预计总量 ~130K-140K，接近完成（~94%）**
- ETA: 约 2-4 小时后完成（~May 26 04:00-06:00 UTC）
- 缓存目录: `/root/autodl-tmp/crm_cache_pi05_2048/long/`, 当前 4.6GB

### 3. 正在运行的 eval 实验 (3个)

| GPU | 进程 | 状态 | 进度 |
|-----|------|------|------|
| GPU 0 | eval_pi05_object_crm_seed42 (PID 601275) | 进行中 | task 3/10, 已跑 ~6h |
| GPU 1 | eval_pi05_long_crm_seed42 (PID 601277) | 进行中 | task 1/10 完成 (70%), 已跑 ~6h |
| GPU 2 | eval_pi05_long_crm_seed43 (PID 625278) | 刚启动 | 模型加载中 |

### 4. 已完成的 eval 结果（bjb1-18228 本地，近 24h）

| 文件 | Benchmark | Mode | Success Rate |
|------|-----------|------|-------------|
| `eval_long_crm_seed42.json` (May 26 00:11) | long | crm_obs_only | **59.0%** |
| `eval_spatial_adaptive_seed47_bjb1.json` (May 25 20:29) | spatial | adaptive_conformal_crm | **81.0%** (trigger_rate=19.1%, τ=0.25) |
| `eval_spatial_vla_only_seed47_n20.json` (May 25 20:27) | spatial | vla_only | **78.5%** |
| `eval_goal_adaptive_pi05_seed42.json` (May 25 16:50) | goal | adaptive_conformal_crm | **0.0%** ⚠️ |
| `eval_object_vla_only_pi05_seed42.json` (May 25 15:59) | object | vla_only | 见文件 |
| `eval_spatial_vla_only_pi05_seed43.json` (May 25 15:58) | spatial | vla_only | 见文件 |
| `eval_object_crm_obs_only_norm0.05_seed48.json` (May 25 06:52) | object | crm_obs_only | **73.5%** |
| `eval_goal_crm_obs_only_norm0.05_seed49.json` (May 25 06:21) | goal | crm_obs_only | **83.5%** |

### 5. 关键发现

- **goal adaptive = 0.0%**: `eval_goal_adaptive_pi05_seed42.json` 所有 10 个 task 全部 0% 成功率，严重异常。可能是 adaptive mode 在 goal benchmark 上有 bug，或 conformal threshold / uncertainty head 配置问题。需要调查。
- **CRM 在 goal 上表现好 (83.5%)，但 adaptive 版本完全失效** — 说明 uncertainty gating 机制可能在 goal benchmark 上错误判断了何时应用 CRM。
- **spatial: adaptive (81.0%) vs vla_only (78.5%)** — CRM adaptive 有微小提升 (+2.5pp)，trigger rate 只有 19.1%。
- **long CRM seed42: 59%** — 已完成但结果偏低，需要对比 vla_only baseline 来判断 CRM 效果。

---
