# code bpe collision diagnosis

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bpe_collision_diagnosis_20260518T113741_result.json`
- **Structured JSON:** [`8c4f315e270243eb4ccd.json`](../../sessions/8c/8c4f315e270243eb4ccd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Qwen3-8B (Qwen2TokenizerFast)
**碰撞组：0** — 27 个 entity type 全部有唯一首 token，无歧义。

### Llama-3.1-8B (PreTrainedTokenizerFast)
**碰撞组：0** — 27 个 entity type 全部有唯一首 token，无歧义。

Qwen3 和 Llama-3.1 的 tokenizer 词表大（~128K），多数 entity type 缩写被整词编码（如 `ORG`→单 token, `SEN`→单 token），天然无碰撞。

### Mistral-7B (LlamaTokenizerFast)
**碰撞组：2，涉及 5 个 entity type：**

| 碰撞 Token | 解码 | 碰撞的 Entity Types |
|---|---|---|
| 29503 | `S` | **SID, SEN, SIDE** |
| 29528 | `B` | **BAL, BOD** |

Mistral 的 32K 词表较小，JSON context 下 `S`/`B` 开头的短缩写没有被合并为多字符 token，导致首 token 退化为单字母。

### 与 AC 分析的违规 pattern 对应

Mistral 的两个碰撞组意味着：在 constrained decoding 的首 token 阶段，模型无法仅通过首 token logit 区分：
- **`SID` vs `SEN` vs `SIDE`** — 如果 AC (Autoregressive Constrained) 解码仅在首 token 做 type-level pruning，这三者会被混淆
- **`BAL` vs `BOD`** — 同理

Qwen3 和 Llama-3.1 不受影响。如果实验中 Mistral 在这 5 个 type 上出现异常高的混淆率或 AC 违规，首 token 碰撞是直接原因。

---
