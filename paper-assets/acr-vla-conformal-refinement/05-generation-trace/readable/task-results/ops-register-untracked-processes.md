# ops register untracked processes

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_register-untracked-processes_20260524T061547_result.json`
- **Structured JSON:** [`889337a5f925e884fdc3.json`](../../sessions/88/889337a5f925e884fdc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 7 个实验已确认在 registry 中有条目，hypothesis 已补充/更新。汇总：

### bjb1-18228 — precompute (3个)

| exp_id | 状态 | hypothesis |
|--------|------|------------|
| `precompute-pi05-object-2048-r2` | **RUNNING** | ✅ 已更新 |
| `precompute-pi05-goal-2048-r2` | **DONE** (已完成) | ✅ 已更新 |
| `precompute-pi05-long-2048-r2` | **RUNNING** | ✅ 已更新 |

### bjb1-32546 — eval Long s46 (4个)

| exp_id | GPU | PID | 状态 | hypothesis |
|--------|-----|-----|------|------------|
| `eval-supp-long-adapt-tau025-s46` | 0 | 261974 | **RUNNING** | ✅ 已更新 |
| `eval-supp-long-crm-norm005-s46` | 1 | 262247 | **RUNNING** | ✅ 已更新 |
| `eval-supp-long-reconvla-s46` | 2 | 262529 | **RUNNING** | ✅ 已更新 |
| `eval-supp-long-k2mean-s46` | 3 | 263191 | **RUNNING** | ✅ 已更新 |

注意：这 7 个实验实际已在 registry 中有条目（通过 `submit_training_job` 自动创建），此次操作补充了 hypothesis 字段。另外任务中提到的 `eval-supp-long-crm-obs-only-s46` 实际 exp_id 是 `eval-supp-long-crm-norm005-s46`（mode=crm_obs_only, norm=0.05）。

---
