# code prepare exp016

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-exp016_20260514T134532_result.json`
- **Structured JSON:** [`5668f7da230b54891c6a.json`](../../sessions/56/5668f7da230b54891c6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有关键参数验证通过。

---

## exp016 准备报告

### 配置文件
- `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp016_lr_compromise.yaml`

### Checkpoint 确认
- 路径: `/root/autodl-tmp/checkpoints/exp015/global_step_5/`
- 大小: **21GB**（含 actor/ 子目录）

### Dry-run 关键参数验证
| 参数 | 值 | 状态 |
|------|-----|------|
| actor LR | **5.0e-07** | OK |
| kl_loss_coef | 0.1 | OK |
| grad_clip | 1.0 | OK |
| resume_mode | resume_path | OK |
| resume_from_path | /root/autodl-tmp/checkpoints/exp015/global_step_5 | OK |
| experiment_name | exp016-alfworld-lr-compromise | OK |
| local_log_dir | /root/autodl-tmp/checkpoints/exp016/ | OK |
| format_penalty | 0 | OK |

### 磁盘空间
- `/root/autodl-tmp`: **184GB 可用**（250GB 总量，27% 使用）— 充足

### 启动命令
```bash
nohup bash /root/cost-verify-agent-rl/scripts/run_exp016.sh > /root/runs/cost-verify-agent-rl/exp016.log 2>&1 &
```

等待审批启动。

---
