# check 019ab final status ve

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_019ab-final-status-ve_20260517T072224_result.json`
- **Structured JSON:** [`b3f9614deeaeeb149b06.json`](../../sessions/b3/b3f9614deeaeeb149b06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 实验状态

| 实验 | 当前步数 | 目标 | 进度 | 最新 eval_return |
|------|---------|------|------|-----------------|
| 019a_v2 (baseline) | 193,648 | 200,000 | ~97% | 69.43 (step 192500) |
| 019b (CIVO trigger) | 69,600 | 200,000 | ~35% | 5.95 (step 62500) |

两个进程都在正常运行。

### V/E Trajectory 关键发现

**019a_v2 (baseline)**：
- value_mean 持续上升至 ~143 并饱和，但 eval_return 只到 ~60-70
- V/E ratio 稳定在 **2.0-2.8** 范围，存在显著的 value overestimation
- 这是 DreamerV3 在 PickCube 上的典型 optimistic value bias

**019b (CIVO trigger)**：
- eval_return 在 22.5k 步达到峰值 24.9 后**持续下降**至 3.7-5.9
- value_mean 同样在下降（27.2 → 15.9），说明 critic 和 policy 同时退化
- V/E ratio 波动大（最高 5.66），训练不稳定

019b 出现了明显的训练崩溃/退化问题，需要诊断原因（可能是 gate_fixed_dt=2 + imag_horizon=8 的组合导致 imagination 质量下降）。

### 产出
1. V/E trajectory JSON 已保存到 `artifacts/pickcube_ve_trajectory.json`
2. 对比图已生成在远程 `/root/autodl-tmp/event-gated-adaptive-horizon/pickcube_ve_comparison.png`

---
