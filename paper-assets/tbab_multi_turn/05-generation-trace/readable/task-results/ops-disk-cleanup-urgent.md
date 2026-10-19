# ops disk cleanup urgent

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-urgent_20260518T214212_result.json`
- **Structured JSON:** [`cfc5228c61636c46ff51.json`](../../sessions/cf/cfc5228c61636c46ff51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。结果汇总：

## 磁盘清理

| | 清理前 | 清理后 |
|---|---|---|
| 磁盘使用 | 29G / 30G (95%) | 18G / 30G (59%) |
| 可用空间 | 1.8G | **13G** |
| Checkpoints | 18G | 7.3G |

**删除了 10 个中间 checkpoint**（共释放 ~11G）：
- c1_s137: checkpoint-157, 314 (各 961M)
- c1_s42: checkpoint-3, 157, 314 (各 961M)
- c2_s42: checkpoint-314 (321M)
- c4_s137: checkpoint-157, 314 (各 1.5G)
- c4_s42: checkpoint-157, 314 (各 1.5G)

所有 final checkpoint (step-471) 均保留。pip cache 清理 12M。

## C4_s137 Eval 结果

**P̄ = 5.49%** (5/91)
- HumanEval: 4/36 = 11.1%
- LiveCodeBench: 1/55 = 1.8%

## C2_s42 Eval 状态

正常运行中，进度 31/91，无磁盘错误。空间已充足（13G），后续写 summary 不会有问题。

---
