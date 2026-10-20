# code westd cleanup grasp restart

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd-cleanup-grasp-restart_20260515T124017_result.json`
- **Structured JSON:** [`1c3313822c5c3e10e505.json`](../../sessions/1c/1c3313822c5c3e10e505.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型正在加载中，运行正常。

---

**清理报告：**

| 操作 | 释放空间 |
|------|---------|
| 删除 `graspune_output/`（冗余中间产物，`pruned_graspune_20/` 已有最终模型） | ~12GB |
| pip cache purge（198 files） | ~2.1GB |
| conda clean --all | ~107MB |

磁盘状态：228GB used → 125GB used，**126GB 可用**（目标 ≥30GB）。

**GraSP baseline 已提交：**
- exp_id: `grasp_baseline_westd`
- 服务器: westd-11672, cuda:0
- PID: 34195, tmux session: `grasp_baseline_westd`
- 跳过 Phase 1/2（pruning + convert 已完成），直接跑 Phase 3 eval（GSM8K）
- 结果将输出到 `results/eval_pruned_graspune_20_greedy.json`

---
