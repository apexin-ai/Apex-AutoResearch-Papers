# eval llama31 s123 batch

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_llama31-s123-batch_20260516T150914_result.json`
- **Structured JSON:** [`df51846a2a7471784009.json`](../../sessions/df/df51846a2a7471784009.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 当前运行中的 eval（4/4 GPU 占满）

| GPU | Eval | 进度 | PID |
|-----|------|------|-----|
| 0 | taxei-s123 injected | 8/47 (~17%) | 293496 |
| 1 | vanilla-s123 injected | 32/47 (~68%) | 290182 |
| 2 | taxei-s123 clean | 14/47 (~30%) | 291995 |
| 3 | random-s123 clean | 18/47 (~38%) | 292353 |

### 已排队

- **random-s123 injected** (PID 294588): 等待 vanilla-s123 eval (PID 290182) 完成后自动在 GPU 1 上启动

### Registry 更新

- `llama31-taxei-s123` → checkpoint_path 已写入
- `llama31-random-s123` → checkpoint_path 已写入
- `llama31-taxei-s123-eval` → RUNNING
- `llama31-taxei-s123-clean` → RUNNING
- `llama31-random-s123-clean` → RUNNING
- `llama31-random-s123-eval` → QUEUED

### Scale-up datagen

PID 266813 已死，`data/scale_up/` 目录不存在。数据生成失败或从未正确启动。

### 待办

5 个 eval 中 4 个已在跑，第 5 个（random-s123 injected）已自动排队。预计 vanilla-s123 约 10-15 分钟内完成后自动启动。全部 eval 预计 ~40 分钟内完成。

---
