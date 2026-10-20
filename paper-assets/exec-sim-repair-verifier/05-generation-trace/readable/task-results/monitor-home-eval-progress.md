# monitor home eval progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_home-eval-progress_20260514T234739_result.json`
- **Structured JSON:** [`8a10deea5cb5ae4f0781.json`](../../sessions/8a/8a10deea5cb5ae4f0781.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 进程 cls4b-v5-ckpt4000-val5120-eval (PID 3186818)
- **状态**: 运行中，已运行 12 分 30 秒
- **进度**: 1632 / 9335 样本 (**17.5%**)
- **速率**: ~130.6 样本/分钟
- **ETA**: 约 **59 分钟**后完成（预计 17:47 左右）
- **GPU**: RTX 5090, 100% 利用率, 31.7GB/32.6GB 显存, 81°C, 537W

⚠️ 日志文件 `~/runs/exec-sim-repair-verifier/cls4b-v5-ckpt4000-val5120-eval.log` 不存在，stdout 输出到 tty（/dev/pts/0），没有重定向到文件。进度通过 output jsonl 行数推算。

### 可用 Checkpoints (checkpoints_repo_cls_v5/)
| Checkpoint | 时间 |
|---|---|
| checkpoint-4600 | May 13 14:24 |
| checkpoint-4400 | May 13 13:49 |
| checkpoint-4200 | May 13 13:13 |
| checkpoint-4000 | May 13 12:38 |
| checkpoint-600 | May 13 02:31 |

checkpoint-4200、4400、4600 均已存在，后续 eval 可直接用。

---
