# ssh check l2norm k07 s46 and s47

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_l2norm_k07_s46_and_s47_20260528T120704_result.json`
- **Structured JSON:** [`c3a7749ba4a9643b1975.json`](../../sessions/c3/c3a7749ba4a9643b1975.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 任务 1：westd-41074 — L2norm k=0.7 seed46 ✅ 已完成

PID 923767 已退出。实验**成功完成**，结果：

**Overall SR = 62.2%**

Per-task 结果：
| Task | SR |
|------|------|
| T0 | 74% |
| T1 | 92% |
| T2 | 66% |
| T3 | 40% |
| T4 | 58% |
| T5 | 66% |
| T6 | 58% |
| T7 | 62% |
| T8 | 10% |
| T9 | 96% |

结果已保存至 `eval_results/pi05_l2norm_k0.70_libero_10_seed46.json`。总耗时 ~155.7 分钟。

---

### 任务 2：westd-38929 — 3 个 seed47 实验 🟢 运行中

3 个 PID 全部存活（已运行 ~57 分钟），当前进度：

| 实验 | 当前进度 | 最新 Task SR |
|------|---------|-------------|
| random k=0.85 s47 | Task 2 完成 (ep 50) | T0=42%, T1=50%, T2=42%（累计 44.7%）|
| l2norm k=0.5 s47 | Task 3 进行中 (ep 30) | T0=68%, T1=68%, T2=86%（累计 74.0%）|
| attn k=0.5 s47 | Task 3 进行中 (ep 30) | T0=76%, T1=44%, T2=64%（累计 61.3%）|

预计每个还需 ~100 分钟完成（总 ~2.5h）。

---

### 任务 3：Stale RUNNING PIDs ✅ 全部已死

| 服务器 | PID | 实验 | 状态 |
|--------|--------|------|------|
| westd-38929 | 457257 | attn k=0.95 s46 | DEAD |
| westd-41074 | 899098 | random k=0.5 s46 | DEAD |
| westd-41074 | 898746 | random k=0.95 s46 | DEAD |
| westd-27271 | 616102 | l2norm k=0.95 s46 | DEAD |

4 个 stale PID 均已退出，registry 可标记为完成。

---
