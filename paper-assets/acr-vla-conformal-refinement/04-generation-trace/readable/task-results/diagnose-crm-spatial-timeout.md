# diagnose crm spatial timeout

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_crm-spatial-timeout_20260522T132326_result.json`
- **Structured JSON:** [`c0b503b66e201d2f1c0e.json`](../../sessions/c0/c0b503b66e201d2f1c0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告：π0.5 CRM Spatial Eval 超时

### 运行时间

三个实验均在 09:17 启动，21:17 被 kill（EXIT_CODE=124），**精确 12 小时超时**。

### Task 完成情况

| Seed | 完成 Tasks | 完成 Rollouts | 超时时正在执行 |
|------|-----------|--------------|---------------|
| 42 | **7/10** | 140/200 | Task 8 尚未开始 |
| 43 | **7/10** | 140/200 | Task 8 尚未开始 |
| 44 | **6/10** | 130/200 | Task 7 rollout 10/20 |

### 已完成 Task 的 Success Rate

| Task (简称) | Seed42 | Seed43 | Seed44 |
|---|---|---|---|
| between_plate_ramekin | 90% (18/20) | 85% (17/20) | 85% (17/20) |
| next_to_ramekin | 95% (19/20) | 95% (19/20) | 90% (18/20) |
| from_table_center | 100% (20/20) | 95% (19/20) | 95% (19/20) |
| on_cookie_box | 100% (20/20) | 90% (18/20) | 90% (18/20) |
| in_top_drawer | 95% (19/20) | 90% (18/20) | 95% (19/20) |
| on_ramekin | 50% (10/20) | 45% (9/20) | 30% (6/20) |
| next_to_cookie_box | 100% (20/20) | 100% (20/20) | *(未完成)* |
| **已完成部分平均** | **90.0%** (126/140) | **85.7%** (120/140) | **80.8%** (97/120) |

### 单 Task 耗时

- 12h / 7 tasks = **~103 分钟/task**（20 rollouts × 300 steps, K=10, n_action_steps=50）
- 预计完成全部 10 tasks 需 **~17.2 小时**

### Partial Results / W&B

- **无 W&B 输出**（日志中无任何 wandb 相关行）
- **无 partial results JSON**（output_file `logs/eval_spatial_acr_vla_pi05_seed*.json` 不存在，脚本在全部完成后才写入）
- 唯一可恢复的数据是日志中已打印的 per-task success rate（如上表）

### 建议

**放弃旧配置，不值得增加 timeout 重跑。** 理由：

1. 即使增加 timeout 到 18h，也只能补全剩余 3 个 task 的数据，而已有 7 个 task 的 partial metrics 已经可以从日志解析
2. 缺失的 3 个 task（task 8/9/10）在不同 seed 之间相同，不影响已完成 task 的对比分析
3. n_action_steps=10 的新实验速度会快 ~5x（决策点从 6 个增到 30 个，但单次生成 token 数大幅减少，且更符合官方配置），单 task 预计 ~20 分钟，全套 10 tasks ~3.5h
4. 如果需要旧配置的 partial 数据做对比，可以直接从日志中解析上表的数字，无需重跑

---
