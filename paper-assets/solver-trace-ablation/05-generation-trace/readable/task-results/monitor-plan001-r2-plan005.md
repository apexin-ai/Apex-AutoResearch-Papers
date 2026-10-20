# monitor plan001 r2 plan005

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_plan001-r2-plan005_20260513T234045_result.json`
- **Structured JSON:** [`c66746853c97fbeae6d8.json`](../../sessions/c6/c66746853c97fbeae6d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### 实验 1: plan001-exec-only-s42-r2 (cuda:0)

| 项目 | 值 |
|------|-----|
| PID 84901 | **存活**，已运行 1h00m |
| 当前进度 | **478/500**（95.6%） |
| 最新 metrics (step 478) | prove_rate=**1.000**, isr=**1.000**, reward=**1.000** |
| 近 20 步 prove_rate 范围 | 0.500 - 1.000，多数 ≥ 0.875 |
| Checkpoints | checkpoint-400, checkpoint-450 ✅ |
| 速度 | ~5-7s/step |
| **预计剩余** | **~2 分钟** |

prove_rate 在 step 378 后确实基本饱和（频繁触及 1.0），reward = prove_rate = isr（sta_weight=0 符合预期）。

---

### 实验 2: plan005-sta-low-s42 (cuda:1)

| 项目 | 值 |
|------|-----|
| PID 85790 | **存活**，已运行 58m |
| 当前进度 | **403/500**（80.6%） |
| 最新 metrics (step 403) | prove_rate=**0.750**, isr=**0.333**, reward=**0.708** |
| 近 20 步 prove_rate 范围 | 0.250 - 1.000，多数 0.750-1.000 |
| 近 20 步 ISR 范围 | 0.036 - 0.464，多数 0.1-0.3 |
| Checkpoints | checkpoint-350, checkpoint-400 ✅ |
| 速度 | ~8-10s/step |
| **预计剩余** | **~15 分钟** |

---

### 对比要点

- **prove_rate**: exec-only 在 step 450+ 几乎全 ≥ 0.875；STA-low 在 step 400 附近仍有波动（0.25-1.0），整体偏低
- **ISR**: exec-only 的 ISR ≡ prove_rate（无 STA 成分，符合预期）；STA-low 的 ISR 远低于 prove_rate（多数 0.1-0.3），说明 STA weight=0.1 对 solver trace 的中间步骤评分拉低了 ISR
- **收敛状态**: exec-only 即将完成且已饱和；STA-low 还有约 100 步，prove_rate 上升趋势存在但远未饱和

---
