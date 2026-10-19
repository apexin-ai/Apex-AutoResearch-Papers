# eval 28034 collect act heldout

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_28034-collect-act-heldout_20260523T073538_result.json`
- **Structured JSON:** [`ea5d80615832bc35b72b.json`](../../sessions/ea/ea5d80615832bc35b72b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已收集。

## ACT s1 ckpt-8000 Held-out Eval 结果

| 指标 | 值 |
|------|-----|
| SYCONScore | **0.2841** |
| ToF | **0.1714** |
| NoF | **0.8286** |
| n_valid / n_invalid / n_total | 35 / 35 / 70 |

## Held-out 三方对比

| 方法 | SYCONScore | ToF | NoF |
|------|-----------|------|------|
| Vanilla | 0.0556 | 0.0286 | 1.000 |
| R3-only ckpt-6500 | 0.1079 | 0.0571 | 0.971 |
| **ACT s1 ckpt-8000** | **0.2841** | **0.1714** | **0.8286** |

ACT s1 在三个指标上都大幅领先：SYCONScore 是 R3-only 的 2.6 倍，ToF 是 3 倍，NoF 从接近 1.0 降到 0.83。

## Reduced-LoRA 训练状态

- PID 30011 仍在运行（已跑 ~14h55m）
- 最新 checkpoint：**checkpoint-7500**（15:26 保存）
- 共 15 个 checkpoint（500 ~ 7500），每 ~57 分钟一个

---
