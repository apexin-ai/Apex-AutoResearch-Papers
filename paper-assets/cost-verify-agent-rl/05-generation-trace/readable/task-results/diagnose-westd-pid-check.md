# diagnose westd pid check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd-pid-check_20260519T145341_result.json`
- **Structured JSON:** [`80fe5f2c27e7d4dcb0a1.json`](../../sessions/80/80fe5f2c27e7d4dcb0a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

tmux 命令被 read_only 白名单拦截，但其余信息已获取。

**SFT 训练进程：**

| 角色 | PID | GPU 显存 |
|------|-----|---------|
| torchrun 主进程 | **120827** | — |
| Worker rank 0 | **120904** | 47004 MiB |
| Worker rank 1 | **120905** | 47232 MiB |
| Worker rank 2 | **120906** | 47232 MiB |
| Worker rank 3 | **120907** | 47040 MiB |

启动脚本：PID **120829**（`bash /root/cost-verify-agent-rl/RAGEN/scripts/run_scienceworld_sft.sh`）

实验：`scienceworld-sft-qwen3-1.7b`，4 GPU FSDP2，Qwen3-1.7B，wandb 已连接（wandb-core PID 123220）。

---
