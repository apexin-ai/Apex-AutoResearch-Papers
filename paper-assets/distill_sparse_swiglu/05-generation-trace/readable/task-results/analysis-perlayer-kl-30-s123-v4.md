# analysis perlayer kl 30 s123 v4

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perlayer_kl_30_s123_v4_20260521T190820_result.json`
- **Structured JSON:** [`b8157b2c51958a895f53.json`](../../sessions/b8/b8157b2c51958a895f53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

**perlayer_kl_30_s123_v4** 训练正常完成，PPL 评估已出。

### 训练
- 10000 steps 完成，EXIT_CODE=0
- avg_kl=0.0114, model-level sparsity=0.296
- Checkpoint: `checkpoints/perlayer_kl_30_s123/predictor_perlayer_kl.pt`

### PPL (WikiText-2, 30% uniform, TEAL global mask)
**PPL = 9.0598**

### 3-seed 汇总

| Seed | PPL | Gap vs E2E (8.81) |
|------|-----|-------------------|
| s42  | 9.0568 | +0.247 (+2.8%) |
| s123 | **9.0598** | +0.250 (+2.8%) |
| s456 | 9.0282 | +0.218 (+2.5%) |
| **Mean** | **9.0483** | **+0.238 (+2.7%)** |

### 结论: **success** (hypothesis confirmed)

3 个 seed 一致：per-layer KL 训练 PPL 在 9.03~9.06，均显著高于端到端 KL (8.81)。Mean gap = +0.238 (+2.7%)，跨 seed 标准差仅 0.017。Cross-layer gradient coupling 在端到端训练中提供稳定、可复现的 PPL 收益，可作为论文 C1 ablation 的因果证据。

---
