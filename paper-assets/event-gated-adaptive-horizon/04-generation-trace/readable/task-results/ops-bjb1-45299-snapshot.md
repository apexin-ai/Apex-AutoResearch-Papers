# ops bjb1 45299 snapshot

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1_45299_snapshot_20260520T113335_result.json`
- **Structured JSON:** [`4a349fe337fb25270263.json`](../../sessions/4a/4a349fe337fb25270263.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 进程状态
| 实验 | PID | 状态 | 运行时间 |
|------|-----|------|----------|
| exp_027_tcn_walker_s1 | 888926 | Running (Sl) | 5h20m |
| exp_030b_tcn_cheetah_s0_sigma05 | 903247 | Running (Sl+) | 22m43s |

### exp_027_tcn_walker_s1 (Walker σ=0.5, seed=1)

| 指标 | 最新值 | step |
|------|--------|------|
| **当前 step** | ~188K / 210K | — |
| **最新 eval_return** | **355.4** | 185K |
| **peak eval_return** | **364.9** | 75K |
| **最新 ve_ratio** | **0.211** | 185K |
| **peak ve_ratio** | **0.735** | 175K |
| **train_return** (最新 4 ep)** | 354.8 / 431.2 / 419.4 / 427.1 | 188K |
| fps | ~10.0 | — |

eval_return 趋势：75K 见顶 364.9 后大幅波动，185K 回升到 355.4。ve_ratio 在 175K 冲到 0.735 后 185K 骤降到 0.211（delta_ve = -0.52）。gate_dt 始终固定在 2.0（100% dt=2）。

### exp_030b_tcn_cheetah_s0_sigma05 (Cheetah σ=0.5, seed=0)

| 指标 | 最新值 | step |
|------|--------|------|
| **当前 step** | ~16K / 210K | — |
| **最新 eval_return** | **78.3** | 15K |
| **最新 ve_ratio** | **0.020** | 15K |
| fps | ~9.7 | — |

刚启动 22 分钟，只有两个 eval 点（5K: 8.3, 15K: 78.3），早期阶段正常上升。

### GPU 状态

| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 (exp_030b) | 21% | 3.8 GB / 95.6 GB |
| cuda:1 (exp_027) | 22% | 2.8 GB / 95.6 GB |

两卡负载都很轻。

---
