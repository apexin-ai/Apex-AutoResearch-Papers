# urgent check docred schema 70b lora

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_check_docred_schema_70b_lora_20260522T043502_result.json`
- **Structured JSON:** [`f3f001d895a9ed53bc21.json`](../../sessions/f3/f3f001d895a9ed53bc21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**确认：westd-16980 上的 70B LoRA DocRED 推理存在同样的 schema 错误。**

## 证据

### 1. Constraints 文件格式（正确）
`ontology_constraints_docred.json` 的 `relation_types` 是 **Wikidata ID → 自然语言名** 的映射：
```json
"P17": "country",
"P159": "headquarters location",
"P361": "part of"
```

### 2. Gold data 格式（正确）
`gold_relations` 使用 Wikidata ID：
```json
{"head": "Piraeus", "tail": "Greece", "type": "P17", ...}
```

### 3. 模型输出格式（**错误**）
`raw_output` 中模型输出的 relation type 是**自然语言名**：
```json
{"head": "Skai TV", "tail": "Greece", "type": "country", ...}
{"head": "Skai TV", "tail": "Skai Group", "type": "parent organization", ...}
{"head": "IBM Research", "tail": "São Paulo", "type": "headquarters location", ...}
```

### 结论

问题与 westd-21461 完全一致：**模型输出自然语言关系名（"country", "headquarters location", "inception"），但 gold 标注使用 Wikidata ID（P17, P159, P571）**。评估时字符串不匹配，导致 R-F1=0.0。

根因：prompt template 在呈现 schema 时把 relation types 展示为自然语言名（constraints 文件的 value），而非 Wikidata ID（constraints 文件的 key），模型自然就输出自然语言名。需要修改 prompt 构建逻辑，让模型输出 Wikidata ID，或在评估时加一层映射。

---
