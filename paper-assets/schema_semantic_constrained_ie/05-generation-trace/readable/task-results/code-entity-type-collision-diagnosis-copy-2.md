# code entity type collision diagnosis

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_entity_type_collision_diagnosis_20260518T014924_result.json`
- **Structured JSON:** [`fec438f8667ad8a2fb7c.json`](../../sessions/fe/fec438f8667ad8a2fb7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。核心发现如下：

## 根因确认：Mistral AC=16.6% → **(A) First-token collision**

### 关键数据

**Mistral (SentencePiece)**:
- ALL 27 entity types bare ≠ generation-context token IDs（SentencePiece 上下文依赖）
- `_build_entity_type_prefix_map()` 全词表扫描 → 所有 generation-context tokens 都在 prefix map 中 ✓（D044 修复有效）
- `compile_type_constraints()` 对 Mistral **直接崩溃**（bare encoding 4 组碰撞），`ensure_first_token_map()` 绕过了检查
- **2 个 generation-context 碰撞组**无法被 mask 区分：

| First Token | ID | Colliding Types |
|---|---|---|
| 'S' | 29503 | SEN, SID, SIDE |
| 'B' | 29528 | BAL, BOD |

**碰撞影响**：**103/245 (42%)** 的 (event_type, role) 约束与碰撞组有 partial overlap，**51/56** event types 受影响。主要模式：几乎所有 agent role 允许 SID 但不允许 SEN/SIDE，mask 无法阻止 SEN/SIDE 生成。

**Qwen**: 0 mismatches, 0 collisions → AC=2.1% 残余来自其他因素
**Llama**: 0 mismatches, 0 collisions → AC=3.4% 残余来自其他因素

### 机制

当约束说 "只允许 SID" 时：
1. Token 29503 ('S') 可达 {SEN, SID, SIDE}，SID ∈ allowed → 不阻塞
2. XGrammar 允许 'EN'/'ID'/'IDE' 三种延续
3. Semantic mask 只在首 token 生效 → SEN/SIDE 可能生成 → AC violation

### 推荐修复

**方案 1（推荐）**: 碰撞组 continuation mask — 检测到碰撞组首 token 未被阻塞时，在下一步对碰撞组成员的第二 token 做 masking
**方案 2**: 多 token trie masking（更通用但更复杂）
**方案 3**: 重命名碰撞 entity types（SEN→SENT, BOD→BODY 等，最简单但需改 ontology+prompt+checker）

详细报告：`artifacts/entity_type_collision_diagnosis.md`
诊断脚本：`scripts/diagnose_entity_type_tokens.py`（已部署到远程服务器并运行）

---
