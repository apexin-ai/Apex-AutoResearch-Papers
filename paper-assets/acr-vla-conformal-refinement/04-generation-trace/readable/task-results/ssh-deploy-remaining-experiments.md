# ssh deploy remaining experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deploy-remaining-experiments_20260520T063721_result.json`
- **Structured JSON:** [`4bc0a2a89ba6a6d66cbc.json`](../../sessions/4b/4bc0a2a89ba6a6d66cbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。注意 seed42 和 seed44 的 random selection 是 retry（之前跑过一轮），registry 自动记录了 retry_count=1。

## 汇报

### 部署结果

| 实验 | 服务器:GPU | 优先级 | 状态 |
|------|-----------|--------|------|
| eval-random-selection-object-seed42 | bjb2-28827:cuda:0 | P0 | ✓ 已启动，加载环境中 |
| eval-random-selection-object-seed44 | bjb2-28827:cuda:2 | P0 | ✓ 已启动，加载环境中 |
| eval-obs-only-object-norm02-seed42 | bjb2-28827:cuda:3 | P1 | ✓ 已启动，加载模型中 |

### eval-adaptive-k-spatial-p50-seed42 确认

✓ 在 bjb2-40593:cuda:0 上运行中（PID 675831，启动于 14:02，已跑约 36 分钟）

### 集群全景

| 服务器 | GPU 总数 | 占用 | 空闲 | 运行中的实验 |
|--------|---------|------|------|-------------|
| bjb1-18228 | 4 | 4 | **0** | vla-only-spatial-seed52/53, crm-long-seed53, vla-only-long-seed54 |
| bjb1-32546 | 6 | 5 | **1** (GPU 5) | crm-long-seed51/54, vla-only-long-seed53/54, vla-only-spatial-seed54 |
| bjb2-28827 | 6 | 6 | **0** | crm-long-seed52, crm-goal-seed49/50 + 新部署 3 个 |
| bjb2-40593 | 1 | 1 | **0** | adaptive-k-spatial-p50-seed42 |

**集群总计**: 17 GPU，16 占用，**1 空闲**（bjb1-32546:cuda:5）。

注意：用户命令模板中 `evaluate.py` 路径已修正为 `src/evaluate.py`；CRM 实验补充了 `--crm_checkpoint` 参数。

---
