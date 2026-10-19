# submit kcurve batch1 k2 seeds

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_kcurve_batch1_k2_seeds_20260523T075228_result.json`
- **Structured JSON:** [`7dd71543725e913b5826.json`](../../sessions/7d/7dd71543725e913b5826.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| `perlayer_kl_k2_s123` | cuda:0 (100%, 35981 MiB) | 123969 | RUNNING, Step 1已输出 |
| `perlayer_kl_k2_s456` | cuda:1 (96%, 34857 MiB) | 124297 | RUNNING, Step 1已输出 |

两个训练都正常启动：模型加载完成，predictor参数75.9M，K=2 per-layer masking，gradient checkpointing启用，~2.3s/step。Registry已推进到RUNNING，cron监控已注册（120s间隔）。预计约40分钟完成1000步。

---
