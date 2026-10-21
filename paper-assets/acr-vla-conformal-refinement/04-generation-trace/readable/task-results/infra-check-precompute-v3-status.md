# infra check precompute v3 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-precompute-v3-status_20260513T182942_result.json`
- **Structured JSON:** [`4336d880eee9752b74ac.json`](../../sessions/43/4336d880eee9752b74ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 进程状态：全部存活

| 进程 | PID | GPU | 状态 | 运行时间 |
|------|-----|-----|------|----------|
| eval-spatial-v3-full | 62654 (子进程 62664) | cuda:0 | **存活** | 51min |
| precompute-v3-shard0 | 62930 (子进程 62935) | cuda:1 | **存活** | 51min |
| precompute-v3-shard1 | 63075 (子进程 63080) | cuda:2 | **存活** | 51min |
| precompute-v3-shard2 | 63218 (子进程 63223) | cuda:3 | **存活** | 51min |

### GPU 使用
4 张 4090 各约 1.4GB 显存占用，GPU 利用率 22-24%，运行正常。

### Precompute 进度（object benchmark 阶段）

| shard | 进度 | 速度 | 预计剩余 |
|-------|------|------|----------|
| shard0 | 2900/4857 (~60%) | 0.43s/sample | ~14min |
| shard1 | 2800/4857 (~58%) | 0.44s/sample | ~15min |
| shard2 | 2600/4856 (~54%) | 0.46s/sample | ~17min |

**spatial benchmark 已完成**：`/root/autodl-tmp/crm_cache_v3/spatial/` 已有完整输出（`manifest.json` + `obs_features.pt` + `k_samples.pt` + `expert_actions.pt`，所有 3 个 shard 的 partial 文件也在）。

**object benchmark 进行中**：`/root/autodl-tmp/crm_cache_v3/object/` 目前只有 partial 文件，每个 shard 已保存到 2000-2500 区间，尚未 merge。

### Eval 进度
task 1 `pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate`：rollout 5/10，已完成 5 次中成功 0 次。还在第 1 个 task（共 10 个 task），进度较慢。

### --cache_dir 参数
**有效**。`train_crm.py` 第 56 行定义了 `--cache_dir` 参数，代码中大量使用，precompute 正常写入 `/root/autodl-tmp/crm_cache_v3/`。

### 旧 cache
`/root/autodl-tmp/crm_cache/spatial/` 存在（上一版缓存），仅有 spatial 子目录。

---
