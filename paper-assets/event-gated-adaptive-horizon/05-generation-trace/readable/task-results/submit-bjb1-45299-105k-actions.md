# submit bjb1 45299 105k actions

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_bjb1_45299_105k_actions_20260520T055247_result.json`
- **Structured JSON:** [`5f1b613ba37953bcae9e.json`](../../sessions/5f/5f1b613ba37953bcae9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Quick verification: exp_027_s0 resumed from 112K (heading to 210K), exp_027_s1 already started (at step 0→5K).

## 结果汇总

### 105K 完整数据

**exp_027_tcn_walker_s0 (TCN σ=0.5)**:
| Step | eval_return | ve_ratio |
|------|-------------|----------|
| 5K | 37.4 | — |
| 15K | 154.6 | 0.02 |
| 25K | 223.6 | 0.11 |
| 35K | 239.9 | 0.24 |
| 45K | 101.2 | 0.86 |
| 55K | 70.0 | 1.68 |
| 65K | 95.1 | 1.54 |
| 75K | 189.2 | 0.83 |
| 85K | 35.9 | **3.97** |
| 95K | 166.4 | 0.68 |
| 105K | 95.5 | 0.92 |

85K→105K: NVE 从 3.97 自校正回 0.92。Eval 波动大但未崩溃。

**exp_028_rave_walker_s0 (RAVE ceil=2.0)** — NEGATIVE:
| Step | eval_return | ve_ratio |
|------|-------------|----------|
| 5K | 37.4 | — |
| 15K | 105.3 | 0.03 |
| 25K | 191.9 | 0.13 |
| 35K | 204.6 | 0.27 |
| 45K | 197.7 | 0.44 |
| 55K | 193.0 | 0.62 |
| 65K | 79.8 | 1.83 |
| 75K | 44.5 | 3.42 |
| 85K | 57.7 | 2.13 |
| 95K | 25.9 | **4.09** |
| 105K | 29.0 | 3.18 |

NVE 持续恶化，eval 从 193→29 彻底崩塌，无自校正。

### 已提交任务
- **exp_027_tcn_walker_s0** → cuda:0, PID 888715, 续跑到 210K（从 112K checkpoint 恢复）
- **exp_027_tcn_walker_s1** → cuda:1, PID 888921, seed=1, 210K（已启动，在 5K）

### Registry 已更新
- exp_027_s0: metrics + target_steps=210K
- exp_028_s0: DONE(negative) + 完整 metrics + checkpoint/log path
- exp_027_s1: RUNNING + spec

---
