# ssh resume qwen training

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_resume-qwen-training_20260520T213102_result.json`
- **Structured JSON:** [`67045d0a3c1d5ba32fc2.json`](../../sessions/67/67045d0a3c1d5ba32fc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练全部恢复成功。以下是最终状态总结：

---

## 恢复训练总结

| | s123 | s456 |
|---|---|---|
| **Training PID** | 4271 (bash: 4270) | 4561 (bash: 4560) |
| **恢复 checkpoint** | checkpoint-3000 | checkpoint-3000 |
| **GPU** | GPU 0: 98%, 30549/32607 MiB | GPU 3: 98%, 21991/32607 MiB |
| **Monitor PID** | 4871 | 4883 |
| **Exit watcher PID** | 4870 | 4882 |

### 预估完成时间

- 剩余 steps: 6633 - 3000 = **3633**
- 速率: ~23.5 s/step（含 eval 开销）
- 预计剩余: 3633 × 23.5 / 3600 ≈ **23.7 小时**
- 预计完成: **2026-05-22 ~05:30 UTC+8**（约 2026-05-21 21:30 UTC）

### 注意事项

- 使用了 `--no_wandb` 因为服务器 wandb 凭证缺失（原训练的 ~/.netrc 已丢失）
- 训练日志: `~/runs/exec-sim-repair-verifier/qwen_cwm_s{123,456}_resume.log`
- Monitor 每 5 分钟检查一次进程存活，训练完成后自动触发 eval 脚本

---
