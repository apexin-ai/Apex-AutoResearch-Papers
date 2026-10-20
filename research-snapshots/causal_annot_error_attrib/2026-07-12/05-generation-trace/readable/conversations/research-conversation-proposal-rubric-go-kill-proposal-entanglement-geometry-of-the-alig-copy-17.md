# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Entanglement Geometry of the Alig

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/0dfc5970-8988-49d4-b50a-c17e1afa7947.jsonl`
- **Structured JSON:** [`5d7715321cdf9ff2a47a.json`](../../sessions/5d/5d7715321cdf9ff2a47a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:40:33.589Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:40:33.589Z",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Entanglement Geometry of the Alignment Tax Across Dense and MoE Architectures in Agentic Tool-Use Settings\n\n## Description\n\nThe alignment tax has been formalized geometrically with elliptic Pareto frontiers parameterized by the principal angle α between safety and capability subspaces (arXiv 2603.00047). But empirically, these subspaces are highly entangled (MSO, ICLR 2026), MoE architectures route safety through sparse expert dynamics, and in agentic settings Plaut (arXiv 2603.02229) observes a near-linear frontier (R²=0.77) without geometric explanation. We hypothesize: high entanglement yields small α, degenerating the ellipse toward linearity, while MoE routing introduces discrete dynamics that violate the framework's continuous-subspace assumptions. We produce three contributions. (C1) The first empirical bridge between two independent metric systems — MSO (parameter-space entanglement, ICLR 2026) and principal angle α (activation-space geometry) — establishing their cross-space correspondence via layer-wise mixed-effects analysis; this determines whether parameter-space interventions (NSPO arXiv 2512.11391, OGPSA arXiv 2602.07892) and activation-space diagnostics operate on compatible foundations, and provides initial evidence for probing-based alignment tax prediction without full DPO sweeps. (C2) A diagnostic dual-estimation test with pre-registered outcome topology: α_repr–α_frontier agreement validates geometric theory under entanglement, while systematic divergence quantifies the linear representation hypothesis's failure boundary; a 2×2 outcome matrix ({dense,MoE} × {chat,agent}) pre-registers interpretations for every divergence pattern, making the paper informative under any result. (C3) MoE as a stress test of continuous-subspace geometry: if safety is routing-mediated (RASA, arXiv 2602.04448), activation-space α may fail to capture MoE safety structure, and α_repr–α_frontier divergence should be larger in MoE than dense models. Using a 2×2 design — {Qwen3-32B, Gemma 4 31B} (dense) × {Qwen3-235B-A22B, Llama-4-Maverick} (MoE) in {chat, agent} — we sweep 16 LoRA-DPO β values per condition with Bayesian model comparison (PSIS-LOO + WAIC) and meta-analytic agreement testing. Expected: (1) higher MSO in agents vs. chat; (2) α_repr ≈ α_frontier in dense models, both smaller in agents (explaining Plaut's frontier as a low-angle ellipse); (3) larger α_repr–α_frontier divergence in MoE than dense, quantifying routing-mediated geometry violation; (4) layer-wise MSO–α_repr correspondence establishing whether parameter-space and activation-space analyses are compatible paradigms.\n\n## Core Problem\n\nThe alignment tax has been formalized geometrically under the linear representation hypothesis, yielding elliptic Pareto frontiers parameterized by the principal angle α between safety and capability subspaces (arXiv 2603.00047). Three empirical challenges prevent direct application. (1) Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185, ICLR 2026) shows safety and capability subspaces are highly entangled, with MSO strongest between useful and safety-specific updates — but MSO operates in parameter space (SVD of weight difference matrices) while α operates in activation space (cross-covariance of activation vectors). These two metric systems have never been connected, creating a measurement schism: the alignment community simultaneously uses parameter-space interventions (null-space gradient projection) and activation-space diagnostics (probing, geometric theory) without knowing if they analyze the same underlying structure. (2) Frontier models are predominantly MoE architectures where safety is governed by sparse expert routing (RASA arXiv 2602.04448, SAFEx arXiv 2506.17368, Sparse Models Sparse Safety arXiv 2602.08621), not global activation subspaces — making the continuous-subspace geometric framework's applicability non-trivial. (3) In agentic tool-use settings, both challenges intensify: text safety does not transfer to tool-call safety (Mind the GAP, arXiv 2602.16943), and the safe controller mapping has inherently higher Lipschitz complexity (Why Does Agentic Safety Fail to Generalize, arXiv 2605.06992). Plaut (arXiv 2603.02229) measured an approximately linear Pareto frontier (R²=0.77, slope −0.83) in agentic DPO on 8B–14B models — but with only two β values, no representation analysis, and no MoE comparison. The geometric framework's author explicitly notes it fails \"for large perturbations, the KL is not quadratic, the representation geometry shifts\" — but this failure boundary has never been quantified.\n\n## Opportunity\n\nFour independent lines of work create a convergence point whose bridges are missing. The Geometry of the Alignment Tax (arXiv 2603.00047, Mar 2026) provides the formal apparatus — principal angles, elliptic Pareto frontiers, tax rate decomposition — but assumes linear separability, static representations, and dense architectures. Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185, ICLR 2026) proves the separability assumption fails via MSO in parameter space, but only in chat on models up to 7B — and operates in a different mathematical space than the geometric theory. The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025) reveals multi-dimensional orthogonal safety directions in activation space, but only in chat on Llama 3 8B. Plaut (arXiv 2603.02229, Mar 2026) discovers a near-linear agentic Pareto frontier, which the geometric theory predicts when α is small — but used only 8B–14B dense models with 2 β values and no representation analysis. The MoE safety literature (RASA arXiv 2602.04448, SAFEx arXiv 2506.17368, Sparse Models Sparse Safety arXiv 2602.08621) establishes that safety operates through routing dynamics — safety-critical experts, routing distribution divergence, expert silencing — meaning MoE safety is fundamentally routing-mediated and may not be capturable by continuous activation-space geometry. This makes MoE a stress test of the geometric framework's foundations. The null-space projection literature (NSPO arXiv 2512.11391, ICLR 2026; OGPSA arXiv 2602.07892) mitigates the tax by projecting safety gradients into capability null spaces — but in parameter space, assuming separable subspaces. If MSO and α_repr do not correspond, then parameter-space interventions and activation-space theory may be analyzing different structures, with direct consequences for intervention design. LoRA rank=1 achieves optimal reasoning-safety tradeoff (arXiv 2507.17075), suggesting safety alignment is intrinsically low-rank and representation probing may suffice to capture relevant structure. AQI (arXiv 2506.13901, EMNLP 2025) demonstrates that latent geometry — cluster divergence metrics applied to safe/unsafe activations — can diagnose alignment quality without generation, validating the general approach of representation-based alignment diagnosis; our work differs by using principal angles (geometric structure parameterizing the Pareto frontier) rather than cluster quality metrics (scalar diagnostic), and by connecting to cross-space correspondence, architecture-specific analysis, and frontier shape prediction.\n\n## Landscape\n\nThe Geometry of the Alignment Tax (arXiv 2603.00047, Mar 2026) proves the Pareto frontier is an ellipse ΔS = ΔC cos α + sin α √(B² − ΔC²) parameterized by the principal angle α, but is purely theoretical with no empirical validation and acknowledges failure under large perturbations or nonlinear encoding. Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185, ICLR 2026) introduces MSO quantifying safety-capability entanglement via SVD overlap matrices; strongest overlap is between useful and safety updates on Llama 2/3.2 and Qwen 2.5 (1B–7B) — chat only, parameter space only, with layer-specific analysis at 70-85 percentile depth. The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025) reveals multi-dimensional orthogonal safety directions with a dominant refusal direction plus interpretable secondary features — chat only, Llama 3 8B, activation space. Safety Training Persists Through Helpfulness Optimization (arXiv 2603.02229, Mar 2026, Plaut) finds an approximately linear Pareto frontier (R²=0.77, slope −0.83) across 180 DPO configurations on Llama 3.1 8B, Qwen 2.5 7B, and Phi 4 14B using ToolEmu (144 tasks); uses only β ∈ {0.05, 0.1}, no representation analysis, no MoE — frontier shape observed but not geometrically explained. The Viscosity of Logic (arXiv 2601.17260, Jan 2026) sweeps DPO β on Mistral-7B and identifies phase transitions at discrete β values near 10⁻², demonstrating that systematic β sweeping reveals nonlinear regime transitions, motivating dense sampling in high-gradient regions. LoRA is All You Need for Safety Alignment of Reasoning LLMs (arXiv 2507.17075) finds rank=1 LoRA achieves optimal reasoning-safety tradeoff, suggesting safety alignment is intrinsically low-rank. AQI (arXiv 2506.13901, EMNLP 2025) uses latent geometry — Xie-Beni, Calinski-Harabasz, Davies-Bouldin, Dunn indices on safe/unsafe activation clusters — to diagnose alignment quality without generation; differs from our approach in using cluster divergence (scalar quality indicator) vs. principal angles (geometric structure parameterizing Pareto frontier shape), and does not address agent/MoE settings or cross-space correspondence. NSPO (arXiv 2512.11391, ICLR 2026) projects safety gradients into the null space of the capability covariance matrix KK⊤ — but assumes separable subspaces. OGPSA (arXiv 2602.07892, Feb 2026) similarly projects safety gradients onto the orthogonal complement of a capability subspace. Can LLM Safety Be Ensured by Constraining Parameter Regions? (arXiv 2602.17696) shows safety regions are dataset-dependent with low IoU. The Geometry of Alignment Collapse (arXiv 2602.15799) shows alignment concentrates in low-dimensional subspaces with sharp curvature. ShaPO (arXiv 2602.07340) enforces geometry-aware preference optimization via selective geometry control. Sparse Crosscoders (arXiv 2603.05805) provides methods for comparing MoE and dense model representations at small scale, finding MoEs learn fewer but more specific features. The Autonomy Tax (Mar 2026) shows 99% timeout rates from agent safety training. Mind the GAP (arXiv 2602.16943, Feb 2026) demonstrates text-tool safety divergence across 17,420 datapoints. Why Does Agentic Safety Fail to Generalize (arXiv 2605.06992, May 2026) proves the safe controller has higher Lipschitz constant than task execution. RASA (arXiv 2602.04448, Feb 2026) identifies safety-critical experts via Adversarial Activation Discrepancy and shows full-parameter MoE safety fine-tuning creates routing shortcuts — restoring original routing collapses harmlessness by Δ ∈ [−0.38, −0.46]. SAFEx (arXiv 2506.17368) shows disabling 12 of 6,144 experts drops refusal rate 22%. Sparse Models Sparse Safety (arXiv 2602.08621, Feb 2026) introduces RoSais scores: masking 5 routers increases ASR 4× to 0.79. Geometric Routing (arXiv 2604.14434, Apr 2026) demonstrates monosemantic experts with frequency-to-syntax gradient. Grassmannian MoE (arXiv 2602.17798, Feb 2026) provides subspace-manifold routing. Fundamental Safety-Capability Trade-offs (arXiv 2503.20807, PNAS Nexus 2026) characterizes theoretical tradeoff limits. The Verifier Tax (Mar 2026) and Steering Externalities (Feb 2026) provide further agentic alignment tax evidence. When Safety Geometry Collapses (arXiv 2605.02914, May 2026) demonstrates safety geometry destruction in guard models. The Causal Impact of Tool Affordance (arXiv 2603.20320, Mar 2026) confirms sharp safety degradation in tool-enabled agents. ATBench (arXiv 2604.02022, Apr 2026) provides paired safe/unsafe trajectory construction with 1,000 trajectories across 1,954 tools. OpenAgentSafety (ICLR 2026) provides 350+ executable tasks with rule-based evaluators. Multi-Agent Security Tax (arXiv 2025) documents safety costs in multi-agent settings. No existing work connects parameter-space MSO to activation-space principal angles, measures alignment tax geometry under entanglement-aware metrics in agentic settings, provides geometric explanation for the observed near-linear frontier in agents, or tests the geometric framework's applicability to MoE routing-mediated safety.\n\n## Approach\n\nWe conduct the first entanglement-aware, architecture-controlled measurement of alignment tax geometry in agentic tool-use settings, using a 2×2 factorial design: {dense, MoE} × {chat, agent}. Three core contributions: (C1) cross-space metric bridge with metrological implications, (C2) diagnostic dual-estimation test with pre-registered outcome topology, (C3) MoE stress test of geometric framework.\n\n**Model Selection (2 dense + 2 MoE):**\n- Dense: Qwen3-32B (32.8B active, Qwen3 family), Gemma 4 31B (31B, Apache 2.0)\n- MoE: Qwen3-235B-A22B (22B active / 235B total, Qwen3 family), Llama-4-Maverick (17B active / 400B total)\n\nThe Qwen3 dense/MoE pair enables within-family comparison (same training data, tokenizer) — this is the primary apples-to-apples comparison. The cross-family pair (Gemma/Maverick) provides generalizability signal. Active parameter counts differ between dense and MoE (32.8B vs. 22B for Qwen3; 31B vs. 17B cross-family); addressed via FLOP-normalized analysis. Maverick contingency: if DPO memory requirements prove prohibitive (400B total requires reference offloading for DPO), fallback to Qwen3-30B-A3B (30B total / 3.3B active, Qwen3 family), which provides an MoE sparsity gradient (22B vs. 3.3B active) within the same model family.\n\n**Priority tiers:** Tier 1 (must-have): Qwen3-32B + Qwen3-235B-A22B × 2 settings × 16 β = 64 runs. Tier 2 (high-priority): Gemma 4 31B × 2 settings × 16 β = 32 runs. Tier 3 (contingent on resources): Maverick (or fallback) × 2 settings × 16 β = 32 runs.\n\n**Phase 1: Entanglement Geometry & Cross-Space Metric Bridge (wk 1–6)**\n\n*Infrastructure Validation (wk 1–2):* End-to-end pipeline verification on 1–2 β values per model: confirm QLoRA/LoRA-DPO training, activation extraction, evaluation pipeline (tau2-bench, OpenAgentSafety, ATBench, AdvBench). For Maverick, validate reference offloading feasibility; if infeasible, trigger fallback to Qwen3-30B-A3B.\n\n*Trajectory Construction:*\nAgent settings: paired safe/unsafe trajectories from (i) OpenAgentSafety's (ICLR 2026) 350+ executable tasks with rule-based safety evaluators across 8 risk categories; (ii) ATBench's (arXiv 2604.02022) planner-based paired trajectory synthesis with 1,000 trajectories across 1,954 tools. Capability subspace: tau2-bench policy-adherence tasks, activations from successful vs. failed completions. Activations extracted at tool-call decision points following LLM Reasoning as Trajectories (arXiv 2604.05655). Chat baseline: AdvBench/BeaverTails prompts matching the original MSO paper's methodology.\n\n*Entanglement Metrics:*\n(a) Mode Subspace Overlap (MSO): following Safety Subspaces are Not Linearly Distinct (ICLR 2026), computed via SVD overlap matrices. Sensitivity ablation over subspace rank K ∈ {5, 10, 20, 50, 100}.\n(b) Multi-dimensional safety decomposition: following Hidden Dimensions (ICML 2025), identifying dominant refusal direction and orthogonal secondary directions.\n(c) Principal angles via SVD on cross-covariance matrices of activation vectors, yielding α_repr. Spectrum of first 10 principal angles reported (not just leading angle). Layer-wise profiles computed per layer.\n\n*Cross-Space Correspondence (C1) with Metrological Implications:*\nWe test the empirical relationship between MSO (parameter space) and α_repr (activation space) at layer-wise granularity: for each model × setting condition, compute both MSO and α_repr at each layer in the middle-third depth range (~10–15 layers per model), yielding ~80–100 (MSO_layer, α_repr_layer) data points total. Analyze via linear mixed-effects model with MSO_layer as predictor, α_repr_layer as response, and random intercept per model-setting condition. This resolves the statistical power limitation of condition-level analysis (n=8) while respecting the nested structure. The correspondence is non-trivial: weight-space overlap may manifest as activation-space masking, amplification, or rank change without angle reduction. Results determine whether parameter-space interventions (NSPO, OGPSA) and activation-space diagnostics operate on compatible foundations — if MSO and α_repr do not correspond, these two analysis paradigms are not interchangeable, directly impacting alignment intervention design.\n\n*Probing-Based Prediction (C1 application):*\nRegression of condition-level representation measurements (MSO, α_repr, effective rank, routing divergence for MoE) against α_frontier and downstream safety metrics. If predictive, this provides initial evidence that alignment tax severity can be estimated from representation probing (~25 GPU-hr per model) without full DPO sweeps (~80+ GPU-hr per model), addressing the open question posed by the Geometry of the Alignment Tax author.\n\n*Trajectory Construction Sensitivity Ablation:*\n(i) Data source ablation: MSO and α_repr from OpenAgentSafety-only vs. ATBench-only vs. combined. (ii) Token position ablation: extraction at (a) tool-call decision points (default), (b) last token of each agent step, (c) mean-pooling over all step tokens.\n\n**Phase 2: Architecture-Aware MoE Routing Analysis (wk 4–7, overlapping)**\nFor MoE models, three-level decomposition:\n(a) Shared attention layers: analogous to dense-model analysis, providing controlled comparison.\n(b) Per-expert FFN subspaces: safety-critical experts identified via Adversarial Activation Discrepancy (RASA, arXiv 2602.04448). Per-expert α_repr and MSO computed to test whether safety is concentrated in specific experts or distributed.\n(c) Router weight space: routing distribution divergence (KL) between safe/unsafe inputs; RoSais-style router safety importance scoring (Sparse Models Sparse Safety, arXiv 2602.08621).\n\nSupplementary/exploratory: Sparse Crosscoders (arXiv 2603.05805) for feature organization comparison, contingent on scaling feasibility at 30B+ scale (original validation at 5-layer models only). Core MoE conclusions do not depend on crosscoder results.\n\n**Phase 3: Pareto Frontier Mapping & Diagnostic Dual-Estimation Test (wk 6–12)**\n\n*Evaluation Axes:*\n- Safety axis: OpenAgentSafety safety score (agent); AdvBench refusal rate + BeaverTails safety score (chat). Cross-setting control: all agent-trained models also evaluated on AdvBench (shared safety metric across settings).\n- Capability axis: tau2-bench task success rate + OpenAgentSafety task completion rate (agent); MMLU (5-shot) + GSM8K (8-shot) (chat). Pareto frontiers reported per capability metric to verify shape robustness.\n- Within-setting comparison (same evaluation protocol, varying architecture/model) is the primary analysis. Cross-setting comparison (agent vs. chat α) is secondary/suggestive, with metric-induced confounds explicitly discussed.\n\n*Training Protocol:*\n- Primary: LoRA-DPO on all layers, LoRA rank matched on total trainable parameters across architectures.\n- Secondary matching: per-token active trainable parameters (MoE LoRA rank increased to compensate for expert sparsity), testing whether matching strategy affects frontier shape conclusions.\n- MoE-specific ablation: (i) shared-attention-only LoRA, (ii) active-expert-only LoRA (HELLoRA-style). These ablations also serve to address the parameter-matching confound by isolating which model components drive frontier shape.\n- FLOP-normalized analysis: per-model training/inference FLOPs reported; FLOP-normalized Pareto frontiers provided alongside parameter-matched frontiers.\n\n*β Sweep:*\n16 LoRA-DPO β values per model/setting (β ∈ {0.003, 0.005, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.15, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0}), with increased density in the high-gradient region. If pre-study power simulation indicates n=16 insufficient for α < 15° discrimination, increase to 24 β points for Tier 1 models (offset by reducing Tier 3 scope). Phase transitions at discrete β values (The Viscosity of Logic, arXiv 2601.17260) motivate the dense sampling.\n\n*Statistical Approach:*\nBayesian model comparison using PSIS-LOO (Vehtari, Gelman & Gabry, 2017; preferred for small-sample robustness) and WAIC for three frontier models: (i) elliptic (α, B), (ii) linear (slope, intercept), (iii) piecewise-linear. Report ΔELPD ± SE(ΔELPD); if |ΔELPD| < SE, honestly reported as inconclusive. Pre-study power simulation: synthetic frontiers at α ∈ {5°, 10°, 15°, 20°, 45°} with realistic noise, testing PSIS-LOO discrimination at n=16 and n=24. Leave-one-out sensitivity: checking whether removing any single β point changes model ranking. Supplementary: local curvature analysis (second-order finite differences along the frontier) to detect deviation from linearity even when global shape discrimination is inconclusive.\n\n*Small-α Fallback:* If most conditions yield α < 10° and PSIS-LOO is inconclusive for elliptic vs. linear, C2's contribution reframes as \"quantifying α's upper bound\" — empirically demonstrating that entanglement is sufficient to collapse the frontier to near-linearity (α < X° with 95% credible interval), which itself validates the geometric theory's prediction that high entanglement linearizes the tax.\n\n*Diagnostic Dual-Estimation Test (C2) with Outcome Topology:*\nα_repr (Phase 1) vs. α_frontier (elliptic fit) compared via random-effects meta-analysis: compute (α_repr − α_frontier) for each of the 8 conditions (with uncertainty from bootstrap for α_repr and posterior for α_frontier), fit random-effects model testing whether the population mean difference deviates from 0. This replaces arbitrary counting thresholds with a formal statistical test of systematic divergence.\n\nPre-registered outcome topology — the 2×2 structure ({dense, MoE} × {chat, agent}) yields four interpretive patterns:\n- Dense agree + MoE diverge → routing violates continuous-subspace assumption (C3 confirmed); activation-space geometry remains valid for dense models but breaks for MoE\n- Chat agree + agent diverge → agentic complexity exceeds linear representation assumption; standard geometric framework applies in chat but not in tool-use settings\n- Both diverge → geometric framework fundamentally inadequate under real entanglement levels; the linear representation hypothesis is a poor approximation for safety-capability geometry\n- Both agree → framework is surprisingly robust despite entanglement; principal angle theory extends beyond its stated assumptions\n\nEach pattern has distinct consequences for alignment intervention design (parameter-space projection vs. routing-aware methods vs. setting-specific approaches), ensuring the paper produces actionable findings regardless of outcome.\n\n**Scope note:** We exclude intervention phases (entanglement-adapted OGPSA or NSPO). We focus on rigorous measurement and geometric explanation.\n\n## Resource Estimate\n\n**GPU hours (distinguishing wall-clock from GPU-hours):**\n- Infrastructure validation (wk 1–2): ~100 GPU-hr (1–2 β × 4 models × 2 settings, quick runs)\n- Phase 1 activation extraction: 4 models × 2 settings × ~25 hr on 4–8×H100 ≈ 400–600 GPU-hr\n- Phase 2 MoE routing analysis: 2 models × 60 hr on 8×H100 ≈ 960 GPU-hr\n- Phase 3 Tier 1 sweep (Qwen3 pair): 2 models × 2 settings × 16 β × ~5 hr on 4×H100 (dense) / 4–8×H100 (MoE QLoRA) ≈ 640–1,280 GPU-hr\n- Phase 3 Tier 2 sweep (Gemma): 1 model × 2 settings × 16 β × ~5 hr on 4×H100 ≈ 640 GPU-hr\n- Phase 3 Tier 3 sweep (Maverick/fallback): 1 model × 2 settings × 16 β × ~5 hr on 8×H100 (with ref offloading) ≈ 1,280 GPU-hr\n- Phase 3 MoE ablation: 2 models × 2 settings × 8 β × ~5 hr on 4–8×H100 ≈ 640–1,280 GPU-hr\n- Agent evaluation (tau2-bench + OpenAgentSafety + ATBench + AdvBench bridging): ~300 GPU-hr\n- Buffer (debugging, reruns, power-contingent β expansion): ~500 GPU-hr\n\n**Total: ~3,500–5,000 GPU-hr** (lower bound = QLoRA feasible + Tier 3 deferred; upper bound = 8×H100 for all MoE + full Tier 3).\n**Timeline:** 16 weeks (wk 1–2 infrastructure validation + trajectory generation + power simulation; wk 2–6 entanglement geometry extraction; wk 4–7 MoE routing analysis; wk 6–12 Pareto sweeps + ablations; wk 13–14 analysis + regression; wk 15–16 writing).\n**Estimated GPU cost:** $10,500–$15,000 at ~$3.00/GPU-hr average.\n**Human-in-loop variant:** Claude-assisted probe code and analysis; API cost ~$700 (Sonnet 4.6). **Auto-research variant:** Opus 4.7; API cost ~$2,800; timeline compressible to ~11 weeks.\n\n## Inspired By\n\nField guide Section 4.1 (pass@1 vs. production gap) + the convergent pattern: (a) the formal alignment tax geometry needs entanglement-robust metrics for empirical validation, (b) Plaut's near-linear agentic frontier needs geometric explanation (our framework predicts: high entanglement → small α → near-linear ellipse), (c) the MoE safety routing literature needs geometric formalization, and (d) null-space projection methods (NSPO, OGPSA) need entanglement-aware adaptation. These four bridges converge in one study.\n\n## Target Venues\n\n- ICLR 2027 (abstract Sep 19, full paper Sep 24, 2026 — primary target, 16-week execution from May 19 start)\n- AAAI 2027 (abstract Jul 26, full paper Aug 2, 2026 — stretch target for dense-model-only subset if Tier 1 results strong by week 10)\n- ICML 2027 (estimated Jan 29, 2027 — fallback with complete results including all tiers)\n\n## Key References\n\n- What Is the Geometry of the Alignment Tax? (arXiv 2603.00047, Mar 2026)\n- Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study (arXiv 2505.14185, ICLR 2026)\n- The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025)\n- Safety Training Persists Through Helpfulness Optimization in LLM Agents (arXiv 2603.02229, Mar 2026, Plaut)\n- The Viscosity of Logic: Phase Transitions in DPO (arXiv 2601.17260, Jan 2026)\n- LoRA is All You Need for Safety Alignment of Reasoning LLMs (arXiv 2507.17075)\n- Alignment Quality Index (arXiv 2506.13901, EMNLP 2025)\n- Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization [NSPO] (arXiv 2512.11391, ICLR 2026)\n- Safety Alignment as Continual Learning via Orthogonal Gradient Projection [OGPSA] (arXiv 2602.07892, Feb 2026)\n- The Autonomy Tax: Defense Training Breaks LLM Agents (arXiv 2026)\n- Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety (arXiv 2602.16943, Feb 2026)\n- Why Does Agentic Safety Fail to Generalize Across Tasks? (arXiv 2605.06992, May 2026)\n- RASA: Routing-Aware Safety Alignment for MoE Models (arXiv 2602.04448, Feb 2026)\n- SAFEx: Analyzing Vulnerabilities of MoE-Based LLMs (arXiv 2506.17368)\n- Sparse Models, Sparse Safety (arXiv 2602.08621, Feb 2026)\n- Geometric Routing Enables Causal Expert Control in MoE (arXiv 2604.14434, Apr 2026)\n- Grassmannian MoE (arXiv 2602.17798, Feb 2026)\n- Sparse Crosscoders for diffing MoEs and Dense models (arXiv 2603.05805, Mar 2026)\n- Can LLM Safety Be Ensured by Constraining Parameter Regions? (arXiv 2602.17696, Feb 2026)\n- The Geometry of Alignment Collapse (arXiv 2602.15799, Feb 2026)\n- ShaPO: Selective Geometry Control for Safety Alignment (arXiv 2602.07340, Feb 2026)\n- Fundamental Safety-Capability Trade-offs (arXiv 2503.20807, PNAS Nexus 2026)\n- Steering Externalities (arXiv 2026)\n- The Verifier Tax (arXiv 2026)\n- When Safety Geometry Collapses (arXiv 2605.02914, May 2026)\n- The Causal Impact of Tool Affordance (arXiv 2603.20320, Mar 2026)\n- OpenAgentSafety (ICLR 2026)\n- ATBench (arXiv 2604.02022, Apr 2026)\n- Multi-Agent Security Tax (arXiv 2025)\n- LLM Reasoning as Trajectories (arXiv 2604.05655)\n- Vehtari, Gelman & Gabry (2017), Practical Bayesian Model Evaluation Using LOO-CV and WAIC, Statistics and Computing 27(5)"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T04:40:33.593Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:40:33.593Z",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947"
}
```

