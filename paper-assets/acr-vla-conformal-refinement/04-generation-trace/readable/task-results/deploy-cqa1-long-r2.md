# deploy cqa1 long r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-long-r2_20260526T103252_result.json`
- **Structured JSON:** [`31b3ed602c08a1b93fad.json`](../../sessions/31/31b3ed602c08a1b93fad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已部署并运行：

| 实验 | GPU | tmux | PID | 状态 |
|---|---|---|---|---|
| pi05-crm-k2-long-s42-r2 | cuda:4 | pi05-crm-k2-long-s42-r2 | 346236 | 加载 PI05 中 |
| pi05-adaptive-long-s42-r2 | cuda:5 | pi05-adaptive-long-s42-r2 | 346704 | 加载 PI05 中 |

**踩坑记录**：首次提交因 `python: command not found`（EXIT_CODE=127）失败，已用 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ..."` 重新提交成功。

**git 状态偏差**：服务器 HEAD 是 `63f5c81`（无 `a594db5`），但工作树的 `src/evaluate.py` 已含 `crm_obs_only` 和 `adaptive_conformal_crm` 两个 mode，命令正常运行。如需严格对齐 `a594db5`，需提供 remote 信息。

---
