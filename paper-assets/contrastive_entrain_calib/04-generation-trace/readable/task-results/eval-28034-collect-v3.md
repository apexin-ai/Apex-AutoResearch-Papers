# eval 28034 collect v3

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_28034-collect-v3_20260523T070258_result.json`
- **Structured JSON:** [`4e41c3f7d7d66c23dc77.json`](../../sessions/4e/4e41c3f7d7d66c23dc77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ckpt-7000 eval 已在 GPU0 上运行。训练在 step 7290，ckpt-7500 尚未生成，GPU2/GPU3 暂无新任务。

## 汇总

### 已完成 Eval 结果

| GPU | Eval | SYCONScore | ToF | NoF | > vanilla (0.1335)? |
|-----|------|-----------|------|------|---------------------|
| 0 | ACT s2 ckpt-2500 | **0.2132** | 0.1215 | 0.8674 | Yes (+59.7%) |
| 2 | reduced-lora ckpt-6000 | **0.2129** | 0.1215 | 0.8564 | Yes (+59.5%) |
| 3 | reduced-lora ckpt-6500 | **0.2368** | 0.1381 | 0.8287 | Yes (+77.4%) |

**ckpt-6500 是 reduced-lora 目前最好的 checkpoint**，SYCONScore 0.2368。

### 新启动的 Eval

| GPU | Eval | PID | 状态 |
|-----|------|-----|------|
| 0 | reduced-lora ckpt-7000 | 55429 | 运行中，已加载模型开始推理 |
| 2 | — | — | 空闲，等 ckpt-7500 |
| 3 | — | — | 空闲，等 ckpt-7500 |

### Reduced-lora 训练状态
- **当前 step**: 7290
- **最新 checkpoint**: checkpoint-7000 (14:29 生成)
- **Loss**: total_loss ≈ 0.000156，lr ≈ 4.55e-6（在衰减）
- **预计 ckpt-7500**: 按 ~57min/500步，约 15:40 左右生成
- **可用 checkpoints**: 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000

GPU1 训练 (PID 30011) 未触碰。

---
