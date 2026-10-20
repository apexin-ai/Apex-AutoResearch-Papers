# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Certifiable Manipulation Resistan

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/bf282443-299e-4737-b983-aec70555c4b7.jsonl`
- **Structured JSON:** [`a6f95e31920cc1c1c7d5.json`](../../sessions/a6/a6f95e31920cc1c1c7d5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:50:23.925Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:50:23.925Z",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation Structure\n\n## Description\n\nLLM evaluation faces systematic adversarial vulnerabilities—open-source judge models show 50–68% average attack success rates (SoK, April 2026, arXiv 2603.29403), and arena rankings can be flipped with ~1,000 strategic votes (ICML 2025). While Robertson & Koyejo (2025, arXiv 2508.05469) proved bounded f-divergence certification for single evaluators, concurrent works established peer prediction incentive-compatibility (Qiu et al., ICLR 2026; Chen et al., NeurIPS 2025), and Kaneko & Baldwin (NeurIPS 2025 spotlight, arXiv 2510.17000) proved tight single-model attack cost bounds (N_min ≥ log₂(1/ε)/I_max), no work provides formal N-judge manipulation-cost scaling as a function of measurable inter-judge correlation.\n\nWe establish the **adversarial dual of diversity scaling** and reveal a fundamental asymmetry. Yang et al. (ICLR 2026 Workshop AIMS, arXiv 2602.03794) proved task performance improves exponentially—residual uncertainty decays as (1-α_c)^{K*} via effective channel count K* = 2^{H(ρ)}. We prove the complementary result: adversarial manipulation cost grows only **polynomially** as Ω(K_eff^{1/2}). The structural reason for this asymmetry: stochastic evaluation errors are **incoherent** across judges and concentrate exponentially via standard inequalities, but adversarial perturbations are **coherent**—the adversary's shared perturbation reintroduces cross-judge coupling, limiting gains to polynomial variance reduction. This asymmetry implies diversity is fundamentally more cost-effective for accuracy than for robustness—a non-obvious result with direct resource-allocation implications.\n\nAs a co-primary contribution, we characterize how PEG's (Chen et al., NeurIPS 2025, arXiv 2505.13636) dominant-strategy truthfulness, requiring conditional independence (Assumption 4), degrades under partial correlation: ε-approximate equilibrium with ε = f(ρ) provides a continuous degradation curve from dominant-strategy (ρ=0) to approximate (ρ→1) regimes. No existing work provides this analysis.\n\nOur proof proceeds in two steps: (1) SDPI per-channel bounds (Polyanskiy & Wu, arXiv 1508.06025) constrain each judge's information leakage to at most I_max per query; across K parallel judges, total adversary information gain is bounded additively by K_eff · I_max. (2) Variance-reduction arguments (Horvath et al., arXiv 2106.06946) yield perturbation energy scaling as Ω(K_eff^{1/2}), giving g(I_max) = ½·log(K_eff)/log(K). The ½ exponent is derived from continuous-space (ℓ₂) variance reduction; for discrete text perturbations, we state it as a conjecture supported by the continuous analogue and test it empirically via adaptive attacks.\n\nUnder Turkmen et al.'s (arXiv 2602.08003) equicorrelated Gaussian copula: K_eff = 1+(K-1)·exp(-2·I_max). For heterogeneous correlation, K* = 2^{H(ρ)} (Yang et al.) serves as an upper-bound approximation of effective dimensionality in the adversarial context; its validity is tested via copula goodness-of-fit and empirical tightness experiments.\n\nA provocative implication: as frontier model capability increases, Kim et al. (ICML 2025, arXiv 2506.07962) show error correlations increase even across providers/architectures. Under our framework, this drives K_eff → 1 regardless of ensemble size, suggesting **certified manipulation-resistance may be fundamentally bounded at the frontier**—a \"diversity ceiling\" where adding more capable judges yields diminishing certified robustness returns even as accuracy continues to improve.\n\nThe framework also serves as a **prescriptive judge-selection tool**: K_eff maximization for certified robustness vs. Turkmen et al.'s MI maximization for accuracy—these may yield different optimal ensembles. We validate against 15 off-the-shelf attacks plus three protocol-aware adaptive attacks on SummEval, LiveCodeBench, and GPQA Diamond, with compute-normalized (FLOP-matched) baselines and copula model validation.\n\n## Core Problem\nCan we provide certifiable manipulation-resistance guarantees for N-judge LLM evaluation protocols, where the certified robustness bound is an explicit, computable function of measurable inter-judge signal correlation, validated against both off-the-shelf and protocol-aware adaptive adversarial attacks?\n\n## Opportunity\nThree critical gaps: (1) No formal N-agent scaling connecting manipulation cost to measurable inter-judge signal correlation. Robertson & Koyejo (arXiv 2508.05469) analyze pairwise evaluations; Chen et al.'s PEG (NeurIPS 2025, arXiv 2505.13636) requires conditional independence (Assumption 4) without characterizing degradation. (2) Empirical validation lacks adaptive attacks targeting multi-judge protocols (Carlini et al., arXiv 1902.06705 standard). (3) Yang et al.'s diversity-scaling (arXiv 2602.03794) addresses performance only—no adversarial dual exists, and the exponential-polynomial asymmetry is unknown.\n\nTurkmen et al. (arXiv 2602.08003): correlated ensemble error floor Φ(Φ⁻¹(1-p)/√ρ), MI decomposition for α estimation. Kaneko & Baldwin (NeurIPS 2025, arXiv 2510.17000): tight single-model bounds, no multi-judge composition. SoK (arXiv 2603.29403): 7-model committees reduce ASR to 10–19% without formal explanation. Qiu et al. (ICLR 2026, arXiv 2601.20299): BNE guarantees for truthfulness, not adversarial robustness.\n\n## Landscape\n**Single-evaluator foundations.** Robertson & Koyejo (arXiv 2508.05469, TMLR under review): TVD-MI, polynomial certification (Theorem 3.3), AUC 0.70–0.77. Identity-Link IRT follow-up (arXiv 2510.14966): sparse evaluation, two-judge validation (ρ=0.872).\n\n**Peer prediction.** Qiu et al. (ICLR 2026, arXiv 2601.20299): BNE guarantees, output truthfulness. Chen et al. PEG (NeurIPS 2025, arXiv 2505.13636): dominant strategy (Lemma 1), O(√T) regret (Theorem 2), Nash convergence (Theorem 3), conditional independence (Assumption 4)—degradation under violation uncharacterized.\n\n**Diversity scaling.** Yang et al. (ICLR 2026 Workshop AIMS, arXiv 2602.03794): K* = 2^{H(ρ)}, (1-α_c)^{K*} decay (Theorem 4.3), heterogeneity advantage (Corollary 4.4). Performance only.\n\n**Correlation models.** Turkmen et al. (arXiv 2602.08003): Gaussian copula, error floor (Theorem 4.4), MI decomposition (Theorem 4.3), within-family ρ~0.7-0.8, cross-family ρ~0.4-0.5. Kim et al. (ICML 2025, arXiv 2506.07962): 60% error agreement, +0.066 same-company, +0.076 same-architecture; larger/more accurate models more correlated even across providers. Chen et al. behavioral entanglement (arXiv 2604.07650): BEI/CIG, cross-family 40–60% lower.\n\n**Single-model adversarial bounds.** Kaneko & Baldwin (NeurIPS 2025 spotlight, arXiv 2510.17000): N_min ≥ log₂(1/ε)/I_max (Theorem 1), SPRT achievability (Theorem 2), four disclosure regimes.\n\n**Certifiable evaluation under noise.** Shen et al. (arXiv 2604.03257): constrained MLE, honest judges. Feng et al. (ICLR 2026, arXiv 2601.20913): hypothesis testing, Type-I error control (Theorem 5.1), variance-corrected thresholds (Theorem 5.4). Both assume non-adversarial judges.\n\n**Semantic/representational collapse.** Kong et al. (arXiv 2605.17193, May 2026): closed-loop multi-LLM systems exhibit semantic collapse across 200–1000 rounds; 12 interventions fail. Patel (arXiv 2604.03809): effective rank 2.17/3.0 for homogeneous committees. Both apply to **iterative closed-loop** settings. Our single-pass evaluation protocol (independent scoring, no inter-judge communication) avoids the feedback loops driving collapse; K_eff serves as a principled detector if diversity erosion occurs.\n\n**Scaling dissociation.** Jung & Na (arXiv 2604.00477): scoring reliability logarithmic, discovery N^0.69 power law.\n\n**Attack/defense landscape.** SoK (arXiv 2603.29403): 50–68% ASR open-source, 27–44% frontier, 7-model → 10–19%. RobustJudge (arXiv 2506.09443): 15 attacks, 7 defenses. CAP (OpenReview 2026): comparative assessment, no formal guarantees. Carlini et al. (arXiv 1902.06705): adaptive attack gold standard.\n\n**Coordination failure.** Frongillo et al. (arXiv 2503.16280): fine-grained signals destabilize uninformative equilibria. Keppo et al. (arXiv 2603.20281): 2→5 LLMs breaks collusion (+22%→+3%).\n\n**Multi-agent evaluation.** CollabEval (arXiv 2603.00993): three-phase, no adversarial guarantees. Ebrahimi et al. (IJCNLP-AACL 2025, arXiv 2505.24239): credibility-based aggregation.\n\n**Certified ensemble robustness.** Chen et al. (arXiv 2107.10873): diversified gradient + confidence margin necessary/sufficient. Horvath et al. (arXiv 2106.06946): √K certified radius via variance reduction. Both in continuous perturbation spaces.\n\nTHE KEY GAP: No formal N-agent manipulation-cost scaling as a function of measurable correlation; no characterization of the exponential-polynomial asymmetry between performance and robustness scaling; no PEG degradation analysis under correlation violation.\n\n## Approach\n\nFive components:\n\n**Component 1: Theoretical Framework—The Asymmetric Adversarial Dual.**\n\nWe prove manipulation cost grows as Ω(K_eff^{1/2}), establishing an asymmetric duality with Yang et al.'s exponential performance scaling. The structural origin: stochastic errors are incoherent across judges (exponential concentration), but adversarial perturbations are coherent (shared perturbation reintroduces coupling → polynomial variance reduction only). This implies a fundamental resource-allocation insight: the marginal robustness value of each additional judge diminishes faster than its marginal accuracy value.\n\n*Step 1—Per-Channel SDPI Bound.* Each judge is a noisy channel; SDPI (Polyanskiy & Wu, arXiv 1508.06025) bounds per-channel information leakage to I_max. K parallel judges yield additive total: K_eff · I_max per round. Extends Kaneko & Baldwin's single-channel N_min.\n\n*Step 2—Variance Reduction to Manipulation Cost.* Fano-ensemble decomposition (Morishita et al., ICML 2022, arXiv 2205.12683) into relevance, redundancy, combination loss. Marton's inequality (TV² ≤ ½·KL) + Robertson & Koyejo's Theorem 3.3 → perturbation energy Ω(K_eff^{1/2}). Exponent: g(I_max) = ½·log(K_eff)/log(K). Boundaries: g(0) = ½ (independent), g → 0 (fully correlated).\n\n*Copula Closed Form.* Turkmen et al.'s equicorrelated model: K_eff = 1+(K-1)·exp(-2·I_max), I_max = -½ log(1-ρ²). Eigenvalues λ₁ = 1+(K-1)ρ, λ₂ = 1-ρ.\n\n*Heterogeneous Extension.* K* = 2^{H(ρ)} (Yang et al.) as upper-bound approximation of adversarial effective dimensionality, yielding g ≥ ½·log(K*)/log(K). K*'s validity in the adversarial context (vs. its original performance context) is an approximation justified by the shared eigenstructure and validated empirically via tightness experiments.\n\n*Exponent Status.* The ½ exponent derives from continuous-space (ℓ₂) variance reduction (Horvath et al., arXiv 2106.06946). For discrete text perturbations, the perturbation geometry differs; we state ½ as a conjecture for the discrete evaluation setting, supported by the continuous analogue, and test it empirically. Whether the true discrete exponent is better or worse than ½ is an open question.\n\n*Frontier Diversity Ceiling.* Kim et al. (ICML 2025) show error correlations increase with model capability even across providers/architectures. Under our framework, this drives K_eff → 1 as ρ → 1, implying certified manipulation-resistance may face a fundamental ceiling at the frontier: adding more capable judges yields diminishing certified robustness returns even as accuracy improves. We examine this empirically and discuss its implications.\n\n**Component 2: PEG Guarantee Degradation + α Regime Analysis.**\n\n*Co-primary contribution.* PEG's dominant-strategy truthfulness (Lemma 1, Assumption 4 conditional independence; Chen et al., NeurIPS 2025, arXiv 2505.13636) degrades under correlation: ε-approximate equilibrium with ε = f(ρ). This degradation pattern may extend to other conditional-independence-assuming mechanisms in peer prediction, though we prove it specifically for PEG.\n\nα estimates using external priors (Turkmen et al. ρ~0.4-0.5; Kim et al. +0.066/+0.076) **validated via direct measurement** in pilot study. Note: Kim et al.'s agreement rate and copula ρ are different quantities; we derive the mapping explicitly.\n- Central: ρ ≈ 0.45, α ∈ [0.35, 0.65], K=7: 2.65–3.7×\n- Sensitivity: α=0.2 → 1.55×; α=0.8 → 5.2×; vacuous at α ≤ 0.05 (ρ ≥ 0.95)\n- Score-coverage dissociation (Jung & Na, arXiv 2604.00477): analyze certified bound saturation rate\n\n**Component 3: Practical Protocol Design.**\n\nThree families: DeepSeek-V4-Flash (284B MoE, 13B active), Qwen-3.5 (397B MoE, 17B active), Llama-4-Maverick (400B MoE, 17B active). Backups: Gemma-2-27B (dense, non-MoE), Mistral-Large-2, Command-R+.\n\nThree phases: (1) Independence measurement (calibration ≥500 samples for copula GoF; sensitivity at {100, 200, 500, 1000, 2000}); (2) TVD-MI evaluation + DMI-weighted aggregation (PEG, Chen et al., NeurIPS 2025); (3) Certification: Ω(K^α) bound with measured α.\n\nPrescriptive judge selection: K_eff maximization (robustness) vs. MI maximization (accuracy, Turkmen et al.) may yield different optimal ensembles.\n\n**Component 4: Certifiable Robustness Framing.**\n\nA defense showing 15% empirical ASR under today's 15 known attacks provides no guarantee against tomorrow's attacks—an adaptive adversary could spike ASR back to 60% with a novel strategy. Our framework guarantees Ω(K^α) manipulation cost regardless of attack strategy. Same value proposition as randomized smoothing: modest certified margins, but provable guarantees. Kaneko & Baldwin's per-judge N_min × K_eff gives multi-judge certified resistance.\n\n**Component 5: Adversarial Validation, PEG Degradation Testing, and Model Assumption Validation.**\n\n*Benchmarks.* SummEval (summarization; CAP comparison; broader quality metrics beyond factuality), LiveCodeBench (code; contamination-resistant, frontier-discriminative), GPQA Diamond (knowledge-intensive QA; discriminative for open-weight judges).\n\n*Threat models.* Black-box (aggregated output only), gray-box (judge identities known, individual outputs hidden), white-box (all outputs + DMI weights visible).\n\n*Off-the-shelf attacks.* RobustJudge's 15 methods + SoK vectors.\n\n*Adaptive attacks (Carlini et al., arXiv 1902.06705):*\n(a) Correlation-exploiting (gray/white): optimize perturbation to simultaneously fool high-ρ pairs; transfer-based optimization on proxy models if full MoE gradient infeasible.\n(b) Aggregation-targeting (white): optimize to shift aggregated score beyond certified bound.\n(c) Weakest-link (gray): concentrate on highest-I_max channel.\n(d) Best-effort tightness (white): PGD on MoE active parameters (13-17B, feasible per-forward-pass); fallback to PAIR + random-search hybrid. Budget: 10,000 queries. Convergence: <0.5% ASR improvement over last 2,000 queries. Report ASR-vs-budget curve with convergence annotation.\n\n*Compute-normalized baselines (FLOP-matched):*\n(a) Frontier single-model (GPT-4o-latest or Claude Sonnet).\n(b) Self-consistency: DeepSeek-V4-Flash × 7 (different temperatures/prompts), majority voting. Reports per-query FLOPs and wall-clock time.\n\n*Other baselines.* 7 RobustJudge defenses; CAP; CollabEval (arXiv 2603.00993); Ebrahimi et al. (IJCNLP-AACL 2025, arXiv 2505.24239); Robertson & Koyejo single-evaluator TVD-MI; majority voting K=3,5,7; PEG with DMI scoring.\n\n*PEG degradation validation.* Dedicated experiment: construct 5-7 judge panels spanning ρ from within-family (~0.7-0.8) to all-cross-family (~0.4-0.5) via mixed composition. For each panel, measure ρ_ij directly. Introduce a strategic deviator judge (via prompt injection) and measure its expected payoff gain vs. truthful baseline—payoff gain > 0 provides empirical ε lower bound. Report (measured_ρ, empirical_ε) scatter against theoretical f(ρ) curve. Track DMI regret across panels.\n\n*Dual-scaling validation.* In K-scaling ablation (K=1,2,3,5,7), simultaneously measure: (a) non-adversarial accuracy (Spearman/Kendall with ground truth), fitting (1-α_c)^{K*} model (report R²); (b) adversarial manipulation cost (empirical query count + certified bound), fitting K^α model (report R²). Overlay both curves (log-scale y-axis) to visualize exponential-polynomial asymmetry.\n\n*Model assumption validation.*\n(a) Full K×K ρ_ij matrix; Var(ρ_ij) for equicorrelation deviation.\n(b) Copula GoF (Anderson-Darling, minimum n=500; 50-100 for ρ stability only).\n(c) If GoF rejects: Kendall's tau rank correlation for dependence estimation; K* from rank-correlation matrix. Report Pearson-based vs. Kendall-based K* gap.\n(d) Heterogeneous bound (K*) vs. closed-form bound gap.\n\n*Ablations.*\n(a) K-scaling: K=1,2,3,5,7 (with dual-scaling overlay).\n(b) Diversity-type 2×2: {same-org, diff-org} × {same-arch-type, diff-arch-type}, ≥1 non-MoE model (Gemma-2-27B).\n(c) Accuracy-robustness tradeoff: MI-maximization vs. K_eff-maximization ensemble selection; Pareto frontier.\n(d) α sensitivity: [0.2, 0.8].\n(e) Calibration sensitivity: ρ at {100, 200, 500, 1000, 2000}; cross-domain calibration transfer (3×3 benchmark matrix: use ρ from benchmark A to compute bound for B, report transferred vs. in-domain bound deviation and ρ cross-domain stability); bootstrap error propagation to CI.\n\n*Statistical rigor.* ≥3 seeds (mean ± std). ρ: bootstrap 95% CI. Primary correction: Benjamini-Hochberg FDR. Conservative check on core claims: Bonferroni. Report uncorrected, BH-adjusted, and Bonferroni-adjusted values.\n\n*Pilot study (Weeks 1-2, ~100 H100-hrs).* ρ_ij on 500 samples per benchmark. Go/no-go: ρ > 0.7 → switch to backups. If all open-weight models show ρ > 0.7, report as empirical finding supporting the frontier diversity ceiling.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '1,800-2,800 H100-equivalent', 'timeline': '18-24 weeks', 'estimated_gpu_cost': '$4,500-$7,000 at $2.50/hr', 'gpu_breakdown': 'Pilot ~100; single-judge baselines ~450; multi-judge protocol ~500; adaptive attacks (transfer/PAIR + tightness PGD) ~500; compute-normalized baselines ~50 + ~$300 API; copula/calibration/cross-domain ~100; PEG degradation validation ~80; diversity + accuracy-robustness ablation ~200; K-scaling + dual-scaling ~200; multi-seed ~300; dev/debug ~150'}, 'human_in_loop': {'gpu_hours': '1,400-2,200', 'timeline': '14-18 weeks', 'claude_api_cost': '$400-$600'}, 'auto_research': {'gpu_hours': '2,100-3,000', 'timeline': '9-13 weeks', 'claude_api_cost': '$1,200-$2,000'}}\n\n## Inspired By\nSeven lines: (1) Robertson & Koyejo bounded f-divergence (arXiv 2508.05469); (2) Qiu et al. BNE (ICLR 2026, arXiv 2601.20299) + Chen et al. PEG (NeurIPS 2025, arXiv 2505.13636); (3) Yang et al. K* diversity-scaling (ICLR 2026 Workshop AIMS, arXiv 2602.03794); (4) Turkmen et al. copula model (arXiv 2602.08003); (5) Kaneko & Baldwin single-model bounds (NeurIPS 2025 spotlight, arXiv 2510.17000); (6) SoK 7-model ASR reduction (arXiv 2603.29403); (7) Error correlation/entanglement (Chen et al. arXiv 2604.07650; Kim et al. ICML 2025, arXiv 2506.07962).\n\n## Target Venues\n- ICLR 2027 (estimated: October 2026; primary—full theory + comprehensive experiments)\n- AAAI 2027 (abstract: July 21, 2026; stretch goal)\n- USENIX Security 2027 Cycle 1 (August 2026; security-focused)\n- NeurIPS 2026 Workshops (~August 29, 2026)\n\n## Key References\n- Let's Measure Information Step-by-Step (Robertson & Koyejo, arXiv 2508.05469, 2025)\n- Identity-Link IRT (Robertson, arXiv 2510.14966, 2025)\n- Truthfulness Despite Weak Supervision (Qiu et al., ICLR 2026, arXiv 2601.20299)\n- PEG (Chen et al., NeurIPS 2025, arXiv 2505.13636)\n- Understanding Agent Scaling via Diversity (Yang et al., ICLR 2026 Workshop AIMS, arXiv 2602.03794)\n- Don't Always Pick the Highest-Performing Model (Turkmen et al., arXiv 2602.08003, 2026)\n- Bits Leaked per Query (Kaneko & Baldwin, NeurIPS 2025 spotlight, arXiv 2510.17000)\n- Robust LLM Performance Certification (Shen et al., arXiv 2604.03257, 2026)\n- Noisy but Valid (Feng et al., ICLR 2026, arXiv 2601.20913)\n- Logarithmic Scores, Power-Law Discoveries (Jung & Na, arXiv 2604.00477, 2026)\n- SoK: Security in LLM-as-a-Judge (arXiv 2603.29403, April 2026)\n- RobustJudge (arXiv 2506.09443, 2025)\n- Correlated Errors in LLMs (Kim et al., ICML 2025, arXiv 2506.07962)\n- Behavioral Entanglement (Chen et al., arXiv 2604.07650, 2026)\n- Benchmark Illusion (arXiv 2602.11898, 2026)\n- Strong Data-Processing Inequalities (Polyanskiy & Wu, arXiv 1508.06025, 2017)\n- Rethinking Fano's Inequality in Ensemble Learning (Morishita et al., ICML 2022, arXiv 2205.12683)\n- Certified Robustness for Ensemble Models (Chen et al., arXiv 2107.10873, 2021)\n- Boosting Randomized Smoothing with Variance Reduced Classifiers (Horvath et al., arXiv 2106.06946, 2021)\n- Information-Theoretically Optimal Adversarial Attacks (Yi et al., arXiv 2007.14042, 2020)\n- On the Fragility of AI Agent Collusion (Keppo et al., arXiv 2603.20281, 2026)\n- CollabEval (arXiv 2603.00993, March 2026)\n- Adversary-Resistant Multi-Agent via Credibility Scoring (Ebrahimi et al., IJCNLP-AACL 2025, arXiv 2505.24239)\n- Certifying Joint Adversarial Robustness for Ensembles (Chiang et al., arXiv 2004.10250, 2020)\n- Peer Prediction with More Signals than Reports (Frongillo et al., arXiv 2503.16280, 2025)\n- Adversarial Manipulation of Voting-Based Leaderboards (ICML 2025)\n- Vote Rigging on Chatbot Arena (ICML 2025)\n- am-ELO: Stable Arena-based Evaluation (ICML 2025 Poster)\n- CAP: Comparative Augmented Prompting (OpenReview 2026)\n- Aligned Textual Scoring Rules (Lu et al., arXiv 2507.06221, 2025)\n- Can You Trick the Grader? (EMNLP 2025 Findings)\n- On Evaluating Adversarial Robustness (Carlini et al., arXiv 1902.06705, 2019)\n- Multi-LLM Systems Exhibit Robust Semantic Collapse (Kong et al., arXiv 2605.17193, May 2026)\n- Representational Collapse in Multi-Agent LLM Committees (Patel, arXiv 2604.03809, April 2026)\n- LiveCodeBench (arXiv 2403.07974, 2024)"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T05:50:23.928Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:50:23.928Z",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-20T05:50:23.979Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation Structure

## Description

LLM evaluation faces systematic adversarial vulnerabilities—open-source judge models show 50–68% average attack success rates (SoK, April 2026, arXiv 2603.29403), and arena rankings can be flipped with ~1,000 strategic votes (ICML 2025). While Robertson & Koyejo (2025, arXiv 2508.05469) proved bounded f-divergence certification for single evaluators, concurrent works established peer prediction incentive-compatibility (Qiu et al., ICLR 2026; Chen et al., NeurIPS 2025), and Kaneko & Baldwin (NeurIPS 2025 spotlight, arXiv 2510.17000) proved tight single-model attack cost bounds (N_min ≥ log₂(1/ε)/I_max), no work provides formal N-judge manipulation-cost scaling as a function of measurable inter-judge correlation.

We establish the **adversarial dual of diversity scaling** and reveal a fundamental asymmetry. Yang et al. (ICLR 2026 Workshop AIMS, arXiv 2602.03794) proved task performance improves exponentially—residual uncertainty decays as (1-α_c)^{K*} via effective channel count K* = 2^{H(ρ)}. We prove the complementary result: adversarial manipulation cost grows only **polynomially** as Ω(K_eff^{1/2}). The structural reason for this asymmetry: stochastic evaluation errors are **incoherent** across judges and concentrate exponentially via standard inequalities, but adversarial perturbations are **coherent**—the adversary's shared perturbation reintroduces cross-judge coupling, limiting gains to polynomial variance reduction. This asymmetry implies diversity is fundamentally more cost-effective for accuracy than for robustness—a non-obvious result with direct resource-allocation implications.

As a co-primary contribution, we characterize how PEG's (Chen et al., NeurIPS 2025, arXiv 2505.13636) dominant-strategy truthfulness, requiring conditional independence (Assumption 4), degrades under partial correlation: ε-approximate equilibrium with ε = f(ρ) provides a continuous degradation curve from dominant-strategy (ρ=0) to approximate (ρ→1) regimes. No existing work provides this analysis.

Our proof proceeds in two steps: (1) SDPI per-channel bounds (Polyanskiy & Wu, arXiv 1508.06025) constrain each judge's information leakage to at most I_max per query; across K parallel judges, total adversary information gain is bounded additively by K_eff · I_max. (2) Variance-reduction arguments (Horvath et al., arXiv 2106.06946) yield perturbation energy scaling as Ω(K_eff^{1/2}), giving g(I_max) = ½·log(K_eff)/log(K). The ½ exponent is derived from continuous-space (ℓ₂) variance reduction; for discrete text perturbations, we state it as a conjecture supported by the continuous analogue and test it empirically via adaptive attacks.

Under Turkmen et al.'s (arXiv 2602.08003) equicorrelated Gaussian copula: K_eff = 1+(K-1)·exp(-2·I_max). For heterogeneous correlation, K* = 2^{H(ρ)} (Yang et al.) serves as an upper-bound approximation of effective dimensionality in the adversarial context; its validity is tested via copula goodness-of-fit and empirical tightness experiments.

A provocative implication: as frontier model capability increases, Kim et al. (ICML 2025, arXiv 2506.07962) show error correlations increase even across providers/architectures. Under our framework, this drives K_eff → 1 regardless of ensemble size, suggesting **certified manipulation-resistance may be fundamentally bounded at the frontier**—a "diversity ceiling" where adding more capable judges yields diminishing certified robustness returns even as accuracy continues to improve.

The framework also serves as a **prescriptive judge-selection tool**: K_eff maximization for certified robustness vs. Turkmen et al.'s MI maximization for accuracy—these may yield different optimal ensembles. We validate against 15 off-the-shelf attacks plus three protocol-aware adaptive attacks on SummEval, LiveCodeBench, and GPQA Diamond, with compute-normalized (FLOP-matched) baselines and copula model validation.

## Core Problem
Can we provide certifiable manipulation-resistance guarantees for N-judge LLM evaluation protocols, where the certified robustness bound is an explicit, computable function of measurable inter-judge signal correlation, validated against both off-the-shelf and protocol-aware adaptive adversarial attacks?

## Opportunity
Three critical gaps: (1) No formal N-agent scaling connecting manipulation cost to measurable inter-judge signal correlation. Robertson & Koyejo (arXiv 2508.05469) analyze pairwise evaluations; Chen et al.'s PEG (NeurIPS 2025, arXiv 2505.13636) requires conditional independence (Assumption 4) without characterizing degradation. (2) Empirical validation lacks adaptive attacks targeting multi-judge protocols (Carlini et al., arXiv 1902.06705 standard). (3) Yang et al.'s diversity-scaling (arXiv 2602.03794) addresses performance only—no adversarial dual exists, and the exponential-polynomial asymmetry is unknown.

Turkmen et al. (arXiv 2602.08003): correlated ensemble error floor Φ(Φ⁻¹(1-p)/√ρ), MI decomposition for α estimation. Kaneko & Baldwin (NeurIPS 2025, arXiv 2510.17000): tight single-model bounds, no multi-judge composition. SoK (arXiv 2603.29403): 7-model committees reduce ASR to 10–19% without formal explanation. Qiu et al. (ICLR 2026, arXiv 2601.20299): BNE guarantees for truthfulness, not adversarial robustness.

## Landscape
**Single-evaluator foundations.** Robertson & Koyejo (arXiv 2508.05469, TMLR under review): TVD-MI, polynomial certification (Theorem 3.3), AUC 0.70–0.77. Identity-Link IRT follow-up (arXiv 2510.14966): sparse evaluation, two-judge validation (ρ=0.872).

**Peer prediction.** Qiu et al. (ICLR 2026, arXiv 2601.20299): BNE guarantees, output truthfulness. Chen et al. PEG (NeurIPS 2025, arXiv 2505.13636): dominant strategy (Lemma 1), O(√T) regret (Theorem 2), Nash convergence (Theorem 3), conditional independence (Assumption 4)—degradation under violation uncharacterized.

**Diversity scaling.** Yang et al. (ICLR 2026 Workshop AIMS, arXiv 2602.03794): K* = 2^{H(ρ)}, (1-α_c)^{K*} decay (Theorem 4.3), heterogeneity advantage (Corollary 4.4). Performance only.

**Correlation models.** Turkmen et al. (arXiv 2602.08003): Gaussian copula, error floor (Theorem 4.4), MI decomposition (Theorem 4.3), within-family ρ~0.7-0.8, cross-family ρ~0.4-0.5. Kim et al. (ICML 2025, arXiv 2506.07962): 60% error agreement, +0.066 same-company, +0.076 same-architecture; larger/more accurate models more correlated even across providers. Chen et al. behavioral entanglement (arXiv 2604.07650): BEI/CIG, cross-family 40–60% lower.

**Single-model adversarial bounds.** Kaneko & Baldwin (NeurIPS 2025 spotlight, arXiv 2510.17000): N_min ≥ log₂(1/ε)/I_max (Theorem 1), SPRT achievability (Theorem 2), four disclosure regimes.

**Certifiable evaluation under noise.** Shen et al. (arXiv 2604.03257): constrained MLE, honest judges. Feng et al. (ICLR 2026, arXiv 2601.20913): hypothesis testing, Type-I error control (Theorem 5.1), variance-corrected thresholds (Theorem 5.4). Both assume non-adversarial judges.

**Semantic/representational collapse.** Kong et al. (arXiv 2605.17193, May 2026): closed-loop multi-LLM systems exhibit semantic collapse across 200–1000 rounds; 12 interventions fail. Patel (arXiv 2604.03809): effective rank 2.17/3.0 for homogeneous committees. Both apply to **iterative closed-loop** settings. Our single-pass evaluation protocol (independent scoring, no inter-judge communication) avoids the feedback loops driving collapse; K_eff serves as a principled detector if diversity erosion occurs.

**Scaling dissociation.** Jung & Na (arXiv 2604.00477): scoring reliability logarithmic, discovery N^0.69 power law.

**Attack/defense landscape.** SoK (arXiv 2603.29403): 50–68% ASR open-source, 27–44% frontier, 7-model → 10–19%. RobustJudge (arXiv 2506.09443): 15 attacks, 7 defenses. CAP (OpenReview 2026): comparative assessment, no formal guarantees. Carlini et al. (arXiv 1902.06705): adaptive attack gold standard.

**Coordination failure.** Frongillo et al. (arXiv 2503.16280): fine-grained signals destabilize uninformative equilibria. Keppo et al. (arXiv 2603.20281): 2→5 LLMs breaks collusion (+22%→+3%).

**Multi-agent evaluation.** CollabEval (arXiv 2603.00993): three-phase, no adversarial guarantees. Ebrahimi et al. (IJCNLP-AACL 2025, arXiv 2505.24239): credibility-based aggregation.

**Certified ensemble robustness.** Chen et al. (arXiv 2107.10873): diversified gradient + confidence margin necessary/sufficient. Horvath et al. (arXiv 2106.06946): √K certified radius via variance reduction. Both in continuous perturbation spaces.

THE KEY GAP: No formal N-agent manipulation-cost scaling as a function of measurable correlation; no characterization of the exponential-polynomial asymmetry between performance and robustness scaling; no PEG degradation analysis under correlation violation.

## Approach

Five components:

**Component 1: Theoretical Framework—The Asymmetric Adversarial Dual.**

We prove manipulation cost grows as Ω(K_eff^{1/2}), establishing an asymmetric duality with Yang et al.'s exponential performance scaling. The structural origin: stochastic errors are incoherent across judges (exponential concentration), but adversarial perturbations are coherent (shared perturbation reintroduces coupling → polynomial variance reduction only). This implies a fundamental resource-allocation insight: the marginal robustness value of each additional judge diminishes faster than its marginal accuracy value.

*Step 1—Per-Channel SDPI Bound.* Each judge is a noisy channel; SDPI (Polyanskiy & Wu, arXiv 1508.06025) bounds per-channel information leakage to I_max. K parallel judges yield additive total: K_eff · I_max per round. Extends Kaneko & Baldwin's single-channel N_min.

*Step 2—Variance Reduction to Manipulation Cost.* Fano-ensemble decomposition (Morishita et al., ICML 2022, arXiv 2205.12683) into relevance, redundancy, combination loss. Marton's inequality (TV² ≤ ½·KL) + Robertson & Koyejo's Theorem 3.3 → perturbation energy Ω(K_eff^{1/2}). Exponent: g(I_max) = ½·log(K_eff)/log(K). Boundaries: g(0) = ½ (independent), g → 0 (fully correlated).

*Copula Closed Form.* Turkmen et al.'s equicorrelated model: K_eff = 1+(K-1)·exp(-2·I_max), I_max = -½ log(1-ρ²). Eigenvalues λ₁ = 1+(K-1)ρ, λ₂ = 1-ρ.

*Heterogeneous Extension.* K* = 2^{H(ρ)} (Yang et al.) as upper-bound approximation of adversarial effective dimensionality, yielding g ≥ ½·log(K*)/log(K). K*'s validity in the adversarial context (vs. its original performance context) is an approximation justified by the shared eigenstructure and validated empirically via tightness experiments.

*Exponent Status.* The ½ exponent derives from continuous-space (ℓ₂) variance reduction (Horvath et al., arXiv 2106.06946). For discrete text perturbations, the perturbation geometry differs; we state ½ as a conjecture for the discrete evaluation setting, supported by the continuous analogue, and test it empirically. Whether the true discrete exponent is better or worse than ½ is an open question.

*Frontier Diversity Ceiling.* Kim et al. (ICML 2025) show error correlations increase with model capability even across providers/architectures. Under our framework, this drives K_eff → 1 as ρ → 1, implying certified manipulation-resistance may face a fundamental ceiling at the frontier: adding more capable judges yields diminishing certified robustness returns even as accuracy improves. We examine this empirically and discuss its implications.

**Component 2: PEG Guarantee Degradation + α Regime Analysis.**

*Co-primary contribution.* PEG's dominant-strategy truthfulness (Lemma 1, Assumption 4 conditional independence; Chen et al., NeurIPS 2025, arXiv 2505.13636) degrades under correlation: ε-approximate equilibrium with ε = f(ρ). This degradation pattern may extend to other conditional-independence-assuming mechanisms in peer prediction, though we prove it specifically for PEG.

α estimates using external priors (Turkmen et al. ρ~0.4-0.5; Kim et al. +0.066/+0.076) **validated via direct measurement** in pilot study. Note: Kim et al.'s agreement rate and copula ρ are different quantities; we derive the mapping explicitly.
- Central: ρ ≈ 0.45, α ∈ [0.35, 0.65], K=7: 2.65–3.7×
- Sensitivity: α=0.2 → 1.55×; α=0.8 → 5.2×; vacuous at α ≤ 0.05 (ρ ≥ 0.95)
- Score-coverage dissociation (Jung & Na, arXiv 2604.00477): analyze certified bound saturation rate

**Component 3: Practical Protocol Design.**

Three families: DeepSeek-V4-Flash (284B MoE, 13B active), Qwen-3.5 (397B MoE, 17B active), Llama-4-Maverick (400B MoE, 17B active). Backups: Gemma-2-27B (dense, non-MoE), Mistral-Large-2, Command-R+.

Three phases: (1) Independence measurement (calibration ≥500 samples for copula GoF; sensitivity at {100, 200, 500, 1000, 2000}); (2) TVD-MI evaluation + DMI-weighted aggregation (PEG, Chen et al., NeurIPS 2025); (3) Certification: Ω(K^α) bound with measured α.

Prescriptive judge selection: K_eff maximization (robustness) vs. MI maximization (accuracy, Turkmen et al.) may yield different optimal ensembles.

**Component 4: Certifiable Robustness Framing.**

A defense showing 15% empirical ASR under today's 15 known attacks provides no guarantee against tomorrow's attacks—an adaptive adversary could spike ASR back to 60% with a novel strategy. Our framework guarantees Ω(K^α) manipulation cost regardless of attack strategy. Same value proposition as randomized smoothing: modest certified margins, but provable guarantees. Kaneko & Baldwin's per-judge N_min × K_eff gives multi-judge certified resistance.

**Component 5: Adversarial Validation, PEG Degradation Testing, and Model Assumption Validation.**

*Benchmarks.* SummEval (summarization; CAP comparison; broader quality metrics beyond factuality), LiveCodeBench (code; contamination-resistant, frontier-discriminative), GPQA Diamond (knowledge-intensive QA; discriminative for open-weight judges).

*Threat models.* Black-box (aggregated output only), gray-box (judge identities known, individual outputs hidden), white-box (all outputs + DMI weights visible).

*Off-the-shelf attacks.* RobustJudge's 15 methods + SoK vectors.

*Adaptive attacks (Carlini et al., arXiv 1902.06705):*
(a) Correlation-exploiting (gray/white): optimize perturbation to simultaneously fool high-ρ pairs; transfer-based optimization on proxy models if full MoE gradient infeasible.
(b) Aggregation-targeting (white): optimize to shift aggregated score beyond certified bound.
(c) Weakest-link (gray): concentrate on highest-I_max channel.
(d) Best-effort tightness (white): PGD on MoE active parameters (13-17B, feasible per-forward-pass); fallback to PAIR + random-search hybrid. Budget: 10,000 queries. Convergence: <0.5% ASR improvement over last 2,000 queries. Report ASR-vs-budget curve with convergence annotation.

*Compute-normalized baselines (FLOP-matched):*
(a) Frontier single-model (GPT-4o-latest or Claude Sonnet).
(b) Self-consistency: DeepSeek-V4-Flash × 7 (different temperatures/prompts), majority voting. Reports per-query FLOPs and wall-clock time.

*Other baselines.* 7 RobustJudge defenses; CAP; CollabEval (arXiv 2603.00993); Ebrahimi et al. (IJCNLP-AACL 2025, arXiv 2505.24239); Robertson & Koyejo single-evaluator TVD-MI; majority voting K=3,5,7; PEG with DMI scoring.

*PEG degradation validation.* Dedicated experiment: construct 5-7 judge panels spanning ρ from within-family (~0.7-0.8) to all-cross-family (~0.4-0.5) via mixed composition. For each panel, measure ρ_ij directly. Introduce a strategic deviator judge (via prompt injection) and measure its expected payoff gain vs. truthful baseline—payoff gain > 0 provides empirical ε lower bound. Report (measured_ρ, empirical_ε) scatter against theoretical f(ρ) curve. Track DMI regret across panels.

*Dual-scaling validation.* In K-scaling ablation (K=1,2,3,5,7), simultaneously measure: (a) non-adversarial accuracy (Spearman/Kendall with ground truth), fitting (1-α_c)^{K*} model (report R²); (b) adversarial manipulation cost (empirical query count + certified bound), fitting K^α model (report R²). Overlay both curves (log-scale y-axis) to visualize exponential-polynomial asymmetry.

*Model assumption validation.*
(a) Full K×K ρ_ij matrix; Var(ρ_ij) for equicorrelation deviation.
(b) Copula GoF (Anderson-Darling, minimum n=500; 50-100 for ρ stability only).
(c) If GoF rejects: Kendall's tau rank correlation for dependence estimation; K* from rank-correlation matrix. Report Pearson-based vs. Kendall-based K* gap.
(d) Heterogeneous bound (K*) vs. closed-form bound gap.

*Ablations.*
(a) K-scaling: K=1,2,3,5,7 (with dual-scaling overlay).
(b) Diversity-type 2×2: {same-org, diff-org} × {same-arch-type, diff-arch-type}, ≥1 non-MoE model (Gemma-2-27B).
(c) Accuracy-robustness tradeoff: MI-maximization vs. K_eff-maximization ensemble selection; Pareto frontier.
(d) α sensitivity: [0.2, 0.8].
(e) Calibration sensitivity: ρ at {100, 200, 500, 1000, 2000}; cross-domain calibration transfer (3×3 benchmark matrix: use ρ from benchmark A to compute bound for B, report transferred vs. in-domain bound deviation and ρ cross-domain stability); bootstrap error propagation to CI.

*Statistical rigor.* ≥3 seeds (mean ± std). ρ: bootstrap 95% CI. Primary correction: Benjamini-Hochberg FDR. Conservative check on core claims: Bonferroni. Report uncorrected, BH-adjusted, and Bonferroni-adjusted values.

*Pilot study (Weeks 1-2, ~100 H100-hrs).* ρ_ij on 500 samples per benchmark. Go/no-go: ρ > 0.7 → switch to backups. If all open-weight models show ρ > 0.7, report as empirical finding supporting the frontier diversity ceiling.

## Resource Estimate
{'manual': {'gpu_hours': '1,800-2,800 H100-equivalent', 'timeline': '18-24 weeks', 'estimated_gpu_cost': '$4,500-$7,000 at $2.50/hr', 'gpu_breakdown': 'Pilot ~100; single-judge baselines ~450; multi-judge protocol ~500; adaptive attacks (transfer/PAIR + tightness PGD) ~500; compute-normalized baselines ~50 + ~$300 API; copula/calibration/cross-domain ~100; PEG degradation validation ~80; diversity + accuracy-robustness ablation ~200; K-scaling + dual-scaling ~200; multi-seed ~300; dev/debug ~150'}, 'human_in_loop': {'gpu_hours': '1,400-2,200', 'timeline': '14-18 weeks', 'claude_api_cost': '$400-$600'}, 'auto_research': {'gpu_hours': '2,100-3,000', 'timeline': '9-13 weeks', 'claude_api_cost': '$1,200-$2,000'}}

## Inspired By
Seven lines: (1) Robertson & Koyejo bounded f-divergence (arXiv 2508.05469); (2) Qiu et al. BNE (ICLR 2026, arXiv 2601.20299) + Chen et al. PEG (NeurIPS 2025, arXiv 2505.13636); (3) Yang et al. K* diversity-scaling (ICLR 2026 Workshop AIMS, arXiv 2602.03794); (4) Turkmen et al. copula model (arXiv 2602.08003); (5) Kaneko & Baldwin single-model bounds (NeurIPS 2025 spotlight, arXiv 2510.17000); (6) SoK 7-model ASR reduction (arXiv 2603.29403); (7) Error correlation/entanglement (Chen et al. arXiv 2604.07650; Kim et al. ICML 2025, arXiv 2506.07962).

## Target Venues
- ICLR 2027 (estimated: October 2026; primary—full theory + comprehensive experiments)
- AAAI 2027 (abstract: July 21, 2026; stretch goal)
- USENIX Security 2027 Cycle 1 (August 2026; security-focused)
- NeurIPS 2026 Workshops (~August 29, 2026)

## Key References
- Let's Measure Information Step-by-Step (Robertson & Koyejo, arXiv 2508.05469, 2025)
- Identity-Link IRT (Robertson, arXiv 2510.14966, 2025)
- Truthfulness Despite Weak Supervision (Qiu et al., ICLR 2026, arXiv 2601.20299)
- PEG (Chen et al., NeurIPS 2025, arXiv 2505.13636)
- Understanding Agent Scaling via Diversity (Yang et al., ICLR 2026 Workshop AIMS, arXiv 2602.03794)
- Don't Always Pick the Highest-Performing Model (Turkmen et al., arXiv 2602.08003, 2026)
- Bits Leaked per Query (Kaneko & Baldwin, NeurIPS 2025 spotlight, arXiv 2510.17000)
- Robust LLM Performance Certification (Shen et al., arXiv 2604.03257, 2026)
- Noisy but Valid (Feng et al., ICLR 2026, arXiv 2601.20913)
- Logarithmic Scores, Power-Law Discoveries (Jung & Na, arXiv 2604.00477, 2026)
- SoK: Security in LLM-as-a-Judge (arXiv 2603.29403, April 2026)
- RobustJudge (arXiv 2506.09443, 2025)
- Correlated Errors in LLMs (Kim et al., ICML 2025, arXiv 2506.07962)
- Behavioral Entanglement (Chen et al., arXiv 2604.07650, 2026)
- Benchmark Illusion (arXiv 2602.11898, 2026)
- Strong Data-Processing Inequalities (Polyanskiy & Wu, arXiv 1508.06025, 2017)
- Rethinking Fano's Inequality in Ensemble Learning (Morishita et al., ICML 2022, arXiv 2205.12683)
- Certified Robustness for Ensemble Models (Chen et al., arXiv 2107.10873, 2021)
- Boosting Randomized Smoothing with Variance Reduced Classifiers (Horvath et al., arXiv 2106.06946, 2021)
- Information-Theoretically Optimal Adversarial Attacks (Yi et al., arXiv 2007.14042, 2020)
- On the Fragility of AI Agent Collusion (Keppo et al., arXiv 2603.20281, 2026)
- CollabEval (arXiv 2603.00993, March 2026)
- Adversary-Resistant Multi-Agent via Credibility Scoring (Ebrahimi et al., IJCNLP-AACL 2025, arXiv 2505.24239)
- Certifying Joint Adversarial Robustness for Ensembles (Chiang et al., arXiv 2004.10250, 2020)
- Peer Prediction with More Signals than Reports (Frongillo et al., arXiv 2503.16280, 2025)
- Adversarial Manipulation of Voting-Based Leaderboards (ICML 2025)
- Vote Rigging on Chatbot Arena (ICML 2025)
- am-ELO: Stable Arena-based Evaluation (ICML 2025 Poster)
- CAP: Comparative Augmented Prompting (OpenReview 2026)
- Aligned Textual Scoring Rules (Lu et al., arXiv 2507.06221, 2025)
- Can You Trick the Grader? (EMNLP 2025 Findings)
- On Evaluating Adversarial Robustness (Carlini et al., arXiv 1902.06705, 2019)
- Multi-LLM Systems Exhibit Robust Semantic Collapse (Kong et al., arXiv 2605.17193, May 2026)
- Representational Collapse in Multi-Agent LLM Committees (Patel, arXiv 2604.03809, April 2026)
- LiveCodeBench (arXiv 2403.07974, 2024)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "93b903bb-07b4-406c-b81b-081fe808e171",
  "type": "user",
  "uuid": "fefd3525-845b-4a49-810b-467976c760e6",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:50:23.977Z_

```json
{
  "parentUuid": "fefd3525-845b-4a49-810b-467976c760e6",
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
  "uuid": "7a814598-630b-45c1-a289-cb36dda16c25",
  "timestamp": "2026-05-20T05:50:23.977Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:50:23.977Z_

```json
{
  "parentUuid": "7a814598-630b-45c1-a289-cb36dda16c25",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b11fa247-81e2-42db-8c85-d9c94fa3c71d",
  "timestamp": "2026-05-20T05:50:23.977Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Corr…",
  "leafUuid": "b11fa247-81e2-42db-8c85-d9c94fa3c71d",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-judge LLM evaluation certifiable robustness bounds",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:50:28.917Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for EMNLP 2026 submission potential. I need to first conduct thorough literature research before scoring. Let me start by loading the WebSearch tool and then conducting searches on the key topics.

Let me first load the WebSearch tool, then do several targeted searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b11fa247-81e2-42db-8c85-d9c94fa3c71d",
  "isSidechain": false,
  "requestId": "req_011CbDJDCm2pimYEuU4TdgMU",
  "type": "assistant",
  "uuid": "5d322032-b323-4dc6-acef-4cf618c332e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R36aAzU5fPK3PxJHmkt2ZC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 22621,
      "output_tokens": 159,
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
          "output_tokens": 159,
          "cache_read_input_tokens": 22621,
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

_source line 9 · 2026-05-20T05:50:29.155Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017tQcCtbFZZVJxpNBSFkeFo`</summary>

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
  "parentUuid": "5d322032-b323-4dc6-acef-4cf618c332e9",
  "isSidechain": false,
  "requestId": "req_011CbDJDCm2pimYEuU4TdgMU",
  "type": "assistant",
  "uuid": "f41db9da-8167-4793-bc12-e87702bb11ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R36aAzU5fPK3PxJHmkt2ZC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 22621,
      "output_tokens": 159,
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
          "output_tokens": 159,
          "cache_read_input_tokens": 22621,
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

_source line 10 · 2026-05-20T05:50:29.161Z_

<details><summary>↩ Tool result · `toolu_017tQcCtbFZZVJxpNBSFkeFo`</summary>

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
  "parentUuid": "f41db9da-8167-4793-bc12-e87702bb11ac",
  "isSidechain": false,
  "promptId": "93b903bb-07b4-406c-b81b-081fe808e171",
  "type": "user",
  "uuid": "5018b46e-309c-41a9-a758-7fcffe994c80",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "f41db9da-8167-4793-bc12-e87702bb11ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T05:50:34.533Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct the required literature searches. I need to do 3-5 targeted searches to understand:
1. The current state of adversarial robustness in LLM-as-a-judge evaluation
2. Multi-judge LLM evaluation and certified robustness
3. Information-theoretic bounds for LLM evaluation manipulation
4. Diversity scaling in multi-agent/multi-judge settings
5. PEG and peer prediction mechanisms for LLM evaluation

Let me launch these searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5018b46e-309c-41a9-a758-7fcffe994c80",
  "isSidechain": false,
  "requestId": "req_011CbDJDb8BkHYFewASN7iSe",
  "type": "assistant",
  "uuid": "332a009c-7c95-4c9d-a746-cdeb4d08c189",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ufWFXq4afCD63k9Ayxrvu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 687,
      "cache_read_input_tokens": 22621,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 22621,
          "cache_creation_input_tokens": 687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 687
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

_source line 12 · 2026-05-20T05:50:35.044Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JNSkpS6RMpJ6vBvCwc6h9S`</summary>

```json
{
  "query": "adversarial robustness LLM-as-a-judge multi-judge evaluation certified guarantees 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "332a009c-7c95-4c9d-a746-cdeb4d08c189",
  "isSidechain": false,
  "requestId": "req_011CbDJDb8BkHYFewASN7iSe",
  "type": "assistant",
  "uuid": "429d832b-be09-402c-8de7-42f97a3e51ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ufWFXq4afCD63k9Ayxrvu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 687,
      "cache_read_input_tokens": 22621,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 22621,
          "cache_creation_input_tokens": 687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 687
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

_source line 13 · 2026-05-20T05:50:35.539Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QMKWfuUQqcFi1zPwKGW46y`</summary>

```json
{
  "query": "information-theoretic bounds manipulation resistance LLM evaluation ensemble diversity scaling 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "429d832b-be09-402c-8de7-42f97a3e51ef",
  "isSidechain": false,
  "requestId": "req_011CbDJDb8BkHYFewASN7iSe",
  "type": "assistant",
  "uuid": "28e4f6be-3b63-4e96-a419-a94a0b39e82c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ufWFXq4afCD63k9Ayxrvu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 687,
      "cache_read_input_tokens": 22621,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 22621,
          "cache_creation_input_tokens": 687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 687
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

_source line 14 · 2026-05-20T05:50:36.105Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MszrR7aayWbdXqEo1SFGZA`</summary>

```json
{
  "query": "SoK security LLM judge arXiv 2603.29403 attack success rate multi-model committee"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28e4f6be-3b63-4e96-a419-a94a0b39e82c",
  "isSidechain": false,
  "requestId": "req_011CbDJDb8BkHYFewASN7iSe",
  "type": "assistant",
  "uuid": "2a0d1ffc-f3fc-43fb-9e89-312b0f608379",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ufWFXq4afCD63k9Ayxrvu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 687,
      "cache_read_input_tokens": 22621,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 22621,
          "cache_creation_input_tokens": 687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 687
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

_source line 15 · 2026-05-20T05:50:42.439Z_

<details><summary>↩ Tool result · `toolu_01JNSkpS6RMpJ6vBvCwc6h9S`</summary>

```text
Web search results for query: "adversarial robustness LLM-as-a-judge multi-judge evaluation certified guarantees 2025 2026"

Links: [{"title":"SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK","url":"https://arxiv.org/pdf/2603.29403"},{"title":"LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge","url":"https://arxiv.org/html/2506.09443v1"},{"title":"Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on   Zero-shot LLM Assessment","url":"https://arxiv.org/pdf/2402.14016"},{"title":"LLM-as-a-Judge Evaluation","url":"https://www.emergentmind.com/topics/llm-as-a-judge-evaluations"},{"title":"LLM-as-Judge Evaluation","url":"https://www.emergentmind.com/topics/llm-as-a-judge-evaluation"},{"title":"LLM-as-a-Judge: Automated Evaluation","url":"https://www.emergentmind.com/topics/large-language-models-as-a-judge-llm-as-a-judge"},{"title":"A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness","url":"https://arxiv.org/pdf/2603.06594"}]

Based on the search results, here's what I found regarding adversarial robustness of LLM-as-a-judge systems and multi-judge evaluation with certified guarantees:

## Key Findings on Adversarial Robustness

LLM-as-a-Judge systems are vulnerable to a range of adversarial attacks, including Combined Attack and PAIR, while defense mechanisms such as Re-tokenization and LLM-based Detectors offer improved protection. LLM-based judges can be easily manipulated by adversarial prompt modifications such as Combined Attack or optimization-based attacks such as PAIR, which achieves high attack success rates and large deviations from correct scores.

## Multi-Judge and Ensemble Approaches

Recent work (Abeyratne et al., 2025) proposed an unsupervised ensemble method to evaluate LLM-generated responses. Additionally, defense mechanisms include re-tokenization and LLM-based detectors, with uncertainty quantification via confusion matrices (analyzing log token probabilities over n² assessments) to yield per-instance reliability.

## Prompt Template Sensitivity

Robustness is highly sensitive to choice of prompt template—decomposed into discrete components such as role, instructions, evaluation criterion, and response format, with minor changes in phrasing or structure potentially swinging vulnerability metrics and attack success rates.

## Certified Guarantees

The search results do not contain specific information about certified guarantees for LLM-as-a-judge systems. While the sources discuss various defense mechanisms and improvements, they do not mention formal certified robustness guarantees or formal verification approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "429d832b-be09-402c-8de7-42f97a3e51ef",
  "isSidechain": false,
  "promptId": "93b903bb-07b4-406c-b81b-081fe808e171",
  "type": "user",
  "uuid": "4cb916cf-7558-4e9d-84cf-d6a39f36d14f",
  "toolUseResult": {
    "query": "adversarial robustness LLM-as-a-judge multi-judge evaluation certified guarantees 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013KjX4ZCf5UCidrk9qdgVBr",
        "content": [
          {
            "title": "SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK",
            "url": "https://arxiv.org/pdf/2603.29403"
          },
          {
            "title": "LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2506.09443v1"
          },
          {
            "title": "Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on   Zero-shot LLM Assessment",
            "url": "https://arxiv.org/pdf/2402.14016"
          },
          {
            "title": "LLM-as-a-Judge Evaluation",
            "url": "https://www.emergentmind.com/topics/llm-as-a-judge-evaluations"
          },
          {
            "title": "LLM-as-Judge Evaluation",
            "url": "https://www.emergentmind.com/topics/llm-as-a-judge-evaluation"
          },
          {
            "title": "LLM-as-a-Judge: Automated Evaluation",
            "url": "https://www.emergentmind.com/topics/large-language-models-as-a-judge-llm-as-a-judge"
          },
          {
            "title": "A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness",
            "url": "https://arxiv.org/pdf/2603.06594"
          }
        ]
      },
      "Based on the search results, here's what I found regarding adversarial robustness of LLM-as-a-judge systems and multi-judge evaluation with certified guarantees:\n\n## Key Findings on Adversarial Robustness\n\nLLM-as-a-Judge systems are vulnerable to a range of adversarial attacks, including Combined Attack and PAIR, while defense mechanisms such as Re-tokenization and LLM-based Detectors offer improved protection. LLM-based judges can be easily manipulated by adversarial prompt modifications such as Combined Attack or optimization-based attacks such as PAIR, which achieves high attack success rates and large deviations from correct scores.\n\n## Multi-Judge and Ensemble Approaches\n\nRecent work (Abeyratne et al., 2025) proposed an unsupervised ensemble method to evaluate LLM-generated responses. Additionally, defense mechanisms include re-tokenization and LLM-based detectors, with uncertainty quantification via confusion matrices (analyzing log token probabilities over n² assessments) to yield per-instance reliability.\n\n## Prompt Template Sensitivity\n\nRobustness is highly sensitive to choice of prompt template—decomposed into discrete components such as role, instructions, evaluation criterion, and response format, with minor changes in phrasing or structure potentially swinging vulnerability metrics and attack success rates.\n\n## Certified Guarantees\n\nThe search results do not contain specific information about certified guarantees for LLM-as-a-judge systems. While the sources discuss various defense mechanisms and improvements, they do not mention formal certified robustness guarantees or formal verification approaches."
    ],
    "durationSeconds": 7.371860514,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "429d832b-be09-402c-8de7-42f97a3e51ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T05:50:43.657Z_

<details><summary>↩ Tool result · `toolu_01MszrR7aayWbdXqEo1SFGZA`</summary>

```text
Web search results for query: "SoK security LLM judge arXiv 2603.29403 attack success rate multi-model committee"

Links: [{"title":"SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK","url":"https://arxiv.org/pdf/2603.29403"},{"title":"[2603.29403] Security in LLM-as-a-Judge: A Comprehensive SoK","url":"https://arxiv.org/abs/2603.29403"},{"title":"SoK: Robustness in Large Language Models against Jailbreak Attacks","url":"https://arxiv.org/html/2605.05058v1"},{"title":"SoK: Robustness in Large Language Models against Jailbreak - IEEE S&P 2026 Cycle 1 #1329 Artifact Evaluation","url":"https://zenodo.org/records/17131481"},{"title":"Adversarial Attacks on LLM-as-a-Judge Systems: Insights from Prompt Injections","url":"https://arxiv.org/html/2504.18333v1"},{"title":"[2605.05058] SoK: Robustness in Large Language Models against Jailbreak Attacks","url":"https://arxiv.org/abs/2605.05058"}]

Based on the search results, I found the paper you're looking for. Here's what the research shows:

This is the first Systematization of Knowledge (SoK) focusing on the security aspects of LLM-as-a-Judge systems, with a comprehensive literature review analyzing 863 works and selecting 45 relevant studies published between 2020 and 2026.

Regarding the specific findings about attack success rates and multi-model committees:

Individual defenses were evaded 32-67% of the time, while multi-model committees of seven architecturally diverse models reduced attack success rates to as low as 10-19%, making committee-based evaluation the strongest available mitigation strategy.

LLM-as-a-Judge is a paradigm where powerful language models assess the quality, safety, or correctness of generated outputs, but while it has improved scalability and efficiency of evaluation processes, it introduces novel security risks, as LLM-based judges can become both targets of adversarial manipulation and instruments through which attacks are conducted.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a0d1ffc-f3fc-43fb-9e89-312b0f608379",
  "isSidechain": false,
  "promptId": "93b903bb-07b4-406c-b81b-081fe808e171",
  "type": "user",
  "uuid": "fb0b94f1-29d8-4013-b12c-d27102532465",
  "toolUseResult": {
    "query": "SoK security LLM judge arXiv 2603.29403 attack success rate multi-model committee",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Nx9BmdzK8mfrdjVTz6TMzQ",
        "content": [
          {
            "title": "SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK",
            "url": "https://arxiv.org/pdf/2603.29403"
          },
          {
            "title": "[2603.29403] Security in LLM-as-a-Judge: A Comprehensive SoK",
            "url": "https://arxiv.org/abs/2603.29403"
          },
          {
            "title": "SoK: Robustness in Large Language Models against Jailbreak Attacks",
            "url": "https://arxiv.org/html/2605.05058v1"
          },
          {
            "title": "SoK: Robustness in Large Language Models against Jailbreak - IEEE S&P 2026 Cycle 1 #1329 Artifact Evaluation",
            "url": "https://zenodo.org/records/17131481"
          },
          {
            "title": "Adversarial Attacks on LLM-as-a-Judge Systems: Insights from Prompt Injections",
            "url": "https://arxiv.org/html/2504.18333v1"
          },
          {
            "title": "[2605.05058] SoK: Robustness in Large Language Models against Jailbreak Attacks",
            "url": "https://arxiv.org/abs/2605.05058"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what the research shows:\n\nThis is the first Systematization of Knowledge (SoK) focusing on the security aspects of LLM-as-a-Judge systems, with a comprehensive literature review analyzing 863 works and selecting 45 relevant studies published between 2020 and 2026.\n\nRegarding the specific findings about attack success rates and multi-model committees:\n\nIndividual defenses were evaded 32-67% of the time, while multi-model committees of seven architecturally diverse models reduced attack success rates to as low as 10-19%, making committee-based evaluation the strongest available mitigation strategy.\n\nLLM-as-a-Judge is a paradigm where powerful language models assess the quality, safety, or correctness of generated outputs, but while it has improved scalability and efficiency of evaluation processes, it introduces novel security risks, as LLM-based judges can become both targets of adversarial manipulation and instruments through which attacks are conducted."
    ],
    "durationSeconds": 7.548789172000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2a0d1ffc-f3fc-43fb-9e89-312b0f608379",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T05:50:45.061Z_

<details><summary>↩ Tool result · `toolu_01QMKWfuUQqcFi1zPwKGW46y`</summary>

```text
Web search results for query: "information-theoretic bounds manipulation resistance LLM evaluation ensemble diversity scaling 2025 2026"

Links: [{"title":"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/pdf/2508.05469"},{"title":"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs","url":"https://arxiv.org/pdf/2510.17000"},{"title":"An Information-Theoretic Perspective on Multi-LLM Uncertainty Estimation","url":"https://www.medrxiv.org/content/10.1101/2025.07.09.25331207.full.pdf"},{"title":"On the Fundamental Limits of LLMs at Scale","url":"https://arxiv.org/pdf/2511.12869"},{"title":"Analysis of Threat-Based Manipulation in Large Language Models: A Dual Perspective on Vulnerabilities and Performance Enhancement Opportunities","url":"https://arxiv.org/pdf/2507.21133"},{"title":"Breaking Myths in LLM scaling and emergent abilities with a comprehensive statistical analysis - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S092523122503214X"}]

Based on the search results, here are the key findings related to your query:

## Information-Theoretic Bounds and Manipulation Resistance in LLM Evaluation

Bounded f-divergences (e.g., total variation distance) maintain polynomial guarantees under attacks while unbounded measures (e.g., KL divergence) degrade exponentially. This research examines which information-theoretic mechanisms are resistant to adversarial manipulation in AI system evaluation.

The data processing inequality shows that any strategic manipulation of content necessarily reduces mutual information between responses, implementing evaluation mechanisms with formal gaming-resistance guarantees.

## Adversarial Attacks and Information Leakage

Achieving error ε requires at least log(1/ε)/I(Z;T) queries, scaling linearly with the inverse leak rate and only logarithmically with the desired accuracy. This framework quantifies how much information can be safely disclosed in LLM responses.

## Ensemble Diversity and Multi-LLM Evaluation

An information-theoretic framework selects LLM subsets by minimizing predictive uncertainty, with key parameters controlling the balance between ensemble breadth and agreement.

## LLM Scaling Analysis

Recent comprehensive statistical analysis of LLM scaling from 2025 found that "gradual emergent abilities" suggest continuous development of capabilities characterized by gradual, task-dependent, and potentially non-linear progress rather than abrupt breakthroughs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28e4f6be-3b63-4e96-a419-a94a0b39e82c",
  "isSidechain": false,
  "promptId": "93b903bb-07b4-406c-b81b-081fe808e171",
  "type": "user",
  "uuid": "922cb1df-ced9-4ed9-be78-20a6edffdaff",
  "toolUseResult": {
    "query": "information-theoretic bounds manipulation resistance LLM evaluation ensemble diversity scaling 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011J3X2U8AGjufQK2hWrbAKw",
        "content": [
          {
            "title": "Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/pdf/2508.05469"
          },
          {
            "title": "Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs",
            "url": "https://arxiv.org/pdf/2510.17000"
          },
          {
            "title": "An Information-Theoretic Perspective on Multi-LLM Uncertainty Estimation",
            "url": "https://www.medrxiv.org/content/10.1101/2025.07.09.25331207.full.pdf"
          },
          {
            "title": "On the Fundamental Limits of LLMs at Scale",
            "url": "https://arxiv.org/pdf/2511.12869"
          },
          {
            "title": "Analysis of Threat-Based Manipulation in Large Language Models: A Dual Perspective on Vulnerabilities and Performance Enhancement Opportunities",
            "url": "https://arxiv.org/pdf/2507.21133"
          },
          {
            "title": "Breaking Myths in LLM scaling and emergent abilities with a comprehensive statistical analysis - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S092523122503214X"
          }
        ]
      },
      "Based on the search results, here are the key findings related to your query:\n\n## Information-Theoretic Bounds and Manipulation Resistance in LLM Evaluation\n\nBounded f-divergences (e.g., total variation distance) maintain polynomial guarantees under attacks while unbounded measures (e.g., KL divergence) degrade exponentially. This research examines which information-theoretic mechanisms are resistant to adversarial manipulation in AI system evaluation.\n\nThe data processing inequality shows that any strategic manipulation of content necessarily reduces mutual information between responses, implementing evaluation mechanisms with formal gaming-resistance guarantees.\n\n## Adversarial Attacks and Information Leakage\n\nAchieving error ε requires at least log(1/ε)/I(Z;T) queries, scaling linearly with the inverse leak rate and only logarithmically with the desired accuracy. This framework quantifies how much information can be safely disclosed in LLM responses.\n\n## Ensemble Diversity and Multi-LLM Evaluation\n\nAn information-theoretic framework selects LLM subsets by minimizing predictive uncertainty, with key parameters controlling the balance between ensemble breadth and agreement.\n\n## LLM Scaling Analysis\n\nRecent comprehensive statistical analysis of LLM scaling from 2025 found that \"gradual emergent abilities\" suggest continuous development of capabilities characterized by gradual, task-dependent, and potentially non-linear progress rather than abrupt breakthroughs."
    ],
    "durationSeconds": 9.519106056999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "28e4f6be-3b63-4e96-a419-a94a0b39e82c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T05:50:48.241Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UrD7F5X76hS47XzMT2Sm2X`</summary>

```json
{
  "query": "Robertson Koyejo \"bounded f-divergence\" TVD-MI LLM evaluation certification arXiv 2508.05469"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "922cb1df-ced9-4ed9-be78-20a6edffdaff",
  "isSidechain": false,
  "requestId": "req_011CbDJEkkesEWqLcAkDS4gd",
  "type": "assistant",
  "uuid": "1d5e1986-df89-4c66-9af5-d2d18a28d64f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XqBWxXEySH1r7gBmRqgYQF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 598,
      "cache_creation_input_tokens": 1774,
      "cache_read_input_tokens": 23308,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1774,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 598,
          "output_tokens": 144,
          "cache_read_input_tokens": 23308,
          "cache_creation_input_tokens": 1774,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1774
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

_source line 19 · 2026-05-20T05:50:48.929Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pq19eH87vBe4tBKsqyUARq`</summary>

```json
{
  "query": "Yang et al diversity scaling multi-agent effective channel count entropy arXiv 2602.03794 ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d5e1986-df89-4c66-9af5-d2d18a28d64f",
  "isSidechain": false,
  "requestId": "req_011CbDJEkkesEWqLcAkDS4gd",
  "type": "assistant",
  "uuid": "42d92a8d-24b3-4cf4-b40e-4ed3ebfb00f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XqBWxXEySH1r7gBmRqgYQF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 598,
      "cache_creation_input_tokens": 1774,
      "cache_read_input_tokens": 23308,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1774,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 598,
          "output_tokens": 144,
          "cache_read_input_tokens": 23308,
          "cache_creation_input_tokens": 1774,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1774
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

_source line 20 · 2026-05-20T05:50:52.602Z_

<details><summary>↩ Tool result · `toolu_01UrD7F5X76hS47XzMT2Sm2X`</summary>

```text
Web search results for query: "Robertson Koyejo "bounded f-divergence" TVD-MI LLM evaluation certification arXiv 2508.05469"

Links: [{"title":"Identity-Link IRT for Label-Free LLM Evaluation:","url":"https://arxiv.org/pdf/2510.14966"},{"title":"[2508.05469] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/abs/2508.05469"},{"title":"Let’s Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/html/2508.05469"},{"title":"[PDF] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Let's-Measure-Information-Step-by-Step:-LLM-Based-Robertson-Koyejo/824098ede34f59514ebc25a69c69c68d1e89b664"},{"title":"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/pdf/2508.05469"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes"

**Authors:** Zachary Robertson and Sanmi Koyejo from Stanford University

**ArXiv ID:** 2508.05469

**Key Contributions:**

The paper analyzes which information-theoretic mechanisms resist adversarial manipulation, extending finite-sample bounds to show that bounded f-divergences (e.g., total variation distance) maintain polynomial guarantees under attacks while unbounded measures (e.g., KL divergence) degrade exponentially.

The authors model the overseer as an agent and characterize incentive-compatible scoring rules as f-mutual information objectives.

**Results:** Under adversarial attacks, TVD-MI maintains effectiveness (area under curve 0.70-0.77) while traditional judge queries are near chance (AUC ≈ 0.50).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d5e1986-df89-4c66-9af5-d2d18a28d64f",
  "isSidechain": false,
  "promptId": "93b903bb-07b4-406c-b81b-081fe808e171",
  "type": "user",
  "uuid": "5379d7b6-9f74-46d8-8aad-e0a764d62f06",
  "toolUseResult": {
    "query": "Robertson Koyejo \"bounded f-divergence\" TVD-MI LLM evaluation certification arXiv 2508.05469",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YBsWMp8ZXQ5N7aTy5bU8WS",
        "content": [
          {
            "title": "Identity-Link IRT for Label-Free LLM Evaluation:",
            "url": "https://arxiv.org/pdf/2510.14966"
          },
          {
            "title": "[2508.05469] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/abs/2508.05469"
          },
          {
            "title": "Let’s Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/html/2508.05469"
          },
          {
            "title": "[PDF] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Let's-Measure-Information-Step-by-Step:-LLM-Based-Robertson-Koyejo/824098ede34f59514ebc25a69c69c68d1e89b664"
          },
          {
            "title": "Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/pdf/2508.05469"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Title:** \"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes\"\n\n**Authors:** Zachary Robertson and Sanmi Koyejo from Stanford University\n\n**ArXiv ID:** 2508.05469\n\n**Key Contributions:**\n\nThe paper analyzes which information-theoretic mechanisms resist adversarial manipulation, extending finite-sample bounds to show that bounded f-divergences (e.g., total variation distance) maintain polynomial guarantees under attacks while unbounded measures (e.g., KL divergence) degrade exponentially.\n\nThe authors model the overseer as an agent and characterize incentive-compatible scoring rules as f-mutual information objectives.\n\n**Results:** Under adversarial attacks, TVD-MI maintains effectiveness (area under curve 0.70-0.77) while traditional judge queries are near chance (AUC ≈ 0.50)."
    ],
    "durationSeconds": 4.356901946999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1d5e1986-df89-4c66-9af5-d2d18a28d64f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Corr…",
  "leafUuid": "5379d7b6-9f74-46d8-8aad-e0a764d62f06",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-judge LLM evaluation certifiable robustness bounds",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7"
}
```

---

### Tool result

_source line 23 · 2026-05-20T05:50:55.427Z_

<details><summary>↩ Tool result · `toolu_01Pq19eH87vBe4tBKsqyUARq`</summary>

```text
Web search results for query: "Yang et al diversity scaling multi-agent effective channel count entropy arXiv 2602.03794 ICLR 2026"

Links: [{"title":"[2602.03794] Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity","url":"https://arxiv.org/abs/2602.03794"},{"title":"Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity","url":"https://arxiv.org/pdf/2602.03794"},{"title":"Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity","url":"https://arxiv.org/html/2602.03794"},{"title":"[2602.03219v2] Beyond Quantity: Trajectory Diversity Scaling for Code Agents","url":"https://arxiv.org/abs/2602.03219v2"},{"title":"Building Coding Agents via Entropy-Enhanced Multi-Turn Preference Optimization","url":"https://arxiv.org/html/2509.12434v2"}]

I found the paper you're looking for! Here are the key details:

## Paper: "Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity"

**Authors:** Yingxuan Yang and 7 other authors

**arXiv ID:** 2602.03794

**Publication Date:** February 3, 2026

### Key Contributions:

The paper presents an information-theoretic framework showing that MAS performance is bounded by the intrinsic task uncertainty, not by agent count, and derives architecture-agnostic bounds demonstrating that improvements depend on how many effective channels the system accesses.

The research finds that scaling performance by increasing the number of agents exhibits strong diminishing returns in homogeneous settings, while introducing heterogeneity (such as different models, prompts, or tools) continues to yield substantial gains.

The authors introduce K*, an effective channel count that quantifies the number of effective channels without groundtruth labels.

### Empirical Results:

Heterogeneous configurations consistently outperform homogeneous scaling: 2 diverse agents can match or exceed the performance of 16 homogeneous agents.

The paper is available at arXiv: https://arxiv.org/abs/2602.03794


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42d92a8d-24b3-4cf4-b40e-4ed3ebfb00f1",
  "isSidechain": false,
  "promptId": "93b903bb-07b4-406c-b81b-081fe808e171",
  "type": "user",
  "uuid": "c0d03f76-3342-48bc-850d-3a6aecdb13a1",
  "toolUseResult": {
    "query": "Yang et al diversity scaling multi-agent effective channel count entropy arXiv 2602.03794 ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KuNgD7PUrMn4zfSDenZYTA",
        "content": [
          {
            "title": "[2602.03794] Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity",
            "url": "https://arxiv.org/abs/2602.03794"
          },
          {
            "title": "Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity",
            "url": "https://arxiv.org/pdf/2602.03794"
          },
          {
            "title": "Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity",
            "url": "https://arxiv.org/html/2602.03794"
          },
          {
            "title": "[2602.03219v2] Beyond Quantity: Trajectory Diversity Scaling for Code Agents",
            "url": "https://arxiv.org/abs/2602.03219v2"
          },
          {
            "title": "Building Coding Agents via Entropy-Enhanced Multi-Turn Preference Optimization",
            "url": "https://arxiv.org/html/2509.12434v2"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n## Paper: \"Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity\"\n\n**Authors:** Yingxuan Yang and 7 other authors\n\n**arXiv ID:** 2602.03794\n\n**Publication Date:** February 3, 2026\n\n### Key Contributions:\n\nThe paper presents an information-theoretic framework showing that MAS performance is bounded by the intrinsic task uncertainty, not by agent count, and derives architecture-agnostic bounds demonstrating that improvements depend on how many effective channels the system accesses.\n\nThe research finds that scaling performance by increasing the number of agents exhibits strong diminishing returns in homogeneous settings, while introducing heterogeneity (such as different models, prompts, or tools) continues to yield substantial gains.\n\nThe authors introduce K*, an effective channel count that quantifies the number of effective channels without groundtruth labels.\n\n### Empirical Results:\n\nHeterogeneous configurations consistently outperform homogeneous scaling: 2 diverse agents can match or exceed the performance of 16 homogeneous agents.\n\nThe paper is available at arXiv: https://arxiv.org/abs/2602.03794"
    ],
    "durationSeconds": 6.494916700000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "42d92a8d-24b3-4cf4-b40e-4ed3ebfb00f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T05:50:58.846Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EXMQp2hHCd4VmA7CBVJ7Gj`</summary>

```json
{
  "query": "PEG peer prediction LLM evaluation Chen et al NeurIPS 2025 arXiv 2505.13636 conditional independence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0d03f76-3342-48bc-850d-3a6aecdb13a1",
  "isSidechain": false,
  "requestId": "req_011CbDJFX6eV3pnnrBJes2BR",
  "type": "assistant",
  "uuid": "1f40ec73-6baa-4c6a-8d38-2926e70d8ec9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Btrq4K8pvznvUx1xNJPekg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1905,
      "cache_read_input_tokens": 25082,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1905,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 25082,
          "cache_creation_input_tokens": 1905,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1905
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

_source line 25 · 2026-05-20T05:50:59.393Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J3gnYv1Gc69ohCAeXSMU9e`</summary>

```json
{
  "query": "Kaneko Baldwin \"bits leaked per query\" information-theoretic adversarial attack LLM arXiv 2510.17000 NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f40ec73-6baa-4c6a-8d38-2926e70d8ec9",
  "isSidechain": false,
  "requestId": "req_011CbDJFX6eV3pnnrBJes2BR",
  "type": "assistant",
  "uuid": "9aa53310-d427-45c1-bbc0-114819ef7167",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Btrq4K8pvznvUx1xNJPekg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1905,
      "cache_read_input_tokens": 25082,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1905,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 25082,
          "cache_creation_input_tokens": 1905,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1905
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

_source line 26 · 2026-05-20T05:51:04.978Z_

<details><summary>↩ Tool result · `toolu_01J3gnYv1Gc69ohCAeXSMU9e`</summary>

```text
Web search results for query: "Kaneko Baldwin "bits leaked per query" information-theoretic adversarial attack LLM arXiv 2510.17000 NeurIPS 2025"

Links: [{"title":"[2510.17000] Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs","url":"https://arxiv.org/abs/2510.17000"},{"title":"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs","url":"https://arxiv.org/html/2510.17000"},{"title":"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs","url":"https://arxiv.org/pdf/2510.17000"},{"title":"Bits Leaked per Query: Information-Theoretic Bounds for Adversarial Attacks on LLMs | OpenReview","url":"https://openreview.net/forum?id=DwXX8c7xst"},{"title":"Information-Theoretic Bounds on Adversarial Attacks against LLMs","url":"https://bytez.com/docs/arxiv/2510.17000/paper"}]

I found the paper you're looking for! Here's what I found:

"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs" is by Masahiro Kaneko and Timothy Baldwin. The paper frames adversarial attacks on LLMs as attempts to infer a target property that becomes knowable only after the model's reply is observed, with examples including the binary flag that triggers harmful responses or rejection, and the degree to which information deleted by unlearning can be restored.

The LLM reveals an observable signal that potentially leaks hints for attacking through a response containing answer tokens, thinking process tokens, or logits. The paper presents an information-theoretic framework that computes how much information can be safely disclosed, treating the mutual information between the observation and target property as the leaked bits per query, showing that achieving error ε requires at least log(1/ε)/I(Z;T) queries.

Experiments on seven LLMs across system-prompt leakage, jailbreak, and relearning attacks show that exposing answer tokens alone requires about a thousand queries; adding logits cuts this to about a hundred; and revealing the full thinking process trims it to a few dozen.

The paper has arXiv identifier 2510.17000 and was posted on October 19, 2025. It's also been submitted to OpenReview and appears to be associated with NeurIPS 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9aa53310-d427-45c1-bbc0-114819ef7167",
  "isSidechain": false,
  "promptId": "93b903bb-07b4-406c-b81b-081fe808e171",
  "type": "user",
  "uuid": "f4c669ec-69be-495a-841c-32f5fbc3567d",
  "toolUseResult": {
    "query": "Kaneko Baldwin \"bits leaked per query\" information-theoretic adversarial attack LLM arXiv 2510.17000 NeurIPS 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QpwHoQ7Asj23NoMtRkx7ex",
        "content": [
          {
            "title": "[2510.17000] Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs",
            "url": "https://arxiv.org/abs/2510.17000"
          },
          {
            "title": "Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs",
            "url": "https://arxiv.org/html/2510.17000"
          },
          {
            "title": "Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs",
            "url": "https://arxiv.org/pdf/2510.17000"
          },
          {
            "title": "Bits Leaked per Query: Information-Theoretic Bounds for Adversarial Attacks on LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=DwXX8c7xst"
          },
          {
            "title": "Information-Theoretic Bounds on Adversarial Attacks against LLMs",
            "url": "https://bytez.com/docs/arxiv/2510.17000/paper"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found:\n\n\"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs\" is by Masahiro Kaneko and Timothy Baldwin. The paper frames adversarial attacks on LLMs as attempts to infer a target property that becomes knowable only after the model's reply is observed, with examples including the binary flag that triggers harmful responses or rejection, and the degree to which information deleted by unlearning can be restored.\n\nThe LLM reveals an observable signal that potentially leaks hints for attacking through a response containing answer tokens, thinking process tokens, or logits. The paper presents an information-theoretic framework that computes how much information can be safely disclosed, treating the mutual information between the observation and target property as the leaked bits per query, showing that achieving error ε requires at least log(1/ε)/I(Z;T) queries.\n\nExperiments on seven LLMs across system-prompt leakage, jailbreak, and relearning attacks show that exposing answer tokens alone requires about a thousand queries; adding logits cuts this to about a hundred; and revealing the full thinking process trims it to a few dozen.\n\nThe paper has arXiv identifier 2510.17000 and was posted on October 19, 2025. It's also been submitted to OpenReview and appears to be associated with NeurIPS 2025."
    ],
    "durationSeconds": 5.5825315440000045,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9aa53310-d427-45c1-bbc0-114819ef7167",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T05:51:11.173Z_

<details><summary>↩ Tool result · `toolu_01EXMQp2hHCd4VmA7CBVJ7Gj`</summary>

```text
Web search results for query: "PEG peer prediction LLM evaluation Chen et al NeurIPS 2025 arXiv 2505.13636 conditional independence"

Links: [{"title":"[2505.13636] Incentivizing Truthful Language Models via Peer Elicitation Games","url":"https://arxiv.org/abs/2505.13636"},{"title":"Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction","url":"https://arxiv.org/pdf/2601.20299"},{"title":"Evaluating LLM-Contaminated Crowdsourcing Data Without Ground Truth","url":"https://arxiv.org/pdf/2506.06991"},{"title":"Eliciting Informative Text Evaluations with Large Language Models","url":"https://arxiv.org/pdf/2405.15077"},{"title":"Machine Learning May 2025","url":"https://www.arxiv.org/list/cs.LG/2025-05?skip=1100&show=2000"}]

I found the paper you're looking for! Here's what I found:

**"Incentivizing Truthful Language Models via Peer Elicitation Games"** introduces Peer Elicitation Games (PEG), a training-free, game-theoretic framework for aligning LLMs through a peer elicitation mechanism involving a generator and multiple discriminators instantiated from distinct base models.

Discriminators interact in a peer evaluation setting, where utilities are computed using a determinant-based mutual information score that provably incentivizes truthful reporting without requiring ground-truth labels.

The paper establishes theoretical guarantees showing that each agent, via online learning, achieves sublinear regret in the sense their cumulative performance approaches that of the best fixed truthful strategy in hindsight. Moreover, the authors prove last-iterate convergence to a truthful Nash equilibrium, ensuring that the actual policies used by agents converge to stable and truthful behavior over time.

Empirical evaluations across multiple benchmarks demonstrate significant improvements in factual accuracy, positioning PEG as a practical approach for eliciting truthful behavior from LLMs without supervision or fine-tuning.

The authors are Baiting Chen, Tong Zhu, Jiale Han, Lexin Li, Gang Li, and Xiaowu Dai. The paper appears to be relevant to the NeurIPS 2025 submission timeline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f40ec73-6baa-4c6a-8d38-2926e70d8ec9",
  "isSidechain": false,
  "promptId": "93b903bb-07b4-406c-b81b-081fe808e171",
  "type": "user",
  "uuid": "a86a81d5-cbec-4d3b-b5c5-923928fbe1dc",
  "toolUseResult": {
    "query": "PEG peer prediction LLM evaluation Chen et al NeurIPS 2025 arXiv 2505.13636 conditional independence",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Rzzy9XUpWexNka8Pv2eeRF",
        "content": [
          {
            "title": "[2505.13636] Incentivizing Truthful Language Models via Peer Elicitation Games",
            "url": "https://arxiv.org/abs/2505.13636"
          },
          {
            "title": "Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction",
            "url": "https://arxiv.org/pdf/2601.20299"
          },
          {
            "title": "Evaluating LLM-Contaminated Crowdsourcing Data Without Ground Truth",
            "url": "https://arxiv.org/pdf/2506.06991"
          },
          {
            "title": "Eliciting Informative Text Evaluations with Large Language Models",
            "url": "https://arxiv.org/pdf/2405.15077"
          },
          {
            "title": "Machine Learning May 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-05?skip=1100&show=2000"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found:\n\n**\"Incentivizing Truthful Language Models via Peer Elicitation Games\"** introduces Peer Elicitation Games (PEG), a training-free, game-theoretic framework for aligning LLMs through a peer elicitation mechanism involving a generator and multiple discriminators instantiated from distinct base models.\n\nDiscriminators interact in a peer evaluation setting, where utilities are computed using a determinant-based mutual information score that provably incentivizes truthful reporting without requiring ground-truth labels.\n\nThe paper establishes theoretical guarantees showing that each agent, via online learning, achieves sublinear regret in the sense their cumulative performance approaches that of the best fixed truthful strategy in hindsight. Moreover, the authors prove last-iterate convergence to a truthful Nash equilibrium, ensuring that the actual policies used by agents converge to stable and truthful behavior over time.\n\nEmpirical evaluations across multiple benchmarks demonstrate significant improvements in factual accuracy, positioning PEG as a practical approach for eliciting truthful behavior from LLMs without supervision or fine-tuning.\n\nThe authors are Baiting Chen, Tong Zhu, Jiale Han, Lexin Li, Gang Li, and Xiaowu Dai. The paper appears to be relevant to the NeurIPS 2025 submission timeline."
    ],
    "durationSeconds": 12.322515660000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1f40ec73-6baa-4c6a-8d38-2926e70d8ec9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T05:51:14.338Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xgf9HHZw6zBH7iCTMfutte`</summary>

```json
{
  "query": "Turkmen et al correlated LLM errors Gaussian copula ensemble error floor arXiv 2602.08003 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a86a81d5-cbec-4d3b-b5c5-923928fbe1dc",
  "isSidechain": false,
  "requestId": "req_011CbDJGgR1qQP4BgD6w6nfJ",
  "type": "assistant",
  "uuid": "4f644cd0-c3a0-4e08-b205-1a6fb5660850",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LUWb6MTJByGc7syYb1H8y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 670,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 26987,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 770,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 670,
          "output_tokens": 145,
          "cache_read_input_tokens": 26987,
          "cache_creation_input_tokens": 770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 770
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

_source line 29 · 2026-05-20T05:51:15.208Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018UUy4mEeD9bpu1LmKe3Tzb`</summary>

```json
{
  "query": "Kim et al correlated errors LLMs ICML 2025 arXiv 2506.07962 same architecture provider agreement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f644cd0-c3a0-4e08-b205-1a6fb5660850",
  "isSidechain": false,
  "requestId": "req_011CbDJGgR1qQP4BgD6w6nfJ",
  "type": "assistant",
  "uuid": "97f8fa55-9d44-463f-95c7-78a0f6a33118",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LUWb6MTJByGc7syYb1H8y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 670,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 26987,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 770,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 670,
          "output_tokens": 145,
          "cache_read_input_tokens": 26987,
          "cache_creation_input_tokens": 770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 770
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

_source line 30 · 2026-05-20T05:51:19.971Z_

<details><summary>↩ Tool result · `toolu_01Xgf9HHZw6zBH7iCTMfutte`</summary>

```text
Web search results for query: "Turkmen et al correlated LLM errors Gaussian copula ensemble error floor arXiv 2602.08003 2026"

Links: [{"title":"[2602.08003] Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection","url":"https://arxiv.org/abs/2602.08003"},{"title":"Don’t Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection","url":"https://arxiv.org/html/2602.08003"},{"title":"Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection","url":"https://arxiv.org/pdf/2602.08003"},{"title":"Breaking the Ceiling of the LLM Community by Treating Token Generation   as a Classification for Ensembling","url":"https://arxiv.org/pdf/2406.12585"},{"title":"LLMs and the Madness of Crowds","url":"https://arxiv.org/pdf/2411.01539"},{"title":"Pareto Optimal Learning for Estimating Large Language Model Errors","url":"https://arxiv.org/pdf/2306.16564"}]

Based on the web search results, I found the paper you're looking for:

The paper "Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection" by Yigit Turkmen, Baturalp Buyukates, and Melih Bastopcu addresses how large language models are often ensembled together to improve overall reliability and robustness, but in practice models are strongly correlated, raising the question of which models should be selected when forming an LLM ensemble.

The paper models the correlated errors of the models using Gaussian-copula and shows an information-theoretic error floor for the performance of the ensemble. The authors formulate budgeted ensemble selection as maximizing the mutual information between the true label and predictions of the selected models.

The paper was published on arXiv on February 8, 2026, with the identifier 2602.08003, matching your search query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f644cd0-c3a0-4e08-b205-1a6fb5660850",
  "isSidechain": false,
  "promptId": "93b903bb-07b4-406c-b81b-081fe808e171",
  "type": "user",
  "uuid": "92392cb1-0d2b-4b96-8c55-91fa26554bd5",
  "toolUseResult": {
    "query": "Turkmen et al correlated LLM errors Gaussian copula ensemble error floor arXiv 2602.08003 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EP1EacCqYD5MsxJZjY3RPd",
        "content": [
          {
            "title": "[2602.08003] Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection",
            "url": "https://arxiv.org/abs/2602.08003"
          },
          {
            "title": "Don’t Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection",
            "url": "https://arxiv.org/html/2602.08003"
          },
          {
            "title": "Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection",
            "url": "https://arxiv.org/pdf/2602.08003"
          },
          {
            "title": "Breaking the Ceiling of the LLM Community by Treating Token Generation   as a Classification for Ensembling",
            "url": "https://arxiv.org/pdf/2406.12585"
          },
          {
            "title": "LLMs and the Madness of Crowds",
            "url": "https://arxiv.org/pdf/2411.01539"
          },
          {
            "title": "Pareto Optimal Learning for Estimating Large Language Model Errors",
            "url": "https://arxiv.org/pdf/2306.16564"
          }
        ]
      },
      "Based on the web search results, I found the paper you're looking for:\n\nThe paper \"Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection\" by Yigit Turkmen, Baturalp Buyukates, and Melih Bastopcu addresses how large language models are often ensembled together to improve overall reliability and robustness, but in practice models are strongly correlated, raising the question of which models should be selected when forming an LLM ensemble.\n\nThe paper models the correlated errors of the models using Gaussian-copula and shows an information-theoretic error floor for the performance of the ensemble. The authors formulate budgeted ensemble selection as maximizing the mutual information between the true label and predictions of the selected models.\n\nThe paper was published on arXiv on February 8, 2026, with the identifier 2602.08003, matching your search query."
    ],
    "durationSeconds": 5.628523386,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4f644cd0-c3a0-4e08-b205-1a6fb5660850",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T05:51:21.276Z_

<details><summary>↩ Tool result · `toolu_018UUy4mEeD9bpu1LmKe3Tzb`</summary>

```text
Web search results for query: "Kim et al correlated errors LLMs ICML 2025 arXiv 2506.07962 same architecture provider agreement"

Links: [{"title":"[2506.07962] Correlated Errors in Large Language Models","url":"https://arxiv.org/abs/2506.07962"},{"title":"[Paper Note] Correlated Errors in Large Language Models, Elliot Kim+, ICML'25 · Issue #2145 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/2145"},{"title":"[2506.07962v1] Correlated Errors in Large Language Models","url":"https://arxiv.org/abs/2506.07962v1"},{"title":"[PDF] Correlated Errors in Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Correlated-Errors-in-Large-Language-Models-Kim-Garg/365ba5ab458c8ad6d4ed6996ab3e0ff3f386edbc"},{"title":"(PDF) Correlated Errors in Large Language Models","url":"https://www.researchgate.net/publication/392529896_Correlated_Errors_in_Large_Language_Models"},{"title":"arXiv:2506.07962v1 [cs.CL] 9 Jun 2025","url":"https://arxiv.org/pdf/2506.07962"},{"title":"LLMs and the Madness of Crowds","url":"https://arxiv.org/pdf/2411.01539"},{"title":"LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations","url":"https://arxiv.org/pdf/2410.02707"}]

Great! I found the paper. Here's the information about the research:

The paper "Correlated Errors in Large Language Models" is authored by Elliot Kim, Avi Garg, Kenny Peng, and Nikhil Garg, and it has been accepted to ICML 2025 (arXiv 2506.07962).

**Key Findings:**

The paper conducts a large-scale empirical evaluation on over 350 LLMs overall, using two popular leaderboards and a resume-screening task.

They find substantial correlation in model errors -- on one leaderboard dataset, models agree 60% of the time when both models err.

**Factors Driving Correlation:**

The authors identify factors driving model correlation, including shared architectures and providers. However, larger and more accurate models have highly correlated errors, even with distinct architectures and providers.

**Implications:**

The paper shows the effects of correlation in two downstream tasks: LLM-as-judge evaluation and hiring -- the latter reflecting theoretical predictions regarding algorithmic monoculture.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97f8fa55-9d44-463f-95c7-78a0f6a33118",
  "isSidechain": false,
  "promptId": "93b903bb-07b4-406c-b81b-081fe808e171",
  "type": "user",
  "uuid": "913bd509-4d16-4e87-837a-9d69a9e380c8",
  "toolUseResult": {
    "query": "Kim et al correlated errors LLMs ICML 2025 arXiv 2506.07962 same architecture provider agreement",
    "results": [
      {
        "tool_use_id": "srvtoolu_018fbSggZi7QbsNqCLeaSquq",
        "content": [
          {
            "title": "[2506.07962] Correlated Errors in Large Language Models",
            "url": "https://arxiv.org/abs/2506.07962"
          },
          {
            "title": "[Paper Note] Correlated Errors in Large Language Models, Elliot Kim+, ICML'25 · Issue #2145 · AkihikoWatanabe/paper_notes",
            "url": "https://github.com/AkihikoWatanabe/paper_notes/issues/2145"
          },
          {
            "title": "[2506.07962v1] Correlated Errors in Large Language Models",
            "url": "https://arxiv.org/abs/2506.07962v1"
          },
          {
            "title": "[PDF] Correlated Errors in Large Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Correlated-Errors-in-Large-Language-Models-Kim-Garg/365ba5ab458c8ad6d4ed6996ab3e0ff3f386edbc"
          },
          {
            "title": "(PDF) Correlated Errors in Large Language Models",
            "url": "https://www.researchgate.net/publication/392529896_Correlated_Errors_in_Large_Language_Models"
          },
          {
            "title": "arXiv:2506.07962v1 [cs.CL] 9 Jun 2025",
            "url": "https://arxiv.org/pdf/2506.07962"
          },
          {
            "title": "LLMs and the Madness of Crowds",
            "url": "https://arxiv.org/pdf/2411.01539"
          },
          {
            "title": "LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations",
            "url": "https://arxiv.org/pdf/2410.02707"
          }
        ]
      },
      "Great! I found the paper. Here's the information about the research:\n\nThe paper \"Correlated Errors in Large Language Models\" is authored by Elliot Kim, Avi Garg, Kenny Peng, and Nikhil Garg, and it has been accepted to ICML 2025 (arXiv 2506.07962).\n\n**Key Findings:**\n\nThe paper conducts a large-scale empirical evaluation on over 350 LLMs overall, using two popular leaderboards and a resume-screening task.\n\nThey find substantial correlation in model errors -- on one leaderboard dataset, models agree 60% of the time when both models err.\n\n**Factors Driving Correlation:**\n\nThe authors identify factors driving model correlation, including shared architectures and providers. However, larger and more accurate models have highly correlated errors, even with distinct architectures and providers.\n\n**Implications:**\n\nThe paper shows the effects of correlation in two downstream tasks: LLM-as-judge evaluation and hiring -- the latter reflecting theoretical predictions regarding algorithmic monoculture."
    ],
    "durationSeconds": 6.066308499999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "97f8fa55-9d44-463f-95c7-78a0f6a33118",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-20T05:51:21.280Z_

```json
{
  "parentUuid": "913bd509-4d16-4e87-837a-9d69a9e380c8",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "456a93f0-f16e-4f65-b68c-e49f3acd33b6",
  "timestamp": "2026-05-20T05:51:21.280Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-20T05:51:25.113Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the key related works. Let me also search for the certified ensemble robustness works and the Horvath et al. variance reduction paper to understand how well the theoretical foundations of this proposal hold up.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "456a93f0-f16e-4f65-b68c-e49f3acd33b6",
  "isSidechain": false,
  "requestId": "req_011CbDJHRhGWx4daBunoKLW2",
  "type": "assistant",
  "uuid": "f15bbf92-5329-45b4-bffb-7eb0a5f147c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QotsoZm7Rcc83zXqhEJU9U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2222,
      "cache_read_input_tokens": 27757,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 27757,
          "cache_creation_input_tokens": 2222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2222
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

_source line 34 · 2026-05-20T05:51:26.014Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DExx1tfraaWExmRcbg1qm4`</summary>

```json
{
  "query": "Horvath et al boosting randomized smoothing variance reduced classifiers certified radius sqrt K ensemble arXiv 2106.06946"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f15bbf92-5329-45b4-bffb-7eb0a5f147c8",
  "isSidechain": false,
  "requestId": "req_011CbDJHRhGWx4daBunoKLW2",
  "type": "assistant",
  "uuid": "249e73bc-dc83-4263-93f9-c3aa4baf0478",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QotsoZm7Rcc83zXqhEJU9U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2222,
      "cache_read_input_tokens": 27757,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 27757,
          "cache_creation_input_tokens": 2222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2222
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

_source line 35 · 2026-05-20T05:51:26.922Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XoXS8En7MrzzuopQR3j91c`</summary>

```json
{
  "query": "certified robustness ensemble models diversified gradient confidence margin arXiv 2107.10873 Chen 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "249e73bc-dc83-4263-93f9-c3aa4baf0478",
  "isSidechain": false,
  "requestId": "req_011CbDJHRhGWx4daBunoKLW2",
  "type": "assistant",
  "uuid": "b05f9e83-d3b0-4746-94c6-2876c39af2ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QotsoZm7Rcc83zXqhEJU9U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2222,
      "cache_read_input_tokens": 27757,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 27757,
          "cache_creation_input_tokens": 2222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2222
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

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Corr…",
  "leafUuid": "b05f9e83-d3b0-4746-94c6-2876c39af2ce",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-judge LLM evaluation certifiable robustness bounds",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7"
}
```

---

### Tool result

_source line 38 · 2026-05-20T05:51:33.078Z_

<details><summary>↩ Tool result · `toolu_01DExx1tfraaWExmRcbg1qm4`</summary>

```text
Web search results for query: "Horvath et al boosting randomized smoothing variance reduced classifiers certified radius sqrt K ensemble arXiv 2106.06946"

Links: [{"title":"[2106.06946] Boosting Randomized Smoothing with Variance Reduced Classifiers","url":"https://arxiv.org/abs/2106.06946"},{"title":"Rethinking Randomized Smoothing from the Perspective of Scalability","url":"https://arxiv.org/html/2312.12608"},{"title":"Boosting Randomized Smoothing with Variance Reduced Classifiers | SRI Lab","url":"https://www.sri.inf.ethz.ch/blog/smoothens"},{"title":"Boosting Randomized Smoothing with Variance Reduced Classifiers","url":"https://arxiv.org/pdf/2106.06946"},{"title":"GitHub - eth-sri/smoothing-ensembles: [ICLR 2022] Boosting Randomized Smoothing with Variance Reduced Classifiers · GitHub","url":"https://github.com/eth-sri/smoothing-ensembles"},{"title":"dblp: Miklós Z. Horváth","url":"https://dblp.org/pid/294/8640.html"},{"title":"Multi-head ensemble of smoothed classifiers for certified robustness - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608025003053"},{"title":"Boosting Certificate Robustness for Time Series Classification with Efficient Self-Ensemble | Proceedings of the 33rd ACM International Conference on Information and Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3627673.3679748"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** Boosting Randomized Smoothing with Variance Reduced Classifiers

**Authors:** Miklós Z. Horváth, Mark Niklas Müller, Marc Fischer, Martin Vechev from ETH Zurich

**Main Contributions:**

The work theoretically motivates why ensembles are a particularly suitable choice as base models for RS, and empirically confirms this choice, obtaining state-of-the-art results in multiple settings.

The key insight is that the reduced variance of ensembles over the perturbations introduced in RS leads to significantly more consistent classifications for a given input, which in turn leads to substantially increased certifiable radii for samples close to the decision boundary.

**Key Results:**

Experimentally, ensembles of only 3 to 10 classifiers consistently improve on their strongest constituting model with respect to their average certified radius by 5% to 21% on both CIFAR10 and ImageNet, achieving a new state-of-the-art ACR of 0.86 and 1.11, respectively.

The work also introduces key optimizations which enable an up to 55-fold decrease in sample complexity of RS for predetermined radii, thus drastically reducing its computational overhead.

The paper is available on arXiv at https://arxiv.org/abs/2106.06946, and code and models are available at https://github.com/eth-sri/smoothing-ensembles.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "249e73bc-dc83-4263-93f9-c3aa4baf0478",
  "isSidechain": false,
  "promptId": "93b903bb-07b4-406c-b81b-081fe808e171",
  "type": "user",
  "uuid": "a3ba86da-fd9f-4635-89a1-771ad86af838",
  "toolUseResult": {
    "query": "Horvath et al boosting randomized smoothing variance reduced classifiers certified radius sqrt K ensemble arXiv 2106.06946",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TXzFXG1sMYTc7Uh1WxN482",
        "content": [
          {
            "title": "[2106.06946] Boosting Randomized Smoothing with Variance Reduced Classifiers",
            "url": "https://arxiv.org/abs/2106.06946"
          },
          {
            "title": "Rethinking Randomized Smoothing from the Perspective of Scalability",
            "url": "https://arxiv.org/html/2312.12608"
          },
          {
            "title": "Boosting Randomized Smoothing with Variance Reduced Classifiers | SRI Lab",
            "url": "https://www.sri.inf.ethz.ch/blog/smoothens"
          },
          {
            "title": "Boosting Randomized Smoothing with Variance Reduced Classifiers",
            "url": "https://arxiv.org/pdf/2106.06946"
          },
          {
            "title": "GitHub - eth-sri/smoothing-ensembles: [ICLR 2022] Boosting Randomized Smoothing with Variance Reduced Classifiers · GitHub",
            "url": "https://github.com/eth-sri/smoothing-ensembles"
          },
          {
            "title": "dblp: Miklós Z. Horváth",
            "url": "https://dblp.org/pid/294/8640.html"
          },
          {
            "title": "Multi-head ensemble of smoothed classifiers for certified robustness - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0893608025003053"
          },
          {
            "title": "Boosting Certificate Robustness for Time Series Classification with Efficient Self-Ensemble | Proceedings of the 33rd ACM International Conference on Information and Knowledge Management",
            "url": "https://dl.acm.org/doi/10.1145/3627673.3679748"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n**Paper Title:** Boosting Randomized Smoothing with Variance Reduced Classifiers\n\n**Authors:** Miklós Z. Horváth, Mark Niklas Müller, Marc Fischer, Martin Vechev from ETH Zurich\n\n**Main Contributions:**\n\nThe work theoretically motivates why ensembles are a particularly suitable choice as base models for RS, and empirically confirms this choice, obtaining state-of-the-art results in multiple settings.\n\nThe key insight is that the reduced variance of ensembles over the perturbations introduced in RS leads to significantly more consistent classifications for a given input, which in turn leads to substantially increased certifiable radii for samples close to the decision boundary.\n\n**Key Results:**\n\nExperimentally, ensembles of only 3 to 10 classifiers consistently improve on their strongest constituting model with respect to their average certified radius by 5% to 21% on both CIFAR10 and ImageNet, achieving a new state-of-the-art ACR of 0.86 and 1.11, respectively.\n\nThe work also introduces key optimizations which enable an up to 55-fold decrease in sample complexity of RS for predetermined radii, thus drastically reducing its computational overhead.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2106.06946, and code and models are available at https://github.com/eth-sri/smoothing-ensembles."
    ],
    "durationSeconds": 7.058895696000007,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "249e73bc-dc83-4263-93f9-c3aa4baf0478",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-20T05:51:36.758Z_

<details><summary>↩ Tool result · `toolu_01XoXS8En7MrzzuopQR3j91c`</summary>

```text
Web search results for query: "certified robustness ensemble models diversified gradient confidence margin arXiv 2107.10873 Chen 2021"

Links: [{"title":"[2107.10873] On the Certified Robustness for Ensemble Models and Beyond","url":"https://arxiv.org/abs/2107.10873"},{"title":"(PDF) On the Certified Robustness for Ensemble Models and Beyond","url":"https://www.researchgate.net/publication/353451347_On_the_Certified_Robustness_for_Ensemble_Models_and_Beyond"},{"title":"ON THE CERTIFIED ROBUSTNESS FOR ENSEMBLE ...","url":"https://openreview.net/pdf?id=tUa4REjGjTf"},{"title":"ON THE CERTIFIED ROBUSTNESS FOR ENSEMBLE MODELS ...","url":"https://openreview.net/pdf?id=IUYthV32lbK"},{"title":"Enhancing Certifiable Robustness via a Deep Model Ensemble","url":"https://arxiv.org/pdf/1910.14655"},{"title":"Certifying Joint Adversarial Robustness for Model Ensembles","url":"https://arxiv.org/pdf/2004.10250"}]

Based on the search results, I found the paper you're looking for:

"On the Certified Robustness for Ensemble Models and Beyond" (arXiv 2107.10873) analyzes and provides certified robustness for ensemble ML models, together with sufficient and necessary conditions of robustness for different ensemble protocols.

The key finding is that diversified gradient and large confidence margin are sufficient and necessary conditions for certifiably robust ensemble models. 

Interestingly, although ensemble models are shown more robust than a single model empirically, standard ensemble models only achieve marginal improvement compared to a single model in terms of certified robustness.

The paper provides bounded model-smoothness analysis based on the proposed Ensemble-before-Smoothing strategy and proves that an ensemble model can always achieve higher certified robustness than a single base model under mild conditions.

The authors propose DRT (Diversity-Regularized Training), a lightweight regularization-based training approach, containing both Gradient Diversity Loss and Confidence Margin Loss.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b05f9e83-d3b0-4746-94c6-2876c39af2ce",
  "isSidechain": false,
  "promptId": "93b903bb-07b4-406c-b81b-081fe808e171",
  "type": "user",
  "uuid": "2578b32d-2535-4549-9dd9-4d71de3d082a",
  "toolUseResult": {
    "query": "certified robustness ensemble models diversified gradient confidence margin arXiv 2107.10873 Chen 2021",
    "results": [
      {
        "tool_use_id": "srvtoolu_013SjNZPJrWHcH2sHiWZMV57",
        "content": [
          {
            "title": "[2107.10873] On the Certified Robustness for Ensemble Models and Beyond",
            "url": "https://arxiv.org/abs/2107.10873"
          },
          {
            "title": "(PDF) On the Certified Robustness for Ensemble Models and Beyond",
            "url": "https://www.researchgate.net/publication/353451347_On_the_Certified_Robustness_for_Ensemble_Models_and_Beyond"
          },
          {
            "title": "ON THE CERTIFIED ROBUSTNESS FOR ENSEMBLE ...",
            "url": "https://openreview.net/pdf?id=tUa4REjGjTf"
          },
          {
            "title": "ON THE CERTIFIED ROBUSTNESS FOR ENSEMBLE MODELS ...",
            "url": "https://openreview.net/pdf?id=IUYthV32lbK"
          },
          {
            "title": "Enhancing Certifiable Robustness via a Deep Model Ensemble",
            "url": "https://arxiv.org/pdf/1910.14655"
          },
          {
            "title": "Certifying Joint Adversarial Robustness for Model Ensembles",
            "url": "https://arxiv.org/pdf/2004.10250"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"On the Certified Robustness for Ensemble Models and Beyond\" (arXiv 2107.10873) analyzes and provides certified robustness for ensemble ML models, together with sufficient and necessary conditions of robustness for different ensemble protocols.\n\nThe key finding is that diversified gradient and large confidence margin are sufficient and necessary conditions for certifiably robust ensemble models. \n\nInterestingly, although ensemble models are shown more robust than a single model empirically, standard ensemble models only achieve marginal improvement compared to a single model in terms of certified robustness.\n\nThe paper provides bounded model-smoothness analysis based on the proposed Ensemble-before-Smoothing strategy and proves that an ensemble model can always achieve higher certified robustness than a single base model under mild conditions.\n\nThe authors propose DRT (Diversity-Regularized Training), a lightweight regularization-based training approach, containing both Gradient Diversity Loss and Confidence Margin Loss."
    ],
    "durationSeconds": 9.83366739000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b05f9e83-d3b0-4746-94c6-2876c39af2ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-20T05:52:18.275Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have sufficient background to evaluate this proposal. Let me also do one more search on the specific connection between this work and EMNLP — the proposal lists target venues as ICLR 2027, AAAI 2027, USENIX Security 2027, and NeurIPS 2026 workshops. The user asks me to evaluate for EMNLP 2026. Let me note that this is an important mismatch but per my instructions, I should NOT use "this idea fits another conference better" as a reason to score it lower. I should focus purely on academic quality.


Now I'm pulling together what I've found across these papers. The SoK work validates the empirical foundation showing that multi-model committees can substantially reduce adversarial success rates, Robertson & Koyejo provides the information-theoretic framework this proposal builds on, and Yang et al. establishes the key scaling relationship that connects entropy to optimal committee size.

The remaining papers fill in critical gaps: Kaneko & Baldwin gives single-model attack bounds that need extending to the multi-judge case, Turkmen et al. models how errors correlate across different LLMs, Kim et al. shows this correlation increases with model capability, Horvath et al. demonstrates certified robustness gains through variance reduction, and Chen et al. establishes that standard ensembles alone don't provide meaningful robustness guarantees.

So the core claim here is that this proposal provides the adversarial dual to Yang et al.'s performance scaling result, while extending the information-theoretic bounds to handle multiple judges and correlated errors.

Now evaluating the strengths: the research question addresses a genuinely important problem.

The strengths are compelling — the adversarial dual framing elegantly captures how performance scales exponentially with diversity while robustness only scales polynomially, the connection between measurable inter-judge correlation and certified bounds is practically grounded, the PEG degradation analysis addresses a real gap, and the experimental work is impressively thorough with adaptive attacks, carefully matched baselines, copula validation across multiple benchmarks, and rigorous statistics. The diversity ceiling insight is particularly thought-provoking.

But there's a significant weakness: the ½ exponent for discrete text is only conjectured, which is a major gap for a theory paper since the main result Ω(K_eff^{1/2}) relies on this exponent being derived rather than assumed.

Beyond that, borrowing K* from performance scaling to adversarial robustness feels like a conceptual stretch — it was designed for one context and the extension to adversarial effective dimensionality is acknowledged but not convincingly justified. The proposal is also extremely dense, pulling together information theory, game theory, and statistical mechanics in ways that could make it hard to present clearly. There's a risk it reads as connecting existing tools rather than developing fundamentally new techniques, and the Ω(K_eff^{1/2}) bound itself may not be tight.

The computational cost of 1,800-2,800 H100-hours is substantial but defensible. Overall, this is a strong proposal addressing a real gap in the literature with elegant theory and comprehensive experiments. The main vulnerabilities are the conjectural exponent for discrete text, the borrowed K* approximation, and the possibility that reviewers see it as incremental rather than introducing novel methods. Still, the work shows deep engagement with the literature and the "adversarial dual of diversity scaling" framing is genuinely compelling.

The PEG degradation analysis adds meaningful secondary value. I'm concerned about a few things though: a theory-focused reviewer might challenge the ½ exponent assumption, the paper will need exceptionally clear writing given how intricate the framework is, and there's a real question about whether the certified bounds actually matter in practice or if they're too loose to be useful. The work sits at an interesting intersection of LLM evaluation security and information-theoretic guarantees, which is relevant to EMNLP's audience even if the venue skews more empirical than theoretical. The core question is whether the academic contribution is strong enough to overcome these concerns.

Looking at the components: the novelty is solid, the theory is sound but relies on that conjectural exponent, the experimental plan is exceptionally thorough, and the feasibility looks reasonable with the proposed compute. The main wildcard is execution—this is genuinely complex to write well. Weighing everything together, I'd estimate this lands somewhere in the 28-42% range, with a median around 35%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2578b32d-2535-4549-9dd9-4d71de3d082a",
  "isSidechain": false,
  "requestId": "req_011CbDJJZni7faGwcnkaHPk5",
  "type": "assistant",
  "uuid": "430e325c-4e28-4eee-8703-fe57405ced86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTWfsHEPEbvUoPf33aEDfT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1602,
      "cache_read_input_tokens": 29979,
      "output_tokens": 6082,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1602,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6082,
          "cache_read_input_tokens": 29979,
          "cache_creation_input_tokens": 1602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1602
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

_source line 41 · 2026-05-20T05:53:56.523Z_

Now I have sufficient research to provide a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [SoK: Security in LLM-as-a-Judge (arXiv 2603.29403)](https://arxiv.org/abs/2603.29403) (2026): 直接动机——863篇文献综述，发现开源judge模型50-68% ASR，7-model committee降至10-19%但缺乏形式化解释。本proposal正是要填补"为什么committee有效"的理论空白。
- [Robertson & Koyejo, "Let's Measure Information Step-by-Step" (arXiv 2508.05469)](https://arxiv.org/abs/2508.05469) (2025, TMLR under review): 建立bounded f-divergence (TVD-MI)单评估器认证框架，AUC 0.70-0.77。本proposal直接扩展其Theorem 3.3到N-judge场景。
- [Kaneko & Baldwin, "Bits Leaked per Query" (arXiv 2510.17000)](https://arxiv.org/abs/2510.17000) (NeurIPS 2025 spotlight): 建立单模型信息泄漏下界N_min ≥ log₂(1/ε)/I_max。本proposal将其组合到多judge场景。
- [Yang et al., "Understanding Agent Scaling via Diversity" (arXiv 2602.03794)](https://arxiv.org/abs/2602.03794) (ICLR 2026 Workshop): 建立K* = 2^{H(ρ)}有效通道数，性能指数级衰减。本proposal声称建立其"对抗性对偶"——操控代价仅多项式增长。
- [Turkmen et al., "Don't Always Pick the Highest-Performing Model" (arXiv 2602.08003)](https://arxiv.org/abs/2602.08003) (2026): Gaussian copula建模相关性错误，MI分解用于ensemble selection。本proposal借用其相关性模型推导closed-form K_eff。
- [Kim et al., "Correlated Errors in Large Language Models" (arXiv 2506.07962)](https://arxiv.org/abs/2506.07962) (ICML 2025): 350+LLM实证——60%错误一致率，同架构+0.066，同公司+0.076，更强模型更相关。支撑本proposal的"diversity ceiling"论断。
- [Chen et al., PEG (arXiv 2505.13636)](https://arxiv.org/abs/2505.13636) (NeurIPS 2025): Peer Elicitation Games，DMI激励下dominant-strategy truthfulness，但Assumption 4要求条件独立。本proposal分析违反条件独立时的退化。
- [Horvath et al., "Boosting Randomized Smoothing" (arXiv 2106.06946)](https://arxiv.org/abs/2106.06946) (ICLR 2022): 连续空间中ensemble的√K认证半径提升。本proposal的½指数直接来源于此。
- [Chen et al., "On the Certified Robustness for Ensemble Models" (arXiv 2107.10873)](https://arxiv.org/abs/2107.10873) (ICLR 2022): 证明标准ensemble在certified robustness上仅有marginal改进；diversified gradient + confidence margin是充要条件。

- 调研总结: LLM-as-a-Judge安全性是2025-2026年的热门课题，经验性发现（multi-model committee大幅降低ASR）已有，但缺乏将操控代价与可度量的judge间相关性形式化联系的理论框架。本proposal精准定位在这个空白上，且所引用的核心文献均可验证为真实存在的近期工作。

【整体印象】:
如果我是审稿人，第一反应是：这是一篇**雄心勃勃、文献调研极其扎实、实验方案详尽到近乎过度**的proposal。研究问题定位精准——"为什么multi-judge能降低ASR？能否给出formal guarantee？"——这是领域真实需要回答的问题。"adversarial dual of diversity scaling"的叙事框架优雅，"指数性能 vs. 多项式鲁棒性"的不对称性是一个有洞察力的结论。

然而，我会有以下核心疑虑：
(1) 主定理的½指数是从连续空间(ℓ₂)推导的，对离散文本扰动仅作为conjecture——这对一篇以"certifiable"为卖点的理论论文来说是显著软肋。
(2) 借用K*从performance context到adversarial context的正当性不够强。
(3) 理论贡献的"新意"需要仔细辨析——核心技术工具（SDPI、Marton不等式、Fano-ensemble分解）都是已有的，贡献在于composition和interpretation。
(4) 论文极度复杂，5个component + 3个理论贡献 + 大量实验，在8页正文中清晰呈现的写作难度极高。

整体倾向：**borderline accept / weak accept**，取决于执行质量，特别是理论表述的清晰度和empirical tightness实验的说服力。

【核心贡献】:
三层贡献：
1. **主贡献**：建立multi-judge操控代价的formal scaling law Ω(K_eff^{1/2})，揭示与performance scaling的指数-多项式不对称性。
2. **共主贡献**：PEG在条件独立假设违反时的ε-approximate equilibrium退化分析 ε = f(ρ)。
3. **实践贡献**：基于K_eff的prescriptive judge selection tool，以及"frontier diversity ceiling"的诊断性洞察。

贡献1如果成立（即½指数在离散场景也能被经验验证），对领域的价值是**高**的——它将SoK中的经验发现提升到了formal guarantee。贡献2是有意义的理论补充。贡献3的实践价值取决于bound的tightness。

【方法合理性】:
方法在大方向上是合理的：SDPI → per-channel information bound → additive composition → variance reduction → manipulation cost scaling。这条推理链在信息论文献中有先例（Polyanskiy & Wu; Horvath et al.）。

**但有两个关键技术质疑：**

(1) **½指数的离散延拓问题**：Horvath et al.的√K结果在连续ℓ₂空间中成立，因为Gaussian noise的variance reduction是well-behaved的。但LLM evaluation的"扰动"是离散文本——prompt injection、style manipulation等——其几何结构与ℓ₂截然不同。Proposal诚实地标注这是conjecture，但这意味着主定理在严格意义上是不完整的。这不是致命的（可以用empirical tightness来补充），但确实削弱了"certifiable"的claim。

(2) **K* 跨context借用**：Yang et al.的K*是在performance context下定义的（描述information gain for accuracy）。将其作为adversarial context的"upper-bound approximation of effective dimensionality"需要更强的论证——adversary的optimization landscape与random noise的statistical structure不同。Proposal承认这是approximation并计划empirical validation，这是正确的做法，但理论上留下了gap。

**是否有更简单的替代方案？** 部分结论可以通过更简单的方法得到——例如，简单的majority voting + correlation correction在实践中可能给出comparable的经验鲁棒性。但本proposal的独特价值在于formal guarantee而非empirical performance，所以替代方案并不能替代它的核心贡献。

【5 维度打分】:

1. 研究问题: 【强】 — "Multi-judge LLM evaluation的certified manipulation resistance如何随inter-judge correlation scaling?"是一个重要且timely的问题。SoK (arXiv 2603.29403)的经验发现（7-model committee降低ASR到10-19%）急需理论解释。Kim et al. (ICML 2025)揭示的相关性增长趋势使问题更加紧迫。问题定义清晰、有实际影响力。

2. 方法与创新: 【中偏强】 — 核心叙事"adversarial dual of diversity scaling"是新颖的概念贡献。但技术层面主要是existing tools的composition：SDPI (Polyanskiy & Wu)、Fano-ensemble (Morishita et al., ICML 2022)、Marton不等式、Robertson & Koyejo的Theorem 3.3、Horvath et al.的variance reduction。每一步都站在前人肩膀上，新的推导步骤是将它们串联并给出closed-form，创新度在"solid but not groundbreaking"。½指数的conjectural status进一步削弱了理论贡献的硬度。PEG退化分析是有意义的但规模较小的贡献。

3. 实验设计: 【强】 — 这是proposal最出色的部分。(a) 遵循Carlini et al. (arXiv 1902.06705) gold standard设计了3类adaptive attacks + convergence criteria；(b) FLOP-matched compute-normalized baselines排除了"多模型就是多计算"的trivial反驳；(c) copula GoF验证模型假设；(d) dual-scaling overlay visualization直接展示exponential-polynomial asymmetry；(e) PEG degradation的dedicated experiment设计合理（measured_ρ vs empirical_ε scatter）；(f) cross-domain calibration transfer + bootstrap CI + Benjamini-Hochberg/Bonferroni双重校正。实验方案的严谨度和完备度超过了多数proposal。

4. 可行性: 【中】 — 1,800-2,800 H100-hours是可行但不小的计算需求。理论部分需要严格的数学证明（SDPI composition、Marton bound extension），需要具备强信息论背景的团队。18-24周时间线合理但紧张。主要风险：pilot study可能发现所有open-weight模型ρ>0.7（proposal已有contingency plan），以及½指数的empirical validation可能不支持conjecture。Proposal的go/no-go pilot design是加分项。

5. 写作与呈现: 【中】 — Proposal本身展现了极强的文献掌握和逻辑组织能力。但复杂度极高（5个component、3个理论贡献、3个benchmark、15+off-the-shelf attacks + 3 adaptive attacks + 大量ablation），在8-9页正文中清晰呈现是巨大挑战。"certifiable"一词可能在离散conjecture的context下引起误解。需要非常精心的写作策略（可能将PEG退化分析放入appendix）。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】:
向上拉动的因素：(1) 研究问题精准定位真实gap，领域需求明确；(2) "adversarial dual"叙事框架有conceptual appeal；(3) 实验设计极其严谨，FLOP-matched baselines和adaptive attacks是strong signals of rigor；(4) 文献调研全面，positioning清晰；(5) "frontier diversity ceiling"是有传播力的insight。

向下拉动的因素：(1) 主定理的½指数在核心场景（discrete text）仅为conjecture，这对一篇标题含"certifiable"的论文是实质性弱点——审稿人很可能追问"what exactly is certified here?"；(2) 技术创新偏向composition而非fundamentally new techniques，novelty评判取决于审稿人是否看重"connecting existing tools to get a new result"；(3) 论文复杂度极高，写作不当会导致审稿人迷失在细节中给出negative review；(4) K*的跨context借用可能被theory-oriented reviewer challenge。

综合判断：这是一篇**有真实贡献的solid work**，但不是那种让审稿人毫不犹豫给accept的"slam dunk"。35%的中位估计反映的是：如果execution完美（写作清晰、½指数empirical验证convincing、bound tightness demonstrations strong），概率可达42%；如果writing不够清晰或empirical results equivocal，概率可降至28%。

【主要风险】:
1. **½指数的conjectural nature**：标题和framing强调"certifiable"，但核心exponent在实际应用场景（discrete text perturbation）中仅为conjecture。一个严格的审稿人会指出：如果exponent未被证明，那么"certified"是overstatement。如果empirical tightness实验显示实际exponent显著偏离½，整个framework的实用价值受质疑。
2. **论文复杂度与清晰度的矛盾**：5 components × 3 benchmarks × 18+ attacks × 大量ablation的规模在有限页面内难以清晰呈现。审稿人可能因为无法在review时间内完全理解而给出conservative（偏negative）评分。

【实施评估】:
  - 计算资源: 1,800-2,800 H100-hours (~$4,500-$7,000)，中等偏大规模。主要消耗在adaptive attacks (PGD on 13-17B active params) 和 multi-judge protocol全流程评估。需要稳定的GPU集群访问。
  - 数据需求: SummEval、LiveCodeBench、GPQA Diamond均为现有公开benchmark，无需自建数据集。Copula calibration需500+ samples per benchmark，量级合理。
  - 人工介入: 低。主要在pilot study的go/no-go决策和adaptive attack设计中需要人工判断。Proposal设计了清晰的decision criteria，减少了主观性。
  - 训练需求: **不需要模型训练**。所有judge模型使用off-the-shelf open-weight models (DeepSeek-V4-Flash, Qwen-3.5, Llama-4-Maverick)。计算主要在inference和adaptive attack optimization上。
  - 新 Benchmark: 不需要。使用3个现有benchmark + 现有attack库(RobustJudge 15 attacks)。
  - 预估周期: 18-24周（manual模式），14-18周（human-in-loop），9-13周（auto-research）。考虑到理论证明的时间需求和实验的规模，18-24周是合理但偏紧的。Pilot study (Weeks 1-2) 的go/no-go设计有效控制了sunk cost风险。
```

Sources:
- [SoK: Security in LLM-as-a-Judge](https://arxiv.org/abs/2603.29403)
- [Let's Measure Information Step-by-Step (Robertson & Koyejo)](https://arxiv.org/abs/2508.05469)
- [Bits Leaked per Query (Kaneko & Baldwin)](https://arxiv.org/abs/2510.17000)
- [Understanding Agent Scaling via Diversity (Yang et al.)](https://arxiv.org/abs/2602.03794)
- [Don't Always Pick the Highest-Performing Model (Turkmen et al.)](https://arxiv.org/abs/2602.08003)
- [Correlated Errors in LLMs (Kim et al.)](https://arxiv.org/abs/2506.07962)
- [Incentivizing Truthful LLMs via PEG (Chen et al.)](https://arxiv.org/abs/2505.13636)
- [Boosting Randomized Smoothing with Variance Reduced Classifiers (Horvath et al.)](https://arxiv.org/abs/2106.06946)
- [On the Certified Robustness for Ensemble Models (Chen et al.)](https://arxiv.org/abs/2107.10873)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "430e325c-4e28-4eee-8703-fe57405ced86",
  "isSidechain": false,
  "requestId": "req_011CbDJJZni7faGwcnkaHPk5",
  "type": "assistant",
  "uuid": "f990d6e5-4ea2-4a3f-8550-d4d930fa128a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTWfsHEPEbvUoPf33aEDfT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1602,
      "cache_read_input_tokens": 29979,
      "output_tokens": 6082,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1602,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6082,
          "cache_read_input_tokens": 29979,
          "cache_creation_input_tokens": 1602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1602
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Corr…",
  "leafUuid": "f990d6e5-4ea2-4a3f-8550-d4d930fa128a",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-judge LLM evaluation certifiable robustness bounds",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Corr…",
  "leafUuid": "f990d6e5-4ea2-4a3f-8550-d4d930fa128a",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-judge LLM evaluation certifiable robustness bounds",
  "sessionId": "bf282443-299e-4737-b983-aec70555c4b7"
}
```

---
