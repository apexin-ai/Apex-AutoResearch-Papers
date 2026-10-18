# ssh q3 val scs confusion correlation

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_q3_val_scs_confusion_correlation_20260517T150710_result.json`
- **Structured JSON:** [`3e40c03cc672bc6dd714.json`](../../sessions/3e/3e40c03cc672bc6dd714.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存到 `/root/schema-dag-extraction/artifacts/q3_val_scs_confusion/q3_val_scs_confusion.json`。

## 结果摘要

| 指标 | Val-only (16 types, 120 pairs) | All-80 (3160 pairs) |
|------|------|------|
| Spearman ρ | **0.2156** | 0.2182 |
| p-value | 0.018 | 2.2e-35 |
| Nonzero subset ρ | 0.5998 (n=11, p=0.051) | 0.1278 (n=272, p=0.035) |

**结论**：Val-only types（与训练数据完全不重叠）的 SCS-confusion 相关性 ρ=0.216, p=0.018，统计显著。相关强度与全集（ρ=0.218）几乎一致，排除了 training-set contamination 的解释。

**Top confused val-only pairs**（均为高 SCS 的语义近邻对）：
1. child ↔ mother: confusion=500, SCS=0.84
2. child ↔ spouse: confusion=100, SCS=0.71
3. member of ↔ part of: confusion=100, SCS=0.90
4. crosses ↔ located in/next to body of water: confusion=75, SCS=0.42
5. mother ↔ spouse: confusion=75, SCS=0.73

---
