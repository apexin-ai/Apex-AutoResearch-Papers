# fix registry s45 s46 cleanup

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_registry-s45-s46-cleanup_20260524T110058_result.json`
- **Structured JSON:** [`2ffe3871281b0e0ea716.json`](../../sessions/2f/2ffe3871281b0e0ea716.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 7 个实验状态确认完毕：

| Exp ID | 当前状态 | 结论 | 操作 |
|---|---|---|---|
| eval-supp-spatial-reconvla-s46 | DONE | success | 已是 DONE，无需操作 |
| eval-supp-spatial-k2mean-s46 | DONE | success | 已是 DONE，无需操作 |
| eval-supp-spatial-adapt-tau025-s45-r3 | DONE | success | 已是 DONE，无需操作 |
| eval-supp-reconvla-obj-s45 | DONE | success | 已是 DONE，无需操作 |
| eval-smolvla-lerobot-goal-seed43-v3 | DONE | success | 已是 DONE，无需操作 |
| eval-smolvla-lerobot-spatial-seed43-v3 | DONE | success | 已是 DONE，无需操作 |
| **eval-supp-spatial-crm-norm005-s47** | **DONE (新)** | **success** | tmux 已消失，JSON 完整，**success_rate=0.805 (161/200)**。已更新 metrics + log_path + checkpoint_path + conclusion + status |

实际只有 1 个 RUNNING→DONE 的 registry 更新（eval-supp-spatial-crm-norm005-s47）。其余 6 个 registry 早已标记 DONE/success，无需处理。

---
