# Paper Framing — Embedding Alignment Gap

## Target Venue
EMNLP 2026 ARR (deadline: May 25, 2026) — Findings full paper (8 pages)

## Title (working)
"The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training"

## Core Insight
In iterative self-training (student-as-generator feedback loop), the geometric diversity of a model's internal embeddings becomes systematically misaligned with content diversity (measured by rare n-gram survival). This "alignment gap" shows an overall declining trend across generations (with a transient early rebound at Gen 1-3 before accelerating decline from Gen 4), causing diversity-based data selection using internal representations to **accelerate** rather than prevent model collapse. All methods that do not rely on degrading internal embeddings — including frozen external embeddings, random selection, and no selection — avoid this catastrophic failure mode.

## Core Claims

### C1: Alignment Gap Exists and Worsens Progressively
- Internal embedding diversity selection ratio degrades from ~1.04 (Gen 0) to ~0.52 (Gen 7)
- Overall declining trend with transient early rebound (Gen 1-3: 0.91→0.93→0.94) before accelerating decline from Gen 4
- The model increasingly selects vocabulary-poor samples when using its own representations for diversity scoring
- Evidence: Phase 2 RGDS selection diagnostics (GPT2-125M, WikiText-103, self-iterate)

### C2-revised: The Failure Is Specific to Internal Embeddings (D013/D014/D015)
- RGDS is the **only** method showing catastrophic performance degradation
- {random_50, external_only, uncurated} form a "normal cluster" (gen7 PPL range: 43-50), while RGDS is a catastrophic outlier (gen7 PPL 75-82)
- External selection ratio stable >1.0 (1.10-1.28 across seeds); random ratio stable ~1.0 (0.96-1.06); only RGDS degrades (1.04→0.52)
- ⚠️ External vs uncurated ordering is **cross-seed inconsistent** (seed=42: ext wins 9.5%; seed=123: uncurated wins 7.6%) — cannot claim external > uncurated
- ⚠️ **D016 UPDATE**: random_50 三 seed 完成（Mean PPL=43.18±1.43）。两 seed 都显示 random < external（seed42: -5.1%, seed123: -15.9%）。差距不再是 noise——趋向 Scenario 2（random 显著优于 external）。等 seed=456 external 完成后做 3-seed t 检验定论。若确认 → 升级 claim：外部嵌入选择（ratio >1.0 过度偏好 rare-rich）也次优，保持自然分布（ratio ~1.0）是最优策略（Goodhart's Law 实例）
- The key insight: the problem is not "which selection method is best" but "using degrading internal representations for selection is catastrophically harmful"

### C3: The Gap Causes Accelerated Collapse (D013 upgraded)
- RGDS vs random_50 (same 50% data budget): PPL 75.07 vs 43.20 (**+74%**), rare n-gram 0.0051 vs 0.0096 (**-47%**) — fully attributable to selection mechanism, data budget controlled
- RGDS vs uncurated: PPL +49% (seed=42), +77% (seed=123) — consistent across seeds, far exceeds cross-method noise (~8-10%)
- Complete causal chain: embedding space contracts → "geometrically diverse" = "vocabulary-poor" → selection amplifies homogeneity → accelerated collapse
- random_50 baseline is the cleanest ablation: isolates selection quality from data budget effect

## Secondary Claims

### S1: PPL and Rare N-gram Improvement Are Disproportionate
- All non-RGDS methods show gen7 rare n-gram in range 0.0090-0.0099 (vs Gen 0 baseline 0.029 = -66% collapse regardless of method)
- PPL varies more across methods (43-50 for normal cluster vs baseline ~37)
- Implication: no tested selection method meaningfully prevents lexical diversity collapse — the collapse is driven by the self-iterate loop itself, not data selection
- ⚠️ Previous claim "external improves PPL -9.5% vs uncurated" is cross-seed inconsistent (D015) — removed from S1

