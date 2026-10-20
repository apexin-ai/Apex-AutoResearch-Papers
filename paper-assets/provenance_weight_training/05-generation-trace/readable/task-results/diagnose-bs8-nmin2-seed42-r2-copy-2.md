# diagnose bs8 nmin2 seed42 r2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bs8_nmin2_seed42_r2_20260515T225654_result.json`
- **Structured JSON:** [`45413280b3aa35de0606.json`](../../sessions/45/45413280b3aa35de0606.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

**bs8_nmin2_seed42_r2 验证结果**

| 项目 | 结果 |
|------|------|
| Checkpoint 完整性 | 通过 (model.safetensors 1.11GB, 596M params, 加载正常) |
| Eval PPL (holdout) | **17.73** (loss=2.8752, 4.08M tokens) |
| 训练 | 6103/6103 steps, train_loss=5.4065, 4.1 GPU-hours |
| SIGHUP 根因 | 容器环境无法查 dmesg/journalctl；推测 tmux/SSH 在 W&B finalization 阶段断连，训练本身已完成 |

**对比参考**：baseline Qwen3-0.6B PPL=22.97, ess_only_seed123 PPL=17.72, ess_only_seed456 PPL=17.72。bs8 (batch_size=8, n_min=2) 的 PPL=17.73 与 bs4 adaptive 实验基本持平，batch size 翻倍未带来 PPL 改善。

---
