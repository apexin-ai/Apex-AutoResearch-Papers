# ops full experiment status check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-experiment-status-check_20260518T213532_result.json`
- **Structured JSON:** [`1f8541e48e735e1c8a4d.json`](../../sessions/1f/1f8541e48e735e1c8a4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告 (2026-05-19 05:36 CST)

### GPU 状态
| GPU | 型号 | 利用率 | 显存 | 进程数 |
|-----|------|--------|------|--------|
| 0 | RTX PRO 6000 | **100%** | 11235/97887 MiB | 3 |
| 1 | RTX PRO 6000 | **24%** | 3278/97887 MiB | 1 |

共 4 个 Python 进程在跑。

---

### 实验总览

| 实验 | 状态 | 当前步数/目标 | 最新 eval_return | value_mean | v/e ratio | GPU | 最后更新 |
|------|------|---------------|-------------------|------------|-----------|-----|----------|
| exp_001_baseline_s2 | ⚠️ **可能停滞** | 112K/105K | 443.46 @105K | 329.16 | 0.742 | cuda:1 | 04:25 (>1h前) |
| exp_009c_no_dt_emb_s3 | 🔄 运行中 | 108K/105K | 311.92 @105K | 120.27 | 0.386 | cuda:1 | 05:37 |
| exp_008f_no_dt_emb_s4 | 🔄 运行中 | 68K/105K (65%) | 405.52 @65K | 124.32 | 0.307 | cuda:0 | 05:34 |
| exp_023_cheetah_baseline_s2 | 🔄 运行中 | 132K/200K (66%) | 343.37 @125K | 304.13 | 0.886 | cuda:0 | 05:34 |

---

### ⚠️ exp_001_baseline_s2 告警
metrics.jsonl 最后修改时间 04:25，距今超 1 小时未更新。已过 105K 目标（train step 到 112K），但 **进程可能已退出或卡住**。nvidia-smi 显示 GPU 1 只有 1 个进程（应为 exp_009c），说明 exp_001 进程大概率已退出。已达到 105K eval checkpoint，数据完整。

---

### 完整 Eval 序列

**exp_001_baseline_s2** (Walker baseline, seed=2) ✅ 已达 105K
| Step | eval_return | value_mean | v/e ratio |
|------|-------------|------------|-----------|
| 5K | 41.21 | — | — |
| 15K | 198.82 | 7.21 | 0.036 |
| 25K | 195.75 | 40.01 | 0.204 |
| 35K | 250.88 | — | 0.310 |
| 45K | 235.28 | — | — |
| 55K | 266.98 | — | — |
| 65K | 205.84 | — | — |
| 75K | 379.00 | — | — |
| 85K | 389.31 | 264.90 | — |
| 95K | 387.42 | 296.03 | 0.764 |
| **105K** | **443.46** | **329.16** | **0.742** |

**exp_009c_no_dt_emb_s3** (Walker no-dt-emb, seed=3) ✅ 已达 105K
| Step | eval_return | value_mean | v/e ratio |
|------|-------------|------------|-----------|
| 5K | 33.83 | — | — |
| 15K | 94.93 | 2.08 | 0.022 |
| 25K | 143.43 | 12.24 | 0.085 |
| 35K | 196.53 | — | 0.131 |
| 45K | 337.17 | — | — |
| 55K | 456.10 | — | — |
| 65K | 457.74 | — | — |
| 75K | 304.59 | — | — |
| 85K | 268.30 | — | — |
| 95K | 187.34 | 123.24 | 0.658 |
| **105K** | **311.92** | **120.27** | **0.386** |

注意：eval_return 在 55-65K 达峰 ~457 后大幅下降，105K 仅 311.92。

**exp_008f_no_dt_emb_s4** (Walker no-dt-emb, seed=4) 🔄 进行中
| Step | eval_return | value_mean | v/e ratio |
|------|-------------|------------|-----------|
| 5K | 33.19 | — | — |
| 15K | 171.78 | 2.79 | 0.016 |
| 25K | 245.55 | 17.07 | 0.069 |
| 35K | 241.78 | — | 0.165 |
| 45K | 213.45 | — | — |
| 55K | 487.53 | 95.44 | 0.196 |
| **65K** | **405.52** | **124.32** | **0.307** |

**exp_023_cheetah_baseline_s2** (Cheetah baseline, seed=2) 🔄 进行中
| Step | eval_return | value_mean | v/e ratio |
|------|-------------|------------|-----------|
| 5K | 17.59 | — | — |
| 15K | 157.48 | 2.61 | 0.017 |
| 25K | 272.15 | 17.66 | 0.065 |
| 35K | 311.87 | 45.28 | 0.145 |
| 45K | 334.79 | — | — |
| 55K | 235.18 | — | — |
| 65K | 410.46 | — | — |
| 75K | 467.81 | — | — |
| 85K | 432.97 | — | — |
| 95K | 384.38 | — | — |
| 105K | 406.06 | 276.32 | 0.680 |
| 115K | 488.37 | 286.85 | 0.587 |
| **125K** | **343.37** | **304.13** | **0.886** |

（部分中间 checkpoint 的 value_mean 因输出截断未提取到，标记为 —）

---

### 关键发现
1. **exp_001_baseline_s2 可能已停止** — 建议 SSH 检查 tmux 会话是否还在。如果已完成 105K eval 且不需要继续跑，可以忽略。
2. **exp_009c_s3 性能下降严重** — 55-65K 峰值 ~457 后跌到 105K 的 311.92，value_mean 仅 120 vs baseline 的 329。
3. **exp_008f_s4 进展正常** — 65K/105K，55K 峰值 487.53 很高，但和 009c 类似可能后续会下降。
4. **exp_023 cheetah baseline** — 125K/200K，eval_return 波动大（75K 峰值 467.81，125K 回落到 343.37），v/e ratio 0.886 很高。

---
