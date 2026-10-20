# code mvp 001c hard problems

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-001c-hard-problems_20260511T235134_result.json`
- **Structured JSON:** [`0910de04d67194767bbf.json`](../../sessions/09/0910de04d67194767bbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **v3 脚本** 已写入 `/home/sonny/redundancy-compound-sparsity/results/mvp/mvp_carc_validation_v3.py`
- **改动**：20 道简单题 → 5 道 AIME/AMC12 竞赛题，移除 `load_math_problems` 函数（直接用硬编码题目），输出改为 `mvp_results_v3.json`，metadata 增加 experiment/parent/purpose 字段，MAX_NEW_TOKENS 保持 4096
- **运行状态**：screen session `mvp-001c` 已启动，模型正在加载中
- **Registry**：mvp-001c 已注册为 RUNNING
- **注意**：`submit_training_job` 工具不在当前可用工具列表中，已用 screen session 替代。日志文件：`results/mvp/mvp_run_v3.log`

查看进度：`tail -f results/mvp/mvp_run_v3.log`（通过 ssh_read_only）

---
