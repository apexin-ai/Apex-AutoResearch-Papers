# check smolvla goal long bjb2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_smolvla-goal-long-bjb2_20260522T053428_result.json`
- **Structured JSON:** [`173a48421f0df4344f19.json`](../../sessions/17/173a48421f0df4344f19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## SmolVLA Goal/Long Eval 进度报告 (bjb2-28827)

### PID → Experiment 映射

| PID (bash) | Python PID | GPU | Benchmark | Seed | Exit ID |
|------------|-----------|-----|-----------|------|---------|
| 171674 | 171683 | cuda:3 | **long** | 43 | eval-smolvla-crm-long-seed43-v2 |
| 171949 | 171958 | cuda:4 | **goal** | 44 | eval-smolvla-crm-goal-seed44-v2 |
| 172552 | 172561 | cuda:5 | **long** | 44 | eval-smolvla-crm-long-seed44-v2 |

共同配置：`--mode acr_vla --K 2 --n_rollouts 20 --crm_checkpoint crm_best.pt --conformal_threshold 0.074855`，`TORCHDYNAMO_DISABLE=1`，模型 `/root/autodl-tmp/models/smolvla_libero/`。

### 进度（截至 13:33）

三个任务全部停留在 **task 1/10, rollout 15/20**（每 5 rollouts 刷一次 log，可能实际跑到 16-19）：

| 实验 | 已运行 | 当前 task | rollout | success |
|------|--------|----------|---------|---------|
| long-seed43 | 22m48s | LIVING_ROOM_SCENE2_put_both_the_alphabet_soup... | 15/20 | 0/15 |
| goal-seed44 | 22m42s | open_the_middle_drawer_of_the_cabinet | 15/20 | 0/15 |
| long-seed44 | 22m35s | LIVING_ROOM_SCENE2_put_both_the_alphabet_soup... | 15/20 | 0/15 |

GPU 显存：long 占 6.3GB，goal 占 5.5GB，正常运行中（log mtime 在最近 30s 内更新）。

### 速度与剩余时间估算

- 模型 load 约 3-5min，之后 ~17-18min 跑完 task1 的 ~15 rollouts → **约 1.1-1.2 min/rollout**
- 总量 200 rollouts/run，剩余 ~185 → **预计还需 ~3.5h，约 17:00 完成**

### 注意点

1. **同名 v1 exit 文件存在**：`/tmp/agent-ml-exit/eval-smolvla-crm-{goal-seed44,long-seed43,long-seed44}.exit`（13:10 写入），说明 v1 已先失败/退出过；当前 v2 是重跑，写到 `*-v2.exit`。
2. **task1 全部 0 成功** — 与 SmolVLA + ACR_VLA 在 long/goal 上历史表现一致；需关注是否所有 task 都 0%（如果是说明 conformal_threshold 配置或 CRM 在此模型上未生效）。
3. 任务标题提到"注册 cron"，但任务正文未描述要注册什么 cron。如需周期性状态检查/wandb push/result 收集，请告知具体目标。

---
