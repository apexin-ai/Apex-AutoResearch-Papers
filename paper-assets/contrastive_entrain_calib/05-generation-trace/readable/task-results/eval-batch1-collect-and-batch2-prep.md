# eval batch1 collect and batch2 prep

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_batch1-collect-and-batch2-prep_20260521T080813_result.json`
- **Structured JSON:** [`7d328f9bfd6d5443e0ab.json`](../../sessions/7d/7d328f9bfd6d5443e0ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 3 已确认启动（PID 191750, 16834MiB）。汇总如下：

---

## 28034 Eval 状态

### 第一批（进行中）
| GPU | Eval | 进度 | 预计完成 |
|-----|------|------|---------|
| 0 | ckpt5000-v2 | 200/362 (55%) | ~16:36 |
| 1 | ckpt6000 | 180/362 (50%) | ~16:45 |
| 2 | ckpt6500 | 180/362 (50%) | ~16:44 |

### 第二批（已提交 1/4）
| GPU | Eval | 状态 |
|-----|------|------|
| 3 | **exp003s2-ckpt3000** | **已启动** (PID 191750, 16.8GB VRAM) |
| 0 | exp003-ckpt7000-v3 | 等 GPU 0 释放（~16:36） |
| 1 | exp003s2-ckpt2000 | 等 GPU 1 释放（~16:45） |
| 2 | exp003s2-ckpt2500 | 等 GPU 2 释放（~16:44） |

所有第二批 checkpoint 文件已验证存在（245MB adapter_model.safetensors）。

---

## 29046 训练状态

| 实验 | GPU | 当前 step | 进度 | 速度 | ETA |
|------|-----|----------|------|------|-----|
| seed1 (exp003) | cuda:1 | 7737/8000 | 97% | ~31s/step | ~18:25 今天 |
| seed2 (exp-003-s2) | cuda:0 | 3636/8000 | 45% | ~30s/step | ~5月23日 04:00 |

### Checkpoint 就绪情况
- **seed1**: ckpt-7500 已生成（14:10 今天），**ckpt-8000 未生成**（预计 ~18:25）
- **seed2**: ckpt-3500 已生成（15:00 今天），下一个 ckpt-4000 预计 ~19:15

**ckpt-7500/8000 尚未 SCP 到 28034，等 Agent 安排。**

---
