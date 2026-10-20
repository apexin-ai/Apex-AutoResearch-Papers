# Llama-3.1-8B DocRED full_s1 (max_new_tokens=6144) — Analysis

**Run:** `llama_docred_full_s1_mt6144` · server westd-16980 · cuda:1 · EXIT_CODE=0
**Output:** `outputs/llama_docred_full_s1_mt6144.jsonl` (11.4 MB, 998 lines)
**Log:** `~/runs/schema_semantic_constrained_ie/llama_docred_full_s1_mt6144.log` (7.27 MB)
**Wall-clock:** 16:19:29 → 22:58:15 (≈6 h 38 m, ~24 s / sample avg)

> ⚠ Confound: this run combines two variables — the new **grammar-first CF fallback** code path *and* `max_new_tokens=6144`. Compared to `llama_docred_full_s1` (mt4096) it is **not** a clean ablation of either factor; treat it as a joint replication.

---

## 1. Headline metrics (v2 checker, all_set F1)

| Metric  | full_s1_mt6144 | full_s1 (mt4096) | unconstrained_mt6144 | unconstrained (mt4096) |
|---------|---------------:|-----------------:|---------------------:|-----------------------:|
| DR (all)| **2.57 %**     | 2.55 %           | 26.18 %              | 26.07 %                |
| RV      | **0.00 %**     | 0.00 %           | 15.89 %              | 16.03 %                |
| ET      | **0.00 %**     | 0.00 %           | 0.13 %               | 0.13 %                 |
| CF      | 12.13 %        | 12.02 %          | 0.17 %               | 0.17 %                 |
| R-F1    | **6.25 %**     | 6.27 %           | 5.95 %               | 5.98 %                 |
| R-P / R-R | 5.45 / 7.32 % | 5.49 / 7.32 %   | 5.18 / 7.00 %        | 5.22 / 7.00 %          |
| E-F1    | 55.04 %        | 55.01 %          | 55.67 %              | 55.65 %                |
| Docs checked | 908 / 998 | 907 / 998        | 931 / 998            | 930 / 998              |
| Parse fail | 90           | 91               | 67                   | 68                     |
| Triples | 16 471         | 16 368           | 16 584               | 16 437                 |
| Unique ents | 11 307     | 11 296           | 11 534               | 11 525                 |

## 2. Headline deltas

**vs. unconstrained_mt6144** (matched mt6144 baseline):
- DR: **26.18 → 2.57 %**, absolute −23.61 pp, relative **−90.2 %** ✓ replicates the DR-reduction result.
- RV: 15.89 → 0 % (full elimination).
- ET: 0.13 → 0 % (full elimination).
- R-F1: 5.95 → 6.25 %, **+0.30 pp** ← essentially identical to the mt4096 +0.29 pp.
- E-F1: 55.67 → 55.04 %, −0.63 pp (small recall dip from constraint pruning).
- CF: 0.17 → 12.13 %, **+11.96 pp** (inflated; confounded — see §4).

**vs. full_s1 (mt4096)** (does mt6144 + new CF fallback move the needle?):
- DR 2.55 → 2.57 % (Δ +0.02 pp) — no change.
- R-F1 6.27 → 6.25 % (Δ −0.02 pp) — no change.
- E-F1 55.01 → 55.04 % (Δ +0.03 pp) — no change.
- Parse fail 91 → 90 — no change.
- CF 12.02 → 12.13 % — no change (despite the new fallback code).

## 3. Fallback statistics

- "Grammar-first fallback triggered" log events: **67 911** total
  - High volume: roughly 67k / 16.5k triples ≈ 4 fallback steps per emitted triple.
  - Confirms the failure mode it was designed to handle (semantic mask eliminates all grammar-valid tokens) is hit frequently in DocRED.
- 90 documents (9.0 %) still failed to parse — all hit the per-sample timeout (~102 s, E=0 R=0). Identical failure pattern to mt4096 (91 timeouts at ~102 s).

## 4. CF rate interpretation (caveat)

CF stays at 12 % under constraint mode in both mt4096 and mt6144. Two reads:
1. The grammar-first CF fallback **did not measurably reduce CF** (12.02 % → 12.13 %).
2. CF is a *post-hoc cross-field consistency* check on per-document entity-type assignment; the constrained decoder enforces local validity (RV / ET / DR) per triple but doesn't propagate type assignments across triples for the same surface entity. The new fallback path doesn't touch that mechanism.

Per the experiment-spec caveat, **do not** quote this CF number as evidence about the new fallback in isolation — it co-varies with mt6144 and would need a mt4096-with-fallback run to disentangle.

## 5. W&B

This run's command does not log to W&B (no `--wandb_*` flags in `run_constrained_extraction.py`). No W&B run id to fetch.

## 6. Conclusion

**status:** success (replication)
**conclusion:** success

- ✅ DR-reduction result holds at **−90.2 %** (matches the mt4096 reading of −90.2 %).
- ✅ R-F1 lift under constraints **stable at +0.30 pp** vs matched unconstrained baseline (mt4096 was +0.29 pp).
- ✅ RV / ET fully eliminated (0.00 %).
- ⚠ Increasing `max_new_tokens` 4096 → 6144 yields **no measurable improvement** on any metric, including parse-failure count (91 → 90). The 90 hard timeouts are not token-budget bound; they are wall-clock-bound on individual hard documents.
- ⚠ The new grammar-first CF fallback code shipped here is not visibly improving CF rate (12.02 % → 12.13 %); a clean mt4096-with-fallback ablation is needed to attribute.

## 7. Impact on paper

- **Use mt4096 numbers** as the primary "full_s1" result in the paper (already analysed and bootstrap-CI'd). The mt6144 run does **not** change conclusions, so it should be cited at most as a robustness / max-tokens-sensitivity check in the appendix.
- Bootstrap CI for mt6144 not yet computed. Given Δ-metrics ≤ 0.03 pp vs mt4096, recomputing CI is low-priority.
- For the "constraint enforcement works" claim: this run is a clean confirmatory replication on Llama under a different token budget.
- The high fallback frequency (67k events) is worth a sentence in the methodology section as evidence that the grammar/semantic mask intersection is genuinely empty often enough to require a fallback rule.

## 8. Files

- `outputs/llama_docred_full_s1_mt6144.jsonl` — raw extraction output, 998 lines.
- `outputs/analysis_llama_docred_full_s1_mt6144_v2.json` — checker summary (this analysis).
- `analyze_llama_docred_full_s1_mt6144.py` — analysis script (cloned from `analyze_llama_docred_mt6144.py`).
