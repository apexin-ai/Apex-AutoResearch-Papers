# verify bjb2 cache and logs

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_bjb2-cache-and-logs_20260514T181913_result.json`
- **Structured JSON:** [`5739579b0c596fa41315.json`](../../sessions/57/5739579b0c596fa41315.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕，汇总如下：

---

## Cache 文件 (`/root/autodl-tmp/crm_cache/`)

| 目录 | 状态 |
|------|------|
| `spatial/` | 8 文件，含 5 个 partial + 3 个合并文件 + manifest |
| `object/` | **空** |

### spatial cache tensor shapes

| 文件 | Shape | 说明 |
|------|-------|------|
| `obs_features.pt` | `[2402, 960]` | 2402 samples, obs_dim=960 |
| `k_samples.pt` | `[2402, 10, 5, 6]` | K=10 rollouts, h_eff=5 steps, 6 action dims |
| `expert_actions.pt` | `[2402, 5, 6]` | h_eff=5, action_dim=6 |
| `partial_s0_0_500.pt` | dict: obs `[500,960]`, ks `[500,10,5,6]`, ea `[500,5,6]` | 500-sample chunk |

manifest: `n_samples=2402, K=10, obs_dim=960, action_dim=6, h_eff=5`

k_samples 值域: min=-8.80, max=19.25, mean=0.095 (原始 VLA action samples)
expert_actions 值域: min=-0.9375, max=0.9375, mean=0.015

---

## norm_stats.pt

| Key | Shape | 值摘要 |
|-----|-------|--------|
| `ba_mean` | `[30]` | base action mean (5步×6维) |
| `ba_std` | `[30]` | 范围 0.28~1.31 |
| `uf_full_mean` | `[40]` | full uncertainty features，含 30 per-DoF conformal + 10 aggregated |
| `uf_full_std` | `[40]` | 范围 0.19~2.14 |
| `uf_scalar_mean` | `[3]` | `[5.27, 1.86, -1.61]` |
| `uf_scalar_std` | `[3]` | `[1.41, 0.17, 1.68]` |
| `obs_mean` | `[960]` | range [-12.09, 8.83] |
| `obs_std` | `[960]` | range [0.033, 0.74] |
| `n_samples` | scalar | 2402 |

归一化统计看起来合理，uf_full 的 mean/std 量级在 O(1) 范围，说明归一化修复生效了（之前 1500x scale 差异已消除）。

---

## 训练进度

| 训练任务 | Epoch | train_loss | val_loss (best) | lr | 状态 |
|----------|-------|------------|-----------------|-----|------|
| crm-train-v3-perdof (181668) | 36/50 | 1.912 | **1.1927** | 2.90e-03 | 持续下降 |
| crm-train-v3-scalar-unc (181896) | 36/50 | 1.934 | **1.1952** | 2.90e-03 | 持续下降 |
| crm-train-v3-obs-only (181973) | 36/50 | 1.879 | **1.1966** | 2.90e-03 | 持续下降 |

三个训练全部在 epoch 36/50，val_loss 每 epoch 都在创 new best，收敛健康。perdof 当前 val_loss 最低（1.1927），obs-only 最高（1.1966），差距不大。

---

## Eval 进度 (eval-vla-mean-spatial, PID 143106)

mode=vla_only, baseline_mode=mean, spatial benchmark

| Task | Success Rate |
|------|-------------|
| between plate and ramekin | 70% (7/10) |
| next to ramekin | **100%** (10/10) |
| from table center | 0% (0/10) |
| on cookie box | 30% (3/10) |
| in top drawer | 0% (0/10) |
| on ramekin | 0% (0/10) |
| next to cookie box | 80% (8/10) |
| on stove | **进行中** (rollout 5/10, 0/5) |

已完成 7/10 tasks，第 8 个进行中。

---

## GPU 状态

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| RTX 4090 D | 4011 / 24564 MiB (16%) | **96%** | eval(2444MB) + 3×train(~510MB each) |

4 个进程全部活跃，GPU 高负载运行。

---
