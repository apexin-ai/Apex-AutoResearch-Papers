# ops verbosity nli only gate

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verbosity_nli_only_gate_20260520T214344_result.json`
- **Structured JSON:** [`1219b7bd21f1fb471083.json`](../../sessions/12/1219b7bd21f1fb471083.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D013 NLI-only gate content verification 完成。

### 结果

| 指标 | 值 |
|------|-----|
| **Total** | 100 |
| **Passed CF** | **86/100 (86.0%)** |
| **Passed DR** | 43/100 (43.0%) |

**按方向分布：**

| Direction | n | Passed CF | NLI mean | BERTScore mean |
|-----------|---|-----------|----------|----------------|
| **forward** (compression, verbose→concise) | 46 | 44/46 (95.7%) | 0.9476 | 0.8449 |
| **backward** (expansion, concise→verbose) | 54 | 42/54 (77.8%) | 0.8267 | 0.6732 |

**产出文件：**
- `data/verified_verbosity.jsonl` — 100 records, 369K
- `data/verified_verbosity_filtered.jsonl` — 86 records (passed_cf=True), 320K

后续 scoring 步骤可用 n=86。expansion 方向通过率偏低 (77.8%)，compression 方向几乎全通过 (95.7%)，符合预期（expansion 增加内容更易引入非蕴含信息）。

---
