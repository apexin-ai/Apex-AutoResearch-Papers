# ops gpu status check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_20260514T061702_result.json`
- **Structured JSON:** [`89e77b15a26912bd784d.json`](../../sessions/89/89e77b15a26912bd784d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **GPU 0**: 0% 利用率, 2751MiB/97887MiB — 运行 **008f** (PID 127766)
- **GPU 1**: 2% 利用率, 4167MiB/97887MiB — 运行 **008e_v3** (PID 126115)
- **008f** (`exp_008f_no_dt_embed_subsample_on_h8`): step=**35000**, 最近 eval 数据在 step 32000 (train_return ~197), 尚未到下一个 eval 点。fps=未记录在最近行
- **008e_v3** (`exp_008e_v3_subsample_on_dt1_h15`): step=**45000**, eval_return=**382.2**, value_mean=**110.7**, fps=6.4。gate_dt 全部锁在 dt=1 (gate_dt_1_frac=1.0, entropy=0)
- **008a**: **已停止**，exit code=0，结束时间 2026-05-14T06:13:09Z

注意：008e_v3 的 gate 完全没有学到变化的 dt，100% 选择 dt=1，gate entropy 为 0。

---
