# check cqa1 oom random k095 goal

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cqa1_oom_random_k095_goal_20260527T093731_result.json`
- **Structured JSON:** [`c2c62db4db3b95aaf4b0.json`](../../sessions/c2/c2c62db4db3b95aaf4b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`eval_openvla_random_k095_goal_seed42` **没有崩溃，已成功完成**。结果文件显示：

**openvla_random_prune_k095_goal_seed42** — 已完成于 2026-05-27 16:07:16
- Overall: **78.4%** (392/500), 耗时 ~345 分钟
- 10/10 tasks 全部跑完（每个 50 episodes）

Per-task 结果：

| Task | Success Rate |
|------|-------------|
| open the middle drawer of the cabinet | 50.0% |
| put the bowl on the stove | 94.0% |
| put the wine bottle on top of the cabinet | 82.0% |
| open the top drawer and put the bowl inside | 56.0% |
| put the bowl on top of the cabinet | 98.0% |
| push the plate to the front of the stove | 84.0% |
| put the cream cheese in the bowl | 76.0% |
| turn on the stove | 100.0% |
| put the bowl on the plate | 86.0% |
| put the wine bottle on the rack | 58.0% |

现在确认其他 4 个 GPU 实验状态。从 `nvidia-smi`：

| GPU | PID | Memory | 预期实验 | 状态 |
|-----|-----|--------|---------|------|
| GPU0 | 109156 | 10131MiB | eval_pi05_random_k07_long (expected PID 109152) | **运行中** |
| GPU1 | 118731 | 9990MiB | eval_pi05_random_k05_long (expected PID 118726) | **运行中** |
| GPU2 | 93525 | 10657MiB | eval_pi05_l2norm_k085_long (expected PID 93525) | **运行中** |
| GPU3 | 897100 | 15694MiB | eval_openvla_attn_k05_goal_v3 (expected PID 897095) | **运行中** |

PID 略有偏移是 parent/child 进程差异，所有 4 个实验正常运行。GPU3 上现在跑的是 `attn_k05_goal_v3`，因为 `random_k095_goal` 已在 16:07 完成释放了 GPU。

---
