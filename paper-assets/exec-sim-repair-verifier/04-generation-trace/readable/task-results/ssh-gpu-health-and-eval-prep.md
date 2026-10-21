# ssh gpu health and eval prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-health-and-eval-prep_20260519T221254_result.json`
- **Structured JSON:** [`0308b4068e92b43cea81.json`](../../sessions/03/0308b4068e92b43cea81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| GPU | 任务 | 状态 | 详情 |
|-----|------|------|------|
| **0** | CWM s123 训练 | **已死 (EXIT_CODE=124)** | timeout 触发。进度 2320/6633 (35%)，运行 ~2h27m 后被 kill。父进程 862540 仍在（壳），子进程 862545 仍占 21GB 显存 |
| **1** | CLS s456 训练 | **已死** | PID 840928 不存在。但 **checkpoint-2200 已存在**（05:51 写入），还有 2000/1800/1600/600 共 5 个 checkpoint |
| **2** | DeepSeek CWM eval | **运行中** | PID 833667，已跑 9h34m，占 29.6GB 显存，GPU 利用率 85% |
| **3** | DeepSeek CLS s456 训练 | **运行中** | PID 842751，已跑 7h42m，占 26.8GB 显存，GPU 利用率 99% |

关键发现：
- **GPU 0 CWM s123**：timeout 86400s 不应在 2.5h 触发——日志显示 `EXIT_CODE=124`，实际是训练脚本内的 timeout 或 OOM 后被 kill。子进程 862545 仍挂着占显存，需要手动清理。
- **GPU 1 空闲**（0MB 显存、100% util 是空转），checkpoint-2200 可用于 eval。
- **eval 脚本**：只有 `eval_repo_cls.py`，无 `_v2` 版本。

---
