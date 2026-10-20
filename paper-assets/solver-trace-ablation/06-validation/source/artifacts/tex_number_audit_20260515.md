# TeX Number Consistency Audit — 2026-05-15

Scope: All quantitative claims in `paper/*.tex` cross-referenced against registry, decisions (D027–D086), and paper_framing.md.

---

## ERRORS (must fix before submission)

### E1. ISR β=0.1 s42 1000-step genuine rate: 1.1% vs registry 2.2%

- **Location**: `experiments.tex:84`
- **Paper says**: "genuine rate collapses to $1.1\%$"
- **Registry**: `plan002-b01-s42-1000` — PR=0.90, H7=87, H8=1, genuine=2. 2/90 = **2.2%**
- **Source**: D086 clean run is authoritative. H7=87, H8=1, remaining=2 genuine.
- **Fix**: Change `1.1\%` → `2.2\%` (or verify if one genuine sample was reclassified post-D086; if so, update registry).

### E2. H1+H7 range stated as "68–97%" — actual range is 68–100%

- **Location**: `experiments.tex:70`, `experiments.tex:157`
- **Paper says**: "GRPO-universal at $68$--$97\%$"
- **Actual data** (H1+H7 per seed):
  - ISR s42: (42+13)/81 = 67.9% → **68%**
  - ISR s43: (0+59)/61 = **96.7%**
  - ISR s44: (0+89)/89 = **100%** ← not captured by "97%"
  - Random s42: 58/79 = 73.4%
  - Random s43: 82/88 = 93.2%
  - Random s44: 71/89 = 79.8%
- **Fix**: Change `68--97\%` → `68--100\%`, or qualify as "68–97% excluding H7-dominated seeds".

### E3. Random β=0.3 H7 data: Table 1 / appendix vs Discussion inconsistency

- **Table 1** (`experiments.tex:60`): Random β=0.3 H7 = **4%** (pooled, = 7/163, using s42 H7=0)
- **Appendix** (`appendix.tex:517`): Random β=0.3 s42 H7 = **0%**
- **Discussion** (`conclusion.tex:16`): "random β=0.3 yields **4–7** H7a samples per seed"
- **D086 authoritative data**: Random β=0.3 s42 H7a = **4**, s43 H7a = **7**, s44 H7a = **0**
- **Problem**: Table 1 and appendix use pre-D086 values (s42 H7=0); Discussion uses D086 values (s42 H7=4). These are contradictory.
- **Fix**: Update appendix β=0.3 table: Random s42 H7=8.3% (4/48), H1=91.7% (44/48). Update Table 1 pooled: H7 = 11/163 = **7%** (not 4%). Update H1 = 152/163 = **93%** (not 95%).

### E4. Discussion "4–7 H7a per seed" is inaccurate

- **Location**: `conclusion.tex:16`
- **Paper says**: "random β=0.3 yields 4--7 H7a samples per seed"
- **Actual**: s42=4, s43=7, s44=**0**. Not all seeds have H7a.
- **Fix**: Change to "random β=0.3 yields 4–7 H7a in two of three seeds (0 in the third)" or "up to 7 H7a per seed".

---

## WARNINGS (verify before submission)

### W1. Random β=0.1 pooled genuine (47/256) marked DEPRECATED in paper_framing

- **Locations**: Table 1 N-H=18%, Fisher test table (p=0.0002, p=0.060)
- **Paper_framing explicitly states**: "DEPRECATED — 待 s43-r3/s44-r2 重训完成后用新数据重算. 所有聚合统计量（Fisher p, Wilson CI, genuine rate）必须用新数据重算"
- **Issue**: Random s43 genuine=6 and s44 genuine=18 are provisional/推算 values from lost data. If 重训 completed with different genuine counts, ALL of the following need updating:
  - Table 1 Random β=0.1 N-H (currently 18%)
  - Fisher p=0.0002 (ISR vs Random genuine, H8+FN corrected)
  - Fisher p=0.060 (conservative H8-only)
  - Fisher p=0.012 (Random vs Exec-only)
  - Wilson CIs [14.0, 23.7] for Random
  - All "18.4%" references
