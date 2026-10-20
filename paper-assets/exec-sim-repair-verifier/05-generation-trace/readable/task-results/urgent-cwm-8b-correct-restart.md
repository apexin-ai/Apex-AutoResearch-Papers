# urgent cwm 8b correct restart

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_cwm-8b-correct-restart_20260514T143053_result.json`
- **Structured JSON:** [`1185f800c32515f5aed1.json`](../../sessions/11/1185f800c32515f5aed1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CWM 8B 已正常运行，无需干预。汇总：

**状态：已在正确运行**
- 脚本：`train_repo_cwm.py`（正确，不是 train_repo_verifier.py）
- GPU 2：98% 利用率，21199 MiB
- 进度：从 checkpoint-1200 恢复，已到 step 1201/6633
- 参数全部正确：`--save_total_limit 20`, `--dataloader_num_workers 0`, `--resume_from_checkpoint checkpoint-1200`
- tmux session：`repo_cwm_8b_restart`
- PID：245775

**发现时的情况**：CWM 8B 已经被另一个 Worker 用正确脚本启动（tmux session 22:28:20 创建），只是在做 70K 样本 preprocessing + 模型加载，所以 GPU 2 暂时显示 0 MiB。没有需要杀掉的错误进程。

**注意**：GPU 3 掉到 0 MiB / 0%——CLS 8B s123 似乎已停止运行，不是我操作导致的，但需要关注。

---
