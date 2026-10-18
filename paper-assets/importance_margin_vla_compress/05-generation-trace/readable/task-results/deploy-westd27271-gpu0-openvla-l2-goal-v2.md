# deploy westd27271 gpu0 openvla l2 goal v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy-westd27271-gpu0-openvla-l2-goal-v2_20260524T001308_result.json`
- **Structured JSON:** [`8d754121591dd649f722.json`](../../sessions/8d/8d754121591dd649f722.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常运行中，L2 pruning 已启动（256→128 tokens）。

**总结：**
- `eval_openvla_l2norm_k05_goal_seed42_v2` 已在 westd-27271 GPU 0 启动，PID=486402
- 使用与 v3 相同的命令（含 conda 激活修复 + `--mode l2norm_prune`）
- Registry 已更新为 RUNNING，spec 含 command/server/data_path=libero_goal/data_count=500/model_name=openvla/seed=42
- **GPU 1 空闲**（0 MiB, 0% utilization），可用于新任务
- 预计运行 ~248 分钟（基于 v3 耗时）

---
