# diagnose perlayer kl k16 s42 v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_perlayer_kl_k16_s42_v2_20260523T040655_result.json`
- **Structured JSON:** [`72e5845bfbd8b852d9fa.json`](../../sessions/72/72e5845bfbd8b852d9fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：`train_perlayer_kl_k4.py:314` 无条件调用 `wandb.init()`，但 westd-34887 上没有配置 wandb API key（无 `.netrc`、无 `~/.config/wandb/`、`.bashrc` 无 `WANDB_API_KEY`）。脚本在初始化阶段就崩溃，未进入训练。

**K=4 为什么没问题**：K=4 训练在 wandb 集成被加入脚本之前完成，K=16 是第一个触发新代码的实验。

**最快修复**：启动命令前加 `WANDB_MODE=disabled`，或在服务器上 `wandb login` 配置 key。

诊断报告已写入 `task_context/diagnose_perlayer_kl_k16_s42_v2.md`。

---
