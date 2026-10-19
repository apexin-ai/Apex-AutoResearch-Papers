# ssh sync adaptive k code

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_sync-adaptive-k-code_20260519T230000_result.json`
- **Structured JSON:** [`763cafac7efb12d02f51.json`](../../sessions/76/763cafac7efb12d02f51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

发现版本差异——**bjb2-40593 才是最新版本**，不是 bjb2-28827：

| 服务器 | 文件大小 | 行数 | adaptive_k 匹配 | 版本 |
|--------|---------|------|-----------------|------|
| bjb2-40593 | 23157 B | 593 | 19 | **最新** — `adaptive_k` 作为独立 mode，含 `select_action_adaptive_k()`, 默认 checkpoint/norm, trigger_rate 统计 |
| bjb2-28827 | 19685 B | 511 | 4 | 旧版 — `adaptive_k` 仅作 flag |
| bjb1-32546 | 19685 B | 511 | 4 | 旧版（同 bjb2-28827） |
| bjb1-18228 | 19685 B | 511 | 4 | 旧版（同 bjb2-28827） |

bjb2-40593 的版本包含 bjb2-28827 所没有的：
- `adaptive_k` 作为 `--mode` 选项（不仅是 flag）
- 独立的 `select_action_adaptive_k()` 函数
- 默认 CRM checkpoint 和 `max_correction_norm=0.2`
- `adaptive_trigger_rate` 统计

**应该从 bjb2-40593 同步到其他 3 台服务器。** 需要确认是否按此执行，还是你确实想用 bjb2-28827 的版本？

---
