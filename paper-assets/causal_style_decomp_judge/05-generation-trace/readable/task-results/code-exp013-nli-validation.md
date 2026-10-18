# code exp013 nli validation

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp013_nli_validation_20260521T004916_result.json`
- **Structured JSON:** [`acbd8093a4ba69d90d66.json`](../../sessions/ac/acbd8093a4ba69d90d66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-013 完成。

**结果汇总：**

| 指标 | 值 |
|------|-----|
| Cohen's kappa | **0.4304** (< 0.6, negative) |
| Agreement rate | 91/100 (91%) |
| FPR (NLI pass but LLM NO) | 1/88 (1.1%) |
| FNR (NLI fail but LLM YES) | 8/12 (66.7%) |

**Confusion Matrix:**
```
                     LLM=YES  LLM=NO
NLI pass (>=0.90)      87       1
NLI fail (<0.90)         8       4
```

**解读：** kappa 低不是因为 NLI gate 不可靠，而是因为它过于保守。NLI gate precision 极高（仅 1 例 false pass），但 recall 很低——12 条 NLI fail 中有 8 条 LLM 认为内容实际上是保持的。这意味着 NLI gate 以丢弃有效 pair 为代价保障了数据质量。在论文中这可以 frame 为：NLI gate 是 precision-oriented 的 conservative filter，对下游分析的可靠性提供了强保障。

---
