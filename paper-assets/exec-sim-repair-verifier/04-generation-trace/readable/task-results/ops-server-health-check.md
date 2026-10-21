# ops server health check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-health-check_20260516T163649_result.json`
- **Structured JSON:** [`bbf7272742c8c1ccc834.json`](../../sessions/bb/bbf7272742c8c1ccc834.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇总

### GPU 使用情况

| GPU | 显存占用 | 利用率 | 运行进程 |
|-----|---------|--------|---------|
| cuda:0 | 19,557 / 32,607 MiB (60%) | 99% | deepseek-cls-repo |
| cuda:1 | 19,713 / 32,607 MiB (60%) | 99% | deepseek-cwm-repo |
| cuda:2 | 0 MiB | 0% | **空闲** |
| cuda:3 | 0 MiB | 0% | **空闲** |

### 各进程状态

**1. deepseek-cls-repo** — PID 470263 (wrapper) / 470268 (training), cuda:0
- 状态：**运行中**
- 进度：step **3156/6633 (48%)**，epoch 2/3，已跑 ~10h
- 速度：~10.5s/step
- 已保存 checkpoint-2211
- ⚠️ **eval_loss = nan**（epoch 1 结束时），需关注

**2. deepseek-cwm-repo** — PID 479953, cuda:1
- 状态：**运行中**
- 进度：step **3683/13266 (28%)**，epoch 1/3，已跑 ~8h21m
- 速度：~8s/step
- checkpoint 目录为空（尚未保存任何 checkpoint）
- 尚无 eval_loss（未完成 epoch 1）

**3. deepseek-traj-repo-8k (s0/默认seed)** — ✅ 已完成
- exit code 0，完成于 2026-05-16 15:33:45Z
- train_loss: **0.2081**, eval_loss: **0.1447**
- best model → `/root/autodl-tmp/checkpoints_deepseek_traj_repo_8k/best`

**4. deepseek-traj-repo-8k-s123** — ✅ 已完成
- exit code 0，完成于 2026-05-16 15:33:40Z
- train_loss: **0.2125**, eval_loss: **0.1462**
- best model → `/root/autodl-tmp/checkpoints_deepseek_traj_repo_8k_s123/best`

**5. deepseek-traj-repo-8k-s456** — ✅ 已完成
- 完成于 2026-05-17 00:30:27（exit 文件缺失但日志确认训练完整结束）
- train_loss: **0.2176**, eval_loss: **0.1547**
- best model → `/root/autodl-tmp/checkpoints_deepseek_traj_repo_8k_s456/best`

**6. deepseek-traj-func** (PID 504483) — ✅ 早已完成，进程不存在

### 异常发现

1. **cls-repo eval_loss = nan**：epoch 1 评估时 loss 为 nan，训练仍在继续但这可能意味着评估有问题（分类任务可能使用了不匹配的 loss 函数或标签有问题）
2. **cwm-repo 无 checkpoint**：已训练 28% 但输出目录为空，可能 save_strategy 设置为按 epoch 保存，需等 epoch 1 完成
3. **GPU 2-3 完全空闲**：3 个 traj-repo-8k 变体均已完成，可用于新任务
4. 用户提到的 "deepseek-traj-repo-8k-s0" 对应的是无后缀的 `deepseek-traj-repo-8k`（默认 seed）

---
