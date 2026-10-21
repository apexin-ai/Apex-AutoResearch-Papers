# audit data tables2 3 fig1 inline

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data-tables2-3-fig1-inline_20260522T035507_result.json`
- **Structured JSON:** [`7b0c009f1872aa7b52f1.json`](../../sessions/7b/7b0c009f1872aa7b52f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。66 个数字已核查，结果：

- **62 ✅** — 与源数据一致
- **2 ⚠️** — 微小舍入差异：Gemma-2 DiD (+0.545→+0.6, 严格应为+0.5)；Qwen-7B GSM8K (+10.1pp vs 源数据+11.07pp, ~1pp差)
- **2 ❌** — §5.6 MinK++ Cohen's d (−1.55, −1.98) 在已定位的源文件中找不到对应数据，`exp008_v4_results.json` 中的 −1.2203 不匹配

需要关注的 3 个 action items 写在报告末尾。已注册为 artifact `art_20260522_8b1150`。

---
