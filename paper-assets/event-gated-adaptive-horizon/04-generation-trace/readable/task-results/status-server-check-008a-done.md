# status server check 008a done

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_server_check_008a_done_20260514T061744_result.json`
- **Structured JSON:** [`7bd6452acff7a68bb84f.json`](../../sessions/7b/7bd6452acff7a68bb84f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/report_server_status.md`。

**汇总:**

| 实验 | GPU | Step | 状态 | 关键指标 |
|------|-----|------|------|---------|
| exp_008f (no_dt_embed, subsample, h8) | GPU 0 | 35K/105K | 运行中 | train_return ~197 |
| exp_008e_v3 (subsample, dt1, h15) | GPU 1 | 45K/105K | 运行中 | eval_return 382.2, **gate 100% dt=1** |
| exp_008a (fixed_dt2, no_subsample) | — | 112K (完成) | 已结束 | train_return 628-842 |

**需注意**: exp_008e_v3 的 gate 完全退化——dt=1 占 100%、entropy=0，subsample 机制形同虚设。exp_008a 无 `checkpoint.ckpt`，仅有 `latest.pt`。

---
