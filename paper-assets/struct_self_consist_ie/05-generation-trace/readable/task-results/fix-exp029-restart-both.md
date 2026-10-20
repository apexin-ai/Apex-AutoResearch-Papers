# fix exp029 restart both

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp029_restart_both_20260518T013614_result.json`
- **Structured JSON:** [`3b418b706cb83e1659a2.json`](../../sessions/3b/3b418b706cb83e1659a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均正常训练中，无报错。

## 汇报

| 项目 | 结果 |
|------|------|
| PID 416808 | 已不存在（No such process） |
| 磁盘可用 | 129G / 250G (49% used) |
| exp_029a PID | **441469** (GPU 0, 3-epoch, 351 steps, ~2.7s/it) |
| exp_029b PID | **441471** (GPU 1, 10-epoch, 1170 steps, ~2.7s/it) |
| GPU 显存 | GPU 0: 24452 MiB / 32607 MiB, GPU 1: 24452 MiB / 32607 MiB |
| GPU 利用率 | 均为 100% |
| 日志 | 两个实验均已正常开始训练，无 error/warning（仅 tokenizer PAD 对齐 warning，正常） |

预估完成时间：exp_029a ~17min，exp_029b ~55min。

---
