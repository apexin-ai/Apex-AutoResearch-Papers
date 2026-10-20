# analyze w8 llama docred ft semantic only

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_w8_llama_docred_ft_semantic_only_20260516T165116_result.json`
- **Structured JSON:** [`afbe027ad8f8fa3bc2fc.json`](../../sessions/af/afbe027ad8f8fa3bc2fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## w8_llama_docred_ft_semantic_only 实验结果

| Metric | Value |
|--------|-------|
| **total_samples** | 998 |
| **parse_failures** | 24 |
| **parse_fail_rate** | 2.40% |
| **docs_checked** | 974 |
| **total_entities** | 19,099 |
| **total_relations** | 16,038 |
| | |
| **E_P** | 85.01 |
| **E_R** | 83.06 |
| **E_F1** | 84.02 |
| **R_P** | 38.89 |
| **R_R** | 50.40 |
| **R_F1** | 43.90 |
| | |
| **ET_violations** | 0 |
| **ET_pct** | 0.00% |
| **RV_violations** | 24 |
| **RV_pct** | 0.15% |
| **DR_violations** | 48 |
| **DR_pct** | 0.30% |
| **CF_violations** | 31 |
| **CF_pct** | 0.16% |

### 与参考基线对比

| Metric | grammar_only | semantic_only (本次) | Delta |
|--------|-------------|---------------------|-------|
| E_F1 | 84.04 | 84.02 | -0.02 (持平) |
| R_F1 | 43.77 | 43.90 | +0.13 (持平) |
| ET_pct | 0% | 0% | = |
| RV_pct | 0% | 0.15% | +0.15% |
| DR_pct | 0.51% | 0.30% | **-0.21%** |
| CF_pct | 0.12% | 0.16% | +0.04% |

### 结论

- F1 指标与 grammar_only 基本持平（E_F1≈84, R_F1≈44）
- **DR 从 0.51% 降至 0.30%**，语义约束有效减少了 domain-range 违规（降幅 41%）
- ET 保持 0%（完美）
- RV 有少量 0.15%（24个 relation 名未命中词汇表，可能是模型偶尔生成的非标准名称）
- CF 0.16%，略高于 grammar_only 的 0.12%
- parse_fail_rate 2.40%（24/998），属正常范围

---
