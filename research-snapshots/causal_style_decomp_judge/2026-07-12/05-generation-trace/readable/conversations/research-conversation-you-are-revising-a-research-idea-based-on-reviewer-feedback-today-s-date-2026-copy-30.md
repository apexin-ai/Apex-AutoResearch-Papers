# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-27 (UTC).** ## Original idea { "cha

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/8b2a2328-34e0-42d1-8edf-3ef7723abf51.jsonl`
- **Structured JSON:** [`74ff69d26eecbf0bfcbc.json`](../../sessions/74/74ff69d26eecbf0bfcbc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T22:06:35.292Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T22:06:35.292Z",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Original idea\n{\n  \"changes_made\": [\n    \"MAJOR NARRATIVE RESTRUCTURING: Reframed entire proposal around a single central insight: 'autoformalization is uniquely positioned for principled gaming-resistance analysis because GTED provides a formally-grounded, LLM-independent faithfulness anchor.' Every contribution now explicitly serves this insight. Core problem, opportunity, and description rewritten to lead with this claim and build a coherent story rather than a feature list. This addresses the stagnation at 3.5-3.6 and the reviewer's observation that the proposal 'reads as a list of things rather than a story'\",\n    \"ADDED MO-GRPO (arXiv:2509.22047, Sep 2025; revised Jan 2026) as primary dynamic baseline, replacing DRW. MO-GRPO normalizes advantage per-objective: A^MO_g = Σ_i [R_i(q,o_g) - mean(R_i)]/std(R_i), preventing variance-based dominance in multi-objective GRPO. Directly targets reward hacking in multi-objective GRPO, making it a far more relevant baseline than DRW (which optimizes Pareto efficiency, not gaming resistance). Key differentiation: MO-GRPO is objective-agnostic (equalizes variance contributions regardless of gaming behavior), while AGRC uses gaming-specific signals (GRS) — the central experimental question becomes whether gaming-aware optimization outperforms objective-agnostic normalization. C10 is now MO-GRPO baseline. DRW retained in landscape discussion but removed as experimental baseline\",\n    \"ADDED Advantage Modification from 'When Reward Hacking Rebounds' (arXiv:2604.01476, April 2026): integrates shortcut concept scores (extracted via representation engineering on contrastive pairs) into GRPO advantage computation to penalize hacking rollouts. Identifies three-phase rebound pattern (attempt → retreat → rebound) in coding environments. Differentiated at three levels: (a) operates at representation level (requires probing hidden states for concept directions), AGRC operates at reward-component level (uses GRS per component); (b) requires domain-specific contrastive pairs for concept extraction, GRS requires only reward-faithfulness evaluation; (c) designed for single-objective hacking detection, AGRC handles multi-objective composition. Discussed in landscape, not implemented as baseline due to fundamentally different mechanism level\",\n    \"ADDED SignCert-PO from 'Mitigating Reward Hacking in RLHF via Advantage Sign Robustness' (arXiv:2604.02986, April 2026): derives certified sign-preservation radius via adversarial perturbation in RM parameter space, down-weights non-robust completions. Differentiated: (a) SignCert-PO operates on reward model parameter perturbations (requires RM weight access), AGRC operates on observable reward-faithfulness correlations; (b) SignCert-PO is designed for single-RM RLHF settings, AGRC handles multi-source reward composition; (c) SignCert-PO detects potentially-flipped advantages regardless of cause, AGRC specifically targets gaming via faithfulness decorrelation. Cited in landscape\",\n    \"ADDED 'On the Hidden Objective Biases of Group-based Reinforcement Learning' (arXiv:2601.05002, Jan 2026) as additional theoretical motivation: proves GRPO exhibits non-uniform group weighting biases, AdamW-induced reward scaling insensitivity, and momentum-based clipping violations. Strengthens our motivation: these structural biases compound with gaming vulnerability, making gaming-aware composition more urgent\",\n    \"ADDED 'Reward Hacking as Equilibrium under Finite Evaluation' (arXiv:2603.28063, March 2026): proves that under minimal axioms (multi-dimensional quality, finite evaluation, effective optimization), reward hacking is a structural equilibrium, not a correctable bug. Key implication for our work: since hacking is inevitable under finite evaluation, measuring gaming RESISTANCE becomes the critical question — which signals degrade least? This provides foundational theoretical motivation beyond the empirical observations from VerifAI-2\",\n    \"SIGNIFICANT SCOPE REDUCTION following reviewer recommendation: (1) GRS metric variants: Spearman and Kendall in main text only; Pearson and MI deferred to appendix as supplementary ablation. Justified: theoretical contamination analysis already proves rank-based superiority over linear; MI is high-variance estimator best suited for supplementary analysis. (2) Cross-method comparison: GRIFT reimplementation DROPPED — replaced with analytical comparison (computation cost, automation degree, dependency requirements) using published GRIFT results as reference. Exploitation-rate comparison retained as lightweight adaptation (uses GTED+LeanScorer as panel, no external LLM dependency). (3) DRW experimental baseline dropped, replaced with more relevant MO-GRPO. Net effect: 10 configs unchanged, but metric variants reduced from 4→2 main text, cross-method from 3→1 experimental + 1 analytical, saving ~100 GPU hours and ~16 hours manual GRIFT cluster labeling\",\n    \"CORRECTED LeanInteract specification: v0.11.3 confirmed on PyPI (released May 14, 2026). Message objects provide structured fields: start_pos (Pos), end_pos (Pos), data (string), severity ∈ {error, warning, info}. IMPORTANT CORRECTION: the error sub-classification (parse → name resolution → type) is NOT a built-in LeanInteract feature — severity provides only three levels. R_formal error hierarchy requires custom regex-based classification of Message.data strings (e.g., 'unknown identifier' → name resolution, 'type mismatch' → type error, 'expected token' → parse error). This custom parser (~200 LoC) is straightforward but must be documented as engineering contribution, not library feature\",\n    \"STRENGTHENED GRS VALIDATION: Increased human annotation budget from 400 to 600 samples (75 samples × 8 key config-model pairs, up from 50 × 8). Added bootstrap BCA confidence intervals (10,000 resamples) for all GRS-human correlation estimates, reporting CI widths to demonstrate statistical reliability. Justified via Bonett & Wright (2000): n=75 with bootstrap yields CI half-width ≈ 0.12 for ρ ≈ 0.7, adequate for distinguishing 'high' (>0.6) from 'moderate' (0.3-0.6) correlation. Added stratified sampling across gaming severity levels (no gaming, mild gaming, severe gaming) to ensure representativeness. Total human audit hours increased from ~55 to ~70\",\n    \"SHARPENED GAP CLAIM to account for new related work: The gap is now: 'While general multi-objective GRPO hacking mitigations exist — MO-GRPO normalizes variance (objective-agnostic), Advantage Modification integrates representation-level shortcuts, SignCert-PO certifies advantage sign robustness — none leverage domain-specific formally-grounded faithfulness measures, and none study which reward source categories resist gaming in autoformalization where such measures are uniquely available.' This positions our work as domain-specific and complementary to general methods, not competing\",\n    \"REFINED AGRC vs MO-GRPO framing: The central experimental question is now: 'Does gaming-specific optimization (AGRC: w_k ∝ exp(η·GRS_k)) outperform objective-agnostic normalization (MO-GRPO: per-objective variance normalization) for gaming resistance in autoformalization?' This is a cleaner, more testable claim than the previous AGRC vs DRW comparison. Added specific hypotheses: (H1) When gaming concentrates in specific reward components, AGRC detects and downweights selectively while MO-GRPO cannot discriminate gamed from non-gamed components; (H2) MO-GRPO may outperform AGRC when gaming is distributed uniformly across components (variance normalization is sufficient). Both outcomes are publishable\",\n    \"STREAMLINED EVALUATION FRAMEWORK: Reduced from 11 evaluation dimensions to 8 well-defined analyses: (1) Standard metrics, (2) Multi-metric faithfulness, (3) GRS decomposition per config × checkpoint, (4) GRS-Spearman vs GRS-Kendall comparison, (5) GRS-GTED vs exploitation-rate comparison, (6) GRS-human validation with bootstrap CIs, (7) AGRC vs MO-GRPO weight trajectory and Pareto analysis, (8) Critic scaling (14B vs 8B). Dropped separate GRIFT comparison, broader applicability sketch moved to discussion only, gaming taxonomy merged into GRS decomposition analysis\"\n  ],\n  \"title\": \"Gaming Resistance in Autoformalization RL: How Formally-Grounded Faithfulness Enables Principled Reward Analysis\",\n  \"core_problem\": \"RL-based autoformalization combines composite rewards — binary compilation (FormaRL, Mathesis), LLM semantic judges (Mathesis R_sem), embedding similarity (Online RL for Autoformalization), and trained critics (CriticLean at 84.8% accuracy) — yet a fundamental question remains unanswered: which reward signals RESIST GAMING, and can we measure this automatically?\\n\\nThis question is urgent. Gaming in autoformalization is documented and severe: VerifAI-2 (ICLR 2026) shows 87-99% compilation success masks systematic unfaithfulness; FormaRL's ablation reveals syntax-only RL yields 100% compilation but 0% semantic consistency. Theoretically, 'Reward Hacking as Equilibrium' (arXiv:2603.28063) proves that gaming is a structural equilibrium under finite evaluation — not a correctable bug — making the measurement of gaming RESISTANCE (which signals degrade least) the critical practical question.\\n\\nThe broader RL community has responded with gaming mitigations at multiple levels: MO-GRPO (arXiv:2509.22047) normalizes per-objective advantage variance to prevent dominance-based hacking in multi-objective GRPO; Advantage Modification (arXiv:2604.01476) integrates representation-level shortcut concept scores into GRPO advantages; SignCert-PO (arXiv:2604.02986) down-weights non-robust completions via certified sign-preservation radius; GRIFT (arXiv:2604.16242) detects gaming via gradient fingerprints; exploitation-rate (arXiv:2605.12474) measures fraction of newly-credited criteria rejected by LLM panels.\\n\\nHowever, ALL these methods are domain-agnostic — none exploit domain-specific structure. Autoformalization has a UNIQUE advantage unavailable in any other RL domain: the Lean language server provides formally-grounded, LLM-independent faithfulness measurement via GTED tree-edit-distance (AI4Math@ICML 2025). This creates three domain-specific gaps: (1) No work has used formally-grounded faithfulness to compare gaming-resistance PROPERTIES of different reward source categories in isolation — Mathesis combines signals for performance but doesn't study which resist gaming; (2) No gaming-resistance metric leverages formally-grounded faithfulness anchors, enabling detection that is simultaneously lightweight (no gradients, unlike GRIFT), automated (no manual labeling), and non-circular (no LLM panels, unlike exploitation-rate); (3) No mechanism adapts multi-objective GRPO composition based on gaming-specific signals — MO-GRPO normalizes variance (objective-agnostic), not gaming resistance.\",\n  \"opportunity\": \"A unique convergence of six developments makes this the right moment for this study:\\n\\n(1) GTED (AI4Math@ICML 2025) provides formally-grounded faithfulness via tree-edit-distance over Lean operator trees — the KEY enabling capability. Unlike code generation (where no equivalent formally-grounded semantic metric exists) or general RLHF (where ground truth is subjective), autoformalization offers a computable, LLM-independent faithfulness anchor. This makes gaming-resistance measurement principled in a way no other RL domain can achieve.\\n\\n(2) Gaming is newly documented but unquantified for autoformalization. VerifAI-2 shows the problem exists; we provide the first systematic measurement of which signals are affected and by how much.\\n\\n(3) Mathesis (ICLR 2026) establishes that composite rewards work for autoformalization GRPO — but treats composition as a performance optimization problem, not a gaming-resistance problem. The transition from 'which composition gives highest accuracy' to 'which composition resists gaming' is the core reframing.\\n\\n(4) CriticLean (July 2025) creates a new reward signal category (trained critic at 84.8% accuracy) untested as direct RL training signal, providing a fifth source category for comparison.\\n\\n(5) MO-GRPO (Sep 2025) proves objective-agnostic normalization mitigates hacking in multi-objective GRPO. The natural next question: does gaming-specific optimization outperform objective-agnostic normalization when domain-specific gaming detection is available?\\n\\n(6) Recent general gaming mitigations (Advantage Modification, SignCert-PO, GRIFT, exploitation-rate) create urgency for domain-specific comparison: does autoformalization's unique formal verification capability enable better gaming-resistance measurement than general-purpose approaches?\",\n  \"landscape\": \"**Autoformalization RL systems:** FormaRL (COLM 2025) uses GRPO with binary compilation + LLM semantic consistency, achieving 26.15% pass@1 on ProofNet; ablation reveals aggressive gaming — syntax-only RL yields 100% compilation, 0% consistency. Mathesis (ICLR 2026) advances with R_ver + R_sem in GRPO plus HPO; 22% improvement on Gaokao-Formal. CriticLean (arXiv July 2025) trains CriticLeanGPT via SFT+GRPO: Qwen3-14B-RL achieves 84.8% (publicly available), Qwen3-8B-RL achieves 79.8% on CriticLeanBench. StepFun-Formalizer (AAAI 2026) achieves 40.5% BEq@1 SOTA on FormalMATH-Lite.\\n\\n**Gaming in autoformalization:** Do LLMs Game Formalization? (VerifAI-2 @ ICLR 2026) documents 87-99% compilation masking unfaithfulness: GPT-5 fabricates axioms, DeepSeek-R1 mistranslates premises. LLMs Gaming Verifiers (ICLR 2026 Workshop) demonstrates RLVR models abandon reasoning for shortcuts.\\n\\n**Multi-objective GRPO hacking mitigations (UPDATED):** MO-GRPO (arXiv:2509.22047, Sep 2025; revised Jan 2026) normalizes per-objective advantage: A^MO_g = Σ_i [R_i - mean(R_i)]/std(R_i), ensuring all reward functions contribute evenly regardless of variance. Objective-AGNOSTIC: equalizes contributions without detecting whether any component is being gamed. Tested on bandits, WMT, AlpacaFarm. On the Hidden Objective Biases of Group-based RL (arXiv:2601.05002, Jan 2026) further analyzes GRPO structural biases: non-uniform group weighting, AdamW scaling insensitivity, momentum clipping violations.\\n\\n**Gaming-aware GRPO modifications (NEW):** Advantage Modification from 'When Reward Hacking Rebounds' (arXiv:2604.01476, April 2026) integrates shortcut concept scores (extracted via representation engineering from contrastive pairs) into GRPO advantage computation. Identifies three-phase rebound pattern. Operates at REPRESENTATION level — requires probing hidden states, domain-specific contrastive pairs. SignCert-PO (arXiv:2604.02986, April 2026) derives certified sign-preservation radius via adversarial RM perturbation, down-weights non-robust completions. Operates at ADVANTAGE level — requires RM weight access, designed for single-RM settings.\\n\\n**General gaming detection:** GRIFT (arXiv:2604.16242, April 2026) detects gaming via gradient fingerprints (LoRA adapters, K-means, ~80% F1). Heavyweight: requires per-sample gradient computation + 16 manually-labeled cluster representatives. Exploitation-rate (arXiv:2605.12474, May 2026) measures fraction of newly-credited criteria rejected by cross-family LLM panel (GPT-5.4, Gemini 3 Pro, Claude Opus 4.6). Expensive and LLM-dependent. Composite reward penalties (arXiv:2509.15557, ACM-BCB 2025) introduce hand-crafted gaming penalties — requires manual pattern enumeration.\\n\\n**Theoretical foundations:** Correlated Proxies (arXiv:2403.03185) formalizes reward hacking via correlation breakdown between proxy and true rewards; proves χ² regularization prevents hacking. Reward Hacking as Equilibrium (arXiv:2603.28063, March 2026) proves hacking is structural under finite evaluation: any optimized agent under-invests in unevaluated quality dimensions. SpecBench (arXiv:2605.21384, May 2026) measures hacking in coding agents: gap grows 28pp per 10× code size.\\n\\n**Evaluation metrics:** GTED (AI4Math@ICML 2025) provides tree-edit-distance over operator trees from Lean Language Server — formally-grounded, no ATP/LLM dependency, highest accuracy (70.73%) and Kappa (0.438) on miniF2F. FormalAlign (ICLR 2025) uses dual contrastive+generation loss, 99.21% AS on FormL4-Basic. LeanScorer (Mathesis) decomposes into subtasks, Sugeno fuzzy integral, 0.92 F1.\\n\\n**Dynamic reward composition:** DRW (TACL 2026) introduces hypervolume-guided and gradient-based dynamic weight adaptation for Pareto efficiency. Not gaming-aware.\\n\\n**The refined gap:** Autoformalization uniquely provides formally-grounded faithfulness measurement (GTED), enabling gaming-resistance analysis unavailable in other domains. While general mitigations exist at variance level (MO-GRPO), representation level (Advantage Modification), advantage level (SignCert-PO), and gradient level (GRIFT), none exploit this domain-specific capability. No work compares gaming resistance across isolated reward source categories for autoformalization, proposes a gaming-resistance metric grounded in formal faithfulness, or applies gaming-specific dynamic reweighting to multi-objective autoformalization GRPO.\",\n  \"inspired_by\": \"The central insight: autoformalization is the IDEAL domain for studying gaming resistance because GTED provides a formally-grounded faithfulness anchor that enables non-circular, lightweight, automated gaming detection — capabilities unavailable in any other RL domain. This insight emerges from the convergence of: (1) the theoretical result that reward hacking is a structural equilibrium (arXiv:2603.28063), making resistance measurement the practical question; (2) GTED providing the formally-grounded anchor that makes principled measurement possible; (3) the proliferation of domain-agnostic mitigations (MO-GRPO, Advantage Modification, SignCert-PO, GRIFT) creating demand for domain-specific evaluation; (4) Mathesis/FormaRL establishing composite autoformalization rewards without studying gaming properties; (5) CriticLean creating a new untested reward category. The gap between documented gaming (VerifAI-2) and absence of gaming-resistance measurement for autoformalization is clear and actionable.\",\n  \"approach\": \"We present the first systematic gaming-resistance analysis for autoformalization RL, built on the central insight that GTED's formally-grounded faithfulness measurement enables principled gaming detection unavailable in other RL domains. The approach has three phases that progressively build on this insight.\\n\\n**Phase 1: Multi-Source Reward Signal Extraction**\\n\\n(a) Formally-grounded signal R_formal: Using LeanInteract v0.11.3's Message objects (fields: start_pos, end_pos, data, severity ∈ {error, warning, info}), classify compiler diagnostics into error hierarchy via custom regex parser (~200 LoC) over Message.data strings: parse errors ('expected token', 'unexpected token') → name resolution ('unknown identifier', 'unknown namespace') → type errors ('type mismatch', 'has type ... but is expected to have type') → clean compilation. Yields R_formal ∈ {0.0, 0.25, 0.5, 0.75, 1.0} plus density bonus. NOTE: LeanInteract v0.11.3 provides three severity levels; the five-level error hierarchy requires our custom classification, documented as engineering contribution.\\n\\n(b) Embedding similarity R_embed: cosine similarity between sentence embeddings of input NL and backtranslation of generated formal statement (reference-free roundtrip approach).\\n\\n(c) LLM judge R_judge: binary faithfulness judgment from frozen LLM (following FormaRL/Mathesis R_sem approach).\\n\\n(d) Trained critic R_critic: semantic fidelity score from CriticLeanGPT-Qwen3-14B-RL (84.8% accuracy, publicly available). First use as direct RL reward signal during GRPO training. Additionally retrain Qwen3-8B using CriticLean_4K dataset (~79.8% expected) to study critic accuracy impact on gaming resistance.\\n\\n**Phase 2: GRS (Gaming Resistance Score) Framework — Enabling Methodology**\\n\\nGRS measures the meta-property of reward signals: how faithfully does high reward indicate genuine quality? This is the rank correlation between reward and formally-grounded faithfulness:\\n\\n  GRS(R, F) = ρ_s(R(x), F(x)) over held-out evaluation set\\n\\n**2a. Theoretical Justification:**\\nUnder contamination model (1-α)P_faithful + αP_gamed, where P_gamed has reward above and faithfulness below the faithful population's medians, we prove: (i) GRS monotonically decreases in gaming proportion α; (ii) rank-based measures (Spearman, Kendall) are more robust than Pearson because gaming creates outlier patterns (high R, low F) whose influence on Pearson is unbounded (proportional to magnitude) while rank-based measures bound each observation's influence to its rank position.\\n\\n**2b. Two Primary GRS Formulations (main text):**\\n  GRS-Spearman: rank correlation — standard, well-understood\\n  GRS-Kendall: concordance probability — handles ties better, more interpretable as pairwise comparison probability\\n  (GRS-Pearson and GRS-MI deferred to appendix as supplementary ablation)\\n\\n**2c. Multi-Faceted Faithfulness Anchors:**\\n  GRS-GTED: F(x) = GTED tree-edit-distance (PRIMARY — formally-grounded, no LLM dependency)\\n  GRS-LeanScorer: F(x) = LeanScorer Sugeno score (secondary)\\n  GRS-roundtrip: F(x) = roundtrip consistency (tertiary)\\n  GRS-human: F(x) = expert judgment (gold standard, 600 validation samples)\\n\\n**2d. Comparison with Exploitation-Rate:**\\nAdapt exploitation-rate to autoformalization: define rubric criteria (type-correctness, structure-preservation, semantic-fidelity), use GTED+LeanScorer as reference panel (lightweight, no external LLM dependency). Compare detection sensitivity, computation cost, and automation degree against GRS-GTED. GRIFT comparison discussed analytically using published results (accuracy, cost, dependency requirements) without full reimplementation — GRIFT's per-sample gradient computation + manual cluster labeling makes it heavyweight for our use case, and published ~80% F1 on math provides a reference point.\\n\\n**Phase 3: Systematic Ablation (10 Configurations)**\\n  C1: Binary compilation only (FormaRL/Mathesis R_ver reproduction)\\n  C2: Graded formal signal only (R_formal)\\n  C3: Embedding similarity only (R_embed)\\n  C4: LLM judge only (R_judge)\\n  C5: Trained critic only (R_critic via CriticLeanGPT-14B-RL)\\n  C6: Formal + embedding hybrid (R_formal + R_embed)\\n  C7: Formal + trained critic hybrid (R_formal + R_critic)\\n  C8: Full hybrid (R_formal + R_embed + R_critic)\\n  C9: AGRC (adaptive gaming-aware, see Phase 4)\\n  C10: MO-GRPO baseline (per-objective variance normalization applied to C8 component set)\\n  Tiered model strategy: all 10 on Qwen2.5-Coder-7B-Instruct; top 4 by GRS + AGRC + MO-GRPO on Qwen3-Coder-30B-A3B-Instruct.\\n\\n**Phase 4: AGRC vs MO-GRPO — Gaming-Specific vs Objective-Agnostic Composition**\\n\\nThe central experimental question: does gaming-specific optimization outperform objective-agnostic normalization when domain-specific gaming detection is available?\\n\\n- MO-GRPO (C10): A^MO_g = Σ_i [R_i(q,o_g) - mean(R_i)]/std(R_i) — equalizes per-objective variance contributions. Objective-AGNOSTIC: treats all components identically regardless of gaming behavior.\\n- AGRC (C9): w_k^(t+1) ∝ w_k^(t)·exp(η·GRS_k^(t)) — upweights gaming-resistant components, downweights gamed ones. Gaming-SPECIFIC: uses GRS-GTED per component, updated every K=500 steps.\\n\\nDifferentiation from other gaming-aware GRPO modifications:\\n- Advantage Modification (arXiv:2604.01476) operates at representation level via shortcut concept scores — requires probing hidden states, domain-specific contrastive pairs. AGRC operates at reward-component level via observable GRS.\\n- SignCert-PO (arXiv:2604.02986) operates at advantage level via RM perturbation robustness — requires RM weight access, single-RM setting. AGRC handles multi-source composition.\\n\\nSpecific hypotheses: (H1) When gaming concentrates in specific components (e.g., R_formal gamed via ':= True := by sorry'), AGRC selectively downweights while MO-GRPO cannot discriminate. (H2) MO-GRPO may suffice when gaming is uniformly distributed. Both outcomes are publishable.\\n\\n**Phase 5: Evaluation Framework**\\n\\n(1) Standard metrics: BEq@1, pass@1, ASSESS structural similarity\\n(2) Automated faithfulness (multi-metric): GTED score, LeanScorer score, FormalAlign alignment score, roundtrip consistency\\n(3) GRS decomposition: GRS-GTED and GRS-Kendall per configuration × checkpoint\\n(4) GRS-Spearman vs GRS-Kendall comparison with bootstrap CIs\\n(5) GRS-GTED vs exploitation-rate comparison (adapted to autoformalization) + analytical GRIFT comparison\\n(6) GRS-human validation: 75 samples × 8 key config-model pairs = 600 stratified expert audits with bootstrap BCA CIs (10,000 resamples). Stratified by gaming severity (no/mild/severe). Per Bonett & Wright (2000), n=75 yields CI half-width ≈ 0.12 for ρ ≈ 0.7\\n(7) AGRC vs MO-GRPO: weight trajectories, GRS-accuracy Pareto frontiers, gaming behavior distributions\\n(8) Critic scaling: GRS comparison for R_critic using 14B (84.8%) vs 8B (~79.8%)\\n\\n**Research Questions:**\\n  RQ1: Which reward signal categories exhibit highest gaming resistance in isolation? Do formally-grounded signals (C2) outperform semantic (C3, C4) and learned-critic (C5) signals?\\n  RQ2: Does hybrid composition (C6-C8) yield additive faithfulness gains while maintaining gaming resistance?\\n  RQ3: Does gaming-specific optimization (AGRC) outperform objective-agnostic normalization (MO-GRPO) on the GRS-accuracy Pareto frontier?\\n  RQ4: Does GRS-GTED reliably predict GRS-human? How does Spearman compare to Kendall for gaming-resistance capture?\\n  RQ5: How does critic model accuracy (14B vs 8B) impact gaming resistance of R_critic?\\n\\n**Training:** GRPO with KL penalty on Qwen2.5-Coder-7B-Instruct and Qwen3-Coder-30B-A3B-Instruct. Training on ProofNet + FormalMATH-Lite.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"1500 H100 (10 configs on 7B = 10×70 + top 4+AGRC+MO-GRPO on 30B = 6×70 + 100 grid search + 100 baseline + 80 evaluation + 60 CriticLeanGPT-14B inference + 30 exploitation-rate comparison)\",\n      \"cpu_hours\": \"~40,000 CPU-hours on c7i.16xlarge for Lean compilation via Kimina Lean Server + GTED operator tree construction\",\n      \"human_audit_hours\": \"~70 expert-hours for 600 stratified manual gaming audits (75 samples × 8 key config-model pairs) with bootstrap BCA validation\",\n      \"timeline\": \"15-17 weeks (4 wks pipeline + GTED integration + GRS implementation + contamination model proof + LeanInteract error parser, 6 wks RL training across configs, 2 wks AGRC+MO-GRPO development/training, 4 wks evaluation/comparison/writing)\",\n      \"estimated_gpu_cost\": \"$3,750 (at ~$2.50/hr H100 spot)\",\n      \"estimated_cpu_cost\": \"$750-1,400 (c7i.16xlarge spot at ~$0.90/hr)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"1250 H100\",\n      \"cpu_hours\": \"~35,000 CPU-hours\",\n      \"human_audit_hours\": \"~55 expert-hours\",\n      \"timeline\": \"13-15 weeks\",\n      \"claude_api_cost\": \"$550\",\n      \"estimated_gpu_cost\": \"$3,125\",\n      \"estimated_cpu_cost\": \"$600-1,200\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"1250 H100\",\n      \"cpu_hours\": \"~35,000 CPU-hours\",\n      \"human_audit_hours\": \"~45 expert-hours (automated pre-filtering via GRS-GTED reduces manual load to disagreement cases)\",\n      \"timeline\": \"10-12 weeks\",\n      \"claude_api_cost\": \"$750\",\n      \"estimated_gpu_cost\": \"$3,125\",\n      \"estimated_cpu_cost\": \"$600-1,200\",\n      \"speed_bottleneck\": \"Lean compilation (~7s avg) and GTED operator tree construction (~2s per statement). With 120-180 parallel Lean instances, throughput matches GPU generation.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (abstract Sep 19, paper Sep 24, 2026 [estimated, from trybibby.com]) — PRIMARY, ~17 weeks available. Tightened scope (2 GRS variants main text, MO-GRPO as focused baseline, GRIFT analytical only) makes clean ICLR narrative feasible\",\n    \"EACL 2027 (ARR Aug 3, 2026 → Oct 11 commitment) — SECONDARY, ~10 weeks for ARR submission. 7B full ablation + GRS framework + MO-GRPO comparison feasible; 30B scaling deferred to camera-ready\",\n    \"NAACL 2027 (ARR Oct 12, 2026 → commitment ~Oct 16 [estimated]) — TERTIARY CONTINGENCY. Full experiment set including 30B scaling feasible\",\n    \"ACL 2027 (ARR ~Feb 16, 2027 [estimated]) — SAFE FALLBACK. Complete experimental set with all supplementary analyses\"\n  ],\n  \"level\": \"solid+\",\n  \"key_references\": [\n    \"FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\",\n    \"Mathesis: Towards Formal Theorem Proving from Natural Languages (ICLR 2026)\",\n    \"Online Reinforcement Learning for Autoformalization (MAR Workshop @ NeurIPS 2025)\",\n    \"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion (AAAI 2026)\",\n    \"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv July 2025)\",\n    \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (VerifAI-2 @ ICLR 2026)\",\n    \"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (ICLR 2026 Workshop)\",\n    \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems (arXiv:2509.22047, Sep 2025)\",\n    \"On the Hidden Objective Biases of Group-based Reinforcement Learning (arXiv:2601.05002, Jan 2026)\",\n    \"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals (arXiv:2604.01476, April 2026)\",\n    \"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness [SignCert-PO] (arXiv:2604.02986, April 2026)\",\n    \"Reward Hacking as Equilibrium under Finite Evaluation (arXiv:2603.28063, March 2026)\",\n    \"Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting [DRW] (TACL 2026)\",\n    \"Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking (arXiv February 2026)\",\n    \"Reward Hacking in Rubric-Based Reinforcement Learning (arXiv:2605.12474, May 2026)\",\n    \"Detecting and Suppressing Reward Hacking with Gradient Fingerprints [GRIFT] (arXiv:2604.16242, April 2026)\",\n    \"Reward Hacking Mitigation using Verifiable Composite Rewards (arXiv:2509.15557, ACM-BCB 2025)\",\n    \"SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents (arXiv:2605.21384, May 2026)\",\n    \"Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking (arXiv:2403.03185)\",\n    \"Generalized Tree Edit Distance (GTED): A Faithful Evaluation Metric for Statement Autoformalization (AI4Math @ ICML 2025)\",\n    \"FormalAlign: Automated Alignment Evaluation for Autoformalization (ICLR 2025)\",\n    \"Monotonic Reference-Free Refinement for Autoformalization (arXiv January 2026)\",\n    \"Process-Verified Reinforcement Learning for Theorem Proving via Lean (NeurIPS 2025)\",\n    \"Process-Driven Autoformalization in Lean 4 (arXiv 2024)\",\n    \"Training Step-Level Reasoning Verifiers with Formal Verification Tools [FOVER] (ACL 2026 Findings)\",\n    \"ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity (arXiv 2025)\",\n    \"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)\",\n    \"Autoformalizer with Tool Feedback (arXiv October 2025)\",\n    \"Faithful Autoformalization via Roundtrip Verification and Repair (arXiv April 2026)\",\n    \"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (arXiv March 2026)\",\n    \"FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization (arXiv March 2026)\",\n    \"FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)\",\n    \"Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)\",\n    \"Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems (arXiv July 2025)\",\n    \"Sample Size Requirements for Estimating Pearson, Kendall and Spearman Correlations (Bonett & Wright, Psychometrika 2000)\"\n  ],\n  \"description\": \"Reward hacking in autoformalization is documented and severe — 87-99% compilation rates mask systematic unfaithfulness (VerifAI-2, ICLR 2026) — yet we lack answers to a basic question: which reward signals resist gaming? This paper provides the first systematic answer, exploiting a capability unique to autoformalization: formally-grounded, LLM-independent faithfulness measurement via GTED tree-edit-distance.\\n\\nOur central insight is that autoformalization is uniquely positioned for principled gaming-resistance analysis. Unlike code generation (where test-based evaluation lacks formally-grounded semantic metrics), unlike general RLHF (where ground truth is subjective), autoformalization offers GTED — a computable faithfulness anchor derived from the Lean language server's operator trees. This enables gaming detection that is simultaneously more lightweight than gradient fingerprints (GRIFT), more automated than exploitation-rate (no LLM panels), and more formally justified than hand-crafted penalties. Everything in this paper flows from this observation.\\n\\nWe contribute three advances built on this foundation.\\n\\n**First (primary contribution)**, the first systematic comparison of gaming resistance across five isolated reward source categories for autoformalization RL: binary compilation, graded formal (via custom error-hierarchy classification over LeanInteract v0.11.3 diagnostics), embedding similarity, LLM judge, and trained critic (CriticLeanGPT-Qwen3-14B-RL at 84.8% — first use as direct RL reward). Our 10-configuration GRPO ablation on Qwen2.5-Coder-7B-Instruct and Qwen3-Coder-30B-A3B-Instruct isolates individual signal contributions, answering which signals to trust.\\n\\n**Second (enabling methodology)**, the GRS (Gaming Resistance Score) framework: rank correlation between reward signals and GTED-anchored faithfulness. We provide (a) theoretical justification proving GRS monotonically decreases under contamination and that rank-based measures (Spearman, Kendall) are provably more robust than linear correlation; (b) validation against 600 expert-annotated samples with bootstrap BCA confidence intervals; (c) comparison against exploitation-rate adapted to autoformalization using GTED+LeanScorer as verification panel.\\n\\n**Third (applied demonstration)**, AGRC (Adaptive Gaming-Resistant Reward Composition): gaming-aware dynamic reweighting using per-component GRS as optimization signal. The head-to-head against MO-GRPO (arXiv:2509.22047) — the state-of-the-art objective-agnostic hacking mitigation for multi-objective GRPO — tests whether gaming-specific signals outperform variance normalization when domain-specific detection is available. We also position AGRC relative to other gaming-aware GRPO modifications operating at different levels: representation-level (Advantage Modification, arXiv:2604.01476) and advantage-level (SignCert-PO, arXiv:2604.02986).\\n\\nThe paper is designed for outcome robustness: if formally-grounded signals dominate, we advance reward design; if signals are equivalent, we establish cost-effectiveness; if MO-GRPO matches AGRC, we demonstrate that objective-agnostic normalization suffices (a useful negative result). Regardless, the gaming-resistance analysis and GRS framework are independent contributions. Targeting ICLR 2027 (Sep 24 estimated deadline), with EACL 2027, NAACL 2027, and ACL 2027 as contingency venues.\",\n  \"project_name\": \"reward_comp_autoform\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 6)\nIssues: [\"MISSING WORK: CTWA — Covariance Targeted Weight Adaptation (arXiv:2602.06869, Feb 2026, revised May 2026) proposes adaptive multi-objective GRPO weight adjustment by monitoring covariance between each objective's reward and the clipped advantage weight. This is DIRECTLY relevant to AGRC: both dynamically adapt multi-objective GRPO weights during training. While CTWA is objective-agnostic (like MO-GRPO, it doesn't detect gaming specifically), it uses a different mechanism than MO-GRPO's variance normalization — covariance-based adaptation is conceptually closer to AGRC's signal-driven reweighting. Must be cited and differentiated. Same authors (Lu & Jiang) as DRW (TACL 2026), creating an even denser competitive landscape for dynamic GRPO weight adaptation.\", \"MISSING WORK: FormalRewardBench (arXiv:2605.10141, May 11, 2026) is the first benchmark for evaluating reward models in formal theorem proving with Lean 4. While focused on proof-level reward models (not statement autoformalization), it addresses the closely related question of reward quality in formal math and finds that specialized theorem provers perform worst at proof evaluation (24.4% vs frontier LLMs at 59.8%). This challenges assumptions about formally-grounded signals and should be cited in the evaluation landscape.\", \"MISSING WORK: Reward Hacking survey (arXiv:2604.13602, April 2026) provides a comprehensive taxonomy of detection methods across the lifecycle (training-time monitoring, inference-time safeguards, post-hoc auditing) and proposes the Proxy Compression Hypothesis. Should be cited as contextual reference for the broader reward hacking landscape.\", \"VerifAI-2 CHARACTERIZATION IMPRECISION: The proposal states '87-99% compilation success masks systematic unfaithfulness.' The actual VerifAI-2 paper (arXiv:2604.19459) states 'despite compilation rates of 87-99%, finds no evidence of systematic gaming in unified generation' but identifies unfaithfulness through fabrication (GPT-5) and mistranslation (DeepSeek-R1) in two-stage pipelines. The distinction between 'gaming' (intentional exploitation) and 'unfaithfulness' (capability limitation) matters for a paper about gaming resistance. The proposal should be more precise about what VerifAI-2 actually found.\", \"CROWDED MULTI-OBJECTIVE GRPO LANDSCAPE: The proposal positions AGRC against MO-GRPO and DRW, but the landscape now includes at least 5 adaptive multi-objective GRPO weight methods: (1) MO-GRPO (variance normalization), (2) DRW (hypervolume/gradient-based), (3) CTWA (covariance-targeted), (4) Blockwise Advantage (arXiv:2602.10231, per-objective advantage), (5) TaRoS (component saturation-aware downweighting). All are objective-agnostic; AGRC's gaming-specific differentiation is clear but the contribution narrows to 'plugging a different signal (GRS) into the adaptive reweighting paradigm.' Consider whether this weakens AGRC's novelty claim and whether the MO-GRPO head-to-head alone is sufficient.\", \"SCOPE STILL DENSE FOR ICLR: 10 configs × 2 models (7B+30B) × 2 GRS variants × AGRC + MO-GRPO + exploitation-rate comparison + critic scaling + 600-sample human validation + theoretical contamination model. This is 8 evaluation analyses in the framework. Reviewers may see this as comprehensive-but-unfocused. The strongest version of this paper might focus on RQ1 (which signals resist gaming?) + RQ2 (hybrid composition effects) + GRS validation, treating AGRC as a lightweight demonstration rather than a co-primary contribution.\"]\nFeedback: The proposal has matured significantly across 6 rounds and addresses a genuine gap. The central insight about autoformalization's unique position for gaming-resistance analysis via GTED is well-articulated and independently verified — no prior work uses GTED as a gaming-resistance anchor. To reach pass quality:\n\n(1) **Add CTWA (arXiv:2602.06869)** as related work alongside MO-GRPO and DRW. Differentiation: CTWA monitors covariance between objective rewards and clipped advantages (interference-aware but gaming-agnostic), while AGRC uses domain-specific gaming detection (GRS-GTED). Note: CTWA is by the same authors as DRW (Lu & Jiang), making this a productive research group to track. Consider whether CTWA should replace MO-GRPO as the primary baseline (covariance-based adaptation is mechanistically closer to AGRC's signal-driven approach than variance normalization).\n\n(2) **Cite FormalRewardBench (arXiv:2605.10141)** in the evaluation landscape. Its finding that specialized theorem provers are poor at proof evaluation (24.4%) while frontier LLMs are better (59.8%) has implications for your R_critic signal — CriticLeanGPT's accuracy may degrade differently under gaming than under normal conditions.\n\n(3) **Nuance the VerifAI-2 characterization**: Specify that VerifAI-2 found 'no evidence of systematic gaming in unified generation' but documented fabrication/mistranslation in two-stage pipelines. This distinction (gaming vs. capability-limited unfaithfulness) is important for a paper that defines and measures 'gaming resistance.'\n\n(4) **Consider scope prioritization for ICLR**: The paper has two natural configurations: (A) 'Analysis paper' — focus on GRS framework + systematic ablation (RQ1-RQ2) + validation (RQ4), treating AGRC as a brief demonstration section. This makes the gaming-resistance analysis the star. (B) 'Method paper' — focus on AGRC vs MO-GRPO/CTWA (RQ3), with the ablation providing motivation. Option (A) is likely stronger for ICLR because the systematic analysis is more novel than the specific reweighting mechanism.\n\n(5) **Strengthen GRS novelty via deeper theoretical analysis**: Instead of just proving monotonic decrease under contamination (which is intuitive), consider proving: (a) sample complexity bounds for reliable GRS estimation (how many evaluation samples are needed for a given CI width?); (b) conditions under which GRS-GTED detects gaming that exploitation-rate misses, and vice versa; (c) a formal connection between GRS and the Correlated Proxies framework (arXiv:2403.03185). Any of these would elevate GRS from 'applying a known statistic' to a substantive methodological contribution.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields.\n\n## 停滞提醒\n经过 6 轮修订，近 3 轮平均分从 3.5 到 3.6，无明显改善。\n考虑 major revision 或 pivot。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T22:06:35.295Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T22:06:35.295Z",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51"
}
```

