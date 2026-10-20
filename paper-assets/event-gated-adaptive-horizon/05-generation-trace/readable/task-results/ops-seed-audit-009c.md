# ops seed audit 009c

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_seed-audit-009c_20260518T170835_result.json`
- **Structured JSON:** [`6380420d711efa7316eb.json`](../../sessions/63/6380420d711efa7316eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**Seed 核查结果：**

| 实验 | seed |
|------|------|
| exp_009c_008f_walker_s2（原） | **2** |
| exp_009c_s2（被 kill） | **2** |

**Reviewer 怀疑成立**——两者 seed 完全相同，只是 determinism check。进一步佐证：两个实验的 prefill 返回值完全一致（62.7, 51.1, 38.2, 36.8）。

**已执行操作：**
1. Kill 了 exp_009c_s2（seed=2）进程
2. 用 **seed=3** 重启，tmux session `exp_009c_s3`，运行在 cuda:1
3. 日志确认 `[SEED CHECK] config.seed = 3`，prefill 返回值已不同（32.9, 36.9, 30.6, 35.4），证明是独立随机性
4. logdir: `logdir/exp_009c_no_dt_emb_s3`
5. 所有其他参数与原 009c 完全一致（`--gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0`）

---
