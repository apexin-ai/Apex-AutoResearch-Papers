# W1 (CF Fallback) Pilot — SciERC Analysis Report

**Experiment:** `w1_cf_fallback_scierc_pilot`
**Date:** 2026-05-15
**Server:** westd-16980
**Dataset / Model / Mode:** SciERC test (551 samples) · Qwen3-8B · `full_s1` + CF fallback
**Output:** `outputs/w1_cf_fallback_scierc_pilot.jsonl`
**Log:** `~/runs/schema_semantic_constrained_ie/w1_cf_fallback_scierc_pilot.log`
**Checker version:** `fixed_20260514_v2 (strip + alias + unique_et)`

---

## 1. Run status

- 551/551 samples completed (`success=551, fail=0`), exit code 0.
- 0 JSON parse failures (json_parse_rate = 1.0).
- No exceptions in log tail; only expected `Grammar-first fallback triggered` info lines.

## 2. Fallback trigger statistics

From `outputs/w1_cf_fallback_scierc_pilot_fallback_stats.json`:

| Metric | Value |
|---|---|
| total_mask_calls | 17 024 |
| grammar_first_fallback_count | 6 237 |
| grammar_first_fallback_rate | **36.64 %** |
| cf_registry_fallback_count | 763 |
| cf_registry_fallback_rate | **4.48 %** |

Interpretation: in **36.6 %** of constrained-decoding mask calls, the semantic mask would have eliminated every grammar-valid token, so the policy fell back to grammar-only (no DR enforcement on that token). The CF-registry fallback (semantic mask compatible with seen-mention types) fired in 4.5 %.

## 3. Violation rates (per-triple unless stated)

| Metric | W1 + CF-fb | Baseline `full_s1` | Δ |
|---|---|---|---|
| Samples | 551 | 551 | — |
| Entities extracted | 2 474 | 2 474 | 0 |
| Triples extracted | 1 725 | 1 729 | −4 |
| ET violation | 0 / 2 474 (0.00 %) | 0 / 2 474 (0.00 %) | 0 |
| RV violation | 0 / 1 725 (0.00 %) | 0 / 1 729 (0.00 %) | 0 |
| **DR violation** | 255 / 1 725 (**14.78 %**) | 16 / 1 729 (**0.93 %**) | **+13.85 pp** |
| **CF violation** | 1 (**0.04 %**) | 245 (**9.90 %**) | **−9.86 pp** |
| Total violations (any) | 256 (6.10 %) | 261 (6.21 %) | −0.11 pp |
| DR + CF budget | **14.82 %** | **10.83 %** | **+3.99 pp** |

DR per relation type (W1):

| Relation | Total | DR violations | DR rate |
|---|---|---|---|
| Feature-of | 494 | 158 | 31.98 % |
| Compare | 71 | 28 | 39.44 % |
| Part-of | 77 | 18 | 23.38 % |
| Evaluate-for | 134 | 31 | 23.13 % |
| Hyponym-of | 125 | 18 | 14.40 % |
| Used-for | 791 | 2 | 0.25 % |
| Conjunction | 33 | 0 | 0.00 % |

DR damage is concentrated in `Feature-of`, `Compare`, `Part-of`, `Evaluate-for` — these are the relation types whose semantic mask most often left zero grammar-valid tokens, triggering the grammar-first fallback.

## 4. F1 metrics (extractive quality)

| Metric | W1 + CF-fb | Baseline `full_s1` | Δ |
|---|---|---|---|
| Entity P / R / F1 | 0.2598 / 0.3837 / **0.3098** | 0.2598 / 0.3837 / **0.3098** | 0 / 0 / **0 pp** |
| Relation P / R / F1 | 0.0643 / 0.1140 / **0.0823** | 0.0654 / 0.1160 / **0.0836** | −0.11 / −0.20 / **−0.13 pp** |
| Entity TP / gold / pred | 642 / 1 673 / 2 471 | 642 / 1 673 / 2 471 | 0 |
| Relation TP / gold / pred | 111 / 974 / 1 725 | (similar) | — |

Entity F1 is byte-identical to baseline (entity-level extraction is unaffected by the CF fallback). Relation F1 drops only 0.13 pp — within noise.

For reference, the **unconstrained baseline** sits at E-F1 ≈ 31.01 %, R-F1 ≈ 8.23 %, DR ≈ 15.37 %, CF ≈ 0 % — so W1 + CF-fb now resembles the unconstrained baseline in DR/CF behaviour rather than the constrained baseline.

## 5. Conclusion

The W1 CF-fallback mechanism does what it says on the tin — **CF violations collapse from 9.90 % to 0.04 %** — but the trade-off is severe: **DR violations explode from 0.93 % to 14.78 %**, and the combined DR + CF budget **increases by ~4 pp**. The grammar-first fallback fires on 36.6 % of mask calls, meaning more than a third of the decoding steps are no longer semantically constrained at all.

Against the task's success criteria:

| Criterion | Required | Observed | Pass? |
|---|---|---|---|
| CF drops significantly | < 9.90 % | 0.04 % | ✅ |
| DR stays low | < 2 % | 14.78 % | ❌ |
| R-F1 not significantly hurt | Δ > −2 pp | −0.13 pp | ✅ |

DR fails the criterion → **conclusion: NEGATIVE** (the mechanism shifts violations from CF onto DR rather than eliminating them).

## 7. Provenance

- Output: `outputs/w1_cf_fallback_scierc_pilot.jsonl` (1 322 087 B, 551 lines)
- Violation report: `outputs/violation_report_w1_cf_fallback_scierc_pilot.json`
- Fallback stats: `outputs/w1_cf_fallback_scierc_pilot_fallback_stats.json`
- Comparison table: `outputs/cf_analysis_w1_pilot/comparison_table.md`
- Pareto plot: `outputs/cf_analysis_w1_pilot/dr_vs_cf_pareto.{pdf,png}`
- Baseline report (re-generated for parity): `outputs/violation_report_phase2_scierc_full_s1_v2.json` (over `outputs/phase2_scierc_full_s1_v2.jsonl`, 551 lines)