- **Action required**: Check if exp1-random-b01-s43-r3 and exp1-random-b01-s44-r2 重训 completed. If yes, recalculate with new data. If not, paper must caveat these numbers or wait for重训.

### W2. Abstract/Introduction omit "at 500 steps" qualifier for H7 69.7% vs 0%

- **Locations**: `abstract.tex:7`, `introduction.tex:27`
- **Issue**: Paper body (`experiments.tex:68`) clearly states "at 500 steps" and notes "random β=0.1 converges to 100% H7 by 1000 steps". But abstract and introduction present "69.7% vs 0%" without temporal qualifier.
- **Risk**: A reviewer noting the 1000-step result could argue the abstract overstates ISR-specificity of H7.
- **Suggestion**: Add "at 500 steps" in abstract/intro, matching what conclusion.tex already does.

---

## MINOR INCONSISTENCIES (low priority)

### M1. SFT non-hacking rate: 92.2% vs 92.3%

- **Body text** (abstract, intro, discussion, experiments): **92.2%** (mean of per-seed percentages, per D079)
- **Appendix Fisher table** (`appendix.tex:108`): **92.3%** [79.7, 97.3]
- **Appendix pooled row** (`appendix.tex:413`): **92.3**
- **Cause**: 92.2% = mean of (92.3+90.9+93.3)/3; 92.3% = 36/39 pooled
- **Suggestion**: Pick one method consistently. Recommend pooled 92.3% everywhere (matches Fisher table).

### M2. ISR* rounding: 0.415 in body vs 0.42 in appendix

- **Body** (`experiments.tex:75`): "raw ISR$^*{=}0.415$"
- **Appendix** (`appendix.tex:540`): "ISR$^*{=}0.42$"
- **Registry**: plan002-b01-s42 ISR*=0.4154
- **Fix**: Use 0.415 consistently.

### M3. Exec-only s44 H7: paper says 100%, registry H7=97 out of 98 proved

- **Paper**: "H7=100%, mean n=2.04" (`experiments.tex:30`)
- **Registry**: plan001-s44 H7=97, PR=0.98. 97/98=99.0%
- **Likely explanation**: Either 97 proved (not 98) making H7=100%, or 1 sample reclassified. Minor.

---

## DECISION CONSTRAINT COMPLIANCE

| Constraint | Status | Notes |
|---|---|---|
| D027: No "additive vs convex" simplification | ✅ PASS | Convex formulation mentioned only as discarded approach (method.tex:68) |
| D044: ISR β=0.1 labeled "lowest hacking rate" not "no hacking" | ✅ PASS | Paper correctly describes as "ISR-specific gaming" |
| D051: 1.06× not 2.4× | ✅ PASS | No mention of 2.4× anywhere; 1.06× used correctly |
| D069: s44 query-as-fact gaming | ✅ PASS | Correctly described in §4.3 and taxonomy |
| D079: SFT 92.2%±1.2% | ✅ PASS | Matches paper (minor 92.2 vs 92.3 noted in M1) |
| D084: genuine = proved − H7 − H1_exact − H8 | ✅ PASS | Standard applied consistently |
| D085: H7b obfuscated tautology | ✅ PASS | Full discussion in taxonomy + appendix |
| D086: H7 dose-response gradient | ⚠️ PARTIAL | Discussion mentions correctly; but table/appendix data not updated (see E3) |
| C006: ISR two-semantics distinction | ✅ PASS | Explicitly discussed in method.tex, crosslogic, discussion |

---

## VERIFIED CONSISTENT (~80+ claims checked)

All of the following numbers match registry data (with acceptable rounding):

**Abstract/Introduction**:
- 93% PR, 87% H1 embedding, ρ=−0.049, p=0.187 ✅
- ISR 0.642→0.132→0.003 (99.5% degradation) ✅
- PR 32%→96%, SFT 92.2% non-hacking ✅
- 69.7% H7 (161/231), 0% random (0/256), 1.06× premise-matched ✅
- β=0.3: ISR 66±42%, Random 54±35%, min 18% ✅
- 3/3 Prolog Goodhart, 0% non-hacking, 8 hacking modes ✅

