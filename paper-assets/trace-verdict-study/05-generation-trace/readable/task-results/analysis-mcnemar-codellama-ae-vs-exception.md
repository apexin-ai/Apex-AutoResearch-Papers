# analysis mcnemar codellama ae vs exception

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mcnemar_codellama_ae_vs_exception_20260519T172812_result.json`
- **Structured JSON:** [`3cdb58f23d57213dbbfe.json`](../../sessions/3c/3cdb58f23d57213dbbfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## McNemar 配对检验结果

**列联表（n=1190）：**

|  | exception_only 对 | exception_only 错 |
|---|---|---|
| **ae_only 对** | a = 1177 | b = 2 |
| **ae_only 错** | c = 11 | d = 0 |

**准确率：**
- ae_only: 99.08% (1179/1190)
- exception_only: 99.83% (1188/1190)

**检验：**
- 方法：McNemar exact binomial test（b+c=13 < 25，用精确检验）
- 不一致对：b=2, c=11（exception_only 纠正了 ae_only 的 11 个错误，仅引入 2 个新错误）
- **p = 0.0225**

**结论：** p < 0.05，差异**统计显著**。exception_only (99.83%) 显著优于 ae_only (99.08%)。

---
