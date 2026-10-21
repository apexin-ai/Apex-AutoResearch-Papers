# code entity type collision diagnosis

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_entity_type_collision_diagnosis_20260518T023202_result.json`
- **Structured JSON:** [`3deb655b4fcb08a09313.json`](../../sessions/3d/3deb655b4fcb08a09313.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整数据已收集。以下是诊断结果汇总：

---

## 诊断结果

### Mistral（核心问题模型，AC=16.6%）

**ROOT CAUSE: first-token collisions prevent disambiguation**

**所有 27 个 entity types 的 bare vs in-context tokenization 都不匹配**（全部 MISS），说明 Mistral tokenizer 对同一字符串在不同上下文中产生完全不同的 token IDs。

#### Bare encode collision groups（4 组，9 types）

| First Token | Collision Group |
|---|---|
| `'S'` (1086) | **SEN, SID, SIDE** |
| `'A'` (1098) | ABS, AML |
| `'B'` (1133) | BAL, BOD |
| `'P'` (1135) | PLA, PTH |

#### In-context encode collision groups（2 组，5 types）

| First Token | Collision Group |
|---|---|
| `'S'` (29503) | **SEN, SID, SIDE** |
| `'B'` (29528) | BAL, BOD |

#### Generation-context 分析（`"type": "` + ET + `"`）
- 所有 27 types 的 generation-context token 都在 prefix map 中（全部 map:OK）
- 但所有 generation-context token ID 都 **!=bare**，说明实际生成时使用的 token 与 bare encode 的不同
- 关键 collision 仍存在：SEN/SID/SIDE 共享 `'S'` (29503)，BAL/BOD 共享 `'B'` (29528)

#### Prefix map 覆盖
- 27 个 entity types 中，**16 个没有完整名称的 vocab token**（如 ABS, AML, SEN, SID, SIDE 等）
- 这意味着这些 types 必须通过多 token 拼写，第一个 token 的 collision 直接影响 semantic mask 区分能力

### Llama（对照）

**ROOT CAUSE: in-context tokens NOT in prefix map (D044-type bug)**

- Bare encode **无 collision**（vocab 128K 大得多，大部分 entity type 有独立完整 token）
- In-context encode 有 1 个 collision group：`"B"` → [BAL, BOD]
- 9 个 types 的 in-context first token 是 `"X` 格式（引号+字母融合），不在 prefix map 中
- 但 generation-context 分析全部 OK，bare = gen，无 map miss

### 修复建议

**Mistral 的核心问题是 SEN/SID/SIDE 和 BAL/BOD 在 generation context 下共享第一个 token，prefix map 无法在第一步区分它们。**

可行方案：
1. **Multi-token lookahead**：当第一个 token 有 collision 时，不在第一步就限制，而是允许所有 collision group 的 types 通过，在第二个 token 再做区分（如 `S` → 看第二个 token 是 `EN`/`ID`/`IDE`）
2. **Token-level trie**：将 entity type 的 token 序列构建成 trie，在每一步根据已生成的 token 前缀精确限制合法的下一个 token
3. **Rename entity types**：使用无 collision 的别名（不推荐，改动大）

---
