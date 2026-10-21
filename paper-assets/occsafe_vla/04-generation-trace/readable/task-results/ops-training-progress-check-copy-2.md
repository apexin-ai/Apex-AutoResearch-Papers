# ops training progress check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-progress-check_20260527T040547_result.json`
- **Structured JSON:** [`a511343c78b17692464e.json`](../../sessions/a5/a511343c78b17692464e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 8 个进程存活，GPU 全部在工作。汇总如下：

## westd-34685

| 实验 | GPU | Step | 进度 | 速度 | 剩余时间 | GPU利用率 |
|------|-----|------|------|------|---------|----------|
| detach_ln_v2_s1_35 | cuda:0 | ~16,913 / 50,005 | 33.8% | 1.07 it/s | ~8.6h | 82%, 62G/98G |
| detach_ln_s4 | cuda:1 | ~16,975 / 50,005 | 33.9% | 1.09 it/s | ~8.4h | 99%, 62G/98G |
| ablation_occ_detach_s4 | cuda:2 | ~14,126 / 50,005 | 28.2% | 1.08 it/s | ~9.2h | 99%, 62G/98G |
| mvp_occ_s4 | cuda:3 | ~14,120 / 50,005 | 28.2% | 1.08 it/s | ~9.2h | 99%, 63G/98G |

## westd-10894

| 实验 | GPU | Step | 进度 | 速度 | 剩余时间 | GPU利用率 |
|------|-----|------|------|------|---------|----------|
| full_occ_ln_v2_s1c_r2 | cuda:0 | ~12,657 / 50,005 | 25.3% | 1.08 it/s | ~9.6h | 99%, 62G/98G |
| full_occ_ln_v2_s2_r2 | cuda:1 | ~12,638 / 50,005 | 25.3% | 1.08 it/s | ~9.6h | 99%, 62G/98G |
| detach_ln_v2_s0c_r2 | cuda:2 | ~12,629 / 50,005 | 25.3% | 1.08 it/s | ~9.6h | 99%, 62G/98G |
| full_occ_ln_v2_s0d | cuda:3 | ~10,107 / 50,005 | 20.2% | 1.08 it/s | ~10.3h | 89%, 62G/98G |

## 关键判断

- **全部 8 个实验预计在 ~10h 内完成**，远在 DDL (2026-05-28 12:00 UTC) 之前。
- `full_occ_ln_v2_s0d` 进度最慢（刚过 10k checkpoint，启动晚约 40min），但也仅需 ~10.3h。
- GPU 0 on westd-34685 利用率 82%（瞬时值），速度正常，无异常。
- 所有实验速度稳定在 ~1.08 it/s，无异常波动。
- **无异常标记**，全部健康运行。

---
