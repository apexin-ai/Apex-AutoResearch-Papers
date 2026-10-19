# diagnosis exp003 ckpt5000 eval results

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp003-ckpt5000-eval-results_20260520T124407_result.json`
- **Structured JSON:** [`ace1e35031b6d9b5311c.json`](../../sessions/ac/ace1e35031b6d9b5311c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已全部获取。GPU 全部空闲（2 MiB），可以确认无 exp-009 残留进程。

---

## exp-003 ckpt-5000 Eval 结果

| 指标 | 值 |
|------|-----|
| **ToF** | 0.0608 |
| **NoF** | 0.9669 |
| **SYCONScore** | **0.1144** |
| n_valid / n_invalid / n_total | 181 / 181 / 362 |
| 耗时 | 5146s (~85min) |

## Claim 2 判定

**不满足。** SYCONScore = 0.1144 < 0.134 阈值。

R3-only (exp-003) 不仅未优于 vanilla baseline (0.1335)，反而**更差**：
- ToF 从 0.0718 降到 0.0608（更不愿纠正正确观点 → 好事）
- 但 NoF 从 0.9448 升到 0.9669（更不愿反驳错误压力 → 坏事，说明模型变得更 sycophantic）
- 综合 SYCONScore 下降了 14.3%

解读：单独的 NLI behavioral reward (R3) 不足以改善 sycophancy，反而让模型在 invalid pressure 下更倾向于顺从。这支持了 direction-contrastive reward (R1/R2) 的必要性。

## 28034 GPU 状态

| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| 0 | RTX 5090 | 2 / 32607 MiB | 0% |
| 1 | RTX 5090 | 2 / 32607 MiB | 0% |
| 2 | RTX 5090 | 2 / 32607 MiB | 0% |
| 3 | RTX 5090 | 2 / 32607 MiB | 0% |

**四张卡完全空闲，exp-009 已彻底清除，无残留进程。**

---
