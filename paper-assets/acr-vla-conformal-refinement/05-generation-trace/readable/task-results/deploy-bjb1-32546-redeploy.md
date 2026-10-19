# deploy bjb1 32546 redeploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-redeploy_20260523T040933_result.json`
- **Structured JSON:** [`b9471d3894790624e4cb.json`](../../sessions/b9/b9471d3894790624e4cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个实验已成功启动并运行。

## 部署报告

| # | exp_id | GPU | PID | 状态 |
|---|--------|-----|-----|------|
| 1 | eval-supp-crm-norm02-spatial-s42-r2 | cuda:0 | 664402 | ✓ 10 tasks loaded |
| 2 | eval-supp-adapt-tau015-spatial-s42-r2 | cuda:1 | 664686 | ✓ 10 tasks loaded |
| 3 | eval-supp-adapt-tau025-spatial-s42-r2 | cuda:2 | 665520 | ✓ 10 tasks loaded |
| 4 | eval-supp-adapt-tau035-spatial-s42-r2 | cuda:4 | 667018 | ✓ 10 tasks loaded |
| 5 | train-crm-unified-4suite-r6 | cuda:3 | 668372 | ✓ epoch 39 训练中 |
| 6 | eval-supp-obj-crm005-s42-r2 | cuda:5 | 669419 | ✓ 10 tasks loaded |

**4-suite CRM 训练**：从 `/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/checkpoint_epoch0038.pt`（epoch 38）恢复，当前已进入 epoch 39。

**GPU 占用**：6 张 RTX 4090 全部分配，显存 544MB~6.3GB，utilization 10-31%。

**注意**：部署前发现旧进程实际仍在运行（GPU 0/3/4/5 上有之前的 evaluate/train 进程）。按指示执行 `tmux kill-server` 清理后重新部署。4-suite 训练从 epoch 38 checkpoint 无缝恢复，无数据丢失。

---