---

## Round 1

42 recorded events

### User

_source line 3 · 2026-05-20T04:40:33.606Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Entanglement Geometry of the Alignment Tax Across Dense and MoE Architectures in Agentic Tool-Use Settings

## Description

The alignment tax has been formalized geometrically with elliptic Pareto frontiers parameterized by the principal angle α between safety and capability subspaces (arXiv 2603.00047). But empirically, these subspaces are highly entangled (MSO, ICLR 2026), MoE architectures route safety through sparse expert dynamics, and in agentic settings Plaut (arXiv 2603.02229) observes a near-linear frontier (R²=0.77) without geometric explanation. We hypothesize: high entanglement yields small α, degenerating the ellipse toward linearity, while MoE routing introduces discrete dynamics that violate the framework's continuous-subspace assumptions. We produce three contributions. (C1) The first empirical bridge between two independent metric systems — MSO (parameter-space entanglement, ICLR 2026) and principal angle α (activation-space geometry) — establishing their cross-space correspondence via layer-wise mixed-effects analysis; this determines whether parameter-space interventions (NSPO arXiv 2512.11391, OGPSA arXiv 2602.07892) and activation-space diagnostics operate on compatible foundations, and provides initial evidence for probing-based alignment tax prediction without full DPO sweeps. (C2) A diagnostic dual-estimation test with pre-registered outcome topology: α_repr–α_frontier agreement validates geometric theory under entanglement, while systematic divergence quantifies the linear representation hypothesis's failure boundary; a 2×2 outcome matrix ({dense,MoE} × {chat,agent}) pre-registers interpretations for every divergence pattern, making the paper informative under any result. (C3) MoE as a stress test of continuous-subspace geometry: if safety is routing-mediated (RASA, arXiv 2602.04448), activation-space α may fail to capture MoE safety structure, and α_repr–α_frontier divergence should be larger in MoE than dense models. Using a 2×2 design — {Qwen3-32B, Gemma 4 31B} (dense) × {Qwen3-235B-A22B, Llama-4-Maverick} (MoE) in {chat, agent} — we sweep 16 LoRA-DPO β values per condition with Bayesian model comparison (PSIS-LOO + WAIC) and meta-analytic agreement testing. Expected: (1) higher MSO in agents vs. chat; (2) α_repr ≈ α_frontier in dense models, both smaller in agents (explaining Plaut's frontier as a low-angle ellipse); (3) larger α_repr–α_frontier divergence in MoE than dense, quantifying routing-mediated geometry violation; (4) layer-wise MSO–α_repr correspondence establishing whether parameter-space and activation-space analyses are compatible paradigms.

## Core Problem

The alignment tax has been formalized geometrically under the linear representation hypothesis, yielding elliptic Pareto frontiers parameterized by the principal angle α between safety and capability subspaces (arXiv 2603.00047). Three empirical challenges prevent direct application. (1) Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185, ICLR 2026) shows safety and capability subspaces are highly entangled, with MSO strongest between useful and safety-specific updates — but MSO operates in parameter space (SVD of weight difference matrices) while α operates in activation space (cross-covariance of activation vectors). These two metric systems have never been connected, creating a measurement schism: the alignment community simultaneously uses parameter-space interventions (null-space gradient projection) and activation-space diagnostics (probing, geometric theory) without knowing if they analyze the same underlying structure. (2) Frontier models are predominantly MoE architectures where safety is governed by sparse expert routing (RASA arXiv 2602.04448, SAFEx arXiv 2506.17368, Sparse Models Sparse Safety arXiv 2602.08621), not global activation subspaces — making the continuous-subspace geometric framework's applicability non-trivial. (3) In agentic tool-use settings, both challenges intensify: text safety does not transfer to tool-call safety (Mind the GAP, arXiv 2602.16943), and the safe controller mapping has inherently higher Lipschitz complexity (Why Does Agentic Safety Fail to Generalize, arXiv 2605.06992). Plaut (arXiv 2603.02229) measured an approximately linear Pareto frontier (R²=0.77, slope −0.83) in agentic DPO on 8B–14B models — but with only two β values, no representation analysis, and no MoE comparison. The geometric framework's author explicitly notes it fails "for large perturbations, the KL is not quadratic, the representation geometry shifts" — but this failure boundary has never been quantified.

## Opportunity

Four independent lines of work create a convergence point whose bridges are missing. The Geometry of the Alignment Tax (arXiv 2603.00047, Mar 2026) provides the formal apparatus — principal angles, elliptic Pareto frontiers, tax rate decomposition — but assumes linear separability, static representations, and dense architectures. Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185, ICLR 2026) proves the separability assumption fails via MSO in parameter space, but only in chat on models up to 7B — and operates in a different mathematical space than the geometric theory. The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025) reveals multi-dimensional orthogonal safety directions in activation space, but only in chat on Llama 3 8B. Plaut (arXiv 2603.02229, Mar 2026) discovers a near-linear agentic Pareto frontier, which the geometric theory predicts when α is small — but used only 8B–14B dense models with 2 β values and no representation analysis. The MoE safety literature (RASA arXiv 2602.04448, SAFEx arXiv 2506.17368, Sparse Models Sparse Safety arXiv 2602.08621) establishes that safety operates through routing dynamics — safety-critical experts, routing distribution divergence, expert silencing — meaning MoE safety is fundamentally routing-mediated and may not be capturable by continuous activation-space geometry. This makes MoE a stress test of the geometric framework's foundations. The null-space projection literature (NSPO arXiv 2512.11391, ICLR 2026; OGPSA arXiv 2602.07892) mitigates the tax by projecting safety gradients into capability null spaces — but in parameter space, assuming separable subspaces. If MSO and α_repr do not correspond, then parameter-space interventions and activation-space theory may be analyzing different structures, with direct consequences for intervention design. LoRA rank=1 achieves optimal reasoning-safety tradeoff (arXiv 2507.17075), suggesting safety alignment is intrinsically low-rank and representation probing may suffice to capture relevant structure. AQI (arXiv 2506.13901, EMNLP 2025) demonstrates that latent geometry — cluster divergence metrics applied to safe/unsafe activations — can diagnose alignment quality without generation, validating the general approach of representation-based alignment diagnosis; our work differs by using principal angles (geometric structure parameterizing the Pareto frontier) rather than cluster quality metrics (scalar diagnostic), and by connecting to cross-space correspondence, architecture-specific analysis, and frontier shape prediction.

## Landscape

