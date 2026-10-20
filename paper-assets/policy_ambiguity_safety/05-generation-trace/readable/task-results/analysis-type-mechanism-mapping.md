# analysis type mechanism mapping

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_type_mechanism_mapping_20260522T152933_result.json`
- **Structured JSON:** [`7fcdc4de33cff3d5eeac.json`](../../sessions/7f/7fcdc4de33cff3d5eeac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both files saved. Key results:

**MI comparison** — The critical metric: I(type; mechanism) = 0.41 bits vs I(type; violation_rate) = 0.01 bits — a **30× ratio**. Type predicts mechanism far better than violation rate.

**Classification accuracy**: 59.3% overall (majority vote). Ranges from 46.8% (coreferential, the messiest type) to 82.7% (scopal → structural_misparse nearly deterministic).

**Cramér's V**: 0.45 (3-way), p ≈ 0, medium-strong association.

**Cross-model consistency**: 3/6 types unanimous at 5-way granularity (authorization_scope, conditional_precedence, scopal), dropping to 2/6 at 3-mechanism level because the "other" bucket (arbitrary_rule_selection + conservative_refusal) breaks conditional_precedence for GPT-4.1. The paper's "3 types achieve unanimity" claim matches the 5-way result.

**Dominant mappings confirmed**:
- authorization_scope → boundary_violation (all 5 models)
- scopal → structural_misparse (all 5 models)
- incompleteness, lexical → gap_filling (3/5 models each)
- coreferential → split between structural_misparse and gap_filling

Outputs: `artifacts/analysis_type_mechanism_mapping.json` and `artifacts/analysis_type_mechanism_mapping_summary.md`.

---
