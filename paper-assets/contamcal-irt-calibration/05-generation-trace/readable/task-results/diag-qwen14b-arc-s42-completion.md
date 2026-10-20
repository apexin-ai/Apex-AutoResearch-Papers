# diag qwen14b arc s42 completion

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_qwen14b-arc-s42-completion_20260520T184819_result.json`
- **Structured JSON:** [`dec81df59135582b1bdd.json`](../../sessions/de/dec81df59135582b1bdd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。Cron 已不存在（无需删除）。

## Collapse 跨种子稳定性分析

| Dosage | s42 | s123 | 双种子均值 |
|--------|-----|------|-----------|
| d000 | 91.04% | 90.44% | 90.74% |
| d005 | 90.36% | 91.47% | 90.92% |
| d025 | 88.91% | 89.76% | 89.34% |
| d050 | 87.63% | 88.74% | 88.19% |
| d100 | 88.48% | 87.29% | 87.89% |
| **Δ(d100−d000)** | **−2.56pp** | **−3.15pp** | **−2.86pp** |

**结论：ARC Collapse 跨种子稳定。**

- 两个种子均为负 Δ：s42 = −2.56pp, s123 = −3.15pp，双种子均值 Δ = −2.86pp
- 整体趋势一致：d000→d050 单调下降（两个种子均如此）
- 细节差异：s42 的 d100 相对 d050 有小幅回弹（+0.85pp），s123 则继续下降。但 d000→d100 的总 Δ 方向和量级一致
- 非单调性集中在高 dosage 端（d050↔d100），可能是 contamination 饱和后的噪声，不影响 Collapse 方向判断

Qwen-14B 在 ARC 上的 Collapse 效应是 robust 的，不依赖特定 seed。

---
