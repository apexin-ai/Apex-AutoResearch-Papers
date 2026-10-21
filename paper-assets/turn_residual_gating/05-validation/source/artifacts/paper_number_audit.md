# Paper Number Audit: Single-Seed -> Mean+/-Std

Generated: 2026-05-23

## Multi-Seed Data Reference

| Metric | s42 | s123 | Mean+/-Std |
|--------|-----|------|------------|
| TG TF GAR | 0.5035 | 0.5052 | 0.504+/-0.001 |
| TG AR GAR | 0.0157 | 0.0165 | 0.016+/-0.001 |
| TG gap ratio | 32x | 30.6x | 31.3+/-1.0x |
| SS TF GAR | 0.5025 | 0.503 | 0.503+/-0.000 |
| SS AR GAR | 0.3887 | 0.418 | 0.403+/-0.021 |
| SS gap ratio | 1.29x | 1.20x | 1.25+/-0.06x |
| Gate mean | 0.9336 | 0.9467 | 0.940+/-0.009 |
| Gate std | 0.0492 | 0.051 | 0.050+/-0.001 |

---

## HIGH PRIORITY: Stale + Needs Mean+/-Std

### 1. SS gap ratio: 1.57x is STALE (should be 1.25+/-0.06x)

The paper quotes SS s42 AR GAR = 0.318 and gap = 1.57x, but the current d048_eval_ss_s42 shows AR GAR = 0.3887 (gap 1.29x). The s123 data (AR GAR 0.418, gap 1.20x) is already in Discussion but not propagated elsewhere. All instances need updating to mean+/-std.

| File | Line | Current | Suggested | Note |
|------|------|---------|-----------|------|
| abstract.tex | 2 | "gap to 1.57$\times$ (single seed)" | "gap to $1.25\pm0.06\times$" | Key claim; remove "(single seed)" |
| introduction.tex | 18 | "from 0.016 to 0.318 (20$\times$), compressing the ${\sim}$31$\times$ gap to 1.57$\times$ (single seed)" | Update AR GAR to 0.40+/-0.02, fold to ~25x, gap to 1.25+/-0.06x; remove "(single seed)" |
| introduction.tex | 20 | "${\sim}$31$\times$ to 1.57$\times$ (single seed)" | "31.3+/-1.0x to 1.25+/-0.06x"; remove "(single seed)" |
| conclusion.tex | 3 | "gap 31$\times$$\to$1.57$\times$; single seed" | "gap $31.3\pm1.0\times\to1.25\pm0.06\times$" |
| discussion.tex | 5 | "AR GAR-ours increases from 0.016 to 0.318 (20$\times$), compressing the ${\sim}$31$\times$ gap to 1.57$\times$... a second seed yields AR GAR=0.418 (gap 1.20$\times$)" | Consolidate: "AR GAR-ours increases from 0.016 to $0.40\pm0.02$ ($\sim$25$\times$), compressing the gap to $1.25\pm0.06\times$ (two seeds)" |
| discussion.tex | 5 | "negligible PPL change (1.38 vs.\ 1.36)" | Verify if s123 PPL available; if so, report mean+/-std |

### 2. SS GAR-Dongre rise

| File | Line | Current | Suggested | Note |
|------|------|---------|-----------|------|
| discussion.tex | 5 | "GAR-Dongre also rises (0.019$\to$0.353)" | Verify if s123 GAR-Dongre available; if so, mean+/-std |
| analysis.tex | 45 | "GAR-Dongre rising to 0.353" | Same |

---

## MEDIUM PRIORITY: Has Multi-Seed Data, Needs Consistency

### 3. TG gap ratio: ~31x -> 31.3+/-1.0x

experiments.tex line 16 already reports "TF GAR-ours $0.504\pm0.001$, AR GAR-ours $0.016\pm0.001$, gap ${\sim}$31$\times$ (range 30.5--32.1$\times$)". This is close but:
- Range should be 30.6--32.0x (not 30.5--32.1x)
- Could express as 31.3+/-1.0x instead of range

Other places quoting the TG gap inconsistently:

| File | Line | Current | Suggested | Note |
|------|------|---------|-----------|------|
| experiments.tex | 16 | "gap ${\sim}$31$\times$ (range 30.5--32.1$\times$)" | "gap $31.3\pm1.0\times$" or fix range to "30.6--32.0x" | Minor precision fix |
| introduction.tex | 18 | "${\sim}$31$\times$ gap" (in SS context) | Use 31.3+/-1.0x when referring to TG gap specifically |
| analysis.tex | 37 | No explicit gap number but references Table 1 | OK as-is |

### 4. Gate profile values

| File | Line | Current | Suggested | Note |
|------|------|---------|-----------|------|
| analysis.tex | 13 | "0.93 to 0.98 (2--7\% attenuation)" | This is a per-layer range, not per-seed. But could add: "gate mean $0.940\pm0.009$ across two seeds" | Optional; the 0.93-0.98 is layer range which is distinct |
| appendix.tex | 68 (fig caption) | "mean $\sim$0.94--0.96" | Could update to "$0.940\pm0.009$" | Minor |

---

## LOW PRIORITY: Single-Seed, No Multi-Seed Data Available

These numbers are currently single-seed and no s123 counterpart was provided. Flag for awareness; may need additional experiments.

