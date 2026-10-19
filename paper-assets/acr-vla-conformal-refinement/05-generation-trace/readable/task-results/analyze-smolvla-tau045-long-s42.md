# analyze smolvla tau045 long s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_smolvla-tau045-long-s42_20260528T023253_result.json`
- **Structured JSON:** [`1d3f8520836886301d97.json`](../../sessions/1d/1d3f8520836886301d97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE. Here's the report:

---

## smolvla-tau045-long-s42 结果

**SR = 59.5%**, **TR = 0.3%**, mean_unc = 0.1239, EXIT_CODE=0, 无错误/OOM

### Per-task SR

| Task | SR |
|------|---:|
| stove_moka_pot | 100% |
| black_bowl_drawer | 100% |
| book_caddy | 85% |
| cream_cheese_butter_basket | 75% |
| yellow_white_mug_microwave | 75% |
| alphabet_soup_cream_cheese_basket | 70% |
| white_mug_yellow_mug_plates | 45% |
| alphabet_soup_tomato_sauce_basket | 20% |
| white_mug_chocolate_pudding | 20% |
| both_moka_pots_stove | 5% |

### τ-sweep 全景（Long suite, SmolVLA, K=2, seed=42）

| τ | SR | TR | 备注 |
|---:|---:|---:|------|
| 0.05 | 44.0% | 97.8% | 过度干预，负效果 |
| 0.10 | 53.5% | 61.3% | |
| 0.15 | **61.0%** | 23.9% | peak |
| 0.20 | 58.5% | 8.7% | |
| 0.25 | 56.0% | 4.2% | |
| 0.30 | 54.5% | 1.6% | |
| 0.35 | 57.5% | 1.3% | |
| **0.45** | **59.5%** | **0.3%** | ← 本次 |
| VLA-only | 58.0±1.5% | 0% | baseline |

### 趋势分析

τ=0.45 处于曲线高阈值尾端，符合预期：
- **TR=0.3%** — CRM 几乎不触发（200 rollouts 中约 0.6 次），延续 TR 随 τ 单调递减的趋势
- **SR=59.5%** — 在 VLA-only baseline (58.0%) 附近，略高 1.5pp，符合"CRM 不介入 → 退化为纯 VLA"的预期
- SR 略超 baseline 可能是统计波动（20 rollouts/task 的方差约 ±2-3pp）

MC2 claim 得到支撑：trigger_rate 与 τ 严格单调递减，整条曲线从 97.8%（τ=0.05）平滑下降到 0.3%（τ=0.45）。

---
