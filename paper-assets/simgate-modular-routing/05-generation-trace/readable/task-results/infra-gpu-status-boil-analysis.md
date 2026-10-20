# infra gpu status boil analysis

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-boil-analysis_20260513T181135_result.json`
- **Structured JSON:** [`1a5377590b8df028a8b8.json`](../../sessions/1a/1a5377590b8df028a8b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU 状态
| GPU | 利用率 | VRAM | 任务 |
|-----|--------|------|------|
| GPU0 | 0% (推理间歇) | 28/32 GB | 预筛 `find-plant` |
| GPU1 | 58% | 28/32 GB | boil v3 (PID 650421, 已运行 1h49m) |

**GPU1 不空闲，boil v3 仍在跑。**

### Boil v3 进度：12/20 episodes

中间结果 vs MVP 对比：

| Mode | v3 (n=12) | MVP (n=20) | 变化 |
|------|-----------|------------|------|
| always_internal | **-41.17** | -49.75 | +8.6 |
| always_deterministic | **0.92** | -19.70 | **+20.6** |
| oracle_routing | **6.33** | -29.70 | **+36.0** |

v3 各 mode 均大幅优于 MVP。oracle_routing 有一个 episode 达 70.0 分（variation 3），但方差很大。

### 预筛进度（GPU0）
- 30 总任务，跳过 5 个 MVP 已测
- 已完成 5/25：chemistry-mix, chemistry-mix-paint-tertiary-color, find-animal, find-living-thing, find-non-living-thing
- 正在跑第 6 个：find-plant
- 剩余 19 个，每个约 20 min → 单 GPU 约需 6+ 小时

### 下一步
boil v3 预计还需 ~30 分钟完成（8 episodes × ~4 min/ep）。完成后 GPU1 空闲，可立即启动 GPU1 分担剩余预筛任务。需要等 boil v3 结束。

---
