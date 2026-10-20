# ops check running status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-running-status_20260513T232651_result.json`
- **Structured JSON:** [`790cd2cb6f307f2afebc.json`](../../sessions/79/790cd2cb6f307f2afebc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 1. plan001-exec-only-s42-r2 (cuda:0)

| 项目 | 状态 |
|------|------|
| 进程 | **存活** — PID 84901, python3, 状态 Rl (running), 已运行 46:42 |
| 进度 | **Step 359/500** (71.8%) |
| GPU 显存 | 80,314 / 97,887 MiB (82%), GPU利用率 88% |
| 最新 metrics (step 359) | **prove_rate=1.000, isr=1.000, reward=1.000** |
| 近5步 step_time | 3.3~10.9s，平均 ~5.6s |
| 预计剩余 | 141 步 × ~6.5s ≈ **~15 分钟** |

近几步 reward 稳定在 0.875~1.0，prove_rate 接近满分，训练已进入后期收敛阶段。

---

### 2. plan005-sta-low-s42 (cuda:1)

| 项目 | 状态 |
|------|------|
| 进程 | **存活** — 实际训练 PID 85795 (非 85790 bash wrapper), python3, 状态 Rl (running), 已运行 44:59 |
| 进度 | **Step 305/500** (61%) |
| GPU 显存 | 80,346 / 97,887 MiB (82%), GPU利用率 87% |
| 最新 metrics (step 305) | **prove_rate=0.500, isr=0.241, reward=0.474** |
| 近5步 step_time | ~9.25s/step |
| 预计剩余 | 195 步 × ~9.3s ≈ **~30 分钟** |

STA 实验的 isr_mean 明显低于 exec-only（0.24 vs 1.0），这是预期中的——STA reward 包含了 structural trace alignment 成分，而 isr 仅衡量 intermediate step reward 部分。prove_rate 波动较大（0.5~1.0），reward 在 0.47~0.93 之间。

---

**注意**: plan005 的实际训练 PID 是 **85795**（不是任务描述中的 85790，85790 是 bash wrapper）。后续监控应跟踪 85795。

---
