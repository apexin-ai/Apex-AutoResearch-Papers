# code w10 type consensus impl

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w10_type_consensus_impl_20260517T050801_result.json`
- **Structured JSON:** [`71987f13a91c219649ce.json`](../../sessions/71/71987f13a91c219649ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

551 samples confirmed. Here's the summary:

---

## Step 1-4 完成

### 代码结构分析
- `TypeConstraintProcessor.__call__` 每步 decode generated text → `PositionDetector.detect()` 判断当前在 entity_type / head_type / tail_type 位置 → 应用 domain/range mask
- `EntityRegistry` 已经追踪 `{text: type}` 从 entities section，但当 D/R constraint 与 registry 冲突时，原版 processor 不强制 registry type → CF violation 产生

### 实现
新建 `/root/schema_semantic_constrained_ie/compiler/type_consensus_processor.py` (Layer 3):
- 维护 `ConsensusRegistry`，从 entities section + 已完成的 relation 字段收集 `{text: first_type}`
- 在 head_type/tail_type 生成位置，如果 entity text 已在 registry 中，**无条件**强制该 type（即使 Layer 2 已经 mask 掉了它，也恢复 logit 到 0.0）
- 对 `run_constrained_extraction.py` 最小化修改：加 `--type_consensus` flag，在 `run_single_pass` 的 processors 列表末尾追加

### Dry-run 结果 (10 docs)
| 指标 | Before (v1) | After (v2) |
|------|------------|------------|
| Success rate | 10/10 | 10/10 |
| JSON valid | 100% | 100% |
| CF violations | 4 (7.69%) | **0 (0.00%)** |
| Relations corrected | - | 6 |

被修正的典型案例：`"MET"` 在 entities 中标为 `OtherScientificTerm`，但 D/R constraint 允许 `Generic` 作为 `Hyponym-of` 的 tail → Layer 2 选了 `Generic` → Layer 3 强制回 `OtherScientificTerm`。

### Full eval 命令（551 docs，未启动）

```bash
cd /root/schema_semantic_constrained_ie && source /root/miniconda3/bin/activate && \
python run_constrained_extraction.py \
  --mode full_s1 \
  --dataset scierc \
  --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B \
  --data_path data/processed_data/test.json \
  --constraints_path ontology_constraints.json \
  --output_path outputs/scierc_full_s1_consensus_551.jsonl \
  --type_consensus \
  --device cuda:0
```

预计耗时 ~35min（3.6s/sample × 551 samples）。

---
