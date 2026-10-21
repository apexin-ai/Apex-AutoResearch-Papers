# code plan003 annotate bugfix

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan003-annotate-bugfix_20260520T100545_result.json`
- **Structured JSON:** [`cd05b952c251a7694525.json`](../../sessions/cd/cd05b952c251a7694525.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个 bug 全部修复完成，验证通过。

### 修改摘要

**annotate.py**:
| Bug | 修改 |
|-----|------|
| Critical 1 | 三个数据集 `label_field` 从 `"label"` 改为 `"label_name"` |
| Critical 2 | VAST classes: `["Pro","Con","Neutral"]` → `["pro","con","neutral"]`；Civil Comments: `["non-toxic","toxic"]` → `["non_toxic","toxic"]`；few-shot examples 同步更新 |
| Critical 3 | prompt 模板已支持 topic（通过 `__topic__:` 拼接机制），VAST 数据现在有 topic 字段可用 |
| Warning 4 | HumAID: 删除不存在的 `donation_and_volunteering` 类（实际 10 类），few-shot 从 5 条扩到 10 条覆盖所有类 |
| Warning 5 | 默认 sample 从 500 改为 1500 |
| Warning 6 | `parse_label` substring match 加 word boundary 检查；fuzzy threshold 从 0.5/0.6 提到 0.7；`_match_to_class` 加连字符/下划线/空格规范化 |

**data/preprocess.py**:
| Bug | 修改 |
|-----|------|
| Critical 3 | VAST 处理新增 `topic` 字段（取自 CSV 的 `new_topic` 列），已重新生成 JSONL |

---
