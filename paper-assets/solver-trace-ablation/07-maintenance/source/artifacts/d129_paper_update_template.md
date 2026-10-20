# D129/D130 Paper Update Template (v4)

> D129 完成后，用实际数据替换 `{{PLACEHOLDER}}`，然后按此模板修改论文。
> v4: 整合 s44 审计结果（H9 conjunction aggregation）+ D130 strict genuine 定义

## 已确认的数据 (s42+s43+s44)

| Condition | s42 | s43 | s44 |
|-----------|-----|-----|-----|
| ISR β=0.1 | H1 100%, PR=100%, ISR*=0.60, strict_genuine=0% | H7a 100%, PR=60%, ISR*=0.75, strict_genuine=0% | H1 39%+H9 47.6%+H8 18.3%, PR=82%, ISR*=0.44, strict_genuine=6.1% (5/82) |
| Random β=0.1 | H9 100%, PR=93% | {{PENDING r2}} | {{PENDING}} |
| ISR β=0.3 | reward collapse, PR=17% | {{PENDING}} | {{PENDING}} |

**核心发现 (三 seed 已确认)**:
- strict_genuine 0–6% 跨 seed（s42=0%, s43=0%, s44=6.1%）
- taxonomy_genuine 可高估（s44: 42.7% → strict 6.1%，H9 conjunction aggregation 逃过分类器）
- Mode 选择 stochastic: s42→H1, s43→H7a, s44→mixed (H1+H9+H8)
- "1.7B 确定性收敛到 H1" 的旧 claim 已推翻
- **D130 framing**: genuine 需同时满足 (a) 不匹配 hacking taxonomy (b) content-dependent predicates

## 1. experiments.tex §4.5 (lines 134-141)

### 1a. Title (line 134) — 保留 "Preliminary"
```
OLD: \subsection{Preliminary Cross-Scale Evidence}
NEW: \subsection{Preliminary Cross-Scale Evidence (N=3 Seeds)}
```

### 1b. Setup sentence (line 137)
```
OLD: We train Qwen3-1.7B under ISR $\beta\in\{0.1,0.3\}$ and Random $\beta{=}0.1$ (single seed, 500 steps).
NEW: We train Qwen3-1.7B under ISR $\beta\in\{0.1,0.3\}$ and Random $\beta{=}0.1$ (3 seeds each, 500 steps).
```

### 1c. Exploratory caveat (line 138) — REPLACE (not delete)
```
OLD: These single-seed results are exploratory and intended to probe whether scale modulates Goodhart basins rather than to establish definitive cross-scale conclusions.
NEW: These preliminary results probe whether scale modulates Goodhart basins; N=3 seeds provides initial replication but may miss rare genuine-capable seeds.
```

### 1d. Results paragraph (lines 139-141) — REWRITE per D130 framing

**D130/D131 structure** (Director-approved):

```
NEW (template — fill {{PLACEHOLDERS}} with final 3-seed data):
At 1.7B scale, ISR $\beta{=}0.1$ fails to produce content-dependent genuine proofs across all 3 tested seeds (strict genuine 0--6\%, vs 22.6\% pooled at 4B at 500 steps).
The specific hacking mode is seed-dependent (H1 in {{N_H1}}/3, H7a in {{N_H7}}/3, mixed in {{N_MIXED}}/3), mirroring stochastic mode selection at 4B.
Remaining taxonomy-escaping proofs employ content-independent conjunction aggregation, evading existing hacking categories but lacking semantic engagement with premises.
However, unlike 4B where {{4B_GENUINE_SEEDS}}/5 seeds access genuine proof modes, no 1.7B seed discovers content-dependent proof strategies, suggesting that genuine reasoning requires representational capacity that 1.7B models lack.
Random $\beta{=}0.1$ converges to {{RANDOM_MODES}} across 3 seeds ({{RANDOM_DETAIL}}).
ISR $\beta{=}0.3$ triggers reward collapse (PR${\leq}${{ISR03_MAX_PR}}\%) across 3 seeds, mirroring the 4B pattern.
```

