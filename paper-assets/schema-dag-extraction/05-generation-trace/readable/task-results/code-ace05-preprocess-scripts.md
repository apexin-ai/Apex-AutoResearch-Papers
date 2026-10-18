# code ace05 preprocess scripts

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ace05-preprocess-scripts_20260515T030622_result.json`
- **Structured JSON:** [`a3c96775124578cef56f.json`](../../sessions/a3/a3c96775124578cef56f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个文件全部完成，已注册到 exp-004：

| 文件 | 路径 | 说明 |
|------|------|------|
| `ace05_entity_types.json` | `configs/` | 7 个 entity type，`{name: description}` 格式 |
| `ace05_relation_types.json` | `configs/` | 18 个 relation subtype，含 `MAJOR:Subtype` 前缀 |
| `preprocess_ace05.py` | `src/` | DyGIE++ / PURE → parquet，支持 `--mode ner/re` |
| `compute_type_embeddings.py` | `src/` | 通用 type embedding 脚本，Qwen3 mean-pool，输出 `{name: tensor}` dict |

关键设计决策：
- type JSON 格式与 `few_nerd_types.json` 完全一致（`name → description` dict）
- `compute_type_embeddings.py` 输出 dict 而非 stacked tensor，key 是 type name，兼容 Few-NERD 和 ACE05
- `preprocess_ace05.py` 输出 parquet schema 与现有 pipeline 对齐：`text` + `entities[{text, type}]` + 可选 `relations[{head, tail, type}]`
- 所有路径通过 argparse 参数化，LDC 数据到位后直接可用

---
