# urgent exp029 full pipeline

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_exp029_full_pipeline_20260518T005118_result.json`
- **Structured JSON:** [`46e8f5dfbf13c5d38afd.json`](../../sessions/46/46e8f5dfbf13c5d38afd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练均正常运行，无报错。

## 汇报

### 1. 磁盘
- 无需清理（使用率 40%，可用 151GB）

### 2. nvidia-smi
| GPU | 状态 | 显存 | 利用率 |
|-----|------|------|--------|
| 0 (RTX 5090) | exp_029a (3-epoch) | 24472/32607 MiB | 100% |
| 1 (RTX 5090) | exp_029b (10-epoch) | 24462/32607 MiB | 87% |
| 2 (RTX 5090) | 空闲 | 2 MiB | 0% |
| 3 (RTX 5090) | 空闲 | 2 MiB | 0% |

### 3. 训练进程
| 实验 | PID | tmux session | 状态 | 总步数 | 速度 |
|------|-----|---|---|---|---|
| exp_029a (3-epoch) | 436761 | exp_029a | 训练中 17/351 steps | 351 steps | ~2.8s/it |
| exp_029b (10-epoch) | 436916 | exp_029b | 训练中 12/1170 steps | 1170 steps | ~2.9s/it |

### 4. 预估完成时间
- exp_029a: ~351 steps × 2.8s ≈ **16 分钟**
- exp_029b: ~1170 steps × 2.9s ≈ **57 分钟**

### 5. 关键修复
- 原问题：LlamaFactory 默认 torchrun 4卡。已用 `FORCE_TORCHRUN=0` + `CUDA_VISIBLE_DEVICES` 强制单卡模式，成功各占一张 GPU。
- 无任何错误或异常。

---