The Geometry of the Alignment Tax (arXiv 2603.00047, Mar 2026) proves the Pareto frontier is an ellipse ΔS = ΔC cos α + sin α √(B² − ΔC²) parameterized by the principal angle α, but is purely theoretical with no empirical validation and acknowledges failure under large perturbations or nonlinear encoding. Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185, ICLR 2026) introduces MSO quantifying safety-capability entanglement via SVD overlap matrices; strongest overlap is between useful and safety updates on Llama 2/3.2 and Qwen 2.5 (1B–7B) — chat only, parameter space only, with layer-specific analysis at 70-85 percentile depth. The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025) reveals multi-dimensional orthogonal safety directions with a dominant refusal direction plus interpretable secondary features — chat only, Llama 3 8B, activation space. Safety Training Persists Through Helpfulness Optimization (arXiv 2603.02229, Mar 2026, Plaut) finds an approximately linear Pareto frontier (R²=0.77, slope −0.83) across 180 DPO configurations on Llama 3.1 8B, Qwen 2.5 7B, and Phi 4 14B using ToolEmu (144 tasks); uses only β ∈ {0.05, 0.1}, no representation analysis, no MoE — frontier shape observed but not geometrically explained. The Viscosity of Logic (arXiv 2601.17260, Jan 2026) sweeps DPO β on Mistral-7B and identifies phase transitions at discrete β values near 10⁻², demonstrating that systematic β sweeping reveals nonlinear regime transitions, motivating dense sampling in high-gradient regions. LoRA is All You Need for Safety Alignment of Reasoning LLMs (arXiv 2507.17075) finds rank=1 LoRA achieves optimal reasoning-safety tradeoff, suggesting safety alignment is intrinsically low-rank. AQI (arXiv 2506.13901, EMNLP 2025) uses latent geometry — Xie-Beni, Calinski-Harabasz, Davies-Bouldin, Dunn indices on safe/unsafe activation clusters — to diagnose alignment quality without generation; differs from our approach in using cluster divergence (scalar quality indicator) vs. principal angles (geometric structure parameterizing Pareto frontier shape), and does not address agent/MoE settings or cross-space correspondence. NSPO (arXiv 2512.11391, ICLR 2026) projects safety gradients into the null space of the capability covariance matrix KK⊤ — but assumes separable subspaces. OGPSA (arXiv 2602.07892, Feb 2026) similarly projects safety gradients onto the orthogonal complement of a capability subspace. Can LLM Safety Be Ensured by Constraining Parameter Regions? (arXiv 2602.17696) shows safety regions are dataset-dependent with low IoU. The Geometry of Alignment Collapse (arXiv 2602.15799) shows alignment concentrates in low-dimensional subspaces with sharp curvature. ShaPO (arXiv 2602.07340) enforces geometry-aware preference optimization via selective geometry control. Sparse Crosscoders (arXiv 2603.05805) provides methods for comparing MoE and dense model representations at small scale, finding MoEs learn fewer but more specific features. The Autonomy Tax (Mar 2026) shows 99% timeout rates from agent safety training. Mind the GAP (arXiv 2602.16943, Feb 2026) demonstrates text-tool safety divergence across 17,420 datapoints. Why Does Agentic Safety Fail to Generalize (arXiv 2605.06992, May 2026) proves the safe controller has higher Lipschitz constant than task execution. RASA (arXiv 2602.04448, Feb 2026) identifies safety-critical experts via Adversarial Activation Discrepancy and shows full-parameter MoE safety fine-tuning creates routing shortcuts — restoring original routing collapses harmlessness by Δ ∈ [−0.38, −0.46]. SAFEx (arXiv 2506.17368) shows disabling 12 of 6,144 experts drops refusal rate 22%. Sparse Models Sparse Safety (arXiv 2602.08621, Feb 2026) introduces RoSais scores: masking 5 routers increases ASR 4× to 0.79. Geometric Routing (arXiv 2604.14434, Apr 2026) demonstrates monosemantic experts with frequency-to-syntax gradient. Grassmannian MoE (arXiv 2602.17798, Feb 2026) provides subspace-manifold routing. Fundamental Safety-Capability Trade-offs (arXiv 2503.20807, PNAS Nexus 2026) characterizes theoretical tradeoff limits. The Verifier Tax (Mar 2026) and Steering Externalities (Feb 2026) provide further agentic alignment tax evidence. When Safety Geometry Collapses (arXiv 2605.02914, May 2026) demonstrates safety geometry destruction in guard models. The Causal Impact of Tool Affordance (arXiv 2603.20320, Mar 2026) confirms sharp safety degradation in tool-enabled agents. ATBench (arXiv 2604.02022, Apr 2026) provides paired safe/unsafe trajectory construction with 1,000 trajectories across 1,954 tools. OpenAgentSafety (ICLR 2026) provides 350+ executable tasks with rule-based evaluators. Multi-Agent Security Tax (arXiv 2025) documents safety costs in multi-agent settings. No existing work connects parameter-space MSO to activation-space principal angles, measures alignment tax geometry under entanglement-aware metrics in agentic settings, provides geometric explanation for the observed near-linear frontier in agents, or tests the geometric framework's applicability to MoE routing-mediated safety.

## Approach

We conduct the first entanglement-aware, architecture-controlled measurement of alignment tax geometry in agentic tool-use settings, using a 2×2 factorial design: {dense, MoE} × {chat, agent}. Three core contributions: (C1) cross-space metric bridge with metrological implications, (C2) diagnostic dual-estimation test with pre-registered outcome topology, (C3) MoE stress test of geometric framework.

**Model Selection (2 dense + 2 MoE):**
- Dense: Qwen3-32B (32.8B active, Qwen3 family), Gemma 4 31B (31B, Apache 2.0)
- MoE: Qwen3-235B-A22B (22B active / 235B total, Qwen3 family), Llama-4-Maverick (17B active / 400B total)

The Qwen3 dense/MoE pair enables within-family comparison (same training data, tokenizer) — this is the primary apples-to-apples comparison. The cross-family pair (Gemma/Maverick) provides generalizability signal. Active parameter counts differ between dense and MoE (32.8B vs. 22B for Qwen3; 31B vs. 17B cross-family); addressed via FLOP-normalized analysis. Maverick contingency: if DPO memory requirements prove prohibitive (400B total requires reference offloading for DPO), fallback to Qwen3-30B-A3B (30B total / 3.3B active, Qwen3 family), which provides an MoE sparsity gradient (22B vs. 3.3B active) within the same model family.

**Priority tiers:** Tier 1 (must-have): Qwen3-32B + Qwen3-235B-A22B × 2 settings × 16 β = 64 runs. Tier 2 (high-priority): Gemma 4 31B × 2 settings × 16 β = 32 runs. Tier 3 (contingent on resources): Maverick (or fallback) × 2 settings × 16 β = 32 runs.

**Phase 1: Entanglement Geometry & Cross-Space Metric Bridge (wk 1–6)**

*Infrastructure Validation (wk 1–2):* End-to-end pipeline verification on 1–2 β values per model: confirm QLoRA/LoRA-DPO training, activation extraction, evaluation pipeline (tau2-bench, OpenAgentSafety, ATBench, AdvBench). For Maverick, validate reference offloading feasibility; if infeasible, trigger fallback to Qwen3-30B-A3B.

*Trajectory Construction:*
Agent settings: paired safe/unsafe trajectories from (i) OpenAgentSafety's (ICLR 2026) 350+ executable tasks with rule-based safety evaluators across 8 risk categories; (ii) ATBench's (arXiv 2604.02022) planner-based paired trajectory synthesis with 1,000 trajectories across 1,954 tools. Capability subspace: tau2-bench policy-adherence tasks, activations from successful vs. failed completions. Activations extracted at tool-call decision points following LLM Reasoning as Trajectories (arXiv 2604.05655). Chat baseline: AdvBench/BeaverTails prompts matching the original MSO paper's methodology.

*Entanglement Metrics:*
(a) Mode Subspace Overlap (MSO): following Safety Subspaces are Not Linearly Distinct (ICLR 2026), computed via SVD overlap matrices. Sensitivity ablation over subspace rank K ∈ {5, 10, 20, 50, 100}.
(b) Multi-dimensional safety decomposition: following Hidden Dimensions (ICML 2025), identifying dominant refusal direction and orthogonal secondary directions.
(c) Principal angles via SVD on cross-covariance matrices of activation vectors, yielding α_repr. Spectrum of first 10 principal angles reported (not just leading angle). Layer-wise profiles computed per layer.

*Cross-Space Correspondence (C1) with Metrological Implications:*
We test the empirical relationship between MSO (parameter space) and α_repr (activation space) at layer-wise granularity: for each model × setting condition, compute both MSO and α_repr at each layer in the middle-third depth range (~10–15 layers per model), yielding ~80–100 (MSO_layer, α_repr_layer) data points total. Analyze via linear mixed-effects model with MSO_layer as predictor, α_repr_layer as response, and random intercept per model-setting condition. This resolves the statistical power limitation of condition-level analysis (n=8) while respecting the nested structure. The correspondence is non-trivial: weight-space overlap may manifest as activation-space masking, amplification, or rank change without angle reduction. Results determine whether parameter-space interventions (NSPO, OGPSA) and activation-space diagnostics operate on compatible foundations — if MSO and α_repr do not correspond, these two analysis paradigms are not interchangeable, directly impacting alignment intervention design.

*Probing-Based Prediction (C1 application):*
Regression of condition-level representation measurements (MSO, α_repr, effective rank, routing divergence for MoE) against α_frontier and downstream safety metrics. If predictive, this provides initial evidence that alignment tax severity can be estimated from representation probing (~25 GPU-hr per model) without full DPO sweeps (~80+ GPU-hr per model), addressing the open question posed by the Geometry of the Alignment Tax author.

*Trajectory Construction Sensitivity Ablation:*
(i) Data source ablation: MSO and α_repr from OpenAgentSafety-only vs. ATBench-only vs. combined. (ii) Token position ablation: extraction at (a) tool-call decision points (default), (b) last token of each agent step, (c) mean-pooling over all step tokens.

**Phase 2: Architecture-Aware MoE Routing Analysis (wk 4–7, overlapping)**
For MoE models, three-level decomposition:
(a) Shared attention layers: analogous to dense-model analysis, providing controlled comparison.
(b) Per-expert FFN subspaces: safety-critical experts identified via Adversarial Activation Discrepancy (RASA, arXiv 2602.04448). Per-expert α_repr and MSO computed to test whether safety is concentrated in specific experts or distributed.
(c) Router weight space: routing distribution divergence (KL) between safe/unsafe inputs; RoSais-style router safety importance scoring (Sparse Models Sparse Safety, arXiv 2602.08621).

Supplementary/exploratory: Sparse Crosscoders (arXiv 2603.05805) for feature organization comparison, contingent on scaling feasibility at 30B+ scale (original validation at 5-layer models only). Core MoE conclusions do not depend on crosscoder results.

**Phase 3: Pareto Frontier Mapping & Diagnostic Dual-Estimation Test (wk 6–12)**

*Evaluation Axes:*
- Safety axis: OpenAgentSafety safety score (agent); AdvBench refusal rate + BeaverTails safety score (chat). Cross-setting control: all agent-trained models also evaluated on AdvBench (shared safety metric across settings).
- Capability axis: tau2-bench task success rate + OpenAgentSafety task completion rate (agent); MMLU (5-shot) + GSM8K (8-shot) (chat). Pareto frontiers reported per capability metric to verify shape robustness.
- Within-setting comparison (same evaluation protocol, varying architecture/model) is the primary analysis. Cross-setting comparison (agent vs. chat α) is secondary/suggestive, with metric-induced confounds explicitly discussed.

*Training Protocol:*
- Primary: LoRA-DPO on all layers, LoRA rank matched on total trainable parameters across architectures.
- Secondary matching: per-token active trainable parameters (MoE LoRA rank increased to compensate for expert sparsity), testing whether matching strategy affects frontier shape conclusions.
- MoE-specific ablation: (i) shared-attention-only LoRA, (ii) active-expert-only LoRA (HELLoRA-style). These ablations also serve to address the parameter-matching confound by isolating which model components drive frontier shape.
- FLOP-normalized analysis: per-model training/inference FLOPs reported; FLOP-normalized Pareto frontiers provided alongside parameter-matched frontiers.

*β Sweep:*
16 LoRA-DPO β values per model/setting (β ∈ {0.003, 0.005, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.15, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0}), with increased density in the high-gradient region. If pre-study power simulation indicates n=16 insufficient for α < 15° discrimination, increase to 24 β points for Tier 1 models (offset by reducing Tier 3 scope). Phase transitions at discrete β values (The Viscosity of Logic, arXiv 2601.17260) motivate the dense sampling.

*Statistical Approach:*
Bayesian model comparison using PSIS-LOO (Vehtari, Gelman & Gabry, 2017; preferred for small-sample robustness) and WAIC for three frontier models: (i) elliptic (α, B), (ii) linear (slope, intercept), (iii) piecewise-linear. Report ΔELPD ± SE(ΔELPD); if |ΔELPD| < SE, honestly reported as inconclusive. Pre-study power simulation: synthetic frontiers at α ∈ {5°, 10°, 15°, 20°, 45°} with realistic noise, testing PSIS-LOO discrimination at n=16 and n=24. Leave-one-out sensitivity: checking whether removing any single β point changes model ranking. Supplementary: local curvature analysis (second-order finite differences along the frontier) to detect deviation from linearity even when global shape discrimination is inconclusive.

*Small-α Fallback:* If most conditions yield α < 10° and PSIS-LOO is inconclusive for elliptic vs. linear, C2's contribution reframes as "quantifying α's upper bound" — empirically demonstrating that entanglement is sufficient to collapse the frontier to near-linearity (α < X° with 95% credible interval), which itself validates the geometric theory's prediction that high entanglement linearizes the tax.

*Diagnostic Dual-Estimation Test (C2) with Outcome Topology:*
α_repr (Phase 1) vs. α_frontier (elliptic fit) compared via random-effects meta-analysis: compute (α_repr − α_frontier) for each of the 8 conditions (with uncertainty from bootstrap for α_repr and posterior for α_frontier), fit random-effects model testing whether the population mean difference deviates from 0. This replaces arbitrary counting thresholds with a formal statistical test of systematic divergence.

Pre-registered outcome topology — the 2×2 structure ({dense, MoE} × {chat, agent}) yields four interpretive patterns:
- Dense agree + MoE diverge → routing violates continuous-subspace assumption (C3 confirmed); activation-space geometry remains valid for dense models but breaks for MoE
- Chat agree + agent diverge → agentic complexity exceeds linear representation assumption; standard geometric framework applies in chat but not in tool-use settings
- Both diverge → geometric framework fundamentally inadequate under real entanglement levels; the linear representation hypothesis is a poor approximation for safety-capability geometry
- Both agree → framework is surprisingly robust despite entanglement; principal angle theory extends beyond its stated assumptions

Each pattern has distinct consequences for alignment intervention design (parameter-space projection vs. routing-aware methods vs. setting-specific approaches), ensuring the paper produces actionable findings regardless of outcome.

**Scope note:** We exclude intervention phases (entanglement-adapted OGPSA or NSPO). We focus on rigorous measurement and geometric explanation.

## Resource Estimate

**GPU hours (distinguishing wall-clock from GPU-hours):**
- Infrastructure validation (wk 1–2): ~100 GPU-hr (1–2 β × 4 models × 2 settings, quick runs)
- Phase 1 activation extraction: 4 models × 2 settings × ~25 hr on 4–8×H100 ≈ 400–600 GPU-hr
- Phase 2 MoE routing analysis: 2 models × 60 hr on 8×H100 ≈ 960 GPU-hr
- Phase 3 Tier 1 sweep (Qwen3 pair): 2 models × 2 settings × 16 β × ~5 hr on 4×H100 (dense) / 4–8×H100 (MoE QLoRA) ≈ 640–1,280 GPU-hr
- Phase 3 Tier 2 sweep (Gemma): 1 model × 2 settings × 16 β × ~5 hr on 4×H100 ≈ 640 GPU-hr
- Phase 3 Tier 3 sweep (Maverick/fallback): 1 model × 2 settings × 16 β × ~5 hr on 8×H100 (with ref offloading) ≈ 1,280 GPU-hr
- Phase 3 MoE ablation: 2 models × 2 settings × 8 β × ~5 hr on 4–8×H100 ≈ 640–1,280 GPU-hr
- Agent evaluation (tau2-bench + OpenAgentSafety + ATBench + AdvBench bridging): ~300 GPU-hr
- Buffer (debugging, reruns, power-contingent β expansion): ~500 GPU-hr

**Total: ~3,500–5,000 GPU-hr** (lower bound = QLoRA feasible + Tier 3 deferred; upper bound = 8×H100 for all MoE + full Tier 3).
**Timeline:** 16 weeks (wk 1–2 infrastructure validation + trajectory generation + power simulation; wk 2–6 entanglement geometry extraction; wk 4–7 MoE routing analysis; wk 6–12 Pareto sweeps + ablations; wk 13–14 analysis + regression; wk 15–16 writing).
**Estimated GPU cost:** $10,500–$15,000 at ~$3.00/GPU-hr average.
**Human-in-loop variant:** Claude-assisted probe code and analysis; API cost ~$700 (Sonnet 4.6). **Auto-research variant:** Opus 4.7; API cost ~$2,800; timeline compressible to ~11 weeks.

## Inspired By

Field guide Section 4.1 (pass@1 vs. production gap) + the convergent pattern: (a) the formal alignment tax geometry needs entanglement-robust metrics for empirical validation, (b) Plaut's near-linear agentic frontier needs geometric explanation (our framework predicts: high entanglement → small α → near-linear ellipse), (c) the MoE safety routing literature needs geometric formalization, and (d) null-space projection methods (NSPO, OGPSA) need entanglement-aware adaptation. These four bridges converge in one study.

## Target Venues

