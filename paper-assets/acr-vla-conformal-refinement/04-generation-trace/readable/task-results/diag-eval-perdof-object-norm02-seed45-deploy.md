# diag eval perdof object norm02 seed45 deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval-perdof-object-norm02-seed45-deploy_20260517T134920_result.json`
- **Structured JSON:** [`be52e57372d5a0de1c88.json`](../../sessions/be/be52e57372d5a0de1c88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**: MuJoCo EGL 渲染初始化时 native segfault。进程在 `[eval] 10 tasks loaded.` 之后、第一个 `env.reset()` 时静默崩溃，无任何 Python 错误输出。SIGSEGV handler 也未被触发，说明是 native 层面的致命崩溃。

**排除项**: 非 OOM（454GB 空闲 RAM，GPU 仅用 5.6/24GB）、非代码错误（无 traceback）。

**触发因素**: 4 张 GPU 同时各跑一个 eval 进程，并发 EGL context 初始化可能存在 driver 竞争。同服务器上多个实验表现相同失败模式。

**当前状态**: PID 634438 已重启同一实验，当前 Running 状态。若再次失败，建议降低并发数（不同时跑 4 个 EGL 进程）。

---
