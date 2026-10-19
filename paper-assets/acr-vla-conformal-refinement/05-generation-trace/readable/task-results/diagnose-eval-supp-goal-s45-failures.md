# diagnose eval supp goal s45 failures

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-supp-goal-s45-failures_20260523T225630_result.json`
- **Structured JSON:** [`0693b5fd01f4c88d628f.json`](../../sessions/06/0693b5fd01f4c88d628f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**两个实验都已正常完成，不是真正的失败。** 是 cron 监控误报。

### 根因

启动这两个实验时**没有写 exit sentinel**，也没有将日志 tee 到 `~/runs/` 路径，且评估脚本不上报 W&B metrics。cron 检测不到任何完成信号，因此：
- `eval-supp-goal-vla-only-s45` → 进程退出后 cron 报 "Process exited without valid W&B metrics"
- `eval-supp-goal-crm-norm005-s45` → 进程退出后 cron 报 "Process gone, no sentinel, no W&B"

### 实验结果

| 实验 | 模式 | Overall Success Rate | 完成时间 |
|------|------|---------------------|----------|
| eval-supp-goal-vla-only-s45 | vla_only | **83.5%** (167/200) | May 24 06:39 |
| eval-supp-goal-crm-norm005-s45 | crm_obs_only (norm=0.05) | **81.0%** (162/200) | May 24 06:45 |

### Per-task 对比

| Task | VLA-only | CRM norm005 |
|------|----------|-------------|
| open_middle_drawer_of_cabinet | 90% | 70% |
| put_bowl_on_stove | 100% | 100% |
| put_wine_bottle_on_top_cabinet | 90% | 85% |
| open_top_drawer_put_bowl_inside | 65% | 60% |
| put_bowl_on_top_cabinet | 85% | 100% |
| push_plate_to_front_stove | 85% | 90% |
| put_cream_cheese_in_bowl | 50% | 50% |
| turn_on_stove | 100% | 95% |
| put_bowl_on_plate | 90% | 95% |
| put_wine_bottle_on_rack | 80% | 65% |

结果 JSON 已保存在服务器上：
- `logs/eval_goal_vla_only_seed45.json`
- `logs/eval_goal_crm_obs_only_norm0.05_seed45.json`

**无需重跑。** 只需将 cron 中这两个实验标记为完成即可。

---
