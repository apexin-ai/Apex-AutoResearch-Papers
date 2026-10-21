# monitor director status check 3items

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_director-status-check-3items_20260523T085913_result.json`
- **Structured JSON:** [`a9038dcea2172b85aed3.json`](../../sessions/a9/a9038dcea2172b85aed3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 1. Object Adaptive tau=0.25 s42 (bjb2-28827)
- **进程 620549**: 存活 (Rl)，已运行 1h43m
- **进度**: Task 7/10，当前 `pick_up_the_butter` rollout 5/20
- 已完成 6 个 task，速率 ~17 min/task
- **预计剩余 ~55 min**

## 2. CRM 4-suite 训练 (bjb1-32546)
- **进程 668382**: 存活 (Rl)，已运行 4h48m
- **进度**: **Epoch 50/50 (最后一轮)**，batch 5400/6316 (85.5%)
- Loss 稳定在 0.007~0.012
- 最新 checkpoint: epoch49 (16:40 保存)，每 epoch ~25 min
- **预计 ~4 min 内完成！**

## 3. 全部实验进度

### bjb2-28827 — 运行中

| 实验 | 进度 | 预估剩余 |
|------|------|----------|
| eval-supp-obj-adapt-tau025-s42 | Task 7/10, butter 5/20 | ~55 min |
| eval-supp-k2mean-object-s42 | Task 7/10, butter 5/20 | ~55 min |
| eval-supp-k2mean-spatial-s42 | Task 8/10, black_bowl_on_stove 10/20 | ~30 min |
| eval-supp-goal-reconvla-s42 | Task 8/10, turn_on_the_stove 5/20 | ~35 min |
| eval-object-vla-only-wrapper-s42-r2 | 运行 4h48m | 不确定 |
| eval-goal-vla-only-wrapper-s42 | 运行 1h43m | 不确定 |
| eval-supp-obj-reconvla-s43 | Task 0/10, 加载模型中 | ~1h40m |

### bjb2-28827 — 已完成

| 实验 | 结果 |
|------|------|
| eval-supp-goal-adapt-tau025-s42 | 84.0% (168/200) |
| eval-supp-goal-crm005-s42 | 85.5% (171/200) |
| eval-supp-obj-adapt-s42-r2 | 77.5% (155/200) |
| eval-supp-obj-reconvla-s42 | 79.0% (158/200) |

### bjb1-32546 — 运行中

| 实验 | 进度 | 预估剩余 |
|------|------|----------|
| **train-crm-unified-4suite-r6** | **Epoch 50/50, batch 5400/6316** | **~4 min** |
| eval-supp-adapt-tau025-object-s43 | Task 2/10, cream_cheese 5/20 | ~1h20m |
| eval-supp-crm-norm005-object-s43 | Task 2/10 | ~1h20m |
| eval-supp-crm-norm005-goal-s43 | Task 2/10, put_bowl_on_stove 10/20 | ~1h20m |
| eval-supp-adapt-tau025-goal-s43 | Task 2/10, put_bowl_on_stove 10/20 | ~1h20m |

### bjb1-32546 — 已完成

| 实验 | 结果 |
|------|------|
| eval-supp-crm-norm02-spatial-s42-r2 | 79.0% (158/200) |

### 即将完成排序
1. **train-crm-unified-4suite-r6** — ~4 min（即将完成）
2. **eval-supp-k2mean-spatial-s42** — ~30 min
3. **eval-supp-goal-reconvla-s42** — ~35 min
4. **eval-supp-obj-adapt-tau025-s42** / **eval-supp-k2mean-object-s42** — ~55 min

---
