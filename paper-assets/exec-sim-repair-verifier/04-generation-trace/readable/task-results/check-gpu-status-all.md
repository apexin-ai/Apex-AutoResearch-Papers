# check gpu status all

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu-status-all_20260516T100839_result.json`
- **Structured JSON:** [`b699372cc01a91cd0f44.json`](../../sessions/b6/b699372cc01a91cd0f44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告

| GPU | 利用率 | 显存 | PID | 任务 |
|-----|--------|------|-----|------|
| **cuda:0** | 99% | 19.6/32.6 GB | 470268 | `train_unified.py` — **deepseek-cls-repo-level**（repo 级 cls，epoch 3） |
| **cuda:1** | 100% | 19.7/32.6 GB | 479953 | `train_unified.py` — **deepseek-cwm-repo-s42**（CWM task，SWE-bench 数据，seed 42） |
| **cuda:2** | 89% | 17.8/32.6 GB | 489475 | `train_unified.py` — **deepseek-cls-func-seed123**（func 级 cls，LoRA r16/α32，seed 123） |
| **cuda:3** | 0% | 0 GB | — | **空闲** |

**cuda:2 (PID 489475)**：仍在运行。checkpoint 目录 `checkpoints_deepseek_cls_func_seed123/` 已产出 `checkpoint-956`，训练进行中。

**cuda:3**：完全空闲，无进程。Inference benchmark 已有产出 `artifacts/benchmark_inference_results.json`，脚本 `benchmark_inference.py` 和 `benchmark_func_inference.py` 均存在。

---
