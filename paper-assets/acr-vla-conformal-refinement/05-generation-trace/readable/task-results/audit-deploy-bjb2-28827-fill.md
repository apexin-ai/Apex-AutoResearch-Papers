# audit deploy bjb2 28827 fill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit-deploy_bjb2-28827-fill_20260520T152900_result.json`
- **Structured JSON:** [`fd7c62d338d059363c16.json`](../../sessions/fd/fd7c62d338d059363c16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计总结

### GPU 状态 (bjb2-28827)
| GPU | PID | 状态 | 实验 |
|-----|-----|------|------|
| cuda:0 | 401372 | ✓ running | K=1 CRM seed42 (plan702) — task 4/10 |
| cuda:1 | 401666 | ✓ running | K=1 CRM seed43 (plan702) — task 4/10 |
| cuda:2 | 433142 | **刚部署** | eval-obs-only-spatial-norm02-seed42-r2 |
| cuda:3 | 365151 | ✓ running | OpenVLA precompute (PID 365151, 非 365142) |
| cuda:4 | 392238 | **占用中** | random_selection object seed44 — task 5/10, 还需 ~30min |
| cuda:5 | 402276 | ✓ running | K=1 CRM seed44 (plan702) — task 4/10 |

### 已完成
- `eval-perdof-object-norm02-seed49` — 注册表中 RUNNING 但进程已死，已标记为 killed

### 未部署
- **cuda:4 的 eval-k5-obs-only-object-seed42 无法部署** — 当前被 `random_selection object seed44` 占用。该实验约 30 分钟后完成，届时 cuda:4 空出可部署。

---