### 5. Steering results (all single-seed, no s123 data provided)

| File | Line | Current | Note |
|------|------|---------|------|
| abstract.tex | 2 | "Steering ($\beta$=5) recovers GAR to 0.727" | Single seed |
| experiments.tex | 50 | "$\beta$=5: 0.062 -> 0.6795+/-0.020, PPL 1.41->1.91" | +/-0.020 is std across N=5 convos, not seeds |
| experiments.tex | 52 | "$\beta$=3: 0.556+/-0.060, PPL 1.56" | Same: std across convos |
| experiments.tex | 52 | "$\beta$=5: GAR 0.727+/-0.061, PPL 1.77+/-0.27" | Same |
| experiments.tex | 52 | "$\beta$=0: mean 0.064, median 0.031, std 0.081" | Distribution stats over convos |
| discussion.tex | 3 | "$\beta$=5 recovers GAR from 0.064 to 0.727" | Single seed |
| conclusion.tex | 3 | "$\beta$=5, GAR 0.727" | Single seed |

### 6. Llama results (only s42 data provided)

| File | Line | Current | Note |
|------|------|---------|------|
| analysis.tex | 48 | "TF GAR-ours (N=50): 0.484 (TG), 0.481 (LO)" | Single seed |
| analysis.tex | 49 | "Median GAR-ours 0.018 (TG, LO), Base 0.009" | Single seed |
| analysis.tex | 49 | "TF-AR gaps of 27x and 26x" | Single seed |
| analysis.tex | 49 | "mean GAR-ours: 0.043 (TG), 0.028 (LO)" | Single seed |
| abstract.tex | 2 | "cross-model evaluation on Llama-3.1-8B confirms the gap ($>$25$\times$)" | Single seed |
| introduction.tex | 20 | "27$\times$ gap" | Single seed |

### 7. Base model observations (no multi-seed data)

| File | Line | Current | Note |
|------|------|---------|------|
| abstract.tex | 2 | "GAR declines 70.8%" | Base model observation, single measurement |
| introduction.tex | 3 | "70.8% relative decline from 0.0418 to 0.0122" | Same |
| related_work.tex | 4 | "70.8% decline" | Same |
| experiments.tex | 14 | "GAR-ours jumps from 0.01 to ~0.50, PPL 4.23 to 2.78" | Base model values |

### 8. Instruction retention (single-seed, single model)

| File | Line | Current | Note |
|------|------|---------|------|
| discussion.tex | 7 | "+23.8 pp, 61.9%->85.7%, overall +11.1 pp" | Single seed, single model |
| discussion.tex | 7 | "r=0.200, p=0.007; McNemar p=0.077" | Same |
| appendix.tex | 30 | Same values repeated | Same |

### 9. Gradient conflict statistics (single-seed)

| File | Line | Current | Note |
|------|------|---------|------|
| analysis.tex | 24 | "68--79% of layers, cos sim -0.089 to -0.042" | Single seed |
| analysis.tex | 24 | "NTP magnitude dominates 7.5--14.7x" | Single seed |
| analysis.tex | 26 | "PPL 2.780 vs 2.784, AR GAR 0.015 vs 0.016" | TG vs PCGrad, single seed |

### 10. Gate turn conditioning details (single-seed)

| File | Line | Current | Note |
|------|------|---------|------|
| analysis.tex | 11-12 | "p = 3.73e-8, r = 0.975" | Single seed |
| analysis.tex | 12 | "L23: 0.769/0.979, L14: 0.747/0.928" | Single seed layer values |

### 11. TRC values (single-seed)

| File | Line | Current | Note |
|------|------|---------|------|
| analysis.tex | 43 | "TG TF/AR TRC 0.334/0.332, LO 0.349/0.411" | Single seed |

---

## NO UPDATE NEEDED: Fixed Parameters / External References

These are experimental design choices or citations, not results:

- N=50, N=5, N=45, N=20 (eval sample sizes)
- T=4 turns, 10-turn conversations
- 8K UltraChat conversations
- LoRA rank 16, alpha=32
- lr=2e-4, batch size 1, grad accum 8, seed 42/123
- tau=0.5, lambda_GAR=1.0, lambda_div=1.0
- 28 layers, 32 layers
- 6 hours training time, 102GB GPU
- "27--48%" from Dongre et al.
- "AUC=0.98" from Dongre et al.
- beta values (2, 3, 5, 10) -- these are hyperparameter choices

---

## Action Summary

| Priority | Count | Action |
|----------|-------|--------|
| HIGH | 6 locations | SS gap/AR GAR values are stale AND need mean+/-std. Must fix before submission. |
| MEDIUM | 3 locations | TG gap range minor precision fix; gate mean+/-std optional |
| LOW | ~20 locations | Single-seed with no s123 data. Consider running s123 for steering and Llama if time permits. |

### Recommended Fix Order
1. Fix stale SS s42 numbers (0.318->0.3887, 1.57x->1.29x) across all sections
2. Consolidate SS to mean+/-std (1.25+/-0.06x) in abstract/intro/conclusion/discussion
3. Fix TG gap range precision (30.5--32.1 -> 30.6--32.0 or use 31.3+/-1.0x)
4. Consider gate mean+/-std in analysis section (optional polish)
