# code audit eval script

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_audit-eval-script_20260514T133016_result.json`
- **Structured JSON:** [`93ab21d06aa294134938.json`](../../sessions/93/93ab21d06aa294134938.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已收集所有数据。以下是审计报告。

---

## Eval 代码统一性审计

### 1. Eval 脚本清单

| 文件 | 角色 |
|------|------|
| `eval/inference.py` | 主推理+评测流水线（新版，当前实际使用） |
| `eval/run_eval.py` | 早期 eval runner（已过时但仍存在） |
| `eval/evaluator.py` | 指标计算核心模块（F1/Ign-F1/Evi-F1/EDCR/format compliance） + `parse_model_output` + `gold_from_docred` |
| `eval/__init__.py` | 空 |

当前 sft_eval_r2 日志确认使用的是 **`inference.py`**（通过 "Detected adapter at" 日志格式判断）。

### 2. 主 inference.py 分析

- **CLI 参数**: 支持 `--model_path`（adapter 或完整模型，自动检测）、`--base_model`、`--data_path`、`--split`（dev/test）、`--batch_size`、`--max_new_tokens`、`--quantize`、`--seed`
- **Prompt 构建**: `SYSTEM_PROMPT` + user message → `apply_chat_template(enable_thinking=False, add_generation_prompt=True)` — 与训练一致
- **Data split**: 参数化（`--split`），默认 dev，从 `SPLIT_FILENAMES` 映射文件名
- **指标**: F1, Ign-F1, Evi-F1, EDCR, format_compliance_rate（全部委托给 `DocREDEvaluator`）

### 3. 存在两套 Parsing 逻辑（关键问题）

**存在 3 个不同的 JSON 解析实现：**

| 特性 | `inference.py` `parse_model_output` | `evaluator.py` `parse_model_output` | `grpo_trainer.py` `_parse_json_output` |
|------|-------------------------------------|-------------------------------------|---------------------------------------|
| 截断修复 | **有**（`_repair_truncated_json`，尝试补 `]`/`}]`/`"}]`） | 无 | 无 |
| 字段校验 | head/tail/relation 必需 | head/tail/relation 必需 | **无逐条校验** |
| None 保护 | `str(x or "")` | `str(x)` | 无 |
| 返回格式 | `(list[dict], bool)` | `list[dict]` | `list[dict]` |
| 使用方 | `inference.py`（当前 eval） | `run_eval.py`（旧 eval） | GRPO 训练 reward |

**`run_eval.py` 导入的是 `evaluator.py` 的 `parse_model_output`**（`from freige.eval.evaluator import ... parse_model_output`），而 **`inference.py` 用自己的实现**。两者行为不同——inference.py 能修复截断 JSON，evaluator.py 的不能。

### 4. Triple Matching 不一致（严重问题）

**Eval (`evaluator.py` `_triple_key`)**:
```python
(doc_id, head.lower().strip(), tail.lower().strip(), relation)  # relation 不 lower
```

**Training reward (`grpo_trainer.py` `f1_reward_fn`)**:
```python
(head.lower().strip(), relation.lower().strip(), tail.lower().strip())  # relation 也 lower
```

**差异**: 训练时 relation 名大小写不敏感匹配，eval 时 relation 名大小写敏感。这意味着训练 reward 对 relation 的容忍度高于 eval，可能导致模型学习到的 relation 大小写与 gold 不一致时训练中得分但 eval 扣分。

### 5. SYSTEM_PROMPT 和 Prompt 格式

**统一**: `inference.py`、`run_eval.py`、`sft_trainer.py`、`grpo_trainer.py` 四个文件使用**完全相同**的 `SYSTEM_PROMPT` 文本和 chat message 结构。

### 6. Data Loading

**统一**: 所有脚本通过 `DocREDProcessor` + `SPLIT_FILENAMES` 加载数据，`gold_from_docred()` 构建 gold 标注。Eval 日志确认 dev set 998 docs、12275 gold triples。

### 7. 结论

**统一: NO**

需要修复的差异：

| # | 问题 | 严重度 | 修复建议 |
|---|------|--------|---------|
| 1 | **Triple matching: eval 不 lower relation，training reward lower 了** | **高** | 统一为不 lower（与 DocRED 原始 relation name 一致），或全部 lower |
| 2 | **两个 eval 脚本并存**（`inference.py` vs `run_eval.py`） | 中 | 删除 `run_eval.py` 或标记为 deprecated，统一用 `inference.py` |
| 3 | **三套 parsing 实现** | 中 | 统一到 `evaluator.py` 一处，`inference.py` 的截断修复逻辑移入 evaluator |
| 4 | **Training reward 的 `_parse_json_output` 无字段校验** | 低 | reward 场景可接受，但建议复用 evaluator 的 parser |

---
