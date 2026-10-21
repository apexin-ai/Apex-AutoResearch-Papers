# diagnose interv pred 14b s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_interv_pred_14b_s42_fp32_20260520T054221_result.json`
- **Structured JSON:** [`7129669bdcb7ad2d39ee.json`](../../sessions/71/7129669bdcb7ad2d39ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**`interv_pred_14b_s42_fp32` — 成功 (DONE/success)**

| 指标 | Gen 0 (baseline) | Gen 1 (trigger) | Gen 2 (recovery) | Gen 10 (final) |
|------|----------|---------|----------|--------|
| token_entropy | 2.946 | **1.418** (↓51.9%) | 2.892 | 2.832 |
| perplexity | 19.68 | 65.37 | 17.44 | 17.60 |
| ECE | 0.007 | 0.281 | 0.017 | 0.026 |
| effective_rank | 50.76 | 90.17 | 58.29 | 51.53 |

- Intervention 在 gen_1 触发（token_entropy 下降 51.9%，远超 15% 阈值），gen_2 起 α=0.0
- Gen_2 即完成恢复，gen_2-10 所有指标稳定
- **与 410M 实验模式完全一致**：gen_1 触发 → gen_2 恢复 → 稳定至 gen_10，验证 Claim 4（scale-independence）
- Registry 已更新为 DONE/success，cron 已删除

---