- ICLR 2027 (abstract Sep 19, full paper Sep 24, 2026 — primary target, 16-week execution from May 19 start)
- AAAI 2027 (abstract Jul 26, full paper Aug 2, 2026 — stretch target for dense-model-only subset if Tier 1 results strong by week 10)
- ICML 2027 (estimated Jan 29, 2027 — fallback with complete results including all tiers)

## Key References

- What Is the Geometry of the Alignment Tax? (arXiv 2603.00047, Mar 2026)
- Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study (arXiv 2505.14185, ICLR 2026)
- The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025)
- Safety Training Persists Through Helpfulness Optimization in LLM Agents (arXiv 2603.02229, Mar 2026, Plaut)
- The Viscosity of Logic: Phase Transitions in DPO (arXiv 2601.17260, Jan 2026)
- LoRA is All You Need for Safety Alignment of Reasoning LLMs (arXiv 2507.17075)
- Alignment Quality Index (arXiv 2506.13901, EMNLP 2025)
- Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization [NSPO] (arXiv 2512.11391, ICLR 2026)
- Safety Alignment as Continual Learning via Orthogonal Gradient Projection [OGPSA] (arXiv 2602.07892, Feb 2026)
- The Autonomy Tax: Defense Training Breaks LLM Agents (arXiv 2026)
- Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety (arXiv 2602.16943, Feb 2026)
- Why Does Agentic Safety Fail to Generalize Across Tasks? (arXiv 2605.06992, May 2026)
- RASA: Routing-Aware Safety Alignment for MoE Models (arXiv 2602.04448, Feb 2026)
- SAFEx: Analyzing Vulnerabilities of MoE-Based LLMs (arXiv 2506.17368)
- Sparse Models, Sparse Safety (arXiv 2602.08621, Feb 2026)
- Geometric Routing Enables Causal Expert Control in MoE (arXiv 2604.14434, Apr 2026)
- Grassmannian MoE (arXiv 2602.17798, Feb 2026)
- Sparse Crosscoders for diffing MoEs and Dense models (arXiv 2603.05805, Mar 2026)
- Can LLM Safety Be Ensured by Constraining Parameter Regions? (arXiv 2602.17696, Feb 2026)
- The Geometry of Alignment Collapse (arXiv 2602.15799, Feb 2026)
- ShaPO: Selective Geometry Control for Safety Alignment (arXiv 2602.07340, Feb 2026)
- Fundamental Safety-Capability Trade-offs (arXiv 2503.20807, PNAS Nexus 2026)
- Steering Externalities (arXiv 2026)
- The Verifier Tax (arXiv 2026)
- When Safety Geometry Collapses (arXiv 2605.02914, May 2026)
- The Causal Impact of Tool Affordance (arXiv 2603.20320, Mar 2026)
- OpenAgentSafety (ICLR 2026)
- ATBench (arXiv 2604.02022, Apr 2026)
- Multi-Agent Security Tax (arXiv 2025)
- LLM Reasoning as Trajectories (arXiv 2604.05655)
- Vehtari, Gelman & Gabry (2017), Practical Bayesian Model Evaluation Using LOO-CV and WAIC, Statistics and Computing 27(5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f21766f1-6940-4f73-a24d-5ba14860739d",
  "type": "user",
  "uuid": "e3fee809-b160-49ce-9ab6-c5a8413e64fa",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:40:33.605Z_

```json
{
  "parentUuid": "e3fee809-b160-49ce-9ab6-c5a8413e64fa",
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
  "uuid": "26e7acb2-16b8-4180-993d-409e73a3370e",
  "timestamp": "2026-05-20T04:40:33.605Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:40:33.605Z_

```json
{
  "parentUuid": "26e7acb2-16b8-4180-993d-409e73a3370e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7f95a873-ff14-4013-8e6b-76253d2da842",
  "timestamp": "2026-05-20T04:40:33.605Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Entanglement Geometry of the Alignment Tax Across Dense and MoE Architectures in Agentic Tool-Use Settings  ## D…",
  "leafUuid": "7f95a873-ff14-4013-8e6b-76253d2da842",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate alignment tax geometry proposal acceptance probability",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:40:38.712Z_

<details><summary>Logged reasoning block</summary>

```text
This is a complex research proposal that I need to evaluate for EMNLP 2026 submission potential. Let me first do thorough web searches to understand the current landscape, then provide my assessment.

Let me search for the key papers and concepts mentioned in this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f95a873-ff14-4013-8e6b-76253d2da842",
  "isSidechain": false,
  "requestId": "req_011CbDCtK9PnmngkEu79aLKx",
  "type": "assistant",
  "uuid": "de6db739-91c9-43f1-8ffc-7146a3296735",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPUZoEcDcRkKuwrzLA1C9e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 23507,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 175,
          "cache_read_input_tokens": 23507,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 9 · 2026-05-20T04:40:39.607Z_

I need to do thorough literature research before evaluating this proposal. Let me search for the key papers and concepts mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de6db739-91c9-43f1-8ffc-7146a3296735",
  "isSidechain": false,
  "requestId": "req_011CbDCtK9PnmngkEu79aLKx",
  "type": "assistant",
  "uuid": "1714d50e-314b-4694-9003-955637ca2f54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPUZoEcDcRkKuwrzLA1C9e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 23507,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 175,
          "cache_read_input_tokens": 23507,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 10 · 2026-05-20T04:40:40.232Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QEn3C6W8fxmJAYLZnQiK9E`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1714d50e-314b-4694-9003-955637ca2f54",
  "isSidechain": false,
  "requestId": "req_011CbDCtK9PnmngkEu79aLKx",
  "type": "assistant",
  "uuid": "de25e64a-bad8-4eeb-9802-e7e2e7f25979",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPUZoEcDcRkKuwrzLA1C9e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 23507,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 175,
          "cache_read_input_tokens": 23507,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 11 · 2026-05-20T04:40:40.239Z_

<details><summary>↩ Tool result · `toolu_01QEn3C6W8fxmJAYLZnQiK9E`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de25e64a-bad8-4eeb-9802-e7e2e7f25979",
  "isSidechain": false,
  "promptId": "f21766f1-6940-4f73-a24d-5ba14860739d",
  "type": "user",
  "uuid": "d56bcaa6-a650-4500-bae0-b958d6beb1ad",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "de25e64a-bad8-4eeb-9802-e7e2e7f25979",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T04:40:42.615Z_

Now let me conduct the required literature searches to understand the landscape before evaluating this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d56bcaa6-a650-4500-bae0-b958d6beb1ad",
  "isSidechain": false,
  "requestId": "req_011CbDCtotH9SQ5L8ZveTiJW",
  "type": "assistant",
  "uuid": "5fca9530-d655-4d1e-8518-8ef6f00c6a4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1cBhsfTZv2RbLMmwj8kf2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 23507,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 305,
          "cache_read_input_tokens": 23507,
          "cache_creation_input_tokens": 703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 703
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

_source line 13 · 2026-05-20T04:40:43.605Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MvgA48LWPQaoXS3xoPVT9f`</summary>

```json
{
  "query": "alignment tax geometry principal angle safety capability subspaces 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fca9530-d655-4d1e-8518-8ef6f00c6a4e",
  "isSidechain": false,
  "requestId": "req_011CbDCtotH9SQ5L8ZveTiJW",
  "type": "assistant",
  "uuid": "d54dd988-a668-4e02-be01-e64705adb631",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1cBhsfTZv2RbLMmwj8kf2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 23507,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 305,
          "cache_read_input_tokens": 23507,
          "cache_creation_input_tokens": 703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 703
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

_source line 14 · 2026-05-20T04:40:44.662Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JjHQ7c2UwPh6sNozNTN1fr`</summary>

```json
{
  "query": "safety subspaces not linearly distinct MSO mode subspace overlap ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d54dd988-a668-4e02-be01-e64705adb631",
  "isSidechain": false,
  "requestId": "req_011CbDCtotH9SQ5L8ZveTiJW",
  "type": "assistant",
  "uuid": "c5bff44c-4cb7-4ed8-972c-1161b915e9df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1cBhsfTZv2RbLMmwj8kf2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 23507,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 305,
          "cache_read_input_tokens": 23507,
          "cache_creation_input_tokens": 703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 703
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

_source line 15 · 2026-05-20T04:40:45.660Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XxS5mibZ4VMjeuNhQqqV5t`</summary>

```json
{
  "query": "MoE mixture of experts safety alignment routing RASA SAFEx sparse safety 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5bff44c-4cb7-4ed8-972c-1161b915e9df",
  "isSidechain": false,
  "requestId": "req_011CbDCtotH9SQ5L8ZveTiJW",
  "type": "assistant",
  "uuid": "f63b47f3-4454-4732-bd42-ecdd872fb6b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1cBhsfTZv2RbLMmwj8kf2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 23507,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 305,
          "cache_read_input_tokens": 23507,
          "cache_creation_input_tokens": 703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 703
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

_source line 16 · 2026-05-20T04:40:46.137Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013cZ5aUYJTqfgbck14CZFih`</summary>

```json
{
  "query": "agentic safety Pareto frontier DPO tool-use alignment tax 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f63b47f3-4454-4732-bd42-ecdd872fb6b1",
  "isSidechain": false,
  "requestId": "req_011CbDCtotH9SQ5L8ZveTiJW",
  "type": "assistant",
  "uuid": "acde676f-6aa3-4ece-954b-935e7a68211a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1cBhsfTZv2RbLMmwj8kf2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 23507,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 305,
          "cache_read_input_tokens": 23507,
          "cache_creation_input_tokens": 703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 703
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

_source line 17 · 2026-05-20T04:40:47.058Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0132i795yK3v9A58PLUVE8jw`</summary>

```json
{
  "query": "alignment quality index latent geometry activation space safety diagnosis EMNLP 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acde676f-6aa3-4ece-954b-935e7a68211a",
  "isSidechain": false,
  "requestId": "req_011CbDCtotH9SQ5L8ZveTiJW",
  "type": "assistant",
  "uuid": "ba52eb49-fb62-4a2d-854f-28fe64ba8818",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1cBhsfTZv2RbLMmwj8kf2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 23507,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 305,
          "cache_read_input_tokens": 23507,
          "cache_creation_input_tokens": 703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 703
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

_source line 18 · 2026-05-20T04:40:50.089Z_

<details><summary>↩ Tool result · `toolu_01MvgA48LWPQaoXS3xoPVT9f`</summary>

```text
Web search results for query: "alignment tax geometry principal angle safety capability subspaces 2026 arXiv"

Links: [{"title":"[2603.00047] What Is the Geometry of the Alignment Tax?","url":"https://arxiv.org/abs/2603.00047"},{"title":"[2603.00047v2] What Is the Alignment Tax?","url":"https://arxiv.org/abs/2603.00047v2"},{"title":"What Is the Alignment Tax?","url":"https://arxiv.org/html/2603.00047v2"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2512.11391"},{"title":"Safety Alignment as Continual Learning: Mitigating the Alignment Tax via Orthogonal Gradient Projection","url":"https://arxiv.org/html/2602.07892v1"},{"title":"Safety Alignment as Continual Learning: Mitigating the Alignment Tax via","url":"https://www.arxiv.org/pdf/2602.07892"},{"title":"The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety","url":"https://arxiv.org/pdf/2602.15799"},{"title":"Mitigating the Safety Alignment Tax with Null-Space Constrained...","url":"https://arxiv.org/abs/2512.11391"}]

I found several relevant papers on arXiv related to your search query. Here are the key results:

## Main Result: "What Is the Geometry of the Alignment Tax?"

The paper provides a geometric theory of the alignment tax in representation space, defining the alignment tax rate as the squared projection of the safety direction onto the capability subspace and deriving the Pareto frontier governing safety-capability tradeoffs, parameterized by the principal angle between the safety and capability subspaces. This paper (arXiv:2603.00047) was published on March 3, 2026.

The frontier is proven to be tight and has a recursive structure. The paper derives a scaling law decomposing the alignment tax into an irreducible component determined by data structure and a packing residual that vanishes as O(m'/d) with model dimension d.

## Related Papers

Other recent papers addressing similar themes include:

- **"Safety Alignment as Continual Learning"** (arXiv:2602.07892, February 2026): Proposes projecting safety gradients onto the orthogonal complement of the capability subspace during alignment to mitigate the alignment tax.

- **"Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization"** (arXiv:2512.11391, January 2026): Uses null-space projection of safety policy gradients into the null space of general tasks, while theoretically proving preservation of core capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d54dd988-a668-4e02-be01-e64705adb631",
  "isSidechain": false,
  "promptId": "f21766f1-6940-4f73-a24d-5ba14860739d",
  "type": "user",
  "uuid": "887cdb36-05bf-4e92-a9df-90d6040a65d0",
  "toolUseResult": {
    "query": "alignment tax geometry principal angle safety capability subspaces 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NkvqAqoaZ7xUXhWNp5E7AS",
        "content": [
          {
            "title": "[2603.00047] What Is the Geometry of the Alignment Tax?",
            "url": "https://arxiv.org/abs/2603.00047"
          },
          {
            "title": "[2603.00047v2] What Is the Alignment Tax?",
            "url": "https://arxiv.org/abs/2603.00047v2"
          },
          {
            "title": "What Is the Alignment Tax?",
            "url": "https://arxiv.org/html/2603.00047v2"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2512.11391"
          },
          {
            "title": "Safety Alignment as Continual Learning: Mitigating the Alignment Tax via Orthogonal Gradient Projection",
            "url": "https://arxiv.org/html/2602.07892v1"
          },
          {
            "title": "Safety Alignment as Continual Learning: Mitigating the Alignment Tax via",
            "url": "https://www.arxiv.org/pdf/2602.07892"
          },
          {
            "title": "The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety",
            "url": "https://arxiv.org/pdf/2602.15799"
          },
          {
            "title": "Mitigating the Safety Alignment Tax with Null-Space Constrained...",
            "url": "https://arxiv.org/abs/2512.11391"
          }
        ]
      },
      "I found several relevant papers on arXiv related to your search query. Here are the key results:\n\n## Main Result: \"What Is the Geometry of the Alignment Tax?\"\n\nThe paper provides a geometric theory of the alignment tax in representation space, defining the alignment tax rate as the squared projection of the safety direction onto the capability subspace and deriving the Pareto frontier governing safety-capability tradeoffs, parameterized by the principal angle between the safety and capability subspaces. This paper (arXiv:2603.00047) was published on March 3, 2026.\n\nThe frontier is proven to be tight and has a recursive structure. The paper derives a scaling law decomposing the alignment tax into an irreducible component determined by data structure and a packing residual that vanishes as O(m'/d) with model dimension d.\n\n## Related Papers\n\nOther recent papers addressing similar themes include:\n\n- **\"Safety Alignment as Continual Learning\"** (arXiv:2602.07892, February 2026): Proposes projecting safety gradients onto the orthogonal complement of the capability subspace during alignment to mitigate the alignment tax.\n\n- **\"Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization\"** (arXiv:2512.11391, January 2026): Uses null-space projection of safety policy gradients into the null space of general tasks, while theoretically proving preservation of core capabilities."
    ],
    "durationSeconds": 6.478915371000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d54dd988-a668-4e02-be01-e64705adb631",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T04:40:50.512Z_

<details><summary>↩ Tool result · `toolu_01JjHQ7c2UwPh6sNozNTN1fr`</summary>

```text
Web search results for query: "safety subspaces not linearly distinct MSO mode subspace overlap ICLR 2026"

Links: [{"title":"SAFETY SUBSPACES ARE NOT LINEARLY DISTINCT","url":"https://openreview.net/pdf/75b8c23862b8fd1143e9069e0ad51e44f37a60df.pdf"},{"title":"Safety Subspaces are Not Distinct: A Fine-Tuning Case Study","url":"https://arxiv.org/html/2505.14185v1"},{"title":"Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study","url":"https://arxiv.org/html/2505.14185"},{"title":"GitHub - CERT-Lab/safety-subspaces: (ICLR '26) Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study · GitHub","url":"https://github.com/CERT-Lab/safety-subspaces"},{"title":"Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study | OpenReview","url":"https://openreview.net/forum?id=Fj6LakRHcT"},{"title":"[2505.14185v2] Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study","url":"https://arxiv.org/abs/2505.14185v2"},{"title":"Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study","url":"https://arxiv.org/pdf/2505.14185"},{"title":"[2505.14185] Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study","url":"https://arxiv.org/abs/2505.14185"}]

I found the research paper you're looking for! Here's what the search results show:

## Paper Overview

The paper demonstrates that safety alignment in LLMs is not confined to distinct subspaces, but rather highly entangled with general ability directions, fundamentally challenging subspace-based defenses.

## Key Findings

Across both weight and activation spaces, subspaces that amplify safe behaviors also amplify useful ones, and prompts with different safety implications activate overlapping representations.

Safety and harmful updates share no relatively significant subspace overlap, confirming that no region of weight space can be isolated specifically for safety.

## Methodology

Mode Subspace Overlap (MSO) is computed between the top-K singular vectors to measure subspace overlap.

## Implications

Safety is highly entangled with the general learning components of the model, suggesting that subspace-based defenses face fundamental limitations and underscoring the need for alternative strategies to preserve safety under continued training.

The findings are corroborated across multiple experiments on five open-source LLMs from the Llama and Qwen families.

The paper was accepted to ICLR 2026 and is available on OpenReview and arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5bff44c-4cb7-4ed8-972c-1161b915e9df",
  "isSidechain": false,
  "promptId": "f21766f1-6940-4f73-a24d-5ba14860739d",
  "type": "user",
  "uuid": "d32c8b97-b151-4dae-b5e6-c539bdd21cbb",
  "toolUseResult": {
    "query": "safety subspaces not linearly distinct MSO mode subspace overlap ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012YecG5FEw3QvxLREBcruXi",
        "content": [
          {
            "title": "SAFETY SUBSPACES ARE NOT LINEARLY DISTINCT",
            "url": "https://openreview.net/pdf/75b8c23862b8fd1143e9069e0ad51e44f37a60df.pdf"
          },
          {
            "title": "Safety Subspaces are Not Distinct: A Fine-Tuning Case Study",
            "url": "https://arxiv.org/html/2505.14185v1"
          },
          {
            "title": "Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study",
            "url": "https://arxiv.org/html/2505.14185"
          },
          {
            "title": "GitHub - CERT-Lab/safety-subspaces: (ICLR '26) Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study · GitHub",
            "url": "https://github.com/CERT-Lab/safety-subspaces"
          },
          {
            "title": "Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study | OpenReview",
            "url": "https://openreview.net/forum?id=Fj6LakRHcT"
          },
          {
            "title": "[2505.14185v2] Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study",
            "url": "https://arxiv.org/abs/2505.14185v2"
          },
          {
            "title": "Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study",
            "url": "https://arxiv.org/pdf/2505.14185"
          },
          {
            "title": "[2505.14185] Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study",
            "url": "https://arxiv.org/abs/2505.14185"
          }
        ]
      },
      "I found the research paper you're looking for! Here's what the search results show:\n\n## Paper Overview\n\nThe paper demonstrates that safety alignment in LLMs is not confined to distinct subspaces, but rather highly entangled with general ability directions, fundamentally challenging subspace-based defenses.\n\n## Key Findings\n\nAcross both weight and activation spaces, subspaces that amplify safe behaviors also amplify useful ones, and prompts with different safety implications activate overlapping representations.\n\nSafety and harmful updates share no relatively significant subspace overlap, confirming that no region of weight space can be isolated specifically for safety.\n\n## Methodology\n\nMode Subspace Overlap (MSO) is computed between the top-K singular vectors to measure subspace overlap.\n\n## Implications\n\nSafety is highly entangled with the general learning components of the model, suggesting that subspace-based defenses face fundamental limitations and underscoring the need for alternative strategies to preserve safety under continued training.\n\nThe findings are corroborated across multiple experiments on five open-source LLMs from the Llama and Qwen families.\n\nThe paper was accepted to ICLR 2026 and is available on OpenReview and arXiv."
    ],
    "durationSeconds": 5.845503305,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c5bff44c-4cb7-4ed8-972c-1161b915e9df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T04:40:53.312Z_

<details><summary>↩ Tool result · `toolu_01XxS5mibZ4VMjeuNhQqqV5t`</summary>

```text
Web search results for query: "MoE mixture of experts safety alignment routing RASA SAFEx sparse safety 2026"

Links: [{"title":"[2602.04448] RASA: Routing-Aware Safety Alignment for Mixture-of-Experts Models","url":"https://arxiv.org/abs/2602.04448"},{"title":"RASA: Routing-Aware Safety Alignment for Mixture-of-Experts Models","url":"https://arxiv.org/pdf/2602.04448"},{"title":"RASA: Routing-Aware Safety Alignment for Mixture-of-Experts Models","url":"https://arxiv.org/html/2602.04448v1"},{"title":"Sparse Models, Sparse Safety: Unsafe Routes in Mixture-of-Experts LLMs","url":"https://arxiv.org/html/2602.08621"},{"title":"UNSAFE ROUTES IN MIXTURE-OF-EXPERTS LLMS","url":"https://openreview.net/pdf/7d11e576b5c6bc5c2789b60f4378fe612305bebd.pdf"}]

Based on the search results, here's what I found about these recent safety alignment approaches for Mixture-of-Experts models:

## RASA (Routing-Aware Safety Alignment)

MoE language models introduce unique challenges for safety alignment due to their sparse routing mechanisms, which can enable degenerate optimization behaviors under standard full-parameter fine-tuning. RASA is a routing-aware expert-level alignment framework that explicitly repairs Safety-Critical Experts while preventing routing-based bypasses. It identifies experts disproportionately activated by successful jailbreaks, selectively fine-tunes only these experts under fixed routing, and subsequently enforces routing consistency with safety-aligned contexts.

RASA achieves near-perfect robustness, strong cross-attack generalization, and substantially reduced over-refusal, while preserving general capabilities on benchmarks such as MMLU, GSM8K, and TruthfulQA. This paper was published in February 2026.

## Sparse Safety Research

Recent research has also examined vulnerabilities in MoE models. MoE-based Transformers use routing mechanisms that dynamically select and activate a subset of specialized experts for each input, substantially reducing training and inference costs while retaining comparable performance to dense models. However, unsafe routes are routing configurations that, when applied to a MoE LLM for a harmful input question, increase the log-likelihood of unsafe model outputs.

## Related Work: SAFEx and SteerMoE

SAFEx identifies safety-critical experts via stability-based selection, and SteerMoE steers behaviors by (de)activating behavior-linked experts, largely by comparing expert activations between safe vs. unsafe modes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f63b47f3-4454-4732-bd42-ecdd872fb6b1",
  "isSidechain": false,
  "promptId": "f21766f1-6940-4f73-a24d-5ba14860739d",
  "type": "user",
  "uuid": "1a306f3e-08ec-4775-a7ff-35e301fcec76",
  "toolUseResult": {
    "query": "MoE mixture of experts safety alignment routing RASA SAFEx sparse safety 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FTn5qXmLzN5eC4EGozWJoM",
        "content": [
          {
            "title": "[2602.04448] RASA: Routing-Aware Safety Alignment for Mixture-of-Experts Models",
            "url": "https://arxiv.org/abs/2602.04448"
          },
          {
            "title": "RASA: Routing-Aware Safety Alignment for Mixture-of-Experts Models",
            "url": "https://arxiv.org/pdf/2602.04448"
          },
          {
            "title": "RASA: Routing-Aware Safety Alignment for Mixture-of-Experts Models",
            "url": "https://arxiv.org/html/2602.04448v1"
          },
          {
            "title": "Sparse Models, Sparse Safety: Unsafe Routes in Mixture-of-Experts LLMs",
            "url": "https://arxiv.org/html/2602.08621"
          },
          {
            "title": "UNSAFE ROUTES IN MIXTURE-OF-EXPERTS LLMS",
            "url": "https://openreview.net/pdf/7d11e576b5c6bc5c2789b60f4378fe612305bebd.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about these recent safety alignment approaches for Mixture-of-Experts models:\n\n## RASA (Routing-Aware Safety Alignment)\n\nMoE language models introduce unique challenges for safety alignment due to their sparse routing mechanisms, which can enable degenerate optimization behaviors under standard full-parameter fine-tuning. RASA is a routing-aware expert-level alignment framework that explicitly repairs Safety-Critical Experts while preventing routing-based bypasses. It identifies experts disproportionately activated by successful jailbreaks, selectively fine-tunes only these experts under fixed routing, and subsequently enforces routing consistency with safety-aligned contexts.\n\nRASA achieves near-perfect robustness, strong cross-attack generalization, and substantially reduced over-refusal, while preserving general capabilities on benchmarks such as MMLU, GSM8K, and TruthfulQA. This paper was published in February 2026.\n\n## Sparse Safety Research\n\nRecent research has also examined vulnerabilities in MoE models. MoE-based Transformers use routing mechanisms that dynamically select and activate a subset of specialized experts for each input, substantially reducing training and inference costs while retaining comparable performance to dense models. However, unsafe routes are routing configurations that, when applied to a MoE LLM for a harmful input question, increase the log-likelihood of unsafe model outputs.\n\n## Related Work: SAFEx and SteerMoE\n\nSAFEx identifies safety-critical experts via stability-based selection, and SteerMoE steers behaviors by (de)activating behavior-linked experts, largely by comparing expert activations between safe vs. unsafe modes."
    ],
    "durationSeconds": 7.648420338,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f63b47f3-4454-4732-bd42-ecdd872fb6b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T04:40:53.809Z_

<details><summary>↩ Tool result · `toolu_0132i795yK3v9A58PLUVE8jw`</summary>

```text
Web search results for query: "alignment quality index latent geometry activation space safety diagnosis EMNLP 2025 2026"

Links: [{"title":"Alignment Quality Index (AQI) : Beyond Refusals: AQI as an Intrinsic Alignment Diagnostic via Latent Geometry, Cluster Divergence, and Layer wise Pooled Representations","url":"https://arxiv.org/pdf/2506.13901"},{"title":"Alignment Quality Index (AQI) : Beyond Refusals: AQI as an Intrinsic Alignment Diagnostic via Latent Geometry, Cluster Divergence, and Layer wise Pooled Representations - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.145/"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Beyond Refusals: AQI as an Intrinsic Alignment","url":"https://aclanthology.org/2025.emnlp-main.145.pdf"},{"title":"AdversariaL attacK sAfety aLIgnment(ALKALI): Safeguarding LLMs through GRACE: Geometric Representation-Aware Contrastive Enhancement- Introducing Adversarial Vulnerability Quality Index (AVQI)","url":"https://arxiv.org/pdf/2506.08885"}]

The search results successfully found the paper you're looking for. Here's what I found:

The paper "Alignment Quality Index (AQI): Beyond Refusals: AQI as an Intrinsic Alignment Diagnostic via Latent Geometry, Cluster Divergence, and Layer wise Pooled Representations" was published in the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP).

The paper introduces the Alignment Quality Index (AQI), a novel geometric and prompt-invariant metric that empirically assesses LLM alignment by analyzing the separation of safe and unsafe activations in latent space. 

AQI combines measures such as the Davies-Bouldin score (DBS), Dunn index (DI), Xie-Beni index (XBI), and Calinski-Harabasz index (CHI) across various formulations to capture clustering quality and detect hidden misalignments and jailbreak risks.

AQI also serves as an early warning signal for alignment faking, offering a robust, decoding-invariant tool for behavior-agnostic safety auditing. The paper demonstrates AQI's correlation with external judges and ability to reveal vulnerabilities missed by refusal metrics across models trained under DPO, GRPO, and RLHF conditions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba52eb49-fb62-4a2d-854f-28fe64ba8818",
  "isSidechain": false,
  "promptId": "f21766f1-6940-4f73-a24d-5ba14860739d",
  "type": "user",
  "uuid": "013a75ed-3684-4db8-bf14-14a80dbca499",
  "toolUseResult": {
    "query": "alignment quality index latent geometry activation space safety diagnosis EMNLP 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019PfDa4TnbVrBgjTNp45qKQ",
        "content": [
          {
            "title": "Alignment Quality Index (AQI) : Beyond Refusals: AQI as an Intrinsic Alignment Diagnostic via Latent Geometry, Cluster Divergence, and Layer wise Pooled Representations",
            "url": "https://arxiv.org/pdf/2506.13901"
          },
          {
            "title": "Alignment Quality Index (AQI) : Beyond Refusals: AQI as an Intrinsic Alignment Diagnostic via Latent Geometry, Cluster Divergence, and Layer wise Pooled Representations - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.145/"
          },
          {
            "title": "Accepted Main Conference Papers - EMNLP 2025",
            "url": "https://2025.emnlp.org/program/main_papers/"
          },
          {
            "title": "Beyond Refusals: AQI as an Intrinsic Alignment",
            "url": "https://aclanthology.org/2025.emnlp-main.145.pdf"
          },
          {
            "title": "AdversariaL attacK sAfety aLIgnment(ALKALI): Safeguarding LLMs through GRACE: Geometric Representation-Aware Contrastive Enhancement- Introducing Adversarial Vulnerability Quality Index (AVQI)",
            "url": "https://arxiv.org/pdf/2506.08885"
          }
        ]
      },
      "The search results successfully found the paper you're looking for. Here's what I found:\n\nThe paper \"Alignment Quality Index (AQI): Beyond Refusals: AQI as an Intrinsic Alignment Diagnostic via Latent Geometry, Cluster Divergence, and Layer wise Pooled Representations\" was published in the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP).\n\nThe paper introduces the Alignment Quality Index (AQI), a novel geometric and prompt-invariant metric that empirically assesses LLM alignment by analyzing the separation of safe and unsafe activations in latent space. \n\nAQI combines measures such as the Davies-Bouldin score (DBS), Dunn index (DI), Xie-Beni index (XBI), and Calinski-Harabasz index (CHI) across various formulations to capture clustering quality and detect hidden misalignments and jailbreak risks.\n\nAQI also serves as an early warning signal for alignment faking, offering a robust, decoding-invariant tool for behavior-agnostic safety auditing. The paper demonstrates AQI's correlation with external judges and ability to reveal vulnerabilities missed by refusal metrics across models trained under DPO, GRPO, and RLHF conditions."
    ],
    "durationSeconds": 6.747150443999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ba52eb49-fb62-4a2d-854f-28fe64ba8818",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Entanglement Geometry of the Alignment Tax Across Dense and MoE Architectures in Agentic Tool-Use Settings  ## D…",
  "leafUuid": "013a75ed-3684-4db8-bf14-14a80dbca499",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate alignment tax geometry proposal acceptance probability",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947"
}
```

---

### Tool result

_source line 24 · 2026-05-20T04:40:53.994Z_

<details><summary>↩ Tool result · `toolu_013cZ5aUYJTqfgbck14CZFih`</summary>

```text
Web search results for query: "agentic safety Pareto frontier DPO tool-use alignment tax 2026"

Links: [{"title":"Safety Training Persists Through Helpfulness Optimization in LLM Agents","url":"https://arxiv.org/pdf/2603.02229"},{"title":"What Is the Alignment Tax?","url":"https://arxiv.org/html/2603.00047v2"},{"title":"Safety Alignment as Continual Learning: Mitigating the Alignment Tax via Orthogonal Gradient Projection","url":"https://arxiv.org/pdf/2602.07892"},{"title":"Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use","url":"https://arxiv.org/pdf/2603.03205"},{"title":"The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents","url":"https://arxiv.org/pdf/2603.20320"},{"title":"Agent Safety Alignment via Reinforcement Learning","url":"https://arxiv.org/pdf/2507.08270"},{"title":"[2510.17426] Navigating the Alignment-Calibration Trade-off: A Pareto-Superior Frontier via Model Merging","url":"https://arxiv.org/abs/2510.17426"},{"title":"Distributional AGI Safety","url":"https://arxiv.org/pdf/2512.16856"},{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"}]

I found several highly relevant research papers on this topic from 2026 and late 2025. Here are the key findings:

## Agentic Safety and Pareto Frontiers

Research on agentic settings (multi-step, tool-use) studies safety using direct preference optimization (DPO) on safety or helpfulness metrics. Studies find that all training configurations end up near a linear Pareto frontier with R² = 0.77.

Interestingly, safety training persists through subsequent helpfulness training, suggesting the two objectives may not be as incompatible as previously thought. However, simultaneously optimizing for safety and helpfulness still resulted in points along the same Pareto frontier rather than discovering "best of both worlds" strategies.

## The Alignment Tax

The "alignment tax" originated informally as a reference to the capability cost of safety. Recent work has systematically measured Pareto fronts between alignment reward and task performance, finding model averaging achieves the best tradeoff.

Recent 2026 papers have proposed methods to mitigate this: Orthogonal Gradient Projection methods consistently improve the safety-utility Pareto frontier across Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and sequential settings.

## Tool-Use Alignment

In tool-using environments, long reasoning traces often omit explicit checks for safety, grounding, or irreversibility, leading to unsafe actions despite extensive deliberation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acde676f-6aa3-4ece-954b-935e7a68211a",
  "isSidechain": false,
  "promptId": "f21766f1-6940-4f73-a24d-5ba14860739d",
  "type": "user",
  "uuid": "dbc0165a-23be-4749-a4e0-916009409733",
  "toolUseResult": {
    "query": "agentic safety Pareto frontier DPO tool-use alignment tax 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013AqF4ihHrDYkTTbwrUG1PW",
        "content": [
          {
            "title": "Safety Training Persists Through Helpfulness Optimization in LLM Agents",
            "url": "https://arxiv.org/pdf/2603.02229"
          },
          {
            "title": "What Is the Alignment Tax?",
            "url": "https://arxiv.org/html/2603.00047v2"
          },
          {
            "title": "Safety Alignment as Continual Learning: Mitigating the Alignment Tax via Orthogonal Gradient Projection",
            "url": "https://arxiv.org/pdf/2602.07892"
          },
          {
            "title": "Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use",
            "url": "https://arxiv.org/pdf/2603.03205"
          },
          {
            "title": "The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents",
            "url": "https://arxiv.org/pdf/2603.20320"
          },
          {
            "title": "Agent Safety Alignment via Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2507.08270"
          },
          {
            "title": "[2510.17426] Navigating the Alignment-Calibration Trade-off: A Pareto-Superior Frontier via Model Merging",
            "url": "https://arxiv.org/abs/2510.17426"
          },
          {
            "title": "Distributional AGI Safety",
            "url": "https://arxiv.org/pdf/2512.16856"
          },
          {
            "title": "Post-Training in 2026: GRPO, DAPO, RLVR & Beyond",
            "url": "https://llm-stats.com/blog/research/post-training-techniques-2026"
          }
        ]
      },
      "I found several highly relevant research papers on this topic from 2026 and late 2025. Here are the key findings:\n\n## Agentic Safety and Pareto Frontiers\n\nResearch on agentic settings (multi-step, tool-use) studies safety using direct preference optimization (DPO) on safety or helpfulness metrics. Studies find that all training configurations end up near a linear Pareto frontier with R² = 0.77.\n\nInterestingly, safety training persists through subsequent helpfulness training, suggesting the two objectives may not be as incompatible as previously thought. However, simultaneously optimizing for safety and helpfulness still resulted in points along the same Pareto frontier rather than discovering \"best of both worlds\" strategies.\n\n## The Alignment Tax\n\nThe \"alignment tax\" originated informally as a reference to the capability cost of safety. Recent work has systematically measured Pareto fronts between alignment reward and task performance, finding model averaging achieves the best tradeoff.\n\nRecent 2026 papers have proposed methods to mitigate this: Orthogonal Gradient Projection methods consistently improve the safety-utility Pareto frontier across Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and sequential settings.\n\n## Tool-Use Alignment\n\nIn tool-using environments, long reasoning traces often omit explicit checks for safety, grounding, or irreversibility, leading to unsafe actions despite extensive deliberation."
    ],
    "durationSeconds": 7.8519516220000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "acde676f-6aa3-4ece-954b-935e7a68211a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T04:40:56.568Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RbiBWuUV3Tndfuu7BbT3yr`</summary>

```json
{
  "query": "hidden dimensions LLM alignment orthogonal safety directions activation space ICML 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbc0165a-23be-4749-a4e0-916009409733",
  "isSidechain": false,
  "requestId": "req_011CbDCupCuVU6aFKSA1L6bz",
  "type": "assistant",
  "uuid": "59ab9942-897a-46c9-ae99-c20f55d618ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS5F5YfWvHgfWGbUKRQJ4C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 704,
      "cache_creation_input_tokens": 3223,
      "cache_read_input_tokens": 24210,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3223,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 704,
          "output_tokens": 173,
          "cache_read_input_tokens": 24210,
          "cache_creation_input_tokens": 3223,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3223
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

_source line 26 · 2026-05-20T04:40:57.501Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TLMxmVSNDK6dtSJu9RuXK9`</summary>

```json
{
  "query": "\"viscosity of logic\" DPO phase transitions beta sweep 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59ab9942-897a-46c9-ae99-c20f55d618ae",
  "isSidechain": false,
  "requestId": "req_011CbDCupCuVU6aFKSA1L6bz",
  "type": "assistant",
  "uuid": "25d3ea41-737a-4f8d-b032-07be11082344",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS5F5YfWvHgfWGbUKRQJ4C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 704,
      "cache_creation_input_tokens": 3223,
      "cache_read_input_tokens": 24210,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3223,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 704,
          "output_tokens": 173,
          "cache_read_input_tokens": 24210,
          "cache_creation_input_tokens": 3223,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3223
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

_source line 27 · 2026-05-20T04:40:57.903Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T1hvByyVbdiSgoGPozStuK`</summary>

```json
{
  "query": "NSPO null-space constrained policy optimization safety alignment ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25d3ea41-737a-4f8d-b032-07be11082344",
  "isSidechain": false,
  "requestId": "req_011CbDCupCuVU6aFKSA1L6bz",
  "type": "assistant",
  "uuid": "630e0035-21f5-4f8e-ab89-03ae2ed948c5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS5F5YfWvHgfWGbUKRQJ4C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 704,
      "cache_creation_input_tokens": 3223,
      "cache_read_input_tokens": 24210,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3223,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 704,
          "output_tokens": 173,
          "cache_read_input_tokens": 24210,
          "cache_creation_input_tokens": 3223,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3223
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

_source line 28 · 2026-05-20T04:41:03.409Z_

<details><summary>↩ Tool result · `toolu_01RbiBWuUV3Tndfuu7BbT3yr`</summary>

```text
Web search results for query: "hidden dimensions LLM alignment orthogonal safety directions activation space ICML 2025"

Links: [{"title":"The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions - CityUHK Scholars","url":"https://scholars.cityu.edu.hk/en/publications/the-hidden-dimensions-of-llm-alignment-a-multi-dimensional-analys/"},{"title":"The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250209674P/abstract"},{"title":"The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions | OpenReview","url":"https://openreview.net/forum?id=wGFEzfhFae"},{"title":"The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions","url":"http://proceedings.mlr.press/v267/pan25f.html"},{"title":"[2502.09674] The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions","url":"https://arxiv.org/abs/2502.09674"},{"title":"The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions","url":"https://arxiv.org/html/2502.09674v4"},{"title":"The Hidden Dimensions of LLM Alignment:","url":"https://arxiv.org/pdf/2502.09674"},{"title":"The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Safety Analysis","url":"https://arxiv.org/html/2502.09674v2"}]

I found the paper you're searching for! Here's what the research reveals:

## Overview

"The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions" was published at ICML 2025, and it examines how language models implement safety alignment.

## Key Findings

Large Language Models' safety-aligned behaviors, such as refusing harmful queries, can be represented by linear directions in activation space. However, previous research modeled safety behavior with a single direction, limiting mechanistic understanding to an isolated safety feature.

The research discovers that safety-aligned behavior is jointly controlled by multi-dimensional directions, studying the vector space of representation shifts during safety fine-tuning on Llama 3 8B for refusing jailbreaks, and finding that a dominant direction governs the model's refusal behavior, while multiple smaller directions represent distinct and interpretable features like hypothetical narrative and role-playing.

## Important Role of Secondary Directions

The researchers measure how different directions promote or suppress the dominant direction, showing the important role of secondary directions in shaping the model's refusal representation.

The paper also explores vulnerabilities, as removing certain trigger tokens in harmful queries can mitigate these directions to bypass the learned safety capability.

Code and artifacts are available at https://github.com/BMPixel/safety-residual-space.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59ab9942-897a-46c9-ae99-c20f55d618ae",
  "isSidechain": false,
  "promptId": "f21766f1-6940-4f73-a24d-5ba14860739d",
  "type": "user",
  "uuid": "67c4c110-1461-424f-8fcb-fb0606d5a752",
  "toolUseResult": {
    "query": "hidden dimensions LLM alignment orthogonal safety directions activation space ICML 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01L8tXQ5QRb6qS1mAXyDyGBZ",
        "content": [
          {
            "title": "The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions - CityUHK Scholars",
            "url": "https://scholars.cityu.edu.hk/en/publications/the-hidden-dimensions-of-llm-alignment-a-multi-dimensional-analys/"
          },
          {
            "title": "The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250209674P/abstract"
          },
          {
            "title": "The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions | OpenReview",
            "url": "https://openreview.net/forum?id=wGFEzfhFae"
          },
          {
            "title": "The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions",
            "url": "http://proceedings.mlr.press/v267/pan25f.html"
          },
          {
            "title": "[2502.09674] The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions",
            "url": "https://arxiv.org/abs/2502.09674"
          },
          {
            "title": "The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions",
            "url": "https://arxiv.org/html/2502.09674v4"
          },
          {
            "title": "The Hidden Dimensions of LLM Alignment:",
            "url": "https://arxiv.org/pdf/2502.09674"
          },
          {
            "title": "The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Safety Analysis",
            "url": "https://arxiv.org/html/2502.09674v2"
          }
        ]
      },
      "I found the paper you're searching for! Here's what the research reveals:\n\n## Overview\n\n\"The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions\" was published at ICML 2025, and it examines how language models implement safety alignment.\n\n## Key Findings\n\nLarge Language Models' safety-aligned behaviors, such as refusing harmful queries, can be represented by linear directions in activation space. However, previous research modeled safety behavior with a single direction, limiting mechanistic understanding to an isolated safety feature.\n\nThe research discovers that safety-aligned behavior is jointly controlled by multi-dimensional directions, studying the vector space of representation shifts during safety fine-tuning on Llama 3 8B for refusing jailbreaks, and finding that a dominant direction governs the model's refusal behavior, while multiple smaller directions represent distinct and interpretable features like hypothetical narrative and role-playing.\n\n## Important Role of Secondary Directions\n\nThe researchers measure how different directions promote or suppress the dominant direction, showing the important role of secondary directions in shaping the model's refusal representation.\n\nThe paper also explores vulnerabilities, as removing certain trigger tokens in harmful queries can mitigate these directions to bypass the learned safety capability.\n\nCode and artifacts are available at https://github.com/BMPixel/safety-residual-space."
    ],
    "durationSeconds": 6.836352971,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "59ab9942-897a-46c9-ae99-c20f55d618ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T04:41:04.266Z_

<details><summary>↩ Tool result · `toolu_01T1hvByyVbdiSgoGPozStuK`</summary>

```text
Web search results for query: "NSPO null-space constrained policy optimization safety alignment ICLR 2026"

Links: [{"title":"Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=GFyVxtyMvq"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2512.11391"},{"title":"Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2512.11391"},{"title":"Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization","url":"https://arxiv.org/html/2512.11391v1"},{"title":"(PDF) Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization","url":"https://www.researchgate.net/publication/398675733_Mitigating_the_Safety_Alignment_Tax_with_Null-Space_Constrained_Policy_Optimization"},{"title":"[2512.11391] Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization","url":"https://arxiv.org/abs/2512.11391"},{"title":"MITIGATING THE SAFETY ALIGNMENT TAX WITH NULL- ...","url":"https://openreview.net/pdf/4bf58e070f2718ae978f627889060e956c044fc4.pdf"}]

Based on the search results, here's what I found about NSPO:

## Overview

NSPO (Null-Space constrained Policy Optimization) is a novel RL framework for LLM safety alignment that preserves core abilities by geometrically projecting safety policy gradients into the null space of general tasks, thereby mitigating the safety alignment tax.

## Key Problem

Safety alignment under Reinforcement Learning often suffers from forgetting learned general abilities, which is also known as the alignment tax. The root cause is that the safety gradient weakens the model's learned general capabilities.

## Technical Approach

The method geometrically projects safety policy gradients into the null space of general task representations, constraining the safety updates to be orthogonal to the subspace spanned by the model's general capabilities.

## Key Results

NSPO outperforms existing methods by a large margin, achieving state-of-the-art safety performance without sacrificing accuracy on general tasks, including math, code, and instruction-following tasks. Additionally, NSPO is data-efficient and only requires 40% of public human-annotated safety data from PKU-SafeRLHF to achieve promising safety performance, without a large amount of mixed general tasks data.

## Theoretical Guarantees

NSPO theoretically preserves the model's original core capabilities, while still guaranteeing a descent direction for effective safety alignment.

The paper was published as a conference paper at ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "630e0035-21f5-4f8e-ab89-03ae2ed948c5",
  "isSidechain": false,
  "promptId": "f21766f1-6940-4f73-a24d-5ba14860739d",
  "type": "user",
  "uuid": "969fd3e2-67f7-4db3-b441-5b823310ef6a",
  "toolUseResult": {
    "query": "NSPO null-space constrained policy optimization safety alignment ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016Xgrk6wtNHxDfY5sojmY6g",
        "content": [
          {
            "title": "Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization | OpenReview",
            "url": "https://openreview.net/forum?id=GFyVxtyMvq"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2512.11391"
          },
          {
            "title": "Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2512.11391"
          },
          {
            "title": "Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization",
            "url": "https://arxiv.org/html/2512.11391v1"
          },
          {
            "title": "(PDF) Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization",
            "url": "https://www.researchgate.net/publication/398675733_Mitigating_the_Safety_Alignment_Tax_with_Null-Space_Constrained_Policy_Optimization"
          },
          {
            "title": "[2512.11391] Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization",
            "url": "https://arxiv.org/abs/2512.11391"
          },
          {
            "title": "MITIGATING THE SAFETY ALIGNMENT TAX WITH NULL- ...",
            "url": "https://openreview.net/pdf/4bf58e070f2718ae978f627889060e956c044fc4.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about NSPO:\n\n## Overview\n\nNSPO (Null-Space constrained Policy Optimization) is a novel RL framework for LLM safety alignment that preserves core abilities by geometrically projecting safety policy gradients into the null space of general tasks, thereby mitigating the safety alignment tax.\n\n## Key Problem\n\nSafety alignment under Reinforcement Learning often suffers from forgetting learned general abilities, which is also known as the alignment tax. The root cause is that the safety gradient weakens the model's learned general capabilities.\n\n## Technical Approach\n\nThe method geometrically projects safety policy gradients into the null space of general task representations, constraining the safety updates to be orthogonal to the subspace spanned by the model's general capabilities.\n\n## Key Results\n\nNSPO outperforms existing methods by a large margin, achieving state-of-the-art safety performance without sacrificing accuracy on general tasks, including math, code, and instruction-following tasks. Additionally, NSPO is data-efficient and only requires 40% of public human-annotated safety data from PKU-SafeRLHF to achieve promising safety performance, without a large amount of mixed general tasks data.\n\n## Theoretical Guarantees\n\nNSPO theoretically preserves the model's original core capabilities, while still guaranteeing a descent direction for effective safety alignment.\n\nThe paper was published as a conference paper at ICLR 2026."
    ],
    "durationSeconds": 6.359758129000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "630e0035-21f5-4f8e-ab89-03ae2ed948c5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T04:41:05.845Z_

<details><summary>↩ Tool result · `toolu_01TLMxmVSNDK6dtSJu9RuXK9`</summary>

```text
Web search results for query: ""viscosity of logic" DPO phase transitions beta sweep 2026"

Links: [{"title":"[2601.17260] The Viscosity of Logic: Phase Transitions and Hysteresis in DPO Alignment","url":"https://arxiv.org/abs/2601.17260"},{"title":"The Viscosity of Logic: Phase Transitions and Hysteresis in DPO Alignment","url":"https://arxiv.org/html/2601.17260v1"},{"title":"Phase behavior and glass transition of 1,2-dioleoylphosphatidylethanolamine (DOPE) dehydrated in the presence of sucrose - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/11513808/"},{"title":"Viscosity peaks at the reentrant isotropic phase transitions","url":"https://www.researchgate.net/publication/330912928_Viscosity_peaks_at_the_reentrant_isotropic_phase_transitions_a_rheological_study"},{"title":"Viscosity Near Phase Transitions","url":"https://ui.adsabs.harvard.edu/abs/arXiv:1010.0015"},{"title":"$\\eta/s$ and Phase Transitions","url":"https://arxiv.org/pdf/0803.3275"},{"title":"Minimal model for beta relaxation in viscous liquids","url":"https://arxiv.org/pdf/cond-mat/0305558"}]

I found relevant search results! Here's what I found about "The Viscosity of Logic: Phase Transitions and Hysteresis in DPO Alignment":

## Overview

"The Viscosity of Logic" treats β as a control parameter and densely sweeps it for three 7B open-weight families under a fixed DPO recipe.

## Key Findings

**Phase Transitions and Architecture-Specific Responses:**
Across architectures under the same sweep, qualitatively different response modes were observed: sharp reorganization in Mistral, selective changes in Llama, and smooth trade-offs in Qwen. In Mistral, capability is sharply non-monotonic: aggregated logic-probe margins become positive only in a narrow band near β ≈ 10⁻² and revert outside it, with boundary points that are seed-sensitive.

**The Margin-Capability Problem:**
The DPO preference margin can anticorrelate with reasoning capability (Pearson r=-0.91 for Llama logic), so margin-based selection can prefer capability-impaired models.

**Hysteresis Effects:**
Training path also matters: exposure to high β induces capability losses that persist even after β is reduced (hysteresis).

The paper was published on January 24, 2026, and suggests that capability-resolved evaluation across the β landscape is needed rather than reliance on margins or aggregate benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25d3ea41-737a-4f8d-b032-07be11082344",
  "isSidechain": false,
  "promptId": "f21766f1-6940-4f73-a24d-5ba14860739d",
  "type": "user",
  "uuid": "405c8230-25f9-4d1f-905e-34d8bb64d1a4",
  "toolUseResult": {
    "query": "\"viscosity of logic\" DPO phase transitions beta sweep 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01McP5noh6qf3WpVeGTgzjpK",
        "content": [
          {
            "title": "[2601.17260] The Viscosity of Logic: Phase Transitions and Hysteresis in DPO Alignment",
            "url": "https://arxiv.org/abs/2601.17260"
          },
          {
            "title": "The Viscosity of Logic: Phase Transitions and Hysteresis in DPO Alignment",
            "url": "https://arxiv.org/html/2601.17260v1"
          },
          {
            "title": "Phase behavior and glass transition of 1,2-dioleoylphosphatidylethanolamine (DOPE) dehydrated in the presence of sucrose - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/11513808/"
          },
          {
            "title": "Viscosity peaks at the reentrant isotropic phase transitions",
            "url": "https://www.researchgate.net/publication/330912928_Viscosity_peaks_at_the_reentrant_isotropic_phase_transitions_a_rheological_study"
          },
          {
            "title": "Viscosity Near Phase Transitions",
            "url": "https://ui.adsabs.harvard.edu/abs/arXiv:1010.0015"
          },
          {
            "title": "$\\eta/s$ and Phase Transitions",
            "url": "https://arxiv.org/pdf/0803.3275"
          },
          {
            "title": "Minimal model for beta relaxation in viscous liquids",
            "url": "https://arxiv.org/pdf/cond-mat/0305558"
          }
        ]
      },
      "I found relevant search results! Here's what I found about \"The Viscosity of Logic: Phase Transitions and Hysteresis in DPO Alignment\":\n\n## Overview\n\n\"The Viscosity of Logic\" treats β as a control parameter and densely sweeps it for three 7B open-weight families under a fixed DPO recipe.\n\n## Key Findings\n\n**Phase Transitions and Architecture-Specific Responses:**\nAcross architectures under the same sweep, qualitatively different response modes were observed: sharp reorganization in Mistral, selective changes in Llama, and smooth trade-offs in Qwen. In Mistral, capability is sharply non-monotonic: aggregated logic-probe margins become positive only in a narrow band near β ≈ 10⁻² and revert outside it, with boundary points that are seed-sensitive.\n\n**The Margin-Capability Problem:**\nThe DPO preference margin can anticorrelate with reasoning capability (Pearson r=-0.91 for Llama logic), so margin-based selection can prefer capability-impaired models.\n\n**Hysteresis Effects:**\nTraining path also matters: exposure to high β induces capability losses that persist even after β is reduced (hysteresis).\n\nThe paper was published on January 24, 2026, and suggests that capability-resolved evaluation across the β landscape is needed rather than reliance on margins or aggregate benchmarks."
    ],
    "durationSeconds": 8.340602884999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "25d3ea41-737a-4f8d-b032-07be11082344",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-20T04:41:05.857Z_

```json
{
  "parentUuid": "405c8230-25f9-4d1f-905e-34d8bb64d1a4",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1a4981d9-b57f-466d-b367-a18a3ee74017",
  "timestamp": "2026-05-20T04:41:05.857Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-20T04:41:09.903Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have a solid understanding of the key papers. Let me do a couple more targeted searches to understand potential competing work and the experimental standards in this area.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a4981d9-b57f-466d-b367-a18a3ee74017",
  "isSidechain": false,
  "requestId": "req_011CbDCvgrvBLNa54N7E3spQ",
  "type": "assistant",
  "uuid": "a4ddb618-9454-433b-8b27-65bda8d3dafb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DU5kQDxp8fm4xsGq5fGHPr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 765,
      "cache_creation_input_tokens": 2497,
      "cache_read_input_tokens": 27433,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2497,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 765,
          "output_tokens": 178,
          "cache_read_input_tokens": 27433,
          "cache_creation_input_tokens": 2497,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2497
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

_source line 33 · 2026-05-20T04:41:10.945Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019VFKNaPZnd7bFKQTxApEv7`</summary>

```json
{
  "query": "cross-space correspondence parameter space activation space alignment safety geometry bridge 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4ddb618-9454-433b-8b27-65bda8d3dafb",
  "isSidechain": false,
  "requestId": "req_011CbDCvgrvBLNa54N7E3spQ",
  "type": "assistant",
  "uuid": "88442aca-c793-4db7-bd19-e91c8db165db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DU5kQDxp8fm4xsGq5fGHPr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 765,
      "cache_creation_input_tokens": 2497,
      "cache_read_input_tokens": 27433,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2497,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 765,
          "output_tokens": 178,
          "cache_read_input_tokens": 27433,
          "cache_creation_input_tokens": 2497,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2497
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

_source line 34 · 2026-05-20T04:41:11.688Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lyy8YQC1VLvk5WnTgro9si`</summary>

```json
{
  "query": "LoRA DPO safety alignment 30B MoE Qwen3 large model safety fine-tuning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88442aca-c793-4db7-bd19-e91c8db165db",
  "isSidechain": false,
  "requestId": "req_011CbDCvgrvBLNa54N7E3spQ",
  "type": "assistant",
  "uuid": "a48a4449-8c63-4f30-ad5e-c738461e3888",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DU5kQDxp8fm4xsGq5fGHPr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 765,
      "cache_creation_input_tokens": 2497,
      "cache_read_input_tokens": 27433,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2497,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 765,
          "output_tokens": 178,
          "cache_read_input_tokens": 27433,
          "cache_creation_input_tokens": 2497,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2497
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

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Entanglement Geometry of the Alignment Tax Across Dense and MoE Architectures in Agentic Tool-Use Settings  ## D…",
  "leafUuid": "a48a4449-8c63-4f30-ad5e-c738461e3888",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate alignment tax geometry proposal acceptance probability",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947"
}
```

---

### Tool result

_source line 37 · 2026-05-20T04:41:17.401Z_

<details><summary>↩ Tool result · `toolu_019VFKNaPZnd7bFKQTxApEv7`</summary>

```text
Web search results for query: "cross-space correspondence parameter space activation space alignment safety geometry bridge 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 ACTIVATIONREASONING:","url":"https://arxiv.org/pdf/2510.18184"},{"title":"(PDF) The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety","url":"https://www.researchgate.net/publication/400894456_The_Geometry_of_Alignment_Collapse_When_Fine-Tuning_Breaks_Safety"},{"title":"Revisiting Robustness for LLM Safety Alignment via Selective Geometry Control","url":"https://arxiv.org/pdf/2602.07340"},{"title":"(PDF) The Geometry of Alignment Collapse: A Critical Review and Multimodal Synthesis","url":"https://www.academia.edu/164808347/The_Geometry_of_Alignment_Collapse_A_Critical_Review_and_Multimodal_Synthesis"},{"title":"The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety","url":"https://arxiv.org/pdf/2602.15799"},{"title":"CLNet: Cross-View Correspondence Makes a Stronger Geo-Localizationer","url":"https://arxiv.org/pdf/2512.14560"},{"title":"AI Safety 2026: Alignment Progress and Open Challenges | Claude 5 Hub","url":"https://claude5.com/news/ai-safety-2026-alignment-progress-and-open-challenges"},{"title":"Alignment Quality Index (AQI) : Beyond Refusals: AQI as an Intrinsic Alignment Diagnostic via Latent Geometry, Cluster Divergence, and Layer wise Pooled Representations","url":"https://arxiv.org/pdf/2506.13901"}]

The search results reveal research on several interconnected topics in AI safety and model interpretability from 2026:

**Activation Space and Geometric Approaches to Safety:**

Recent work proposes inspecting representational geometry rather than relying solely on behavioral outputs, with the Alignment Quality Index (AQI) providing an intrinsic diagnostic that evaluates latent activations for alignment fidelity.

**Parameter Space and Safety Geometry:**

Research shows that preserving alignment during fine-tuning requires identifying parameters most sensitive to safety behavior, with some weights encoding safety-critical functions while others govern task-general behavior, and alignment-critical parameters defined as those whose perturbation disproportionately alters a model's refusal response.

**Alignment Collapse and Fine-Tuning:**

Work on the geometry of alignment collapse operates in weight space, where the Fisher Information Matrix's eigenvectors define alignment-sensitive directions.

**Activation Space Interpretability:**

Raw LLM activations are highly entangled and subject to superposition, but researchers project activations into a sparse and more interpretable feature space using Sparse Autoencoders (SAEs) to promote monosemanticity by aligning individual dimensions with distinct, human-interpretable concepts.

These papers collectively address how geometric and representational properties of neural networks relate to safety alignment, activation space organization, and parameter space structure.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88442aca-c793-4db7-bd19-e91c8db165db",
  "isSidechain": false,
  "promptId": "f21766f1-6940-4f73-a24d-5ba14860739d",
  "type": "user",
  "uuid": "6e42e923-05b3-49c7-8c0c-f2a1b06979dc",
  "toolUseResult": {
    "query": "cross-space correspondence parameter space activation space alignment safety geometry bridge 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EhJVpz5x2YjFBSJeUqHvxe",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026 ACTIVATIONREASONING:",
            "url": "https://arxiv.org/pdf/2510.18184"
          },
          {
            "title": "(PDF) The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety",
            "url": "https://www.researchgate.net/publication/400894456_The_Geometry_of_Alignment_Collapse_When_Fine-Tuning_Breaks_Safety"
          },
          {
            "title": "Revisiting Robustness for LLM Safety Alignment via Selective Geometry Control",
            "url": "https://arxiv.org/pdf/2602.07340"
          },
          {
            "title": "(PDF) The Geometry of Alignment Collapse: A Critical Review and Multimodal Synthesis",
            "url": "https://www.academia.edu/164808347/The_Geometry_of_Alignment_Collapse_A_Critical_Review_and_Multimodal_Synthesis"
          },
          {
            "title": "The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety",
            "url": "https://arxiv.org/pdf/2602.15799"
          },
          {
            "title": "CLNet: Cross-View Correspondence Makes a Stronger Geo-Localizationer",
            "url": "https://arxiv.org/pdf/2512.14560"
          },
          {
            "title": "AI Safety 2026: Alignment Progress and Open Challenges | Claude 5 Hub",
            "url": "https://claude5.com/news/ai-safety-2026-alignment-progress-and-open-challenges"
          },
          {
            "title": "Alignment Quality Index (AQI) : Beyond Refusals: AQI as an Intrinsic Alignment Diagnostic via Latent Geometry, Cluster Divergence, and Layer wise Pooled Representations",
            "url": "https://arxiv.org/pdf/2506.13901"
          }
        ]
      },
      "The search results reveal research on several interconnected topics in AI safety and model interpretability from 2026:\n\n**Activation Space and Geometric Approaches to Safety:**\n\nRecent work proposes inspecting representational geometry rather than relying solely on behavioral outputs, with the Alignment Quality Index (AQI) providing an intrinsic diagnostic that evaluates latent activations for alignment fidelity.\n\n**Parameter Space and Safety Geometry:**\n\nResearch shows that preserving alignment during fine-tuning requires identifying parameters most sensitive to safety behavior, with some weights encoding safety-critical functions while others govern task-general behavior, and alignment-critical parameters defined as those whose perturbation disproportionately alters a model's refusal response.\n\n**Alignment Collapse and Fine-Tuning:**\n\nWork on the geometry of alignment collapse operates in weight space, where the Fisher Information Matrix's eigenvectors define alignment-sensitive directions.\n\n**Activation Space Interpretability:**\n\nRaw LLM activations are highly entangled and subject to superposition, but researchers project activations into a sparse and more interpretable feature space using Sparse Autoencoders (SAEs) to promote monosemanticity by aligning individual dimensions with distinct, human-interpretable concepts.\n\nThese papers collectively address how geometric and representational properties of neural networks relate to safety alignment, activation space organization, and parameter space structure."
    ],
    "durationSeconds": 6.449962120999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "88442aca-c793-4db7-bd19-e91c8db165db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T04:41:19.361Z_

<details><summary>↩ Tool result · `toolu_01Lyy8YQC1VLvk5WnTgro9si`</summary>

```text
Web search results for query: "LoRA DPO safety alignment 30B MoE Qwen3 large model safety fine-tuning 2026"

Links: [{"title":"How to Fine Tune Qwen: The Complete Guide to LLM Refinement - H3sync","url":"https://h3sync.com/blog/how-to-fine-tune-qwen/"},{"title":"Qwen3 - How to Run & Fine-tune | Unsloth Documentation","url":"https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune"},{"title":"Fine-Tuning Qwen/Qwen3-VL-30B-A3B MoE Architecture with LoRA | by Shaaf Salman | Medium","url":"https://medium.com/@ishaafsalman/fine-tuning-qwen-qwen3-vl-30b-a3b-moe-architecture-with-lora-2365359e870f"},{"title":"Defending MoE LLMs against Harmful Fine-Tuning via Safety Routing Alignment","url":"https://arxiv.org/html/2509.22745v1"},{"title":"Decoupling Safety into Orthogonal Subspace: Cost-Efficient and Performance-Preserving Alignment for Large Language Models","url":"https://arxiv.org/pdf/2510.09004"},{"title":"Safe LoRA: the Silver Lining of Reducing Safety Risks when Fine-tuning   Large Language Models","url":"https://arxiv.org/pdf/2405.16833"},{"title":"Safe Pruning LoRA: Robust Distance-Guided Pruning for Safety Alignment in Adaptation of LLMs","url":"https://arxiv.org/pdf/2506.18931"}]

I found relevant search results on this topic. Here's what the search returned:

## Key Findings:

**Safety Alignment and Fine-tuning in 2026:**
In 2026, the standard pipeline is SFT followed by DPO, where SFT provides the 'what,' and DPO provides the 'how' in terms of quality and alignment.

**Qwen3 30B MoE Support:**
Fine-tuning support includes a 2026 Faster MOE update with 30B-A3B and 235B-A22B models, with Qwen3-30B-A3B working on just 17.5GB VRAM with Unsloth.

**LoRA Fine-tuning for MoE Models:**
For fine-tuning MoE models, it's probably not a good idea to fine-tune the router layer so it's disabled by default. Additionally, Qwen3-VL-30B-A3B-Instruct is a vision-language model with 30B total parameters and 3B activated per token.

**LoRA for Safety Alignment:**
LoRA-based safety alignment has three key advantages: it's performance-preserving by substantially reducing jailbreak attack success rates while maintaining general capabilities, cost-efficient through training on safety data alone, and plug-and-play as lightweight modular components.

**Research on MoE Safety:**
The search also returned research on defending MoE LLMs against harmful fine-tuning, with experiments conducted on Qwen3-30B-A3B and other MoE models, with all models used being safety-aligned versions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a48a4449-8c63-4f30-ad5e-c738461e3888",
  "isSidechain": false,
  "promptId": "f21766f1-6940-4f73-a24d-5ba14860739d",
  "type": "user",
  "uuid": "4c794c47-22b5-429b-80cb-0e473e59493a",
  "toolUseResult": {
    "query": "LoRA DPO safety alignment 30B MoE Qwen3 large model safety fine-tuning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BgbMweznGgyc2jCknvc6Fg",
        "content": [
          {
            "title": "How to Fine Tune Qwen: The Complete Guide to LLM Refinement - H3sync",
            "url": "https://h3sync.com/blog/how-to-fine-tune-qwen/"
          },
          {
            "title": "Qwen3 - How to Run & Fine-tune | Unsloth Documentation",
            "url": "https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune"
          },
          {
            "title": "Fine-Tuning Qwen/Qwen3-VL-30B-A3B MoE Architecture with LoRA | by Shaaf Salman | Medium",
            "url": "https://medium.com/@ishaafsalman/fine-tuning-qwen-qwen3-vl-30b-a3b-moe-architecture-with-lora-2365359e870f"
          },
          {
            "title": "Defending MoE LLMs against Harmful Fine-Tuning via Safety Routing Alignment",
            "url": "https://arxiv.org/html/2509.22745v1"
          },
          {
            "title": "Decoupling Safety into Orthogonal Subspace: Cost-Efficient and Performance-Preserving Alignment for Large Language Models",
            "url": "https://arxiv.org/pdf/2510.09004"
          },
          {
            "title": "Safe LoRA: the Silver Lining of Reducing Safety Risks when Fine-tuning   Large Language Models",
            "url": "https://arxiv.org/pdf/2405.16833"
          },
          {
            "title": "Safe Pruning LoRA: Robust Distance-Guided Pruning for Safety Alignment in Adaptation of LLMs",
            "url": "https://arxiv.org/pdf/2506.18931"
          }
        ]
      },
      "I found relevant search results on this topic. Here's what the search returned:\n\n## Key Findings:\n\n**Safety Alignment and Fine-tuning in 2026:**\nIn 2026, the standard pipeline is SFT followed by DPO, where SFT provides the 'what,' and DPO provides the 'how' in terms of quality and alignment.\n\n**Qwen3 30B MoE Support:**\nFine-tuning support includes a 2026 Faster MOE update with 30B-A3B and 235B-A22B models, with Qwen3-30B-A3B working on just 17.5GB VRAM with Unsloth.\n\n**LoRA Fine-tuning for MoE Models:**\nFor fine-tuning MoE models, it's probably not a good idea to fine-tune the router layer so it's disabled by default. Additionally, Qwen3-VL-30B-A3B-Instruct is a vision-language model with 30B total parameters and 3B activated per token.\n\n**LoRA for Safety Alignment:**\nLoRA-based safety alignment has three key advantages: it's performance-preserving by substantially reducing jailbreak attack success rates while maintaining general capabilities, cost-efficient through training on safety data alone, and plug-and-play as lightweight modular components.\n\n**Research on MoE Safety:**\nThe search also returned research on defending MoE LLMs against harmful fine-tuning, with experiments conducted on Qwen3-30B-A3B and other MoE models, with all models used being safety-aligned versions."
    ],
    "durationSeconds": 7.643238010000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a48a4449-8c63-4f30-ad5e-c738461e3888",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T04:42:02.672Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have sufficient background to evaluate this proposal. Let me synthesize my findings and provide a thorough assessment.

Key observations from my research:

1. **The core papers cited are real and accurately described**:
   - "What Is the Geometry of the Alignment Tax?" (arXiv 2603.00047) - real paper, purely theoretical
   - "Safety Subspaces are Not Linearly Distinct" (ICLR 2026) - real, introduces MSO
   - "Hidden Dimensions of LLM Alignment" (ICML 2025) - real, multi-dimensional safety directions
   - Plaut's "Safety Training Persists" (arXiv 2603.02229) - real, near-linear frontier
   - RASA, SAFEx, and other MoE safety papers - all verified
   - NSPO (ICLR 2026) - real null-space projection method
   - AQI (EMNLP 2025) - real paper on latent geometry for alignment diagnosis

2. **The gap identification seems legitimate**: No existing work connects parameter-space MSO to activation-space principal angles. The cross-space bridge is indeed missing.

3. **Concerns**: This is primarily an empirical measurement paper rather than proposing a new method or intervention, and the experimental design appears incomplete.

The scope is ambitious—a 2×2 factorial with 16 β values across multiple models and benchmarks, requiring substantial computational resources (3,500-5,000 GPU-hours, $10,500-15,000). The proposal tries to deliver three distinct contributions, each substantial enough to stand alone. The pre-registered outcome topology is clever but also feels like a hedge—ensuring the work will be informative regardless of what the data shows. There's also a timing mismatch: the proposal targets ICLR 2027, AAAI 2027, and ICML 2027, but I'm evaluating it for EMNLP 2026, which is slightly odd but doesn't affect the quality assessment.

The proposal has real strengths: a thorough literature survey, genuine identification of an understudied gap between MSO and principal angles, a well-executed factorial design with clear statistical rigor, and thoughtful contingency planning. But the core weakness is that this is fundamentally a measurement and characterization paper—it diagnoses and measures rather than proposing new methods or interventions. While EMNLP accepts such work, the bar is high, and the scope creep across three contributions (the cross-space bridge, diagnostic dual-estimation, and MoE stress test) makes it feel unfocused rather than cohesive.

The cross-space correspondence itself might underwhelm—if MSO and the representation-level metric correlate, it's somewhat expected since they're measuring related safety-capability geometry; if they don't, the takeaway is just that they're different things operating in different spaces. The statistical power is also questionable with only eight conditions across four models and two settings, and the dense versus MoE comparison conflates multiple variables like active parameter counts and training data. The resource demands of 3,500 to 5,000 GPU-hours are substantial, which raises the stakes for what the findings need to deliver.

If the Maverick experiment fails and I fall back to Qwen3-30B-A3B, the comparison shifts dramatically from 22B active parameters down to 3.3B, which changes the entire experimental narrative. The geometric explanation for Plaut's linear frontier also feels somewhat circular—if high entanglement produces a small α that makes the ellipse nearly linear, how do I statistically distinguish between elliptic and linear models? The proposal acknowledges this with a fallback to small-α cases, but that weakens the core claim. There's also a risk of reviewer fatigue given how dense the proposal is with many interconnected components, making it hard to identify what the central contribution actually is. For EMNLP, the topic itself is relevant to the conference, though the methodology needs to be evaluated carefully.

Looking at this holistically, the proposal is well-researched and thoughtfully designed, but it's primarily an empirical characterization without intervention or real-world application, it's overscoped with three contributions when one or two would be stronger, and some of the contributions could end up underwhelming regardless of how the experiments turn out. The resource requirements are also substantial. I'd put this at around 25-35% probability for acceptance at a top venue—the phenomenon is real, but the paper might not provide enough actionable insight beyond documenting what we measured.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c794c47-22b5-429b-80cb-0e473e59493a",
  "isSidechain": false,
  "requestId": "req_011CbDCwgbKH3y4K6psDJvmC",
  "type": "assistant",
  "uuid": "e599a0b3-945d-41af-a951-95e5a5ed6002",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvJy9Xkw5agqNL28EDqjfF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2608,
      "cache_read_input_tokens": 29930,
      "output_tokens": 6317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2608,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6317,
          "cache_read_input_tokens": 29930,
          "cache_creation_input_tokens": 2608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2608
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

_source line 40 · 2026-05-20T04:43:55.755Z_

Now I have sufficient research to evaluate this proposal. Let me compile my assessment.

```
【阶段】: Triage

【领域调研】:
- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047) (arXiv, Mar 2026): The theoretical foundation this proposal builds on. Purely theoretical — proves Pareto frontier is an ellipse parameterized by principal angle α. Explicitly notes limitations under large perturbations and nonlinear encoding. No empirical validation exists yet, which is the gap this proposal targets.
- [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185) (ICLR 2026): Introduces MSO in parameter space; shows safety-capability subspaces are highly entangled on Llama 2/3.2 and Qwen 2.5 (1B–7B), chat only. Core tool for this proposal's C1 contribution. Confirmed real and accurately described.
- [The Hidden Dimensions of LLM Alignment](https://arxiv.org/abs/2502.09674) (ICML 2025): Multi-dimensional orthogonal safety directions in activation space on Llama 3 8B. Chat only. Provides the activation-space methodology for principal angle extraction. Accurately cited.
- [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229) (Plaut, Mar 2026): Observes near-linear Pareto frontier (R²=0.77) in agentic DPO on 8B–14B dense models with only 2 β values. No representation analysis, no MoE. This is the key empirical observation the proposal aims to geometrically explain.
- [RASA: Routing-Aware Safety Alignment](https://arxiv.org/abs/2602.04448) (Feb 2026): Shows safety in MoE is routing-mediated; full-parameter fine-tuning creates routing shortcuts. Restoring original routing collapses harmlessness by Δ∈[−0.38, −0.46]. Key evidence for C3.
- [Sparse Models, Sparse Safety](https://arxiv.org/abs/2602.08621) (Feb 2026): RoSais scores show masking 5 routers increases ASR 4× to 0.79. Further evidence that MoE safety is structurally different from dense safety.
- [NSPO](https://arxiv.org/abs/2512.11391) (ICLR 2026): Null-space projection method that assumes separable subspaces. This proposal argues if MSO and α_repr don't correspond, NSPO-like methods and activation-space diagnostics may be analyzing different structures.
- [The Viscosity of Logic](https://arxiv.org/abs/2601.17260) (Jan 2026): Phase transitions in DPO β sweeps on 7B models. Motivates the dense β sampling design. Architecture-specific responses found (sharp in Mistral, smooth in Qwen).
- [AQI](https://aclanthology.org/2025.emnlp-main.145/) (EMNLP 2025): Uses cluster divergence metrics on safe/unsafe activations for alignment diagnosis without generation. Most directly related prior work using representation geometry for alignment quality. Differs in using cluster quality (scalar) vs. principal angles (structural).
- 调研总结: The gap identification is legitimate — no prior work connects parameter-space MSO to activation-space principal angles, tests the geometric framework on MoE architectures, or provides geometric explanation for Plaut's near-linear agentic frontier. However, this is an extremely crowded and fast-moving area (20+ papers in 3 months), and the proposal's contribution is fundamentally characterization/measurement rather than a new method or intervention.

【整体印象】:
如果我是审稿人，第一反应是：这是一份极其 well-researched 的 proposal，文献调研几乎无可挑剔，实验设计也非常严谨（pre-registered outcome topology、Bayesian model comparison、分层优先级）。但随之而来的第二反应是：这到底在贡献什么？三个 contributions 加在一起构成的是一个大型 empirical characterization study，但缺乏 actionable 的方法论输出——不提出新的 alignment 方法、不提出新的优化算法、不构建新的 benchmark。它的核心是"测量并桥接两个已有的度量系统"，这在 significance 上面临挑战。

我会倾向于 **borderline reject**，理由是：(1) 核心贡献是诊断/测量性质的，缺乏直接的 actionable impact；(2) 过度铺展三个贡献导致每个都不够深入；(3) 部分结论可能无论结果如何都是"意料之中"的（MSO和α要么相关——说明它们测量相似结构，要么不相关——说明它们测量不同结构，两个结论都不够 surprising）。

【核心贡献】:
核心贡献是建立 parameter-space (MSO) 和 activation-space (principal angle α) 两个独立度量系统之间的 cross-space correspondence，并在 agentic + MoE 设置下测试几何理论框架的适用性。这本质上是一个 metrological/diagnostic 贡献——回答"我们已有的两套工具是否在测量同一个底层现象？"以及"理论框架在更复杂的架构和设置下是否成立？"

对领域的价值：中等。如果发现 MSO 和 α_repr 高度对应，这为 parameter-space 干预方法（NSPO、OGPSA）和 activation-space 诊断方法提供了统一的理论基础，有实际意义。如果发现不对应，则警告社区不要混用两种范式。但无论哪种结果，直接影响偏间接——不会立即改变任何人的训练/对齐流程。

MoE 作为几何框架的 stress test（C3）可能是最有趣的贡献，因为它直接关系到前沿模型（大多是 MoE 架构）的 alignment 实践。但这也是资源消耗最大、最可能出现技术障碍的部分。

【方法合理性】:
方法设计本身是合理且严谨的。2×2 factorial design、16-point β sweep、Bayesian model comparison（PSIS-LOO + WAIC）、pre-registered outcome topology——这些都是方法论上的良好实践。

然而，存在几个合理性质疑：

1. **Cross-space correspondence 的 layer-wise mixed-effects 分析**：用 ~80-100 个 (MSO_layer, α_repr_layer) 数据点做 mixed-effects model，每个 model-setting 条件只有 ~10-15 个 layers——这有严重的 pseudoreplication 风险。层与层之间高度非独立（特别是相邻层），mixed-effects model 的 random intercept 不足以解决这个问题。

2. **α_repr vs. α_frontier 的比较**：α_repr 来自 Phase 1（representation analysis），α_frontier 来自 Phase 3（elliptic fit to Pareto frontier）。但 α_frontier 的估计依赖于 elliptic model 的拟合优度——如果大多数条件下 elliptic 和 linear model 不可区分（小 α scenario），α_frontier 的 uncertainty 会很大，使得 dual-estimation test 失去 power。

3. **更简单的替代方案**：直接对比 dense vs. MoE 模型在相同 DPO 设置下的 Pareto frontier 形状，配合 representation probing，可能用 1/3 的资源达到 80% 的 insight。Cross-space bridge 和 diagnostic dual-estimation 增加了大量复杂性，但边际信息增益不确定。

4. **Dense vs. MoE 的 confounding**：即使 Qwen3 family 内部比较，32B dense vs. 22B active MoE 在 active parameter count 上差 50%。FLOP-normalized analysis 帮助但不能完全消除 confound。

【5 维度打分】:

1. 研究问题: **中** — 问题是真实存在的：parameter-space 和 activation-space 的度量确实从未被连接，MoE 安全的几何理解确实缺失，Plaut 的近线性 frontier 确实缺乏解释。但这些更像是"测量空白"而非"理解瓶颈"——填补它们不会直接解决任何 alignment 的实际问题。对比同类工作：AQI (EMNLP 2025) 被接收是因为它提出了一个可直接使用的诊断工具；NSPO (ICLR 2026) 被接收是因为它提出了一个有效的优化方法。本 proposal 的输出更接近"characterization report"，在顶会中的价值定位不够清晰。

2. 方法与创新: **中** — 方法论设计严谨（Bayesian model comparison、pre-registered outcomes、mixed-effects analysis），但创新主要在于"将已有工具组合应用于新设置"，而非提出新的分析工具或方法。Cross-space correspondence 是 MSO (ICLR 2026) + principal angles (arXiv 2603.00047) 的直接组合；MoE routing analysis 基本沿用 RASA (arXiv 2602.04448) 和 RoSais (arXiv 2602.08621) 的方法。Pre-registered outcome topology 是一个亮点，但更多是"好的实验实践"而非"方法创新"。

3. 实验设计: **强** — 这是 proposal 最突出的优势。16-point β sweep（远超 Plaut 的 2 点）、2×2 factorial design（覆盖 dense/MoE × chat/agent）、Bayesian model comparison 而非 p-value hacking、多种 evaluation benchmarks（tau2-bench, OpenAgentSafety, ATBench, AdvBench）、sensitivity ablations（rank K, data source, token position）、power simulation before data collection、tiered priority system with fallback plans。这是顶会级别的实验设计。如果执行到位，实验部分本身没有明显漏洞。

4. 可行性: **中偏弱** — 3,500-5,000 GPU-hours / $10,500-15,000 是一笔不小的开支。16 周时间线紧张但可行。最大风险点：(a) Maverick (400B total) 的 DPO 训练可能因内存问题不可行——proposal 承认了这一点并有 fallback，但 fallback 到 Qwen3-30B-A3B (3.3B active) 会大幅改变实验 narrative（从"前沿规模 MoE"变成"小规模 MoE"）；(b) 在 30B+ 模型上进行 128 runs (4 models × 2 settings × 16 β) 的 DPO 训练，加上 representation extraction 和 evaluation，需要非常高效的工程实践；(c) 多个 benchmark 的集成（tau2-bench, OpenAgentSafety, ATBench）增加了工程复杂度。对于一个不是大型实验室的团队来说，这个规模可能过于雄心勃勃。

5. 写作与呈现: **中偏强** — Proposal 的文献覆盖极其全面（30+ 篇相关工作，每篇都精确定位与本工作的关系），逻辑结构清晰（Core Problem → Opportunity → Landscape → Approach → Resource）。但存在两个写作问题：(a) **过度密集**——信息密度太高，审稿人需要花大量精力理解三个 contributions 之间的关系和每个的具体内容，可能导致 reviewer fatigue；(b) **narrative 不够聚焦**——试图同时服务四个 narrative（cross-space bridge, geometric explanation of linearity, MoE stress test, probing-based prediction），核心 story 不够突出。

【概率估计】: [18% - 32%] 中位 25%

【估计理由】:
**向上因素**：(1) Gap 是真实的，文献调研无懈可击，没有直接竞争的 concurrent work；(2) 实验设计非常严谨，方法论上挑不出大问题；(3) Pre-registered outcome topology 是审稿人喜欢的实验设计范式；(4) 如果 C3（MoE stress test）得出强结论（如 MoE 几何完全不同于 dense），这对前沿 alignment 实践有实际指导意义。

**向下因素**：(1) **核心身份问题**——这是 characterization/measurement paper，不提出新方法或工具，在 top venue 的 impact bar 上处于劣势，审稿人可能评价为 "interesting but incremental"；(2) **三个 contributions 的聚焦度不足**——每个 contribution 独立来看都是"测量 X 和 Y 是否对应"或"在新设置下验证已有框架"，没有任何一个强到可以单独撑起一篇顶会；(3) **可预测性风险**——部分结论无论结果如何都不够 surprising（如果 MSO 和 α 对应：expected since both capture safety-capability geometry；如果不对应：trivially expected since they're in different spaces）；(4) **资源可行性**——如果 Maverick 不可行且 fallback 到小规模 MoE，C3 的 narrative 弱化严重；(5) **小 α scenario**——如果大多数条件下 α < 10°，C2 的 elliptic-vs-linear discrimination 可能 inconclusive，fallback 到 "quantifying upper bound" 虽然 informative 但不够 exciting。

中位 25% 的定位理由：实验设计扎实将其拉到合格线以上，但 characterization paper 的身份和 significance 不足将其压在"需要运气"的区间。一个友好的审稿人组可能给 borderline accept，但大概率会有至少一个审稿人质疑 "so what?"。

【主要风险】:
1. **"So what?" 风险**：审稿人质疑——"你测量了 MSO 和 α 的对应关系，发现它们对应/不对应，然后呢？这如何改变我们做 alignment 的方式？"缺乏从诊断到行动的闭环（proposal 明确排除了 intervention phase），这在顶会中是常见的 reject 理由。
2. **Scope 过大导致执行不完整**：128 runs DPO + representation extraction + multi-benchmark evaluation + MoE routing analysis，如果任何环节出现技术困难（Maverick 不可行、某个 benchmark 集成有 bug、某些 β 值训练不稳定），整个 2×2 design 的完整性就会受损，paper 会变成"我们做了一部分实验，结论是 preliminary"。

【实施评估】:
  - 计算资源: 3,500-5,000 GPU-hours (4-8×H100)，$10,500-15,000。属于中等偏大规模实验，需要稳定的 GPU 集群访问或充足的 cloud budget。
  - 数据需求: 主要依赖已有 benchmark（OpenAgentSafety, ATBench, AdvBench, tau2-bench, BeaverTails）。不需要构建新数据集，但需要集成多个异构 benchmark 的 evaluation pipeline，工程量不小。
  - 人工介入: 中等。probe code、evaluation pipeline 搭建需要扎实的工程能力。统计分析（Bayesian model comparison, mixed-effects modeling）需要统计学专业知识。
  - 训练需求: 是，需要对 4 个 30B+ 模型进行 LoRA-DPO 训练，每个模型 16 个 β 值 × 2 个 setting。MoE 模型的 DPO 训练可能需要 reference model offloading 等特殊处理。
  - 新 Benchmark: 否，不需要构建新 benchmark。
  - 预估周期: 16 周（proposal 自估），考虑到工程调试和不可预见问题，20 周更现实。
```

Sources:
- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047)
- [Safety Subspaces are Not Linearly Distinct (ICLR 2026)](https://arxiv.org/abs/2505.14185)
- [The Hidden Dimensions of LLM Alignment (ICML 2025)](https://arxiv.org/abs/2502.09674)
- [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229)
- [RASA: Routing-Aware Safety Alignment for MoE Models](https://arxiv.org/abs/2602.04448)
- [Sparse Models, Sparse Safety](https://arxiv.org/abs/2602.08621)
- [NSPO (ICLR 2026)](https://arxiv.org/abs/2512.11391)
- [The Viscosity of Logic](https://arxiv.org/abs/2601.17260)
- [AQI (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.145/)
- [The Geometry of Alignment Collapse](https://arxiv.org/abs/2602.15799)
- [OGPSA](https://arxiv.org/abs/2602.07892)
- [SAFEx](https://arxiv.org/abs/2506.17368)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e599a0b3-945d-41af-a951-95e5a5ed6002",
  "isSidechain": false,
  "requestId": "req_011CbDCwgbKH3y4K6psDJvmC",
  "type": "assistant",
  "uuid": "4cc671c9-f361-4a4f-b770-885d4fc6014b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvJy9Xkw5agqNL28EDqjfF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2608,
      "cache_read_input_tokens": 29930,
      "output_tokens": 6317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2608,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6317,
          "cache_read_input_tokens": 29930,
          "cache_creation_input_tokens": 2608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2608
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

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Entanglement Geometry of the Alignment Tax Across Dense and MoE Architectures in Agentic Tool-Use Settings  ## D…",
  "leafUuid": "4cc671c9-f361-4a4f-b770-885d4fc6014b",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate alignment tax geometry proposal acceptance probability",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Entanglement Geometry of the Alignment Tax Across Dense and MoE Architectures in Agentic Tool-Use Settings  ## D…",
  "leafUuid": "4cc671c9-f361-4a4f-b770-885d4fc6014b",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate alignment tax geometry proposal acceptance probability",
  "sessionId": "0dfc5970-8988-49d4-b50a-c17e1afa7947"
}
```

---
