# analysis qwen14b kl30 s123 eval v4

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b_kl30_s123_eval_v4_20260519T125648_result.json`
- **Structured JSON:** [`d9300656b3c2effb468d.json`](../../sessions/d9/d9300656b3c2effb468d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**s123 eval v4 指标：**
- WikiText-2 PPL = **7.6607**
- ARC-C acc_norm = **0.5606**
- WinoGrande = **0.7293**
- MMLU = **0.6449**
- HellaSwag acc_norm = **0.7132**
- PIQA acc_norm = **0.7535**
- Model sparsity = **0.275**

**三种子对比：**

| Metric | s42 | s456 | s123 | Mean±Std |
|--------|-----|------|------|----------|
| PPL | 7.623 | 7.693 | 7.661 | 7.659±0.029 |
| ARC_norm | 0.572 | 0.532 | 0.561 | 0.555±0.016 |
| WinoGrande | 0.721 | 0.723 | 0.729 | 0.724±0.004 |
| MMLU | 0.637 | 0.641 | 0.645 | 0.641±0.003 |

**结论：**
- MMLU reversal 是 **systematic**——三种子均在 0.637–0.645（std=0.003），非随机波动
- 所有指标跨种子方差极小，训练稳定
- 训练正常完成 1000/1000 steps，checkpoint 在 `checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt`
- 报告已注册：`art_20260519_810a65`

---
