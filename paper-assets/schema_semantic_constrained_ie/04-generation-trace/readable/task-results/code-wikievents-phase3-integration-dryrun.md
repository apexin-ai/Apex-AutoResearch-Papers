# code wikievents phase3 integration dryrun

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_phase3_integration_dryrun_20260517T150624_result.json`
- **Structured JSON:** [`6e156a7609b865a9a93d.json`](../../sessions/6e/6e156a7609b865a9a93d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry Run 报告

### 门控条件: **全部 PASS**

| 条件 | 结果 |
|------|------|
| (a) XGrammar 编译 event JSON schema | ✓ PASS |
| (b) Unconstrained violation > 5% | ✓ PASS (EV=15.8%, RoV=83.2%) |
| (c) Constrained F1 drop < 5pp | ✓ PASS (Trigger F1 +13.3pp) |

### 对比结果 (10 docs)

|  | Unconstrained | Constrained (full_s1) |
|--|--------------|----------------------|
| Parse success | 8/10 | 5/10 |
| EV violation | **15.8%** | **0.0%** ↓ |
| RoV violation | 83.2% | 83.3% |
| Trigger F1 | 10.2% | **23.5%** ↑ |
| Argument F1 | 0.0% | 0.0% |

### 代码改动
1. **`compiler/ontology_compiler.py`**: `_build_spec()` 新增 `event_constraints` → `argument_constraints` 格式转换
2. **`violation_checker_wikievents.py`**: `load_constraints()` 同上转换
3. **`run_constrained_extraction.py`**: 新增 `--dataset wikievents` 支持（数据加载、event prompt、event JSON schema 编译、`--max_docs` 别名）

### 已知限制
1. **Semantic layer (Layer 2) 对 EE 失效**: 层级事件类型名共享 first token（如 `ArtifactExistence.*` 全部共享 token 85578），触发 XGrammar assertion error → fallback 到 grammar-only
2. **5/10 parse failure**: max_new_tokens=2048 不够文档级抽取，需增至 4096+
3. **RoV 仍高**: grammar 只约束全局 80 个 role enum，不约束 per-event-type role → 需 trie-based multi-token masking

报告已保存到 `outputs/dryrun_report.md`。

---
