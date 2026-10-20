# ssh d064 collect final

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d064_collect_final_20260519T124552_result.json`
- **Structured JSON:** [`2ce8c3a7cb4736297c5d.json`](../../sessions/2c/2ce8c3a7cb4736297c5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## d064 状态汇总

**所有 6 个推理任务仍在运行中，尚无完成的文件。**

### 当前进度

| GPU | 任务 | 进度 | 速度 | ETA |
|-----|------|------|------|-----|
| GPU 0 | Llama greedy unc | 546/998 (55%) | ~17s/doc | ~23:00 今天 |
| GPU 1 | Qwen beam-4 unc | 614/998 (62%) | ~20s/doc | ~23:00 今天 |

### 已完成的步骤
- Llama LoRA 训练 ✅ (train_loss=0.0571, token_acc=98.1%)
- Llama LoRA merge ✅

### 待运行（按队列顺序）
- GPU 0: Llama greedy con → beam-4 unc → beam-4 con（最终完成 ETA ~5月20日 16:40）
- GPU 1: Qwen beam-4 con（ETA ~5月20日 04:30）

### 关键信息
- 服务器**没有**重启，原始进程仍在运行（PID 98185, 102892）
- Qwen beam-4 unc 解析失败率 ~3.3%（16/490）
- Cascade 脚本用 `set -e`，任一步骤失败会终止整个链
- 需要等文件完成后才能计算 F1 / violation rate 指标

---
