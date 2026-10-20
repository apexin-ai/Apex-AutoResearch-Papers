# writing rebuttal framework

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_rebuttal-framework_20260521T151442_result.json`
- **Structured JSON:** [`27e7b38960338e681db4.json`](../../sessions/27/27e7b38960338e681db4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Rebuttal framework written to `artifacts/rebuttal_framework.md`.

**Coverage**: 8 个 R6 issues + 4 个 dream review 预判 concerns，共 12 条回应策略。

**关键回应**:
- **R6-N1 (single-seed)**: CWM 3-seed 数据 May 22 到齐；即使 single-seed，per-test LPM z=−23.7 (n=56,480) 已是 overwhelming evidence
- **R6-W2 (CWM regime)**: forced-parse 实验是杀手证据——rescue 90.6% unparseable 后 accuracy 仅 49.4%，远低于 majority baseline 72.96%，证明问题是 semantic 而非 format
- **R6-W4 (TRAJ confound)**: DeepSeek power=0.112 标为 exploratory；Qwen power=0.91 结论 stands；TRAJ 天然在 trajectory 粒度操作，400 examples 是 formulation 固有属性
- **NEW-1 (constrained decoding)**: 最大预判风险，已有 forced-parse 数据预备回应

**Blocking item**: CWM multi-seed (ETA May 22 15:30) → 之后可 close R6-N1 + R6-W5 + R6-M3。

---
