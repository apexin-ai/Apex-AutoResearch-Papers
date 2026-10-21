# fix eval vla only k1 bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval-vla-only-k1-bjb1_20260514T000130_result.json`
- **Structured JSON:** [`7fe0962e20707f43cbbe.json`](../../sessions/7f/7fe0962e20707f43cbbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**修复内容**: `evaluate.py` 第 364-365 行，在 `parse_args()` 后添加 `if args.mode == "vla_only": args.K = 1`，使 vla_only 模式从 K=10 降为 K=1。

**结果**:
- 旧进程 PID 117486 已 kill
- 新进程 **PID 123755**，日志确认 `K: 1` 已生效
- 日志路径: `/root/autodl-tmp/eval_results/eval-spatial-v7.log`
- 其他 3 个进程未受影响:
  - 117814 — acr_vla eval (cuda:1, K=10)
  - 118108 — reconvla eval (cuda:2, K=10)
  - 121984 — crm training (cuda:3)

---
