# check orphaned eval westd

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_orphaned-eval-westd_20260514T230152_result.json`
- **Structured JSON:** [`86d70c23cbe2d80ebe02.json`](../../sessions/86/86d70c23cbe2d80ebe02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### eval 进程状态
**PID 300321 仍然存活**，但 eval 已于 **2026-05-13 01:24** 完成。进程处于 `R (running)` 状态，占用 cuda:0 约 **19.2 GB** 显存，属于僵尸进程（完成任务但未退出）。

命令行：`python eval_repo_cls.py --checkpoint_dir checkpoint-800 --model_name Qwen3-8B --split val --max_seq_length 8192 --device cuda:0`

### eval 结果（ckpt-800, val8192）

| seed | Accuracy | F1 (fail) | F1 (pass) | 结果文件 |
|------|----------|-----------|-----------|----------|
| 42 | **90.48%** | 90.06% | 90.86% | `eval_results/cls8b_seed42.json` |
| 123 | **89.37%** | 89.19% | 89.54% | `eval_results/cls8b_seed123_results.json` |

两个 seed 均通过 MVP-B 标准（per-class F1 >65%, accuracy gap ≥10pp）。

### cuda:0 状态
**被占用** — PID 300321 占着 19.2 GB 显存未释放。需要手动 kill 该进程才能回收 cuda:0。

### 其他 GPU 状态
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| cuda:0 | 73% | 19.2/32.6 GB（僵尸 eval 进程） |
| cuda:1 | 99% | 27.3/32.6 GB |
| cuda:2 | 95% | 30.7/32.6 GB |
| cuda:3 | 97% | 30.9/32.6 GB |

需要我 kill PID 300321 释放 cuda:0 吗？

---
