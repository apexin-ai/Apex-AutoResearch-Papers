# check bjb2 28827 crm eval

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb2-28827-crm-eval_20260523T010023_result.json`
- **Structured JSON:** [`df5a011f8dc66e330c03.json`](../../sessions/df/df5a011f8dc66e330c03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完毕。以下是完整状态报告：

---

## 6 个进程状态汇总

### GPU 0/1/2: CRM obs_only Object eval（对应 exp_id）

| GPU | PID | seed | 启动时间 (CST) | 状态 |
|-----|-----|------|---------------|------|
| cuda:0 | 366365 | 42 | 07:12:50 | **RUNNING** |
| cuda:1 | 367985 | 43 | ~07:13 | **RUNNING** |
| cuda:2 | 368249 | 44 | ~07:13 | **RUNNING** |

- 实际命令: `python -u src/evaluate.py --mode crm_obs_only --model smolvla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed {42,43,44} --n_rollouts 20 --K 10 --obs_dim 960 --n_action_steps 50 --max_steps 280`
- 运行时长: **~2 小时**（不是 10 小时，启动于 23:12 UTC May 22，当前服务器时间 09:00 CST = 01:00 UTC May 23）
- 显存占用: 各 ~3408MiB，GPU 利用率 22-27%
- **无输出文件产生**：尚未生成 JSON 结果或视频文件，stdout 通过 pipe 输出（非日志文件）
- 预计工作量: 10 tasks × 20 rollouts × max 280 steps，K=10 CRM 推理较慢，预计还需数小时

### GPU 3/4/5: VLA-only Spatial eval（额外任务）

| GPU | PID | seed | 启动时间 (CST) | 状态 |
|-----|-----|------|---------------|------|
| cuda:3 | 373281 | 42 | 07:20:29 | **RUNNING** |
| cuda:4 | 373273 | 43 | ~07:20 | **RUNNING** |
| cuda:5 | 373275 | 44 | ~07:20 | **RUNNING** |

- 命令: `python -u src/evaluate.py --mode vla_only --model smolvla --benchmark spatial --seed {42,43,44} --n_rollouts 20 --K 1 --n_action_steps 50 --max_steps 280`
- 显存: 各 ~2501MiB，GPU 利用率 13-17%
- **GPU 3/4/5 不空闲**

### 注意事项

1. **实际 mode 不是 `crm_k1_accg`，而是 `crm_obs_only`**。Checkpoint 也不同：用的是 `crm_smolvla_3suite_v1/crm_best.pt`（不是之前的 `crm_k1/crm_k1_best.pt`），K=10 而非 K=1。
2. **之前的 CRM k1 结果**（`eval_crm_k1_object_seed{42,43,44}_plan702.json`，May 21）已完成：success_rate 分别为 0.11, 0.11, 0.10。
3. **VLA-only object eval** 的 3 个完整 20-rollout 结果存在 `outputs/eval/2026-05-22/` 下（23:05 CST 启动，已完成）。
4. 进程 stdout 输出到 pipe 而非文件，无法直接查看进度。需等待进程完成后检查输出 JSON。

---
