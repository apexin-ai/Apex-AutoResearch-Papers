# Paper Framing — simgate-modular-routing

## Target Venue
- **EMNLP 2026 Main Conference — Long Paper (8 pages + references)**
- Deadline: ARR May 25, 2026 (10 days remaining)
- D050: Upgraded from short paper (4p, Findings) per user directive

## Core Insight

**[D126 Framework-centric pivot]** We develop a **diagnostic framework** — episode-level counterfactual analysis — for understanding when and why deterministic computation helps LLM agents. Per-step oracle labeling degenerates to 97.4% ties in sparse-reward settings; our framework overcomes this by comparing complete episode outcomes under pure-internal and pure-deterministic strategies. Applied to ScienceWorld as a case study, the framework reveals that **death avoidance accounts for ~90% of routing signal** (78.9% of non-tie labels from death asymmetry [A]; DAF=90.41% at P=100 [A]; r=0.9698, p=8.12e-07 [A] across 11 task types / 245 episodes [A]; source: plan-012-full). The framework further diagnoses that routing is nearly unnecessary (oracle ≈ always-deterministic, 96.3% agreement [A]), turning the router negative result into a validated framework prediction rather than a limitation. The contribution is the reusable diagnostic methodology + the case study finding, not the router architecture itself.

## Core Claims (3 claims for long paper) — [D126 reordered: framework-first]

**C1 (Diagnostic framework: episode-level counterfactual analysis)**: Per-step oracle labeling degenerates in sparse-reward environments (97.4% tie rate on ScienceWorld). We propose episode-level counterfactual analysis — running complete episodes under pure-internal and pure-deterministic strategies — as a **reusable diagnostic framework** that overcomes this circularity and decomposes routing signal into interpretable components (death avoidance vs non-death performance). The framework produces three diagnostic outputs: (1) penalty-independent label fraction (what % of routing decisions stem from catastrophic failure?), (2) Death Avoidance Factor decomposition (how much of the performance gap is death-driven?), (3) oracle degeneracy detection (is routing necessary at all?). Router training on framework-produced labels yields an **informative negative**: episode-level independent eval 47.1±2.2% < majority-vote 50.0% (8-seed cross-split, D089), and data scaling (25%–800%) shows no improvement — consistent with the framework's diagnosis that signal is task-type-level, not step-level learnable.

**C2 (Case study finding: death avoidance dominates ScienceWorld routing)**: Applied to ScienceWorld (11 task types, 245 episodes [A]), the framework reveals that **death avoidance is the dominant routing mechanism**: 78.9% of non-tie labels from death asymmetry [A], DAF=90.41% at P=100 [A] (Δ_full=+29.60, Δ_nd=+2.84 [A]), r=0.9698 (p=8.12e-07) [A]. Death rates: internal 42.9% / deterministic 16.3% [A]. Episode-level label distribution: det-preferred 86 / internal-preferred 9 / no-preference 150 [A]. Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death) [A]. The framework further diagnoses oracle degeneracy: 96.3% of oracle decisions match always-deterministic [A], meaning routing is nearly unnecessary — a framework prediction validated by the router negative result (C1). Death dominance resists four axes of intervention: retry (48→43.5%), Reflexion (48→34%, DAF>100% at N≥3), 10× scaling to 72B (DAF=92.4%), and prompt warning (48→37%).

**C3 (Cross-validation: model families + environment boundary probes)**: 
- **Cross-model (ScienceWorld)**: Three architecturally distinct models independently converge on DAF 88–90% (spread 2.2pp, all 95% CIs overlapping): Qwen2.5-7B (DAF=90.4%, N=245), Llama-3.1-8B (DAF=88.2%, N=220, ΔDR=+30.0pp), Gemma-2-9B-it (DAF=89.7%, N=220, CI=[79.5, 98.4], sliding window attention vs full attention in Qwen/Llama). Internal death rates 36–43% across three families — death vulnerability is a task-environment property, not model-specific. Qwen-72B (N=255): DAF=92.4%, death dominance persists across capability levels.
- **Cross-model (ALFWorld)**: Llama-3.1-8B (135 games, 100% directional consistency, 16/16 non-tie labels favor deterministic) and Qwen2.5-7B (25.9% det-preferred, 94.6% directional consistency, 35/37 non-tie labels) both diagnose information asymmetry — not death — as the routing mechanism, without framework modification.
- **Cross-domain boundary probes**: MATH (N=795, code interpreter): no catastrophic failure → no routing signal (+0.5pp, McNemar p=0.81). MiniHack (n=40, 0% death) and Crafter (n=25, 100% death) produce no death asymmetry — boundary conditions where the mechanism is absent or universal.

