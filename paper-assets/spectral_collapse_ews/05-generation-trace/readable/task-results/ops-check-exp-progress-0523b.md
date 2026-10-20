# ops check exp progress 0523b

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-exp-progress-0523b_20260523T220125_result.json`
- **Structured JSON:** [`2cdf5f20b31c0bdf5380.json`](../../sessions/2c/2cdf5f20b31c0bdf5380.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## exp_019 (GPT-2 small, r=0.2, seed44) — GPU 1

| 指标 | 值 |
|------|-----|
| **当前进度** | **Gen 9** — 正在生成合成样本 ~3520/40000 (9%) |
| **已完成** | Gen 0-8（Gen 0 baseline eval + 8 轮训练） |
| **总计** | --generations 10（Gen 0 baseline + Gen 1-10，共 11 轮） |
| **已运行** | 17h 54m |
| **平均每 gen** | ~2.0h |
| **剩余** | Gen 9 剩余 ~1.8h + Gen 10 ~2h ≈ **~3.5-4h** |

Gen 1-8 指标趋势：eff_rank 476→497（缓慢上升），ppl 10.3→12.7（逐步退化），distinct4 0.65→0.28（明显下降），training loss 1.76→1.00（持续降低）。

## exp_020 (GPT-2 medium, r=0, seed42) — GPU 0

| 指标 | 值 |
|------|-----|
| **当前进度** | **Gen 5** — 正在生成合成样本 ~42560/50000 (85%) |
| **已完成** | Gen 0-4（Gen 0 baseline eval + 4 轮训练） |
| **总计** | --generations 10（同上，共 11 轮） |
| **剩余** | Gen 5 剩余 + Gen 6-10 ≈ **~12-15h**（GPT-2 medium 每 gen 更慢） |

Gen 1-4 指标趋势：eff_rank 23→170（猛增），ppl 15.5→32.1（快速退化），distinct4 0.91→0.76（缓慢下降）。纯合成数据训练（r=0）退化比 r=0.2 更快。

## GPU 状态

| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | **96%** | 26.4 / 97.9 GB |
| 1 | RTX PRO 6000 Blackwell | **90%** | 25.0 / 97.9 GB |

两块 GPU 满载运行，训练正常。

---
