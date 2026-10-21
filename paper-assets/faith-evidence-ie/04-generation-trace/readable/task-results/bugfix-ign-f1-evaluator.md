# bugfix ign f1 evaluator

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_ign_f1_evaluator_20260515T235133_result.json`
- **Structured JSON:** [`813e04a2e1202381d9d9.json`](../../sessions/81/813e04a2e1202381d9d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

### 修复内容
**evaluator.py** (`/root/autodl-tmp/freige/eval/evaluator.py`)：
- `__init__` 新增 `train_facts: set[tuple]` 参数
- `from_train_file` 额外构建 `train_facts`——key 为 `(head, tail, relation)` 不含 `doc_id`
- `compute_f1` 的 Ign 过滤改为 `k[1:] not in self.train_facts`（按事实过滤，而非按文档级 triple 过滤）

### 重算结果（32 个实验）

| 指标 | 结果 |
|------|------|
| train_facts | 34,610 个唯一事实 |
| F1 匹配 | 28/32 完全匹配，4 个低分实验有 < 0.003 偏差 |
| Ign-F1 < F1 | 15/32 实验（过滤生效） |
| 典型 delta | sft_no_evidence: -0.016, rsft 系列: -0.008~-0.010, dpo_ced_1ep_fixed: -0.015 |

所有 `metrics_v2.json` 已保存到各实验目录，原 `metrics.json` 未覆盖。备份在 `evaluator.py.bak`。

---
