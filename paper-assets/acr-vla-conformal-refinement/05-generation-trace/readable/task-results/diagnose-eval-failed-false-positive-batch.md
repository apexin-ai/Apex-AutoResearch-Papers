# diagnose eval failed false positive batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-failed-false-positive-batch_20260520T195334_result.json`
- **Structured JSON:** [`92b45d9bdac5578b21a0.json`](../../sessions/92/92b45d9bdac5578b21a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总结论

### 实验 1: eval-obs-only-object-norm02-seed43-r3 (bjb2-28827)

**判断：真正失败，非误判。**

- 日志仅 37 行，完整内容已读取
- 只完成了 **8/10 个 task**（到 `milk` 为止），缺少 task 9、10
- 无 "Overall Success Rate" 汇总行
- 无 error/traceback（进程被静默 kill）
- JSON 输出文件 `eval_obs_only_object_norm02_seed43_r3.json` **不存在**
- 已完成的 8 个 task 结果：0+0+3+2+1+1+1+2 = **10/80 成功**（12.5%）
- Registry 的 sr=16 与实际日志不符（只完成了 80/100 rollouts），metrics 来源存疑

### 实验 2: eval-obs-only-object-norm01-seed48 (bjb1-18228)

**判断：真正失败，非误判。**

- 日志仅 32 行，完整内容已读取
- 只完成了 **5.5/10 个 task**（`tomato_sauce` 在 rollout 5/10 处中断）
- 无 "Overall Success Rate" 汇总行
- 无 error/traceback（进程被静默 kill）
- JSON 输出文件 `eval_obs_only_object_norm01_seed48.json` **不存在**
- 已完成部分：0+1+1+3+0 = **5/55 成功**（task 6 未完成不计）
- Registry 的 success_rate=0.18, n_tasks=10, total_rollouts=100 与实际日志严重不符（实际只跑了约一半），metrics 来源存疑

### 总结

两个实验都是**进程被静默终止**（无 traceback，无 JSON 输出），监控标记 failed 是正确的。Registry 中的 metrics 与日志实际进度不一致，建议核查 metrics 的注册来源——可能是从其他 run 误录入或手动填写的。两个实验都需要重跑。

---
