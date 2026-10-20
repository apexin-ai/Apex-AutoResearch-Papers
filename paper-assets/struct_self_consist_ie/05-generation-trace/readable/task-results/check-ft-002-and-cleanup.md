# check ft 002 and cleanup

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_ft_002_and_cleanup_20260514T080112_result.json`
- **Structured JSON:** [`fc6867b4924ea803bcc4.json`](../../sessions/fc/fc6867b4924ea803bcc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 项目 | 结果 |
|------|------|
| **stale wget** | PID 3762/3804 已 kill |
| **ft_002 状态** | **已崩溃（killed）** — 进程不存在，GPU 全空闲 |
| **训练进度** | 70/585 steps (11.97%)，elapsed 3m32s |
| **最后 loss** | 0.1134 (step 70)，loss 曲线正常下降中 (0.77→0.11) |
| **checkpoint** | 无模型权重保存，仅有 trainer_log.jsonl |
| **崩溃原因** | 不明 — 无 ft_002_train.log（训练可能未用 nohup 重定向，或日志路径不同） |
| **registry** | 已更新：status=DONE, conclusion=killed, metrics 已记录 |

需要重新启动 ft_002 训练时，建议用 nohup 并重定向日志到 `ft_002_train.log` 以便排查。

---
