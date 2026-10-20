# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Certifiable Manipulation Resistan

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/99f8a341-e187-4e1a-bf75-1dd45e1a7c6e.jsonl`
- **Structured JSON:** [`1428ee091a96afd2ffe3.json`](../../sessions/14/1428ee091a96afd2ffe3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:46:52.941Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:46:52.941Z",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation Structure\n\n## Description\n\nLLM evaluation faces systematic adversarial vulnerabilities—open-source judge models show 50–68% average attack success rates (SoK, April 2026, arXiv 2603.29403), and arena rankings can be flipped with ~1,000 strategic votes (ICML 2025). While Robertson & Koyejo (2025, arXiv 2508.05469) proved bounded f-divergence certification for single evaluators, concurrent works established peer prediction incentive-compatibility (Qiu et al., ICLR 2026; Chen et al., NeurIPS 2025), and Kaneko & Baldwin (NeurIPS 2025 spotlight, arXiv 2510.17000) proved tight single-model attack cost bounds (N_min ≥ log₂(1/ε)/I_max), no work provides formal N-judge manipulation-cost scaling as a function of measurable inter-judge correlation.\n\nWe establish the **adversarial dual of diversity scaling** and reveal a fundamental asymmetry. Yang et al. (ICLR 2026 Workshop AIMS, arXiv 2602.03794) proved task performance improves exponentially—residual uncertainty decays as (1-α_c)^{K*} via effective channel count K* = 2^{H(ρ)}. We prove the complementary result: adversarial manipulation cost grows only **polynomially** as Ω(K_eff^{1/2}). The structural reason for this asymmetry: stochastic evaluation errors are **incoherent** across judges and concentrate exponentially via standard inequalities, but adversarial perturbations are **coherent**—the adversary's shared perturbation reintroduces cross-judge coupling, limiting gains to polynomial variance reduction. This asymmetry implies diversity is fundamentally more cost-effective for accuracy than for robustness—a non-obvious result with direct resource-allocation implications.\n\nAs a co-primary contribution, we characterize how PEG's (Chen et al., NeurIPS 2025, arXiv 2505.13636) dominant-strategy truthfulness, requiring conditional independence (Assumption 4), degrades under partial correlation: ε-approximate equilibrium with ε = f(ρ) provides a continuous degradation curve from dominant-strategy (ρ=0) to approximate (ρ→1) regimes. No existing work provides this analysis.\n\nOur proof proceeds in two steps: (1) SDPI per-channel bounds (Polyanskiy & Wu, arXiv 1508.06025) constrain each judge's information leakage to at most I_max per query; across K parallel judges, total adversary information gain is bounded additively by K_eff · I_max. (2) Variance-reduction arguments (Horvath et al., arXiv 2106.06946) yield perturbation energy scaling as Ω(K_eff^{1/2}), giving g(I_max) = ½·log(K_eff)/log(K). The ½ exponent is derived from continuous-space (ℓ₂) variance reduction; for discrete text perturbations, we state it as a conjecture supported by the continuous analogue and test it empirically via adaptive attacks.\n\nUnder Turkmen et al.'s (arXiv 2602.08003) equicorrelated Gaussian copula: K_eff = 1+(K-1)·exp(-2·I_max). For heterogeneous correlation, K* = 2^{H(ρ)} (Yang et al.) serves as an upper-bound approximation of effective dimensionality in the adversarial context; its validity is tested via copula goodness-of-fit and empirical tightness experiments.\n\nA provocative implication: as frontier model capability increases, Kim et al. (ICML 2025, arXiv 2506.07962) show error correlations increase even across providers/architectures. Under our framework, this drives K_eff → 1 regardless of ensemble size, suggesting **certified manipulation-resistance may be fundamentally bounded at the frontier**—a \"diversity ceiling\" where adding more capable judges yields diminishing certified robustness returns even as accuracy continues to improve.\n\nThe framework also serves as a **prescriptive judge-selection tool**: K_eff maximization for certified robustness vs. Turkmen et al.'s MI maximization for accuracy—these may yield different optimal ensembles. We validate against 15 off-the-shelf attacks plus three protocol-aware adaptive attacks on SummEval, LiveCodeBench, and GPQA Diamond, with compute-normalized (FLOP-matched) baselines and copula model validation.\n\n## Core Problem\nCan we provide certifiable manipulation-resistance guarantees for N-judge LLM evaluation protocols, where the certified robustness bound is an explicit, computable function of measurable inter-judge signal correlation, validated against both off-the-shelf and protocol-aware adaptive adversarial attacks?\n\n## Opportunity\nThree critical gaps: (1) No formal N-agent scaling connecting manipulation cost to measurable inter-judge signal correlation. Robertson & Koyejo (arXiv 2508.05469) analyze pairwise evaluations; Chen et al.'s PEG (NeurIPS 2025, arXiv 2505.13636) requires conditional independence (Assumption 4) without characterizing degradation. (2) Empirical validation lacks adaptive attacks targeting multi-judge protocols (Carlini et al., arXiv 1902.06705 standard). (3) Yang et al.'s diversity-scaling (arXiv 2602.03794) addresses performance only—no adversarial dual exists, and the exponential-polynomial asymmetry is unknown.\n\nTurkmen et al. (arXiv 2602.08003): correlated ensemble error floor Φ(Φ⁻¹(1-p)/√ρ), MI decomposition for α estimation. Kaneko & Baldwin (NeurIPS 2025, arXiv 2510.17000): tight single-model bounds, no multi-judge composition. SoK (arXiv 2603.29403): 7-model committees reduce ASR to 10–19% without formal explanation. Qiu et al. (ICLR 2026, arXiv 2601.20299): BNE guarantees for truthfulness, not adversarial robustness.\n\n## Landscape\n**Single-evaluator foundations.** Robertson & Koyejo (arXiv 2508.05469, TMLR under review): TVD-MI, polynomial certification (Theorem 3.3), AUC 0.70–0.77. Identity-Link IRT follow-up (arXiv 2510.14966): sparse evaluation, two-judge validation (ρ=0.872).\n\n**Peer prediction.** Qiu et al. (ICLR 2026, arXiv 2601.20299): BNE guarantees, output truthfulness. Chen et al. PEG (NeurIPS 2025, arXiv 2505.13636): dominant strategy (Lemma 1), O(√T) regret (Theorem 2), Nash convergence (Theorem 3), conditional independence (Assumption 4)—degradation under violation uncharacterized.\n\n**Diversity scaling.** Yang et al. (ICLR 2026 Workshop AIMS, arXiv 2602.03794): K* = 2^{H(ρ)}, (1-α_c)^{K*} decay (Theorem 4.3), heterogeneity advantage (Corollary 4.4). Performance only.\n\n**Correlation models.** Turkmen et al. (arXiv 2602.08003): Gaussian copula, error floor (Theorem 4.4), MI decomposition (Theorem 4.3), within-family ρ~0.7-0.8, cross-family ρ~0.4-0.5. Kim et al. (ICML 2025, arXiv 2506.07962): 60% error agreement, +0.066 same-company, +0.076 same-architecture; larger/more accurate models more correlated even across providers. Chen et al. behavioral entanglement (arXiv 2604.07650): BEI/CIG, cross-family 40–60% lower.\n\n**Single-model adversarial bounds.** Kaneko & Baldwin (NeurIPS 2025 spotlight, arXiv 2510.17000): N_min ≥ log₂(1/ε)/I_max (Theorem 1), SPRT achievability (Theorem 2), four disclosure regimes.\n\n**Certifiable evaluation under noise.** Shen et al. (arXiv 2604.03257): constrained MLE, honest judges. Feng et al. (ICLR 2026, arXiv 2601.20913): hypothesis testing, Type-I error control (Theorem 5.1), variance-corrected thresholds (Theorem 5.4). Both assume non-adversarial judges.\n\n**Semantic/representational collapse.** Kong et al. (arXiv 2605.17193, May 2026): closed-loop multi-LLM systems exhibit semantic collapse across 200–1000 rounds; 12 interventions fail. Patel (arXiv 2604.03809): effective rank 2.17/3.0 for homogeneous committees. Both apply to **iterative closed-loop** settings. Our single-pass evaluation protocol (independent scoring, no inter-judge communication) avoids the feedback loops driving collapse; K_eff serves as a principled detector if diversity erosion occurs.\n\n**Scaling dissociation.** Jung & Na (arXiv 2604.00477): scoring reliability logarithmic, discovery N^0.69 power law.\n\n**Attack/defense landscape.** SoK (arXiv 2603.29403): 50–68% ASR open-source, 27–44% frontier, 7-model → 10–19%. RobustJudge (arXiv 2506.09443): 15 attacks, 7 defenses. CAP (OpenReview 2026): comparative assessment, no formal guarantees. Carlini et al. (arXiv 1902.06705): adaptive attack gold standard.\n\n**Coordination failure.** Frongillo et al. (arXiv 2503.16280): fine-grained signals destabilize uninformative equilibria. Keppo et al. (arXiv 2603.20281): 2→5 LLMs breaks collusion (+22%→+3%).\n\n**Multi-agent evaluation.** CollabEval (arXiv 2603.00993): three-phase, no adversarial guarantees. Ebrahimi et al. (IJCNLP-AACL 2025, arXiv 2505.24239): credibility-based aggregation.\n\n**Certified ensemble robustness.** Chen et al. (arXiv 2107.10873): diversified gradient + confidence margin necessary/sufficient. Horvath et al. (arXiv 2106.06946): √K certified radius via variance reduction. Both in continuous perturbation spaces.\n\nTHE KEY GAP: No formal N-agent manipulation-cost scaling as a function of measurable correlation; no characterization of the exponential-polynomial asymmetry between performance and robustness scaling; no PEG degradation analysis under correlation violation.\n\n## Approach\n\nFive components:\n\n**Component 1: Theoretical Framework—The Asymmetric Adversarial Dual.**\n\nWe prove manipulation cost grows as Ω(K_eff^{1/2}), establishing an asymmetric duality with Yang et al.'s exponential performance scaling. The structural origin: stochastic errors are incoherent across judges (exponential concentration), but adversarial perturbations are coherent (shared perturbation reintroduces coupling → polynomial variance reduction only). This implies a fundamental resource-allocation insight: the marginal robustness value of each additional judge diminishes faster than its marginal accuracy value.\n\n*Step 1—Per-Channel SDPI Bound.* Each judge is a noisy channel; SDPI (Polyanskiy & Wu, arXiv 1508.06025) bounds per-channel information leakage to I_max. K parallel judges yield additive total: K_eff · I_max per round. Extends Kaneko & Baldwin's single-channel N_min.\n\n*Step 2—Variance Reduction to Manipulation Cost.* Fano-ensemble decomposition (Morishita et al., ICML 2022, arXiv 2205.12683) into relevance, redundancy, combination loss. Marton's inequality (TV² ≤ ½·KL) + Robertson & Koyejo's Theorem 3.3 → perturbation energy Ω(K_eff^{1/2}). Exponent: g(I_max) = ½·log(K_eff)/log(K). Boundaries: g(0) = ½ (independent), g → 0 (fully correlated).\n\n*Copula Closed Form.* Turkmen et al.'s equicorrelated model: K_eff = 1+(K-1)·exp(-2·I_max), I_max = -½ log(1-ρ²). Eigenvalues λ₁ = 1+(K-1)ρ, λ₂ = 1-ρ.\n\n*Heterogeneous Extension.* K* = 2^{H(ρ)} (Yang et al.) as upper-bound approximation of adversarial effective dimensionality, yielding g ≥ ½·log(K*)/log(K). K*'s validity in the adversarial context (vs. its original performance context) is an approximation justified by the shared eigenstructure and validated empirically via tightness experiments.\n\n*Exponent Status.* The ½ exponent derives from continuous-space (ℓ₂) variance reduction (Horvath et al., arXiv 2106.06946). For discrete text perturbations, the perturbation geometry differs; we state ½ as a conjecture for the discrete evaluation setting, supported by the continuous analogue, and test it empirically. Whether the true discrete exponent is better or worse than ½ is an open question.\n\n*Frontier Diversity Ceiling.* Kim et al. (ICML 2025) show error correlations increase with model capability even across providers/architectures. Under our framework, this drives K_eff → 1 as ρ → 1, implying certified manipulation-resistance may face a fundamental ceiling at the frontier: adding more capable judges yields diminishing certified robustness returns even as accuracy improves. We examine this empirically and discuss its implications.\n\n**Component 2: PEG Guarantee Degradation + α Regime Analysis.**\n\n*Co-primary contribution.* PEG's dominant-strategy truthfulness (Lemma 1, Assumption 4 conditional independence; Chen et al., NeurIPS 2025, arXiv 2505.13636) degrades under correlation: ε-approximate equilibrium with ε = f(ρ). This degradation pattern may extend to other conditional-independence-assuming mechanisms in peer prediction, though we prove it specifically for PEG.\n\nα estimates using external priors (Turkmen et al. ρ~0.4-0.5; Kim et al. +0.066/+0.076) **validated via direct measurement** in pilot study. Note: Kim et al.'s agreement rate and copula ρ are different quantities; we derive the mapping explicitly.\n- Central: ρ ≈ 0.45, α ∈ [0.35, 0.65], K=7: 2.65–3.7×\n- Sensitivity: α=0.2 → 1.55×; α=0.8 → 5.2×; vacuous at α ≤ 0.05 (ρ ≥ 0.95)\n- Score-coverage dissociation (Jung & Na, arXiv 2604.00477): analyze certified bound saturation rate\n\n**Component 3: Practical Protocol Design.**\n\nThree families: DeepSeek-V4-Flash (284B MoE, 13B active), Qwen-3.5 (397B MoE, 17B active), Llama-4-Maverick (400B MoE, 17B active). Backups: Gemma-2-27B (dense, non-MoE), Mistral-Large-2, Command-R+.\n\nThree phases: (1) Independence measurement (calibration ≥500 samples for copula GoF; sensitivity at {100, 200, 500, 1000, 2000}); (2) TVD-MI evaluation + DMI-weighted aggregation (PEG, Chen et al., NeurIPS 2025); (3) Certification: Ω(K^α) bound with measured α.\n\nPrescriptive judge selection: K_eff maximization (robustness) vs. MI maximization (accuracy, Turkmen et al.) may yield different optimal ensembles.\n\n**Component 4: Certifiable Robustness Framing.**\n\nA defense showing 15% empirical ASR under today's 15 known attacks provides no guarantee against tomorrow's attacks—an adaptive adversary could spike ASR back to 60% with a novel strategy. Our framework guarantees Ω(K^α) manipulation cost regardless of attack strategy. Same value proposition as randomized smoothing: modest certified margins, but provable guarantees. Kaneko & Baldwin's per-judge N_min × K_eff gives multi-judge certified resistance.\n\n**Component 5: Adversarial Validation, PEG Degradation Testing, and Model Assumption Validation.**\n\n*Benchmarks.* SummEval (summarization; CAP comparison; broader quality metrics beyond factuality), LiveCodeBench (code; contamination-resistant, frontier-discriminative), GPQA Diamond (knowledge-intensive QA; discriminative for open-weight judges).\n\n*Threat models.* Black-box (aggregated output only), gray-box (judge identities known, individual outputs hidden), white-box (all outputs + DMI weights visible).\n\n*Off-the-shelf attacks.* RobustJudge's 15 methods + SoK vectors.\n\n*Adaptive attacks (Carlini et al., arXiv 1902.06705):*\n(a) Correlation-exploiting (gray/white): optimize perturbation to simultaneously fool high-ρ pairs; transfer-based optimization on proxy models if full MoE gradient infeasible.\n(b) Aggregation-targeting (white): optimize to shift aggregated score beyond certified bound.\n(c) Weakest-link (gray): concentrate on highest-I_max channel.\n(d) Best-effort tightness (white): PGD on MoE active parameters (13-17B, feasible per-forward-pass); fallback to PAIR + random-search hybrid. Budget: 10,000 queries. Convergence: <0.5% ASR improvement over last 2,000 queries. Report ASR-vs-budget curve with convergence annotation.\n\n*Compute-normalized baselines (FLOP-matched):*\n(a) Frontier single-model (GPT-4o-latest or Claude Sonnet).\n(b) Self-consistency: DeepSeek-V4-Flash × 7 (different temperatures/prompts), majority voting. Reports per-query FLOPs and wall-clock time.\n\n*Other baselines.* 7 RobustJudge defenses; CAP; CollabEval (arXiv 2603.00993); Ebrahimi et al. (IJCNLP-AACL 2025, arXiv 2505.24239); Robertson & Koyejo single-evaluator TVD-MI; majority voting K=3,5,7; PEG with DMI scoring.\n\n*PEG degradation validation.* Dedicated experiment: construct 5-7 judge panels spanning ρ from within-family (~0.7-0.8) to all-cross-family (~0.4-0.5) via mixed composition. For each panel, measure ρ_ij directly. Introduce a strategic deviator judge (via prompt injection) and measure its expected payoff gain vs. truthful baseline—payoff gain > 0 provides empirical ε lower bound. Report (measured_ρ, empirical_ε) scatter against theoretical f(ρ) curve. Track DMI regret across panels.\n\n*Dual-scaling validation.* In K-scaling ablation (K=1,2,3,5,7), simultaneously measure: (a) non-adversarial accuracy (Spearman/Kendall with ground truth), fitting (1-α_c)^{K*} model (report R²); (b) adversarial manipulation cost (empirical query count + certified bound), fitting K^α model (report R²). Overlay both curves (log-scale y-axis) to visualize exponential-polynomial asymmetry.\n\n*Model assumption validation.*\n(a) Full K×K ρ_ij matrix; Var(ρ_ij) for equicorrelation deviation.\n(b) Copula GoF (Anderson-Darling, minimum n=500; 50-100 for ρ stability only).\n(c) If GoF rejects: Kendall's tau rank correlation for dependence estimation; K* from rank-correlation matrix. Report Pearson-based vs. Kendall-based K* gap.\n(d) Heterogeneous bound (K*) vs. closed-form bound gap.\n\n*Ablations.*\n(a) K-scaling: K=1,2,3,5,7 (with dual-scaling overlay).\n(b) Diversity-type 2×2: {same-org, diff-org} × {same-arch-type, diff-arch-type}, ≥1 non-MoE model (Gemma-2-27B).\n(c) Accuracy-robustness tradeoff: MI-maximization vs. K_eff-maximization ensemble selection; Pareto frontier.\n(d) α sensitivity: [0.2, 0.8].\n(e) Calibration sensitivity: ρ at {100, 200, 500, 1000, 2000}; cross-domain calibration transfer (3×3 benchmark matrix: use ρ from benchmark A to compute bound for B, report transferred vs. in-domain bound deviation and ρ cross-domain stability); bootstrap error propagation to CI.\n\n*Statistical rigor.* ≥3 seeds (mean ± std). ρ: bootstrap 95% CI. Primary correction: Benjamini-Hochberg FDR. Conservative check on core claims: Bonferroni. Report uncorrected, BH-adjusted, and Bonferroni-adjusted values.\n\n*Pilot study (Weeks 1-2, ~100 H100-hrs).* ρ_ij on 500 samples per benchmark. Go/no-go: ρ > 0.7 → switch to backups. If all open-weight models show ρ > 0.7, report as empirical finding supporting the frontier diversity ceiling.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '1,800-2,800 H100-equivalent', 'timeline': '18-24 weeks', 'estimated_gpu_cost': '$4,500-$7,000 at $2.50/hr', 'gpu_breakdown': 'Pilot ~100; single-judge baselines ~450; multi-judge protocol ~500; adaptive attacks (transfer/PAIR + tightness PGD) ~500; compute-normalized baselines ~50 + ~$300 API; copula/calibration/cross-domain ~100; PEG degradation validation ~80; diversity + accuracy-robustness ablation ~200; K-scaling + dual-scaling ~200; multi-seed ~300; dev/debug ~150'}, 'human_in_loop': {'gpu_hours': '1,400-2,200', 'timeline': '14-18 weeks', 'claude_api_cost': '$400-$600'}, 'auto_research': {'gpu_hours': '2,100-3,000', 'timeline': '9-13 weeks', 'claude_api_cost': '$1,200-$2,000'}}\n\n## Inspired By\nSeven lines: (1) Robertson & Koyejo bounded f-divergence (arXiv 2508.05469); (2) Qiu et al. BNE (ICLR 2026, arXiv 2601.20299) + Chen et al. PEG (NeurIPS 2025, arXiv 2505.13636); (3) Yang et al. K* diversity-scaling (ICLR 2026 Workshop AIMS, arXiv 2602.03794); (4) Turkmen et al. copula model (arXiv 2602.08003); (5) Kaneko & Baldwin single-model bounds (NeurIPS 2025 spotlight, arXiv 2510.17000); (6) SoK 7-model ASR reduction (arXiv 2603.29403); (7) Error correlation/entanglement (Chen et al. arXiv 2604.07650; Kim et al. ICML 2025, arXiv 2506.07962).\n\n## Target Venues\n- ICLR 2027 (estimated: October 2026; primary—full theory + comprehensive experiments)\n- AAAI 2027 (abstract: July 21, 2026; stretch goal)\n- USENIX Security 2027 Cycle 1 (August 2026; security-focused)\n- NeurIPS 2026 Workshops (~August 29, 2026)\n\n## Key References\n- Let's Measure Information Step-by-Step (Robertson & Koyejo, arXiv 2508.05469, 2025)\n- Identity-Link IRT (Robertson, arXiv 2510.14966, 2025)\n- Truthfulness Despite Weak Supervision (Qiu et al., ICLR 2026, arXiv 2601.20299)\n- PEG (Chen et al., NeurIPS 2025, arXiv 2505.13636)\n- Understanding Agent Scaling via Diversity (Yang et al., ICLR 2026 Workshop AIMS, arXiv 2602.03794)\n- Don't Always Pick the Highest-Performing Model (Turkmen et al., arXiv 2602.08003, 2026)\n- Bits Leaked per Query (Kaneko & Baldwin, NeurIPS 2025 spotlight, arXiv 2510.17000)\n- Robust LLM Performance Certification (Shen et al., arXiv 2604.03257, 2026)\n- Noisy but Valid (Feng et al., ICLR 2026, arXiv 2601.20913)\n- Logarithmic Scores, Power-Law Discoveries (Jung & Na, arXiv 2604.00477, 2026)\n- SoK: Security in LLM-as-a-Judge (arXiv 2603.29403, April 2026)\n- RobustJudge (arXiv 2506.09443, 2025)\n- Correlated Errors in LLMs (Kim et al., ICML 2025, arXiv 2506.07962)\n- Behavioral Entanglement (Chen et al., arXiv 2604.07650, 2026)\n- Benchmark Illusion (arXiv 2602.11898, 2026)\n- Strong Data-Processing Inequalities (Polyanskiy & Wu, arXiv 1508.06025, 2017)\n- Rethinking Fano's Inequality in Ensemble Learning (Morishita et al., ICML 2022, arXiv 2205.12683)\n- Certified Robustness for Ensemble Models (Chen et al., arXiv 2107.10873, 2021)\n- Boosting Randomized Smoothing with Variance Reduced Classifiers (Horvath et al., arXiv 2106.06946, 2021)\n- Information-Theoretically Optimal Adversarial Attacks (Yi et al., arXiv 2007.14042, 2020)\n- On the Fragility of AI Agent Collusion (Keppo et al., arXiv 2603.20281, 2026)\n- CollabEval (arXiv 2603.00993, March 2026)\n- Adversary-Resistant Multi-Agent via Credibility Scoring (Ebrahimi et al., IJCNLP-AACL 2025, arXiv 2505.24239)\n- Certifying Joint Adversarial Robustness for Ensembles (Chiang et al., arXiv 2004.10250, 2020)\n- Peer Prediction with More Signals than Reports (Frongillo et al., arXiv 2503.16280, 2025)\n- Adversarial Manipulation of Voting-Based Leaderboards (ICML 2025)\n- Vote Rigging on Chatbot Arena (ICML 2025)\n- am-ELO: Stable Arena-based Evaluation (ICML 2025 Poster)\n- CAP: Comparative Augmented Prompting (OpenReview 2026)\n- Aligned Textual Scoring Rules (Lu et al., arXiv 2507.06221, 2025)\n- Can You Trick the Grader? (EMNLP 2025 Findings)\n- On Evaluating Adversarial Robustness (Carlini et al., arXiv 1902.06705, 2019)\n- Multi-LLM Systems Exhibit Robust Semantic Collapse (Kong et al., arXiv 2605.17193, May 2026)\n- Representational Collapse in Multi-Agent LLM Committees (Patel, arXiv 2604.03809, April 2026)\n- LiveCodeBench (arXiv 2403.07974, 2024)"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T05:46:52.946Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:46:52.946Z",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e"
}
```

