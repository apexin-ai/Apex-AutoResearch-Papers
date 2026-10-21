# code qwen3 traj repo train prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen3-traj-repo-train-prep_20260518T183507_result.json`
- **Structured JSON:** [`501f1b03cd6abad06cdb.json`](../../sessions/50/501f1b03cd6abad06cdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

配置已写入 `artifacts/qwen3_traj_repo_launch_config.md`。

关键发现：
- **Qwen3-4B 不在服务器上**，只有 Qwen3-8B 和 Qwen3-32B。命令已改用 Qwen3-8B。
- 训练数据在 `data/swebench_full/traj_train.jsonl`（386 条 SWE-bench repo-level diffs）
- 超参复用 DeepSeek TRAJ repo_8k 的实测配置：batch=1, grad_accum=8, seq=8192, epochs=3, lr=2e-4
- 预计训练 ~45-51 分钟，eval ~2-3 分钟
- Qwen3 的 thinking mode 已被训练脚本的 `detect_thinking_support()` 自动处理，不需要额外操作
- GPU 3 当前还在跑 CWM eval（99% utilization），释放后可直接启动

---
