# check d088 and openvla status round2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d088-and-openvla-status-round2_20260520T173448_result.json`
- **Structured JSON:** [`e209bcbd8089c6847093.json`](../../sessions/e2/e209bcbd8089c6847093.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

### 1. D088 Adaptive Uncertainty Head Eval

| Seed | PID | GPU | n_rollouts | 已运行 | 状态 | 进度 |
|------|-----|-----|------------|--------|------|------|
| 42 | 741948 | cuda:0 | 10/task | 14min | **RUNNING** | 1/10 tasks done |
| 43 | 742213 | cuda:1 | 10/task | 14min | **RUNNING** | 1/10 tasks done |
| 44 | 728278 | cuda:5 | 10/task (n_rollouts=100) | 35min | **RUNNING** | ~2.5/10 tasks done |

**Seed44 已完成 task 结果：**
| Task | SR |
|------|----|
| alphabet_soup | 0% (0/10) |
| cream_cheese | 10% (1/10) |
| salad_dressing | 进行中 (1/5) |

**Seed42 & 43** 都刚完成第 1 个 task (alphabet_soup: 0%)，正在跑第 2 个。

注意：seed44 的 args 显示 n_rollouts=100，但实际每个 task 跑 10 rollouts（100 total / 10 tasks = 10 per task），和 seed42/43 一致。

### 2. OpenVLA Precompute

| 指标 | 值 |
|------|----|
| PID | 365151 |
| 状态 | **RUNNING** |
| 已运行 | 3h 45min |
| 缓存文件数 | **67,530** .pt files |
| 缓存大小 | 5.5 GB |
| 缓存路径 | `/root/autodl-tmp/crm_cache_k1_openvla/object/` |
| 最后写入 | 01:37 (仍在活跃写入) |

### 3. GPU 使用状态

| GPU | Util | Mem Used | Mem Total | 占用进程 |
|-----|------|----------|-----------|----------|
| 0 | 17% | 5166 MiB | 24564 MiB | seed42 eval |
| 1 | 20% | 5166 MiB | 24564 MiB | seed43 eval |
| 2 | 0% | 1 MiB | 24564 MiB | **空闲** |
| 3 | 35% | 22651 MiB | 24564 MiB | OpenVLA precompute |
| 4 | 30% | 5267 MiB | 24564 MiB | 未知进程 |
| 5 | 99% | 9499 MiB | 24564 MiB | seed44 eval |

GPU 2 完全空闲，GPU 4 有未知占用（5.2GB）。

---
