# diagnose eval reconvla spatial v1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-reconvla-spatial-v1_20260513T202755_result.json`
- **Structured JSON:** [`bc7ef3010e3fca534b21.json`](../../sessions/bc/bc7ef3010e3fca534b21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：实验未失败，EXIT_CODE=129 是误报。**

- PID 87787 当前正常运行（CPU 273%，GPU 2 占用 1414MiB），tmux session 存活
- exit code 文件不存在，进程从未退出
- 日志停在 "10 tasks loaded" 是正常的——rollout 进度每 5 轮打印一次，第一批还没跑完
- 代码路径正确：reconvla 模式不需要 `--checkpoint`，所有依赖已加载成功

报告已写入 `artifacts/eval-reconvla-spatial-v1-diag.md`。

---
