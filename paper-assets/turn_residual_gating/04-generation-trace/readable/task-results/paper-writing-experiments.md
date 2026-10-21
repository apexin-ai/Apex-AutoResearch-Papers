# paper writing experiments

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260519T220825_result.json`
- **Structured JSON:** [`26f6ec4a64a9adf0d8a4.json`](../../sessions/26/26f6ec4a64a9adf0d8a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `paper/sections/experiments.tex`。

内容概要:
- **§5.1 Setup**: Qwen-2.5-7B-Instruct, UltraChat 8K, LoRA r=8, 三项损失函数参数 inline, 四路消融配置定义, IID/held-out 两种评估协议
- **§5.2 Main Results**: Table 1 (full-width `table*`, booktabs, 4行×6数据列), 核心叙事 = 三方趋同 (held-out GAR-ours spread 0.75pp, PPL spread 0), Base→fine-tuned 45倍 GAR 提升归因于 LoRA, GAR-Dongre 持续低位, 30× teacher-forced vs autoregressive gap, 因果分析 defer 到 §6
- **§5.3 Cross-Model Validation**: Llama-3.1-8B placeholder, 2 句说明实验进行中

---
