# monitor scan all running evals

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_scan-all-running-evals_20260524T103511_result.json`
- **Structured JSON:** [`e83bedc08fc2639ce558.json`](../../sessions/e8/e83bedc08fc2639ce558.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

注意：当前运行的 session 与预期不同——全部是 **s47 evals**，原来的 s45/s46 spatial evals 已不在。以下是精确状态：

## bjb2-28827
GPU 0-5 全部活跃 (4.2-5.6 GB)

| Session | Status | Progress | Notes |
|---------|--------|----------|-------|
| goal-adapt-s47 | RUNNING | task 4/10, rollout 10/20 | 已完成: middle_drawer 85%, bowl_stove 100%, wine_bottle 85% |
| goal-crm-s47 | RUNNING | task 4/10, rollout 10/20 | 已完成: middle_drawer 80%, bowl_stove 100%, wine_bottle 80% |
| goal-k2mean-s47 | RUNNING | task 4/10, rollout 10/20 | 已完成: middle_drawer 65%, bowl_stove 100%, wine_bottle 90% |
| goal-reconvla-s47 | RUNNING | task 4/10, rollout 15/20 | 已完成: middle_drawer 85%, bowl_stove 100%, wine_bottle 95% |
| long-k2mean-s47 | RUNNING | task 2/10, rollout 20/20 | task 1: 15.0% |
| obj-reconvla-s47 | RUNNING | task 4/10, rollout 5/20 | 已完成: cream_cheese 95%, salad_dressing 70% |

## cqa1-32758
GPU 4-5 活跃 (3.3 GB), GPU 0-3 空闲。**原 Spatial s45/s46 已消失，改为 Long s47。**

| Session | Status | Progress | Notes |
|---------|--------|----------|-------|
| long-adapt-s47 | RUNNING | task 7/10, rollout 10/20 | ~65% done, SCENE5 35%, STUDY_SCENE1 90% |
| long-vla-s47 | RUNNING | task 7/10, rollout 15/20 | ~67% done, SCENE5 45%, STUDY_SCENE1 90% |

## bjb1-32546
GPU 0-5 全部活跃 (1.8-2.4 GB)。**原 Object reconvla s45 已消失，改为 Long+Object s47 全套。**

| Session | Status | Progress | Notes |
|---------|--------|----------|-------|
| long-crm-s47 | RUNNING | task 9/10, rollout 20/20 | ~90% ⬆ almost done, SCENE6 15%, SCENE1_basket 60% |
| long-reconvla-s47 | RUNNING | task 9/10, rollout 20/20 | ~90% ⬆ almost done, SCENE6 40%, SCENE1_basket 50% |
| obj-adapt-s47 | RUNNING | task 8/10, rollout 15/20 | ~77%, tomato_sauce 65%, butter 65% |
| obj-crm-s47 | RUNNING | task 9/10, rollout 15/20 | ~87%, tomato_sauce 80%, butter 85%, milk 75% |
| obj-k2mean-s47 | RUNNING | task 9/10, rollout 15/20 | ~87%, tomato_sauce 70%, butter 55%, milk 80% |
| obj-vla-s47 | RUNNING | task 9/10, rollout 20/20 | ~90%, tomato_sauce 75%, butter 70%, milk 70% |

## bjb1-18228
GPU 1-3 活跃, GPU 0 空闲

| Session | Status | Progress | Notes |
|---------|--------|----------|-------|
| goal-vla-s47 | RUNNING | task 7/10, rollout 20/20 | ~70%, wine_bottle 90%, top_drawer 55%, bowl_cabinet 85% |
| long-vla-s47 | RUNNING | task 3/10, rollout 5/20 | ~22%, task1 15%, task2 75% |
| precompute-pi05-long-2048-r2 | RUNNING | 71K samples (s0) | PID 114507, GPU 3 (9.9GB), 运行 >24h。goal/object/spatial 的 s0 已完成，long 的 s0 仍在进行 |

**总结**：
- **0 个已完成** — 全部 16 个 eval session 仍在运行
- **接近完成**（>85%）：bjb1-32546 上的 long-crm, long-reconvla, obj-crm, obj-k2mean, obj-vla — 预计 1-2 小时内完成
- **中段**（60-77%）：cqa1 的 2 个 long, bjb1-32546 的 obj-adapt, bjb1-18228 的 goal-vla
- **早期**（<40%）：bjb2-28827 的 6 个 session, bjb1-18228 的 long-vla — 这些 ~6-7h 前才启动
- precompute 仍在 GPU 3 运行，long benchmark 的 s0 约 90% 完成

---
