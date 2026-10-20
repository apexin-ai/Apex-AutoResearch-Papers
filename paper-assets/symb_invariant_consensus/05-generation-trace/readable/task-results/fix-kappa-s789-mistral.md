# fix kappa s789 mistral

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kappa-s789-mistral_20260522T225503_result.json`
- **Structured JSON:** [`3b4b7e5aeb091e0d8451.json`](../../sessions/3b/3b4b7e5aeb091e0d8451.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功（27 pages, 无错误）。

**修改前后对比：**

| 字段 | 修改前（错误） | 修改后（正确） |
|------|---------------|---------------|
| κ | 0.41 | 0.45 |
| K_eff | 2.17 | 2.03 |
| SC | 54.41% | 59.31% |
| Δ | −0.49 | −2.45 |

**错因：** s789 行的全部四个值都是错的。κ=0.41 / K_eff=2.17 与 cross-model 表中 LLaMA-3.1-8B 行完全一致（L740），SC=54.41 则与 s123 行相同——是 copy-paste 错误。正确值通过 `compute_fleiss_kappa_unified.py` 在 `mistral_folio_seed789` traces 上重算验证。

**Cross-model 表（L735-745）** 无 s789 引用，不需要修改。

---
