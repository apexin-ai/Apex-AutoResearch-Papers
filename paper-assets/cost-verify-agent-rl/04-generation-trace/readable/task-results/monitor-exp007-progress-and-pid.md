# monitor exp007 progress and pid

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp007_progress_and_pid_20260514T005836_result.json`
- **Structured JSON:** [`ac438e39ed8568ad7eb4.json`](../../sessions/ac/ac438e39ed8568ad7eb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp007 训练状态报告

| 项目 | 状态 |
|------|------|
| **tmux session** | `exp007` |
| **train.py PID** | `178842` |
| **当前步数** | **0/30** — 仍在第一个 step 的 rollout 阶段（生成序列） |
| **action_is_valid** | 尚无数据（step 0 未完成） |
| **启动时间** | 2026-05-14 08:50 UTC（约 9 分钟前） |
| **模型** | Qwen3-1.7B，2× GPU（FSDP），CUDA_VISIBLE_DEVICES=0,1 |
| **checkpoint 目录** | `/root/autodl-tmp/checkpoints/exp_007/` — 空，尚无 checkpoint |
| **磁盘** | 根分区 30G，已用 9.8G (33%)，剩余 21G — 健康 |

**关键进程树**：
- tmux session `exp007` → bash (178832) → timeout (178836) → train.py (178842) → Ray workers (TaskRunner 182091, WorkerDict 182293/182294)

**预计到达 step 10**：第一个 step 包含环境初始化 + vLLM 引擎加载，通常最慢。后续 step 应快得多。无法精确预估，建议 30-60 分钟后再次检查。

---
