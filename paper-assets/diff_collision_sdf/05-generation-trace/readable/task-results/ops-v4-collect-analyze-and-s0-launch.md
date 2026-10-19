# ops v4 collect analyze and s0 launch

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v4_collect_analyze_and_s0_launch_20260525T163529_result.json`
- **Structured JSON:** [`4697e4a8a1814b3b44f3.json`](../../sessions/46/4697e4a8a1814b3b44f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都在运行。cuda:1 加载了 9GB（s0_l005 正在跑 T0），cuda:2 的 s0_l01 还在加载模型阶段。

---

## A. v4 结果表

| Eval | Avg TSR | Avg CAR | T0 TSR/CAR | T1 TSR/CAR | T2 TSR/CAR | T3 TSR/CAR |
|------|---------|---------|------------|------------|------------|------------|
| s1_l005_v4 | 4.0% | 51.5% | 0%/54% | 16%/48% | 0%/88% | 0%/16% |
| s2_l005_v4 | 9.0% | 53.0% | 4%/60% | 32%/46% | 0%/86% | 0%/20% |
| s2_l01_v3 | 7.5% | 53.0% | 0%/62% | 30%/42% | 0%/88% | 0%/20% |

## B. Displacement 分析

**核心发现：所有模型的 safe episodes 100% 是 frozen（max_displacement < 0.001m）。Filtered CAR = 0%。**

| Eval | Raw CAR | Filtered CAR | Frozen% | TSR |
|------|---------|-------------|---------|-----|
| s1_l01_30k | 52.5% | 0.0% | 100.0% | 8% |
| s1_l005_30k | 51.5% | 0.0% | 100.0% | 4% |
| s2_l005_30k | 53.0% | 0.0% | 100.0% | 9% |
| s2_l01_30k | 53.0% | 0.0% | 100.0% | 8% |

**Sensitivity（Filtered CAR at different thresholds）：**

| Threshold | s1_l01_30k | s1_l005_30k | s2_l005_30k | s2_l01_30k |
|-----------|-----------|-------------|-------------|-----------|
| 0.0001 | 1.0% (F=98%) | 1.0% (F=98%) | 0.0% (F=100%) | 1.0% (F=98%) |
| 0.001 | 0.0% (F=100%) | 0.0% (F=100%) | 0.0% (F=100%) | 0.0% (F=100%) |
| 0.005 | 0.0% (F=100%) | 0.0% (F=100%) | 0.0% (F=100%) | 0.0% (F=100%) |
| 0.01 | 0.0% (F=100%) | 0.0% (F=100%) | 0.0% (F=100%) | 0.0% (F=100%) |

Histogram 已保存到 `/root/autodl-tmp/eval_results/displacement_hist_30k_batch.pdf`。

## C. s0 补跑状态

| Eval | PID | GPU | 显存 | 状态 |
|------|-----|-----|------|------|
| s0_l005_30k | 478653 | cuda:1 | 9012 MiB | 运行中，T0 开始 |
| s0_l01_30k | 478930 | cuda:2 | 加载中 | 运行中，模型加载 |

- cuda:0 (27GB) = spatial_bowl 训练（PID 168730）未受影响
- cuda:3 空闲
- 日志：`/root/colliforce-vla/logs/eval_s0_l005_30k.log` / `eval_s0_l01_30k.log`

---
