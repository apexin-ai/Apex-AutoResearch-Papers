# code mistral tokenizer continuation fix

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral_tokenizer_continuation_fix_20260517T205410_result.json`
- **Structured JSON:** [`2d59a1cc4bef9e8d8940.json`](../../sessions/2d/2d59a1cc4bef9e8d8940.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Local copy is a different version (399 lines vs remote's 796). The remote is authoritative. Fix is applied and verified on the server.

---

## 诊断结果

### 三模型 Tokenization 对比

| Role | Mistral bare encode | Mistral in-context (after `"`) | Match? |
|---|---|---|---|
| Subject | [26326] `Subject` | [22978] `Subject` | **MISMATCH** |
| Target | [16023] `Target` | [6100] `Target` | **MISMATCH** |
| Source | [8961] `Source` | [4988] `Source` | **MISMATCH** |
| Communicator | [6563,18341] `Commun+icator` | [4680,12729,1796] `Comm+unic+ator` | **MISMATCH** |
| Recipient | [4291,1276,1490] `Rec+ip+ient` | [4523,1276,1490] `Rec+ip+ient` | **MISMATCH** (first tok) |
| Patient | [4954,1490] `Pat+ient` | [9011,1490] `Pat+ient` | **MISMATCH** (first tok) |
| Place | [12619] `Place` | [19730] `Place` | **MISMATCH** |
| Victim | [7736,1089] `Vict+im` | [29558,1616,1089] `V+ict+im` | **MISMATCH** |
| Attacker | [6056,21940] `Att+acker` | [3285,21940] `Att+acker` | **MISMATCH** (first tok) |
| Defendant | [5135,8858] `Def+endant` | [3237,8858] `Def+endant` | **MISMATCH** (first tok) |
| Instrument | [1328,16317] `In+strument` | [1425,16317] `In+strument` | **MISMATCH** (first tok) |

Qwen: all tokens match between bare and in-context encoding.

### 根因：Case B + C 混合

Mistral 使用 SentencePiece 分词，**同一文本在不同上下文中产生不同 token ID**。`encode("Subject")` 产生 `▁Subject` (带 SentencePiece 前缀，ID=26326)，但在 JSON 值位置（`"` 之后），生成的是不带前缀的 `Subject` (ID=22978)。前缀 map 用 bare encode 构建，仅包含 `▁`-前缀版本的 ID，导致实际生成的 token 完全绕过 mask。**ALL 11/11 roles 的首 token 均未被 prefix map 覆盖**。

## 修复内容

三处修改：

1. **`_build_role_prefix_map`**: 用词表扫描替代 `encode()` — 对所有 vocab entry 做 `decode()`，与 role prefix 集合精确匹配。覆盖所有 context-dependent token ID。
2. **`_build_entity_type_prefix_map`**: 同样改为词表扫描（防御性修复）。
3. **`_build_role_continuation_tokens`**: 增加 in-context encoding（`encode('"' + role + '"')`），确保 continuation token set 包含实际生成的 token。

修复后 `type_mask_processor.py` 行数：**812**（原 796）。

通用性保证：词表扫描方式与 tokenizer 实现无关 — 只依赖 `get_vocab()` 和 `decode()`，不依赖特定 BPE 分词行为。Qwen/Llama 使用相同逻辑，prefix map 只会是原来的超集（增加 entries 但不减少），不影响已有正确行为。

## 验证结果

- **Mistral dry-run (5 docs)**: RoV=**0%**, EV=**0%**, ET=**0%**, AC=3.8%
- **Qwen 回归 (3 docs)**: RoV=**0%**, EV=**0%**, ET=**0%**, AC=1.9%
- **"Subject" grep**: 0 occurrences in Mistral output

## 下一步建议

- 当前 cuda:1 上运行的 Mistral constrained 实验使用的是旧代码（fix 前），那批结果的 RoV 违规预期仍会出现。需要重跑该实验才能获得修复后的完整结果。
- AC (Argument Constraint) 违规仍存在 (~2-4%)，这是不同层面的问题（entity type 对 role 的约束），不在本次修复范围内。

---
