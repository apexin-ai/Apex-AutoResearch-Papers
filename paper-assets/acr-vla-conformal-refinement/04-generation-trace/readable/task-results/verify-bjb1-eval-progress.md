# verify bjb1 eval progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_bjb1-eval-progress_20260514T181408_result.json`
- **Structured JSON:** [`fad93d38ffc4f408f883.json`](../../sessions/fa/fad93d38ffc4f408f883.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 4 个 Eval 进度汇报

所有 4 个进程**均存活**。

| Eval | PID | 运行时间 | 已完成 tasks | 当前进度 | 当前 success rate | 预估剩余 |
|------|-----|---------|-------------|---------|-----------------|---------|
| **eval-acr-spatial-v3** | 197057 | 5h57m | **4/10** | 刚完成 task 4 | 1/40 = **2.5%** | ~9h |
| **eval-acr-object-v3** | 197803 | 5h57m | **4/10** | 刚完成 task 4 | 0/40 = **0%** | ~9h |
| **eval-argmin-only-spatial** | 231421 | 26m | **0/10** | task 1 进行中（未到 5-rollout 检查点） | — | ~15h |
| **eval-tiny-correction-spatial** | 232815 | 25m | **0/10** | task 1: rollout 5/10, **4/5 success** | 4/5 = **80%** | ~15h |

### 关键发现

- **eval-tiny-correction-spatial (max_norm=0.05)** 表现惊人——task 1 前 5 个 rollout 4/5 成功，远好于同 task 的 spatial-v3 (1/10)。
- **eval-acr-spatial-v3 / object-v3** 跑了近 6 小时，成功率极低（spatial 2.5%, object 0%），CRM v2 未归一化版本效果很差。
- **eval-argmin-only-spatial** 刚启动 26 分钟，按 spatial-v3 的速度（~90 min/task），首个 5-rollout 检查点约在 ~45 分钟时出现，再等 20 分钟应该能看到第一批结果。

---
