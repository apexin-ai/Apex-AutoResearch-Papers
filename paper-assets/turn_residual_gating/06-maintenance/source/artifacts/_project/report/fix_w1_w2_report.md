# Fix Report: W1 + W2 + INFO-1 + INFO-2

## W1: tab_crossmodel_detail SS row (WARNING)

**Problem:** TF GAR from IID s42 (0.498), AR GAR from 3-seed mean (0.401), mixed data sources.

**Fix:**
- SS row updated to consistent s42 data: TF=0.502, AR=0.347, Gap=1.4x
- Caption: added "All Qwen rows use seed 42; SS per-seed mean analysis in Table perseed-ss"
- File: `artifacts/appendix_expansion/tab_crossmodel_detail.tex`

**Cascade updates (narrative references to SS gap):**
All main-text references changed from ~1.2x to ~1.3x (3-seed mean = 0.517/0.401 = 1.29):
- `introduction.tex`: fig1 caption + contribution bullet
- `experiments.tex`: fig caption + SS paragraph (TF GAR updated to 0.517+-0.032)
- `analysis.tex`: cross-model paragraph
- `conclusion.tex`: summary sentence
- `appendix.tex`: EB scaling section (lines 491, 495, 500), llama-vs-qwen-ss table (TF 0.498->0.517, gap 1.2->1.3, compression 6.6->6.1), surrounding text (line 810)

## W2: tab_perseed_tg AR protocol mismatch (WARNING)

**Problem:** Table uses N=5, T=10 protocol (AR GAR 0.016/0.017), main results use N=50 gen-mode (0.064).

**Fix:** No N=50 per-seed data for all metrics (PPL, GAR-Dongre). Added protocol clarification to caption:
"AR evaluation uses extended-generation protocol (N=5, T=10 turns); under the gen-mode protocol (N=50) used in Table five-way, AR GAR is 0.064 (s42) and 0.055 (s123) with gap ratios 7.9x and 9.1x respectively."

File: `artifacts/appendix_expansion/tab_perseed_tg.tex`

## INFO-1: SS s42 TF GAR cross-table inconsistency

**Problem:** perseed table s42 TF=0.502, crossmodel table had 0.498.
**Fix:** Resolved by W1 fix (crossmodel SS TF now 0.502).

## INFO-2: Cost table training time precision

**Problem:** Uniform Gate actual 6.11h rounded to 6.0h (same as ThreadGate).
**Fix:** Uniform Gate time changed from 6.0 to 6.1 in `appendix.tex` cost table.

## Unchanged (verified correct)
- `tab_perseed_ss.tex`: no changes needed
- Per-seed gap values in appendix paragraph (s42=1.4x, s123=1.3x, s456=1.2x): already correct
- Llama SS values: unchanged (single evaluation, internally consistent)
