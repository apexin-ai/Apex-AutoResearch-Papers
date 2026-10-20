# status gpu check 20260522 1400

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_gpu_check_20260522_1400_20260522T134931_result.json`
- **Structured JSON:** [`b135f5cacf27622b8570.json`](../../sessions/b1/b135f5cacf27622b8570.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 1. GPU 状态
| GPU | 型号 | 显存占用 | 利用率 | 进程 |
|-----|------|---------|--------|------|
| cuda:0 | RTX PRO 6000 Black | 46067/97887 MiB | 50% | PID 757995 (python) |
| cuda:1 | RTX PRO 6000 Black | 46035/97887 MiB | 98% | PID 764812 (python) |
| cuda:2 | RTX PRO 6000 Black | 14570/97887 MiB | 100% | PID 779496 + 780665 (两个 python) |
| cuda:3 | RTX PRO 6000 Black | 0/97887 MiB | 0% | 无进程 |

## 2. bs8_adaptive (cuda:0)
当前 step: 3941/6103 (65%)，已运行 ~3h，预计剩余 ~1h33m

## 3. bs8_uniform (cuda:1)
当前 step: 3286/6103 (54%)，已运行 ~2h20m，预计剩余 ~2h

## 4. detect_remove wiki eval
- **PID 779491** (bash wrapper): 仍在运行，elapsed 12m30s，log 显示进度 1000/5000 docs
- **PID 780665**: 另一个 eval_perplexity_fp32.py 进程，运行 3m11s，输出到 `eval_wiki_fp32.json`（不同文件名）
- **已有 eval_wiki.json**: 结果异常 — **loss=NaN, perplexity=Infinity**（27M tokens, 721s）。这是之前完成的一次运行，结果无效
- eval_results 目录下还有 eval_holdout.json 和 eval_owt.json

## 5. cuda:3
空闲，无进程，显存 0 MiB，利用率 0%

---
