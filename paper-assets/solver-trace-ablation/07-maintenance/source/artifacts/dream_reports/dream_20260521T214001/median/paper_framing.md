# Paper Framing — solver-trace-ablation

## Target Venue
- **EMNLP 2026 Main** (NLP and Symbolic Reasoning track)
- Deadline: ARR May 25, 2026

## Core Claims (3 条 — Goodhart 主线诊断/分析论文)

| Claim | Status | 闭环标志 |
|-------|--------|----------|
| Claim 1: STA 诊断能力 | ✅ 已闭环 → 🔄 扩展中 (cross-scale) | 5-seed (s42-s46) + 1000-step trajectory + hacking taxonomy (9 modes). **Planned**: +8B 3-seed cross-scale (plan_021), +s45/s46 1000-step (plan_020) |
| Claim 2: Goodhart inevitable + ISR double-edged | ✅ 已闭环 → 🔄 扩展中 | 5-seed ISR + 5-seed random β=0.1 + premise-count-matched + SFT baseline + 1.7B cross-scale + β=0.05 no-safe-dose. **Planned**: +3 ISR seeds (plan_022), +8B ISR stretch (plan_023) |
| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: 3/3 gaming — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |

### Claim 1: ISR as Reward Hacking Diagnostic ✅
STA derives ISR via LOO ablation on solver inputs. ISR detects reward hacking that prove_rate misses: exec-only GRPO achieves PR=93% but ISR collapses 0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步).

**Evidence (compact)**:
- 5-seed exec-only (s42-s46): All show ≥90% structural degeneration (H1+H7+H8). s42: H1=87.1%; s43: PR=13% collapse; s44: H7=100%; s45: TS=93.9%, genuine=1.0%; s46: CE=89.2%, genuine=9.7%
- 1000-step trajectory (s42): ISR collapses 99.6% (0.6423→0.0027), 94.8% proved samples ISR=0
- Hacking taxonomy: 9 distinct modes (CE, TS, PG, H7a/b, H8, H9, degenerate-syntax, query-as-fact)
- SFT baseline: PR=14%, 92.9% genuine — confirms hacking is RL-reward-specific
- **Planned**: Qwen3-8B exec-only 3 seeds (plan_021) for cross-scale validation; s45/s46 1000-step extension (plan_020) for N=3 trajectory evidence

### Claim 2: ISR as Reward — Inevitable Goodhart Collapse ✅
ISR has inherent structural bias: P→P tautologies receive ISR≥0.5, creating a positive feedback loop. β controls timing not destiny.

**Key findings (5-seed primary)**:
- ISR β=0.1: genuine 22.6% vs Random 7.7% (OR=3.48, p<10⁻⁸; CMH OR=3.37, p<10⁻⁹), BUT H7 54.3% vs 29.5% (OR=2.84, p<5×10⁻¹²) → double-edged sword
- Genuine advantage is selection effect (proportion), not quality (premise-matched ISR 1.06×)
- Transient: 1000步 genuine 17%→2%; s45 55%→0%
- β=0.05: 2/2 seeds deterministic H7 (97-100%) — no safe dose
- β=0.3: multi-modal instability (PR=66±42%, 3 different failure paths)
- Non-monotonic dose-response: β=0.05 deterministic → β=0.1 bimodal → β=0.2 deterministic → β=0.3 multi-modal
- H7b obfuscated tautology (ISR s44): meta-Goodhart triple gaming (execution + ISR + detector evasion)
- 3-seed vs 5-seed: H7 OR collapsed 15.05→2.84; genuine reversed from n.s. to OR=3.48 (s45/s46 addition)
- Stochastic bifurcation: 2/5 seeds collapse immediately, 3/5 sustain transient genuine window
- **Planned**: +3 ISR β=0.1 seeds (plan_022) for N=8; +Qwen3-8B ISR stretch (plan_023)

### Claim 3: Cross-Logic Diagnostic Transfer ✅
STA transfers across formal languages: Prolog→SWI-Prolog shows same degeneration.

**Evidence**:
- Prolog exec-only 3-seed: PR=53.3%±31.1%, ISR near-zero (2/3 seeds <0.04)
- Prolog STA 3-seed: **3/3 seeds gaming, 0% genuine** — universal Goodhart
  - s42: Clean H7 (100%), s43: Degenerate syntax (97.4% H1, functional H7), s44: Query-as-fact gaming (97.9% functional H7, Reviewer-corrected from initial "100% genuine")
- Prolog gaming more extreme than FOL (0% vs ~6% genuine residual) — simpler semantics → more complete hacking

