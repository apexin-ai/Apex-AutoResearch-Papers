# AI Text Detection & Model Collapse — Writing Patterns

8 deep-read papers' narrative/figure/table analysis.

## Story & Hook

**突破局限型 7/8** (exception: FineWeb 化繁为简). Three hooks: (1) **Urgency+stats** ("ChatGPT: 0.1% daily global words", Tale of Tails). (2) **Contradiction** ("detectors beat benchmarks yet OpenAI shut theirs", Two Paradigms). (3) **Inevitability** ("synthetic contamination unavoidable", Closer Look). Support: 8/8, high.

## Intro (7/8 consensus)

3-5 paras + 3 numbered contributions (identify→analyze→validate). P1: urgency. P2: quantified existing failures ("0.99→0.93 OOD"). P3: approach+headline number. Key: quantified failure > vague criticism. Exception: FineWeb single dense paragraph with 6 implicit contributions.

## Tension Strategies

Detection: **"works in lab, fails in wild"** (3/4 detection papers). Theory: **"right but practically wrong"** (Closer Look: "variance collapse rarely practical concern"). **Black-box constraint**: solving harder realistic problem (Ghostbuster: no target model access). Support: 7/8, high.

## Figure 1 (8/8)

Detection=problem_illustration (domains×models). Collapse=motivation (degradation mechanism). Method=pipeline overview (L→R). Consensus: horizontal flow, pastel color-coding, real examples grounding abstract concepts. Support: 8/8, high.

## Tables vs Figures

**Theory/collapse: 0 tables** (4/4)—all line plots over iterations. **Detection: 6-12 tables** (MAGE:12, Ghostbuster:8). Rule: trajectories→figures, comparisons→tables, pipeline ablations→bar charts.

Detection table pattern: rows=methods by_category, cols=grouped_by_dataset (ID+OOD), bold_best, 4-10 baselines, point estimates without std (5/8).

## Visualization

Line plots dominant (6/8): scaling, collapse trajectories, log-log. Heatmaps for cross-model matrices (Two Paradigms). Scatter for correlation (r=0.91, Closer Look). Gain: solid/dashed (filtered/unfiltered), diverging colormaps, parallel theory-vs-experiment layout (Tale of Tails: Fig3→Fig4 matching).

## Figure Narrative Arc (7/8)

motivation→evidence→mechanism→ablation→extension. Patterns: **paired qualitative+quantitative** (Closer Look: face grids+curves). **Progressive difficulty** (MAGE: 8 testbeds). **Ablation-as-narrative** (FineWeb: each stage=mini-experiment).

## Steal-worthy Techniques

1. **"Practical insufficiency"** (Closer Look): prior work right but misses what matters. 2/8, medium.
2. **Ablation-as-narrative** (FineWeb): pipeline stages as sequential experiments. 1/8 but universally applicable.
3. **Promise-and-peril** (Escaping Collapse): short-term good + long-term caution. 1/8, high novelty.
4. **Contradiction opener** (Two Paradigms): success vs failure paragraph 1. 2/8, medium.
5. **Thought experiment** (Two Paradigms §3.3): iteratively add authors to break attribution—viscerally intuitive.