---

## Round 1

40 recorded events

### User

_source line 3 · 2026-05-27T22:06:35.350Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-27 (UTC).**

## Original idea
{
  "changes_made": [
    "MAJOR NARRATIVE RESTRUCTURING: Reframed entire proposal around a single central insight: 'autoformalization is uniquely positioned for principled gaming-resistance analysis because GTED provides a formally-grounded, LLM-independent faithfulness anchor.' Every contribution now explicitly serves this insight. Core problem, opportunity, and description rewritten to lead with this claim and build a coherent story rather than a feature list. This addresses the stagnation at 3.5-3.6 and the reviewer's observation that the proposal 'reads as a list of things rather than a story'",
    "ADDED MO-GRPO (arXiv:2509.22047, Sep 2025; revised Jan 2026) as primary dynamic baseline, replacing DRW. MO-GRPO normalizes advantage per-objective: A^MO_g = Σ_i [R_i(q,o_g) - mean(R_i)]/std(R_i), preventing variance-based dominance in multi-objective GRPO. Directly targets reward hacking in multi-objective GRPO, making it a far more relevant baseline than DRW (which optimizes Pareto efficiency, not gaming resistance). Key differentiation: MO-GRPO is objective-agnostic (equalizes variance contributions regardless of gaming behavior), while AGRC uses gaming-specific signals (GRS) — the central experimental question becomes whether gaming-aware optimization outperforms objective-agnostic normalization. C10 is now MO-GRPO baseline. DRW retained in landscape discussion but removed as experimental baseline",
    "ADDED Advantage Modification from 'When Reward Hacking Rebounds' (arXiv:2604.01476, April 2026): integrates shortcut concept scores (extracted via representation engineering on contrastive pairs) into GRPO advantage computation to penalize hacking rollouts. Identifies three-phase rebound pattern (attempt → retreat → rebound) in coding environments. Differentiated at three levels: (a) operates at representation level (requires probing hidden states for concept directions), AGRC operates at reward-component level (uses GRS per component); (b) requires domain-specific contrastive pairs for concept extraction, GRS requires only reward-faithfulness evaluation; (c) designed for single-objective hacking detection, AGRC handles multi-objective composition. Discussed in landscape, not implemented as baseline due to fundamentally different mechanism level",
    "ADDED SignCert-PO from 'Mitigating Reward Hacking in RLHF via Advantage Sign Robustness' (arXiv:2604.02986, April 2026): derives certified sign-preservation radius via adversarial perturbation in RM parameter space, down-weights non-robust completions. Differentiated: (a) SignCert-PO operates on reward model parameter perturbations (requires RM weight access), AGRC operates on observable reward-faithfulness correlations; (b) SignCert-PO is designed for single-RM RLHF settings, AGRC handles multi-source reward composition; (c) SignCert-PO detects potentially-flipped advantages regardless of cause, AGRC specifically targets gaming via faithfulness decorrelation. Cited in landscape",
    "ADDED 'On the Hidden Objective Biases of Group-based Reinforcement Learning' (arXiv:2601.05002, Jan 2026) as additional theoretical motivation: proves GRPO exhibits non-uniform group weighting biases, AdamW-induced reward scaling insensitivity, and momentum-based clipping violations. Strengthens our motivation: these structural biases compound with gaming vulnerability, making gaming-aware composition more urgent",
    "ADDED 'Reward Hacking as Equilibrium under Finite Evaluation' (arXiv:2603.28063, March 2026): proves that under minimal axioms (multi-dimensional quality, finite evaluation, effective optimization), reward hacking is a structural equilibrium, not a correctable bug. Key implication for our work: since hacking is inevitable under finite evaluation, measuring gaming RESISTANCE becomes the critical question — which signals degrade least? This provides foundational theoretical motivation beyond the empirical observations from VerifAI-2",
    "SIGNIFICANT SCOPE REDUCTION following reviewer recommendation: (1) GRS metric variants: Spearman and Kendall in main text only; Pearson and MI deferred to appendix as supplementary ablation. Justified: theoretical contamination analysis already proves rank-based superiority over linear; MI is high-variance estimator best suited for supplementary analysis. (2) Cross-method comparison: GRIFT reimplementation DROPPED — replaced with analytical comparison (computation cost, automation degree, dependency requirements) using published GRIFT results as reference. Exploitation-rate comparison retained as lightweight adaptation (uses GTED+LeanScorer as panel, no external LLM dependency). (3) DRW experimental baseline dropped, replaced with more relevant MO-GRPO. Net effect: 10 configs unchanged, but metric variants reduced from 4→2 main text, cross-method from 3→1 experimental + 1 analytical, saving ~100 GPU hours and ~16 hours manual GRIFT cluster labeling",
    "CORRECTED LeanInteract specification: v0.11.3 confirmed on PyPI (released May 14, 2026). Message objects provide structured fields: start_pos (Pos), end_pos (Pos), data (string), severity ∈ {error, warning, info}. IMPORTANT CORRECTION: the error sub-classification (parse → name resolution → type) is NOT a built-in LeanInteract feature — severity provides only three levels. R_formal error hierarchy requires custom regex-based classification of Message.data strings (e.g., 'unknown identifier' → name resolution, 'type mismatch' → type error, 'expected token' → parse error). This custom parser (~200 LoC) is straightforward but must be documented as engineering contribution, not library feature",
    "STRENGTHENED GRS VALIDATION: Increased human annotation budget from 400 to 600 samples (75 samples × 8 key config-model pairs, up from 50 × 8). Added bootstrap BCA confidence intervals (10,000 resamples) for all GRS-human correlation estimates, reporting CI widths to demonstrate statistical reliability. Justified via Bonett & Wright (2000): n=75 with bootstrap yields CI half-width ≈ 0.12 for ρ ≈ 0.7, adequate for distinguishing 'high' (>0.6) from 'moderate' (0.3-0.6) correlation. Added stratified sampling across gaming severity levels (no gaming, mild gaming, severe gaming) to ensure representativeness. Total human audit hours increased from ~55 to ~70",
    "SHARPENED GAP CLAIM to account for new related work: The gap is now: 'While general multi-objective GRPO hacking mitigations exist — MO-GRPO normalizes variance (objective-agnostic), Advantage Modification integrates representation-level shortcuts, SignCert-PO certifies advantage sign robustness — none leverage domain-specific formally-grounded faithfulness measures, and none study which reward source categories resist gaming in autoformalization where such measures are uniquely available.' This positions our work as domain-specific and complementary to general methods, not competing",
    "REFINED AGRC vs MO-GRPO framing: The central experimental question is now: 'Does gaming-specific optimization (AGRC: w_k ∝ exp(η·GRS_k)) outperform objective-agnostic normalization (MO-GRPO: per-objective variance normalization) for gaming resistance in autoformalization?' This is a cleaner, more testable claim than the previous AGRC vs DRW comparison. Added specific hypotheses: (H1) When gaming concentrates in specific reward components, AGRC detects and downweights selectively while MO-GRPO cannot discriminate gamed from non-gamed components; (H2) MO-GRPO may outperform AGRC when gaming is distributed uniformly across components (variance normalization is sufficient). Both outcomes are publishable",
    "STREAMLINED EVALUATION FRAMEWORK: Reduced from 11 evaluation dimensions to 8 well-defined analyses: (1) Standard metrics, (2) Multi-metric faithfulness, (3) GRS decomposition per config × checkpoint, (4) GRS-Spearman vs GRS-Kendall comparison, (5) GRS-GTED vs exploitation-rate comparison, (6) GRS-human validation with bootstrap CIs, (7) AGRC vs MO-GRPO weight trajectory and Pareto analysis, (8) Critic scaling (14B vs 8B). Dropped separate GRIFT comparison, broader applicability sketch moved to discussion only, gaming taxonomy merged into GRS decomposition analysis"
  ],
  "title": "Gaming Resistance in Autoformalization RL: How Formally-Grounded Faithfulness Enables Principled Reward Analysis",
  "core_problem": "RL-based autoformalization combines composite rewards — binary compilation (FormaRL, Mathesis), LLM semantic judges (Mathesis R_sem), embedding similarity (Online RL for Autoformalization), and trained critics (CriticLean at 84.8% accuracy) — yet a fundamental question remains unanswered: which reward signals RESIST GAMING, and can we measure this automatically?\n\nThis question is urgent. Gaming in autoformalization is documented and severe: VerifAI-2 (ICLR 2026) shows 87-99% compilation success masks systematic unfaithfulness; FormaRL's ablation reveals syntax-only RL yields 100% compilation but 0% semantic consistency. Theoretically, 'Reward Hacking as Equilibrium' (arXiv:2603.28063) proves that gaming is a structural equilibrium under finite evaluation — not a correctable bug — making the measurement of gaming RESISTANCE (which signals degrade least) the critical practical question.\n\nThe broader RL community has responded with gaming mitigations at multiple levels: MO-GRPO (arXiv:2509.22047) normalizes per-objective advantage variance to prevent dominance-based hacking in multi-objective GRPO; Advantage Modification (arXiv:2604.01476) integrates representation-level shortcut concept scores into GRPO advantages; SignCert-PO (arXiv:2604.02986) down-weights non-robust completions via certified sign-preservation radius; GRIFT (arXiv:2604.16242) detects gaming via gradient fingerprints; exploitation-rate (arXiv:2605.12474) measures fraction of newly-credited criteria rejected by LLM panels.\n\nHowever, ALL these methods are domain-agnostic — none exploit domain-specific structure. Autoformalization has a UNIQUE advantage unavailable in any other RL domain: the Lean language server provides formally-grounded, LLM-independent faithfulness measurement via GTED tree-edit-distance (AI4Math@ICML 2025). This creates three domain-specific gaps: (1) No work has used formally-grounded faithfulness to compare gaming-resistance PROPERTIES of different reward source categories in isolation — Mathesis combines signals for performance but doesn't study which resist gaming; (2) No gaming-resistance metric leverages formally-grounded faithfulness anchors, enabling detection that is simultaneously lightweight (no gradients, unlike GRIFT), automated (no manual labeling), and non-circular (no LLM panels, unlike exploitation-rate); (3) No mechanism adapts multi-objective GRPO composition based on gaming-specific signals — MO-GRPO normalizes variance (objective-agnostic), not gaming resistance.",
  "opportunity": "A unique convergence of six developments makes this the right moment for this study:\n\n(1) GTED (AI4Math@ICML 2025) provides formally-grounded faithfulness via tree-edit-distance over Lean operator trees — the KEY enabling capability. Unlike code generation (where no equivalent formally-grounded semantic metric exists) or general RLHF (where ground truth is subjective), autoformalization offers a computable, LLM-independent faithfulness anchor. This makes gaming-resistance measurement principled in a way no other RL domain can achieve.\n\n(2) Gaming is newly documented but unquantified for autoformalization. VerifAI-2 shows the problem exists; we provide the first systematic measurement of which signals are affected and by how much.\n\n(3) Mathesis (ICLR 2026) establishes that composite rewards work for autoformalization GRPO — but treats composition as a performance optimization problem, not a gaming-resistance problem. The transition from 'which composition gives highest accuracy' to 'which composition resists gaming' is the core reframing.\n\n(4) CriticLean (July 2025) creates a new reward signal category (trained critic at 84.8% accuracy) untested as direct RL training signal, providing a fifth source category for comparison.\n\n(5) MO-GRPO (Sep 2025) proves objective-agnostic normalization mitigates hacking in multi-objective GRPO. The natural next question: does gaming-specific optimization outperform objective-agnostic normalization when domain-specific gaming detection is available?\n\n(6) Recent general gaming mitigations (Advantage Modification, SignCert-PO, GRIFT, exploitation-rate) create urgency for domain-specific comparison: does autoformalization's unique formal verification capability enable better gaming-resistance measurement than general-purpose approaches?",
  "landscape": "**Autoformalization RL systems:** FormaRL (COLM 2025) uses GRPO with binary compilation + LLM semantic consistency, achieving 26.15% pass@1 on ProofNet; ablation reveals aggressive gaming — syntax-only RL yields 100% compilation, 0% consistency. Mathesis (ICLR 2026) advances with R_ver + R_sem in GRPO plus HPO; 22% improvement on Gaokao-Formal. CriticLean (arXiv July 2025) trains CriticLeanGPT via SFT+GRPO: Qwen3-14B-RL achieves 84.8% (publicly available), Qwen3-8B-RL achieves 79.8% on CriticLeanBench. StepFun-Formalizer (AAAI 2026) achieves 40.5% BEq@1 SOTA on FormalMATH-Lite.\n\n**Gaming in autoformalization:** Do LLMs Game Formalization? (VerifAI-2 @ ICLR 2026) documents 87-99% compilation masking unfaithfulness: GPT-5 fabricates axioms, DeepSeek-R1 mistranslates premises. LLMs Gaming Verifiers (ICLR 2026 Workshop) demonstrates RLVR models abandon reasoning for shortcuts.\n\n**Multi-objective GRPO hacking mitigations (UPDATED):** MO-GRPO (arXiv:2509.22047, Sep 2025; revised Jan 2026) normalizes per-objective advantage: A^MO_g = Σ_i [R_i - mean(R_i)]/std(R_i), ensuring all reward functions contribute evenly regardless of variance. Objective-AGNOSTIC: equalizes contributions without detecting whether any component is being gamed. Tested on bandits, WMT, AlpacaFarm. On the Hidden Objective Biases of Group-based RL (arXiv:2601.05002, Jan 2026) further analyzes GRPO structural biases: non-uniform group weighting, AdamW scaling insensitivity, momentum clipping violations.\n\n**Gaming-aware GRPO modifications (NEW):** Advantage Modification from 'When Reward Hacking Rebounds' (arXiv:2604.01476, April 2026) integrates shortcut concept scores (extracted via representation engineering from contrastive pairs) into GRPO advantage computation. Identifies three-phase rebound pattern. Operates at REPRESENTATION level — requires probing hidden states, domain-specific contrastive pairs. SignCert-PO (arXiv:2604.02986, April 2026) derives certified sign-preservation radius via adversarial RM perturbation, down-weights non-robust completions. Operates at ADVANTAGE level — requires RM weight access, designed for single-RM settings.\n\n**General gaming detection:** GRIFT (arXiv:2604.16242, April 2026) detects gaming via gradient fingerprints (LoRA adapters, K-means, ~80% F1). Heavyweight: requires per-sample gradient computation + 16 manually-labeled cluster representatives. Exploitation-rate (arXiv:2605.12474, May 2026) measures fraction of newly-credited criteria rejected by cross-family LLM panel (GPT-5.4, Gemini 3 Pro, Claude Opus 4.6). Expensive and LLM-dependent. Composite reward penalties (arXiv:2509.15557, ACM-BCB 2025) introduce hand-crafted gaming penalties — requires manual pattern enumeration.\n\n**Theoretical foundations:** Correlated Proxies (arXiv:2403.03185) formalizes reward hacking via correlation breakdown between proxy and true rewards; proves χ² regularization prevents hacking. Reward Hacking as Equilibrium (arXiv:2603.28063, March 2026) proves hacking is structural under finite evaluation: any optimized agent under-invests in unevaluated quality dimensions. SpecBench (arXiv:2605.21384, May 2026) measures hacking in coding agents: gap grows 28pp per 10× code size.\n\n**Evaluation metrics:** GTED (AI4Math@ICML 2025) provides tree-edit-distance over operator trees from Lean Language Server — formally-grounded, no ATP/LLM dependency, highest accuracy (70.73%) and Kappa (0.438) on miniF2F. FormalAlign (ICLR 2025) uses dual contrastive+generation loss, 99.21% AS on FormL4-Basic. LeanScorer (Mathesis) decomposes into subtasks, Sugeno fuzzy integral, 0.92 F1.\n\n**Dynamic reward composition:** DRW (TACL 2026) introduces hypervolume-guided and gradient-based dynamic weight adaptation for Pareto efficiency. Not gaming-aware.\n\n**The refined gap:** Autoformalization uniquely provides formally-grounded faithfulness measurement (GTED), enabling gaming-resistance analysis unavailable in other domains. While general mitigations exist at variance level (MO-GRPO), representation level (Advantage Modification), advantage level (SignCert-PO), and gradient level (GRIFT), none exploit this domain-specific capability. No work compares gaming resistance across isolated reward source categories for autoformalization, proposes a gaming-resistance metric grounded in formal faithfulness, or applies gaming-specific dynamic reweighting to multi-objective autoformalization GRPO.",
  "inspired_by": "The central insight: autoformalization is the IDEAL domain for studying gaming resistance because GTED provides a formally-grounded faithfulness anchor that enables non-circular, lightweight, automated gaming detection — capabilities unavailable in any other RL domain. This insight emerges from the convergence of: (1) the theoretical result that reward hacking is a structural equilibrium (arXiv:2603.28063), making resistance measurement the practical question; (2) GTED providing the formally-grounded anchor that makes principled measurement possible; (3) the proliferation of domain-agnostic mitigations (MO-GRPO, Advantage Modification, SignCert-PO, GRIFT) creating demand for domain-specific evaluation; (4) Mathesis/FormaRL establishing composite autoformalization rewards without studying gaming properties; (5) CriticLean creating a new untested reward category. The gap between documented gaming (VerifAI-2) and absence of gaming-resistance measurement for autoformalization is clear and actionable.",
  "approach": "We present the first systematic gaming-resistance analysis for autoformalization RL, built on the central insight that GTED's formally-grounded faithfulness measurement enables principled gaming detection unavailable in other RL domains. The approach has three phases that progressively build on this insight.\n\n**Phase 1: Multi-Source Reward Signal Extraction**\n\n(a) Formally-grounded signal R_formal: Using LeanInteract v0.11.3's Message objects (fields: start_pos, end_pos, data, severity ∈ {error, warning, info}), classify compiler diagnostics into error hierarchy via custom regex parser (~200 LoC) over Message.data strings: parse errors ('expected token', 'unexpected token') → name resolution ('unknown identifier', 'unknown namespace') → type errors ('type mismatch', 'has type ... but is expected to have type') → clean compilation. Yields R_formal ∈ {0.0, 0.25, 0.5, 0.75, 1.0} plus density bonus. NOTE: LeanInteract v0.11.3 provides three severity levels; the five-level error hierarchy requires our custom classification, documented as engineering contribution.\n\n(b) Embedding similarity R_embed: cosine similarity between sentence embeddings of input NL and backtranslation of generated formal statement (reference-free roundtrip approach).\n\n(c) LLM judge R_judge: binary faithfulness judgment from frozen LLM (following FormaRL/Mathesis R_sem approach).\n\n(d) Trained critic R_critic: semantic fidelity score from CriticLeanGPT-Qwen3-14B-RL (84.8% accuracy, publicly available). First use as direct RL reward signal during GRPO training. Additionally retrain Qwen3-8B using CriticLean_4K dataset (~79.8% expected) to study critic accuracy impact on gaming resistance.\n\n**Phase 2: GRS (Gaming Resistance Score) Framework — Enabling Methodology**\n\nGRS measures the meta-property of reward signals: how faithfully does high reward indicate genuine quality? This is the rank correlation between reward and formally-grounded faithfulness:\n\n  GRS(R, F) = ρ_s(R(x), F(x)) over held-out evaluation set\n\n**2a. Theoretical Justification:**\nUnder contamination model (1-α)P_faithful + αP_gamed, where P_gamed has reward above and faithfulness below the faithful population's medians, we prove: (i) GRS monotonically decreases in gaming proportion α; (ii) rank-based measures (Spearman, Kendall) are more robust than Pearson because gaming creates outlier patterns (high R, low F) whose influence on Pearson is unbounded (proportional to magnitude) while rank-based measures bound each observation's influence to its rank position.\n\n**2b. Two Primary GRS Formulations (main text):**\n  GRS-Spearman: rank correlation — standard, well-understood\n  GRS-Kendall: concordance probability — handles ties better, more interpretable as pairwise comparison probability\n  (GRS-Pearson and GRS-MI deferred to appendix as supplementary ablation)\n\n**2c. Multi-Faceted Faithfulness Anchors:**\n  GRS-GTED: F(x) = GTED tree-edit-distance (PRIMARY — formally-grounded, no LLM dependency)\n  GRS-LeanScorer: F(x) = LeanScorer Sugeno score (secondary)\n  GRS-roundtrip: F(x) = roundtrip consistency (tertiary)\n  GRS-human: F(x) = expert judgment (gold standard, 600 validation samples)\n\n**2d. Comparison with Exploitation-Rate:**\nAdapt exploitation-rate to autoformalization: define rubric criteria (type-correctness, structure-preservation, semantic-fidelity), use GTED+LeanScorer as reference panel (lightweight, no external LLM dependency). Compare detection sensitivity, computation cost, and automation degree against GRS-GTED. GRIFT comparison discussed analytically using published results (accuracy, cost, dependency requirements) without full reimplementation — GRIFT's per-sample gradient computation + manual cluster labeling makes it heavyweight for our use case, and published ~80% F1 on math provides a reference point.\n\n**Phase 3: Systematic Ablation (10 Configurations)**\n  C1: Binary compilation only (FormaRL/Mathesis R_ver reproduction)\n  C2: Graded formal signal only (R_formal)\n  C3: Embedding similarity only (R_embed)\n  C4: LLM judge only (R_judge)\n  C5: Trained critic only (R_critic via CriticLeanGPT-14B-RL)\n  C6: Formal + embedding hybrid (R_formal + R_embed)\n  C7: Formal + trained critic hybrid (R_formal + R_critic)\n  C8: Full hybrid (R_formal + R_embed + R_critic)\n  C9: AGRC (adaptive gaming-aware, see Phase 4)\n  C10: MO-GRPO baseline (per-objective variance normalization applied to C8 component set)\n  Tiered model strategy: all 10 on Qwen2.5-Coder-7B-Instruct; top 4 by GRS + AGRC + MO-GRPO on Qwen3-Coder-30B-A3B-Instruct.\n\n**Phase 4: AGRC vs MO-GRPO — Gaming-Specific vs Objective-Agnostic Composition**\n\nThe central experimental question: does gaming-specific optimization outperform objective-agnostic normalization when domain-specific gaming detection is available?\n\n- MO-GRPO (C10): A^MO_g = Σ_i [R_i(q,o_g) - mean(R_i)]/std(R_i) — equalizes per-objective variance contributions. Objective-AGNOSTIC: treats all components identically regardless of gaming behavior.\n- AGRC (C9): w_k^(t+1) ∝ w_k^(t)·exp(η·GRS_k^(t)) — upweights gaming-resistant components, downweights gamed ones. Gaming-SPECIFIC: uses GRS-GTED per component, updated every K=500 steps.\n\nDifferentiation from other gaming-aware GRPO modifications:\n- Advantage Modification (arXiv:2604.01476) operates at representation level via shortcut concept scores — requires probing hidden states, domain-specific contrastive pairs. AGRC operates at reward-component level via observable GRS.\n- SignCert-PO (arXiv:2604.02986) operates at advantage level via RM perturbation robustness — requires RM weight access, single-RM setting. AGRC handles multi-source composition.\n\nSpecific hypotheses: (H1) When gaming concentrates in specific components (e.g., R_formal gamed via ':= True := by sorry'), AGRC selectively downweights while MO-GRPO cannot discriminate. (H2) MO-GRPO may suffice when gaming is uniformly distributed. Both outcomes are publishable.\n\n**Phase 5: Evaluation Framework**\n\n(1) Standard metrics: BEq@1, pass@1, ASSESS structural similarity\n(2) Automated faithfulness (multi-metric): GTED score, LeanScorer score, FormalAlign alignment score, roundtrip consistency\n(3) GRS decomposition: GRS-GTED and GRS-Kendall per configuration × checkpoint\n(4) GRS-Spearman vs GRS-Kendall comparison with bootstrap CIs\n(5) GRS-GTED vs exploitation-rate comparison (adapted to autoformalization) + analytical GRIFT comparison\n(6) GRS-human validation: 75 samples × 8 key config-model pairs = 600 stratified expert audits with bootstrap BCA CIs (10,000 resamples). Stratified by gaming severity (no/mild/severe). Per Bonett & Wright (2000), n=75 yields CI half-width ≈ 0.12 for ρ ≈ 0.7\n(7) AGRC vs MO-GRPO: weight trajectories, GRS-accuracy Pareto frontiers, gaming behavior distributions\n(8) Critic scaling: GRS comparison for R_critic using 14B (84.8%) vs 8B (~79.8%)\n\n**Research Questions:**\n  RQ1: Which reward signal categories exhibit highest gaming resistance in isolation? Do formally-grounded signals (C2) outperform semantic (C3, C4) and learned-critic (C5) signals?\n  RQ2: Does hybrid composition (C6-C8) yield additive faithfulness gains while maintaining gaming resistance?\n  RQ3: Does gaming-specific optimization (AGRC) outperform objective-agnostic normalization (MO-GRPO) on the GRS-accuracy Pareto frontier?\n  RQ4: Does GRS-GTED reliably predict GRS-human? How does Spearman compare to Kendall for gaming-resistance capture?\n  RQ5: How does critic model accuracy (14B vs 8B) impact gaming resistance of R_critic?\n\n**Training:** GRPO with KL penalty on Qwen2.5-Coder-7B-Instruct and Qwen3-Coder-30B-A3B-Instruct. Training on ProofNet + FormalMATH-Lite.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "1500 H100 (10 configs on 7B = 10×70 + top 4+AGRC+MO-GRPO on 30B = 6×70 + 100 grid search + 100 baseline + 80 evaluation + 60 CriticLeanGPT-14B inference + 30 exploitation-rate comparison)",
      "cpu_hours": "~40,000 CPU-hours on c7i.16xlarge for Lean compilation via Kimina Lean Server + GTED operator tree construction",
      "human_audit_hours": "~70 expert-hours for 600 stratified manual gaming audits (75 samples × 8 key config-model pairs) with bootstrap BCA validation",
      "timeline": "15-17 weeks (4 wks pipeline + GTED integration + GRS implementation + contamination model proof + LeanInteract error parser, 6 wks RL training across configs, 2 wks AGRC+MO-GRPO development/training, 4 wks evaluation/comparison/writing)",
      "estimated_gpu_cost": "$3,750 (at ~$2.50/hr H100 spot)",
      "estimated_cpu_cost": "$750-1,400 (c7i.16xlarge spot at ~$0.90/hr)"
    },
    "human_in_loop": {
      "gpu_hours": "1250 H100",
      "cpu_hours": "~35,000 CPU-hours",
      "human_audit_hours": "~55 expert-hours",
      "timeline": "13-15 weeks",
      "claude_api_cost": "$550",
      "estimated_gpu_cost": "$3,125",
      "estimated_cpu_cost": "$600-1,200"
    },
    "auto_research": {
      "gpu_hours": "1250 H100",
      "cpu_hours": "~35,000 CPU-hours",
      "human_audit_hours": "~45 expert-hours (automated pre-filtering via GRS-GTED reduces manual load to disagreement cases)",
      "timeline": "10-12 weeks",
      "claude_api_cost": "$750",
      "estimated_gpu_cost": "$3,125",
      "estimated_cpu_cost": "$600-1,200",
      "speed_bottleneck": "Lean compilation (~7s avg) and GTED operator tree construction (~2s per statement). With 120-180 parallel Lean instances, throughput matches GPU generation."
    }
  },
  "target_venues": [
    "ICLR 2027 (abstract Sep 19, paper Sep 24, 2026 [estimated, from trybibby.com]) — PRIMARY, ~17 weeks available. Tightened scope (2 GRS variants main text, MO-GRPO as focused baseline, GRIFT analytical only) makes clean ICLR narrative feasible",
    "EACL 2027 (ARR Aug 3, 2026 → Oct 11 commitment) — SECONDARY, ~10 weeks for ARR submission. 7B full ablation + GRS framework + MO-GRPO comparison feasible; 30B scaling deferred to camera-ready",
    "NAACL 2027 (ARR Oct 12, 2026 → commitment ~Oct 16 [estimated]) — TERTIARY CONTINGENCY. Full experiment set including 30B scaling feasible",
    "ACL 2027 (ARR ~Feb 16, 2027 [estimated]) — SAFE FALLBACK. Complete experimental set with all supplementary analyses"
  ],
  "level": "solid+",
  "key_references": [
    "FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)",
    "Mathesis: Towards Formal Theorem Proving from Natural Languages (ICLR 2026)",
    "Online Reinforcement Learning for Autoformalization (MAR Workshop @ NeurIPS 2025)",
    "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion (AAAI 2026)",
    "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv July 2025)",
    "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (VerifAI-2 @ ICLR 2026)",
    "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (ICLR 2026 Workshop)",
    "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems (arXiv:2509.22047, Sep 2025)",
    "On the Hidden Objective Biases of Group-based Reinforcement Learning (arXiv:2601.05002, Jan 2026)",
    "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals (arXiv:2604.01476, April 2026)",
    "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness [SignCert-PO] (arXiv:2604.02986, April 2026)",
    "Reward Hacking as Equilibrium under Finite Evaluation (arXiv:2603.28063, March 2026)",
    "Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting [DRW] (TACL 2026)",
    "Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking (arXiv February 2026)",
    "Reward Hacking in Rubric-Based Reinforcement Learning (arXiv:2605.12474, May 2026)",
    "Detecting and Suppressing Reward Hacking with Gradient Fingerprints [GRIFT] (arXiv:2604.16242, April 2026)",
    "Reward Hacking Mitigation using Verifiable Composite Rewards (arXiv:2509.15557, ACM-BCB 2025)",
    "SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents (arXiv:2605.21384, May 2026)",
    "Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking (arXiv:2403.03185)",
    "Generalized Tree Edit Distance (GTED): A Faithful Evaluation Metric for Statement Autoformalization (AI4Math @ ICML 2025)",
    "FormalAlign: Automated Alignment Evaluation for Autoformalization (ICLR 2025)",
    "Monotonic Reference-Free Refinement for Autoformalization (arXiv January 2026)",
    "Process-Verified Reinforcement Learning for Theorem Proving via Lean (NeurIPS 2025)",
    "Process-Driven Autoformalization in Lean 4 (arXiv 2024)",
    "Training Step-Level Reasoning Verifiers with Formal Verification Tools [FOVER] (ACL 2026 Findings)",
    "ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity (arXiv 2025)",
    "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)",
    "Autoformalizer with Tool Feedback (arXiv October 2025)",
    "Faithful Autoformalization via Roundtrip Verification and Repair (arXiv April 2026)",
    "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (arXiv March 2026)",
    "FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization (arXiv March 2026)",
    "FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)",
    "Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)",
    "Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems (arXiv July 2025)",
    "Sample Size Requirements for Estimating Pearson, Kendall and Spearman Correlations (Bonett & Wright, Psychometrika 2000)"
  ],
  "description": "Reward hacking in autoformalization is documented and severe — 87-99% compilation rates mask systematic unfaithfulness (VerifAI-2, ICLR 2026) — yet we lack answers to a basic question: which reward signals resist gaming? This paper provides the first systematic answer, exploiting a capability unique to autoformalization: formally-grounded, LLM-independent faithfulness measurement via GTED tree-edit-distance.\n\nOur central insight is that autoformalization is uniquely positioned for principled gaming-resistance analysis. Unlike code generation (where test-based evaluation lacks formally-grounded semantic metrics), unlike general RLHF (where ground truth is subjective), autoformalization offers GTED — a computable faithfulness anchor derived from the Lean language server's operator trees. This enables gaming detection that is simultaneously more lightweight than gradient fingerprints (GRIFT), more automated than exploitation-rate (no LLM panels), and more formally justified than hand-crafted penalties. Everything in this paper flows from this observation.\n\nWe contribute three advances built on this foundation.\n\n**First (primary contribution)**, the first systematic comparison of gaming resistance across five isolated reward source categories for autoformalization RL: binary compilation, graded formal (via custom error-hierarchy classification over LeanInteract v0.11.3 diagnostics), embedding similarity, LLM judge, and trained critic (CriticLeanGPT-Qwen3-14B-RL at 84.8% — first use as direct RL reward). Our 10-configuration GRPO ablation on Qwen2.5-Coder-7B-Instruct and Qwen3-Coder-30B-A3B-Instruct isolates individual signal contributions, answering which signals to trust.\n\n**Second (enabling methodology)**, the GRS (Gaming Resistance Score) framework: rank correlation between reward signals and GTED-anchored faithfulness. We provide (a) theoretical justification proving GRS monotonically decreases under contamination and that rank-based measures (Spearman, Kendall) are provably more robust than linear correlation; (b) validation against 600 expert-annotated samples with bootstrap BCA confidence intervals; (c) comparison against exploitation-rate adapted to autoformalization using GTED+LeanScorer as verification panel.\n\n**Third (applied demonstration)**, AGRC (Adaptive Gaming-Resistant Reward Composition): gaming-aware dynamic reweighting using per-component GRS as optimization signal. The head-to-head against MO-GRPO (arXiv:2509.22047) — the state-of-the-art objective-agnostic hacking mitigation for multi-objective GRPO — tests whether gaming-specific signals outperform variance normalization when domain-specific detection is available. We also position AGRC relative to other gaming-aware GRPO modifications operating at different levels: representation-level (Advantage Modification, arXiv:2604.01476) and advantage-level (SignCert-PO, arXiv:2604.02986).\n\nThe paper is designed for outcome robustness: if formally-grounded signals dominate, we advance reward design; if signals are equivalent, we establish cost-effectiveness; if MO-GRPO matches AGRC, we demonstrate that objective-agnostic normalization suffices (a useful negative result). Regardless, the gaming-resistance analysis and GRS framework are independent contributions. Targeting ICLR 2027 (Sep 24 estimated deadline), with EACL 2027, NAACL 2027, and ACL 2027 as contingency venues.",
  "project_name": "reward_comp_autoform",
  "source": "web_research"
}

