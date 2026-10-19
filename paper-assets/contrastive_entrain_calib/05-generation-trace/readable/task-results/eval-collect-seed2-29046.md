# eval collect seed2 29046

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect-seed2-29046_20260522T035518_result.json`
- **Structured JSON:** [`24073b1e09005cc6c0a4.json`](../../sessions/24/24073b1e09005cc6c0a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Seed 2 ckpt-4000 Eval 结果
| 指标 | 值 |
|------|-----|
| **SYCONScore** | **0.143** |
| ToF | 0.0773 |
| NoF | 0.9448 |

**这是 seed 2 目前最高分**，且超过了 vanilla baseline (0.134) 和 seed 1 ckpt-4000 (0.114)。

Seed 2 各 checkpoint 趋势：
- ckpt-2000: 0.085 → ckpt-2500: 0.105 → ckpt-3000: 0.095 → ckpt-3500: 0.074 → **ckpt-4000: 0.143**

ckpt-4000 出现大幅跳升，从 3500 的低谷直接拉到最高点。

### 训练进度
- 当前 step: **6384/8000 (80%)**
- 速度: ~26s/step
- ETA: ~11.5 小时
- 最新 checkpoint: **checkpoint-6000**

Registry 已更新为 DONE/success。

---
