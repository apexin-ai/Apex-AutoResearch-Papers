# prep d029 benchmark batch

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_d029_benchmark_batch_20260516T040547_result.json`
- **Structured JSON:** [`a4ae221ddf9fdcb6a671.json`](../../sessions/a4/a4ae221ddf9fdcb6a671.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已写入并注册。汇总：

**当前状态：** 0 个 benchmark_eval 结果完成。cuda:0 跑 d030_kl30_uniform，cuda:1 跑 lm_eval_mistral（0-shot 旧脚本，需用 benchmark_eval 重跑）。

**剩余 11 条命令：**
- **cuda:1（5 条，先空出）：** Mistral KL 50% → Mistral Dense → KL 50% → KL 30% → KL 70%
- **cuda:0（6 条，d030 后）：** Dense baseline → TEAL 50% → TEAL 30% → WINA 50% → STE 50% → BCE iso-compute 50%

**排除：** SPON（benchmark_eval.py 不支持）、多种子（D029 只跑 s42）、d030_kl30_uniform（属 D030）。

**预估总时长：** ~4.5h（双 GPU 并行）。

---
