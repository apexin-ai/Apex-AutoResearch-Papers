# infra check 4090x4 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-4090x4-status_20260513T151613_result.json`
- **Structured JSON:** [`e743b66a149c6912f6c8.json`](../../sessions/e7/e743b66a149c6912f6c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. Precompute shards — 全部 **completed**

3 个 precompute 进程（PID 46966/47044/47186）已全部退出（`ps` 找不到进程），日志均显示 `EXIT_CODE=0`。

| Shard | 样本数 | 耗时 | 状态 |
|-------|--------|------|------|
| shard0 | 4857/4857 | ~2118s (35min) | **completed** |
| shard1 | 4857/4857 | ~2049s (34min) | **completed** |
| shard2 | 4856/4856 | ~2027s (34min) | **completed** |

**输出文件**（`/root/autodl-tmp/crm_cache/`）：

- **object/**：merge 完成，生成最终文件：
  - `obs_features.pt` (54M), `k_samples.pt` (17M), `expert_actions.pt` (1.7M), `manifest.json`
  - 日志确认：`Saved 14570 samples + manifest to /root/autodl-tmp/crm_cache/object`

- **spatial/**：merge 也已完成：
  - `obs_features.pt` (45M), `k_samples.pt` (14M), `expert_actions.pt` (1.4M), `manifest.json`

> 注意：shard1 和 shard2 的日志显示 `Shard 0 not done, skipping merge`，但 shard0（最后完成的）触发了 merge，spatial 和 object 的最终文件都已生成。

### 2. Spatial eval — **running**

PID 43809 仍然存活，已运行 **3h43m**。

已完成 7/10 个 task 的评估，当前结果**全部 0% success rate**（vla_only baseline）：
```
pick_up_the_black_bowl_between_the_plate_and_the_ramekin...  0/3
pick_up_the_black_bowl_next_to_the_ramekin...                0/3
pick_up_the_black_bowl_from_table_center...                  0/3
pick_up_the_black_bowl_on_the_cookie_box...                  0/3
pick_up_the_black_bowl_in_the_top_drawer...                  0/3
pick_up_the_black_bowl_on_the_ramekin...                     0/3
pick_up_the_black_bowl_next_to_the_cookie_box...             0/3
```

结果文件 `/tmp/eval_spatial_results.json` 尚未生成（eval 未全部完成）。还剩 3 个 task，预计 ~1-1.5h 完成。

### 3. GPU 状态

| GPU | 显存使用 | 利用率 |
|-----|---------|--------|
| 0 | 1389/24564 MiB | 20% |
| 1 | 0/24564 MiB | 0% |
| 2 | 0/24564 MiB | 0% |
| 3 | 0/24564 MiB | 0% |

GPU 0 在跑 eval，GPU 1-3 空闲（precompute 已完成）。

---
