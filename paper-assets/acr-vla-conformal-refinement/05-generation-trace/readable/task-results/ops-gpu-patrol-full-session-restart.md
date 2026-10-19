# ops gpu patrol full session restart

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-patrol-full-session-restart_20260518T102453_result.json`
- **Structured JSON:** [`e52e8e54a24b1f66b5c4.json`](../../sessions/e5/e52e8e54a24b1f66b5c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态

### bjb2-28827 (6x RTX 4090, CUDA 13.0)
| GPU | PID | 模式 | seed | norm | K | 备注 |
|-----|-----|------|------|------|---|------|
| 0 | 492545 | random_selection | 43 | — | 10 | **未注册** |
| 1 | 497445 | crm_obs_only | 42 | 0.1 | 10 | |
| 2 | 527474 | crm_obs_only | 43 | 0.2 | 5 | |
| 3 | 497642 | crm_perdof | 42 | 0.1 | 10 | |
| 4 | 514350 | random_selection | 44 | — | 10 | |
| 5 | 488665 (bash: 488656) | crm_perdof | 48 | 0.2 | 10 | **未注册** |

空闲 GPU: **无**

### bjb1-32546 (6x RTX 4090, CUDA 13.2)
| GPU | PID | 模式 | seed | norm | K | 备注 |
|-----|-----|------|------|------|---|------|
| 0 | 565173 | crm_obs_only | 45 | 0.05 | 10 | |
| 1 | 549432 | crm_obs_only | 44 | 0.05 | 10 | **未注册** |
| 2 | 553052 (bash: 553043) | crm_perdof | 44 | 0.05 | 10 | **未注册** |
| 3 | 562396 | crm_obs_only | 46 | 0.1 | 10 | |
| 4 | 535595 | crm_perdof | 43 | 0.2 | 10 | |
| 5 | 571010 | crm_perdof | 43 | 0.1 | 10 | |

空闲 GPU: **无**

### bjb1-18228 (4x RTX 4090, CUDA 13.0)
| GPU | PID | 模式 | seed | norm | K | 备注 |
|-----|-----|------|------|------|---|------|
| 0 | 796900 | crm_obs_only | 48 | 0.2 | 10 | |
| 1 | 774342 | crm_obs_only | 48 | 0.1 | 10 | |
| 2 | 774543 | crm_obs_only | 48 | 0.3 | 10 | |
| 3 | — | — | — | — | — | **空闲** (1MiB, 0% util) |

**perdof-norm02-seed45-r3 诊断: 正常完成。** PID 749547 已退出，JSON 输出文件存在且完整（1488 bytes, 18:14 写入），10 个 task 全部有结果，overall_success_rate=0.12。无 exit sentinel 是因为 r3 未通过 agent-ml wrapper 启动（无 trap）。~/runs 下也无对应日志，仅有 deploy 和 r2 的旧日志。

空闲 GPU: **[3]**

### bjb2-40593 (1x RTX 4090 D, CUDA 13.0)
| GPU | PID | 模式 | seed | norm | K |
|-----|-----|------|------|------|---|
| 0 | 395256 | random_selection | 42 | — | 10 |

空闲 GPU: **无**

---

## 未注册 cron 实验

| exp_id | PID (python) | 服务器 | GPU | 命令摘要 | 状态 |
|--------|-------------|--------|-----|----------|------|
| eval-perdof-object-norm02-seed48 | 488656 → 488665 | bjb2-28827 | 5 | crm_perdof, object, seed=48, K=10, norm=0.2 | 运行中 |
| eval-random-selection-object-seed43 | 492545 | bjb2-28827 | 0 | random_selection, object, seed=43, K=10 | 运行中 |
| eval-obs-only-object-norm005-seed44 | 549432 | bjb1-32546 | 1 | crm_obs_only, object, seed=44, K=10, norm=0.05 | 运行中 |
| eval-perdof-object-norm005-seed44 | 553043 → 553052 | bjb1-32546 | 2 | crm_perdof, object, seed=44, K=10, norm=0.05 | 运行中 |

4 个未注册实验均正常运行中。

---

## 空闲 GPU 汇总

| 服务器 | 空闲 GPU |
|--------|----------|
| bjb2-28827 | 无 (6/6 占用) |
| bjb1-32546 | 无 (6/6 占用) |
| bjb1-18228 | **GPU 3** (1/4 空闲) |
| bjb2-40593 | 无 (1/1 占用) |

**全集群共 1 块空闲 GPU: bjb1-18228 cuda:3**

---
