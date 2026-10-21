# code ensemble cv 7 8b

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ensemble_cv_7_8b_20260521T231310_result.json`
- **Structured JSON:** [`cf62e9fb24f3073d829a.json`](../../sessions/cf/cf62e9fb24f3073d829a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已在运行（PID 17070, CPU 1912%），日志因 Python stdout 缓冲暂时为空，待脚本 flush 后会显示进度。

完成摘要：
- **脚本同步** ✓ — 修正 R1-8B 路径 `hidden_states` → `hidden_states_r1_8b_full`
- **Dry-run** ✓ — 成功加载 209 traces
- **任务提交** ✓ — tmux session `ensemble_cv_7_8b`，PID 17070
- **Registry** ✓ — 状态 RUNNING
- **OT-7B** — hidden states 不存在于服务器，该模型会在脚本中 catch exception 并记录 error
- **产出** — `artifacts/ensemble_cv_results.json`（实际只含 R1-8B 结果 + OT-7B error）
- **日志** — `~/runs/contrastive_trace_safety/ensemble_cv_7_8b.log`

---
