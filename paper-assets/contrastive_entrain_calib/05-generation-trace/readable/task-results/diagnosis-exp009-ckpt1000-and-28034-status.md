# diagnosis exp009 ckpt1000 and 28034 status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp009-ckpt1000-and-28034-status_20260520T121745_result.json`
- **Structured JSON:** [`f2f278ff01fb7ffcfec4.json`](../../sessions/f2/f2f278ff01fb7ffcfec4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-009 eval 已完成，结果已拿到。exp-003 eval 还在跑（280/362）。汇总如下：

---

## exp-009 ckpt-1000 Eval
状态：**完成**
ToF: 0.0608 | NoF: 0.9337 | SYCONScore: 0.1141
vs ckpt-500: ToF 0.0663→0.0608 (↓8.3%) | SYCONScore 0.1238→0.1141 (↓7.8%)
Kill 标准: **不满足** (SYCONScore 0.1141 > 0.10, ToF 0.0608 > 0.03)

⚠️ 但趋势下行——ckpt-500→ckpt-1000 两个指标均退化，ToF 和 SYCONScore 都在下降。

## exp-003 ckpt-5000 Eval
状态：**进行中** (280/362, ~77%)
预计 ~15-20 分钟内完成

## 28034 GPU
| GPU | Util | VRAM Used | VRAM Total |
|-----|------|-----------|------------|
| 0 | 17% | 16.5 GB | 31.8 GB |
| 1 | 0% | 30.7 GB | 31.8 GB |
| 2 | 0% | 30.0 GB | 31.8 GB |
| 3 | 0% | 0 GB | 31.8 GB |

GPU0 在跑 exp-003 eval（17% util），GPU1/2 被占用但 idle（可能是 exp-009 训练残留或其他进程），GPU3 空闲。

---
