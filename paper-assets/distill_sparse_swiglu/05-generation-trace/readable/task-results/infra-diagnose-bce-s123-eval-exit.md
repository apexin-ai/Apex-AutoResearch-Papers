# infra diagnose bce s123 eval exit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_diagnose_bce_s123_eval_exit_20260517T222033_result.json`
- **Structured JSON:** [`fd2cd5db6958745d0f7b.json`](../../sessions/fd/fd2cd5db6958745d0f7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**bce_isocompute_v3_s123_eval → DONE/success**

| Metric | Value |
|--------|-------|
| WikiText-2 PPL | 28.0627 |
| ARC-Challenge acc_norm | 0.2696 |
| WinoGrande acc | 0.5130 |
| MMLU acc | 0.2655 |
| GSM8K exact_match | 0.0220 |

Registry 已更新，cron 已删除。注意这些 downstream benchmark 分数很低（MMLU ~26.5% 接近随机），与 PPL 28 一致，说明 50% global sparsity BCE predictor (seed 123) 在 LLaMA-3.1-8B 上的 downstream 质量严重退化。

---