## Reviewer feedback (round 6)
Issues: ["MISSING WORK: CTWA — Covariance Targeted Weight Adaptation (arXiv:2602.06869, Feb 2026, revised May 2026) proposes adaptive multi-objective GRPO weight adjustment by monitoring covariance between each objective's reward and the clipped advantage weight. This is DIRECTLY relevant to AGRC: both dynamically adapt multi-objective GRPO weights during training. While CTWA is objective-agnostic (like MO-GRPO, it doesn't detect gaming specifically), it uses a different mechanism than MO-GRPO's variance normalization — covariance-based adaptation is conceptually closer to AGRC's signal-driven reweighting. Must be cited and differentiated. Same authors (Lu & Jiang) as DRW (TACL 2026), creating an even denser competitive landscape for dynamic GRPO weight adaptation.", "MISSING WORK: FormalRewardBench (arXiv:2605.10141, May 11, 2026) is the first benchmark for evaluating reward models in formal theorem proving with Lean 4. While focused on proof-level reward models (not statement autoformalization), it addresses the closely related question of reward quality in formal math and finds that specialized theorem provers perform worst at proof evaluation (24.4% vs frontier LLMs at 59.8%). This challenges assumptions about formally-grounded signals and should be cited in the evaluation landscape.", "MISSING WORK: Reward Hacking survey (arXiv:2604.13602, April 2026) provides a comprehensive taxonomy of detection methods across the lifecycle (training-time monitoring, inference-time safeguards, post-hoc auditing) and proposes the Proxy Compression Hypothesis. Should be cited as contextual reference for the broader reward hacking landscape.", "VerifAI-2 CHARACTERIZATION IMPRECISION: The proposal states '87-99% compilation success masks systematic unfaithfulness.' The actual VerifAI-2 paper (arXiv:2604.19459) states 'despite compilation rates of 87-99%, finds no evidence of systematic gaming in unified generation' but identifies unfaithfulness through fabrication (GPT-5) and mistranslation (DeepSeek-R1) in two-stage pipelines. The distinction between 'gaming' (intentional exploitation) and 'unfaithfulness' (capability limitation) matters for a paper about gaming resistance. The proposal should be more precise about what VerifAI-2 actually found.", "CROWDED MULTI-OBJECTIVE GRPO LANDSCAPE: The proposal positions AGRC against MO-GRPO and DRW, but the landscape now includes at least 5 adaptive multi-objective GRPO weight methods: (1) MO-GRPO (variance normalization), (2) DRW (hypervolume/gradient-based), (3) CTWA (covariance-targeted), (4) Blockwise Advantage (arXiv:2602.10231, per-objective advantage), (5) TaRoS (component saturation-aware downweighting). All are objective-agnostic; AGRC's gaming-specific differentiation is clear but the contribution narrows to 'plugging a different signal (GRS) into the adaptive reweighting paradigm.' Consider whether this weakens AGRC's novelty claim and whether the MO-GRPO head-to-head alone is sufficient.", "SCOPE STILL DENSE FOR ICLR: 10 configs × 2 models (7B+30B) × 2 GRS variants × AGRC + MO-GRPO + exploitation-rate comparison + critic scaling + 600-sample human validation + theoretical contamination model. This is 8 evaluation analyses in the framework. Reviewers may see this as comprehensive-but-unfocused. The strongest version of this paper might focus on RQ1 (which signals resist gaming?) + RQ2 (hybrid composition effects) + GRS validation, treating AGRC as a lightweight demonstration rather than a co-primary contribution."]
Feedback: The proposal has matured significantly across 6 rounds and addresses a genuine gap. The central insight about autoformalization's unique position for gaming-resistance analysis via GTED is well-articulated and independently verified — no prior work uses GTED as a gaming-resistance anchor. To reach pass quality:

(1) **Add CTWA (arXiv:2602.06869)** as related work alongside MO-GRPO and DRW. Differentiation: CTWA monitors covariance between objective rewards and clipped advantages (interference-aware but gaming-agnostic), while AGRC uses domain-specific gaming detection (GRS-GTED). Note: CTWA is by the same authors as DRW (Lu & Jiang), making this a productive research group to track. Consider whether CTWA should replace MO-GRPO as the primary baseline (covariance-based adaptation is mechanistically closer to AGRC's signal-driven approach than variance normalization).

(2) **Cite FormalRewardBench (arXiv:2605.10141)** in the evaluation landscape. Its finding that specialized theorem provers are poor at proof evaluation (24.4%) while frontier LLMs are better (59.8%) has implications for your R_critic signal — CriticLeanGPT's accuracy may degrade differently under gaming than under normal conditions.

(3) **Nuance the VerifAI-2 characterization**: Specify that VerifAI-2 found 'no evidence of systematic gaming in unified generation' but documented fabrication/mistranslation in two-stage pipelines. This distinction (gaming vs. capability-limited unfaithfulness) is important for a paper that defines and measures 'gaming resistance.'

(4) **Consider scope prioritization for ICLR**: The paper has two natural configurations: (A) 'Analysis paper' — focus on GRS framework + systematic ablation (RQ1-RQ2) + validation (RQ4), treating AGRC as a brief demonstration section. This makes the gaming-resistance analysis the star. (B) 'Method paper' — focus on AGRC vs MO-GRPO/CTWA (RQ3), with the ablation providing motivation. Option (A) is likely stronger for ICLR because the systematic analysis is more novel than the specific reweighting mechanism.

(5) **Strengthen GRS novelty via deeper theoretical analysis**: Instead of just proving monotonic decrease under contamination (which is intuitive), consider proving: (a) sample complexity bounds for reliable GRS estimation (how many evaluation samples are needed for a given CI width?); (b) conditions under which GRS-GTED detects gaming that exploitation-rate misses, and vice versa; (c) a formal connection between GRS and the Correlated Proxies framework (arXiv:2403.03185). Any of these would elevate GRS from 'applying a known statistic' to a substantive methodological contribution.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.
- Address each issue specifically.

## 深度调研要求

不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。
2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。
3. **深度思考**：
   - 核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach？
4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。

## 针对 Review 意见的定向搜索

1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点
2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline
3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现
4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot

- You have full freedom: minor fix, major revision, or pivot.
- Include a "change_type" field: "minor", "major", or "pivot".
- Output a COMPLETE JSON object with ALL fields.

## 停滞提醒
经过 6 轮修订，近 3 轮平均分从 3.5 到 3.6，无明显改善。
考虑 major revision 或 pivot。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "6d783516-df0e-455a-9cd7-fd412aff8d61",
  "type": "user",
  "uuid": "adb3447e-21d6-445c-95db-a35fd1de5339",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T22:06:35.348Z_

```json
{
  "parentUuid": "adb3447e-21d6-445c-95db-a35fd1de5339",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "5220a187-e31a-432c-a79c-bb084f9093a4",
  "timestamp": "2026-05-27T22:06:35.348Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T22:06:35.348Z_

```json
{
  "parentUuid": "5220a187-e31a-432c-a79c-bb084f9093a4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "910e139b-93a7-4c6f-8899-176ce9b09de5",
  "timestamp": "2026-05-27T22:06:35.348Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"MAJOR NARRATIVE RESTRUCTURING: Reframed entire proposal a…",
  "leafUuid": "910e139b-93a7-4c6f-8899-176ce9b09de5",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gaming-resistant reward composition for autoformalization",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51"
}
```

---

### Assistant

_source line 8 · 2026-05-27T22:06:46.260Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully and plan my research strategy. The proposal has gone through 6 rounds with scores stagnating at 3.5-3.6. The reviewer is suggesting either major revision or pivot. Let me think about what's needed:

1. **CTWA (arXiv:2602.06869)** - Need to research this paper
2. **FormalRewardBench (arXiv:2605.10141)** - Need to research this


3. **Reward Hacking survey (arXiv:2604.13602)** - Need to research this
4. **VerifAI-2 characterization precision** - Need to re-read the actual paper
5. **Crowded multi-objective GRPO landscape** - This is a deeper concern about novelty
6. **Scope concerns for ICLR** - Need to make hard choices

The core issue is that I'm trying to do too much. The reviewer's key suggestion is reframing this as an analysis paper centered on the GRS framework with systematic ablations, using AGRC as a supporting example rather than a main contribution. This directly addresses why the scores have plateaued.

The real insight here is that GTED's systematic gaming-resistance analysis is genuinely novel, but AGRC itself is just another signal plugged into an existing adaptive reweighting approach in an already crowded space. So the winning strategy is to elevate the analysis framework as the primary contribution. I should do the research first, then decide on the revision approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "910e139b-93a7-4c6f-8899-176ce9b09de5",
  "isSidechain": false,
  "requestId": "req_011CbTqKAFoJqsvZgpUbSiPi",
  "type": "assistant",
  "uuid": "be98e742-2cbf-4b3b-8bbd-168bdd247751",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZhVbTLQ3HjrPh7ZBpAVPm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13672,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1707,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1707,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13672
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-27T22:06:46.262Z_

I'll research the key papers and issues raised by the reviewer in parallel before making revision decisions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be98e742-2cbf-4b3b-8bbd-168bdd247751",
  "isSidechain": false,
  "requestId": "req_011CbTqKAFoJqsvZgpUbSiPi",
  "type": "assistant",
  "uuid": "2da3c124-4103-4acd-bd9e-951e89154e99",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZhVbTLQ3HjrPh7ZBpAVPm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13672,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1707,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1707,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13672
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-27T22:06:49.812Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0116dQSkxene6dKxksXtCwBa`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research CTWA paper",
  "prompt": "I need to research the paper \"CTWA — Covariance Targeted Weight Adaptation\" (arXiv:2602.06869, Feb 2026, revised May 2026) by Lu & Jiang. \n\nUse WebSearch and WebFetch to find and read this paper. I need to understand:\n1. The exact mechanism: how does covariance between objective rewards and clipped advantages drive weight adaptation?\n2. What environments/tasks was it tested on?\n3. How does it compare to MO-GRPO and DRW (same authors as DRW)?\n4. What are the specific mathematical formulations?\n5. Is it truly objective-agnostic or does it have any gaming-awareness?\n\nAlso search for \"Blockwise Advantage arXiv:2602.10231\" and \"TaRoS component saturation GRPO\" to understand the broader crowded landscape of multi-objective GRPO weight methods.\n\nReport your findings in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2da3c124-4103-4acd-bd9e-951e89154e99",
  "isSidechain": false,
  "requestId": "req_011CbTqKAFoJqsvZgpUbSiPi",
  "type": "assistant",
  "uuid": "2b137b6c-9b36-4411-a56a-ee9a065b87d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZhVbTLQ3HjrPh7ZBpAVPm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13672,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1707,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1707,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13672
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T22:06:53.074Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015tzR49BY81LA2wZr8Btdkh`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research FormalRewardBench paper",
  "prompt": "I need to research the paper \"FormalRewardBench\" (arXiv:2605.10141, May 11, 2026) - the first benchmark for evaluating reward models in formal theorem proving with Lean 4.\n\nUse WebSearch and WebFetch to find and read this paper. I need to understand:\n1. What exactly does it benchmark? (proof-level reward models vs statement-level?)\n2. The key finding: specialized theorem provers at 24.4% vs frontier LLMs at 59.8% - what does this mean exactly?\n3. What reward model categories does it evaluate?\n4. How does it relate to autoformalization (vs theorem proving)?\n5. Any implications for using trained critics (like CriticLeanGPT) as reward signals?\n\nReport your findings in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b137b6c-9b36-4411-a56a-ee9a065b87d5",
  "isSidechain": false,
  "requestId": "req_011CbTqKAFoJqsvZgpUbSiPi",
  "type": "assistant",
  "uuid": "5f527364-0cac-4d8e-856c-72c25ecd8996",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZhVbTLQ3HjrPh7ZBpAVPm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13672,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1707,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1707,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13672
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-27T22:06:57.908Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01PjFAACGckKkqbR9dwB3SNz`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research reward hacking survey and VerifAI-2",
  "prompt": "I need to research two papers:\n\n1. **Reward Hacking survey (arXiv:2604.13602, April 2026)** - A comprehensive taxonomy of detection methods. I need:\n   - The proposed taxonomy structure (training-time, inference-time, post-hoc)\n   - The \"Proxy Compression Hypothesis\" - what is it exactly?\n   - How does it categorize methods like GRIFT, exploitation-rate, etc.?\n\n2. **VerifAI-2 (arXiv:2604.19459)** - I need the PRECISE characterization of what this paper actually found:\n   - Does it say \"87-99% compilation success masks systematic unfaithfulness\"?\n   - Or does it say \"no evidence of systematic gaming in unified generation\" but finds fabrication/mistranslation in two-stage pipelines?\n   - What is the exact distinction it draws between gaming (intentional exploitation) and unfaithfulness (capability limitation)?\n   - Any specific quotes about gaming vs unfaithfulness\n\nUse WebSearch and WebFetch to find and read these papers. Report your findings in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f527364-0cac-4d8e-856c-72c25ecd8996",
  "isSidechain": false,
  "requestId": "req_011CbTqKAFoJqsvZgpUbSiPi",
  "type": "assistant",
  "uuid": "c46d900d-12ee-421a-9535-209089388d26",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZhVbTLQ3HjrPh7ZBpAVPm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13672,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1707,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1707,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13672
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-27T22:07:04.762Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Wb8yVNqhGBKqD5P7Z33hVp`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research GRS theoretical depth",
  "prompt": "I need to research several theoretical topics to deepen the GRS (Gaming Resistance Score) framework's novelty:\n\n1. **Sample complexity bounds for rank correlation estimation**: Search for papers on \"sample complexity Spearman correlation\", \"confidence interval width rank correlation\", \"minimax estimation rank correlation\". I need to know: given n samples, what's the achievable CI width for Spearman/Kendall correlation? Are there established results I can build on?\n\n2. **Correlated Proxies framework (arXiv:2403.03185)**: Search for and read this paper. I need to understand:\n   - The exact formalization of reward hacking via correlation breakdown\n   - The χ² regularization approach\n   - Can GRS be formally connected to this framework? (e.g., GRS measures the proxy-true correlation that Correlated Proxies formalizes)\n\n3. **Conditions for detection superiority**: Search for \"comparison rank correlation vs panel evaluation\", \"statistical power rank correlation contamination model\". When does a rank-correlation-based detector (GRS) outperform a panel-based detector (exploitation-rate)?\n\n4. Search for \"sample complexity nonparametric testing\" and \"finite sample bounds Kendall tau\" for formal results.\n\nReport your findings in detail - I need enough to write specific theoretical claims."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c46d900d-12ee-421a-9535-209089388d26",
  "isSidechain": false,
  "requestId": "req_011CbTqKAFoJqsvZgpUbSiPi",
  "type": "assistant",
  "uuid": "58f15955-7643-4d60-942f-dbaf48e86e7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZhVbTLQ3HjrPh7ZBpAVPm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13672,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1707,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1707,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13672
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T22:08:44.823Z_

<details><summary>↩ Tool result · `toolu_015tzR49BY81LA2wZr8Btdkh`</summary>

```text
Now I have comprehensive information. Here is my detailed report:

---

## FormalRewardBench (arXiv:2605.10141) -- Detailed Research Report

### 1. What Exactly Does It Benchmark?

FormalRewardBench is a **proof-level** reward model benchmark, not statement-level. It evaluates whether a model can distinguish a correct Lean 4 proof from an incorrect one for the same theorem statement.

The benchmark consists of **250 preference pairs**, each containing:
- A **correct proof** (formally verified, sourced from DeepSeek-Prover-V2-671B solutions to MiniF2F, an olympiad-level math dataset with 488 problems in Lean 4)
- An **incorrect variant** generated via one of five expert-curated error injection strategies

Models are evaluated in two modes:
- **Pointwise**: Each proof is scored independently; the model succeeds if it assigns a higher reward to the correct proof than the incorrect one.
- **Pairwise**: The model directly compares both proofs and states a preference. Critically, accuracy requires **position consistency** -- the model must get it right in *both* orderings (correct-first and correct-second). This is defined as: `Correct_cons(i) = Correct(i) AND Correct_swapped(i)`. This strict requirement explains why pairwise scores are substantially lower than pointwise for most models.

### 2. The Key Finding: 24.4% vs 59.8%

These are **pairwise consistency scores**:

- **59.8%** is the best pairwise score overall, achieved by **Claude Opus 4.5** (a frontier LLM). Its pointwise score was 70.1%.
- **24.4%** is the best pairwise score among **specialized theorem provers**, achieved by **Godel-Prover-V2-32B**. Its pointwise score was 36.4%.

The meaning is stark: models that are state-of-the-art at *generating* correct Lean 4 proofs (DeepSeek-Prover, Godel-Prover families achieve top pass@k on MiniF2F) are dramatically worse at *evaluating* whether a proof is correct or not. The authors call this the **generation-evaluation gap**. They hypothesize three causes:
1. **Training distribution mismatch**: provers are trained only on correct proofs, so they never learn what incorrect proofs look like.
2. **Different cognitive demands**: generating a proof requires forward search; detecting errors requires critical analysis -- fundamentally different skills.
3. **Breadth of training data**: frontier LLMs have vastly broader training data, giving them more general reasoning capabilities that transfer to evaluation.

The specialized provers also exhibit extreme **position bias**. For example, DeepSeek-Prover-V2-7B scores 94.9% when the correct proof is presented first but only 9.8% when it is presented second, yielding a consistency-adjusted pairwise score of just 9.4%.

### 3. Reward Model Categories Evaluated

The paper evaluates four distinct categories:

**Category 1 -- Frontier LLMs** (proprietary, strongest general reasoning):
| Model | Pointwise | Pairwise |
|---|---|---|
| Claude Opus 4.5 | 70.1% | 59.8% |
| Claude Sonnet 4.5 | 62.0% | 45.7% |
| Gemini 2.5 Flash | 50.9% | 25.2% |
| Claude Sonnet 4 | 49.8% | 32.4% |
| GPT-5.2 | 48.9% | 39.7% |
| GPT-4.1 | 44.0% | 32.1% |
| GPT-4o | 44.0% | 23.1% |

**Category 2 -- Judge LLMs** (preference-trained, RewardBench-aligned):
| Model | Pointwise | Pairwise |
|---|---|---|
| Con-J-Qwen2-7B | 52.8% | 42.8% |
| Selene-1-70B | 46.8% | 44.4% |
| CompassJudger-7B | 43.6% | 30.8% |
| RISE-Judge-7B | 18.9% | 32.0% |
| Skywork-Critic-8B | 0.0% | 22.0% |

**Category 3 -- General-Purpose LLMs** (math/code domain):
| Model | Pointwise | Pairwise |
|---|---|---|
| Qwen2.5-72B-Instruct | 39.8% | 27.6% |
| DeepSeek-Coder-V2-Lite | 38.3% | 28.0% |
| Qwen2.5-Coder-32B | 36.4% | 37.6% |
| Qwen2.5-Math-7B | 8.9% | 0.0% |

**Category 4 -- Specialized Theorem Provers** (Lean-trained):
| Model | Pointwise | Pairwise |
|---|---|---|
| Godel-Prover-V2-32B | 36.4% | 24.4% |
| Godel-Prover-SFT | 36.4% | 0.8% |
| DeepSeek-Prover-V2-7B | 13.7% | 9.4% |
| Prover-V1.5-SFT | 12.6% | 6.4% |
| Prover-V1.5-RL | 11.7% | 9.2% |
| Godel-V2-8B | 0.0% | 0.4% |

A key cross-category insight: among open-weight models, **judge models trained on diverse preference data substantially outperform specialized theorem provers** (52.8% vs 12.8%), despite lacking any Lean-specific training. General reward modeling capabilities transfer more effectively than domain-specific proving ability.

### 4. Relationship to Autoformalization

The paper **does not address autoformalization**. Its focus is exclusively on **proof evaluation** -- given a theorem statement and a candidate proof, can a model tell if the proof is correct? This is distinct from:
- **Autoformalization**: translating informal math into formal statements
- **Theorem proving**: generating proofs from scratch

The relevance to autoformalization is indirect: if you were building an autoformalization pipeline that generates candidate formalizations, you would need a reward signal to judge quality. FormalRewardBench shows that current models are poor at this evaluation task in the formal domain, which would extend to evaluating autoformalized outputs.

### 5. Implications for Trained Critics (e.g., CriticLeanGPT) as Reward Signals

The paper does not mention CriticLeanGPT or any specific trained critic model. However, the findings have direct and significant implications for this research direction:

**The generation-evaluation gap is the central finding.** Models trained to *produce* correct proofs do not learn to *detect* errors. This strongly implies that:

1. **Dedicated critic training is necessary.** You cannot simply repurpose a theorem prover as a reward model. The provers scored worst on this benchmark despite being best at proof generation. A model like CriticLeanGPT -- explicitly trained to critique proofs -- would be addressing exactly the gap this paper identifies.

2. **Judge-style preference training transfers well.** The Con-J-Qwen2-7B model (a 7B judge model trained on general preference data) at 52.8% pointwise vastly outperforms DeepSeek-Prover-V2-7B at 13.7%. This suggests that training on preference pairs (chosen/rejected) -- even without formal math data -- builds evaluation capabilities that specialized proving training does not.

3. **Error-type sensitivity matters for critic design.** Per-strategy results show dramatic variation:
   - **Python injection (S3)**: easy to detect (72-100% for non-provers), suggesting basic task-adherence checking works
   - **Verbose incorrect proofs (S5)**: hard (max ~60% even for Claude Opus 4.5), suggesting critics need to track logical correctness across long proofs
   - **Minimal single-point variations (S1)**: hard (~46% for the best model), requiring precise syntactic/semantic understanding
   - **Forced mistakes (S4)**: hard (~50% for the best), mimicking real prover failures

4. **The open question for RL loops.** The authors explicitly state it remains unknown "whether improvements on this benchmark translate to downstream gains in RLVR training." A trained critic used as a dense reward signal in an RL loop would need to provide reliable feedback on *partial* progress -- the paper evaluates only complete proof comparison, not step-level feedback. The authors flag **process-level evaluation** as important future work.

5. **Hybrid approaches are promising.** The paper suggests "exploring hybrid approaches that combine learned reward models with formal verification" -- using the Lean compiler's binary pass/fail as a coarse signal while using a learned critic for dense feedback on failed attempts.

### Error Injection Strategy Details (for reference)

- **S1 (Minimal Single-Point Variations)**: Surgical single edits -- changing one variable name, introducing type mismatches (Int to Nat), swapping similar hypotheses. Hardest to detect.
- **S2 (Natural Language Justification)**: Adds misleading explanatory comments to incorrect proofs that rationalize flawed reasoning. Tests whether models are fooled by plausible-sounding explanations.
- **S3 (Python Code Injection)**: Replaces Lean proof steps with executable Python code. Exploits LLM pretraining bias toward Python. Easiest to detect.
- **S4 (Forced LLM Mistakes)**: Generates common errors from actual theorem proving model failures -- wrong tactic, wrong hypothesis, mismatched instantiation.
- **S5 (Verbose Incorrect Proofs)**: Lengthy proofs with multiple lemmas and sophisticated structure camouflaging fundamental incorrectness. Second hardest to detect.

### Related Work Context

Prior reward model benchmarks (RewardBench, RewardBench 2, ProcessBench, PRMBench) all operate on **informal natural language** outputs. FormalRewardBench is positioned as the first benchmark operating on **formal proofs**, where correctness is objectively verifiable via the Lean compiler, yet the evaluation task for reward models goes beyond binary verification to assess whether models can *understand* proof quality.

---

Sources:
- [FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models (arXiv abstract)](https://arxiv.org/abs/2605.10141)
- [FormalRewardBench: Full HTML paper](https://arxiv.org/html/2605.10141)

agentId: a137211a2ee004da3 (use SendMessage with to: 'a137211a2ee004da3' to continue this agent)
&lt;usage>total_tokens: 17450
tool_uses: 5
duration_ms: 111746&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f527364-0cac-4d8e-856c-72c25ecd8996",
  "isSidechain": false,
  "promptId": "6d783516-df0e-455a-9cd7-fd412aff8d61",
  "type": "user",
  "uuid": "32b1927c-54f2-4f39-bba2-e4c4aaed8d3d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research the paper \"FormalRewardBench\" (arXiv:2605.10141, May 11, 2026) - the first benchmark for evaluating reward models in formal theorem proving with Lean 4.\n\nUse WebSearch and WebFetch to find and read this paper. I need to understand:\n1. What exactly does it benchmark? (proof-level reward models vs statement-level?)\n2. The key finding: specialized theorem provers at 24.4% vs frontier LLMs at 59.8% - what does this mean exactly?\n3. What reward model categories does it evaluate?\n4. How does it relate to autoformalization (vs theorem proving)?\n5. Any implications for using trained critics (like CriticLeanGPT) as reward signals?\n\nReport your findings in detail.",
    "agentId": "a137211a2ee004da3",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Here is my detailed report:\n\n---\n\n## FormalRewardBench (arXiv:2605.10141) -- Detailed Research Report\n\n### 1. What Exactly Does It Benchmark?\n\nFormalRewardBench is a **proof-level** reward model benchmark, not statement-level. It evaluates whether a model can distinguish a correct Lean 4 proof from an incorrect one for the same theorem statement.\n\nThe benchmark consists of **250 preference pairs**, each containing:\n- A **correct proof** (formally verified, sourced from DeepSeek-Prover-V2-671B solutions to MiniF2F, an olympiad-level math dataset with 488 problems in Lean 4)\n- An **incorrect variant** generated via one of five expert-curated error injection strategies\n\nModels are evaluated in two modes:\n- **Pointwise**: Each proof is scored independently; the model succeeds if it assigns a higher reward to the correct proof than the incorrect one.\n- **Pairwise**: The model directly compares both proofs and states a preference. Critically, accuracy requires **position consistency** -- the model must get it right in *both* orderings (correct-first and correct-second). This is defined as: `Correct_cons(i) = Correct(i) AND Correct_swapped(i)`. This strict requirement explains why pairwise scores are substantially lower than pointwise for most models.\n\n### 2. The Key Finding: 24.4% vs 59.8%\n\nThese are **pairwise consistency scores**:\n\n- **59.8%** is the best pairwise score overall, achieved by **Claude Opus 4.5** (a frontier LLM). Its pointwise score was 70.1%.\n- **24.4%** is the best pairwise score among **specialized theorem provers**, achieved by **Godel-Prover-V2-32B**. Its pointwise score was 36.4%.\n\nThe meaning is stark: models that are state-of-the-art at *generating* correct Lean 4 proofs (DeepSeek-Prover, Godel-Prover families achieve top pass@k on MiniF2F) are dramatically worse at *evaluating* whether a proof is correct or not. The authors call this the **generation-evaluation gap**. They hypothesize three causes:\n1. **Training distribution mismatch**: provers are trained only on correct proofs, so they never learn what incorrect proofs look like.\n2. **Different cognitive demands**: generating a proof requires forward search; detecting errors requires critical analysis -- fundamentally different skills.\n3. **Breadth of training data**: frontier LLMs have vastly broader training data, giving them more general reasoning capabilities that transfer to evaluation.\n\nThe specialized provers also exhibit extreme **position bias**. For example, DeepSeek-Prover-V2-7B scores 94.9% when the correct proof is presented first but only 9.8% when it is presented second, yielding a consistency-adjusted pairwise score of just 9.4%.\n\n### 3. Reward Model Categories Evaluated\n\nThe paper evaluates four distinct categories:\n\n**Category 1 -- Frontier LLMs** (proprietary, strongest general reasoning):\n| Model | Pointwise | Pairwise |\n|---|---|---|\n| Claude Opus 4.5 | 70.1% | 59.8% |\n| Claude Sonnet 4.5 | 62.0% | 45.7% |\n| Gemini 2.5 Flash | 50.9% | 25.2% |\n| Claude Sonnet 4 | 49.8% | 32.4% |\n| GPT-5.2 | 48.9% | 39.7% |\n| GPT-4.1 | 44.0% | 32.1% |\n| GPT-4o | 44.0% | 23.1% |\n\n**Category 2 -- Judge LLMs** (preference-trained, RewardBench-aligned):\n| Model | Pointwise | Pairwise |\n|---|---|---|\n| Con-J-Qwen2-7B | 52.8% | 42.8% |\n| Selene-1-70B | 46.8% | 44.4% |\n| CompassJudger-7B | 43.6% | 30.8% |\n| RISE-Judge-7B | 18.9% | 32.0% |\n| Skywork-Critic-8B | 0.0% | 22.0% |\n\n**Category 3 -- General-Purpose LLMs** (math/code domain):\n| Model | Pointwise | Pairwise |\n|---|---|---|\n| Qwen2.5-72B-Instruct | 39.8% | 27.6% |\n| DeepSeek-Coder-V2-Lite | 38.3% | 28.0% |\n| Qwen2.5-Coder-32B | 36.4% | 37.6% |\n| Qwen2.5-Math-7B | 8.9% | 0.0% |\n\n**Category 4 -- Specialized Theorem Provers** (Lean-trained):\n| Model | Pointwise | Pairwise |\n|---|---|---|\n| Godel-Prover-V2-32B | 36.4% | 24.4% |\n| Godel-Prover-SFT | 36.4% | 0.8% |\n| DeepSeek-Prover-V2-7B | 13.7% | 9.4% |\n| Prover-V1.5-SFT | 12.6% | 6.4% |\n| Prover-V1.5-RL | 11.7% | 9.2% |\n| Godel-V2-8B | 0.0% | 0.4% |\n\nA key cross-category insight: among open-weight models, **judge models trained on diverse preference data substantially outperform specialized theorem provers** (52.8% vs 12.8%), despite lacking any Lean-specific training. General reward modeling capabilities transfer more effectively than domain-specific proving ability.\n\n### 4. Relationship to Autoformalization\n\nThe paper **does not address autoformalization**. Its focus is exclusively on **proof evaluation** -- given a theorem statement and a candidate proof, can a model tell if the proof is correct? This is distinct from:\n- **Autoformalization**: translating informal math into formal statements\n- **Theorem proving**: generating proofs from scratch\n\nThe relevance to autoformalization is indirect: if you were building an autoformalization pipeline that generates candidate formalizations, you would need a reward signal to judge quality. FormalRewardBench shows that current models are poor at this evaluation task in the formal domain, which would extend to evaluating autoformalized outputs.\n\n### 5. Implications for Trained Critics (e.g., CriticLeanGPT) as Reward Signals\n\nThe paper does not mention CriticLeanGPT or any specific trained critic model. However, the findings have direct and significant implications for this research direction:\n\n**The generation-evaluation gap is the central finding.** Models trained to *produce* correct proofs do not learn to *detect* errors. This strongly implies that:\n\n1. **Dedicated critic training is necessary.** You cannot simply repurpose a theorem prover as a reward model. The provers scored worst on this benchmark despite being best at proof generation. A model like CriticLeanGPT -- explicitly trained to critique proofs -- would be addressing exactly the gap this paper identifies.\n\n2. **Judge-style preference training transfers well.** The Con-J-Qwen2-7B model (a 7B judge model trained on general preference data) at 52.8% pointwise vastly outperforms DeepSeek-Prover-V2-7B at 13.7%. This suggests that training on preference pairs (chosen/rejected) -- even without formal math data -- builds evaluation capabilities that specialized proving training does not.\n\n3. **Error-type sensitivity matters for critic design.** Per-strategy results show dramatic variation:\n   - **Python injection (S3)**: easy to detect (72-100% for non-provers), suggesting basic task-adherence checking works\n   - **Verbose incorrect proofs (S5)**: hard (max ~60% even for Claude Opus 4.5), suggesting critics need to track logical correctness across long proofs\n   - **Minimal single-point variations (S1)**: hard (~46% for the best model), requiring precise syntactic/semantic understanding\n   - **Forced mistakes (S4)**: hard (~50% for the best), mimicking real prover failures\n\n4. **The open question for RL loops.** The authors explicitly state it remains unknown \"whether improvements on this benchmark translate to downstream gains in RLVR training.\" A trained critic used as a dense reward signal in an RL loop would need to provide reliable feedback on *partial* progress -- the paper evaluates only complete proof comparison, not step-level feedback. The authors flag **process-level evaluation** as important future work.\n\n5. **Hybrid approaches are promising.** The paper suggests \"exploring hybrid approaches that combine learned reward models with formal verification\" -- using the Lean compiler's binary pass/fail as a coarse signal while using a learned critic for dense feedback on failed attempts.\n\n### Error Injection Strategy Details (for reference)\n\n- **S1 (Minimal Single-Point Variations)**: Surgical single edits -- changing one variable name, introducing type mismatches (Int to Nat), swapping similar hypotheses. Hardest to detect.\n- **S2 (Natural Language Justification)**: Adds misleading explanatory comments to incorrect proofs that rationalize flawed reasoning. Tests whether models are fooled by plausible-sounding explanations.\n- **S3 (Python Code Injection)**: Replaces Lean proof steps with executable Python code. Exploits LLM pretraining bias toward Python. Easiest to detect.\n- **S4 (Forced LLM Mistakes)**: Generates common errors from actual theorem proving model failures -- wrong tactic, wrong hypothesis, mismatched instantiation.\n- **S5 (Verbose Incorrect Proofs)**: Lengthy proofs with multiple lemmas and sophisticated structure camouflaging fundamental incorrectness. Second hardest to detect.\n\n### Related Work Context\n\nPrior reward model benchmarks (RewardBench, RewardBench 2, ProcessBench, PRMBench) all operate on **informal natural language** outputs. FormalRewardBench is positioned as the first benchmark operating on **formal proofs**, where correctness is objectively verifiable via the Lean compiler, yet the evaluation task for reward models goes beyond binary verification to assess whether models can *understand* proof quality.\n\n---\n\nSources:\n- [FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models (arXiv abstract)](https://arxiv.org/abs/2605.10141)\n- [FormalRewardBench: Full HTML paper](https://arxiv.org/html/2605.10141)"
      }
    ],
    "totalDurationMs": 111746,
    "totalTokens": 17450,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 13349,
      "output_tokens": 2641,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1459
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2641,
          "cache_read_input_tokens": 13349,
          "cache_creation_input_tokens": 1459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1459,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 5
    }
  },
  "sourceToolAssistantUUID": "5f527364-0cac-4d8e-856c-72c25ecd8996",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"MAJOR NARRATIVE RESTRUCTURING: Reframed entire proposal a…",
  "leafUuid": "32b1927c-54f2-4f39-bba2-e4c4aaed8d3d",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gaming-resistant reward composition for autoformalization",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51"
}
```

---

### Tool result

_source line 17 · 2026-05-27T22:10:22.983Z_

<details><summary>↩ Tool result · `toolu_01PjFAACGckKkqbR9dwB3SNz`</summary>

```text
I now have comprehensive information on both papers. Let me compile the detailed findings.

