# check gamma sweep full eval integrity

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gamma_sweep_full_eval_integrity_20260512T171314_result.json`
- **Structured JSON:** [`db8c80925c3d9e3bd2f5.json`](../../sessions/db/db8c80925c3d9e3bd2f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 39560 已退出（崩溃）。全部信息到齐，结论如下：

---

## 结论

### OOM 没有影响 gamma_sweep 的 [full] eval

**OOM Traceback 来自 PID 39560 (run_inverted_ema.py)，不是 PID 40063 (gamma_sweep)**。

证据：
- OOM 错误信息：`Process 39560 has 28.43 GiB ... this process has 31.88 GiB ... Process 40063 has 34.52 GiB` — "this process" 指抛出错误的进程（39560）
- PID 39560 已经退出（已崩溃），PID 40063 仍在运行
- Traceback 的 stderr 输出被混入了 gamma_sweep.log（两个进程共享终端输出）

### 源码验证：无 try/except

`run_strategy()` 的 eval 循环中**没有任何异常处理**。如果 OOM 打到 gamma_sweep，进程会直接崩溃退出，不存在"静默跳过 token"的可能。

### [full] baseline 数据可信

- [full]、[random] (PPL=7.6353)、[recency] (PPL=7.1758) 三个 baseline 均已完成
- 每个 eval 都处理了 6554 tokens（预期值），进度条正常走到 100%
- **不需要重跑**

### 当前进度

- 三个 baseline 完成 ✓
- 正在执行 gamma sweep 第 1/8 个：`ema_0.1` eval 47% (3052/6554)
- 整体进度 ~32%（3.5/11 strategies）
- PID 40063 运行 40 分钟，预计总耗时 ~2 小时

### 日志中两次 "Running baseline: full" 的原因

日志包含两次运行的拼接输出：第一次运行（lines 1-34）被手动终止，第二次运行（lines 35+, PID 40063）是当前正在执行的进程。

---
