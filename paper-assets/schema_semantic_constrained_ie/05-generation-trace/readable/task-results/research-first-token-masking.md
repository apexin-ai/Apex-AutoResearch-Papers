# research first token masking

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_first_token_masking_20260513T193339_result.json`
- **Structured JSON:** [`3729e26c0c3e257c1de7.json`](../../sessions/37/3729e26c0c3e257c1de7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### SciERC Entity Types (Qwen3-8B tokenizer)

| Type | Token IDs | Decoded | First Token ID |
|------|-----------|---------|---------------|
| Task | [6262] | ['Task'] | 6262 |
| Method | [3523] | ['Method'] | 3523 |
| Material | [13415] | ['Material'] | 13415 |
| Metric | [54310] | ['Metric'] | 54310 |
| OtherScientificTerm | [11409, 50565, 1086, 17249] | ['Other', 'Scient', 'ific', 'Term'] | 11409 |
| Generic | [19964] | ['Generic'] | 19964 |

**SciERC: 6 个 type 的 first token 全部唯一，SAFE。** Reviewer 担心的 Method/Material/Metric 首字母都是 "M"，但 Qwen3 tokenizer 把它们各自编码为完整单词 token，不存在冲突。

### DocRED Entity Types

| Type | Token IDs | Decoded | First Token ID |
|------|-----------|---------|---------------|
| PER | [9654] | ['PER'] | 9654 |
| ORG | [44927] | ['ORG'] | 44927 |
| LOC | [12052] | ['LOC'] | 12052 |
| TIME | [18129] | ['TIME'] | 18129 |
| NUM | [17488] | ['NUM'] | 17488 |
| MISC | [44, 27629] | ['M', 'ISC'] | 44 |

**DocRED: 6 个 type 的 first token 全部唯一，SAFE。** MISC 被拆为 ['M', 'ISC']，但 first token id=44 ('M') 与其他 type 无冲突。

### Context-dependent Tokenization

所有 12 个 type 在 JSON 上下文（`"type": "` 之后）的 tokenization 与独立 tokenization **完全一致**。First-token masking 在实际生成场景中不会因上下文改变而失效。

### 结论

First-token masking 对 SciERC 和 DocRED 两个数据集均安全，无需 trie-based 方案。

---
