# ops fix cuda2 collision and register crons

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_cuda2_collision_and_register_crons_20260519T064156_result.json`
- **Structured JSON:** [`5cfe251074754d0bb8ea.json`](../../sessions/5c/5cfe251074754d0bb8ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

冲突已解决。汇总：

## GPU 状态 (westd-29022)

| GPU | 进程 | 显存 | 利用率 | 状态 |
|-----|------|------|--------|------|
| cuda:0 | PID 56151 | 19242MiB | 98% | 运行中（其他任务） |
| cuda:1 | PID 66531 | 17254MiB | 99% | 运行中（其他任务） |
| cuda:2 | PID 63783 (SFT CKA-only) | 17802MiB | 98% | **冲突已解决**，仅剩此进程 |
| cuda:3 | PID 74303 (RASP fair) | 13110MiB | 97% | 正常运行 (2/164) |

## 冲突处理

- **存在冲突**：cuda:2 上同时运行 SFT CKA-only (PID 63783, 17802MiB) 和 Standard fair v2 (PID 74379, 12980MiB)，合计 30796MiB
- **已杀掉** `eval_humaneval_standard_fair` tmux session (Standard fair v2)，因为它刚启动无数据损失
- **Registry 已更新**：`eval_humaneval_grpo_standard_20_fair_2048_v2` → DONE/failed，原因：GPU collision
- **SFT CKA-only** (PID 63783) 继续在 cuda:2 独占运行，结果文件尚未生成
- **RASP fair** 在 cuda:3 正常运行，进度 2/164

**待办**：SFT CKA-only 完成后，需重启 Standard fair v2 (在 cuda:2 上)。

---
