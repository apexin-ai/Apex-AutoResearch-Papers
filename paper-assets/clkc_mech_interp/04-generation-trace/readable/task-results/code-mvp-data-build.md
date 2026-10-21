# code mvp data build

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_data_build_20260521T120253_result.json`
- **Structured JSON:** [`21f23d58a17e11ab9ac6.json`](../../sessions/21/21f23d58a17e11ab9ac6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。最终产出：

**`data/` 目录**：
| 文件 | 行数 | 说明 |
|------|------|------|
| `en_conflict_train.jsonl` | 800 | 400 conflict + 400 no_conflict |
| `en_conflict_test.jsonl` | 200 | 100 conflict + 100 no_conflict |
| `raw_sampled_train.jsonl` | 400 | 原始 ConflictQA 采样数据 |
| `raw_sampled_test.jsonl` | 100 | 原始 ConflictQA 采样数据 |
| `DATA_README.md` | 数据文档 |

**`src/` 目录**：
| 文件 | 说明 |
|------|------|
| `translate_to_zh.py` | ZH 翻译脚本，使用 Qwen3-8B，需 GPU 服务器运行 |

**标签设计**：二分类——`conflict`（context 与参数知识矛盾，使用 `counter_memory_aligned_evidence`）vs `no_conflict`（context 与参数知识一致，使用 `parametric_memory_aligned_evidence`）。数据来源为 ConflictQA 的 `popQA-chatgpt` 子集，seed=42 采样 500 条原始样本。

---
