# ops starcoder chain restart

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_starcoder_chain_restart_20260516T162141_result.json`
- **Structured JSON:** [`d4f97f4b97d1507a3f97.json`](../../sessions/d4/d4f97f4b97d1507a3f97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动。

**总结：**
- Killed watcher (PID 20226) 和误启动的 supplement 进程
- 创建了 `/root/structfuse/scripts/run_starcoder_resume_from_embed_s44.sh`，按原始配置串行跑 4 个 run
- 已通过 `submit_training_job` 提交，tmux session: `m2_full_starcoder_resumed`
- GPU 1 已占用 45.4GB/97.9GB，utilization 100%，embedding_distance_s44 正在训练
- 日志: `/root/runs/structfuse-context/m2_full_starcoder_resumed.log`
- 超时设置 72h，预计 ~36h 完成全部 4 runs

---
