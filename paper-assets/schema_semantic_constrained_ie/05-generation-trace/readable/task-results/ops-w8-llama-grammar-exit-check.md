# ops w8 llama grammar exit check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_w8_llama_grammar_exit_check_20260516T122843_result.json`
- **Structured JSON:** [`b4706216dd528cb30ba1.json`](../../sessions/b4/b4706216dd528cb30ba1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron job（可能在之前的 session 中已清除或未在本 session 创建）。Registry 已更新完毕。

## 总结

**w8_llama_docred_ft_grammar_only** — 成功完成，998/998 样本。

| 指标 | 值 |
|------|-----|
| E-F1 | 84.04% |
| R-F1 | 43.77% |
| ET% | **0.00%** |
| RV% | **0.00%** |
| DR% | 0.51% |
| CF% | 0.12% |
| parse_fail | 2.3% (23/998) |

**结论**：Grammar 层在 FT 模型上完全消除了 ET 和 RV 违规（从 unconstrained 的非零降到 0%），但 DR 残留 0.51% 未被 grammar 层解决（符合预期——domain-range 属于 semantic 层约束）。CF 0.12% 也未被 grammar 层处理。这说明在 FT regime 下，grammar 层仍有价值（消除残余 ET/RV），而 semantic 层对 DR 仍是必要的。

---
