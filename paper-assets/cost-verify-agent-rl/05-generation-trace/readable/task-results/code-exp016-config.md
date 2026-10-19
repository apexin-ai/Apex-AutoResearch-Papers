# code exp016 config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp016-config_20260514T134552_result.json`
- **Structured JSON:** [`1535c344d1abe4e951ac.json`](../../sessions/15/1535c344d1abe4e951ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。以下是 exp016 审批摘要：

---

### exp016 Pre-flight 结果

| 检查项 | 状态 |
|--------|------|
| Checkpoint `/root/autodl-tmp/checkpoints/exp015/global_step_5/actor/` | 存在（含 model/optim/extra_state 分片） |
| 磁盘 `/root/autodl-tmp` | 184GB 可用 (27%) |
| 配置文件 | `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp016_lr_compromise.yaml` |
| 启动脚本 | `/root/cost-verify-agent-rl/scripts/run_exp016.sh` |
| Dry-run | VALIDATED OK |

### exp016 vs exp015 差异

| 参数 | exp015 | exp016 |
|------|--------|--------|
| `lr` | 1e-7 | **5e-7** |
| `resume_mode` | disable | **resume_path** |
| `resume_from_path` | (无) | **/root/autodl-tmp/checkpoints/exp015/global_step_5** |
| 其余参数 | — | 完全一致 |

### 启动命令

```bash
nohup bash /root/cost-verify-agent-rl/scripts/run_exp016.sh > /root/runs/cost-verify-agent-rl/exp016.log 2>&1 &
```

### ⚠️ 阻塞问题

**exp015 仍在运行**（PID 334705，含 Ray 集群和 WorkerDict workers），未被 kill。两个实验共享 `CUDA_VISIBLE_DEVICES=0,1`，必须先终止 exp015 才能启动 exp016。

等待指令：是否 kill exp015 并启动 exp016？

---
