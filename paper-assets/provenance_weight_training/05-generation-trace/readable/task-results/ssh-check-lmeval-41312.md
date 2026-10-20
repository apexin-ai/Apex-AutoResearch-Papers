# ssh check lmeval 41312

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_lmeval_41312_20260517T220202_result.json`
- **Structured JSON:** [`084b98147d78623a4ac1.json`](../../sessions/08/084b98147d78623a4ac1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

| 项目 | 状态 |
|------|------|
| **lm_eval** | 已安装，版本 `0.4.11`，路径 `/root/miniconda3/bin/lm_eval` |
| **adaptive_fix_seed42** | checkpoint 存在，`/root/autodl-tmp/provenance_weight_training/output/models/adaptive_fix_seed42/final/`，含完整模型文件（model.safetensors 1.1GB + tokenizer） |
| **qwen06b_uniform_seed42** | 目录不存在，未找到 trainer_state.json，该模型尚未在此服务器上训练 |

lm-evaluation-harness 已就绪，可直接用 `lm_eval` 命令运行评估。

---
