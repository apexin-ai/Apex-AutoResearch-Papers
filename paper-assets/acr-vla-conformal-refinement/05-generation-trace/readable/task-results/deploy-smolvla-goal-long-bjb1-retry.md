# deploy smolvla goal long bjb1 retry

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_smolvla-goal-long-bjb1-retry_20260522T053355_result.json`
- **Structured JSON:** [`60e40b5e9b23510c10e2.json`](../../sessions/60/60e40b5e9b23510c10e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

## 部署摘要

| Exp ID | GPU | Benchmark | Seed | PID |
|--------|-----|-----------|------|-----|
| eval-smolvla-acr-goal-seed42 | cuda:3 | goal | 42 | 243608 |
| eval-smolvla-acr-long-seed42 | cuda:4 | long | 42 | 243677 |
| eval-smolvla-acr-goal-seed43 | cuda:5 | goal | 43 | 243748 |

均已在 registry 标记为 RUNNING。三个进程均已加载 SmolVLA 并打印正确 args，进入 rollout 阶段。

## 偏离原任务说明

1. **submit_training_job 工具不可用**，改用 `nohup + 独立 wrapper 脚本 + PID 捕获`（位于 `/tmp/launch_eval_*.sh`，日志写到 `/root/runs/acr-vla-conformal-refinement/`）。
2. **预计算 cache 不需要**：bjb2-28827 上的同类 SmolVLA acr_vla 评估命令（PIDs 171674/171949/172552）不引用任何 `crm_cache_v5/*goal*.pt`，并且 bjb2-28827 上 `/root/autodl-tmp/crm_cache_v5/` 目录根本不存在。SmolVLA acr_vla 评估 on-the-fly 计算特征。**跳过了 rsync 步骤**。
3. **bjb2-28827 实际运行的命令使用 `--crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt`**（与任务描述中 `crm_v3_norm/obs_only/crm_best.pt` 不同）。本次部署按用户明确指定使用 `crm_v3_norm/obs_only/crm_best.pt`（bjb1 本机已存在，1.32 MB，2026-05-15 训练）。如希望与 bjb2-28827 结果直接合并需确认是否同一 checkpoint。
4. evaluate.py 已原生支持 `--benchmark goal/long`（line 63, choices 列表包含两者）。
5. 三个 seed 设置（goal-42, long-42, goal-43）与 bjb2-28827 已部署的（long-43, goal-44, long-44）正好互补，覆盖 Goal 42/43 和 Long 42 三个新点。

## 命令模板（实际使用）

```bash
TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py \
  --mode acr_vla --benchmark &lt;goal|long> --n_rollouts 20 \
  --seed <42|43> --K 2 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt \
  --max_correction_norm 0.2 \
  --output_file logs/eval_&lt;bench>_acr_seed&lt;seed>.json
```

---