---

## Round 1

47 recorded events

### User

_source line 3 · 2026-05-20T05:46:53.017Z_

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
  "promptId": "2758bb61-6675-4f99-8284-20dd6e249133",
  "type": "user",
  "uuid": "8a2e57f1-dec1-421f-9717-2ffcbeb1d73d",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:46:53.015Z_

```json
{
  "parentUuid": "8a2e57f1-dec1-421f-9717-2ffcbeb1d73d",
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
  "uuid": "d85f1273-8894-40d3-96ce-5b32c507485b",
  "timestamp": "2026-05-20T05:46:53.015Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:46:53.015Z_

```json
{
  "parentUuid": "d85f1273-8894-40d3-96ce-5b32c507485b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "95b69454-1940-42eb-8550-5980666a5b26",
  "timestamp": "2026-05-20T05:46:53.015Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
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
  "leafUuid": "95b69454-1940-42eb-8550-5980666a5b26",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-judge LLM evaluation manipulation resistance bounds",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:46:57.140Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal carefully. It's about certifiable manipulation resistance for multi-judge LLM evaluation, using information-theoretic bounds. Before I can give a fair assessment, I need to do thorough research on the current state of this field.

Let me start by searching for the key papers and concepts mentioned in this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95b69454-1940-42eb-8550-5980666a5b26",
  "isSidechain": false,
  "requestId": "req_011CbDHwejnFBDKvPmUk6AMs",
  "type": "assistant",
  "uuid": "59949410-114c-4449-8bc9-ebf5ab60bd9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Crhhv7BZrvibXPXLA8JEHD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11247,
      "cache_read_input_tokens": 11374,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11247,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 189,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 11247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11247
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

_source line 9 · 2026-05-20T05:46:58.244Z_

I need to conduct thorough research before evaluating this proposal. Let me search for the key papers and current state of the field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59949410-114c-4449-8bc9-ebf5ab60bd9b",
  "isSidechain": false,
  "requestId": "req_011CbDHwejnFBDKvPmUk6AMs",
  "type": "assistant",
  "uuid": "d71c215f-f37c-4d52-b9ff-0c2c74893791",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Crhhv7BZrvibXPXLA8JEHD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11247,
      "cache_read_input_tokens": 11374,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11247,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 189,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 11247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11247
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

_source line 10 · 2026-05-20T05:46:58.598Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015qTp5G2SvDXskxKUDoR1eN`</summary>

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
  "parentUuid": "d71c215f-f37c-4d52-b9ff-0c2c74893791",
  "isSidechain": false,
  "requestId": "req_011CbDHwejnFBDKvPmUk6AMs",
  "type": "assistant",
  "uuid": "13d41f0e-171b-4024-ae36-93ccc3c61c97",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Crhhv7BZrvibXPXLA8JEHD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11247,
      "cache_read_input_tokens": 11374,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11247,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 189,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 11247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11247
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

_source line 11 · 2026-05-20T05:46:58.605Z_

<details><summary>↩ Tool result · `toolu_015qTp5G2SvDXskxKUDoR1eN`</summary>

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
  "parentUuid": "13d41f0e-171b-4024-ae36-93ccc3c61c97",
  "isSidechain": false,
  "promptId": "2758bb61-6675-4f99-8284-20dd6e249133",
  "type": "user",
  "uuid": "9e4c33f2-e45d-4158-97e5-a2200341e42b",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "13d41f0e-171b-4024-ae36-93ccc3c61c97",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T05:47:01.865Z_

Now let me conduct the required research searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e4c33f2-e45d-4158-97e5-a2200341e42b",
  "isSidechain": false,
  "requestId": "req_011CbDHx4n98A2CywfU5w1q9",
  "type": "assistant",
  "uuid": "1a981eee-44e6-4389-aa53-21d611d9e4d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfnyMJbKouFrL6vKXNMAb9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 22621,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 307,
          "cache_read_input_tokens": 22621,
          "cache_creation_input_tokens": 717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 717
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

_source line 13 · 2026-05-20T05:47:02.401Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TVJ41u9aC3CQPmyHoEBFUY`</summary>

```json
{
  "query": "LLM-as-a-judge adversarial robustness multi-judge certification 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a981eee-44e6-4389-aa53-21d611d9e4d5",
  "isSidechain": false,
  "requestId": "req_011CbDHx4n98A2CywfU5w1q9",
  "type": "assistant",
  "uuid": "feebf688-0e1f-4f38-adb6-cf1ac862b544",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfnyMJbKouFrL6vKXNMAb9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 22621,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 307,
          "cache_read_input_tokens": 22621,
          "cache_creation_input_tokens": 717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 717
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

_source line 14 · 2026-05-20T05:47:02.881Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MktupXGcvZdieoLuNwKCnz`</summary>

```json
{
  "query": "information-theoretic bounds manipulation resistance ensemble LLM evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "feebf688-0e1f-4f38-adb6-cf1ac862b544",
  "isSidechain": false,
  "requestId": "req_011CbDHx4n98A2CywfU5w1q9",
  "type": "assistant",
  "uuid": "2bae7317-01f8-4cfc-9bbd-78126a1fb5c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfnyMJbKouFrL6vKXNMAb9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 22621,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 307,
          "cache_read_input_tokens": 22621,
          "cache_creation_input_tokens": 717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 717
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

_source line 15 · 2026-05-20T05:47:03.812Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PJymUoKZG4iK4ZYEsKrVzE`</summary>

```json
{
  "query": "Robertson Koyejo bounded f-divergence LLM evaluator certification arXiv 2508.05469"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bae7317-01f8-4cfc-9bbd-78126a1fb5c7",
  "isSidechain": false,
  "requestId": "req_011CbDHx4n98A2CywfU5w1q9",
  "type": "assistant",
  "uuid": "14838ca5-ccb1-4f43-b7f7-94b804dded58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfnyMJbKouFrL6vKXNMAb9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 22621,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 307,
          "cache_read_input_tokens": 22621,
          "cache_creation_input_tokens": 717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 717
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

_source line 16 · 2026-05-20T05:47:05.223Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Howb4qRPfiybti2qG3Apqd`</summary>

```json
{
  "query": "Kaneko Baldwin bits leaked per query NeurIPS 2025 arXiv 2510.17000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14838ca5-ccb1-4f43-b7f7-94b804dded58",
  "isSidechain": false,
  "requestId": "req_011CbDHx4n98A2CywfU5w1q9",
  "type": "assistant",
  "uuid": "1c7d477d-c8b0-42f0-93e4-16f02a9db846",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfnyMJbKouFrL6vKXNMAb9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 22621,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 307,
          "cache_read_input_tokens": 22621,
          "cache_creation_input_tokens": 717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 717
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

_source line 17 · 2026-05-20T05:47:05.795Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EdivgyjCEZBwgLiRkqT2CG`</summary>

```json
{
  "query": "Yang et al diversity scaling multi-agent effective channel count arXiv 2602.03794"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c7d477d-c8b0-42f0-93e4-16f02a9db846",
  "isSidechain": false,
  "requestId": "req_011CbDHx4n98A2CywfU5w1q9",
  "type": "assistant",
  "uuid": "f60868ac-b29e-4a19-914f-7f17c4530a10",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfnyMJbKouFrL6vKXNMAb9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 22621,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 307,
          "cache_read_input_tokens": 22621,
          "cache_creation_input_tokens": 717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 717
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

_source line 18 · 2026-05-20T05:47:10.459Z_

<details><summary>↩ Tool result · `toolu_01PJymUoKZG4iK4ZYEsKrVzE`</summary>

```text
Web search results for query: "Robertson Koyejo bounded f-divergence LLM evaluator certification arXiv 2508.05469"

Links: [{"title":"[2508.05469] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/abs/2508.05469"},{"title":"Identity-Link IRT for Label-Free LLM Evaluation:","url":"https://arxiv.org/pdf/2510.14966"},{"title":"[PDF] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Let's-Measure-Information-Step-by-Step:-LLM-Based-Robertson-Koyejo/824098ede34f59514ebc25a69c69c68d1e89b664"},{"title":"Let’s Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/html/2508.05469"},{"title":"Computer Science Aug 2025","url":"https://www.arxiv.org/list/cs/2025-08?skip=2725&show=2000"},{"title":"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/pdf/2508.05469"},{"title":"Large Language Models are Inconsistent and Biased Evaluators","url":"https://arxiv.org/pdf/2405.01724"},{"title":"Beyond Single-Point Judgment: Distribution Alignment for LLM-as-a-Judge","url":"https://arxiv.org/pdf/2505.12301"}]

Based on the search results, I found the paper you're looking for:

The paper is titled "Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes" by Zachary Robertson and Sanmi Koyejo, with the arXiv identifier 2508.05469.

The paper studies evaluation of AI systems without ground truth by exploiting a link between strategic gaming and information loss. The authors analyze which information-theoretic mechanisms resist adversarial manipulation, extending finite-sample bounds to show that bounded f-divergences (e.g., total variation distance) maintain polynomial guarantees under attacks while unbounded measures (e.g., KL divergence) degrade exponentially. To implement these mechanisms, they model the overseer as an agent and characterize incentive-compatible scoring rules as f-mutual information objectives.

Under adversarial attacks, TVD-MI (Total Variation Distance Mutual Information) maintains effectiveness (area under curve 0.70-0.77) while traditional judge queries are near chance (AUC ≈ 0.50).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14838ca5-ccb1-4f43-b7f7-94b804dded58",
  "isSidechain": false,
  "promptId": "2758bb61-6675-4f99-8284-20dd6e249133",
  "type": "user",
  "uuid": "e5056eb2-45d3-4402-a3ca-ab1f37246354",
  "toolUseResult": {
    "query": "Robertson Koyejo bounded f-divergence LLM evaluator certification arXiv 2508.05469",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QxjcgadsazJQsdvUVbDSTK",
        "content": [
          {
            "title": "[2508.05469] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/abs/2508.05469"
          },
          {
            "title": "Identity-Link IRT for Label-Free LLM Evaluation:",
            "url": "https://arxiv.org/pdf/2510.14966"
          },
          {
            "title": "[PDF] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Let's-Measure-Information-Step-by-Step:-LLM-Based-Robertson-Koyejo/824098ede34f59514ebc25a69c69c68d1e89b664"
          },
          {
            "title": "Let’s Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/html/2508.05469"
          },
          {
            "title": "Computer Science Aug 2025",
            "url": "https://www.arxiv.org/list/cs/2025-08?skip=2725&show=2000"
          },
          {
            "title": "Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/pdf/2508.05469"
          },
          {
            "title": "Large Language Models are Inconsistent and Biased Evaluators",
            "url": "https://arxiv.org/pdf/2405.01724"
          },
          {
            "title": "Beyond Single-Point Judgment: Distribution Alignment for LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2505.12301"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper is titled \"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes\" by Zachary Robertson and Sanmi Koyejo, with the arXiv identifier 2508.05469.\n\nThe paper studies evaluation of AI systems without ground truth by exploiting a link between strategic gaming and information loss. The authors analyze which information-theoretic mechanisms resist adversarial manipulation, extending finite-sample bounds to show that bounded f-divergences (e.g., total variation distance) maintain polynomial guarantees under attacks while unbounded measures (e.g., KL divergence) degrade exponentially. To implement these mechanisms, they model the overseer as an agent and characterize incentive-compatible scoring rules as f-mutual information objectives.\n\nUnder adversarial attacks, TVD-MI (Total Variation Distance Mutual Information) maintains effectiveness (area under curve 0.70-0.77) while traditional judge queries are near chance (AUC ≈ 0.50)."
    ],
    "durationSeconds": 6.642665363,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "14838ca5-ccb1-4f43-b7f7-94b804dded58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T05:47:12.055Z_

<details><summary>↩ Tool result · `toolu_01TVJ41u9aC3CQPmyHoEBFUY`</summary>

```text
Web search results for query: "LLM-as-a-judge adversarial robustness multi-judge certification 2025 2026"

Links: [{"title":"SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK","url":"https://arxiv.org/pdf/2603.29403"},{"title":"LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge","url":"https://arxiv.org/html/2506.09443v1"},{"title":"When AIs Judge AIs: The Rise of Agent-as-a-Judge Evaluation for LLMs","url":"https://arxiv.org/html/2508.02994v1"},{"title":"LLM-as-a-Judge Evaluation","url":"https://www.emergentmind.com/topics/llm-as-a-judge-evaluations"},{"title":"LLM-as-a-Judge Systems","url":"https://www.emergentmind.com/topics/llm-as-a-judge-systems"},{"title":"LLM-as-Judge Evaluation","url":"https://www.emergentmind.com/topics/llm-as-a-judge-evaluation"},{"title":"LLM-Judge Evaluation Techniques","url":"https://www.emergentmind.com/topics/llm-judge-evaluation"},{"title":"A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness","url":"https://arxiv.org/pdf/2603.06594"}]

Based on the search results, I found recent research on LLM-as-a-Judge adversarial robustness and multi-judge certification from 2025-2026:

## Key Findings on Adversarial Robustness

LLM-as-a-Judge systems are vulnerable to adversarial attacks, including Combined Attack and PAIR, while defense mechanisms such as Re-tokenization and LLM-based Detectors offer improved protection.

## Multi-Judge Approaches

Multi-agent setups could be more robust, since a deceptive output would have to fool not one but multiple agents. Ensemble and meta-judge architectures, combining outputs from multiple specialized judges, approach inter-annotator agreement with humans, and outperform both traditional metrics.

## RobustJudge Framework

RobustJudge is a unified framework for systematically auditing vulnerabilities, showing that re-tokenization, delimiter insertion, and instructional prevention mitigate but do not eliminate adversarial success. Prompt template optimization and model selection materially improve robustness.

## Critical Vulnerabilities

Current validation protocols fail to consider relevant distribution shifts that occur in standard adversarial attack and robustness evaluations. Additionally, robustness is highly sensitive to choice of prompt template, and minor changes in phrasing or structure can swing vulnerability metrics and attack success rates.

## Future Directions

Research emphasizes modular, explainable metrics, bias-controlled data pipelines, domain-aligned multi-agent systems, and structured human-centered workflows as best practices for the next generation of LLM-Judge evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "feebf688-0e1f-4f38-adb6-cf1ac862b544",
  "isSidechain": false,
  "promptId": "2758bb61-6675-4f99-8284-20dd6e249133",
  "type": "user",
  "uuid": "fc660797-71f8-413a-8fc0-9c3fcf7081be",
  "toolUseResult": {
    "query": "LLM-as-a-judge adversarial robustness multi-judge certification 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017mF5CEF4gtBfRgwj21yaLS",
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
            "title": "When AIs Judge AIs: The Rise of Agent-as-a-Judge Evaluation for LLMs",
            "url": "https://arxiv.org/html/2508.02994v1"
          },
          {
            "title": "LLM-as-a-Judge Evaluation",
            "url": "https://www.emergentmind.com/topics/llm-as-a-judge-evaluations"
          },
          {
            "title": "LLM-as-a-Judge Systems",
            "url": "https://www.emergentmind.com/topics/llm-as-a-judge-systems"
          },
          {
            "title": "LLM-as-Judge Evaluation",
            "url": "https://www.emergentmind.com/topics/llm-as-a-judge-evaluation"
          },
          {
            "title": "LLM-Judge Evaluation Techniques",
            "url": "https://www.emergentmind.com/topics/llm-judge-evaluation"
          },
          {
            "title": "A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness",
            "url": "https://arxiv.org/pdf/2603.06594"
          }
        ]
      },
      "Based on the search results, I found recent research on LLM-as-a-Judge adversarial robustness and multi-judge certification from 2025-2026:\n\n## Key Findings on Adversarial Robustness\n\nLLM-as-a-Judge systems are vulnerable to adversarial attacks, including Combined Attack and PAIR, while defense mechanisms such as Re-tokenization and LLM-based Detectors offer improved protection.\n\n## Multi-Judge Approaches\n\nMulti-agent setups could be more robust, since a deceptive output would have to fool not one but multiple agents. Ensemble and meta-judge architectures, combining outputs from multiple specialized judges, approach inter-annotator agreement with humans, and outperform both traditional metrics.\n\n## RobustJudge Framework\n\nRobustJudge is a unified framework for systematically auditing vulnerabilities, showing that re-tokenization, delimiter insertion, and instructional prevention mitigate but do not eliminate adversarial success. Prompt template optimization and model selection materially improve robustness.\n\n## Critical Vulnerabilities\n\nCurrent validation protocols fail to consider relevant distribution shifts that occur in standard adversarial attack and robustness evaluations. Additionally, robustness is highly sensitive to choice of prompt template, and minor changes in phrasing or structure can swing vulnerability metrics and attack success rates.\n\n## Future Directions\n\nResearch emphasizes modular, explainable metrics, bias-controlled data pipelines, domain-aligned multi-agent systems, and structured human-centered workflows as best practices for the next generation of LLM-Judge evaluation."
    ],
    "durationSeconds": 9.648441714999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "feebf688-0e1f-4f38-adb6-cf1ac862b544",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T05:47:12.221Z_

<details><summary>↩ Tool result · `toolu_01Howb4qRPfiybti2qG3Apqd`</summary>

```text
Web search results for query: "Kaneko Baldwin bits leaked per query NeurIPS 2025 arXiv 2510.17000"

Links: [{"title":"[2510.17000] Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs","url":"https://arxiv.org/abs/2510.17000"},{"title":"Machine Learning Oct 2025","url":"https://arxiv.org/list/cs.LG/2025-10?skip=4175&show=25"},{"title":"How many queries does it take to break an AI? We put a number on it. - MBZUAI","url":"https://mbzuai.ac.ae/news/how-many-queries-does-it-take-to-break-an-ai-we-put-a-number-on-it/"},{"title":"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs","url":"https://arxiv.org/html/2510.17000"},{"title":"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs","url":"https://arxiv.org/pdf/2510.17000"},{"title":"Bits Leaked per Query: Information-Theoretic Bounds for Adversarial Attacks on LLMs | OpenReview","url":"https://openreview.net/forum?id=DwXX8c7xst"},{"title":"MBZUAI on X: \"This year, our NeurIPS papers share a simple ambition: to make AI that doesn’t just predict, but understands, imagines, and communicates. We looked at how models leak information (Bits Leaked per Query), how they learn cause and effect (CausalVerse), how their abilities evolve https://t.co/GJTBnxYtEd\" / X","url":"https://x.com/mbzuai/status/1995414451705758049"}]

I found information about the paper you're searching for. Here's what I found:

"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs" by Masahiro Kaneko and Timothy Baldwin was accepted as a NeurIPS 2025 spotlight paper (arXiv 2510.17000).

The paper frames adversarial attacks against LLMs as attempts to infer target properties (such as binary flags that trigger harmful responses or information deleted by unlearning) through the model's responses.

The paper proposes measuring the bits leaked per query to predict the minimum number of queries an adversary needs. According to their framework, to drive the attack error rate down to ε, you need at least log(1/ε)/I queries, where I is the mutual information between what the model exposes and the attacker's target.

The evaluation covers seven LLMs including GPT-4, DeepSeek-R1, OLMo-2 variants, and Llama-4 checkpoints, and confirms that the query cost of attacking an LLM falls in near-perfect inverse proportion to the information it leaks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c7d477d-c8b0-42f0-93e4-16f02a9db846",
  "isSidechain": false,
  "promptId": "2758bb61-6675-4f99-8284-20dd6e249133",
  "type": "user",
  "uuid": "b8f1bc61-aaa7-42f6-bbb9-95c9f3a42deb",
  "toolUseResult": {
    "query": "Kaneko Baldwin bits leaked per query NeurIPS 2025 arXiv 2510.17000",
    "results": [
      {
        "tool_use_id": "srvtoolu_014qSXxJ57Y5d4GpbDwsFhhP",
        "content": [
          {
            "title": "[2510.17000] Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs",
            "url": "https://arxiv.org/abs/2510.17000"
          },
          {
            "title": "Machine Learning Oct 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-10?skip=4175&show=25"
          },
          {
            "title": "How many queries does it take to break an AI? We put a number on it. - MBZUAI",
            "url": "https://mbzuai.ac.ae/news/how-many-queries-does-it-take-to-break-an-ai-we-put-a-number-on-it/"
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
            "title": "MBZUAI on X: \"This year, our NeurIPS papers share a simple ambition: to make AI that doesn’t just predict, but understands, imagines, and communicates. We looked at how models leak information (Bits Leaked per Query), how they learn cause and effect (CausalVerse), how their abilities evolve https://t.co/GJTBnxYtEd\" / X",
            "url": "https://x.com/mbzuai/status/1995414451705758049"
          }
        ]
      },
      "I found information about the paper you're searching for. Here's what I found:\n\n\"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs\" by Masahiro Kaneko and Timothy Baldwin was accepted as a NeurIPS 2025 spotlight paper (arXiv 2510.17000).\n\nThe paper frames adversarial attacks against LLMs as attempts to infer target properties (such as binary flags that trigger harmful responses or information deleted by unlearning) through the model's responses.\n\nThe paper proposes measuring the bits leaked per query to predict the minimum number of queries an adversary needs. According to their framework, to drive the attack error rate down to ε, you need at least log(1/ε)/I queries, where I is the mutual information between what the model exposes and the attacker's target.\n\nThe evaluation covers seven LLMs including GPT-4, DeepSeek-R1, OLMo-2 variants, and Llama-4 checkpoints, and confirms that the query cost of attacking an LLM falls in near-perfect inverse proportion to the information it leaks."
    ],
    "durationSeconds": 6.995156053999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1c7d477d-c8b0-42f0-93e4-16f02a9db846",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T05:47:13.591Z_

<details><summary>↩ Tool result · `toolu_01EdivgyjCEZBwgLiRkqT2CG`</summary>

```text
Web search results for query: "Yang et al diversity scaling multi-agent effective channel count arXiv 2602.03794"

Links: [{"title":"[2602.03794] Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity","url":"https://arxiv.org/abs/2602.03794"},{"title":"Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity","url":"https://arxiv.org/pdf/2602.03794"},{"title":"Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity","url":"https://arxiv.org/html/2602.03794"},{"title":"[2602.03219v2] Beyond Quantity: Trajectory Diversity Scaling for Code Agents","url":"https://arxiv.org/abs/2602.03219v2"},{"title":"Dynamical Mechanisms in Multi-agent Systems: Minority Games","url":"https://arxiv.org/pdf/cond-mat/0310607"}]

I found the paper! Here are the key details about the arXiv paper 2602.03794:

**Title:** Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity

**Authors:** Yingxuan Yang, Chengrui Qu, Muning Wen, Laixi Shi, Ying Wen, Weinan Zhang, Adam Wierman, and Shangding Gu

**Publication Date:** February 3, 2026

**Main Contributions:**

The paper investigates how multi-agent LLM systems scale and demonstrates that scaling exhibits strong diminishing returns in homogeneous settings, while introducing heterogeneity (e.g., different models, prompts, or tools) continues to yield substantial gains.

**Key Framework:**

The authors present an information-theoretic framework showing that MAS performance is bounded by the intrinsic task uncertainty, not by agent count, and derive architecture-agnostic bounds demonstrating that improvements depend on how many effective channels the system accesses. 

**Effective Channel Count:**

The authors introduce K*, an effective channel count that quantifies the number of effective channels without groundtruth labels.

**Empirical Results:**

Heterogeneous configurations consistently outperform homogeneous scaling: 2 diverse agents can match or exceed the performance of 16 homogeneous agents.

The paper and code are available on arXiv and GitHub respectively.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f60868ac-b29e-4a19-914f-7f17c4530a10",
  "isSidechain": false,
  "promptId": "2758bb61-6675-4f99-8284-20dd6e249133",
  "type": "user",
  "uuid": "123bcef5-507b-4526-8ada-96f6d33fc641",
  "toolUseResult": {
    "query": "Yang et al diversity scaling multi-agent effective channel count arXiv 2602.03794",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RQNwLxBXXgF987ysST1R6C",
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
            "title": "Dynamical Mechanisms in Multi-agent Systems: Minority Games",
            "url": "https://arxiv.org/pdf/cond-mat/0310607"
          }
        ]
      },
      "I found the paper! Here are the key details about the arXiv paper 2602.03794:\n\n**Title:** Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity\n\n**Authors:** Yingxuan Yang, Chengrui Qu, Muning Wen, Laixi Shi, Ying Wen, Weinan Zhang, Adam Wierman, and Shangding Gu\n\n**Publication Date:** February 3, 2026\n\n**Main Contributions:**\n\nThe paper investigates how multi-agent LLM systems scale and demonstrates that scaling exhibits strong diminishing returns in homogeneous settings, while introducing heterogeneity (e.g., different models, prompts, or tools) continues to yield substantial gains.\n\n**Key Framework:**\n\nThe authors present an information-theoretic framework showing that MAS performance is bounded by the intrinsic task uncertainty, not by agent count, and derive architecture-agnostic bounds demonstrating that improvements depend on how many effective channels the system accesses. \n\n**Effective Channel Count:**\n\nThe authors introduce K*, an effective channel count that quantifies the number of effective channels without groundtruth labels.\n\n**Empirical Results:**\n\nHeterogeneous configurations consistently outperform homogeneous scaling: 2 diverse agents can match or exceed the performance of 16 homogeneous agents.\n\nThe paper and code are available on arXiv and GitHub respectively."
    ],
    "durationSeconds": 7.793924329999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f60868ac-b29e-4a19-914f-7f17c4530a10",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Corr…",
  "leafUuid": "123bcef5-507b-4526-8ada-96f6d33fc641",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-judge LLM evaluation manipulation resistance bounds",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e"
}
```

---

### Tool result

_source line 24 · 2026-05-20T05:47:14.457Z_

<details><summary>↩ Tool result · `toolu_01MktupXGcvZdieoLuNwKCnz`</summary>

```text
Web search results for query: "information-theoretic bounds manipulation resistance ensemble LLM evaluation"

Links: [{"title":"Let’s Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/html/2508.05469"},{"title":"(PDF) Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://www.researchgate.net/publication/394397315_Let's_Measure_Information_Step-by-Step_LLM-Based_Evaluation_Beyond_Vibes"},{"title":"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/pdf/2508.05469"},{"title":"[2508.05469] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/abs/2508.05469"},{"title":"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs","url":"https://arxiv.org/pdf/2510.17000"},{"title":"An Information-Theoretic Perspective on Multi-LLM Uncertainty Estimation","url":"https://www.medrxiv.org/content/10.1101/2025.07.09.25331207.full.pdf"}]

I found relevant research on this topic. Here are the key findings from my search:

## Main Result: Information-Theoretic Mechanisms for LLM Evaluation

Recent research studies evaluation of AI systems without ground truth by exploiting a link between strategic gaming and information loss, analyzing which information-theoretic mechanisms resist adversarial manipulation and extending finite-sample bounds to show that bounded f-divergences (e.g., total variation distance) maintain polynomial guarantees under attacks while unbounded measures (e.g., KL divergence) degrade exponentially.

## Key Theoretical Contributions

The research proves that f-mutual information measures are the unique gaming resistant mechanisms under natural conditions, with the overseer acting as an agent. The approach leverages the data processing inequality: any strategic manipulation of content necessarily reduces mutual information between responses, and by measuring these information relationships, evaluation mechanisms with formal gaming-resistance guarantees can be implemented.

## Empirical Performance

Bounded measures like total variation distance mutual information (TVD-MI) achieve the largest effect sizes (mean d = 5.2) while demonstrating 10-100× better resistance to adversarial manipulation than LLM judges. Empirically, across ten domains from translation to peer review, all information-theoretic mechanisms achieve perfect discrimination (d > 0.5) between faithful and strategic agents.

The research represents a significant shift in AI evaluation methodology by proposing measurable, theoretically-grounded alternatives to traditional quality judgments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bae7317-01f8-4cfc-9bbd-78126a1fb5c7",
  "isSidechain": false,
  "promptId": "2758bb61-6675-4f99-8284-20dd6e249133",
  "type": "user",
  "uuid": "50ed3e36-3939-4843-b379-3f1c84628d1e",
  "toolUseResult": {
    "query": "information-theoretic bounds manipulation resistance ensemble LLM evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WLHmLYuXAAgdtrriufKePH",
        "content": [
          {
            "title": "Let’s Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/html/2508.05469"
          },
          {
            "title": "(PDF) Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://www.researchgate.net/publication/394397315_Let's_Measure_Information_Step-by-Step_LLM-Based_Evaluation_Beyond_Vibes"
          },
          {
            "title": "Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/pdf/2508.05469"
          },
          {
            "title": "[2508.05469] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/abs/2508.05469"
          },
          {
            "title": "Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs",
            "url": "https://arxiv.org/pdf/2510.17000"
          },
          {
            "title": "An Information-Theoretic Perspective on Multi-LLM Uncertainty Estimation",
            "url": "https://www.medrxiv.org/content/10.1101/2025.07.09.25331207.full.pdf"
          }
        ]
      },
      "I found relevant research on this topic. Here are the key findings from my search:\n\n## Main Result: Information-Theoretic Mechanisms for LLM Evaluation\n\nRecent research studies evaluation of AI systems without ground truth by exploiting a link between strategic gaming and information loss, analyzing which information-theoretic mechanisms resist adversarial manipulation and extending finite-sample bounds to show that bounded f-divergences (e.g., total variation distance) maintain polynomial guarantees under attacks while unbounded measures (e.g., KL divergence) degrade exponentially.\n\n## Key Theoretical Contributions\n\nThe research proves that f-mutual information measures are the unique gaming resistant mechanisms under natural conditions, with the overseer acting as an agent. The approach leverages the data processing inequality: any strategic manipulation of content necessarily reduces mutual information between responses, and by measuring these information relationships, evaluation mechanisms with formal gaming-resistance guarantees can be implemented.\n\n## Empirical Performance\n\nBounded measures like total variation distance mutual information (TVD-MI) achieve the largest effect sizes (mean d = 5.2) while demonstrating 10-100× better resistance to adversarial manipulation than LLM judges. Empirically, across ten domains from translation to peer review, all information-theoretic mechanisms achieve perfect discrimination (d > 0.5) between faithful and strategic agents.\n\nThe research represents a significant shift in AI evaluation methodology by proposing measurable, theoretically-grounded alternatives to traditional quality judgments."
    ],
    "durationSeconds": 11.574522409,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2bae7317-01f8-4cfc-9bbd-78126a1fb5c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T05:47:18.094Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014HroeS5ixwSbqGUF9djK4A`</summary>

```json
{
  "query": "PEG peer evaluation game Chen NeurIPS 2025 arXiv 2505.13636 conditional independence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50ed3e36-3939-4843-b379-3f1c84628d1e",
  "isSidechain": false,
  "requestId": "req_011CbDHyEM934FcWE2Kydk8v",
  "type": "assistant",
  "uuid": "b9bcc3d4-154f-4c8a-b464-caa5acd31317",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01St4CA1JQtyRUMdcDnSpva6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2109,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 23338,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2109,
          "output_tokens": 248,
          "cache_read_input_tokens": 23338,
          "cache_creation_input_tokens": 1801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1801
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

_source line 26 · 2026-05-20T05:47:19.044Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017xkznbvHtYe54PZPNfjCoM`</summary>

```json
{
  "query": "Turkmen et al correlated LLM ensemble Gaussian copula arXiv 2602.08003"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9bcc3d4-154f-4c8a-b464-caa5acd31317",
  "isSidechain": false,
  "requestId": "req_011CbDHyEM934FcWE2Kydk8v",
  "type": "assistant",
  "uuid": "507bd7a1-71db-418f-80af-0b30fae6f6ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01St4CA1JQtyRUMdcDnSpva6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2109,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 23338,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2109,
          "output_tokens": 248,
          "cache_read_input_tokens": 23338,
          "cache_creation_input_tokens": 1801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1801
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

_source line 27 · 2026-05-20T05:47:20.060Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018QGG1RzhDWRN6xJeSd1wLX`</summary>

```json
{
  "query": "certified robustness ensemble variance reduction polynomial scaling Horvath 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "507bd7a1-71db-418f-80af-0b30fae6f6ec",
  "isSidechain": false,
  "requestId": "req_011CbDHyEM934FcWE2Kydk8v",
  "type": "assistant",
  "uuid": "23d7af40-4241-400b-96e6-0290f34b96cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01St4CA1JQtyRUMdcDnSpva6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2109,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 23338,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2109,
          "output_tokens": 248,
          "cache_read_input_tokens": 23338,
          "cache_creation_input_tokens": 1801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1801
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

_source line 28 · 2026-05-20T05:47:20.846Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014zuPY3JyN1GSMCGbdQn255`</summary>

```json
{
  "query": "Kim et al correlated errors LLMs ICML 2025 arXiv 2506.07962 same architecture provider"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23d7af40-4241-400b-96e6-0290f34b96cd",
  "isSidechain": false,
  "requestId": "req_011CbDHyEM934FcWE2Kydk8v",
  "type": "assistant",
  "uuid": "86061525-fa1e-4f8f-9d84-ae52b9e88d91",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01St4CA1JQtyRUMdcDnSpva6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2109,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 23338,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2109,
          "output_tokens": 248,
          "cache_read_input_tokens": 23338,
          "cache_creation_input_tokens": 1801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1801
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

_source line 29 · 2026-05-20T05:47:24.871Z_

<details><summary>↩ Tool result · `toolu_014HroeS5ixwSbqGUF9djK4A`</summary>

```text
Web search results for query: "PEG peer evaluation game Chen NeurIPS 2025 arXiv 2505.13636 conditional independence"

Links: [{"title":"[2505.13636] Incentivizing Truthful Language Models via Peer Elicitation Games","url":"https://arxiv.org/abs/2505.13636"},{"title":"Incentivizing Truthful Language Models via Peer Elicitation Games","url":"https://arxiv.org/pdf/2505.13636"},{"title":"Incentivizing Truthful Language Models via Peer Elicitation Games","url":"https://arxiv.org/html/2505.13636"},{"title":"Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction","url":"https://arxiv.org/pdf/2601.20299"},{"title":"Incentivizing Evaluation via Limited Access to Ground Truth:   Peer-Prediction Makes Things Worse","url":"https://arxiv.org/pdf/1606.07042"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

Peer Elicitation Games (PEG) is a training-free, game-theoretic framework for aligning LLMs through a peer elicitation mechanism involving a generator and multiple discriminators instantiated from distinct base models.

Discriminators interact in a peer evaluation setting, where rewards are computed using a determinant-based mutual information score that provably incentivizes truthful reporting without requiring ground-truth labels.

The paper's theoretical contributions include: Each agent achieves sublinear regret via online learning, with cumulative performance approaching the best fixed truthful strategy, and the framework proves last-iterate convergence to a truthful Nash equilibrium.

In the evaluation setup, a generator LLM agent produces answers, while a group of discriminator LLM agents independently evaluate each response, serving as peers to promote both accuracy and consistency.

The paper is authored by Baiting Chen and colleagues and was submitted to NeurIPS 2025. You can access the full paper at [arXiv:2505.13636](https://arxiv.org/abs/2505.13636).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9bcc3d4-154f-4c8a-b464-caa5acd31317",
  "isSidechain": false,
  "promptId": "2758bb61-6675-4f99-8284-20dd6e249133",
  "type": "user",
  "uuid": "98b40036-3ab0-453f-a0ff-70eb90577c2a",
  "toolUseResult": {
    "query": "PEG peer evaluation game Chen NeurIPS 2025 arXiv 2505.13636 conditional independence",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WPcuAZUJqkiSTbp5zRaZfv",
        "content": [
          {
            "title": "[2505.13636] Incentivizing Truthful Language Models via Peer Elicitation Games",
            "url": "https://arxiv.org/abs/2505.13636"
          },
          {
            "title": "Incentivizing Truthful Language Models via Peer Elicitation Games",
            "url": "https://arxiv.org/pdf/2505.13636"
          },
          {
            "title": "Incentivizing Truthful Language Models via Peer Elicitation Games",
            "url": "https://arxiv.org/html/2505.13636"
          },
          {
            "title": "Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction",
            "url": "https://arxiv.org/pdf/2601.20299"
          },
          {
            "title": "Incentivizing Evaluation via Limited Access to Ground Truth:   Peer-Prediction Makes Things Worse",
            "url": "https://arxiv.org/pdf/1606.07042"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what I found:\n\nPeer Elicitation Games (PEG) is a training-free, game-theoretic framework for aligning LLMs through a peer elicitation mechanism involving a generator and multiple discriminators instantiated from distinct base models.\n\nDiscriminators interact in a peer evaluation setting, where rewards are computed using a determinant-based mutual information score that provably incentivizes truthful reporting without requiring ground-truth labels.\n\nThe paper's theoretical contributions include: Each agent achieves sublinear regret via online learning, with cumulative performance approaching the best fixed truthful strategy, and the framework proves last-iterate convergence to a truthful Nash equilibrium.\n\nIn the evaluation setup, a generator LLM agent produces answers, while a group of discriminator LLM agents independently evaluate each response, serving as peers to promote both accuracy and consistency.\n\nThe paper is authored by Baiting Chen and colleagues and was submitted to NeurIPS 2025. You can access the full paper at [arXiv:2505.13636](https://arxiv.org/abs/2505.13636)."
    ],
    "durationSeconds": 6.772768448999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b9bcc3d4-154f-4c8a-b464-caa5acd31317",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T05:47:25.863Z_

<details><summary>↩ Tool result · `toolu_017xkznbvHtYe54PZPNfjCoM`</summary>

```text
Web search results for query: "Turkmen et al correlated LLM ensemble Gaussian copula arXiv 2602.08003"

Links: [{"title":"[2602.08003] Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection","url":"https://arxiv.org/abs/2602.08003"},{"title":"Don’t Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection","url":"https://arxiv.org/html/2602.08003"},{"title":"Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection","url":"https://arxiv.org/pdf/2602.08003"},{"title":"Rethinking the Role of LLMs in Time Series Forecasting","url":"https://arxiv.org/html/2602.14744v1"},{"title":"Wisdom of the Silicon Crowd: LLM Ensemble Prediction Capabilities Rival   Human Crowd Accuracy","url":"https://arxiv.org/pdf/2402.19379"}]

I found the paper! Here are the key details:

The paper is titled "Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection" by Yigit Turkmen, Baturalp Buyukates, and Melih Bastopcu.

**Main Contributions:**

The paper addresses the fact that large language models are often ensembled together to improve overall reliability and robustness, but in practice models are strongly correlated. 

The authors formulate budgeted ensemble selection as maximizing the mutual information between the true label and predictions of the selected models.

**Key Technical Approach:**

To explain why performance can saturate even with many models, the authors model the correlated errors of the models using Gaussian-copula and show an information-theoretic error floor for the performance of the ensemble.

They propose a simple greedy mutual-information selection algorithm that estimates the required information terms directly from data and iteratively builds an ensemble under a query budget.

**Evaluation:**

They test their approach on two question answering datasets and one binary sentiment classification dataset: MEDMCQA, MMLU, and IMDB movie reviews.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "507bd7a1-71db-418f-80af-0b30fae6f6ec",
  "isSidechain": false,
  "promptId": "2758bb61-6675-4f99-8284-20dd6e249133",
  "type": "user",
  "uuid": "9812ac2e-7b26-4a20-b4e1-60080ec1ad4c",
  "toolUseResult": {
    "query": "Turkmen et al correlated LLM ensemble Gaussian copula arXiv 2602.08003",
    "results": [
      {
        "tool_use_id": "srvtoolu_015MCqF35GicEBoLoQyBrNbN",
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
            "title": "Rethinking the Role of LLMs in Time Series Forecasting",
            "url": "https://arxiv.org/html/2602.14744v1"
          },
          {
            "title": "Wisdom of the Silicon Crowd: LLM Ensemble Prediction Capabilities Rival   Human Crowd Accuracy",
            "url": "https://arxiv.org/pdf/2402.19379"
          }
        ]
      },
      "I found the paper! Here are the key details:\n\nThe paper is titled \"Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection\" by Yigit Turkmen, Baturalp Buyukates, and Melih Bastopcu.\n\n**Main Contributions:**\n\nThe paper addresses the fact that large language models are often ensembled together to improve overall reliability and robustness, but in practice models are strongly correlated. \n\nThe authors formulate budgeted ensemble selection as maximizing the mutual information between the true label and predictions of the selected models.\n\n**Key Technical Approach:**\n\nTo explain why performance can saturate even with many models, the authors model the correlated errors of the models using Gaussian-copula and show an information-theoretic error floor for the performance of the ensemble.\n\nThey propose a simple greedy mutual-information selection algorithm that estimates the required information terms directly from data and iteratively builds an ensemble under a query budget.\n\n**Evaluation:**\n\nThey test their approach on two question answering datasets and one binary sentiment classification dataset: MEDMCQA, MMLU, and IMDB movie reviews."
    ],
    "durationSeconds": 6.8139311379999965,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "507bd7a1-71db-418f-80af-0b30fae6f6ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T05:47:27.437Z_

<details><summary>↩ Tool result · `toolu_018QGG1RzhDWRN6xJeSd1wLX`</summary>

```text
Web search results for query: "certified robustness ensemble variance reduction polynomial scaling Horvath 2021"

Links: [{"title":"Multi-head ensemble of smoothed classifiers for certified robustness - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608025003053"},{"title":"Boosting Certified Robustness for Time Series Classification with Efficient Self-Ensemble","url":"https://arxiv.org/html/2409.02802v3"},{"title":"CR-UTP: Certified Robustness against Universal Text Perturbations on Large Language Models","url":"https://arxiv.org/html/2406.01873v2"},{"title":"Boosting Certificate Robustness for Time Series Classification with Efficient Self-Ensemble | Proceedings of the 33rd ACM International Conference on Information and Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3627673.3679748"},{"title":"[2107.10873] On the Certified Robustness for Ensemble Models and Beyond","url":"https://arxiv.org/abs/2107.10873"},{"title":"Multi-head Ensemble of Smoothed Classifiers for Certified Robustness","url":"https://arxiv.org/pdf/2211.10882"},{"title":"(PDF) On the Certified Robustness for Ensemble Models and Beyond","url":"https://www.researchgate.net/publication/353451347_On_the_Certified_Robustness_for_Ensemble_Models_and_Beyond"}]

Based on the search results, I found relevant information about the Horvath 2021 work on certified robustness and ensemble variance reduction. Here are the key findings:

The paper by Miklós Z Horváth, Mark Niklas Müller, Marc Fischer, and Martin Vechev is titled "Boosting randomized smoothing with variance reduced classifiers" (arXiv preprint arXiv:2106.06946, 2021).

The main contribution of this work involves showing that the ensemble of multiple DNNs trained separately can reduce the predictive variance against Gaussian noises, leading to certified robustness improvements.

Horváth et al. (2021) employed ensembling techniques to reduce variance, thereby enhancing robustness. More specifically, this approach has been adapted for Randomized Smoothing, which involves employing multiple base classifiers trained with identical architectures but different random seeds.

The work has been influential in the field, with subsequent research building upon these ideas. For example, Randomized Smoothing (RS) is a promising technique for certified robustness, and recently in RS the ensemble of multiple Deep Neural Networks (DNNs) has shown state-of-the-art performances due to its variance reduction effect over Gaussian noise.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23d7af40-4241-400b-96e6-0290f34b96cd",
  "isSidechain": false,
  "promptId": "2758bb61-6675-4f99-8284-20dd6e249133",
  "type": "user",
  "uuid": "1be05cd3-5e49-47d8-b451-583262791648",
  "toolUseResult": {
    "query": "certified robustness ensemble variance reduction polynomial scaling Horvath 2021",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LQekEXnjsgBaHBVVKKnKbF",
        "content": [
          {
            "title": "Multi-head ensemble of smoothed classifiers for certified robustness - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0893608025003053"
          },
          {
            "title": "Boosting Certified Robustness for Time Series Classification with Efficient Self-Ensemble",
            "url": "https://arxiv.org/html/2409.02802v3"
          },
          {
            "title": "CR-UTP: Certified Robustness against Universal Text Perturbations on Large Language Models",
            "url": "https://arxiv.org/html/2406.01873v2"
          },
          {
            "title": "Boosting Certificate Robustness for Time Series Classification with Efficient Self-Ensemble | Proceedings of the 33rd ACM International Conference on Information and Knowledge Management",
            "url": "https://dl.acm.org/doi/10.1145/3627673.3679748"
          },
          {
            "title": "[2107.10873] On the Certified Robustness for Ensemble Models and Beyond",
            "url": "https://arxiv.org/abs/2107.10873"
          },
          {
            "title": "Multi-head Ensemble of Smoothed Classifiers for Certified Robustness",
            "url": "https://arxiv.org/pdf/2211.10882"
          },
          {
            "title": "(PDF) On the Certified Robustness for Ensemble Models and Beyond",
            "url": "https://www.researchgate.net/publication/353451347_On_the_Certified_Robustness_for_Ensemble_Models_and_Beyond"
          }
        ]
      },
      "Based on the search results, I found relevant information about the Horvath 2021 work on certified robustness and ensemble variance reduction. Here are the key findings:\n\nThe paper by Miklós Z Horváth, Mark Niklas Müller, Marc Fischer, and Martin Vechev is titled \"Boosting randomized smoothing with variance reduced classifiers\" (arXiv preprint arXiv:2106.06946, 2021).\n\nThe main contribution of this work involves showing that the ensemble of multiple DNNs trained separately can reduce the predictive variance against Gaussian noises, leading to certified robustness improvements.\n\nHorváth et al. (2021) employed ensembling techniques to reduce variance, thereby enhancing robustness. More specifically, this approach has been adapted for Randomized Smoothing, which involves employing multiple base classifiers trained with identical architectures but different random seeds.\n\nThe work has been influential in the field, with subsequent research building upon these ideas. For example, Randomized Smoothing (RS) is a promising technique for certified robustness, and recently in RS the ensemble of multiple Deep Neural Networks (DNNs) has shown state-of-the-art performances due to its variance reduction effect over Gaussian noise."
    ],
    "durationSeconds": 7.373466774000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "23d7af40-4241-400b-96e6-0290f34b96cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T05:47:27.882Z_

<details><summary>↩ Tool result · `toolu_014zuPY3JyN1GSMCGbdQn255`</summary>

```text
Web search results for query: "Kim et al correlated errors LLMs ICML 2025 arXiv 2506.07962 same architecture provider"

Links: [{"title":"[2506.07962] Correlated Errors in Large Language Models","url":"https://arxiv.org/abs/2506.07962"},{"title":"[Paper Note] Correlated Errors in Large Language Models, Elliot Kim+, ICML'25 · Issue #2145 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/2145"},{"title":"[2506.07962v1] Correlated Errors in Large Language Models","url":"https://arxiv.org/abs/2506.07962v1"},{"title":"[PDF] Correlated Errors in Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Correlated-Errors-in-Large-Language-Models-Kim-Garg/365ba5ab458c8ad6d4ed6996ab3e0ff3f386edbc"},{"title":"(PDF) Correlated Errors in Large Language Models","url":"https://www.researchgate.net/publication/392529896_Correlated_Errors_in_Large_Language_Models"},{"title":"arXiv:2506.07962v1 [cs.CL] 9 Jun 2025","url":"https://arxiv.org/pdf/2506.07962"},{"title":"LLMs and the Madness of Crowds","url":"https://arxiv.org/pdf/2411.01539"},{"title":"LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations","url":"https://arxiv.org/pdf/2410.02707"}]

I found the paper! Here's what the search results reveal about this research:

## Paper Overview

The paper is titled "Correlated Errors in Large Language Models" by Elliot Kim, Avi Garg, Kenny Peng, and Nikhil Garg, and it was submitted to arXiv on June 9, 2025.

## Key Findings

The researchers conducted a large-scale empirical evaluation on over 350 LLMs using two popular leaderboards and a resume-screening task, finding substantial correlation in model errors—on one leaderboard dataset, models agree 60% of the time when both models err.

The study identifies factors driving model correlation, including shared architectures and providers. However, larger and more accurate models have highly correlated errors, even with distinct architectures and providers.

## Downstream Applications

The paper shows the effects of correlation in two downstream tasks: LLM-as-judge evaluation and hiring—the latter reflecting theoretical predictions regarding algorithmic monoculture.

You can access the full paper at https://arxiv.org/abs/2506.07962.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86061525-fa1e-4f8f-9d84-ae52b9e88d91",
  "isSidechain": false,
  "promptId": "2758bb61-6675-4f99-8284-20dd6e249133",
  "type": "user",
  "uuid": "5436a438-2ec0-46a2-b8c0-5e2921040b1c",
  "toolUseResult": {
    "query": "Kim et al correlated errors LLMs ICML 2025 arXiv 2506.07962 same architecture provider",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Voi2tqeFETQSkecspfMTjo",
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
      "I found the paper! Here's what the search results reveal about this research:\n\n## Paper Overview\n\nThe paper is titled \"Correlated Errors in Large Language Models\" by Elliot Kim, Avi Garg, Kenny Peng, and Nikhil Garg, and it was submitted to arXiv on June 9, 2025.\n\n## Key Findings\n\nThe researchers conducted a large-scale empirical evaluation on over 350 LLMs using two popular leaderboards and a resume-screening task, finding substantial correlation in model errors—on one leaderboard dataset, models agree 60% of the time when both models err.\n\nThe study identifies factors driving model correlation, including shared architectures and providers. However, larger and more accurate models have highly correlated errors, even with distinct architectures and providers.\n\n## Downstream Applications\n\nThe paper shows the effects of correlation in two downstream tasks: LLM-as-judge evaluation and hiring—the latter reflecting theoretical predictions regarding algorithmic monoculture.\n\nYou can access the full paper at https://arxiv.org/abs/2506.07962."
    ],
    "durationSeconds": 7.033435970999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "86061525-fa1e-4f8f-9d84-ae52b9e88d91",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-20T05:47:27.886Z_

```json
{
  "parentUuid": "5436a438-2ec0-46a2-b8c0-5e2921040b1c",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "92ab09a9-162a-46b2-ba23-21698a6dd2ff",
  "timestamp": "2026-05-20T05:47:27.886Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Corr…",
  "leafUuid": "92ab09a9-162a-46b2-ba23-21698a6dd2ff",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-judge LLM evaluation manipulation resistance bounds",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e"
}
```

---

### Assistant

_source line 36 · 2026-05-20T05:47:32.308Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've gathered substantial research. Let me do a couple more targeted searches to fill in gaps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92ab09a9-162a-46b2-ba23-21698a6dd2ff",
  "isSidechain": false,
  "requestId": "req_011CbDHzDkT7QxCQLTXK99aA",
  "type": "assistant",
  "uuid": "acea905a-3042-4cc5-be1d-e880fc2a78ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDzz1b8wgByo7Pb9a4eCYw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5046,
      "cache_read_input_tokens": 25139,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5046,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 245,
          "cache_read_input_tokens": 25139,
          "cache_creation_input_tokens": 5046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5046
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

_source line 37 · 2026-05-20T05:47:32.667Z_

Let me do a few more targeted searches to complete my research.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acea905a-3042-4cc5-be1d-e880fc2a78ff",
  "isSidechain": false,
  "requestId": "req_011CbDHzDkT7QxCQLTXK99aA",
  "type": "assistant",
  "uuid": "4c3928f6-e834-4c58-987a-d181670cee87",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDzz1b8wgByo7Pb9a4eCYw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5046,
      "cache_read_input_tokens": 25139,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5046,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 245,
          "cache_read_input_tokens": 25139,
          "cache_creation_input_tokens": 5046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5046
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

_source line 38 · 2026-05-20T05:47:34.090Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ky4WbhL5zFpgqG4VepY2c2`</summary>

```json
{
  "query": "SoK security LLM-as-a-judge arXiv 2603.29403 multi-model committee attack success rate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c3928f6-e834-4c58-987a-d181670cee87",
  "isSidechain": false,
  "requestId": "req_011CbDHzDkT7QxCQLTXK99aA",
  "type": "assistant",
  "uuid": "c752e333-2367-432f-a598-6193d3f0a50d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDzz1b8wgByo7Pb9a4eCYw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5046,
      "cache_read_input_tokens": 25139,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5046,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 245,
          "cache_read_input_tokens": 25139,
          "cache_creation_input_tokens": 5046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5046
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

_source line 39 · 2026-05-20T05:47:35.087Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y4jfjPQspKs5L7BhHgACE1`</summary>

```json
{
  "query": "SDPI strong data processing inequality Polyanskiy Wu adversarial channel capacity bounds"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c752e333-2367-432f-a598-6193d3f0a50d",
  "isSidechain": false,
  "requestId": "req_011CbDHzDkT7QxCQLTXK99aA",
  "type": "assistant",
  "uuid": "6fcf5086-6da4-4624-bd41-be4859eea7de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDzz1b8wgByo7Pb9a4eCYw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5046,
      "cache_read_input_tokens": 25139,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5046,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 245,
          "cache_read_input_tokens": 25139,
          "cache_creation_input_tokens": 5046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5046
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

_source line 40 · 2026-05-20T05:47:36.011Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012fPPMzkNcUytgm62jpJeSE`</summary>

```json
{
  "query": "semantic collapse multi-LLM systems Kong 2026 arXiv 2605.17193 representational collapse committee"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fcf5086-6da4-4624-bd41-be4859eea7de",
  "isSidechain": false,
  "requestId": "req_011CbDHzDkT7QxCQLTXK99aA",
  "type": "assistant",
  "uuid": "05e72621-f033-4ede-9ef5-e30317820d59",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDzz1b8wgByo7Pb9a4eCYw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5046,
      "cache_read_input_tokens": 25139,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5046,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 245,
          "cache_read_input_tokens": 25139,
          "cache_creation_input_tokens": 5046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5046
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

_source line 41 · 2026-05-20T05:47:39.820Z_

<details><summary>↩ Tool result · `toolu_01Ky4WbhL5zFpgqG4VepY2c2`</summary>

```text
Web search results for query: "SoK security LLM-as-a-judge arXiv 2603.29403 multi-model committee attack success rate"

Links: [{"title":"[2603.29403] Security in LLM-as-a-Judge: A Comprehensive SoK","url":"https://arxiv.org/abs/2603.29403"},{"title":"SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK","url":"https://arxiv.org/pdf/2603.29403"},{"title":"From Code to Courtroom: LLMs as the New Software Judges","url":"https://arxiv.org/pdf/2503.02246"},{"title":"The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2509.26072"},{"title":"Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on   Zero-shot LLM Assessment","url":"https://arxiv.org/pdf/2402.14016"},{"title":"Safer or Luckier? LLMs as Safety Evaluators Are Not Robust to Artifacts","url":"https://arxiv.org/pdf/2503.09347"},{"title":"Evaluating the Reliability and Fidelity of Automated Judgment Systems of Large Language Models","url":"https://arxiv.org/pdf/2603.22214"}]

Based on the search results, I found the paper you're looking for. LLM-as-a-Judge (LaaJ) is a paradigm where powerful language models assess the quality, safety, or correctness of generated outputs, but it introduces novel security risks and reliability concerns - LLM-based judges can become both targets of adversarial manipulation and instruments through which attacks are conducted, potentially compromising the trustworthiness of evaluation pipelines.

The paper presents the first Systematization of Knowledge (SoK) focusing on the security aspects of LLM-as-a-Judge systems, performing a comprehensive literature review across major academic databases, analyzing 863 works and selecting 45 relevant studies published between 2020 and 2026.

The paper (arXiv:2603.29403) was submitted on March 31, 2026 with a revised version on April 6, 2026. However, the search results do not contain specific information about multi-model committee attacks or their success rates from this paper. To find those specific details, you would need to access the full PDF of the paper directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c752e333-2367-432f-a598-6193d3f0a50d",
  "isSidechain": false,
  "promptId": "2758bb61-6675-4f99-8284-20dd6e249133",
  "type": "user",
  "uuid": "b29bb6d2-c5e1-4418-978d-04f106aa9cf1",
  "toolUseResult": {
    "query": "SoK security LLM-as-a-judge arXiv 2603.29403 multi-model committee attack success rate",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TXFi8DqwA8FvPaqutBCS1s",
        "content": [
          {
            "title": "[2603.29403] Security in LLM-as-a-Judge: A Comprehensive SoK",
            "url": "https://arxiv.org/abs/2603.29403"
          },
          {
            "title": "SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK",
            "url": "https://arxiv.org/pdf/2603.29403"
          },
          {
            "title": "From Code to Courtroom: LLMs as the New Software Judges",
            "url": "https://arxiv.org/pdf/2503.02246"
          },
          {
            "title": "The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2509.26072"
          },
          {
            "title": "Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on   Zero-shot LLM Assessment",
            "url": "https://arxiv.org/pdf/2402.14016"
          },
          {
            "title": "Safer or Luckier? LLMs as Safety Evaluators Are Not Robust to Artifacts",
            "url": "https://arxiv.org/pdf/2503.09347"
          },
          {
            "title": "Evaluating the Reliability and Fidelity of Automated Judgment Systems of Large Language Models",
            "url": "https://arxiv.org/pdf/2603.22214"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. LLM-as-a-Judge (LaaJ) is a paradigm where powerful language models assess the quality, safety, or correctness of generated outputs, but it introduces novel security risks and reliability concerns - LLM-based judges can become both targets of adversarial manipulation and instruments through which attacks are conducted, potentially compromising the trustworthiness of evaluation pipelines.\n\nThe paper presents the first Systematization of Knowledge (SoK) focusing on the security aspects of LLM-as-a-Judge systems, performing a comprehensive literature review across major academic databases, analyzing 863 works and selecting 45 relevant studies published between 2020 and 2026.\n\nThe paper (arXiv:2603.29403) was submitted on March 31, 2026 with a revised version on April 6, 2026. However, the search results do not contain specific information about multi-model committee attacks or their success rates from this paper. To find those specific details, you would need to access the full PDF of the paper directly."
    ],
    "durationSeconds": 5.725784983000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c752e333-2367-432f-a598-6193d3f0a50d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T05:47:40.935Z_

<details><summary>↩ Tool result · `toolu_01Y4jfjPQspKs5L7BhHgACE1`</summary>

```text
Web search results for query: "SDPI strong data processing inequality Polyanskiy Wu adversarial channel capacity bounds"

Links: [{"title":"Strong data-processing inequalities for channels and Bayesian networks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2015arXiv150806025P/abstract"},{"title":"[PDF] A note on the strong data-processing inequalities in Bayesian networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-note-on-the-strong-data-processing-inequalities-Polyanskiy-Wu/5b60c094c7aa5a43f92464db0395da3b7557a331"},{"title":"[PDF] Strong data-processing inequalities for channels and Bayesian networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Strong-data-processing-inequalities-for-channels-Polyanskiy-Wu/1ed8f456a9d95dea1d7a76725a26ffa7bf364311"},{"title":"[1508.06025] Strong data-processing inequalities for channels and Bayesian networks","url":"https://arxiv.org/abs/1508.06025"},{"title":"Strong Data-Processing Inequalities for Channels and Bayesian Networks | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-1-4939-7005-6_7"},{"title":"Strong data-processing inequalities for channels and Bayesian networks","url":"https://people.lids.mit.edu/yp/homepage/data/simple-IMA.pdf"},{"title":"Strong Data Processing Inequalities for Input Constrained Additive Noise Channels | Request PDF","url":"https://www.researchgate.net/publication/386862458_Strong_Data_Processing_Inequalities_for_Input_Constrained_Additive_Noise_Channels"},{"title":"Strong Data-Processing Inequalities for Channels and Bayesian Networks","url":"https://www.researchgate.net/publication/316328061_Strong_Data-Processing_Inequalities_for_Channels_and_Bayesian_Networks"},{"title":"Strong data-processing inequalities for channels and Bayesian networks","url":"https://arxiv.org/pdf/1508.06025"},{"title":"[1512.06429] Strong Data Processing Inequalities for Input Constrained Additive Noise Channels","url":"https://arxiv.org/abs/1512.06429"}]

Based on the search results, here's what I found:

## Overview

The data-processing inequality states that I(U;Y) ≤ I(U;X) for a Markov chain U → X → Y, and has been used for proving impossibility results in information theory.

## Strong Data Processing Inequalities (SDPIs)

Various channel-dependent improvements called strong data-processing inequalities, or SDPIs, have been proposed both classically and more recently. 

The key work by Polyanskiy and Wu addresses these concepts in their paper "Strong data-processing inequalities for channels and Bayesian networks." Their work surveys known results relating various notions of contraction for a single channel, and then considers the basic extension: given SDPI for each constituent channel in a Bayesian network, how to produce an end-to-end SDPI.

## Methodology

Their approach is based on the Evans-Schulman method, which is demonstrated for three different kinds of SDPIs: the usual Ahlswede-Gács type contraction coefficients (mutual information), Dobrushin's contraction coefficients (total variation), and the F_I-curve (the best possible non-linear SDPI for a given channel).

## Related Work on Noise Channels

A related paper by Calmon, Polyanskiy, and Wu quantifies the observation that adding noise reduces available information by means of non-linear strong data processing inequalities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fcf5086-6da4-4624-bd41-be4859eea7de",
  "isSidechain": false,
  "promptId": "2758bb61-6675-4f99-8284-20dd6e249133",
  "type": "user",
  "uuid": "b17372af-1218-42ea-8fe2-c6484c1b6c2f",
  "toolUseResult": {
    "query": "SDPI strong data processing inequality Polyanskiy Wu adversarial channel capacity bounds",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ULBcSQZj4HaiHzYmooehoJ",
        "content": [
          {
            "title": "Strong data-processing inequalities for channels and Bayesian networks - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2015arXiv150806025P/abstract"
          },
          {
            "title": "[PDF] A note on the strong data-processing inequalities in Bayesian networks | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/A-note-on-the-strong-data-processing-inequalities-Polyanskiy-Wu/5b60c094c7aa5a43f92464db0395da3b7557a331"
          },
          {
            "title": "[PDF] Strong data-processing inequalities for channels and Bayesian networks | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Strong-data-processing-inequalities-for-channels-Polyanskiy-Wu/1ed8f456a9d95dea1d7a76725a26ffa7bf364311"
          },
          {
            "title": "[1508.06025] Strong data-processing inequalities for channels and Bayesian networks",
            "url": "https://arxiv.org/abs/1508.06025"
          },
          {
            "title": "Strong Data-Processing Inequalities for Channels and Bayesian Networks | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-1-4939-7005-6_7"
          },
          {
            "title": "Strong data-processing inequalities for channels and Bayesian networks",
            "url": "https://people.lids.mit.edu/yp/homepage/data/simple-IMA.pdf"
          },
          {
            "title": "Strong Data Processing Inequalities for Input Constrained Additive Noise Channels | Request PDF",
            "url": "https://www.researchgate.net/publication/386862458_Strong_Data_Processing_Inequalities_for_Input_Constrained_Additive_Noise_Channels"
          },
          {
            "title": "Strong Data-Processing Inequalities for Channels and Bayesian Networks",
            "url": "https://www.researchgate.net/publication/316328061_Strong_Data-Processing_Inequalities_for_Channels_and_Bayesian_Networks"
          },
          {
            "title": "Strong data-processing inequalities for channels and Bayesian networks",
            "url": "https://arxiv.org/pdf/1508.06025"
          },
          {
            "title": "[1512.06429] Strong Data Processing Inequalities for Input Constrained Additive Noise Channels",
            "url": "https://arxiv.org/abs/1512.06429"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\n## Overview\n\nThe data-processing inequality states that I(U;Y) ≤ I(U;X) for a Markov chain U → X → Y, and has been used for proving impossibility results in information theory.\n\n## Strong Data Processing Inequalities (SDPIs)\n\nVarious channel-dependent improvements called strong data-processing inequalities, or SDPIs, have been proposed both classically and more recently. \n\nThe key work by Polyanskiy and Wu addresses these concepts in their paper \"Strong data-processing inequalities for channels and Bayesian networks.\" Their work surveys known results relating various notions of contraction for a single channel, and then considers the basic extension: given SDPI for each constituent channel in a Bayesian network, how to produce an end-to-end SDPI.\n\n## Methodology\n\nTheir approach is based on the Evans-Schulman method, which is demonstrated for three different kinds of SDPIs: the usual Ahlswede-Gács type contraction coefficients (mutual information), Dobrushin's contraction coefficients (total variation), and the F_I-curve (the best possible non-linear SDPI for a given channel).\n\n## Related Work on Noise Channels\n\nA related paper by Calmon, Polyanskiy, and Wu quantifies the observation that adding noise reduces available information by means of non-linear strong data processing inequalities."
    ],
    "durationSeconds": 5.843577321999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6fcf5086-6da4-4624-bd41-be4859eea7de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-20T05:47:43.414Z_

<details><summary>↩ Tool result · `toolu_012fPPMzkNcUytgm62jpJeSE`</summary>

```text
Web search results for query: "semantic collapse multi-LLM systems Kong 2026 arXiv 2605.17193 representational collapse committee"

Links: [{"title":"[2605.17193] Multi-LLM Systems Exhibit Robust Semantic Collapse","url":"https://arxiv.org/abs/2605.17193"},{"title":"How to Tame Your LLM: Semantic Collapse in Continuous Systems","url":"https://arxiv.org/html/2512.05162v1"},{"title":"How to Tame Your LLM: Semantic Collapse in Continuous Systems","url":"https://arxiv.org/pdf/2512.05162"},{"title":"Asymptotic Semantic Collapse in Hierarchical Optimization","url":"https://arxiv.org/pdf/2602.18450"},{"title":"[2512.05162] How to Tame Your LLM: Semantic Collapse in Continuous Systems","url":"https://arxiv.org/abs/2512.05162"},{"title":"Representational Collapse in Multi-Agent LLM Committees: Measurement and Diversity-Aware Consensus","url":"https://arxiv.org/pdf/2604.03809"}]

Based on the search results, I found relevant information about your query:

## Multi-LLM Systems and Semantic Collapse (Kong et al., 2026)

Multi-LLM systems operating in closed loops exhibit semantic collapse: systematic convergence in semantic representations despite apparent lexical variation. This is the arXiv paper 2605.17193 authored by Weiyi Kong, Shiyang Lai, Jinghua Piao, and James Evans, submitted on May 16, 2026.

The research shows that across model families, extended simulations of 200 to 1,000 rounds show this pattern consistently, and twelve intervention strategies spanning decoding parameters, prompt design, agent composition, activation engineering, and reinforcement learning fail to restore semantic diversity. Mechanistic analyses suggest that semantic collapse is not explained by alignment or conformity biases, but is consistent with intrinsic properties of autoregressive generation.

## Representational Collapse in LLM Committees

Additionally, the search found a related paper on representational collapse in multi-agent LLM committees, where agents replicate the same model under different role prompts with majority vote aggregation, and measurements show mean cosine similarity of 0.888 and effective rank of 2.17 out of 3.0 across three agents on GSM8K questions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05e72621-f033-4ede-9ef5-e30317820d59",
  "isSidechain": false,
  "promptId": "2758bb61-6675-4f99-8284-20dd6e249133",
  "type": "user",
  "uuid": "2ce2f936-555c-4a67-b5ed-11d9f382b378",
  "toolUseResult": {
    "query": "semantic collapse multi-LLM systems Kong 2026 arXiv 2605.17193 representational collapse committee",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TdXZ2oukrWJLp32jBbMwCh",
        "content": [
          {
            "title": "[2605.17193] Multi-LLM Systems Exhibit Robust Semantic Collapse",
            "url": "https://arxiv.org/abs/2605.17193"
          },
          {
            "title": "How to Tame Your LLM: Semantic Collapse in Continuous Systems",
            "url": "https://arxiv.org/html/2512.05162v1"
          },
          {
            "title": "How to Tame Your LLM: Semantic Collapse in Continuous Systems",
            "url": "https://arxiv.org/pdf/2512.05162"
          },
          {
            "title": "Asymptotic Semantic Collapse in Hierarchical Optimization",
            "url": "https://arxiv.org/pdf/2602.18450"
          },
          {
            "title": "[2512.05162] How to Tame Your LLM: Semantic Collapse in Continuous Systems",
            "url": "https://arxiv.org/abs/2512.05162"
          },
          {
            "title": "Representational Collapse in Multi-Agent LLM Committees: Measurement and Diversity-Aware Consensus",
            "url": "https://arxiv.org/pdf/2604.03809"
          }
        ]
      },
      "Based on the search results, I found relevant information about your query:\n\n## Multi-LLM Systems and Semantic Collapse (Kong et al., 2026)\n\nMulti-LLM systems operating in closed loops exhibit semantic collapse: systematic convergence in semantic representations despite apparent lexical variation. This is the arXiv paper 2605.17193 authored by Weiyi Kong, Shiyang Lai, Jinghua Piao, and James Evans, submitted on May 16, 2026.\n\nThe research shows that across model families, extended simulations of 200 to 1,000 rounds show this pattern consistently, and twelve intervention strategies spanning decoding parameters, prompt design, agent composition, activation engineering, and reinforcement learning fail to restore semantic diversity. Mechanistic analyses suggest that semantic collapse is not explained by alignment or conformity biases, but is consistent with intrinsic properties of autoregressive generation.\n\n## Representational Collapse in LLM Committees\n\nAdditionally, the search found a related paper on representational collapse in multi-agent LLM committees, where agents replicate the same model under different role prompts with majority vote aggregation, and measurements show mean cosine similarity of 0.888 and effective rank of 2.17 out of 3.0 across three agents on GSM8K questions."
    ],
    "durationSeconds": 7.399135069999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "05e72621-f033-4ede-9ef5-e30317820d59",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-20T05:48:35.021Z_

<details><summary>Logged reasoning block</summary>

```text
I now have comprehensive research. Let me synthesize everything and produce a thorough evaluation of this proposal. Let me think through each dimension carefully.

## Summary of what this proposal does:

The proposal aims to establish formal information-theoretic bounds on how much it costs an adversary to manipulate a multi-judge LLM evaluation system, as a function of measurable inter-judge correlation. The core theoretical claim is an "asymmetric duality": while accuracy improves exponentially with diverse judges (per Yang et al.), adversarial manipulation cost grows only polynomially (Ω(K_eff^{1/2})). 


The main contributions center on deriving formal N-judge manipulation-cost scaling, analyzing how performance degrades when correlation assumptions break down, proposing a practical protocol with empirical validation against adaptive attacks, and identifying what they call a "frontier diversity ceiling" insight.

**Strengths:**
The proposal demonstrates exceptional command of the literature with over 35 citations including very recent work, and it correctly identifies a genuine gap—no existing work provides formal N-judge manipulation-cost scaling as a function of measurable correlation.

Robertson & Koyejo focus on single evaluators, Kaneko & Baldwin on single models, Yang et al. on performance without adversarial robustness, and PEG assumes conditional independence without analyzing what happens when that breaks. The asymmetric duality between exponential accuracy scaling and polynomial robustness scaling with diversity is non-obvious and has real implications for how to allocate resources. The experimental design is comprehensive—15 off-the-shelf attacks plus 3 adaptive variants, FLOP-matched baselines, copula validation, PEG degradation analysis, dual-scaling visualization, cross-domain calibration transfer, and multiple ablations with proper statistical corrections. The "frontier diversity ceiling" insight is timely and grounded in empirical findings.

The authors are honest about limitations: the ½ exponent is stated as a conjecture for discrete settings, K* validity in adversarial contexts is an approximation, and they distinguish single-pass evaluation from iterative settings where collapse happens. But the ½ exponent conjecture is really the theoretical core—the entire manipulation cost bound relies on continuous-space variance reduction theory, which doesn't directly apply to discrete text perturbations where the geometry is fundamentally different. That's a significant gap that a reviewer could exploit by arguing the main theoretical claim is unproven. The proof also composes existing tools—SDPI, variance reduction, copula modeling, and Robertson's framework—rather than introducing fundamentally new theory.

The K* approximation for effective dimensionality in adversarial settings is hand-wavy too; if that bound is loose, the practical guarantees could become vacuous. And while the PEG degradation analysis under correlation is interesting, it feels more like a secondary corollary than a co-primary contribution, especially since the ε = f(ρ) relationship isn't concretely specified.

The scope here is extremely ambitious—five components, three benchmarks, fifteen-plus attacks, multiple ablations, theory, PEG analysis, a practical protocol, and frontier ceiling implications—which risks spreading effort too thin across many areas rather than developing a few deeply. Even if the certified bounds work out, they might be too loose to matter in practice; a 2.65-3.7× query increase to fool seven judges versus one might not justify the sevenfold computational cost of running seven judges in the first place. And there's a deeper issue with the discrete text space: adversarial perturbations don't naturally have an ℓ₂ structure, so the connection between continuous theory and discrete language is more problematic than I've acknowledged.

The proposal targets ICLR, AAAI, USENIX Security, and NeurIPS workshops in 2026-2027, not EMNLP 2026, though that doesn't affect the quality assessment itself. Looking at this for EMNLP specifically, the research question is genuinely important—LLM-as-a-judge systems are everywhere and their robustness matters—and the literature review is thorough. The theoretical framework, even if it's mostly composing existing tools, does surface an interesting asymmetry, and the experimental design seems solid so far.

The main weakness is that the core theoretical claim about the ½ exponent for discrete text is still just a conjecture, which undermines the "certifiable" framing. The scope is also quite ambitious. For EMNLP, this sits at the intersection of evaluation methodology and information theory—both areas the venue covers regularly—though the theoretical depth might be atypical. The research problem is strong and timely, the method shows medium-to-strong innovation with that asymmetry insight but relies on a conjecture for the discrete case, and the experimental design appears comprehensive with adaptive attacks and proper baselines.

The feasibility is medium given the ambition, though resource estimates seem reasonable. Writing is detailed but dense, and could better distinguish what's proven versus conjectured. I'm estimating around 30-42% acceptance probability, with a midpoint near 36%—solid research quality with genuine novelty, but the conjecture issue and scope concerns keep it from being a clear strong accept. The topic alignment with EMNLP 2026 is strong, though I should weigh whether that pushes the estimate higher.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ce2f936-555c-4a67-b5ed-11d9f382b378",
  "isSidechain": false,
  "requestId": "req_011CbDJ1NAjzg2GgX3MbBnDt",
  "type": "assistant",
  "uuid": "72e7915d-641b-41d0-a180-1a65b952292a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G77QaroGbJEJCbgofSmHuB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2505,
      "cache_read_input_tokens": 30185,
      "output_tokens": 6852,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2505,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6852,
          "cache_read_input_tokens": 30185,
          "cache_creation_input_tokens": 2505,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2505
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

_source line 45 · 2026-05-20T05:50:22.735Z_

Now I have sufficient research to evaluate this proposal thoroughly. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [Robertson & Koyejo, arXiv 2508.05469] (TMLR under review, 2025): Single-evaluator information-theoretic certification. TVD-MI achieves AUC 0.70–0.77 under adversarial manipulation; proves bounded f-divergences maintain polynomial guarantees. This is the direct single-judge predecessor; the proposal correctly identifies that it does not compose to N judges.
- [Kaneko & Baldwin, arXiv 2510.17000] (NeurIPS 2025 spotlight): Tight single-model adversarial query bounds N_min ≥ log₂(1/ε)/I_max via SPRT. Confirmed empirically on 7 LLMs. The proposal extends this to multi-judge composition—a natural and unstudied direction.
- [Yang et al., arXiv 2602.03794] (ICLR 2026 Workshop AIMS): Diversity-scaling framework; K* effective channel count; performance decays as (1-α_c)^{K*}. The proposal's "adversarial dual" framing is novel—Yang et al. only address performance, not adversarial robustness.
- [Turkmen et al., arXiv 2602.08003] (2026): Gaussian copula model for correlated LLM ensembles; MI-based selection; error floor theorem. Provides the copula parametric model the proposal uses for closed-form K_eff.
- [Kim et al., arXiv 2506.07962] (ICML 2025): Large-scale empirical study showing 60% error agreement across LLMs; +0.066 same-company, +0.076 same-architecture effects; larger/more accurate models are more correlated even across providers. Directly supports the "frontier diversity ceiling" claim.
- [Chen et al., arXiv 2505.13636] (NeurIPS 2025): PEG framework; dominant-strategy truthfulness via DMI scoring; conditional independence assumption (Assumption 4) is noted but degradation under violation is not characterized. The proposal's PEG degradation analysis fills this specific gap.
- [SoK, arXiv 2603.29403] (April 2026): Comprehensive systematization of LLM-as-a-Judge security; 50–68% ASR on open-source judges; 7-model committee reduces to 10–19% ASR but without formal explanation. The proposal aims to provide that formal explanation.
- [Horvath et al., arXiv 2106.06946] (2021): √K certified radius via ensemble variance reduction in continuous perturbation spaces. The ½ exponent origin—central to the proposal's core bound but proven only for continuous (ℓ₂) settings.
- [Kong et al., arXiv 2605.17193] (May 2026): Semantic collapse in closed-loop multi-LLM systems across 200–1000 rounds; 12 interventions fail. The proposal correctly distinguishes its single-pass protocol from this iterative setting.
- [Patel, arXiv 2604.03809] (April 2026): Effective rank 2.17/3.0 for homogeneous 3-agent committees. Supports diversity concerns but in iterative settings.
- [Polyanskiy & Wu, arXiv 1508.06025] (2017): Foundational SDPI framework; contraction coefficients for channels and Bayesian networks. The per-channel information leakage bound machinery.
- 调研总结: LLM-as-a-judge adversarial robustness is a rapidly growing field with strong single-evaluator foundations (Robertson & Koyejo, Kaneko & Baldwin) and emerging ensemble correlation models (Turkmen, Kim). The specific gap—formal multi-judge manipulation-cost scaling as a function of measurable correlation—is genuinely open. No existing work provides the exponential-polynomial asymmetry between performance and robustness scaling. The proposal is well-positioned at a real research frontier.

【整体印象】:
作为审稿人，我的第一反应是：这是一篇极其充分准备的 proposal，展示了对文献的卓越掌握和对研究 gap 的精准定位。asymmetric adversarial dual（性能指数级提升 vs. 鲁棒性仅多项式提升）这个 insight 是 genuinely interesting 且 non-obvious 的，如果能被严格证明，对资源分配有直接的实践指导意义。实验设计的完备程度在 proposal 阶段罕见。

然而，我有两个核心顾虑让我无法直接倾向 accept：
(1) 核心理论声称的 ½ 指数在离散文本空间中是 conjecture 而非 theorem——这实质性地削弱了 "certifiable" 的标题承诺；
(2) 方法本质上是对多个已有工具（SDPI + variance reduction + copula + TVD-MI）的组合，而非建立根本性的新理论。

整体倾向：**borderline accept / weak accept**——如果实验能证实离散空间中的 ½ 指数 conjecture 且 certified bounds 不过于 vacuous，可以 accept；否则可能滑向 weak reject。

【核心贡献】:
三层贡献：
1. **理论**：建立 N-judge manipulation cost 关于 K_eff 的 Ω(K_eff^{1/2}) 下界，并揭示与 Yang et al. 性能指数级 scaling 之间的 asymmetry——这是最核心的贡献。"Frontier diversity ceiling" 推论（因为高能力模型相关性增加，K_eff → 1）是一个高影响力的 provocative insight。
2. **分析**：PEG 在相关性违反条件独立假设下的 ε-approximate equilibrium 退化曲线——虽然声称是 co-primary contribution，但更像是一个有价值的 corollary。
3. **实证**：极其全面的 adversarial validation pipeline，包含 adaptive attacks、FLOP-matched baselines、copula GoF 验证、dual-scaling 可视化。

对领域的价值：如果理论结果成立，这将为 multi-judge evaluation 的 robustness 提供第一个可计算的形式化保证，填补了一个真实且重要的空白。"Frontier diversity ceiling" 的政策含义对整个 AI evaluation 社区有价值。

【方法合理性】:
方法的整体逻辑链是合理的：SDPI 限制每个 judge 的信息泄露 → 并行 judges 信息增益可加 → variance reduction 给出 perturbation cost 下界。这个推理框架在连续空间是 sound 的。

**但存在两个关键的方法论风险：**

1. **½ 指数的离散空间推广**：连续空间 ℓ₂ variance reduction 的 √K 不能自动推广到离散文本 perturbation。离散空间没有自然的 ℓ₂ 结构；对抗性文本扰动的几何与连续扰动根本不同（token 替换、插入、删除）。proposal 诚实地承认这是 conjecture，但 "certifiable" 标题暗示的是 proven guarantee。这个 gap 是审稿人最可能攻击的点。

2. **K* 在对抗性场景中的有效性**：K* = 2^{H(ρ)} 原本是为 performance scaling 设计的（Yang et al.），将其用作 adversarial effective dimensionality 的 upper-bound approximation，理由是 "shared eigenstructure"，这个 justification 较弱。如果 K* 在对抗性场景中是 loose bound，certified bounds 可能 vacuous。

**更简单的替代方案？** 纯经验性的方法（如 SoK 中的 7-model committee）已经将 ASR 降到 10-19%，不需要理论框架。但 proposal 正确指出经验方法无法保证对未来攻击的鲁棒性——certified guarantee 的价值在于其 attack-agnostic 性质，类似于 randomized smoothing 的价值主张。这个论证是有说服力的。

【5 维度打分】:
  1. 研究问题: 【强】 — Multi-judge LLM evaluation 的形式化鲁棒性保证是一个重要且 timely 的问题。SoK (arXiv 2603.29403) 已证明 50-68% ASR 的现实威胁；Kim et al. (ICML 2025) 揭示的相关性模式使得问题更加紧迫。gap 定位准确：单 judge 有 Robertson & Koyejo 和 Kaneko & Baldwin 的理论，多 judge 没有。"性能 vs. 鲁棒性 asymmetry" 对资源分配有直接实践意义。
  
  2. 方法与创新: 【中】 — 核心 insight（exponential-polynomial asymmetry）是 genuinely novel 且 non-obvious 的。但方法上主要是组合已有工具：SDPI (Polyanskiy & Wu) + variance reduction (Horvath et al.) + copula (Turkmen et al.) + TVD-MI (Robertson & Koyejo)。组合本身有价值，但理论深度受限于 ½ 指数在离散空间仍为 conjecture。PEG 退化分析是自然的 extension，创新性有限。与 Horvath et al. (2021) 的区别主要在于将 continuous certified robustness 应用到 LLM evaluation 场景——场景创新多于方法创新。K* 的对抗性场景适用性论证不够有力。
  
  3. 实验设计: 【强】 — 这是 proposal 最突出的维度。遵循 Carlini et al. (arXiv 1902.06705) adaptive attack 标准；15 off-the-shelf + 3 protocol-aware adaptive attacks；FLOP-matched baselines（避免公平性争议）；copula GoF 验证（检验模型假设）；dual-scaling 可视化（直接展示核心 asymmetry）；cross-domain calibration transfer（实用性）；PEG degradation 专项实验；多 seed + bootstrap CI + BH/Bonferroni 校正。pilot study 设计了 go/no-go 标准。几乎没有遗漏。唯一的小问题：15 attacks + 3 adaptive + 所有 ablations + 3 benchmarks 的实际执行可能超出 timeline。
  
  4. 可行性: 【中】 — 资源估计（1,800-2,800 H100-hrs, ~$4,500-7,000）是合理的。但 scope 极其 ambitious：5 components × 3 benchmarks × 18+ attack vectors × 多项 ablations × 理论证明 × PEG 分析，18-24 周的 timeline 非常紧张。存在执行风险：如果 pilot study 发现 ρ > 0.7（所有开源模型高度相关），虽然 proposal 有 backup plan，但主要实验设计可能需要根本性调整。½ 指数的经验验证如果不支持 conjecture，需要在论文中如何处理？
  
  5. 写作与呈现: 【中】 — 文献覆盖极其全面（35+ references），gap 定位精准，逻辑链清晰。但 proposal 过于密集——信息量过大反而模糊了核心贡献的清晰度。"Co-primary contribution" 的 PEG 分析分散了注意力。"Certifiable" 标题与 conjecture 现实之间的张力需要在写作中更审慎地处理。建议正文聚焦于 asymmetry + frontier ceiling，将 PEG 退化作为 secondary contribution。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】:
向上因素：(1) 研究问题的重要性和时效性——LLM-as-a-judge 安全是当前热点；(2) 文献覆盖和 gap 定位的质量在 proposal 中属于顶级；(3) 实验设计的完备程度本身就是显著加分项，特别是 adaptive attacks + FLOP-matched baselines；(4) "frontier diversity ceiling" 是一个有政策影响力的 insight，如果得到验证将引起广泛关注；(5) asymmetric duality 是一个 clean 且 memorable 的核心结果。

向下因素：(1) **核心理论的 ½ 指数在离散文本空间是 conjecture，不是 proof**——这直接削弱了 "certifiable" 的核心承诺，是最可能导致 reject 的因素；(2) 方法的组合性质（connecting existing dots）可能被认为 novelty 不足，特别是理论贡献部分；(3) scope 过于 ambitious，执行风险高——如果必须削减，核心理论 + frontier ceiling + 一个 benchmark 可能是最优子集；(4) certified bounds 的 practical tightness 是未知数——如果 2.65-3.7× cost multiplier 对应 7× compute cost，cost-benefit 不吸引人。

中位 35% 反映：这是一篇高于平均水平的 solid 投稿，在研究问题和实验设计上有明显优势，但核心理论贡献被 conjecture status 削弱、方法创新以组合为主而非原创性突破，这两个因素将其拉回 borderline 区间。如果执行良好且 conjecture 得到强实验支持，可以向 40%+ 靠拢。

【主要风险】:
1. **½ 指数 conjecture 风险**：离散文本空间的 perturbation geometry 与连续 ℓ₂ 空间根本不同。如果经验验证显示真实指数与 ½ 有显著偏差（特别是如果更差），核心理论框架的 credibility 将受到严重质疑。审稿人很可能以 "main theorem is a conjecture, not a proof" 为由给 weak reject。
2. **Certified bounds 可能 vacuous**：类似于 randomized smoothing 在高维空间中 certified radius 往往过小，K_eff-based bounds 可能在实际规模（K=3-7）下给出的 manipulation cost 增益过于 modest，使得整个 certification 框架缺乏实际指导价值。如果 certified bounds 远松于 empirical observation，reviewer 会质疑 theoretical contribution 的实际意义。

【实施评估】:
  - 计算资源: 1,800-2,800 H100-equivalent GPU hours (~$4,500-$7,000)。主要消耗在 adaptive attacks (PGD on 13-17B active params) 和 multi-judge protocol runs。合理但偏 ambitious；建议预留 20% buffer。
  - 数据需求: SummEval (已有)、LiveCodeBench (已有，contamination-resistant)、GPQA Diamond (已有)。无需新数据收集，仅需 calibration samples (≥500/benchmark)。数据方面风险低。
  - 人工介入: 无人工标注需求。但 adaptive attack 设计和 copula model selection 需要专业判断。PEG degradation 实验中的 "strategic deviator judge" 构造需要 careful prompt engineering。
  - 训练需求: **无模型训练**。全部使用 off-the-shelf 模型。这是一个重要的实施优势——降低了不确定性和资源风险。
  - 新 Benchmark: 不需要。使用已有 benchmarks。
  - 预估周期: 18-24 周（manual）。建议按 24 周上限规划。关键路径：Pilot (2w) → 理论证明 refinement (4w) → 主实验 (8w) → Adaptive attacks (4w) → 写作 (4-6w)。Pilot 的 go/no-go 决策是关键门控点。
```

Sources:
- [Security in LLM-as-a-Judge: A Comprehensive SoK](https://arxiv.org/abs/2603.29403)
- [RobustJudge: LLMs Cannot Reliably Judge](https://arxiv.org/html/2506.09443v1)
- [Let's Measure Information Step-by-Step (Robertson & Koyejo)](https://arxiv.org/abs/2508.05469)
- [Bits Leaked per Query (Kaneko & Baldwin)](https://arxiv.org/abs/2510.17000)
- [Understanding Agent Scaling via Diversity (Yang et al.)](https://arxiv.org/abs/2602.03794)
- [Don't Always Pick the Highest-Performing Model (Turkmen et al.)](https://arxiv.org/abs/2602.08003)
- [PEG: Incentivizing Truthful Language Models (Chen et al.)](https://arxiv.org/abs/2505.13636)
- [Correlated Errors in Large Language Models (Kim et al.)](https://arxiv.org/abs/2506.07962)
- [Multi-LLM Systems Exhibit Robust Semantic Collapse (Kong et al.)](https://arxiv.org/abs/2605.17193)
- [Representational Collapse in Multi-Agent LLM Committees (Patel)](https://arxiv.org/abs/2604.03809)
- [Strong Data-Processing Inequalities (Polyanskiy & Wu)](https://arxiv.org/abs/1508.06025)
- [Certified Robustness for Ensemble Models (Chen et al.)](https://arxiv.org/abs/2107.10873)
- [Boosting Randomized Smoothing with Variance Reduced Classifiers (Horvath et al.)](https://arxiv.org/abs/2106.06946)
- [A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness](https://arxiv.org/pdf/2603.06594)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72e7915d-641b-41d0-a180-1a65b952292a",
  "isSidechain": false,
  "requestId": "req_011CbDJ1NAjzg2GgX3MbBnDt",
  "type": "assistant",
  "uuid": "d89f31e0-e7ce-4aa4-bf2a-29574e288e95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G77QaroGbJEJCbgofSmHuB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2505,
      "cache_read_input_tokens": 30185,
      "output_tokens": 6852,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2505,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6852,
          "cache_read_input_tokens": 30185,
          "cache_creation_input_tokens": 2505,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2505
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

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Corr…",
  "leafUuid": "d89f31e0-e7ce-4aa4-bf2a-29574e288e95",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-judge LLM evaluation manipulation resistance bounds",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Corr…",
  "leafUuid": "d89f31e0-e7ce-4aa4-bf2a-29574e288e95",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-judge LLM evaluation manipulation resistance bounds",
  "sessionId": "99f8a341-e187-4e1a-bf75-1dd45e1a7c6e"
}
```

---