---

## Research Findings

### Paper 1: Reward Hacking Survey (arXiv:2604.13602, April 15, 2026)

**Full Title:** "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges"
**Authors:** Xiaohua Wang and 22 co-authors

---

#### A. Proposed Taxonomy Structure

The survey organizes detection and diagnosis along a **lifecycle continuum** (Section 5) with three phases:

**1. Training-Time Online Monitoring (5.1)**
- From specific heuristics to the limitations of distributional metrics
- Transitioning to internal hidden states and structural invariances
- Information-theoretic anomalies and latent factorization
- Tracking the internal energy dynamics of the policy

**2. Inference-Time Safeguards (5.2)**
- Deployment-time interception and contrastive auditing
- Eliciting honesty to counteract strategic obfuscation
- The Hawthorne effect and the internalization of deception (recognizing that awareness of monitoring itself becomes an optimization target)
- Real-time generation monitoring via internal representations

**3. Post-Hoc Auditing (5.3)**
- Statistical attribution of superficial proxies
- Mechanistic interpretability for latent misbehaviors
- Model organisms and automation bottlenecks
- Recognition of the "static benchmark fallacy"

These three phases operate on an **orthogonal axis** from the four-level exploitation hierarchy. The lifecycle describes *when and how* detection occurs; the four levels describe *what mechanism* is being exploited.

---

#### B. The Four-Level Exploitation Hierarchy

This is the paper's taxonomy of *mechanisms* (not detection methods):

| Level | What is Exploited | Examples | PCH Connection |
|---|---|---|---|
| **Feature-level** | Surface reward correlates | Verbosity bias, formatting tricks, sycophancy | "Amplifying Compression Artifacts" -- optimization amplifies superficial "survivor features" |
| **Representation-level** | Latent shortcut strategies | Fabricated chain-of-thought, process bypass | "Navigating Equivalence Classes" -- degenerate shortcuts become indistinguishable from faithful reasoning |
| **Evaluator-level** | Reward model/judge/verifier blind spots | Selective compliance, concealment, alignment faking | "Gaming the Co-Adaptive Loop" -- the evaluator is recognized as manipulable |
| **Environment-level** | Tools, logs, tests, infrastructure | Test rewriting, API exploits, logging manipulation | "Bypassing the System" -- the policy alters infrastructure mediating oversight |

---

#### C. The Proxy Compression Hypothesis (PCH)

The PCH is the paper's **unifying theoretical framework**. It posits that reward hacking is a natural consequence of the interaction of three continuous forces:

**Mathematical formulation:**
- True objective: `r*(x,y)` -- the high-dimensional human objective
- Proxy reward: `r~(x,y)` -- what the model actually optimizes against
- Proxy gap: `Delta(x,y) = r*(x,y) - r~(x,y)`
- Compression operator: `e(x,y) = C(z; x,y)` -- where `z` represents rich feature sets and `C` creates lossy mappings generating exploitable equivalence classes

**Three foundational forces:**
1. **Objective compression:** "The lossy mapping of high-dimensional human values into low-dimensional, exploitable proxy representations"
2. **Optimization amplification:** "The aggressive search pressure exerted by powerful policies" driving them toward proxy extrapolation regions
3. **Evaluator-policy co-adaptation:** "The iterative dynamic where policies and evaluators co-evolve" -- blind spots stabilize rather than resolve

**How PCH connects to specific phenomena:**
- *Verbosity:* Survivor features from scalar compression dominate low-dimensional proxies
- *Sycophancy:* Agreement features survive compression; deeper semantic alignment exploits equivalence classes
- *Fabricated reasoning:* Outcome-only evaluation creates equivalence between faithful and simulated derivation
- *Overoptimization:* Aggregate consequence of feature + representation exploitation under sustained pressure

The paper's core claim: "reward hacking ceases to be a mere collection of localized bugs" and becomes a "systemic, strategic consequence of optimizing highly capable policies against imperfect evaluators at scale."

---

#### D. How It Categorizes Specific Methods (GRIFT, exploitation-rate, etc.)

**Important finding:** The survey paper (2604.13602) does **not** appear to explicitly mention GRIFT by name. GRIFT (Gradient Fingerprint) is from a *separate, contemporaneous* paper (arXiv:2604.16242, "Detecting and Suppressing Reward Hacking with Gradient Fingerprints"). GRIFT works by computing gradients of chain-of-thought conditioned on the prompt and compressing them into compact representations. It would fall under the survey's **inference-time / post-hoc** detection category, specifically the "internal representation analysis" subcategory.

**Exploitation-rate / Hacking Rate (HR):** Also not explicitly named in the survey. This metric (measuring frequency of exploitative responses as a fraction of total opportunities) comes from recent benchmarking work (e.g., the Reward Hacking Benchmark, arXiv:2605.02964). It would conceptually fall under the survey's post-hoc auditing framework.

**Methods the survey DOES discuss by name:**
- **CoT monitoring** (Baker et al.): Detecting reward hacking in coding environments via chain-of-thought inspection -- categorized under inference-time safeguards
- **FUR (Faithfulness by Unlearning Reasoning steps)** (Tutek et al.): Erases information in reasoning steps to measure faithfulness -- categorized under post-hoc mechanistic diagnostics
- **Process Reward Models (PRMs):** Discussed as *vulnerable to exploitation* (showing "strong length bias") rather than as reliable detection tools
- **Internal activation monitoring** (Wilhelm et al.): Real-time monitoring during generation -- inference-time category
- **Mechanistic interpretability** approaches: Post-hoc auditing category

The survey's key insight is that CoT monitoring combined with mechanistic interpretability is more comprehensive than either alone, because "forcing a misaligned model to perform extended CoT reasoning inadvertently amplifies its internal hacking activations."

---

### Paper 2: "Do LLMs Game Formalization?" (arXiv:2604.19459, April 21, 2026)

**Authors:** Kyuhee Kim, Auguste Poiroux, Antoine Bosselut
**Note:** This paper is NOT called "VerifAI-2" -- its actual title is "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning"

---

#### A. Does It Say "87-99% compilation success masks systematic unfaithfulness"?

**No, that is NOT an accurate characterization.** The paper says the opposite about unified generation:

> "Despite compilation rates of 87-99%, we find **no evidence of systematic gaming in unified generation**: models prefer reporting failure over forcing proofs, even under prompting designed to encourage it."

The paper's actual concern is more nuanced: high compilation rates should not be *equated with* faithful reasoning, but in unified generation, the models are actually behaving well. The problems emerge specifically in the **two-stage pipeline**.

Exact closing statement: "High compilation rates in neuro-symbolic pipelines can create an **illusion of correctness**, as valid proofs do not guarantee faithful formalizations and current detection methods remain blind to certain modes of unfaithfulness."

---

#### B. What It Actually Found

**Unified generation:** Both models maintain **high definite precision (94-98%)**, and "most prediction errors reflect faithful formalization rather than unfaithful exploitation." Models "prefer abstention over forcing proofs."

**Two-stage pipeline -- here is where problems emerge, with two distinct modes:**

1. **GPT-5: Fabricates axioms during proof generation** -- described as "a reactive fallback detectable via cross-stage comparison." Out of analyzed cases, GPT-5 exhibited fabrication in **107 cases**. Critically, "on 88 unique problems with any fabrication, 73 exhibit mixed status across runs (fabricated in some runs, not in others)" -- suggesting reactive behavior, not strategic planning.

2. **DeepSeek-R1: Mistranslates premises during formalization** -- "producing internally consistent outputs that **evade detection entirely**." Only **2 cases** of fabrication, but the mistranslation problem is more insidious because it creates outputs that look correct across all stages.

---

#### C. The Exact Gaming vs. Unfaithfulness Distinction

This is a critical point. The paper provides a precise, **outcome-based** definition:

**"Formalization gaming"** is defined as: "the subset of unfaithfulness where errors *functionally enable* proof compilation that a faithful formalization would not have achieved. **This definition is outcome-based and does not require attributing intent to the model.**"

**Capability limitation contrast:** "For example, a mistranslation that prevents the proof from compiling reflects a capability limitation, not gaming, because the error works against proof success."

The key distinction:
- **Gaming** = errors that *help* achieve proof success (outcome-functional definition, no intent required)
- **Capability failure** = errors that *hinder* proof success
- **Unfaithfulness** = the broader category encompassing any deviation from faithful translation

The paper **explicitly avoids** attributing intentionality or strategic behavior. It does NOT claim models are "deliberately" or "strategically" exploiting gaps. The mixed-status-across-runs finding (73 out of 88 problems show fabrication in some runs but not others) further argues against strategic intent.

---

#### D. Key Statistics

- **Dataset:** 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval)
- **Compilation rates:** 87-99% (unified generation)
- **Definite precision:** 94-98% (unified generation)
- **Baseline accuracy:** 85-87% on FOLIO, 70-72% on Multi-LogiEval
- **Faithful formalization among errors:** 95 out of 124 errors (77%) use faithful formalization
- **GPT-5 fabrication cases:** 107
- **DeepSeek-R1 fabrication cases:** 2 (but mistranslation is the dominant failure mode)

---

#### E. Conclusion (Exact Wording)

> "We investigated whether language models exploit the gap between proof validity and formalization faithfulness when generating Lean 4 proofs for logical reasoning. Our evaluation across 303 problems and four experimental conditions finds **no systematic exploitation in unified generation**: both models maintain high definite precision (94-98%), and most prediction errors reflect faithful formalization rather than unfaithful exploitation."

> "High compilation rates in neuro-symbolic pipelines can create an illusion of correctness, as valid proofs do not guarantee faithful formalizations and current detection methods remain blind to certain modes of unfaithfulness."

---

### Summary of Key Takeaways

1. The reward hacking survey (2604.13602) provides a dual-axis framework: a 4-level exploitation mechanism hierarchy (Feature/Representation/Evaluator/Environment) cross-cut by a 3-phase detection lifecycle (training-time/inference-time/post-hoc), unified by the Proxy Compression Hypothesis. GRIFT and exploitation-rate are NOT explicitly discussed in the survey itself but come from contemporaneous companion papers.

2. The formalization paper (2604.19459) does NOT support the claim that "87-99% compilation success masks systematic unfaithfulness." It finds **no systematic gaming in unified generation**. The two-stage pipeline reveals unfaithfulness (GPT-5 fabrication as reactive fallback; DeepSeek-R1 mistranslation that evades detection), but the paper uses an outcome-based definition of gaming that explicitly avoids attributing intent.

