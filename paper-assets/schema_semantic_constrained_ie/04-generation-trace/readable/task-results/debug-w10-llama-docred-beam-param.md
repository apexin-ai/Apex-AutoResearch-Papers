# debug w10 llama docred beam param

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_w10_llama_docred_beam_param_20260517T074352_result.json`
- **Structured JSON:** [`16164c25ed1dadb77fc7.json`](../../sessions/16/16164c25ed1dadb77fc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**RV = 0/614 (0.0%)！D/R = 0/614 (0.0%)！** Grammar constraint 完全正常工作。

## 最终结论

### 1. 根因

**不是 grammar constraint 失效，而是用错了 violation checker。**

- `violation_checker.py`（用于 SciERC）对 DocRED 的 dict 格式 `relation_types` 迭代 keys（P-codes），无法匹配模型输出的自然语言名称 → RV=100%
- `violation_checker_docred.py`（DocRED 专用）有 `build_relation_name_to_id()` 映射名称→P-codes → RV=0%

### 2. 代码逻辑确认

`load_constraint_spec`（run_constrained_extraction.py:359-362）**设计如此**：
```python
# DocRED: {P-code: name} dict -> use names as relation types
relation_types = list(code_to_name.values())  # 自然语言名称
```

Grammar schema 的 enum 约束模型输出为这些名称，prompt 也列出这些名称。Grammar 正确生效。

### 3. 参数格式

`--beam_size` 在 `run_constrained_extraction.py` 中**不存在**。两个 beam 实验都用了相同格式：
```
--decoding_strategy beam --num_beams 4
```

SciERC beam 日志确认：`Decoding: beam search (num_beams=4)`

### 4. 正确的 violation checker 结果

```
RV = 0/614 (0.0%)
D/R = 0/614 (0.0%)
Entity type violations = 0
Cross-field consistency = 6
```

### 5. 不需要重新跑实验

原始数据 `docred_llama_beam_50.jsonl` 完全正确。只需用 `violation_checker_docred.py` 评估即可。未来 DocRED 实验评估统一用这个 checker。

---
