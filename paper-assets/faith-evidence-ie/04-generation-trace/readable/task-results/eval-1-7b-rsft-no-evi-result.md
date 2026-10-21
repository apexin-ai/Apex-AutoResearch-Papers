# eval 1 7b rsft no evi result

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_1_7b-rsft-no-evi-result_20260522T225801_result.json`
- **Structured JSON:** [`af2a62ecc2fb62588479.json`](../../sessions/af/af2a62ecc2fb62588479.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已被删除或未在本 session 创建），跳过。

## 1.7B RSFT no-evi test 结果

状态: **success**

| 指标 | 值 |
|------|-----|
| **ign_f1** | **0.2390** |
| f1 | 0.2390 |
| precision | 0.4294 |
| recall | 0.1655 |
| format_ok_rate | 97.4% |
| n_truncated | 474/500 |

**RSFT test evidence tax**: with_evi(0.2933) - no_evi(0.2390) = **+5.43pp**

去掉 evidence 后 ign_f1 下降 5.43pp，说明 evidence 对 RSFT 1.7B 有显著正面作用（与 SFT test tax -4.31pp 方向一致：evidence helps）。

---
