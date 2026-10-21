# diagnosis 28034 eval and gpu

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_28034-eval-and-gpu_20260520T080254_result.json`
- **Structured JSON:** [`3cd3b7e2ab25ed07ca35.json`](../../sessions/3c/3cd3b7e2ab25ed07ca35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-28034 (exp-009)

### GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 5/32607 MiB (空闲) |
| 1 | 100% | 31432/32607 MiB |
| 2 | 67% | 30668/32607 MiB |
| 3 | 49% | 16766/32607 MiB |

GPU 1-2 跑训练 (PID 200881/200882)，GPU 3 跑 eval (PID 227022)，GPU 0 空闲。

### exp-009 训练
- **PID 200283**: 运行中，已 5h16m
- **Step**: 902/8000 (11%)，~20s/step，预估剩余 ~40h
- **最新 reward**: r1=0.397, r2=0.000, r3=0.714, combined=0.635

### exp-009 ckpt-500 eval
- **PID 227017**: 运行中，已 1h04m
- **进度**: 180/362 (50%)，每 20 个约 6-7min
- **结果文件**: **尚未生成**（results 目录为空）
- 预估还需 ~1h 完成

**eval 还在跑，结果还没出来。需要等完成后再读 ToF/NoF/SYCONScore。**

---

## westd-29046 (exp-003)

### GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 95% | 38049/97887 MiB |
| 1 | 97% | 38161/97887 MiB |

两卡高负载运行中。

### exp-003 (seed1)
- **PID 70649**: 运行中，已 1天15h31m
- **Step**: 3760/8000 (47%)，~45s/step
- **最新 checkpoint**: checkpoint-4500 (May 20 12:33)
- **reward (step 3760)**: r3_mean=0.6972, std=0.4051
- **预估剩余**: ~55h

### exp-003-s2 (seed2)
- **PID 237437**: 运行中，已 8h05m
- **Step**: 793/8000 (10%)，~40s/step
- **最新 checkpoint**: 有一个（May 20 13:51）
- **预估剩余**: ~80h

两个实验都是 R3-only（d_syc not loaded），正常运行。

---
