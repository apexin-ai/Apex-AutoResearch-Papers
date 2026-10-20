# code test split support

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_test_split_support_20260516T052513_result.json`
- **Structured JSON:** [`48cc18676fb396d8e27f.json`](../../sessions/48/48cc18676fb396d8e27f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，验证通过。

**变更摘要：**

1. **`prepare_test_data()`** (L147) — 从 test.json 的 vertexSet 直接构建 entity list + prompt，不依赖 labels
2. **`convert_to_codalab()`** (L200) — 模型预测 → CodaLab 提交格式 `[{title, h_idx, t_idx, r, evidence}]`，entity/relation 匹配用 lowercase+strip 容错
3. **`main()` 分支** — `--split test` 时调用 `prepare_test_data`，跳过 `evaluate()`，输出 `codalab_submission.json`

**验证结果：**
- `--help` 正常，`--split {dev,test}` 可选
- `from freige.eval.inference import prepare_test_data, convert_to_codalab` 导入正常
- 备份在 `inference.py.bak`

---
