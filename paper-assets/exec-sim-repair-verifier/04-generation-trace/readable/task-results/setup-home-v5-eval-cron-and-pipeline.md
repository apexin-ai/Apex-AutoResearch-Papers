# setup home v5 eval cron and pipeline

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_home-v5-eval-cron-and-pipeline_20260514T223815_result.json`
- **Structured JSON:** [`9f7769dc79419e340dae.json`](../../sessions/9f/9f7769dc79419e340dae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

| 项目 | 值 |
|------|-----|
| PID | **3179262** |
| 已运行 | ~15 分钟 |
| 命令 | `python eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-600 --split val --max_seq_length 5120 --device cuda:0` |
| Registry | `cls4b-v5-ckpt600-val5120-eval` → RUNNING, parent=repo-level-cls-v5 |
| Cron 监控 | 每 3 分钟检查 PID 存活（job `03ba2fcf`） |

val@5120 eval 通常 20-40 分钟完成，预计 **再跑 5-25 分钟**。进程结束时 cron 会自动通知。

---