### S3: Random Pruning Effect (D017: DOWNGRADED to directional observation)
- Seed=42: random_50 (43.20) < uncurated (50.28) → -14.1%
- Seed=123: random_50 (41.75) < uncurated (46.15) → -9.5%
- Seed=456: random_50 (44.60) < uncurated (50.12) → gap 仅 +0.2%
- **D017**: 3-seed t-test p≈0.10，未达显著性。降级为 directional observation
- 论文中不做因果推断，表述限定为 "conflates any selection benefit with a data quantity effect"
- ⚠️ 50% vs 100% 对比混淆数据量效应，仅 within-budget 对比（RGDS vs Random，同 50%）无混淆

### S2: Representation Quality Metrics Don't Detect Diversity Collapse
- RankMe increases during collapse (280→303, +8%)
- k-NN probe accuracy stable (0.988 throughout)
- These metrics track representation structure, not content diversity — a cautionary finding for monitoring frameworks

## 355M Scaling Observations (seed=42+123, pending seed=456)
- **C3 holds across scale**: RGDS vs Random +21.2% at 355M 2-seed mean (vs +72.0% at 125M 3-seed mean). 压缩 3.4×。
- **Absolute collapse far more severe**: PPL multiplier gen0→gen7 = 2.7-3.5x (355M) vs 1.2-2.0x (125M)
- **External alignment gap widens with scale**: +12.2%(355M: 3-seed External 80.10 / 2-seed Random 71.40) vs +7.4%(125M 3-seed mean). 扩大 1.6×。
- **355M seed=42 ranking**: Random (70.25) < External (77.74) < RGDS (82.84) < Uncurated (91.66)
- **355M seed=123 ranking**: Random (72.55) < External (79.56) < Uncurated (87.05) < RGDS (90.25)

### ⚠️ RGDS vs Uncurated 跨 seed 排序翻转
- seed=42: Uncurated(91.66) > RGDS(82.84) → uncurated 最差
- seed=123: RGDS(90.25) > Uncurated(87.05) → rgds 最差（与 125M 一致）
- 方法间差距在 355M 大幅压缩（高 PPL 区间 87-92），排序不稳定
- **论文 §5.7 需修正**："两个 50% 方法都优于 Uncurated" 只对 seed=42 成立。改为报告排序不稳定 + 差距压缩

### Ratio 数据（2-seed）
- 355M gen7 RGDS ratio: 0.831(s42), 0.873(s123) → 均值 **0.852±0.029**（方差极小）
- 125M gen7 RGDS ratio: 均值 **0.636±0.20**（方差大，seed=456=0.868 接近 355M 范围）
- 355M ratio 更高且更稳定，consistent with **selective attenuation**，但 125M seed=456=0.868 阻止了跨 scale 的统计区分
- ⚠️ 125M ratio 分布实为双峰（两 seed ~0.52，一 seed ~0.87），均值 0.636 不可靠——ratio 跨 scale 比较无法做 t-test

### 不对称 Gap 模式（featured observation，非 claim；Reviewer 评估 2026-05-14）
- RGDS gap: +72.0%(125M 3-seed) → +21.2%(355M 2-seed)（压缩 3.4×）
- External gap: +7.4% → +12.2%（扩大 1.6×；355M External 已 3-seed: 80.10±2.67）
- Uncurated gap: +8.9% → +25.1%（扩大 2.8×）
- 纯 ceiling effect 也能部分解释不对称（RGDS 原有 gap 最大，压缩空间最大），**不足以排除纯 ceiling effect**
- Reviewer 结论：**directionally consistent with** representational redundancy，但不能说 "primarily"。维持 dual-hypothesis
- 应作为 Results 中的 **featured observation**（附 Table）+ Discussion 中分析，不升级为 S4 claim
- 论文中使用 "selective attenuation" 或 "differential scaling"，不用 "genuine attenuation"

