# diagnose spatial r4 baseline missing

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_spatial-r4-baseline-missing_20260522T135352_result.json`
- **Structured JSON:** [`e733e032ce250c3cd039.json`](../../sessions/e7/e733e032ce250c3cd039.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：正常完成

3 个 seed 全部在今天 20:17-20:18（北京时间）完成，结果文件完整。

### 各 seed Success Rate

| Seed | Overall | 失败任务 |
|------|---------|----------|
| 42 | **98.0%** | bowl_on_ramekin 85%, bowl_on_wooden_cabinet 95% |
| 43 | **97.5%** | bowl_on_ramekin 75% |
| 44 | **98.5%** | bowl_on_ramekin 90%, bowl_on_wooden_cabinet 95% |

**均值：98.0%**（3 seeds 平均）

### Per-task 摘要
- 10 个任务中 **8 个在所有 seed 下都是 100%**
- 唯一短板任务：`pick_up_the_black_bowl_on_the_ramekin`（3 seed 均值 83.3%）
- `bowl_on_wooden_cabinet` 在 seed42/44 略低（95%），seed43 为 100%

### 当前服务器状态
- tmux 仅剩 `precompute-pi05-long-bjb1-18228` session（今天 17:00 创建）
- cuda:1-3 已释放，可用于其他任务

---
