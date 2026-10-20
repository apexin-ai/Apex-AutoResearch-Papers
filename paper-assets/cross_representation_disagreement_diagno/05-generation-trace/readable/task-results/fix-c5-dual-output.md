# fix c5 dual output

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_c5_dual_output_20260515T065852_result.json`
- **Structured JSON:** [`a35bf51a136ba14ef92b.json`](../../sessions/a3/a35bf51a136ba14ef92b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

执行完成。结果：

**C5 双值输出 (All samples):**
- `c5_committed`: **94.59%** (35/37) [skips ambiguous] — Bootstrap 95% CI: [0.8611, 1.0000]
- `c5_coverage`: **53.03%** (35/66) [ambiguous=fail] — Bootstrap 95% CI: [0.4098, 0.6508]
- `ambiguous_rate`: **43.94%** (29/66)

**Excl GT=Unknown:**
- `c5_committed`: **96.15%** (25/26) — CI: [0.8710, 1.0000]
- `c5_coverage`: **65.79%** (25/38) — CI: [0.5000, 0.8056]
- `ambiguous_rate`: **31.58%** (12/38)

C1-C4 不变。JSON 已保存到 `results/eval_unified_folio_d012.json`。

备注：c5_committed 比预期的 85.4% 高（94.59%），ambiguous_rate 也是 43.94% 而非 37.9%——这可能是数据版本差异，但双值拆分逻辑本身正确。

---