**Experiments §4.1 (Diagnostic)**:
- ISR collapse: 0.642→0.132→0.003 (214× collapse) ✅
- Component count 6.58→18.55, 94.8% ISR=0 at 1000 steps ✅
- Cross-seed: s42 PR=93% H1=87%, s43 PR=13%, s44 PR=98% H7=100% n=2.04 ✅
- σ=±47pp ✅
- SFT: PR=13.0%, H7=0, H1=7.7%, 92.2% N-H, n=39 ✅
- 100-step: PR=32%, 31.2% hacking (9 H7 + 1 H1 = 10/32) ✅

**Experiments §4.2 (Goodhart)**:
- Table 1: Base PR=12%, SFT PR=13/ISR*=0.595/N-H=92% ✅
- Exec-only s42: PR=93, ISR*=0.132, H1=87, N-H=8 ✅
- ISR β=0.1 pooled: PR=77±14, H7=70%, H1=18%, N-H=7% ✅
- Random β=0.1: PR=85±6, ISR*=0.086±0.04, H7=0, H1=81%, N-H=18% ✅
- ISR β=0.3: PR=66±42, ISR*=0.39±0.31 ✅
- Per-seed β=0.3: s42 PR=18%, s43 PR=86%/H1=69%/N-H=27%, s44 PR=95%/H7=100%/ISR*=0.742 ✅
- Premise-count: raw 3.2× (0.415/0.131), matched 1.06× (0.258/0.243) ✅
- Fisher: 6.9% vs 18.4%, p=0.0002; conservative 12.1% vs 18.4%, p=0.060 ✅
- ISR s42 1000-step: H7 16.0%→96.7%, ISR*=0.88 ✅ (genuine rate is E1)

**Experiments §4.3 (Cross-Logic)**:
- Prolog exec-only: s42 PR=0.83/ISR*=0.037, s43 PR=0.56/ISR*=0.015, s44 PR=0.21/ISR*=0.387 ✅
- Prolog ISR: s42 ISR*=1.0/50 proved, s43 38/38 n_nec=1, s44 95/97 n_nec=1 ✅
- 3/3 0% non-hacking ✅

**Experiments §4.4 (Taxonomy)**:
- H7a=149, H7b=12, H7 total=161 ✅
- H7a 65% + H7b 5% of ISR proved ✅
- H7b: 11/12 vacuous quantifier, 1/12 structural simplification, 10/12 ISR≈0.8 ✅
- H8: exec-only 6% (6/93), ISR 5% (12/231 pooled) ✅
- ≥80% hacking across all RL conditions, SFT 92% non-hacking ✅

**Appendix**:
- Fisher tests: all 6 comparisons verified ✅
- O(1) ablation: PR=63%, ISR*=0.007 ✅
- All per-seed detailed tables spot-checked ✅
- Prolog detailed: all ISR*/PR values verified ✅
- SFT per-seed: s42=92.3%, s43=90.9%, s44=93.3% ✅

---

## NUMBERS NOT IN PAPER (from task reference list)

| Reference Value | In Paper? | Status |
|---|---|---|
| Bootstrap genuine parity p=0.637 | No | ✅ Correctly absent (pre-H8/FN value, superseded by Fisher p=0.0002) |
| ISR β=0.1 hacking 69.1% strict (D044) | No | ✅ Paper uses H7=69.7% pooled (different metric, both correct for their scope) |
| Random β=0.1 hacking 74.7% (D044) | No | ✅ Not directly cited; D044 was s42-only strict analysis |

---

## SUMMARY

- **4 errors** requiring fixes (E1–E4), of which E3 is the most impactful (table/appendix vs Discussion data conflict)
- **2 warnings** requiring verification (W1 is high-priority: DEPRECATED random data affects all Fisher tests)
- **3 minor inconsistencies** (M1–M3)
- **All decision constraints** satisfied except D086 partially (table data not updated)
- **~80+ other quantitative claims** verified consistent with registry
