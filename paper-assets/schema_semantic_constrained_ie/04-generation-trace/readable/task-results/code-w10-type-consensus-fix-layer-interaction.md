# code w10 type consensus fix layer interaction

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w10_type_consensus_fix_layer_interaction_20260517T052744_result.json`
- **Structured JSON:** [`d7ca027c2f99fa4a17d4.json`](../../sessions/d7/d7ca027c2f99fa4a17d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。3 个 CF violations 正好对应 skip 日志中的 3 个 entity（MET, Japanese character strings, image information），这些都是因为 consensus type 不在 DR allowed set 中被正确 skip 的。

**结果总结**：
- DR violations: **0.0%**（远优于 baseline 0.93%）✓
- CF violations: **3 个**（都是 DR-conflict skip 导致的，设计预期内）
- JSON valid: **100%** ✓

---

READY FOR FULL EVAL

551-doc 完整评估命令：

```bash
cd /root/schema_semantic_constrained_ie && source /root/miniconda3/bin/activate && \
python run_constrained_extraction.py \
  --mode full_s1 --dataset scierc \
  --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B \
  --data_path data/processed_data/test.json \
  --constraints_path ontology_constraints.json \
  --output_path outputs/scierc_full_s1_consensus_v2.jsonl \
  --type_consensus --device cuda:0
```

评估后跑 violation checker：
```bash
python violation_checker.py \
  --input_path outputs/scierc_full_s1_consensus_v2.jsonl \
  --constraints_path ontology_constraints.json \
  --output_path outputs/violation_report_scierc_full_s1_consensus_v2.json
```

---

**修复核心逻辑**：在 `type_consensus_processor.py` 的 `__call__` 中，force consensus 前通过 `spec.get_constraint(relation_type)` 查询 DR validity。如果 `consensus_type ∉ allowed_types`，跳过 force 并记录 warning。方案 C 实现，只改了 GTC processor 一个文件，未修改 Layer 2。

---
