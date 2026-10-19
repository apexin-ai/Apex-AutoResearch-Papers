# ssh seed45 final harvest

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_seed45-final-harvest_20260516T201251_result.json`
- **Structured JSON:** [`817ba6c233cc6c139251.json`](../../sessions/81/817ba6c233cc6c139251.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 seed45 实验都**尚未完成**，仍在运行中。

**当前进度:**

### obs_only seed45 (bjb1-32546, GPU 3)
9/10 任务已完成，最后一个任务 (orange_juice) 正在跑：

| Task | Successes/10 |
|------|-------------|
| alphabet_soup | 0 |
| cream_cheese | 0 |
| salad_dressing | 1 |
| bbq_sauce | 4 |
| ketchup | 1 |
| tomato_sauce | 1 |
| butter | 1 |
| milk | 2 |
| chocolate_pudding | 4 |
| orange_juice | **running...** |

已完成部分: **14/90**

### argmin seed45 (bjb2-28827, GPU 5)
7/10 任务已完成，还有 3 个任务待跑 (milk, chocolate_pudding, orange_juice)：

| Task | Successes/10 |
|------|-------------|
| alphabet_soup | 0 |
| cream_cheese | 0 |
| salad_dressing | 1 |
| bbq_sauce | 4 |
| ketchup | 0 |
| tomato_sauce | 0 |
| butter | 1 |
| milk~orange_juice | **pending** |

已完成部分: **6/70**

### 预估

obs_only seed45 还差 1 个任务的 10 rollouts，预计 1-2 小时内完成。argmin seed45 还差 3 个任务，预计 3-5 小时。

JSON 文件要等实验全部跑完才会写出。目前无法计算 4-seed Fisher test。需要等两个实验都结束后再读取。

---
