# monitor deberta finetune

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_deberta-finetune_20260522T174529_result.json`
- **Structured JSON:** [`d3ce13fdb9bb89ec7265.json`](../../sessions/d3/d3ce13fdb9bb89ec7265.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态报告

| 项目 | 状态 |
|------|------|
| **进程** | PID 650586 存活，已运行 22h14m（含数据加载/tokenization时间） |
| **当前进度** | Step 4312/21820（19.8%），epoch 1 即将完成（4312/4364 = **98.8%**） |
| **训练速度** | ~3.5 it/s |
| **Eval 结果** | 尚无——epoch 1 还差 ~52 步完成，eval 即将触发 |
| **Checkpoints** | 输出目录 `/root/autodl-tmp/symb_invariant_consensus/models/deberta-large-pw-owa/` 已创建但为空，等 epoch 1 eval 完成后保存 |
| **预估剩余时间** | (21820-4312) / 3.5 ≈ **1h23m**（不含 eval 时间） |
| **磁盘** | 数据盘 350G 用了 220G，剩余 131G，充足 |

**关键信息**：每 epoch 4364 步，当前 4312 步，再跑约 15 秒就完成 epoch 1 并触发第一次 eval。5 个 epoch 总计约 1.5h 训练时间（不含 eval），预计约 1h23m 后全部完成。

---
