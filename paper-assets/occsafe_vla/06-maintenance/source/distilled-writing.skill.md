# VLA Safety + 3D: Distilled Writing Patterns

Source: 8 deep-read papers, 2024-2026.

## Story & Structure

**"突破局限型" dominates** (5/8): "X great but lacks Y → existing fixes fail → our insight." 统一框架型 (2/8), 化繁为简型 (1/8).

**Universal hook**: "VLA shows promise, BUT [concrete gap]." 6/8 use this in P1.

**Dual-elimination tension** (4/8): Rule out two alternatives before presenting yours. SpatialForcing: "sensors fail AND estimators fail." VLSA: "retraining is expensive AND motion planning overwrites semantics."

**Intro**: 4-5 paragraphs. P1=promise+gap → P2=existing limitations → P3=deeper analysis → P4=method → P5=contributions. **3-contribution standard** universal (7/8): method + design/benchmark + validation.

## Motivation Techniques

1. **Empirical diagnosis** (SpatialForcing): Depth probing experiment proves VLA embeddings lack spatial info—evidence, not assumption. Strongest intro technique.
2. **Counter-intuitive reframing** (VLSA): "Safety Enables Success"—safety increases TSR by preventing cascading failures.
3. **Intuitive statistic** (OccVLA): "90% of 3D space is empty" makes occupancy feel inevitable.
4. **Extreme stress-test** (SafeVLA): CC=71.68 vs 2.20 in impossible tasks—32x gap is unforgettable.
5. **Paradoxical finding** (DepthVLA): Predicted depth > GT depth creates memory anchor.

## Figure 1 Design

**method_overview** (5/8), but best ones are hybrid. SpatialForcing: method + result + diagnosis in 3 panels. OccVLA: three-paradigm comparison positions paper instantly. VLSA: before/after trajectory. **Shared**: multi-panel (7/8), color-coded modules (6/8), flow arrows (6/8).

## Result Presentation

**Tables for quantitative** (6/8): rows=methods by_category, cols=grouped_by_dataset, bold_best. 8 baselines median. No mean±std in manipulation VLA (6/8 single-run). Add Input/Supervision columns to highlight simpler requirements (OccVLA).

**Figures for qualitative**: trajectory/depth before-after grid (4/8). Safety: time-series h(x) plot proves constraint satisfaction (VLSA, OGM-CBF).

**Ablation**: full_numbers (5/8) > delta_from_base (2/8). GST-VLA's 7-table ablation with Δ column is gold standard. Checkmark grid NOT used in this field.

**Division**: quantitative→table, qualitative→figure, safety→figure, hyperparameters→figure, per-task detail→appendix.

## Figure Narrative Flow

Consensus: **overview → motivation → results → ablation → real-world**. 5-6 figures in main paper. SpatialForcing exemplar: teaser → paradigm comparison → depth probing → sim → efficiency → real-world.
