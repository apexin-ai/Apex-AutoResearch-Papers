# code llama conll finetune prep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_conll_finetune_prep_20260518T164458_result.json`
- **Structured JSON:** [`95b2e436ff951b4e2d4c.json`](../../sessions/95/95b2e436ff951b4e2d4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已在 cuda:0 上正常运行。

**汇总：**
- 配置：`train_config_llama_conll2003_3ep.yaml`，与 FewNERD 训练完全对齐（LoRA r=32, α=64, lr=2e-4, 3 epochs, batch 2×8）
- 模型：Meta-Llama-3.1-8B-Instruct
- 数据：CoNLL-2003 NER（conll2003_uie_train/dev）
- 总步数：2,634 steps，预估 ~67 分钟（~1.53s/step）
- 输出：`checkpoints/llama3.1-8b-conll2003-lora-3ep`
- Registry：`exp_017_llama_conll_finetune` → RUNNING
- GPU 0 占用 19.9 GB，GPU 1 FewNERD 训练并行运行中

---
