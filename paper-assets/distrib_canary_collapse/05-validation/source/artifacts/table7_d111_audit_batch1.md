# Table 7 D111 Audit — Batch 1

D111 rules applied:
- naive_fwd = naive_xcorr.significant AND peak_lag > 0
- diff_fwd = diff_xcorr.significant_fdr AND peak_lag > 0
- thresh = threshold_onset.significant
- permG = perm_granger.significant (raw, direction=fwd)
- TY = ty_granger.significant_fdr (or .significant if no FDR field)
- K = sum(naive_fwd, diff_fwd, thresh, permG, TY)

Note: No `significant_3sigma` field found in any experiment; used `significant` for threshold_onset.

---

## 1. Pythia-6.9B s42 (bf16)

**Source**: westd-17855 `scale_check/pythia69b_wiki_a100_s42/analysis_results.json`
(Task specified `generalize/scale_69b_a100_s42/` — path not found; actual data at scale_check/)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh | permG | TY | K |
|------|-----------|-----------|-----------|----------|--------------|----------|--------|-------|----|---|
| te→d1 | -1 | T | **F** | -1 | T | **F** | T | T | F | 2 |
| te→d2 | -2 | T | **F** | -2 | T | **F** | T | T | T | 3 |
| te→d3 | 5 | T | T | -4 | T | **F** | T | T | T | 4 |
| te→mauve | 4 | T | T | 2 | F | F | T | F | T | 3 |
| ece→d1 | -1 | T | **F** | -1 | T | **F** | T | T | F | 2 |
| ece→d2 | -1 | T | **F** | -1 | T | **F** | T | T | F | 2 |
| ece→d3 | -3 | T | **F** | -3 | T | **F** | T | T | T | 3 |
| ece→mauve | 4 | T | T | -1 | F | F | T | T | F | 3 |

**Summary**: naive_fwd 3/8, diff_fwd 0/8, PermG 7/8, K≥3 **5/8**, K≥4 **1/8**
**Registry**: PermG=7/8, K≥3=8/8, K≥4=3/8
**Change**: K≥3 8/8→5/8 (**↓3**), K≥4 3/8→1/8 (**↓2**)

Impact: D111 removes naive_fwd for 5 pairs (lag<0) and diff_fwd for 8 pairs (all lag≤0 or not sig_fdr). Pairs te→d1, ece→d1, ece→d2 drop below K≥3.

---

## 2. Qwen3.5-0.8B s42

**Source**: westd-17855 `generalize/qwen35_08b_wiki_a100_s42_fp32_v2/analysis_results.json`

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh | permG | TY | K |
|------|-----------|-----------|-----------|----------|--------------|----------|--------|-------|----|---|
| te→d1 | 5 | T | T | -1 | T | **F** | T | T | F | 3 |
| te→d2 | 5 | T | T | -1 | T | **F** | T | T | T | 4 |
| te→d3 | 5 | T | T | -1 | T | **F** | T | T | F | 3 |
| te→mauve | 2 | T | T | -1 | T | **F** | T | T | T | 4 |
| ece→d1 | -1 | T | **F** | -1 | T | **F** | T | T | T | 3 |
| ece→d2 | -1 | T | **F** | -1 | T | **F** | T | T | T | 3 |
| ece→d3 | -4 | T | **F** | -1 | T | **F** | T | T | T | 3 |
| ece→mauve | -5 | T | **F** | 4 | T | T | T | T | T | 4 |

**Summary**: naive_fwd 4/8, diff_fwd 1/8, PermG 8/8, K≥3 **8/8**, K≥4 **3/8**
**Registry**: PermG=8/8, K≥3=8/8, K≥4=6/8
**Change**: K≥3 8/8→8/8 (no change), K≥4 6/8→3/8 (**↓3**)

Impact: Strong TY (6/8) and PermG (8/8) compensate for xcorr direction losses. All 8 pairs maintain K≥3. Three pairs lose K≥4 status (te→d1, te→d3, ece→d1 drop from 4→3).

---

## 3. Pythia-1.4B s42

