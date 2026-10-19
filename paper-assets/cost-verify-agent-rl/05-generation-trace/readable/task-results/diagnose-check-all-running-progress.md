# diagnose check all running progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_check-all-running-progress_20260518T202445_result.json`
- **Structured JSON:** [`1aa0fa6202890470bada.json`](../../sessions/1a/1aa0fa6202890470bada.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。汇总报告如下：

---

## 实验状态汇总 (2026-05-19 04:30 UTC)

| | **factorial_seed2** | **hsweep_h10_seed1** | **hsweep_h20_seed1** |
|---|---|---|---|
| **服务器** | westd-47453 (cuda:0,1) | westd-47453 (cuda:2,3) | bjb1-17606 (cuda:0,1) |
| **PID** | 576727 | 34193 | 77613 |
| **进程存活** | Y | Y | Y |
| **当前 step** | **11/15 (73%)** | **2/15 (13%)** | **0/15 (0%)** |
| **GPU 利用率** | 100% / 96% | 96% / 100% | 100% / 100% |
| **最新 train success** | **62.5%** (step 11) | 尚无 (当前 run) | 无数据 |
| **最新 train pass@8** | 93.75% (step 11) | - | - |
| **最新 val success** | **2.24%** OOD (step 5,10 均为此值) | 6.25% (初始 val) | 无数据 |
| **最新 ppo_kl** | **0.110** (step 11) | - | - |
| **最新 entropy** | 0.748 (step 11) | - | - |
| **最新 log 时间** | ~04:00 (step 11 rollout 中) | ~04:01 (step 2 后 rollout 中) | ~03:30 (step 0 rollout 中) |
| **预估完成** | **~07:00 May 19** (~3h) | **~17:00 May 19** (~13h) | 无法估算 |
| **磁盘** | 77% (60GB free) | 同左 | 47% (17GB free) |

### 关键观察

**factorial_seed2** (最有价值的数据):
- train success 趋势: step5=31% → step7=47% → step8=11%(掉了) → step11=62.5%，波动较大
- val OOD success 两次 eval (step 5, step 10) 均卡在 2.24% (3/134)，**OOD 泛化未见改善**
- ppo_kl 从 0.047 (step5) 上升到 0.110 (step11)，在合理范围内
- 磁盘曾 >95% full（raylet 大量 warning），目前已恢复到 77%

**hsweep_h10_seed1**:
- 之前的 run (wandb da7701tk) 到 step 6 时 train success 降到 0%（**疑似 collapse**），随后重启
- 当前 run 刚到 step 2，还没有完整的 step 级指标
- 初始 val success=6.25% (2/32)

**hsweep_h20_seed1**:
- 刚启动 ~1.3h，仍在第一轮 rollout 生成中，无任何训练指标

---