**D013 note (updated for framework-centric)**: C2 no longer claims "selective > unconditional." Router ≈ always-det is a **framework prediction** (oracle degeneracy detected), not a limitation. Keyword heuristic structurally fails (D014) — further evidence that the signal the framework detects is not capturable by simple heuristics.

## Positioning vs Tool-Use Literature (Dream-driven addition)

**Critical gap identified by all 3 Dream tiers**: The core pipeline (counterfactual labels → SFT small classifier → selective invocation) is standard in tool-use learning. Must position against:
- **Toolformer** (Schick et al. 2024): Self-supervised tool-use learning via API call insertion. SimGate differs: hindsight labels from environment forking (not self-supervised), safety-aware framing (not general tool selection).
- **ART** (Paranjape et al. 2023): Automated tool selection via LLM reasoning. SimGate: dedicated lightweight router, not LLM-as-router.
- **Chameleon** (Lu et al. 2024): LLM-as-planner routing to diverse tools. SimGate: single modality (deterministic computation), explicit small router.
- **ToolkenGPT** (Hao et al. 2024): Token-level tool triggers. SimGate: step-level routing with counterfactual labels.

**Our differentiation** [D126 framework-centric]: (1) **Diagnostic framework**, not tool selector — we provide a reusable methodology for decomposing routing signal, not a better router. (2) Episode-level counterfactual labeling overcomes per-step oracle circularity (97.4% tie rate). (3) Framework produces interpretable diagnostics: label fraction, DAF decomposition, oracle degeneracy detection. (4) Router negative result is a **validated framework prediction** (oracle degeneracy → routing unnecessary → router should fail), not a limitation. (5) Cross-domain boundary probes (MATH, ALFWorld) demonstrate framework generalizability.

**Paper must include a dedicated Related Work section** (not just intro paragraphs). Minimum coverage: tool-use learning (Toolformer, ART, Chameleon), adaptive computation (CogRouter, ARES, Mixture-of-Depths), world model routing (ITP-R, Dyna-Think), agent frameworks (ReAct).

## Story Spine — [D126 framework-centric]

- **Problem**: LLM agents can route between internal reasoning and deterministic external computation (simulators, code interpreters), but existing approaches learn WHEN to route without understanding WHAT the routing signal actually captures. Per-step oracle labeling degenerates in sparse-reward settings (97.4% tie rate on ScienceWorld). Tool-use methods (Toolformer, ART, Chameleon) learn general tool selection but don't decompose WHY tool invocation helps. The field lacks a diagnostic methodology for understanding routing signal composition.

- **Our contribution**: We develop episode-level counterfactual analysis as a diagnostic framework. By comparing complete episode outcomes under pure-internal and pure-deterministic strategies, the framework decomposes routing signal into interpretable components and detects oracle degeneracy. **ScienceWorld case study**: the framework reveals death avoidance accounts for ~90% of routing signal [A] (78.9% of non-tie labels from death asymmetry), and diagnoses that routing is nearly unnecessary (96.3% oracle-det agreement). This dominance resists four axes of intervention (retry, Reflexion, 10× scaling, prompt warning). Cross-model replication across three architecturally distinct families (Qwen-7B: DAF=90.4%, Llama-8B: DAF=88.2%, Gemma-9B: DAF=89.7%; spread 2.2pp) confirms generality; Qwen-72B (DAF=92.4%) shows persistence at scale. Cross-domain probes (MATH: no death → no signal; ALFWorld: information asymmetry, not death; MiniHack/Crafter: boundary conditions) demonstrate framework applicability beyond the primary case study. Router training yields an informative negative (47.1% < majority-vote 50.0%) — a framework prediction, not a limitation.

