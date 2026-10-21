# diagnose eval adaptive k spatial p50 seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-adaptive-k-spatial-p50-seed44_20260520T064034_result.json`
- **Structured JSON:** [`28d43984c34cc4613601.json`](../../sessions/28/28d43984c34cc4613601.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**失败原因**：启动命令使用了错误路径 `/root/acr-vla-conformal-refinement/evaluate.py`，实际脚本在 `src/evaluate.py`。进程瞬间退出（EXIT_CODE=2），没有跑任何 episode，无部分结果。

**修复**：将启动命令中的脚本路径改为 `src/evaluate.py`，直接重跑即可。服务器 GPU 状态正常，无其他问题。

报告已写入 `artifacts/diagnose-eval-adaptive-k-spatial-p50-seed44.md`。

---
