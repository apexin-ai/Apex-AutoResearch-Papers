# analysis perlayer kl k8 s42 eval check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perlayer_kl_k8_s42_eval_check_20260523T044816_result.json`
- **Structured JSON:** [`46902c06386d713fa156.json`](../../sessions/46/46902c06386d713fa156.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**K=8 eval 结果（perlayer_kl_k8_s42_eval → DONE/success）：**

| Metric | Value |
|--------|-------|
| wikitext2 PPL | 8.9704 |
| ARC-C acc_norm | 0.4104 |
| WinoGrande acc | 0.6740 |
| MMLU acc | 0.3980 |
| GSM8K exact_match | 0.0561 |
| HellaSwag acc_norm | 0.6919 |
| PIQA acc_norm | 0.7612 |

**K=2 训练已提交（perlayer_kl_k2_s42_train → RUNNING）：**
- 服务器：westd-34887 cuda:1
- PID：112468
- 1000 steps, save_every=500, gradient_checkpointing
- Cron 监控已注册（120s 间隔）

---
