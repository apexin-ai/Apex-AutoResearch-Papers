# code fix format parsing

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-format-parsing_20260515T000205_result.json`
- **Structured JSON:** [`6df61d2370757568aa63.json`](../../sessions/6d/6df61d2370757568aa63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件语法检查全部通过。

### 修改总结

**文件 1: `freige/eval/evaluator.py`**
- `_triple_key()`: relation 字段加了 `.lower().strip()`，解决关系名大小写不匹配
- 新增 `_get_field(d, *keys)` 辅助函数，按优先级取字段
- `_normalize_triples()`: 字段名容忍 `head`/`head_entity`, `tail`/`tail_entity`, `relation`/`type`/`label`, `evidence`/`sentence_ids`；relation 值统一 lowercase+strip

**文件 2: `freige/training/grpo_trainer.py`**
- `format_reward_fn()`: 同样接受变体字段名，不再严格要求 `head`+`tail`+`relation`+`evidence`

**文件 3: `freige/training/rsft_generate.py`**
- `generate_batch()`: 新增返回截断标志（生成长度 >= max_new_tokens）
- 主循环：添加 format_ok / truncation / diversity 实时监控
- 前 100 文档后打印汇总，之后每 100 文档滚动窗口打印
- format_ok < 85% 或 truncation > 10% 时输出警告

**验证结果**：
- 6/6 有效变体格式 → `format_ok=True`（之前只有标准格式通过）
- 无效输入正确拒绝
- 关系名 "Founded By" 正确归一化为 "founded by"
- 三个文件语法检查全部通过

---
