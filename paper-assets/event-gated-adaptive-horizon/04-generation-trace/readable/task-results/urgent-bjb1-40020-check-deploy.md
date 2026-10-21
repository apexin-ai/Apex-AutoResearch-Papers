# urgent bjb1 40020 check deploy

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_bjb1-40020-check-deploy_20260523T074426_result.json`
- **Structured JSON:** [`ff866cbe39a41d23d4dc.json`](../../sessions/ff/ff866cbe39a41d23d4dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 两个实验均在运行，即将完成

| 实验 | PID | 运行时间 | 当前步数 | 目标 | 预计剩余 |
|------|-----|----------|----------|------|----------|
| exp_050 (PegInsertion CIVO s0) | 304736 | 13h07m | 205,600 | 210K | ~17 min |
| exp_051 (StackCube frozen_dt_emb s0) | 305974 | 12h54m | 207,000 | 210K | ~12 min |

### exp_050 eval_return 趋势
- **Peak**: 14.21 @ 22.5K，14.13 @ 62.5K，14.10 @ 192.5K
- **Latest** (202.5K): 7.49
- 性能波动大，无明确上升趋势

### exp_050 ve_ratio 趋势（122.5K→）

| Step | ve_ratio |
|------|----------|
| 122.5K | 2.63 |
| 132.5K | 3.75 |
| 142.5K | 3.20 |
| 152.5K | **8.46** (peak) |
| 162.5K | 1.94 |
| 172.5K | 3.13 |
| 182.5K | 2.21 |
| 192.5K | 0.75 |
| 202.5K | 1.23 |

ve_ratio 从 152.5K 的 8.46 高点下降，最近两个点在 0.75-1.23 区间，趋势偏低。

### exp_051 eval_return 趋势
- **Peak**: 38.21 @ 182.5K
- **Latest** (202.5K): 33.97
- 后半程稳定在 27-38 区间，表现良好

### exp_051 ve_ratio 趋势（122.5K→）
持续极低（0.14-0.38），已收敛到 ~0.16，frozen dt_emb 下 CIVO 基本不触发。

### 下一步
两个实验预计 20 分钟内完成。exp_051 完成后立即释放 cuda:1，可部署 exp_055。需要等进程结束后再执行部署和 registry 更新。是否需要我设置定时回来检查？

---
