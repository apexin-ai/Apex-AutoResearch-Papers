# exp random50 fix relaunch

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_random50_fix_relaunch_20260513T114420_result.json`
- **Structured JSON:** [`5dd5195100264dae97c6.json`](../../sessions/5d/5dd5195100264dae97c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

### 执行结果

| 步骤 | 结果 |
|------|------|
| **Kill** | `phase2_random50_baseline` tmux session 已终止 |
| **代码修改** | `run_random50.sh` 已覆写：lr=5e-5, epochs=3, gen_tokens=500K, +env.sh +TRANSFORMERS_OFFLINE=1。`run_mvp.py` 中 `random_50` 已有实现（L118-128），无需修改 |
| **新进程** | PID **219838**，tmux session `phase2_random50_v2`，超参数已确认正确 |
| **Registry** | `phase2_random50_baseline` → DONE/failed；`phase2_random50_v2` → RUNNING |
| **GPU** | cuda:0 已分配 61GB / 98% 利用率（与 seed123 rgds 实验共享 GPU） |

注意：GPU 0 上同时跑了两个实验（random50_v2 PID 219838 + seed123 rgds PID 211830），可能互相争抢显存/算力，影响速度。如果出现 OOM 需要错开。

---
