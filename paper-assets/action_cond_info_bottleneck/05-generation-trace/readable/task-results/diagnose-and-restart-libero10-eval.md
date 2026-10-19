# diagnose and restart libero10 eval

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose-and-restart_libero10_eval_20260516T032128_result.json`
- **Structured JSON:** [`eef8c571f0edef205084.json`](../../sessions/ee/eef8c571f0edef205084.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**两个任务都已被重启，无需再次提交。**

| 实验 | 状态 | PID | 说明 |
|------|------|-----|------|
| `mvp1_baseline_std_libero10` | 运行中 | 733616 | libero_10 eval，已跑 ~21 分钟，videos 生成中 |
| `acib_v5_div_reg_seed2` | 运行中 | 744808 | step 200/20000，~0.8 steps/s |

**seed2 失败根因**：`wandb.init()` 认证失败（`maybe_login` 抛异常）。已用 `WANDB_MODE=disabled` 绕过重启。

---
