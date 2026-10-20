# paper discussion s7

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_discussion_s7_20260514T091759_result.json`
- **Structured JSON:** [`64312065ff1b2738f70a.json`](../../sessions/64/64312065ff1b2738f70a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

File looks correct. Summary:

**Placeholder replacements (1)**:
- Crossover numbers updated from old II values (0.032/0.818/7.20/1.36) to confirmed bf16 raw severity values (0.584/3.002/30.903/2.915)

**New paragraphs added (3)**:
1. **"Random masking as a falsification control"** (lines 18-22) — 8/8 FAIL evidence, isolates amplification as strategy-specific
2. **"Cross-model replication and magnitude asymmetry"** (lines 24-31) — Spearman ρ=1.0, gradient permutation p=0.043, Wilcoxon 8/8 significant, Qwen ~1/5 magnitude, onset threshold difference, distillation conjecture
3. **"Mechanistic evidence: discrimination collapse as the robust signal"** (lines 33-38) — Gini/CV robust, entropy model-dependent (Qwen s025 reversal +0.045, s030 near-zero -0.007), framed as "preliminary mechanistic evidence"

**Content updated in existing paragraphs (3)**:
- Future directions §: mechanism paragraph rewritten to reflect partial confirmation and model-dependent entropy
- Statistical scope limitation: added qw_rand_s030 B=5000→B=10000 PASS→FAIL anomaly (lines 88-90)
- Model scale limitation: updated to reference model-dependent entropy component

**No remaining TODO/PENDING markers.** All confirmed numbers are incorporated with provenance comments. Framing follows constraints: "emergent phase-strategy interaction" throughout, no "importance is broken" framing.

---
