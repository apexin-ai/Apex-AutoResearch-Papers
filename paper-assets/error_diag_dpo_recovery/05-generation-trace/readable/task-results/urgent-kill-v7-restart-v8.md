# urgent kill v7 restart v8

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_kill-v7-restart-v8_20260513T065318_result.json`
- **Structured JSON:** [`ea3b848dbddba1dcc04b.json`](../../sessions/ea/ea3b848dbddba1dcc04b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两卡都已成功加载模型并开始收集 trajectory：

- **cuda:0**: `Collecting 300 trajectories -> data/trajectories_v8_icl_cuda0/train_part0.jsonl`, ICL examples=2
- **cuda:1**: `Collecting 300 trajectories -> data/trajectories_v8_icl_cuda1/train_part1.jsonl`, ICL examples=2
- GPU 显存: cuda:0 = 10151 MiB, cuda:1 = 10171 MiB（模型已加载，正常范围）

---

## 检查清单

- [x] v7 进程已 kill（838043/838422 + 子进程 838056/838543 全部 SIGKILL）
- [x] temperature = 0.5 在命令行显式指定（`--temperature 0.5`）
- [x] CUDA_VISIBLE_DEVICES 硬设置（cuda:0 → `CUDA_VISIBLE_DEVICES=0`，cuda:1 → `CUDA_VISIBLE_DEVICES=1`）
- [x] φ Σ=1 自测通过（gamma=0.85/0.92/0.97/1.0 全 PASS）
- [x] v8 两卡启动成功（nvidia-smi 确认 GPU 0: 10151 MiB, GPU 1: 10171 MiB）
- [x] γ_max = 1.0 已修复（服务器 + 本地都已是 1.0）
- [x] Registry 已更新（v7 conclusion=failed + notes; v8 notes 已补充）

**注意**: 首次提交 v8 时因 v7 python 子进程残留导致 OOM，已 kill -9 清理后重新提交成功。

---
