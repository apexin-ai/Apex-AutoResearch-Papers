# ops fix bjb1 32546 conflicts deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-bjb1-32546-conflicts-deploy_20260516T213224_result.json`
- **Structured JSON:** [`f9b8a0d440aa0db38978.json`](../../sessions/f9/f9b8a0d440aa0db38978.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Kill 结果
两个未注册进程已成功终止：
- PID 306318 (`crm_perdof`, norm=0.3, seed=45) — 已 kill
- PID 306518 (`crm_perdof`, norm=0.2, seed=46) — 已 kill

GPU 2 只剩 PID 309158，GPU 4 只剩 PID 310485，符合预期。

### 2. 新实验部署状态

| 实验 | GPU | tmux PID | Python PID | 显存 | 状态 |
|------|-----|----------|-----------|------|------|
| eval-obs-only-object-norm02-seed47 | cuda:0 | 319119 | 319128 | 5020 MiB | ✓ 运行中 |
| eval-perdof-object-norm03-seed45-r2 | cuda:5 | 319454 | 319463 | 5630 MiB | ✓ 运行中 |

### 3. 未注册进程来源分析

被 kill 的两个进程的完整命令：
```
306318: python -u src/evaluate.py --mode crm_perdof ... --max_correction_norm 0.3 --seed 45 --output_file logs/eval_object_perdof_norm03_seed45.json
306518: python -u src/evaluate.py --mode crm_perdof ... --max_correction_norm 0.2 --seed 46 --output_file logs/eval_object_perdof_norm02_seed46.json
```

**判断：旧 Worker 遗留进程。** 依据：
- 无对应 tmux session（kill 前 tmux ls 只有 `eval-argmin-object-seed46`）
- 无 cron 定时任务
- 命令格式与 `submit_training_job` 提交的一致，但缺少 tmux 包装 → 可能是某次 Worker 通过 `ssh_execute` 直接启动（未走 `submit_training_job`），或对应 tmux session 意外退出后进程变为孤儿进程

---
