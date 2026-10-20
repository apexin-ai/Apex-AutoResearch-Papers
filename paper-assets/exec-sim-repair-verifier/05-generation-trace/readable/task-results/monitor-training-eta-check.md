# monitor training eta check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-eta-check_20260515T005703_result.json`
- **Structured JSON:** [`49ab3f48571494dd003e.json`](../../sessions/49/49ab3f48571494dd003e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| Experiment | GPU | Step | Progress | ETA | Loss | Eval Loss |
|---|---|---|---|---|---|---|
| cls-8b-s42-resume | 1 | 1542/6633 | 23% | **~17h** | 0.886 | 0.323 |
| cwm-8b-conda-v4 | 2 | ~2800/6633 | 42% | **~25h** | 0.063 | 0.426 |
| cls-8b-seed123-conda-v3 | 3 | 5102/6633 | 77% | **~5.4h** | 0.090 | 0.365 |
| cls8b-s42-ckpt800-eval | 0 | — | **DONE** | — | — | Acc=84.5% |

要点：
- **seed123 最快**，预计今天下午完成
- **CWM 最慢**，eval 每 100 步跑一次（每次 19 分钟），严重拖慢训练。建议改成 200 或 400 步 eval 一次
- **eval 已完成**，GPU 0 空闲可用，ckpt-800 准确率 84.5%，F1-macro 79.2%

---
