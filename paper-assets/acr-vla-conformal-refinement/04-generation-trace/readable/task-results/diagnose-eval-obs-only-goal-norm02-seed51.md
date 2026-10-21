# diagnose eval obs only goal norm02 seed51

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-goal-norm02-seed51_20260520T133048_result.json`
- **Structured JSON:** [`3dace0c25bfcf50ddcaf.json`](../../sessions/3d/3dace0c25bfcf50ddcaf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**实验实际上已成功完成，被误判为失败。**

### 证据

1. **日志完整**：所有 10 个 task × 10 rollouts 全部跑完，最终输出 `Overall success rate (crm_obs_only): 66.0% (66/100)`
2. **JSON 结果已保存**：`logs/eval_obs_only_goal_norm02_seed51.json` (1319 bytes, 21:19 写入)，内容完整
3. **GPU 已释放**：cuda:1 当前空闲（2MiB / 0% utilization），进程正常退出
4. **无错误信息**：日志中无 OOM、segfault、traceback，stderr 为空，return_code = 0

### 完整结果

| Task | Success Rate |
|------|-------------|
| turn_on_the_stove | 100% (10/10) |
| put_the_bowl_on_the_plate | 100% (10/10) |
| put_the_bowl_on_the_stove | 90% (9/10) |
| push_the_plate_to_the_front_of_the_stove | 90% (9/10) |
| put_the_bowl_on_top_of_the_cabinet | 80% (8/10) |
| put_the_wine_bottle_on_top_of_the_cabinet | 50% (5/10) |
| put_the_wine_bottle_on_the_rack | 50% (5/10) |
| open_the_middle_drawer_of_the_cabinet | 40% (4/10) |
| open_the_top_drawer_and_put_the_bowl_inside | 40% (4/10) |
| put_the_cream_cheese_in_the_bowl | 20% (2/10) |
| **Overall** | **66.0% (66/100)** |

## 诊断结论

**误报（False Positive）**。实验正常完成并输出了完整结果，但监控系统因未检测到 sentinel 标记或 W&B 日志而判定失败。根因是评估脚本没有写入监控系统期望的 sentinel/完成标记。不需要重试，结果已可用。需要修复的是监控侧的完成检测逻辑，或在 `evaluate.py` 末尾添加 sentinel 输出。

---