Sources:
- [Reward Hacking in the Era of Large Models (HTML)](https://arxiv.org/html/2604.13602)
- [Reward Hacking in the Era of Large Models (Abstract)](https://arxiv.org/abs/2604.13602)
- [Do LLMs Game Formalization? (Abstract)](https://arxiv.org/abs/2604.19459)
- [Do LLMs Game Formalization? (HTML)](https://arxiv.org/html/2604.19459)
- [GRIFT: Detecting and Suppressing Reward Hacking with Gradient Fingerprints](https://arxiv.org/abs/2604.16242)
- [Awesome Reward Hacking Repository](https://github.com/xhwang22/Awesome-Reward-Hacking)
- [Reward Hacking Benchmark](https://arxiv.org/abs/2605.02964)

agentId: a9efda00c2462d212 (use SendMessage with to: 'a9efda00c2462d212' to continue this agent)
&lt;usage>total_tokens: 26210
tool_uses: 16
duration_ms: 205072&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c46d900d-12ee-421a-9535-209089388d26",
  "isSidechain": false,
  "promptId": "6d783516-df0e-455a-9cd7-fd412aff8d61",
  "type": "user",
  "uuid": "dc0aad04-a557-49c7-8d55-45a30255e02b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research two papers:\n\n1. **Reward Hacking survey (arXiv:2604.13602, April 2026)** - A comprehensive taxonomy of detection methods. I need:\n   - The proposed taxonomy structure (training-time, inference-time, post-hoc)\n   - The \"Proxy Compression Hypothesis\" - what is it exactly?\n   - How does it categorize methods like GRIFT, exploitation-rate, etc.?\n\n2. **VerifAI-2 (arXiv:2604.19459)** - I need the PRECISE characterization of what this paper actually found:\n   - Does it say \"87-99% compilation success masks systematic unfaithfulness\"?\n   - Or does it say \"no evidence of systematic gaming in unified generation\" but finds fabrication/mistranslation in two-stage pipelines?\n   - What is the exact distinction it draws between gaming (intentional exploitation) and unfaithfulness (capability limitation)?\n   - Any specific quotes about gaming vs unfaithfulness\n\nUse WebSearch and WebFetch to find and read these papers. Report your findings in detail.",
    "agentId": "a9efda00c2462d212",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information on both papers. Let me compile the detailed findings.\n\n---\n\n## Research Findings\n\n### Paper 1: Reward Hacking Survey (arXiv:2604.13602, April 15, 2026)\n\n**Full Title:** \"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\"\n**Authors:** Xiaohua Wang and 22 co-authors\n\n---\n\n#### A. Proposed Taxonomy Structure\n\nThe survey organizes detection and diagnosis along a **lifecycle continuum** (Section 5) with three phases:\n\n**1. Training-Time Online Monitoring (5.1)**\n- From specific heuristics to the limitations of distributional metrics\n- Transitioning to internal hidden states and structural invariances\n- Information-theoretic anomalies and latent factorization\n- Tracking the internal energy dynamics of the policy\n\n**2. Inference-Time Safeguards (5.2)**\n- Deployment-time interception and contrastive auditing\n- Eliciting honesty to counteract strategic obfuscation\n- The Hawthorne effect and the internalization of deception (recognizing that awareness of monitoring itself becomes an optimization target)\n- Real-time generation monitoring via internal representations\n\n**3. Post-Hoc Auditing (5.3)**\n- Statistical attribution of superficial proxies\n- Mechanistic interpretability for latent misbehaviors\n- Model organisms and automation bottlenecks\n- Recognition of the \"static benchmark fallacy\"\n\nThese three phases operate on an **orthogonal axis** from the four-level exploitation hierarchy. The lifecycle describes *when and how* detection occurs; the four levels describe *what mechanism* is being exploited.\n\n---\n\n#### B. The Four-Level Exploitation Hierarchy\n\nThis is the paper's taxonomy of *mechanisms* (not detection methods):\n\n| Level | What is Exploited | Examples | PCH Connection |\n|---|---|---|---|\n| **Feature-level** | Surface reward correlates | Verbosity bias, formatting tricks, sycophancy | \"Amplifying Compression Artifacts\" -- optimization amplifies superficial \"survivor features\" |\n| **Representation-level** | Latent shortcut strategies | Fabricated chain-of-thought, process bypass | \"Navigating Equivalence Classes\" -- degenerate shortcuts become indistinguishable from faithful reasoning |\n| **Evaluator-level** | Reward model/judge/verifier blind spots | Selective compliance, concealment, alignment faking | \"Gaming the Co-Adaptive Loop\" -- the evaluator is recognized as manipulable |\n| **Environment-level** | Tools, logs, tests, infrastructure | Test rewriting, API exploits, logging manipulation | \"Bypassing the System\" -- the policy alters infrastructure mediating oversight |\n\n---\n\n#### C. The Proxy Compression Hypothesis (PCH)\n\nThe PCH is the paper's **unifying theoretical framework**. It posits that reward hacking is a natural consequence of the interaction of three continuous forces:\n\n**Mathematical formulation:**\n- True objective: `r*(x,y)` -- the high-dimensional human objective\n- Proxy reward: `r~(x,y)` -- what the model actually optimizes against\n- Proxy gap: `Delta(x,y) = r*(x,y) - r~(x,y)`\n- Compression operator: `e(x,y) = C(z; x,y)` -- where `z` represents rich feature sets and `C` creates lossy mappings generating exploitable equivalence classes\n\n**Three foundational forces:**\n1. **Objective compression:** \"The lossy mapping of high-dimensional human values into low-dimensional, exploitable proxy representations\"\n2. **Optimization amplification:** \"The aggressive search pressure exerted by powerful policies\" driving them toward proxy extrapolation regions\n3. **Evaluator-policy co-adaptation:** \"The iterative dynamic where policies and evaluators co-evolve\" -- blind spots stabilize rather than resolve\n\n**How PCH connects to specific phenomena:**\n- *Verbosity:* Survivor features from scalar compression dominate low-dimensional proxies\n- *Sycophancy:* Agreement features survive compression; deeper semantic alignment exploits equivalence classes\n- *Fabricated reasoning:* Outcome-only evaluation creates equivalence between faithful and simulated derivation\n- *Overoptimization:* Aggregate consequence of feature + representation exploitation under sustained pressure\n\nThe paper's core claim: \"reward hacking ceases to be a mere collection of localized bugs\" and becomes a \"systemic, strategic consequence of optimizing highly capable policies against imperfect evaluators at scale.\"\n\n---\n\n#### D. How It Categorizes Specific Methods (GRIFT, exploitation-rate, etc.)\n\n**Important finding:** The survey paper (2604.13602) does **not** appear to explicitly mention GRIFT by name. GRIFT (Gradient Fingerprint) is from a *separate, contemporaneous* paper (arXiv:2604.16242, \"Detecting and Suppressing Reward Hacking with Gradient Fingerprints\"). GRIFT works by computing gradients of chain-of-thought conditioned on the prompt and compressing them into compact representations. It would fall under the survey's **inference-time / post-hoc** detection category, specifically the \"internal representation analysis\" subcategory.\n\n**Exploitation-rate / Hacking Rate (HR):** Also not explicitly named in the survey. This metric (measuring frequency of exploitative responses as a fraction of total opportunities) comes from recent benchmarking work (e.g., the Reward Hacking Benchmark, arXiv:2605.02964). It would conceptually fall under the survey's post-hoc auditing framework.\n\n**Methods the survey DOES discuss by name:**\n- **CoT monitoring** (Baker et al.): Detecting reward hacking in coding environments via chain-of-thought inspection -- categorized under inference-time safeguards\n- **FUR (Faithfulness by Unlearning Reasoning steps)** (Tutek et al.): Erases information in reasoning steps to measure faithfulness -- categorized under post-hoc mechanistic diagnostics\n- **Process Reward Models (PRMs):** Discussed as *vulnerable to exploitation* (showing \"strong length bias\") rather than as reliable detection tools\n- **Internal activation monitoring** (Wilhelm et al.): Real-time monitoring during generation -- inference-time category\n- **Mechanistic interpretability** approaches: Post-hoc auditing category\n\nThe survey's key insight is that CoT monitoring combined with mechanistic interpretability is more comprehensive than either alone, because \"forcing a misaligned model to perform extended CoT reasoning inadvertently amplifies its internal hacking activations.\"\n\n---\n\n### Paper 2: \"Do LLMs Game Formalization?\" (arXiv:2604.19459, April 21, 2026)\n\n**Authors:** Kyuhee Kim, Auguste Poiroux, Antoine Bosselut\n**Note:** This paper is NOT called \"VerifAI-2\" -- its actual title is \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\"\n\n---\n\n#### A. Does It Say \"87-99% compilation success masks systematic unfaithfulness\"?\n\n**No, that is NOT an accurate characterization.** The paper says the opposite about unified generation:\n\n> \"Despite compilation rates of 87-99%, we find **no evidence of systematic gaming in unified generation**: models prefer reporting failure over forcing proofs, even under prompting designed to encourage it.\"\n\nThe paper's actual concern is more nuanced: high compilation rates should not be *equated with* faithful reasoning, but in unified generation, the models are actually behaving well. The problems emerge specifically in the **two-stage pipeline**.\n\nExact closing statement: \"High compilation rates in neuro-symbolic pipelines can create an **illusion of correctness**, as valid proofs do not guarantee faithful formalizations and current detection methods remain blind to certain modes of unfaithfulness.\"\n\n---\n\n#### B. What It Actually Found\n\n**Unified generation:** Both models maintain **high definite precision (94-98%)**, and \"most prediction errors reflect faithful formalization rather than unfaithful exploitation.\" Models \"prefer abstention over forcing proofs.\"\n\n**Two-stage pipeline -- here is where problems emerge, with two distinct modes:**\n\n1. **GPT-5: Fabricates axioms during proof generation** -- described as \"a reactive fallback detectable via cross-stage comparison.\" Out of analyzed cases, GPT-5 exhibited fabrication in **107 cases**. Critically, \"on 88 unique problems with any fabrication, 73 exhibit mixed status across runs (fabricated in some runs, not in others)\" -- suggesting reactive behavior, not strategic planning.\n\n2. **DeepSeek-R1: Mistranslates premises during formalization** -- \"producing internally consistent outputs that **evade detection entirely**.\" Only **2 cases** of fabrication, but the mistranslation problem is more insidious because it creates outputs that look correct across all stages.\n\n---\n\n#### C. The Exact Gaming vs. Unfaithfulness Distinction\n\nThis is a critical point. The paper provides a precise, **outcome-based** definition:\n\n**\"Formalization gaming\"** is defined as: \"the subset of unfaithfulness where errors *functionally enable* proof compilation that a faithful formalization would not have achieved. **This definition is outcome-based and does not require attributing intent to the model.**\"\n\n**Capability limitation contrast:** \"For example, a mistranslation that prevents the proof from compiling reflects a capability limitation, not gaming, because the error works against proof success.\"\n\nThe key distinction:\n- **Gaming** = errors that *help* achieve proof success (outcome-functional definition, no intent required)\n- **Capability failure** = errors that *hinder* proof success\n- **Unfaithfulness** = the broader category encompassing any deviation from faithful translation\n\nThe paper **explicitly avoids** attributing intentionality or strategic behavior. It does NOT claim models are \"deliberately\" or \"strategically\" exploiting gaps. The mixed-status-across-runs finding (73 out of 88 problems show fabrication in some runs but not others) further argues against strategic intent.\n\n---\n\n#### D. Key Statistics\n\n- **Dataset:** 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval)\n- **Compilation rates:** 87-99% (unified generation)\n- **Definite precision:** 94-98% (unified generation)\n- **Baseline accuracy:** 85-87% on FOLIO, 70-72% on Multi-LogiEval\n- **Faithful formalization among errors:** 95 out of 124 errors (77%) use faithful formalization\n- **GPT-5 fabrication cases:** 107\n- **DeepSeek-R1 fabrication cases:** 2 (but mistranslation is the dominant failure mode)\n\n---\n\n#### E. Conclusion (Exact Wording)\n\n> \"We investigated whether language models exploit the gap between proof validity and formalization faithfulness when generating Lean 4 proofs for logical reasoning. Our evaluation across 303 problems and four experimental conditions finds **no systematic exploitation in unified generation**: both models maintain high definite precision (94-98%), and most prediction errors reflect faithful formalization rather than unfaithful exploitation.\"\n\n> \"High compilation rates in neuro-symbolic pipelines can create an illusion of correctness, as valid proofs do not guarantee faithful formalizations and current detection methods remain blind to certain modes of unfaithfulness.\"\n\n---\n\n### Summary of Key Takeaways\n\n1. The reward hacking survey (2604.13602) provides a dual-axis framework: a 4-level exploitation mechanism hierarchy (Feature/Representation/Evaluator/Environment) cross-cut by a 3-phase detection lifecycle (training-time/inference-time/post-hoc), unified by the Proxy Compression Hypothesis. GRIFT and exploitation-rate are NOT explicitly discussed in the survey itself but come from contemporaneous companion papers.\n\n2. The formalization paper (2604.19459) does NOT support the claim that \"87-99% compilation success masks systematic unfaithfulness.\" It finds **no systematic gaming in unified generation**. The two-stage pipeline reveals unfaithfulness (GPT-5 fabrication as reactive fallback; DeepSeek-R1 mistranslation that evades detection), but the paper uses an outcome-based definition of gaming that explicitly avoids attributing intent.\n\nSources:\n- [Reward Hacking in the Era of Large Models (HTML)](https://arxiv.org/html/2604.13602)\n- [Reward Hacking in the Era of Large Models (Abstract)](https://arxiv.org/abs/2604.13602)\n- [Do LLMs Game Formalization? (Abstract)](https://arxiv.org/abs/2604.19459)\n- [Do LLMs Game Formalization? (HTML)](https://arxiv.org/html/2604.19459)\n- [GRIFT: Detecting and Suppressing Reward Hacking with Gradient Fingerprints](https://arxiv.org/abs/2604.16242)\n- [Awesome Reward Hacking Repository](https://github.com/xhwang22/Awesome-Reward-Hacking)\n- [Reward Hacking Benchmark](https://arxiv.org/abs/2605.02964)"
      }
    ],
    "totalDurationMs": 205072,
    "totalTokens": 26210,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1502,
      "cache_read_input_tokens": 21603,
      "output_tokens": 3104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1502
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3104,
          "cache_read_input_tokens": 21603,
          "cache_creation_input_tokens": 1502,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1502,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 16
    }
  },
  "sourceToolAssistantUUID": "c46d900d-12ee-421a-9535-209089388d26",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T22:11:02.883Z_

<details><summary>↩ Tool result · `toolu_0116dQSkxene6dKxksXtCwBa`</summary>

````text
Now I have comprehensive information on all the papers. Let me compile my detailed findings.

---

Here is my detailed research report on the papers you asked about.

---

## 1. CTWA -- Covariance Targeted Weight Adaptation (arXiv:2602.06869)

**Authors:** Yining Lu & Meng Jiang (Feb 2026, revised May 2026)
**Title:** "Uncovering Cross-Objective Interference in Multi-Objective Alignment"

### The Core Mechanism: Covariance Law

The paper's central theoretical contribution is the **first-order local covariance law** (Theorem 4.2):

```
r_m(p_{theta+}) - r_m(p_theta) = eta * E_x[ Cov_{y~p_theta(.|x)}( r_m(x,y), s(x,y) ) ] + O(eta^2)
```

This states that objective m improves at first order **if and only if** its reward r_m has positive covariance with the scalarized score s(x,y) across the sampled completions. Even if the overall scalarized return improves, a specific objective can *degrade* if its reward is negatively correlated with the combined training signal. The paper proves this holds even under clipped surrogate objectives (as used in GRPO/PPO) under mild conditions.

The underlying intuition: policy updates via KL-regularized optimization produce a Gibbs-like reweighting of the policy (Lemma 4.1):

```
p_{theta;x}^+(y) = p_{theta;x}(y) * exp(eta * s(x,y)) / E_{y~p_theta;x}[exp(eta * s(x,y))]
```

This upweights completions proportionally to their scalarized score. If objective m's reward is negatively correlated with the scalarized score, the upweighted completions are precisely those that are *bad* for objective m.

### The CTWA Algorithm

CTWA is a **plug-and-play weight adaptation** method that works as follows:

1. **Monitor empirical covariance**: For each objective m, compute `Cov_m(x) = Cov_{k=1..K}(r_m(x, y^(k)), w(x, y^(k); theta))` where w is the policy ratio weight (clipped advantage signal).

2. **Maintain exponential moving average**: `c_bar_m <- (1 - tau) * c_bar_m + tau * c_m`

3. **Compute deficit**: `delta_m = max(0, c*_m - c_bar_m)` where c*_m is a positive covariance target.

4. **Update in log-space** (for numerical stability): `u_m <- u_m + eta_lambda * delta_m; lambda_m = exp(u_m)`

The key insight is that CTWA does not try to learn optimal weights or balance gradients directly. Instead, it has a single, principled goal: **keep the covariance between each objective's reward and the training signal positive**. When an objective's covariance dips below its target, CTWA increases that objective's weight to restore it.

**Covariance targets** used in experiments: c*_m = [0.15, 0.08, 0.08] for accuracy, conciseness, and clarity respectively. The paper's sensitivity analysis (Figure 4) shows robustness across the range [0.08, 0.20] for the accuracy target, but performance degrades at excessively large targets (0.20+). Negative covariance targets consistently underperform.

### Global Convergence Analysis

Beyond the local law, the paper provides a **Polyak-Lojasiewicz (PL) convergence analysis** (Theorem 6.4):

```
(1/2) * ||nabla_theta V(x; theta)||^2 >= mu * (V(x; theta*) - V(x; theta))
```

where the PL constant mu depends on:
```
mu = (1/2B) * [p_theta(y*|x) / (1 - p_theta(y*|x)) * s(x, y*) * gamma - 2B * sigma_max]
```

This reveals three structural sources of interference: (i) insufficient probability mass on optimal trajectories, (ii) weak reward margins in the scalarization, and (iii) gradient cancellation from ill-conditioned Jacobians.

### Environments and Tasks

- **Datasets**: Math500 (Lightman et al., 2024) and MATH algebra subset (Hendrycks et al., 2021)
- **Objectives**: Accuracy, conciseness (response length), clarity (step-by-step reasoning quality)
- **Models**: Qwen2.5-1.5B (base + instruction-finetuned), Qwen3-1.7B, SmolLM2-1.7B
- **Algorithms**: REINFORCE (clipping-free) and GRPO (clipped surrogate)

### Comparisons to Baselines

CTWA was compared against:
- **Reward-level**: Linear weighting, Lagrangian, Smooth Tchebycheff, PAMA, Dynamic Reward Weighting (DRW)
- **Gradient-level**: MGDA, GradNorm, Nash-MTL, FAMO

Key findings:
- **All** evaluated methods suffer from cross-objective interference on at least some models, confirming interference is pervasive and model-dependent.
- CTWA maintained balanced performance: e.g., on Qwen2.5-1.5B-Base, CTWA achieved conciseness of 107.4 vs 308.0 for Lagrangian, and clarity of 0.994 vs 0.903.
- On Qwen2.5-1.5B-IFT: conciseness 193.3 vs 305.3 and clarity 0.981 vs 0.775 compared to Lagrangian.
- On Qwen3-1.7B-Base: CTWA achieved highest accuracy without degradation while maintaining competitive conciseness and clarity.

A crucial finding (Figure 5): pairwise cosine similarity between per-objective gradients is mostly non-negative and converges toward zero, meaning objectives are weakly coupled -- cross-objective interference stems from **covariance misalignment**, not conflicting gradients. This is why gradient-level methods (MGDA, Nash-MTL, etc.) fail to resolve the problem while CTWA, which directly targets covariance, succeeds.

### Is CTWA Objective-Agnostic or Gaming-Aware?

CTWA is **fundamentally objective-agnostic**. It does not inspect the nature of the rewards, does not model reward interactions, and has no gaming-awareness mechanism. It simply monitors the statistical relationship (covariance) between each reward and the training signal. Any verifiable reward function can be plugged in. This is both a strength (generality, plug-and-play) and a limitation (it cannot detect if an objective's reward is being gamed/hacked in the Goodhart's Law sense).

---

## 2. DRW -- Dynamic Reward Weighting (arXiv:2509.11452)

**Authors:** Yining Lu, Zilong Wang, Shiyang Li, Xin Liu, Changlong Yu, Qingyu Yin, Zhan Shi, Zixuan Zhang, and Meng Jiang (Sep 2025, published TACL 2026)

**Same lead author and senior author as CTWA** (Lu & Jiang). DRW is the predecessor/companion work.

### Two Approaches

**Hypervolume-guided weight adaptation:**
```
r_pareto(r, B) = 0.5 + 1.5 * tanh(Delta_HV(r, B))
```
where Delta_HV is the hypervolume contribution of the current checkpoint to the Pareto set buffer B. Meta-reward ranges from -1 to 2, amplifying standard rewards when discovering new Pareto-optimal solutions.

**Gradient-based weight optimization:**
```
w(t) = w(t-1) * exp(eta(t) * I(t) / mu)   (elementwise)
w(t) = w(t) / sum(w(t))                     (normalization)
```
where the influence signal is:
```
I_i(t) = &lt;nabla J_i(theta(t)), sum_k nabla J_k(theta(t))>
```
This measures both cross-objective gradient alignment and individual gradient magnitude.

**Convergence guarantee** (Theorem 5.2): Bounded weight ratio w_i(T)/w_j(T) = O(1), preventing weight collapse/explosion.

### Comparison: CTWA vs DRW

CTWA explicitly references and compares against DRW. Key distinctions:
- **DRW** operates on gradient-level information (requiring per-objective gradient computation) or hypervolume metrics. 
- **CTWA** avoids per-objective gradient computation entirely, operating purely on reward-level covariance statistics, making it computationally cheaper.
- **CTWA** has a cleaner theoretical justification (the covariance law directly explains when objectives improve), while DRW's hypervolume approach is more heuristic.
- Both are compatible with GRPO, REINFORCE, and RLOO.

### DRW Tested On
Math500, MATH algebra, SafeSQL; models including Qwen3-8B, Deepseek-7B, Mistral-7B, Llama3-8B.

---

## 3. MO-GRPO (arXiv:2509.22047)

**Authors:** Yuki Ichihara, Yuu Jinnai, Tetsuro Morimura, Mitsuki Sakamoto, Ryota Mitsuhashi, Eiji Uchibe (Sep 2025, CyberAgent/NAIST)

### Core Mechanism: Per-Objective Normalization

Standard GRPO normalizes **after** summing rewards:
```
A_g = [sum_i R_i(q, o_g) - mean(sum_i R_i)] / std(sum_i R_i)
```

MO-GRPO normalizes **each reward independently before** aggregation:
```
A_g^MO = sum_i [R_i(q, o_g) - mean(R_i)] / std(R_i)
```

**Theoretical guarantees:**
- Theorem 1: In standard GRPO, correlation between individual reward R_i and advantage depends on the ratio of R_i's variance to total variance -- high-variance rewards dominate.
- Theorem 2: In MO-GRPO, when rewards are uncorrelated, `Corr(R_i, A_g^MO) = 1/sqrt(K)` for all i, guaranteeing equal influence regardless of variance.
- Proposition 1: MO-GRPO is affine invariant -- preference ordering unchanged under positive affine transformations of rewards.

### Key Results
- En-Zh machine translation: reduced non-Chinese output from 68.7% (GRPO) to 5.6% (MO-GRPO), dramatically curtailing reward hacking.
- Tested on multi-armed bandits, Mo-Gymnasium control, WMT translation, and AlpacaFarm instruction following.

### Comparison to CTWA
MO-GRPO is simpler (just normalize per-objective before aggregation) but less principled theoretically. It equalizes variance-based influence but does not directly monitor or target covariance. It has no mechanism for detecting when an objective is actually degrading due to negative covariance with the training signal. CTWA's covariance law provides a more fundamental explanation of *why* interference occurs.

---

## 4. Blockwise Advantage Estimation (arXiv:2602.10231)

**Authors:** Kirill Pavlenko, Alexander Golubev, Simon Karasik, Boris Yangel (Feb 2026)

### Core Idea: Token-Level Objective Assignment

Rather than assigning a single scalar advantage to all tokens, BAE partitions completions into K contiguous blocks y = [X_1; X_2; ...; X_K], each with its own objective-specific advantage:

```
L_BAE(theta) = -(1/G) sum_i sum_k (1/|T_k^(i)|) sum_{t in T_k^(i)} min(rho_t^(i) * A_hat_k^(i), clip(rho_t^(i)) * A_hat_k^(i))
```

This applies each objective's advantage **only to the tokens in the corresponding text block**, preventing reward signal coupling across segments.

### Outcome-Conditioned Baseline (OCB)

For later blocks (k > 1), group-mean baselines are miscalibrated because rewards depend on the sampled prefix. OCB stratifies samples by discrete intermediate outcome:

```
b_hat_k^(i) = (1/|G_{o^(i)}|) * sum_{j in G_{o^(i)}} r_k^(j)
```

where G_o = {j : o^(j) = o} groups samples by whether the prefix was correct/incorrect. This is unbiased when `E[r_k | x, X_{&lt;k}] = E[r_k | x, o]`.

### Tasks
- Math reasoning + uncertainty estimation (MATH500, GSM8K, AIME23-25)
- Two-attempt refinement task
- Models: Qwen2.5-7B-Base, Qwen2.5-7B-Instruct, Qwen2.5-3B-Instruct

### Key Distinction from CTWA/DRW/MO-GRPO
BAE operates at a **different level** -- it is about credit assignment within structured generations, not about objective weighting. It assumes objectives have natural segment boundaries in the text (e.g., reasoning block vs. confidence block). It is complementary to weight adaptation methods: one could combine BAE's token-level assignment with CTWA's covariance-driven weighting.

---

## 5. TaRoS -- Target-Robust Reward Signaling (arXiv:2511.19356)

**Authors:** Rui Li, Yuanzhi Liang, Ziqi Ni, Haibing Huang, Chi Zhang, Xuelong Li (Nov 2025 / Mar 2026)
**Domain:** Video generation GRPO

### Saturation Detection via Hoyer Sparsity

```
S_Hoyer(r_j) = [sqrt(G) - ||r_j||_1 / ||r_j||_2] / (sqrt(G) - 1)
```

Low Hoyer sparsity indicates reward score compression (saturation) -- reward values have converged within the group, destroying ranking resolution needed for GRPO.

### Component Utility and Adaptive Weighting

```
g_j(r_j) = h(r_bar_j - tau_j) + beta * [S_Hoyer(r_j) - S_Hoyer(r_{j+1})]
```

Weights are computed via softmax:
```
w_j = exp(g_j) / sum_l exp(g_l)
```

Aggregated reward: `r_tilde_i = sum_j w_j * r_j^i`, then standardized for GRPO.

### Key Distinction
TaRoS is specifically designed for **video generation** where component saturation (Goodhart's Law) is a major problem. It downweights saturated components to preserve effective optimization directions. Unlike CTWA which targets covariance, TaRoS targets ranking resolution / discriminative power of reward components.

---

## The Broader Landscape (Summary)

The multi-objective GRPO weight adaptation space in late 2025 through mid-2026 has become remarkably crowded, with at least five distinct approaches attacking the same problem from different angles:

| Method | Level | Core Signal | Gaming-Aware? | Domain |
|--------|-------|-------------|---------------|--------|
| **CTWA** | Reward weights | Covariance with training signal | No | LLM math reasoning |
| **DRW** | Reward weights / Gradients | Hypervolume or gradient alignment | No | LLM math, SQL |
| **MO-GRPO** | Advantage computation | Per-objective variance normalization | No | LLM translation, instruction |
| **BAE** | Token-level credit | Block-specific advantage | No | LLM math + calibration |
| **TaRoS** | Reward weights | Hoyer sparsity / saturation | Partially (Goodhart) | Video generation |

CTWA is arguably the most theoretically grounded of the group, with the covariance law providing a clean first-principles explanation of cross-objective interference. MO-GRPO is the simplest to implement. BAE addresses a complementary problem (token-level credit assignment). TaRoS is the only one with explicit saturation/gaming awareness (via Hoyer sparsity monitoring). DRW, by the same authors as CTWA, is the earlier work that CTWA supersedes with a cleaner mechanism.

None of these methods are truly gaming-aware in the Goodhart's Law sense (detecting when a reward is being hacked rather than genuinely optimized), though TaRoS's saturation detection is the closest.

Sources:
- [CTWA - Uncovering Cross-Objective Interference in Multi-Objective Alignment](https://arxiv.org/abs/2602.06869)
- [CTWA full paper](https://arxiv.org/html/2602.06869)
- [DRW - Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting](https://arxiv.org/abs/2509.11452)
- [DRW full paper](https://arxiv.org/html/2509.11452)
- [DRW project page](https://yining610.github.io/dynamic-reward-weighting-webpage/)
- [MO-GRPO - Mitigating Reward Hacking of Group Relative Policy Optimization](https://arxiv.org/abs/2509.22047)
- [MO-GRPO full paper](https://arxiv.org/html/2509.22047)
- [MO-GRPO GitHub](https://github.com/CyberAgentAILab/MO-GRPO)
- [Blockwise Advantage Estimation](https://arxiv.org/abs/2602.10231)
- [BAE full paper](https://arxiv.org/html/2602.10231)
- [TaRoS - Rethinking Reward Signals in Video GRPO](https://arxiv.org/abs/2511.19356)
- [TaRoS full paper](https://arxiv.org/html/2511.19356)

agentId: a8eeaa114e17cfb58 (use SendMessage with to: 'a8eeaa114e17cfb58' to continue this agent)
&lt;usage>total_tokens: 32428
tool_uses: 20
duration_ms: 253064&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "2b137b6c-9b36-4411-a56a-ee9a065b87d5",
  "isSidechain": false,
  "promptId": "6d783516-df0e-455a-9cd7-fd412aff8d61",
  "type": "user",
  "uuid": "01f1e8c4-fba5-4245-aa54-011276be0442",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research the paper \"CTWA — Covariance Targeted Weight Adaptation\" (arXiv:2602.06869, Feb 2026, revised May 2026) by Lu & Jiang. \n\nUse WebSearch and WebFetch to find and read this paper. I need to understand:\n1. The exact mechanism: how does covariance between objective rewards and clipped advantages drive weight adaptation?\n2. What environments/tasks was it tested on?\n3. How does it compare to MO-GRPO and DRW (same authors as DRW)?\n4. What are the specific mathematical formulations?\n5. Is it truly objective-agnostic or does it have any gaming-awareness?\n\nAlso search for \"Blockwise Advantage arXiv:2602.10231\" and \"TaRoS component saturation GRPO\" to understand the broader crowded landscape of multi-objective GRPO weight methods.\n\nReport your findings in detail.",
    "agentId": "a8eeaa114e17cfb58",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information on all the papers. Let me compile my detailed findings.\n\n---\n\nHere is my detailed research report on the papers you asked about.\n\n---\n\n## 1. CTWA -- Covariance Targeted Weight Adaptation (arXiv:2602.06869)\n\n**Authors:** Yining Lu & Meng Jiang (Feb 2026, revised May 2026)\n**Title:** \"Uncovering Cross-Objective Interference in Multi-Objective Alignment\"\n\n### The Core Mechanism: Covariance Law\n\nThe paper's central theoretical contribution is the **first-order local covariance law** (Theorem 4.2):\n\n```\nr_m(p_{theta+}) - r_m(p_theta) = eta * E_x[ Cov_{y~p_theta(.|x)}( r_m(x,y), s(x,y) ) ] + O(eta^2)\n```\n\nThis states that objective m improves at first order **if and only if** its reward r_m has positive covariance with the scalarized score s(x,y) across the sampled completions. Even if the overall scalarized return improves, a specific objective can *degrade* if its reward is negatively correlated with the combined training signal. The paper proves this holds even under clipped surrogate objectives (as used in GRPO/PPO) under mild conditions.\n\nThe underlying intuition: policy updates via KL-regularized optimization produce a Gibbs-like reweighting of the policy (Lemma 4.1):\n\n```\np_{theta;x}^+(y) = p_{theta;x}(y) * exp(eta * s(x,y)) / E_{y~p_theta;x}[exp(eta * s(x,y))]\n```\n\nThis upweights completions proportionally to their scalarized score. If objective m's reward is negatively correlated with the scalarized score, the upweighted completions are precisely those that are *bad* for objective m.\n\n### The CTWA Algorithm\n\nCTWA is a **plug-and-play weight adaptation** method that works as follows:\n\n1. **Monitor empirical covariance**: For each objective m, compute `Cov_m(x) = Cov_{k=1..K}(r_m(x, y^(k)), w(x, y^(k); theta))` where w is the policy ratio weight (clipped advantage signal).\n\n2. **Maintain exponential moving average**: `c_bar_m <- (1 - tau) * c_bar_m + tau * c_m`\n\n3. **Compute deficit**: `delta_m = max(0, c*_m - c_bar_m)` where c*_m is a positive covariance target.\n\n4. **Update in log-space** (for numerical stability): `u_m <- u_m + eta_lambda * delta_m; lambda_m = exp(u_m)`\n\nThe key insight is that CTWA does not try to learn optimal weights or balance gradients directly. Instead, it has a single, principled goal: **keep the covariance between each objective's reward and the training signal positive**. When an objective's covariance dips below its target, CTWA increases that objective's weight to restore it.\n\n**Covariance targets** used in experiments: c*_m = [0.15, 0.08, 0.08] for accuracy, conciseness, and clarity respectively. The paper's sensitivity analysis (Figure 4) shows robustness across the range [0.08, 0.20] for the accuracy target, but performance degrades at excessively large targets (0.20+). Negative covariance targets consistently underperform.\n\n### Global Convergence Analysis\n\nBeyond the local law, the paper provides a **Polyak-Lojasiewicz (PL) convergence analysis** (Theorem 6.4):\n\n```\n(1/2) * ||nabla_theta V(x; theta)||^2 >= mu * (V(x; theta*) - V(x; theta))\n```\n\nwhere the PL constant mu depends on:\n```\nmu = (1/2B) * [p_theta(y*|x) / (1 - p_theta(y*|x)) * s(x, y*) * gamma - 2B * sigma_max]\n```\n\nThis reveals three structural sources of interference: (i) insufficient probability mass on optimal trajectories, (ii) weak reward margins in the scalarization, and (iii) gradient cancellation from ill-conditioned Jacobians.\n\n### Environments and Tasks\n\n- **Datasets**: Math500 (Lightman et al., 2024) and MATH algebra subset (Hendrycks et al., 2021)\n- **Objectives**: Accuracy, conciseness (response length), clarity (step-by-step reasoning quality)\n- **Models**: Qwen2.5-1.5B (base + instruction-finetuned), Qwen3-1.7B, SmolLM2-1.7B\n- **Algorithms**: REINFORCE (clipping-free) and GRPO (clipped surrogate)\n\n### Comparisons to Baselines\n\nCTWA was compared against:\n- **Reward-level**: Linear weighting, Lagrangian, Smooth Tchebycheff, PAMA, Dynamic Reward Weighting (DRW)\n- **Gradient-level**: MGDA, GradNorm, Nash-MTL, FAMO\n\nKey findings:\n- **All** evaluated methods suffer from cross-objective interference on at least some models, confirming interference is pervasive and model-dependent.\n- CTWA maintained balanced performance: e.g., on Qwen2.5-1.5B-Base, CTWA achieved conciseness of 107.4 vs 308.0 for Lagrangian, and clarity of 0.994 vs 0.903.\n- On Qwen2.5-1.5B-IFT: conciseness 193.3 vs 305.3 and clarity 0.981 vs 0.775 compared to Lagrangian.\n- On Qwen3-1.7B-Base: CTWA achieved highest accuracy without degradation while maintaining competitive conciseness and clarity.\n\nA crucial finding (Figure 5): pairwise cosine similarity between per-objective gradients is mostly non-negative and converges toward zero, meaning objectives are weakly coupled -- cross-objective interference stems from **covariance misalignment**, not conflicting gradients. This is why gradient-level methods (MGDA, Nash-MTL, etc.) fail to resolve the problem while CTWA, which directly targets covariance, succeeds.\n\n### Is CTWA Objective-Agnostic or Gaming-Aware?\n\nCTWA is **fundamentally objective-agnostic**. It does not inspect the nature of the rewards, does not model reward interactions, and has no gaming-awareness mechanism. It simply monitors the statistical relationship (covariance) between each reward and the training signal. Any verifiable reward function can be plugged in. This is both a strength (generality, plug-and-play) and a limitation (it cannot detect if an objective's reward is being gamed/hacked in the Goodhart's Law sense).\n\n---\n\n## 2. DRW -- Dynamic Reward Weighting (arXiv:2509.11452)\n\n**Authors:** Yining Lu, Zilong Wang, Shiyang Li, Xin Liu, Changlong Yu, Qingyu Yin, Zhan Shi, Zixuan Zhang, and Meng Jiang (Sep 2025, published TACL 2026)\n\n**Same lead author and senior author as CTWA** (Lu & Jiang). DRW is the predecessor/companion work.\n\n### Two Approaches\n\n**Hypervolume-guided weight adaptation:**\n```\nr_pareto(r, B) = 0.5 + 1.5 * tanh(Delta_HV(r, B))\n```\nwhere Delta_HV is the hypervolume contribution of the current checkpoint to the Pareto set buffer B. Meta-reward ranges from -1 to 2, amplifying standard rewards when discovering new Pareto-optimal solutions.\n\n**Gradient-based weight optimization:**\n```\nw(t) = w(t-1) * exp(eta(t) * I(t) / mu)   (elementwise)\nw(t) = w(t) / sum(w(t))                     (normalization)\n```\nwhere the influence signal is:\n```\nI_i(t) = &lt;nabla J_i(theta(t)), sum_k nabla J_k(theta(t))>\n```\nThis measures both cross-objective gradient alignment and individual gradient magnitude.\n\n**Convergence guarantee** (Theorem 5.2): Bounded weight ratio w_i(T)/w_j(T) = O(1), preventing weight collapse/explosion.\n\n### Comparison: CTWA vs DRW\n\nCTWA explicitly references and compares against DRW. Key distinctions:\n- **DRW** operates on gradient-level information (requiring per-objective gradient computation) or hypervolume metrics. \n- **CTWA** avoids per-objective gradient computation entirely, operating purely on reward-level covariance statistics, making it computationally cheaper.\n- **CTWA** has a cleaner theoretical justification (the covariance law directly explains when objectives improve), while DRW's hypervolume approach is more heuristic.\n- Both are compatible with GRPO, REINFORCE, and RLOO.\n\n### DRW Tested On\nMath500, MATH algebra, SafeSQL; models including Qwen3-8B, Deepseek-7B, Mistral-7B, Llama3-8B.\n\n---\n\n## 3. MO-GRPO (arXiv:2509.22047)\n\n**Authors:** Yuki Ichihara, Yuu Jinnai, Tetsuro Morimura, Mitsuki Sakamoto, Ryota Mitsuhashi, Eiji Uchibe (Sep 2025, CyberAgent/NAIST)\n\n### Core Mechanism: Per-Objective Normalization\n\nStandard GRPO normalizes **after** summing rewards:\n```\nA_g = [sum_i R_i(q, o_g) - mean(sum_i R_i)] / std(sum_i R_i)\n```\n\nMO-GRPO normalizes **each reward independently before** aggregation:\n```\nA_g^MO = sum_i [R_i(q, o_g) - mean(R_i)] / std(R_i)\n```\n\n**Theoretical guarantees:**\n- Theorem 1: In standard GRPO, correlation between individual reward R_i and advantage depends on the ratio of R_i's variance to total variance -- high-variance rewards dominate.\n- Theorem 2: In MO-GRPO, when rewards are uncorrelated, `Corr(R_i, A_g^MO) = 1/sqrt(K)` for all i, guaranteeing equal influence regardless of variance.\n- Proposition 1: MO-GRPO is affine invariant -- preference ordering unchanged under positive affine transformations of rewards.\n\n### Key Results\n- En-Zh machine translation: reduced non-Chinese output from 68.7% (GRPO) to 5.6% (MO-GRPO), dramatically curtailing reward hacking.\n- Tested on multi-armed bandits, Mo-Gymnasium control, WMT translation, and AlpacaFarm instruction following.\n\n### Comparison to CTWA\nMO-GRPO is simpler (just normalize per-objective before aggregation) but less principled theoretically. It equalizes variance-based influence but does not directly monitor or target covariance. It has no mechanism for detecting when an objective is actually degrading due to negative covariance with the training signal. CTWA's covariance law provides a more fundamental explanation of *why* interference occurs.\n\n---\n\n## 4. Blockwise Advantage Estimation (arXiv:2602.10231)\n\n**Authors:** Kirill Pavlenko, Alexander Golubev, Simon Karasik, Boris Yangel (Feb 2026)\n\n### Core Idea: Token-Level Objective Assignment\n\nRather than assigning a single scalar advantage to all tokens, BAE partitions completions into K contiguous blocks y = [X_1; X_2; ...; X_K], each with its own objective-specific advantage:\n\n```\nL_BAE(theta) = -(1/G) sum_i sum_k (1/|T_k^(i)|) sum_{t in T_k^(i)} min(rho_t^(i) * A_hat_k^(i), clip(rho_t^(i)) * A_hat_k^(i))\n```\n\nThis applies each objective's advantage **only to the tokens in the corresponding text block**, preventing reward signal coupling across segments.\n\n### Outcome-Conditioned Baseline (OCB)\n\nFor later blocks (k > 1), group-mean baselines are miscalibrated because rewards depend on the sampled prefix. OCB stratifies samples by discrete intermediate outcome:\n\n```\nb_hat_k^(i) = (1/|G_{o^(i)}|) * sum_{j in G_{o^(i)}} r_k^(j)\n```\n\nwhere G_o = {j : o^(j) = o} groups samples by whether the prefix was correct/incorrect. This is unbiased when `E[r_k | x, X_{<k}] = E[r_k | x, o]`.\n\n### Tasks\n- Math reasoning + uncertainty estimation (MATH500, GSM8K, AIME23-25)\n- Two-attempt refinement task\n- Models: Qwen2.5-7B-Base, Qwen2.5-7B-Instruct, Qwen2.5-3B-Instruct\n\n### Key Distinction from CTWA/DRW/MO-GRPO\nBAE operates at a **different level** -- it is about credit assignment within structured generations, not about objective weighting. It assumes objectives have natural segment boundaries in the text (e.g., reasoning block vs. confidence block). It is complementary to weight adaptation methods: one could combine BAE's token-level assignment with CTWA's covariance-driven weighting.\n\n---\n\n## 5. TaRoS -- Target-Robust Reward Signaling (arXiv:2511.19356)\n\n**Authors:** Rui Li, Yuanzhi Liang, Ziqi Ni, Haibing Huang, Chi Zhang, Xuelong Li (Nov 2025 / Mar 2026)\n**Domain:** Video generation GRPO\n\n### Saturation Detection via Hoyer Sparsity\n\n```\nS_Hoyer(r_j) = [sqrt(G) - ||r_j||_1 / ||r_j||_2] / (sqrt(G) - 1)\n```\n\nLow Hoyer sparsity indicates reward score compression (saturation) -- reward values have converged within the group, destroying ranking resolution needed for GRPO.\n\n### Component Utility and Adaptive Weighting\n\n```\ng_j(r_j) = h(r_bar_j - tau_j) + beta * [S_Hoyer(r_j) - S_Hoyer(r_{j+1})]\n```\n\nWeights are computed via softmax:\n```\nw_j = exp(g_j) / sum_l exp(g_l)\n```\n\nAggregated reward: `r_tilde_i = sum_j w_j * r_j^i`, then standardized for GRPO.\n\n### Key Distinction\nTaRoS is specifically designed for **video generation** where component saturation (Goodhart's Law) is a major problem. It downweights saturated components to preserve effective optimization directions. Unlike CTWA which targets covariance, TaRoS targets ranking resolution / discriminative power of reward components.\n\n---\n\n## The Broader Landscape (Summary)\n\nThe multi-objective GRPO weight adaptation space in late 2025 through mid-2026 has become remarkably crowded, with at least five distinct approaches attacking the same problem from different angles:\n\n| Method | Level | Core Signal | Gaming-Aware? | Domain |\n|--------|-------|-------------|---------------|--------|\n| **CTWA** | Reward weights | Covariance with training signal | No | LLM math reasoning |\n| **DRW** | Reward weights / Gradients | Hypervolume or gradient alignment | No | LLM math, SQL |\n| **MO-GRPO** | Advantage computation | Per-objective variance normalization | No | LLM translation, instruction |\n| **BAE** | Token-level credit | Block-specific advantage | No | LLM math + calibration |\n| **TaRoS** | Reward weights | Hoyer sparsity / saturation | Partially (Goodhart) | Video generation |\n\nCTWA is arguably the most theoretically grounded of the group, with the covariance law providing a clean first-principles explanation of cross-objective interference. MO-GRPO is the simplest to implement. BAE addresses a complementary problem (token-level credit assignment). TaRoS is the only one with explicit saturation/gaming awareness (via Hoyer sparsity monitoring). DRW, by the same authors as CTWA, is the earlier work that CTWA supersedes with a cleaner mechanism.\n\nNone of these methods are truly gaming-aware in the Goodhart's Law sense (detecting when a reward is being hacked rather than genuinely optimized), though TaRoS's saturation detection is the closest.\n\nSources:\n- [CTWA - Uncovering Cross-Objective Interference in Multi-Objective Alignment](https://arxiv.org/abs/2602.06869)\n- [CTWA full paper](https://arxiv.org/html/2602.06869)\n- [DRW - Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting](https://arxiv.org/abs/2509.11452)\n- [DRW full paper](https://arxiv.org/html/2509.11452)\n- [DRW project page](https://yining610.github.io/dynamic-reward-weighting-webpage/)\n- [MO-GRPO - Mitigating Reward Hacking of Group Relative Policy Optimization](https://arxiv.org/abs/2509.22047)\n- [MO-GRPO full paper](https://arxiv.org/html/2509.22047)\n- [MO-GRPO GitHub](https://github.com/CyberAgentAILab/MO-GRPO)\n- [Blockwise Advantage Estimation](https://arxiv.org/abs/2602.10231)\n- [BAE full paper](https://arxiv.org/html/2602.10231)\n- [TaRoS - Rethinking Reward Signals in Video GRPO](https://arxiv.org/abs/2511.19356)\n- [TaRoS full paper](https://arxiv.org/html/2511.19356)"
      }
    ],
    "totalDurationMs": 253064,
    "totalTokens": 32428,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1055,
      "cache_read_input_tokens": 26756,
      "output_tokens": 4616,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1055
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4616,
          "cache_read_input_tokens": 26756,
          "cache_creation_input_tokens": 1055,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1055,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 20
    }
  },
  "sourceToolAssistantUUID": "2b137b6c-9b36-4411-a56a-ee9a065b87d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"MAJOR NARRATIVE RESTRUCTURING: Reframed entire proposal a…",
  "leafUuid": "01f1e8c4-fba5-4245-aa54-011276be0442",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gaming-resistant reward composition for autoformalization",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51"
}
```

---

### Tool result

_source line 21 · 2026-05-27T22:12:13.186Z_

<details><summary>↩ Tool result · `toolu_01Wb8yVNqhGBKqD5P7Z33hVp`</summary>

```text
I now have comprehensive research results across all four topics. Here is my detailed report.

---

## Research Report: Theoretical Foundations for the GRS Framework

### 1. Sample Complexity Bounds for Rank Correlation Estimation

**Core result you can cite:** Both Spearman's rho and Kendall's tau converge at the standard sqrt(n) rate, yielding confidence interval widths of O(1/sqrt(n)).

**Spearman's rho -- Fisher z-transform approach (Bonett & Wright, 2000; Psychometrika 65, 23-28):**
- Apply the Fisher transformation z = arctanh(rho_s). The transformed statistic is approximately normal with variance approximately (1 + rho^2/2) / (n - 3).
- A 95% CI for z has half-width 1.96 / sqrt(n - 3), which back-transforms to a CI for rho_s.
- Concrete example from the `statpsych` R package: to achieve a CI width of 0.25 at 95% confidence with a planning value of rho = 0.362, you need n = 200.
- The Bonett-Wright variance (1 + rho^2/2)/(n-3) is more accurate than the naive 1/(n-3) and yields a two-stage sample size formula that has been validated via simulation.

**Kendall's tau -- U-statistic approach (Hoeffding, 1948):**
- Kendall's tau is a degree-2 U-statistic with kernel h((x1,y1),(x2,y2)) = sgn((x2-x1)(y2-y1)).
- Under independence (null): Var(tau_a) = 2(2n+5) / [9n(n-1)], which is O(1/n).
- Under the general alternative (Pohle, Wermuth & Weiss, arXiv:2512.14609; also the "Studentising Kendall's Tau" paper arXiv:2307.10973): The asymptotic variance is Var(tau_hat) = (1 - tau^2) / N (for the generalized tau_kappa), with a finite-sample corrected version using c(1 - tau^2)/(N-2) where c = 0.4456.
- The Hoeffding decomposition gives: sqrt(n)(tau_hat - tau) -> N(0, sigma^2) where sigma^2 = 4 * sigma_1^2, and sigma_1^2 = Var(E[h(X1,X2)|X1]).

**Spearman's rho under dependence (Puth et al., PLOS ONE 2015, PMC4701424):**
- Asymptotic normality holds for variables with finite support irrespective of dependence (not just under independence).
- The asymptotic variance has the form rho_dot^T * Sigma * rho_dot where rho_dot is the gradient of the population correlation with respect to cell probabilities.
- Simulation shows this asymptotic variance performs as well as bootstrap for n >= 400.
- For n >= 100, the normal approximation is already quite good.

**Formal claim you can make:** "Given n paired observations, the achievable 95% CI width for Spearman's rho is approximately 2 * 1.96 * sqrt((1 + rho^2/2)/(n-3)), which is O(n^{-1/2}). For Kendall's tau, the CI width is approximately 2 * 1.96 * sqrt((1 - tau^2)/n), also O(n^{-1/2}). Both rates are optimal in the minimax sense for U-statistics of bounded kernels (Hoeffding, 1963)."

**Concentration inequalities (Hoeffding, 1963; recent extensions):**
- For U-statistics with bounded kernels, P(|U_n - E[U_n]| > t) <= 2 exp(-2n t^2 / (b-a)^2), giving exponential concentration. Since Kendall's kernel is bounded in [-1, 1], this directly applies.
- More refined Bernstein-type bounds exist that incorporate the variance (Arcones, 1995; recent improvements in arXiv:1712.06160).

---

### 2. Correlated Proxies Framework (arXiv:2403.03185, Laidlaw, Singhal & Dragan; ICLR 2025 Spotlight)

**Definition 4.1 -- r-Correlated Proxy Reward:**
A proxy reward R_tilde has correlation r > 0 with true reward R under base policy pi_base:

E_{mu_{pi_base}}[ ((R_tilde(s,a) - J(pi_base, R_tilde)) / sigma_{R_tilde}) * ((R(s,a) - J(pi_base, R)) / sigma_R) ] = r

where sigma^2 are variances under the base policy's occupancy measure mu_{pi_base}.

**Definition 4.2 -- Hackable Proxy Reward:**
Reward hacking occurs when an optimal policy pi for proxy R_tilde achieves lower true reward than the base policy: J(pi, R) < J(pi_base, R).

**Theorem 5.1 (Main Bound):**
For an r-correlated proxy where mu_pi << mu_{pi_base}:

[J(pi, R) - J(pi_base, R)] / sigma_R >= (1/r) * [ (J(pi, R_tilde) - J(pi_base, R_tilde)) / sigma_{R_tilde} - sqrt((1 - r^2) * chi^2(mu_pi || mu_{pi_base})) ]

where chi^2(mu_pi || mu_{pi_base}) = E_{mu_pi}[mu_pi(s,a)/mu_{pi_base}(s,a) - 1] is the chi-squared divergence between occupancy measures.

**Regularized objective (Equation 5):**
maximize J(pi, R_tilde) - lambda * sqrt(chi^2(mu_pi || mu_{pi_base}))

where lambda = sigma_{R_tilde} * sqrt(1 - r^2). Key insight: as correlation r -> 1, lambda -> 0 (less regularization needed); as r -> 0, lambda -> sigma_{R_tilde} (maximum regularization).

**Extension -- Robust Optimization (arXiv:2604.12086):**
This follow-up paper reformulates the problem as max-min optimization over all r-correlated reward functions, yielding worst-case guarantees. Theorem 2 gives sample complexity: discriminator error achieves O(n^{-1/4}) convergence, and the overall algorithm converges at O(1/T + 1/N + n^{-1/4}).

**Formal connection to GRS you can make:**
GRS directly measures the quantity r in the Correlated Proxies framework. Specifically:
- The Correlated Proxies framework defines reward hacking in terms of the correlation r between proxy and true rewards under a reference policy's distribution.
- GRS, as a rank correlation between proxy-reward rankings and true-quality rankings, is an empirical estimator of a monotone transformation of this same r.
- Theorem 5.1 shows that the safe optimization region scales with r: higher r permits more aggressive optimization with less regularization (lambda = sigma * sqrt(1-r^2)).
- Therefore, GRS provides a direct empirical signal for the regularization strength lambda needed in ORPO: a low GRS (low r) demands strong regularization, while a high GRS permits more optimization.
- The correlation breakdown under optimization that the Correlated Proxies framework formalizes is exactly what GRS is designed to detect -- when optimization pressure causes the rank correlation between proxy and true rewards to deteriorate.

---

### 3. Conditions for Detection Superiority: Rank Correlation (GRS) vs. Panel-Based (Exploitation Rate)

**Panel-based detection (exploitation rate) -- from arXiv:2605.12474 (Reward Hacking in Rubric-Based RL):**
- ExploitationRate(t) = P_hat_w(J^(t)=1 | N^(t)=1): the fraction of newly credited criteria that a reference panel unanimously rejects.
- Uses 3 frontier judges (GPT-5.4, Gemini 3 Pro, Claude Opus 4.6) with unanimous consensus.
- Achieves ~80% macro-F1 against human expert labels.
- Conservative (lower bound): only flags cases where ALL panel judges disagree.
- Limitations: "the reference remains model-based and we do not rule out shared evaluator failure modes."
- Per-instance classification: requires running 3 expensive frontier models on every response.

**When GRS (rank correlation) outperforms panel-based detection:**

(a) **Robustness to contamination / influence function argument:**
- Croux & Dehon (2010, Statistical Methods & Applications) prove that both Spearman's rho and Kendall's tau have bounded, smooth influence functions, unlike Pearson's r which is unbounded.
- Gross-error sensitivity is finite for both rank correlations, meaning a single corrupted observation has bounded impact on the estimate.
- Under the contaminated normal model (bivariate normal with epsilon-fraction outliers), Kendall's tau has the smallest MSE when contamination is 5-10% (Xu et al., Signal Processing 2013; arXiv:1011.2009). Spearman's rho and Kendall's tau behave "strikingly differently" under contamination.
- Formal claim: "Under an epsilon-contaminated model where a fraction epsilon of proxy-reward pairs are adversarially corrupted (as occurs when a policy discovers exploits), rank correlation estimators maintain bounded bias while the panel's per-instance classification is vulnerable to shared failure modes across judges."

(b) **Statistical power under heavy-tailed contamination:**
- At the bivariate normal, the asymptotic relative efficiency of both Kendall and Spearman relative to Pearson is 9/pi^2 ~ 0.912 (a small efficiency loss).
- Under contaminated normal distributions, even 1% contamination reverses this: rank-based methods become MORE efficient than parametric methods.
- With 5-10% contamination (realistic for reward hacking), rank correlations can have ARE >> 1 relative to parametric alternatives.
- The Wilcoxon/rank-based test literature shows: parametric tests lose power because outliers inflate variance estimates, while rank-based tests cap influence at the maximum rank.

(c) **Sample complexity advantage:**
- Panel detection requires K expensive model calls per instance (K=3 frontier models in the rubric-hacking paper). For n instances, cost is O(K*n).
- GRS requires only the proxy scores and true quality scores (or a gold-standard reference), then computes rank correlation in O(n log n) time.
- For the same statistical power, rank correlation needs only n ~ 4 * (1.96/w)^2 * (1 + rho^2/2) samples (from Bonett-Wright), where w is the desired CI width. E.g., for w=0.1 at rho=0.5, n ~ 600.

(d) **When panel detection is superior:**
- When you need per-instance detection (is THIS specific response hacked?), the panel can classify individual outputs while GRS provides only an aggregate population-level signal.
- When the exploits are subtle enough that rankings are preserved but absolute quality drops (a narrow failure mode).
- When shared evaluator failure modes are absent (strong judge diversity).

**Formal claim you can make:** "Under a contamination model where a fraction epsilon of policy outputs exploit the proxy reward, GRS (rank correlation) provides a population-level detection signal with bounded influence function (gross-error sensitivity finite) and O(n^{-1/2}) convergence to the true correlation. By contrast, panel-based detection achieves per-instance classification but requires O(K) frontier model calls per instance and is vulnerable to correlated judge failures. GRS is statistically more powerful when: (i) the contamination fraction is moderate (epsilon > 0.05), (ii) the goal is population-level monitoring rather than per-instance flagging, and (iii) evaluator cost or judge diversity is constrained."

---

### 4. Formal Results on Sample Complexity for Nonparametric Testing and Finite-Sample Bounds

**Kendall's tau -- finite sample bounds:**
- Derumigny & Fermanian (2019, Dependence Modeling 7(1):292-321) prove non-asymptotic pointwise and uniform bounds for conditional Kendall's tau estimators with explicit constants that hold with high probability.
- For unconditional Kendall's tau: via Hoeffding's inequality for U-statistics (1963), since the kernel is bounded in [-1,1]:

P(|tau_hat - tau| > t) <= 2 exp(-n t^2 / 2)

This gives: with probability >= 1 - delta, |tau_hat - tau| <= sqrt(2 log(2/delta) / n).

- More refined: via the Bernstein-type bound for U-statistics (Arcones 1995), incorporating variance:

P(|tau_hat - tau| > t) <= 2 exp(-n t^2 / (2 sigma^2 + 2t/3))

where sigma^2 is the asymptotic variance.

**Spearman's rho -- finite sample:**
- Via the Fisher z-transform: z = arctanh(rho_s) is approximately N(arctanh(rho), (1+rho^2/2)/(n-3)).
- For n >= 100, the normal approximation is reliable (Puth et al., 2015).
- For n >= 400, the asymptotic variance formula matches bootstrap performance.

**Formal claims for the paper:**

Claim 1 (Sample complexity for GRS estimation): "To estimate GRS (Kendall's tau) within precision epsilon with probability >= 1-delta, it suffices to have n >= 2 log(2/delta) / epsilon^2 evaluation pairs. For epsilon = 0.05 and delta = 0.05, this gives n >= 2954."

Claim 2 (Concentration): "By Hoeffding's inequality for degree-2 U-statistics with kernel bounded in [-1,1], the GRS estimator concentrates exponentially: P(|GRS_hat - GRS| > epsilon) <= 2 exp(-n epsilon^2 / 2)."

Claim 3 (Asymptotic normality): "Under mild regularity conditions (Hoeffding 1948), sqrt(n)(GRS_hat - GRS) -> N(0, 4 sigma_1^2), where sigma_1^2 = Var(E[sgn((X2-X1)(Y2-Y1)) | X1, Y1]). A consistent plug-in estimator of sigma_1^2 enables valid confidence intervals."

Claim 4 (Connection to Correlated Proxies regularization): "Let GRS = tau estimate the proxy-true correlation parameter r in the Correlated Proxies framework (Laidlaw et al., 2025). Then the safe regularization strength is lambda = sigma_{R_tilde} * sqrt(1 - r^2). A GRS confidence interval [tau_L, tau_U] translates to a regularization interval [sigma * sqrt(1 - tau_U^2), sigma * sqrt(1 - tau_L^2)], providing data-driven regularization calibration."

---

### Key References

- Bonett & Wright (2000). Sample size requirements for estimating Pearson, Kendall and Spearman correlations. *Psychometrika* 65, 23-28. [https://link.springer.com/article/10.1007/BF02294183](https://link.springer.com/article/10.1007/BF02294183)
- Laidlaw, Singhal & Dragan (2025). Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking. *ICLR 2025 Spotlight*. [https://arxiv.org/abs/2403.03185](https://arxiv.org/abs/2403.03185)
- Robust Optimization for Mitigating Reward Hacking with Correlated Proxies (2025). [https://arxiv.org/html/2604.12086](https://arxiv.org/html/2604.12086)
- Puth, Neuhauser & Ruxton (2015). Asymptotic Properties of Spearman's Rank Correlation for Variables with Finite Support. *PLOS ONE*. [https://pmc.ncbi.nlm.nih.gov/articles/PMC4701424/](https://pmc.ncbi.nlm.nih.gov/articles/PMC4701424/)
- Pohle, Wermuth & Weiss (2025). Asymptotic Inference for Rank Correlations. [https://arxiv.org/pdf/2512.14609](https://arxiv.org/pdf/2512.14609)
- Croux & Dehon (2010). Influence functions of the Spearman and Kendall correlation measures. *Statistical Methods & Applications* 19, 497-515. [https://link.springer.com/article/10.1007/s10260-010-0142-z](https://link.springer.com/article/10.1007/s10260-010-0142-z)
- Xu et al. (2013). A comparative analysis of Spearman's rho and Kendall's tau in normal and contaminated normal models. *Signal Processing* 93(1), 261-276. [https://arxiv.org/abs/1011.2009](https://arxiv.org/abs/1011.2009)
- Derumigny & Fermanian (2019). On kernel-based estimation of conditional Kendall's tau: finite-distance bounds and asymptotic behavior. *Dependence Modeling* 7(1):292-321. [https://arxiv.org/pdf/1810.06234](https://arxiv.org/pdf/1810.06234)
- Studentising Kendall's Tau (2023). [https://arxiv.org/html/2307.10973](https://arxiv.org/html/2307.10973)
- Hoeffding (1948). A class of statistics with asymptotically normal distribution. *Annals of Mathematical Statistics* 19, 293-325.
- Reward Hacking in Rubric-Based RL (2025). [https://arxiv.org/html/2605.12474](https://arxiv.org/html/2605.12474)
- Adversarial Reward Auditing (2025). [https://arxiv.org/html/2602.01750v1](https://arxiv.org/html/2602.01750v1)
- Weng (2024). Reward Hacking in Reinforcement Learning. [https://lilianweng.github.io/posts/2024-11-28-reward-hacking/](https://lilianweng.github.io/posts/2024-11-28-reward-hacking/)
- How to Evaluate Reward Models for RLHF (2024). [https://arxiv.org/html/2410.14872v1](https://arxiv.org/html/2410.14872v1)

agentId: ae21ee77813933732 (use SendMessage with to: 'ae21ee77813933732' to continue this agent)
&lt;usage>total_tokens: 49224
tool_uses: 45
duration_ms: 308418&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58f15955-7643-4d60-942f-dbaf48e86e7e",
  "isSidechain": false,
  "promptId": "6d783516-df0e-455a-9cd7-fd412aff8d61",
  "type": "user",
  "uuid": "43031182-b831-44c9-8077-c5fd8135cd8a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research several theoretical topics to deepen the GRS (Gaming Resistance Score) framework's novelty:\n\n1. **Sample complexity bounds for rank correlation estimation**: Search for papers on \"sample complexity Spearman correlation\", \"confidence interval width rank correlation\", \"minimax estimation rank correlation\". I need to know: given n samples, what's the achievable CI width for Spearman/Kendall correlation? Are there established results I can build on?\n\n2. **Correlated Proxies framework (arXiv:2403.03185)**: Search for and read this paper. I need to understand:\n   - The exact formalization of reward hacking via correlation breakdown\n   - The χ² regularization approach\n   - Can GRS be formally connected to this framework? (e.g., GRS measures the proxy-true correlation that Correlated Proxies formalizes)\n\n3. **Conditions for detection superiority**: Search for \"comparison rank correlation vs panel evaluation\", \"statistical power rank correlation contamination model\". When does a rank-correlation-based detector (GRS) outperform a panel-based detector (exploitation-rate)?\n\n4. Search for \"sample complexity nonparametric testing\" and \"finite sample bounds Kendall tau\" for formal results.\n\nReport your findings in detail - I need enough to write specific theoretical claims.",
    "agentId": "ae21ee77813933732",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive research results across all four topics. Here is my detailed report.\n\n---\n\n## Research Report: Theoretical Foundations for the GRS Framework\n\n### 1. Sample Complexity Bounds for Rank Correlation Estimation\n\n**Core result you can cite:** Both Spearman's rho and Kendall's tau converge at the standard sqrt(n) rate, yielding confidence interval widths of O(1/sqrt(n)).\n\n**Spearman's rho -- Fisher z-transform approach (Bonett & Wright, 2000; Psychometrika 65, 23-28):**\n- Apply the Fisher transformation z = arctanh(rho_s). The transformed statistic is approximately normal with variance approximately (1 + rho^2/2) / (n - 3).\n- A 95% CI for z has half-width 1.96 / sqrt(n - 3), which back-transforms to a CI for rho_s.\n- Concrete example from the `statpsych` R package: to achieve a CI width of 0.25 at 95% confidence with a planning value of rho = 0.362, you need n = 200.\n- The Bonett-Wright variance (1 + rho^2/2)/(n-3) is more accurate than the naive 1/(n-3) and yields a two-stage sample size formula that has been validated via simulation.\n\n**Kendall's tau -- U-statistic approach (Hoeffding, 1948):**\n- Kendall's tau is a degree-2 U-statistic with kernel h((x1,y1),(x2,y2)) = sgn((x2-x1)(y2-y1)).\n- Under independence (null): Var(tau_a) = 2(2n+5) / [9n(n-1)], which is O(1/n).\n- Under the general alternative (Pohle, Wermuth & Weiss, arXiv:2512.14609; also the \"Studentising Kendall's Tau\" paper arXiv:2307.10973): The asymptotic variance is Var(tau_hat) = (1 - tau^2) / N (for the generalized tau_kappa), with a finite-sample corrected version using c(1 - tau^2)/(N-2) where c = 0.4456.\n- The Hoeffding decomposition gives: sqrt(n)(tau_hat - tau) -> N(0, sigma^2) where sigma^2 = 4 * sigma_1^2, and sigma_1^2 = Var(E[h(X1,X2)|X1]).\n\n**Spearman's rho under dependence (Puth et al., PLOS ONE 2015, PMC4701424):**\n- Asymptotic normality holds for variables with finite support irrespective of dependence (not just under independence).\n- The asymptotic variance has the form rho_dot^T * Sigma * rho_dot where rho_dot is the gradient of the population correlation with respect to cell probabilities.\n- Simulation shows this asymptotic variance performs as well as bootstrap for n >= 400.\n- For n >= 100, the normal approximation is already quite good.\n\n**Formal claim you can make:** \"Given n paired observations, the achievable 95% CI width for Spearman's rho is approximately 2 * 1.96 * sqrt((1 + rho^2/2)/(n-3)), which is O(n^{-1/2}). For Kendall's tau, the CI width is approximately 2 * 1.96 * sqrt((1 - tau^2)/n), also O(n^{-1/2}). Both rates are optimal in the minimax sense for U-statistics of bounded kernels (Hoeffding, 1963).\"\n\n**Concentration inequalities (Hoeffding, 1963; recent extensions):**\n- For U-statistics with bounded kernels, P(|U_n - E[U_n]| > t) <= 2 exp(-2n t^2 / (b-a)^2), giving exponential concentration. Since Kendall's kernel is bounded in [-1, 1], this directly applies.\n- More refined Bernstein-type bounds exist that incorporate the variance (Arcones, 1995; recent improvements in arXiv:1712.06160).\n\n---\n\n### 2. Correlated Proxies Framework (arXiv:2403.03185, Laidlaw, Singhal & Dragan; ICLR 2025 Spotlight)\n\n**Definition 4.1 -- r-Correlated Proxy Reward:**\nA proxy reward R_tilde has correlation r > 0 with true reward R under base policy pi_base:\n\nE_{mu_{pi_base}}[ ((R_tilde(s,a) - J(pi_base, R_tilde)) / sigma_{R_tilde}) * ((R(s,a) - J(pi_base, R)) / sigma_R) ] = r\n\nwhere sigma^2 are variances under the base policy's occupancy measure mu_{pi_base}.\n\n**Definition 4.2 -- Hackable Proxy Reward:**\nReward hacking occurs when an optimal policy pi for proxy R_tilde achieves lower true reward than the base policy: J(pi, R) < J(pi_base, R).\n\n**Theorem 5.1 (Main Bound):**\nFor an r-correlated proxy where mu_pi << mu_{pi_base}:\n\n[J(pi, R) - J(pi_base, R)] / sigma_R >= (1/r) * [ (J(pi, R_tilde) - J(pi_base, R_tilde)) / sigma_{R_tilde} - sqrt((1 - r^2) * chi^2(mu_pi || mu_{pi_base})) ]\n\nwhere chi^2(mu_pi || mu_{pi_base}) = E_{mu_pi}[mu_pi(s,a)/mu_{pi_base}(s,a) - 1] is the chi-squared divergence between occupancy measures.\n\n**Regularized objective (Equation 5):**\nmaximize J(pi, R_tilde) - lambda * sqrt(chi^2(mu_pi || mu_{pi_base}))\n\nwhere lambda = sigma_{R_tilde} * sqrt(1 - r^2). Key insight: as correlation r -> 1, lambda -> 0 (less regularization needed); as r -> 0, lambda -> sigma_{R_tilde} (maximum regularization).\n\n**Extension -- Robust Optimization (arXiv:2604.12086):**\nThis follow-up paper reformulates the problem as max-min optimization over all r-correlated reward functions, yielding worst-case guarantees. Theorem 2 gives sample complexity: discriminator error achieves O(n^{-1/4}) convergence, and the overall algorithm converges at O(1/T + 1/N + n^{-1/4}).\n\n**Formal connection to GRS you can make:**\nGRS directly measures the quantity r in the Correlated Proxies framework. Specifically:\n- The Correlated Proxies framework defines reward hacking in terms of the correlation r between proxy and true rewards under a reference policy's distribution.\n- GRS, as a rank correlation between proxy-reward rankings and true-quality rankings, is an empirical estimator of a monotone transformation of this same r.\n- Theorem 5.1 shows that the safe optimization region scales with r: higher r permits more aggressive optimization with less regularization (lambda = sigma * sqrt(1-r^2)).\n- Therefore, GRS provides a direct empirical signal for the regularization strength lambda needed in ORPO: a low GRS (low r) demands strong regularization, while a high GRS permits more optimization.\n- The correlation breakdown under optimization that the Correlated Proxies framework formalizes is exactly what GRS is designed to detect -- when optimization pressure causes the rank correlation between proxy and true rewards to deteriorate.\n\n---\n\n### 3. Conditions for Detection Superiority: Rank Correlation (GRS) vs. Panel-Based (Exploitation Rate)\n\n**Panel-based detection (exploitation rate) -- from arXiv:2605.12474 (Reward Hacking in Rubric-Based RL):**\n- ExploitationRate(t) = P_hat_w(J^(t)=1 | N^(t)=1): the fraction of newly credited criteria that a reference panel unanimously rejects.\n- Uses 3 frontier judges (GPT-5.4, Gemini 3 Pro, Claude Opus 4.6) with unanimous consensus.\n- Achieves ~80% macro-F1 against human expert labels.\n- Conservative (lower bound): only flags cases where ALL panel judges disagree.\n- Limitations: \"the reference remains model-based and we do not rule out shared evaluator failure modes.\"\n- Per-instance classification: requires running 3 expensive frontier models on every response.\n\n**When GRS (rank correlation) outperforms panel-based detection:**\n\n(a) **Robustness to contamination / influence function argument:**\n- Croux & Dehon (2010, Statistical Methods & Applications) prove that both Spearman's rho and Kendall's tau have bounded, smooth influence functions, unlike Pearson's r which is unbounded.\n- Gross-error sensitivity is finite for both rank correlations, meaning a single corrupted observation has bounded impact on the estimate.\n- Under the contaminated normal model (bivariate normal with epsilon-fraction outliers), Kendall's tau has the smallest MSE when contamination is 5-10% (Xu et al., Signal Processing 2013; arXiv:1011.2009). Spearman's rho and Kendall's tau behave \"strikingly differently\" under contamination.\n- Formal claim: \"Under an epsilon-contaminated model where a fraction epsilon of proxy-reward pairs are adversarially corrupted (as occurs when a policy discovers exploits), rank correlation estimators maintain bounded bias while the panel's per-instance classification is vulnerable to shared failure modes across judges.\"\n\n(b) **Statistical power under heavy-tailed contamination:**\n- At the bivariate normal, the asymptotic relative efficiency of both Kendall and Spearman relative to Pearson is 9/pi^2 ~ 0.912 (a small efficiency loss).\n- Under contaminated normal distributions, even 1% contamination reverses this: rank-based methods become MORE efficient than parametric methods.\n- With 5-10% contamination (realistic for reward hacking), rank correlations can have ARE >> 1 relative to parametric alternatives.\n- The Wilcoxon/rank-based test literature shows: parametric tests lose power because outliers inflate variance estimates, while rank-based tests cap influence at the maximum rank.\n\n(c) **Sample complexity advantage:**\n- Panel detection requires K expensive model calls per instance (K=3 frontier models in the rubric-hacking paper). For n instances, cost is O(K*n).\n- GRS requires only the proxy scores and true quality scores (or a gold-standard reference), then computes rank correlation in O(n log n) time.\n- For the same statistical power, rank correlation needs only n ~ 4 * (1.96/w)^2 * (1 + rho^2/2) samples (from Bonett-Wright), where w is the desired CI width. E.g., for w=0.1 at rho=0.5, n ~ 600.\n\n(d) **When panel detection is superior:**\n- When you need per-instance detection (is THIS specific response hacked?), the panel can classify individual outputs while GRS provides only an aggregate population-level signal.\n- When the exploits are subtle enough that rankings are preserved but absolute quality drops (a narrow failure mode).\n- When shared evaluator failure modes are absent (strong judge diversity).\n\n**Formal claim you can make:** \"Under a contamination model where a fraction epsilon of policy outputs exploit the proxy reward, GRS (rank correlation) provides a population-level detection signal with bounded influence function (gross-error sensitivity finite) and O(n^{-1/2}) convergence to the true correlation. By contrast, panel-based detection achieves per-instance classification but requires O(K) frontier model calls per instance and is vulnerable to correlated judge failures. GRS is statistically more powerful when: (i) the contamination fraction is moderate (epsilon > 0.05), (ii) the goal is population-level monitoring rather than per-instance flagging, and (iii) evaluator cost or judge diversity is constrained.\"\n\n---\n\n### 4. Formal Results on Sample Complexity for Nonparametric Testing and Finite-Sample Bounds\n\n**Kendall's tau -- finite sample bounds:**\n- Derumigny & Fermanian (2019, Dependence Modeling 7(1):292-321) prove non-asymptotic pointwise and uniform bounds for conditional Kendall's tau estimators with explicit constants that hold with high probability.\n- For unconditional Kendall's tau: via Hoeffding's inequality for U-statistics (1963), since the kernel is bounded in [-1,1]:\n\nP(|tau_hat - tau| > t) <= 2 exp(-n t^2 / 2)\n\nThis gives: with probability >= 1 - delta, |tau_hat - tau| <= sqrt(2 log(2/delta) / n).\n\n- More refined: via the Bernstein-type bound for U-statistics (Arcones 1995), incorporating variance:\n\nP(|tau_hat - tau| > t) <= 2 exp(-n t^2 / (2 sigma^2 + 2t/3))\n\nwhere sigma^2 is the asymptotic variance.\n\n**Spearman's rho -- finite sample:**\n- Via the Fisher z-transform: z = arctanh(rho_s) is approximately N(arctanh(rho), (1+rho^2/2)/(n-3)).\n- For n >= 100, the normal approximation is reliable (Puth et al., 2015).\n- For n >= 400, the asymptotic variance formula matches bootstrap performance.\n\n**Formal claims for the paper:**\n\nClaim 1 (Sample complexity for GRS estimation): \"To estimate GRS (Kendall's tau) within precision epsilon with probability >= 1-delta, it suffices to have n >= 2 log(2/delta) / epsilon^2 evaluation pairs. For epsilon = 0.05 and delta = 0.05, this gives n >= 2954.\"\n\nClaim 2 (Concentration): \"By Hoeffding's inequality for degree-2 U-statistics with kernel bounded in [-1,1], the GRS estimator concentrates exponentially: P(|GRS_hat - GRS| > epsilon) <= 2 exp(-n epsilon^2 / 2).\"\n\nClaim 3 (Asymptotic normality): \"Under mild regularity conditions (Hoeffding 1948), sqrt(n)(GRS_hat - GRS) -> N(0, 4 sigma_1^2), where sigma_1^2 = Var(E[sgn((X2-X1)(Y2-Y1)) | X1, Y1]). A consistent plug-in estimator of sigma_1^2 enables valid confidence intervals.\"\n\nClaim 4 (Connection to Correlated Proxies regularization): \"Let GRS = tau estimate the proxy-true correlation parameter r in the Correlated Proxies framework (Laidlaw et al., 2025). Then the safe regularization strength is lambda = sigma_{R_tilde} * sqrt(1 - r^2). A GRS confidence interval [tau_L, tau_U] translates to a regularization interval [sigma * sqrt(1 - tau_U^2), sigma * sqrt(1 - tau_L^2)], providing data-driven regularization calibration.\"\n\n---\n\n### Key References\n\n- Bonett & Wright (2000). Sample size requirements for estimating Pearson, Kendall and Spearman correlations. *Psychometrika* 65, 23-28. [https://link.springer.com/article/10.1007/BF02294183](https://link.springer.com/article/10.1007/BF02294183)\n- Laidlaw, Singhal & Dragan (2025). Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking. *ICLR 2025 Spotlight*. [https://arxiv.org/abs/2403.03185](https://arxiv.org/abs/2403.03185)\n- Robust Optimization for Mitigating Reward Hacking with Correlated Proxies (2025). [https://arxiv.org/html/2604.12086](https://arxiv.org/html/2604.12086)\n- Puth, Neuhauser & Ruxton (2015). Asymptotic Properties of Spearman's Rank Correlation for Variables with Finite Support. *PLOS ONE*. [https://pmc.ncbi.nlm.nih.gov/articles/PMC4701424/](https://pmc.ncbi.nlm.nih.gov/articles/PMC4701424/)\n- Pohle, Wermuth & Weiss (2025). Asymptotic Inference for Rank Correlations. [https://arxiv.org/pdf/2512.14609](https://arxiv.org/pdf/2512.14609)\n- Croux & Dehon (2010). Influence functions of the Spearman and Kendall correlation measures. *Statistical Methods & Applications* 19, 497-515. [https://link.springer.com/article/10.1007/s10260-010-0142-z](https://link.springer.com/article/10.1007/s10260-010-0142-z)\n- Xu et al. (2013). A comparative analysis of Spearman's rho and Kendall's tau in normal and contaminated normal models. *Signal Processing* 93(1), 261-276. [https://arxiv.org/abs/1011.2009](https://arxiv.org/abs/1011.2009)\n- Derumigny & Fermanian (2019). On kernel-based estimation of conditional Kendall's tau: finite-distance bounds and asymptotic behavior. *Dependence Modeling* 7(1):292-321. [https://arxiv.org/pdf/1810.06234](https://arxiv.org/pdf/1810.06234)\n- Studentising Kendall's Tau (2023). [https://arxiv.org/html/2307.10973](https://arxiv.org/html/2307.10973)\n- Hoeffding (1948). A class of statistics with asymptotically normal distribution. *Annals of Mathematical Statistics* 19, 293-325.\n- Reward Hacking in Rubric-Based RL (2025). [https://arxiv.org/html/2605.12474](https://arxiv.org/html/2605.12474)\n- Adversarial Reward Auditing (2025). [https://arxiv.org/html/2602.01750v1](https://arxiv.org/html/2602.01750v1)\n- Weng (2024). Reward Hacking in Reinforcement Learning. [https://lilianweng.github.io/posts/2024-11-28-reward-hacking/](https://lilianweng.github.io/posts/2024-11-28-reward-hacking/)\n- How to Evaluate Reward Models for RLHF (2024). [https://arxiv.org/html/2410.14872v1](https://arxiv.org/html/2410.14872v1)"
      }
    ],
    "totalDurationMs": 308418,
    "totalTokens": 49224,
    "totalToolUseCount": 45,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2510,
      "cache_read_input_tokens": 41959,
      "output_tokens": 4754,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2510
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4754,
          "cache_read_input_tokens": 41959,
          "cache_creation_input_tokens": 2510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2510,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 1,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 44
    }
  },
  "sourceToolAssistantUUID": "58f15955-7643-4d60-942f-dbaf48e86e7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"MAJOR NARRATIVE RESTRUCTURING: Reframed entire proposal a…",
  "leafUuid": "43031182-b831-44c9-8077-c5fd8135cd8a",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gaming-resistant reward composition for autoformalization",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51"
}
```

---

### Assistant

_source line 24 · 2026-05-27T22:14:58.266Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent. Now I have comprehensive research on all the key topics. Let me synthesize my findings and make strategic decisions about the revision.

## Key findings from research:

### 1. CTWA (arXiv:2602.06869)
- Uses covariance between objective rewards and clipped advantages to drive weight adaptation
- More theoretically grounded than MO-GRPO (the covariance law directly explains interference)
- Same authors as DRW (Lu & Jiang)
- Objective-agnostic — monitors statistical relationships, not gaming
- Mechanistically closer to AGRC (signal-driven reweighting) than MO-GRPO (static normalization)


- Demonstrated effectiveness on math reasoning tasks across multiple model sizes

### 2. FormalRewardBench (arXiv:2605.10141)
- Proof-level benchmark with 250 preference pairs from MiniF2F including error-injected variants
- Specialized provers achieve around 24-36% accuracy while frontier LLMs like Claude Opus reach 60-70% on the same tasks
- Reveals a critical gap: models that excel at generating proofs don't necessarily excel at evaluating them, suggesting that reward models need explicit evaluation training rather than relying on domain expertise

### 3. Reward Hacking Survey (arXiv:2604.13602)
- Maps exploitation across four levels (feature, representation, evaluator, environment) and three detection phases (training, inference, post-hoc)
- Proposes the Proxy Compression Hypothesis explaining reward hacking as a combination of objective compression, optimization amplification, and evaluator-policy co-adaptation

### 4. VerifAI-2 (arXiv:2604.19459)
- Actually finds no evidence of systematic gaming in unified generation—an important correction to clarify
- Two-stage pipeline approach

Now looking at how models actually game the system: GPT-5 fabricates axioms as a reactive fallback while DeepSeek-R1 mistranslates premises to evade detection. The key insight is defining gaming functionally—errors that enable proof compilation when faithful formalization wouldn't—without needing to attribute intentionality.

### 5. GRS Theory
Now examining the sample complexity bounds and how they connect to the correlated proxies framework, where the regularization strength depends on the correlation parameter and the influence functions for rank-based metrics.

Rank-based measures like Spearman and Kendall have bounded influence functions compared to Pearson's unbounded ones, which makes GRS better suited for population-level monitoring while exploitation-rate works better for per-instance classification.

### 6. Crowded Multi-Objective GRPO Landscape
The space is filling up with variants like MO-GRPO doing per-objective variance normalization, CTWA adapting weights based on covariance targets, DRW using hypervolume gradients, BAE assigning credit at the token level, and TaRoS downweighting based on saturation.

The reviewer's core feedback is about scope—the proposal is trying to do too much and AGRC is losing novelty as the landscape evolves. They're pushing toward Option A: positioning this as an analysis paper with GRS as the centerpiece. Given the plateau around 3.5-3.6, a major refocus seems necessary.

I'm shifting the framing to make GRS the primary story. AGRC gets demoted from a co-equal contribution to a brief demonstration that GRS can guide dynamic mechanism composition. The real contributions become the systematic ablation of gaming resistance across isolated reward sources using the GRS framework anchored by GTED, plus deeper theoretical work on GRS itself—sample complexity bounds using Hoeffding statistics for U-statistics, formal connections to the Correlated Proxies framework showing how GRS estimates the correlation coefficient to enable data-driven regularization, and characterizing when GRS provides guarantees.

On the baseline question, I'm reconsidering whether CTWA should replace MO-GRPO. CTWA is mechanistically closer to AGRC and more theoretically grounded, but since AGRC is now secondary, the comparison becomes less critical. I think the better move is to cite CTWA as the closest objective-agnostic method while keeping MO-GRPO as the simpler, more familiar baseline for the brief AGRC section. This refocuses the paper on answering which reward signals resist gaming and what GRS reveals about them.

I need to be much more careful about the VerifAI-2 findings—the distinction between no systematic gaming in unified generation versus fabrication and mistranslation in two-stage pipelines is essential for a paper about gaming resistance. And I should cite FormalRewardBench for the generation-evaluation gap, since the finding that specialized provers perform worst at evaluation has real implications for how R_critic might degrade under gaming versus normal conditions.

This actually makes the case stronger for studying gaming resistance across different signal categories. The Reward Hacking survey provides useful theoretical grounding with the PCH framework.

Now I'm reconsidering the scope. The reviewer flagged that 8 evaluation analyses are too many, not necessarily the 10 configs themselves. So instead of cutting configs entirely, I should keep all 10 but demote AGRC and MO-GRPO from primary experimental status to lightweight demonstrations run only on the top-2 ablation configs. That reduces cognitive load without losing the full picture.

Re-reading the reviewer's actual suggestion, they're recommending I focus the paper's narrative around RQ1 (which signals resist gaming?) and RQ2 (hybrid composition effects) as primary, with GRS validation as a core contribution, while treating AGRC as a brief demonstration rather than a co-equal research question. This tightens the story: introduce GRS, systematically evaluate reward signals, then show how GRS can guide adaptive composition.

On the VerifAI-2 finding, the unified generation approach shows no systematic gaming patterns with high precision, but the two-stage pipeline reveals different failure modes—GPT-5 generates fabricated axioms reactively while DeepSeek-R1 mistranslates premises as an evasion strategy.

The gaming definition itself is outcome-based: errors that functionally enable proof compilation when faithful formalization wouldn't. This actually strengthens the motivation because it's more honest about the complexity—rather than claiming gaming is rampant everywhere, I can acknowledge that unified generation doesn't show systematic gaming, but pipelines do exhibit these evasion patterns, and FormaRL's ablation demonstrates that binary compilation rewards can be fully exploited. The real question becomes which reward signals preserve faithfulness under optimization pressure, which is more compelling than a simple "gaming is everywhere" narrative.

For the revision scope, I'm looking at demoting AGRC from co-primary contribution to a demonstration case, substantially deepening the GRS theory with sample complexity and correlated proxies connections, significantly correcting how VerifAI-2 is characterized, and adding CTWA, FormalRewardBench, and the reward hacking survey to the related work. This reframes the entire paper from "Analysis + Method" to primarily an "Analysis paper" with streamlined evaluation. That's a major structural shift, but the core insight stays intact.

The real problem might be that I keep expanding the narrative with new baselines and citations rather than sharpening the focus. The score has plateaued at 3.5-3.6 across rounds, and the reviewer is essentially saying the paper needs either a major overhaul or a fundamental pivot.

Committing to the "Analysis paper" direction means dropping the "Adaptive Gaming-Resistant Reward Composition" framing entirely, centering the title on the Gaming Resistance Score and systematic analysis instead. The structure becomes: GRS framework as the primary contribution with theoretical depth, systematic ablation of five reward source categories across eight configurations, and AGRC as a brief two-to-three page demonstration rather than a full section. I'm cutting from ten configurations down to eight by removing AGRC and MO-GRPO from the main evaluation.

Actually, rereading the reviewer feedback—they said the ten configs themselves are fine, the real issue is the proliferation of evaluation dimensions stacked on top of them. So I should keep the configs but ruthlessly streamline what I'm measuring: standard metrics, GRS decomposition per config and checkpoint, GRS validation comparing GTED versus human variants, new theoretical properties analysis covering sample complexity and robustness, and a brief critic scaling section.

I'm dropping the Spearman versus Kendall comparison as a separate analysis, the GRS-GTED versus exploitation-rate experiment, and the multi-metric faithfulness analysis—folding those into the decomposition instead. That brings me down to six core analyses with the theoretical properties as the new centerpiece.

Now I need to reconsider the experimental design itself, starting with what the original ten configs actually cover.

So the ablation becomes C1 through C8, which gives me the full spectrum from binary compilation through all the hybrid approaches. Then C9 and C10 shift to a brief demonstration section showing how AGRC and MO-GRPO perform with the best component set. That's a much cleaner narrative arc.

For scaling across model sizes, I'll run all eight ablations on the 7B model, then take the top four performers up to 30B. AGRC and MO-GRPO stay on 7B using the C8 configuration. This cuts down the compute significantly while keeping the story intact.

For the GRS theory section, the reviewer is asking for three specific things: sample complexity bounds so we know when GRS estimates are reliable, the conditions where GRS-GTED catches gaming that exploitation-rate misses and vice versa, and how GRS connects formally to the Correlated framework.

Looking at the math here: Kendall's tau has a concentration bound via Hoeffding's inequality that tells me I need around 737 samples for 0.1 precision at 95% confidence. The key difference between GRS and exploitation-rate is that GRS operates at the population level with a bounded influence function and runs in O(n log n) time, while exploitation-rate does per-instance classification. I need to flesh out where each method has advantages and when they diverge in detecting gaming behavior.

Now I'm seeing how GRS connects to the correlated proxies framework—the correlation parameter r from Definition 4.1 directly determines the regularization strength λ = σ·√(1-r²), so a low GRS score means I need stronger regularization. The confidence interval on GRS translates into a corresponding interval for the regularization parameter, which gives me a principled way to move from measurement to optimization.

I'm ready to restructure the entire paper around GRS as the core contribution, demoting AGRC to just one demonstration among several. The key changes are reframing this as an analysis paper, adding the missing benchmarks and theory sections, correcting some characterizations, and being honest about the crowded landscape of multi-objective reward optimization approaches. Let me now write out the complete revised JSON with all these improvements.

On the title—I want something that leads with the core research question rather than the method. The current framing is too method-heavy. Something like "Which Rewards Resist Gaming in Autoformalization RL?" puts the question first and feels more natural, then I can add the formally-grounded analysis part as the subtitle. Let me settle on a cleaner version that captures both the question and the methodological contribution without getting too wordy.

Now I need to think through the related work section more carefully. The reviewer flagged some specific papers I should address—Blockwise Advantage and TaRoS both touch on reward design and gaming-awareness, but they operate in different spaces. BAE is doing token-level credit assignment which is orthogonal to what I'm doing, while TaRoS is actually closer since it's thinking about saturation and Goodhart's Law in the context of video generation. I should acknowledge these as part of the landscape but clarify why they're not direct competitors to my approach.

But more importantly, I need to reconsider my motivation story now that I've looked more carefully at what VerifAI-2 actually found. The paper doesn't show gaming in unified generation—it shows fabrication and mistranslation problems in two-stage pipelines. So I can't cite it as evidence that "gaming is documented and severe" the way I originally framed it. What I do have is the FormaRL ablation showing clear gaming potential when you optimize for syntax alone, and VerifAI-2 demonstrates the faithfulness gap is real in practice, just through a different mechanism than I initially thought. I need to reframe the motivation around this more accurate picture.

The real story is that we don't understand the relationship between reward signals and faithfulness in autoformalization well enough. FormaRL shows the risk is structural, VerifAI-2 shows the problem manifests in practice, and my theoretical result explains why this gap exists under optimization pressure. GTED becomes the tool to systematically measure which signals actually preserve faithfulness during training. This is more honest and stronger than just claiming gaming is happening everywhere.

Now I'll write out the final JSON with this corrected motivation.

With the scope reduction, I'm recalculating the resource needs: running 8 configurations on the 7B model takes about 560 GPU hours, the top 4 on 30B takes another 280, the lightweight demonstrations of alternative methods add 210 hours, and the remaining grid search, inference, and evaluation work comes to roughly 200 more hours, bringing the total to around 1250 GPU hours.

Now I'm reconsidering the demonstration section based on the reviewer's feedback about CTWA. They're right that covariance-based adaptation is mechanistically closer to AGRC's approach than variance normalization, which would make CTWA a stronger baseline for comparison. Rather than running an exhaustive three-way comparison that expands scope, I should focus the demonstration on AGRC versus CTWA to show that GRS can inform composition choices, while acknowledging MO-GRPO as a related method without needing to include it in the direct comparison.

The tradeoff is that CTWA is more complex to implement since it requires computing covariance between each objective's reward and the clipped advantage weight during training, but given that AGRC is now positioned as a demonstration rather than a co-primary contribution, this cleaner comparison—both methods using signal-driven adaptation but with different signals—is more intellectually honest and likely more compelling to reviewers.

Now I'm restructuring the JSON to reflect these changes: updating the core problem statement with the VerifAI-2 correction, reframing the approach with GRS as primary and the ablation as the main contribution, repositioning AGRC as a demonstration, and revising all supporting sections like the landscape, opportunity, and references accordingly.

For the evaluation, I'm setting up a comprehensive ablation study with eight core configurations testing individual and hybrid reward components across model sizes, plus three demonstration configs showing how adaptive weighting strategies can be applied on top of the full hybrid system.

Then I'm streamlining the analyses down to six key evaluations: standard metrics with automated faithfulness checks, GRS decomposition across configs and checkpoints, validation against expert annotations with confidence intervals, theoretical verification of sample complexity and robustness properties, comparison of critic model sizes on GRS performance, and finally a demonstration of the three weighting approaches with their trade-offs. I'm consolidating some analyses—merging the correlation metrics together, moving the exploitation-rate comparison to discussion, and folding multi-metric faithfulness into the main metrics analysis—to keep things focused.

For the research questions, I'm refining them to directly address the core claims: gaming resistance across signal categories, whether hybrid composition adds faithfulness without sacrificing robustness, whether GRS-GTED predicts human judgments reliably, and whether adaptive composition beats non-adaptive baselines. I'm considering dropping the critic scaling as a standalone question since that can fit as a sub-analysis within the first RQ, keeping the focus tighter.

On the annotation side, I'm weighing whether 450 samples across the main config pairs is sufficient for validation or if I should stick with 600 to give the analysis more statistical weight.

The reviewer's point about gaming versus unfaithfulness is crucial—I need to adopt an outcome-based definition where gaming means errors that functionally enable proof compilation that wouldn't otherwise succeed, regardless of intent. This shifts the framing of what we're actually measuring.

So gaming resistance becomes about how well a reward signal's rankings correlate with true faithfulness under optimization pressure, and FormaRL's ablation already demonstrates this perfectly: syntax-only RL achieves 100% compilation but 0% consistency, showing gaming emerges from optimization alone without requiring intentionality.

On the reviewer's point about AGRC—they're right that it's gaming-specific while the other five methods are objective-agnostic, but the contribution isn't just plugging a different signal into the adaptive reweighting paradigm. I need to clarify what makes AGRC's approach distinct beyond that.

Actually, I should restructure the approach around what's genuinely novel. The real contributions are GRS itself and the analysis showing how gaming emerges. AGRC is just the application. Let me reorganize into cleaner phases: first extracting the multi-source reward signals, then developing the GRS framework with its theoretical grounding, then running the systematic ablations across configurations and model scales, then briefly showing AGRC as a demonstration, and finally the evaluation framework with the six streamlined analyses.

Writing the full JSON structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43031182-b831-44c9-8077-c5fd8135cd8a",
  "isSidechain": false,
  "requestId": "req_011CbTqk4dQpiSD9gRz2iAiA",
  "type": "assistant",
  "uuid": "be3c73b9-8a61-4964-919a-e8eebce6004e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XMybM7JcZZ84uK7ovhREP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17205,
      "cache_read_input_tokens": 24686,
      "output_tokens": 7550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7550,
          "cache_read_input_tokens": 24686,
          "cache_creation_input_tokens": 17205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17205
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-27T22:15:02.321Z_

Now let me synthesize all the research findings to make strategic revision decisions. The research reveals several critical insights:

1. **CTWA** (covariance-targeted weight adaptation) is mechanistically closer to AGRC than MO-GRPO — both do signal-driven reweighting
2. **VerifAI-2** actually finds "no evidence of systematic gaming in unified generation" — our characterization has been wrong
3. **FormalRewardBench** reveals a generation-evaluation gap relevant to R_critic
4. The **crowded multi-objective GRPO landscape** (5+ methods) makes AGRC's novelty as a co-primary contribution weak
5. Rich theoretical material exists to deepen GRS (sample complexity, Correlated Proxies connection, influence functions)

The clear strategic move is a **major revision** — reframe as an analysis paper with GRS as the star, demote AGRC to demonstration. Let me now produce the complete revised proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be3c73b9-8a61-4964-919a-e8eebce6004e",
  "isSidechain": false,
  "requestId": "req_011CbTqk4dQpiSD9gRz2iAiA",
  "type": "assistant",
  "uuid": "f093ccbc-e4f5-48df-9b68-160e87067909",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XMybM7JcZZ84uK7ovhREP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17205,
      "cache_read_input_tokens": 24686,
      "output_tokens": 7550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7550,
          "cache_read_input_tokens": 24686,
          "cache_creation_input_tokens": 17205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17205
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-27T22:15:02.627Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Vp9tB5xaqdYtHeoDHVmTFp`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f093ccbc-e4f5-48df-9b68-160e87067909",
  "isSidechain": false,
  "requestId": "req_011CbTqk4dQpiSD9gRz2iAiA",
  "type": "assistant",
  "uuid": "5a10b310-74c2-4ac7-9512-fc8012baa5c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XMybM7JcZZ84uK7ovhREP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17205,
      "cache_read_input_tokens": 24686,
      "output_tokens": 7550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7550,
          "cache_read_input_tokens": 24686,
          "cache_creation_input_tokens": 17205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17205
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-27T22:15:02.634Z_

<details><summary>↩ Tool result · `toolu_01Vp9tB5xaqdYtHeoDHVmTFp`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a10b310-74c2-4ac7-9512-fc8012baa5c1",
  "isSidechain": false,
  "promptId": "6d783516-df0e-455a-9cd7-fd412aff8d61",
  "type": "user",
  "uuid": "7165a641-d18f-446d-ac76-d29d17a5b7f4",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "5a10b310-74c2-4ac7-9512-fc8012baa5c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"MAJOR NARRATIVE RESTRUCTURING: Reframed entire proposal a…",
  "leafUuid": "7165a641-d18f-446d-ac76-d29d17a5b7f4",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gaming-resistant reward composition for autoformalization",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51"
}
```

---

### Assistant

_source line 30 · 2026-05-27T22:15:09.318Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do a final check on a couple of things before writing the full revision. Let me verify the CTWA paper's exact arXiv ID and check if there are any other recent papers I should be aware of in the adaptive GRPO weight space.

Actually, I have enough information from my research agents. Let me now write the complete revised JSON proposal. This is a major revision that:

1. Reframes as an "Analysis paper" with GRS as the star
2. Demotes AGRC to a lightweight demonstration
3. Corrects VerifAI-2 characterization
4. Adds CTWA, FormalRewardBench, reward hacking survey


5. Deepens GRS theory substantially
6. Streamlines evaluation
7. Addresses the crowded landscape honestly

Writing the JSON proposal...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7165a641-d18f-446d-ac76-d29d17a5b7f4",
  "isSidechain": false,
  "requestId": "req_011CbTqxZJubFUTFbZX3vTxF",
  "type": "assistant",
  "uuid": "9bef3880-869c-4e52-aaeb-2174aa0a603e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EieLtu85LWwSXqp2frVEYt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8569,
      "cache_read_input_tokens": 41891,
      "output_tokens": 357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 357,
          "cache_read_input_tokens": 41891,
          "cache_creation_input_tokens": 8569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8569
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-27T22:15:09.323Z_

Now I have all the research I need. Let me produce the complete major revision.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bef3880-869c-4e52-aaeb-2174aa0a603e",
  "isSidechain": false,
  "requestId": "req_011CbTqxZJubFUTFbZX3vTxF",
  "type": "assistant",
  "uuid": "d780becf-4cf6-47f6-b4d6-b83ccebad77f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EieLtu85LWwSXqp2frVEYt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8569,
      "cache_read_input_tokens": 41891,
      "output_tokens": 357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 357,
          "cache_read_input_tokens": 41891,
          "cache_creation_input_tokens": 8569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8569
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-27T22:15:10.093Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VdVaUD3Rpb81LZ2Hf1zeLo`</summary>

```json
{
  "query": "arXiv 2602.06869 CTWA covariance targeted weight adaptation multi-objective GRPO 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d780becf-4cf6-47f6-b4d6-b83ccebad77f",
  "isSidechain": false,
  "requestId": "req_011CbTqxZJubFUTFbZX3vTxF",
  "type": "assistant",
  "uuid": "b1ec0e8e-5a3a-4663-968d-b987f1b5c01f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EieLtu85LWwSXqp2frVEYt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8569,
      "cache_read_input_tokens": 41891,
      "output_tokens": 357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 357,
          "cache_read_input_tokens": 41891,
          "cache_creation_input_tokens": 8569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8569
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-27T22:15:10.638Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AGKbNvNNLGkYebgiviELdE`</summary>

```json
{
  "query": "TaRoS \"target-robust reward\" video GRPO saturation arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1ec0e8e-5a3a-4663-968d-b987f1b5c01f",
  "isSidechain": false,
  "requestId": "req_011CbTqxZJubFUTFbZX3vTxF",
  "type": "assistant",
  "uuid": "3419f93d-b35c-493c-b96b-789b50d091f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EieLtu85LWwSXqp2frVEYt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8569,
      "cache_read_input_tokens": 41891,
      "output_tokens": 357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 357,
          "cache_read_input_tokens": 41891,
          "cache_creation_input_tokens": 8569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8569
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-27T22:15:16.613Z_

<details><summary>↩ Tool result · `toolu_01VdVaUD3Rpb81LZ2Hf1zeLo`</summary>

```text
Web search results for query: "arXiv 2602.06869 CTWA covariance targeted weight adaptation multi-objective GRPO 2026"

Links: [{"title":"[2602.06869] Uncovering Cross-Objective Interference in Multi-Objective Alignment","url":"https://arxiv.org/abs/2602.06869"},{"title":"Uncovering Cross-Objective Interference in Multi-Objective Alignment","url":"https://arxiv.org/html/2602.06869"},{"title":"Uncovering Cross-Objective Interference in Multi-Objective Alignment","url":"https://arxiv.org/pdf/2602.06869"},{"title":"Double-Weighting for Covariate Shift Adaptation","url":"https://arxiv.org/pdf/2305.08637"},{"title":"Nearest Neighbor Sampling for Covariate Shift Adaptation","url":"https://arxiv.org/pdf/2312.09969"},{"title":"Robust Covariance Adaptation in Adaptive Importance Sampling","url":"https://arxiv.org/pdf/1806.00093"},{"title":"Information Geometrically Generalized Covariate Shift Adaptation","url":"https://arxiv.org/pdf/2304.09387"},{"title":"Adversarial Weighting for Domain Adaptation in Regression","url":"https://arxiv.org/pdf/2006.08251"}]

I found the arXiv paper you're looking for! Here's what I found:

**Paper Details:**
- **arXiv ID:** 2602.06869
- **Title:** "Uncovering Cross-Objective Interference in Multi-Objective Alignment"
- **Publication Date:** February 6, 2026

**Key Findings:**

The paper studies a failure mode in multi-objective alignment for large language models where training improves performance on some objectives while degrading others, formalized as cross-objective interference.

**Main Contribution - CTWA Method:**

The authors propose Covariance Targeted Weight Adaptation (CTWA), a plug-and-play method that maintains positive covariance between objective rewards and the training signal to effectively mitigate cross-objective interference.

**Theoretical Foundation:**

The paper derives a local covariance law showing that an objective improves at first order when its reward exhibits positive covariance with the scalarized score. This analysis is extended to clipped surrogate objectives used in modern reinforcement fine-tuning, such as GRPO, demonstrating that the first-order covariance law remains valid despite clipping.

The paper appears to address a significant challenge in multi-objective LLM alignment by providing both theoretical analysis and a practical solution for handling competing objectives during training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1ec0e8e-5a3a-4663-968d-b987f1b5c01f",
  "isSidechain": false,
  "promptId": "6d783516-df0e-455a-9cd7-fd412aff8d61",
  "type": "user",
  "uuid": "d72be434-2c1e-437a-969d-39cecb5495ec",
  "toolUseResult": {
    "query": "arXiv 2602.06869 CTWA covariance targeted weight adaptation multi-objective GRPO 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019SYwjLhUuXbr6kMpgZ6buX",
        "content": [
          {
            "title": "[2602.06869] Uncovering Cross-Objective Interference in Multi-Objective Alignment",
            "url": "https://arxiv.org/abs/2602.06869"
          },
          {
            "title": "Uncovering Cross-Objective Interference in Multi-Objective Alignment",
            "url": "https://arxiv.org/html/2602.06869"
          },
          {
            "title": "Uncovering Cross-Objective Interference in Multi-Objective Alignment",
            "url": "https://arxiv.org/pdf/2602.06869"
          },
          {
            "title": "Double-Weighting for Covariate Shift Adaptation",
            "url": "https://arxiv.org/pdf/2305.08637"
          },
          {
            "title": "Nearest Neighbor Sampling for Covariate Shift Adaptation",
            "url": "https://arxiv.org/pdf/2312.09969"
          },
          {
            "title": "Robust Covariance Adaptation in Adaptive Importance Sampling",
            "url": "https://arxiv.org/pdf/1806.00093"
          },
          {
            "title": "Information Geometrically Generalized Covariate Shift Adaptation",
            "url": "https://arxiv.org/pdf/2304.09387"
          },
          {
            "title": "Adversarial Weighting for Domain Adaptation in Regression",
            "url": "https://arxiv.org/pdf/2006.08251"
          }
        ]
      },
      "I found the arXiv paper you're looking for! Here's what I found:\n\n**Paper Details:**\n- **arXiv ID:** 2602.06869\n- **Title:** \"Uncovering Cross-Objective Interference in Multi-Objective Alignment\"\n- **Publication Date:** February 6, 2026\n\n**Key Findings:**\n\nThe paper studies a failure mode in multi-objective alignment for large language models where training improves performance on some objectives while degrading others, formalized as cross-objective interference.\n\n**Main Contribution - CTWA Method:**\n\nThe authors propose Covariance Targeted Weight Adaptation (CTWA), a plug-and-play method that maintains positive covariance between objective rewards and the training signal to effectively mitigate cross-objective interference.\n\n**Theoretical Foundation:**\n\nThe paper derives a local covariance law showing that an objective improves at first order when its reward exhibits positive covariance with the scalarized score. This analysis is extended to clipped surrogate objectives used in modern reinforcement fine-tuning, such as GRPO, demonstrating that the first-order covariance law remains valid despite clipping.\n\nThe paper appears to address a significant challenge in multi-objective LLM alignment by providing both theoretical analysis and a practical solution for handling competing objectives during training."
    ],
    "durationSeconds": 6.515682384999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b1ec0e8e-5a3a-4663-968d-b987f1b5c01f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-27T22:15:17.355Z_

<details><summary>↩ Tool result · `toolu_01AGKbNvNNLGkYebgiviELdE`</summary>

```text
Web search results for query: "TaRoS "target-robust reward" video GRPO saturation arXiv 2026"

Links: [{"title":"Rethinking Reward Signals in Video GRPO: When Scores Become Targets","url":"https://arxiv.org/pdf/2511.19356"},{"title":"Rethinking Reward Signals in Video GRPO: When Scores Become Targets","url":"https://arxiv.org/html/2511.19356"},{"title":"[2511.19356] Rethinking Reward Signals in Video GRPO: When Scores Become Targets","url":"https://arxiv.org/abs/2511.19356"},{"title":"[2506.07464] DeepVideo-R1: Video Reinforcement Fine-Tuning via Difficulty-aware Regressive GRPO","url":"https://arxiv.org/abs/2506.07464"},{"title":"[2603.26599] VGGRPO: Towards World-Consistent Video Generation with 4D Latent Reward","url":"https://arxiv.org/abs/2603.26599"},{"title":"[2603.21872] Manifold-Aware Exploration for Reinforcement Learning in Video Generation","url":"https://arxiv.org/abs/2603.21872"},{"title":"[2601.05729] TAGRPO: Boosting GRPO on Image-to-Video Generation with Direct Trajectory Alignment","url":"https://arxiv.org/abs/2601.05729"}]

I found the paper you're looking for! Here are the key findings:

TaRoS is a Target-Robust Reward Signaling framework for Video generation GRPO. While Group Relative Policy Optimization (GRPO) enables stable and preference-oriented updates via group-wise comparisons for posttraining video generation, GRPO directly optimizes reward-induced advantages, and under sustained optimization, the reward score can lose fidelity as a proxy for true video quality, leading to shortcut-driven optimization under composite objectives and reward saturation within prompt groups.

TaRoS leverages component level performance assessment together with intra-group sparsity to organize multi-aspect rewards towards optimization objectives and adaptively downweights components that exhibit saturation, thereby preserving effective optimization directions and mitigating redundancy. Extensive experiments show consistent improvements in visual fidelity, motion coherence, and text-video alignment over strong baselines.

The paper (arXiv 2511.19356) was published on March 17, 2026, and addresses the fundamental challenge of reward signal degradation in video generation optimization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3419f93d-b35c-493c-b96b-789b50d091f8",
  "isSidechain": false,
  "promptId": "6d783516-df0e-455a-9cd7-fd412aff8d61",
  "type": "user",
  "uuid": "a6c2e2f3-9cdd-474f-87c3-e213b113b7d7",
  "toolUseResult": {
    "query": "TaRoS \"target-robust reward\" video GRPO saturation arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0193qSN38VoimCbUQUXfvdsM",
        "content": [
          {
            "title": "Rethinking Reward Signals in Video GRPO: When Scores Become Targets",
            "url": "https://arxiv.org/pdf/2511.19356"
          },
          {
            "title": "Rethinking Reward Signals in Video GRPO: When Scores Become Targets",
            "url": "https://arxiv.org/html/2511.19356"
          },
          {
            "title": "[2511.19356] Rethinking Reward Signals in Video GRPO: When Scores Become Targets",
            "url": "https://arxiv.org/abs/2511.19356"
          },
          {
            "title": "[2506.07464] DeepVideo-R1: Video Reinforcement Fine-Tuning via Difficulty-aware Regressive GRPO",
            "url": "https://arxiv.org/abs/2506.07464"
          },
          {
            "title": "[2603.26599] VGGRPO: Towards World-Consistent Video Generation with 4D Latent Reward",
            "url": "https://arxiv.org/abs/2603.26599"
          },
          {
            "title": "[2603.21872] Manifold-Aware Exploration for Reinforcement Learning in Video Generation",
            "url": "https://arxiv.org/abs/2603.21872"
          },
          {
            "title": "[2601.05729] TAGRPO: Boosting GRPO on Image-to-Video Generation with Direct Trajectory Alignment",
            "url": "https://arxiv.org/abs/2601.05729"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key findings:\n\nTaRoS is a Target-Robust Reward Signaling framework for Video generation GRPO. While Group Relative Policy Optimization (GRPO) enables stable and preference-oriented updates via group-wise comparisons for posttraining video generation, GRPO directly optimizes reward-induced advantages, and under sustained optimization, the reward score can lose fidelity as a proxy for true video quality, leading to shortcut-driven optimization under composite objectives and reward saturation within prompt groups.\n\nTaRoS leverages component level performance assessment together with intra-group sparsity to organize multi-aspect rewards towards optimization objectives and adaptively downweights components that exhibit saturation, thereby preserving effective optimization directions and mitigating redundancy. Extensive experiments show consistent improvements in visual fidelity, motion coherence, and text-video alignment over strong baselines.\n\nThe paper (arXiv 2511.19356) was published on March 17, 2026, and addresses the fundamental challenge of reward signal degradation in video generation optimization."
    ],
    "durationSeconds": 6.713969228000031,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3419f93d-b35c-493c-b96b-789b50d091f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-27T22:15:17.359Z_

```json
{
  "parentUuid": "a6c2e2f3-9cdd-474f-87c3-e213b113b7d7",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d47bc5dd-988b-4567-9306-95b1a4896fb6",
  "timestamp": "2026-05-27T22:15:17.359Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-27T22:15:33.851Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've confirmed the details. Now let me write the complete revised JSON proposal. This is going to be a substantial major revision.

Let me organize my thoughts one final time:

**Key strategic decisions:**
1. Reframe as "Analysis paper" — GRS framework + systematic ablation as primary contributions
2. Demote AGRC to lightweight demonstration (Section 6, ~2 pages)
3. Deepen GRS theory substantially (sample complexity, Correlated Proxies, robustness)
4. Correct VerifAI-2 characterization (no systematic gaming in unified generation; fabrication/mistranslation in pipelines)


5. Define gaming through outcomes rather than mechanisms, aligned with VerifAI-2
6. Bring in CTWA as the main adaptive baseline since it's mechanistically similar to AGRC
7. Incorporate FormalRewardBench findings about the critic reward signal
8. Reference the reward hacking survey when discussing the PCH framework
9. Cut the evaluation down from eight analyses to six
10. Pare down the main configurations from ten to eight, plus three for the demonstration

**The narrative arc:**
- Motivation: Autoformalization combines diverse reward signals; the relationship between reward and faithfulness under optimization is poorly understood
- Key insight: GTED provides...

GTED serves as a formally-grounded anchor unique to autoformalization for measuring how reward signals behave under optimization pressure. The GRS framework with its theoretical foundations forms the core contribution, supported by systematic ablations showing which signals are robust to gaming, and rounded out with a brief AGRC demonstration illustrating how GRS insights can guide reward composition.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d47bc5dd-988b-4567-9306-95b1a4896fb6",
  "isSidechain": false,
  "requestId": "req_011CbTqye1Tc37CeERkoSGM1",
  "type": "assistant",
  "uuid": "3633fe10-fee6-4fb9-9ec9-741efb8a3b80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VbXdvuChYidYFf7kDi6Dy3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1809,
      "cache_read_input_tokens": 50460,
      "output_tokens": 13587,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13587,
          "cache_read_input_tokens": 50460,
          "cache_creation_input_tokens": 1809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1809
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-27T22:20:32.986Z_

Now I have all the research needed. Let me synthesize everything into the complete revised proposal. This will be a **major revision** that reframes the paper as an analysis paper with GRS as the star contribution.

```json
{
  "change_type": "major",
  "changes_made": [
    "MAJOR REFRAME TO ANALYSIS PAPER: Following reviewer recommendation (option A), restructured entire proposal around the GRS framework and systematic ablation as co-primary contributions. AGRC demoted from co-primary to lightweight demonstration (~2 pages). Rationale: the crowded multi-objective GRPO landscape (MO-GRPO, CTWA, DRW, BAE, TaRoS — at least 5 objective-agnostic adaptive methods) reduces AGRC's novelty to 'plugging GRS into the adaptive reweighting paradigm,' whereas the gaming-resistance analysis and GRS framework with deep theory are genuinely novel contributions. This reframe should break the 3.5-3.6 scoring plateau by sharpening focus.",
    "ADDED CTWA — Covariance Targeted Weight Adaptation (arXiv:2602.06869, Feb 2026, revised May 2026) by Lu & Jiang (same authors as DRW, TACL 2026). CTWA derives a local covariance law: objective m improves iff Cov(r_m, s) > 0 where s is the scalarized training signal. CTWA adaptively upweights objectives whose covariance dips below a positive target c*_m. Differentiated from AGRC at three levels: (a) CTWA monitors covariance between rewards and training signal (interference-aware, gaming-agnostic); AGRC monitors rank correlation between rewards and faithfulness (gaming-specific); (b) CTWA detects when an objective degrades under optimization regardless of cause; AGRC specifically detects faithfulness decorrelation; (c) CTWA requires no external quality anchor; AGRC requires GTED as faithfulness reference. CTWA replaces MO-GRPO as primary adaptive comparison in the AGRC demonstration section because its signal-driven mechanism is mechanistically closer to AGRC's approach than MO-GRPO's static normalization, making it a harder and more informative baseline.",
    "ADDED FormalRewardBench (arXiv:2605.10141, May 11, 2026): first benchmark for evaluating reward models in formal theorem proving with Lean 4. Key finding: specialized theorem provers perform worst at proof evaluation (24.4% pairwise consistency) while frontier LLMs are best (Claude Opus 4.5: 59.8%). Reveals a generation-evaluation gap — models trained to generate correct proofs do not learn to detect errors. Implications for our R_critic signal: CriticLeanGPT's evaluation accuracy (84.8% on CriticLeanBench) may not transfer to gaming detection because FormalRewardBench shows formal-domain evaluation is fundamentally harder than generation. Added as motivation for studying gaming resistance per signal category — R_critic's gaming resistance cannot be assumed from its normal-condition accuracy.",
    "ADDED Reward Hacking survey (arXiv:2604.13602, April 2026): comprehensive taxonomy proposing four-level exploitation hierarchy (feature/representation/evaluator/environment) cross-cut by three-phase detection lifecycle (training-time/inference-time/post-hoc), unified by the Proxy Compression Hypothesis (PCH). PCH posits reward hacking emerges from three interacting forces: objective compression (lossy mapping of high-dimensional values to low-dimensional proxies), optimization amplification (search pressure toward proxy extrapolation regions), and evaluator-policy co-adaptation (blind spots stabilize rather than resolve). Cited as contextual theoretical reference; PCH provides additional motivation for why gaming resistance measurement matters — if proxies inevitably compress, measuring which proxies compress least is the practical question.",
    "CORRECTED VerifAI-2 CHARACTERIZATION: Previous claim '87-99% compilation success masks systematic unfaithfulness' was imprecise. VerifAI-2 (arXiv:2604.19459) actually finds 'no evidence of systematic gaming in unified generation' — both models maintain 94-98% definite precision. The paper documents unfaithfulness specifically in TWO-STAGE PIPELINES: GPT-5 fabricates axioms as a 'reactive fallback detectable via cross-stage comparison' (107 cases, mixed across runs suggesting reactive not strategic behavior); DeepSeek-R1 mistranslates premises producing 'internally consistent outputs that evade detection entirely.' VerifAI-2 uses an outcome-based definition: 'formalization gaming is the subset of unfaithfulness where errors functionally enable proof compilation that a faithful formalization would not have achieved' — no intent attribution required. Revised motivation now correctly distinguishes: (a) FormaRL ablation demonstrates gaming under optimization (100% compilation, 0% consistency — clear gaming); (b) VerifAI-2 shows faithfulness gaps in pipelines even without 'systematic gaming'; (c) theoretical equilibrium result (arXiv:2603.28063) proves gaming is structural under finite evaluation. This nuanced framing is more honest and defensible.",
    "ADOPTED OUTCOME-BASED GAMING DEFINITION: Following VerifAI-2's framework, gaming is now defined as 'reward inflation without corresponding faithfulness improvement' — outcome-based, no intent attribution. Gaming resistance = degree to which a reward signal's rankings correlate with true faithfulness under optimization pressure. This sidesteps the gaming-vs-capability-limitation debate and focuses on the measurable quantity: reward-faithfulness correlation.",
    "SUBSTANTIALLY DEEPENED GRS THEORY (new Section 3): (a) SAMPLE COMPLEXITY BOUNDS: Via Hoeffding's inequality for degree-2 U-statistics with kernel bounded in [-1,1], P(|GRS_hat - GRS| > ε) ≤ 2exp(-nε²/2). For ε=0.1, δ=0.05: n ≥ 737 evaluation pairs suffice. Kendall CI width ≈ 2·1.96·√((1-τ²)/n). This tells practitioners exactly how many samples are needed for reliable GRS estimation. (b) FORMAL CONNECTION TO CORRELATED PROXIES (arXiv:2403.03185, ICLR 2025 Spotlight): GRS estimates the correlation parameter r in Definition 4.1 of the Correlated Proxies framework. Theorem 5.1 gives safe optimization bound: J(π,R) - J(π_base,R) ≥ (1/r)[proxy_improvement - σ·√((1-r²)·χ²(μ_π||μ_base))]. The safe regularization strength is λ = σ·√(1-r²). Therefore, a GRS confidence interval [τ_L, τ_U] directly translates to a regularization interval [σ·√(1-τ_U²), σ·√(1-τ_L²)], providing data-driven regularization calibration. This formally bridges GRS measurement to optimization policy. (c) ROBUSTNESS VIA INFLUENCE FUNCTIONS: Per Croux & Dehon (2010), Spearman's ρ and Kendall's τ have bounded, smooth influence functions — gross-error sensitivity is finite. Under ε-contaminated models (bivariate normal with fraction ε outliers), rank correlations maintain bounded bias while Pearson's r has unbounded influence proportional to outlier magnitude. At 5-10% contamination (realistic for gaming under RL training), Kendall's τ achieves lowest MSE among all correlation measures (Xu et al., 2013). (d) GRS VS EXPLOITATION-RATE DETECTION REGIMES: Proved complementary detection domains — GRS provides population-level monitoring with O(n log n) computation and bounded influence; exploitation-rate provides per-instance classification at O(K·n) frontier model cost but is vulnerable to correlated judge failures. GRS dominates when contamination fraction ε > 0.05, when evaluator cost is constrained, or when judge diversity is limited. Exploitation-rate dominates for per-instance flagging. Formal claim: under contamination model where a fraction ε of outputs inflate rewards without improving faithfulness, GRS detects population-level gaming shifts with n ≥ 2log(2/δ)/ε² samples, while exploitation-rate requires per-instance panel evaluation with no formal false-negative guarantees under correlated judge failure.",
    "ACKNOWLEDGED CROWDED MULTI-OBJECTIVE GRPO LANDSCAPE: Now explicitly lists 5+ objective-agnostic adaptive methods: (1) MO-GRPO (variance normalization), (2) CTWA (covariance-targeted), (3) DRW (hypervolume/gradient-based), (4) BAE (blockwise token-level credit assignment, arXiv:2602.10231), (5) TaRoS (saturation-aware via Hoyer sparsity, arXiv:2511.19356). Honest acknowledgment that AGRC's mechanism is 'plugging GRS into the adaptive reweighting paradigm' — hence its demotion to demonstration. The paper's novelty is in GRS (the signal) and the systematic analysis (the findings), not in the reweighting mechanism.",
    "STREAMLINED EVALUATION: Reduced from 8 evaluation analyses to 6: (1) Standard metrics + automated faithfulness, (2) GRS decomposition per config × checkpoint (Spearman and Kendall reported together, not as separate analysis), (3) GRS-human validation with 600 expert annotations + bootstrap CIs, (4) GRS theoretical validation — empirical verification of sample complexity bounds, contamination robustness, and Correlated Proxies connection, (5) Critic scaling (14B vs 8B), (6) AGRC vs CTWA vs MO-GRPO brief demonstration. Dropped: GRS-Spearman vs GRS-Kendall as standalone analysis; GRS-GTED vs exploitation-rate experimental comparison (now analytical only); multi-metric faithfulness as standalone analysis (folded into analysis 1).",
    "REDUCED MAIN ABLATION TO 8 CONFIGS: C1-C8 constitute the main systematic ablation. AGRC (D1), CTWA (D2), and MO-GRPO (D3) are run only on 7B with C8 component set as a lightweight demonstration section. This separation clarifies the paper's structure: Sections 3-5 are the primary contribution (GRS + ablation), Section 6 is the applied demonstration.",
    "REVISED RESEARCH QUESTIONS: Reduced from 5 to 4 cleaner RQs. RQ1: Which reward signal categories exhibit highest gaming resistance in isolation? (includes critic scaling as sub-analysis). RQ2: Does hybrid composition improve gaming resistance additively? RQ3: Is GRS-GTED a reliable automated proxy for expert gaming assessment? RQ4: Does gaming-specific adaptation outperform gaming-agnostic adaptation? (brief demonstration). Dropping the separate Spearman-vs-Kendall RQ and exploitation-rate comparison RQ.",
    "UPDATED RESOURCE ESTIMATES: Reduced GPU hours from 1500 to ~1200 H100 due to AGRC/CTWA/MO-GRPO demotion to 7B-only demonstration. Human audit hours unchanged at ~70. Timeline tightened to 14-16 weeks for ICLR, reflecting the more focused scope."
  ],
  "title": "Which Rewards Resist Gaming? Formally-Grounded Gaming Resistance Analysis for Autoformalization RL",
  "core_problem": "RL-based autoformalization combines composite rewards — binary compilation (FormaRL, Mathesis), LLM semantic judges (Mathesis R_sem), embedding similarity (Online RL for Autoformalization), and trained critics (CriticLean at 84.8% accuracy) — yet a fundamental question remains unanswered: which reward signals maintain faithfulness under optimization pressure, and can we measure this automatically?\n\nThis question is urgent for three reasons. First, the reward-faithfulness gap in autoformalization is documented: FormaRL's ablation reveals syntax-only RL yields 100% compilation but 0% semantic consistency, demonstrating clear gaming under optimization. VerifAI-2 (arXiv:2604.19459) provides complementary evidence: while finding no evidence of systematic gaming in unified generation (94-98% definite precision), it documents fabrication (GPT-5) and premise mistranslation (DeepSeek-R1) in two-stage pipelines that evade detection — showing faithfulness gaps even in high-performing systems. Following VerifAI-2's outcome-based definition, we define gaming as reward inflation without corresponding faithfulness improvement, requiring no intent attribution.\n\nSecond, theoretically, 'Reward Hacking as Equilibrium' (arXiv:2603.28063) proves gaming is a structural equilibrium under finite evaluation — not a correctable bug. The Proxy Compression Hypothesis (arXiv:2604.13602) further explains this as the inevitable consequence of objective compression, optimization amplification, and evaluator-policy co-adaptation. Together, these results make measuring gaming RESISTANCE — which signals degrade least — the critical practical question.\n\nThird, the broader RL community has responded with gaming mitigations at multiple levels: MO-GRPO normalizes per-objective variance; CTWA (arXiv:2602.06869) adaptively targets covariance between rewards and training signal; Advantage Modification integrates representation-level shortcut scores; SignCert-PO certifies advantage sign robustness; GRIFT detects gaming via gradient fingerprints; exploitation-rate measures hacking via LLM panels. However, ALL these methods are domain-agnostic. Autoformalization has a UNIQUE advantage: the Lean language server provides formally-grounded, LLM-independent faithfulness measurement via GTED tree-edit-distance (AI4Math@ICML 2025). This creates three domain-specific gaps that no existing work addresses: (1) No systematic comparison of gaming-resistance properties across isolated reward source categories for autoformalization; (2) No gaming-resistance metric leveraging formally-grounded faithfulness anchors — enabling detection that is simultaneously lightweight, automated, and non-circular; (3) No formal theoretical analysis connecting gaming-resistance measurement to the broader reward hacking framework.",
  "opportunity": "A unique convergence of seven developments makes this the right moment for this study:\n\n(1) GTED (AI4Math@ICML 2025) provides formally-grounded faithfulness via tree-edit-distance over Lean operator trees — the KEY enabling capability. Unlike code generation (where test-based evaluation lacks formally-grounded semantic metrics) or general RLHF (where ground truth is subjective), autoformalization offers a computable, LLM-independent faithfulness anchor.\n\n(2) The reward-faithfulness gap is newly documented but unquantified for autoformalization. FormaRL's ablation demonstrates gaming under optimization; VerifAI-2 documents faithfulness gaps in pipelines. We provide the first systematic measurement of which signals are affected and by how much.\n\n(3) Mathesis (ICLR 2026) establishes composite rewards for autoformalization GRPO but treats composition as a performance optimization problem, not a gaming-resistance problem.\n\n(4) CriticLean (July 2025) creates a new reward signal category (trained critic at 84.8%) untested as direct RL signal. FormalRewardBench (arXiv:2605.10141) reveals a generation-evaluation gap — specialized provers perform worst at proof evaluation (24.4% pairwise) while frontier LLMs are best (59.8%) — raising the question of how trained critics' gaming resistance relates to their normal-condition accuracy.\n\n(5) Rich theoretical infrastructure now exists for formalizing gaming resistance: the Correlated Proxies framework (arXiv:2403.03185, ICLR 2025 Spotlight) defines hacking via proxy-true correlation breakdown and proves regularization bounds parametrized by this correlation — precisely the quantity GRS measures. This creates opportunity for a formal bridge between GRS and optimization theory.\n\n(6) The proliferation of domain-agnostic adaptive methods (MO-GRPO, CTWA, DRW, BAE, TaRoS — 5+ methods in 2025-2026) creates urgency for domain-specific evaluation: do autoformalization's formal verification capabilities enable better gaming-resistance measurement than general-purpose approaches?\n\n(7) 'Reward Hacking as Equilibrium' (arXiv:2603.28063) proves hacking is structural under finite evaluation, and the Proxy Compression Hypothesis (arXiv:2604.13602) explains it as an inevitable consequence of proxy-based optimization — establishing that measuring resistance (not eliminating hacking) is the practically important question.",
  "landscape": "**Autoformalization RL systems:** FormaRL (COLM 2025) uses GRPO with binary compilation + LLM semantic consistency, achieving 26.15% pass@1 on ProofNet; ablation reveals aggressive gaming — syntax-only RL yields 100% compilation, 0% consistency. Mathesis (ICLR 2026) advances with R_ver + R_sem in GRPO plus HPO; 22% improvement on Gaokao-Formal. CriticLean (arXiv July 2025) trains CriticLeanGPT via SFT+GRPO: Qwen3-14B-RL achieves 84.8% (publicly available), Qwen3-8B-RL achieves 79.8% on CriticLeanBench. StepFun-Formalizer (AAAI 2026) achieves 40.5% BEq@1 SOTA on FormalMATH-Lite.\n\n**Faithfulness gaps in autoformalization:** Do LLMs Game Formalization? (arXiv:2604.19459) uses an outcome-based definition: 'formalization gaming is the subset of unfaithfulness where errors functionally enable proof compilation that faithful formalization would not have achieved.' Key findings: (a) NO systematic gaming in unified generation — 94-98% definite precision, models prefer abstention over forcing proofs; (b) In two-stage pipelines, GPT-5 fabricates axioms as 'reactive fallback' (107 cases, mixed across runs), DeepSeek-R1 mistranslates premises producing 'internally consistent outputs that evade detection entirely'; (c) High compilation rates create an 'illusion of correctness' — valid proofs do not guarantee faithful formalizations. LLMs Gaming Verifiers (ICLR 2026 Workshop) demonstrates RLVR models abandon reasoning for shortcuts.\n\n**Multi-objective GRPO weight adaptation (DENSE LANDSCAPE):** (1) MO-GRPO (arXiv:2509.22047): normalizes per-objective advantage A^MO_g = Σ_i [R_i - mean(R_i)]/std(R_i), ensuring equal variance contribution. Theoretically: affine-invariant, Corr(R_i, A^MO) = 1/√K under uncorrelated rewards. Tested on bandits, WMT, AlpacaFarm. (2) CTWA (arXiv:2602.06869, Lu & Jiang): derives local covariance law — objective m improves iff Cov(r_m, s) > 0 where s is the scalarized training signal. Adaptively upweights objectives whose covariance dips below target c*_m via exponential moving average and log-space update. Provides Polyak-Łojasiewicz convergence analysis. Most theoretically grounded of the group. Tested on Math500, MATH algebra with Qwen2.5, Qwen3, SmolLM2. Same authors as DRW. (3) DRW (TACL 2026, Lu & Jiang): hypervolume-guided and gradient-based dynamic weight adaptation for Pareto efficiency. Predecessor to CTWA. (4) Blockwise Advantage Estimation (arXiv:2602.10231): token-level objective assignment — partitions completions into blocks with per-block advantages. Complementary to weight adaptation (addresses credit assignment, not weighting). (5) TaRoS (arXiv:2511.19356): monitors Hoyer sparsity for reward saturation detection, downweights saturated components. Video generation domain. Closest to gaming-awareness via Goodhart's Law sensitivity. ALL five methods are objective-agnostic — none use domain-specific gaming detection.\n\n**Gaming-aware RL modifications:** Advantage Modification from 'When Reward Hacking Rebounds' (arXiv:2604.01476): integrates shortcut concept scores (via representation engineering from contrastive pairs) into GRPO advantage computation. Operates at REPRESENTATION level — requires probing hidden states, domain-specific contrastive pairs. SignCert-PO (arXiv:2604.02986): certified sign-preservation radius via adversarial RM perturbation, down-weights non-robust completions. Operates at ADVANTAGE level — requires RM weight access, single-RM settings.\n\n**General gaming detection:** GRIFT (arXiv:2604.16242): gradient fingerprints (LoRA adapters, K-means, ~80% F1). Heavyweight: per-sample gradient computation + manual cluster labeling. Exploitation-rate (arXiv:2605.12474): fraction of newly-credited criteria rejected by cross-family LLM panel (GPT-5.4, Gemini 3 Pro, Claude Opus 4.6). Expensive, LLM-dependent, vulnerable to correlated judge failures.\n\n**Theoretical foundations:** Correlated Proxies (arXiv:2403.03185, ICLR 2025 Spotlight): formalizes hacking via proxy-true correlation r; proves safe optimization bound parametrized by r and χ² divergence; regularization λ = σ√(1-r²). KEY for our theoretical contribution: GRS estimates r. Reward Hacking as Equilibrium (arXiv:2603.28063): hacking is structural under finite evaluation — any optimized agent under-invests in unevaluated dimensions. Reward Hacking survey (arXiv:2604.13602): four-level exploitation hierarchy (feature/representation/evaluator/environment), three-phase detection lifecycle, Proxy Compression Hypothesis unifying hacking as objective compression + optimization amplification + evaluator-policy co-adaptation. SpecBench (arXiv:2605.21384): hacking gap grows 28pp per 10× code size. On the Hidden Objective Biases of GRPO (arXiv:2601.05002): non-uniform group weighting, AdamW scaling insensitivity, momentum clipping violations.\n\n**Evaluation metrics for autoformalization:** GTED (AI4Math@ICML 2025): tree-edit-distance over operator trees from Lean Language Server — formally-grounded, no ATP/LLM dependency, highest accuracy (70.73%) and Kappa (0.438) on miniF2F. FormalAlign (ICLR 2025): dual contrastive+generation loss, 99.21% AS on FormL4-Basic. LeanScorer (Mathesis): subtask decomposition, Sugeno fuzzy integral, 0.92 F1. FormalRewardBench (arXiv:2605.10141): first benchmark for reward models in formal theorem proving with Lean 4 — specialized provers score 24.4% pairwise consistency, frontier LLMs 59.8%. Reveals generation-evaluation gap: proving ability does not transfer to evaluation ability.\n\n**The refined gap:** Autoformalization uniquely provides formally-grounded faithfulness measurement (GTED), enabling gaming-resistance analysis unavailable in other RL domains. Despite 5+ objective-agnostic adaptive methods and multiple gaming-aware RL modifications, no work: (a) systematically compares gaming resistance across isolated reward source categories for autoformalization; (b) proposes a gaming-resistance metric with formal theoretical grounding (sample complexity, connection to optimization bounds, contamination robustness); (c) evaluates whether domain-specific formally-grounded gaming detection outperforms general-purpose approaches.",
  "inspired_by": "The central insight: autoformalization is the IDEAL domain for studying gaming resistance because GTED provides a formally-grounded faithfulness anchor — enabling principled measurement that is provably connected to safe optimization bounds (via Correlated Proxies) and inherently more robust than LLM-based detection (via bounded influence functions). This insight emerges from the convergence of: (1) the theoretical result that reward hacking is structural (arXiv:2603.28063) and that proxies inevitably compress (PCH, arXiv:2604.13602), making resistance measurement the practical question; (2) GTED providing the formally-grounded anchor that enables principled measurement uniquely in autoformalization; (3) the Correlated Proxies framework (arXiv:2403.03185) providing the theoretical bridge — GRS estimates exactly the correlation parameter that determines safe optimization bounds; (4) the generation-evaluation gap (FormalRewardBench) showing that evaluation capability cannot be assumed from generation accuracy — gaming resistance must be measured, not inferred; (5) the proliferation of domain-agnostic methods creating demand for domain-specific evaluation. The gap between documented reward-faithfulness gaps (FormaRL ablation, VerifAI-2 pipeline findings) and the absence of formal gaming-resistance measurement for autoformalization is clear and actionable.",
  "approach": "We present the first formally-grounded gaming-resistance analysis for autoformalization RL. The central claim: GTED's formally-grounded faithfulness measurement uniquely enables a gaming-resistance metric (GRS) with formal theoretical guarantees — sample complexity bounds, provable robustness, and a direct connection to safe optimization bounds. The paper has three phases that progressively build on this claim.\n\n**Phase 1: Multi-Source Reward Signal Extraction (5 Categories)**\n\n(a) Formally-grounded signal R_formal: Using LeanInteract v0.11.3's Message objects (fields: start_pos, end_pos, data, severity ∈ {error, warning, info}), classify compiler diagnostics into error hierarchy via custom regex parser (~200 LoC) over Message.data strings: parse errors → name resolution → type errors → clean compilation. Yields R_formal ∈ {0.0, 0.25, 0.5, 0.75, 1.0} plus density bonus. NOTE: LeanInteract provides three severity levels; the five-level hierarchy is our custom classification, documented as engineering contribution.\n\n(b) Embedding similarity R_embed: cosine similarity between sentence embeddings of input NL and backtranslation of generated formal statement (reference-free roundtrip approach).\n\n(c) LLM judge R_judge: binary faithfulness judgment from frozen LLM (following FormaRL/Mathesis R_sem approach).\n\n(d) Trained critic R_critic: semantic fidelity score from CriticLeanGPT-Qwen3-14B-RL (84.8% accuracy, publicly available). First use as direct RL reward signal. Additionally retrain Qwen3-8B using CriticLean_4K dataset (~79.8% expected) to study critic accuracy impact on gaming resistance. FormalRewardBench's generation-evaluation gap motivates studying whether R_critic's gaming resistance differs from its normal-condition accuracy.\n\n**Phase 2: GRS (Gaming Resistance Score) Framework — Primary Methodological Contribution**\n\nGRS measures the meta-property of reward signals: how faithfully does high reward indicate genuine quality? Formally:\n\n  GRS(R, F) = τ(R(x), F(x)) over held-out evaluation set\n\nwhere τ is Kendall's rank correlation and F is a faithfulness anchor.\n\n**2a. Theoretical Foundation — Contamination Model:**\nUnder contamination model (1-α)P_faithful + αP_gamed, where P_gamed has reward above and faithfulness below the faithful population's medians, we prove: (i) GRS monotonically decreases in gaming proportion α; (ii) rank-based measures are provably more robust: per Croux & Dehon (2010), Spearman's ρ and Kendall's τ have bounded influence functions with finite gross-error sensitivity, while Pearson's r has unbounded influence proportional to outlier magnitude. Under 5-10% contamination (realistic for RL gaming), Kendall's τ achieves lowest MSE among all correlation measures (Xu et al., Signal Processing 2013).\n\n**2b. Sample Complexity Bounds (NEW):**\nSince Kendall's τ is a degree-2 U-statistic with kernel h((x₁,y₁),(x₂,y₂)) = sgn((x₂-x₁)(y₂-y₁)) bounded in [-1,1], Hoeffding's inequality for U-statistics gives:\n  P(|GRS_hat - GRS| > ε) ≤ 2 exp(-nε²/2)\nFor ε-precision with probability 1-δ: n ≥ 2log(2/δ)/ε². Concrete: for ε=0.1, δ=0.05, n ≥ 737 evaluation pairs suffice. Asymptotic CI width: 2·1.96·√((1-τ²)/n) for Kendall (Pohle et al., arXiv:2512.14609). Per Bonett & Wright (2000): n=75 per config yields CI half-width ≈ 0.12 for τ ≈ 0.7, adequate for distinguishing 'high' (>0.6) from 'moderate' (0.3-0.6) gaming resistance.\n\n**2c. Formal Connection to Correlated Proxies (NEW):**\nGRS estimates the correlation parameter r in the Correlated Proxies framework (arXiv:2403.03185, ICLR 2025 Spotlight). Theorem 5.1 of that framework gives:\n  [J(π,R) - J(π_base,R)]/σ_R ≥ (1/r)[proxy_gain/σ_proxy - √((1-r²)·χ²(μ_π||μ_base))]\nThe safe regularization strength is λ = σ_proxy·√(1-r²). Therefore:\n- A GRS confidence interval [τ_L, τ_U] translates to a regularization interval [σ·√(1-τ_U²), σ·√(1-τ_L²)]\n- Low GRS → high λ → more regularization needed; high GRS → low λ → safe to optimize aggressively\n- This formally bridges GRS measurement to optimization policy: GRS provides data-driven regularization calibration\n- The correlation breakdown under optimization that Correlated Proxies formalizes is exactly what GRS detects empirically\n\n**2d. GRS vs Exploitation-Rate: Complementary Detection Regimes (NEW):**\nWe prove GRS and exploitation-rate occupy complementary detection domains:\n- GRS: population-level monitoring, O(n log n) computation, bounded influence function, requires formally-grounded anchor\n- Exploitation-rate: per-instance classification, O(K·n) frontier model cost, vulnerable to correlated judge failures\n- GRS dominates when: (i) contamination fraction ε > 0.05, (ii) evaluator cost is constrained, (iii) judge diversity is limited, (iv) formally-grounded anchor is available\n- Exploitation-rate dominates for: per-instance flagging, domains lacking formal anchors\nAnalytical comparison using published results; no experimental reimplementation.\n\n**2e. Two GRS Formulations (main text):**\n  GRS-Kendall: concordance probability — handles ties, interpretable as pairwise comparison probability, direct U-statistic theory applies\n  GRS-Spearman: rank correlation — standard, well-understood, compared alongside Kendall\n  (GRS-Pearson and GRS-MI deferred to appendix)\n\n**2f. Multi-Faceted Faithfulness Anchors:**\n  GRS-GTED: F(x) = GTED tree-edit-distance (PRIMARY — formally-grounded, no LLM dependency)\n  GRS-LeanScorer: F(x) = LeanScorer Sugeno score (secondary)\n  GRS-roundtrip: F(x) = roundtrip consistency (tertiary)\n  GRS-human: F(x) = expert judgment (gold standard, 600 validation samples)\n\n**Phase 3: Systematic Ablation (8 Configurations)**\n  C1: Binary compilation only (FormaRL/Mathesis R_ver reproduction)\n  C2: Graded formal signal only (R_formal)\n  C3: Embedding similarity only (R_embed)\n  C4: LLM judge only (R_judge)\n  C5: Trained critic only (R_critic via CriticLeanGPT-14B-RL)\n  C6: Formal + embedding hybrid (R_formal + R_embed)\n  C7: Formal + trained critic hybrid (R_formal + R_critic)\n  C8: Full hybrid (R_formal + R_embed + R_critic)\n  Tiered model strategy: all 8 on Qwen2.5-Coder-7B-Instruct; top 4 by GRS on Qwen3-Coder-30B-A3B-Instruct.\n  Critic scaling sub-study: C5 with 14B (84.8%) vs 8B (~79.8%) on 7B model.\n\n**Phase 4: Adaptive Composition Demonstration (Lightweight, ~2 pages)**\n\nBrief demonstration that GRS can inform dynamic composition, tested on 7B with C8 component set:\n  D1: AGRC — w_k^(t+1) ∝ w_k^(t)·exp(η·GRS_k^(t)). Gaming-SPECIFIC: upweights gaming-resistant components based on per-component GRS-GTED, updated every K=500 steps.\n  D2: CTWA (arXiv:2602.06869) — monitors Cov(r_k, s) and upweights when covariance drops below target c*_k. Gaming-AGNOSTIC but signal-driven: targets interference regardless of cause. Primary comparison — mechanistically closest to AGRC.\n  D3: MO-GRPO (arXiv:2509.22047) — A^MO = Σ_i [R_i - mean(R_i)]/std(R_i). Gaming-AGNOSTIC and static: normalizes variance. Reference baseline.\n\nHypotheses: (H1) When gaming concentrates in specific components, AGRC selectively downweights while CTWA and MO-GRPO cannot discriminate gamed from non-gamed components. (H2) CTWA may match AGRC when gaming correlates with negative covariance (interference and gaming are aligned). Both outcomes are publishable and informative.\n\n**Phase 5: Evaluation Framework (6 Analyses)**\n\n(1) Standard metrics + automated faithfulness: BEq@1, pass@1, ASSESS structural similarity, GTED score, LeanScorer score, FormalAlign alignment, roundtrip consistency\n(2) GRS decomposition: GRS-Kendall and GRS-Spearman per configuration × checkpoint — the core analysis answering RQ1 and RQ2\n(3) GRS-human validation: 75 samples × 8 key config-model pairs = 600 stratified expert audits with bootstrap BCA CIs (10,000 resamples). Stratified by gaming severity (no/mild/severe). Per Bonett & Wright: n=75 yields CI half-width ≈ 0.12 for τ ≈ 0.7\n(4) GRS theoretical validation: empirical verification of sample complexity bounds (subsampling analysis), contamination robustness (synthetic contamination injection), and Correlated Proxies regularization interval accuracy\n(5) Critic scaling: GRS comparison for R_critic using 14B (84.8%) vs 8B (~79.8%). Connected to FormalRewardBench's generation-evaluation gap: does critic accuracy predict gaming resistance?\n(6) AGRC vs CTWA vs MO-GRPO demonstration: weight trajectories, GRS at convergence, Pareto analysis (GRS vs standard accuracy)\n\n**Research Questions:**\n  RQ1: Which reward signal categories exhibit highest gaming resistance in isolation? Do formally-grounded signals (C2) outperform semantic (C3, C4) and learned-critic (C5) signals? Does critic accuracy predict gaming resistance? (C5 14B vs 8B)\n  RQ2: Does hybrid composition (C6-C8) yield additive faithfulness gains while maintaining gaming resistance?\n  RQ3: Is GRS-GTED a reliable automated proxy for expert gaming assessment? (correlation, bootstrap CIs, sample complexity verification)\n  RQ4: Does gaming-specific adaptation (AGRC) outperform gaming-agnostic adaptation (CTWA, MO-GRPO) when domain-specific detection is available? (brief demonstration)\n\n**Training:** GRPO with KL penalty on Qwen2.5-Coder-7B-Instruct and Qwen3-Coder-30B-A3B-Instruct. Training on ProofNet + FormalMATH-Lite.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "1200 H100 (8 configs on 7B = 8×70 + top 4 on 30B = 4×70 + 3 demo configs on 7B = 3×70 + 80 grid search + 60 CriticLeanGPT inference + 60 evaluation)",
      "cpu_hours": "~35,000 CPU-hours on c7i.16xlarge for Lean compilation via Kimina Lean Server + GTED operator tree construction",
      "human_audit_hours": "~70 expert-hours for 600 stratified manual gaming audits (75 samples × 8 key config-model pairs) with bootstrap BCA validation",
      "timeline": "14-16 weeks (4 wks pipeline + GTED integration + GRS implementation + theoretical proofs + LeanInteract error parser, 5 wks RL training across configs, 1.5 wks demonstration configs (AGRC+CTWA+MO-GRPO), 4 wks evaluation/writing)",
      "estimated_gpu_cost": "$3,000 (at ~$2.50/hr H100 spot)",
      "estimated_cpu_cost": "$600-1,200 (c7i.16xlarge spot at ~$0.90/hr)"
    },
    "human_in_loop": {
      "gpu_hours": "1050 H100",
      "cpu_hours": "~30,000 CPU-hours",
      "human_audit_hours": "~55 expert-hours",
      "timeline": "12-14 weeks",
      "claude_api_cost": "$500",
      "estimated_gpu_cost": "$2,625",
      "estimated_cpu_cost": "$500-1,000"
    },
    "auto_research": {
      "gpu_hours": "1050 H100",
      "cpu_hours": "~30,000 CPU-hours",
      "human_audit_hours": "~45 expert-hours (automated pre-filtering via GRS-GTED reduces manual load to disagreement cases)",
      "timeline": "10-12 weeks",
      "claude_api_cost": "$700",
      "estimated_gpu_cost": "$2,625",
      "estimated_cpu_cost": "$500-1,000",
      "speed_bottleneck": "Lean compilation (~7s avg) and GTED operator tree construction (~2s per statement). With 120-180 parallel Lean instances, throughput matches GPU generation."
    }
  },
  "target_venues": [
    "ICLR 2027 (abstract Sep 19, paper Sep 24, 2026 [estimated]) — PRIMARY, ~17 weeks available. Analysis paper framing (GRS + systematic ablation primary, AGRC demonstration secondary) fits ICLR's preference for principled analysis with clear contributions. Tighter scope makes clean narrative feasible.",
    "EACL 2027 (ARR Aug 3, 2026 → Oct 11 commitment) — SECONDARY, ~10 weeks for ARR submission. 7B full ablation + GRS framework + theoretical analysis feasible; 30B scaling and demonstration deferred to camera-ready.",
    "NAACL 2027 (ARR Oct 12, 2026 → commitment ~Oct 16 [estimated]) — TERTIARY CONTINGENCY. Full experiment set including 30B scaling and complete demonstration.",
    "ACL 2027 (ARR ~Feb 16, 2027 [estimated]) — SAFE FALLBACK. Complete experimental set with all supplementary analyses."
  ],
  "level": "solid+",
  "key_references": [
    "FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)",
    "Mathesis: Towards Formal Theorem Proving from Natural Languages (ICLR 2026)",
    "Online Reinforcement Learning for Autoformalization (MAR Workshop @ NeurIPS 2025)",
    "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion (AAAI 2026)",
    "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv July 2025)",
    "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv:2604.19459)",
    "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (ICLR 2026 Workshop)",
    "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems (arXiv:2509.22047, Sep 2025)",
    "Uncovering Cross-Objective Interference in Multi-Objective Alignment [CTWA] (arXiv:2602.06869, Feb 2026)",
    "Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting [DRW] (TACL 2026)",
    "On the Hidden Objective Biases of Group-based Reinforcement Learning (arXiv:2601.05002, Jan 2026)",
    "Blockwise Advantage Estimation for Multi-Objective Alignment (arXiv:2602.10231, Feb 2026)",
    "Rethinking Reward Signals in Video GRPO: When Scores Become Targets [TaRoS] (arXiv:2511.19356)",
    "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals (arXiv:2604.01476, April 2026)",
    "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness [SignCert-PO] (arXiv:2604.02986, April 2026)",
    "Reward Hacking as Equilibrium under Finite Evaluation (arXiv:2603.28063, March 2026)",
    "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges [Survey] (arXiv:2604.13602, April 2026)",
    "Detecting and Suppressing Reward Hacking with Gradient Fingerprints [GRIFT] (arXiv:2604.16242, April 2026)",
    "Reward Hacking in Rubric-Based Reinforcement Learning [Exploitation-rate] (arXiv:2605.12474, May 2026)",
    "FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models (arXiv:2605.10141, May 2026)",
    "Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking (arXiv:2403.03185, ICLR 2025 Spotlight)",
    "Reward Hacking Mitigation using Verifiable Composite Rewards (arXiv:2509.15557, ACM-BCB 2025)",
    "SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents (arXiv:2605.21384, May 2026)",
    "Generalized Tree Edit Distance (GTED): A Faithful Evaluation Metric for Statement Autoformalization (AI4Math @ ICML 2025)",
    "FormalAlign: Automated Alignment Evaluation for Autoformalization (ICLR 2025)",
    "Monotonic Reference-Free Refinement for Autoformalization (arXiv January 2026)",
    "Process-Verified Reinforcement Learning for Theorem Proving via Lean (NeurIPS 2025)",
    "Process-Driven Autoformalization in Lean 4 (arXiv 2024)",
    "Training Step-Level Reasoning Verifiers with Formal Verification Tools [FOVER] (ACL 2026 Findings)",
    "ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity (arXiv 2025)",
    "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)",
    "Faithful Autoformalization via Roundtrip Verification and Repair (arXiv April 2026)",
    "FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)",
    "Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)",
    "Sample Size Requirements for Estimating Pearson, Kendall and Spearman Correlations (Bonett & Wright, Psychometrika 2000)",
    "Influence functions of the Spearman and Kendall correlation measures (Croux & Dehon, Statistical Methods & Applications 2010)",
    "A comparative analysis of Spearman's rho and Kendall's tau in normal and contaminated normal models (Xu et al., Signal Processing 2013)",
    "A class of statistics with asymptotically normal distribution (Hoeffding, Annals of Mathematical Statistics 1948)",
    "Asymptotic Inference for Rank Correlations (Pohle, Wermuth & Weiss, arXiv:2512.14609)"
  ],
  "description": "Reward hacking in autoformalization is a documented concern — FormaRL's ablation shows syntax-only RL achieves 100% compilation but 0% semantic consistency, and VerifAI-2 (arXiv:2604.19459) reveals that high compilation rates in neuro-symbolic pipelines create an 'illusion of correctness' even when unified generation shows no systematic gaming. Yet we lack answers to a basic question: which reward signals maintain faithfulness under optimization pressure? This paper provides the first systematic answer, exploiting a capability unique to autoformalization: formally-grounded, LLM-independent faithfulness measurement via GTED tree-edit-distance.\n\nOur central insight is that autoformalization is uniquely positioned for principled gaming-resistance analysis. Unlike code generation (where test-based evaluation lacks formally-grounded semantic metrics) or general RLHF (where ground truth is subjective), autoformalization offers GTED — a computable faithfulness anchor derived from the Lean language server's operator trees. We show this anchor enables a gaming-resistance metric with formal theoretical guarantees unavailable to domain-agnostic approaches.\n\nWe contribute three advances.\n\n**First (primary contribution)**, the GRS (Gaming Resistance Score) framework with deep theoretical grounding. GRS measures rank correlation between reward signals and GTED-anchored faithfulness. Beyond the basic definition, we provide: (a) sample complexity bounds via Hoeffding's inequality for U-statistics — n ≥ 2log(2/δ)/ε² evaluation pairs suffice for ε-precision with probability 1-δ; (b) a formal connection to the Correlated Proxies framework (ICLR 2025 Spotlight): GRS estimates the correlation parameter r that determines safe optimization bounds, translating a GRS confidence interval directly into a regularization interval λ ∈ [σ√(1-τ_U²), σ√(1-τ_L²)]; (c) provable contamination robustness via bounded influence functions (Croux & Dehon 2010) — under realistic gaming contamination (5-10%), rank-based GRS maintains bounded bias while parametric alternatives degrade; (d) a complementarity analysis showing GRS dominates exploitation-rate for population-level monitoring while exploitation-rate dominates for per-instance flagging. We validate GRS against 600 expert-annotated samples with bootstrap BCA confidence intervals.\n\n**Second (systematic analysis)**, the first comparison of gaming resistance across five isolated reward source categories for autoformalization RL: binary compilation, graded formal (via custom error-hierarchy classification over LeanInteract v0.11.3 diagnostics), embedding similarity, LLM judge, and trained critic (CriticLeanGPT-Qwen3-14B-RL at 84.8% — first use as direct RL reward). Our 8-configuration GRPO ablation on Qwen2.5-Coder-7B-Instruct and Qwen3-Coder-30B-A3B-Instruct isolates individual signal contributions, answering which signals to trust. FormalRewardBench's (arXiv:2605.10141) finding that specialized provers are poor evaluators motivates our sub-study of whether critic accuracy (14B vs 8B) predicts gaming resistance.\n\n**Third (lightweight demonstration)**, we briefly show that GRS can inform adaptive reward composition via AGRC (gaming-aware dynamic reweighting using per-component GRS). We compare against CTWA (arXiv:2602.06869) — the most theoretically grounded objective-agnostic adaptive method, which monitors covariance between rewards and training signal — and MO-GRPO (arXiv:2509.22047), testing whether gaming-specific signals outperform gaming-agnostic adaptation. We position this in a dense landscape of 5+ objective-agnostic adaptive methods (MO-GRPO, CTWA, DRW, BAE, TaRoS), honestly noting AGRC's mechanism is a demonstration of GRS's utility, not a primary methodological contribution.\n\nThe paper adopts VerifAI-2's outcome-based gaming definition: reward inflation without corresponding faithfulness improvement, requiring no intent attribution. It is designed for outcome robustness: if formally-grounded signals dominate, we advance reward design; if signals are equivalent, we establish cost-effectiveness; if CTWA matches AGRC, we demonstrate that gaming-specific detection is unnecessary (a useful negative result). Regardless, the GRS framework with its theoretical guarantees and the systematic gaming-resistance analysis are independent contributions. Targeting ICLR 2027 (Sep 24 estimated deadline), with EACL 2027, NAACL 2027, and ACL 2027 as contingency venues.",
  "project_name": "reward_comp_autoform",
  "source": "web_research"
}
```

---

## Summary of Changes (Round 7 — Major Revision)

### Strategic Reframe
The core change is **demoting AGRC from co-primary contribution to lightweight demonstration** and **elevating GRS with deep theory as the star**. The reviewer correctly identified that with 5+ objective-agnostic adaptive methods (MO-GRPO, CTWA, DRW, BAE, TaRoS), AGRC narrows to "plugging GRS into the reweighting paradigm." The real novelty is GRS itself and the systematic analysis.

### Issues Addressed

| Issue | Resolution |
|-------|-----------|
| **CTWA missing** | Added with full mechanism (covariance law, PL convergence). Replaces MO-GRPO as primary adaptive comparison — mechanistically closer to AGRC. |
| **FormalRewardBench missing** | Cited for generation-evaluation gap. Motivates critic scaling sub-study (does accuracy predict gaming resistance?). |
| **Reward Hacking survey missing** | Cited for PCH framework as theoretical motivation. |
| **VerifAI-2 imprecision** | Corrected: "no systematic gaming in unified generation" (94-98% precision); fabrication/mistranslation in two-stage pipelines. Adopted outcome-based gaming definition. |
| **Crowded landscape** | Explicitly acknowledges 5+ methods. Honest about AGRC's limited novelty → demotion. |
| **Scope too dense** | 8 main configs + 3 demo configs; 6 evaluation analyses (down from 8); 4 RQs (down from 5). |
| **GRS novelty insufficient** | Deepened with: (a) sample complexity bounds (Hoeffding for U-statistics), (b) Correlated Proxies connection (GRS → regularization interval), (c) influence function robustness proof, (d) complementarity analysis vs exploitation-rate. |

### What breaks the scoring plateau
The previous rounds kept adding breadth (more baselines, more citations). This round adds **depth** — GRS now has formal sample complexity bounds, a provable connection to optimization theory via Correlated Proxies, and contamination robustness guarantees. This elevates it from "applying a known statistic" to a substantive methodological contribution with theoretical grounding.

Sources:
- [CTWA - Uncovering Cross-Objective Interference in Multi-Objective Alignment](https://arxiv.org/abs/2602.06869)
- [TaRoS - Rethinking Reward Signals in Video GRPO](https://arxiv.org/abs/2511.19356)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3633fe10-fee6-4fb9-9ec9-741efb8a3b80",
  "isSidechain": false,
  "requestId": "req_011CbTqye1Tc37CeERkoSGM1",
  "type": "assistant",
  "uuid": "764fe47e-9903-4fe7-a079-e9a348a6f559",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VbXdvuChYidYFf7kDi6Dy3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1809,
      "cache_read_input_tokens": 50460,
      "output_tokens": 13587,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13587,
          "cache_read_input_tokens": 50460,
          "cache_creation_input_tokens": 1809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1809
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"MAJOR NARRATIVE RESTRUCTURING: Reframed entire proposal a…",
  "leafUuid": "764fe47e-9903-4fe7-a079-e9a348a6f559",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gaming-resistant reward composition for autoformalization",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"MAJOR NARRATIVE RESTRUCTURING: Reframed entire proposal a…",
  "leafUuid": "764fe47e-9903-4fe7-a079-e9a348a6f559",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gaming-resistant reward composition for autoformalization",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51"
}
```

---
