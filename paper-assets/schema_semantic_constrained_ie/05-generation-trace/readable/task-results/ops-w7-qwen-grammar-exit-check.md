# ops w7 qwen grammar exit check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_w7_qwen_grammar_exit_check_20260516T063347_result.json`
- **Structured JSON:** [`32591d93186634ec133e.json`](../../sessions/32/32591d93186634ec133e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All results in. Here's the report:

---

## w7_qwen_scierc_ft_grammar_only — 结果报告

**状态**: SUCCESS (进程已退出，551/551 samples 全部完成)

**输出文件**: `/root/schema_semantic_constrained_ie/outputs/w7_qwen_scierc_ft_grammar_only.jsonl` (998KB, 2026-05-16 14:33)

**注意**: 无 exit sentinel 文件 (`/tmp/agent-ml-exit/` 中无 w7 条目)，但输出完整。

### Violation Metrics

| Metric | Value |
|--------|-------|
| Entity Type (ET%) | **0.0%** (0/1784) |
| Relation Vocab (RV%) | **0.0%** (0/1128) |
| Domain/Range (DR%) | **1.9%** (22/1128) |
| Cross-Field (CF%) | **0.0%** (0) |
| JSON parse failures | 0.0% |

### F1 Metrics (violation_checker)

| Metric | P | R | F1 |
|--------|---|---|-----|
| Entity F1 | 0.6523 | 0.6898 | **0.6705** |
| Relation F1 | 0.4087 | 0.4733 | **0.4386** |

### F1 Metrics (unified_f1_eval, method_all_set)

| Metric | P | R | F1 |
|--------|---|---|-----|
| Entity F1 | 0.5848 | 0.6031 | **0.5938** |
| Relation F1 | 0.0699 | 0.1002 | **0.0824** |

### 结论

**SUCCESS** — grammar_only constrained decoding 在 fine-tuned Qwen3-8B 上完整运行。ET/RV/CF 全部为 0（grammar 层完全消除了类型和词汇违规），仅残留 1.9% DR 违规（grammar 层不约束 domain/range，这是 semantic layer 的职责）。Entity F1=0.67, Relation F1=0.44（violation_checker 口径）。

---