### Scaling Narrative Framework (Reviewer-approved: Modified Option B)
**双假说共存，不做二元对立**。论文 Discussion 呈现为：
> "Scaling reduces alignment gap penalty, which may arise from (i) higher representational redundancy (RankMe 275→365) buffering geometric distortion, and/or (ii) compression of method differences when absolute collapse is severe."

**关键证据**：
- 绝对差也大幅缩小（125M 均值 31.10 → 355M 12.59），不符合纯 ceiling effect
- **不对称 gap 模式（方向性证据）**：External gap +7.4%(125M 3-seed)→+10.2%(355M 2-seed mean)，Uncurated gap +8.9%→+25.1%（2.8×↑），仅 RGDS gap +72.0%→+21.2%（3.4×↓）。方向上 consistent with representational redundancy，但 ceiling effect 也能部分解释（RGDS 原 gap 最大→压缩空间最大）
- 355M gen7 RGDS ratio = 0.831（125M 均值 0.636, SD=0.20）→ ratio 保留更好，但 125M seed=456 也达 0.868，高方差削弱结论
- RankMe 33% 更高提供表征冗余缓冲的机制支持

**Ratio 鉴别力有限（Reviewer 评估 2026-05-14）**：由于 125M seed=456 ratio=0.868 接近 355M 范围，即使 355M 3-seed ratio 均 >0.8 且 SD<0.05，ratio 跨 scale 比较也无法做出统计显著性判断。
- **主攻证据改为不对称 gap 模式**（见 "不对称 Gap 模式" 小节）
- Ratio 降级为辅助证据，不做 t-test，改用 effect size + 置信区间描述
- seed=456 ratio 仍需记录以确认 355M ratio 的稳定性（SD<0.05），但不再是叙事强度的决定性鉴别

**必加 limitation**："Definitively distinguishing between representational redundancy and floor-compression effects requires experiments at 3+ model scales. The asymmetric gap pattern at 355M—where only the alignment-gap-driven penalty contracts while other method differences expand—provides directional evidence consistent with representational redundancy, but does not rule out scale-dependent floor compression."

## Anticipated Reviewer Concerns

### R1: "GPT2-125M is too small — does this generalize?"
- GPT2-medium (355M) experiments in progress: seed=42 complete (4 methods), seed=123 running, seed=456 queued (D019)
- 355M 2-seed mean confirms C3 (RGDS vs Random +21.2%, same budget) — "scales beyond toy models"
- Absolute collapse worse at 355M but relative alignment gap penalty narrows (ceiling effect caveat needed)

### R2: "Only one dataset (WikiText-103)"
- Response: OpenWebText subset planned as P1
- The mechanism is data-agnostic (self-iterate collapse is well-documented across datasets)

### R3: "N=1 seed — is this noise?"
- seed=42 and seed=123 complete for RGDS/external/uncurated — C1 ratio highly consistent (gen7: 0.517 vs 0.524)
- seed=456 full methods + random_50 seed=123/456 in progress → 3-seed t-tests imminent
- Cross-seed variance: normal cluster ~4-6.5 PPL, RGDS effect size 49-77% → far exceeds noise

### R4: "You only found a problem, not a solution"
- Response: (a) Random data pruning (50%) is a **zero-cost practical solution** — performs comparably to sophisticated external embedding selection (D013); (b) practitioners should avoid internal-embedding-based curation during iterative training; (c) embedding re-anchoring experiment planned as additional mitigation
- The message is actionable: "don't use your model's own embeddings for data selection during iterative training; random sampling works just as well"

### R5: "What's the theoretical explanation for the gap?"
- Connect to dimensional collapse literature (Jing et al. 2022) rather than neural collapse (Papyan et al. 2020) — dimensional collapse in self-supervised learning is more mechanistically appropriate than supervised classification neural collapse
- Self-iterate reduces embedding effective dimensionality → greedy submodular selection in low-dim space favors collapsed mode directions
- Not a formal proof, but a plausible mechanistic analogy with empirical support
- Dream review consensus: neural collapse connection is speculative; soften to analogy or replace with dimensional collapse

