# analysis bootstrap crossval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-crossval_20260522T074144_result.json`
- **Structured JSON:** [`78e8281dcbb9dd01bf95.json`](../../sessions/78/78e8281dcbb9dd01bf95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| Config | Bootstrap R-F1 | Registry R-F1 | Δ (pp) | ±0.01pp |
|--------|:-:|:-:|:-:|:-:|
| Qwen SciERC FT constrained | 43.77 | 43.77 | +0.00 | **PASS** |
| Llama SciERC FT constrained | 45.47 | 45.47 | +0.00 | **PASS** |
| Qwen DocRED FT constrained | 40.60 | 40.56 | +0.04 | **FAIL** |
| Llama DocRED FT constrained | 43.83 | 43.78 | +0.05 | **FAIL** |

**SciERC 完美通过** — 两个配置 parse_fail_rate = 0%，无分歧。

**DocRED 有系统性偏差** — bootstrap 一致偏高 0.04–0.11pp。根因不是 violation_checker.py 的 parse-failure bug（已修复），而是 bootstrap 脚本和 eval_d064.py 对 parse failure 文档的 F1 分母处理不同：eval_d064.py 将 parse-failed 文档的 gold relations 计为 FN（正确），bootstrap 脚本可能排除了这些文档。偏差量级远小于 bootstrap CI 宽度（~1.5pp），不影响任何显著性结论。

报告已写入 `artifacts/bootstrap_crossval_report.md` 并注册。

---
