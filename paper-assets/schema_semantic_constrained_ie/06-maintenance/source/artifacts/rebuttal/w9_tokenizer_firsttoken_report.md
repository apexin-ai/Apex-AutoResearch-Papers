# W9: First-Token Uniqueness Verification for Schema-Constrained Decoding

**Date**: 2026-05-15
**Server**: westd-16980
**Models tested**:
- Llama-3.1-8B-Instruct (`/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`)
- Qwen3-8B (`/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`)

## TL;DR

**First-token uniqueness holds for ALL tested entity type sets on BOTH tokenizers, under both `raw` and `space-prefix` variants.**

| Tokenizer / Schema      | Raw form | Space-prefix form |
|-------------------------|----------|-------------------|
| Llama-3.1-8B / SciERC   | **PASS** 6/6 | **PASS** 6/6 |
| Llama-3.1-8B / DocRED   | **PASS** 6/6 | **PASS** 6/6 |
| Qwen3-8B    / SciERC    | **PASS** 6/6 | **PASS** 6/6 |
| Qwen3-8B    / DocRED    | **PASS** 6/6 | **PASS** 6/6 |

The grammar-constrained decoding assumption is **valid** for the SciERC and DocRED schemas under both tokenizers; the prefix-matching trie can disambiguate entity types using only the first generated subword token.

---

## 1. SciERC Entity Types

Entity vocabulary: `["Generic", "Method", "Material", "Metric", "OtherScientificTerm", "Task"]`

### 1.1 Llama-3.1-8B-Instruct

| Type | Raw first_id | Raw first_tok | All ids (raw) | n | Space first_id | Space first_tok | All ids (space) | n |
|------|-------------:|---------------|---------------|---:|--------------:|------------------|------------------|---:|
| Generic              | 20560 | `Generic`  | [20560] | 1 | 21981 | ` Generic`  | [21981] | 1 |
| Method               | 3607  | `Method`   | [3607]  | 1 | 6872  | ` Method`   | [6872]  | 1 |
| Material             | 13721 | `Material` | [13721] | 1 | 10441 | ` Material` | [10441] | 1 |
| Metric               | 55410 | `Metric`   | [55410] | 1 | 53558 | ` Metric`   | [53558] | 1 |
| OtherScientificTerm  | 11663 | `Other`    | [11663, 51665, 1104, 17695] | 4 | 7089  | ` Other`    | [7089, 51665, 1104, 17695] | 4 |
| Task                 | 6396  | `Task`     | [6396]  | 1 | 5546  | ` Task`     | [5546]  | 1 |

Uniqueness: **PASS** (6/6 unique first_ids in both variants).

### 1.2 Qwen3-8B

| Type | Raw first_id | Raw first_tok | All ids (raw) | n | Space first_id | Space first_tok | All ids (space) | n |
|------|-------------:|---------------|---------------|---:|--------------:|------------------|------------------|---:|
| Generic              | 19964 | `Generic`  | [19964] | 1 | 21281 | ` Generic`  | [21281] | 1 |
| Method               | 3523  | `Method`   | [3523]  | 1 | 6730  | ` Method`   | [6730]  | 1 |
| Material             | 13415 | `Material` | [13415] | 1 | 10230 | ` Material` | [10230] | 1 |
| Metric               | 54310 | `Metric`   | [54310] | 1 | 52458 | ` Metric`   | [52458] | 1 |
| OtherScientificTerm  | 11409 | `Other`    | [11409, 50565, 1086, 17249] | 4 | 6944  | ` Other`    | [6944, 50565, 1086, 17249] | 4 |
| Task                 | 6262  | `Task`     | [6262]  | 1 | 5430  | ` Task`     | [5430]  | 1 |

Uniqueness: **PASS** (6/6 unique first_ids in both variants).

---

## 2. DocRED Entity Types

Entity vocabulary (from `ontology_constraints_docred.json`): `["LOC", "MISC", "NUM", "ORG", "PER", "TIME"]`

### 2.1 Llama-3.1-8B-Instruct

| Type | Raw first_id | Raw first_tok | All ids (raw) | n | Space first_id | Space first_tok | All ids (space) | n |
|------|-------------:|---------------|---------------|---:|--------------:|------------------|------------------|---:|
| LOC  | 12321 | `LOC`  | [12321]      | 1 | 28195 | ` LOC`  | [28195]      | 1 |
| MISC | 44    | `M`    | [44, 28729]  | 2 | 386   | ` M`    | [386, 28729] | 2 |
| NUM  | 17946 | `NUM`  | [17946]      | 1 | 16322 | ` NUM`  | [16322]      | 1 |
| ORG  | 46027 | `ORG`  | [46027]      | 1 | 2794  | ` OR`   | [2794, 38]   | 2 |
| PER  | 9851  | `PER`  | [9851]       | 1 | 18335 | ` PER`  | [18335]      | 1 |
| TIME | 18621 | `TIME` | [18621]      | 1 | 23029 | ` TIME` | [23029]      | 1 |

