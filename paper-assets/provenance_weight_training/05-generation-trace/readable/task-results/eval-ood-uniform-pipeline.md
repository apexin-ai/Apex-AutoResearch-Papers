# eval ood uniform pipeline

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_ood_uniform_pipeline_20260519T181309_result.json`
- **Structured JSON:** [`161b0fcf95ac7aed62d9.json`](../../sessions/16/161b0fcf95ac7aed62d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**In-dist PPL 验证通过：**
- seed123: 17.686 (expected 17.686, Δ<0.001) 
- seed456: 17.702 (expected 17.702, Δ<0.001) 

**OOD 结果（3 seeds: 42/123/456）：**

| Dataset | Mean PPL | Std |
|---------|----------|-----|
| OpenWebText | 18.37 | 0.01 |
| Wikipedia | 15.36 | 0.02 |

**Adaptive 训练：** 两个 seed (123/456) 均已完成，checkpoint 保存在 `output/models/adaptive_ood_seed{123,456}/final`。

产出已注册：`uniform_eval_results.md`

---
