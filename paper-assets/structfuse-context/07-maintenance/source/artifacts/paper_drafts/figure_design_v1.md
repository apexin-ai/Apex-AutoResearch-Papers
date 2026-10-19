# Figure Design — StructFuse Paper

Target: EMNLP 2026 Main (ARR May 25 deadline)
Style: Two-column ACL format, max width ~3.25in (single col) or ~6.75in (full width)

---

## Figure 1: StructFuse Pipeline Overview

**Purpose**: Establish the full method at a glance. Supports Claim 3 (CodeQL pipeline practicality) and orients the reader for §3.

**Layout**: Full-width (2-column span). Left-to-right flow diagram with 4 major blocks:

```
[Input]              [Extraction]           [Mining]              [Training]
┌──────────┐      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│ Repo +   │ ──→  │ CodeQL       │ ──→  │ Negative     │ ──→  │ Contrastive  │
│ Bug      │      │ Data-flow    │      │ Mining       │      │ Fine-tuning  │
│ Report   │      │ Analysis     │      │ (3 strats)   │      │ (InfoNCE)    │
└──────────┘      └──────────────┘      └──────────────┘      └──────────────┘
                        │                      │
                   Structural            ┌─────┴─────┐
                   Graph G               │ Random    │
                                         │ Embedding │
                                         │ Dataflow  │
                                         └───────────┘
```

- Input block: repo file tree icon + issue/bug report text snippet
- Extraction block: CodeQL logo/icon, arrows showing inter-procedural data-flow paths crossing file boundaries, output = Graph G (nodes=files, edges=data-flow)
- Mining block: 3 parallel branches for the 3 strategies, each with a mini-icon (dice for random, cosine curve for embedding, graph for dataflow). Show query → candidate selection for each
- Training block: encoder icon (Qwen/StarCoder), InfoNCE loss formula snippet, output = trained retriever
- Bottom annotation: "Static mining — computed once, no re-mining during training"

**Data source**: No empirical data needed. Schematic only.

