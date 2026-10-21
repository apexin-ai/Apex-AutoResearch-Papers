# check bjb1 18228 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1-18228-status_20260525T174341_result.json`
- **Structured JSON:** [`2d13a2b8f34de4b3736b.json`](../../sessions/2d/2d13a2b8f34de4b3736b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-18228 进程状态

### 原始查询的两个实验

- **precompute-pi05-long-2048-r2**: **RUNNING** — PID 114507, 已运行 2天21小时, 进度 127300/136090 (93.5%), 速度 1.96s/sample, 预计剩余 ~4.8 小时完成。GPU 3 占用 9883 MiB。
- **eval-crm-long-s42-d149**: **RUNNING** — PID 601277, GPU 1 占用 14100 MiB。正在跑 long benchmark task 1/10 (`LIVING_ROOM_SCENE2_put_both_alphabet_soup_and_tomato_sauce_in_basket`), 当前 task 成功率 70% (14/20)，刚完成第 1 个 task。

### GPU 使用

| GPU | 显存占用 | 利用率 | 运行内容 |
|-----|---------|--------|---------|
| 0 | 13195/24564 MiB | 26% | eval_pi05_**object**_crm_seed42 |
| 1 | 14100/24564 MiB | 27% | eval_pi05_**long**_crm_seed42 |
| 2 | 4/24564 MiB | 0% | eval_pi05_**long**_crm_seed43 (刚启动) |
| 3 | 9883/24564 MiB | 24% | precompute PID 114507 |

### 不在 registry 中的进程

1. **eval_pi05_object_crm_seed42** (GPU 0, PID 601275) — RUNNING, object benchmark, 已完成 3/10 tasks:
   - alphabet_soup: 100% (20/20)
   - cream_cheese: 70% (14/20)
   - salad_dressing: 进行中

2. **eval_pi05_long_crm_seed43** (GPU 2, PID 625278) — 刚启动 (~2分钟前), long benchmark seed 43, 还在加载模型

3. **eval-vla-only-spatial-s47-d149** (tmux session) — **DONE**, spatial benchmark vla_only baseline, **overall success rate: 78.5% (157/200)**, 结果已保存至 `logs/eval_spatial_vla_only_seed47_n20.json`

### 缓存文件

precompute 缓存目录 `/root/autodl-tmp/crm_cache_pi05_2048/long/` 已累计 ~1.2GB，含 254 个 partial 文件 (每个 4.6MB, 覆盖 0-127000 样本)。

---
