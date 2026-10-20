# train exp 002 conll2003 finetune

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_exp_002_conll2003_finetune_20260514T114540_result.json`
- **Structured JSON:** [`a9d139db0e80f1ddccb0.json`](../../sessions/a9/a9d139db0e80f1ddccb0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动，正在加载数据集。

**完成摘要：**

| 步骤 | 状态 |
|------|------|
| conll2003 dev LLaMA Factory 数据生成（3250 条） | ✓ |
| dataset_info.json 添加 `conll2003_uie_dev` | ✓ |
| `train_config_conll2003.yaml` 创建（LoRA r=32, α=64, bs=2, grad_accum=8, 5 epochs, enable_thinking=false） | ✓ |
| `export_config_conll2003.yaml` 创建（合并到 qwen3-8b-conll2003-merged） | ✓ |
| Dry-run 2 步验证通过（loss 0.89→0.28, 无 OOM） | ✓ |
| 训练提交 `exp_002_ner_conll2003`，tmux session 运行中，cuda:1 | ✓ |

训练完成后需用 `llamafactory-cli export export_config_conll2003.yaml` 合并 LoRA adapter。

---