**Design notes**:
- Color: 3 distinct colors for the 3 strategies — use Okabe-Ito palette consistently across all figures (orange=#E69F00 for random, blue=#0072B2 for embedding, green=#009E73 for dataflow)
- Rounded rectangles, thin arrows, sans-serif labels
- Reference style: similar to ANCE (Xiong et al. 2021) Fig 1, or DPR (Karpukhin et al. 2020) pipeline diagrams
- Tools: TikZ or draw.io → PDF export

**Priority**: **必须** — every methods paper needs a pipeline figure

---

## Figure 2: Negative Mining Strategies Illustration

**Purpose**: Make the 3 strategies intuitive. Directly supports §3.4 and helps readers understand what "structurally disconnected but textually similar" means concretely.

**Layout**: Full-width. 3 panels side by side, each showing the same mini-repo graph with different negative selections highlighted.

Panel structure (each ~2.2in wide):
```
(a) Random               (b) Embedding-distance      (c) Dataflow-aware
┌─────────────────┐      ┌─────────────────┐         ┌─────────────────┐
│  ○ ○ ○ ○ ○      │      │  ○ ○ ○ ○ ○      │         │  ○ ○ ○ ○ ○      │
│   /  \           │      │   /  \           │         │   /  \           │
│  ○────○          │      │  ○────○          │         │  ○────○          │
│  query  pos      │      │  query  pos      │         │  query  pos      │
│                  │      │                  │         │                  │
│  neg₁ neg₂ neg₃ │      │  neg₁ neg₂ neg₃ │         │  neg₁ neg₂ neg₃ │
│  (scattered)     │      │  (close to query)│         │  (close but      │
│                  │      │                  │         │   disconnected)  │
└─────────────────┘      └─────────────────┘         └─────────────────┘
```

Each panel shows:
- File nodes arranged as a graph with data-flow edges (solid lines)
- Query node (star marker, fixed position)
- Gold/positive file (green fill, connected to query via data-flow)
- Selected negatives (red/highlighted, position varies by strategy)
- (a) Random: negatives scattered randomly, most far from query
- (b) Embedding: negatives clustered near query in embedding space (shown as spatial proximity), some connected via data-flow
- (c) Dataflow: negatives near query in embedding space BUT with no data-flow edges to gold files — dashed lines showing "no connection"

Key visual element: data-flow edges drawn as solid gray lines between connected nodes; absence of edges for dataflow-aware negatives emphasized with ✕ or dotted-line-with-cross.

**Data source**: No empirical data. Use a stylized 8-10 node example.

**Design notes**:
- Same 3-color scheme as Figure 1 for strategy identity
- Negative nodes: filled with strategy color; non-selected nodes: light gray
- Add a small "sim(q, f⁻)" annotation showing relative similarity values
- Reference style: similar to GraphCodeBERT (Guo et al. 2021) data-flow illustrations
- This is the figure that makes the paper "click" for reviewers — invest design effort here

**Priority**: **必须** — critical for paper comprehension

---

## Figure 3: Main Results Comparison

**Purpose**: Visual summary of Table 1 main results. Supports Claim 1 (embedding mining suffices) and Claim 2 (dataflow encoder-dependent).

**Layout**: Single-column width (~3.25in). Grouped bar chart.

```
         Qwen2.5-Coder-3B              StarCoder2-3B
    ┌───────────────────────┐     ┌───────────────────────┐
R@1 │  ██ ██ ██ ██          │     │  ██ ██ ██ ██          │
    │  Ra BM Em DF          │     │  Ra BM Em DF          │
    └───────────────────────┘     └───────────────────────┘
```

- X-axis: 4 strategies (Random, BM25-mined, Embedding-distance, Dataflow-aware)
- Y-axis: R@1 (truncated axis starting from a reasonable baseline, e.g., 0.40)
- Error bars: ±1 std across 3 seeds
- Two panels side-by-side for the two encoders
- Horizontal dashed line: BM25 retrieval baseline (no training)
- Significance annotations: bracket + asterisk for statistically significant differences (bootstrap 95% CI)

**Data source**: Table 1 from experiments_v1.md — currently placeholder values. M2 full runs in progress:
- Qwen random: s42=0.5527, s43=0.5554, s44 running (eval@500: 0.6009)
- StarCoder random: s42=0.4604, s43 running (eval@500: 0.4708)
- Embedding/dataflow seeds: not yet started
- **Available for figure**: after M2 completes (~3-4 days)

**Design notes**:
- Truncated y-axis to magnify differences (document the truncation clearly)
- Okabe-Ito colors consistent with Fig 1-2
- Consider adding a small inset or annotation showing the delta (pp improvement) above embedding bars
- Alternative: radar/spider chart showing R@1/R@5/MRR simultaneously — but bar chart is cleaner for the primary claim

**Priority**: **必须** — main evidence figure. Cannot be finalized until M2 completes.

---

## Figure 4: Representation Geometry & Negative Difficulty

**Purpose**: Visual evidence for the mechanistic hypothesis (Claim 2). Shows WHY embedding mining works and why dataflow interacts with encoder geometry.

**Layout**: Full-width. Composite figure with 2-3 panels. Recommend merging/adapting from the 3 existing charts.

### Panel (a): Margin Comparison (adapting existing `neg_difficulty_margin_comparison`)
```
   Qwen (saturated)           StarCoder (healthy)
   pos_sim ≈ 0.986            pos_sim ≈ 0.80
┌──────────────────┐        ┌──────────────────┐
│  ████ ████ ████  │        │  ████ ████ ████  │
│  neg_sim  margin │        │  neg_sim  margin │
│  Ra   Em   DF   │        │  Ra   Em   DF   │
└──────────────────┘        └──────────────────┘
```
- Stacked bars: neg_sim (bottom, lighter) + margin (top, darker)
- Dashed horizontal line at pos_sim level
- Qwen: tiny margins (0.017–0.074), visually compressed
- StarCoder: larger margins (0.067–0.194), visually spread
- Key message: StarCoder has 2.6–4.1× more room to separate

### Panel (b): Similarity Distribution (adapting existing `neg_difficulty_similarity_dist`)
- Violin or KDE plot showing full distribution of query-negative cosine similarities
- 3 strategies overlaid per encoder
- Qwen: distributions tightly packed near 0.95–0.99
- StarCoder: distributions spread across 0.4–0.8
- Shows not just means but distribution shape — important for understanding tail behavior

### Panel (c): Margin Ratio Heatmap (evaluate whether needed)
- 2×3 heatmap: encoders × strategies, cell value = SC/Qwen margin ratio
- May be redundant with panel (a) — consider dropping if space is tight
- Alternative: include as supplementary material

**Data source**: `neg_difficulty_stats_v3_2048.json` on server. All data available now.
- Qwen 2048t: random margin=0.074, embedding margin=0.017, dataflow margin=0.029
- StarCoder 2048t: random margin=0.194, embedding margin=0.067, dataflow margin=0.119
- SC/Qwen ratio: random=2.61, embedding=3.94, dataflow=4.07

**Existing charts** (on server, need evaluation):
- `neg_difficulty_margin_comparison.{pdf,png}` — 1×2 stacked bar, Okabe-Ito, 300 DPI
- `neg_difficulty_similarity_dist.{pdf,png}` — distribution plot
- `neg_difficulty_ratio_heatmap.{pdf,png}` — ratio heatmap

**Design notes**:
- Panels (a)+(b) are the strongest combination — (a) shows aggregate, (b) shows distribution
- Drop panel (c) from main paper, move to appendix if needed
- Add margin value annotations directly on bars in panel (a)
- Ensure axis labels are readable at ACL column width
- Consider adding a schematic inset in panel (a) showing "saturated" vs "healthy" embedding space as 2D projections

**Priority**: **必须** — key mechanistic evidence figure. Data already available, can be produced now.

---

## Figure 5: Pool Size Sensitivity

**Purpose**: Robustness check — show that strategy rankings hold across evaluation pool sizes. Addresses anticipated reviewer concern about pool size = 50 being too small.

**Layout**: Single-column width. Line plot with 2 panels (Qwen, StarCoder) or overlaid.

```
R@1
 │     ─●─ Embedding
 │     ─○─ Random
 │     ─△─ Dataflow
 │
 └──────────────────→
   50  100  200  500
        Pool Size
```

- X-axis: pool size {50, 100, 200, 500}
- Y-axis: R@1
- 3 lines per encoder (one per strategy)
- Error bands: ±1 std (3 seeds)
- Key message: embedding > random gap persists (or widens) at larger pool sizes

**Data source**: plan_019 — not yet executed. Requires M2 best checkpoints + re-evaluation at different pool sizes.
- **Available for figure**: after M2 completes + plan_019 runs (~4-5 days)

**Design notes**:
- If gap widens at larger pools, this strengthens the paper substantially
- If gap closes, need careful framing — "sufficient at practical pool sizes"
- Log-scale x-axis may be cleaner

**Priority**: **建议** — strong robustness evidence, likely requested by reviewers. Can be table-only (Table 3) if figure space is tight.

---

## Figure 6: Training Dynamics (Learning Curves)

**Purpose**: Show training behavior differences across strategies — does embedding mining converge faster? Is there overfitting divergence?

**Layout**: Single-column width. 2×1 panels (Qwen top, StarCoder bottom) or 1×2 side-by-side.

```
R@1
 │    /──── Embedding
 │   / ──── Dataflow
 │  / ──── Random
 │ /
 └──────────────────→
   0   500  1000 1500 2000
          Training Step
```

- X-axis: training steps
- Y-axis: validation R@1 (or val loss)
- 3 curves per encoder
- Shaded regions: ±1 std across seeds
- Mark best checkpoint with ★
- Show overfitting region (s42 3-epoch run provides this data)

**Data source**: M2 training logs — partially available (random s42 curves for both encoders). Full data after M2 completes.
- Qwen random s42: R@1 peaks at step 1000 (0.5527), then oscillates
- StarCoder random s42: R@1 peaks at step 2500 (0.4604), slower convergence

**Design notes**:
- This figure is information-dense but potentially very insightful
- Alternative: move to appendix, show only val_loss in main paper
- Can combine with dual-checkpoint analysis (val_loss vs R@1 divergence for StarCoder)

**Priority**: **可选** — informative but not essential for claims. Consider appendix placement.

---

## Figure 7: SWE-bench Downstream Results

**Purpose**: Validate that retrieval improvements translate to real-world bug fixing. Supports external validity.

**Layout**: Single-column width. Simple bar chart or table figure.

```
Resolve Rate (%)
 │  ██ BM25
 │  ██ Random-trained
 │  ██ Embedding-trained
 │
 └──────────────────→
```

- X-axis: retriever variant
- Y-axis: resolve rate (%)
- 3 bars (BM25 baseline, random-trained, embedding-trained)
- Optional: add confidence intervals if multiple runs

**Data source**: plan_003 — not yet executed. Requires M2 best checkpoints + SWE-bench Lite evaluation pipeline.
- **Available for figure**: after plan_003 completes (~post-M2)

**Design notes**:
- If improvement is small (<2pp), present as table instead of figure
- If improvement is substantial, this becomes a highlight figure
- Consider showing per-category breakdown (by repo or difficulty tier) if data allows

**Priority**: **建议** — high impact if results are strong. Space decision depends on effect size.

---

## Figure 8: Stratified Analysis by Structural Data Availability

**Purpose**: Disentangle the dataflow strategy's effectiveness from confound variables (repo size, pool size). Addresses the 99.3% rich-dataflow-in-large-repos confound identified in plan_005.

**Layout**: Single-column width. Grouped bar chart with 3 strata.

```
R@1 Delta (Emb vs DF)
 │  ██ Rich dataflow (≥5 edges)
 │  ██ Sparse (1-4 edges)
 │  ██ No structural data
 │
 └──────────────────→
      Qwen    StarCoder
```

- Show per-stratum R@1 delta between embedding and dataflow strategies
- Control for pool size (use within-bin comparison from plan_005 design)
- Mark underpowered strata (n<30) with hatching

**Data source**: plan_005 — script ready, awaiting M2 checkpoints.
- Confound analysis available: rich-dataflow 99.3% in large/xlarge repos
- **Available for figure**: after M2 + plan_005 evaluation

**Design notes**:
- This is the most technically nuanced figure — may be better as a table (Table 5)
- If dataflow benefit is stratum-dependent, figure is more effective than table
- Include pool-size-controlled numbers to address the confound

**Priority**: **可选** — important for Claim 2 depth, but table may suffice. Move to appendix if main paper is tight.

---

## Summary & Production Timeline

| Figure | Type | Purpose | Data Ready? | Priority | Estimated Effort |
|--------|------|---------|-------------|----------|-----------------|
| Fig 1: Pipeline | Schematic | Method overview | Yes (no data) | 必须 | 4-6h (TikZ/draw.io) |
| Fig 2: Mining Strategies | Schematic | Strategy intuition | Yes (no data) | 必须 | 3-4h (TikZ) |
| Fig 3: Main Results | Bar chart | Claim 1 evidence | No (M2 running) | 必须 | 1h (matplotlib) |
| Fig 4: Rep. Geometry | Composite | Claim 2 mechanism | Yes (v3 data) | 必须 | 2-3h (refine existing) |
| Fig 5: Pool Sensitivity | Line plot | Robustness | No (plan_019) | 建议 | 1h (matplotlib) |
| Fig 6: Training Curves | Line plot | Training dynamics | Partial | 可选 | 1h (matplotlib) |
| Fig 7: SWE-bench | Bar chart | Downstream validity | No (plan_003) | 建议 | 1h (matplotlib) |
| Fig 8: Stratified | Bar chart | Confound control | No (plan_005) | 可选 | 1-2h (matplotlib) |

**Space budget**: ACL 2-column format typically allows 5-7 figures in 8 pages. Recommend 4 必须 figures in main paper + 1-2 建议 figures. 可选 figures go to appendix.

**Production order**:
1. Fig 4 (data ready now — refine existing charts)
2. Fig 1 + Fig 2 (schematics, no data dependency)
3. Fig 3 (after M2 completes)
4. Fig 5/7 (after respective plans complete)

**Color scheme** (Okabe-Ito, consistent across all figures):
- Random: #E69F00 (orange)
- Embedding-distance: #0072B2 (blue)
- Dataflow-aware: #009E73 (green)
- BM25: #CC79A7 (pink/mauve)
- Qwen encoder: solid lines/fills
- StarCoder encoder: hatched fills or dashed lines
