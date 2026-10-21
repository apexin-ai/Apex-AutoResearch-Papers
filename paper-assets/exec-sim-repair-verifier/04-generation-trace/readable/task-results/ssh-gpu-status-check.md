# ssh gpu status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-status-check_20260519T182646_result.json`
- **Structured JSON:** [`a572db4ffe41666f98ca.json`](../../sessions/a5/a572db4ffe41666f98ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

### 4 卡全满载

| GPU | 利用率 | 显存 | 温度 | 进程 | 实验 | 状态 |
|-----|--------|------|------|------|------|------|
| **cuda:0** | 92% | 27.7/32.6 GB | 62°C | PID 778334 (子进程 of 778328) | D146 Qwen3 CWM eval @seq4096 | **运行中** — 9144/9784 (93.5%), acc=64.2%, 预计~1h完成 |
| **cuda:1** | 85% | 28.1/32.6 GB | 67°C | PID 840933 (子进程 of 840928) | CLS 8B s456 train v2 | **运行中** — 1228/6633 (18.5%), eval_loss=0.392, ~8.7s/it, 刚过 checkpoint-1200, 已跑 4h13m |
| **cuda:2** | 75% | 28.8/32.6 GB | 53°C | PID 833672 | **DeepSeek CWM repo s42 seq4096 eval** | **运行中** — 4476/9784 (45.7%), acc=61.1%, 已跑 5h48m |
| **cuda:3** | 99% | 28.5/32.6 GB | 72°C | PID 842756 (子进程 of 842751) | DeepSeek CLS s456 train v3 | **运行中** — 1246/6489 (19.2%), ~10.7s/it, 已跑 3h46m |

### PID 存活状态

| PID | 实验 | 状态 |
|-----|------|------|
| 778328 | D146 Qwen3 CWM eval | **存活** (运行 18h16m) |
| 840928 | CLS 8B s456 train v2 | **存活** (运行 4h19m) |
| 842751 | DeepSeek CLS s456 train v3 | **存活** (运行 3h56m) |
| 698033 | deepseek-cls-repo-v5 | **已死** |
| 668680 | deepseek-cwm-repo-s123 eval | **已死** |
| 734440 | D131-cwm-s42-epoch3-seq2048 | **已死** |

### cuda:2 说明

之前的 D131 (PID 734440) 已结束。当前 cuda:2 上跑的是 **DeepSeek CWM repo s42 seq4096 eval** (PID 833672, 父进程 833671)，checkpoint-13266，batch_size=4，max_new_tokens=512。进度约 45.7%，速率 ~20s/4条，预计还需 ~6-7h。

---
