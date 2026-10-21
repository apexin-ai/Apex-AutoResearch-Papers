# diagnose ess only 41312

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_ess_only_41312_20260517T205919_result.json`
- **Structured JSON:** [`3390096f37417be72187.json`](../../sessions/33/3390096f37417be72187.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是结果：

---

## 根因：两个实验被外部 SIGTERM (kill) 终止

两个进程在 2026-05-17T20:55:28-29Z 几乎同时收到 SIGTERM 信号，退出码 143 (128+15)。它们当时运行正常，分别完成了 47% 和 49% 的训练进度（约 5.5 小时）。

**不是 OOM**（cgroup memory.events 显示 oom_kill=0），**不是代码错误**（日志中无 traceback），**不是基础设施故障**（GPU 状态正常）。

**无 W&B 数据的原因**：脚本中设置了 `WANDB_MODE=disabled`，这是配置问题，不是失败导致的。

bash_history 中无 kill 记录，无 journalctl 日志，无 crontab。最可能的来源是某个自动化脚本/agent 发送了 kill 信号（两个进程几乎同一秒被杀）。

---

```json
{"exp_id": "ess_only_seed456_r2", "root_cause": "进程被外部 SIGTERM 终止 (exit_code=143)，在 step 2897/6103 (47%) 时被杀。非 OOM、非代码错误。同时 WANDB_MODE=disabled 导致无 W&B 数据。", "error_type": "infrastructure", "fix_steps": ["1. 确认是什么发送了 SIGTERM（检查其他自动化 agent/脚本）", "2. 移除脚本中的 WANDB_MODE=disabled 或改为 online", "3. 在 tmux session 中重新启动：tmux new -s ess_only_seed456_r2 'bash /root/provenance_weight_training/scripts/run_ess_only_seed456.sh'", "4. 考虑从 checkpoint 恢复（如果 output_dir 中有 checkpoint）"], "can_auto_fix": true}
{"exp_id": "ess_only_seed123_r2", "root_cause": "进程被外部 SIGTERM 终止 (exit_code=143)，在 step 2989/6103 (49%) 时被杀。非 OOM、非代码错误。同时 WANDB_MODE=disabled 导致无 W&B 数据。", "error_type": "infrastructure", "fix_steps": ["1. 确认是什么发送了 SIGTERM（检查其他自动化 agent/脚本）", "2. 移除脚本中的 WANDB_MODE=disabled 或改为 online", "3. 在 tmux session 中重新启动：tmux new -s ess_only_seed123_r2 'bash /root/provenance_weight_training/scripts/run_ess_only_seed123.sh'", "4. 考虑从 checkpoint 恢复（如果 output_dir 中有 checkpoint）"], "can_auto_fix": true}
```

---

### 日志尾部 (关键部分)

**ess_only_seed456_r2** — 最后几行：
```
 47%|████▋     | 2896/6103 [5:21:52<1:52:49,  2.11s/it]
 47%|████▋     | 2897/6103 [5:21:53<1:52:51,  2.11s/it]Terminated
EXIT_CODE=143
```

**ess_only_seed123_r2** — 最后几行：
```
 49%|████▉     | 2988/6103 [5:24:16<1:49:15,  2.10s/it]
 49%|████▉     | 2989/6103 [5:24:18<1:49:12,  2.10s/it]Terminated
EXIT_CODE=143
```

两个实验日志之间均为正常的 weighting metrics 输出（loss、ESS、alpha_eff 等数值合理），训练过程本身没有异常。

---

**当前 GPU 状态**：GPU 0 和 GPU 3 上分别在跑 `random_reweight_seed456` 和 `qwen06b_uniform_seed42_v2`。GPU 1 和 GPU 2 空闲，可立即重启被杀的实验。

---
