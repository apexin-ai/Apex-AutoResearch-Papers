# analysis 4b eval hang root cause

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_4b-eval-hang-root-cause_20260515T020036_result.json`
- **Structured JSON:** [`04192595b2fb0d3cb4fc.json`](../../sessions/04/04192595b2fb0d3cb4fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/4b_eval_hang_analysis.md`。

**核心结论**：根因是 **RTX 5090 的间歇性 CUDA hang**（driver 570.211.01 是早期 Blackwell 驱动）。

关键证据：
- v1 卡在 sample 6544，v2 卡在 sample 2000 — 位置不同，非特定 sample 问题
- 所有已处理 batch 耗时正常 (7-8s)，无渐进退化
- v2 的双层 watchdog（signal.alarm + threading+os._exit）均未触发 — 说明阻塞在 Python 层以下

watchdog 失效原因：SIGALRM 无法打断 CUDA C 调用；`os._exit()` 在 CUDA driver 异常时可能被 driver cleanup 死锁。

**最高优先级修复**：
1. watchdog 改用 `os.kill(os.getpid(), SIGKILL)` 替代 `os._exit(1)` — SIGKILL 不可屏蔽
2. 加断点续跑 — 被 kill 后从上次完成的 sample 继续（v2 已有增量写入，只差 resume 逻辑）
3. `max_new_tokens` 从 512 降回 8

---