- **Headline result template**: "We develop episode-level counterfactual analysis as a diagnostic framework for understanding when and why deterministic computation helps LLM agents. On ScienceWorld, the framework reveals that death avoidance accounts for 78.9% of routing labels and 88–90% of the performance gap (DAF) across three architecturally distinct model families (Qwen-7B, Llama-8B, Gemma-9B; spread 2.2pp), a finding that resists four standard agent improvements and persists at 72B scale. Cross-domain probes confirm the framework generalizes: ALFWorld diagnoses information asymmetry (not death); MATH finds no routing signal."

## Paper Structure (8-page long paper)

| Section | Pages | Content |
|---------|-------|---------|
| Abstract | 0.3 | Counterfactual analysis framing, death avoidance finding (multi-model), headline numbers, cross-domain evidence |
| Introduction | 1.2 | Problem (LLM catastrophic failures) + gap (per-step oracle degeneracy) + contribution (methodology + finding + cross-model/domain validation) |
| Related Work | 1.0 | Tool-use learning (Toolformer/ART/Chameleon/ToolkenGPT), adaptive computation (CogRouter/ARES/MoD), world model routing (ITP-R/Dyna-Think), safe RL, counterfactual-in-RL (Amitai/Gajcin/Olson) |
| Method | 1.5 | Full formalism: counterfactual framework definition, labeling pipeline (pseudocode/algorithm), DAF derivation + properties, router architecture, death decomposition framework |
| Experiments | 3.0 | §4.1 ScienceWorld death decomposition (core, Qwen2.5-7B); §4.2 Multi-model validation (Model B on same tasks); §4.3 Cross-domain negative contrast: MATH 795 problems (internal ≈ code interpreter → confirms death avoidance mechanism); §4.4 Temporal analysis + failure modes; §4.5 Ablations (router, labeling quality, keyword baseline structural failure) |
| Discussion | 0.5 | Implications for router design, scaling predictions (stronger models → lower death rate → lower DAF), when methodology applies vs doesn't |
| Conclusion | 0.5 | Summary + limitations + future work |
| References | ~1.0 | Not counted in 8-page limit |

## Anticipated Reviewer Concerns & Mitigations

1. **"Novelty is incremental — just SFT a small model to classify"**
   - Mitigation [D126 framework-centric]: Contribution is the **diagnostic framework** (episode-level counterfactual analysis), not the router. Router negative result is a **framework prediction** (oracle degeneracy detected → routing unnecessary → router should fail), not a limitation. R1 explicitly endorsed: "如果选择 framework-centric 路线，novelty 质疑就会被大幅缓解." Framework produces three diagnostic outputs applicable to any agent-tool routing scenario.

2. **"Only one benchmark (ScienceWorld)"**
   - Mitigation [UPGRADED for long paper]: Multi-model validation (§4.2) shows finding holds across model families. MATH 795-problem evaluation (§4.3) demonstrates cross-domain applicability (code interpreter as deterministic oracle). ALFWorld exploratory evidence in Discussion.

3. **"Comparison unfair — CogRouter uses RL (CoPO), you use SFT"**
   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.

4. **"Death avoidance is trivial — just always use deterministic"**
   - Mitigation: We do NOT claim selective > unconditional deterministic. Our contribution is the empirical finding that death avoidance dominates routing signal (~90% [A]), and the methodology that reveals this. Always-deterministic is a strong baseline — the interesting question is WHY (death avoidance), not WHETHER to route selectively. Plan-011 rule-based comparison + plan-012 death decomposition quantify this.

5. **"DAgger gap — SFT on pure-strategy trajectories may not transfer to mixed-strategy deployment"**
   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Plan C exacerbates this: router trains on always-internal/always-deterministic trajectories but deploys on mixed. Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension. Note: Plan C's episode-level labels avoid oracle circularity (no per-step tie-breaking), which is a methodological advantage even if distribution shift remains.

