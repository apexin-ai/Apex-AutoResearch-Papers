# exp accum olmo temp 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_accum_olmo_temp_001_20260521T072723_result.json`
- **Structured JSON:** [`b7fc2d58087d4dd0e77a.json`](../../sessions/b7/b7fc2d58087d4dd0e77a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 已正常启动运行。Phase 1 正在加载 OLMo-1B 权重进行 LoRA 训练。

完成情况：
- 脚本 `accumulation_pipeline_olmo_temp09.py` 已创建并部署到服务器
- 数据就绪：`depth_0.jsonl`（symlink→olmo/depth_0.jsonl）+ `depth_1.jsonl`，各 5000 行
- 训练任务 `accum_olmo_temp_001` 已通过 `submit_training_job` 提交，tmux session 运行中，PID 361607
- Registry 已更新为 RUNNING，spec 包含完整 provenance
- 当前正在 Phase 1b LoRA training，使用 cuda:0

mix50 等 mix25 完成后再提交。

---
