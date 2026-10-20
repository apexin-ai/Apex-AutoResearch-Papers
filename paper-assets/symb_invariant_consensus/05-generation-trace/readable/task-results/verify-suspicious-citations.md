# verify suspicious citations

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_suspicious-citations_20260517T182150_result.json`
- **Structured JSON:** [`32dfcd5f60d108e1aa3f.json`](../../sessions/32/32dfcd5f60d108e1aa3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**3 篇引用全部 VERIFIED，均为真实论文，无虚构引用。**

验证结果已写入 `artifacts/citation_verification.md`。需要注意的问题：

| bib_key | 真实论文 | Venue | 问题 |
|---------|---------|-------|------|
| `diverseaware2025` | Diversity-aware Training for Test-time Scaling (RePrism) | ICLR 2026 (submitted) | **年份错误**: bib key 标 2025，实际是 2026；需确认是否已 accepted |
| `satbench2025` | SATBench: Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas | EMNLP 2025 | 无问题 |
| `llmmeets_cp2025` | Large Language Model Meets Constraint Propagation (GenCP) | IJCAI 2025 | 论文实际关注受约束文本生成，非通用约束求解，建议核实引用上下文 |

---
