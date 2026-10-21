# ssh urgent gpu check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-gpu-check_20260519T194444_result.json`
- **Structured JSON:** [`aae824811112759d2e2a.json`](../../sessions/aa/aae824811112759d2e2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态总览

| GPU | 显存 | 利用率 | 任务 | 状态 |
|-----|------|--------|------|------|
| **0** | **0 MiB / 32 GB** | **0%** | D146 Qwen3-8B CWM repo eval | **已完成，GPU 空闲** |
| 1 | 28 GB / 32 GB | 91% | CLS s456 train (Qwen3-8B) | 运行中 |
| 2 | 29 GB / 32 GB | 85% | DeepSeek CWM repo eval | 运行中 |
| 3 | 28 GB / 32 GB | 86% | DeepSeek CLS s456 train | 运行中 |

## 各任务详情

**D146 (GPU 0)** — pid 778328 已死，eval 于 03:44 正常退出 (EXIT_CODE=0)。结果：
- Accuracy 64.36%, F1 macro 54.42%, fail F1 33.1%
- 6236 条 unparseable predictions
- 输出已保存到 `eval_repo_cwm.json` + `eval_repo_cwm_predictions.jsonl`

**CLS s456 train (GPU 1)** — pid 840928 存活，运行 5h36m，进度 **8407/9335 ≈ 90%**（当前 epoch），~13 it/s，预计几分钟内完成当前 epoch。已有 checkpoint-600 到 checkpoint-1400。

**DeepSeek CWM eval (GPU 2)** — pid 833667 存活，运行 7h05m。

**DeepSeek CLS s456 train (GPU 3)** — pid 842751 存活，运行 5h13m，进度 **1669/6489 ≈ 25.7%**，~10.8s/it，ETA ~14h。

**GPU 0 现在空闲可用。**

---
