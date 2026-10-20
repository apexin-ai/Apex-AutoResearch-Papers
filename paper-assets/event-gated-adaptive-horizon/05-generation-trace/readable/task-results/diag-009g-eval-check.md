# diag 009g eval check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_009g_eval_check_20260515T190127_result.json`
- **Structured JSON:** [`779ab4c2521301489b82.json`](../../sessions/77/779ab4c2521301489b82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**009g eval 未成功 —— 进程被 SIGTERM 杀掉了。**

| 项目 | 状态 |
|------|------|
| 009g 当前 step | 停在 5000 |
| eval 是否完成 | **否** — 日志仅有 `Start evaluation.`，无 eval return 输出，随后 `Terminated` / `EXIT_CODE=143`（SIGTERM） |
| eval return 值 | 无（未产出） |
| PID 517810 (test_cuda1_eval) | 已退出 |
| GPU 1 当前进程 | PID 519956 — `test_cuda1_eval2`，运行在 **cuda:0**（不是 cuda:1），已跑约 2 分钟，占 794 MiB |

009g 在进入 eval 后被外部 kill（EXIT_CODE=143 = SIGTERM）。这不是 eval 挂死，而是进程被主动终止。可能是之前的 test_cuda1_eval 测试脚本清理时把它杀了，或者手动终止过。

GPU 1 上目前没有跑实验的进程（519956 的 test_cuda1_eval2 绑定的是 cuda:0）。

---
