# fix westb mbpp dataset sync

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westb_mbpp_dataset_sync_20260519T185123_result.json`
- **Structured JSON:** [`3928e79328e2eca7dc91.json`](../../sessions/39/3928e79328e2eca7dc91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切正常：

- **tmux session**: ALIVE
- **MBPP 数据集**: 已缓存（`/root/.cache/huggingface/datasets/mbpp/` 下有 `full/` 和 `sanitized/` 两个子集）
- **eval 脚本**: 存在，最新（May 20 02:14）
- **实验进度**: 模型已加载，MBPP 数据集已成功下载（374 tasks），正在推理中 — 当前完成 11/374（约 3%），每个 task ~35s，预计总耗时约 3.6 小时
- **Registry**: 该实验未在 registry 中注册（retry worker 直接用 tmux 重启的）

`network_turbo` 方案已生效，数据集自动下载成功，实验正常运行中，无需干预。

---
