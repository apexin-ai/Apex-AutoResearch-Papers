# ops full status check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_status_check_20260514T061009_result.json`
- **Structured JSON:** [`52a501d7a7d2231163b9.json`](../../sessions/52/52a501d7a7d2231163b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 008a (PID 106947) — ALIVE，已超目标
- **进程**: alive，运行 4h32m，CPU 923%
- **当前 step**: ~112K（目标 105K 已完成，仍在继续跑）
- **GPU**: GPU0，4158 MiB

**75K-105K eval trajectory:**

| Step | eval_return | value_mean | v/e ratio |
|------|------------|------------|-----------|
| 75000 | 469.93 | 251.78 | 0.536 (53.6%) |
| 85000 | 583.73 | 277.36 | 0.475 (47.5%) |
| 95000 | 572.24 | 284.28 | 0.497 (49.7%) |
| 105000 | **777.66** | 300.27 | 0.386 (38.6%) |

eval_return 在 105K 达到峰值 777.66，但 value_mean 始终远低于 eval_return（v/e ratio 38-54%），value function 严重低估实际回报。gate 全部固定在 dt=2（符合 fixed_dt2 配置）。

---

### 008e_v3 (PID 126115) — ALIVE
- **进程**: alive，运行 1h41m，CPU 885%
- **当前 step**: ~44K
- **GPU**: GPU0，4158 MiB（与 008a 共享 GPU0）
- **最新 train_return**: 303-473 @ 44K

---

### 008f (PID 127766) — ALIVE
- **进程**: alive，运行 1h18m，CPU 837%
- **当前 step**: ~32K
- **GPU**: GPU1，2742 MiB
- **最新 train_return**: 169-215 @ 32K

---

### GPU 总览
| GPU | 利用率 | 显存使用 | 进程 |
|-----|--------|---------|------|
| GPU0 | 62% | 6914/97887 MiB | 008a (4158M) + 008e_v3 (4158M) |
| GPU1 | 1% | 4167/97887 MiB | 008f (2742M) |

注意：008a 和 008e_v3 都在 GPU0 上（都配了 `--device cuda:0`），008f 单独在 GPU1。GPU1 利用率极低（1%），008f 可能处于 eval 间歇。

---
