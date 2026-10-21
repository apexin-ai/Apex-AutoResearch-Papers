# analyze eval mag perdof norm03

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-mag-perdof-norm03_20260515T171431_result.json`
- **Structured JSON:** [`bd27324ff401dede003d.json`](../../sessions/bd/bd27324ff401dede003d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/negative。

**总结：**

- **perdof CRM v3-norm, spatial, norm=0.3 → 10-task SR = 26.0% (26/100)**
- 7-task 快照 32.9% → 最终 3 个 task (T7=10%, T8=20%, T9=0%) 拉低了均值
- **低于 argmin baseline 34%** → conclusion = negative，perdof 在高 norm (0.3) 下性能崩塌
- ROADMAP 中 26.0% 数字确认准确，来源是此次实验的完整运行结果
- 日志位于 `~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm03.log`（非 `logs/` 目录）
- 进程 EXIT_CODE=0，于 2026-05-15T16:49:44Z 正常退出

---
