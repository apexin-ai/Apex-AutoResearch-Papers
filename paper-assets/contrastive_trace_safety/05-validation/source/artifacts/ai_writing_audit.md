# AI Writing Style Audit

## Summary
- Total issues: 33
- Files checked: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex

## Issues by Category

### Em-dash / En-dash (0 issues)
0 issues found ✓

No Unicode em-dash (—) or explanatory en-dash ( – ) detected in any file.

### -ing Phrases (29 issues)

**Main body (6):**

- `sections/introduction.tex:13` — "...79--92\% variance retained), **providing** partial evidence against a pure capacity explanation." → 拆分："...79--92\% variance retained); this provides partial evidence against..."
- `sections/method.tex:52` — "...the three metrics are positively correlated by construction, **making** the correction stricter than under independence." → 改为："...by construction, so the correction is stricter than under independence."
- `sections/discussion.tex:7` — "PCA capacity matching preserves significance (+16.8 to +23.1pp), **providing** partial evidence against a pure capacity explanation." → 改为："PCA capacity matching preserves significance (+16.8 to +23.1pp) and provides partial evidence against..."
- `sections/discussion.tex:10` — "...while R1-32B reaches only 50\% early detection, **suggesting** that the commitment signal strength itself varies across models." → 改为："...only 50\% early detection. The gap suggests that the commitment signal strength varies across models."
- `sections/limitations.tex:7` — "...are selected on the same validation set, **yielding** up to 2,240 configurations" → 改为："...are selected on the same validation set (up to 2,240 configurations);"

**Appendix (23):**

- `sections/appendix.tex:47` — "...it selects L63 (98\%) and L46 (72\%), **demonstrating** sensitivity to the data split." → "...L46 (72\%), which demonstrates sensitivity to the data split."
- `sections/appendix.tex:53` — "...3 windows, **yielding** 192 configurations" → "...3 windows (192 configurations)"
- `sections/appendix.tex:53` — "...to deep (L60 at $W{=}5$), **confirming** a layer-window interaction." → "...at $W{=}5$), which confirms a layer-window interaction."
- `sections/appendix.tex:134` — "...consistent with the bootstrap values, **confirming** that the bootstrap-based conclusions are not artifacts" → "...consistent with the bootstrap values and confirm that the conclusions are not artifacts"
- `sections/appendix.tex:213` — "...window sweep on R1-8B, **confirming** that temporal context benefits text probes" → "...sweep on R1-8B and confirms that temporal context benefits text probes"
- `sections/appendix.tex:240` — "...trained with STILL on Qwen2.5-7B, **producing** a 7B reasoning model" → "...STILL on Qwen2.5-7B to produce a 7B reasoning model"
- `sections/appendix.tex:290` — "...+8.5pp precision, $-$18.4pp FPR), **following** the same pattern as R1-8B" → "...$-$18.4pp FPR), consistent with the R1-8B pattern."
- `sections/appendix.tex:298` — "...as a validation set for early stopping, **yielding** an effective 60/10/30 split." → "...for early stopping (effective 60/10/30 split)."
- `sections/appendix.tex:300` — "...through the network) at each step, **producing** a higher-dimensional input" → "...at each step to produce a higher-dimensional input"
- `sections/appendix.tex:371` — "...LR probe at layer 16 (10.0\%), **confirming** that GRUs gain lead time at the cost of more false alarms" → "...at layer 16 (10.0\%), which confirms that GRUs gain lead time..."
- `sections/appendix.tex:387` — "...selectivity is 16.1pp at L63, **confirming** that safety-specific signal persists at deep layers." → "...at L63, which confirms that safety-specific signal persists..."
- `sections/appendix.tex:399` — "...only 50\% early detection even with oracle labels, **suggesting** that its commitment signal is inherently weaker." → "...even with oracle labels, consistent with an inherently weaker commitment signal."
- `sections/appendix.tex:554` — "...consistent in both magnitude and direction, **confirming** that the HS advantage is not an artifact" → "...in both magnitude and direction, so the HS advantage is not an artifact"
- `sections/appendix.tex:562` — "...trivially predictive, **producing** a spuriously significant result" → "...trivially predictive and produced a spuriously significant result"
- `sections/appendix.tex:619` — "...in some models but not others, **making** it unreliable as a general-purpose method." → "...in some models but not others, so it is unreliable as a general-purpose method."
- `sections/appendix.tex:623` — "...CCS still requires CP labels for pair construction, **making** it semi-supervised." → "...still requires CP labels for pair construction and is therefore semi-supervised."
- `sections/appendix.tex:636` — "...almost never triggers detection in practice, **rendering** it useless for deployment" → "...almost never triggers detection in practice and is useless for deployment"
- `sections/appendix.tex:689` — "...preserves 79--92\% of variance, **raising** the question of whether the HS advantage depends on PCA's structure" → "...preserves 79--92\% of variance. A natural question is whether the HS advantage depends on PCA's structure"
- `sections/appendix.tex:708` — "...projection preserves the HS advantage, **suggesting** the safety signal is broadly distributed" → "...preserves the HS advantage. The safety signal appears broadly distributed"
- `sections/appendix.tex:733` — "...falls between MiniLM and HS across all models, **confirming** that encoder quality progressively narrows the gap." → "...across all models, consistent with encoder quality progressively narrowing the gap."
- `sections/appendix.tex:759` — "...residualized HS-text gap is +1.9pp ($p{=}0.914$), **indicating** its HS advantage is position-mediated." → "...is +1.9pp ($p{=}0.914$), so its HS advantage is position-mediated."
- `sections/appendix.tex:767` — "...is large (up to 2,240 configurations per model), **raising** the concern that reported performance reflects overfitting" → "...is large (up to 2,240 configurations per model). This raises the concern that reported performance reflects overfitting"
- `sections/appendix.tex:791` — "The CI excludes zero, **confirming** significance despite seed fragility." → "The CI excludes zero and confirms significance despite seed fragility."
- `sections/appendix.tex:932` — "...comparable to those at threshold-dependent layers, **confirming** that the HS advantage is robust to the choice" → "...comparable to those at threshold-dependent layers, so the HS advantage is robust to the choice"

