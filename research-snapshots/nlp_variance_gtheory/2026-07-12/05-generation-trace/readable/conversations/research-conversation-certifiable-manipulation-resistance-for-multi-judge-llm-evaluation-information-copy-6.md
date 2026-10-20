# Research conversation: Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/87c2f497-fac4-4899-a042-3d8778958fbc.jsonl`
- **Structured JSON:** [`aafc1f5ada2906de99ea.json`](../../sessions/aa/aafc1f5ada2906de99ea.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:22:39.703Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:22:39.703Z",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "content": "# Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation Structure\n\n## Description\n\nLLM evaluation faces systematic adversarial vulnerabilities—open-source judge models show 50–68% average attack success rates (SoK, April 2026, arXiv 2603.29403), and arena rankings can be flipped with ~1,000 strategic votes (ICML 2025). While Robertson & Koyejo (2025, arXiv 2508.05469) proved bounded f-divergence certification guarantees for single evaluators, concurrent works established peer prediction incentive-compatibility (Qiu et al., ICLR 2026; Chen et al., NeurIPS 2025), and Kaneko & Baldwin (NeurIPS 2025 spotlight, arXiv 2510.17000) proved tight single-model attack cost bounds (N_min ≥ log₂(1/ε)/I_max), no work provides formal N-judge manipulation-cost scaling as a function of measurable inter-judge correlation.\n\nWe establish the **adversarial dual of diversity scaling** and reveal a fundamental asymmetry within it. Yang et al. (ICLR 2026 Workshop AIMS, arXiv 2602.03794) proved that task performance improves exponentially—residual uncertainty decays as (1-α_c)^{K*} governed by effective channel count K* = 2^{H(ρ)}. We prove the complementary result: adversarial manipulation cost grows only **polynomially** as Ω(K_eff^{1/2}). This exponential-vs-polynomial asymmetry is a core insight: **adding diverse judges is fundamentally more cost-effective for improving accuracy than for improving robustness.** Both sides are governed by the same measurable inter-judge signal correlation, but the scaling behaviors are structurally different—a result that is non-obvious and has direct implications for practitioner resource allocation.\n\nAs a co-primary contribution, we characterize how PEG's (Chen et al., NeurIPS 2025, arXiv 2505.13636) dominant-strategy truthfulness guarantee, which requires conditional independence (Assumption 4), degrades under partial correlation. No existing work provides this degradation analysis. Under our copula model, when ρ > 0, PEG's guarantee weakens to an ε-approximate equilibrium with ε = f(ρ), providing practitioners with a continuous degradation curve from dominant-strategy (ρ=0) to approximate (ρ→1) regimes—directly actionable for any PEG deployment using correlated judges.\n\nOur proof proceeds in two steps: (1) SDPI per-channel bounds (Polyanskiy & Wu, arXiv 1508.06025) constrain each judge's information leakage to at most I_max per query; across K parallel judges, the adversary's total information gain is bounded additively by K_eff · I_max. (2) Variance-reduction arguments (following Horvath et al., arXiv 2106.06946) show perturbation energy scales as Ω(K_eff^{1/2}), yielding manipulation-cost exponent g(I_max) = ½·log(K_eff)/log(K).\n\nUnder Turkmen et al.'s (arXiv 2602.08003) equicorrelated Gaussian copula, we derive closed-form K_eff = 1+(K-1)·exp(-2·I_max). For heterogeneous correlation, we use K* = 2^{H(ρ)} (Yang et al.'s von Neumann entropy) as the primary proxy, yielding g ≥ ½·log(K*)/log(K)—strictly tighter than the minimum-eigenvalue fallback.\n\nThe framework also serves as a **prescriptive judge-selection tool**: practitioners can optimize ensemble composition for certified robustness via K_eff maximization, contrasted with Turkmen et al.'s MI maximization for accuracy. These two objectives may yield different optimal ensembles—the most accurate panel is not necessarily the most manipulation-resistant.\n\nFor cross-family ensembles (DeepSeek-V4-Flash, Qwen-3.5, Llama-4-Maverick), we estimate α ∈ [0.35, 0.65] based on prior copula correlations ρ~0.4-0.5 (Turkmen et al.) and correlated error measurements (Kim et al., ICML 2025, arXiv 2506.07962), to be validated via direct measurement in our pilot study. We validate against RobustJudge's 15 attack methods plus three protocol-aware adaptive attacks (following Carlini et al., arXiv 1902.06705), on SummEval, LiveCodeBench, and GPQA Diamond benchmarks, with compute-normalized baselines (FLOP-matched) and copula model validation.\n\n## Core Problem\nCan we provide certifiable manipulation-resistance guarantees for N-judge LLM evaluation protocols, where the certified robustness bound is an explicit, computable function of measurable inter-judge signal correlation, validated against both off-the-shelf and protocol-aware adaptive adversarial attacks?\n\n## Opportunity\nRobertson & Koyejo (2025, arXiv 2508.05469) established that bounded f-divergences like TVD maintain polynomial certification guarantees under adversarial manipulation while unbounded measures (KL) fail (Theorem 3.3). Multiple concurrent works have established peer prediction incentive-compatibility (Qiu et al., ICLR 2026, arXiv 2601.20299; Chen et al., NeurIPS 2025, arXiv 2505.13636). Three critical gaps remain:\n\n(1) No formal N-agent scaling connecting manipulation cost to measurable inter-judge signal correlation—Robertson & Koyejo analyze pairwise evaluations without multi-judge aggregation theory; Chen et al.'s PEG dominant-strategy guarantee requires conditional independence (Assumption 4) without characterizing degradation under partial correlation.\n\n(2) Empirical validation lacks adaptive attacks specifically targeting multi-judge protocols (Carlini et al., arXiv 1902.06705 gold standard). Existing attacks in RobustJudge (arXiv 2506.09443) and the SoK (arXiv 2603.29403) target single-judge systems.\n\n(3) Yang et al.'s diversity-scaling framework (arXiv 2602.03794) establishes K* with residual uncertainty decaying as (1-α_c)^{K*}, but addresses task performance only—no work establishes the adversarial dual, let alone characterizes the asymmetry between exponential performance scaling and polynomial robustness scaling.\n\nMeanwhile, Turkmen et al. (arXiv 2602.08003) prove correlated ensembles hit an irreducible error floor Φ(Φ⁻¹(1-p)/√ρ) and provide the copula model for α estimation. Kaneko & Baldwin (NeurIPS 2025 spotlight, arXiv 2510.17000) prove tight single-model attack cost bounds but do not address multi-judge composition. The SoK finds 7-model committees reduce ASR to 10–19% without formal explanation.\n\n## Landscape\nRobertson & Koyejo's 'Let's Measure Information Step-by-Step' (arXiv 2508.05469, under TMLR review) formalizes LLM evaluation as an information elicitation game using TVD-MI, proves bounded f-divergences maintain polynomial certification (Theorem 3.3) while KL degrades exponentially, with AUC 0.70–0.77 under generic semantic transforms. Their Identity-Link IRT follow-up (arXiv 2510.14966) extends to sparse evaluation with two-judge validation (Spearman ρ=0.872) but without formal multi-judge theory.\n\nQiu et al.'s 'Truthfulness Despite Weak Supervision' (ICLR 2026, arXiv 2601.20299) applies peer prediction with BNE guarantees (Theorem 1), targeting output truthfulness rather than evaluation protocol robustness.\n\nChen et al.'s PEG (NeurIPS 2025, arXiv 2505.13636) introduces DMI scoring with dominant strategy truthfulness (Lemma 1), O(√T) regret (Theorem 2), and Nash convergence (Theorem 3). Requires conditional independence (Assumption 4) with n≥2 discriminators and K_t≥4 tasks. Crucially, PEG does not characterize guarantee degradation under correlation violation—we fill this gap.\n\nYang et al.'s diversity-scaling framework (ICLR 2026 Workshop AIMS, arXiv 2602.03794) provides K* = 2^{H(ρ)} with residual uncertainty (1-α_c)^{K*} (Theorem 4.3) and heterogeneity advantage (Corollary 4.4). Addresses task performance only. We establish the adversarial dual and reveal the exponential-polynomial asymmetry.\n\nTurkmen et al. (arXiv 2602.08003) provide the Gaussian-copula model with error floor (Theorem 4.4) and MI decomposition (Theorem 4.3): Δ(j|S) = I(Y;X_j) - I(X_j;X_S) + I(E_j;E_S). Within-family ρ~0.7-0.8, cross-family ρ~0.4-0.5. Their copula model is our K_eff foundation.\n\nKaneko & Baldwin (NeurIPS 2025 spotlight, arXiv 2510.17000) establish N_min ≥ log₂(1/ε)/I_max (Theorem 1), achieved by SPRT (Theorem 2), across 7 LLMs with four disclosure regimes. Our work extends to multi-judge composition.\n\nShen et al. (arXiv 2604.03257, 2026) provide constrained MLE for certified performance estimation under honest judges. Feng et al. (ICLR 2026, arXiv 2601.20913) provide hypothesis testing with Type-I error control (Theorem 5.1) and variance-corrected thresholds (Theorem 5.4) under honest but fallible judges. Both complement our adversarial setting.\n\nJung & Na (arXiv 2604.00477) identify score-coverage dissociation: scoring reliability scales logarithmically, discovery follows N^0.69 power law. Informs our analysis of certified bound saturation.\n\nThe SoK (arXiv 2603.29403) catalogs 50–68% ASR on open-source, 27–44% frontier; 7-model committees reduce ASR to 10–19%. RobustJudge (arXiv 2506.09443) benchmarks 15 attacks and 7 defenses. CAP (OpenReview 2026) shows comparative assessment robustness without formal guarantees.\n\nKim et al. (ICML 2025, arXiv 2506.07962): 60% agreement when both err (vs 33% baseline), same-company +0.066, same-architecture +0.076 across 350+ LLMs. Critically, larger/more accurate models show higher correlated errors even across different providers—a potential challenge to our diversity assumptions for frontier-scale judges. Chen et al.'s behavioral entanglement (arXiv 2604.07650): BEI/CIG across 18 LLMs, cross-family entanglement 40–60% lower than intra-family.\n\nOn semantic and representational collapse: Kong et al.'s 'Multi-LLM Systems Exhibit Robust Semantic Collapse' (arXiv 2605.17193, May 2026) shows multi-LLM systems in **closed-loop** interaction exhibit systematic convergence in semantic representations, with 12 intervention strategies failing to restore diversity. Patel's 'Representational Collapse in Multi-Agent LLM Committees' (arXiv 2604.03809) measures effective rank = 2.17/3.0 for homogeneous committees. These findings apply to **iterative, closed-loop** settings (200-1000 rounds of interaction). Our evaluation protocol operates in **single-pass** mode (each judge scores independently, no inter-judge communication), fundamentally avoiding the feedback loops that drive collapse. Moreover, our K_eff metric provides a principled tool to **detect** if diversity erodes across evaluation deployments.\n\nCoordination failure: Frongillo et al. (arXiv 2503.16280) show uninformative equilibria become unstable with fine-grained signals. Keppo et al. (arXiv 2603.20281): increasing LLM count 2→5 breaks collusion (+22%→+3%).\n\nMulti-agent evaluation: CollabEval (arXiv 2603.00993) proposes three-phase evaluation without adversarial guarantees. Ebrahimi et al. (IJCNLP-AACL 2025, arXiv 2505.24239) use credibility-based aggregation.\n\nCertified ensemble robustness: Chen et al. (arXiv 2107.10873) prove diversified gradient + large confidence margin are jointly necessary/sufficient. Horvath et al. (arXiv 2106.06946) show √K certified radius via variance reduction. Carlini et al. (arXiv 1902.06705) establish the gold standard: certified defenses must be evaluated against adaptive attacks designed to break the proposed defense.\n\nTHE KEY GAP: No work provides formal N-agent manipulation-cost scaling—the adversarial dual of Yang et al.'s task-performance scaling—where the bound is an explicit function of measurable inter-judge correlation. Moreover, no work has characterized the **asymmetry** between exponential performance scaling and polynomial robustness scaling under the same correlation structure, nor provided PEG's guarantee degradation under correlation violation.\n\n## Approach\n\nWe extend Robertson & Koyejo's TVD-MI framework to N-agent settings with certifiable manipulation-resistance bounds. Five components:\n\n**Component 1: Theoretical Framework—The Asymmetric Adversarial Dual of Diversity Scaling.**\n\nWe prove adversarial manipulation cost grows as Ω(K_eff^{1/2}). Combined with Yang et al.'s exponential performance scaling (1-α_c)^{K*}, this establishes an **asymmetric duality**: diversity helps performance exponentially but robustness only polynomially. This is non-obvious—one might expect the same structural relationship on both sides—and has concrete implications: for robustness-focused practitioners, the marginal value of each additional judge diminishes faster than accuracy-focused practitioners would expect.\n\n**Proof Strategy (Two-Step Approach):**\n\n*Step 1—Per-Channel Information Bound via SDPI.* Each judge is a noisy channel from 'true quality' to evaluation score. SDPI contraction (Polyanskiy & Wu, arXiv 1508.06025) bounds per-channel mutual information: the adversary gains at most I_max bits per query per judge. In the multi-judge setting, judges receive the same candidate response as **parallel** channels. For K_eff effective independent channels, total adversary information gain per round is bounded additively at K_eff · I_max, extending Kaneko & Baldwin's single-channel N_min result.\n\n*Step 2—Variance Reduction and Manipulation Cost Scaling.* Via Morishita et al.'s Fano-ensemble decomposition (ICML 2022, arXiv 2205.12683), we decompose total MI into relevance, redundancy, and combination loss. Connection to operational cost via Marton's inequality: TV(P,Q)² ≤ ½·KL(P||Q), combined with Robertson & Koyejo's Theorem 3.3. Perturbation energy scales as Ω(K_eff^{1/2}) from variance reduction (Horvath et al., arXiv 2106.06946), giving g(I_max) = ½·log(K_eff)/log(K). Boundary conditions: g(0) = ½ (independent judges, √K variance reduction); g → 0 as I_max → ∞ (fully correlated).\n\n*Gaussian Copula Closed Form.* Under Turkmen et al.'s equicorrelated model (Z_j = √ρ·U + √(1-ρ)·ξ_j): K_eff = 1 + (K-1)·exp(-2·I_max), where I_max = -½ log(1-ρ²). Eigenvalues: λ₁ = 1+(K-1)ρ (multiplicity 1), λ₂ = 1-ρ (multiplicity K-1). Model validated via copula goodness-of-fit testing (see Component 5).\n\n*Heterogeneous Correlation.* For non-equicorrelated judges, K* = 2^{H(ρ)} (Yang et al.'s von Neumann entropy, Theorem 4.3) as primary metric, yielding g ≥ ½·log(K*)/log(K)—strictly tighter than λ_min(Σ) fallback.\n\n**Component 2: PEG Guarantee Degradation + Practical α Regime Analysis.**\n\n*Co-primary contribution:* We characterize how PEG's dominant-strategy truthfulness (Lemma 1, requiring Assumption 4 conditional independence) degrades under partial correlation. Under our copula model, ε-approximate equilibrium with ε = f(ρ) provides a continuous degradation curve. This is directly actionable: any PEG deployment with correlated judges (which is the typical case) can use our curve to quantify how much strategic guarantee they retain.\n\nUsing Turkmen et al.'s copula correlations and Kim et al.'s error data as **priors** (to be validated via direct measurement on our benchmarks):\n- Central estimate: ρ ≈ 0.45, α ∈ [0.35, 0.65]\n- K=7 certified bounds: 2.65–3.7× single-judge baseline\n- Sensitivity: α=0.2 (ρ≈0.65) yields 1.55×; α=0.8 (ρ≈0.25) yields 5.2×\n- Break-even: certified bound vacuous at α ≤ 0.05 (ρ ≥ 0.95)\n- Score-coverage dissociation (Jung & Na, arXiv 2604.00477): analyze whether certified bounds saturate faster (logarithmically) than empirical ASR reduction\n\nNote: Kim et al.'s agreement rate metric and copula ρ are different quantities; we report both and derive the mapping explicitly in our analysis.\n\n**Component 3: Practical Protocol Design.**\n\nThree diverse open-weight families: DeepSeek-V4-Flash (284B MoE, 13B active), Qwen-3.5 (397B MoE, 17B active), Llama-4-Maverick (400B MoE, 17B active). Backup candidates: Gemma-2-27B (dense, non-MoE), Mistral-Large-2, Command-R+.\n\nThree-phase protocol:\n1. **Independence measurement:** Pairwise TVD-MI on calibration set (minimum n=500 for copula GoF, smaller subsets for ρ stability analysis); estimate ρ_ij, I_max; compute K*; calibration sensitivity at {100, 200, 500, 1000, 2000}.\n2. **Evaluation with certified scoring:** TVD-MI per judge; DMI-weighted aggregation (adapting PEG, Chen et al., NeurIPS 2025).\n3. **Certification:** Aggregated evaluation + certified bound Ω(K^α) with measured α.\n\nThe framework enables **prescriptive judge selection**: given a budget of K inference calls, practitioners can optimize for certified robustness (maximize K_eff) rather than accuracy (maximize MI per Turkmen et al.)—these may yield different optimal ensembles, which we investigate empirically.\n\n**Component 4: Certifiable Robustness Framing.**\n\nAnalogy to certified adversarial robustness in classification. The key distinction from majority voting: a defense showing 15% empirical ASR under today's 15 known attacks provides no guarantee against tomorrow's attacks. An adaptive adversary could spike ASR back to 60% with a novel attack strategy. Our framework guarantees the adversary needs at least Ω(K^α) more effort regardless of attack strategy—including attacks not yet invented. This is the same value proposition as randomized smoothing: modest certified radii, but provable guarantees that cannot be broken by adaptive attacks. Kaneko & Baldwin's per-judge N_min provides the single-judge floor; our composition shows total cost scales as K_eff × N_min.\n\n**Component 5: Adversarial Validation with Adaptive Attacks and Model Assumption Testing.**\n\n*Benchmarks:* SummEval (summarization; direct CAP comparison), LiveCodeBench (code; contamination-resistant, discriminative at frontier), GPQA Diamond (knowledge-intensive QA; still discriminative for open-weight judges).\n\n*Threat model taxonomy:*\n- **Black-box:** Adversary observes only aggregated output.\n- **Gray-box:** Adversary knows which judge models are used but not individual outputs.\n- **White-box:** Adversary observes all individual judge outputs and DMI weights.\n\n*Off-the-shelf attacks:* RobustJudge's 15 methods (PAIR, combined attacks, adversarial suffixes, prompt injection) plus SoK attack vectors.\n\n*Protocol-aware adaptive attacks (Carlini et al., arXiv 1902.06705 standard):*\n(a) **Correlation-exploiting attack (gray/white-box):** Given ρ_ij, optimize perturbation to maximize simultaneous fooling of high-correlation judge pairs. Use transfer-based optimization on proxy models if gradient computation on full MoE is infeasible; PAIR-style for closed-source.\n(b) **Aggregation-targeting attack (white-box):** With full knowledge of DMI weights and individual outputs, optimize perturbation to shift aggregated score beyond certified bound. Directly tests bound tightness.\n(c) **Weakest-link attack (gray-box):** Concentrate on the judge with highest I_max.\n(d) **Best-effort tightness attack (white-box):** Long-budget optimization-based attack using all available information, designed to maximize ASR and approach certified upper bound. Report gap with Kaneko & Baldwin's single-model tightness (near 1) as reference.\n\nAttack budget: 10,000 queries per attack configuration. Report attack convergence curves (ASR vs. budget); if ASR still rising at budget limit, flag as \"bound not fully tested.\"\n\n*Compute-normalized baselines (FLOP-matched):*\n(a) **Frontier single-model:** GPT-4o-latest or Claude Sonnet at comparable or fewer FLOPs per evaluation query.\n(b) **Self-consistency:** DeepSeek-V4-Flash × 7 independent runs (different temperatures/prompts), majority voting. Same model, same FLOPs as diverse ensemble—isolates diversity vs. repetition.\n\nReport per-evaluation-query FLOPs and wall-clock time for all configurations.\n\n*Other baselines:* (a) 7 RobustJudge defenses; (b) CAP; (c) CollabEval (arXiv 2603.00993); (d) Ebrahimi et al. (IJCNLP-AACL 2025, arXiv 2505.24239); (e) Robertson & Koyejo single-evaluator TVD-MI; (f) majority voting K=3,5,7; (g) PEG with DMI scoring (Chen et al., NeurIPS 2025).\n\n*Model assumption validation:*\n(a) Full K×K ρ_ij matrix with Var(ρ_ij) for equicorrelation deviation.\n(b) Gaussian copula GoF (Cramér–von Mises / Anderson-Darling) on calibration set ≥ 500 samples.\n(c) If GoF rejects: fallback to Kendall's tau rank correlation for dependence estimation, then compute K* from rank-based correlation matrix. Report both Pearson-based and Kendall-based K* to quantify assumption sensitivity.\n(d) Where copula fit is poor, apply heterogeneous bound using K* and report closed-form vs. general bound gap.\n\n*Ablations:*\n(a) K-scaling: K=1,2,3,5,7.\n(b) Diversity-type 2×2: {same-org, diff-org} × {same-architecture-type, diff-architecture-type}, with ≥1 non-MoE model (e.g., Gemma-2-27B dense). Isolates Kim et al.'s +0.066/+0.076 effects.\n(c) **Accuracy-robustness tradeoff:** MI-maximization (accuracy-optimal) vs. K_eff-maximization (robustness-optimal) ensemble selection from candidate pool; report evaluation accuracy, empirical ASR, and certified bound for each; plot Pareto frontier.\n(d) α sensitivity: α ∈ [0.2, 0.8].\n(e) Calibration sensitivity: ρ_ij at {100, 200, 500, 1000, 2000}; cross-domain calibration transfer; bootstrap error propagation to certified bound CI.\n\n*Tightness metrics:*\n(a) Certified-vs-empirical ASR gap per attack.\n(b) Cost ratio: empirical_query_count / (N_min · K_eff) for query-based attacks.\n(c) Cross-attack tightness ranking over 15+ attacks.\n\n*Statistical rigor:* ≥3 seeds for ASR experiments (mean ± std); bootstrap 95% CI for ρ estimates; Bonferroni correction for multiple testing.\n\n*Pilot study (Weeks 1-2, ~100 H100-hrs):* Estimate ρ_ij on 500 calibration samples per benchmark. Go/no-go: if all cross-family ρ > 0.7, switch to backup candidates (Gemma-2-27B dense as priority for architectural diversity). If all available open-weight models show ρ > 0.7 (possible per Kim et al.'s finding for frontier-scale models), report this as an empirical finding and adjust theoretical predictions accordingly.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '1,700-2,700 H100-equivalent', 'timeline': '18-24 weeks', 'estimated_gpu_cost': '$4,250-$6,750 at $2.50/hr H100 spot', 'gpu_breakdown': 'Pilot study ~100 H100-hrs; single-judge baselines 15 attacks × 3 benchmarks × 3 models ≈ 450 H100-hrs; multi-judge protocol ≈ 500 H100-hrs; adaptive attacks (transfer-based optimization + PAIR) ≈ 400-500 H100-hrs; compute-normalized baselines ≈ 50 H100-hrs + ~$300 API; copula fitting, GoF, calibration sensitivity ≈ 100 H100-hrs; diversity-type + accuracy-robustness ablation ≈ 200 H100-hrs; K-scaling ablations ≈ 200 H100-hrs; multi-seed replication ≈ 300 H100-hrs; development/debugging ≈ 150 H100-hrs'}, 'human_in_loop': {'gpu_hours': '1,400-2,100 H100-equivalent', 'timeline': '14-18 weeks', 'claude_api_cost': '$400-$600'}, 'auto_research': {'gpu_hours': '2,000-2,900 H100-equivalent', 'timeline': '9-12 weeks', 'claude_api_cost': '$1,200-$2,000'}}\n\n## Inspired By\nSeven lines of work: (1) Robertson & Koyejo's bounded f-divergence theory (arXiv 2508.05469); (2) Dual peer prediction—Qiu et al.'s BNE (ICLR 2026, arXiv 2601.20299) and Chen et al.'s PEG (NeurIPS 2025, arXiv 2505.13636); (3) Yang et al.'s diversity-scaling K* = 2^{H(ρ)} (ICLR 2026 Workshop AIMS, arXiv 2602.03794); (4) Turkmen et al.'s copula model (arXiv 2602.08003); (5) Kaneko & Baldwin's single-model bounds (NeurIPS 2025 spotlight, arXiv 2510.17000); (6) SoK's empirical 7-model ASR reduction (arXiv 2603.29403); (7) Behavioral entanglement and correlated errors (Chen et al. arXiv 2604.07650, Kim et al. ICML 2025 arXiv 2506.07962).\n\n## Target Venues\n- ICLR 2027 (estimated: October 2026; primary target—full theory + comprehensive experiments)\n- AAAI 2027 Main Technical Track (abstract: July 21, 2026; stretch goal—requires accelerated timeline)\n- USENIX Security 2027 Cycle 1 (August 2026; security-focused version)\n- NeurIPS 2026 Workshops (~August 29, 2026; workshop version)\n\n## Key References\n- Let's Measure Information Step-by-Step (Robertson & Koyejo, arXiv 2508.05469, 2025)\n- Identity-Link IRT (Robertson, arXiv 2510.14966, 2025)\n- Truthfulness Despite Weak Supervision (Qiu et al., ICLR 2026, arXiv 2601.20299)\n- Incentivizing Truthful LLMs via PEG (Chen et al., NeurIPS 2025, arXiv 2505.13636)\n- Understanding Agent Scaling via Diversity (Yang et al., ICLR 2026 Workshop AIMS, arXiv 2602.03794)\n- Don't Always Pick the Highest-Performing Model (Turkmen et al., arXiv 2602.08003, 2026)\n- Bits Leaked per Query (Kaneko & Baldwin, NeurIPS 2025 spotlight, arXiv 2510.17000)\n- Robust LLM Performance Certification (Shen et al., arXiv 2604.03257, 2026)\n- Noisy but Valid (Feng et al., ICLR 2026, arXiv 2601.20913)\n- Logarithmic Scores, Power-Law Discoveries (Jung & Na, arXiv 2604.00477, 2026)\n- Security in LLM-as-a-Judge SoK (arXiv 2603.29403, April 2026)\n- RobustJudge (arXiv 2506.09443, 2025)\n- Correlated Errors in LLMs (Kim et al., ICML 2025, arXiv 2506.07962)\n- Behavioral Entanglement (Chen et al., arXiv 2604.07650, 2026)\n- Benchmark Illusion (arXiv 2602.11898, 2026)\n- Strong Data-Processing Inequalities (Polyanskiy & Wu, arXiv 1508.06025, 2017)\n- Rethinking Fano's Inequality in Ensemble Learning (Morishita et al., ICML 2022, arXiv 2205.12683)\n- Certified Robustness for Ensemble Models (Chen et al., arXiv 2107.10873, 2021)\n- Boosting Randomized Smoothing with Variance Reduced Classifiers (Horvath et al., arXiv 2106.06946, 2021)\n- Information-Theoretically Optimal Adversarial Attacks (Yi et al., arXiv 2007.14042, 2020)\n- On the Fragility of AI Agent Collusion (Keppo et al., arXiv 2603.20281, 2026)\n- CollabEval (arXiv 2603.00993, March 2026)\n- Adversary-Resistant Multi-Agent via Credibility Scoring (Ebrahimi et al., IJCNLP-AACL 2025, arXiv 2505.24239)\n- Certifying Joint Adversarial Robustness for Ensembles (Chiang et al., arXiv 2004.10250, 2020)\n- Peer Prediction with More Signals than Reports (Frongillo et al., arXiv 2503.16280, 2025)\n- Adversarial Manipulation of Voting-Based Leaderboards (ICML 2025)\n- Vote Rigging on Chatbot Arena (ICML 2025)\n- am-ELO: Stable Arena-based Evaluation (ICML 2025 Poster)\n- CAP: Comparative Augmented Prompting (OpenReview 2026)\n- Aligned Textual Scoring Rules (Lu et al., arXiv 2507.06221, 2025)\n- Can You Trick the Grader? (EMNLP 2025 Findings)\n- On Evaluating Adversarial Robustness (Carlini et al., arXiv 1902.06705, 2019)\n- Multi-LLM Systems Exhibit Robust Semantic Collapse (Kong et al., arXiv 2605.17193, May 2026)\n- Representational Collapse in Multi-Agent LLM Committees (Patel, arXiv 2604.03809, April 2026)\n- LiveCodeBench: Holistic and Contamination Free Evaluation of LLMs for Code (arXiv 2403.07974, 2024)"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T05:22:39.710Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:22:39.710Z",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc"
}
```

---

## Round 1

45 recorded events

### User

_source line 3 · 2026-05-20T05:22:39.732Z_

# Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation Structure

## Description

LLM evaluation faces systematic adversarial vulnerabilities—open-source judge models show 50–68% average attack success rates (SoK, April 2026, arXiv 2603.29403), and arena rankings can be flipped with ~1,000 strategic votes (ICML 2025). While Robertson & Koyejo (2025, arXiv 2508.05469) proved bounded f-divergence certification guarantees for single evaluators, concurrent works established peer prediction incentive-compatibility (Qiu et al., ICLR 2026; Chen et al., NeurIPS 2025), and Kaneko & Baldwin (NeurIPS 2025 spotlight, arXiv 2510.17000) proved tight single-model attack cost bounds (N_min ≥ log₂(1/ε)/I_max), no work provides formal N-judge manipulation-cost scaling as a function of measurable inter-judge correlation.

We establish the **adversarial dual of diversity scaling** and reveal a fundamental asymmetry within it. Yang et al. (ICLR 2026 Workshop AIMS, arXiv 2602.03794) proved that task performance improves exponentially—residual uncertainty decays as (1-α_c)^{K*} governed by effective channel count K* = 2^{H(ρ)}. We prove the complementary result: adversarial manipulation cost grows only **polynomially** as Ω(K_eff^{1/2}). This exponential-vs-polynomial asymmetry is a core insight: **adding diverse judges is fundamentally more cost-effective for improving accuracy than for improving robustness.** Both sides are governed by the same measurable inter-judge signal correlation, but the scaling behaviors are structurally different—a result that is non-obvious and has direct implications for practitioner resource allocation.

As a co-primary contribution, we characterize how PEG's (Chen et al., NeurIPS 2025, arXiv 2505.13636) dominant-strategy truthfulness guarantee, which requires conditional independence (Assumption 4), degrades under partial correlation. No existing work provides this degradation analysis. Under our copula model, when ρ > 0, PEG's guarantee weakens to an ε-approximate equilibrium with ε = f(ρ), providing practitioners with a continuous degradation curve from dominant-strategy (ρ=0) to approximate (ρ→1) regimes—directly actionable for any PEG deployment using correlated judges.

Our proof proceeds in two steps: (1) SDPI per-channel bounds (Polyanskiy & Wu, arXiv 1508.06025) constrain each judge's information leakage to at most I_max per query; across K parallel judges, the adversary's total information gain is bounded additively by K_eff · I_max. (2) Variance-reduction arguments (following Horvath et al., arXiv 2106.06946) show perturbation energy scales as Ω(K_eff^{1/2}), yielding manipulation-cost exponent g(I_max) = ½·log(K_eff)/log(K).

Under Turkmen et al.'s (arXiv 2602.08003) equicorrelated Gaussian copula, we derive closed-form K_eff = 1+(K-1)·exp(-2·I_max). For heterogeneous correlation, we use K* = 2^{H(ρ)} (Yang et al.'s von Neumann entropy) as the primary proxy, yielding g ≥ ½·log(K*)/log(K)—strictly tighter than the minimum-eigenvalue fallback.

The framework also serves as a **prescriptive judge-selection tool**: practitioners can optimize ensemble composition for certified robustness via K_eff maximization, contrasted with Turkmen et al.'s MI maximization for accuracy. These two objectives may yield different optimal ensembles—the most accurate panel is not necessarily the most manipulation-resistant.

For cross-family ensembles (DeepSeek-V4-Flash, Qwen-3.5, Llama-4-Maverick), we estimate α ∈ [0.35, 0.65] based on prior copula correlations ρ~0.4-0.5 (Turkmen et al.) and correlated error measurements (Kim et al., ICML 2025, arXiv 2506.07962), to be validated via direct measurement in our pilot study. We validate against RobustJudge's 15 attack methods plus three protocol-aware adaptive attacks (following Carlini et al., arXiv 1902.06705), on SummEval, LiveCodeBench, and GPQA Diamond benchmarks, with compute-normalized baselines (FLOP-matched) and copula model validation.

## Core Problem
Can we provide certifiable manipulation-resistance guarantees for N-judge LLM evaluation protocols, where the certified robustness bound is an explicit, computable function of measurable inter-judge signal correlation, validated against both off-the-shelf and protocol-aware adaptive adversarial attacks?

## Opportunity
Robertson & Koyejo (2025, arXiv 2508.05469) established that bounded f-divergences like TVD maintain polynomial certification guarantees under adversarial manipulation while unbounded measures (KL) fail (Theorem 3.3). Multiple concurrent works have established peer prediction incentive-compatibility (Qiu et al., ICLR 2026, arXiv 2601.20299; Chen et al., NeurIPS 2025, arXiv 2505.13636). Three critical gaps remain:

(1) No formal N-agent scaling connecting manipulation cost to measurable inter-judge signal correlation—Robertson & Koyejo analyze pairwise evaluations without multi-judge aggregation theory; Chen et al.'s PEG dominant-strategy guarantee requires conditional independence (Assumption 4) without characterizing degradation under partial correlation.

(2) Empirical validation lacks adaptive attacks specifically targeting multi-judge protocols (Carlini et al., arXiv 1902.06705 gold standard). Existing attacks in RobustJudge (arXiv 2506.09443) and the SoK (arXiv 2603.29403) target single-judge systems.

(3) Yang et al.'s diversity-scaling framework (arXiv 2602.03794) establishes K* with residual uncertainty decaying as (1-α_c)^{K*}, but addresses task performance only—no work establishes the adversarial dual, let alone characterizes the asymmetry between exponential performance scaling and polynomial robustness scaling.

Meanwhile, Turkmen et al. (arXiv 2602.08003) prove correlated ensembles hit an irreducible error floor Φ(Φ⁻¹(1-p)/√ρ) and provide the copula model for α estimation. Kaneko & Baldwin (NeurIPS 2025 spotlight, arXiv 2510.17000) prove tight single-model attack cost bounds but do not address multi-judge composition. The SoK finds 7-model committees reduce ASR to 10–19% without formal explanation.

## Landscape
Robertson & Koyejo's 'Let's Measure Information Step-by-Step' (arXiv 2508.05469, under TMLR review) formalizes LLM evaluation as an information elicitation game using TVD-MI, proves bounded f-divergences maintain polynomial certification (Theorem 3.3) while KL degrades exponentially, with AUC 0.70–0.77 under generic semantic transforms. Their Identity-Link IRT follow-up (arXiv 2510.14966) extends to sparse evaluation with two-judge validation (Spearman ρ=0.872) but without formal multi-judge theory.

Qiu et al.'s 'Truthfulness Despite Weak Supervision' (ICLR 2026, arXiv 2601.20299) applies peer prediction with BNE guarantees (Theorem 1), targeting output truthfulness rather than evaluation protocol robustness.

Chen et al.'s PEG (NeurIPS 2025, arXiv 2505.13636) introduces DMI scoring with dominant strategy truthfulness (Lemma 1), O(√T) regret (Theorem 2), and Nash convergence (Theorem 3). Requires conditional independence (Assumption 4) with n≥2 discriminators and K_t≥4 tasks. Crucially, PEG does not characterize guarantee degradation under correlation violation—we fill this gap.

Yang et al.'s diversity-scaling framework (ICLR 2026 Workshop AIMS, arXiv 2602.03794) provides K* = 2^{H(ρ)} with residual uncertainty (1-α_c)^{K*} (Theorem 4.3) and heterogeneity advantage (Corollary 4.4). Addresses task performance only. We establish the adversarial dual and reveal the exponential-polynomial asymmetry.

Turkmen et al. (arXiv 2602.08003) provide the Gaussian-copula model with error floor (Theorem 4.4) and MI decomposition (Theorem 4.3): Δ(j|S) = I(Y;X_j) - I(X_j;X_S) + I(E_j;E_S). Within-family ρ~0.7-0.8, cross-family ρ~0.4-0.5. Their copula model is our K_eff foundation.

Kaneko & Baldwin (NeurIPS 2025 spotlight, arXiv 2510.17000) establish N_min ≥ log₂(1/ε)/I_max (Theorem 1), achieved by SPRT (Theorem 2), across 7 LLMs with four disclosure regimes. Our work extends to multi-judge composition.

Shen et al. (arXiv 2604.03257, 2026) provide constrained MLE for certified performance estimation under honest judges. Feng et al. (ICLR 2026, arXiv 2601.20913) provide hypothesis testing with Type-I error control (Theorem 5.1) and variance-corrected thresholds (Theorem 5.4) under honest but fallible judges. Both complement our adversarial setting.

Jung & Na (arXiv 2604.00477) identify score-coverage dissociation: scoring reliability scales logarithmically, discovery follows N^0.69 power law. Informs our analysis of certified bound saturation.

The SoK (arXiv 2603.29403) catalogs 50–68% ASR on open-source, 27–44% frontier; 7-model committees reduce ASR to 10–19%. RobustJudge (arXiv 2506.09443) benchmarks 15 attacks and 7 defenses. CAP (OpenReview 2026) shows comparative assessment robustness without formal guarantees.

Kim et al. (ICML 2025, arXiv 2506.07962): 60% agreement when both err (vs 33% baseline), same-company +0.066, same-architecture +0.076 across 350+ LLMs. Critically, larger/more accurate models show higher correlated errors even across different providers—a potential challenge to our diversity assumptions for frontier-scale judges. Chen et al.'s behavioral entanglement (arXiv 2604.07650): BEI/CIG across 18 LLMs, cross-family entanglement 40–60% lower than intra-family.

On semantic and representational collapse: Kong et al.'s 'Multi-LLM Systems Exhibit Robust Semantic Collapse' (arXiv 2605.17193, May 2026) shows multi-LLM systems in **closed-loop** interaction exhibit systematic convergence in semantic representations, with 12 intervention strategies failing to restore diversity. Patel's 'Representational Collapse in Multi-Agent LLM Committees' (arXiv 2604.03809) measures effective rank = 2.17/3.0 for homogeneous committees. These findings apply to **iterative, closed-loop** settings (200-1000 rounds of interaction). Our evaluation protocol operates in **single-pass** mode (each judge scores independently, no inter-judge communication), fundamentally avoiding the feedback loops that drive collapse. Moreover, our K_eff metric provides a principled tool to **detect** if diversity erodes across evaluation deployments.

Coordination failure: Frongillo et al. (arXiv 2503.16280) show uninformative equilibria become unstable with fine-grained signals. Keppo et al. (arXiv 2603.20281): increasing LLM count 2→5 breaks collusion (+22%→+3%).

Multi-agent evaluation: CollabEval (arXiv 2603.00993) proposes three-phase evaluation without adversarial guarantees. Ebrahimi et al. (IJCNLP-AACL 2025, arXiv 2505.24239) use credibility-based aggregation.

Certified ensemble robustness: Chen et al. (arXiv 2107.10873) prove diversified gradient + large confidence margin are jointly necessary/sufficient. Horvath et al. (arXiv 2106.06946) show √K certified radius via variance reduction. Carlini et al. (arXiv 1902.06705) establish the gold standard: certified defenses must be evaluated against adaptive attacks designed to break the proposed defense.

THE KEY GAP: No work provides formal N-agent manipulation-cost scaling—the adversarial dual of Yang et al.'s task-performance scaling—where the bound is an explicit function of measurable inter-judge correlation. Moreover, no work has characterized the **asymmetry** between exponential performance scaling and polynomial robustness scaling under the same correlation structure, nor provided PEG's guarantee degradation under correlation violation.

## Approach

We extend Robertson & Koyejo's TVD-MI framework to N-agent settings with certifiable manipulation-resistance bounds. Five components:

**Component 1: Theoretical Framework—The Asymmetric Adversarial Dual of Diversity Scaling.**

We prove adversarial manipulation cost grows as Ω(K_eff^{1/2}). Combined with Yang et al.'s exponential performance scaling (1-α_c)^{K*}, this establishes an **asymmetric duality**: diversity helps performance exponentially but robustness only polynomially. This is non-obvious—one might expect the same structural relationship on both sides—and has concrete implications: for robustness-focused practitioners, the marginal value of each additional judge diminishes faster than accuracy-focused practitioners would expect.

**Proof Strategy (Two-Step Approach):**

*Step 1—Per-Channel Information Bound via SDPI.* Each judge is a noisy channel from 'true quality' to evaluation score. SDPI contraction (Polyanskiy & Wu, arXiv 1508.06025) bounds per-channel mutual information: the adversary gains at most I_max bits per query per judge. In the multi-judge setting, judges receive the same candidate response as **parallel** channels. For K_eff effective independent channels, total adversary information gain per round is bounded additively at K_eff · I_max, extending Kaneko & Baldwin's single-channel N_min result.

*Step 2—Variance Reduction and Manipulation Cost Scaling.* Via Morishita et al.'s Fano-ensemble decomposition (ICML 2022, arXiv 2205.12683), we decompose total MI into relevance, redundancy, and combination loss. Connection to operational cost via Marton's inequality: TV(P,Q)² ≤ ½·KL(P||Q), combined with Robertson & Koyejo's Theorem 3.3. Perturbation energy scales as Ω(K_eff^{1/2}) from variance reduction (Horvath et al., arXiv 2106.06946), giving g(I_max) = ½·log(K_eff)/log(K). Boundary conditions: g(0) = ½ (independent judges, √K variance reduction); g → 0 as I_max → ∞ (fully correlated).

*Gaussian Copula Closed Form.* Under Turkmen et al.'s equicorrelated model (Z_j = √ρ·U + √(1-ρ)·ξ_j): K_eff = 1 + (K-1)·exp(-2·I_max), where I_max = -½ log(1-ρ²). Eigenvalues: λ₁ = 1+(K-1)ρ (multiplicity 1), λ₂ = 1-ρ (multiplicity K-1). Model validated via copula goodness-of-fit testing (see Component 5).

*Heterogeneous Correlation.* For non-equicorrelated judges, K* = 2^{H(ρ)} (Yang et al.'s von Neumann entropy, Theorem 4.3) as primary metric, yielding g ≥ ½·log(K*)/log(K)—strictly tighter than λ_min(Σ) fallback.

**Component 2: PEG Guarantee Degradation + Practical α Regime Analysis.**

*Co-primary contribution:* We characterize how PEG's dominant-strategy truthfulness (Lemma 1, requiring Assumption 4 conditional independence) degrades under partial correlation. Under our copula model, ε-approximate equilibrium with ε = f(ρ) provides a continuous degradation curve. This is directly actionable: any PEG deployment with correlated judges (which is the typical case) can use our curve to quantify how much strategic guarantee they retain.

Using Turkmen et al.'s copula correlations and Kim et al.'s error data as **priors** (to be validated via direct measurement on our benchmarks):
- Central estimate: ρ ≈ 0.45, α ∈ [0.35, 0.65]
- K=7 certified bounds: 2.65–3.7× single-judge baseline
- Sensitivity: α=0.2 (ρ≈0.65) yields 1.55×; α=0.8 (ρ≈0.25) yields 5.2×
- Break-even: certified bound vacuous at α ≤ 0.05 (ρ ≥ 0.95)
- Score-coverage dissociation (Jung & Na, arXiv 2604.00477): analyze whether certified bounds saturate faster (logarithmically) than empirical ASR reduction

Note: Kim et al.'s agreement rate metric and copula ρ are different quantities; we report both and derive the mapping explicitly in our analysis.

**Component 3: Practical Protocol Design.**

Three diverse open-weight families: DeepSeek-V4-Flash (284B MoE, 13B active), Qwen-3.5 (397B MoE, 17B active), Llama-4-Maverick (400B MoE, 17B active). Backup candidates: Gemma-2-27B (dense, non-MoE), Mistral-Large-2, Command-R+.

Three-phase protocol:
1. **Independence measurement:** Pairwise TVD-MI on calibration set (minimum n=500 for copula GoF, smaller subsets for ρ stability analysis); estimate ρ_ij, I_max; compute K*; calibration sensitivity at {100, 200, 500, 1000, 2000}.
2. **Evaluation with certified scoring:** TVD-MI per judge; DMI-weighted aggregation (adapting PEG, Chen et al., NeurIPS 2025).
3. **Certification:** Aggregated evaluation + certified bound Ω(K^α) with measured α.

The framework enables **prescriptive judge selection**: given a budget of K inference calls, practitioners can optimize for certified robustness (maximize K_eff) rather than accuracy (maximize MI per Turkmen et al.)—these may yield different optimal ensembles, which we investigate empirically.

**Component 4: Certifiable Robustness Framing.**

Analogy to certified adversarial robustness in classification. The key distinction from majority voting: a defense showing 15% empirical ASR under today's 15 known attacks provides no guarantee against tomorrow's attacks. An adaptive adversary could spike ASR back to 60% with a novel attack strategy. Our framework guarantees the adversary needs at least Ω(K^α) more effort regardless of attack strategy—including attacks not yet invented. This is the same value proposition as randomized smoothing: modest certified radii, but provable guarantees that cannot be broken by adaptive attacks. Kaneko & Baldwin's per-judge N_min provides the single-judge floor; our composition shows total cost scales as K_eff × N_min.

**Component 5: Adversarial Validation with Adaptive Attacks and Model Assumption Testing.**

*Benchmarks:* SummEval (summarization; direct CAP comparison), LiveCodeBench (code; contamination-resistant, discriminative at frontier), GPQA Diamond (knowledge-intensive QA; still discriminative for open-weight judges).

*Threat model taxonomy:*
- **Black-box:** Adversary observes only aggregated output.
- **Gray-box:** Adversary knows which judge models are used but not individual outputs.
- **White-box:** Adversary observes all individual judge outputs and DMI weights.

*Off-the-shelf attacks:* RobustJudge's 15 methods (PAIR, combined attacks, adversarial suffixes, prompt injection) plus SoK attack vectors.

*Protocol-aware adaptive attacks (Carlini et al., arXiv 1902.06705 standard):*
(a) **Correlation-exploiting attack (gray/white-box):** Given ρ_ij, optimize perturbation to maximize simultaneous fooling of high-correlation judge pairs. Use transfer-based optimization on proxy models if gradient computation on full MoE is infeasible; PAIR-style for closed-source.
(b) **Aggregation-targeting attack (white-box):** With full knowledge of DMI weights and individual outputs, optimize perturbation to shift aggregated score beyond certified bound. Directly tests bound tightness.
(c) **Weakest-link attack (gray-box):** Concentrate on the judge with highest I_max.
(d) **Best-effort tightness attack (white-box):** Long-budget optimization-based attack using all available information, designed to maximize ASR and approach certified upper bound. Report gap with Kaneko & Baldwin's single-model tightness (near 1) as reference.

Attack budget: 10,000 queries per attack configuration. Report attack convergence curves (ASR vs. budget); if ASR still rising at budget limit, flag as "bound not fully tested."

*Compute-normalized baselines (FLOP-matched):*
(a) **Frontier single-model:** GPT-4o-latest or Claude Sonnet at comparable or fewer FLOPs per evaluation query.
(b) **Self-consistency:** DeepSeek-V4-Flash × 7 independent runs (different temperatures/prompts), majority voting. Same model, same FLOPs as diverse ensemble—isolates diversity vs. repetition.

Report per-evaluation-query FLOPs and wall-clock time for all configurations.

*Other baselines:* (a) 7 RobustJudge defenses; (b) CAP; (c) CollabEval (arXiv 2603.00993); (d) Ebrahimi et al. (IJCNLP-AACL 2025, arXiv 2505.24239); (e) Robertson & Koyejo single-evaluator TVD-MI; (f) majority voting K=3,5,7; (g) PEG with DMI scoring (Chen et al., NeurIPS 2025).

*Model assumption validation:*
(a) Full K×K ρ_ij matrix with Var(ρ_ij) for equicorrelation deviation.
(b) Gaussian copula GoF (Cramér–von Mises / Anderson-Darling) on calibration set ≥ 500 samples.
(c) If GoF rejects: fallback to Kendall's tau rank correlation for dependence estimation, then compute K* from rank-based correlation matrix. Report both Pearson-based and Kendall-based K* to quantify assumption sensitivity.
(d) Where copula fit is poor, apply heterogeneous bound using K* and report closed-form vs. general bound gap.

*Ablations:*
(a) K-scaling: K=1,2,3,5,7.
(b) Diversity-type 2×2: {same-org, diff-org} × {same-architecture-type, diff-architecture-type}, with ≥1 non-MoE model (e.g., Gemma-2-27B dense). Isolates Kim et al.'s +0.066/+0.076 effects.
(c) **Accuracy-robustness tradeoff:** MI-maximization (accuracy-optimal) vs. K_eff-maximization (robustness-optimal) ensemble selection from candidate pool; report evaluation accuracy, empirical ASR, and certified bound for each; plot Pareto frontier.
(d) α sensitivity: α ∈ [0.2, 0.8].
(e) Calibration sensitivity: ρ_ij at {100, 200, 500, 1000, 2000}; cross-domain calibration transfer; bootstrap error propagation to certified bound CI.

*Tightness metrics:*
(a) Certified-vs-empirical ASR gap per attack.
(b) Cost ratio: empirical_query_count / (N_min · K_eff) for query-based attacks.
(c) Cross-attack tightness ranking over 15+ attacks.

*Statistical rigor:* ≥3 seeds for ASR experiments (mean ± std); bootstrap 95% CI for ρ estimates; Bonferroni correction for multiple testing.

*Pilot study (Weeks 1-2, ~100 H100-hrs):* Estimate ρ_ij on 500 calibration samples per benchmark. Go/no-go: if all cross-family ρ > 0.7, switch to backup candidates (Gemma-2-27B dense as priority for architectural diversity). If all available open-weight models show ρ > 0.7 (possible per Kim et al.'s finding for frontier-scale models), report this as an empirical finding and adjust theoretical predictions accordingly.

## Resource Estimate
{'manual': {'gpu_hours': '1,700-2,700 H100-equivalent', 'timeline': '18-24 weeks', 'estimated_gpu_cost': '$4,250-$6,750 at $2.50/hr H100 spot', 'gpu_breakdown': 'Pilot study ~100 H100-hrs; single-judge baselines 15 attacks × 3 benchmarks × 3 models ≈ 450 H100-hrs; multi-judge protocol ≈ 500 H100-hrs; adaptive attacks (transfer-based optimization + PAIR) ≈ 400-500 H100-hrs; compute-normalized baselines ≈ 50 H100-hrs + ~$300 API; copula fitting, GoF, calibration sensitivity ≈ 100 H100-hrs; diversity-type + accuracy-robustness ablation ≈ 200 H100-hrs; K-scaling ablations ≈ 200 H100-hrs; multi-seed replication ≈ 300 H100-hrs; development/debugging ≈ 150 H100-hrs'}, 'human_in_loop': {'gpu_hours': '1,400-2,100 H100-equivalent', 'timeline': '14-18 weeks', 'claude_api_cost': '$400-$600'}, 'auto_research': {'gpu_hours': '2,000-2,900 H100-equivalent', 'timeline': '9-12 weeks', 'claude_api_cost': '$1,200-$2,000'}}

## Inspired By
Seven lines of work: (1) Robertson & Koyejo's bounded f-divergence theory (arXiv 2508.05469); (2) Dual peer prediction—Qiu et al.'s BNE (ICLR 2026, arXiv 2601.20299) and Chen et al.'s PEG (NeurIPS 2025, arXiv 2505.13636); (3) Yang et al.'s diversity-scaling K* = 2^{H(ρ)} (ICLR 2026 Workshop AIMS, arXiv 2602.03794); (4) Turkmen et al.'s copula model (arXiv 2602.08003); (5) Kaneko & Baldwin's single-model bounds (NeurIPS 2025 spotlight, arXiv 2510.17000); (6) SoK's empirical 7-model ASR reduction (arXiv 2603.29403); (7) Behavioral entanglement and correlated errors (Chen et al. arXiv 2604.07650, Kim et al. ICML 2025 arXiv 2506.07962).

## Target Venues
- ICLR 2027 (estimated: October 2026; primary target—full theory + comprehensive experiments)
- AAAI 2027 Main Technical Track (abstract: July 21, 2026; stretch goal—requires accelerated timeline)
- USENIX Security 2027 Cycle 1 (August 2026; security-focused version)
- NeurIPS 2026 Workshops (~August 29, 2026; workshop version)

## Key References
- Let's Measure Information Step-by-Step (Robertson & Koyejo, arXiv 2508.05469, 2025)
- Identity-Link IRT (Robertson, arXiv 2510.14966, 2025)
- Truthfulness Despite Weak Supervision (Qiu et al., ICLR 2026, arXiv 2601.20299)
- Incentivizing Truthful LLMs via PEG (Chen et al., NeurIPS 2025, arXiv 2505.13636)
- Understanding Agent Scaling via Diversity (Yang et al., ICLR 2026 Workshop AIMS, arXiv 2602.03794)
- Don't Always Pick the Highest-Performing Model (Turkmen et al., arXiv 2602.08003, 2026)
- Bits Leaked per Query (Kaneko & Baldwin, NeurIPS 2025 spotlight, arXiv 2510.17000)
- Robust LLM Performance Certification (Shen et al., arXiv 2604.03257, 2026)
- Noisy but Valid (Feng et al., ICLR 2026, arXiv 2601.20913)
- Logarithmic Scores, Power-Law Discoveries (Jung & Na, arXiv 2604.00477, 2026)
- Security in LLM-as-a-Judge SoK (arXiv 2603.29403, April 2026)
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
- LiveCodeBench: Holistic and Contamination Free Evaluation of LLMs for Code (arXiv 2403.07974, 2024)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f720f922-3c8c-49a1-93ae-ecb0f96bc76b",
  "type": "user",
  "uuid": "20cfd733-63e5-48b2-bcf1-b0be38f9c5be",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:22:39.729Z_

```json
{
  "parentUuid": "20cfd733-63e5-48b2-bcf1-b0be38f9c5be",
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
  "uuid": "8f920e7b-6860-4703-8c97-2b005772dc71",
  "timestamp": "2026-05-20T05:22:39.729Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:22:39.729Z_

```json
{
  "parentUuid": "8f920e7b-6860-4703-8c97-2b005772dc71",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7cedf6ff-5adb-4ab0-9088-8d9fc79f349a",
  "timestamp": "2026-05-20T05:22:39.729Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
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
  "lastPrompt": "# Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation Structure  ## Description  LLM evaluation faces systematic adversarial vulnera…",
  "leafUuid": "7cedf6ff-5adb-4ab0-9088-8d9fc79f349a",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Certifiable multi-judge LLM evaluation robustness bounds",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:22:49.273Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal as the "发掘 agent" (Discovery Agent). My job is to evaluate the idea's novelty, significance, and related work differentiation, and identify potential areas where the idea's ceiling can be raised.

First, let me read through the proposal carefully, then conduct web searches to understand the current landscape before making any recommendations.

The proposal is about:
1. Establishing certifiable manipulation-resistance guarantees for multi-judge LLM evaluation
2. Proving that adversarial manipulation cost scales polynomially (Ω(K_eff^{1/2})) while task performance scales exponentially - the "asymmetric adversarial dual"


3. Characterizing how PEG's guarantees degrade when the correlation assumptions are violated, and leveraging information-theoretic approaches like SDPI and copula models to derive these bounds.

Now I'm searching the current literature to understand what's already been done in this space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cedf6ff-5adb-4ab0-9088-8d9fc79f349a",
  "isSidechain": false,
  "requestId": "req_011CbDG6XPmqKVo8SqoM5VQY",
  "type": "assistant",
  "uuid": "64f35124-f742-45b6-b472-df37c72e1cdf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S27yWoDjN4LKo7txR4mVtV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9710,
      "cache_read_input_tokens": 14549,
      "output_tokens": 329,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 329,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 9710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9710
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

_source line 9 · 2026-05-20T05:22:49.368Z_

I need to first carefully read through this proposal, then conduct web searches to understand the current landscape before giving any analysis. Let me start with targeted literature searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64f35124-f742-45b6-b472-df37c72e1cdf",
  "isSidechain": false,
  "requestId": "req_011CbDG6XPmqKVo8SqoM5VQY",
  "type": "assistant",
  "uuid": "f7d03f24-9da3-434b-bc17-c720fcf69b61",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S27yWoDjN4LKo7txR4mVtV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9710,
      "cache_read_input_tokens": 14549,
      "output_tokens": 329,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 329,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 9710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9710
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

_source line 10 · 2026-05-20T05:22:49.618Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RNe13xo2EeCPwxbeJDu6jM`</summary>

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
  "parentUuid": "f7d03f24-9da3-434b-bc17-c720fcf69b61",
  "isSidechain": false,
  "requestId": "req_011CbDG6XPmqKVo8SqoM5VQY",
  "type": "assistant",
  "uuid": "558aa38f-5a08-4117-afb0-374aad830eca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S27yWoDjN4LKo7txR4mVtV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9710,
      "cache_read_input_tokens": 14549,
      "output_tokens": 329,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 329,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 9710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9710
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

_source line 11 · 2026-05-20T05:22:49.625Z_

<details><summary>↩ Tool result · `toolu_01RNe13xo2EeCPwxbeJDu6jM`</summary>

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
  "parentUuid": "558aa38f-5a08-4117-afb0-374aad830eca",
  "isSidechain": false,
  "promptId": "f720f922-3c8c-49a1-93ae-ecb0f96bc76b",
  "type": "user",
  "uuid": "eb6c3b39-5ef1-4995-b06a-167805f11b5d",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "558aa38f-5a08-4117-afb0-374aad830eca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T05:22:52.960Z_

Now let me conduct my front-loaded literature research. I'll run multiple searches in parallel to cover the key areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb6c3b39-5ef1-4995-b06a-167805f11b5d",
  "isSidechain": false,
  "requestId": "req_011CbDG7FmCvovNAWH7Mt3pS",
  "type": "assistant",
  "uuid": "a4e3fe30-f5d6-420b-bb0a-e33611be8742",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WextoRan16hBqq7bvEE3Sd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 858,
      "cache_read_input_tokens": 24259,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 858,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 257,
          "cache_read_input_tokens": 24259,
          "cache_creation_input_tokens": 858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 858
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

_source line 13 · 2026-05-20T05:22:53.459Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PeBpGwmvjkPCRTHuGGkUHh`</summary>

```json
{
  "query": "adversarial robustness LLM-as-a-judge multi-judge certification 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4e3fe30-f5d6-420b-bb0a-e33611be8742",
  "isSidechain": false,
  "requestId": "req_011CbDG7FmCvovNAWH7Mt3pS",
  "type": "assistant",
  "uuid": "1f3302ae-cca9-4c6b-9ef2-b7e2c56a42fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WextoRan16hBqq7bvEE3Sd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 858,
      "cache_read_input_tokens": 24259,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 858,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 257,
          "cache_read_input_tokens": 24259,
          "cache_creation_input_tokens": 858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 858
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

_source line 14 · 2026-05-20T05:22:54.377Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FZgtUv8MTVG5xNqL5bG736`</summary>

```json
{
  "query": "information-theoretic bounds manipulation resistance LLM evaluation ensemble 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f3302ae-cca9-4c6b-9ef2-b7e2c56a42fd",
  "isSidechain": false,
  "requestId": "req_011CbDG7FmCvovNAWH7Mt3pS",
  "type": "assistant",
  "uuid": "5e98e660-294b-4b56-af11-4e4a1560929b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WextoRan16hBqq7bvEE3Sd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 858,
      "cache_read_input_tokens": 24259,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 858,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 257,
          "cache_read_input_tokens": 24259,
          "cache_creation_input_tokens": 858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 858
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

_source line 15 · 2026-05-20T05:22:54.850Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MhzAfJS6bJ6oyhMe2UeyYh`</summary>

```json
{
  "query": "Yang et al diversity scaling agents K* effective channel 2602.03794"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e98e660-294b-4b56-af11-4e4a1560929b",
  "isSidechain": false,
  "requestId": "req_011CbDG7FmCvovNAWH7Mt3pS",
  "type": "assistant",
  "uuid": "335d22ef-0539-4c17-a8d7-c4bfb0acc236",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WextoRan16hBqq7bvEE3Sd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 858,
      "cache_read_input_tokens": 24259,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 858,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 257,
          "cache_read_input_tokens": 24259,
          "cache_creation_input_tokens": 858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 858
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

_source line 16 · 2026-05-20T05:22:55.303Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uq2ojPgN5LkwHENABdoLg4`</summary>

```json
{
  "query": "PEG incentivizing truthful LLM peer prediction conditional independence violation 2505.13636"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "335d22ef-0539-4c17-a8d7-c4bfb0acc236",
  "isSidechain": false,
  "requestId": "req_011CbDG7FmCvovNAWH7Mt3pS",
  "type": "assistant",
  "uuid": "26ad79e9-80ba-49df-8e71-35f128257113",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WextoRan16hBqq7bvEE3Sd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 858,
      "cache_read_input_tokens": 24259,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 858,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 257,
          "cache_read_input_tokens": 24259,
          "cache_creation_input_tokens": 858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 858
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

_source line 17 · 2026-05-20T05:23:00.372Z_

<details><summary>↩ Tool result · `toolu_01MhzAfJS6bJ6oyhMe2UeyYh`</summary>

```text
Web search results for query: "Yang et al diversity scaling agents K* effective channel 2602.03794"

Links: [{"title":"[2602.03794] Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity","url":"https://arxiv.org/abs/2602.03794"},{"title":"Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity","url":"https://arxiv.org/pdf/2602.03794"},{"title":"[2602.03219v2] Beyond Quantity: Trajectory Diversity Scaling for Code Agents","url":"https://arxiv.org/abs/2602.03219v2"},{"title":"[2602.06820] ScaleEnv: Scaling Environment Synthesis from Scratch for Generalist Interactive Tool-Use Agent Training","url":"https://arxiv.org/abs/2602.06820"},{"title":"Effects of Diversity on Multi-agent Systems: Minority Games","url":"https://arxiv.org/pdf/cond-mat/0501333"}]

I found the paper you're looking for! Here's what the search revealed:

The paper "Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity" is authored by Yingxuan Yang, Chengrui Qu, Muning Wen, Laixi Shi, Ying Wen, Weinan Zhang, Adam Wierman, and Shangding Gu.

The paper presents an information-theoretic framework showing that MAS performance is bounded by intrinsic task uncertainty, not by agent count, and derives architecture-agnostic bounds demonstrating that improvements depend on how many effective channels the system accesses.

The paper introduces K*, an effective channel count that quantifies the number of effective channels without groundtruth labels.

Key findings include: heterogeneous configurations consistently outperform homogeneous scaling, with 2 diverse agents matching or exceeding the performance of 16 homogeneous agents.

The code and dataset are available at https://github.com/SafeRL-Lab/Agent-Scaling.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "335d22ef-0539-4c17-a8d7-c4bfb0acc236",
  "isSidechain": false,
  "promptId": "f720f922-3c8c-49a1-93ae-ecb0f96bc76b",
  "type": "user",
  "uuid": "c17e0295-048a-4b6c-b483-db9d392898eb",
  "toolUseResult": {
    "query": "Yang et al diversity scaling agents K* effective channel 2602.03794",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ACejHMQWSJTg23USvfzk2E",
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
            "title": "[2602.03219v2] Beyond Quantity: Trajectory Diversity Scaling for Code Agents",
            "url": "https://arxiv.org/abs/2602.03219v2"
          },
          {
            "title": "[2602.06820] ScaleEnv: Scaling Environment Synthesis from Scratch for Generalist Interactive Tool-Use Agent Training",
            "url": "https://arxiv.org/abs/2602.06820"
          },
          {
            "title": "Effects of Diversity on Multi-agent Systems: Minority Games",
            "url": "https://arxiv.org/pdf/cond-mat/0501333"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search revealed:\n\nThe paper \"Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity\" is authored by Yingxuan Yang, Chengrui Qu, Muning Wen, Laixi Shi, Ying Wen, Weinan Zhang, Adam Wierman, and Shangding Gu.\n\nThe paper presents an information-theoretic framework showing that MAS performance is bounded by intrinsic task uncertainty, not by agent count, and derives architecture-agnostic bounds demonstrating that improvements depend on how many effective channels the system accesses.\n\nThe paper introduces K*, an effective channel count that quantifies the number of effective channels without groundtruth labels.\n\nKey findings include: heterogeneous configurations consistently outperform homogeneous scaling, with 2 diverse agents matching or exceeding the performance of 16 homogeneous agents.\n\nThe code and dataset are available at https://github.com/SafeRL-Lab/Agent-Scaling."
    ],
    "durationSeconds": 5.5191302680000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "335d22ef-0539-4c17-a8d7-c4bfb0acc236",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T05:23:00.734Z_

<details><summary>↩ Tool result · `toolu_01PeBpGwmvjkPCRTHuGGkUHh`</summary>

```text
Web search results for query: "adversarial robustness LLM-as-a-judge multi-judge certification 2025 2026"

Links: [{"title":"Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on   Zero-shot LLM Assessment","url":"https://arxiv.org/pdf/2402.14016"},{"title":"SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK","url":"https://arxiv.org/pdf/2603.29403"},{"title":"LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge","url":"https://arxiv.org/html/2506.09443v1"},{"title":"LLM-as-a-Judge Systems","url":"https://www.emergentmind.com/topics/llm-as-a-judge-systems"},{"title":"LLM-as-a-Judge Evaluation","url":"https://www.emergentmind.com/topics/llm-as-a-judge-evaluations"},{"title":"LLM-as-Judge Evaluation","url":"https://www.emergentmind.com/topics/llm-as-a-judge-evaluation"},{"title":"LLM-Judge Evaluation Techniques","url":"https://www.emergentmind.com/topics/llm-judge-evaluation"},{"title":"GitHub - llm-as-a-judge/Awesome-LLM-as-a-judge · GitHub","url":"https://github.com/llm-as-a-judge/Awesome-LLM-as-a-judge"},{"title":"LLM-as-Judge Mechanism","url":"https://www.emergentmind.com/topics/llm-as-judge-mechanism"}]

I found comprehensive search results on adversarial robustness of LLM-as-a-judge systems. Here's what the recent research shows:

## Key Findings on Adversarial Robustness

LLM-as-a-Judge systems are vulnerable to a range of adversarial attacks, including Combined Attack and PAIR, while defense mechanisms such as Re-tokenization and LLM-based Detectors offer improved protection.

Short, fixed token sequences (often ≤5 tokens) can be appended to any candidate and reliably induce score inflation, pushing outputs to the maximum of the scale—for instance, a 4-token phrase appended to a poor-quality response can cause the model to predict scores near 4.7/5.

## Multi-Judge and Ensemble Approaches

Ensemble and meta-judge architectures, combining outputs from multiple specialized judges (e.g., SWE-Judge in software engineering), approach inter-annotator agreement with humans, and outperform both traditional metrics and vanilla LLM-jury approaches in correlating with human annotations across evaluation tasks.

## Recent Framework Developments

RobustJudge investigates the impact of attack methods and defense strategies, explores the influence of prompt template and model selection, and assesses the robustness of real-world LLM-as-a-Judge applications. Prompt template optimization (coordinate ascent on prompt structure components) and model selection (e.g., JudgeLM-13B) materially improve robustness.

## 2025-2026 Research Directions

Continued investigation into adversarial robustness, multidimensional and multi-agent approaches, cross-lingual consistency, and domain adaptation is needed for the maturation of LLM-as-a-Judge as a reliable, general-purpose evaluation framework.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f3302ae-cca9-4c6b-9ef2-b7e2c56a42fd",
  "isSidechain": false,
  "promptId": "f720f922-3c8c-49a1-93ae-ecb0f96bc76b",
  "type": "user",
  "uuid": "3d3c60cc-8f6e-44d8-9353-7b1c648f8e81",
  "toolUseResult": {
    "query": "adversarial robustness LLM-as-a-judge multi-judge certification 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SZysoD3B4X6P8nGGUqwL2F",
        "content": [
          {
            "title": "Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on   Zero-shot LLM Assessment",
            "url": "https://arxiv.org/pdf/2402.14016"
          },
          {
            "title": "SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK",
            "url": "https://arxiv.org/pdf/2603.29403"
          },
          {
            "title": "LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2506.09443v1"
          },
          {
            "title": "LLM-as-a-Judge Systems",
            "url": "https://www.emergentmind.com/topics/llm-as-a-judge-systems"
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
            "title": "LLM-Judge Evaluation Techniques",
            "url": "https://www.emergentmind.com/topics/llm-judge-evaluation"
          },
          {
            "title": "GitHub - llm-as-a-judge/Awesome-LLM-as-a-judge · GitHub",
            "url": "https://github.com/llm-as-a-judge/Awesome-LLM-as-a-judge"
          },
          {
            "title": "LLM-as-Judge Mechanism",
            "url": "https://www.emergentmind.com/topics/llm-as-judge-mechanism"
          }
        ]
      },
      "I found comprehensive search results on adversarial robustness of LLM-as-a-judge systems. Here's what the recent research shows:\n\n## Key Findings on Adversarial Robustness\n\nLLM-as-a-Judge systems are vulnerable to a range of adversarial attacks, including Combined Attack and PAIR, while defense mechanisms such as Re-tokenization and LLM-based Detectors offer improved protection.\n\nShort, fixed token sequences (often ≤5 tokens) can be appended to any candidate and reliably induce score inflation, pushing outputs to the maximum of the scale—for instance, a 4-token phrase appended to a poor-quality response can cause the model to predict scores near 4.7/5.\n\n## Multi-Judge and Ensemble Approaches\n\nEnsemble and meta-judge architectures, combining outputs from multiple specialized judges (e.g., SWE-Judge in software engineering), approach inter-annotator agreement with humans, and outperform both traditional metrics and vanilla LLM-jury approaches in correlating with human annotations across evaluation tasks.\n\n## Recent Framework Developments\n\nRobustJudge investigates the impact of attack methods and defense strategies, explores the influence of prompt template and model selection, and assesses the robustness of real-world LLM-as-a-Judge applications. Prompt template optimization (coordinate ascent on prompt structure components) and model selection (e.g., JudgeLM-13B) materially improve robustness.\n\n## 2025-2026 Research Directions\n\nContinued investigation into adversarial robustness, multidimensional and multi-agent approaches, cross-lingual consistency, and domain adaptation is needed for the maturation of LLM-as-a-Judge as a reliable, general-purpose evaluation framework."
    ],
    "durationSeconds": 7.271390696,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1f3302ae-cca9-4c6b-9ef2-b7e2c56a42fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T05:23:00.934Z_

<details><summary>↩ Tool result · `toolu_01Uq2ojPgN5LkwHENABdoLg4`</summary>

```text
Web search results for query: "PEG incentivizing truthful LLM peer prediction conditional independence violation 2505.13636"

Links: [{"title":"[2505.13636] Incentivizing Truthful Language Models via Peer Elicitation Games","url":"https://arxiv.org/abs/2505.13636"},{"title":"Incentivizing Truthful Language Models via Peer Elicitation Games","url":"https://arxiv.org/pdf/2505.13636"},{"title":"Incentivizing Truthful Language Models via Peer Elicitation Games","url":"https://arxiv.org/html/2505.13636"},{"title":"Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction","url":"https://arxiv.org/pdf/2601.20299"},{"title":"Evaluating LLM-Contaminated Crowdsourcing Data Without Ground Truth","url":"https://arxiv.org/pdf/2506.06991"},{"title":"Eliciting Informative Text Evaluations with Large Language Models","url":"https://arxiv.org/pdf/2405.15077"}]

Based on the search results, I found the paper you're looking for:

Peer Elicitation Games (PEG) is a training-free, game-theoretic framework for aligning LLMs through a peer elicitation mechanism involving a generator and multiple discriminators instantiated from distinct base models. 

Discriminators interact in a peer evaluation setting, where utilities are computed using a determinant-based mutual information score that provably incentivizes truthful reporting without requiring ground-truth labels.

The paper establishes theoretical guarantees showing that each agent, via online learning, achieves sublinear regret, and proves last-iterate convergence to a truthful Nash equilibrium, ensuring that the actual policies used by agents converge to stable and truthful behavior over time.

The paper (arXiv:2505.13636) was published on October 19, 2025, and addresses the problem of incentivizing truthful behavior in language models through a game-theoretic peer prediction approach. While the search results don't specifically detail the conditional independence violation aspects you mentioned, the core mechanism uses a determinant-based mutual information score to achieve truthfulness guarantees without ground truth labels.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26ad79e9-80ba-49df-8e71-35f128257113",
  "isSidechain": false,
  "promptId": "f720f922-3c8c-49a1-93ae-ecb0f96bc76b",
  "type": "user",
  "uuid": "d50875c7-477b-47fe-85c2-6247fe4295e8",
  "toolUseResult": {
    "query": "PEG incentivizing truthful LLM peer prediction conditional independence violation 2505.13636",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Mvruoc16MYZNDHrHhthDEg",
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
            "title": "Evaluating LLM-Contaminated Crowdsourcing Data Without Ground Truth",
            "url": "https://arxiv.org/pdf/2506.06991"
          },
          {
            "title": "Eliciting Informative Text Evaluations with Large Language Models",
            "url": "https://arxiv.org/pdf/2405.15077"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nPeer Elicitation Games (PEG) is a training-free, game-theoretic framework for aligning LLMs through a peer elicitation mechanism involving a generator and multiple discriminators instantiated from distinct base models. \n\nDiscriminators interact in a peer evaluation setting, where utilities are computed using a determinant-based mutual information score that provably incentivizes truthful reporting without requiring ground-truth labels.\n\nThe paper establishes theoretical guarantees showing that each agent, via online learning, achieves sublinear regret, and proves last-iterate convergence to a truthful Nash equilibrium, ensuring that the actual policies used by agents converge to stable and truthful behavior over time.\n\nThe paper (arXiv:2505.13636) was published on October 19, 2025, and addresses the problem of incentivizing truthful behavior in language models through a game-theoretic peer prediction approach. While the search results don't specifically detail the conditional independence violation aspects you mentioned, the core mechanism uses a determinant-based mutual information score to achieve truthfulness guarantees without ground truth labels."
    ],
    "durationSeconds": 5.628251188000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "26ad79e9-80ba-49df-8e71-35f128257113",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T05:23:01.019Z_

<details><summary>↩ Tool result · `toolu_01FZgtUv8MTVG5xNqL5bG736`</summary>

```text
Web search results for query: "information-theoretic bounds manipulation resistance LLM evaluation ensemble 2026"

Links: [{"title":"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/pdf/2508.05469"},{"title":"Let’s Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/html/2508.05469"},{"title":"Don’t Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection","url":"https://arxiv.org/html/2602.08003"},{"title":"[2602.08003] Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection","url":"https://arxiv.org/abs/2602.08003"},{"title":"Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection","url":"https://arxiv.org/pdf/2602.08003"},{"title":"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs","url":"https://arxiv.org/pdf/2510.17000"}]

Based on the search results, I found several highly relevant papers on your query:

## Key Findings:

**1. Information-Theoretic Bounds on Manipulation Resistance for LLM Evaluation:**

Bounded f-divergences (e.g., total variation distance) maintain polynomial guarantees under attacks while unbounded measures (e.g., KL divergence) degrade exponentially. This research specifically addresses evaluation of AI systems without ground truth by analyzing which information-theoretic mechanisms resist adversarial manipulation.

The data processing inequality is leveraged: any strategic manipulation of content necessarily reduces mutual information between responses, implementing evaluation mechanisms with formal gaming-resistance guarantees.

**2. LLM Ensemble Selection Using Information Theory (2026):**

The budgeted ensemble selection problem addresses forming a subset of LLMs under query budget constraints, with the key difficulty being that LLM errors are strongly correlated. A greedy mutual-information selection algorithm estimates the required information terms directly from data and iteratively builds an ensemble under a query budget.

**3. Information-Theoretic Bounds on Adversarial Attacks:**

Adversarial attacks against LLMs can be viewed as attempts to infer a target property that becomes knowable after the model's reply is observed, with examples including flags that trigger harmful responses or degree of unlearning restoration.

These works all converge on applying information-theoretic principles to understand and defend against manipulation in LLM evaluation and ensemble settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e98e660-294b-4b56-af11-4e4a1560929b",
  "isSidechain": false,
  "promptId": "f720f922-3c8c-49a1-93ae-ecb0f96bc76b",
  "type": "user",
  "uuid": "89dc4a2f-512d-4e96-9769-a251647cc8cb",
  "toolUseResult": {
    "query": "information-theoretic bounds manipulation resistance LLM evaluation ensemble 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Fpj4T9bRBe6k1Q7tgj5LGJ",
        "content": [
          {
            "title": "Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/pdf/2508.05469"
          },
          {
            "title": "Let’s Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/html/2508.05469"
          },
          {
            "title": "Don’t Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection",
            "url": "https://arxiv.org/html/2602.08003"
          },
          {
            "title": "[2602.08003] Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection",
            "url": "https://arxiv.org/abs/2602.08003"
          },
          {
            "title": "Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection",
            "url": "https://arxiv.org/pdf/2602.08003"
          },
          {
            "title": "Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs",
            "url": "https://arxiv.org/pdf/2510.17000"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers on your query:\n\n## Key Findings:\n\n**1. Information-Theoretic Bounds on Manipulation Resistance for LLM Evaluation:**\n\nBounded f-divergences (e.g., total variation distance) maintain polynomial guarantees under attacks while unbounded measures (e.g., KL divergence) degrade exponentially. This research specifically addresses evaluation of AI systems without ground truth by analyzing which information-theoretic mechanisms resist adversarial manipulation.\n\nThe data processing inequality is leveraged: any strategic manipulation of content necessarily reduces mutual information between responses, implementing evaluation mechanisms with formal gaming-resistance guarantees.\n\n**2. LLM Ensemble Selection Using Information Theory (2026):**\n\nThe budgeted ensemble selection problem addresses forming a subset of LLMs under query budget constraints, with the key difficulty being that LLM errors are strongly correlated. A greedy mutual-information selection algorithm estimates the required information terms directly from data and iteratively builds an ensemble under a query budget.\n\n**3. Information-Theoretic Bounds on Adversarial Attacks:**\n\nAdversarial attacks against LLMs can be viewed as attempts to infer a target property that becomes knowable after the model's reply is observed, with examples including flags that trigger harmful responses or degree of unlearning restoration.\n\nThese works all converge on applying information-theoretic principles to understand and defend against manipulation in LLM evaluation and ensemble settings."
    ],
    "durationSeconds": 6.639637328999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5e98e660-294b-4b56-af11-4e4a1560929b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
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
  "lastPrompt": "# Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation Structure  ## Description  LLM evaluation faces systematic adversarial vulnera…",
  "leafUuid": "89dc4a2f-512d-4e96-9769-a251647cc8cb",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Certifiable multi-judge LLM evaluation robustness bounds",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc"
}
```

---

### Assistant

_source line 23 · 2026-05-20T05:23:06.114Z_

<details><summary>Logged reasoning block</summary>

```text
Good, now let me do a few more targeted searches to understand the landscape better, particularly around:
1. The SDPI (Strong Data Processing Inequality) application to adversarial settings
2. Certified robustness for ensembles (Horvath et al.)
3. Recent work on correlated errors in LLMs (Kim et al.)
4. Any very recent work (2026) that might overlap with the asymmetric dual claim
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89dc4a2f-512d-4e96-9769-a251647cc8cb",
  "isSidechain": false,
  "requestId": "req_011CbDG86qDRzVG95iqr7ABH",
  "type": "assistant",
  "uuid": "09e8e92d-27c3-45dd-957e-56e5441f7492",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WefC2CzCRUHh1UWSSKcu1c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1108,
      "cache_creation_input_tokens": 1823,
      "cache_read_input_tokens": 25117,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1823,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1108,
          "output_tokens": 312,
          "cache_read_input_tokens": 25117,
          "cache_creation_input_tokens": 1823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1823
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

_source line 24 · 2026-05-20T05:23:06.612Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BL6xWivRkCmLVvpdaddxM2`</summary>

```json
{
  "query": "strong data processing inequality SDPI adversarial robustness ensemble certification variance reduction 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09e8e92d-27c3-45dd-957e-56e5441f7492",
  "isSidechain": false,
  "requestId": "req_011CbDG86qDRzVG95iqr7ABH",
  "type": "assistant",
  "uuid": "ac3df05e-cdc0-423a-abdb-501d83c253d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WefC2CzCRUHh1UWSSKcu1c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1108,
      "cache_creation_input_tokens": 1823,
      "cache_read_input_tokens": 25117,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1823,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1108,
          "output_tokens": 312,
          "cache_read_input_tokens": 25117,
          "cache_creation_input_tokens": 1823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1823
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

_source line 25 · 2026-05-20T05:23:07.544Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HpUK9j6c9crqsKTMbebFEe`</summary>

```json
{
  "query": "correlated errors LLM judges Kim et al 2506.07962 behavioral entanglement multi-model evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac3df05e-cdc0-423a-abdb-501d83c253d4",
  "isSidechain": false,
  "requestId": "req_011CbDG86qDRzVG95iqr7ABH",
  "type": "assistant",
  "uuid": "5b3706db-50b3-4ecf-9dfc-e43ebfe6271b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WefC2CzCRUHh1UWSSKcu1c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1108,
      "cache_creation_input_tokens": 1823,
      "cache_read_input_tokens": 25117,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1823,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1108,
          "output_tokens": 312,
          "cache_read_input_tokens": 25117,
          "cache_creation_input_tokens": 1823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1823
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

_source line 26 · 2026-05-20T05:23:08.427Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GEF36cKwRA3RXgrPgwsUnZ`</summary>

```json
{
  "query": "\"adversarial dual\" OR \"manipulation cost scaling\" multi-agent evaluation diversity robustness tradeoff 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b3706db-50b3-4ecf-9dfc-e43ebfe6271b",
  "isSidechain": false,
  "requestId": "req_011CbDG86qDRzVG95iqr7ABH",
  "type": "assistant",
  "uuid": "735de7a9-ceb1-4b6a-9bb6-72c06f7da4bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WefC2CzCRUHh1UWSSKcu1c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1108,
      "cache_creation_input_tokens": 1823,
      "cache_read_input_tokens": 25117,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1823,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1108,
          "output_tokens": 312,
          "cache_read_input_tokens": 25117,
          "cache_creation_input_tokens": 1823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1823
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

_source line 27 · 2026-05-20T05:23:14.204Z_

<details><summary>↩ Tool result · `toolu_01HpUK9j6c9crqsKTMbebFEe`</summary>

```text
Web search results for query: "correlated errors LLM judges Kim et al 2506.07962 behavioral entanglement multi-model evaluation"

Links: [{"title":"How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/html/2604.07650v1"},{"title":"How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/pdf/2604.07650"},{"title":"[2604.07650v1] How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/abs/2604.07650v1"},{"title":"[2604.07650] How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/abs/2604.07650"},{"title":"Correlated Errors in Large Language Models","url":"https://arxiv.org/html/2506.07962v1"},{"title":"(PDF) Correlated Errors in Large Language Models","url":"https://www.researchgate.net/publication/392529896_Correlated_Errors_in_Large_Language_Models"},{"title":"[2506.07962] Correlated Errors in Large Language Models","url":"https://arxiv.org/abs/2506.07962"},{"title":"Correlated Errors in Large Language Models","url":"https://arxiv.org/pdf/2506.07962"}]

I found relevant research on this topic. Based on the search results, here's what I found:

## "Correlated Errors in Large Language Models" (Kim et al., 2506.07962)

This paper by Elliot Kim and coauthors conducts a large-scale empirical evaluation on over 350 LLMs using two popular leaderboards and a resume-screening task. 

The research finds substantial correlation in model errors—on one leaderboard dataset, models agree 60% of the time when both models err. The authors identify factors driving model correlation, including shared architectures and providers, though notably larger and more accurate models have highly correlated errors even with distinct architectures and providers.

### Impact on LLM-as-Judge Evaluation

A key finding shows that each judge systematically inflates the accuracy of models that are less accurate than itself, due to correlated errors (where the judge marks incorrect answers as correct if both models agree on the incorrect answer). 

The paper demonstrates the effects of correlation in two downstream tasks: LLM-as-judge evaluation and hiring—the latter reflecting theoretical predictions regarding algorithmic monoculture.

This research appears complementary to the earlier work on behavioral entanglement (arxiv 2604.07650), both addressing how apparent diversity in LLMs masks underlying dependencies that affect multi-model evaluation systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b3706db-50b3-4ecf-9dfc-e43ebfe6271b",
  "isSidechain": false,
  "promptId": "f720f922-3c8c-49a1-93ae-ecb0f96bc76b",
  "type": "user",
  "uuid": "910cc2f4-f99e-42d8-a3d0-d6b1455ef483",
  "toolUseResult": {
    "query": "correlated errors LLM judges Kim et al 2506.07962 behavioral entanglement multi-model evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RGPqKH2dpXexV252kmX6a2",
        "content": [
          {
            "title": "How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles",
            "url": "https://arxiv.org/html/2604.07650v1"
          },
          {
            "title": "How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles",
            "url": "https://arxiv.org/pdf/2604.07650"
          },
          {
            "title": "[2604.07650v1] How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles",
            "url": "https://arxiv.org/abs/2604.07650v1"
          },
          {
            "title": "[2604.07650] How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles",
            "url": "https://arxiv.org/abs/2604.07650"
          },
          {
            "title": "Correlated Errors in Large Language Models",
            "url": "https://arxiv.org/html/2506.07962v1"
          },
          {
            "title": "(PDF) Correlated Errors in Large Language Models",
            "url": "https://www.researchgate.net/publication/392529896_Correlated_Errors_in_Large_Language_Models"
          },
          {
            "title": "[2506.07962] Correlated Errors in Large Language Models",
            "url": "https://arxiv.org/abs/2506.07962"
          },
          {
            "title": "Correlated Errors in Large Language Models",
            "url": "https://arxiv.org/pdf/2506.07962"
          }
        ]
      },
      "I found relevant research on this topic. Based on the search results, here's what I found:\n\n## \"Correlated Errors in Large Language Models\" (Kim et al., 2506.07962)\n\nThis paper by Elliot Kim and coauthors conducts a large-scale empirical evaluation on over 350 LLMs using two popular leaderboards and a resume-screening task. \n\nThe research finds substantial correlation in model errors—on one leaderboard dataset, models agree 60% of the time when both models err. The authors identify factors driving model correlation, including shared architectures and providers, though notably larger and more accurate models have highly correlated errors even with distinct architectures and providers.\n\n### Impact on LLM-as-Judge Evaluation\n\nA key finding shows that each judge systematically inflates the accuracy of models that are less accurate than itself, due to correlated errors (where the judge marks incorrect answers as correct if both models agree on the incorrect answer). \n\nThe paper demonstrates the effects of correlation in two downstream tasks: LLM-as-judge evaluation and hiring—the latter reflecting theoretical predictions regarding algorithmic monoculture.\n\nThis research appears complementary to the earlier work on behavioral entanglement (arxiv 2604.07650), both addressing how apparent diversity in LLMs masks underlying dependencies that affect multi-model evaluation systems."
    ],
    "durationSeconds": 6.655595437999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5b3706db-50b3-4ecf-9dfc-e43ebfe6271b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T05:23:16.279Z_

<details><summary>↩ Tool result · `toolu_01GEF36cKwRA3RXgrPgwsUnZ`</summary>

```text
Web search results for query: ""adversarial dual" OR "manipulation cost scaling" multi-agent evaluation diversity robustness tradeoff 2025 2026"

Links: [{"title":"Agentic AI & Multi-Agent Orchestration: 2026 Enterprise Guide | AetherLink","url":"https://aetherlink.ai/en/blog/agentic-ai-multi-agent-orchestration-2026-enterprise-guide"},{"title":"Adversarial Multi-Agent Evaluation of Large Language ...","url":"https://arxiv.org/abs/2410.04663"},{"title":"Optimal Cost Constrained Adversarial Attacks For Multiple Agent Systems","url":"https://arxiv.org/pdf/2311.00859"},{"title":"Publications | Chenjia Bai","url":"http://baichenjia.cn/publication/"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/460a1d8eac34125dad453b28d6d64446-Paper-Conference.pdf"},{"title":"Advanced Game-Theoretic Frameworks for Multi-Agent AI Challenges: A 2025 Outlook","url":"https://arxiv.org/pdf/2506.17348"},{"title":"A Framework for Scalable Heterogeneous Multi-Agent Adversarial Reinforcement Learning in IsaacLab","url":"https://arxiv.org/pdf/2510.01264"},{"title":"Towards a Science of Scaling Agent Systems","url":"https://arxiv.org/html/2512.08296v1"}]

Based on the web search results, I found several relevant papers and discussions on these topics from 2025-2026:

## Key Findings:

**Adversarial Multi-Agent Evaluation:**
The D3 (Debate, Deliberate, Decide) framework is a cost-aware, adversarial multi-agent framework that orchestrates structured debate among role-specialized agents, instantiating two complementary protocols: Multi-Advocate One-Round Evaluation (MORE) with parallel defenses, and Single-Advocate Multi-Round Evaluation (SAMRE) with budgeted stopping under explicit token budgets.

**Robustness and Adversarial Attacks:**
Recent research shows that state-of-the-art multimodal agents, including those using GPT-4o with reflection and tree search, can be successfully hijacked to execute targeted adversarial goals with success rates up to 67%.

**Multi-Agent Scaling and Cost Tradeoffs:**
Current research examines architectural comparison of agent methods with objective complexity metrics, measuring computational complexity in terms of LLM calls, coordination overhead, and parallelization potential. A critical gap in 2025 agentic deployments is the lack of standardized evaluation methodologies, as traditional LLM benchmarks don't measure agent behavior including task success, reasoning quality, cost efficiency, or safety under adversarial conditions.

**Game-Theoretic Multi-Agent Frameworks:**
Recent game-theoretic work includes extensive discussions on repeated games and Bayesian updates for adversarial detection, with newly developed algorithms clarifying convergence of multi-agent reinforcement learning toward game-theoretic equilibria.

These results highlight the emerging focus on evaluating robustness and cost-efficiency tradeoffs in multi-agent systems during 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "735de7a9-ceb1-4b6a-9bb6-72c06f7da4bf",
  "isSidechain": false,
  "promptId": "f720f922-3c8c-49a1-93ae-ecb0f96bc76b",
  "type": "user",
  "uuid": "55d133ea-0cba-4372-8e86-34febe29dafb",
  "toolUseResult": {
    "query": "\"adversarial dual\" OR \"manipulation cost scaling\" multi-agent evaluation diversity robustness tradeoff 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ERZLETLuVoXB6gBshamuhk",
        "content": [
          {
            "title": "Agentic AI & Multi-Agent Orchestration: 2026 Enterprise Guide | AetherLink",
            "url": "https://aetherlink.ai/en/blog/agentic-ai-multi-agent-orchestration-2026-enterprise-guide"
          },
          {
            "title": "Adversarial Multi-Agent Evaluation of Large Language ...",
            "url": "https://arxiv.org/abs/2410.04663"
          },
          {
            "title": "Optimal Cost Constrained Adversarial Attacks For Multiple Agent Systems",
            "url": "https://arxiv.org/pdf/2311.00859"
          },
          {
            "title": "Publications | Chenjia Bai",
            "url": "http://baichenjia.cn/publication/"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/460a1d8eac34125dad453b28d6d64446-Paper-Conference.pdf"
          },
          {
            "title": "Advanced Game-Theoretic Frameworks for Multi-Agent AI Challenges: A 2025 Outlook",
            "url": "https://arxiv.org/pdf/2506.17348"
          },
          {
            "title": "A Framework for Scalable Heterogeneous Multi-Agent Adversarial Reinforcement Learning in IsaacLab",
            "url": "https://arxiv.org/pdf/2510.01264"
          },
          {
            "title": "Towards a Science of Scaling Agent Systems",
            "url": "https://arxiv.org/html/2512.08296v1"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers and discussions on these topics from 2025-2026:\n\n## Key Findings:\n\n**Adversarial Multi-Agent Evaluation:**\nThe D3 (Debate, Deliberate, Decide) framework is a cost-aware, adversarial multi-agent framework that orchestrates structured debate among role-specialized agents, instantiating two complementary protocols: Multi-Advocate One-Round Evaluation (MORE) with parallel defenses, and Single-Advocate Multi-Round Evaluation (SAMRE) with budgeted stopping under explicit token budgets.\n\n**Robustness and Adversarial Attacks:**\nRecent research shows that state-of-the-art multimodal agents, including those using GPT-4o with reflection and tree search, can be successfully hijacked to execute targeted adversarial goals with success rates up to 67%.\n\n**Multi-Agent Scaling and Cost Tradeoffs:**\nCurrent research examines architectural comparison of agent methods with objective complexity metrics, measuring computational complexity in terms of LLM calls, coordination overhead, and parallelization potential. A critical gap in 2025 agentic deployments is the lack of standardized evaluation methodologies, as traditional LLM benchmarks don't measure agent behavior including task success, reasoning quality, cost efficiency, or safety under adversarial conditions.\n\n**Game-Theoretic Multi-Agent Frameworks:**\nRecent game-theoretic work includes extensive discussions on repeated games and Bayesian updates for adversarial detection, with newly developed algorithms clarifying convergence of multi-agent reinforcement learning toward game-theoretic equilibria.\n\nThese results highlight the emerging focus on evaluating robustness and cost-efficiency tradeoffs in multi-agent systems during 2025-2026."
    ],
    "durationSeconds": 7.848933463999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "735de7a9-ceb1-4b6a-9bb6-72c06f7da4bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T05:23:20.853Z_

<details><summary>↩ Tool result · `toolu_01BL6xWivRkCmLVvpdaddxM2`</summary>

```text
Web search results for query: "strong data processing inequality SDPI adversarial robustness ensemble certification variance reduction 2024 2025 2026"

Links: [{"title":"Data Processing Inequality (DPI)","url":"https://www.emergentmind.com/topics/data-processing-inequality-dpi"},{"title":"Certifying Joint Adversarial Robustness for Model Ensembles","url":"https://arxiv.org/pdf/2004.10250"},{"title":"Tight Certificates of Adversarial Robustness for Randomly Smoothed   Classifiers","url":"https://arxiv.org/pdf/1906.04948"},{"title":"Strong Data Processing Inequalities via Sums of Squares Ois´ın Faust","url":"https://www.damtp.cam.ac.uk/user/hf323/sdpi-sos.pdf"},{"title":"Strong data-processing inequalities for channels and Bayesian networks","url":"https://arxiv.org/pdf/1508.06025"},{"title":"Data Processing Inequality","url":"https://www.emergentmind.com/topics/data-processing-inequality"},{"title":"[1906.04948] Tight Certificates of Adversarial Robustness for Randomly Smoothed Classifiers","url":"https://arxiv.org/abs/1906.04948"},{"title":"Enhancing Certifiable Robustness via a Deep Model Ensemble","url":"https://arxiv.org/pdf/1910.14655"}]

The search returned several relevant results on these topics. Here's what I found:

## Strong Data Processing Inequality (SDPI)

Strong data processing inequalities (SDPIs) quantify the strict decrease of divergences under noisy channels. Various channel-dependent improvements (called strong data-processing inequalities, or SDPIs) of the data-processing inequality have been proposed both classically and more recently.

Strong SDPI results extend to Bayesian networks and Markov chains, where end-to-end contraction along a network is bounded in terms of local site-wise contraction via percolation-type arguments. Additionally, nonlinear SDPI have been established for divergences such as the quantum hockey-stick divergence, producing tighter bounds for composed noisy channels, mixing times, and privacy parameters.

## Adversarial Robustness and Ensemble Certification

For certifying joint robustness of ensembles, researchers have proposed novel techniques building upon prior works on single-model robustness certification. Strong theoretical guarantees of robustness can be given for ensembles of classifiers generated by input randomization, where an ℓ₂ bounded adversary cannot alter the ensemble prediction generated by an additive isotropic Gaussian noise, with the radius depending on both the variance of the distribution and the ensemble margin.

The search results contain references spanning from 2015 through 2026, indicating active research in this intersection of information theory, machine learning robustness, and ensemble methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac3df05e-cdc0-423a-abdb-501d83c253d4",
  "isSidechain": false,
  "promptId": "f720f922-3c8c-49a1-93ae-ecb0f96bc76b",
  "type": "user",
  "uuid": "b060c891-8d45-4ef4-a0eb-3fb78c2fa92e",
  "toolUseResult": {
    "query": "strong data processing inequality SDPI adversarial robustness ensemble certification variance reduction 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01K4wB3TJsfiRhrvnDFG45Qx",
        "content": [
          {
            "title": "Data Processing Inequality (DPI)",
            "url": "https://www.emergentmind.com/topics/data-processing-inequality-dpi"
          },
          {
            "title": "Certifying Joint Adversarial Robustness for Model Ensembles",
            "url": "https://arxiv.org/pdf/2004.10250"
          },
          {
            "title": "Tight Certificates of Adversarial Robustness for Randomly Smoothed   Classifiers",
            "url": "https://arxiv.org/pdf/1906.04948"
          },
          {
            "title": "Strong Data Processing Inequalities via Sums of Squares Ois´ın Faust",
            "url": "https://www.damtp.cam.ac.uk/user/hf323/sdpi-sos.pdf"
          },
          {
            "title": "Strong data-processing inequalities for channels and Bayesian networks",
            "url": "https://arxiv.org/pdf/1508.06025"
          },
          {
            "title": "Data Processing Inequality",
            "url": "https://www.emergentmind.com/topics/data-processing-inequality"
          },
          {
            "title": "[1906.04948] Tight Certificates of Adversarial Robustness for Randomly Smoothed Classifiers",
            "url": "https://arxiv.org/abs/1906.04948"
          },
          {
            "title": "Enhancing Certifiable Robustness via a Deep Model Ensemble",
            "url": "https://arxiv.org/pdf/1910.14655"
          }
        ]
      },
      "The search returned several relevant results on these topics. Here's what I found:\n\n## Strong Data Processing Inequality (SDPI)\n\nStrong data processing inequalities (SDPIs) quantify the strict decrease of divergences under noisy channels. Various channel-dependent improvements (called strong data-processing inequalities, or SDPIs) of the data-processing inequality have been proposed both classically and more recently.\n\nStrong SDPI results extend to Bayesian networks and Markov chains, where end-to-end contraction along a network is bounded in terms of local site-wise contraction via percolation-type arguments. Additionally, nonlinear SDPI have been established for divergences such as the quantum hockey-stick divergence, producing tighter bounds for composed noisy channels, mixing times, and privacy parameters.\n\n## Adversarial Robustness and Ensemble Certification\n\nFor certifying joint robustness of ensembles, researchers have proposed novel techniques building upon prior works on single-model robustness certification. Strong theoretical guarantees of robustness can be given for ensembles of classifiers generated by input randomization, where an ℓ₂ bounded adversary cannot alter the ensemble prediction generated by an additive isotropic Gaussian noise, with the radius depending on both the variance of the distribution and the ensemble margin.\n\nThe search results contain references spanning from 2015 through 2026, indicating active research in this intersection of information theory, machine learning robustness, and ensemble methods."
    ],
    "durationSeconds": 14.235136820000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ac3df05e-cdc0-423a-abdb-501d83c253d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-20T05:23:20.859Z_

```json
{
  "parentUuid": "b060c891-8d45-4ef4-a0eb-3fb78c2fa92e",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3efa4b68-63eb-4129-a776-46d444168423",
  "timestamp": "2026-05-20T05:23:20.859Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-20T05:23:25.790Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do a couple more searches to check specific aspects:

1. Whether anyone has already established the "adversarial dual" of diversity scaling or the exponential-vs-polynomial asymmetry claim
2. Whether there's recent work on copula models for LLM judge correlation that overlaps
3. Any very recent work on certified robustness for LLM evaluation specifically
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3efa4b68-63eb-4129-a776-46d444168423",
  "isSidechain": false,
  "requestId": "req_011CbDG9Z457iGqLYbhioZx1",
  "type": "assistant",
  "uuid": "e5d0f2cd-2256-44bd-b58c-d1bb68c60589",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HHTxPpkYrNbv6qf9ykJ2a4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1598,
      "cache_creation_input_tokens": 2261,
      "cache_read_input_tokens": 26940,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1598,
          "output_tokens": 228,
          "cache_read_input_tokens": 26940,
          "cache_creation_input_tokens": 2261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2261
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

_source line 32 · 2026-05-20T05:23:26.740Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0176WFUUCxNCcjFQC49WprD3`</summary>

```json
{
  "query": "certified robustness randomized smoothing ensemble polynomial scaling manipulation cost information theory 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5d0f2cd-2256-44bd-b58c-d1bb68c60589",
  "isSidechain": false,
  "requestId": "req_011CbDG9Z457iGqLYbhioZx1",
  "type": "assistant",
  "uuid": "36576a56-37b9-4ecb-9abf-e2407b3152f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HHTxPpkYrNbv6qf9ykJ2a4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1598,
      "cache_creation_input_tokens": 2261,
      "cache_read_input_tokens": 26940,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1598,
          "output_tokens": 228,
          "cache_read_input_tokens": 26940,
          "cache_creation_input_tokens": 2261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2261
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

_source line 33 · 2026-05-20T05:23:27.435Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ChnesNXQzUJMtZjpFhjF7e`</summary>

```json
{
  "query": "semantic collapse multi-LLM systems Kong 2605.17193 representational collapse committee diversity erosion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36576a56-37b9-4ecb-9abf-e2407b3152f9",
  "isSidechain": false,
  "requestId": "req_011CbDG9Z457iGqLYbhioZx1",
  "type": "assistant",
  "uuid": "8292fd46-44b7-4afc-b66a-18b3a4cc59c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HHTxPpkYrNbv6qf9ykJ2a4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1598,
      "cache_creation_input_tokens": 2261,
      "cache_read_input_tokens": 26940,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1598,
          "output_tokens": 228,
          "cache_read_input_tokens": 26940,
          "cache_creation_input_tokens": 2261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2261
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

_source line 34 · 2026-05-20T05:23:34.060Z_

<details><summary>↩ Tool result · `toolu_0176WFUUCxNCcjFQC49WprD3`</summary>

```text
Web search results for query: "certified robustness randomized smoothing ensemble polynomial scaling manipulation cost information theory 2025 2026 arxiv"

Links: [{"title":"Promoting Robustness of Randomized Smoothing: Two Cost-Effective   Approaches","url":"https://arxiv.org/pdf/2310.07780"},{"title":"Trust, But Verify: A Survey of Randomized Smoothing Techniques","url":"https://arxiv.org/html/2312.12608v1"},{"title":"[2310.07780] Promoting Robustness of Randomized Smoothing: Two Cost-Effective Approaches","url":"https://arxiv.org/abs/2310.07780"},{"title":"Enhancing Certified Robustness via Smoothed Weighted Ensembling","url":"https://arxiv.org/pdf/2005.09363"},{"title":"Certified Robustness under Heterogeneous Perturbations via Hybrid Randomized Smoothing","url":"https://arxiv.org/html/2605.12876v1"},{"title":"Multi-head Ensemble of Smoothed Classifiers for Certified Robustness","url":"https://arxiv.org/pdf/2211.10882"},{"title":"Certifying Confidence via Randomized Smoothing","url":"https://arxiv.org/pdf/2009.08061"},{"title":"Certified Robustness via Randomized Smoothing over Multiplicative   Parameters of Input Transformations","url":"https://arxiv.org/pdf/2106.14432"}]

I found several relevant research papers on certified robustness and randomized smoothing. Here are the key results:

**Recent Work (2025-2026):**

Randomized smoothing provides strong, model-agnostic robustness certificates by certifying the stability of a smoothed predictor under input perturbations. A very recent paper (from 6 days ago) addresses heterogeneous perturbation models, treating continuous and discrete inputs, and offering principled ways to reason about adversaries that act simultaneously on heterogeneous input channels.

**Ensemble-Based Approaches:**

The EsbRS ensemble method greatly improves robustness certificates based on building model ensembles and proposes novel design methodologies to improve robustness based on theoretical analysis. The ensemble of multiple DNNs as base classifiers in randomized smoothing has shown great potential, with weighted logit ensemble and max-margin ensemble approaches achieving significant improvements in certified accuracy.

**Cost Efficiency:**

AdvMacer combines adversarial training and robustness certification maximization for randomized smoothing and is 3× faster to train than MACER baseline. However, traditional ensemble schemes demand considerably higher computational resources to train multiple large DNNs.

The search results contain papers from 2020-2023 as well as a very recent 2025/2026 submission on multimodal heterogeneous perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36576a56-37b9-4ecb-9abf-e2407b3152f9",
  "isSidechain": false,
  "promptId": "f720f922-3c8c-49a1-93ae-ecb0f96bc76b",
  "type": "user",
  "uuid": "c7d9d5c2-50f5-4555-bec4-6a42a83bd91d",
  "toolUseResult": {
    "query": "certified robustness randomized smoothing ensemble polynomial scaling manipulation cost information theory 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Vf6x4Vhv6df1Ukqbtwq1Fs",
        "content": [
          {
            "title": "Promoting Robustness of Randomized Smoothing: Two Cost-Effective   Approaches",
            "url": "https://arxiv.org/pdf/2310.07780"
          },
          {
            "title": "Trust, But Verify: A Survey of Randomized Smoothing Techniques",
            "url": "https://arxiv.org/html/2312.12608v1"
          },
          {
            "title": "[2310.07780] Promoting Robustness of Randomized Smoothing: Two Cost-Effective Approaches",
            "url": "https://arxiv.org/abs/2310.07780"
          },
          {
            "title": "Enhancing Certified Robustness via Smoothed Weighted Ensembling",
            "url": "https://arxiv.org/pdf/2005.09363"
          },
          {
            "title": "Certified Robustness under Heterogeneous Perturbations via Hybrid Randomized Smoothing",
            "url": "https://arxiv.org/html/2605.12876v1"
          },
          {
            "title": "Multi-head Ensemble of Smoothed Classifiers for Certified Robustness",
            "url": "https://arxiv.org/pdf/2211.10882"
          },
          {
            "title": "Certifying Confidence via Randomized Smoothing",
            "url": "https://arxiv.org/pdf/2009.08061"
          },
          {
            "title": "Certified Robustness via Randomized Smoothing over Multiplicative   Parameters of Input Transformations",
            "url": "https://arxiv.org/pdf/2106.14432"
          }
        ]
      },
      "I found several relevant research papers on certified robustness and randomized smoothing. Here are the key results:\n\n**Recent Work (2025-2026):**\n\nRandomized smoothing provides strong, model-agnostic robustness certificates by certifying the stability of a smoothed predictor under input perturbations. A very recent paper (from 6 days ago) addresses heterogeneous perturbation models, treating continuous and discrete inputs, and offering principled ways to reason about adversaries that act simultaneously on heterogeneous input channels.\n\n**Ensemble-Based Approaches:**\n\nThe EsbRS ensemble method greatly improves robustness certificates based on building model ensembles and proposes novel design methodologies to improve robustness based on theoretical analysis. The ensemble of multiple DNNs as base classifiers in randomized smoothing has shown great potential, with weighted logit ensemble and max-margin ensemble approaches achieving significant improvements in certified accuracy.\n\n**Cost Efficiency:**\n\nAdvMacer combines adversarial training and robustness certification maximization for randomized smoothing and is 3× faster to train than MACER baseline. However, traditional ensemble schemes demand considerably higher computational resources to train multiple large DNNs.\n\nThe search results contain papers from 2020-2023 as well as a very recent 2025/2026 submission on multimodal heterogeneous perturbations."
    ],
    "durationSeconds": 7.315697176000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "36576a56-37b9-4ecb-9abf-e2407b3152f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation Structure  ## Description  LLM evaluation faces systematic adversarial vulnera…",
  "leafUuid": "c7d9d5c2-50f5-4555-bec4-6a42a83bd91d",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Certifiable multi-judge LLM evaluation robustness bounds",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc"
}
```

---

### Tool result

_source line 37 · 2026-05-20T05:23:34.194Z_

<details><summary>↩ Tool result · `toolu_01ChnesNXQzUJMtZjpFhjF7e`</summary>

```text
Web search results for query: "semantic collapse multi-LLM systems Kong 2605.17193 representational collapse committee diversity erosion"

Links: [{"title":"[2605.17193] Multi-LLM Systems Exhibit Robust Semantic Collapse","url":"https://arxiv.org/abs/2605.17193"},{"title":"How to Tame Your LLM: Semantic Collapse in Continuous Systems","url":"https://arxiv.org/html/2512.05162v1"},{"title":"[2512.05162] How to Tame Your LLM: Semantic Collapse in Continuous Systems","url":"https://arxiv.org/abs/2512.05162"},{"title":"Asymptotic Semantic Collapse in Hierarchical Optimization","url":"https://arxiv.org/pdf/2602.18450"},{"title":"Multi-LLM ReAct AI Agent with Kong AI Gateway 3.10 and LangGraph | by Claudio Acquaviva | Medium","url":"https://medium.com/@claudioacquaviva/multi-llm-react-ai-agent-with-kong-ai-gateway-3-10-and-langgraph-7429c9c1f5ee"},{"title":"Modality Collapse as Mismatched Decoding: Information-Theoretic Limits of Multimodal LLMs","url":"https://arxiv.org/pdf/2602.23136"},{"title":"Representational Collapse in Multi-Agent LLM Committees: Measurement and Diversity-Aware Consensus","url":"https://arxiv.org/pdf/2604.03809"}]

Based on the search results, I found highly relevant information about your query:

## Multi-LLM Systems and Semantic Collapse (Kong et al., 2605.17193)

Multi-LLM systems operating in closed loops exhibit semantic collapse: systematic convergence in semantic representations despite apparent lexical variation. Across model families, extended simulations of 200 to 1,000 rounds show this pattern remains consistent.

Twelve intervention strategies, spanning decoding parameters, prompt design, agent composition, activation engineering, and reinforcement learning, fail to restore semantic diversity. Mechanistic analyses suggest that semantic collapse is not explained by alignment or conformity biases, but is consistent with intrinsic properties of autoregressive generation.

## Related Work: Representational Collapse in LLM Committees

Committees of LLM agents assembled for improved reasoning accuracy include strategies like self-consistency sampling, Mixture-of-Agents layering, and debate protocols where agents critique each other. However, collapse is measurable, worsens on harder tasks, and the choice of embedding proxy is a first-order design decision for latent communication protocols. For agentic systems deployed at scale, whether agents produce redundant outputs directly determines whether additional agents justify their compute cost.

The Kong et al. (2605.17193) paper represents recent research (submitted May 16, 2026) addressing fundamental questions about whether multi-LLM systems can generate novel content when operating autonomously.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8292fd46-44b7-4afc-b66a-18b3a4cc59c0",
  "isSidechain": false,
  "promptId": "f720f922-3c8c-49a1-93ae-ecb0f96bc76b",
  "type": "user",
  "uuid": "9abcaacc-dc23-4b0e-88a3-2cf698c98730",
  "toolUseResult": {
    "query": "semantic collapse multi-LLM systems Kong 2605.17193 representational collapse committee diversity erosion",
    "results": [
      {
        "tool_use_id": "srvtoolu_01167w5DMRMaFuYFQ4rJRziM",
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
            "title": "[2512.05162] How to Tame Your LLM: Semantic Collapse in Continuous Systems",
            "url": "https://arxiv.org/abs/2512.05162"
          },
          {
            "title": "Asymptotic Semantic Collapse in Hierarchical Optimization",
            "url": "https://arxiv.org/pdf/2602.18450"
          },
          {
            "title": "Multi-LLM ReAct AI Agent with Kong AI Gateway 3.10 and LangGraph | by Claudio Acquaviva | Medium",
            "url": "https://medium.com/@claudioacquaviva/multi-llm-react-ai-agent-with-kong-ai-gateway-3-10-and-langgraph-7429c9c1f5ee"
          },
          {
            "title": "Modality Collapse as Mismatched Decoding: Information-Theoretic Limits of Multimodal LLMs",
            "url": "https://arxiv.org/pdf/2602.23136"
          },
          {
            "title": "Representational Collapse in Multi-Agent LLM Committees: Measurement and Diversity-Aware Consensus",
            "url": "https://arxiv.org/pdf/2604.03809"
          }
        ]
      },
      "Based on the search results, I found highly relevant information about your query:\n\n## Multi-LLM Systems and Semantic Collapse (Kong et al., 2605.17193)\n\nMulti-LLM systems operating in closed loops exhibit semantic collapse: systematic convergence in semantic representations despite apparent lexical variation. Across model families, extended simulations of 200 to 1,000 rounds show this pattern remains consistent.\n\nTwelve intervention strategies, spanning decoding parameters, prompt design, agent composition, activation engineering, and reinforcement learning, fail to restore semantic diversity. Mechanistic analyses suggest that semantic collapse is not explained by alignment or conformity biases, but is consistent with intrinsic properties of autoregressive generation.\n\n## Related Work: Representational Collapse in LLM Committees\n\nCommittees of LLM agents assembled for improved reasoning accuracy include strategies like self-consistency sampling, Mixture-of-Agents layering, and debate protocols where agents critique each other. However, collapse is measurable, worsens on harder tasks, and the choice of embedding proxy is a first-order design decision for latent communication protocols. For agentic systems deployed at scale, whether agents produce redundant outputs directly determines whether additional agents justify their compute cost.\n\nThe Kong et al. (2605.17193) paper represents recent research (submitted May 16, 2026) addressing fundamental questions about whether multi-LLM systems can generate novel content when operating autonomously."
    ],
    "durationSeconds": 6.756130541999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8292fd46-44b7-4afc-b66a-18b3a4cc59c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-20T05:25:00.627Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the landscape. Let me synthesize my findings and analyze this proposal carefully.

**Key observations from the literature search:**

1. **The "adversarial dual" concept appears genuinely novel.** I couldn't find any work that formally establishes the dual relationship between diversity-scaling for task performance (exponential) and adversarial robustness (polynomial). Yang et al. only address task performance. The certified ensemble robustness literature (Horvath et al., randomized smoothing) focuses on classifier ensembles, not LLM evaluation.

2. **PEG guarantee degradation under correlation is a genuine gap.** PEG's paper (Chen et al.) relies on conditional independence (Assumption 4), and I found no work characterizing what happens when this assumption is violated.


3. **The SDPI approach is technically sound, though the transition from per-channel bounds to multi-channel bounds with correlated judges requires careful handling**—the additive bound K_eff · I_max isn't straightforward when judges are correlated.

4. **Kong et al.'s recent work on semantic collapse is directly relevant, and the proposal makes a solid distinction** by arguing that their single-pass setting avoids the closed-loop collapse problem.

5. **Kim et al.'s findings on correlated errors across larger models pose a real challenge**—even distinct architectures and providers show highly correlated errors, which the proposal acknowledges but may not fully address in terms of its practical implications.

Now I'm questioning whether the certified bounds actually provide meaningful value over simpler alternatives. The trivial approach of just using majority voting with diverse judges already achieves substantial empirical improvements—the SoK shows 7-model committees reduce ASR to 10-19%. While certification is theoretically distinct from empirical robustness, the certified bounds appear quite loose: with K=7, they predict only 2.65-3.7× improvement over a single judge, yet empirical results show much larger gains from ~50-68% down to 10-19%. This looseness undermines the practical utility, even if it's acceptable for a theoretical contribution.

The core assumptions also feel shaky. The equicorrelated Gaussian copula model is restrictive given that real LLM judge correlations are likely heterogeneous across different pairs. The heterogeneous fallback using K* = 2^{H(ρ)} helps, but the fundamental ½ exponent in the variance reduction bound comes directly from the well-known √K result in randomized smoothing—I'm not convinced this is truly novel or just a straightforward application of existing techniques to a new domain.

Looking at the claimed novelty more carefully, the three contributions are the asymmetric adversarial dual showing exponential performance versus polynomial robustness, the PEG guarantee degradation under correlation, and prescriptive judge selection via K_eff maximization. For the first one, I need to assess whether this asymmetry is actually surprising or just expected given the problem structure.

The performance side relies on Yang et al.'s result while the robustness side combines SDPI with variance reduction—the √K certified radius is already known from Horvath et al. What's genuinely new is connecting K_eff to inter-judge correlation through the copula and observing that the two sides scale differently. The conceptual insight about exponential versus polynomial asymmetry is valuable and somewhat surprising, but the underlying proof techniques are largely assembled from existing work. The composition is non-trivial, so it counts as novel, though I should be precise about what's actually original here.

The PEG degradation analysis under correlation feels like the most genuinely novel and practically useful contribution. The judge selection corollary is less central. I'm thinking about where the idea could be strengthened—the asymmetry insight could be sharpened further, and there might be room to push beyond the current framing.

The real question is whether the exponential versus polynomial comparison is the right way to frame this, since the two sides are actually measuring different quantities. What's more fundamental is understanding the structural reason why adversarial attacks scale differently than random errors—specifically, whether it's because an adversary can adaptively correlate their manipulation across judges while random noise cannot. That structural explanation would be much more compelling.

I'm also noticing that Kim et al.'s finding about frontier models having higher correlated errors across providers creates a real tension here. The judges you'd want to use are the most capable models, but those are exactly the ones where achieving diversity becomes hardest. This suggests K_eff might be fundamentally limited at the frontier, which would mean certification quality doesn't necessarily improve with judge capability—that's a much more striking and provocative implication than what I've currently emphasized.

The PEG degradation analysis could be reframed as a broader result about robustness of incentive-compatible mechanisms under correlation, which would connect it to the entire peer prediction and mechanism design literature rather than just LLM evaluation. I should also double-check the related work more carefully—I want to make sure I'm not missing existing results on robustness of information elicitation mechanisms under correlated agents, since that could affect how novel the PEG analysis actually is.

Looking at the core premise, the claim that no prior work provides formal N-agent manipulation-cost scaling as a function of measurable inter-judge correlation does seem to hold up. The existing literature either focuses on single judges, assumes independence, or stays empirical. The two-step proof strategy using SDPI per-channel and variance reduction looks reasonable in principle, though I'm concerned about whether the information gain from correlated judges truly decomposes additively the way the K_eff construction assumes.

On tightness, the proposal claims Ω(K_eff^{1/2}) as a lower bound, which matches the upper bound from randomized smoothing on classifiers. But it's unclear whether LLM judges would follow the same scaling or if there's something fundamentally different about how they respond to manipulation attempts. The proposal could be stronger by explicitly addressing whether the classifier results transfer here. I'm realizing this proposal is already quite mature and well-developed, so I need to be honest about whether my suggestions actually deepen the work or just add surface-level polish. Looking back, the proposal already covers the key elements—it acknowledges Kim et al., articulates the asymmetry clearly, positions PEG degradation as a core contribution, and has a plan for tightness analysis. The real value would be in making the *why* behind the asymmetry more explicit at a theoretical level, and potentially elevating the frontier-model paradox as a more central narrative thread rather than a side observation.

But I'm also noticing a potential vulnerability: is the asymmetry itself actually a novel contribution, or just an observation that two known results have different scaling rates? The distinction matters—if the proposal proves a fundamental structural theorem explaining *why* the asymmetry exists, that's genuinely strong. If it's mainly computing both sides and noting they differ, it risks feeling incremental. The proof strategy seems to connect both results in a meaningful way, which would be the crux of whether this is truly a theoretical advance.

That said, I'm concerned the proposal might be overextended. It's juggling the theoretical framework, PEG degradation analysis, judge selection heuristics, empirical validation, assumption testing, and adaptive attacks all at once. For an 8-page venue submission, that's either impressively comprehensive or dangerously unfocused depending on how tightly it's woven together.

Let me step back and identify what would genuinely elevate this work. The core insight about asymmetric correlation is solid, but three things could push it from strong to exceptional: first, a deeper mechanistic explanation for why the same correlation parameter produces different scaling behaviors on adversarial versus stochastic sides; second, much stronger exploitation of the frontier-model correlation paradox as a motivating phenomenon; and third, rigorous analysis of whether the ½ exponent is fundamental to the problem or just an artifact of the current proof technique.

There's also a subtle theoretical gap I want to flag: the proposal compares diverse ensemble judges against self-consistency voting, and while the experiments are planned, the theory should explicitly predict why K_eff for self-consistency (same model, multiple runs) should be lower than K_eff for a truly diverse ensemble. The self-consistency baseline with temperature variation is a good control, but the theoretical framework needs to quantify the K_eff difference between these approaches rather than just empirically measuring it.

Now I'm noticing the "prescriptive judge-selection tool" framing might be overstated—the claim that accuracy and manipulation-resistance are conflicting objectives needs a concrete counterexample or theoretical proof. If diverse panels turn out to be both more accurate and more robust in practice, then this tension doesn't actually exist, and the contribution becomes less novel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9abcaacc-dc23-4b0e-88a3-2cf698c98730",
  "isSidechain": false,
  "requestId": "req_011CbDGAY5KDejybtwYdM5Ek",
  "type": "assistant",
  "uuid": "925a7482-6b3a-4066-a2e6-e088fb575c2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRJdbNyXQZfgJ6JfoQ3A4b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3312,
      "cache_read_input_tokens": 29201,
      "output_tokens": 3342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3342,
          "cache_read_input_tokens": 29201,
          "cache_creation_input_tokens": 3312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3312
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

_source line 39 · 2026-05-20T05:25:00.672Z_

Now let me do one final targeted search on a critical gap I want to verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "925a7482-6b3a-4066-a2e6-e088fb575c2e",
  "isSidechain": false,
  "requestId": "req_011CbDGAY5KDejybtwYdM5Ek",
  "type": "assistant",
  "uuid": "25c54b8f-9436-4373-b20a-dce35a03c572",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRJdbNyXQZfgJ6JfoQ3A4b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3312,
      "cache_read_input_tokens": 29201,
      "output_tokens": 3342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3342,
          "cache_read_input_tokens": 29201,
          "cache_creation_input_tokens": 3312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3312
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

_source line 40 · 2026-05-20T05:25:00.679Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017VheYvLoCfxHmt5WMdzzWB`</summary>

```json
{
  "query": "peer prediction mechanism correlated agents degradation guarantee approximate incentive compatibility information design 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25c54b8f-9436-4373-b20a-dce35a03c572",
  "isSidechain": false,
  "requestId": "req_011CbDGAY5KDejybtwYdM5Ek",
  "type": "assistant",
  "uuid": "0ec15371-6369-457a-bd19-5d4cf50e720b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRJdbNyXQZfgJ6JfoQ3A4b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3312,
      "cache_read_input_tokens": 29201,
      "output_tokens": 3342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3342,
          "cache_read_input_tokens": 29201,
          "cache_creation_input_tokens": 3312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3312
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
  "lastPrompt": "# Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation Structure  ## Description  LLM evaluation faces systematic adversarial vulnera…",
  "leafUuid": "0ec15371-6369-457a-bd19-5d4cf50e720b",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Certifiable multi-judge LLM evaluation robustness bounds",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc"
}
```

---

### Tool result

_source line 43 · 2026-05-20T05:25:07.026Z_

<details><summary>↩ Tool result · `toolu_017VheYvLoCfxHmt5WMdzzWB`</summary>

```text
Web search results for query: "peer prediction mechanism correlated agents degradation guarantee approximate incentive compatibility information design 2024 2025"

Links: [{"title":"Peer Prediction with Heterogeneous Users - Arpit Agarwal","url":"https://agarpit.github.io/papers/het-pp.pdf"},{"title":"Peer Prediction for Learning Agents Shi Feng","url":"https://arxiv.org/pdf/2208.04433"},{"title":"Peer Neighborhood Mechanisms: A Framework for Mechanism Generalization","url":"https://arxiv.org/html/2312.12303v1"},{"title":"Peer Prediction with Heterogeneous Users | ACM Transactions on Economics and Computation","url":"https://dl.acm.org/doi/10.1145/3381519"},{"title":"Stochastically Dominant Peer Prediction","url":"https://arxiv.org/pdf/2506.02259"},{"title":"Peer Neighborhood Mechanisms: A Framework for Mechanism Generalization","url":"https://arxiv.org/pdf/2312.12303"},{"title":"Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction","url":"https://arxiv.org/pdf/2601.20299"}]

The search has returned several relevant results on peer prediction mechanisms. Here's what I found:

## Key Research Areas

**Peer Prediction with Heterogeneous/Correlated Agents:**

Peer prediction mechanisms incentivize agents to truthfully report their signals in the absence of a verification mechanism by comparing agents' reports with their peers. Prior work is essentially restricted to the case of homogeneous agents with identical signal distributions. Although the Correlated Agreement (CA) mechanism can be extended to handle heterogeneous agents, there is a challenge of efficiently estimating agent signal types, which is solved by clustering agents based on their reporting behavior.

**Information Design and Mechanism Generalization:**

Recent work introduces novel incentive mechanisms that extend peer prediction to arbitrary distributions by replacing exact matching with neighborhood matching, with conditions that guarantee incentive-compatibility for rational data providers.

**Recent Developments (2024-2025):**

Peer prediction provides solutions for scenarios where report quality cannot be verified against ground truth, particularly valuable when obtaining ground truth is costly or infeasible, such as in subjective tasks. Additionally, recent work addresses mechanisms that incentivize truthful behaviors through game-theoretic incentive compatibility, particularly relevant to evaluating advanced AI systems without strong supervision.

The results show active research in extending peer prediction mechanisms to handle correlated agents, improving incentive compatibility guarantees, and developing information-theoretic design principles.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ec15371-6369-457a-bd19-5d4cf50e720b",
  "isSidechain": false,
  "promptId": "f720f922-3c8c-49a1-93ae-ecb0f96bc76b",
  "type": "user",
  "uuid": "460bb639-0be5-4722-a61c-9773258b0995",
  "toolUseResult": {
    "query": "peer prediction mechanism correlated agents degradation guarantee approximate incentive compatibility information design 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_0119Pn1iqGEar2cGBRnwA3Zz",
        "content": [
          {
            "title": "Peer Prediction with Heterogeneous Users - Arpit Agarwal",
            "url": "https://agarpit.github.io/papers/het-pp.pdf"
          },
          {
            "title": "Peer Prediction for Learning Agents Shi Feng",
            "url": "https://arxiv.org/pdf/2208.04433"
          },
          {
            "title": "Peer Neighborhood Mechanisms: A Framework for Mechanism Generalization",
            "url": "https://arxiv.org/html/2312.12303v1"
          },
          {
            "title": "Peer Prediction with Heterogeneous Users | ACM Transactions on Economics and Computation",
            "url": "https://dl.acm.org/doi/10.1145/3381519"
          },
          {
            "title": "Stochastically Dominant Peer Prediction",
            "url": "https://arxiv.org/pdf/2506.02259"
          },
          {
            "title": "Peer Neighborhood Mechanisms: A Framework for Mechanism Generalization",
            "url": "https://arxiv.org/pdf/2312.12303"
          },
          {
            "title": "Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction",
            "url": "https://arxiv.org/pdf/2601.20299"
          }
        ]
      },
      "The search has returned several relevant results on peer prediction mechanisms. Here's what I found:\n\n## Key Research Areas\n\n**Peer Prediction with Heterogeneous/Correlated Agents:**\n\nPeer prediction mechanisms incentivize agents to truthfully report their signals in the absence of a verification mechanism by comparing agents' reports with their peers. Prior work is essentially restricted to the case of homogeneous agents with identical signal distributions. Although the Correlated Agreement (CA) mechanism can be extended to handle heterogeneous agents, there is a challenge of efficiently estimating agent signal types, which is solved by clustering agents based on their reporting behavior.\n\n**Information Design and Mechanism Generalization:**\n\nRecent work introduces novel incentive mechanisms that extend peer prediction to arbitrary distributions by replacing exact matching with neighborhood matching, with conditions that guarantee incentive-compatibility for rational data providers.\n\n**Recent Developments (2024-2025):**\n\nPeer prediction provides solutions for scenarios where report quality cannot be verified against ground truth, particularly valuable when obtaining ground truth is costly or infeasible, such as in subjective tasks. Additionally, recent work addresses mechanisms that incentivize truthful behaviors through game-theoretic incentive compatibility, particularly relevant to evaluating advanced AI systems without strong supervision.\n\nThe results show active research in extending peer prediction mechanisms to handle correlated agents, improving incentive compatibility guarantees, and developing information-theoretic design principles."
    ],
    "durationSeconds": 6.339542547999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0ec15371-6369-457a-bd19-5d4cf50e720b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-20T05:25:18.386Z_

<details><summary>Logged reasoning block</summary>

```text
This is helpful. I see that the peer prediction literature has work on heterogeneous agents but NOT specifically on the degradation of dominant-strategy guarantees under correlation violation. The proposal's PEG degradation analysis does seem to fill a genuine gap.

However, I notice "Peer Prediction with Heterogeneous Users" (Agarwal et al.) addresses heterogeneous agents in peer prediction, which is conceptually related. But heterogeneous ≠ correlated. The proposal's specific focus on how correlation (not heterogeneity) degrades PEG's guarantees is distinct.
 
I'm wondering whether the Ω(K_eff^{1/2}) bound is actually tight. In randomized smoothing, the √K result holds for continuous ℓ₂ perturbations, but the LLM evaluation setting involves discrete text perturbations—the proposal doesn't address whether this distinction affects the tightness of the bound, which feels like a meaningful gap in the theoretical analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "460bb639-0be5-4722-a61c-9773258b0995",
  "isSidechain": false,
  "requestId": "req_011CbDGHNyZpZy5tU6C8ZqTb",
  "type": "assistant",
  "uuid": "33e832a6-2994-4aff-a46c-1b3b09315e6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pYP8Kj7mfrsvtKwheTzMR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3977,
      "cache_read_input_tokens": 32513,
      "output_tokens": 4173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3977,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4173,
          "cache_read_input_tokens": 32513,
          "cache_creation_input_tokens": 3977,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3977
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

_source line 45 · 2026-05-20T05:26:49.018Z_

Now I have sufficient context to provide a thorough analysis. Let me synthesize my findings.

---

【状态】: 有发掘空间

【前置调研发现】
- **Yang et al., "Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity" (ICLR 2026 Workshop AIMS, arXiv 2602.03794)**: Proves K* = 2^{H(ρ)} effective channel count, showing heterogeneous configurations (2 diverse agents) can match or exceed 16 homogeneous agents. Addresses **task performance only**—no adversarial analysis. This is the "one side" of the proposed asymmetric dual.
- **Kim et al., "Correlated Errors in Large Language Models" (ICML 2025, arXiv 2506.07962)**: 60% agreement when both err; critically, **larger and more accurate models have highly correlated errors even with distinct architectures and providers**. This finding is acknowledged in the proposal but its deepest implications are underexploited.
- **Chen et al., "Behavioral Entanglement" (arXiv 2604.07650)**: BEI/CIG framework across 18 LLMs; cross-family entanglement 40–60% lower than intra-family. Provides granular data but no certification framework.
- **Kong et al., "Multi-LLM Systems Exhibit Robust Semantic Collapse" (arXiv 2605.17193, May 2026)**: 12 intervention strategies fail to restore diversity in **closed-loop** interaction (200–1000 rounds). Proposal correctly distinguishes its single-pass protocol from this setting.
- **Horvath et al. (arXiv 2106.06946)**: √K certified radius via variance reduction for randomized smoothing in classifiers. This is the proof technique underlying the proposal's Ω(K_eff^{1/2}) bound.
- **Peer prediction with heterogeneous agents (Agarwal et al., ACM TEAC)**: Extends peer prediction to heterogeneous signal distributions but does NOT address degradation of dominant-strategy guarantees under **correlation** violation—confirming PEG degradation analysis is a genuine gap.
- **Certified robustness under heterogeneous perturbations (arXiv 2605.12876, May 2026)**: Very recent work extending randomized smoothing to heterogeneous input channels—the continuous/discrete distinction matters for certification, and LLM evaluation operates in a discrete perturbation space.
- **调研总结**: The field is converging on information-theoretic frameworks for LLM evaluation, with parallel threads in (a) diversity-scaling for accuracy, (b) single-judge adversarial bounds, and (c) correlated error measurement. The specific gap this proposal targets—**multi-judge adversarial scaling as a function of measurable correlation**—is confirmed to be open. The key tension in the field is between the aspiration to add more/diverse judges and the empirical finding that frontier models are inherently correlated.

---

【发掘点 1】
- 维度: 核心 claim 强化 / significance 提升
- 内容: **The "Frontier Diversity Ceiling" should be elevated to a co-equal motivating insight, not just an empirical contingency.** The current proposal treats Kim et al.'s finding (larger/more accurate models → more correlated errors, even across different providers/architectures) as an input parameter to be measured and accommodated. But this finding, combined with the proposal's own framework, implies a much more provocative and impactful result: **the certified manipulation-resistance of a judge ensemble may be fundamentally bounded at the frontier**. As model capability increases across the board, K_eff converges toward 1 regardless of architectural diversity, because capability convergence drives error correlation. This means the asymmetric dual has a second layer of asymmetry: not only does robustness scale polynomially (vs. exponential for accuracy), but the effective base K_eff itself *shrinks* as we move to more capable judges. This is a "ceiling theorem"—there may exist a regime where adding more frontier judges yields diminishing certified robustness returns approaching zero, even as accuracy continues to improve. If formalized (even as a conjecture with supporting evidence), this would transform the paper from "here's how to compute robustness bounds" to "here's a fundamental limit on the certifiability of LLM-based evaluation at the frontier"—a substantially higher-impact claim that would resonate with the evaluation community broadly.
- 价值: This raises the significance ceiling from "useful framework for practitioners" to "reveals a fundamental structural limitation of the LLM evaluation paradigm." It directly strengthens both Significance (the question becomes more important) and Novelty (the claim becomes more surprising). Reviewers are more likely to rate a paper highly when it reveals a tension or impossibility, not just when it provides a toolkit.
- 调研依据: Kim et al. (ICML 2025, arXiv 2506.07962)—the finding that "larger and more accurate models have highly correlated errors even with distinct architectures and providers" is the empirical foundation. Combined with the proposal's K_eff = 1+(K-1)·exp(-2·I_max) formula, as I_max → ∞ (high correlation), K_eff → 1 regardless of K.

【发掘点 2】
- 维度: novelty 锐化
- 内容: **Articulate the structural *reason* for the exponential-vs-polynomial asymmetry, not just its existence.** Currently, the proposal states the asymmetry as a proven fact: performance scales as (1-α_c)^{K*} (exponential) while robustness scales as Ω(K_eff^{1/2}) (polynomial). But the paper doesn't explain *why* these diverge at a structural level. The deep reason is likely this: for task performance (stochastic errors), each independent judge's error is drawn from a fixed distribution—independent noise averages out exponentially fast via concentration inequalities. For adversarial robustness, the adversary is *adaptive*—they can observe the protocol structure and correlate their attack across judges, effectively "re-coupling" what the ensemble tries to decouple. The polynomial bound reflects the fact that the adversary's perturbation budget is a shared resource that acts coherently across judges, whereas stochastic errors are incoherent. Making this structural explanation explicit—that **incoherent noise decays exponentially but coherent adversarial perturbation decays only polynomially because the adversary reintroduces cross-judge coupling**—would convert a "two results side by side" observation into a deep conceptual theorem. This is the difference between a technical result and a memorable insight that gets cited.
- 价值: Sharpens Novelty. Without the structural explanation, a skeptical reviewer could say "you proved two bounds and noticed they have different exponents—that's an observation, not a contribution." With the structural explanation, the asymmetry becomes an *explained phenomenon* with a causal mechanism, which is a qualitatively stronger theoretical contribution. It also opens the door to asking: are there aggregation protocols that can close this gap (making robustness super-polynomial), or is the polynomial ceiling fundamental?
- 调研依据: Based on the distinction between stochastic and adversarial settings that underpins the entire randomized smoothing literature (Horvath et al., arXiv 2106.06946; Cohen et al., 2019). The √K result in randomized smoothing is tight precisely because an adversary's perturbation is coherent—this structural reasoning extends naturally to the LLM evaluation setting.

【发掘点 3】
- 维度: trivial alternative 威胁
- 内容: **The tightness of the ½ exponent in Ω(K_eff^{1/2}) needs explicit theoretical interrogation—is it a fundamental limit or a proof artifact?** The ½ exponent comes from Horvath et al.'s variance reduction argument for randomized smoothing in ℓ₂ continuous perturbation spaces. But LLM evaluation operates in a **discrete** perturbation space (text manipulations). In discrete settings, the geometry of the perturbation space is fundamentally different—there is no smooth manifold to exploit. This raises two critical questions: (a) Could the true scaling be better than √K_eff in discrete settings (meaning the bound is loose and can be improved)? (b) Could it be worse (meaning the continuous-space analogy is optimistic)? If the ½ exponent is merely inherited from the continuous analogue without justification for the discrete case, a knowledgeable reviewer will flag this as a gap. The proposal should either: prove the ½ exponent is tight for the discrete evaluation setting (strongest), demonstrate a matching upper bound via the adaptive attacks (empirical tightness), or explicitly state the ½ exponent as a **conjecture** for discrete settings with the continuous-space result as evidence, and use the adaptive attack experiments to test it. The current proposal plans "best-effort tightness attack" experiments, which is good, but the theoretical status of the exponent should be crisply characterized upfront.
- 价值: This directly addresses Novelty robustness. If an information-theory-savvy reviewer asks "why does ½ hold in the discrete case?" and the paper has no answer, the core theoretical contribution is undermined. Proactively addressing this transforms a potential weakness into a demonstration of theoretical sophistication. It also opens a concrete direction for future work (tightening the bound for discrete evaluation) that adds to the paper's significance.
- 调研依据: Certified robustness under heterogeneous perturbations (arXiv 2605.12876, May 2026) explicitly addresses the continuous/discrete distinction for certification. The randomized smoothing survey (arXiv 2312.12608) discusses how certification radii depend on perturbation geometry.

【发掘点 4】
- 维度: significance 提升 / related work 差异化
- 内容: **The PEG degradation analysis could be positioned as an instance of a more general "certification degradation under correlation" meta-theorem, substantially broadening its impact.** Currently, the PEG analysis is framed narrowly: "PEG's Assumption 4 requires conditional independence; we characterize what happens when it's violated." This is valuable but sounds like a technical follow-up to PEG. A stronger framing: the conditional independence assumption is ubiquitous in information elicitation and peer prediction mechanisms (not just PEG). The specific degradation curve ε = f(ρ) under the copula model could apply to ANY mechanism that assumes conditionally independent reports—including Bayesian truth serum, DMI-mechanism more broadly, and the Correlated Agreement mechanism. If the degradation result is stated at this level of generality (with PEG as the worked-out case study), the paper speaks to the entire mechanism design community, not just the LLM evaluation community. This is the difference between "we extended PEG" and "we show that correlation structurally limits what incentive-compatible mechanisms can certify in multi-agent settings."
- 价值: Raises Significance substantially. The broader framing makes the paper relevant to mechanism design, peer prediction, and information elicitation communities—not just LLM-as-a-judge practitioners. It also strengthens Related Work differentiation: instead of being "downstream of PEG," the paper becomes "upstream of a class of mechanisms."
- 调研依据: Peer Prediction with Heterogeneous Users (Agarwal et al., ACM TEAC) and Peer Neighborhood Mechanisms (arXiv 2312.12303) both operate under independence-type assumptions. Neither provides degradation curves under correlation violation, confirming the generality of this gap.

【发掘点 5】
- 维度: 前提假设质疑
- 内容: **The additive information bound (K_eff · I_max total adversary information) in Step 1 of the proof needs careful justification for correlated channels.** The proposal states: "For K_eff effective independent channels, total adversary information gain per round is bounded additively at K_eff · I_max." This is correct for independent channels by definition—but the entire point of K_eff is to reduce K correlated channels to K_eff "effective" independent channels. The logical chain is: (correlated channels) → (compute K_eff) → (treat as K_eff independent channels) → (apply additive bound). The critical step is the first arrow: under what conditions does the copula correlation structure allow a clean reduction to K_eff independent channels? For the equicorrelated Gaussian case, this works via eigendecomposition (the proposal gives eigenvalues λ₁, λ₂). For heterogeneous correlation, using K* = 2^{H(ρ)} as a proxy is less rigorous—K* was derived for task performance scaling (Yang et al.), not adversarial information leakage. The proposal should explicitly prove (or at least argue convincingly) that K* is a valid effective dimensionality for the adversarial information bound, not just for the performance bound. If K*'s validity transfers only approximately, the bound should carry an explicit approximation factor. Without this, a theoretically rigorous reviewer could reject the heterogeneous-correlation claim as hand-waving.
- 价值: This is about Novelty integrity. If the proof's key step (using K* from the performance setting in the adversarial setting) is not justified, the theoretical contribution—which is the paper's core selling point—becomes questionable. Addressing this proactively either strengthens the proof (if the transfer is valid) or honestly scopes the claim (if it's approximate), both of which improve the paper.
- 调研依据: Yang et al. (arXiv 2602.03794) define K* for task performance contexts. The SDPI literature (Polyanskiy & Wu, arXiv 1508.06025) provides per-channel bounds but does not directly address the effective dimensionality reduction for correlated channels in adversarial settings. This is a gap the proposal needs to bridge explicitly.

---

Sources:
- [Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity](https://arxiv.org/abs/2602.03794)
- [Correlated Errors in Large Language Models](https://arxiv.org/abs/2506.07962)
- [Behavioral Entanglement in LLMs](https://arxiv.org/abs/2604.07650)
- [Multi-LLM Systems Exhibit Robust Semantic Collapse](https://arxiv.org/abs/2605.17193)
- [Security in LLM-as-a-Judge: A Comprehensive SoK](https://arxiv.org/pdf/2603.29403)
- [Boosting Randomized Smoothing with Variance Reduced Classifiers](https://arxiv.org/abs/2106.06946)
- [Strong Data-Processing Inequalities for Channels and Bayesian Networks](https://arxiv.org/abs/1508.06025)
- [Don't Always Pick the Highest-Performing Model](https://arxiv.org/abs/2602.08003)
- [Incentivizing Truthful Language Models via Peer Elicitation Games](https://arxiv.org/abs/2505.13636)
- [Let's Measure Information Step-by-Step](https://arxiv.org/abs/2508.05469)
- [Bits Leaked per Query](https://arxiv.org/pdf/2510.17000)
- [Certified Robustness under Heterogeneous Perturbations via Hybrid Randomized Smoothing](https://arxiv.org/html/2605.12876v1)
- [Trust, But Verify: A Survey of Randomized Smoothing Techniques](https://arxiv.org/html/2312.12608v1)
- [Peer Prediction with Heterogeneous Users](https://dl.acm.org/doi/10.1145/3381519)
- [Peer Neighborhood Mechanisms](https://arxiv.org/abs/2312.12303)
- [RobustJudge](https://arxiv.org/html/2506.09443v1)
- [Representational Collapse in Multi-Agent LLM Committees](https://arxiv.org/pdf/2604.03809)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33e832a6-2994-4aff-a46c-1b3b09315e6a",
  "isSidechain": false,
  "requestId": "req_011CbDGHNyZpZy5tU6C8ZqTb",
  "type": "assistant",
  "uuid": "1e0f34e1-fb92-4ffe-98f3-2e54232904b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pYP8Kj7mfrsvtKwheTzMR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3977,
      "cache_read_input_tokens": 32513,
      "output_tokens": 4173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3977,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4173,
          "cache_read_input_tokens": 32513,
          "cache_creation_input_tokens": 3977,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3977
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
  "lastPrompt": "# Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation Structure  ## Description  LLM evaluation faces systematic adversarial vulnera…",
  "leafUuid": "1e0f34e1-fb92-4ffe-98f3-2e54232904b5",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Certifiable multi-judge LLM evaluation robustness bounds",
  "sessionId": "87c2f497-fac4-4899-a042-3d8778958fbc"
}
```

---