Uniqueness: **PASS** (6/6 unique first_ids in both variants).

### 2.2 Qwen3-8B

| Type | Raw first_id | Raw first_tok | All ids (raw) | n | Space first_id | Space first_tok | All ids (space) | n |
|------|-------------:|---------------|---------------|---:|--------------:|------------------|------------------|---:|
| LOC  | 12052 | `LOC`  | [12052]      | 1 | 27096 | ` LOC`  | [27096]      | 1 |
| MISC | 44    | `M`    | [44, 27629]  | 2 | 386   | ` M`    | [386, 27629] | 2 |
| NUM  | 17488 | `NUM`  | [17488]      | 1 | 15943 | ` NUM`  | [15943]      | 1 |
| ORG  | 44927 | `ORG`  | [44927]      | 1 | 2726  | ` OR`   | [2726, 38]   | 2 |
| PER  | 9654  | `PER`  | [9654]       | 1 | 17854 | ` PER`  | [17854]      | 1 |
| TIME | 18129 | `TIME` | [18129]      | 1 | 22236 | ` TIME` | [22236]      | 1 |

Uniqueness: **PASS** (6/6 unique first_ids in both variants).

---

## 3. Conflict List

**None.** No first-token collisions detected in any of the four (tokenizer × schema) combinations under either the `raw` or `space-prefix` variant.

---

## 4. Llama vs Qwen Comparison

| Aspect | Llama-3.1-8B | Qwen3-8B |
|--------|--------------|----------|
| First-token uniqueness (SciERC, raw) | PASS 6/6 | PASS 6/6 |
| First-token uniqueness (SciERC, space) | PASS 6/6 | PASS 6/6 |
| First-token uniqueness (DocRED, raw) | PASS 6/6 | PASS 6/6 |
| First-token uniqueness (DocRED, space) | PASS 6/6 | PASS 6/6 |
| Single-token types (SciERC) | 5/6 (`OtherScientificTerm` splits into 4) | 5/6 (same) |
| Single-token types (DocRED, raw) | 4/6 (`MISC`→2 tok; `ORG`→1 tok) | 4/6 (same) |
| Single-token types (DocRED, space) | 3/6 (`MISC`,`ORG` split) | 3/6 (same) |
| Byte-level BPE shared id for `'M'` | id=44 | id=44 (identical) |
| Byte-level BPE shared id for `' M'` | id=386 | id=386 (identical) |

**Observations**:

1. **Byte-level BPE alignment.** Llama and Qwen share identical ids for the low-frequency byte-level tokens `M` (44) and ` M` (386). Both tokenizers descend from the GPT-2/tiktoken byte-level BPE family, so they agree on early single-byte ids.
2. **`OtherScientificTerm` is multi-subword (4 tokens) in both tokenizers**, but its first subword `Other` is unique within the SciERC type set on both tokenizers, so prefix-matching remains valid.
3. **DocRED `MISC` and `ORG` (space-prefix) are multi-subword**, but their first subwords (`M`/` M` for MISC, `OR`/` OR` for ORG) remain unique among the 6 types on both tokenizers.
4. **Caveat for `MISC`**: its first token is just the byte `'M'` (id=44). Any other future type beginning with capital-`M` (e.g., a hypothetical `Movie`) would collide. The current 6-type DocRED schema is safe, but the assumption is fragile if the schema is extended.

---

## 5. Methodology

For each entity type, we computed both:
- **Raw** encoding: `tokenizer.encode(type, add_special_tokens=False)`
- **Space-prefix** encoding: `tokenizer.encode(" " + type, add_special_tokens=False)`

This is necessary because byte-level BPE tokenizers (Llama, Qwen) produce different ids depending on whether the type appears at sentence start (no leading space) or mid-stream (leading space). Grammar-constrained decoding typically emits types after a separator (e.g., after `:` or newline), so both variants are relevant.

Uniqueness was checked by counting `len(set(first_ids)) == len(types)` per variant.

Script: `/tmp/w9_tokenizer_check.py` on westd-16980; JSON dump at `/tmp/w9_tokenizer_results.json`.

---

## 6. Conclusion

The grammar-constrained decoding mechanism described in the paper, which relies on a unique first-subword-token per entity type for prefix trie matching, is **fully validated** on the SciERC and DocRED schemas for both Llama-3.1-8B-Instruct and Qwen3-8B tokenizers. No conflicts exist; no implementation workaround is needed for the current schemas.
