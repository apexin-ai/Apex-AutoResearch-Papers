# analysis r16 trie verify

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r16_trie_verify_20260521T034406_result.json`
- **Structured JSON:** [`99c113b42ac4920de992.json`](../../sessions/99/99c113b42ac4920de992.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Findings

**The trie is NOT buggy — DR=95.5% is the expected result proving the enabling dependency.**

### Trie behavior
- Contains all 6 entity types + 7 relation types
- Constrains ONLY at type field positions (detected via regex on `"type":`, `"head_type":`, `"tail_type":`)
- Does NOT enforce JSON structure — this is by design (GCD-equivalent)

### Why DR=95.5%
Three patterns, all consistent with "trie works, but no schema enforcement":

1. **~83% of samples**: Model generates valid JSON but **omits head_type/tail_type fields entirely**. Relations have only `{head, tail, type}` — no type fields to constrain → DR checker sees empty types → violations. Entity types and relation types are all valid (0% violations for both).

2. **~9% (50 samples)**: Model attempts head_type/tail_type but **generates broken JSON**. Two failure modes:
   - **Hedging**: `"type": "Part-of" or "Used-for"` — trie constrains "Part-of" then model continues unconstrained with `or "Used-for"`
   - **Missing commas**: `"type": "Feature-of" "head_type": "OtherScientificTerm"` — correct values, no separators

3. **~4.5%**: Valid JSON with head_type/tail_type properly constrained.

### Conclusion
This proves the enabling dependency: **grammar-level schema enforcement is prerequisite for vocabulary constraints to cover full schema compliance**. The trie can only constrain values at positions it detects — it cannot force the model to generate those positions in the first place, nor prevent JSON malformation around them.

### Experiment progress
- Qwen FT: **done** (551/551)
- Qwen ZS: **running** (233/551)
- Llama FT/ZS: **pending**
- PID 241846: alive (36 min elapsed)

Output written to `artifacts/r16_verification/trie_verify.json`.

---
