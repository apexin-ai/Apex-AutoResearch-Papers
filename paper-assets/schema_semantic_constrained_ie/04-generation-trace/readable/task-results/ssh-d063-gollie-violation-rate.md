# ssh d063 gollie violation rate

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d063_gollie_violation_rate_20260519T090427_result.json`
- **Structured JSON:** [`de457f576bd88bab4465.json`](../../sessions/de/de457f576bd88bab4465.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| Metric | GoLLIE-7B | OntoCoDec Unconstrained | OntoCoDec Constrained (S1) |
|--------|-----------|------------------------|---------------------------|
| DR%    | **0.00**  | 15.37                  | 0.93                      |
| RV%    | **0.00**  | 1.39                   | 0                         |
| ET%    | **0.00**  | 0.40                   | 0                         |
| CF%    | **0.67**  | 0.08                   | 9.90                      |

GoLLIE 的 Python dataclass 输出格式充当隐式 schema 约束：类名即类型名，所以 ET/RV 必然为 0%。但代价是极低的抽取覆盖率：100 篇文档仅抽出 300 个实体（ground truth ~1400）和 7 个关系（ground truth ~800），45% 文档输出为空。DR=0% 基于仅 7 个关系样本，统计上不可靠。

报告已写入 `/root/schema_semantic_constrained_ie/d063_gollie_results.md`，artifact 已注册（`art_20260519_46e287`）。

---