### R6: "External embeddings don't outperform random — what's the point of C2?"
- C2-revised is diagnostic, not prescriptive: it pinpoints that the catastrophic failure is **specific to internal embeddings**, not inherent to embedding-based selection or data pruning in general
- External and random both avoid the failure, confirming the mechanism (alignment gap in internal representations) rather than advocating a specific solution
- Opens future work: what selection signal DOES preserve lexical diversity?

## Narrative Arc (D014 revised)
1. **Setup**: Iterative self-training causes model collapse (established). Diversity-based data curation is a natural mitigation idea.
2. **Surprise**: Using the model's own representations for diversity selection makes collapse WORSE, not better — +74% PPL vs random selection with the same data budget.
3. **Explanation**: The Embedding Alignment Gap — internal representations' notion of "diverse" diverges from content diversity as training progresses (selection ratio 1.04→0.52).
4. **Contrast**: All methods that bypass internal embeddings — random selection, external embeddings, or no selection — form a "normal cluster" (PPL 43-50) with no catastrophic failure. The failure is specific to self-referential selection.
5. **Implication**: In iterative training, never use the model's own embeddings for data selection. Random sampling is a zero-cost alternative that avoids the alignment gap entirely.

## Related Work Positioning
Current: **36 references** across 8 subfields (artifacts/related_work_references.md), Reviewer 验证通过

### Existing
- Model collapse: Shumailov et al. (Nature 2024), Alemohammad et al. (2024), Dohmatob et al. (2024)
- Data selection/curation: SemDeDup (Abbas 2023), D4 (Tirumala 2023), DSIR (Xie 2023) — static (non-iterative) curation; we show iterative setting introduces new failure mode
- Representation quality metrics: RankMe (Garrido et al. 2023) — we show RankMe doesn't detect diversity collapse

### Must Add (Dream-identified gaps)
- **Concept drift / embedding drift**: Lu et al. (2019 survey), Gama et al. (2014) — alignment gap is fundamentally a concept drift phenomenon
- **Active learning under distribution shift**: Ash et al. (2020, BADGE), Kirsch et al. (2019) — acquisition function degradation is same class of problem
- **Dimensional collapse in self-supervised learning**: Jing et al. (2022), Hua et al. (2021) — replaces neural collapse as mechanistic reference
- **Broader model collapse**: Guo et al. (2024), Seddik et al. (2024), Briesch et al. (2023)
- **Broader data selection**: Xia et al. (2024, LESS), SelectIT, QuRating, Engstrom et al. (2024)
- **Goodhart's law / reward hacking**: Gao et al. (2023), Skalse et al. (2022) — alignment gap as Goodhart instance
- **Diversity metrics**: Li et al. (2016, distinct-n), Zhu et al. (2018, Self-BLEU)
- **Submodular maximization theory**: Iyer & Bilmes (2013), Wei et al. (2015)

## Novelty Framing Note (Dream D011)
The conceptual insight (representations degrade under distribution shift) is NOT novel — it's expected from concept drift theory. The genuine contribution is the **quantification and decomposition**: (1) selection ratio metric as diagnostic, (2) magnitude of acceleration (+74% PPL vs random baseline with controlled data budget, D013), (3) isolation of failure to internal embeddings specifically (random_50 ablation as cleanest evidence). Frame accordingly — overclaiming conceptual novelty will trigger reviewer pushback.

## Writing Cautions (Reviewer)
- "Monotonically decreasing" → "overall declining trend" (Gen 1-3 rebound: 0.91→0.93→0.94)
- "Self-repair" for external_only PPL recovery → needs mechanistic justification (external anchor guiding model back to original distribution, not autonomous repair)
- Uncurated rank_corr p=0.049 is borderline — wait for multi-seed before claiming significance
