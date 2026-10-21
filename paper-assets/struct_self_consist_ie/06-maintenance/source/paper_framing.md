# Paper Framing — struct_self_consist_ie

> Updated 2026-05-22 — **D237 FRAMING OVERHAUL**: dataset-dependent optimal aggregation strategy + diagnostic cascade as primary contribution. N-scaling unified data (N=8/16/32/64) confirms MV gains are monotonically increasing but universally <1pp. LP-best saturates at N=8. Optimal strategy is dataset-dependent: LP dominates on FewNERD (+8pp), MV dominates on CoNLL (+0.61pp vs LP -2.34pp), SciERC approximately neutral.

## Target Venue
- Primary: EMNLP 2026 **Main Conference** (via ARR May 2026)
- Deadline: ARR May cycle, 2026-05-25

## Core Claims (D237 — TRIPLE CONTRIBUTION: QE + diagnostic + prescriptive)

### Claim 1 (PRIMARY — QE Framework + Selection Diagnostic)
**Positive contribution (A)**: Confidence signals reliably predict structured IE output quality at the population level (AUROC up to 0.82, ρ up to 0.45), enabling practical QE/selective prediction.

**Diagnostic contribution (B)** (D237 revised): The optimal aggregation strategy is **dataset-dependent**, determined by a four-stage diagnostic cascade:
1. **Instance degeneracy** (21-58% of instances produce identical F1 across N samples)
2. **LP compression** (within-instance LP range median 0.041 nats)
3. **LP-F1 alignment** (primary cross-dataset predictor: FewNERD ρ~0.5-0.7 → LP works; SciERC ρ~0.2 → LP fails; cross-dataset degeneracy-LP ρ=0.052, p=0.81)
4. **Structural signal limitation** (4/5 signals are instance-level aggregates → cannot rank candidates by construction)

**N-scaling evidence** (unified baseline, N=8/16/32/64, seed=42):
- SciERC: MV Δ = -1.24/-0.61/+0.24/+0.53 (monotonic ↑, crosses ~N=28, 3-seed mean ≈0 at N=32)
- CoNLL: MV Δ = +0.20/+0.32/+0.44/+0.61 (always positive, always <1pp)
- FewNERD: MV Δ = -2.71/-1.65/TBD (N=32 pending, strongly negative)
- LP-best saturates at N=8 (SciERC: 66.5→67.1% across N=8-64, Δ<0.6pp)

**Dataset-dependent optimal strategy**:
| Dataset | LP-best@N=8 vs greedy | MV@N=64 vs greedy | Winner |
|---------|----------------------|-------------------|--------|
| FewNERD | +8pp | negative | LP >> MV |
| SciERC | -0.32pp (N=8) / +0.29pp (N=64) | +0.53pp | ~tied |
| CoNLL | -1.42pp (N=8) / -2.34pp (N=64) | +0.61pp | MV >> LP |

**Core insight**: The diagnostic cascade predicts which method works where. On most datasets, gains <1pp regardless of method — the diagnostic framework itself is the primary contribution.

**Capability-diversity tension** (unifying insight): Model capability → output convergence → instance degeneracy → vanishing selection headroom. CoNLL (91% F1) → 58% degen; SciERC (66%) → 21%; FewNERD (79%) → 10%.

### Claim 2 (METHODOLOGY — QE Evaluation Framework)
Systematic evaluation of 5 confidence signals across 4 families for structured IE quality estimation. Task-dependent signal ranking: structural > probabilistic for NER, reversed for RE (binary-dominated F1 distributions). QE enables selective prediction: filtering 20% low-confidence instances yields +5-8pp F1 gain.

### Claim 3 (Diagnostic — task-complexity boundary)
RE task has 43-47% zero-F1 samples, creating binary-dominated signal distributions. LP's entire RE advantage is binary classification (cond ρ=0.011, n.s.). Task-dependent signal effectiveness is a novel characterization.

### Claim 4 (Prescriptive — Entity-Level Construction)
Entity-level construction (aggregate entities across N samples via MV): SciERC +1.02pp, FewNERD +1.40pp, CoNLL +0.10pp (n.s.). LP-weighted construction for 72B zero-shot: SciERC +1.53pp. Effectiveness is headroom-dependent.

## Story Spine

**Problem**: Test-time scaling via multi-sample generation improves LLM reasoning, but its effectiveness for structured IE is unclear.

**Gap**: Self-consistency and MBR succeed for discrete-answer reasoning via majority vote. Structured IE outputs (entity sets, relation triples) present fundamentally different challenges — prior work applies instance-level selection, which is the wrong analogy for set-structured outputs.

**Our contribution (TRIPLE)**:
1. **QE Framework** (Positive): 5 signals reliably predict quality (AUROC 0.82, ρ 0.45). Enables selective prediction (+5-8pp @80% coverage).
2. **Diagnostic cascade** (Why aggregation mostly fails): degeneracy → LP compression → LP-alignment → structural signal limitation. Dataset-dependent: LP wins on high-alignment tasks, MV wins on high-capability tasks, neither exceeds ~1pp on most tasks.
3. **Entity-level construction** (Prescriptive): The correct self-consistency analogy is entity-level construction, not instance-level selection. +1.02-1.53pp where headroom allows.

**Key distinctions from prior work**:
- Yao et al. (2026): task-level correlation only, no entity-level mechanisms, no selection analysis
- Yun et al. (2025): reasoning-focused, discrete answers, no structured IE
- Nédellec & Xia (2026): surface-level string matching, single domain, no multi-signal comparison

## Key Evidence Summary

- **3 NER datasets**: SciERC (529 instances), CoNLL-2003 (2756), FewNERD INTRA (32,565)
- **Cross-model**: Qwen3-8B + Qwen3-4B + LLaMA-3.1-8B
- **N-scaling**: N=8/16/32/64 with unified instance baseline, perfectly monotonic
- **Free-form ablation**: Score compression is model/task intrinsic (std ratio 0.97)
- **LoRA rank ablation**: Reducing degeneracy 3× still doesn't fix selection → multi-causal
- **Scale ablation**: Correlation-selection gap persists from 4B to 8B
- **Supervised verifier**: AUC 0.92 but +0.32pp OOF → even trained discriminator barely helps
- **Bootstrap significance**: FewNERD LP p<0.05, SciERC LP p=0.39 (n.s.)

## Anticipated Reviewer Concerns

1. **N=8 too small** → N-scaling to N=64 with 4-point monotonic curve, MV still <1pp
2. **LP always wins claim** → CORRECTED: dataset-dependent, CoNLL MV > LP
3. **Generalization** → 3 datasets × 3 models × 2 tasks
4. **Proposition 1 unrealistic** → Repositioned as motivating analysis
5. **Yao et al. overlap** → Entity-level vs task-level, diagnostic mechanisms, construction workaround
6. **Causal language** → Systematic audit, correlational framing throughout
7. **RE/SQL preliminary** → Scoped as preliminary evidence in Limitations
8. **Theory contribution limited** → Empirical characterization is primary, not theoretical
9. **No TTS improvement** → QE + diagnostic cascade + construction as triple contribution

## Venue Fit

EMNLP Main target. Strengths: systematic empirical comparison with mechanistic diagnosis, novel N-scaling evidence, cross-model/cross-dataset validation, entity-level construction as actionable workaround. Risk: "gains <1pp" may feel incremental to some reviewers, but diagnostic framework contribution is the main selling point.
