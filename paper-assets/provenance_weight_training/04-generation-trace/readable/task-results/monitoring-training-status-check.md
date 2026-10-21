# monitoring training status check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitoring_training-status-check_20260517T205037_result.json`
- **Structured JSON:** [`e654725646205109d07d.json`](../../sessions/e6/e654725646205109d07d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B API 有参数问题，但从 logs 已获得足够信息。汇总如下：

## 训练进度总览

| exp_id | server | gpu | step/total | train_loss | ETA | 状态 |
|--------|--------|-----|-----------|------------|-----|------|
| grid_b0_3_seed123_r2 | westd-30476 | cuda:1 | 2249/8477 | — | ~32min | RUNNING |
| rho02_adaptive_tau08_seed42 | westd-30476 | cuda:2 | 3948/6103 | 2.81 (weighted) | ~1h28m | RUNNING |
| batchsize16_nmin8_r2* | westd-30476 | cuda:3 | 1925/6103 | 2.71 | ~2h51m | RUNNING |
| qwen06b_uniform_seed42 | westd-41312 | cuda:0 | 4406/6103 | 2.04 | ~59min | RUNNING |
| ess_only_seed456* | westd-41312 | cuda:1 | 2797/6103 | 2.96 (weighted) | ~1h56m | RUNNING |
| ess_only_seed123* | westd-41312 | cuda:2 | 2895/6103 | 1.69 (weighted) | ~1h53m | RUNNING |
| random_reweight_seed456 | westd-41312 | cuda:3 | 3192/8477 | — | ~27min | RUNNING |

## GPU 利用率

**westd-30476** (4x H800 97GB):
| GPU | Util | VRAM |
|-----|------|------|
| 0 | 100% | 75.0/97.9 GB |
| 1 | 99% | 75.0/97.9 GB |
| 2 | 99% | 46.5/97.9 GB |
| 3 | 100% | 71.2/97.9 GB |

**westd-41312** (4x H800 97GB):
| GPU | Util | VRAM |
|-----|------|------|
| 0 | 100% | 46.5/97.9 GB |
| 1 | 100% | 75.0/97.9 GB |
| 2 | 100% | 75.0/97.9 GB |
| 3 | 73% | 75.0/97.9 GB |

## 备注

1. **文件名不一致**: `batchsize16_nmin8_r3` 实际是 `r2`；`ess_only_seed456_r2` / `ess_only_seed123_r2` 实际无 `_r2` 后缀
2. **total_steps 不同**: `grid_b0_3_seed123_r2` 和 `random_reweight_seed456` 总步数是 8477（非 6103），速度 ~3.25 it/s，说明它们用了不同 batch size 或 eval 配置
3. **ess_only 两个实验已跑 5h+** 但只到 46-47%，速度 2.1s/it——按当前速率还需近 2h，说明可能中间有重启或暂停
4. **最快完成**: random_reweight_seed456 (~27min) 和 grid_b0_3_seed123_r2 (~32min)
5. **最慢完成**: batchsize16_nmin8_r2 (~2h51m)

---