### Consecutive Transition Words (0 issues)
0 issues found ✓

No "Furthermore", "Moreover", or consecutive transition words in same paragraphs.

### AI Blacklist Words (1 issue)

- `sections/appendix.tex:206` — "QwQ-32B produces **notably** longer lead times than R1-8B" → "QwQ-32B produces longer lead times than R1-8B" (或 "substantially longer")

### Over-segmented Paragraphs (0 issues)
0 issues found ✓

All paragraphs are substantive (5+ sentences or dense technical content). No 2-sentence paragraph splitting detected.

### Unclear Pronouns (3 issues)

- `sections/discussion.tex:10` — "...only 50\% early detection, suggesting that the commitment signal strength itself varies across models. **This indicates** that distillation and native reasoning produce qualitatively different safety representation geometry." → "This" 的先行词是前一个从句的整体含义，但读起来指代不够清晰。建议："The cross-model variation indicates that distillation and native reasoning produce qualitatively different safety representation geometry."
- `sections/appendix.tex:397` — "The oracle detector has access to the true CP label and computes how many steps before CP the representation trajectory first enters a region that is linearly separable from pre-CP states with perfect accuracy on the training set. **This provides** a theoretical ceiling on early detection performance." → "This" 指代整个 oracle detector 的计算过程。建议："The resulting bound provides a theoretical ceiling..."
- `sections/appendix.tex:708` — "RP precision is slightly lower than PCA-384d (expected, as PCA preserves maximal variance), but the gap is small. **This weakens** a pure capacity explanation: even a structure-destroying projection preserves the HS advantage" → "This" 指代 RP 和 PCA 结果接近这一事实。建议："The small gap weakens a pure capacity explanation..."

---

## Priority

1. **-ing phrases (29)** — 这是最显著的 AI 写作标志，数量较多，尤其 appendix 中 "confirming that..." 出现 10+ 次，重复度高。建议：全文替换 `, confirming` → 改为 "which confirms" / "and confirms" / "so" / "consistent with"。
2. **Blacklist words (1)** — "notably" 只出现一次，容易修。
3. **Unclear pronouns (3)** — 修复成本低。
