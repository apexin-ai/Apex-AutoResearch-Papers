# code test inference redocred fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_test-inference-redocred-fix_20260521T054226_result.json`
- **Structured JSON:** [`b20d4168401b2f38f6ef.json`](../../sessions/b2/b20d4168401b2f38f6ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

### 改动摘要

**`freige/data/docred_processor.py`** — `SPLIT_FILENAMES` 新增 3 个 Re-DocRED 映射：
- `"train_revised"` → `"train_revised.json"`
- `"dev_revised"` → `"dev_revised.json"`
- `"test_revised"` → `"test_revised.json"`

**`freige/eval/test_inference.py`** — 4 处修改：
1. 新增 `evaluate` 和 `gold_from_docred` import
2. `prepare_test_data()` 新增 `split` 参数（默认 `"test"`，向后兼容）
3. `main()` 新增 `--split` CLI 参数
4. 推理后自动检测 `has_labels`：有 labels 时调用 `evaluate()` 计算 F1/Ign-F1/Evi-F1/EDCR 并打印；无 labels 时走原来的纯预测路径

### Dry-run 结果

- Re-DocRED `test_revised.json`: **500 篇文档**
- 文档 keys: `['title', 'vertexSet', 'labels', 'sents']`
- **有 labels**（首篇文档 11 个标注三元组）
- 所有 import 正常

### 向后兼容

原有 `--split test`（默认值）和 `--data_path /root/autodl-tmp/data/docred` 用法不变。原 DocRED test.json 无 labels，自动走 CodaLab-only 路径。

---
