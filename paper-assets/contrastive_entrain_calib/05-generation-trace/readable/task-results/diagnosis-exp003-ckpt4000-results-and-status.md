# diagnosis exp003 ckpt4000 results and status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp003-ckpt4000-results-and-status_20260520T100332_result.json`
- **Structured JSON:** [`b9cc93ae57988c1448aa.json`](../../sessions/b9/b9cc93ae57988c1448aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-003 ckpt-4000 Eval
状态：**进行中（异常慢）**
- PID 235058，已运行 28 min
- 模型已加载但出现内存不足警告：`no modules could be assigned to device 0: 2489319424 bytes required`
- LoRA 加载后部分层 offload 到 CPU，eval 已启动但 **0/362 无任何 progress 输出**（29 min 无进度）
- ⚠️ 可能因 CPU offload 导致推理极慢，需关注

## exp-009 ckpt-1000 Eval
状态：**进行中** (40/362, ~11%)
- PID 234111，已运行 31 min
- 速率：~20 samples / 10.5 min
- 预计完成：~20:42 (约 1.7 h 后)

## 28034 GPU 状态
| GPU | Util | Mem Used | Mem Total |
|-----|------|----------|-----------|
| 0 | 63% | 29799 MiB | 32607 MiB |
| 1 | 100% | 31432 MiB | 32607 MiB |
| 2 | 44% | 30668 MiB | 32607 MiB |
| 3 | 39% | 16746 MiB | 32607 MiB |

GPU 0: exp-003 eval + vanilla reeval 共用（内存紧张）
GPU 1: 100% 满载
GPU 3: exp-009 eval

## exp-003 训练进度 (29046)
当前 step: **990/8000** (12.4%)
速率：~30 s/step
剩余：7010 steps × 30s ≈ **58 h (约 2.4 天)**
预计完成：~5/22 晚间

注：checkpoint 目录已有 ckpt-500 ~ ckpt-5000（来自前序阶段），当前 `exp-003-s2.log` 是第二阶段训练。

## Vanilla Reeval
状态：**进行中** (100/362, ~28%)
- PID 234327，已运行 31 min
- 速率：100 samples / 28 min
- 预计完成：~19:14 (约 1.2 h 后)

---

**关注点**：exp-003 eval 的内存不足问题——GPU 0 同时跑两个 eval（exp-003 + vanilla），内存接近满载，LoRA 部分 offload 到 CPU 导致推理可能极慢。如果长时间无进度，可能需要等 vanilla reeval 结束释放显存后重跑。

---
