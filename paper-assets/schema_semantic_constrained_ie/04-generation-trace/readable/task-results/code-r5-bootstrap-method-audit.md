# code r5 bootstrap method audit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r5_bootstrap_method_audit_20260517T141145_result.json`
- **Structured JSON:** [`cd38de0bb5ea9a5cafbf.json`](../../sessions/cd/cd38de0bb5ea9a5cafbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**审计结论：所有 bootstrap 脚本已使用 corpus micro-F1，无需修改。**

三个脚本 (`compute_bootstrap_ci.py`, `compute_bootstrap_ci_ft.py`, `compute_bootstrap_ci_llama.py`) 均采用相同逻辑：bootstrap resample 后对 TP/gold/pred 全局求和再算 F1（即 micro-F1），与主表计算方式一致。ZS 和 FT 的所有 p-value 和 CI 均无需更新。

报告已注册：`r5_bootstrap_method_audit`。

---
