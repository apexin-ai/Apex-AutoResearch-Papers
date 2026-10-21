# collect smolvla long seed1 result

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_smolvla-long-seed1-result_20260522T154005_result.json`
- **Structured JSON:** [`5edbd902776354ca11d0.json`](../../sessions/5e/5edbd902776354ca11d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 所有 6 个 eval 进程均被中途 kill，未生成 JSON 结果文件

**vla-only eval（10 rollouts/task）— 仅完成 2/10 tasks：**

| Task | seed0 | seed1 | seed2 |
|------|-------|-------|-------|
| put_alphabet_soup_and_tomato_sauce_in_basket | 0% (0/10) | 10% (1/10) | 10% (1/10) |
| put_cream_cheese_box_and_butter_in_basket | 80% (8/10) | 90% (9/10) | 70% (7/10) |
| turn_on_stove_and_put_moka_pot (task 2) | 开始执行后被 kill | 开始执行后被 kill | 开始执行后被 kill |

日志最后修改时间：~22:59（运行约 54 min）

**lerobot eval（20 episodes/task）— 完成 6/10 tasks：**

| Task # | seed0 | seed1 | seed2 |
|--------|-------|-------|-------|
| 0 | 25% | 10% | 10% |
| 1 | 40% | 45% | 55% |
| 2 | 85% | 70% | 80% |
| 3 | 70% | 85% | 85% |
| 4 | 45% | 35% | 35% |
| 5 | 75% | 70% | 60% |
| 6-9 | killed mid-task | killed mid-task | killed mid-task |

日志最后修改时间：~23:45（运行约 40 min）

**kill 原因**：无法读取 dmesg（容器限制）。6 个 eval 进程并行跑在 6×4090 上（3个 vla-only + 3个 lerobot），可能是 CPU/RAM OOM 或被平台调度终止。当前 GPU 仍有 3 块占用 ~10GB（可能是残留进程）。

**结论**：seed1（及 seed0/seed2）均为 **failed — 被 kill，未完成**。需要重跑。

---
