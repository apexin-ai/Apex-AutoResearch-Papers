# infra status check both servers

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_status_check_both_servers_20260521T014037_result.json`
- **Structured JSON:** [`0bc1256ce2ed95dd747c.json`](../../sessions/0b/0bc1256ce2ed95dd747c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-34685 (occ 训练)

| Seed | 主PID | GPU | Util | 显存 | 最新 Checkpoint | Step |
|------|-------|-----|------|------|----------------|------|
| occ_s0 | 27667 | 0 | 99% | 62 GB | 32500_chkpt (09:15) | ~32500+ |
| occ_s1 | 58802 (重启) | 1 | 99% | 62 GB | 7500_chkpt (09:16) | ~7500+ |
| occ_s2 | 29970 | 2 | 95% | 62 GB | 32500_chkpt (09:15) | ~32500+ |
| — | — | 3 | 100% | 0 MB | — | 空闲 |

- **occ_s1 已重启**: 原始 PID 28827 已死，当前 PID 58802。restart log 最后一条: `step=1600, occ_loss=0.0099, action_loss=0.1260`（log 滞后，实际已到 7500+）
- **occ_s0/s2 进度一致**，~32500/50000（65%）
- **monitor_and_eval_occ.sh**: 存在，监控 PID 27667/28827/29970，训练结束后自动触发 eval。**注意**: PID 28827(s1 原进程) 已死，monitor 可能已误判 s1 训练完成并触发了一次 eval（但 eval 结果目录中没有 occ_s1 结果，所以可能只是检测到退出但没找到 checkpoint）

## westd-10894 (eval)

- **eval 进程**: 无，全部完成
- **GPU**: 4 卡全空闲 (0%, 0 MiB)
- **monitor_status.txt**: All evals completed at 2026-05-21 08:50:13

### Eval 结果汇总 (vanilla baseline, libero_spatial, 200 episodes, threshold=0.001)

**vanilla_s0:**
| Step | TSR | CAR | Collisions |
|------|-----|-----|------------|
| 35000 | 0.905 | 0.695 | 61 |
| 40000 | 0.950 | 0.700 | 60 |
| 45000 | 0.955 | 0.745 | 51 |
| 50000 (final) | 0.910 | 0.775 | 45 |

**vanilla_s1:**
| Step | TSR | CAR | Collisions |
|------|-----|-----|------------|
| 35000 | 0.860 | 0.700 | 60 |
| 40000 | 0.910 | 0.725 | 55 |
| 45000 | 0.965 | 0.730 | 54 |
| 50000 (final) | 0.935 | 0.765 | 47 |

**vanilla_s2:**
| Step | TSR | CAR | Collisions |
|------|-----|-----|------------|
| 50000 (final) | 0.910 | 0.770 | 46 |

`safelibero_*.json` × 2 是 vanilla_s0 step 40000/45000 的重复 eval（结果完全一致）。`midtrain` 文件 = step 35000 的别名。

**趋势**: TSR 在 step 45000 达到峰值（s0=0.955, s1=0.965），50000 略回落。CAR 随 step 单调上升，50000 最优（~0.77）。碰撞数从 ~60 降到 ~46。

---
