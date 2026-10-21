# diag norm005 seed67 cron check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_norm005-seed67-cron-check_20260521T044046_result.json`
- **Structured JSON:** [`3beeebdd054587fb8ca0.json`](../../sessions/3b/3beeebdd054587fb8ca0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，汇总如下：

## 诊断结果

### 1. eval-obs-only-object-norm005-seed67：**从未启动**

- 无进程运行
- 无日志文件、无 JSON 输出、无 sentinel
- 服务器上 norm005 最新的 seed 是 seed66（非 seed67）
- **Cron 告警原因**：该实验从未被启动，cron 监控了一个不存在的任务名。属于 cron 配置错误，不是 false positive。

### 2. eval-obs-only-object-norm005-seed66（附带发现）：**进程已死，未完成**

- 进程不在运行
- 日志 `/root/autodl-tmp/logs/norm005_seed66.log` 停在第 9/10 个任务（chocolate_pudding），最后修改 12:41
- 无输出 JSON
- **状态：failed**（进程在最后一个任务 orange_juice 之前死亡）

### 3. eval-obs-only-object-norm01-seed67：**已完成**

- `overall_success_rate`: **14.0%** (14/100)
- `per_task_sr`:

| Task | SR |
|------|-----|
| alphabet_soup | 0% (0/10) |
| cream_cheese | 0% (0/10) |
| salad_dressing | 20% (2/10) |
| bbq_sauce | 40% (4/10) |
| ketchup | 0% (0/10) |
| tomato_sauce | 10% (1/10) |
| butter | 0% (0/10) |
| milk | 20% (2/10) |
| chocolate_pudding | 20% (2/10) |
| orange_juice | 30% (3/10) |

- JSON: `/root/logs/eval_object_crm_obs_only_norm0.1_seed67.json`
- **Cron miss 1/5 是 false positive**（已完成，cron 找不到 sentinel/W&B 而已）

### 行动建议

- norm005-seed67 需要手动启动（或修正 cron 监控名到实际存在的实验）
- norm005-seed66 需要重跑（进程异常退出，差 1 个任务未完成）

---