### Cross-Scale Evidence: Qwen3-1.7B
- Random β=0.1: PR=93%, H9=100% (contradiction explosion, ISR≈0)
- ISR β=0.1: PR=100%, ISR=0.6 zero-variance, H1=100% (fixed template gaming)
- ISR β=0.3: PR=17%, genuine=29.4% (learning suppression)
- Capacity-dependent Goodhart basins: 4B→H7 (sophisticated tautology), 1.7B→H1 (simplest exploit)
- Confirms: ISR gaming transfers across scales, only strategy differs

## ISR Capability Boundary
ISR measures syntactic necessity, NOT semantic faithfulness. Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, n.s.). Treated as Limitation.

## Story Spine
- **Problem**: GRPO with exec-only rewards produces structurally degenerate outputs while achieving high prove rates. No diagnostic exists.
- **Gap**: No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools.
- **Contribution**: STA (LOO ablation → ISR) as diagnostic. Key findings: (1) ISR quantifies hacking invisible to PR; (2) ISR contains inherent Goodhart vulnerability (tautologies get ISR≥0.5); (3) double-edged at β=0.1 (more genuine AND more H7); (4) stochastic bifurcation; (5) 9-mode hacking taxonomy; (6) transfers across logic types (Prolog) and model scales (1.7B); (7) β=0.05 confirms no safe dose; (8) premise-count confound is methodological contribution.
- **Headline**: ISR reliable as diagnostic, unreliable as optimization target at any dose. β controls when collapse occurs, not whether.

## Venue Fit Risks
- **EMNLP fit**: Diagnostic/analysis paper, empirical findings + mechanistic insight
- **"Just negative results"**: ISR as diagnostic IS positive (C1); meta-Goodhart is novel mechanistic insight; 9-mode taxonomy is actionable
- **"Old wine"**: ISR = LOO ablation. Novelty at application level + empirical findings
- **"Single-logic"**: Prolog validates (3/3 gaming, 0% genuine)
- **"Single-model" (MF-7)**: **Planned**: Qwen3-8B cross-scale (plan_021). Combined with 1.7B → 3 scale points (1.7B/4B/8B)

## Anticipated Reviewer Concerns
1. **"ISR is just LOO ablation"** — Acknowledge. Contribution is application + Goodhart analysis + taxonomy.
2. **"β=0.1 success is one seed"** — 5-seed: 3/5 sustain genuine window (transient). OR=3.48 but premise-matched 1.06×.
3. **"Conclusion embedding invalidates"** — GRPO-universal (both conditions). Random H1 higher (58.5% vs 18.3%).
4. **"Goodhart obvious"** — Conceptual yes; empirical characterization in formal GRPO is not. Meta-Goodhart novel.
5. **"No positive result"** — ISR diagnostic IS positive. Negative on ISR-as-reward IS the contribution.
6. **"ISR circular"** — Validated: ISR reward → ISR-specific gaming. Use for diagnosis only.
7. **"Only one logic"** — Prolog: 3/3 gaming, 0% genuine (stronger than FOL).
8. **"500 steps too short"** — 1000-step: ISR 0.123→0.003 (-97.8%).
9. **"Seeds insufficient"** — 5-seed exec-only, stochastic bifurcation IS the finding.
10. **"2.4x was wrong"** — Transparent correction. 5-seed OR=3.48 confirms genuine proportion advantage; quality same (1.06×).
11. **"Premise count obvious"** — LOO metrics widely used without this correction. Documenting it is methodological.
12. **"Can't act on this"** — 7 actionable insights. ISR + component count diagnostic deployable.
13. **"Prolog s44 misclassified"** — Transparent correction; classifier blind spot is itself a finding.
14. **"ISR has genuine benefit — why not use?"** — Transient (17%→2%). Same LOO bias rewards tautologies. No stable operating point.
15. **"Only 2 seeds at β=0.05"** — 2/2 deterministic collapse already strong evidence.
16. **"Only one model (Qwen3-4B)" (MF-7)** — **Planned**: 8B cross-scale (plan_021). Combined with 1.7B → 3 scale points. LLaMA-3.2-3B establishes lower capability bound (PR≈15%).
17. **"N=3 seeds insufficient" (MF-1)** — Already N=5 exec-only (s42-s46, all ≥90% degeneration). Planned: s45/s46 to 1000 steps + 3 more ISR seeds for N=8.

## Discussion Notes
- **Hack mode switching**: GRPO degeneration mode is seed-determined. Single-seed results unreliable.
- **H7 OR revision**: 3-seed OR=15.05 → 5-seed OR=2.84. ISR modestly increases H7; mode selection stochastic.
- **Genuine OR reversal**: 3-seed n.s. → 5-seed OR=3.48. ISR double-edged. Quantity not quality, transient.
- **Non-monotonic dose-response**: β=0.05 deterministic → β=0.1 bimodal → β=0.2 deterministic → β=0.3 multi-modal.

## Detailed Data Reference
Full per-seed data tables, statistical tests, and internal tracking notes preserved in `paper_framing_full_backup.md`.
