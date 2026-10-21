# IRT × Person-Fit × Contamination Detection — Writing Patterns

Distilled from 8 deep-read papers.

## Story Types & Hooks

**Two types evenly split**: "突破局限型" (4/8: ConStat, Self-Critique, PSN-IRT, Wang) vs "化繁为简型" (4/8: Min-K%, CoDeC, ATLAS, Sinharay). "跨界迁移型" is unused — a differentiator for our psychometrics→NLP bridge. **置信度**: 高

**"Integrity crisis" is the default hook** (4/8). Sinharay's concrete fraud incident (GRE 50-100 point inflation) and PSN-IRT's real leaderboard screenshot stand out. **Recommended**: Open with an impossible response pattern (hard items right, easy wrong) — the psychometric hook no NLP paper uses.

## Intro & Contributions

**5-6 paragraphs** for contamination papers: problem → method critique → insight → method → results preview → contributions. **3 contributions** is standard (5/8): method + framework + findings, escalating scope. **置信度**: 高

## Figure 1

**Motivation/problem illustration dominates** (4/8) over method_overview (2/8). Most effective: dual-panel contrast (contaminated vs clean). Self-Critique's entropy curves and CoDeC's logprob bars are exemplary. Color convention: red=contaminated, green/blue=clean. Pipeline diagrams → Figure 2, not Figure 1. **置信度**: 高

## Result Tables

Row=methods, col=datasets×metrics (6/8). Bold-best universal; bold+underline adds nuance (ATLAS: 3-tier). Average column for quick comparison. Baseline count: 3-10, median ~5. Category headers in rows add structure (Wang groups detectors by type). **置信度**: 高

**No variance is norm but risky**: 6/8 single-run. Adding CIs differentiates.

## Visual Strategy

**Two schools**: figure-heavy (CoDeC 11fig/1tab; Wang 14fig/6tab) for phenomenon papers vs table-heavy (ConStat 2fig/17tab) for method comparisons. **Figures carry analysis** (distributions for mechanism, scatter for calibration, line for scaling), **tables carry numbers**.

**Appendix**: 2-4 main tables; per-model breakdowns in appendix. ConStat's 17-table appendix accepted at NeurIPS. **置信度**: 高

## Figure Narrative Arc

**Consensus flow**: motivation → method_overview → main_result → ablation. **置信度**: 高 (7/8)

## Techniques Worth Adopting

1. **ConStat's definitional pivot**: "All prior work asks the wrong question" → elevates to problem reformulation, not just better method. **来源**: ConStat (NeurIPS 2024)
2. **Wang's negative result first**: Proving 10 baselines ≈ random creates urgency. **来源**: Wang et al. (ICLR 2026)
3. **Min-K%'s case studies**: Three applications (copyright, contamination, unlearning) multiply perceived impact. **来源**: Min-K% (ICLR 2024)
4. **PSN-IRT's numbered findings**: "5 key discoveries" with labels make psychometric analysis scannable. **来源**: PSN-IRT (AAAI 2026)
