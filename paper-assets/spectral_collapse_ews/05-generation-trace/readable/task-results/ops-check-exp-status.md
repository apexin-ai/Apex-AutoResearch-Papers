# ops check exp status

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_exp_status_20260520T175548_result.json`
- **Structured JSON:** [`1bb075e459cfc9c94970.json`](../../sessions/1b/1bb075e459cfc9c94970.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### exp_012 — Phase 1: fixed_mix (r=0.3, seed=43)

| 项目 | 值 |
|------|-----|
| **状态** | **RUNNING** |
| **GPU** | GPU 0 (94% util, 25GB/98GB) |
| **进度** | Gen 8/10 — 生成样本中 32000/35000 (91%) |
| **已运行** | ~14.9h (05-20 11:03 → 05-21 01:57 CST) |
| **预计剩余** | ~3-4h (Gen 8 完成 + Gen 9 完整周期) |

**已完成 Gen 0-7 指标：**

| Gen | eff_rank | log_det | ppl | distinct4 | train_loss | σ₁ |
|-----|----------|---------|------|-----------|------------|--------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.7415 | — | 1942.8 |
| 1 | 476.75 | 2363.89 | 10.19 | 0.6676 | 1.837 | 948.7 |
| 2 | 483.02 | 2363.64 | 10.58 | 0.5348 | 1.765 | 867.9 |
| 3 | 489.31 | 2389.87 | 10.91 | 0.5225 | 1.544 | 827.0 |
| 4 | 494.15 | 2408.14 | 11.25 | 0.5097 | 1.461 | 800.1 |
| 5 | 498.80 | 2431.29 | 11.55 | 0.5046 | 1.441 | 778.2 |
| 6 | 502.00 | 2445.24 | 11.88 | 0.4527 | 1.435 | 769.4 |
| 7 | 505.90 | 2462.25 | 12.18 | 0.3219 | 1.328 | 760.0 |

---

### exp_013 — Phase 1: pure_collapse (r=0.0, seed=44)

| 项目 | 值 |
|------|-----|
| **状态** | **RUNNING** |
| **GPU** | GPU 1 (78% util, 25GB/98GB) |
| **进度** | Gen 4/10 — 生成样本中 48000/50000 (96%) |
| **已运行** | ~10h (05-20 15:52 → 05-21 01:57 CST) |
| **预计剩余** | ~15h (Gen 4 完成 + Gen 5-9，每 gen 50000 样本，~2.5h/gen) |

**已完成 Gen 0-3 指标：**

| Gen | eff_rank | log_det | ppl | distinct4 | train_loss | σ₁ |
|-----|----------|---------|------|-----------|------------|--------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.7305 | — | 1942.8 |
| 1 | 490.77 | 2459.40 | 11.36 | 0.6019 | 1.626 | 808.1 |
| 2 | 495.83 | 2467.38 | 13.54 | 0.4943 | 1.233 | 726.0 |
| 3 | 493.45 | 2442.40 | 16.22 | 0.4283 | 1.024 | 710.0 |

---

**无 hellaswag 指标**（日志中未找到相关输出）。

σ₁ 取自 `top_10_singular_values[0]`。pure_collapse 退化速度显著快于 fixed_mix：3 gen 内 ppl 从 9.55 飙到 16.22（+70%），而 fixed_mix 7 gen 后仅到 12.18（+28%）。eff_rank 在 pure_collapse 中 Gen 3 已出现回落（495.83→493.45）。

---
