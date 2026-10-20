# analysis llama tokenizer verify

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_tokenizer_verify_20260515T140251_result.json`
- **Structured JSON:** [`6ba2ead88a537fb0dd9c.json`](../../sessions/6b/6ba2ead88a537fb0dd9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 12 entity type first-tokens are unique on both tokenizers, in standalone and JSON-context settings.

### 结果汇总

**Llama-3.1-8B-Instruct (vocab=128000)**

| Dataset | Type | first_token_id | first_token | full_ids | is_single_token |
|---|---|---|---|---|---|
| SciERC | Task | 6396 | `Task` | [6396] | ✓ |
| SciERC | Method | 3607 | `Method` | [3607] | ✓ |
| SciERC | Material | 13721 | `Material` | [13721] | ✓ |
| SciERC | Metric | 55410 | `Metric` | [55410] | ✓ |
| SciERC | OtherScientificTerm | 11663 | `Other` | [11663, 51665, 1104, 17695] | ✗ (4 tok) |
| SciERC | Generic | 20560 | `Generic` | [20560] | ✓ |
| DocRED | PER | 9851 | `PER` | [9851] | ✓ |
| DocRED | ORG | 46027 | `ORG` | [46027] | ✓ |
| DocRED | LOC | 12321 | `LOC` | [12321] | ✓ |
| DocRED | TIME | 18621 | `TIME` | [18621] | ✓ |
| DocRED | NUM | 17946 | `NUM` | [17946] | ✓ |
| DocRED | MISC | 44 | `M` | [44, 28729] | ✗ (2 tok) |

- SciERC: 6/6 唯一 ✓
- DocRED: 6/6 唯一 ✓
- JSON 上下文 `"entity_type": "&lt;T>"`：所有 type 的关键 token id 与 standalone 一致（`"` 是开界符，BPE 在引号后启动新 token），6/6 唯一 ✓

**Qwen3-8B (作对比)**

行为完全一致——同样 10 个 type 单 token、`OtherScientificTerm` 切 4 段、`MISC` 切为 `M`+`ISC`。所有 first-token 在两个数据集内 6/6 唯一。两个 tokenizer 的切分粒度同构（只是 token id 数值不同）。

JSON 文件已保存：`/root/schema_semantic_constrained_ie/artifacts/w9_tokenizer/tokenizer_uniqueness.json`

### 冲突分析

无 first-token 冲突。但有两个 type 是**多 token**：

1. **`OtherScientificTerm`** (SciERC) — 拆为 `Other` / `Scient` / `ific` / `Term`（4 tokens）
2. **`MISC`** (DocRED) — 拆为 `M` / `ISC`（2 tokens）

对约束解码的影响：first-token masking 在这两个 type 仍然唯一可判别（`Other` 和 `M` 都没有跟其他 type 冲突），但**生成端需要在该 type 的首 token 被选中后继续强制后续 token 序列**（即 prefix-tree / trie-constrained decoding），否则模型可能写出 `Other...` 但跑偏到非法 suffix（如 `OtherTerm`）。也就是说：first-token 决策足以唯一确定 type，但 type label 的**完整生成**仍需后续 token 受约束。

### 论文 Limitations 建议措辞

> Our first-token constrained decoding relies on the property that, for the entity-type vocabulary of each dataset (SciERC and DocRED), the first sub-word token produced by the Llama-3.1 BPE tokenizer is unique across types — we verify this is the case for all 6+6 labels considered (Table X). Two labels (`OtherScientificTerm` in SciERC and `MISC` in DocRED) tokenize to multiple sub-words, so although the first-token decision suffices to **disambiguate** the type, the decoder must still apply a prefix-trie constraint over the remaining sub-words to **commit** to a syntactically valid label string. The same property holds verbatim for the Qwen3-8B tokenizer, suggesting the method transfers to other modern BPE-based LLMs without modification; however, this uniqueness is an empirical property of the chosen label vocabulary and is not guaranteed in general — schemas with semantically overlapping labels (e.g., `Person` vs. `Performer`, both starting with the `Per` token under Llama-3.1) would require either label renaming or fallback to multi-token disambiguation, which we leave to future work.

---
