# code tost sensitivity 5model

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tost_sensitivity_5model_20260520T194838_result.json`
- **Structured JSON:** [`1b2a00570c661ca62c3d.json`](../../sessions/1b/1b2a00570c661ca62c3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已执行完成，从 judgment 文件验证的 per-type rates 与提供的数据完全一致（scopal 的 N=249 是数据本身少一条）。

结果：
- `tost_sensitivity_5model.json` 已输出到 `artifacts/full_study/analysis/`
- 15 对 type pair 中，±5pp 等价 0 对，±10pp 3 对，±15pp 8 对，±20pp 12 对
- 3 对在 ±20pp 仍不等价：conditional_precedence–incompleteness (diff=16.8pp)、coreferential–incompleteness (diff=22.0pp)、incompleteness–scopal (diff=14.2pp)——都涉及 incompleteness（最高 53.6%）与低端 type 的对比

---
