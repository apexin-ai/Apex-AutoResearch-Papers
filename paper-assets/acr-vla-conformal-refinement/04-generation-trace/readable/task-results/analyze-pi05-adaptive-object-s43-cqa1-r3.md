# analyze pi05 adaptive object s43 cqa1 r3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_pi05-adaptive-object-s43-cqa1-r3_20260526T160006_result.json`
- **Structured JSON:** [`64187c74b93ba544837a.json`](../../sessions/64/64187c74b93ba544837a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the analysis:

---

## pi05-adaptive-object-s43-cqa1-r3 结果

**来源：log + JSON（cqa1-32758）**

| 指标 | 值 |
|------|-----|
| **Overall SR** | **85.0%** (170/200) |
| Trigger rate | 4.0% (1368/34067 steps) |
| Mean uncertainty | 0.0846 |
| Mean correction norm | 0.200 (= max cap) |
| τ | 0.25, K=2 |

**Per-task SR（JSON）：**

| Task | SR |
|------|-----|
| alphabet_soup | 95% |
| salad_dressing | 95% |
| milk | 95% |
| bbq_sauce | 90% |
| tomato_sauce | 85% |
| chocolate_pudding | 85% |
| orange_juice | 85% |
| butter | 80% |
| cream_cheese | 70% |
| ketchup | 70% |

无 OOM / CUDA error，EXIT_CODE=0，实验健康。

---

## 同组对比（Registry）

### Adaptive Conformal on Object（τ=0.25, K=2, norm=0.2）

| Seed | SR | Trigger Rate | Source |
|------|-----|-------------|--------|
| s42 | 85.5% | 3.68% | pi05-adaptive-object-s42-cqa1 |
| **s43** | **85.0%** | **4.0%** | **本次实验** |
| s44 | — | — | failed (pi05-adaptive-object-s44-cqa1-r2) |

**2-seed 均值：85.25% ± 0.35%**（s42+s43），高度一致。s44 无有效数据。

### 对比 Baseline（Registry）

| Method | s42 | s43 | s44 | Mean±Std |
|--------|-----|-----|-----|----------|
| **VLA-only** | 99.5% | 100% | 99.5% | **99.7% ± 0.3%** |
| **CRM (always-on)** | 89% | 87% | 88% | **88.0% ± 1.0%** |
| **Adaptive Conformal** | 85.5% | 85.0% | — | **85.25% ± 0.35%** |

---

## Conclusion: **Negative**

π0.5 VLA-only 在 Object 上接近 ceiling（99.7%）。任何 correction 干预都在 degrading performance：

- CRM always-on：-11.7pp（99.7→88.0）
- Adaptive Conformal：-14.4pp（99.7→85.25）

Adaptive 的 trigger rate 仅 4%（conformal 阈值正确地保守），但触发时的 corrections（norm=0.2 打满 cap）在 near-expert VLA 上仍然有害。Adaptive 甚至比 always-on CRM 低 2.75pp，说明 conformal 触发的时机选择可能并不优于随机——在 VLA 已经近乎完美的场景下，"何时 correct" 和 "是否 correct" 同样不成立。

**对 Table 2 的意义：** Object suite 确认了预期——Adaptive Conformal 在 VLA 强势场景下无正向收益。该方法的价值需要在 VLA 较弱的 suite（Spatial、Long）上体现。s42/s43 两个 seed 高度一致，结果可信。s44 仍需补跑才能完成 3-seed 统计。

---
