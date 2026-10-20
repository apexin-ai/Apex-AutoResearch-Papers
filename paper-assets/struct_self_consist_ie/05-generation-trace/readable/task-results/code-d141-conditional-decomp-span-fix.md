# code d141 conditional decomp span fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d141_conditional_decomp_span_fix_20260518T141657_result.json`
- **Structured JSON:** [`b2ab76f664775fa45f34.json`](../../sessions/b2/b2ab76f664775fa45f34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修复内容和结果：

**修复**: `entity_f1` 从 `(text, type)` 改回 `(start, end, type)` span matching，其他部分（数据源、N=8 截断、gold filter）未改动。

**Span matching 结果要点**:

| Dataset | Favorable Delta | Favorable % | 趋势 |
|---------|----------------|-------------|------|
| SciERC | +0.0252 [0.0034, 0.0476] | 42.9% | LP selection 显著正向 |
| CoNLL | -0.0188 [-0.0293, -0.0085] | 30.5% | LP selection 显著负向 |
| FewNERD | +0.0069 [0.0005, 0.0135] | 47.4% | LP selection 显著正向 |

CoNLL 的 Favorable bucket 在 span matching 下 delta 为负，与 text matching 时表现不同。FewNERD Cond1-only bucket 出现 +0.0274 的强正向增益。

结果已写入 `artifacts/d141_v2_fix/d141_conditional_decomp_span_matching_results.md`。

---
