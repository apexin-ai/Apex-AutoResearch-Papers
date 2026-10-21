# diag bjb1 vla only k check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb1-vla-only-k-check_20260514T000418_result.json`
- **Structured JSON:** [`9a2ab6f96fab1ac9662a.json`](../../sessions/9a/9a2ab6f96fab1ac9662a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**bjb1 evaluate.py 当前已有 K=1 修复**（第 365 行：`args.K = 1`），但修复是在进程启动之后才加入的。

**eval-spatial-v6-full 确实受 K=10 bug 影响**：
- 日志明确显示启动参数 `'K': 10, 'mode': 'vla_only'` — 修复代码会在 print 之前把 K 改成 1，说明该进程启动时用的是**旧版代码**
- 日志停在 `10 tasks loaded`，之后无任何 rollout 输出 — 与 bjb2 的 K=10 卡死表现一致

**PID 117486 已不存在** — 进程已死（可能自行崩溃或被 kill）。

**结论**：eval-spatial-v6-full 的结果无效，需要用修复后的代码重新跑。当前 evaluate.py 已有修复，直接重启即可。

---
