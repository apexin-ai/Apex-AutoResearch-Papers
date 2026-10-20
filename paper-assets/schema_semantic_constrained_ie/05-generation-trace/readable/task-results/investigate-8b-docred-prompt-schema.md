# investigate 8b docred prompt schema

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_8b_docred_prompt_schema_20260522T043652_result.json`
- **Structured JSON:** [`e6246b7c5b5efa475b28.json`](../../sessions/e6/e6246b7c5b5efa475b28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have a complete picture. Let me provide the analysis.

---

## 调查结论

### 1. 8B 和 70B 输出的 relation type 格式

**都是自然语言名**，不是 P-code。关键区别在于是否精确匹配 ontology 中的 canonical name：

| 模型 | 输出示例 | Ontology 名称 |
|------|---------|--------------|
| 8B constrained | `"country"` | `P17: "country"` ✓ |
| 8B constrained | `"headquarters location"` | `P159: "headquarters location"` ✓ |
| 8B constrained | `"owned by"` | `P127: "owned by"` ✓ |
| 70B constrained | `"location"` | ✗ (应为 "headquarters location") |
| 70B constrained | `"part of"` | ✗ (应为 "owned by") |
| 70B constrained | `"country of origin"` | ✗ (应为 "country") |
| 70B constrained | `"located in the administrative territorial entity"` | `P131` ✓ |

### 2. 为何 8B 能匹配

`run_constrained_extraction.py:344-347` — `load_constraint_spec` 将 DocRED 的 `{P-code: name}` dict 转成 name list：

```python
if isinstance(raw_rtypes, dict):
    code_to_name = raw_rtypes
    relation_types = list(code_to_name.values())  # ["country", "headquarters location", ...]
```

这个 `relation_types` 被写入 JSON schema 的 `"enum"` 字段（`run_constrained_extraction.py:270`）：
```python
"type": {"type": "string", "enum": relation_types}
```

8B 本地 vLLM/HF 推理 **物理强制** 模型只能输出 enum 中的精确字符串。

评估脚本 `eval_d064.py` 将 gold P-codes 转为 canonical names：
```python
rtype_name = pcode_to_name.get(rtype_raw, rtype_raw).lower().strip()
```

所以 8B predicted `"country"` == gold normalized `"country"` → 匹配 → **R-F1=44.7**。

### 3. 为何 70B 不能匹配

70B `70b_docred_constrained.jsonl` 输出的 relation names 多数 **不是** ontology canonical names。尽管文件名带 "constrained"，模型实际输出了自由发挥的关系名（"location", "part of", "country of origin"）。

可能原因：
- 70B 通过 API（如 vLLM serving mode）推理时，JSON schema constraint 只强制了 JSON 结构格式，**没有严格 enforce enum**
- 或者 70B AWQ INT4 量化后的 logit masking 行为不同

### 4. 关于 R-F1=0.0 的澄清

实际服务器上的评估结果：
- `d065_eval_llama_con_4096.json`（8B Llama constrained）：**R-F1=44.7**
- `unified_eval/70b_con.json`（70B constrained）：**R-F1=13.05**（不是 0.0）

70B 之所以还有 13.05，是因为少数长关系名碰巧精确匹配了 ontology（如 "located in the administrative territorial entity"、"operator"）。

如果你看到 R-F1=0.0，那可能来自一个**不做 name normalization 的评估脚本**（直接拿 predicted type 比对 gold P-code），或者来自 `r16_70b_lora_docred` 中尚未评估的 run。

### 5. 最佳修复路径

核心问题：70B 的 "constrained decoding" 没有真正 enforce relation type enum。

修复选项（按优先级）：

1. **确保 70B 推理时 JSON schema enum 生效** — 检查 vLLM serving 是否正确传递了 `guided_json` 参数（vLLM 的 `--guided-decoding-backend` 需要指定）
2. **评估时加 fuzzy matching** — `unified_f1_eval.py` 已有 Levenshtein + token overlap 的 `normalize_relation()` 函数，对 70B 输出做 soft mapping（如 "country of origin" → "country"）。但这改变了评估标准的公平性
3. **在 prompt 中强化 relation name 约束** — 如果无法 enforce enum，至少在 prompt 中列出精确的 relation names 并明确要求 "use exactly these names"

---
