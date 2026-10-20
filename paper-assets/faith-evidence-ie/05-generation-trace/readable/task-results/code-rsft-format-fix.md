# code rsft format fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rsft-format-fix_20260515T011149_result.json`
- **Structured JSON:** [`53bf02ced4a9e950821f.json`](../../sessions/53/53bf02ced4a9e950821f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个脚本语法验证通过。

## 汇报

### 格式兼容性：无 bug
任务描述中的 bug **在当前代码中不存在**。`rsft_score_filter.py` 已经：
- 输出 JSONL 格式（`rsft_train.jsonl`，每行一个 JSON 对象）
- 字段名与 trainer 一致

### 字段名映射表

| 字段 | generate 输出 | score_filter 输出 | trainer 期望 |
|------|-------------|-----------------|------------|
| 用户输入 | `prompt`（完整 chat template） | `input`（从 prompt 提取 user 内容） | `s["input"]` |
| 模型输出 | `output` | `output` | `s["output"]` |
| CED 分数 | — | `ced_score`（取自 `ced_reward`） | `s.get("ced_score", 1.0)` |
| 文档 ID | `doc_id` | `doc_id` | — |

### 修改内容

| 文件 | 修改 | 原因 |
|------|------|------|
| `rsft_generate.py:51` | `quantize=True` → `quantize=False` | 函数默认值与 argparse 默认值不一致，防止非 CLI 调用时误启用量化 |
| `rsft_score_filter.py:14` | docstring `rsft_train.json` → `rsft_train.jsonl (JSONL)` | docstring 与实际输出格式不符 |

### quantize 默认值检查

| 脚本 | argparse 默认值 | 备注 |
|------|----------------|------|
| `rsft_generate.py` | `False`（`store_true`） | 函数参数默认值已修为 `False` |
| `rsft_trainer.py` | `False`（`store_true`） | 正确 |
| `rsft_score_filter.py` | 无 `--quantize` 参数 | 不涉及模型推理 |

---
