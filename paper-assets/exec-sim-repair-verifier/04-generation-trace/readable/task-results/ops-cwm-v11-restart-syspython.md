# ops cwm v11 restart syspython

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cwm-v11-restart-syspython_20260513T111450_result.json`
- **Structured JSON:** [`873e07ff8087dbe00f9f.json`](../../sessions/87/873e07ff8087dbe00f9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终汇总

| 项目 | 值 |
|------|-----|
| **新 PID** | 145692（Python 进程），145691（bash wrapper） |
| **恢复起始 step** | 从 checkpoint-500 恢复，实际训练从 step 501 开始 |
| **训练速度** | ~8.9s/step（steps 503-511 平均），符合预期 8-9s/step |
| **cuda:2 显存** | 16295 MiB（已占用） |
| **系统 Python** | /usr/bin/python3 Python 3.10.12 |
| **transformers** | 5.8.0（系统 pip） |
| **日志文件** | /tmp/cwm_v11_restart.log |

**注意**：首次尝试 `--resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_v11/` 失败（`trainer_state.json` 不在 output_dir 根目录），改为指定 `checkpoint-500` 子目录后成功。

---
