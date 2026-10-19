# monitor bjb2 28827 sweep verify

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bjb2-28827-sweep-verify_20260515T033519_result.json`
- **Structured JSON:** [`8ef947f54a0cda83045e.json`](../../sessions/8e/8ef947f54a0cda83045e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 6 路 magnitude sweep 状态总结

### 进程状态：全部存活 ✓

| exp_id | PID | 运行时间 | 状态 |
|--------|-----|---------|------|
| eval-mag-perdof-norm003 | 13185 | 19:30 | 运行中 |
| eval-mag-perdof-norm005 | 13456 | 19:28 | 运行中 |
| eval-mag-perdof-norm02 | 13728 | 19:26 | 运行中 |
| eval-mag-perdof-norm03 | 14260 | 19:23 | 运行中 |
| eval-mag-obsonly-norm005 | 14854 | 19:20 | 运行中 |
| eval-mag-obsonly-norm02 | 15190 | 19:18 | 运行中 |

### GPU 显存

所有 6 块 GPU 各占用 **~6240 MiB / 24564 MiB (25%)**，利用率 ~19%。无 OOM 风险。没有额外的旧进程残留——6 块 GPU 显存用量一致。

### 日志进度

- 所有 6 个实验均已完成模型加载、CRM checkpoint 加载、10 个 task 加载
- **perdof-norm03** (norm=0.3) 进度最快：task 1 `pick_up_the_black_bowl...` rollout 5/10，成功率 5/5
- 其余 5 个实验日志停在 "10 tasks loaded"，正在执行 task 1 的 rollouts（python -u 已启用，但 rollout 进度行用 `\r` 覆盖写入，完成整个 task 后才会输出新行）

### 结论

6 路实验全部正常运行，无异常。norm=0.3 的实验跑得最快（correction 幅度大，可能更快到达目标导致 episode 更短）。按 10 tasks × 10 rollouts 的规模，预计每个实验需要 1-3 小时完成。

---
