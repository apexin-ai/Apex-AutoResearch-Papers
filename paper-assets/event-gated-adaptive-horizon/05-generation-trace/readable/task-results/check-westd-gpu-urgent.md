# check westd gpu urgent

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd_gpu_urgent_20260525T222842_result.json`
- **Structured JSON:** [`924b4d582d1bbda4a7c4.json`](../../sessions/92/924b4d582d1bbda4a7c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-19154 GPU 状态报告

### exp_091_cheetah_008d_s2 (cuda:0)
- **状态**: 🟢 存活
- **PID**: 47303 (parent) / 47308 (GPU 进程)，运行时间 ~2h
- **当前 step**: 105,000（最新 train step 104,000，正在跑 eval @ 105k）
- **FPS**: ~14
- **GPU 显存**: 3,223 MiB / 97,887 MiB，利用率 5%
- **目标总 steps**: 假设标准 500k → 当前 ~21% 完成
- **ETA**: 按 14 fps 算，剩余 ~395k steps × 500 env_steps/1k_train_steps... 约需 ~7.8h

### plan_030 RSSM 分析
- **状态**: ❌ 无结果
- `artifacts/plan_030_rssm_quality/` 目录不存在，全 artifacts 下也无相关目录
- 之前在 cuda:1 上跑的进程已结束，未留下产出文件

### GPU 空闲状况

| GPU | 状态 |
|-----|------|
| cuda:0 (RTX PRO 6000 Black) | 占用中 (exp_091, 3.2GB/98GB, 5% util) |
| cuda:1 (RTX PRO 6000 Black) | **空闲** (0 进程, 1MiB, 0% util) |

**cuda:1 完全空闲**，可安排新实验。

---
