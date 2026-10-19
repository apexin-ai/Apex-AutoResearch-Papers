# ops 7b sft eval ood

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_7b-sft-eval-ood_20260519T071452_result.json`
- **Structured JSON:** [`6a0d6c83849c63fbf09d.json`](../../sessions/6a/6a0d6c83849c63fbf09d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动验证完成：

| 项目 | 值 |
|---|---|
| tmux session | `sft_eval_ood` |
| PID | 807986 (主进程) |
| GPU | 2 (16.9GB), 3 (17.4GB) |
| W&B run | `8v6iysv3` |
| W&B URL | wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/8v6iysv3 |
| 日志 | `/root/autodl-tmp/logs/7b_sft_eval_ood.log` |

附加操作：SFT checkpoint 清理了 86GB 训练状态文件（optimizer.bin + pytorch_model_fsdp.bin），磁盘从 100% 降到 66%。`/final` 目录未生成（磁盘满时 save 失败），但 `checkpoint-231/` 中的 safetensors 模型完整可用。

---
