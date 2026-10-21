# ops 14b status westd

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_14b-status-westd_20260518T040646_result.json`
- **Structured JSON:** [`b512b21728575451134c.json`](../../sessions/b5/b512b21728575451134c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验状态：运行中**

- **PID 20700** 存活，GPU 0 占用 32GB VRAM，GPU 利用率 92%
- **当前 phase**: Phase 3.1b — 生成 d1（LoRA(d0) 生成）
- **进度**:
  - d0 生成：✅ 完成 (5000/5000)
  - d0 LoRA finetune：✅ 完成 (3 epochs, loss=0.5451, adapter 已保存)
  - d1 生成：进行中 **2832/5000** (56.6%)

**ETA 估算**:
- d0 生成 5000 条用了约 3.3 小时 (从 08:38 文件创建到 07:56 完成时间推算日志)
- d1 当前速度：2832 条在约 4 小时内生成（08:00 finetune 完 → 12:07 现在）
- d1 剩余 ~2168 条，预计还需 ~1.5-2 小时
- 之后还需：d1 finetune + d2 生成 + d2 finetune + d3 生成 + RF 训练
- **总体预计还需 ~10-12 小时完成全部流程**

---
