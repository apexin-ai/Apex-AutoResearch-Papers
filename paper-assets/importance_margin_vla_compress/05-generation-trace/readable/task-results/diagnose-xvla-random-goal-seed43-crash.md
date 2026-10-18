# diagnose xvla random goal seed43 crash

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose-xvla-random-goal-seed43-crash_20260523T222112_result.json`
- **Structured JSON:** [`d902f4ba6f0521a6840e.json`](../../sessions/d9/d902f4ba6f0521a6840e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**Root cause: 外部信号杀死（SIGHUP），不是代码 bug。**

三次运行都在裸 SSH 会话中启动，SSH 断开即死。关键证据：

1. **无 traceback** — 日志干净截断，无任何错误信息，典型的外部 kill 表现
2. **崩溃位置不一致** — v1 跑了 269 episodes（到 Task 5），v2 跑了 33 episodes，v3 跑了 54 episodes。不是同一位置 crash，排除代码 bug
3. **死亡时间与新实验启动强相关** — v2 死于 05:47，05:48 新 tmux 批次启动；v3 死于 06:22，06:24 spatial 实验启动
4. **同服务器 tmux 实验运行正常** — 当前 4 个 tmux 实验稳定运行 38+ 分钟
5. **资源充足** — GPU 98GB 仅用 5GB，磁盘 29%

**修复**：用 tmux 启动即可。报告已写入 `artifacts/diag_xvla_random_k05_goal_seed43_crash.md`。

---