6. **"ScienceWorld's -100 penalty inflates gains"** (Dream all 3 tiers)
   - Mitigation: Report gains WITH and WITHOUT death episodes separately. If non-death gains are small, honestly acknowledge that the primary value is catastrophic failure prevention — this IS our framing. Also report: what fraction of routing labels are genuine vs tie-break artifacts.

7. **"Missing tool-use literature — this is just Toolformer"** (Dream all 3 tiers, CRITICAL)
   - Mitigation: Dedicated Related Work section. Position against Toolformer/ART/Chameleon. Differentiation: counterfactual trajectory labeling (not self-supervised), safety-aware framing (not general tool selection), explicit modular router (not LLM-as-router). (4) Episode-level counterfactual labeling — overcomes per-step oracle circularity in sparse-reward environments (97.4% tie rate).

8. **"Rule-based routing baseline missing"** (Dream median + worst)
   - Mitigation: **D014 resolved — keyword routing structurally fails.** Two keyword lists tested: v1 (generic verbs incl. connect) → ≈always-det (85.8%); v2 (science-only: heat/boil/melt/freeze) → ≈always-internal (4.9%, near-zero hits). ScienceWorld actions use generic interaction verbs, not science keywords. Paper positions this as "structural failure analysis" — keyword heuristics fundamentally cannot capture routing signal in this environment, supporting the need for learned/observation-based approaches. D014: keywords v2 (science-only verbs), v1 had connect/disconnect degeneracy.

## Venue Fit Risks (Long Paper, Main Track)

- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)
- Long paper needs: breadth (multi-model + cross-domain) + depth (temporal analysis + failure taxonomy) + methodology contribution
- Risk: "Analysis paper, no method contribution" — [D126] framework-centric pivot directly addresses this: C1 IS the methodology contribution. Algorithm box + formal definitions + three diagnostic outputs elevate from ad hoc to principled.
- Risk: "Death avoidance is the only signal" — mitigate: multi-model validation shows it's a general phenomenon; MATH shows methodology generalizes; Discussion section addresses when/why this applies.
- Risk: Router ≈ always-det → [D126] reframed as framework prediction (oracle degeneracy detected), not novelty concern. **D014: keyword routing structurally fails** — further validates framework's diagnostic value.
- Risk: Scaling concern (stronger models → less death → less routing signal) — address honestly in Discussion as a feature not bug: the methodology DETECTS when routing adds value.

## Key Differences from IDEA_BRIEF / Short Paper

1. **D050 scope expansion**: From short paper (4p, ScienceWorld only) to long paper (8p, multi-model + cross-domain).
2. **C3 added**: Cross-model generality claim (pending multi-model experiment).
3. **MATH upgraded**: From "future work" to §4.3 full evaluation (795 problems).
4. **Structure**: Full Related Work + Discussion sections; Method expanded with formalism.
5. **D126 Framing pivoted**: From finding-centric ("we found death avoidance dominates") to framework-centric ("we develop a diagnostic framework; ScienceWorld case study reveals death avoidance dominates"). R1 endorsed this pivot.

## Robustness Check (30-task prescreening, appendix only)

A broader prescreening analysis across 30 task types / 249 episodes [B] provides robustness support: Δ_full=+38.33 [B], Δ_nd=+0.48 [B], DAF=98.75% [B], r=0.9864 [B]. The higher DAF in prescreening reflects the inclusion of many low-n task types where death dominance is even more pronounced. These numbers appear only in the appendix.

## 数据源权威声明

- **主表（A）**: plan-012-full, 11 tasks / 245 episodes — 所有主文引用
- **Robustness（B）**: prescreening, 30 tasks / 249 episodes — 仅 appendix
- **绝对不引用**: death_decomposition_report.json（文件名误导，实际是 30-task 数据）
- **绝对不引用**: results/plan_c_test_labels/implicit_sft.jsonl（标签损坏，no-preference→internal 映射错误）
