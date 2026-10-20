# ops cheetah unexposed progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cheetah-unexposed-progress_20260518T181705_result.json`
- **Structured JSON:** [`cd1488505da4a60d4040.json`](../../sessions/cd/cd1488505da4a60d4040.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，汇总如下：

## 实验进度汇总

```
实验ID                           | 当前步数/目标 | 状态     | 最新eval_return | value_mean | v/e ratio | NVE
─────────────────────────────────┼──────────────┼─────────┼────────────────┼───────────┼──────────┼─────
exp_008a_cheetah_unexposed_s0    | 112K/105K    | ✅ 完成  | 532.35 @105K   | 169.98    | 0.3193   | 0.490
exp_008a_cheetah_unexposed_s1    | 112K/105K    | ✅ 完成  | 504.38 @105K   | 156.97    | 0.3112   | 0.478
exp_023a_cheetah_baseline_s0     | 212K/???     | 运行中   | 624.71 @205K   | 392.47    | 0.6282   | —
exp_023b_cheetah_baseline_s1     | 212K/???     | 运行中   | 520.27 @205K   | 387.52    | 0.7448   | —
exp_023_cheetah_baseline_s2      | 52K/???      | 运行中   | 334.79 @45K    | 83.07     | 0.2481   | —
```

## NVE 计算 (@ 105K 步对齐)

Baseline v/e @ 105K:
- 023a_s0: v/e = 0.7428 (value_mean=239.16, eval_return=321.97)
- 023b_s1: v/e = 0.5592 (value_mean=243.83, eval_return=436.02)
- **Baseline avg v/e = 0.6510**

Unexposed NVE:
- **s0: NVE = 0.3193 / 0.6510 = 0.490**
- **s1: NVE = 0.3112 / 0.6510 = 0.478**
- **avg NVE = 0.484**

## 008a 完整 eval checkpoint 序列

| Step | s0 eval_return | s1 eval_return |
|------|---------------|---------------|
| 5K   | 8.26          | 13.48         |
| 15K  | 175.04        | 29.87         |
| 25K  | 314.15        | 176.46        |
| 35K  | 372.21        | 177.41        |
| 45K  | 383.03        | 282.01        |
| 55K  | 402.76        | 389.36        |
| 65K  | 479.54        | 429.57        |
| 75K  | 482.10        | 393.89        |
| 85K  | 485.29        | 512.32        |
| 95K  | 496.45        | 519.03        |
| 105K | 532.35        | 504.38        |

v/e ratio 序列 (from civo/ve_ratio):
- s0: 0.014 → 0.056 → ... → 0.326 @95K → **0.319 @105K**
- s1: 0.065 → 0.060 → ... → 0.277 @95K → **0.311 @105K**

## 关键观察

1. **两个 unexposed 实验已完成**，均超过 105K 目标
2. unexposed 的 v/e ratio (~0.31) 显著低于 baseline 在同步数的 v/e (~0.65)，**NVE ≈ 0.48**，说明 unexposed 配置下 critic 的值估计相对 return 偏保守约一半
3. 所有 unexposed 实验的 gate_dt 始终锁定在 2.0（gate_dt_2_frac = 1.0），gate 没有学到变化
4. baseline s2 刚到 52K，还在早期阶段

---
