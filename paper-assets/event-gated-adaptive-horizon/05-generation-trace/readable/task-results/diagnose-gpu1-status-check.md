# diagnose gpu1 status check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu1_status_check_20260514T044415_result.json`
- **Structured JSON:** [`19ff33df460298a2c789.json`](../../sessions/19/19ff33df460298a2c789.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

**GPU 0 — 008a / 008d：**
- **008a** (`exp_008a_fixed_dt2_no_subsample`): step 76000, train_return 590.76
- **008d** (`exp_008d_subsample_on_h8`): step 55000（metrics 行仅含 step）
- 两个 python 进程在跑：PID 106947 (4158 MiB) + PID 109524 (2744 MiB)

**GPU 1 — exp_008e_v3 正在运行：**
- PID 126115 (python dreamer.py, 4156 MiB, 运行 15 分钟)，`CUDA_VISIBLE_DEVICES=1 --device cuda:0`
- 当前 step 8000, train_return 35.14, metrics.jsonl 11 行
- 单一 tfevents 文件（PID 126115），logdir 干净，无双写问题

**旧 PID 状态：**
- PID 125392 (exp_008e_v2): **已死亡**
- PID 126110 (exp_008e_v3 wrapper bash): 存活，是 126115 的父进程

**008e logdir 清理情况：**
- `exp_008e_v2_contaminated_20260514_1228` — 已归档，含 2 个 tfevents（双写证据），不影响当前实验
- `exp_008e_v2_dead_20260514_1227` — 已归档，空壳
- `exp_008e_v3_subsample_on_dt1_h15` — **活跃且干净**，单进程写入，无污染

**结论：** GPU 1 不空闲——exp_008e_v3 已在正常运行，logdir 干净，无需干预。两个归档目录可后续清除，不影响当前实验。

---
