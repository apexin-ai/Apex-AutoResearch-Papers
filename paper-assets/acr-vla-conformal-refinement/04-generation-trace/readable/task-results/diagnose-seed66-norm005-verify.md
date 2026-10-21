# diagnose seed66 norm005 verify

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_seed66-norm005-verify_20260521T045625_result.json`
- **Structured JSON:** [`ceb4e97218c1bd9bcc1b.json`](../../sessions/ce/ceb4e97218c1bd9bcc1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 seed66 experiments已经在 registry 中被修正，无需进一步操作。

## 实际状态汇总

| 实验 | 状态 | SR | 备注 |
|------|------|-----|------|
| eval-obs-only-object-norm003-seed66 | **completed** (DONE/success) | **11.5%** (23/200) | 10 tasks × 20 rollouts 全部完成 |
| eval-obs-only-object-norm005-seed66 | **completed** (DONE/success) | **11.0%** (22/200) | 10 tasks × 20 rollouts 全部完成。之前误判 failed 已修正 |
| eval-obs-only-object-norm01-seed66 | **completed** (DONE/success) | **13.5%** (27/200) | 10 tasks × 20 rollouts 全部完成 |

3 个进程均已自然退出（PID 不存在），但 output JSON 完整生成在 `/root/logs/`。Registry 已被修正为 DONE/success 并补录了 metrics，无需额外更新。

---
