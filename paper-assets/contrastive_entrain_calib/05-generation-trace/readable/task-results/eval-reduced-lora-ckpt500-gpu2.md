# eval reduced lora ckpt500 gpu2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_reduced-lora-ckpt500-gpu2_20260522T191608_result.json`
- **Structured JSON:** [`23e3a6e5e56e8f8eba99.json`](../../sessions/23/23e3a6e5e56e8f8eba99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-004-reduced-lora ckpt-500 结果

| 指标 | 值 |
|------|-----|
| **SYCONScore** | **0.1515** |
| ToF | 0.0829 |
| NoF | 0.8840 |

### 对比

| 实验 | SYCONScore | vs vanilla | 说明 |
|------|-----------|------------|------|
| Vanilla baseline | 0.1335 | — | 无训练 |
| **Reduced LoRA ckpt-500** | **0.1515** | **+13.5%** | r=64, α=64, 4 modules (qkvo) |
| Standard ACT ckpt-500 | 0.2230 | +67.0% | Full LoRA (r=128, α=128, 8 modules) |
| Reduced LoRA ckpt-1000 | 0.1700 | +27.3% | 同配置，更多步数 |

### 分析

Reduced LoRA ckpt-500 的 SYCONScore (0.1515) 显著低于标准 ACT ckpt-500 (0.2230)，差距 **-32.1%**。LoRA capacity 减半（rank 64→128, modules 4→8）明显制约了 calibration 能力。

好消息是 ckpt-500→ckpt-1000 改善了 12.2%（0.1515→0.1700），说明 reduced LoRA 仍在学习，只是收敛更慢。可能需要更多训练步数才能接近标准 ACT 的表现。

---