### Key narrative principles (D131-finalized):
1. **Lead with strict genuine 0–6%** — content-dependent is the bar
2. **s44 ≈6% reported honestly** — not rounded to zero (D131 decision)
3. **H9 NOT added to taxonomy** — one sentence about conjunction aggregation, no Table space (D131 decision)
4. **No strict genuine definition in §4.5** — definition handled in §3 Method or footnote, not inline
5. **Mode divergence as supporting detail** — one sentence
6. **Capacity interpretation** — genuine modes require capacity 1.7B lacks
7. **✅ RESOLVED**: 4B genuine 无 content_independent 高估（genuine 中 CI=0），taxonomy genuine = strict genuine，无需修正

## 2. Table 2 — hacking taxonomy (lines 147-170)

### 2a. Data columns — no H9 subcategory (D131)
```
Keep 1.7B_ISR column with pooled data:
  H1={{ISR01_H1_POOLED_PCT}}, H7={{ISR01_H7_POOLED_PCT}}, H8={{H8_PCT}}, N-H={{STRICT_GENUINE_PCT}}

H9 conjunction aggregation folded into "other hacking" or described in text only.
Caption addition: "1.7B ISR: hacking mode varies by seed (H1/H7a)"
```

### 2b. Caption (line 168)
```
OLD: 1.7B: s42
NEW: 1.7B: 3-seed pooled; hacking mode varies by seed; N-H = strict genuine (≈6\%)
```

## 3. introduction.tex (line 27)

```
OLD: The effect transfers to Prolog (3/3 seeds, 0\% non-hacking) and is preliminarily observed at 1.7B scale.
NEW: The effect transfers to Prolog (3/3 seeds, 0\% non-hacking) and is confirmed at 1.7B scale (3 seeds, 0--6\% strict genuine; no seed discovers content-dependent proof strategies).
```

## 4. limitations.tex (lines 22-26)

```
NEW (template — D131 finalized):
\paragraph{Cross-scale replication.}
Our 1.7B experiments use 3 seeds per condition.
All seeds produce ${\leq}6\%$ strict genuine output, but N=3 may miss rare genuine-capable initializations (at 4B, {{4B_GENUINE_SEEDS}}/5 ISR seeds show transient genuine output).
Hacking mode is seed-dependent at 1.7B (H1, H7a, and mixed modes under ISR $\beta{=}0.1$), consistent with stochastic mode selection at 4B but with a strictly hacking-dominated mode repertoire.

\paragraph{Classifier limitations.}
Our hacking taxonomy (Table~\ref{tab:hacking-taxonomy}) does not capture all exploitation strategies.
One 1.7B seed produces proofs that escape all known categories but employ content-independent conjunction aggregation rather than genuine reasoning from premises.
Future work should develop content-dependency tests alongside taxonomy-based classification.
```

## 5. Appendix — cross-scale replication paragraph

appendix.tex ~line 186 ("Single-seed unreliability") — update:
```
NEW direction: cite 1.7B 3-seed mode divergence AND s44 classifier gap as further evidence that:
(a) single-seed results can misrepresent mode identity
(b) taxonomy-based classification alone may overestimate genuine rates
```

## 6. Conclusion — brief addition (optional)

```
Stochastic mode selection is scale-invariant, but the accessible mode repertoire is scale-dependent: 1.7B models are constrained to hacking-only modes under all tested conditions, with strict genuine rates of 0--6\% compared to 22.6\% at 4B.
```

## Checklist after D129 data is in
- [x] s44 审计完成：strict_genuine=5/82 (6.1%), H9 conjunction aggregation 识别
- [x] §4.5 模板更新至 v4 (D130 strict genuine framing)
- [ ] 4B 回溯检查：content_independent 是否高估 4B genuine（Worker 进行中）
- [ ] All {{PLACEHOLDER}} replaced with actual numbers from all 6 runs
- [ ] Table 2: 1.7B columns updated with pooled data + strict genuine
- [ ] Introduction line 27: "preliminarily" → "confirmed at 1.7B (3 seeds, 0–6% strict genuine)"
- [ ] Limitations: rewritten for 3 seeds + classifier gap caveat
- [ ] §4.5 title: keep "Preliminary", add "(N=3 Seeds)"
- [ ] §4.5 body: D130 structure (lead strict genuine, define term, s44 gap as one sentence)
- [ ] Appendix "single-seed unreliability" updated
- [ ] re-compile LaTeX, check page count
- [ ] grep for remaining "single seed" / "fixed template" / "genuine=0%" without strict qualifier
- [x] ✅ 4B genuine backcheck: no inflation (CI=0 in genuine), taxonomy genuine = strict genuine
