# code bugfix reviewer

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bugfix_reviewer_20260512T102418_result.json`
- **Structured JSON:** [`a5090bf7288a8dcb2817.json`](../../sessions/a5/a5090bf7288a8dcb2817.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成，语法验证通过。修改汇总：

| Bug | 文件 | 修复内容 |
|-----|------|---------|
| **1** | `contrastive_model.py:178-183` | `pos_weights` 从乘 logit 改为对 per-sample loss 加权 |
| **2** | `bounded_dataflow.ql:119-131` | `pathLength` 从中间节点计数改为 call-graph hop distance（same func=0, direct edge=1, else=2） |
| **3** | `train.py:227-236` | `evaluate()` 末尾用 `accelerator.reduce()` 聚合多 GPU 指标 |
| **4** | `build_training_data.py:263-277` | 正样本拼接加 token-budget 截断（按 path_distance 升序，超预算即停），新增 `--max-seq-length` 参数 |

所有修改已同步到 `_project/intermediate/` 副本。

---
