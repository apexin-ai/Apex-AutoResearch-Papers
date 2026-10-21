# ops gpu cleanup and fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_cleanup_and_fix_20260519T131517_result.json`
- **Structured JSON:** [`2377bcb9e632329761e6.json`](../../sessions/23/2377bcb9e632329761e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 报告

### 子任务 1: Kill cuda:0 zombie 进程
- PID 675161/675171 已确认存活但 registry 标记 DONE/success
- 已执行 `kill 675161 675171`，进程已终止
- **cuda:0 已完全释放**: 0 MiB 占用，32110 MiB 可用

### 子任务 2: d112_rsft_s44_eval_bf16 状态
- 进程正常运行：PID 693535（python eval），tmux session 存在，log 文件存在
- 推理进度：16/247 batches（~6%），约 ~40s/batch，预计还需约 2.5 小时
- Registry 已从 PREPARING 推进到 **RUNNING**（PID 693535, cuda:2）

### 子任务 3: GPU 完整状态

| GPU | 显存占用 | 显存空闲 | 利用率 | 状态 |
|-----|---------|---------|--------|------|
| cuda:0 | 0 MiB | 32110 MiB | 0% | **空闲可用** |
| cuda:1 | 31805 MiB | 306 MiB | 79% | 占用（PID 633119） |
| cuda:2 | 29262 MiB | 2848 MiB | 87% | 占用（d112_eval_bf16 + plan019_8b_rsft_no_evidence_eval） |
| cuda:3 | 31594 MiB | 516 MiB | 92% | 占用（PID 679723 + 683952） |

**cuda:0 是唯一空闲 GPU，可立即使用。**

---
