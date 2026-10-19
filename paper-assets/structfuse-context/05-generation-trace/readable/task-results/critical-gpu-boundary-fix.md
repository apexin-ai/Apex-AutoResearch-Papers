# critical gpu boundary fix

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_critical_gpu_boundary_fix_20260512T115336_result.json`
- **Structured JSON:** [`f5b0ee69c951cd9b2f02.json`](../../sessions/f5/f5b0ee69c951cd9b2f02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

---

## 修复报告

| 项目 | 结果 |
|------|------|
| **kill PID 59170** | 成功终止（SIGTERM，无需 force kill） |
| **GPU 5 释放** | 已确认 0MiB，无残留进程 |
| **run_mvp.py** | 服务器上不存在此文件。进程名为 `python run_mvp.py`，但文件已被删除或从未在 `/root/structfuse/` 下。实际存在的类似入口是 `mvp_phase1.py` |
| **CUDA_VISIBLE_DEVICES=4 验证** | 生效：仅可见 1 块 GPU（物理 GPU 4），device 0 映射正确 |

**修复的文件清单：**

服务器端（4 个）：
1. `/root/structfuse/training/train.py`
2. `/root/structfuse/evaluation/eval_retrieval.py`
3. `/root/structfuse/evaluation/eval_swebench.py`
4. `/root/structfuse/mvp_phase1.py`

本地（6 个）：
1. `artifacts/code/training/train.py`
2. `artifacts/code/evaluation/eval_retrieval.py`
3. `artifacts/code/evaluation/eval_swebench.py`
4. `artifacts/_project/intermediate/train.py`
5. `artifacts/_project/data/eval_retrieval.py`
6. `artifacts/_project/data/eval_swebench.py`

`_project/intermediate/contrastive_model.py` 无 device 相关代码，无需修复。

---
