# ops exp025b 60s verify

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp025b_60s_verify_20260515T074158_result.json`
- **Structured JSON:** [`610b537f0794c01c56bd.json`](../../sessions/61/610b537f0794c01c56bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp025b 验证结果

| 项目 | 状态 |
|------|------|
| 1. 进程存活 | **YES** — PID 615550 存活，运行 36s |
| 2. GPU 在用 | **NO** — GPU 0: 3 MiB, GPU 1: 3 MiB（模型未加载） |
| 3. 日志有 error | **YES — 严重错误，实验大概率已失败** |

### 错误详情

Ray worker 大面积崩溃，核心错误是 **线程资源耗尽**：

- `Resource temporarily unavailable [system:11]` — 重复 36x+
- `Fatal Python error: Aborted` — 重复 43x+
- `jemalloc: arena 0 background thread creation failed (11)` — 重复 9x
- 多个 `AlfworldWorker` 进程（619960, 642313, 642695, 642974, 642896）调用 `__cxxabiv1::__terminate()` 崩溃

**根因**：系统无法创建足够线程（EAGAIN），导致 Ray worker 初始化时 abort。可能原因：
1. 之前实验的 Ray 进程残留，占用线程/进程配额
2. `ulimit -u` (nproc) 上限不足
3. `env.rollout.n=8` 个 AlfworldWorker + Ray 内部线程总数超过系统限制

GPU 显存仅 3 MiB 说明模型从未加载，训练还没开始 worker 就已经崩了。主进程虽然还活着，但已无法恢复。建议 kill 后排查线程资源再重启。

---
