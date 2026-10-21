# audit bjb2 28827 preparing fix

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_bjb2-28827-preparing-fix_20260523T121441_result.json`
- **Structured JSON:** [`c9a491c6ea2360688bc7.json`](../../sessions/c9/c9a491c6ea2360688bc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报：

| 实验 | GPU | PID | 状态 | 当前进度 |
|------|-----|-----|------|----------|
| eval-supp-long-reconvla-s42 | cuda:3 | 711479 | RUNNING ✓ | LIVING_ROOM_SCENE5 rollout 5/20 |
| eval-supp-long-adapt-tau025-s42 | cuda:4 | 711770 | RUNNING ✓ | LIVING_ROOM_SCENE5 rollout 10/20 |
| eval-supp-long-crm-norm005-s42 | cuda:5 | 712378 | RUNNING ✓ | LIVING_ROOM_SCENE5 rollout 5/20 |

- 3 个实验都在 Long benchmark 的最后一个任务（LIVING_ROOM_SCENE5），接近完成
- Registry 已从 PREPARING → QUEUED → RUNNING 更新完毕
- 每 20 分钟监控 cron 已注册（job `ed6f6ab6`），会自动检查完成状态并更新 registry

---
