# eval llama rsft no evi result

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_llama-rsft-no-evi-result_20260522T235610_result.json`
- **Structured JSON:** [`6ea23dbd7dffc4cc770e.json`](../../sessions/6e/6ea23dbd7dffc4cc770e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已被删除或在其他 session 创建）。Registry 已更新完毕。

## LLaMA RSFT no-evi test 结果

状态: **success**

| 指标 | 值 |
|------|-----|
| **ign_f1** | **0.3334** |
| f1 | 0.3334 |
| precision | 0.4549 |
| recall | 0.2632 |
| n_truncated | 269/500 |
| format_ok_rate | 99.8% |

**RSFT test evidence tax**: no_evi(0.3334) - with_evi(0.3599) = **-2.65pp**

负值 = 去掉 evidence 后性能下降，evidence 对 RSFT 有收益。与 dev 方向一致（dev tax = -2.17pp），test 上 evidence 收益更大。

---
