# diagnose norm003 seed63 failure

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_norm003-seed63-failure_20260521T003025_result.json`
- **Structured JSON:** [`3bb2390c7a3c3f25ec71.json`](../../sessions/3b/3bb2390c7a3c3f25ec71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：所有 5 个实验（包括原以为还在运行的 seed49-r2）都在启动瞬间失败，原因是 nohup 启动命令用了裸 `python`，而服务器 PATH 中没有 `python`（Python 在 `/root/miniconda3/bin/python`，不在默认 PATH 里）。`/usr/local/bin/python` 的符号链接是今天 08:30 才补上的，实验启动时还不存在。

**结论**：
- 不是 OOM、GPU 错误或代码 bug，实验从未运行过
- 所有 5 个都可以直接重跑，无需调参
- 重跑时需在启动命令中激活 conda 环境或用完整路径 `/root/miniconda3/bin/python`

报告已写入 `artifacts/diagnose_bjb1_32546_batch_failure.md`。

---