**Source**: westd-19828 `generalize/pythia14b_wiki_a100_s42/analysis/5method_leadlag.json`
(Task specified westd-17855 — not found there; data on westd-19828)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh | permG | TY_fdr | K |
|------|-----------|-----------|-----------|----------|--------------|----------|--------|-------|----|---|
| te→d1 | -1 | T | **F** | -1 | T | **F** | T | T | F | 2 |
| te→d2 | -5 | T | **F** | -1 | T | **F** | T | T | F | 2 |
| te→d3 | -5 | T | **F** | -1 | T | **F** | T | F | F | 1 |
| te→mauve | -5 | T | **F** | -5 | F | F | T | F | F | 1 |
| ece→d1 | -1 | T | **F** | -1 | T | **F** | T | T | F | 2 |
| ece→d2 | 3 | T | T | -1 | T | **F** | T | T | F | 3 |
| ece→d3 | 3 | T | T | -1 | T | **F** | T | T | F | 3 |
| ece→mauve | -5 | T | **F** | 4 | T | T | T | F | F | 2 |

**Summary**: naive_fwd 2/8, diff_fwd 1/8, PermG 5/8, K≥3 **2/8**, K≥4 **0/8**
**Registry**: PermG=2/8, K≥3=2/8, K≥4=0/8
**Change**: K≥3 2/8→2/8 (no change), K≥4 0/8→0/8 (no change)

Impact: No change. Registry permG uses FDR (2/8); raw permG is 5/8 but doesn't affect K≥3 boundary pairs. TY=0/8 (FDR) throughout. This experiment was already weak pre-D111.

Note: PermG discrepancy — registry says 2/8 (FDR-corrected sig_fdr_permethod), raw significant gives 5/8. This audit uses raw per task spec.

---

## 4. Pythia-1.4B s43

**Source**: westd-19828 `generalize/pythia14b_wiki_a100_s43/analysis/5method_leadlag.json`
(Task specified westd-17855 — not found there; data on westd-19828)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh | permG | TY_fdr | K |
|------|-----------|-----------|-----------|----------|--------------|----------|--------|-------|----|---|
| te→d1 | 5 | T | T | -1 | T | **F** | T | T | F | 3 |
| te→d2 | 5 | T | T | -1 | T | **F** | T | T | F | 3 |
| te→d3 | 5 | T | T | -4 | T | **F** | T | T | F | 3 |
| te→mauve | 1 | T | T | 5 | T | T | T | F | F | 3 |
| ece→d1 | 1 | T | T | -1 | T | **F** | T | T | T | 4 |
| ece→d2 | 1 | T | T | -1 | T | **F** | T | T | T | 4 |
| ece→d3 | 1 | T | T | -1 | T | **F** | T | T | T | 4 |
| ece→mauve | -5 | F | F | 5 | T | T | T | F | F | 2 |

**Summary**: naive_fwd 7/8, diff_fwd 2/8, PermG 6/8, K≥3 **7/8**, K≥4 **3/8**
**Registry**: PermG=6/8, K≥3=6/8, K≥4=3/8
**Change**: K≥3 6/8→7/8 (**↑1**), K≥4 3/8→3/8 (no change)

Impact: K≥3 increased because D111 lag>0 rule for naive_xcorr validates 7/8 naive pairs (mostly positive lags in s43), adding votes that the pre-D111 analysis may not have counted. Registry K≥3=6/8 likely computed with different permG/TY conventions.

---

## Cross-experiment Summary

| Experiment | PermG | K≥3 (old) | K≥3 (D111) | Δ | K≥4 (old) | K≥4 (D111) | Δ |
|------------|-------|-----------|-------------|---|-----------|-------------|---|
| Pythia-6.9B s42 | 7/8 | 8/8 | 5/8 | **-3** | 3/8 | 1/8 | **-2** |
| Qwen3.5-0.8B s42 | 8/8 | 8/8 | 8/8 | 0 | 6/8 | 3/8 | **-3** |
| Pythia-1.4B s42 | 5/8 | 2/8 | 2/8 | 0 | 0/8 | 0/8 | 0 |
| Pythia-1.4B s43 | 6/8 | 6/8 | 7/8 | +1 | 3/8 | 3/8 | 0 |

Key findings:
1. **diff_xcorr almost universally has peak_lag ≤ 0** — only 4/32 pairs across all experiments have diff lag > 0. D111 effectively eliminates diff_xcorr as a consensus contributor in most cases.
2. **naive_xcorr lag polarity is model/seed dependent** — Pythia-6.9B has mostly negative lags, Qwen3.5/Pythia-1.4B s43 have mostly positive lags for token_entropy pairs.
3. **Pythia-6.9B hit hardest** — K≥3 drops from 8/8 to 5/8 because nearly all xcorr lags are negative.
4. **Qwen3.5 K≥3 survives** at 8/8 thanks to strong TY (6/8) and PermG (8/8), but K≥4 drops significantly.
5. **Pythia-1.4B s42 was already weak** — no D111 impact since few xcorr votes existed in the first place.
