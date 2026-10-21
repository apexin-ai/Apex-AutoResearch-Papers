# ops status check launch

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status_check_launch_20260517T152517_result.json`
- **Structured JSON:** [`d77725363950787984b1.json`](../../sessions/d7/d77725363950787984b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态
| GPU | 型号 | 显存占用 | GPU-Util | 温度 |
|-----|------|---------|----------|------|
| 0 | RTX PRO 6000 | 65909/97887 MiB | 94% | 63°C |
| 1 | RTX PRO 6000 | 25017/97887 MiB | 94% | 63°C |

两块卡均满载运行。

---

## exp_001 (Phase 0, cuda:0)
**状态: Gen 0-9 已完成，进程仍在运行（可能在跑 Gen 10）**
- PID 59365: **存活**，已运行 16h05m（`--resume_from_gen 4`）
- 日志显示 "Generation 10/10"，当前生成样本 14400/50000
- `phase0_results.json` 已包含 Gen 0-9 全量数据

### 全量数据表

| Gen | eff_rank | log_det | ppl | distinct4 | hellaswag |
|-----|----------|---------|-----|-----------|-----------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.7414 | 0.4130 |
| 1 | 491.77 | 2464.76 | 11.38 | 0.6256 | 0.3897 |
| 2 | 496.44 | 2469.93 | 13.58 | 0.5154 | 0.3764 |
| 3 | 493.31 | 2440.57 | 16.25 | 0.4900 | 0.3658 |
| 4 | 485.67 | 2405.05 | 19.80 | 0.4679 | 0.3558 |
| 5 | 479.21 | 2370.17 | 24.59 | 0.4630 | 0.3439 |
| 6 | 473.00 | 2335.17 | 30.91 | 0.4655 | 0.3311 |
| 7 | 464.20 | 2304.19 | 38.89 | 0.4474 | 0.3187 |
| 8 | 456.76 | 2252.12 | 49.29 | 0.4401 | 0.3103 |
| 9 | 448.45 | 2207.57 | 63.32 | 0.4262 | 0.3009 |

趋势：eff_rank 从 Gen 2 峰值 496 单调下降至 448，log_det 从 Gen 2 峰值 2470 下降至 2208，ppl 从 9.5 飙升至 63.3，hellaswag 从 0.413 下降至 0.301。**Spectral collapse 信号清晰。**

---

## exp_005 (Phase 1 adaptive k=20, cuda:1)
**状态: Gen 2/10 进行中**
- PID 116947: **存活**，已运行 2h08m
- Checkpoints: gen_0, gen_1 已保存（gen_1 @ 22:45）
- 25008 MiB 显存占用

### Controller 行为
- Gen 1 mix_ratio: **0.50**
- controller_ratio: **0.50**
- log_det delta: 2366.68 → 2366.46 (delta ≈ -0.22)

### k=20 验证: **ratio = 0.50，未触发调整**
Gen 1 的 mix_ratio 仍为默认值 0.50，controller 未生效。不过 Gen 0→1 的 log_det 变化极小（-0.22），可能还不足以触发 tau=0.002 的阈值。需要观察 Gen 2+ 是否开始响应。

---

## exp_004 (fixed_mix)
**等待 cuda:0 释放，暂不启动。**
PID 59365 仍占用 cuda:0（65900 MiB），无法启动 exp_004。exp_001 当前在生成 Gen 10 的样本（14400/50000），预计还需数小时完成。

---
