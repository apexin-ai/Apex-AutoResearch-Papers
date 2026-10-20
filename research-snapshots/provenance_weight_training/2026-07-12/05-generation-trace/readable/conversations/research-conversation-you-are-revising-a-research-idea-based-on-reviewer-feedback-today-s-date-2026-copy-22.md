# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-13 (UTC).** ## Original idea { "tit

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/d1da6575-a77d-4a5e-984b-7ebc8af7dd82.jsonl`
- **Structured JSON:** [`026d38571f4a95a980fc.json`](../../sessions/02/026d38571f4a95a980fc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T05:46:39.900Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T05:46:39.900Z",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-13 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Causal Token Selection for Invariant VLA Policies via Amortized Interventional Scoring\",\n  \"core_problem\": \"VLA models learn spurious visual correlations — attending to background textures, lighting conditions, and distractor objects that co-occur with target actions in training data — causing catastrophic failure under visual distribution shifts. Recent work (arXiv 2502.11501, ACL Findings 2025; arXiv 2512.07580, ICLR 2026) reveals two critical findings: (1) many attention-based token pruning methods underperform even naive random selection due to flawed scoring criteria, and (2) visual token information 'vanishes' in deep LLM layers, becoming uniformly uninformative beyond an 'information horizon' — meaning that any token selection must operate before this horizon. Meanwhile, a proliferation of concurrent VLA token selection methods (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, Compressor-VLA, Gaze-VLA — all 2025-2026) each propose different heuristic criteria (attention intersection, cross-attention TopK, Gumbel softmax, Kendall rank consistency, spatio-semantic dual-aware scoring, hierarchical importance, instruction-guided compression, gaze alignment), yet none provide formal justification for why their criterion identifies task-relevant tokens rather than merely attention-salient tokens. A complementary line of work addresses VLA spurious correlations via language-guided spatial reasoning (InSpire, arXiv 2505.13888), redirecting attention through prompting rather than principled token selection. Simple adaptation methods like FTM (arXiv 2512.02902) can recover substantial robustness with only 4K parameters, raising the question: can we identify *why* certain tokens matter and provide interpretable, formally grounded selection criteria rather than black-box affine recalibration?\",\n  \"opportunity\": \"Three research threads have developed in isolation: (1) causal intervention for imitation learning robustness (Causal-ACT, arXiv 2507.22380; ICIL, NeurIPS 2021), operating at the feature level in smaller architectures, (2) VLA token pruning for efficiency and robustness (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, VLA-Pruner, VLA-IAP, OTPrune, Compressor-VLA, SpecPrune-VLA, VLA-Cache), using attention/gradient/geometric/rank/temporal heuristics without causal grounding, and (3) causal attention distillation (LeaF, NeurIPS 2025) and learnable pruning (LearnPruner, arXiv 2604.23950), which move beyond pure attention heuristics but lack formal causal intervention criteria. A fourth thread — causality-inspired robustness theory — has recently achieved a breakthrough: CIRRL (arXiv 2505.12868) provides the first finite-radius robustness guarantee in nonlinear settings by combining identifiable representation learning with anchor regression, showing that operating at the representation level (where latent variables are identifiable up to affine transformation) is the key to extending causal robustness beyond linear models. A critical empirical finding connects these threads to VLA architectures specifically: visual tokens in VLA architectures preserve spatial correspondence to image patches at the vision encoder output (where SigLIP provides semantic and DINOv2 provides spatial features), but this spatial structure degrades progressively through LLM layers due to self-attention mixing, ultimately vanishing at an 'information horizon' (arXiv 2512.07580). This means token-level causal selection must operate at or near the vision encoder output — where spatial locality is preserved by construction — rather than at deep LLM layers where existing attention-based methods struggle (explaining why they often underperform random selection). The vision encoder output provides a form of identifiable representation (spatial correspondence = patch-level identifiability), analogous to CIRRL's requirement for identifiable latent variables, suggesting that representation-level causal robustness can extend to the VLA setting. Formalizing this insight via a structural causal model over the token-action pipeline, with amortized interventional scoring operating at the pre-LLM representation layer, would provide the principled criterion that existing pruning methods lack while operating in the representation space where the criterion is most valid.\",\n  \"landscape\": \"**Robustness benchmarking**: LIBERO-Plus (arXiv 2510.13626, CVPR 2026) demonstrates VLA catastrophic failures across 7 perturbation dimensions, with the current SOTA at 82.1% average success (SRPO, arXiv 2511.15605) — SRPO achieves 167% improvement over one-shot SFT baseline via self-referential RL without token selection. **Causal approaches in imitation learning**: Causal-ACT (arXiv 2507.22380, July 2025) integrates causal structure learning into ACT by learning binary causal graphs over ResNet features — achieving 0.82 OOD success on ALOHA cube transfer vs. 0.23 for standard ACT. However, it operates at the feature level in small architectures, uses heuristic energy-based graph search, and evaluates on a single simple task. ICIL (NeurIPS 2021) learns domain-invariant features for imitation but not at the token level. CLIP-ICM (ICML 2025) applies causal invariance to VLMs via SCMs but for classification, not action policies. **Spurious correlation mitigation via prompting**: InSpire (arXiv 2505.13888, May 2025) mitigates VLA spurious correlations by boosting spatial reasoning — prepending directional questions ('In which direction is [object] relative to the robot?') to redirect attention to task-relevant features. Achieves +6.2%/+10% on seen/unseen LIBERO tasks for miniVLA-VQ and +25%/+26% in real-world tasks for π0-FAST. Complementary approach (prompting-based attention redirection vs. CaTS's principled token selection); evaluated on standard LIBERO, not LIBERO-Plus perturbation dimensions. **Simple adaptation baselines**: FTM (arXiv 2512.02902) achieves 87.1% on LIBERO viewpoint with just 4K parameters via global affine token modulation; FLA extends to 90.8% with 4.7M parameters. Neither evaluated on full LIBERO-Plus; neither provides interpretability. **Active attention**: AVA-VLA (arXiv 2511.18960) dynamically reweights visual tokens via active attention, achieving 74.7% on LIBERO-Plus. **Causality-inspired robustness theory**: CIRRL (arXiv 2505.12868, May 2025) provides the first causality-inspired finite-radius robustness guarantee in nonlinear settings, using identifiable representation learning (Distributional Principal Autoencoders) to recover latent variables up to affine transformation, then applying anchor regression in the identifiable latent space. Key theorem: the two-step estimator achieves optimal worst-case risk among all L²-integrable functions under elliptical noise. Directly relevant to CaTS's theoretical framework — CIRRL validates the principle that representation-level causal robustness can overcome IRM/V-REx limitations, though its elliptical distribution assumptions and tabular data focus limit direct application to high-dimensional VLA visual tokens. CaTS's encoder-level scoring operates at a representation layer where spatial identifiability holds (analogous to CIRRL's affine identifiability), providing an empirical bridge between CIRRL's theory and VLA practice. **Concurrent VLA token pruning/selection methods (2025-2026) — all using heuristic criteria**: (i) SP-VLA (arXiv 2506.12723, ICLR 2026) jointly addresses temporal and spatial redundancy via action-aware model scheduling (switching between VLA and lightweight generator for deliberative vs. intuitive actions) and spatio-semantic dual-aware token pruning. Achieves 1.5× lossless acceleration on LIBERO and 2.4× on SimplerEnv with up to 6% performance gain. As an ICLR 2026 accepted paper, it represents the strongest efficiency-focused VLA pruning method. However, its spatio-semantic scoring criterion is designed for efficiency (removing redundant tokens) rather than robustness (removing spuriously correlated tokens) — a token may be spatially/semantically important yet causally spurious (e.g., a distinctive background element near the target object). Not evaluated under distribution shift. Code available on GitHub. (ii) DTP (arXiv 2601.16065, Jan 2026) prunes 'distracting tokens' via attention intersection scoring — tokens in task-irrelevant regions exceeding a scaled threshold of the maximum attention in task-relevant regions are pruned. Evaluated on SIMPLER, not LIBERO-Plus. Directly analogous motivation to CaTS (removing spuriously correlated tokens), but uses attention heuristics without formal justification that attention-salient ≠ causally relevant. Code available. (iii) FocusVLA (arXiv 2603.28740, Mar 2026) uses cross-attention-based TopK patch selection with modality cascaded attention, achieving 98.7% on standard LIBERO. Not evaluated on LIBERO-Plus; assumes cross-attention scores identify task relevance without causal validation. (iv) LightVLA (arXiv 2509.12594, ICRA 2026) uses Gumbel softmax for differentiable token selection, reducing FLOPs by 59.1% with 2.9% success rate improvement on LIBERO. End-to-end learned selection but criterion is implicitly defined by task loss — no interpretability or formal robustness criterion. (v) TIES (arXiv 2603.24941, Mar 2026) introduces Kendall rank consistency across layers as a stability metric, improving average success by 6% on CogACT+SIMPLER while reducing tokens by 78%. Most relevant concurrent work: uses rank consistency as a robustness signal, but this is a statistical regularity heuristic, not a causal criterion — rank consistency does not distinguish causal from spuriously consistent tokens. Not evaluated under environmental perturbations. (vi) BFA++ (arXiv 2602.20566, Feb 2026) uses hierarchical intra-view and inter-view importance predictors for multi-view VLAs. (vii) Compressor-VLA (arXiv 2511.18950) uses instruction-guided semantic and spatial compression modules, reducing visual tokens by 3× on LIBERO. (viii) Gaze-Regularized VLA (arXiv 2603.23202, Mar 2026) aligns attention with human gaze heatmaps via KL divergence. Requires human gaze data; provides indirect causal signal. (ix) LearnPruner (arXiv 2604.23950, Apr 2026) trains a learnable pruning module after the vision encoder, retaining only 5.5% of tokens while preserving ~95% performance. (x) SpecPrune-VLA (arXiv 2509.05614) uses action-aware self-speculative pruning with global history context, combining static action-level and dynamic layer-level pruning with an action-aware controller that classifies actions as coarse/fine-grained. Achieves 1.57× speedup on LIBERO and 1.70× in real-world with negligible degradation. Primarily efficiency-focused, exploiting temporal redundancy. (xi) VLA-Cache (arXiv 2502.02175, NeurIPS 2025) adaptively caches and reuses static visual tokens across consecutive frames via layer-adaptive token reusing, achieving 1.7× speedup with negligible success rate loss. Exploits temporal redundancy between adjacent observations — complementary to CaTS which addresses spatial token selection within a single frame for robustness rather than efficiency. **Token information dynamics**: arXiv 2512.07580 (ICLR 2026) discovers 'vanishing token information' — visual tokens progressively lose discriminative salience in deep LLM layers, becoming uniformly uninformative beyond an 'information horizon' (~layer 20 for general tasks, deeper for OCR). This explains why attention-based pruning in late layers underperforms random selection and motivates scoring at early/intermediate layers where spatial information is preserved. **Token pruning critique**: arXiv 2502.11501 (ACL Findings 2025) systematically shows many attention-based pruning methods underperform random selection due to position bias and flawed attention-as-importance assumptions. **Causal token pruning in NLP**: LeaF (NeurIPS 2025, arXiv 2506.07851) uses gradient-based teacher-student comparison to identify confounding tokens. Analogous in spirit but targets LLM reasoning, not embodied action; uses gradient heuristics, not formal interventions. **Robustness training**: RobustVLA (ICLR 2026, arXiv 2510.00037) uses offline robust optimization with 12.6% absolute gains on π0 backbone. **World models**: Mask World Model (arXiv 2604.19683) achieves 98.3% on standard LIBERO via geometric information bottleneck but not evaluated on LIBERO-Plus. **Shortcut learning**: arXiv 2508.06426 (CoRL 2025) identifies dataset diversity as root cause — complementary data-side approach. **Invariance theory limitations**: Rosenfeld et al. (ICLR 2021) demonstrate IRM fails in non-linear settings. V-REx (Krueger et al., ICML 2021) proposes variance-based risk extrapolation as simpler alternative but suffers similar non-linear limitations. CIRRL (arXiv 2505.12868) overcomes these limitations via identifiable representation learning but requires elliptical distribution assumptions. Wasserstein DRO (Kuhn et al., 2024) provides genuine finite-sample guarantees without requiring linear/invariance assumptions. **Amortized causal estimation**: CausalPFN (NeurIPS 2025) demonstrates amortized causal effect estimation via in-context learning with asymptotic consistency guarantees; ACTIVA (arXiv 2503.01290) uses transformer-based VAEs but is limited to tabular data. Amortized Shapley estimation (SurroShap, SimSHAP) provides non-asymptotic convergence bounds: Pr(|ϕ̂ − ϕ| ≥ ε) ≤ 2·exp(−2mε²/r²) for m samples and marginal contribution range r (Maleki et al., 2013). **No existing work combines formal token-level causal intervention criteria with amortized estimation in VLA transformers, operating at the vision encoder output where spatial locality is empirically validated, for cross-environment policy invariance.**\",\n  \"approach\": \"We propose Causal Token Selection (CaTS) v3, which identifies and retains visual tokens whose causal effect on action predictions is significant and stable across visual environments, using an amortized interventional scoring framework operating at the vision encoder output where spatial locality is empirically grounded.\\n\\n**Formal SCM for VLA Token-Action Pipeline.** We define a structural causal model: observation O is processed by the vision encoder into T(O) = {t_1,...,t_N} (N=256 for OpenVLA's SigLIP+DINOv2 encoder); each token t_i corresponds to an image patch and carries causal content C_i (object geometry, gripper state, contact regions) and spurious content S_i (background texture, lighting, distractor appearance); environment variable E influences S_i but not C_i; action A = π(f(T)) where f is the LLM backbone. We formalize the *encoder-level spatial locality* assumption (revised from the original spatial locality assumption): at the vision encoder output — before LLM self-attention layers mix token representations — causal content C_i is concentrated in a subset T* ⊂ T corresponding to image patches containing task-relevant objects, while spurious content S_i is distributed across patches containing background and distractors. **Justification**: this is grounded in two empirical findings: (a) DINOv2's attention maps show foreground object concentration by layers 3-6, with the CLS token primarily aggregating foreground tokens (arXiv 2602.22394); (b) the 'vanishing token information' phenomenon (arXiv 2512.07580) confirms that spatial discriminability is maximal at the vision encoder output and degrades through LLM depth. By scoring at the encoder output, CaTS operates precisely where the assumption is most valid, unlike methods scoring at deep LLM layers where information mixing undermines spatial selectivity. This encoder-level identifiability is analogous to CIRRL's (arXiv 2505.12868) key insight that robustness guarantees extend to nonlinear settings when operating on identifiable representations — the vision encoder's spatial correspondence provides patch-level identifiability that enables causal reasoning at the token level.\\n\\n**Multi-Layer Scoring Architecture.** Rather than scoring tokens at a single layer (where the spatial locality / information quality tradeoff is unclear), CaTS employs a two-stage scoring approach: (1) *Primary scoring* at the vision encoder output (post-MLP projection, pre-LLM), where spatial locality is strongest. (2) *Optional refinement scoring* at an intermediate LLM layer (before the information horizon, empirically determined per-model via the protocol of arXiv 2512.07580 — typically layer 8-15 for 7B models), capturing cross-modal relevance signals that emerge only after some language-vision interaction. The two scores are combined via a learned convex combination α·s_encoder + (1-α)·s_intermediate, where α is a learnable scalar. **Degradation analysis**: we formally analyze how the ε-invariance bound degrades as spatial locality weakens (parameterized by α_leak = fraction of causal information C_i that 'leaks' to non-corresponding tokens through self-attention). When α_leak is high (poor spatial locality at the scoring layer), the bound degrades gracefully — the theory predicts diminishing returns of causal selection over random pruning, which is empirically testable.\\n\\n**Theorem (Conditional Invariance) with Approximate Constants.** Under four assumptions — (A1) causal sufficiency: A ⊥ E | C(T*); (A2) token-level identifiability: do(t_i) changes C(T*) with positive probability for t_i ∈ T*; (A3) environment diversity: training environments span relevant E dimensions; (A4) bounded amortization error of the causal scorer — the causal token selection operator S_τ with threshold τ satisfies:\\n\\n*Concrete bound*: max_{e,e'} |R(π,e) - R(π,e')| ≤ ε(N_env, M, τ, α_leak) where:\\nε = C₁/√M + C₂·exp(-c·N_env/d_E) + C₃·α_leak·g(τ) + ε_amort\\n\\n**Approximate constant estimates (order-of-magnitude):**\\n\\n- *C₁/√M (Shapley estimation error)*: Using the Hoeffding-based bound from Maleki et al. (2013): Pr(|ϕ̂ − ϕ| ≥ ε) ≤ 2·exp(−2Mε²/r²), where r is the range of marginal contributions. With action loss normalized to [0,1] (r=1) and confidence δ=0.05: C₁ = r·√(ln(2/δ)/2) ≈ 1.36. With M=200 Shapley samples per token: C₁/√M ≈ 0.096. With M=500: ≈ 0.061. **Practical implication**: M=200 samples (200 forward passes per scored token, feasible with batch inference) yields estimation error below 0.1, sufficient for reliable token ranking.\\n\\n- *C₂·exp(-c·N_env/d_E) (environment coverage gap)*: d_E ≈ 7 for LIBERO-Plus's 7 perturbation dimensions (camera, robot, language, light, background, noise, layout). With N_env = 35 distinct environments (7 dimensions × 5 perturbation levels each) and c ≈ 0.5-1.0 (standard covering-number scaling for bounded domains): exp(-c·35/7) = exp(-2.5 to -5.0) ≈ 0.007-0.082. With C₂ ≈ 1 (bounded loss): this term contributes ≈ 0.01-0.08. **Practical implication**: 35 environments across 7 dimensions make this term small; the bound suggests N_env = Ω(d_E · log(1/δ)) ≈ 21 environments suffice for δ=0.05, which LIBERO-Plus comfortably exceeds.\\n\\n- *C₃·α_leak·g(τ) (spatial locality violation)*: α_leak is empirically measurable — at the vision encoder output, we estimate α_leak ≈ 0.05-0.15 (based on DINOv2's foreground concentration in layers 3-6, arXiv 2602.22394); at intermediate LLM layer ~10, α_leak ≈ 0.3-0.5; beyond the information horizon (layer 20+), α_leak → 1.0. With g(τ) ≈ (1-τ)/τ for pruning ratio τ and C₃ ≈ 1: at encoder output with τ=0.5 (50% pruning), C₃·α_leak·g(τ) ≈ 0.1·1.0 = 0.10. At layer 20+ with α_leak ≈ 1.0: this term ≈ 1.0, dominating the bound and explaining why late-layer pruning degenerates to random selection.\\n\\n- *ε_amort (amortization gap)*: ε_amort ≤ ε_approx(W,d) + ε_stat(n_train). For a 2-layer MLP scorer with W=512 hidden units on d=1024-dimensional token embeddings: ε_approx = O(1/√W) ≈ 0.044 (for Barron-class functions); ε_stat = O(1/√n_train) ≈ 0.01 for n_train=10,000 training interventions. Total ε_amort ≈ 0.054.\\n\\n**Overall bound estimate**: At the vision encoder output with M=200, N_env=35, α_leak=0.1, τ=0.5: ε ≈ 0.096 + 0.01 + 0.10 + 0.054 ≈ 0.26. This predicts a maximum cross-environment performance gap of ~26% — a testable prediction against the empirically observed ~50-65% gap for unmodified VLAs on LIBERO-Plus. The bound tightens substantially with M=500 (ε ≈ 0.22) and with higher pruning threshold τ=0.7 (ε ≈ 0.20).\\n\\n**Full proof strategy**: The proof proceeds in three steps: (1) show that under A1-A2, exact token-level ACE identifies T* (follows from standard do-calculus); (2) bound the approximation error when ACE is estimated from M samples via Shapley decomposition (using Hoeffding-type concentration on bounded action losses, directly applying the non-asymptotic bound from Maleki et al., 2013); (3) bound the error from amortizing the Shapley estimates via a neural network (using universal approximation for Barron-class functions + Rademacher complexity of the MLP hypothesis class). Step (3) yields the ε_amort term.\\n\\n**Failure modes (explicit with analysis):** (F1) Insufficient environment diversity violates A3 — same limitation as IRM/V-REx, partially addressed by CIRRL's identifiable representation approach but CIRRL requires elliptical distribution assumptions that may not hold for VLA visual tokens. Mitigation: LIBERO-Plus provides 7 perturbation dimensions with ~35 environments; we report per-dimension results to identify which dimensions have sufficient diversity. (F2) Spatial locality violation at scoring layer (high α_leak). Mitigation: multi-layer scoring allows operating at the layer with lowest α_leak; we empirically measure α_leak by comparing per-token ACE computed at encoder output vs. intermediate LLM layers. (F3) Amortization gap (see detailed analysis below). (F4) V-REx variance penalty limitations in non-linear settings — see honest framing below.\\n\\n**Amortized Causal Scoring (ACS) with Quantified Amortization Gap.** We train a lightweight causal scoring head attached to the frozen VLA backbone. Training data is generated via *batch stochastic interventions*: for randomly sampled token subsets across LIBERO-Plus perturbation environments, we replace token embeddings with environment-marginal statistics and measure KL divergence in action distributions. A Shapley-value-inspired decomposition attributes group effects to individual tokens. The scorer (2-layer MLP with width 512, <1M parameters) learns to predict token-level causal effects from token embeddings.\\n\\n**Amortization gap analysis**: The gap between the learned scorer s_θ(t_i) and the true ACE(t_i) is bounded by: ε_amort ≤ ε_approx(W, d) + ε_stat(n_train) where ε_approx(W, d) = O(1/√W) ≈ 0.044 for W=512 (for Barron-class functions on compact domains), and ε_stat(n_train) = O(1/√n_train) ≈ 0.01 for n_train=10,000 training interventions. **Central validation protocol** (not merely an ablation): we compute exact ACE on a validation set of 50 tokens × 5 environments (250 forward passes per token = 12,500 total, feasible) and report: (a) Pearson/Spearman correlation between s_θ and exact ACE; (b) mean absolute error; (c) rank agreement (does s_θ rank tokens in the same order as exact ACE?). The amortized scorer is considered validated if rank-order Spearman ρ > 0.8 and the scoring threshold τ selects a token set overlapping ≥ 85% with the exact-ACE-selected set. If validation fails, we fall back to exact ACE computation at inference (trading efficiency for correctness), which remains a viable contribution.\\n\\n**Composite Robustness Objective (honest framing with V-REx/DRO interaction analysis).** We do NOT claim to solve the non-linear invariance problem. Instead, we use a *composite robustness objective* combining three components: (1) Standard action prediction loss on selected tokens: L_task = E_e[L(π(S_τ(T)), a*)]. (2) V-REx-style variance penalty: L_var = Var_e(L(π(S_τ(T)), a*)), which penalizes cross-environment loss variance. We frame this honestly as a *practical heuristic* that is simpler and more stable than IRMv1 (Krueger et al., ICML 2021) but shares the same fundamental limitation in non-linear settings: it does not distinguish between underfitting and inherent noise, and can fail under heteroskedastic environments. (3) Wasserstein DRO regularization: L_DRO = sup_{Q: W(Q,P̂)≤ρ} E_Q[L], providing finite-sample robustness guarantees (Kuhn et al., 2024) that do not require linear assumptions.\\n\\n**V-REx and DRO interaction analysis.** The two regularizers target complementary failure modes but can interact non-trivially. *When complementary*: V-REx stabilizes performance across *known* training environments by penalizing loss variance — preventing environment-specific overfitting where the model excels in one environment but fails in others. DRO provides robustness to *unseen* environments within the Wasserstein ball — guarding against distributional shift at test time. Together, they create a 'robust-within-uniform' objective: the policy must perform uniformly across training environments (V-REx) while being robust to perturbations of each environment's distribution (DRO). *When potentially conflicting*: DRO with large radius ρ may concentrate model capacity on worst-case distributions, potentially increasing cross-environment variance to better handle the hardest cases — precisely what V-REx penalizes. *Resolution*: for small-to-moderate DRO radius ρ, Wasserstein DRO is equivalent to variation regularization (Kuhn et al., 2024), making the two objectives approximately aligned. In practice, we operate with moderate ρ where the Wasserstein ball captures realistic perturbations (calibrated to LIBERO-Plus perturbation magnitudes) rather than adversarial worst cases. The sensitivity analysis (ablation c) explicitly measures the V-REx/DRO tradeoff by sweeping λ_var and λ_DRO independently and jointly, reporting both average performance and cross-environment variance to identify the Pareto frontier. We note that CIRRL (arXiv 2505.12868) offers a principled alternative — identifiable representation learning followed by anchor regression — that avoids the V-REx/DRO tension entirely, but requires elliptical distribution assumptions that we cannot verify for VLA visual tokens; adapting CIRRL's framework to VLA architectures is an important direction for future work.\\n\\nThe combined loss is L = L_task + λ_var·L_var + λ_DRO·L_DRO, where λ_var and λ_DRO are hyperparameters with explicit sensitivity analysis. We expect V-REx to provide better empirical performance in practice (as observed in prior work) while DRO provides the theoretical safety net.\\n\\n**Architecture.** Frozen OpenVLA-OFT backbone (7B). The ACS head operates at the vision encoder output (post-projection), with optional refinement at an intermediate LLM layer. Total trainable parameters: ACS scoring head (~0.5M) + thin LoRA adaptation (~3.5M) = ~4M total. At inference, the scorer assigns causal scores to all visual tokens in a single forward pass; tokens below threshold τ are pruned before entering the LLM backbone, providing both robustness and efficiency.\\n\\n**Evaluation with Formal Statistical Protocol.** Primary benchmark: LIBERO-Plus across all 7 perturbation dimensions. Primary metric: average success rate under distribution shift.\\n\\n**Statistical protocol against random pruning** (addressing arXiv 2502.11501's findings): We adopt a paired bootstrap protocol with bias-corrected accelerated (BCa) confidence intervals and sign-flip permutation tests (following arXiv 2511.19794). Specifically: (a) train CaTS and random-pruning variants under identical conditions with 5 random seeds; (b) record per-seed, per-task success rate differences; (c) compute BCa 95% confidence intervals on the mean difference; (d) perform sign-flip permutation test (10,000 permutations) for each perturbation dimension. CaTS claims significant improvement only if the BCa interval lies entirely above zero AND the permutation p-value < 0.05. *A priori success criterion*: CaTS must significantly outperform random pruning on at least 5 of 7 perturbation dimensions. If this criterion is not met, we report the negative result transparently and analyze which perturbation types resist causal selection (contributing understanding of when causal criteria matter vs. when random suffices).\\n\\n**Baselines (8 core, with code availability assessment).** We streamline from 11 to 8 core baselines, prioritizing those with available code or reproducible implementations on LIBERO-Plus, and dropping baselines requiring non-trivial cross-architecture adaptation:\\n\\n(1) SRPO (arXiv 2511.15605) — current LIBERO-Plus SOTA (82.1%). Evaluated in original LIBERO-Plus paper; results directly comparable. (2) FTM/FLA (arXiv 2512.02902) — simple adaptation baseline. Reproduced on LIBERO-Plus; FTM requires only 4K trainable parameters, making reproduction straightforward even without official code (single affine transform layer). (3) AVA-VLA (arXiv 2511.18960) — active visual attention, 74.7% on LIBERO-Plus. Already evaluated on LIBERO-Plus in original work. (4) RobustVLA (ICLR 2026, arXiv 2510.00037) — offline robust optimization, directly targets VLA robustness. ICLR 2026 accepted, code expected. (5) DTP (arXiv 2601.16065) — most directly analogous concurrent work (attention-based distractor identification). Code available at anonymous repository. Requires adaptation to LIBERO-Plus (originally evaluated on SIMPLER). (6) TIES (arXiv 2603.24941) — most sophisticated heuristic baseline (inter-layer rank consistency). Code availability: pending. Method is training-free and well-specified, making reimplementation feasible. (7) VLA-Pruner (arXiv 2511.16449) — temporal-aware dual-level pruning. Code available on GitHub (MINT-SJTU/VLA-Pruner). (8) Random token pruning — critical control baseline, trivial to implement.\\n\\n**Baselines discussed but not reproduced (with justification)**: Causal-ACT (feature-level ResNet+ACT architecture → token-level OpenVLA adaptation requires non-trivial architectural changes beyond a fair comparison). LeaF-adapted (NLP reasoning → VLA action policies requires speculative adaptation with unclear design choices). FocusVLA, LightVLA, BFA++, Compressor-VLA (not evaluated on LIBERO-Plus; codebases target different VLA architectures). SP-VLA, SpecPrune-VLA, VLA-Cache (efficiency-focused methods exploiting temporal redundancy; not evaluated under distribution shift; complementary rather than competing with CaTS's robustness objective). InSpire (prompting-based approach, orthogonal mechanism targeting same problem; could be combined with CaTS in future work). These are all discussed in the landscape section with explicit differentiation.\\n\\n**Ablations**: (a) amortized vs. exact ACE (central validation, not just ablation); (b) encoder-level vs. intermediate-layer vs. late-layer scoring (testing spatial locality assumption directly); (c) V-REx only vs. DRO only vs. composite objective (including joint λ_var × λ_DRO sensitivity sweep to characterize the interaction frontier and identify the complementary vs. conflicting regime); (d) variance penalty weight sensitivity; (e) DRO radius ρ sensitivity (calibrated against LIBERO-Plus perturbation magnitudes); (f) pruning ratio sweep (10-90%); (g) per-perturbation-dimension analysis; (h) causal score interpretability analysis (do high-scoring tokens correspond to task-relevant regions via IoU with ground-truth object masks?); (i) α_leak measurement across layers.\\n\\n**Key differentiations from all concurrent work.** The central claim is not merely that causal criteria exist, but that they provide *measurably better token selection than heuristic alternatives* — the burden of proof is on CaTS, and the evaluation is designed to test this rigorously.\\n\\nvs. SP-VLA (ICLR 2026): SP-VLA jointly optimizes temporal scheduling and spatial token pruning for efficiency — its spatio-semantic criterion identifies tokens that are spatially/semantically redundant but not necessarily causally spurious. A background token near the target object may have high spatio-semantic importance (spatially close, semantically related to the scene) yet be causally irrelevant to the action. CaTS's interventional criterion tests causal relevance directly via environment-marginal replacement. The two approaches are potentially complementary: SP-VLA for temporal efficiency, CaTS for causal robustness within each selected frame.\\n\\nvs. DTP (arXiv 2601.16065): DTP uses attention intersection heuristics (tokens in irrelevant regions with attention exceeding scaled threshold are pruned). CaTS uses formal causal intervention criteria. DTP's attention-based scoring is exactly the type shown to be unreliable by arXiv 2502.11501; CaTS's causal scoring is designed to be the principled alternative. Empirical comparison on LIBERO-Plus will directly test whether causal grounding outperforms attention-based distractor identification.\\n\\nvs. FocusVLA (arXiv 2603.28740): FocusVLA uses cross-attention TopK selection + modality cascaded attention, achieving strong results on standard LIBERO (98.7%) but without robustness evaluation. CaTS targets robustness under distribution shift specifically. FocusVLA's TopK is a differentiable selection mechanism but provides no criterion for *which* tokens matter for cross-environment generalization.\\n\\nvs. LightVLA (arXiv 2509.12594): LightVLA learns token selection end-to-end via Gumbel softmax — the selection criterion is implicitly defined by the training loss and may overfit to spurious correlations in training environments. CaTS's explicit causal criterion is designed to prevent exactly this overfitting.\\n\\nvs. TIES (arXiv 2603.24941): TIES uses inter-layer rank consistency (Kendall τ) as a stability signal — an innovative heuristic that captures token 'reliability' across layers. However, rank consistency does not distinguish between causally relevant tokens and tokens that are consistently spurious (e.g., a distinctive background element present in all training scenes would have high rank consistency but is causally irrelevant). CaTS's interventional scoring directly tests causal relevance via environment-marginal replacement.\\n\\nvs. InSpire (arXiv 2505.13888): InSpire redirects VLA attention via language prompting (spatial reasoning questions), achieving an indirect form of spurious correlation mitigation without token-level selection. CaTS operates at the token level with formal causal criteria. The two approaches are complementary — InSpire provides a zero-cost attention redirect while CaTS provides principled token selection with theoretical guarantees. Future work could combine InSpire's spatial prompting with CaTS's causal scoring.\\n\\nvs. CIRRL (arXiv 2505.12868): CIRRL provides finite-radius nonlinear robustness via identifiable representation learning, but operates on tabular data with elliptical distribution assumptions. CaTS draws theoretical inspiration from CIRRL's key insight (representation-level identifiability enables causal robustness) while adapting to the VLA setting where visual encoder outputs provide spatial patch-level identifiability. CaTS's DRO component provides analogous finite-sample guarantees without requiring elliptical assumptions.\\n\\nvs. Gaze-VLA (arXiv 2603.23202): Uses human gaze as an indirect causal signal (humans look at task-relevant regions). Requires gaze data collection; gaze provides a noisy proxy for causal relevance (humans also look at salient distractors). CaTS derives causal relevance from the model's own action predictions under intervention.\\n\\nvs. Causal-ACT (arXiv 2507.22380): Token-level in 7B VLA (not feature-level in ResNet+ACT); amortized scoring (not heuristic graph search); comprehensive LIBERO-Plus evaluation; concrete ε-invariance bound with approximate constants.\\n\\nvs. FTM: Interpretable per-token causal scores (not black-box affine transform); selective token removal (not global recalibration); formal robustness criterion.\\n\\nvs. LeaF (NeurIPS 2025): VLA action policies (not NLP reasoning); cross-environment interventional scoring (not single-domain gradient heuristics); formal SCM (not teacher-student comparison).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~800h A100 (80GB): ~350h for 22-28 LoRA fine-tuning runs with ACS head at ~14h each (including multi-layer scoring variants and composite objective hyperparameter search), ~250h for batch intervention data generation, amortized scorer training, and exact ACE validation (12,500 forward passes for validation set + systematic coverage across 7 perturbation types), ~200h for baseline reproduction (DTP and TIES reproduction on LIBERO-Plus, FTM on LIBERO-Plus, 8 baselines total with 5 seeds each for statistical protocol) and ablations\",\n      \"gpu_utilization\": \"Low (~25-30%). GPUs sit idle during code development, causal scoring pipeline debugging, statistical protocol implementation, α_leak measurement analysis, and theorem proof development.\",\n      \"timeline\": \"4-6 months\",\n      \"team\": \"1-2 researchers (one with causal inference/DRO background for theorem formalization and proof, one with VLA/robotics experience for implementation and evaluation)\",\n      \"estimated_gpu_cost\": \"~$640 (800h × $0.80/hr A100 spot/discount pricing from specialized providers such as Thunder Compute or TensorDock, May 2026 market rate; range $0.78-$1.07/hr across providers)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~1200h A100 (80GB): agent explores ~40-50 training configurations more systematically, runs comprehensive ablations across all 7 perturbation dimensions with 5 seeds, evaluates all 8 baselines, and performs extensive α_leak measurements across layers\",\n      \"gpu_utilization\": \"Moderate (~50-60%). Agent queues experiments faster but pauses at approval gates for: multi-layer scoring architecture decisions, DRO radius selection, amortization validation thresholds, theorem assumption checking.\",\n      \"timeline\": \"2-4 months\",\n      \"team\": \"1 researcher, ~45min/day check-in for approving experiment plans, reviewing causal score visualizations, validating amortization gap measurements, and verifying theorem proof steps\",\n      \"claude_api_cost\": \"$500-700 (5000-7000 conversation turns for experiment design, code generation, theorem checking, statistical protocol implementation, result analysis)\",\n      \"estimated_gpu_cost\": \"~$960 (1200h × $0.80/hr)\",\n      \"risk_note\": \"Amortized scorer validation (Spearman ρ > 0.8 threshold) requires careful human judgment — if the scorer barely misses the threshold, the decision to proceed with amortized vs. exact scoring has significant downstream implications. DRO radius selection and the V-REx/DRO tradeoff require human expertise. Theorem proof needs verification by someone with expertise in both causal inference and approximation theory.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~2500h A100 (80GB): agent runs 120-150 experiment configurations including aggressive sweeps for scoring layer selection, V-REx/DRO weight ratios, pruning ratios, Shapley approximation methods, scorer architectures (varying width W), plus all baseline reproductions with 5 seeds and failed exploration runs\",\n      \"gpu_utilization\": \"High (~90%+). Agent queues next experiment immediately upon completion. Continuous 24/7 execution.\",\n      \"timeline\": \"3-5 weeks with 4-8 concurrent A100s; as few as 8-10 days with 16 concurrent GPUs\",\n      \"team\": \"0 (initial setup: configure LIBERO-Plus environments, OpenVLA-OFT checkpoint, define intervention distribution, implement statistical testing protocol, implement α_leak measurement)\",\n      \"claude_api_cost\": \"$700-1100 (7000-11000 turns for autonomous experiment design, debugging, statistical analysis, and paper drafting)\",\n      \"estimated_gpu_cost\": \"~$2,000 (2500h × $0.80/hr)\",\n      \"speed_bottleneck\": \"Number of concurrent A100 GPU instances. Secondary: intervention data generation is I/O-intensive (requires rendering perturbation environments). Statistical protocol with 5 seeds × 8 baselines × 7 perturbation dimensions requires organized experiment management.\",\n      \"risk_note\": \"Without human gates, agent may over-explore suboptimal scoring layer combinations or DRO radius values. The theorem formalization cannot be fully automated — agent-generated proofs require expert verification, especially the amortization gap bound (step 3 of the proof involving Rademacher complexity). The statistical protocol is automatable but interpretation of borderline results (e.g., CaTS significant on 4/7 dimensions vs. the a priori 5/7 criterion) requires human judgment. Risk mitigation: pre-define structured search space with early stopping on amortization validation metrics; halt if Spearman ρ < 0.6 after initial scorer training.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (deadline: ~August 1, 2026 — primary target, sufficient time for theoretical development, multi-layer scoring implementation, and statistical evaluation)\",\n    \"ICLR 2027 (deadline: ~October 2026 — strong target, allows comprehensive evaluation and concurrent work comparison)\",\n    \"ICRA 2027 (deadline: ~September 2026 — robotics venue, good fit for empirical contribution)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations [Causal-ACT] (arXiv 2507.22380, July 2025)\",\n    \"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling [FTM/FLA] (arXiv 2512.02902, Dec 2025)\",\n    \"Learning to Focus: Causal Attention Distillation via Gradient-Guided Token Pruning [LeaF] (NeurIPS 2025, arXiv 2506.07851)\",\n    \"Shortcut Learning in Generalist Robot Policies: The Role of Dataset Diversity and Fragmentation (CoRL 2025, arXiv 2508.06426)\",\n    \"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem? (ACL Findings 2025, arXiv 2502.11501)\",\n    \"When Token Pruning is Worse than Random: Understanding Visual Token Information in VLLMs (ICLR 2026, arXiv 2512.07580)\",\n    \"The Risks of Invariant Risk Minimization (ICLR 2021, arXiv 2010.05761)\",\n    \"Out-of-Distribution Generalization via Risk Extrapolation [V-REx] (ICML 2021, arXiv 2003.00688)\",\n    \"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models (arXiv 2511.15605)\",\n    \"AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention (arXiv 2511.18960)\",\n    \"ACTIVA: Amortized Causal Effect Estimation via Transformer-based Variational Autoencoder (arXiv 2503.01290)\",\n    \"CausalPFN: Amortized Causal Effect Estimation via In-Context Learning (NeurIPS 2025, arXiv 2506.07918)\",\n    \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026, arXiv 2510.13626)\",\n    \"Invariant Causal Imitation Learning for Generalizable Policies [ICIL] (NeurIPS 2021)\",\n    \"DTP: A Simple yet Effective Distracting Token Pruning Framework for VLA Models (arXiv 2601.16065, Jan 2026)\",\n    \"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models (arXiv 2603.28740, Mar 2026)\",\n    \"LightVLA: Towards Efficient VLA Models via Differentiable Token Pruning (ICRA 2026, arXiv 2509.12594)\",\n    \"TIES: Beyond Attention Magnitude — Leveraging Inter-layer Rank Consistency for Efficient VLA Models (arXiv 2603.24941, Mar 2026)\",\n    \"BFA++: Hierarchical Best-Feature-Aware Token Pruning for Multi-View VLA Models (arXiv 2602.20566, Feb 2026)\",\n    \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation (arXiv 2511.18950)\",\n    \"Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation (arXiv 2603.23202, Mar 2026)\",\n    \"LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models (arXiv 2604.23950, Apr 2026)\",\n    \"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations [RobustVLA] (ICLR 2026, arXiv 2510.00037)\",\n    \"Mask World Model: Predicting What Matters for Robust Robot Policy Learning (arXiv 2604.19683, April 2026)\",\n    \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient VLA Inference (arXiv 2511.16449)\",\n    \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for VLA Models (arXiv 2603.22991, March 2026)\",\n    \"Learning Invariant Causal Mechanism from Vision-Language Models [CLIP-ICM] (ICML 2025, arXiv 2405.15289)\",\n    \"OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport (arXiv 2602.20205)\",\n    \"Wasserstein Distributionally Robust Optimization and Variation Regularization (Operations Research, 2024)\",\n    \"Finite-Sample Guarantees for Wasserstein DRO: Breaking the Curse of Dimensionality (Operations Research, 2023)\",\n    \"Vision Transformers Need More Than Registers (arXiv 2602.22394, Feb 2026)\",\n    \"Bounding the Estimation Error of Sampling-based Shapley Value Approximation (arXiv 1306.4265)\",\n    \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success [OpenVLA-OFT] (arXiv 2025)\",\n    \"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration (ICLR 2026, arXiv 2506.12723)\",\n    \"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning (arXiv 2509.05614)\",\n    \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching (NeurIPS 2025, arXiv 2502.02175)\",\n    \"InSpire: Vision-Language-Action Models with Intrinsic Spatial Reasoning (arXiv 2505.13888, May 2025)\",\n    \"Causality-Inspired Robustness for Nonlinear Models via Representation Learning [CIRRL] (arXiv 2505.12868, May 2025)\"\n  ],\n  \"description\": \"VLA models suffer catastrophic failures under visual distribution shifts, yet a proliferation of concurrent token pruning methods (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, Compressor-VLA, Gaze-VLA — all 2025-2026) each propose different heuristic criteria without formal justification, and recent work shows many attention-based methods underperform random selection (arXiv 2502.11501) due to 'vanishing token information' in deep layers (arXiv 2512.07580). We propose Causal Token Selection (CaTS) v3, bridging three disconnected threads: VLA token pruning, causal intervention for imitation learning (Causal-ACT, ICIL), and causal attention distillation (LeaF), while drawing theoretical inspiration from CIRRL's (arXiv 2505.12868) breakthrough showing that representation-level identifiability enables nonlinear causal robustness guarantees. CaTS defines a formal SCM over the VLA token-action pipeline with a revised *encoder-level spatial locality* assumption — grounded in empirical findings that DINOv2/SigLIP encoder outputs preserve spatial correspondence (a form of patch-level identifiability analogous to CIRRL's affine identifiability) while LLM self-attention progressively mixes token information. Key advances over v2: (1) Multi-layer scoring at vision encoder output (where spatial locality is empirically validated) with optional intermediate-layer refinement. (2) Concrete ε-invariance bound with approximate constants: ε = C₁/√M + C₂·exp(-c·N_env/d_E) + C₃·α_leak·g(τ) + ε_amort, with order-of-magnitude estimates (M=200 Shapley samples → estimation error ~0.096; N_env=35 across d_E=7 dimensions → coverage term ~0.01; encoder-level α_leak≈0.1 → locality term ~0.10; overall ε≈0.26, a testable prediction against the observed ~50-65% gap for unmodified VLAs). (3) Honest composite robustness objective combining V-REx (practical heuristic) with Wasserstein DRO (finite-sample guarantees), including explicit analysis of their interaction: complementary for moderate DRO radius ρ (V-REx stabilizes known environments, DRO guards against unseen shifts; for small ρ, Wasserstein DRO approximates variation regularization, aligning with V-REx), with potential conflict at large ρ resolved by operating in the moderate-ρ regime calibrated to LIBERO-Plus perturbation magnitudes. (4) Quantified amortization gap: ε_amort ≤ O(1/√W) + O(1/√n_train) ≈ 0.054 for W=512, n_train=10K, with central validation protocol (Spearman ρ > 0.8). (5) Formal statistical protocol against random pruning with a priori 5/7 dimension criterion. Evaluated against 8 core baselines (streamlined from 11 with explicit code availability assessment: VLA-Pruner and DTP have public code; TIES is training-free and reimplementable; FTM is trivially reimplementable) including SRPO (82.1% SOTA), DTP, TIES, and VLA-Pruner. Concurrent efficiency-focused methods (SP-VLA ICLR 2026, SpecPrune-VLA, VLA-Cache NeurIPS 2025) are discussed as complementary — targeting temporal/spatial redundancy rather than causal robustness. InSpire (arXiv 2505.13888) is discussed as a complementary prompting-based approach to the same spurious correlation problem. GPU costs updated to current May 2026 market rates ($0.80/hr A100 spot from specialized providers). Primary targets: AAAI 2027 and ICLR 2027.\",\n  \"project_name\": \"causal_token_sel_vla\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 4)\nIssues: [\"MISSING RELATED WORK — ViT-Shapley (ICLR 2023 Oral, arXiv 2206.05282): 'Learning to Estimate Shapley Values with Vision Transformers' demonstrates amortized Shapley value estimation for ViT tokens using a learned explainer model that generates per-patch importance scores in a single forward pass. This is the most direct technical predecessor to CaTS's amortized causal scoring head — both train a lightweight model to predict per-token Shapley-style importance scores from token embeddings. The key difference (interventional/causal effects for cross-environment invariance vs. observational Shapley for model explanation) must be explicitly discussed. The ViT-Shapley code is publicly available and its attention masking approach for evaluating ViTs with partial information is directly applicable to CaTS's intervention mechanism.\", \"MISSING RELATED WORK — Mechanistic Interpretability for Steering VLA Models (CoRL 2025, arXiv 2509.00328): This paper uses activation patching / causal tracing on VLA internal representations (OpenVLA, Pi0) to identify sparse semantic directions causally linked to action selection, enabling zero-shot behavioral steering without fine-tuning. While it operates at the neuron/direction level rather than the token level, it demonstrates that interventional methods can identify causal structure in VLA representations — validating CaTS's premise. Evaluated on LIBERO and real UR5 robot. Should be cited as evidence that causal/interventional analysis of VLA representations is feasible and informative.\", \"VLM→VLA EXTRAPOLATION UNACKNOWLEDGED: The 'vanishing token information' paper (arXiv 2512.07580) evaluates VLMs (Qwen2.5-VL, LLaVA-1.5), not VLAs. The proposal treats its findings as directly applicable to VLA architectures (OpenVLA) without acknowledging this extrapolation. While VLAs share the VLM backbone architecture making extrapolation reasonable, VLA models have different training objectives (action prediction vs. text generation) and different attention patterns (action tokens attend to visual tokens differently than text tokens). The information horizon position may differ for VLAs. This should be noted as an assumption requiring empirical verification in the evaluation.\", \"MISSING CONCURRENT WORK — Test-Time Perturbation Learning with Delayed Feedback (arXiv 2604.18107, April 2026): PDF addresses VLA spurious correlations ('trajectory overfitting where VLAs over-attend to spurious correlation between actions and entities') via test-time adaptation with uncertainty-based augmentation and action voting. Achieves +7.4% on LIBERO. While complementary (test-time adaptation vs. training-time causal selection), it targets the exact same core problem and should be discussed.\"]\nFeedback: The proposal has improved dramatically across 3 rounds and is now close to passing. The remaining issues are targeted and fixable:\n\n1. **Cite ViT-Shapley (ICLR 2023 Oral)**: This is the most important addition. CaTS's amortized scoring head is technically similar to ViT-Shapley's learned explainer — both train a model to predict per-token importance from embeddings in a single forward pass. Differentiation: (a) ViT-Shapley estimates observational Shapley values for model explanation; CaTS estimates interventional causal effects via environment-marginal replacement for cross-environment invariance. (b) ViT-Shapley's masking evaluates prediction change; CaTS's intervention evaluates action distribution stability across environments. (c) CaTS's scorer is trained on multi-environment intervention data, not single-distribution Shapley estimates. The ViT-Shapley codebase (github.com/suinleelab/vit-shapley) could inform implementation.\n\n2. **Cite Mechanistic Interpretability for VLA Steering (CoRL 2025)**: This validates CaTS's core premise — that interventional methods can identify causally relevant structure in VLA representations. Differentiate: it operates at neuron/direction level for behavioral steering, while CaTS operates at token level for robustness-oriented selection.\n\n3. **Acknowledge the VLM→VLA extrapolation**: Add one sentence noting that arXiv 2512.07580 evaluates VLMs, and verifying the information horizon in VLA architectures (where action prediction creates different attention dynamics) is part of the empirical contribution (ablation b already tests this implicitly).\n\n4. **Briefly mention PDF (arXiv 2604.18107)**: As a complementary test-time approach to the same spurious correlation problem. Could potentially be combined with CaTS (CaTS for training-time causal selection + PDF for test-time adaptation).\n\nWith these additions, the novelty differentiation will be stronger (CaTS goes beyond ViT-Shapley by targeting interventional rather than observational importance, beyond mechanistic interpretability by operating at token level for robustness rather than direction level for steering) and the landscape coverage will be complete.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 4 轮修订，近 3 轮的平均分从 3.6 到 3.9，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-13T05:46:39.908Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T05:46:39.908Z",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82"
}
```

---

## Round 1

56 recorded events

### User

_source line 3 · 2026-05-13T05:46:39.967Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-13 (UTC).**

## Original idea
{
  "title": "Causal Token Selection for Invariant VLA Policies via Amortized Interventional Scoring",
  "core_problem": "VLA models learn spurious visual correlations — attending to background textures, lighting conditions, and distractor objects that co-occur with target actions in training data — causing catastrophic failure under visual distribution shifts. Recent work (arXiv 2502.11501, ACL Findings 2025; arXiv 2512.07580, ICLR 2026) reveals two critical findings: (1) many attention-based token pruning methods underperform even naive random selection due to flawed scoring criteria, and (2) visual token information 'vanishes' in deep LLM layers, becoming uniformly uninformative beyond an 'information horizon' — meaning that any token selection must operate before this horizon. Meanwhile, a proliferation of concurrent VLA token selection methods (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, Compressor-VLA, Gaze-VLA — all 2025-2026) each propose different heuristic criteria (attention intersection, cross-attention TopK, Gumbel softmax, Kendall rank consistency, spatio-semantic dual-aware scoring, hierarchical importance, instruction-guided compression, gaze alignment), yet none provide formal justification for why their criterion identifies task-relevant tokens rather than merely attention-salient tokens. A complementary line of work addresses VLA spurious correlations via language-guided spatial reasoning (InSpire, arXiv 2505.13888), redirecting attention through prompting rather than principled token selection. Simple adaptation methods like FTM (arXiv 2512.02902) can recover substantial robustness with only 4K parameters, raising the question: can we identify *why* certain tokens matter and provide interpretable, formally grounded selection criteria rather than black-box affine recalibration?",
  "opportunity": "Three research threads have developed in isolation: (1) causal intervention for imitation learning robustness (Causal-ACT, arXiv 2507.22380; ICIL, NeurIPS 2021), operating at the feature level in smaller architectures, (2) VLA token pruning for efficiency and robustness (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, VLA-Pruner, VLA-IAP, OTPrune, Compressor-VLA, SpecPrune-VLA, VLA-Cache), using attention/gradient/geometric/rank/temporal heuristics without causal grounding, and (3) causal attention distillation (LeaF, NeurIPS 2025) and learnable pruning (LearnPruner, arXiv 2604.23950), which move beyond pure attention heuristics but lack formal causal intervention criteria. A fourth thread — causality-inspired robustness theory — has recently achieved a breakthrough: CIRRL (arXiv 2505.12868) provides the first finite-radius robustness guarantee in nonlinear settings by combining identifiable representation learning with anchor regression, showing that operating at the representation level (where latent variables are identifiable up to affine transformation) is the key to extending causal robustness beyond linear models. A critical empirical finding connects these threads to VLA architectures specifically: visual tokens in VLA architectures preserve spatial correspondence to image patches at the vision encoder output (where SigLIP provides semantic and DINOv2 provides spatial features), but this spatial structure degrades progressively through LLM layers due to self-attention mixing, ultimately vanishing at an 'information horizon' (arXiv 2512.07580). This means token-level causal selection must operate at or near the vision encoder output — where spatial locality is preserved by construction — rather than at deep LLM layers where existing attention-based methods struggle (explaining why they often underperform random selection). The vision encoder output provides a form of identifiable representation (spatial correspondence = patch-level identifiability), analogous to CIRRL's requirement for identifiable latent variables, suggesting that representation-level causal robustness can extend to the VLA setting. Formalizing this insight via a structural causal model over the token-action pipeline, with amortized interventional scoring operating at the pre-LLM representation layer, would provide the principled criterion that existing pruning methods lack while operating in the representation space where the criterion is most valid.",
  "landscape": "**Robustness benchmarking**: LIBERO-Plus (arXiv 2510.13626, CVPR 2026) demonstrates VLA catastrophic failures across 7 perturbation dimensions, with the current SOTA at 82.1% average success (SRPO, arXiv 2511.15605) — SRPO achieves 167% improvement over one-shot SFT baseline via self-referential RL without token selection. **Causal approaches in imitation learning**: Causal-ACT (arXiv 2507.22380, July 2025) integrates causal structure learning into ACT by learning binary causal graphs over ResNet features — achieving 0.82 OOD success on ALOHA cube transfer vs. 0.23 for standard ACT. However, it operates at the feature level in small architectures, uses heuristic energy-based graph search, and evaluates on a single simple task. ICIL (NeurIPS 2021) learns domain-invariant features for imitation but not at the token level. CLIP-ICM (ICML 2025) applies causal invariance to VLMs via SCMs but for classification, not action policies. **Spurious correlation mitigation via prompting**: InSpire (arXiv 2505.13888, May 2025) mitigates VLA spurious correlations by boosting spatial reasoning — prepending directional questions ('In which direction is [object] relative to the robot?') to redirect attention to task-relevant features. Achieves +6.2%/+10% on seen/unseen LIBERO tasks for miniVLA-VQ and +25%/+26% in real-world tasks for π0-FAST. Complementary approach (prompting-based attention redirection vs. CaTS's principled token selection); evaluated on standard LIBERO, not LIBERO-Plus perturbation dimensions. **Simple adaptation baselines**: FTM (arXiv 2512.02902) achieves 87.1% on LIBERO viewpoint with just 4K parameters via global affine token modulation; FLA extends to 90.8% with 4.7M parameters. Neither evaluated on full LIBERO-Plus; neither provides interpretability. **Active attention**: AVA-VLA (arXiv 2511.18960) dynamically reweights visual tokens via active attention, achieving 74.7% on LIBERO-Plus. **Causality-inspired robustness theory**: CIRRL (arXiv 2505.12868, May 2025) provides the first causality-inspired finite-radius robustness guarantee in nonlinear settings, using identifiable representation learning (Distributional Principal Autoencoders) to recover latent variables up to affine transformation, then applying anchor regression in the identifiable latent space. Key theorem: the two-step estimator achieves optimal worst-case risk among all L²-integrable functions under elliptical noise. Directly relevant to CaTS's theoretical framework — CIRRL validates the principle that representation-level causal robustness can overcome IRM/V-REx limitations, though its elliptical distribution assumptions and tabular data focus limit direct application to high-dimensional VLA visual tokens. CaTS's encoder-level scoring operates at a representation layer where spatial identifiability holds (analogous to CIRRL's affine identifiability), providing an empirical bridge between CIRRL's theory and VLA practice. **Concurrent VLA token pruning/selection methods (2025-2026) — all using heuristic criteria**: (i) SP-VLA (arXiv 2506.12723, ICLR 2026) jointly addresses temporal and spatial redundancy via action-aware model scheduling (switching between VLA and lightweight generator for deliberative vs. intuitive actions) and spatio-semantic dual-aware token pruning. Achieves 1.5× lossless acceleration on LIBERO and 2.4× on SimplerEnv with up to 6% performance gain. As an ICLR 2026 accepted paper, it represents the strongest efficiency-focused VLA pruning method. However, its spatio-semantic scoring criterion is designed for efficiency (removing redundant tokens) rather than robustness (removing spuriously correlated tokens) — a token may be spatially/semantically important yet causally spurious (e.g., a distinctive background element near the target object). Not evaluated under distribution shift. Code available on GitHub. (ii) DTP (arXiv 2601.16065, Jan 2026) prunes 'distracting tokens' via attention intersection scoring — tokens in task-irrelevant regions exceeding a scaled threshold of the maximum attention in task-relevant regions are pruned. Evaluated on SIMPLER, not LIBERO-Plus. Directly analogous motivation to CaTS (removing spuriously correlated tokens), but uses attention heuristics without formal justification that attention-salient ≠ causally relevant. Code available. (iii) FocusVLA (arXiv 2603.28740, Mar 2026) uses cross-attention-based TopK patch selection with modality cascaded attention, achieving 98.7% on standard LIBERO. Not evaluated on LIBERO-Plus; assumes cross-attention scores identify task relevance without causal validation. (iv) LightVLA (arXiv 2509.12594, ICRA 2026) uses Gumbel softmax for differentiable token selection, reducing FLOPs by 59.1% with 2.9% success rate improvement on LIBERO. End-to-end learned selection but criterion is implicitly defined by task loss — no interpretability or formal robustness criterion. (v) TIES (arXiv 2603.24941, Mar 2026) introduces Kendall rank consistency across layers as a stability metric, improving average success by 6% on CogACT+SIMPLER while reducing tokens by 78%. Most relevant concurrent work: uses rank consistency as a robustness signal, but this is a statistical regularity heuristic, not a causal criterion — rank consistency does not distinguish causal from spuriously consistent tokens. Not evaluated under environmental perturbations. (vi) BFA++ (arXiv 2602.20566, Feb 2026) uses hierarchical intra-view and inter-view importance predictors for multi-view VLAs. (vii) Compressor-VLA (arXiv 2511.18950) uses instruction-guided semantic and spatial compression modules, reducing visual tokens by 3× on LIBERO. (viii) Gaze-Regularized VLA (arXiv 2603.23202, Mar 2026) aligns attention with human gaze heatmaps via KL divergence. Requires human gaze data; provides indirect causal signal. (ix) LearnPruner (arXiv 2604.23950, Apr 2026) trains a learnable pruning module after the vision encoder, retaining only 5.5% of tokens while preserving ~95% performance. (x) SpecPrune-VLA (arXiv 2509.05614) uses action-aware self-speculative pruning with global history context, combining static action-level and dynamic layer-level pruning with an action-aware controller that classifies actions as coarse/fine-grained. Achieves 1.57× speedup on LIBERO and 1.70× in real-world with negligible degradation. Primarily efficiency-focused, exploiting temporal redundancy. (xi) VLA-Cache (arXiv 2502.02175, NeurIPS 2025) adaptively caches and reuses static visual tokens across consecutive frames via layer-adaptive token reusing, achieving 1.7× speedup with negligible success rate loss. Exploits temporal redundancy between adjacent observations — complementary to CaTS which addresses spatial token selection within a single frame for robustness rather than efficiency. **Token information dynamics**: arXiv 2512.07580 (ICLR 2026) discovers 'vanishing token information' — visual tokens progressively lose discriminative salience in deep LLM layers, becoming uniformly uninformative beyond an 'information horizon' (~layer 20 for general tasks, deeper for OCR). This explains why attention-based pruning in late layers underperforms random selection and motivates scoring at early/intermediate layers where spatial information is preserved. **Token pruning critique**: arXiv 2502.11501 (ACL Findings 2025) systematically shows many attention-based pruning methods underperform random selection due to position bias and flawed attention-as-importance assumptions. **Causal token pruning in NLP**: LeaF (NeurIPS 2025, arXiv 2506.07851) uses gradient-based teacher-student comparison to identify confounding tokens. Analogous in spirit but targets LLM reasoning, not embodied action; uses gradient heuristics, not formal interventions. **Robustness training**: RobustVLA (ICLR 2026, arXiv 2510.00037) uses offline robust optimization with 12.6% absolute gains on π0 backbone. **World models**: Mask World Model (arXiv 2604.19683) achieves 98.3% on standard LIBERO via geometric information bottleneck but not evaluated on LIBERO-Plus. **Shortcut learning**: arXiv 2508.06426 (CoRL 2025) identifies dataset diversity as root cause — complementary data-side approach. **Invariance theory limitations**: Rosenfeld et al. (ICLR 2021) demonstrate IRM fails in non-linear settings. V-REx (Krueger et al., ICML 2021) proposes variance-based risk extrapolation as simpler alternative but suffers similar non-linear limitations. CIRRL (arXiv 2505.12868) overcomes these limitations via identifiable representation learning but requires elliptical distribution assumptions. Wasserstein DRO (Kuhn et al., 2024) provides genuine finite-sample guarantees without requiring linear/invariance assumptions. **Amortized causal estimation**: CausalPFN (NeurIPS 2025) demonstrates amortized causal effect estimation via in-context learning with asymptotic consistency guarantees; ACTIVA (arXiv 2503.01290) uses transformer-based VAEs but is limited to tabular data. Amortized Shapley estimation (SurroShap, SimSHAP) provides non-asymptotic convergence bounds: Pr(|ϕ̂ − ϕ| ≥ ε) ≤ 2·exp(−2mε²/r²) for m samples and marginal contribution range r (Maleki et al., 2013). **No existing work combines formal token-level causal intervention criteria with amortized estimation in VLA transformers, operating at the vision encoder output where spatial locality is empirically validated, for cross-environment policy invariance.**",
  "approach": "We propose Causal Token Selection (CaTS) v3, which identifies and retains visual tokens whose causal effect on action predictions is significant and stable across visual environments, using an amortized interventional scoring framework operating at the vision encoder output where spatial locality is empirically grounded.\n\n**Formal SCM for VLA Token-Action Pipeline.** We define a structural causal model: observation O is processed by the vision encoder into T(O) = {t_1,...,t_N} (N=256 for OpenVLA's SigLIP+DINOv2 encoder); each token t_i corresponds to an image patch and carries causal content C_i (object geometry, gripper state, contact regions) and spurious content S_i (background texture, lighting, distractor appearance); environment variable E influences S_i but not C_i; action A = π(f(T)) where f is the LLM backbone. We formalize the *encoder-level spatial locality* assumption (revised from the original spatial locality assumption): at the vision encoder output — before LLM self-attention layers mix token representations — causal content C_i is concentrated in a subset T* ⊂ T corresponding to image patches containing task-relevant objects, while spurious content S_i is distributed across patches containing background and distractors. **Justification**: this is grounded in two empirical findings: (a) DINOv2's attention maps show foreground object concentration by layers 3-6, with the CLS token primarily aggregating foreground tokens (arXiv 2602.22394); (b) the 'vanishing token information' phenomenon (arXiv 2512.07580) confirms that spatial discriminability is maximal at the vision encoder output and degrades through LLM depth. By scoring at the encoder output, CaTS operates precisely where the assumption is most valid, unlike methods scoring at deep LLM layers where information mixing undermines spatial selectivity. This encoder-level identifiability is analogous to CIRRL's (arXiv 2505.12868) key insight that robustness guarantees extend to nonlinear settings when operating on identifiable representations — the vision encoder's spatial correspondence provides patch-level identifiability that enables causal reasoning at the token level.\n\n**Multi-Layer Scoring Architecture.** Rather than scoring tokens at a single layer (where the spatial locality / information quality tradeoff is unclear), CaTS employs a two-stage scoring approach: (1) *Primary scoring* at the vision encoder output (post-MLP projection, pre-LLM), where spatial locality is strongest. (2) *Optional refinement scoring* at an intermediate LLM layer (before the information horizon, empirically determined per-model via the protocol of arXiv 2512.07580 — typically layer 8-15 for 7B models), capturing cross-modal relevance signals that emerge only after some language-vision interaction. The two scores are combined via a learned convex combination α·s_encoder + (1-α)·s_intermediate, where α is a learnable scalar. **Degradation analysis**: we formally analyze how the ε-invariance bound degrades as spatial locality weakens (parameterized by α_leak = fraction of causal information C_i that 'leaks' to non-corresponding tokens through self-attention). When α_leak is high (poor spatial locality at the scoring layer), the bound degrades gracefully — the theory predicts diminishing returns of causal selection over random pruning, which is empirically testable.\n\n**Theorem (Conditional Invariance) with Approximate Constants.** Under four assumptions — (A1) causal sufficiency: A ⊥ E | C(T*); (A2) token-level identifiability: do(t_i) changes C(T*) with positive probability for t_i ∈ T*; (A3) environment diversity: training environments span relevant E dimensions; (A4) bounded amortization error of the causal scorer — the causal token selection operator S_τ with threshold τ satisfies:\n\n*Concrete bound*: max_{e,e'} |R(π,e) - R(π,e')| ≤ ε(N_env, M, τ, α_leak) where:\nε = C₁/√M + C₂·exp(-c·N_env/d_E) + C₃·α_leak·g(τ) + ε_amort\n\n**Approximate constant estimates (order-of-magnitude):**\n\n- *C₁/√M (Shapley estimation error)*: Using the Hoeffding-based bound from Maleki et al. (2013): Pr(|ϕ̂ − ϕ| ≥ ε) ≤ 2·exp(−2Mε²/r²), where r is the range of marginal contributions. With action loss normalized to [0,1] (r=1) and confidence δ=0.05: C₁ = r·√(ln(2/δ)/2) ≈ 1.36. With M=200 Shapley samples per token: C₁/√M ≈ 0.096. With M=500: ≈ 0.061. **Practical implication**: M=200 samples (200 forward passes per scored token, feasible with batch inference) yields estimation error below 0.1, sufficient for reliable token ranking.\n\n- *C₂·exp(-c·N_env/d_E) (environment coverage gap)*: d_E ≈ 7 for LIBERO-Plus's 7 perturbation dimensions (camera, robot, language, light, background, noise, layout). With N_env = 35 distinct environments (7 dimensions × 5 perturbation levels each) and c ≈ 0.5-1.0 (standard covering-number scaling for bounded domains): exp(-c·35/7) = exp(-2.5 to -5.0) ≈ 0.007-0.082. With C₂ ≈ 1 (bounded loss): this term contributes ≈ 0.01-0.08. **Practical implication**: 35 environments across 7 dimensions make this term small; the bound suggests N_env = Ω(d_E · log(1/δ)) ≈ 21 environments suffice for δ=0.05, which LIBERO-Plus comfortably exceeds.\n\n- *C₃·α_leak·g(τ) (spatial locality violation)*: α_leak is empirically measurable — at the vision encoder output, we estimate α_leak ≈ 0.05-0.15 (based on DINOv2's foreground concentration in layers 3-6, arXiv 2602.22394); at intermediate LLM layer ~10, α_leak ≈ 0.3-0.5; beyond the information horizon (layer 20+), α_leak → 1.0. With g(τ) ≈ (1-τ)/τ for pruning ratio τ and C₃ ≈ 1: at encoder output with τ=0.5 (50% pruning), C₃·α_leak·g(τ) ≈ 0.1·1.0 = 0.10. At layer 20+ with α_leak ≈ 1.0: this term ≈ 1.0, dominating the bound and explaining why late-layer pruning degenerates to random selection.\n\n- *ε_amort (amortization gap)*: ε_amort ≤ ε_approx(W,d) + ε_stat(n_train). For a 2-layer MLP scorer with W=512 hidden units on d=1024-dimensional token embeddings: ε_approx = O(1/√W) ≈ 0.044 (for Barron-class functions); ε_stat = O(1/√n_train) ≈ 0.01 for n_train=10,000 training interventions. Total ε_amort ≈ 0.054.\n\n**Overall bound estimate**: At the vision encoder output with M=200, N_env=35, α_leak=0.1, τ=0.5: ε ≈ 0.096 + 0.01 + 0.10 + 0.054 ≈ 0.26. This predicts a maximum cross-environment performance gap of ~26% — a testable prediction against the empirically observed ~50-65% gap for unmodified VLAs on LIBERO-Plus. The bound tightens substantially with M=500 (ε ≈ 0.22) and with higher pruning threshold τ=0.7 (ε ≈ 0.20).\n\n**Full proof strategy**: The proof proceeds in three steps: (1) show that under A1-A2, exact token-level ACE identifies T* (follows from standard do-calculus); (2) bound the approximation error when ACE is estimated from M samples via Shapley decomposition (using Hoeffding-type concentration on bounded action losses, directly applying the non-asymptotic bound from Maleki et al., 2013); (3) bound the error from amortizing the Shapley estimates via a neural network (using universal approximation for Barron-class functions + Rademacher complexity of the MLP hypothesis class). Step (3) yields the ε_amort term.\n\n**Failure modes (explicit with analysis):** (F1) Insufficient environment diversity violates A3 — same limitation as IRM/V-REx, partially addressed by CIRRL's identifiable representation approach but CIRRL requires elliptical distribution assumptions that may not hold for VLA visual tokens. Mitigation: LIBERO-Plus provides 7 perturbation dimensions with ~35 environments; we report per-dimension results to identify which dimensions have sufficient diversity. (F2) Spatial locality violation at scoring layer (high α_leak). Mitigation: multi-layer scoring allows operating at the layer with lowest α_leak; we empirically measure α_leak by comparing per-token ACE computed at encoder output vs. intermediate LLM layers. (F3) Amortization gap (see detailed analysis below). (F4) V-REx variance penalty limitations in non-linear settings — see honest framing below.\n\n**Amortized Causal Scoring (ACS) with Quantified Amortization Gap.** We train a lightweight causal scoring head attached to the frozen VLA backbone. Training data is generated via *batch stochastic interventions*: for randomly sampled token subsets across LIBERO-Plus perturbation environments, we replace token embeddings with environment-marginal statistics and measure KL divergence in action distributions. A Shapley-value-inspired decomposition attributes group effects to individual tokens. The scorer (2-layer MLP with width 512, <1M parameters) learns to predict token-level causal effects from token embeddings.\n\n**Amortization gap analysis**: The gap between the learned scorer s_θ(t_i) and the true ACE(t_i) is bounded by: ε_amort ≤ ε_approx(W, d) + ε_stat(n_train) where ε_approx(W, d) = O(1/√W) ≈ 0.044 for W=512 (for Barron-class functions on compact domains), and ε_stat(n_train) = O(1/√n_train) ≈ 0.01 for n_train=10,000 training interventions. **Central validation protocol** (not merely an ablation): we compute exact ACE on a validation set of 50 tokens × 5 environments (250 forward passes per token = 12,500 total, feasible) and report: (a) Pearson/Spearman correlation between s_θ and exact ACE; (b) mean absolute error; (c) rank agreement (does s_θ rank tokens in the same order as exact ACE?). The amortized scorer is considered validated if rank-order Spearman ρ > 0.8 and the scoring threshold τ selects a token set overlapping ≥ 85% with the exact-ACE-selected set. If validation fails, we fall back to exact ACE computation at inference (trading efficiency for correctness), which remains a viable contribution.\n\n**Composite Robustness Objective (honest framing with V-REx/DRO interaction analysis).** We do NOT claim to solve the non-linear invariance problem. Instead, we use a *composite robustness objective* combining three components: (1) Standard action prediction loss on selected tokens: L_task = E_e[L(π(S_τ(T)), a*)]. (2) V-REx-style variance penalty: L_var = Var_e(L(π(S_τ(T)), a*)), which penalizes cross-environment loss variance. We frame this honestly as a *practical heuristic* that is simpler and more stable than IRMv1 (Krueger et al., ICML 2021) but shares the same fundamental limitation in non-linear settings: it does not distinguish between underfitting and inherent noise, and can fail under heteroskedastic environments. (3) Wasserstein DRO regularization: L_DRO = sup_{Q: W(Q,P̂)≤ρ} E_Q[L], providing finite-sample robustness guarantees (Kuhn et al., 2024) that do not require linear assumptions.\n\n**V-REx and DRO interaction analysis.** The two regularizers target complementary failure modes but can interact non-trivially. *When complementary*: V-REx stabilizes performance across *known* training environments by penalizing loss variance — preventing environment-specific overfitting where the model excels in one environment but fails in others. DRO provides robustness to *unseen* environments within the Wasserstein ball — guarding against distributional shift at test time. Together, they create a 'robust-within-uniform' objective: the policy must perform uniformly across training environments (V-REx) while being robust to perturbations of each environment's distribution (DRO). *When potentially conflicting*: DRO with large radius ρ may concentrate model capacity on worst-case distributions, potentially increasing cross-environment variance to better handle the hardest cases — precisely what V-REx penalizes. *Resolution*: for small-to-moderate DRO radius ρ, Wasserstein DRO is equivalent to variation regularization (Kuhn et al., 2024), making the two objectives approximately aligned. In practice, we operate with moderate ρ where the Wasserstein ball captures realistic perturbations (calibrated to LIBERO-Plus perturbation magnitudes) rather than adversarial worst cases. The sensitivity analysis (ablation c) explicitly measures the V-REx/DRO tradeoff by sweeping λ_var and λ_DRO independently and jointly, reporting both average performance and cross-environment variance to identify the Pareto frontier. We note that CIRRL (arXiv 2505.12868) offers a principled alternative — identifiable representation learning followed by anchor regression — that avoids the V-REx/DRO tension entirely, but requires elliptical distribution assumptions that we cannot verify for VLA visual tokens; adapting CIRRL's framework to VLA architectures is an important direction for future work.\n\nThe combined loss is L = L_task + λ_var·L_var + λ_DRO·L_DRO, where λ_var and λ_DRO are hyperparameters with explicit sensitivity analysis. We expect V-REx to provide better empirical performance in practice (as observed in prior work) while DRO provides the theoretical safety net.\n\n**Architecture.** Frozen OpenVLA-OFT backbone (7B). The ACS head operates at the vision encoder output (post-projection), with optional refinement at an intermediate LLM layer. Total trainable parameters: ACS scoring head (~0.5M) + thin LoRA adaptation (~3.5M) = ~4M total. At inference, the scorer assigns causal scores to all visual tokens in a single forward pass; tokens below threshold τ are pruned before entering the LLM backbone, providing both robustness and efficiency.\n\n**Evaluation with Formal Statistical Protocol.** Primary benchmark: LIBERO-Plus across all 7 perturbation dimensions. Primary metric: average success rate under distribution shift.\n\n**Statistical protocol against random pruning** (addressing arXiv 2502.11501's findings): We adopt a paired bootstrap protocol with bias-corrected accelerated (BCa) confidence intervals and sign-flip permutation tests (following arXiv 2511.19794). Specifically: (a) train CaTS and random-pruning variants under identical conditions with 5 random seeds; (b) record per-seed, per-task success rate differences; (c) compute BCa 95% confidence intervals on the mean difference; (d) perform sign-flip permutation test (10,000 permutations) for each perturbation dimension. CaTS claims significant improvement only if the BCa interval lies entirely above zero AND the permutation p-value < 0.05. *A priori success criterion*: CaTS must significantly outperform random pruning on at least 5 of 7 perturbation dimensions. If this criterion is not met, we report the negative result transparently and analyze which perturbation types resist causal selection (contributing understanding of when causal criteria matter vs. when random suffices).\n\n**Baselines (8 core, with code availability assessment).** We streamline from 11 to 8 core baselines, prioritizing those with available code or reproducible implementations on LIBERO-Plus, and dropping baselines requiring non-trivial cross-architecture adaptation:\n\n(1) SRPO (arXiv 2511.15605) — current LIBERO-Plus SOTA (82.1%). Evaluated in original LIBERO-Plus paper; results directly comparable. (2) FTM/FLA (arXiv 2512.02902) — simple adaptation baseline. Reproduced on LIBERO-Plus; FTM requires only 4K trainable parameters, making reproduction straightforward even without official code (single affine transform layer). (3) AVA-VLA (arXiv 2511.18960) — active visual attention, 74.7% on LIBERO-Plus. Already evaluated on LIBERO-Plus in original work. (4) RobustVLA (ICLR 2026, arXiv 2510.00037) — offline robust optimization, directly targets VLA robustness. ICLR 2026 accepted, code expected. (5) DTP (arXiv 2601.16065) — most directly analogous concurrent work (attention-based distractor identification). Code available at anonymous repository. Requires adaptation to LIBERO-Plus (originally evaluated on SIMPLER). (6) TIES (arXiv 2603.24941) — most sophisticated heuristic baseline (inter-layer rank consistency). Code availability: pending. Method is training-free and well-specified, making reimplementation feasible. (7) VLA-Pruner (arXiv 2511.16449) — temporal-aware dual-level pruning. Code available on GitHub (MINT-SJTU/VLA-Pruner). (8) Random token pruning — critical control baseline, trivial to implement.\n\n**Baselines discussed but not reproduced (with justification)**: Causal-ACT (feature-level ResNet+ACT architecture → token-level OpenVLA adaptation requires non-trivial architectural changes beyond a fair comparison). LeaF-adapted (NLP reasoning → VLA action policies requires speculative adaptation with unclear design choices). FocusVLA, LightVLA, BFA++, Compressor-VLA (not evaluated on LIBERO-Plus; codebases target different VLA architectures). SP-VLA, SpecPrune-VLA, VLA-Cache (efficiency-focused methods exploiting temporal redundancy; not evaluated under distribution shift; complementary rather than competing with CaTS's robustness objective). InSpire (prompting-based approach, orthogonal mechanism targeting same problem; could be combined with CaTS in future work). These are all discussed in the landscape section with explicit differentiation.\n\n**Ablations**: (a) amortized vs. exact ACE (central validation, not just ablation); (b) encoder-level vs. intermediate-layer vs. late-layer scoring (testing spatial locality assumption directly); (c) V-REx only vs. DRO only vs. composite objective (including joint λ_var × λ_DRO sensitivity sweep to characterize the interaction frontier and identify the complementary vs. conflicting regime); (d) variance penalty weight sensitivity; (e) DRO radius ρ sensitivity (calibrated against LIBERO-Plus perturbation magnitudes); (f) pruning ratio sweep (10-90%); (g) per-perturbation-dimension analysis; (h) causal score interpretability analysis (do high-scoring tokens correspond to task-relevant regions via IoU with ground-truth object masks?); (i) α_leak measurement across layers.\n\n**Key differentiations from all concurrent work.** The central claim is not merely that causal criteria exist, but that they provide *measurably better token selection than heuristic alternatives* — the burden of proof is on CaTS, and the evaluation is designed to test this rigorously.\n\nvs. SP-VLA (ICLR 2026): SP-VLA jointly optimizes temporal scheduling and spatial token pruning for efficiency — its spatio-semantic criterion identifies tokens that are spatially/semantically redundant but not necessarily causally spurious. A background token near the target object may have high spatio-semantic importance (spatially close, semantically related to the scene) yet be causally irrelevant to the action. CaTS's interventional criterion tests causal relevance directly via environment-marginal replacement. The two approaches are potentially complementary: SP-VLA for temporal efficiency, CaTS for causal robustness within each selected frame.\n\nvs. DTP (arXiv 2601.16065): DTP uses attention intersection heuristics (tokens in irrelevant regions with attention exceeding scaled threshold are pruned). CaTS uses formal causal intervention criteria. DTP's attention-based scoring is exactly the type shown to be unreliable by arXiv 2502.11501; CaTS's causal scoring is designed to be the principled alternative. Empirical comparison on LIBERO-Plus will directly test whether causal grounding outperforms attention-based distractor identification.\n\nvs. FocusVLA (arXiv 2603.28740): FocusVLA uses cross-attention TopK selection + modality cascaded attention, achieving strong results on standard LIBERO (98.7%) but without robustness evaluation. CaTS targets robustness under distribution shift specifically. FocusVLA's TopK is a differentiable selection mechanism but provides no criterion for *which* tokens matter for cross-environment generalization.\n\nvs. LightVLA (arXiv 2509.12594): LightVLA learns token selection end-to-end via Gumbel softmax — the selection criterion is implicitly defined by the training loss and may overfit to spurious correlations in training environments. CaTS's explicit causal criterion is designed to prevent exactly this overfitting.\n\nvs. TIES (arXiv 2603.24941): TIES uses inter-layer rank consistency (Kendall τ) as a stability signal — an innovative heuristic that captures token 'reliability' across layers. However, rank consistency does not distinguish between causally relevant tokens and tokens that are consistently spurious (e.g., a distinctive background element present in all training scenes would have high rank consistency but is causally irrelevant). CaTS's interventional scoring directly tests causal relevance via environment-marginal replacement.\n\nvs. InSpire (arXiv 2505.13888): InSpire redirects VLA attention via language prompting (spatial reasoning questions), achieving an indirect form of spurious correlation mitigation without token-level selection. CaTS operates at the token level with formal causal criteria. The two approaches are complementary — InSpire provides a zero-cost attention redirect while CaTS provides principled token selection with theoretical guarantees. Future work could combine InSpire's spatial prompting with CaTS's causal scoring.\n\nvs. CIRRL (arXiv 2505.12868): CIRRL provides finite-radius nonlinear robustness via identifiable representation learning, but operates on tabular data with elliptical distribution assumptions. CaTS draws theoretical inspiration from CIRRL's key insight (representation-level identifiability enables causal robustness) while adapting to the VLA setting where visual encoder outputs provide spatial patch-level identifiability. CaTS's DRO component provides analogous finite-sample guarantees without requiring elliptical assumptions.\n\nvs. Gaze-VLA (arXiv 2603.23202): Uses human gaze as an indirect causal signal (humans look at task-relevant regions). Requires gaze data collection; gaze provides a noisy proxy for causal relevance (humans also look at salient distractors). CaTS derives causal relevance from the model's own action predictions under intervention.\n\nvs. Causal-ACT (arXiv 2507.22380): Token-level in 7B VLA (not feature-level in ResNet+ACT); amortized scoring (not heuristic graph search); comprehensive LIBERO-Plus evaluation; concrete ε-invariance bound with approximate constants.\n\nvs. FTM: Interpretable per-token causal scores (not black-box affine transform); selective token removal (not global recalibration); formal robustness criterion.\n\nvs. LeaF (NeurIPS 2025): VLA action policies (not NLP reasoning); cross-environment interventional scoring (not single-domain gradient heuristics); formal SCM (not teacher-student comparison).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~800h A100 (80GB): ~350h for 22-28 LoRA fine-tuning runs with ACS head at ~14h each (including multi-layer scoring variants and composite objective hyperparameter search), ~250h for batch intervention data generation, amortized scorer training, and exact ACE validation (12,500 forward passes for validation set + systematic coverage across 7 perturbation types), ~200h for baseline reproduction (DTP and TIES reproduction on LIBERO-Plus, FTM on LIBERO-Plus, 8 baselines total with 5 seeds each for statistical protocol) and ablations",
      "gpu_utilization": "Low (~25-30%). GPUs sit idle during code development, causal scoring pipeline debugging, statistical protocol implementation, α_leak measurement analysis, and theorem proof development.",
      "timeline": "4-6 months",
      "team": "1-2 researchers (one with causal inference/DRO background for theorem formalization and proof, one with VLA/robotics experience for implementation and evaluation)",
      "estimated_gpu_cost": "~$640 (800h × $0.80/hr A100 spot/discount pricing from specialized providers such as Thunder Compute or TensorDock, May 2026 market rate; range $0.78-$1.07/hr across providers)"
    },
    "human_in_loop": {
      "gpu_hours": "~1200h A100 (80GB): agent explores ~40-50 training configurations more systematically, runs comprehensive ablations across all 7 perturbation dimensions with 5 seeds, evaluates all 8 baselines, and performs extensive α_leak measurements across layers",
      "gpu_utilization": "Moderate (~50-60%). Agent queues experiments faster but pauses at approval gates for: multi-layer scoring architecture decisions, DRO radius selection, amortization validation thresholds, theorem assumption checking.",
      "timeline": "2-4 months",
      "team": "1 researcher, ~45min/day check-in for approving experiment plans, reviewing causal score visualizations, validating amortization gap measurements, and verifying theorem proof steps",
      "claude_api_cost": "$500-700 (5000-7000 conversation turns for experiment design, code generation, theorem checking, statistical protocol implementation, result analysis)",
      "estimated_gpu_cost": "~$960 (1200h × $0.80/hr)",
      "risk_note": "Amortized scorer validation (Spearman ρ > 0.8 threshold) requires careful human judgment — if the scorer barely misses the threshold, the decision to proceed with amortized vs. exact scoring has significant downstream implications. DRO radius selection and the V-REx/DRO tradeoff require human expertise. Theorem proof needs verification by someone with expertise in both causal inference and approximation theory."
    },
    "auto_research": {
      "gpu_hours": "~2500h A100 (80GB): agent runs 120-150 experiment configurations including aggressive sweeps for scoring layer selection, V-REx/DRO weight ratios, pruning ratios, Shapley approximation methods, scorer architectures (varying width W), plus all baseline reproductions with 5 seeds and failed exploration runs",
      "gpu_utilization": "High (~90%+). Agent queues next experiment immediately upon completion. Continuous 24/7 execution.",
      "timeline": "3-5 weeks with 4-8 concurrent A100s; as few as 8-10 days with 16 concurrent GPUs",
      "team": "0 (initial setup: configure LIBERO-Plus environments, OpenVLA-OFT checkpoint, define intervention distribution, implement statistical testing protocol, implement α_leak measurement)",
      "claude_api_cost": "$700-1100 (7000-11000 turns for autonomous experiment design, debugging, statistical analysis, and paper drafting)",
      "estimated_gpu_cost": "~$2,000 (2500h × $0.80/hr)",
      "speed_bottleneck": "Number of concurrent A100 GPU instances. Secondary: intervention data generation is I/O-intensive (requires rendering perturbation environments). Statistical protocol with 5 seeds × 8 baselines × 7 perturbation dimensions requires organized experiment management.",
      "risk_note": "Without human gates, agent may over-explore suboptimal scoring layer combinations or DRO radius values. The theorem formalization cannot be fully automated — agent-generated proofs require expert verification, especially the amortization gap bound (step 3 of the proof involving Rademacher complexity). The statistical protocol is automatable but interpretation of borderline results (e.g., CaTS significant on 4/7 dimensions vs. the a priori 5/7 criterion) requires human judgment. Risk mitigation: pre-define structured search space with early stopping on amortization validation metrics; halt if Spearman ρ < 0.6 after initial scorer training."
    }
  },
  "target_venues": [
    "AAAI 2027 (deadline: ~August 1, 2026 — primary target, sufficient time for theoretical development, multi-layer scoring implementation, and statistical evaluation)",
    "ICLR 2027 (deadline: ~October 2026 — strong target, allows comprehensive evaluation and concurrent work comparison)",
    "ICRA 2027 (deadline: ~September 2026 — robotics venue, good fit for empirical contribution)"
  ],
  "level": "top-tier",
  "key_references": [
    "Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations [Causal-ACT] (arXiv 2507.22380, July 2025)",
    "VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling [FTM/FLA] (arXiv 2512.02902, Dec 2025)",
    "Learning to Focus: Causal Attention Distillation via Gradient-Guided Token Pruning [LeaF] (NeurIPS 2025, arXiv 2506.07851)",
    "Shortcut Learning in Generalist Robot Policies: The Role of Dataset Diversity and Fragmentation (CoRL 2025, arXiv 2508.06426)",
    "Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem? (ACL Findings 2025, arXiv 2502.11501)",
    "When Token Pruning is Worse than Random: Understanding Visual Token Information in VLLMs (ICLR 2026, arXiv 2512.07580)",
    "The Risks of Invariant Risk Minimization (ICLR 2021, arXiv 2010.05761)",
    "Out-of-Distribution Generalization via Risk Extrapolation [V-REx] (ICML 2021, arXiv 2003.00688)",
    "SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models (arXiv 2511.15605)",
    "AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention (arXiv 2511.18960)",
    "ACTIVA: Amortized Causal Effect Estimation via Transformer-based Variational Autoencoder (arXiv 2503.01290)",
    "CausalPFN: Amortized Causal Effect Estimation via In-Context Learning (NeurIPS 2025, arXiv 2506.07918)",
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026, arXiv 2510.13626)",
    "Invariant Causal Imitation Learning for Generalizable Policies [ICIL] (NeurIPS 2021)",
    "DTP: A Simple yet Effective Distracting Token Pruning Framework for VLA Models (arXiv 2601.16065, Jan 2026)",
    "FocusVLA: Focused Visual Utilization for Vision-Language-Action Models (arXiv 2603.28740, Mar 2026)",
    "LightVLA: Towards Efficient VLA Models via Differentiable Token Pruning (ICRA 2026, arXiv 2509.12594)",
    "TIES: Beyond Attention Magnitude — Leveraging Inter-layer Rank Consistency for Efficient VLA Models (arXiv 2603.24941, Mar 2026)",
    "BFA++: Hierarchical Best-Feature-Aware Token Pruning for Multi-View VLA Models (arXiv 2602.20566, Feb 2026)",
    "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation (arXiv 2511.18950)",
    "Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation (arXiv 2603.23202, Mar 2026)",
    "LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models (arXiv 2604.23950, Apr 2026)",
    "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations [RobustVLA] (ICLR 2026, arXiv 2510.00037)",
    "Mask World Model: Predicting What Matters for Robust Robot Policy Learning (arXiv 2604.19683, April 2026)",
    "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient VLA Inference (arXiv 2511.16449)",
    "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for VLA Models (arXiv 2603.22991, March 2026)",
    "Learning Invariant Causal Mechanism from Vision-Language Models [CLIP-ICM] (ICML 2025, arXiv 2405.15289)",
    "OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport (arXiv 2602.20205)",
    "Wasserstein Distributionally Robust Optimization and Variation Regularization (Operations Research, 2024)",
    "Finite-Sample Guarantees for Wasserstein DRO: Breaking the Curse of Dimensionality (Operations Research, 2023)",
    "Vision Transformers Need More Than Registers (arXiv 2602.22394, Feb 2026)",
    "Bounding the Estimation Error of Sampling-based Shapley Value Approximation (arXiv 1306.4265)",
    "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success [OpenVLA-OFT] (arXiv 2025)",
    "SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration (ICLR 2026, arXiv 2506.12723)",
    "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning (arXiv 2509.05614)",
    "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching (NeurIPS 2025, arXiv 2502.02175)",
    "InSpire: Vision-Language-Action Models with Intrinsic Spatial Reasoning (arXiv 2505.13888, May 2025)",
    "Causality-Inspired Robustness for Nonlinear Models via Representation Learning [CIRRL] (arXiv 2505.12868, May 2025)"
  ],
  "description": "VLA models suffer catastrophic failures under visual distribution shifts, yet a proliferation of concurrent token pruning methods (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, Compressor-VLA, Gaze-VLA — all 2025-2026) each propose different heuristic criteria without formal justification, and recent work shows many attention-based methods underperform random selection (arXiv 2502.11501) due to 'vanishing token information' in deep layers (arXiv 2512.07580). We propose Causal Token Selection (CaTS) v3, bridging three disconnected threads: VLA token pruning, causal intervention for imitation learning (Causal-ACT, ICIL), and causal attention distillation (LeaF), while drawing theoretical inspiration from CIRRL's (arXiv 2505.12868) breakthrough showing that representation-level identifiability enables nonlinear causal robustness guarantees. CaTS defines a formal SCM over the VLA token-action pipeline with a revised *encoder-level spatial locality* assumption — grounded in empirical findings that DINOv2/SigLIP encoder outputs preserve spatial correspondence (a form of patch-level identifiability analogous to CIRRL's affine identifiability) while LLM self-attention progressively mixes token information. Key advances over v2: (1) Multi-layer scoring at vision encoder output (where spatial locality is empirically validated) with optional intermediate-layer refinement. (2) Concrete ε-invariance bound with approximate constants: ε = C₁/√M + C₂·exp(-c·N_env/d_E) + C₃·α_leak·g(τ) + ε_amort, with order-of-magnitude estimates (M=200 Shapley samples → estimation error ~0.096; N_env=35 across d_E=7 dimensions → coverage term ~0.01; encoder-level α_leak≈0.1 → locality term ~0.10; overall ε≈0.26, a testable prediction against the observed ~50-65% gap for unmodified VLAs). (3) Honest composite robustness objective combining V-REx (practical heuristic) with Wasserstein DRO (finite-sample guarantees), including explicit analysis of their interaction: complementary for moderate DRO radius ρ (V-REx stabilizes known environments, DRO guards against unseen shifts; for small ρ, Wasserstein DRO approximates variation regularization, aligning with V-REx), with potential conflict at large ρ resolved by operating in the moderate-ρ regime calibrated to LIBERO-Plus perturbation magnitudes. (4) Quantified amortization gap: ε_amort ≤ O(1/√W) + O(1/√n_train) ≈ 0.054 for W=512, n_train=10K, with central validation protocol (Spearman ρ > 0.8). (5) Formal statistical protocol against random pruning with a priori 5/7 dimension criterion. Evaluated against 8 core baselines (streamlined from 11 with explicit code availability assessment: VLA-Pruner and DTP have public code; TIES is training-free and reimplementable; FTM is trivially reimplementable) including SRPO (82.1% SOTA), DTP, TIES, and VLA-Pruner. Concurrent efficiency-focused methods (SP-VLA ICLR 2026, SpecPrune-VLA, VLA-Cache NeurIPS 2025) are discussed as complementary — targeting temporal/spatial redundancy rather than causal robustness. InSpire (arXiv 2505.13888) is discussed as a complementary prompting-based approach to the same spurious correlation problem. GPU costs updated to current May 2026 market rates ($0.80/hr A100 spot from specialized providers). Primary targets: AAAI 2027 and ICLR 2027.",
  "project_name": "causal_token_sel_vla",
  "source": "web_research"
}

## Reviewer feedback (round 4)
Issues: ["MISSING RELATED WORK — ViT-Shapley (ICLR 2023 Oral, arXiv 2206.05282): 'Learning to Estimate Shapley Values with Vision Transformers' demonstrates amortized Shapley value estimation for ViT tokens using a learned explainer model that generates per-patch importance scores in a single forward pass. This is the most direct technical predecessor to CaTS's amortized causal scoring head — both train a lightweight model to predict per-token Shapley-style importance scores from token embeddings. The key difference (interventional/causal effects for cross-environment invariance vs. observational Shapley for model explanation) must be explicitly discussed. The ViT-Shapley code is publicly available and its attention masking approach for evaluating ViTs with partial information is directly applicable to CaTS's intervention mechanism.", "MISSING RELATED WORK — Mechanistic Interpretability for Steering VLA Models (CoRL 2025, arXiv 2509.00328): This paper uses activation patching / causal tracing on VLA internal representations (OpenVLA, Pi0) to identify sparse semantic directions causally linked to action selection, enabling zero-shot behavioral steering without fine-tuning. While it operates at the neuron/direction level rather than the token level, it demonstrates that interventional methods can identify causal structure in VLA representations — validating CaTS's premise. Evaluated on LIBERO and real UR5 robot. Should be cited as evidence that causal/interventional analysis of VLA representations is feasible and informative.", "VLM→VLA EXTRAPOLATION UNACKNOWLEDGED: The 'vanishing token information' paper (arXiv 2512.07580) evaluates VLMs (Qwen2.5-VL, LLaVA-1.5), not VLAs. The proposal treats its findings as directly applicable to VLA architectures (OpenVLA) without acknowledging this extrapolation. While VLAs share the VLM backbone architecture making extrapolation reasonable, VLA models have different training objectives (action prediction vs. text generation) and different attention patterns (action tokens attend to visual tokens differently than text tokens). The information horizon position may differ for VLAs. This should be noted as an assumption requiring empirical verification in the evaluation.", "MISSING CONCURRENT WORK — Test-Time Perturbation Learning with Delayed Feedback (arXiv 2604.18107, April 2026): PDF addresses VLA spurious correlations ('trajectory overfitting where VLAs over-attend to spurious correlation between actions and entities') via test-time adaptation with uncertainty-based augmentation and action voting. Achieves +7.4% on LIBERO. While complementary (test-time adaptation vs. training-time causal selection), it targets the exact same core problem and should be discussed."]
Feedback: The proposal has improved dramatically across 3 rounds and is now close to passing. The remaining issues are targeted and fixable:

1. **Cite ViT-Shapley (ICLR 2023 Oral)**: This is the most important addition. CaTS's amortized scoring head is technically similar to ViT-Shapley's learned explainer — both train a model to predict per-token importance from embeddings in a single forward pass. Differentiation: (a) ViT-Shapley estimates observational Shapley values for model explanation; CaTS estimates interventional causal effects via environment-marginal replacement for cross-environment invariance. (b) ViT-Shapley's masking evaluates prediction change; CaTS's intervention evaluates action distribution stability across environments. (c) CaTS's scorer is trained on multi-environment intervention data, not single-distribution Shapley estimates. The ViT-Shapley codebase (github.com/suinleelab/vit-shapley) could inform implementation.

2. **Cite Mechanistic Interpretability for VLA Steering (CoRL 2025)**: This validates CaTS's core premise — that interventional methods can identify causally relevant structure in VLA representations. Differentiate: it operates at neuron/direction level for behavioral steering, while CaTS operates at token level for robustness-oriented selection.

3. **Acknowledge the VLM→VLA extrapolation**: Add one sentence noting that arXiv 2512.07580 evaluates VLMs, and verifying the information horizon in VLA architectures (where action prediction creates different attention dynamics) is part of the empirical contribution (ablation b already tests this implicitly).

4. **Briefly mention PDF (arXiv 2604.18107)**: As a complementary test-time approach to the same spurious correlation problem. Could potentially be combined with CaTS (CaTS for training-time causal selection + PDF for test-time adaptation).

With these additions, the novelty differentiation will be stronger (CaTS goes beyond ViT-Shapley by targeting interventional rather than observational importance, beyond mechanistic interpretability by operating at token level for robustness rather than direction level for steering) and the landscape coverage will be complete.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.
- Address each issue specifically.

## 深度调研要求（每一轮修订都必须执行）

不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。
   - 搜索最新的相关论文（arXiv, conference proceedings）
   - 搜索 benchmark/leaderboard 确认当前 SOTA
   - 搜索可能遗漏的相关工作和 concurrent work

2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，
   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。

3. **深度思考**：在修订之前，先独立思考以下问题：
   - 这个 idea 的核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach 来解决同一个核心问题？
   - 修订后的 idea 相比上一版有什么本质性的改进？

4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，
   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。

## 针对 Review 意见的定向搜索

对 reviewer 指出的每个问题，执行以下搜索流程：

1. **如果 reviewer 说'已有类似工作'**：
   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读
   - 搜索该论文的 cited-by，找到后续跟进工作
   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot

2. **如果 reviewer 说'SOTA 过时'**：
   - 用 Papers With Code 查看当前排行榜
   - 搜索过去 6 个月的最新方法
   - 更新你的 landscape 和 baseline

3. **如果 reviewer 说'可行性有问题'**：
   - 搜索类似规模实验的实际成本和时间线
   - 搜索 GitHub 上是否有可复用的实现
   - 搜索相关数据集/模型的可获取性

4. **如果 reviewer 说'novelty 不足'**：
   - 对核心方法尽量做 3-5 种不同关键词组合的搜索
   - 搜索相邻领域是否有类似思路
   - 如果确实 novelty 不足，考虑 major revision 或 pivot

- Use WebSearch to find updated information if the reviewer flagged outdated claims.
- You have full freedom in how much to change:
  - Minor fix: if only specific details are wrong, correct them and keep everything else.
  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.
  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.
- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.
- In the output JSON, include a "change_type" field with one of: "minor", "major", or "pivot" to indicate the scope of your changes.
- Output the revised idea as a COMPLETE JSON object (same schema as original, plus "change_type").

## 停滞提醒
这个 idea 已经经过 4 轮修订，近 3 轮的平均分从 3.6 到 3.9，没有明显改善。

请认真思考：
- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？
- 如果你认为问题出在 approach 而非 framing，可以做 major revision。
- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。
- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。

最终由你判断——做你认为最能提升 idea 质量的选择。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c18dd896-5585-4f7b-b0bc-42c2f8ad78d2",
  "type": "user",
  "uuid": "ac92c514-04a2-46f8-92db-5b72c2a5f4d4",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T05:46:39.961Z_

```json
{
  "parentUuid": "ac92c514-04a2-46f8-92db-5b72c2a5f4d4",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "c17a24ec-6195-41a2-a1ee-862612e37807",
  "timestamp": "2026-05-13T05:46:39.961Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T05:46:39.961Z_

```json
{
  "parentUuid": "c17a24ec-6195-41a2-a1ee-862612e37807",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "03a76252-c362-47b1-af70-0e65d5cb7e5b",
  "timestamp": "2026-05-13T05:46:39.961Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"Causal Token Selection for Invariant VLA Policies via Amortized Interv…",
  "leafUuid": "03a76252-c362-47b1-af70-0e65d5cb7e5b",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise VLA causal token selection with ViT-Shapley differentiation",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82"
}
```

---

### Assistant

_source line 8 · 2026-05-13T05:46:53.950Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully before diving into research. The feedback identifies 4 specific issues:

1. Missing ViT-Shapley (ICLR 2023 Oral) - most direct technical predecessor to CaTS's amortized scoring
2. Missing Mechanistic Interpretability for VLA Steering (CoRL 2025) - validates CaTS's premise
3. VLM→VLA extrapolation unacknowledged for the vanishing token information paper
4. Missing concurrent work on test-time perturbation learning (arXiv 2604.18107)

The reviewer says the proposal is "close to passing" and these are "targeted and fixable" issues. 

The stagnation warning makes me reconsider whether these minor fixes are sufficient or if something more fundamental needs attention. But looking at this honestly: the core idea about causal token selection for VLA robustness is solid, the theoretical framework is well-developed, and the issues really do come down to missing citations that need proper integration and one unacknowledged assumption. The reviewer's explicit statement that the work has "improved dramatically" and is "close to passing" suggests these are genuinely fixable gaps rather than fundamental flaws. I need to research and integrate these four items properly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03a76252-c362-47b1-af70-0e65d5cb7e5b",
  "isSidechain": false,
  "requestId": "req_011Caz3GHHvFdxxAVqE4SnFr",
  "type": "assistant",
  "uuid": "8b9347da-595e-4be0-9c52-868a9e760d3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJh3His3FzGaiKjrQynJYG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21361,
      "cache_read_input_tokens": 11841,
      "output_tokens": 459,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21361,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 459,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21361
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

_source line 9 · 2026-05-13T05:46:53.953Z_

I'll research each paper the reviewer flagged, then revise the proposal. Let me start by fetching the key papers and searching for any additional related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b9347da-595e-4be0-9c52-868a9e760d3e",
  "isSidechain": false,
  "requestId": "req_011Caz3GHHvFdxxAVqE4SnFr",
  "type": "assistant",
  "uuid": "442a2d28-2228-4a38-bc92-7caf738ceb13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJh3His3FzGaiKjrQynJYG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21361,
      "cache_read_input_tokens": 11841,
      "output_tokens": 459,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21361,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 459,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21361
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

_source line 10 · 2026-05-13T05:46:54.202Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017Fb2q8JhNPdbpx2St1TTsQ`</summary>

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
  "parentUuid": "442a2d28-2228-4a38-bc92-7caf738ceb13",
  "isSidechain": false,
  "requestId": "req_011Caz3GHHvFdxxAVqE4SnFr",
  "type": "assistant",
  "uuid": "e94de764-f2b0-4b1b-a30c-73d1fd9432b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJh3His3FzGaiKjrQynJYG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21361,
      "cache_read_input_tokens": 11841,
      "output_tokens": 459,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21361,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 459,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21361
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

_source line 11 · 2026-05-13T05:46:54.210Z_

<details><summary>↩ Tool result · `toolu_017Fb2q8JhNPdbpx2St1TTsQ`</summary>

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
  "parentUuid": "e94de764-f2b0-4b1b-a30c-73d1fd9432b5",
  "isSidechain": false,
  "promptId": "c18dd896-5585-4f7b-b0bc-42c2f8ad78d2",
  "type": "user",
  "uuid": "4deabba5-a3d8-404c-9f08-3beff66e8d6a",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "e94de764-f2b0-4b1b-a30c-73d1fd9432b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-13T05:46:56.929Z_

Let me research all four papers the reviewer flagged, plus check for any additional related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4deabba5-a3d8-404c-9f08-3beff66e8d6a",
  "isSidechain": false,
  "requestId": "req_011Caz3HLFoJBFMm3gSbnGTT",
  "type": "assistant",
  "uuid": "8ee351ca-a306-482c-8025-7ad898e36ea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146iPGatJdYDfdBdizfsuie",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1479,
      "cache_read_input_tokens": 33202,
      "output_tokens": 481,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1479,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 481,
          "cache_read_input_tokens": 33202,
          "cache_creation_input_tokens": 1479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1479
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

_source line 13 · 2026-05-13T05:46:59.362Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M2eEHezNv5PihnUryffPih`</summary>

```json
{
  "url": "https://arxiv.org/abs/2206.05282",
  "prompt": "Extract the full abstract, key method details, and main contributions of ViT-Shapley. How does it train a model to predict per-patch Shapley values? What masking/intervention mechanism does it use? What is the architecture of the explainer model?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ee351ca-a306-482c-8025-7ad898e36ea2",
  "isSidechain": false,
  "requestId": "req_011Caz3HLFoJBFMm3gSbnGTT",
  "type": "assistant",
  "uuid": "8fb84007-90aa-45c9-89c3-ad8c4f7ae7e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146iPGatJdYDfdBdizfsuie",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1479,
      "cache_read_input_tokens": 33202,
      "output_tokens": 481,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1479,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 481,
          "cache_read_input_tokens": 33202,
          "cache_creation_input_tokens": 1479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1479
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

_source line 14 · 2026-05-13T05:47:02.187Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QtEZuPJ16FXZVt3YSLrhnn`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.00328",
  "prompt": "Extract the full abstract, key method details, and main contributions of this mechanistic interpretability paper for VLA steering. What interventional methods does it use (activation patching, causal tracing)? Which VLA models are evaluated? What tasks/benchmarks? How does it identify causal structure in VLA representations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fb84007-90aa-45c9-89c3-ad8c4f7ae7e4",
  "isSidechain": false,
  "requestId": "req_011Caz3HLFoJBFMm3gSbnGTT",
  "type": "assistant",
  "uuid": "85071a7a-585d-44ed-9dbb-cd8d497f3392",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146iPGatJdYDfdBdizfsuie",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1479,
      "cache_read_input_tokens": 33202,
      "output_tokens": 481,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1479,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 481,
          "cache_read_input_tokens": 33202,
          "cache_creation_input_tokens": 1479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1479
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

_source line 15 · 2026-05-13T05:47:03.656Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TFepaZc8ci11ZPHs53hejM`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.18107",
  "prompt": "Extract the full abstract, key method details, and main contributions. How does it address VLA spurious correlations? What is the test-time perturbation learning approach? What benchmarks and results? How does it compare to other VLA robustness methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85071a7a-585d-44ed-9dbb-cd8d497f3392",
  "isSidechain": false,
  "requestId": "req_011Caz3HLFoJBFMm3gSbnGTT",
  "type": "assistant",
  "uuid": "cd54b7cb-80bc-469c-b9ff-02d5cd414fe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146iPGatJdYDfdBdizfsuie",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1479,
      "cache_read_input_tokens": 33202,
      "output_tokens": 481,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1479,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 481,
          "cache_read_input_tokens": 33202,
          "cache_creation_input_tokens": 1479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1479
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

_source line 16 · 2026-05-13T05:47:04.244Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019DAaW6oghd14cVJCSkNKdi`</summary>

```json
{
  "query": "ViT-Shapley ICLR 2023 \"Learning to Estimate Shapley Values with Vision Transformers\" amortized explainer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd54b7cb-80bc-469c-b9ff-02d5cd414fe1",
  "isSidechain": false,
  "requestId": "req_011Caz3HLFoJBFMm3gSbnGTT",
  "type": "assistant",
  "uuid": "0db86780-f2f6-41d9-b57c-9715e0127731",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146iPGatJdYDfdBdizfsuie",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1479,
      "cache_read_input_tokens": 33202,
      "output_tokens": 481,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1479,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 481,
          "cache_read_input_tokens": 33202,
          "cache_creation_input_tokens": 1479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1479
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

_source line 17 · 2026-05-13T05:47:05.002Z_

<details><summary>↩ Tool result · `toolu_01M2eEHezNv5PihnUryffPih`</summary>

```text
# ViT-Shapley: Estimating Shapley Values for Vision Transformers

## Abstract
The paper addresses explaining vision transformer predictions through Shapley values. The authors note that "Shapley values offer a theoretically sound alternative" to attention-based methods, but computational costs make them impractical. Their solution involves creating a learned model to generate these explanations efficiently.

## Key Method Details

**Masking Mechanism:**
The approach leverages "an attention masking approach to evaluate ViTs with partial information," allowing the model to process incomplete inputs while computing feature importance.

**Explainer Architecture:**
Rather than computing Shapley values directly, the team develops "a procedure to generate Shapley value explanations via a separate, learned explainer model." This separate neural network learns to predict explanation scores without requiring expensive individual model evaluations.

## Main Contributions

1. **Practical Shapley computation**: Makes theoretically sound explanations computationally feasible for large vision transformers

2. **Empirical validation**: Their experiments demonstrate that "our approach provides more accurate explanations than existing methods for ViTs," outperforming baseline techniques like attention rollout, GradCAM, and LRP

3. **Attention masking adaptation**: Adapts masking strategies to work with transformer architectures, enabling partial input evaluation

The work was accepted to ICLR 2023, indicating peer-reviewed validation of the approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fb84007-90aa-45c9-89c3-ad8c4f7ae7e4",
  "isSidechain": false,
  "promptId": "c18dd896-5585-4f7b-b0bc-42c2f8ad78d2",
  "type": "user",
  "uuid": "9c67666e-27ea-4674-8774-4e320f7062a1",
  "toolUseResult": {
    "bytes": 45126,
    "code": 200,
    "codeText": "OK",
    "result": "# ViT-Shapley: Estimating Shapley Values for Vision Transformers\n\n## Abstract\nThe paper addresses explaining vision transformer predictions through Shapley values. The authors note that \"Shapley values offer a theoretically sound alternative\" to attention-based methods, but computational costs make them impractical. Their solution involves creating a learned model to generate these explanations efficiently.\n\n## Key Method Details\n\n**Masking Mechanism:**\nThe approach leverages \"an attention masking approach to evaluate ViTs with partial information,\" allowing the model to process incomplete inputs while computing feature importance.\n\n**Explainer Architecture:**\nRather than computing Shapley values directly, the team develops \"a procedure to generate Shapley value explanations via a separate, learned explainer model.\" This separate neural network learns to predict explanation scores without requiring expensive individual model evaluations.\n\n## Main Contributions\n\n1. **Practical Shapley computation**: Makes theoretically sound explanations computationally feasible for large vision transformers\n\n2. **Empirical validation**: Their experiments demonstrate that \"our approach provides more accurate explanations than existing methods for ViTs,\" outperforming baseline techniques like attention rollout, GradCAM, and LRP\n\n3. **Attention masking adaptation**: Adapts masking strategies to work with transformer architectures, enabling partial input evaluation\n\nThe work was accepted to ICLR 2023, indicating peer-reviewed validation of the approach.",
    "durationMs": 5625,
    "url": "https://arxiv.org/abs/2206.05282"
  },
  "sourceToolAssistantUUID": "8fb84007-90aa-45c9-89c3-ad8c4f7ae7e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T05:47:07.495Z_

<details><summary>↩ Tool result · `toolu_01QtEZuPJ16FXZVt3YSLrhnn`</summary>

```text
# Mechanistic Interpretability for Steering Vision-Language-Action Models

## Abstract
The paper presents the first framework for interpreting and steering VLAs through their internal representations, enabling direct intervention during inference without fine-tuning or reward signals.

## Key Method Details

The approach identifies sparse semantic directions within transformer layers by projecting "feedforward activations onto the token embedding basis." These directions—such as speed and direction—are found to be "causally linked to action selection."

The authors introduce "a general-purpose activation steering method that modulates behavior in real time" without requiring environment interaction or model retraining.

## Causal Structure Identification

Rather than traditional causal tracing methods, the framework uses **projection analysis**: mapping internal activations onto semantic embedding space to discover interpretable, sparse directions that causally influence action outputs.

## Models & Evaluation

**VLA Models Tested:**
- Pi0
- OpenVLA

**Evaluation Settings:**
- Simulation: LIBERO benchmark
- Physical robot: UR5 robotic arm
- "Zero-shot behavioral control" demonstrates the method's generalization

## Main Contributions

The work establishes that "interpretable components of embodied VLAs can be systematically harnessed for control," creating a new paradigm for transparent, steerable foundation models in robotics without explicit kinematic or dynamic models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85071a7a-585d-44ed-9dbb-cd8d497f3392",
  "isSidechain": false,
  "promptId": "c18dd896-5585-4f7b-b0bc-42c2f8ad78d2",
  "type": "user",
  "uuid": "a0a8d9af-0726-4eb6-843f-fc386f6b5d4e",
  "toolUseResult": {
    "bytes": 47165,
    "code": 200,
    "codeText": "OK",
    "result": "# Mechanistic Interpretability for Steering Vision-Language-Action Models\n\n## Abstract\nThe paper presents the first framework for interpreting and steering VLAs through their internal representations, enabling direct intervention during inference without fine-tuning or reward signals.\n\n## Key Method Details\n\nThe approach identifies sparse semantic directions within transformer layers by projecting \"feedforward activations onto the token embedding basis.\" These directions—such as speed and direction—are found to be \"causally linked to action selection.\"\n\nThe authors introduce \"a general-purpose activation steering method that modulates behavior in real time\" without requiring environment interaction or model retraining.\n\n## Causal Structure Identification\n\nRather than traditional causal tracing methods, the framework uses **projection analysis**: mapping internal activations onto semantic embedding space to discover interpretable, sparse directions that causally influence action outputs.\n\n## Models & Evaluation\n\n**VLA Models Tested:**\n- Pi0\n- OpenVLA\n\n**Evaluation Settings:**\n- Simulation: LIBERO benchmark\n- Physical robot: UR5 robotic arm\n- \"Zero-shot behavioral control\" demonstrates the method's generalization\n\n## Main Contributions\n\nThe work establishes that \"interpretable components of embodied VLAs can be systematically harnessed for control,\" creating a new paradigm for transparent, steerable foundation models in robotics without explicit kinematic or dynamic models.",
    "durationMs": 5305,
    "url": "https://arxiv.org/abs/2509.00328"
  },
  "sourceToolAssistantUUID": "85071a7a-585d-44ed-9dbb-cd8d497f3392",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T05:47:11.592Z_

<details><summary>↩ Tool result · `toolu_019DAaW6oghd14cVJCSkNKdi`</summary>

```text
Web search results for query: "ViT-Shapley ICLR 2023 "Learning to Estimate Shapley Values with Vision Transformers" amortized explainer"

Links: [{"title":"[2206.05282] Learning to Estimate Shapley Values with Vision Transformers","url":"https://arxiv.org/abs/2206.05282"},{"title":"ICLR 2023 Learning to Estimate Shapley Values with Vision Transformers Oral","url":"https://iclr.cc/virtual/2023/oral/12745"},{"title":"Learning to Estimate Shapley Values with Vision Transformers | OpenReview","url":"https://openreview.net/forum?id=5ktFNz_pJLK"},{"title":"GitHub - suinleelab/vit-shapley: Learning to Estimate Shapley Values with Vision Transformers · GitHub","url":"https://github.com/suinleelab/vit-shapley"},{"title":"Learning to Estimate Shapley Values with Vision Transformers | by JensRahnfeld | Medium","url":"https://medium.com/@JensRahnfeld/shapley-values-with-vision-transformers-9a0d705ee52d"},{"title":"(PDF) Learning to Estimate Shapley Values with Vision Transformers","url":"https://www.researchgate.net/publication/361274669_Learning_to_Estimate_Shapley_Values_with_Vision_Transformers"},{"title":"[2206.05282v1] Learning to Estimate Shapley Values with Vision Transformers","url":"https://arxiv.org/abs/2206.05282v1"},{"title":"Learning to Estimate Shapley Values with Vision Transformers","url":"https://www.catalyzex.com/paper/learning-to-estimate-shapley-values-with"},{"title":"[PDF] Learning to Estimate Shapley Values with Vision Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Learning-to-Estimate-Shapley-Values-with-Vision-Covert-Kim/a71b9fc58d8df11d4ae725568308fb5ace3da24a"},{"title":"Learning to Estimate Shapley Values with Vision Transformers. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2a69de817dc7222a00a94d5029e4b23f7/dblp"}]

Based on the search results, here's what I found about ViT-Shapley:

## Overview

ViT-Shapley makes Shapley values practical for vision transformer (ViT) models by learning an amortized explainer model that generates explanations in a single forward pass.

## The Problem

Transformers have become a default architecture in computer vision, but understanding what drives their predictions remains a challenging problem. Current explanation approaches rely on attention values or input gradients, but these give a limited understanding of a model's dependencies. Shapley values offer a theoretically sound alternative, but their computational cost makes them impractical for large, high-dimensional models.

## The Approach

The work leverages an attention masking approach to evaluate ViTs with partial information, and then develops a procedure to generate Shapley value explanations via a separate, learned explainer model.

## Results

The experiments compare Shapley values to many baseline methods (e.g., attention rollout, GradCAM, LRP), and find that the approach provides more accurate explanations than existing methods for ViTs.

## Publication

The paper "Learning to Estimate Shapley Values with Vision Transformers" was published by Covert et al. at ICLR 2023. The paper is also available on arXiv (2206.05282) and has associated code available on GitHub at the suinleelab/vit-shapley repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0db86780-f2f6-41d9-b57c-9715e0127731",
  "isSidechain": false,
  "promptId": "c18dd896-5585-4f7b-b0bc-42c2f8ad78d2",
  "type": "user",
  "uuid": "88be810b-7028-4dcf-b6c1-7ff866bc5cd6",
  "toolUseResult": {
    "query": "ViT-Shapley ICLR 2023 \"Learning to Estimate Shapley Values with Vision Transformers\" amortized explainer",
    "results": [
      {
        "tool_use_id": "srvtoolu_01E4XYdmF66hPGUwgfBun36q",
        "content": [
          {
            "title": "[2206.05282] Learning to Estimate Shapley Values with Vision Transformers",
            "url": "https://arxiv.org/abs/2206.05282"
          },
          {
            "title": "ICLR 2023 Learning to Estimate Shapley Values with Vision Transformers Oral",
            "url": "https://iclr.cc/virtual/2023/oral/12745"
          },
          {
            "title": "Learning to Estimate Shapley Values with Vision Transformers | OpenReview",
            "url": "https://openreview.net/forum?id=5ktFNz_pJLK"
          },
          {
            "title": "GitHub - suinleelab/vit-shapley: Learning to Estimate Shapley Values with Vision Transformers · GitHub",
            "url": "https://github.com/suinleelab/vit-shapley"
          },
          {
            "title": "Learning to Estimate Shapley Values with Vision Transformers | by JensRahnfeld | Medium",
            "url": "https://medium.com/@JensRahnfeld/shapley-values-with-vision-transformers-9a0d705ee52d"
          },
          {
            "title": "(PDF) Learning to Estimate Shapley Values with Vision Transformers",
            "url": "https://www.researchgate.net/publication/361274669_Learning_to_Estimate_Shapley_Values_with_Vision_Transformers"
          },
          {
            "title": "[2206.05282v1] Learning to Estimate Shapley Values with Vision Transformers",
            "url": "https://arxiv.org/abs/2206.05282v1"
          },
          {
            "title": "Learning to Estimate Shapley Values with Vision Transformers",
            "url": "https://www.catalyzex.com/paper/learning-to-estimate-shapley-values-with"
          },
          {
            "title": "[PDF] Learning to Estimate Shapley Values with Vision Transformers | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Learning-to-Estimate-Shapley-Values-with-Vision-Covert-Kim/a71b9fc58d8df11d4ae725568308fb5ace3da24a"
          },
          {
            "title": "Learning to Estimate Shapley Values with Vision Transformers. | BibSonomy",
            "url": "https://www.bibsonomy.org/bibtex/2a69de817dc7222a00a94d5029e4b23f7/dblp"
          }
        ]
      },
      "Based on the search results, here's what I found about ViT-Shapley:\n\n## Overview\n\nViT-Shapley makes Shapley values practical for vision transformer (ViT) models by learning an amortized explainer model that generates explanations in a single forward pass.\n\n## The Problem\n\nTransformers have become a default architecture in computer vision, but understanding what drives their predictions remains a challenging problem. Current explanation approaches rely on attention values or input gradients, but these give a limited understanding of a model's dependencies. Shapley values offer a theoretically sound alternative, but their computational cost makes them impractical for large, high-dimensional models.\n\n## The Approach\n\nThe work leverages an attention masking approach to evaluate ViTs with partial information, and then develops a procedure to generate Shapley value explanations via a separate, learned explainer model.\n\n## Results\n\nThe experiments compare Shapley values to many baseline methods (e.g., attention rollout, GradCAM, LRP), and find that the approach provides more accurate explanations than existing methods for ViTs.\n\n## Publication\n\nThe paper \"Learning to Estimate Shapley Values with Vision Transformers\" was published by Covert et al. at ICLR 2023. The paper is also available on arXiv (2206.05282) and has associated code available on GitHub at the suinleelab/vit-shapley repository."
    ],
    "durationSeconds": 7.344102393999997
  },
  "sourceToolAssistantUUID": "0db86780-f2f6-41d9-b57c-9715e0127731",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T05:47:11.636Z_

<details><summary>↩ Tool result · `toolu_01TFepaZc8ci11ZPHs53hejM`</summary>

```text
# Test-Time Perturbation Learning for Vision-Language-Action Models

## Full Abstract

The paper addresses fragility in Vision-Language-Action models when facing environmental shifts like object pose changes. The authors attribute this brittleness to "trajectory overfitting, where VLAs over-attend to the spurious correlation between actions and entities, then reproduce memorized action patterns."

## Key Method: Perturbation Learning with Delayed Feedback (PDF)

**Core approach:**
- A verifier-free test-time adaptation framework that operates without fine-tuning the base model
- Uses "uncertainty-based data augmentation and action voting" to counteract spurious correlations
- Incorporates an adaptive scheduler to balance computational efficiency with performance
- Learns a lightweight perturbation module that retrospectively adjusts action logits based on delayed feedback to address overconfidence

## Main Contributions

1. Identifies trajectory overfitting as the root cause of VLA brittleness
2. Proposes a practical test-time adaptation approach requiring no model retraining
3. Introduces delayed feedback mechanism for corrective action adjustments
4. Demonstrates consistent empirical improvements across multiple domains

## Benchmarks & Results

- **LIBERO:** +7.4% success rate improvement
- **Atari:** +10.3 human-normalized score gain
- Shows consistent advantages over vanilla VLAs and other test-time adaptation approaches

## Comparison to Other Methods

The paper directly contrasts its approach against "vanilla VLA and VLA with test-time adaptation," establishing superior performance while maintaining practical efficiency through its adaptive budget allocation mechanism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd54b7cb-80bc-469c-b9ff-02d5cd414fe1",
  "isSidechain": false,
  "promptId": "c18dd896-5585-4f7b-b0bc-42c2f8ad78d2",
  "type": "user",
  "uuid": "24ac44a6-8162-4818-8b40-d41db549979b",
  "toolUseResult": {
    "bytes": 47487,
    "code": 200,
    "codeText": "OK",
    "result": "# Test-Time Perturbation Learning for Vision-Language-Action Models\n\n## Full Abstract\n\nThe paper addresses fragility in Vision-Language-Action models when facing environmental shifts like object pose changes. The authors attribute this brittleness to \"trajectory overfitting, where VLAs over-attend to the spurious correlation between actions and entities, then reproduce memorized action patterns.\"\n\n## Key Method: Perturbation Learning with Delayed Feedback (PDF)\n\n**Core approach:**\n- A verifier-free test-time adaptation framework that operates without fine-tuning the base model\n- Uses \"uncertainty-based data augmentation and action voting\" to counteract spurious correlations\n- Incorporates an adaptive scheduler to balance computational efficiency with performance\n- Learns a lightweight perturbation module that retrospectively adjusts action logits based on delayed feedback to address overconfidence\n\n## Main Contributions\n\n1. Identifies trajectory overfitting as the root cause of VLA brittleness\n2. Proposes a practical test-time adaptation approach requiring no model retraining\n3. Introduces delayed feedback mechanism for corrective action adjustments\n4. Demonstrates consistent empirical improvements across multiple domains\n\n## Benchmarks & Results\n\n- **LIBERO:** +7.4% success rate improvement\n- **Atari:** +10.3 human-normalized score gain\n- Shows consistent advantages over vanilla VLAs and other test-time adaptation approaches\n\n## Comparison to Other Methods\n\nThe paper directly contrasts its approach against \"vanilla VLA and VLA with test-time adaptation,\" establishing superior performance while maintaining practical efficiency through its adaptive budget allocation mechanism.",
    "durationMs": 7974,
    "url": "https://arxiv.org/abs/2604.18107"
  },
  "sourceToolAssistantUUID": "cd54b7cb-80bc-469c-b9ff-02d5cd414fe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"Causal Token Selection for Invariant VLA Policies via Amortized Interv…",
  "leafUuid": "24ac44a6-8162-4818-8b40-d41db549979b",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise VLA causal token selection with ViT-Shapley differentiation",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82"
}
```

---

### Assistant

_source line 23 · 2026-05-13T05:47:14.776Z_

Now let me get more details on ViT-Shapley's technical approach and search for any follow-up work or additional missing references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24ac44a6-8162-4818-8b40-d41db549979b",
  "isSidechain": false,
  "requestId": "req_011Caz3Jcab3c3NReUv7CZWi",
  "type": "assistant",
  "uuid": "f3fcd0c4-f38d-4abe-83f8-c3281c42a901",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HSzdf2yjScqt6p9QXzJLx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 969,
      "cache_creation_input_tokens": 1527,
      "cache_read_input_tokens": 34681,
      "output_tokens": 335,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1527,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 969,
          "output_tokens": 335,
          "cache_read_input_tokens": 34681,
          "cache_creation_input_tokens": 1527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1527
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

_source line 24 · 2026-05-13T05:47:16.258Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ToLTJiSSZqk9sNmBCX7uJy`</summary>

```json
{
  "url": "https://github.com/suinleelab/vit-shapley",
  "prompt": "What is the architecture of the explainer model? How is the surrogate/explainer trained? What masking mechanism is used? What are the key implementation details?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3fcd0c4-f38d-4abe-83f8-c3281c42a901",
  "isSidechain": false,
  "requestId": "req_011Caz3Jcab3c3NReUv7CZWi",
  "type": "assistant",
  "uuid": "848c751f-97c9-4454-8a44-1997681a9f00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HSzdf2yjScqt6p9QXzJLx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 969,
      "cache_creation_input_tokens": 1527,
      "cache_read_input_tokens": 34681,
      "output_tokens": 335,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1527,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 969,
          "output_tokens": 335,
          "cache_read_input_tokens": 34681,
          "cache_creation_input_tokens": 1527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1527
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

_source line 25 · 2026-05-13T05:47:17.256Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K7sevtuXXgagXgirKLchzt`</summary>

```json
{
  "query": "ViT-Shapley follow-up work amortized Shapley vision transformers token importance 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "848c751f-97c9-4454-8a44-1997681a9f00",
  "isSidechain": false,
  "requestId": "req_011Caz3Jcab3c3NReUv7CZWi",
  "type": "assistant",
  "uuid": "c173f3a9-d562-4d44-8133-d4f03893730c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HSzdf2yjScqt6p9QXzJLx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 969,
      "cache_creation_input_tokens": 1527,
      "cache_read_input_tokens": 34681,
      "output_tokens": 335,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1527,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 969,
          "output_tokens": 335,
          "cache_read_input_tokens": 34681,
          "cache_creation_input_tokens": 1527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1527
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

_source line 26 · 2026-05-13T05:47:18.197Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AQw5cBL2yoDvCzJJH8tr9h`</summary>

```json
{
  "query": "\"mechanistic interpretability\" VLA \"activation patching\" \"causal tracing\" robot manipulation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c173f3a9-d562-4d44-8133-d4f03893730c",
  "isSidechain": false,
  "requestId": "req_011Caz3Jcab3c3NReUv7CZWi",
  "type": "assistant",
  "uuid": "3315dfb3-ea70-412b-92ff-bb4141b4bca3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HSzdf2yjScqt6p9QXzJLx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 969,
      "cache_creation_input_tokens": 1527,
      "cache_read_input_tokens": 34681,
      "output_tokens": 335,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1527,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 969,
          "output_tokens": 335,
          "cache_read_input_tokens": 34681,
          "cache_creation_input_tokens": 1527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1527
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

_source line 27 · 2026-05-13T05:47:18.985Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GhSYqMQpsn9qUq8Dj92KUk`</summary>

```json
{
  "query": "arXiv 2604.18107 \"test-time perturbation\" VLA delayed feedback 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3315dfb3-ea70-412b-92ff-bb4141b4bca3",
  "isSidechain": false,
  "requestId": "req_011Caz3Jcab3c3NReUv7CZWi",
  "type": "assistant",
  "uuid": "1df1fe7c-0fd0-443a-b13c-d5d6a0e06a60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HSzdf2yjScqt6p9QXzJLx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 969,
      "cache_creation_input_tokens": 1527,
      "cache_read_input_tokens": 34681,
      "output_tokens": 335,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1527,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 969,
          "output_tokens": 335,
          "cache_read_input_tokens": 34681,
          "cache_creation_input_tokens": 1527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1527
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

_source line 28 · 2026-05-13T05:47:22.242Z_

<details><summary>↩ Tool result · `toolu_01ToLTJiSSZqk9sNmBCX7uJy`</summary>

```text
# ViT-Shapley: Architecture and Training Details

Based on the provided GitHub repository content, here's what can be determined about the system:

## Explainer Architecture
The repository doesn't explicitly detail the explainer model architecture in the provided content. It's described as an "amortized explainer model" that generates explanations in a single forward pass, but specific layer compositions or design choices aren't documented in this excerpt.

## Training Pipeline
The system uses a three-stage workflow:

1. **Classifier Stage**: Train initial ViT image classifier
2. **Surrogate Stage**: Fine-tune the classifier with random masking to accommodate held-out image patches
3. **Explainer Stage**: Train the explainer to produce Shapley values in one forward pass

## Masking Mechanisms
The repository implements multiple masking strategies:
- **Attention-based masking** (surrogate_attn.yaml)
- **Zero masking** (surrogate_zero.yaml)

Both strategies are trained as separate surrogate models that feed into the final explainer.

## Key Details
- Output consists of per-patch importance scores (196 values for a 14×14 patch grid)
- The approach leverages existing methods: "KernelSHAP, FastSHAP" as foundational work
- System supports both multiclass (softmax) and binary classification (sigmoid)
- Implementation uses YAML-based configuration for reproducibility

The paper referenced (ICLR spotlight) likely contains architectural specifics not included in this repository documentation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "848c751f-97c9-4454-8a44-1997681a9f00",
  "isSidechain": false,
  "promptId": "c18dd896-5585-4f7b-b0bc-42c2f8ad78d2",
  "type": "user",
  "uuid": "9c4e602c-0add-4bfb-a890-9c5470390486",
  "toolUseResult": {
    "bytes": 284930,
    "code": 200,
    "codeText": "OK",
    "result": "# ViT-Shapley: Architecture and Training Details\n\nBased on the provided GitHub repository content, here's what can be determined about the system:\n\n## Explainer Architecture\nThe repository doesn't explicitly detail the explainer model architecture in the provided content. It's described as an \"amortized explainer model\" that generates explanations in a single forward pass, but specific layer compositions or design choices aren't documented in this excerpt.\n\n## Training Pipeline\nThe system uses a three-stage workflow:\n\n1. **Classifier Stage**: Train initial ViT image classifier\n2. **Surrogate Stage**: Fine-tune the classifier with random masking to accommodate held-out image patches\n3. **Explainer Stage**: Train the explainer to produce Shapley values in one forward pass\n\n## Masking Mechanisms\nThe repository implements multiple masking strategies:\n- **Attention-based masking** (surrogate_attn.yaml)\n- **Zero masking** (surrogate_zero.yaml)\n\nBoth strategies are trained as separate surrogate models that feed into the final explainer.\n\n## Key Details\n- Output consists of per-patch importance scores (196 values for a 14×14 patch grid)\n- The approach leverages existing methods: \"KernelSHAP, FastSHAP\" as foundational work\n- System supports both multiclass (softmax) and binary classification (sigmoid)\n- Implementation uses YAML-based configuration for reproducibility\n\nThe paper referenced (ICLR spotlight) likely contains architectural specifics not included in this repository documentation.",
    "durationMs": 5980,
    "url": "https://github.com/suinleelab/vit-shapley"
  },
  "sourceToolAssistantUUID": "848c751f-97c9-4454-8a44-1997681a9f00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-13T05:47:24.125Z_

<details><summary>↩ Tool result · `toolu_01K7sevtuXXgagXgirKLchzt`</summary>

```text
Web search results for query: "ViT-Shapley follow-up work amortized Shapley vision transformers token importance 2024 2025 2026"

Links: [{"title":"GitHub - suinleelab/vit-shapley: Learning to Estimate Shapley Values with Vision Transformers · GitHub","url":"https://github.com/suinleelab/vit-shapley"},{"title":"Learning to Estimate Shapley Values with Vision Transformers | OpenReview","url":"https://openreview.net/forum?id=5ktFNz_pJLK"},{"title":"[PDF] Learning to Estimate Shapley Values with Vision Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/a71b9fc58d8df11d4ae725568308fb5ace3da24a"},{"title":"(PDF) Learning to Estimate Shapley Values with Vision Transformers","url":"https://www.researchgate.net/publication/361274669_Learning_to_Estimate_Shapley_Values_with_Vision_Transformers"},{"title":"[2206.05282] Learning to Estimate Shapley Values with Vision Transformers","url":"https://arxiv.org/abs/2206.05282"},{"title":"Efficient token pruning in Vision Transformers using an attention-based Multilayer Network - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957417425010711"},{"title":"Learning to Estimate Shapley Values with Vision Transformers | by JensRahnfeld | Medium","url":"https://medium.com/@JensRahnfeld/shapley-values-with-vision-transformers-9a0d705ee52d"},{"title":"Unifying Prediction and Explanation in Time-Series Transformers via Shapley-based Pretraining","url":"https://arxiv.org/html/2501.15070v1"},{"title":"GTP-ViT: Efficient Vision Transformers via Graph-based Token Propagation","url":"https://openaccess.thecvf.com/content/WACV2024/papers/Xu_GTP-ViT_Efficient_Vision_Transformers_via_Graph-Based_Token_Propagation_WACV_2024_paper.pdf"},{"title":"Multi-Modal Vision Transformer with Explainable Shapley Additive Explanations Value Embedding for Cymbidium goeringii Quality Grading","url":"https://www.mdpi.com/2076-3417/14/22/10157"}]

Based on the search results, here's what I found regarding ViT-Shapley and follow-up work on amortized Shapley values for vision transformers:

## Original ViT-Shapley Work

ViT-Shapley makes Shapley values practical for vision transformer (ViT) models by learning an amortized explainer model that generates explanations in a single forward pass. The approach leverages an attention masking approach to evaluate ViTs with partial information, and develops a procedure to generate Shapley value explanations via a separate, learned explainer model. The original work was published as an ICLR spotlight paper.

## Follow-up Work on Amortized Shapley Values

While the search results don't contain extensive follow-up work specifically on ViT-Shapley from 2024-2026, there is related research extending amortized Shapley value estimation:

1. **Fast Weighted Shapley (FW-Shapley)**: An amortized framework for efficiently computing weighted Shapley values using a learned estimator, with theoretical validity even without ground truth Weighted Shapley values during training.

2. **Time-Series Applications**: ShapTST integrates Shapley-based explanations in a time-series transformer framework that combines amortized Shapley value estimation with pre-training, enabling valid explanations without extra computational cost post-inference.

The search results suggest active research in applying amortized Shapley methods to different domains (time-series, multi-modal), but I didn't find specific follow-up publications on ViT-Shapley itself from 2024-2026. You may want to check arXiv, recent conference proceedings (ICCV, ECCV, NeurIPS), or the authors' recent publications for the most current developments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c173f3a9-d562-4d44-8133-d4f03893730c",
  "isSidechain": false,
  "promptId": "c18dd896-5585-4f7b-b0bc-42c2f8ad78d2",
  "type": "user",
  "uuid": "fd13f440-1f69-4faf-b715-66cd7c2dbc3d",
  "toolUseResult": {
    "query": "ViT-Shapley follow-up work amortized Shapley vision transformers token importance 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ca2tCZvJxGVhJkRYe7qTi6",
        "content": [
          {
            "title": "GitHub - suinleelab/vit-shapley: Learning to Estimate Shapley Values with Vision Transformers · GitHub",
            "url": "https://github.com/suinleelab/vit-shapley"
          },
          {
            "title": "Learning to Estimate Shapley Values with Vision Transformers | OpenReview",
            "url": "https://openreview.net/forum?id=5ktFNz_pJLK"
          },
          {
            "title": "[PDF] Learning to Estimate Shapley Values with Vision Transformers | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/a71b9fc58d8df11d4ae725568308fb5ace3da24a"
          },
          {
            "title": "(PDF) Learning to Estimate Shapley Values with Vision Transformers",
            "url": "https://www.researchgate.net/publication/361274669_Learning_to_Estimate_Shapley_Values_with_Vision_Transformers"
          },
          {
            "title": "[2206.05282] Learning to Estimate Shapley Values with Vision Transformers",
            "url": "https://arxiv.org/abs/2206.05282"
          },
          {
            "title": "Efficient token pruning in Vision Transformers using an attention-based Multilayer Network - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0957417425010711"
          },
          {
            "title": "Learning to Estimate Shapley Values with Vision Transformers | by JensRahnfeld | Medium",
            "url": "https://medium.com/@JensRahnfeld/shapley-values-with-vision-transformers-9a0d705ee52d"
          },
          {
            "title": "Unifying Prediction and Explanation in Time-Series Transformers via Shapley-based Pretraining",
            "url": "https://arxiv.org/html/2501.15070v1"
          },
          {
            "title": "GTP-ViT: Efficient Vision Transformers via Graph-based Token Propagation",
            "url": "https://openaccess.thecvf.com/content/WACV2024/papers/Xu_GTP-ViT_Efficient_Vision_Transformers_via_Graph-Based_Token_Propagation_WACV_2024_paper.pdf"
          },
          {
            "title": "Multi-Modal Vision Transformer with Explainable Shapley Additive Explanations Value Embedding for Cymbidium goeringii Quality Grading",
            "url": "https://www.mdpi.com/2076-3417/14/22/10157"
          }
        ]
      },
      "Based on the search results, here's what I found regarding ViT-Shapley and follow-up work on amortized Shapley values for vision transformers:\n\n## Original ViT-Shapley Work\n\nViT-Shapley makes Shapley values practical for vision transformer (ViT) models by learning an amortized explainer model that generates explanations in a single forward pass. The approach leverages an attention masking approach to evaluate ViTs with partial information, and develops a procedure to generate Shapley value explanations via a separate, learned explainer model. The original work was published as an ICLR spotlight paper.\n\n## Follow-up Work on Amortized Shapley Values\n\nWhile the search results don't contain extensive follow-up work specifically on ViT-Shapley from 2024-2026, there is related research extending amortized Shapley value estimation:\n\n1. **Fast Weighted Shapley (FW-Shapley)**: An amortized framework for efficiently computing weighted Shapley values using a learned estimator, with theoretical validity even without ground truth Weighted Shapley values during training.\n\n2. **Time-Series Applications**: ShapTST integrates Shapley-based explanations in a time-series transformer framework that combines amortized Shapley value estimation with pre-training, enabling valid explanations without extra computational cost post-inference.\n\nThe search results suggest active research in applying amortized Shapley methods to different domains (time-series, multi-modal), but I didn't find specific follow-up publications on ViT-Shapley itself from 2024-2026. You may want to check arXiv, recent conference proceedings (ICCV, ECCV, NeurIPS), or the authors' recent publications for the most current developments."
    ],
    "durationSeconds": 6.866132851999995
  },
  "sourceToolAssistantUUID": "c173f3a9-d562-4d44-8133-d4f03893730c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-13T05:47:26.041Z_

<details><summary>↩ Tool result · `toolu_01AQw5cBL2yoDvCzJJH8tr9h`</summary>

```text
Web search results for query: ""mechanistic interpretability" VLA "activation patching" "causal tracing" robot manipulation 2025 2026"

Links: [{"title":"Understanding Mechanistic Interpretability in AI Models | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://arxiv.org/html/2509.00328v1"},{"title":"Mechanistic Interpretability Meets Vision Language Models: Insights and Limitations | ICLR Blogposts 2025","url":"https://d2jud02ci9yv69.cloudfront.net/2025-04-28-vlm-understanding-29/blog/vlm-understanding/"},{"title":"Mechanistic Interpretability for Steering Vision Language Action Models","url":"https://vla-mech-interp.github.io/"},{"title":"[2509.00328] Mechanistic interpretability for steering vision-language-action models","url":"https://arxiv.org/abs/2509.00328"},{"title":"Open problems in mechanistic interpretability: 2026 status report","url":"https://gist.github.com/bigsnarfdude/629f19f635981999c51a8bd44c6e2a54"},{"title":"Understanding Mechanistic Interpretability in AI Models","url":"https://intuitionlabs.ai/pdfs/understanding-mechanistic-interpretability-in-ai-models.pdf"},{"title":"Mechanistic Interpretability Framework","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-framework"},{"title":"Mechanistic Interpretability Explained: Circuits, Sparse Autoencoders, Causal Tracing, and AI Safety | by Adnan Masood, PhD. | Apr, 2026 | Medium","url":"https://medium.com/@adnanmasood/mechanistic-interpretability-explained-circuits-sparse-autoencoders-causal-tracing-and-ai-88ecc8d70b72"},{"title":"[2511.05923] Causal Tracing of Object Representations in Large Vision Language Models: Mechanistic Interpretability and Hallucination Mitigation","url":"https://arxiv.org/abs/2511.05923"}]

Based on my search results, here's what I found regarding mechanistic interpretability, vision-language-action (VLA) models, activation patching, and causal tracing in robot manipulation:

## Key Recent Work on VLA Mechanistic Interpretability

The first attempt to use mechanistic interpretability techniques developed for LLMs with large robotics models is a 2025 research effort that introduced a framework for interpreting and steering VLAs. The work projects feedforward activations within transformer layers onto the token embedding basis, identifying sparse semantic directions – such as speed and direction – that are causally linked to action selection.

## Application to Robot Manipulation

Sparse semantic directions - such as speed and direction - are causally linked to action selection, and a general-purpose activation steering method modulates behavior in real time, without fine-tuning, reward signals, or environment interaction. The method was evaluated on two recent open-source VLAs, Pi0 and OpenVLA, demonstrating zero-shot behavioral control in simulation (LIBERO) and on a physical robot (UR5).

## Broader Context on Mechanistic Interpretability Advances

Mechanistic interpretability methods include probing, activation patching, logit lens, sparse autoencoders, and automated explanation. Geiger et al.'s causal abstraction framework (JMLR, 2025) provides the most developed theoretical foundation, unifying activation patching, circuit analysis, SAEs, and steering under precise mathematical definitions.

The field is experiencing significant momentum, with MIT Technology Review's recognition of mechanistic interpretability as a 2026 Breakthrough Technology reflecting growing maturity in the field.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3315dfb3-ea70-412b-92ff-bb4141b4bca3",
  "isSidechain": false,
  "promptId": "c18dd896-5585-4f7b-b0bc-42c2f8ad78d2",
  "type": "user",
  "uuid": "517bd7e7-a7af-422b-8f5e-78122df7eda2",
  "toolUseResult": {
    "query": "\"mechanistic interpretability\" VLA \"activation patching\" \"causal tracing\" robot manipulation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01222VCRyXpX17D3ybLjoJ4n",
        "content": [
          {
            "title": "Understanding Mechanistic Interpretability in AI Models | IntuitionLabs",
            "url": "https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"
          },
          {
            "title": "Mechanistic Interpretability for Steering Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2509.00328v1"
          },
          {
            "title": "Mechanistic Interpretability Meets Vision Language Models: Insights and Limitations | ICLR Blogposts 2025",
            "url": "https://d2jud02ci9yv69.cloudfront.net/2025-04-28-vlm-understanding-29/blog/vlm-understanding/"
          },
          {
            "title": "Mechanistic Interpretability for Steering Vision Language Action Models",
            "url": "https://vla-mech-interp.github.io/"
          },
          {
            "title": "[2509.00328] Mechanistic interpretability for steering vision-language-action models",
            "url": "https://arxiv.org/abs/2509.00328"
          },
          {
            "title": "Open problems in mechanistic interpretability: 2026 status report",
            "url": "https://gist.github.com/bigsnarfdude/629f19f635981999c51a8bd44c6e2a54"
          },
          {
            "title": "Understanding Mechanistic Interpretability in AI Models",
            "url": "https://intuitionlabs.ai/pdfs/understanding-mechanistic-interpretability-in-ai-models.pdf"
          },
          {
            "title": "Mechanistic Interpretability Framework",
            "url": "https://www.emergentmind.com/topics/mechanistic-interpretability-framework"
          },
          {
            "title": "Mechanistic Interpretability Explained: Circuits, Sparse Autoencoders, Causal Tracing, and AI Safety | by Adnan Masood, PhD. | Apr, 2026 | Medium",
            "url": "https://medium.com/@adnanmasood/mechanistic-interpretability-explained-circuits-sparse-autoencoders-causal-tracing-and-ai-88ecc8d70b72"
          },
          {
            "title": "[2511.05923] Causal Tracing of Object Representations in Large Vision Language Models: Mechanistic Interpretability and Hallucination Mitigation",
            "url": "https://arxiv.org/abs/2511.05923"
          }
        ]
      },
      "Based on my search results, here's what I found regarding mechanistic interpretability, vision-language-action (VLA) models, activation patching, and causal tracing in robot manipulation:\n\n## Key Recent Work on VLA Mechanistic Interpretability\n\nThe first attempt to use mechanistic interpretability techniques developed for LLMs with large robotics models is a 2025 research effort that introduced a framework for interpreting and steering VLAs. The work projects feedforward activations within transformer layers onto the token embedding basis, identifying sparse semantic directions – such as speed and direction – that are causally linked to action selection.\n\n## Application to Robot Manipulation\n\nSparse semantic directions - such as speed and direction - are causally linked to action selection, and a general-purpose activation steering method modulates behavior in real time, without fine-tuning, reward signals, or environment interaction. The method was evaluated on two recent open-source VLAs, Pi0 and OpenVLA, demonstrating zero-shot behavioral control in simulation (LIBERO) and on a physical robot (UR5).\n\n## Broader Context on Mechanistic Interpretability Advances\n\nMechanistic interpretability methods include probing, activation patching, logit lens, sparse autoencoders, and automated explanation. Geiger et al.'s causal abstraction framework (JMLR, 2025) provides the most developed theoretical foundation, unifying activation patching, circuit analysis, SAEs, and steering under precise mathematical definitions.\n\nThe field is experiencing significant momentum, with MIT Technology Review's recognition of mechanistic interpretability as a 2026 Breakthrough Technology reflecting growing maturity in the field."
    ],
    "durationSeconds": 7.841626065000004
  },
  "sourceToolAssistantUUID": "3315dfb3-ea70-412b-92ff-bb4141b4bca3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-13T05:47:26.598Z_

<details><summary>↩ Tool result · `toolu_01GhSYqMQpsn9qUq8Dj92KUk`</summary>

```text
Web search results for query: "arXiv 2604.18107 "test-time perturbation" VLA delayed feedback 2026"

Links: [{"title":"[2604.18107] Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.18107"},{"title":"Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models","url":"https://arxiv.org/html/2604.18107"},{"title":"Test-Time Perturbation Learning with Delayed Feedback for","url":"https://arxiv.org/pdf/2604.18107"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748v1"},{"title":"Long-Term Memory for VLA-based Agents in Open-World Task Execution","url":"https://arxiv.org/html/2604.15671"},{"title":"[2604.15671] Long-Term Memory for VLA-based Agents in Open-World Task Execution","url":"https://arxiv.org/abs/2604.15671"},{"title":"Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision–Language–Action Models via Latent Iterative Reasoning","url":"https://arxiv.org/html/2602.07845v1"},{"title":"[2602.07845] Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision-Language-Action Models via Latent Iterative Reasoning","url":"https://arxiv.org/abs/2602.07845"},{"title":"HELM: Harness-Enhanced Long-horizon Memory for Vision-Language-Action Manipulation","url":"https://arxiv.org/html/2604.18791"},{"title":"Adaptor: Advancing Assistive Teleoperation with Few-Shot Learning and Cross-Operator Generalization","url":"https://arxiv.org/html/2604.09462v1"}]

I found the arXiv paper you're looking for! Here are the key details about arXiv paper 2604.18107:

**Title:** Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models

**Authors and Affiliation:** The paper was authored by Zehua Zang, Xi Wang, Fuchun Sun, Xiao Xu, Lixiang Liu, Jiahuan Zhou, and Jiangmeng Li from the Institute of Software (Chinese Academy of Sciences), University of Chinese Academy of Sciences, Tsinghua University, Wangxuan Institute of Computer Technology (Peking University), and National Defense University

**Submission Date:** Submitted on April 20, 2026

**Main Contribution:** The paper proposes Perturbation learning with Delayed Feedback (PDF), a verifier-free test-time adaptation framework that improves decision performance without fine-tuning the base model.

**Problem Addressed:** Vision-Language-Action models (VLAs) achieve remarkable performance in sequential decision-making but remain fragile to subtle environmental shifts, such as small changes in object pose. The brittleness is attributed to trajectory overfitting, where VLAs over-attend to the spurious correlation between actions and entities, then reproduce memorized action patterns.

**Approach:** PDF mitigates the spurious correlation through uncertainty-based data augmentation and action voting, while an adaptive scheduler allocates augmentation budgets to balance performance and efficiency. PDF learns a lightweight perturbation module that retrospectively adjusts action logits guided by delayed feedback, correcting overconfidence issues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1df1fe7c-0fd0-443a-b13c-d5d6a0e06a60",
  "isSidechain": false,
  "promptId": "c18dd896-5585-4f7b-b0bc-42c2f8ad78d2",
  "type": "user",
  "uuid": "e067830f-d6b2-4f1b-852e-0e839707ebd5",
  "toolUseResult": {
    "query": "arXiv 2604.18107 \"test-time perturbation\" VLA delayed feedback 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017acTccvGM82G7K31136VEZ",
        "content": [
          {
            "title": "[2604.18107] Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2604.18107"
          },
          {
            "title": "Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2604.18107"
          },
          {
            "title": "Test-Time Perturbation Learning with Delayed Feedback for",
            "url": "https://arxiv.org/pdf/2604.18107"
          },
          {
            "title": "On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/html/2601.06748v1"
          },
          {
            "title": "Long-Term Memory for VLA-based Agents in Open-World Task Execution",
            "url": "https://arxiv.org/html/2604.15671"
          },
          {
            "title": "[2604.15671] Long-Term Memory for VLA-based Agents in Open-World Task Execution",
            "url": "https://arxiv.org/abs/2604.15671"
          },
          {
            "title": "Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision–Language–Action Models via Latent Iterative Reasoning",
            "url": "https://arxiv.org/html/2602.07845v1"
          },
          {
            "title": "[2602.07845] Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision-Language-Action Models via Latent Iterative Reasoning",
            "url": "https://arxiv.org/abs/2602.07845"
          },
          {
            "title": "HELM: Harness-Enhanced Long-horizon Memory for Vision-Language-Action Manipulation",
            "url": "https://arxiv.org/html/2604.18791"
          },
          {
            "title": "Adaptor: Advancing Assistive Teleoperation with Few-Shot Learning and Cross-Operator Generalization",
            "url": "https://arxiv.org/html/2604.09462v1"
          }
        ]
      },
      "I found the arXiv paper you're looking for! Here are the key details about arXiv paper 2604.18107:\n\n**Title:** Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models\n\n**Authors and Affiliation:** The paper was authored by Zehua Zang, Xi Wang, Fuchun Sun, Xiao Xu, Lixiang Liu, Jiahuan Zhou, and Jiangmeng Li from the Institute of Software (Chinese Academy of Sciences), University of Chinese Academy of Sciences, Tsinghua University, Wangxuan Institute of Computer Technology (Peking University), and National Defense University\n\n**Submission Date:** Submitted on April 20, 2026\n\n**Main Contribution:** The paper proposes Perturbation learning with Delayed Feedback (PDF), a verifier-free test-time adaptation framework that improves decision performance without fine-tuning the base model.\n\n**Problem Addressed:** Vision-Language-Action models (VLAs) achieve remarkable performance in sequential decision-making but remain fragile to subtle environmental shifts, such as small changes in object pose. The brittleness is attributed to trajectory overfitting, where VLAs over-attend to the spurious correlation between actions and entities, then reproduce memorized action patterns.\n\n**Approach:** PDF mitigates the spurious correlation through uncertainty-based data augmentation and action voting, while an adaptive scheduler allocates augmentation budgets to balance performance and efficiency. PDF learns a lightweight perturbation module that retrospectively adjusts action logits guided by delayed feedback, correcting overconfidence issues."
    ],
    "durationSeconds": 7.609911642999999
  },
  "sourceToolAssistantUUID": "1df1fe7c-0fd0-443a-b13c-d5d6a0e06a60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-13T05:47:26.605Z_

```json
{
  "parentUuid": "e067830f-d6b2-4f1b-852e-0e839707ebd5",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2d26bb9a-eb2c-46d9-91af-1fa2df59c20d",
  "timestamp": "2026-05-13T05:47:26.605Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"Causal Token Selection for Invariant VLA Policies via Amortized Interv…",
  "leafUuid": "2d26bb9a-eb2c-46d9-91af-1fa2df59c20d",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise VLA causal token selection with ViT-Shapley differentiation",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82"
}
```

---

### Assistant

_source line 35 · 2026-05-13T05:47:32.807Z_

Good, I have solid details on all four papers. Let me now search for a couple more things: whether the vanishing token information paper has been tested on VLAs specifically, and any other recent work I might be missing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d26bb9a-eb2c-46d9-91af-1fa2df59c20d",
  "isSidechain": false,
  "requestId": "req_011Caz3KiUKtULavScePhKX7",
  "type": "assistant",
  "uuid": "14f42437-8973-4227-b62a-b6c9e354bb9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfG81XLn1gD5M5Ju2hWWzm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4749,
      "cache_read_input_tokens": 36208,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 36208,
          "cache_creation_input_tokens": 4749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4749
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

_source line 36 · 2026-05-13T05:47:33.614Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Lo8NH9WKq8FKjxqyzNUK4`</summary>

```json
{
  "query": "\"vanishing token information\" VLA visual tokens \"information horizon\" OpenVLA action prediction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14f42437-8973-4227-b62a-b6c9e354bb9a",
  "isSidechain": false,
  "requestId": "req_011Caz3KiUKtULavScePhKX7",
  "type": "assistant",
  "uuid": "d9a41dda-febc-473a-b05c-6006bda69ec2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfG81XLn1gD5M5Ju2hWWzm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4749,
      "cache_read_input_tokens": 36208,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 36208,
          "cache_creation_input_tokens": 4749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4749
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

_source line 37 · 2026-05-13T05:47:34.218Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015oWrrkRDin7WKgJgFs7oCk`</summary>

```json
{
  "query": "ViT-Shapley \"causal\" \"interventional\" Shapley values token selection robustness distribution shift"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9a41dda-febc-473a-b05c-6006bda69ec2",
  "isSidechain": false,
  "requestId": "req_011Caz3KiUKtULavScePhKX7",
  "type": "assistant",
  "uuid": "d1dd4365-6481-489f-a533-1f5b0330c1f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfG81XLn1gD5M5Ju2hWWzm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4749,
      "cache_read_input_tokens": 36208,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 36208,
          "cache_creation_input_tokens": 4749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4749
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

_source line 38 · 2026-05-13T05:47:40.697Z_

<details><summary>↩ Tool result · `toolu_013Lo8NH9WKq8FKjxqyzNUK4`</summary>

```text
Web search results for query: ""vanishing token information" VLA visual tokens "information horizon" OpenVLA action prediction 2026"

Links: [{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"Open-Loop Planning, Closed-Loop Verification: Speculative Verification for VLA","url":"https://arxiv.org/html/2604.02965"},{"title":"Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denosing Diffusion Process | OpenReview","url":"https://openreview.net/forum?id=UvQOcw2oCD"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=ZMnD6QZAE6"},{"title":"Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action Models","url":"https://arxiv.org/html/2509.23655v1"},{"title":"FAST: Efficient Action Tokenization for Vision-Language-Action Models","url":"https://www.pi.website/download/fast.pdf"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"}]

Based on the search results, I found relevant information about Vision-Language-Action (VLA) models and related concepts, though the specific term "vanishing token information" or "information horizon" as a distinct research concept doesn't appear explicitly in these results. However, I can provide some relevant context:

## Key Findings:

**Prediction Horizon in VLAs**: In VLA inference, H (prediction horizon) represents how many actions are predicted in each chunk. This relates to how many future actions the model predicts at once.

**OpenVLA and Action Prediction**: OpenVLA's formulation is to adopt a discrete tokenization strategy for robot action prediction through fine-tuning the Prismatic-7B VLM backbone, framing action prediction as a vision-language task that maps input observation images and natural language instructions to discrete robot action sequences.

**Token Information in Action Sequences**: VLAs predict future actions as "chunks," and highly correlated action tokens diminish the effectiveness of the next token prediction objective used in autoregressive VLAs. This suggests a challenge where information becomes less distinct across correlated action tokens in a sequence.

**Visual Token Efficiency**: Recent work like Oat-VLA has focused on optimizing visual tokens, where the method can drastically reduce the number of visual tokens to just a few tokens without sacrificing performance.

The search results don't contain a specific research paper or discussion titled with "vanishing token information" and "information horizon" as formal concepts. If you're looking for more specific recent research on this topic, you may want to check arxiv.org directly or provide additional context about where you encountered these terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9a41dda-febc-473a-b05c-6006bda69ec2",
  "isSidechain": false,
  "promptId": "c18dd896-5585-4f7b-b0bc-42c2f8ad78d2",
  "type": "user",
  "uuid": "9e73dcb9-bb38-4d00-95d0-0eb9765603dd",
  "toolUseResult": {
    "query": "\"vanishing token information\" VLA visual tokens \"information horizon\" OpenVLA action prediction 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018DnG1YFgBjRUDaeYch884s",
        "content": [
          {
            "title": "Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)",
            "url": "https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"
          },
          {
            "title": "VQ-VLA: Improving Vision-Language-Action Models via Scaling",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"
          },
          {
            "title": "Vision Language Action Models (VLA) & Policies for Robots",
            "url": "https://learnopencv.com/vision-language-action-models-lerobot-policy/"
          },
          {
            "title": "Open-Loop Planning, Closed-Loop Verification: Speculative Verification for VLA",
            "url": "https://arxiv.org/html/2604.02965"
          },
          {
            "title": "Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denosing Diffusion Process | OpenReview",
            "url": "https://openreview.net/forum?id=UvQOcw2oCD"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model | OpenReview",
            "url": "https://openreview.net/forum?id=ZMnD6QZAE6"
          },
          {
            "title": "Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action Models",
            "url": "https://arxiv.org/html/2509.23655v1"
          },
          {
            "title": "FAST: Efficient Action Tokenization for Vision-Language-Action Models",
            "url": "https://www.pi.website/download/fast.pdf"
          },
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          }
        ]
      },
      "Based on the search results, I found relevant information about Vision-Language-Action (VLA) models and related concepts, though the specific term \"vanishing token information\" or \"information horizon\" as a distinct research concept doesn't appear explicitly in these results. However, I can provide some relevant context:\n\n## Key Findings:\n\n**Prediction Horizon in VLAs**: In VLA inference, H (prediction horizon) represents how many actions are predicted in each chunk. This relates to how many future actions the model predicts at once.\n\n**OpenVLA and Action Prediction**: OpenVLA's formulation is to adopt a discrete tokenization strategy for robot action prediction through fine-tuning the Prismatic-7B VLM backbone, framing action prediction as a vision-language task that maps input observation images and natural language instructions to discrete robot action sequences.\n\n**Token Information in Action Sequences**: VLAs predict future actions as \"chunks,\" and highly correlated action tokens diminish the effectiveness of the next token prediction objective used in autoregressive VLAs. This suggests a challenge where information becomes less distinct across correlated action tokens in a sequence.\n\n**Visual Token Efficiency**: Recent work like Oat-VLA has focused on optimizing visual tokens, where the method can drastically reduce the number of visual tokens to just a few tokens without sacrificing performance.\n\nThe search results don't contain a specific research paper or discussion titled with \"vanishing token information\" and \"information horizon\" as formal concepts. If you're looking for more specific recent research on this topic, you may want to check arxiv.org directly or provide additional context about where you encountered these terms."
    ],
    "durationSeconds": 7.0771364060000055
  },
  "sourceToolAssistantUUID": "d9a41dda-febc-473a-b05c-6006bda69ec2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-13T05:47:40.932Z_

<details><summary>↩ Tool result · `toolu_015oWrrkRDin7WKgJgFs7oCk`</summary>

```text
Web search results for query: "ViT-Shapley "causal" "interventional" Shapley values token selection robustness distribution shift"

Links: [{"title":"Causal Shapley Values: Exploiting Causal Knowledge to ...","url":"https://proceedings.neurips.cc/paper/2020/file/32e54441e6382a7fbacbbbaf3c450059-Paper.pdf"},{"title":"Causal Shapley Values: Exploiting Causal Knowledge","url":"https://papers.neurips.cc/paper_files/paper/2020/file/32e54441e6382a7fbacbbbaf3c450059-Paper.pdf"},{"title":"Explaining individual predictions when features are dependent: More accurate approximations to Shapley values - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0004370221000539"},{"title":"A feature selection method based on Shapley values robust for concept shift in regression | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-024-09745-4"},{"title":"Manifold Restricted Interventional Shapley Values Muhammad Faaiz Tauﬁq1","url":"https://arxiv.org/pdf/2301.04041"},{"title":"Manifold Restricted Interventional Shapley Values Muhammad Faaiz Taufiq1","url":"https://proceedings.mlr.press/v206/taufiq23a/taufiq23a.pdf"},{"title":"1 Causal Analysis of Shapley Values: Conditional vs. Marginal Ilya Rozenfeld","url":"https://arxiv.org/pdf/2409.06157"},{"title":"Master thesis Computer Science Radboud University Causal Shapley values for","url":"https://www.cs.ru.nl/masters-theses/2020/E_Sijben___Causal_Shapley_values_for_interpretable_machine_learning.pdf"},{"title":"[1910.13413] Feature relevance quantification in explainable AI: A causal problem","url":"https://ar5iv.labs.arxiv.org/html/1910.13413"},{"title":"[2011.01625] Causal Shapley Values: Exploiting Causal Knowledge to Explain Individual Predictions of Complex Models","url":"https://arxiv.org/abs/2011.01625"}]

Based on the search results, I found relevant information about causal and interventional Shapley values, along with related concepts on robustness and distribution shift. However, the results don't contain specific information about "ViT-Shapley" (Vision Transformer-Shapley) or token selection. Let me provide what was found:

## Key Findings on Causal and Interventional Shapley Values

The term 'causal' Shapley values refers to those that attempt to incorporate causal relationships using Pearl's do-calculus, while 'interventional' Shapley values have been coined for causal explanations of the prediction algorithm that ignore causal relationships between features in the real world.

Causal interpretation of Shapley values involves replacing conventional "conditioning by observation" with "conditioning by intervention", as in Pearl's do-calculus.

## Robustness and Distribution Shift

ManifoldShap provides a compromise between conditional and interventional Shapley values, attempting to estimate causal contributions of features while providing robustness guarantees.

When dealing with dataset shifts and concept shifts, the influence of a variable cannot be the only indicator of its quality as a regressor, since relationships learned during training may not correspond to the current situation. An approach can establish a direct relationship between Shapley values and prediction errors to effectively detect individual biases introduced by each variable.

The search results don't specifically address ViT-Shapley or token selection for Vision Transformers. For more targeted information on that topic, a more specific search would be needed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1dd4365-6481-489f-a533-1f5b0330c1f7",
  "isSidechain": false,
  "promptId": "c18dd896-5585-4f7b-b0bc-42c2f8ad78d2",
  "type": "user",
  "uuid": "b3bd7903-1fcf-44ac-b59c-a7ad27d832bb",
  "toolUseResult": {
    "query": "ViT-Shapley \"causal\" \"interventional\" Shapley values token selection robustness distribution shift",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Vxog3wRp3C3T4JmWb6eZPW",
        "content": [
          {
            "title": "Causal Shapley Values: Exploiting Causal Knowledge to ...",
            "url": "https://proceedings.neurips.cc/paper/2020/file/32e54441e6382a7fbacbbbaf3c450059-Paper.pdf"
          },
          {
            "title": "Causal Shapley Values: Exploiting Causal Knowledge",
            "url": "https://papers.neurips.cc/paper_files/paper/2020/file/32e54441e6382a7fbacbbbaf3c450059-Paper.pdf"
          },
          {
            "title": "Explaining individual predictions when features are dependent: More accurate approximations to Shapley values - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0004370221000539"
          },
          {
            "title": "A feature selection method based on Shapley values robust for concept shift in regression | Neural Computing and Applications | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s00521-024-09745-4"
          },
          {
            "title": "Manifold Restricted Interventional Shapley Values Muhammad Faaiz Tauﬁq1",
            "url": "https://arxiv.org/pdf/2301.04041"
          },
          {
            "title": "Manifold Restricted Interventional Shapley Values Muhammad Faaiz Taufiq1",
            "url": "https://proceedings.mlr.press/v206/taufiq23a/taufiq23a.pdf"
          },
          {
            "title": "1 Causal Analysis of Shapley Values: Conditional vs. Marginal Ilya Rozenfeld",
            "url": "https://arxiv.org/pdf/2409.06157"
          },
          {
            "title": "Master thesis Computer Science Radboud University Causal Shapley values for",
            "url": "https://www.cs.ru.nl/masters-theses/2020/E_Sijben___Causal_Shapley_values_for_interpretable_machine_learning.pdf"
          },
          {
            "title": "[1910.13413] Feature relevance quantification in explainable AI: A causal problem",
            "url": "https://ar5iv.labs.arxiv.org/html/1910.13413"
          },
          {
            "title": "[2011.01625] Causal Shapley Values: Exploiting Causal Knowledge to Explain Individual Predictions of Complex Models",
            "url": "https://arxiv.org/abs/2011.01625"
          }
        ]
      },
      "Based on the search results, I found relevant information about causal and interventional Shapley values, along with related concepts on robustness and distribution shift. However, the results don't contain specific information about \"ViT-Shapley\" (Vision Transformer-Shapley) or token selection. Let me provide what was found:\n\n## Key Findings on Causal and Interventional Shapley Values\n\nThe term 'causal' Shapley values refers to those that attempt to incorporate causal relationships using Pearl's do-calculus, while 'interventional' Shapley values have been coined for causal explanations of the prediction algorithm that ignore causal relationships between features in the real world.\n\nCausal interpretation of Shapley values involves replacing conventional \"conditioning by observation\" with \"conditioning by intervention\", as in Pearl's do-calculus.\n\n## Robustness and Distribution Shift\n\nManifoldShap provides a compromise between conditional and interventional Shapley values, attempting to estimate causal contributions of features while providing robustness guarantees.\n\nWhen dealing with dataset shifts and concept shifts, the influence of a variable cannot be the only indicator of its quality as a regressor, since relationships learned during training may not correspond to the current situation. An approach can establish a direct relationship between Shapley values and prediction errors to effectively detect individual biases introduced by each variable.\n\nThe search results don't specifically address ViT-Shapley or token selection for Vision Transformers. For more targeted information on that topic, a more specific search would be needed."
    ],
    "durationSeconds": 6.711355858000003
  },
  "sourceToolAssistantUUID": "d1dd4365-6481-489f-a533-1f5b0330c1f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-13T05:48:02.703Z_

<details><summary>Logged reasoning block</summary>

```text
Good. I now have a thorough understanding of all four flagged issues. Let me also check for Causal Shapley Values (NeurIPS 2020) as this is related to the distinction between observational and interventional Shapley values that matters for ViT-Shapley differentiation.

Now let me think about the revision strategy:

1. **ViT-Shapley**: This is the most important addition. I need to integrate it into the landscape, opportunity, and approach sections. Key points:
   - ViT-Shapley uses a three-stage pipeline: train classifier → train surrogate with attention masking → train explainer to predict Shapley values in one forward pass
   - The explainer predicts observational Shapley values for model explanation, while CaTS differs by estimating interventional/causal effects through environment-marginal replacement and targeting cross-environment invariance rather than single-model explanation
   - ViT-Shapley's attention masking approach could inform how CaTS designs its intervention mechanism, and the Causal Shapley Values literature provides the theoretical grounding for distinguishing between observational and interventional Shapley values

2. **Mechanistic Interpretability for VLA Steering (CoRL 2025)**: This validates CaTS's core premise that interventional methods can effectively steer model behavior.

3. **VLM→VLA extrapolation**: The referenced work evaluates VLMs rather than VLAs, so verifying the information horizon in actual VLAs becomes part of the empirical contribution.

4. **PDF (arXiv 2604.18107)**: A complementary test-time approach worth noting in the broader landscape.

The reviewer flagged these as targeted, fixable issues—the core idea is sound, just needs better related work coverage and acknowledgment of one key assumption. I should integrate ViT-Shapley more thoroughly into the landscape and differentiation sections, then finalize the revised JSON.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3bd7903-1fcf-44ac-b59c-a7ad27d832bb",
  "isSidechain": false,
  "requestId": "req_011Caz3Lmp2XcU1rH71MeefY",
  "type": "assistant",
  "uuid": "c9ad0252-7826-415f-9d6e-afc6e2f5226f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUKU1oG8XdUds8pw6XurWC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2141,
      "cache_read_input_tokens": 40957,
      "output_tokens": 3298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2141,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3298,
          "cache_read_input_tokens": 40957,
          "cache_creation_input_tokens": 2141,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2141
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

_source line 41 · 2026-05-13T05:48:04.488Z_

I now have detailed understanding of all four papers. Let me synthesize and produce the revision. The issues are genuinely targeted — the core idea is sound, and these are related work gaps plus one assumption acknowledgment. This is a minor fix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9ad0252-7826-415f-9d6e-afc6e2f5226f",
  "isSidechain": false,
  "requestId": "req_011Caz3Lmp2XcU1rH71MeefY",
  "type": "assistant",
  "uuid": "dcb06852-4931-4383-ba45-43470b9be9ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUKU1oG8XdUds8pw6XurWC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2141,
      "cache_read_input_tokens": 40957,
      "output_tokens": 3298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2141,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3298,
          "cache_read_input_tokens": 40957,
          "cache_creation_input_tokens": 2141,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2141
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

_source line 42 · 2026-05-13T05:49:04.549Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DrprPHVpyidUfCuAfRhyri`</summary>

```json
{
  "description": "Draft revised research idea JSON",
  "prompt": "I need you to help me produce a complete revised JSON for a research idea called \"Causal Token Selection for Invariant VLA Policies via Amortized Interventional Scoring\" (CaTS). I'll give you the specific changes needed and you should output the complete JSON.\n\nThe reviewer flagged 4 issues, all related work gaps or assumption acknowledgments. The proposal is \"close to passing.\" This is a minor fix.\n\nHere are the SPECIFIC changes I need integrated into each field:\n\n## Changes to `core_problem`\nNo changes needed — the problem framing is solid.\n\n## Changes to `opportunity`\nAdd two sentences about ViT-Shapley and mechanistic interpretability:\n- After the sentence about causal attention distillation (LeaF), add: \"A fourth thread — amortized Shapley estimation for vision transformers — demonstrates the feasibility of training a lightweight explainer model to predict per-patch importance scores in a single forward pass (ViT-Shapley, ICLR 2023 Oral, arXiv 2206.05282), but targets observational Shapley values for model explanation rather than interventional causal effects for cross-environment robustness.\"\n- Add: \"Mechanistic interpretability work (arXiv 2509.00328, CoRL 2025) has independently validated that interventional methods can identify causally relevant structure in VLA representations — activation projection identifies sparse semantic directions in OpenVLA and Pi0 that are causally linked to action selection — but operates at the neuron/direction level for behavioral steering rather than the token level for robustness-oriented selection.\"\n\nRenumber the existing \"fourth thread\" (CIRRL) to \"sixth thread\" and adjust thread numbering.\n\n## Changes to `landscape`\nAdd three new sections:\n\n1. **Amortized Shapley estimation for vision transformers**: \"ViT-Shapley (ICLR 2023 Oral, arXiv 2206.05282) trains a separate explainer model to predict per-patch Shapley values in a single forward pass, using a three-stage pipeline: (1) train ViT classifier, (2) fine-tune a surrogate with attention masking to handle partial inputs, (3) train the explainer to amortize Shapley computation. The explainer produces 196 per-patch importance scores (14×14 grid) and outperforms attention rollout, GradCAM, and LRP for ViT explanation. Publicly available code (github.com/suinleelab/vit-shapley). CaTS's amortized causal scoring head is architecturally analogous — both train a lightweight model to predict per-token importance from embeddings in a single forward pass. The critical difference: ViT-Shapley estimates observational Shapley values (how much does masking patch i change the model's prediction?) for post-hoc explanation of a fixed model on a single distribution, while CaTS estimates interventional causal effects (how much does replacing token i with environment-marginal statistics change action predictions across environments?) for cross-environment invariance during training. This distinction parallels the broader observational vs. interventional Shapley literature (Heskes et al., NeurIPS 2020): observational Shapley captures feature relevance within a distribution, while interventional Shapley captures causal influence robust to distribution shift. CaTS's intervention mechanism (environment-marginal replacement across LIBERO-Plus perturbation dimensions) is specifically designed to distinguish causal from spuriously correlated tokens — a distinction that observational Shapley cannot make when spurious correlations are present in the training distribution. ViT-Shapley's attention masking approach for evaluating ViTs with partial information is directly applicable to CaTS's intervention mechanism and informs implementation.\"\n\n2. **Mechanistic interpretability for VLA**: \"Mechanistic interpretability for VLA steering (CoRL 2025, arXiv 2509.00328) projects feedforward activations onto the token embedding basis to identify sparse semantic directions — such as speed and direction — that are causally linked to action selection in OpenVLA and Pi0. Enables zero-shot behavioral steering on LIBERO and real UR5 robot without fine-tuning. This validates CaTS's core premise: interventional methods can identify causally relevant structure in VLA representations. Key differentiation: operates at the neuron/direction level for behavioral steering (which directions in activation space control speed/direction?), while CaTS operates at the token level for robustness-oriented selection (which input patches contain causal vs. spurious visual information?). The two approaches are complementary — mechanistic interpretability explains how VLA representations encode action semantics, while CaTS identifies which visual tokens should feed into those representations for cross-environment robustness.\"\n\n3. **Test-time adaptation**: \"PDF (arXiv 2604.18107, April 2026) addresses VLA spurious correlations ('trajectory overfitting where VLAs over-attend to spurious correlation between actions and entities') via test-time perturbation learning with delayed feedback. Uses uncertainty-based data augmentation and action voting without fine-tuning, achieving +7.4% on LIBERO. Complementary to CaTS: PDF is a test-time adaptation method that corrects overconfident action predictions post-hoc, while CaTS is a training-time causal selection method that prevents spurious correlations from entering the policy. The two could be combined — CaTS for principled token selection during training, PDF for residual correction at test time.\"\n\n## Changes to `approach`\n1. In the \"Encoder-level spatial locality assumption\" justification paragraph, after the sentence about vanishing token information, add: \"**Important caveat**: arXiv 2512.07580 evaluates VLMs (Qwen2.5-VL, LLaVA-1.5), not VLAs. While VLAs share the VLM backbone architecture making extrapolation reasonable, VLA models have different training objectives (action prediction vs. text generation) and potentially different attention patterns — action tokens may attend to visual tokens differently than text tokens. The information horizon position may differ for VLAs. Verifying the information horizon in VLA architectures is an explicit part of our empirical contribution (ablation b: encoder-level vs. intermediate-layer vs. late-layer scoring directly tests where spatial information degrades in VLA models).\"\n\n2. In the \"Amortized Causal Scoring\" section, add connection to ViT-Shapley: \"**Relationship to ViT-Shapley (ICLR 2023)**: CaTS's amortized scoring architecture draws on the ViT-Shapley paradigm of training a separate model to predict per-token importance in a single forward pass. However, CaTS departs in three key ways: (a) the scoring target is interventional causal effects computed via environment-marginal token replacement across LIBERO-Plus perturbation dimensions, not observational Shapley values computed via masking on a single distribution; (b) the surrogate stage uses multi-environment intervention data rather than random masking, training the scorer to predict action distribution stability across environments rather than prediction change under masking; (c) the scorer is integrated into a training-time robustness objective (composite V-REx + DRO loss), not used for post-hoc explanation. ViT-Shapley's attention masking approach for evaluating ViTs with partial information informs our intervention mechanism — we adapt their masking strategy to implement environment-marginal token replacement, replacing masked tokens with marginal statistics pooled across perturbation environments rather than zeroing them out.\"\n\n3. In the \"Key differentiations\" section, add two entries:\n\n\"vs. ViT-Shapley (ICLR 2023): CaTS's amortized scorer is architecturally analogous to ViT-Shapley's learned explainer — both predict per-token importance from embeddings in one forward pass. The fundamental difference is the scoring target: ViT-Shapley estimates observational Shapley values for explaining a model's predictions within a single distribution; CaTS estimates interventional causal effects across environments to identify tokens whose influence on actions is invariant to visual distribution shifts. Observational Shapley values cannot distinguish causal from spuriously correlated tokens when both correlate with the outcome in the training distribution. CaTS's environment-marginal replacement directly probes cross-environment invariance, providing the causal grounding that ViT-Shapley's masking-based approach lacks.\"\n\n\"vs. Mechanistic Interpretability for VLA Steering (CoRL 2025): Both use interventional methods on VLA representations. The steering work identifies neuron-level semantic directions (speed, direction) for zero-shot behavioral control; CaTS identifies token-level causal importance for robustness under visual distribution shift. Complementary: steering explains internal action semantics, CaTS determines which visual inputs matter.\"\n\n## Changes to `key_references`\nAdd these 4 new references:\n- \"Learning to Estimate Shapley Values with Vision Transformers [ViT-Shapley] (ICLR 2023 Oral, arXiv 2206.05282)\"\n- \"Mechanistic Interpretability for Steering Vision-Language-Action Models (CoRL 2025, arXiv 2509.00328)\"  \n- \"Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models [PDF] (arXiv 2604.18107, April 2026)\"\n- \"Causal Shapley Values: Exploiting Causal Knowledge to Explain Individual Predictions of Complex Models (NeurIPS 2020, arXiv 2011.01625)\"\n\n## Changes to `description`\nAdd a brief mention of the new related work coverage:\nAfter \"Key advances over v2:\" add \"(5) Explicit differentiation from ViT-Shapley (ICLR 2023 Oral) — CaTS's amortized scorer extends the ViT-Shapley paradigm from observational Shapley values for model explanation to interventional causal effects for cross-environment invariance. (6) Acknowledgment that the 'vanishing token information' finding (arXiv 2512.07580) was validated on VLMs, not VLAs — verifying the information horizon in VLA architectures is part of the empirical contribution. (7) Integration with mechanistic interpretability evidence (CoRL 2025) validating that interventional methods identify causal structure in VLA representations, and positioning against test-time adaptation approaches (PDF, arXiv 2604.18107) as complementary training-time vs. test-time methods for the same spurious correlation problem.\"\n\n## Other fields\n- `change_type`: \"minor\"\n- All other fields (title, core_problem, resource_estimate, target_venues, level, project_name, source) remain IDENTICAL to the original.\n\nPlease output the COMPLETE JSON object with all these changes integrated. Make sure to preserve every detail from the original that isn't being changed. The JSON should be valid and complete.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcb06852-4931-4383-ba45-43470b9be9ea",
  "isSidechain": false,
  "requestId": "req_011Caz3Lmp2XcU1rH71MeefY",
  "type": "assistant",
  "uuid": "cd331472-05ef-446c-9331-2e2025c9698e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUKU1oG8XdUds8pw6XurWC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2141,
      "cache_read_input_tokens": 40957,
      "output_tokens": 3298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2141,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3298,
          "cache_read_input_tokens": 40957,
          "cache_creation_input_tokens": 2141,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2141
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

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"Causal Token Selection for Invariant VLA Policies via Amortized Interv…",
  "leafUuid": "cd331472-05ef-446c-9331-2e2025c9698e",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise VLA causal token selection with ViT-Shapley differentiation",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82"
}
```

---

### Tool result

_source line 45 · 2026-05-13T06:05:34.700Z_

<details><summary>↩ Tool result · `toolu_01DrprPHVpyidUfCuAfRhyri`</summary>

````text
&lt;persisted-output>
Output too large (59.2KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-/d1da6575-a77d-4a5e-984b-7ebc8af7dd82/tool-results/toolu_01DrprPHVpyidUfCuAfRhyri.json

Preview (first 2KB):
[
  {
    "type": "text",
    "text": "The file write needs permission. Let me verify the JSON is valid by outputting it directly. Here is the complete revised JSON with all changes integrated:\n\n```json\n{\n  \"title\": \"Causal Token Selection for Invariant VLA Policies via Amortized Interventional Scoring\",\n  \"change_type\": \"minor\",\n  \"core_problem\": \"VLA models learn spurious visual correlations — attending to background textures, lighting conditions, and distractor objects that co-occur with target actions in training data — causing catastrophic failure under visual distribution shifts. Recent work (arXiv 2502.11501, ACL Findings 2025; arXiv 2512.07580, ICLR 2026) reveals two critical findings: (1) many attention-based token pruning methods underperform even naive random selection due to flawed scoring criteria, and (2) visual token information 'vanishes' in deep LLM layers, becoming uniformly uninformative beyond an 'information horizon' — meaning that any token selection must operate before this horizon. Meanwhile, a proliferation of concurrent VLA token selection methods (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, Compressor-VLA, Gaze-VLA — all 2025-2026) each propose different heuristic criteria (attention intersection, cross-attention TopK, Gumbel softmax, Kendall rank consistency, spatio-semantic dual-aware scoring, hierarchical importance, instruction-guided compression, gaze alignment), yet none provide formal justification for why their criterion identifies task-relevant tokens rather than merely attention-salient tokens. A complementary line of work addresses VLA spurious correlations via language-guided spatial reasoning (InSpire, arXiv 2505.13888), redirecting attention through prompting rather than principled token selection. Simple adaptation methods like FTM (arXiv 2512.02902) can recover substantial robustness with only 4K parameters, raising the question: can we identify *why* certain tokens matter and provide interpretable, forma
...
&lt;/persisted-output>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "cd331472-05ef-446c-9331-2e2025c9698e",
  "isSidechain": false,
  "promptId": "c18dd896-5585-4f7b-b0bc-42c2f8ad78d2",
  "type": "user",
  "uuid": "eb680509-7b00-4439-99e0-ffa4ef559deb",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to help me produce a complete revised JSON for a research idea called \"Causal Token Selection for Invariant VLA Policies via Amortized Interventional Scoring\" (CaTS). I'll give you the specific changes needed and you should output the complete JSON.\n\nThe reviewer flagged 4 issues, all related work gaps or assumption acknowledgments. The proposal is \"close to passing.\" This is a minor fix.\n\nHere are the SPECIFIC changes I need integrated into each field:\n\n## Changes to `core_problem`\nNo changes needed — the problem framing is solid.\n\n## Changes to `opportunity`\nAdd two sentences about ViT-Shapley and mechanistic interpretability:\n- After the sentence about causal attention distillation (LeaF), add: \"A fourth thread — amortized Shapley estimation for vision transformers — demonstrates the feasibility of training a lightweight explainer model to predict per-patch importance scores in a single forward pass (ViT-Shapley, ICLR 2023 Oral, arXiv 2206.05282), but targets observational Shapley values for model explanation rather than interventional causal effects for cross-environment robustness.\"\n- Add: \"Mechanistic interpretability work (arXiv 2509.00328, CoRL 2025) has independently validated that interventional methods can identify causally relevant structure in VLA representations — activation projection identifies sparse semantic directions in OpenVLA and Pi0 that are causally linked to action selection — but operates at the neuron/direction level for behavioral steering rather than the token level for robustness-oriented selection.\"\n\nRenumber the existing \"fourth thread\" (CIRRL) to \"sixth thread\" and adjust thread numbering.\n\n## Changes to `landscape`\nAdd three new sections:\n\n1. **Amortized Shapley estimation for vision transformers**: \"ViT-Shapley (ICLR 2023 Oral, arXiv 2206.05282) trains a separate explainer model to predict per-patch Shapley values in a single forward pass, using a three-stage pipeline: (1) train ViT classifier, (2) fine-tune a surrogate with attention masking to handle partial inputs, (3) train the explainer to amortize Shapley computation. The explainer produces 196 per-patch importance scores (14×14 grid) and outperforms attention rollout, GradCAM, and LRP for ViT explanation. Publicly available code (github.com/suinleelab/vit-shapley). CaTS's amortized causal scoring head is architecturally analogous — both train a lightweight model to predict per-token importance from embeddings in a single forward pass. The critical difference: ViT-Shapley estimates observational Shapley values (how much does masking patch i change the model's prediction?) for post-hoc explanation of a fixed model on a single distribution, while CaTS estimates interventional causal effects (how much does replacing token i with environment-marginal statistics change action predictions across environments?) for cross-environment invariance during training. This distinction parallels the broader observational vs. interventional Shapley literature (Heskes et al., NeurIPS 2020): observational Shapley captures feature relevance within a distribution, while interventional Shapley captures causal influence robust to distribution shift. CaTS's intervention mechanism (environment-marginal replacement across LIBERO-Plus perturbation dimensions) is specifically designed to distinguish causal from spuriously correlated tokens — a distinction that observational Shapley cannot make when spurious correlations are present in the training distribution. ViT-Shapley's attention masking approach for evaluating ViTs with partial information is directly applicable to CaTS's intervention mechanism and informs implementation.\"\n\n2. **Mechanistic interpretability for VLA**: \"Mechanistic interpretability for VLA steering (CoRL 2025, arXiv 2509.00328) projects feedforward activations onto the token embedding basis to identify sparse semantic directions — such as speed and direction — that are causally linked to action selection in OpenVLA and Pi0. Enables zero-shot behavioral steering on LIBERO and real UR5 robot without fine-tuning. This validates CaTS's core premise: interventional methods can identify causally relevant structure in VLA representations. Key differentiation: operates at the neuron/direction level for behavioral steering (which directions in activation space control speed/direction?), while CaTS operates at the token level for robustness-oriented selection (which input patches contain causal vs. spurious visual information?). The two approaches are complementary — mechanistic interpretability explains how VLA representations encode action semantics, while CaTS identifies which visual tokens should feed into those representations for cross-environment robustness.\"\n\n3. **Test-time adaptation**: \"PDF (arXiv 2604.18107, April 2026) addresses VLA spurious correlations ('trajectory overfitting where VLAs over-attend to spurious correlation between actions and entities') via test-time perturbation learning with delayed feedback. Uses uncertainty-based data augmentation and action voting without fine-tuning, achieving +7.4% on LIBERO. Complementary to CaTS: PDF is a test-time adaptation method that corrects overconfident action predictions post-hoc, while CaTS is a training-time causal selection method that prevents spurious correlations from entering the policy. The two could be combined — CaTS for principled token selection during training, PDF for residual correction at test time.\"\n\n## Changes to `approach`\n1. In the \"Encoder-level spatial locality assumption\" justification paragraph, after the sentence about vanishing token information, add: \"**Important caveat**: arXiv 2512.07580 evaluates VLMs (Qwen2.5-VL, LLaVA-1.5), not VLAs. While VLAs share the VLM backbone architecture making extrapolation reasonable, VLA models have different training objectives (action prediction vs. text generation) and potentially different attention patterns — action tokens may attend to visual tokens differently than text tokens. The information horizon position may differ for VLAs. Verifying the information horizon in VLA architectures is an explicit part of our empirical contribution (ablation b: encoder-level vs. intermediate-layer vs. late-layer scoring directly tests where spatial information degrades in VLA models).\"\n\n2. In the \"Amortized Causal Scoring\" section, add connection to ViT-Shapley: \"**Relationship to ViT-Shapley (ICLR 2023)**: CaTS's amortized scoring architecture draws on the ViT-Shapley paradigm of training a separate model to predict per-token importance in a single forward pass. However, CaTS departs in three key ways: (a) the scoring target is interventional causal effects computed via environment-marginal token replacement across LIBERO-Plus perturbation dimensions, not observational Shapley values computed via masking on a single distribution; (b) the surrogate stage uses multi-environment intervention data rather than random masking, training the scorer to predict action distribution stability across environments rather than prediction change under masking; (c) the scorer is integrated into a training-time robustness objective (composite V-REx + DRO loss), not used for post-hoc explanation. ViT-Shapley's attention masking approach for evaluating ViTs with partial information informs our intervention mechanism — we adapt their masking strategy to implement environment-marginal token replacement, replacing masked tokens with marginal statistics pooled across perturbation environments rather than zeroing them out.\"\n\n3. In the \"Key differentiations\" section, add two entries:\n\n\"vs. ViT-Shapley (ICLR 2023): CaTS's amortized scorer is architecturally analogous to ViT-Shapley's learned explainer — both predict per-token importance from embeddings in one forward pass. The fundamental difference is the scoring target: ViT-Shapley estimates observational Shapley values for explaining a model's predictions within a single distribution; CaTS estimates interventional causal effects across environments to identify tokens whose influence on actions is invariant to visual distribution shifts. Observational Shapley values cannot distinguish causal from spuriously correlated tokens when both correlate with the outcome in the training distribution. CaTS's environment-marginal replacement directly probes cross-environment invariance, providing the causal grounding that ViT-Shapley's masking-based approach lacks.\"\n\n\"vs. Mechanistic Interpretability for VLA Steering (CoRL 2025): Both use interventional methods on VLA representations. The steering work identifies neuron-level semantic directions (speed, direction) for zero-shot behavioral control; CaTS identifies token-level causal importance for robustness under visual distribution shift. Complementary: steering explains internal action semantics, CaTS determines which visual inputs matter.\"\n\n## Changes to `key_references`\nAdd these 4 new references:\n- \"Learning to Estimate Shapley Values with Vision Transformers [ViT-Shapley] (ICLR 2023 Oral, arXiv 2206.05282)\"\n- \"Mechanistic Interpretability for Steering Vision-Language-Action Models (CoRL 2025, arXiv 2509.00328)\"  \n- \"Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models [PDF] (arXiv 2604.18107, April 2026)\"\n- \"Causal Shapley Values: Exploiting Causal Knowledge to Explain Individual Predictions of Complex Models (NeurIPS 2020, arXiv 2011.01625)\"\n\n## Changes to `description`\nAdd a brief mention of the new related work coverage:\nAfter \"Key advances over v2:\" add \"(5) Explicit differentiation from ViT-Shapley (ICLR 2023 Oral) — CaTS's amortized scorer extends the ViT-Shapley paradigm from observational Shapley values for model explanation to interventional causal effects for cross-environment invariance. (6) Acknowledgment that the 'vanishing token information' finding (arXiv 2512.07580) was validated on VLMs, not VLAs — verifying the information horizon in VLA architectures is part of the empirical contribution. (7) Integration with mechanistic interpretability evidence (CoRL 2025) validating that interventional methods identify causal structure in VLA representations, and positioning against test-time adaptation approaches (PDF, arXiv 2604.18107) as complementary training-time vs. test-time methods for the same spurious correlation problem.\"\n\n## Other fields\n- `change_type`: \"minor\"\n- All other fields (title, core_problem, resource_estimate, target_venues, level, project_name, source) remain IDENTICAL to the original.\n\nPlease output the COMPLETE JSON object with all these changes integrated. Make sure to preserve every detail from the original that isn't being changed. The JSON should be valid and complete.\n",
    "agentId": "ad283643819abe769",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "The file write needs permission. Let me verify the JSON is valid by outputting it directly. Here is the complete revised JSON with all changes integrated:\n\n```json\n{\n  \"title\": \"Causal Token Selection for Invariant VLA Policies via Amortized Interventional Scoring\",\n  \"change_type\": \"minor\",\n  \"core_problem\": \"VLA models learn spurious visual correlations — attending to background textures, lighting conditions, and distractor objects that co-occur with target actions in training data — causing catastrophic failure under visual distribution shifts. Recent work (arXiv 2502.11501, ACL Findings 2025; arXiv 2512.07580, ICLR 2026) reveals two critical findings: (1) many attention-based token pruning methods underperform even naive random selection due to flawed scoring criteria, and (2) visual token information 'vanishes' in deep LLM layers, becoming uniformly uninformative beyond an 'information horizon' — meaning that any token selection must operate before this horizon. Meanwhile, a proliferation of concurrent VLA token selection methods (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, Compressor-VLA, Gaze-VLA — all 2025-2026) each propose different heuristic criteria (attention intersection, cross-attention TopK, Gumbel softmax, Kendall rank consistency, spatio-semantic dual-aware scoring, hierarchical importance, instruction-guided compression, gaze alignment), yet none provide formal justification for why their criterion identifies task-relevant tokens rather than merely attention-salient tokens. A complementary line of work addresses VLA spurious correlations via language-guided spatial reasoning (InSpire, arXiv 2505.13888), redirecting attention through prompting rather than principled token selection. Simple adaptation methods like FTM (arXiv 2512.02902) can recover substantial robustness with only 4K parameters, raising the question: can we identify *why* certain tokens matter and provide interpretable, formally grounded selection criteria rather than black-box affine recalibration?\",\n  \"opportunity\": \"Three research threads have developed in isolation: (1) causal intervention for imitation learning robustness (Causal-ACT, arXiv 2507.22380; ICIL, NeurIPS 2021), operating at the feature level in smaller architectures, (2) VLA token pruning for efficiency and robustness (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, VLA-Pruner, VLA-IAP, OTPrune, Compressor-VLA, SpecPrune-VLA, VLA-Cache), using attention/gradient/geometric/rank/temporal heuristics without causal grounding, and (3) causal attention distillation (LeaF, NeurIPS 2025) and learnable pruning (LearnPruner, arXiv 2604.23950), which move beyond pure attention heuristics but lack formal causal intervention criteria. A fourth thread — amortized Shapley estimation for vision transformers — demonstrates the feasibility of training a lightweight explainer model to predict per-patch importance scores in a single forward pass (ViT-Shapley, ICLR 2023 Oral, arXiv 2206.05282), but targets observational Shapley values for model explanation rather than interventional causal effects for cross-environment robustness. Mechanistic interpretability work (arXiv 2509.00328, CoRL 2025) has independently validated that interventional methods can identify causally relevant structure in VLA representations — activation projection identifies sparse semantic directions in OpenVLA and Pi0 that are causally linked to action selection — but operates at the neuron/direction level for behavioral steering rather than the token level for robustness-oriented selection. A sixth thread — causality-inspired robustness theory — has recently achieved a breakthrough: CIRRL (arXiv 2505.12868) provides the first finite-radius robustness guarantee in nonlinear settings by combining identifiable representation learning with anchor regression, showing that operating at the representation level (where latent variables are identifiable up to affine transformation) is the key to extending causal robustness beyond linear models. A critical empirical finding connects these threads to VLA architectures specifically: visual tokens in VLA architectures preserve spatial correspondence to image patches at the vision encoder output (where SigLIP provides semantic and DINOv2 provides spatial features), but this spatial structure degrades progressively through LLM layers due to self-attention mixing, ultimately vanishing at an 'information horizon' (arXiv 2512.07580). This means token-level causal selection must operate at or near the vision encoder output — where spatial locality is preserved by construction — rather than at deep LLM layers where existing attention-based methods struggle (explaining why they often underperform random selection). The vision encoder output provides a form of identifiable representation (spatial correspondence = patch-level identifiability), analogous to CIRRL's requirement for identifiable latent variables, suggesting that representation-level causal robustness can extend to the VLA setting. Formalizing this insight via a structural causal model over the token-action pipeline, with amortized interventional scoring operating at the pre-LLM representation layer, would provide the principled criterion that existing pruning methods lack while operating in the representation space where the criterion is most valid.\",\n  \"landscape\": \"**Robustness benchmarking**: LIBERO-Plus (arXiv 2510.13626, CVPR 2026) demonstrates VLA catastrophic failures across 7 perturbation dimensions, with the current SOTA at 82.1% average success (SRPO, arXiv 2511.15605) — SRPO achieves 167% improvement over one-shot SFT baseline via self-referential RL without token selection. **Causal approaches in imitation learning**: Causal-ACT (arXiv 2507.22380, July 2025) integrates causal structure learning into ACT by learning binary causal graphs over ResNet features — achieving 0.82 OOD success on ALOHA cube transfer vs. 0.23 for standard ACT. However, it operates at the feature level in small architectures, uses heuristic energy-based graph search, and evaluates on a single simple task. ICIL (NeurIPS 2021) learns domain-invariant features for imitation but not at the token level. CLIP-ICM (ICML 2025) applies causal invariance to VLMs via SCMs but for classification, not action policies. **Spurious correlation mitigation via prompting**: InSpire (arXiv 2505.13888, May 2025) mitigates VLA spurious correlations by boosting spatial reasoning — prepending directional questions ('In which direction is [object] relative to the robot?') to redirect attention to task-relevant features. Achieves +6.2%/+10% on seen/unseen LIBERO tasks for miniVLA-VQ and +25%/+26% in real-world tasks for π0-FAST. Complementary approach (prompting-based attention redirection vs. CaTS's principled token selection); evaluated on standard LIBERO, not LIBERO-Plus perturbation dimensions. **Simple adaptation baselines**: FTM (arXiv 2512.02902) achieves 87.1% on LIBERO viewpoint with just 4K parameters via global affine token modulation; FLA extends to 90.8% with 4.7M parameters. Neither evaluated on full LIBERO-Plus; neither provides interpretability. **Active attention**: AVA-VLA (arXiv 2511.18960) dynamically reweights visual tokens via active attention, achieving 74.7% on LIBERO-Plus. **Causality-inspired robustness theory**: CIRRL (arXiv 2505.12868, May 2025) provides the first causality-inspired finite-radius robustness guarantee in nonlinear settings, using identifiable representation learning (Distributional Principal Autoencoders) to recover latent variables up to affine transformation, then applying anchor regression in the identifiable latent space. Key theorem: the two-step estimator achieves optimal worst-case risk among all L²-integrable functions under elliptical noise. Directly relevant to CaTS's theoretical framework — CIRRL validates the principle that representation-level causal robustness can overcome IRM/V-REx limitations, though its elliptical distribution assumptions and tabular data focus limit direct application to high-dimensional VLA visual tokens. CaTS's encoder-level scoring operates at a representation layer where spatial identifiability holds (analogous to CIRRL's affine identifiability), providing an empirical bridge between CIRRL's theory and VLA practice. **Amortized Shapley estimation for vision transformers**: ViT-Shapley (ICLR 2023 Oral, arXiv 2206.05282) trains a separate explainer model to predict per-patch Shapley values in a single forward pass, using a three-stage pipeline: (1) train ViT classifier, (2) fine-tune a surrogate with attention masking to handle partial inputs, (3) train the explainer to amortize Shapley computation. The explainer produces 196 per-patch importance scores (14×14 grid) and outperforms attention rollout, GradCAM, and LRP for ViT explanation. Publicly available code (github.com/suinleelab/vit-shapley). CaTS's amortized causal scoring head is architecturally analogous — both train a lightweight model to predict per-token importance from embeddings in a single forward pass. The critical difference: ViT-Shapley estimates observational Shapley values (how much does masking patch i change the model's prediction?) for post-hoc explanation of a fixed model on a single distribution, while CaTS estimates interventional causal effects (how much does replacing token i with environment-marginal statistics change action predictions across environments?) for cross-environment invariance during training. This distinction parallels the broader observational vs. interventional Shapley literature (Heskes et al., NeurIPS 2020): observational Shapley captures feature relevance within a distribution, while interventional Shapley captures causal influence robust to distribution shift. CaTS's intervention mechanism (environment-marginal replacement across LIBERO-Plus perturbation dimensions) is specifically designed to distinguish causal from spuriously correlated tokens — a distinction that observational Shapley cannot make when spurious correlations are present in the training distribution. ViT-Shapley's attention masking approach for evaluating ViTs with partial information is directly applicable to CaTS's intervention mechanism and informs implementation. **Mechanistic interpretability for VLA**: Mechanistic interpretability for VLA steering (CoRL 2025, arXiv 2509.00328) projects feedforward activations onto the token embedding basis to identify sparse semantic directions — such as speed and direction — that are causally linked to action selection in OpenVLA and Pi0. Enables zero-shot behavioral steering on LIBERO and real UR5 robot without fine-tuning. This validates CaTS's core premise: interventional methods can identify causally relevant structure in VLA representations. Key differentiation: operates at the neuron/direction level for behavioral steering (which directions in activation space control speed/direction?), while CaTS operates at the token level for robustness-oriented selection (which input patches contain causal vs. spurious visual information?). The two approaches are complementary — mechanistic interpretability explains how VLA representations encode action semantics, while CaTS identifies which visual tokens should feed into those representations for cross-environment robustness. **Test-time adaptation**: PDF (arXiv 2604.18107, April 2026) addresses VLA spurious correlations ('trajectory overfitting where VLAs over-attend to spurious correlation between actions and entities') via test-time perturbation learning with delayed feedback. Uses uncertainty-based data augmentation and action voting without fine-tuning, achieving +7.4% on LIBERO. Complementary to CaTS: PDF is a test-time adaptation method that corrects overconfident action predictions post-hoc, while CaTS is a training-time causal selection method that prevents spurious correlations from entering the policy. The two could be combined — CaTS for principled token selection during training, PDF for residual correction at test time. **Concurrent VLA token pruning/selection methods (2025-2026) — all using heuristic criteria**: (i) SP-VLA (arXiv 2506.12723, ICLR 2026) jointly addresses temporal and spatial redundancy via action-aware model scheduling (switching between VLA and lightweight generator for deliberative vs. intuitive actions) and spatio-semantic dual-aware token pruning. Achieves 1.5× lossless acceleration on LIBERO and 2.4× on SimplerEnv with up to 6% performance gain. As an ICLR 2026 accepted paper, it represents the strongest efficiency-focused VLA pruning method. However, its spatio-semantic scoring criterion is designed for efficiency (removing redundant tokens) rather than robustness (removing spuriously correlated tokens) — a token may be spatially/semantically important yet causally spurious (e.g., a distinctive background element near the target object). Not evaluated under distribution shift. Code available on GitHub. (ii) DTP (arXiv 2601.16065, Jan 2026) prunes 'distracting tokens' via attention intersection scoring — tokens in task-irrelevant regions exceeding a scaled threshold of the maximum attention in task-relevant regions are pruned. Evaluated on SIMPLER, not LIBERO-Plus. Directly analogous motivation to CaTS (removing spuriously correlated tokens), but uses attention heuristics without formal justification that attention-salient ≠ causally relevant. Code available. (iii) FocusVLA (arXiv 2603.28740, Mar 2026) uses cross-attention-based TopK patch selection with modality cascaded attention, achieving 98.7% on standard LIBERO. Not evaluated on LIBERO-Plus; assumes cross-attention scores identify task relevance without causal validation. (iv) LightVLA (arXiv 2509.12594, ICRA 2026) uses Gumbel softmax for differentiable token selection, reducing FLOPs by 59.1% with 2.9% success rate improvement on LIBERO. End-to-end learned selection but criterion is implicitly defined by task loss — no interpretability or formal robustness criterion. (v) TIES (arXiv 2603.24941, Mar 2026) introduces Kendall rank consistency across layers as a stability metric, improving average success by 6% on CogACT+SIMPLER while reducing tokens by 78%. Most relevant concurrent work: uses rank consistency as a robustness signal, but this is a statistical regularity heuristic, not a causal criterion — rank consistency does not distinguish causal from spuriously consistent tokens. Not evaluated under environmental perturbations. (vi) BFA++ (arXiv 2602.20566, Feb 2026) uses hierarchical intra-view and inter-view importance predictors for multi-view VLAs. (vii) Compressor-VLA (arXiv 2511.18950) uses instruction-guided semantic and spatial compression modules, reducing visual tokens by 3× on LIBERO. (viii) Gaze-Regularized VLA (arXiv 2603.23202, Mar 2026) aligns attention with human gaze heatmaps via KL divergence. Requires human gaze data; provides indirect causal signal. (ix) LearnPruner (arXiv 2604.23950, Apr 2026) trains a learnable pruning module after the vision encoder, retaining only 5.5% of tokens while preserving ~95% performance. (x) SpecPrune-VLA (arXiv 2509.05614) uses action-aware self-speculative pruning with global history context, combining static action-level and dynamic layer-level pruning with an action-aware controller that classifies actions as coarse/fine-grained. Achieves 1.57× speedup on LIBERO and 1.70× in real-world with negligible degradation. Primarily efficiency-focused, exploiting temporal redundancy. (xi) VLA-Cache (arXiv 2502.02175, NeurIPS 2025) adaptively caches and reuses static visual tokens across consecutive frames via layer-adaptive token reusing, achieving 1.7× speedup with negligible success rate loss. Exploits temporal redundancy between adjacent observations — complementary to CaTS which addresses spatial token selection within a single frame for robustness rather than efficiency. **Token information dynamics**: arXiv 2512.07580 (ICLR 2026) discovers 'vanishing token information' — visual tokens progressively lose discriminative salience in deep LLM layers, becoming uniformly uninformative beyond an 'information horizon' (~layer 20 for general tasks, deeper for OCR). This explains why attention-based pruning in late layers underperforms random selection and motivates scoring at early/intermediate layers where spatial information is preserved. **Token pruning critique**: arXiv 2502.11501 (ACL Findings 2025) systematically shows many attention-based pruning methods underperform random selection due to position bias and flawed attention-as-importance assumptions. **Causal token pruning in NLP**: LeaF (NeurIPS 2025, arXiv 2506.07851) uses gradient-based teacher-student comparison to identify confounding tokens. Analogous in spirit but targets LLM reasoning, not embodied action; uses gradient heuristics, not formal interventions. **Robustness training**: RobustVLA (ICLR 2026, arXiv 2510.00037) uses offline robust optimization with 12.6% absolute gains on π0 backbone. **World models**: Mask World Model (arXiv 2604.19683) achieves 98.3% on standard LIBERO via geometric information bottleneck but not evaluated on LIBERO-Plus. **Shortcut learning**: arXiv 2508.06426 (CoRL 2025) identifies dataset diversity as root cause — complementary data-side approach. **Invariance theory limitations**: Rosenfeld et al. (ICLR 2021) demonstrate IRM fails in non-linear settings. V-REx (Krueger et al., ICML 2021) proposes variance-based risk extrapolation as simpler alternative but suffers similar non-linear limitations. CIRRL (arXiv 2505.12868) overcomes these limitations via identifiable representation learning but requires elliptical distribution assumptions. Wasserstein DRO (Kuhn et al., 2024) provides genuine finite-sample guarantees without requiring linear/invariance assumptions. **Amortized causal estimation**: CausalPFN (NeurIPS 2025) demonstrates amortized causal effect estimation via in-context learning with asymptotic consistency guarantees; ACTIVA (arXiv 2503.01290) uses transformer-based VAEs but is limited to tabular data. Amortized Shapley estimation (SurroShap, SimSHAP) provides non-asymptotic convergence bounds: Pr(|ϕ̂ − ϕ| ≥ ε) ≤ 2·exp(−2mε²/r²) for m samples and marginal contribution range r (Maleki et al., 2013). **No existing work combines formal token-level causal intervention criteria with amortized estimation in VLA transformers, operating at the vision encoder output where spatial locality is empirically validated, for cross-environment policy invariance.**\",\n  \"approach\": \"We propose Causal Token Selection (CaTS) v3, which identifies and retains visual tokens whose causal effect on action predictions is significant and stable across visual environments, using an amortized interventional scoring framework operating at the vision encoder output where spatial locality is empirically grounded.\\n\\n**Formal SCM for VLA Token-Action Pipeline.** We define a structural causal model: observation O is processed by the vision encoder into T(O) = {t_1,...,t_N} (N=256 for OpenVLA's SigLIP+DINOv2 encoder); each token t_i corresponds to an image patch and carries causal content C_i (object geometry, gripper state, contact regions) and spurious content S_i (background texture, lighting, distractor appearance); environment variable E influences S_i but not C_i; action A = π(f(T)) where f is the LLM backbone. We formalize the *encoder-level spatial locality* assumption (revised from the original spatial locality assumption): at the vision encoder output — before LLM self-attention layers mix token representations — causal content C_i is concentrated in a subset T* ⊂ T corresponding to image patches containing task-relevant objects, while spurious content S_i is distributed across patches containing background and distractors. **Justification**: this is grounded in two empirical findings: (a) DINOv2's attention maps show foreground object concentration by layers 3-6, with the CLS token primarily aggregating foreground tokens (arXiv 2602.22394); (b) the 'vanishing token information' phenomenon (arXiv 2512.07580) confirms that spatial discriminability is maximal at the vision encoder output and degrades through LLM depth. **Important caveat**: arXiv 2512.07580 evaluates VLMs (Qwen2.5-VL, LLaVA-1.5), not VLAs. While VLAs share the VLM backbone architecture making extrapolation reasonable, VLA models have different training objectives (action prediction vs. text generation) and potentially different attention patterns — action tokens may attend to visual tokens differently than text tokens. The information horizon position may differ for VLAs. Verifying the information horizon in VLA architectures is an explicit part of our empirical contribution (ablation b: encoder-level vs. intermediate-layer vs. late-layer scoring directly tests where spatial information degrades in VLA models). By scoring at the encoder output, CaTS operates precisely where the assumption is most valid, unlike methods scoring at deep LLM layers where information mixing undermines spatial selectivity. This encoder-level identifiability is analogous to CIRRL's (arXiv 2505.12868) key insight that robustness guarantees extend to nonlinear settings when operating on identifiable representations — the vision encoder's spatial correspondence provides patch-level identifiability that enables causal reasoning at the token level.\\n\\n**Multi-Layer Scoring Architecture.** Rather than scoring tokens at a single layer (where the spatial locality / information quality tradeoff is unclear), CaTS employs a two-stage scoring approach: (1) *Primary scoring* at the vision encoder output (post-MLP projection, pre-LLM), where spatial locality is strongest. (2) *Optional refinement scoring* at an intermediate LLM layer (before the information horizon, empirically determined per-model via the protocol of arXiv 2512.07580 — typically layer 8-15 for 7B models), capturing cross-modal relevance signals that emerge only after some language-vision interaction. The two scores are combined via a learned convex combination α·s_encoder + (1-α)·s_intermediate, where α is a learnable scalar. **Degradation analysis**: we formally analyze how the ε-invariance bound degrades as spatial locality weakens (parameterized by α_leak = fraction of causal information C_i that 'leaks' to non-corresponding tokens through self-attention). When α_leak is high (poor spatial locality at the scoring layer), the bound degrades gracefully — the theory predicts diminishing returns of causal selection over random pruning, which is empirically testable.\\n\\n**Theorem (Conditional Invariance) with Approximate Constants.** Under four assumptions — (A1) causal sufficiency: A ⊥ E | C(T*); (A2) token-level identifiability: do(t_i) changes C(T*) with positive probability for t_i ∈ T*; (A3) environment diversity: training environments span relevant E dimensions; (A4) bounded amortization error of the causal scorer — the causal token selection operator S_τ with threshold τ satisfies:\\n\\n*Concrete bound*: max_{e,e'} |R(π,e) - R(π,e')| ≤ ε(N_env, M, τ, α_leak) where:\\nε = C₁/√M + C₂·exp(-c·N_env/d_E) + C₃·α_leak·g(τ) + ε_amort\\n\\n**Approximate constant estimates (order-of-magnitude):**\\n\\n- *C₁/√M (Shapley estimation error)*: Using the Hoeffding-based bound from Maleki et al. (2013): Pr(|ϕ̂ − ϕ| ≥ ε) ≤ 2·exp(−2Mε²/r²), where r is the range of marginal contributions. With action loss normalized to [0,1] (r=1) and confidence δ=0.05: C₁ = r·√(ln(2/δ)/2) ≈ 1.36. With M=200 Shapley samples per token: C₁/√M ≈ 0.096. With M=500: ≈ 0.061. **Practical implication**: M=200 samples (200 forward passes per scored token, feasible with batch inference) yields estimation error below 0.1, sufficient for reliable token ranking.\\n\\n- *C₂·exp(-c·N_env/d_E) (environment coverage gap)*: d_E ≈ 7 for LIBERO-Plus's 7 perturbation dimensions (camera, robot, language, light, background, noise, layout). With N_env = 35 distinct environments (7 dimensions × 5 perturbation levels each) and c ≈ 0.5-1.0 (standard covering-number scaling for bounded domains): exp(-c·35/7) = exp(-2.5 to -5.0) ≈ 0.007-0.082. With C₂ ≈ 1 (bounded loss): this term contributes ≈ 0.01-0.08. **Practical implication**: 35 environments across 7 dimensions make this term small; the bound suggests N_env = Ω(d_E · log(1/δ)) ≈ 21 environments suffice for δ=0.05, which LIBERO-Plus comfortably exceeds.\\n\\n- *C₃·α_leak·g(τ) (spatial locality violation)*: α_leak is empirically measurable — at the vision encoder output, we estimate α_leak ≈ 0.05-0.15 (based on DINOv2's foreground concentration in layers 3-6, arXiv 2602.22394); at intermediate LLM layer ~10, α_leak ≈ 0.3-0.5; beyond the information horizon (layer 20+), α_leak → 1.0. With g(τ) ≈ (1-τ)/τ for pruning ratio τ and C₃ ≈ 1: at encoder output with τ=0.5 (50% pruning), C₃·α_leak·g(τ) ≈ 0.1·1.0 = 0.10. At layer 20+ with α_leak ≈ 1.0: this term ≈ 1.0, dominating the bound and explaining why late-layer pruning degenerates to random selection.\\n\\n- *ε_amort (amortization gap)*: ε_amort ≤ ε_approx(W,d) + ε_stat(n_train). For a 2-layer MLP scorer with W=512 hidden units on d=1024-dimensional token embeddings: ε_approx = O(1/√W) ≈ 0.044 (for Barron-class functions); ε_stat = O(1/√n_train) ≈ 0.01 for n_train=10,000 training interventions. Total ε_amort ≈ 0.054.\\n\\n**Overall bound estimate**: At the vision encoder output with M=200, N_env=35, α_leak=0.1, τ=0.5: ε ≈ 0.096 + 0.01 + 0.10 + 0.054 ≈ 0.26. This predicts a maximum cross-environment performance gap of ~26% — a testable prediction against the empirically observed ~50-65% gap for unmodified VLAs on LIBERO-Plus. The bound tightens substantially with M=500 (ε ≈ 0.22) and with higher pruning threshold τ=0.7 (ε ≈ 0.20).\\n\\n**Full proof strategy**: The proof proceeds in three steps: (1) show that under A1-A2, exact token-level ACE identifies T* (follows from standard do-calculus); (2) bound the approximation error when ACE is estimated from M samples via Shapley decomposition (using Hoeffding-type concentration on bounded action losses, directly applying the non-asymptotic bound from Maleki et al., 2013); (3) bound the error from amortizing the Shapley estimates via a neural network (using universal approximation for Barron-class functions + Rademacher complexity of the MLP hypothesis class). Step (3) yields the ε_amort term.\\n\\n**Failure modes (explicit with analysis):** (F1) Insufficient environment diversity violates A3 — same limitation as IRM/V-REx, partially addressed by CIRRL's identifiable representation approach but CIRRL requires elliptical distribution assumptions that may not hold for VLA visual tokens. Mitigation: LIBERO-Plus provides 7 perturbation dimensions with ~35 environments; we report per-dimension results to identify which dimensions have sufficient diversity. (F2) Spatial locality violation at scoring layer (high α_leak). Mitigation: multi-layer scoring allows operating at the layer with lowest α_leak; we empirically measure α_leak by comparing per-token ACE computed at encoder output vs. intermediate LLM layers. (F3) Amortization gap (see detailed analysis below). (F4) V-REx variance penalty limitations in non-linear settings — see honest framing below.\\n\\n**Amortized Causal Scoring (ACS) with Quantified Amortization Gap.** We train a lightweight causal scoring head attached to the frozen VLA backbone. Training data is generated via *batch stochastic interventions*: for randomly sampled token subsets across LIBERO-Plus perturbation environments, we replace token embeddings with environment-marginal statistics and measure KL divergence in action distributions. A Shapley-value-inspired decomposition attributes group effects to individual tokens. The scorer (2-layer MLP with width 512, <1M parameters) learns to predict token-level causal effects from token embeddings.\\n\\n**Relationship to ViT-Shapley (ICLR 2023)**: CaTS's amortized scoring architecture draws on the ViT-Shapley paradigm of training a separate model to predict per-token importance in a single forward pass. However, CaTS departs in three key ways: (a) the scoring target is interventional causal effects computed via environment-marginal token replacement across LIBERO-Plus perturbation dimensions, not observational Shapley values computed via masking on a single distribution; (b) the surrogate stage uses multi-environment intervention data rather than random masking, training the scorer to predict action distribution stability across environments rather than prediction change under masking; (c) the scorer is integrated into a training-time robustness objective (composite V-REx + DRO loss), not used for post-hoc explanation. ViT-Shapley's attention masking approach for evaluating ViTs with partial information informs our intervention mechanism — we adapt their masking strategy to implement environment-marginal token replacement, replacing masked tokens with marginal statistics pooled across perturbation environments rather than zeroing them out.\\n\\n**Amortization gap analysis**: The gap between the learned scorer s_θ(t_i) and the true ACE(t_i) is bounded by: ε_amort ≤ ε_approx(W, d) + ε_stat(n_train) where ε_approx(W, d) = O(1/√W) ≈ 0.044 for W=512 (for Barron-class functions on compact domains), and ε_stat(n_train) = O(1/√n_train) ≈ 0.01 for n_train=10,000 training interventions. **Central validation protocol** (not merely an ablation): we compute exact ACE on a validation set of 50 tokens × 5 environments (250 forward passes per token = 12,500 total, feasible) and report: (a) Pearson/Spearman correlation between s_θ and exact ACE; (b) mean absolute error; (c) rank agreement (does s_θ rank tokens in the same order as exact ACE?). The amortized scorer is considered validated if rank-order Spearman ρ > 0.8 and the scoring threshold τ selects a token set overlapping ≥ 85% with the exact-ACE-selected set. If validation fails, we fall back to exact ACE computation at inference (trading efficiency for correctness), which remains a viable contribution.\\n\\n**Composite Robustness Objective (honest framing with V-REx/DRO interaction analysis).** We do NOT claim to solve the non-linear invariance problem. Instead, we use a *composite robustness objective* combining three components: (1) Standard action prediction loss on selected tokens: L_task = E_e[L(π(S_τ(T)), a*)]. (2) V-REx-style variance penalty: L_var = Var_e(L(π(S_τ(T)), a*)), which penalizes cross-environment loss variance. We frame this honestly as a *practical heuristic* that is simpler and more stable than IRMv1 (Krueger et al., ICML 2021) but shares the same fundamental limitation in non-linear settings: it does not distinguish between underfitting and inherent noise, and can fail under heteroskedastic environments. (3) Wasserstein DRO regularization: L_DRO = sup_{Q: W(Q,P̂)≤ρ} E_Q[L], providing finite-sample robustness guarantees (Kuhn et al., 2024) that do not require linear assumptions.\\n\\n**V-REx and DRO interaction analysis.** The two regularizers target complementary failure modes but can interact non-trivially. *When complementary*: V-REx stabilizes performance across *known* training environments by penalizing loss variance — preventing environment-specific overfitting where the model excels in one environment but fails in others. DRO provides robustness to *unseen* environments within the Wasserstein ball — guarding against distributional shift at test time. Together, they create a 'robust-within-uniform' objective: the policy must perform uniformly across training environments (V-REx) while being robust to perturbations of each environment's distribution (DRO). *When potentially conflicting*: DRO with large radius ρ may concentrate model capacity on worst-case distributions, potentially increasing cross-environment variance to better handle the hardest cases — precisely what V-REx penalizes. *Resolution*: for small-to-moderate DRO radius ρ, Wasserstein DRO is equivalent to variation regularization (Kuhn et al., 2024), making the two objectives approximately aligned. In practice, we operate with moderate ρ where the Wasserstein ball captures realistic perturbations (calibrated to LIBERO-Plus perturbation magnitudes) rather than adversarial worst cases. The sensitivity analysis (ablation c) explicitly measures the V-REx/DRO tradeoff by sweeping λ_var and λ_DRO independently and jointly, reporting both average performance and cross-environment variance to identify the Pareto frontier. We note that CIRRL (arXiv 2505.12868) offers a principled alternative — identifiable representation learning followed by anchor regression — that avoids the V-REx/DRO tension entirely, but requires elliptical distribution assumptions that we cannot verify for VLA visual tokens; adapting CIRRL's framework to VLA architectures is an important direction for future work.\\n\\nThe combined loss is L = L_task + λ_var·L_var + λ_DRO·L_DRO, where λ_var and λ_DRO are hyperparameters with explicit sensitivity analysis. We expect V-REx to provide better empirical performance in practice (as observed in prior work) while DRO provides the theoretical safety net.\\n\\n**Architecture.** Frozen OpenVLA-OFT backbone (7B). The ACS head operates at the vision encoder output (post-projection), with optional refinement at an intermediate LLM layer. Total trainable parameters: ACS scoring head (~0.5M) + thin LoRA adaptation (~3.5M) = ~4M total. At inference, the scorer assigns causal scores to all visual tokens in a single forward pass; tokens below threshold τ are pruned before entering the LLM backbone, providing both robustness and efficiency.\\n\\n**Evaluation with Formal Statistical Protocol.** Primary benchmark: LIBERO-Plus across all 7 perturbation dimensions. Primary metric: average success rate under distribution shift.\\n\\n**Statistical protocol against random pruning** (addressing arXiv 2502.11501's findings): We adopt a paired bootstrap protocol with bias-corrected accelerated (BCa) confidence intervals and sign-flip permutation tests (following arXiv 2511.19794). Specifically: (a) train CaTS and random-pruning variants under identical conditions with 5 random seeds; (b) record per-seed, per-task success rate differences; (c) compute BCa 95% confidence intervals on the mean difference; (d) perform sign-flip permutation test (10,000 permutations) for each perturbation dimension. CaTS claims significant improvement only if the BCa interval lies entirely above zero AND the permutation p-value < 0.05. *A priori success criterion*: CaTS must significantly outperform random pruning on at least 5 of 7 perturbation dimensions. If this criterion is not met, we report the negative result transparently and analyze which perturbation types resist causal selection (contributing understanding of when causal criteria matter vs. when random suffices).\\n\\n**Baselines (8 core, with code availability assessment).** We streamline from 11 to 8 core baselines, prioritizing those with available code or reproducible implementations on LIBERO-Plus, and dropping baselines requiring non-trivial cross-architecture adaptation:\\n\\n(1) SRPO (arXiv 2511.15605) — current LIBERO-Plus SOTA (82.1%). Evaluated in original LIBERO-Plus paper; results directly comparable. (2) FTM/FLA (arXiv 2512.02902) — simple adaptation baseline. Reproduced on LIBERO-Plus; FTM requires only 4K trainable parameters, making reproduction straightforward even without official code (single affine transform layer). (3) AVA-VLA (arXiv 2511.18960) — active visual attention, 74.7% on LIBERO-Plus. Already evaluated on LIBERO-Plus in original work. (4) RobustVLA (ICLR 2026, arXiv 2510.00037) — offline robust optimization, directly targets VLA robustness. ICLR 2026 accepted, code expected. (5) DTP (arXiv 2601.16065) — most directly analogous concurrent work (attention-based distractor identification). Code available at anonymous repository. Requires adaptation to LIBERO-Plus (originally evaluated on SIMPLER). (6) TIES (arXiv 2603.24941) — most sophisticated heuristic baseline (inter-layer rank consistency). Code availability: pending. Method is training-free and well-specified, making reimplementation feasible. (7) VLA-Pruner (arXiv 2511.16449) — temporal-aware dual-level pruning. Code available on GitHub (MINT-SJTU/VLA-Pruner). (8) Random token pruning — critical control baseline, trivial to implement.\\n\\n**Baselines discussed but not reproduced (with justification)**: Causal-ACT (feature-level ResNet+ACT architecture → token-level OpenVLA adaptation requires non-trivial architectural changes beyond a fair comparison). LeaF-adapted (NLP reasoning → VLA action policies requires speculative adaptation with unclear design choices). FocusVLA, LightVLA, BFA++, Compressor-VLA (not evaluated on LIBERO-Plus; codebases target different VLA architectures). SP-VLA, SpecPrune-VLA, VLA-Cache (efficiency-focused methods exploiting temporal redundancy; not evaluated under distribution shift; complementary rather than competing with CaTS's robustness objective). InSpire (prompting-based approach, orthogonal mechanism targeting same problem; could be combined with CaTS in future work). These are all discussed in the landscape section with explicit differentiation.\\n\\n**Ablations**: (a) amortized vs. exact ACE (central validation, not just ablation); (b) encoder-level vs. intermediate-layer vs. late-layer scoring (testing spatial locality assumption directly); (c) V-REx only vs. DRO only vs. composite objective (including joint λ_var × λ_DRO sensitivity sweep to characterize the interaction frontier and identify the complementary vs. conflicting regime); (d) variance penalty weight sensitivity; (e) DRO radius ρ sensitivity (calibrated against LIBERO-Plus perturbation magnitudes); (f) pruning ratio sweep (10-90%); (g) per-perturbation-dimension analysis; (h) causal score interpretability analysis (do high-scoring tokens correspond to task-relevant regions via IoU with ground-truth object masks?); (i) α_leak measurement across layers.\\n\\n**Key differentiations from all concurrent work.** The central claim is not merely that causal criteria exist, but that they provide *measurably better token selection than heuristic alternatives* — the burden of proof is on CaTS, and the evaluation is designed to test this rigorously.\\n\\nvs. SP-VLA (ICLR 2026): SP-VLA jointly optimizes temporal scheduling and spatial token pruning for efficiency — its spatio-semantic criterion identifies tokens that are spatially/semantically redundant but not necessarily causally spurious. A background token near the target object may have high spatio-semantic importance (spatially close, semantically related to the scene) yet be causally irrelevant to the action. CaTS's interventional criterion tests causal relevance directly via environment-marginal replacement. The two approaches are potentially complementary: SP-VLA for temporal efficiency, CaTS for causal robustness within each selected frame.\\n\\nvs. DTP (arXiv 2601.16065): DTP uses attention intersection heuristics (tokens in irrelevant regions with attention exceeding scaled threshold are pruned). CaTS uses formal causal intervention criteria. DTP's attention-based scoring is exactly the type shown to be unreliable by arXiv 2502.11501; CaTS's causal scoring is designed to be the principled alternative. Empirical comparison on LIBERO-Plus will directly test whether causal grounding outperforms attention-based distractor identification.\\n\\nvs. FocusVLA (arXiv 2603.28740): FocusVLA uses cross-attention TopK selection + modality cascaded attention, achieving strong results on standard LIBERO (98.7%) but without robustness evaluation. CaTS targets robustness under distribution shift specifically. FocusVLA's TopK is a differentiable selection mechanism but provides no criterion for *which* tokens matter for cross-environment generalization.\\n\\nvs. LightVLA (arXiv 2509.12594): LightVLA learns token selection end-to-end via Gumbel softmax — the selection criterion is implicitly defined by the training loss and may overfit to spurious correlations in training environments. CaTS's explicit causal criterion is designed to prevent exactly this overfitting.\\n\\nvs. TIES (arXiv 2603.24941): TIES uses inter-layer rank consistency (Kendall τ) as a stability signal — an innovative heuristic that captures token 'reliability' across layers. However, rank consistency does not distinguish between causally relevant tokens and tokens that are consistently spurious (e.g., a distinctive background element present in all training scenes would have high rank consistency but is causally irrelevant). CaTS's interventional scoring directly tests causal relevance via environment-marginal replacement.\\n\\nvs. InSpire (arXiv 2505.13888): InSpire redirects VLA attention via language prompting (spatial reasoning questions), achieving an indirect form of spurious correlation mitigation without token-level selection. CaTS operates at the token level with formal causal criteria. The two approaches are complementary — InSpire provides a zero-cost attention redirect while CaTS provides principled token selection with theoretical guarantees. Future work could combine InSpire's spatial prompting with CaTS's causal scoring.\\n\\nvs. CIRRL (arXiv 2505.12868): CIRRL provides finite-radius nonlinear robustness via identifiable representation learning, but operates on tabular data with elliptical distribution assumptions. CaTS draws theoretical inspiration from CIRRL's key insight (representation-level identifiability enables causal robustness) while adapting to the VLA setting where visual encoder outputs provide spatial patch-level identifiability. CaTS's DRO component provides analogous finite-sample guarantees without requiring elliptical assumptions.\\n\\nvs. Gaze-VLA (arXiv 2603.23202): Uses human gaze as an indirect causal signal (humans look at task-relevant regions). Requires gaze data collection; gaze provides a noisy proxy for causal relevance (humans also look at salient distractors). CaTS derives causal relevance from the model's own action predictions under intervention.\\n\\nvs. Causal-ACT (arXiv 2507.22380): Token-level in 7B VLA (not feature-level in ResNet+ACT); amortized scoring (not heuristic graph search); comprehensive LIBERO-Plus evaluation; concrete ε-invariance bound with approximate constants.\\n\\nvs. FTM: Interpretable per-token causal scores (not black-box affine transform); selective token removal (not global recalibration); formal robustness criterion.\\n\\nvs. LeaF (NeurIPS 2025): VLA action policies (not NLP reasoning); cross-environment interventional scoring (not single-domain gradient heuristics); formal SCM (not teacher-student comparison).\\n\\nvs. ViT-Shapley (ICLR 2023): CaTS's amortized scorer is architecturally analogous to ViT-Shapley's learned explainer — both predict per-token importance from embeddings in one forward pass. The fundamental difference is the scoring target: ViT-Shapley estimates observational Shapley values for explaining a model's predictions within a single distribution; CaTS estimates interventional causal effects across environments to identify tokens whose influence on actions is invariant to visual distribution shifts. Observational Shapley values cannot distinguish causal from spuriously correlated tokens when both correlate with the outcome in the training distribution. CaTS's environment-marginal replacement directly probes cross-environment invariance, providing the causal grounding that ViT-Shapley's masking-based approach lacks.\\n\\nvs. Mechanistic Interpretability for VLA Steering (CoRL 2025): Both use interventional methods on VLA representations. The steering work identifies neuron-level semantic directions (speed, direction) for zero-shot behavioral control; CaTS identifies token-level causal importance for robustness under visual distribution shift. Complementary: steering explains internal action semantics, CaTS determines which visual inputs matter.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~800h A100 (80GB): ~350h for 22-28 LoRA fine-tuning runs with ACS head at ~14h each (including multi-layer scoring variants and composite objective hyperparameter search), ~250h for batch intervention data generation, amortized scorer training, and exact ACE validation (12,500 forward passes for validation set + systematic coverage across 7 perturbation types), ~200h for baseline reproduction (DTP and TIES reproduction on LIBERO-Plus, FTM on LIBERO-Plus, 8 baselines total with 5 seeds each for statistical protocol) and ablations\",\n      \"gpu_utilization\": \"Low (~25-30%). GPUs sit idle during code development, causal scoring pipeline debugging, statistical protocol implementation, α_leak measurement analysis, and theorem proof development.\",\n      \"timeline\": \"4-6 months\",\n      \"team\": \"1-2 researchers (one with causal inference/DRO background for theorem formalization and proof, one with VLA/robotics experience for implementation and evaluation)\",\n      \"estimated_gpu_cost\": \"~$640 (800h × $0.80/hr A100 spot/discount pricing from specialized providers such as Thunder Compute or TensorDock, May 2026 market rate; range $0.78-$1.07/hr across providers)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~1200h A100 (80GB): agent explores ~40-50 training configurations more systematically, runs comprehensive ablations across all 7 perturbation dimensions with 5 seeds, evaluates all 8 baselines, and performs extensive α_leak measurements across layers\",\n      \"gpu_utilization\": \"Moderate (~50-60%). Agent queues experiments faster but pauses at approval gates for: multi-layer scoring architecture decisions, DRO radius selection, amortization validation thresholds, theorem assumption checking.\",\n      \"timeline\": \"2-4 months\",\n      \"team\": \"1 researcher, ~45min/day check-in for approving experiment plans, reviewing causal score visualizations, validating amortization gap measurements, and verifying theorem proof steps\",\n      \"claude_api_cost\": \"$500-700 (5000-7000 conversation turns for experiment design, code generation, theorem checking, statistical protocol implementation, result analysis)\",\n      \"estimated_gpu_cost\": \"~$960 (1200h × $0.80/hr)\",\n      \"risk_note\": \"Amortized scorer validation (Spearman ρ > 0.8 threshold) requires careful human judgment — if the scorer barely misses the threshold, the decision to proceed with amortized vs. exact scoring has significant downstream implications. DRO radius selection and the V-REx/DRO tradeoff require human expertise. Theorem proof needs verification by someone with expertise in both causal inference and approximation theory.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~2500h A100 (80GB): agent runs 120-150 experiment configurations including aggressive sweeps for scoring layer selection, V-REx/DRO weight ratios, pruning ratios, Shapley approximation methods, scorer architectures (varying width W), plus all baseline reproductions with 5 seeds and failed exploration runs\",\n      \"gpu_utilization\": \"High (~90%+). Agent queues next experiment immediately upon completion. Continuous 24/7 execution.\",\n      \"timeline\": \"3-5 weeks with 4-8 concurrent A100s; as few as 8-10 days with 16 concurrent GPUs\",\n      \"team\": \"0 (initial setup: configure LIBERO-Plus environments, OpenVLA-OFT checkpoint, define intervention distribution, implement statistical testing protocol, implement α_leak measurement)\",\n      \"claude_api_cost\": \"$700-1100 (7000-11000 turns for autonomous experiment design, debugging, statistical analysis, and paper drafting)\",\n      \"estimated_gpu_cost\": \"~$2,000 (2500h × $0.80/hr)\",\n      \"speed_bottleneck\": \"Number of concurrent A100 GPU instances. Secondary: intervention data generation is I/O-intensive (requires rendering perturbation environments). Statistical protocol with 5 seeds × 8 baselines × 7 perturbation dimensions requires organized experiment management.\",\n      \"risk_note\": \"Without human gates, agent may over-explore suboptimal scoring layer combinations or DRO radius values. The theorem formalization cannot be fully automated — agent-generated proofs require expert verification, especially the amortization gap bound (step 3 of the proof involving Rademacher complexity). The statistical protocol is automatable but interpretation of borderline results (e.g., CaTS significant on 4/7 dimensions vs. the a priori 5/7 criterion) requires human judgment. Risk mitigation: pre-define structured search space with early stopping on amortization validation metrics; halt if Spearman ρ < 0.6 after initial scorer training.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (deadline: ~August 1, 2026 — primary target, sufficient time for theoretical development, multi-layer scoring implementation, and statistical evaluation)\",\n    \"ICLR 2027 (deadline: ~October 2026 — strong target, allows comprehensive evaluation and concurrent work comparison)\",\n    \"ICRA 2027 (deadline: ~September 2026 — robotics venue, good fit for empirical contribution)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations [Causal-ACT] (arXiv 2507.22380, July 2025)\",\n    \"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling [FTM/FLA] (arXiv 2512.02902, Dec 2025)\",\n    \"Learning to Focus: Causal Attention Distillation via Gradient-Guided Token Pruning [LeaF] (NeurIPS 2025, arXiv 2506.07851)\",\n    \"Shortcut Learning in Generalist Robot Policies: The Role of Dataset Diversity and Fragmentation (CoRL 2025, arXiv 2508.06426)\",\n    \"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem? (ACL Findings 2025, arXiv 2502.11501)\",\n    \"When Token Pruning is Worse than Random: Understanding Visual Token Information in VLLMs (ICLR 2026, arXiv 2512.07580)\",\n    \"The Risks of Invariant Risk Minimization (ICLR 2021, arXiv 2010.05761)\",\n    \"Out-of-Distribution Generalization via Risk Extrapolation [V-REx] (ICML 2021, arXiv 2003.00688)\",\n    \"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models (arXiv 2511.15605)\",\n    \"AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention (arXiv 2511.18960)\",\n    \"ACTIVA: Amortized Causal Effect Estimation via Transformer-based Variational Autoencoder (arXiv 2503.01290)\",\n    \"CausalPFN: Amortized Causal Effect Estimation via In-Context Learning (NeurIPS 2025, arXiv 2506.07918)\",\n    \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026, arXiv 2510.13626)\",\n    \"Invariant Causal Imitation Learning for Generalizable Policies [ICIL] (NeurIPS 2021)\",\n    \"DTP: A Simple yet Effective Distracting Token Pruning Framework for VLA Models (arXiv 2601.16065, Jan 2026)\",\n    \"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models (arXiv 2603.28740, Mar 2026)\",\n    \"LightVLA: Towards Efficient VLA Models via Differentiable Token Pruning (ICRA 2026, arXiv 2509.12594)\",\n    \"TIES: Beyond Attention Magnitude — Leveraging Inter-layer Rank Consistency for Efficient VLA Models (arXiv 2603.24941, Mar 2026)\",\n    \"BFA++: Hierarchical Best-Feature-Aware Token Pruning for Multi-View VLA Models (arXiv 2602.20566, Feb 2026)\",\n    \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation (arXiv 2511.18950)\",\n    \"Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation (arXiv 2603.23202, Mar 2026)\",\n    \"LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models (arXiv 2604.23950, Apr 2026)\",\n    \"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations [RobustVLA] (ICLR 2026, arXiv 2510.00037)\",\n    \"Mask World Model: Predicting What Matters for Robust Robot Policy Learning (arXiv 2604.19683, April 2026)\",\n    \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient VLA Inference (arXiv 2511.16449)\",\n    \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for VLA Models (arXiv 2603.22991, March 2026)\",\n    \"Learning Invariant Causal Mechanism from Vision-Language Models [CLIP-ICM] (ICML 2025, arXiv 2405.15289)\",\n    \"OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport (arXiv 2602.20205)\",\n    \"Wasserstein Distributionally Robust Optimization and Variation Regularization (Operations Research, 2024)\",\n    \"Finite-Sample Guarantees for Wasserstein DRO: Breaking the Curse of Dimensionality (Operations Research, 2023)\",\n    \"Vision Transformers Need More Than Registers (arXiv 2602.22394, Feb 2026)\",\n    \"Bounding the Estimation Error of Sampling-based Shapley Value Approximation (arXiv 1306.4265)\",\n    \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success [OpenVLA-OFT] (arXiv 2025)\",\n    \"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration (ICLR 2026, arXiv 2506.12723)\",\n    \"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning (arXiv 2509.05614)\",\n    \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching (NeurIPS 2025, arXiv 2502.02175)\",\n    \"InSpire: Vision-Language-Action Models with Intrinsic Spatial Reasoning (arXiv 2505.13888, May 2025)\",\n    \"Causality-Inspired Robustness for Nonlinear Models via Representation Learning [CIRRL] (arXiv 2505.12868, May 2025)\",\n    \"Learning to Estimate Shapley Values with Vision Transformers [ViT-Shapley] (ICLR 2023 Oral, arXiv 2206.05282)\",\n    \"Mechanistic Interpretability for Steering Vision-Language-Action Models (CoRL 2025, arXiv 2509.00328)\",\n    \"Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models [PDF] (arXiv 2604.18107, April 2026)\",\n    \"Causal Shapley Values: Exploiting Causal Knowledge to Explain Individual Predictions of Complex Models (NeurIPS 2020, arXiv 2011.01625)\"\n  ],\n  \"description\": \"VLA models suffer catastrophic failures under visual distribution shifts, yet a proliferation of concurrent token pruning methods (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, Compressor-VLA, Gaze-VLA — all 2025-2026) each propose different heuristic criteria without formal justification, and recent work shows many attention-based methods underperform random selection (arXiv 2502.11501) due to 'vanishing token information' in deep layers (arXiv 2512.07580). We propose Causal Token Selection (CaTS) v3, bridging three disconnected threads: VLA token pruning, causal intervention for imitation learning (Causal-ACT, ICIL), and causal attention distillation (LeaF), while drawing theoretical inspiration from CIRRL's (arXiv 2505.12868) breakthrough showing that representation-level identifiability enables nonlinear causal robustness guarantees. CaTS defines a formal SCM over the VLA token-action pipeline with a revised *encoder-level spatial locality* assumption — grounded in empirical findings that DINOv2/SigLIP encoder outputs preserve spatial correspondence (a form of patch-level identifiability analogous to CIRRL's affine identifiability) while LLM self-attention progressively mixes token information. Key advances over v2: (1) Multi-layer scoring at vision encoder output (where spatial locality is empirically validated) with optional intermediate-layer refinement. (2) Concrete ε-invariance bound with approximate constants: ε = C₁/√M + C₂·exp(-c·N_env/d_E) + C₃·α_leak·g(τ) + ε_amort, with order-of-magnitude estimates (M=200 Shapley samples → estimation error ~0.096; N_env=35 across d_E=7 dimensions → coverage term ~0.01; encoder-level α_leak≈0.1 → locality term ~0.10; overall ε≈0.26, a testable prediction against the observed ~50-65% gap for unmodified VLAs). (3) Honest composite robustness objective combining V-REx (practical heuristic) with Wasserstein DRO (finite-sample guarantees), including explicit analysis of their interaction: complementary for moderate DRO radius ρ (V-REx stabilizes known environments, DRO guards against unseen shifts; for small ρ, Wasserstein DRO approximates variation regularization, aligning with V-REx), with potential conflict at large ρ resolved by operating in the moderate-ρ regime calibrated to LIBERO-Plus perturbation magnitudes. (4) Quantified amortization gap: ε_amort ≤ O(1/√W) + O(1/√n_train) ≈ 0.054 for W=512, n_train=10K, with central validation protocol (Spearman ρ > 0.8). (5) Explicit differentiation from ViT-Shapley (ICLR 2023 Oral) — CaTS's amortized scorer extends the ViT-Shapley paradigm from observational Shapley values for model explanation to interventional causal effects for cross-environment invariance. (6) Acknowledgment that the 'vanishing token information' finding (arXiv 2512.07580) was validated on VLMs, not VLAs — verifying the information horizon in VLA architectures is part of the empirical contribution. (7) Integration with mechanistic interpretability evidence (CoRL 2025) validating that interventional methods identify causal structure in VLA representations, and positioning against test-time adaptation approaches (PDF, arXiv 2604.18107) as complementary training-time vs. test-time methods for the same spurious correlation problem. Formal statistical protocol against random pruning with a priori 5/7 dimension criterion. Evaluated against 8 core baselines (streamlined from 11 with explicit code availability assessment: VLA-Pruner and DTP have public code; TIES is training-free and reimplementable; FTM is trivially reimplementable) including SRPO (82.1% SOTA), DTP, TIES, and VLA-Pruner. Concurrent efficiency-focused methods (SP-VLA ICLR 2026, SpecPrune-VLA, VLA-Cache NeurIPS 2025) are discussed as complementary — targeting temporal/spatial redundancy rather than causal robustness. InSpire (arXiv 2505.13888) is discussed as a complementary prompting-based approach to the same spurious correlation problem. GPU costs updated to current May 2026 market rates ($0.80/hr A100 spot from specialized providers). Primary targets: AAAI 2027 and ICLR 2027.\",\n  \"project_name\": \"causal_token_sel_vla\",\n  \"source\": \"web_research\"\n}\n```\n\n---\n\nHere is a summary of all changes integrated into this v4 revision, mapping to the reviewer's 4 issues:\n\n**Opportunity field** -- Added ViT-Shapley as a \"fourth thread\" (amortized Shapley estimation for vision transformers, observational vs. interventional distinction). Added mechanistic interpretability (CoRL 2025) as a fifth thread. Renumbered CIRRL from \"fourth\" to \"sixth thread.\"\n\n**Landscape field** -- Added three new sections: (1) \"Amortized Shapley estimation for vision transformers\" covering ViT-Shapley's pipeline, architectural analogy to CaTS, and the observational vs. interventional Shapley distinction with reference to Heskes et al. NeurIPS 2020. (2) \"Mechanistic interpretability for VLA\" covering the CoRL 2025 paper's activation projection approach, complementarity with CaTS. (3) \"Test-time adaptation\" covering PDF (arXiv 2604.18107) and its complementary positioning vs. CaTS.\n\n**Approach field** -- Added the VLM-not-VLA caveat after the spatial locality justification paragraph, noting that ablation (b) explicitly tests this. Added the \"Relationship to ViT-Shapley (ICLR 2023)\" subsection in the ACS section. Added two new \"vs.\" entries in Key differentiations: vs. ViT-Shapley and vs. Mechanistic Interpretability for VLA Steering.\n\n**Key references** -- Added all 4 new references: ViT-Shapley, Mechanistic Interpretability for VLA Steering, PDF, and Causal Shapley Values (Heskes et al.).\n\n**Description** -- Added points (5), (6), and (7) after \"Key advances over v2:\" covering ViT-Shapley differentiation, VLM-not-VLA acknowledgment, and mechanistic interpretability/PDF positioning.\n\n**Other fields** -- `change_type` set to `\"minor\"`. All other fields (title, core_problem, resource_estimate, target_venues, level, project_name, source) preserved identically from v3."
      }
    ],
    "totalDurationMs": 990140,
    "totalTokens": 94912,
    "totalToolUseCount": 31,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 78630,
      "cache_read_input_tokens": 0,
      "output_tokens": 16281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 78630
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16281,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 78630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 78630,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 8,
      "searchCount": 11,
      "bashCount": 11,
      "editFileCount": 1,
      "linesAdded": 90,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "cd331472-05ef-446c-9331-2e2025c9698e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"Causal Token Selection for Invariant VLA Policies via Amortized Interv…",
  "leafUuid": "eb680509-7b00-4439-99e0-ffa4ef559deb",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise VLA causal token selection with ViT-Shapley differentiation",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82"
}
```

---

### Assistant

_source line 48 · 2026-05-13T06:05:38.595Z_

Let me read the full output to verify all changes were integrated correctly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb680509-7b00-4439-99e0-ffa4ef559deb",
  "isSidechain": false,
  "requestId": "req_011Caz4hvjFNxvs7H8FoKb4S",
  "type": "assistant",
  "uuid": "7ed3d85e-44af-4b65-a839-8ef26f7057ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016b4UP5ZggwKi571xjKPPkG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3917,
      "cache_read_input_tokens": 43098,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3917,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 43098,
          "cache_creation_input_tokens": 3917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3917
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

_source line 49 · 2026-05-13T06:05:38.945Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NNojbXo7A6nGNegJgvz3v2`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-/d1da6575-a77d-4a5e-984b-7ebc8af7dd82/tool-results/toolu_01DrprPHVpyidUfCuAfRhyri.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ed3d85e-44af-4b65-a839-8ef26f7057ec",
  "isSidechain": false,
  "requestId": "req_011Caz4hvjFNxvs7H8FoKb4S",
  "type": "assistant",
  "uuid": "4041e574-e9b4-4cde-b753-bfd566e59ec8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016b4UP5ZggwKi571xjKPPkG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3917,
      "cache_read_input_tokens": 43098,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3917,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 43098,
          "cache_creation_input_tokens": 3917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3917
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

_source line 50 · 2026-05-13T06:05:39.233Z_

<details><summary>↩ Tool result · `toolu_01NNojbXo7A6nGNegJgvz3v2`</summary>

````text
1	[
2	  {
3	    "type": "text",
4	    "text": "The file write needs permission. Let me verify the JSON is valid by outputting it directly. Here is the complete revised JSON with all changes integrated:\n\n```json\n{\n  \"title\": \"Causal Token Selection for Invariant VLA Policies via Amortized Interventional Scoring\",\n  \"change_type\": \"minor\",\n  \"core_problem\": \"VLA models learn spurious visual correlations — attending to background textures, lighting conditions, and distractor objects that co-occur with target actions in training data — causing catastrophic failure under visual distribution shifts. Recent work (arXiv 2502.11501, ACL Findings 2025; arXiv 2512.07580, ICLR 2026) reveals two critical findings: (1) many attention-based token pruning methods underperform even naive random selection due to flawed scoring criteria, and (2) visual token information 'vanishes' in deep LLM layers, becoming uniformly uninformative beyond an 'information horizon' — meaning that any token selection must operate before this horizon. Meanwhile, a proliferation of concurrent VLA token selection methods (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, Compressor-VLA, Gaze-VLA — all 2025-2026) each propose different heuristic criteria (attention intersection, cross-attention TopK, Gumbel softmax, Kendall rank consistency, spatio-semantic dual-aware scoring, hierarchical importance, instruction-guided compression, gaze alignment), yet none provide formal justification for why their criterion identifies task-relevant tokens rather than merely attention-salient tokens. A complementary line of work addresses VLA spurious correlations via language-guided spatial reasoning (InSpire, arXiv 2505.13888), redirecting attention through prompting rather than principled token selection. Simple adaptation methods like FTM (arXiv 2512.02902) can recover substantial robustness with only 4K parameters, raising the question: can we identify *why* certain tokens matter and provide interpretable, formally grounded selection criteria rather than black-box affine recalibration?\",\n  \"opportunity\": \"Three research threads have developed in isolation: (1) causal intervention for imitation learning robustness (Causal-ACT, arXiv 2507.22380; ICIL, NeurIPS 2021), operating at the feature level in smaller architectures, (2) VLA token pruning for efficiency and robustness (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, VLA-Pruner, VLA-IAP, OTPrune, Compressor-VLA, SpecPrune-VLA, VLA-Cache), using attention/gradient/geometric/rank/temporal heuristics without causal grounding, and (3) causal attention distillation (LeaF, NeurIPS 2025) and learnable pruning (LearnPruner, arXiv 2604.23950), which move beyond pure attention heuristics but lack formal causal intervention criteria. A fourth thread — amortized Shapley estimation for vision transformers — demonstrates the feasibility of training a lightweight explainer model to predict per-patch importance scores in a single forward pass (ViT-Shapley, ICLR 2023 Oral, arXiv 2206.05282), but targets observational Shapley values for model explanation rather than interventional causal effects for cross-environment robustness. Mechanistic interpretability work (arXiv 2509.00328, CoRL 2025) has independently validated that interventional methods can identify causally relevant structure in VLA representations — activation projection identifies sparse semantic directions in OpenVLA and Pi0 that are causally linked to action selection — but operates at the neuron/direction level for behavioral steering rather than the token level for robustness-oriented selection. A sixth thread — causality-inspired robustness theory — has recently achieved a breakthrough: CIRRL (arXiv 2505.12868) provides the first finite-radius robustness guarantee in nonlinear settings by combining identifiable representation learning with anchor regression, showing that operating at the representation level (where latent variables are identifiable up to affine transformation) is the key to extending causal robustness beyond linear models. A critical empirical finding connects these threads to VLA architectures specifically: visual tokens in VLA architectures preserve spatial correspondence to image patches at the vision encoder output (where SigLIP provides semantic and DINOv2 provides spatial features), but this spatial structure degrades progressively through LLM layers due to self-attention mixing, ultimately vanishing at an 'information horizon' (arXiv 2512.07580). This means token-level causal selection must operate at or near the vision encoder output — where spatial locality is preserved by construction — rather than at deep LLM layers where existing attention-based methods struggle (explaining why they often underperform random selection). The vision encoder output provides a form of identifiable representation (spatial correspondence = patch-level identifiability), analogous to CIRRL's requirement for identifiable latent variables, suggesting that representation-level causal robustness can extend to the VLA setting. Formalizing this insight via a structural causal model over the token-action pipeline, with amortized interventional scoring operating at the pre-LLM representation layer, would provide the principled criterion that existing pruning methods lack while operating in the representation space where the criterion is most valid.\",\n  \"landscape\": \"**Robustness benchmarking**: LIBERO-Plus (arXiv 2510.13626, CVPR 2026) demonstrates VLA catastrophic failures across 7 perturbation dimensions, with the current SOTA at 82.1% average success (SRPO, arXiv 2511.15605) — SRPO achieves 167% improvement over one-shot SFT baseline via self-referential RL without token selection. **Causal approaches in imitation learning**: Causal-ACT (arXiv 2507.22380, July 2025) integrates causal structure learning into ACT by learning binary causal graphs over ResNet features — achieving 0.82 OOD success on ALOHA cube transfer vs. 0.23 for standard ACT. However, it operates at the feature level in small architectures, uses heuristic energy-based graph search, and evaluates on a single simple task. ICIL (NeurIPS 2021) learns domain-invariant features for imitation but not at the token level. CLIP-ICM (ICML 2025) applies causal invariance to VLMs via SCMs but for classification, not action policies. **Spurious correlation mitigation via prompting**: InSpire (arXiv 2505.13888, May 2025) mitigates VLA spurious correlations by boosting spatial reasoning — prepending directional questions ('In which direction is [object] relative to the robot?') to redirect attention to task-relevant features. Achieves +6.2%/+10% on seen/unseen LIBERO tasks for miniVLA-VQ and +25%/+26% in real-world tasks for π0-FAST. Complementary approach (prompting-based attention redirection vs. CaTS's principled token selection); evaluated on standard LIBERO, not LIBERO-Plus perturbation dimensions. **Simple adaptation baselines**: FTM (arXiv 2512.02902) achieves 87.1% on LIBERO viewpoint with just 4K parameters via global affine token modulation; FLA extends to 90.8% with 4.7M parameters. Neither evaluated on full LIBERO-Plus; neither provides interpretability. **Active attention**: AVA-VLA (arXiv 2511.18960) dynamically reweights visual tokens via active attention, achieving 74.7% on LIBERO-Plus. **Causality-inspired robustness theory**: CIRRL (arXiv 2505.12868, May 2025) provides the first causality-inspired finite-radius robustness guarantee in nonlinear settings, using identifiable representation learning (Distributional Principal Autoencoders) to recover latent variables up to affine transformation, then applying anchor regression in the identifiable latent space. Key theorem: the two-step estimator achieves optimal worst-case risk among all L²-integrable functions under elliptical noise. Directly relevant to CaTS's theoretical framework — CIRRL validates the principle that representation-level causal robustness can overcome IRM/V-REx limitations, though its elliptical distribution assumptions and tabular data focus limit direct application to high-dimensional VLA visual tokens. CaTS's encoder-level scoring operates at a representation layer where spatial identifiability holds (analogous to CIRRL's affine identifiability), providing an empirical bridge between CIRRL's theory and VLA practice. **Amortized Shapley estimation for vision transformers**: ViT-Shapley (ICLR 2023 Oral, arXiv 2206.05282) trains a separate explainer model to predict per-patch Shapley values in a single forward pass, using a three-stage pipeline: (1) train ViT classifier, (2) fine-tune a surrogate with attention masking to handle partial inputs, (3) train the explainer to amortize Shapley computation. The explainer produces 196 per-patch importance scores (14×14 grid) and outperforms attention rollout, GradCAM, and LRP for ViT explanation. Publicly available code (github.com/suinleelab/vit-shapley). CaTS's amortized causal scoring head is architecturally analogous — both train a lightweight model to predict per-token importance from embeddings in a single forward pass. The critical difference: ViT-Shapley estimates observational Shapley values (how much does masking patch i change the model's prediction?) for post-hoc explanation of a fixed model on a single distribution, while CaTS estimates interventional causal effects (how much does replacing token i with environment-marginal statistics change action predictions across environments?) for cross-environment invariance during training. This distinction parallels the broader observational vs. interventional Shapley literature (Heskes et al., NeurIPS 2020): observational Shapley captures feature relevance within a distribution, while interventional Shapley captures causal influence robust to distribution shift. CaTS's intervention mechanism (environment-marginal replacement across LIBERO-Plus perturbation dimensions) is specifically designed to distinguish causal from spuriously correlated tokens — a distinction that observational Shapley cannot make when spurious correlations are present in the training distribution. ViT-Shapley's attention masking approach for evaluating ViTs with partial information is directly applicable to CaTS's intervention mechanism and informs implementation. **Mechanistic interpretability for VLA**: Mechanistic interpretability for VLA steering (CoRL 2025, arXiv 2509.00328) projects feedforward activations onto the token embedding basis to identify sparse semantic directions — such as speed and direction — that are causally linked to action selection in OpenVLA and Pi0. Enables zero-shot behavioral steering on LIBERO and real UR5 robot without fine-tuning. This validates CaTS's core premise: interventional methods can identify causally relevant structure in VLA representations. Key differentiation: operates at the neuron/direction level for behavioral steering (which directions in activation space control speed/direction?), while CaTS operates at the token level for robustness-oriented selection (which input patches contain causal vs. spurious visual information?). The two approaches are complementary — mechanistic interpretability explains how VLA representations encode action semantics, while CaTS identifies which visual tokens should feed into those representations for cross-environment robustness. **Test-time adaptation**: PDF (arXiv 2604.18107, April 2026) addresses VLA spurious correlations ('trajectory overfitting where VLAs over-attend to spurious correlation between actions and entities') via test-time perturbation learning with delayed feedback. Uses uncertainty-based data augmentation and action voting without fine-tuning, achieving +7.4% on LIBERO. Complementary to CaTS: PDF is a test-time adaptation method that corrects overconfident action predictions post-hoc, while CaTS is a training-time causal selection method that prevents spurious correlations from entering the policy. The two could be combined — CaTS for principled token selection during training, PDF for residual correction at test time. **Concurrent VLA token pruning/selection methods (2025-2026) — all using heuristic criteria**: (i) SP-VLA (arXiv 2506.12723, ICLR 2026) jointly addresses temporal and spatial redundancy via action-aware model scheduling (switching between VLA and lightweight generator for deliberative vs. intuitive actions) and spatio-semantic dual-aware token pruning. Achieves 1.5× lossless acceleration on LIBERO and 2.4× on SimplerEnv with up to 6% performance gain. As an ICLR 2026 accepted paper, it represents the strongest efficiency-focused VLA pruning method. However, its spatio-semantic scoring criterion is designed for efficiency (removing redundant tokens) rather than robustness (removing spuriously correlated tokens) — a token may be spatially/semantically important yet causally spurious (e.g., a distinctive background element near the target object). Not evaluated under distribution shift. Code available on GitHub. (ii) DTP (arXiv 2601.16065, Jan 2026) prunes 'distracting tokens' via attention intersection scoring — tokens in task-irrelevant regions exceeding a scaled threshold of the maximum attention in task-relevant regions are pruned. Evaluated on SIMPLER, not LIBERO-Plus. Directly analogous motivation to CaTS (removing spuriously correlated tokens), but uses attention heuristics without formal justification that attention-salient ≠ causally relevant. Code available. (iii) FocusVLA (arXiv 2603.28740, Mar 2026) uses cross-attention-based TopK patch selection with modality cascaded attention, achieving 98.7% on standard LIBERO. Not evaluated on LIBERO-Plus; assumes cross-attention scores identify task relevance without causal validation. (iv) LightVLA (arXiv 2509.12594, ICRA 2026) uses Gumbel softmax for differentiable token selection, reducing FLOPs by 59.1% with 2.9% success rate improvement on LIBERO. End-to-end learned selection but criterion is implicitly defined by task loss — no interpretability or formal robustness criterion. (v) TIES (arXiv 2603.24941, Mar 2026) introduces Kendall rank consistency across layers as a stability metric, improving average success by 6% on CogACT+SIMPLER while reducing tokens by 78%. Most relevant concurrent work: uses rank consistency as a robustness signal, but this is a statistical regularity heuristic, not a causal criterion — rank consistency does not distinguish causal from spuriously consistent tokens. Not evaluated under environmental perturbations. (vi) BFA++ (arXiv 2602.20566, Feb 2026) uses hierarchical intra-view and inter-view importance predictors for multi-view VLAs. (vii) Compressor-VLA (arXiv 2511.18950) uses instruction-guided semantic and spatial compression modules, reducing visual tokens by 3× on LIBERO. (viii) Gaze-Regularized VLA (arXiv 2603.23202, Mar 2026) aligns attention with human gaze heatmaps via KL divergence. Requires human gaze data; provides indirect causal signal. (ix) LearnPruner (arXiv 2604.23950, Apr 2026) trains a learnable pruning module after the vision encoder, retaining only 5.5% of tokens while preserving ~95% performance. (x) SpecPrune-VLA (arXiv 2509.05614) uses action-aware self-speculative pruning with global history context, combining static action-level and dynamic layer-level pruning with an action-aware controller that classifies actions as coarse/fine-grained. Achieves 1.57× speedup on LIBERO and 1.70× in real-world with negligible degradation. Primarily efficiency-focused, exploiting temporal redundancy. (xi) VLA-Cache (arXiv 2502.02175, NeurIPS 2025) adaptively caches and reuses static visual tokens across consecutive frames via layer-adaptive token reusing, achieving 1.7× speedup with negligible success rate loss. Exploits temporal redundancy between adjacent observations — complementary to CaTS which addresses spatial token selection within a single frame for robustness rather than efficiency. **Token information dynamics**: arXiv 2512.07580 (ICLR 2026) discovers 'vanishing token information' — visual tokens progressively lose discriminative salience in deep LLM layers, becoming uniformly uninformative beyond an 'information horizon' (~layer 20 for general tasks, deeper for OCR). This explains why attention-based pruning in late layers underperforms random selection and motivates scoring at early/intermediate layers where spatial information is preserved. **Token pruning critique**: arXiv 2502.11501 (ACL Findings 2025) systematically shows many attention-based pruning methods underperform random selection due to position bias and flawed attention-as-importance assumptions. **Causal token pruning in NLP**: LeaF (NeurIPS 2025, arXiv 2506.07851) uses gradient-based teacher-student comparison to identify confounding tokens. Analogous in spirit but targets LLM reasoning, not embodied action; uses gradient heuristics, not formal interventions. **Robustness training**: RobustVLA (ICLR 2026, arXiv 2510.00037) uses offline robust optimization with 12.6% absolute gains on π0 backbone. **World models**: Mask World Model (arXiv 2604.19683) achieves 98.3% on standard LIBERO via geometric information bottleneck but not evaluated on LIBERO-Plus. **Shortcut learning**: arXiv 2508.06426 (CoRL 2025) identifies dataset diversity as root cause — complementary data-side approach. **Invariance theory limitations**: Rosenfeld et al. (ICLR 2021) demonstrate IRM fails in non-linear settings. V-REx (Krueger et al., ICML 2021) proposes variance-based risk extrapolation as simpler alternative but suffers similar non-linear limitations. CIRRL (arXiv 2505.12868) overcomes these limitations via identifiable representation learning but requires elliptical distribution assumptions. Wasserstein DRO (Kuhn et al., 2024) provides genuine finite-sample guarantees without requiring linear/invariance assumptions. **Amortized causal estimation**: CausalPFN (NeurIPS 2025) demonstrates amortized causal effect estimation via in-context learning with asymptotic consistency guarantees; ACTIVA (arXiv 2503.01290) uses transformer-based VAEs but is limited to tabular data. Amortized Shapley estimation (SurroShap, SimSHAP) provides non-asymptotic convergence bounds: Pr(|ϕ̂ − ϕ| ≥ ε) ≤ 2·exp(−2mε²/r²) for m samples and marginal contribution range r (Maleki et al., 2013). **No existing work combines formal token-level causal intervention criteria with amortized estimation in VLA transformers, operating at the vision encoder output where spatial locality is empirically validated, for cross-environment policy invariance.**\",\n  \"approach\": \"We propose Causal Token Selection (CaTS) v3, which identifies and retains visual tokens whose causal effect on action predictions is significant and stable across visual environments, using an amortized interventional scoring framework operating at the vision encoder output where spatial locality is empirically grounded.\\n\\n**Formal SCM for VLA Token-Action Pipeline.** We define a structural causal model: observation O is processed by the vision encoder into T(O) = {t_1,...,t_N} (N=256 for OpenVLA's SigLIP+DINOv2 encoder); each token t_i corresponds to an image patch and carries causal content C_i (object geometry, gripper state, contact regions) and spurious content S_i (background texture, lighting, distractor appearance); environment variable E influences S_i but not C_i; action A = π(f(T)) where f is the LLM backbone. We formalize the *encoder-level spatial locality* assumption (revised from the original spatial locality assumption): at the vision encoder output — before LLM self-attention layers mix token representations — causal content C_i is concentrated in a subset T* ⊂ T corresponding to image patches containing task-relevant objects, while spurious content S_i is distributed across patches containing background and distractors. **Justification**: this is grounded in two empirical findings: (a) DINOv2's attention maps show foreground object concentration by layers 3-6, with the CLS token primarily aggregating foreground tokens (arXiv 2602.22394); (b) the 'vanishing token information' phenomenon (arXiv 2512.07580) confirms that spatial discriminability is maximal at the vision encoder output and degrades through LLM depth. **Important caveat**: arXiv 2512.07580 evaluates VLMs (Qwen2.5-VL, LLaVA-1.5), not VLAs. While VLAs share the VLM backbone architecture making extrapolation reasonable, VLA models have different training objectives (action prediction vs. text generation) and potentially different attention patterns — action tokens may attend to visual tokens differently than text tokens. The information horizon position may differ for VLAs. Verifying the information horizon in VLA architectures is an explicit part of our empirical contribution (ablation b: encoder-level vs. intermediate-layer vs. late-layer scoring directly tests where spatial information degrades in VLA models). By scoring at the encoder output, CaTS operates precisely where the assumption is most valid, unlike methods scoring at deep LLM layers where information mixing undermines spatial selectivity. This encoder-level identifiability is analogous to CIRRL's (arXiv 2505.12868) key insight that robustness guarantees extend to nonlinear settings when operating on identifiable representations — the vision encoder's spatial correspondence provides patch-level identifiability that enables causal reasoning at the token level.\\n\\n**Multi-Layer Scoring Architecture.** Rather than scoring tokens at a single layer (where the spatial locality / information quality tradeoff is unclear), CaTS employs a two-stage scoring approach: (1) *Primary scoring* at the vision encoder output (post-MLP projection, pre-LLM), where spatial locality is strongest. (2) *Optional refinement scoring* at an intermediate LLM layer (before the information horizon, empirically determined per-model via the protocol of arXiv 2512.07580 — typically layer 8-15 for 7B models), capturing cross-modal relevance signals that emerge only after some language-vision interaction. The two scores are combined via a learned convex combination α·s_encoder + (1-α)·s_intermediate, where α is a learnable scalar. **Degradation analysis**: we formally analyze how the ε-invariance bound degrades as spatial locality weakens (parameterized by α_leak = fraction of causal information C_i that 'leaks' to non-corresponding tokens through self-attention). When α_leak is high (poor spatial locality at the scoring layer), the bound degrades gracefully — the theory predicts diminishing returns of causal selection over random pruning, which is empirically testable.\\n\\n**Theorem (Conditional Invariance) with Approximate Constants.** Under four assumptions — (A1) causal sufficiency: A ⊥ E | C(T*); (A2) token-level identifiability: do(t_i) changes C(T*) with positive probability for t_i ∈ T*; (A3) environment diversity: training environments span relevant E dimensions; (A4) bounded amortization error of the causal scorer — the causal token selection operator S_τ with threshold τ satisfies:\\n\\n*Concrete bound*: max_{e,e'} |R(π,e) - R(π,e')| ≤ ε(N_env, M, τ, α_leak) where:\\nε = C₁/√M + C₂·exp(-c·N_env/d_E) + C₃·α_leak·g(τ) + ε_amort\\n\\n**Approximate constant estimates (order-of-magnitude):**\\n\\n- *C₁/√M (Shapley estimation error)*: Using the Hoeffding-based bound from Maleki et al. (2013): Pr(|ϕ̂ − ϕ| ≥ ε) ≤ 2·exp(−2Mε²/r²), where r is the range of marginal contributions. With action loss normalized to [0,1] (r=1) and confidence δ=0.05: C₁ = r·√(ln(2/δ)/2) ≈ 1.36. With M=200 Shapley samples per token: C₁/√M ≈ 0.096. With M=500: ≈ 0.061. **Practical implication**: M=200 samples (200 forward passes per scored token, feasible with batch inference) yields estimation error below 0.1, sufficient for reliable token ranking.\\n\\n- *C₂·exp(-c·N_env/d_E) (environment coverage gap)*: d_E ≈ 7 for LIBERO-Plus's 7 perturbation dimensions (camera, robot, language, light, background, noise, layout). With N_env = 35 distinct environments (7 dimensions × 5 perturbation levels each) and c ≈ 0.5-1.0 (standard covering-number scaling for bounded domains): exp(-c·35/7) = exp(-2.5 to -5.0) ≈ 0.007-0.082. With C₂ ≈ 1 (bounded loss): this term contributes ≈ 0.01-0.08. **Practical implication**: 35 environments across 7 dimensions make this term small; the bound suggests N_env = Ω(d_E · log(1/δ)) ≈ 21 environments suffice for δ=0.05, which LIBERO-Plus comfortably exceeds.\\n\\n- *C₃·α_leak·g(τ) (spatial locality violation)*: α_leak is empirically measurable — at the vision encoder output, we estimate α_leak ≈ 0.05-0.15 (based on DINOv2's foreground concentration in layers 3-6, arXiv 2602.22394); at intermediate LLM layer ~10, α_leak ≈ 0.3-0.5; beyond the information horizon (layer 20+), α_leak → 1.0. With g(τ) ≈ (1-τ)/τ for pruning ratio τ and C₃ ≈ 1: at encoder output with τ=0.5 (50% pruning), C₃·α_leak·g(τ) ≈ 0.1·1.0 = 0.10. At layer 20+ with α_leak ≈ 1.0: this term ≈ 1.0, dominating the bound and explaining why late-layer pruning degenerates to random selection.\\n\\n- *ε_amort (amortization gap)*: ε_amort ≤ ε_approx(W,d) + ε_stat(n_train). For a 2-layer MLP scorer with W=512 hidden units on d=1024-dimensional token embeddings: ε_approx = O(1/√W) ≈ 0.044 (for Barron-class functions); ε_stat = O(1/√n_train) ≈ 0.01 for n_train=10,000 training interventions. Total ε_amort ≈ 0.054.\\n\\n**Overall bound estimate**: At the vision encoder output with M=200, N_env=35, α_leak=0.1, τ=0.5: ε ≈ 0.096 + 0.01 + 0.10 + 0.054 ≈ 0.26. This predicts a maximum cross-environment performance gap of ~26% — a testable prediction against the empirically observed ~50-65% gap for unmodified VLAs on LIBERO-Plus. The bound tightens substantially with M=500 (ε ≈ 0.22) and with higher pruning threshold τ=0.7 (ε ≈ 0.20).\\n\\n**Full proof strategy**: The proof proceeds in three steps: (1) show that under A1-A2, exact token-level ACE identifies T* (follows from standard do-calculus); (2) bound the approximation error when ACE is estimated from M samples via Shapley decomposition (using Hoeffding-type concentration on bounded action losses, directly applying the non-asymptotic bound from Maleki et al., 2013); (3) bound the error from amortizing the Shapley estimates via a neural network (using universal approximation for Barron-class functions + Rademacher complexity of the MLP hypothesis class). Step (3) yields the ε_amort term.\\n\\n**Failure modes (explicit with analysis):** (F1) Insufficient environment diversity violates A3 — same limitation as IRM/V-REx, partially addressed by CIRRL's identifiable representation approach but CIRRL requires elliptical distribution assumptions that may not hold for VLA visual tokens. Mitigation: LIBERO-Plus provides 7 perturbation dimensions with ~35 environments; we report per-dimension results to identify which dimensions have sufficient diversity. (F2) Spatial locality violation at scoring layer (high α_leak). Mitigation: multi-layer scoring allows operating at the layer with lowest α_leak; we empirically measure α_leak by comparing per-token ACE computed at encoder output vs. intermediate LLM layers. (F3) Amortization gap (see detailed analysis below). (F4) V-REx variance penalty limitations in non-linear settings — see honest framing below.\\n\\n**Amortized Causal Scoring (ACS) with Quantified Amortization Gap.** We train a lightweight causal scoring head attached to the frozen VLA backbone. Training data is generated via *batch stochastic interventions*: for randomly sampled token subsets across LIBERO-Plus perturbation environments, we replace token embeddings with environment-marginal statistics and measure KL divergence in action distributions. A Shapley-value-inspired decomposition attributes group effects to individual tokens. The scorer (2-layer MLP with width 512, <1M parameters) learns to predict token-level causal effects from token embeddings.\\n\\n**Relationship to ViT-Shapley (ICLR 2023)**: CaTS's amortized scoring architecture draws on the ViT-Shapley paradigm of training a separate model to predict per-token importance in a single forward pass. However, CaTS departs in three key ways: (a) the scoring target is interventional causal effects computed via environment-marginal token replacement across LIBERO-Plus perturbation dimensions, not observational Shapley values computed via masking on a single distribution; (b) the surrogate stage uses multi-environment intervention data rather than random masking, training the scorer to predict action distribution stability across environments rather than prediction change under masking; (c) the scorer is integrated into a training-time robustness objective (composite V-REx + DRO loss), not used for post-hoc explanation. ViT-Shapley's attention masking approach for evaluating ViTs with partial information informs our intervention mechanism — we adapt their masking strategy to implement environment-marginal token replacement, replacing masked tokens with marginal statistics pooled across perturbation environments rather than zeroing them out.\\n\\n**Amortization gap analysis**: The gap between the learned scorer s_θ(t_i) and the true ACE(t_i) is bounded by: ε_amort ≤ ε_approx(W, d) + ε_stat(n_train) where ε_approx(W, d) = O(1/√W) ≈ 0.044 for W=512 (for Barron-class functions on compact domains), and ε_stat(n_train) = O(1/√n_train) ≈ 0.01 for n_train=10,000 training interventions. **Central validation protocol** (not merely an ablation): we compute exact ACE on a validation set of 50 tokens × 5 environments (250 forward passes per token = 12,500 total, feasible) and report: (a) Pearson/Spearman correlation between s_θ and exact ACE; (b) mean absolute error; (c) rank agreement (does s_θ rank tokens in the same order as exact ACE?). The amortized scorer is considered validated if rank-order Spearman ρ > 0.8 and the scoring threshold τ selects a token set overlapping ≥ 85% with the exact-ACE-selected set. If validation fails, we fall back to exact ACE computation at inference (trading efficiency for correctness), which remains a viable contribution.\\n\\n**Composite Robustness Objective (honest framing with V-REx/DRO interaction analysis).** We do NOT claim to solve the non-linear invariance problem. Instead, we use a *composite robustness objective* combining three components: (1) Standard action prediction loss on selected tokens: L_task = E_e[L(π(S_τ(T)), a*)]. (2) V-REx-style variance penalty: L_var = Var_e(L(π(S_τ(T)), a*)), which penalizes cross-environment loss variance. We frame this honestly as a *practical heuristic* that is simpler and more stable than IRMv1 (Krueger et al., ICML 2021) but shares the same fundamental limitation in non-linear settings: it does not distinguish between underfitting and inherent noise, and can fail under heteroskedastic environments. (3) Wasserstein DRO regularization: L_DRO = sup_{Q: W(Q,P̂)≤ρ} E_Q[L], providing finite-sample robustness guarantees (Kuhn et al., 2024) that do not require linear assumptions.\\n\\n**V-REx and DRO interaction analysis.** The two regularizers target complementary failure modes but can interact non-trivially. *When complementary*: V-REx stabilizes performance across *known* training environments by penalizing loss variance — preventing environment-specific overfitting where the model excels in one environment but fails in others. DRO provides robustness to *unseen* environments within the Wasserstein ball — guarding against distributional shift at test time. Together, they create a 'robust-within-uniform' objective: the policy must perform uniformly across training environments (V-REx) while being robust to perturbations of each environment's distribution (DRO). *When potentially conflicting*: DRO with large radius ρ may concentrate model capacity on worst-case distributions, potentially increasing cross-environment variance to better handle the hardest cases — precisely what V-REx penalizes. *Resolution*: for small-to-moderate DRO radius ρ, Wasserstein DRO is equivalent to variation regularization (Kuhn et al., 2024), making the two objectives approximately aligned. In practice, we operate with moderate ρ where the Wasserstein ball captures realistic perturbations (calibrated to LIBERO-Plus perturbation magnitudes) rather than adversarial worst cases. The sensitivity analysis (ablation c) explicitly measures the V-REx/DRO tradeoff by sweeping λ_var and λ_DRO independently and jointly, reporting both average performance and cross-environment variance to identify the Pareto frontier. We note that CIRRL (arXiv 2505.12868) offers a principled alternative — identifiable representation learning followed by anchor regression — that avoids the V-REx/DRO tension entirely, but requires elliptical distribution assumptions that we cannot verify for VLA visual tokens; adapting CIRRL's framework to VLA architectures is an important direction for future work.\\n\\nThe combined loss is L = L_task + λ_var·L_var + λ_DRO·L_DRO, where λ_var and λ_DRO are hyperparameters with explicit sensitivity analysis. We expect V-REx to provide better empirical performance in practice (as observed in prior work) while DRO provides the theoretical safety net.\\n\\n**Architecture.** Frozen OpenVLA-OFT backbone (7B). The ACS head operates at the vision encoder output (post-projection), with optional refinement at an intermediate LLM layer. Total trainable parameters: ACS scoring head (~0.5M) + thin LoRA adaptation (~3.5M) = ~4M total. At inference, the scorer assigns causal scores to all visual tokens in a single forward pass; tokens below threshold τ are pruned before entering the LLM backbone, providing both robustness and efficiency.\\n\\n**Evaluation with Formal Statistical Protocol.** Primary benchmark: LIBERO-Plus across all 7 perturbation dimensions. Primary metric: average success rate under distribution shift.\\n\\n**Statistical protocol against random pruning** (addressing arXiv 2502.11501's findings): We adopt a paired bootstrap protocol with bias-corrected accelerated (BCa) confidence intervals and sign-flip permutation tests (following arXiv 2511.19794). Specifically: (a) train CaTS and random-pruning variants under identical conditions with 5 random seeds; (b) record per-seed, per-task success rate differences; (c) compute BCa 95% confidence intervals on the mean difference; (d) perform sign-flip permutation test (10,000 permutations) for each perturbation dimension. CaTS claims significant improvement only if the BCa interval lies entirely above zero AND the permutation p-value < 0.05. *A priori success criterion*: CaTS must significantly outperform random pruning on at least 5 of 7 perturbation dimensions. If this criterion is not met, we report the negative result transparently and analyze which perturbation types resist causal selection (contributing understanding of when causal criteria matter vs. when random suffices).\\n\\n**Baselines (8 core, with code availability assessment).** We streamline from 11 to 8 core baselines, prioritizing those with available code or reproducible implementations on LIBERO-Plus, and dropping baselines requiring non-trivial cross-architecture adaptation:\\n\\n(1) SRPO (arXiv 2511.15605) — current LIBERO-Plus SOTA (82.1%). Evaluated in original LIBERO-Plus paper; results directly comparable. (2) FTM/FLA (arXiv 2512.02902) — simple adaptation baseline. Reproduced on LIBERO-Plus; FTM requires only 4K trainable parameters, making reproduction straightforward even without official code (single affine transform layer). (3) AVA-VLA (arXiv 2511.18960) — active visual attention, 74.7% on LIBERO-Plus. Already evaluated on LIBERO-Plus in original work. (4) RobustVLA (ICLR 2026, arXiv 2510.00037) — offline robust optimization, directly targets VLA robustness. ICLR 2026 accepted, code expected. (5) DTP (arXiv 2601.16065) — most directly analogous concurrent work (attention-based distractor identification). Code available at anonymous repository. Requires adaptation to LIBERO-Plus (originally evaluated on SIMPLER). (6) TIES (arXiv 2603.24941) — most sophisticated heuristic baseline (inter-layer rank consistency). Code availability: pending. Method is training-free and well-specified, making reimplementation feasible. (7) VLA-Pruner (arXiv 2511.16449) — temporal-aware dual-level pruning. Code available on GitHub (MINT-SJTU/VLA-Pruner). (8) Random token pruning — critical control baseline, trivial to implement.\\n\\n**Baselines discussed but not reproduced (with justification)**: Causal-ACT (feature-level ResNet+ACT architecture → token-level OpenVLA adaptation requires non-trivial architectural changes beyond a fair comparison). LeaF-adapted (NLP reasoning → VLA action policies requires speculative adaptation with unclear design choices). FocusVLA, LightVLA, BFA++, Compressor-VLA (not evaluated on LIBERO-Plus; codebases target different VLA architectures). SP-VLA, SpecPrune-VLA, VLA-Cache (efficiency-focused methods exploiting temporal redundancy; not evaluated under distribution shift; complementary rather than competing with CaTS's robustness objective). InSpire (prompting-based approach, orthogonal mechanism targeting same problem; could be combined with CaTS in future work). These are all discussed in the landscape section with explicit differentiation.\\n\\n**Ablations**: (a) amortized vs. exact ACE (central validation, not just ablation); (b) encoder-level vs. intermediate-layer vs. late-layer scoring (testing spatial locality assumption directly); (c) V-REx only vs. DRO only vs. composite objective (including joint λ_var × λ_DRO sensitivity sweep to characterize the interaction frontier and identify the complementary vs. conflicting regime); (d) variance penalty weight sensitivity; (e) DRO radius ρ sensitivity (calibrated against LIBERO-Plus perturbation magnitudes); (f) pruning ratio sweep (10-90%); (g) per-perturbation-dimension analysis; (h) causal score interpretability analysis (do high-scoring tokens correspond to task-relevant regions via IoU with ground-truth object masks?); (i) α_leak measurement across layers.\\n\\n**Key differentiations from all concurrent work.** The central claim is not merely that causal criteria exist, but that they provide *measurably better token selection than heuristic alternatives* — the burden of proof is on CaTS, and the evaluation is designed to test this rigorously.\\n\\nvs. SP-VLA (ICLR 2026): SP-VLA jointly optimizes temporal scheduling and spatial token pruning for efficiency — its spatio-semantic criterion identifies tokens that are spatially/semantically redundant but not necessarily causally spurious. A background token near the target object may have high spatio-semantic importance (spatially close, semantically related to the scene) yet be causally irrelevant to the action. CaTS's interventional criterion tests causal relevance directly via environment-marginal replacement. The two approaches are potentially complementary: SP-VLA for temporal efficiency, CaTS for causal robustness within each selected frame.\\n\\nvs. DTP (arXiv 2601.16065): DTP uses attention intersection heuristics (tokens in irrelevant regions with attention exceeding scaled threshold are pruned). CaTS uses formal causal intervention criteria. DTP's attention-based scoring is exactly the type shown to be unreliable by arXiv 2502.11501; CaTS's causal scoring is designed to be the principled alternative. Empirical comparison on LIBERO-Plus will directly test whether causal grounding outperforms attention-based distractor identification.\\n\\nvs. FocusVLA (arXiv 2603.28740): FocusVLA uses cross-attention TopK selection + modality cascaded attention, achieving strong results on standard LIBERO (98.7%) but without robustness evaluation. CaTS targets robustness under distribution shift specifically. FocusVLA's TopK is a differentiable selection mechanism but provides no criterion for *which* tokens matter for cross-environment generalization.\\n\\nvs. LightVLA (arXiv 2509.12594): LightVLA learns token selection end-to-end via Gumbel softmax — the selection criterion is implicitly defined by the training loss and may overfit to spurious correlations in training environments. CaTS's explicit causal criterion is designed to prevent exactly this overfitting.\\n\\nvs. TIES (arXiv 2603.24941): TIES uses inter-layer rank consistency (Kendall τ) as a stability signal — an innovative heuristic that captures token 'reliability' across layers. However, rank consistency does not distinguish between causally relevant tokens and tokens that are consistently spurious (e.g., a distinctive background element present in all training scenes would have high rank consistency but is causally irrelevant). CaTS's interventional scoring directly tests causal relevance via environment-marginal replacement.\\n\\nvs. InSpire (arXiv 2505.13888): InSpire redirects VLA attention via language prompting (spatial reasoning questions), achieving an indirect form of spurious correlation mitigation without token-level selection. CaTS operates at the token level with formal causal criteria. The two approaches are complementary — InSpire provides a zero-cost attention redirect while CaTS provides principled token selection with theoretical guarantees. Future work could combine InSpire's spatial prompting with CaTS's causal scoring.\\n\\nvs. CIRRL (arXiv 2505.12868): CIRRL provides finite-radius nonlinear robustness via identifiable representation learning, but operates on tabular data with elliptical distribution assumptions. CaTS draws theoretical inspiration from CIRRL's key insight (representation-level identifiability enables causal robustness) while adapting to the VLA setting where visual encoder outputs provide spatial patch-level identifiability. CaTS's DRO component provides analogous finite-sample guarantees without requiring elliptical assumptions.\\n\\nvs. Gaze-VLA (arXiv 2603.23202): Uses human gaze as an indirect causal signal (humans look at task-relevant regions). Requires gaze data collection; gaze provides a noisy proxy for causal relevance (humans also look at salient distractors). CaTS derives causal relevance from the model's own action predictions under intervention.\\n\\nvs. Causal-ACT (arXiv 2507.22380): Token-level in 7B VLA (not feature-level in ResNet+ACT); amortized scoring (not heuristic graph search); comprehensive LIBERO-Plus evaluation; concrete ε-invariance bound with approximate constants.\\n\\nvs. FTM: Interpretable per-token causal scores (not black-box affine transform); selective token removal (not global recalibration); formal robustness criterion.\\n\\nvs. LeaF (NeurIPS 2025): VLA action policies (not NLP reasoning); cross-environment interventional scoring (not single-domain gradient heuristics); formal SCM (not teacher-student comparison).\\n\\nvs. ViT-Shapley (ICLR 2023): CaTS's amortized scorer is architecturally analogous to ViT-Shapley's learned explainer — both predict per-token importance from embeddings in one forward pass. The fundamental difference is the scoring target: ViT-Shapley estimates observational Shapley values for explaining a model's predictions within a single distribution; CaTS estimates interventional causal effects across environments to identify tokens whose influence on actions is invariant to visual distribution shifts. Observational Shapley values cannot distinguish causal from spuriously correlated tokens when both correlate with the outcome in the training distribution. CaTS's environment-marginal replacement directly probes cross-environment invariance, providing the causal grounding that ViT-Shapley's masking-based approach lacks.\\n\\nvs. Mechanistic Interpretability for VLA Steering (CoRL 2025): Both use interventional methods on VLA representations. The steering work identifies neuron-level semantic directions (speed, direction) for zero-shot behavioral control; CaTS identifies token-level causal importance for robustness under visual distribution shift. Complementary: steering explains internal action semantics, CaTS determines which visual inputs matter.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~800h A100 (80GB): ~350h for 22-28 LoRA fine-tuning runs with ACS head at ~14h each (including multi-layer scoring variants and composite objective hyperparameter search), ~250h for batch intervention data generation, amortized scorer training, and exact ACE validation (12,500 forward passes for validation set + systematic coverage across 7 perturbation types), ~200h for baseline reproduction (DTP and TIES reproduction on LIBERO-Plus, FTM on LIBERO-Plus, 8 baselines total with 5 seeds each for statistical protocol) and ablations\",\n      \"gpu_utilization\": \"Low (~25-30%). GPUs sit idle during code development, causal scoring pipeline debugging, statistical protocol implementation, α_leak measurement analysis, and theorem proof development.\",\n      \"timeline\": \"4-6 months\",\n      \"team\": \"1-2 researchers (one with causal inference/DRO background for theorem formalization and proof, one with VLA/robotics experience for implementation and evaluation)\",\n      \"estimated_gpu_cost\": \"~$640 (800h × $0.80/hr A100 spot/discount pricing from specialized providers such as Thunder Compute or TensorDock, May 2026 market rate; range $0.78-$1.07/hr across providers)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~1200h A100 (80GB): agent explores ~40-50 training configurations more systematically, runs comprehensive ablations across all 7 perturbation dimensions with 5 seeds, evaluates all 8 baselines, and performs extensive α_leak measurements across layers\",\n      \"gpu_utilization\": \"Moderate (~50-60%). Agent queues experiments faster but pauses at approval gates for: multi-layer scoring architecture decisions, DRO radius selection, amortization validation thresholds, theorem assumption checking.\",\n      \"timeline\": \"2-4 months\",\n      \"team\": \"1 researcher, ~45min/day check-in for approving experiment plans, reviewing causal score visualizations, validating amortization gap measurements, and verifying theorem proof steps\",\n      \"claude_api_cost\": \"$500-700 (5000-7000 conversation turns for experiment design, code generation, theorem checking, statistical protocol implementation, result analysis)\",\n      \"estimated_gpu_cost\": \"~$960 (1200h × $0.80/hr)\",\n      \"risk_note\": \"Amortized scorer validation (Spearman ρ > 0.8 threshold) requires careful human judgment — if the scorer barely misses the threshold, the decision to proceed with amortized vs. exact scoring has significant downstream implications. DRO radius selection and the V-REx/DRO tradeoff require human expertise. Theorem proof needs verification by someone with expertise in both causal inference and approximation theory.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~2500h A100 (80GB): agent runs 120-150 experiment configurations including aggressive sweeps for scoring layer selection, V-REx/DRO weight ratios, pruning ratios, Shapley approximation methods, scorer architectures (varying width W), plus all baseline reproductions with 5 seeds and failed exploration runs\",\n      \"gpu_utilization\": \"High (~90%+). Agent queues next experiment immediately upon completion. Continuous 24/7 execution.\",\n      \"timeline\": \"3-5 weeks with 4-8 concurrent A100s; as few as 8-10 days with 16 concurrent GPUs\",\n      \"team\": \"0 (initial setup: configure LIBERO-Plus environments, OpenVLA-OFT checkpoint, define intervention distribution, implement statistical testing protocol, implement α_leak measurement)\",\n      \"claude_api_cost\": \"$700-1100 (7000-11000 turns for autonomous experiment design, debugging, statistical analysis, and paper drafting)\",\n      \"estimated_gpu_cost\": \"~$2,000 (2500h × $0.80/hr)\",\n      \"speed_bottleneck\": \"Number of concurrent A100 GPU instances. Secondary: intervention data generation is I/O-intensive (requires rendering perturbation environments). Statistical protocol with 5 seeds × 8 baselines × 7 perturbation dimensions requires organized experiment management.\",\n      \"risk_note\": \"Without human gates, agent may over-explore suboptimal scoring layer combinations or DRO radius values. The theorem formalization cannot be fully automated — agent-generated proofs require expert verification, especially the amortization gap bound (step 3 of the proof involving Rademacher complexity). The statistical protocol is automatable but interpretation of borderline results (e.g., CaTS significant on 4/7 dimensions vs. the a priori 5/7 criterion) requires human judgment. Risk mitigation: pre-define structured search space with early stopping on amortization validation metrics; halt if Spearman ρ < 0.6 after initial scorer training.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (deadline: ~August 1, 2026 — primary target, sufficient time for theoretical development, multi-layer scoring implementation, and statistical evaluation)\",\n    \"ICLR 2027 (deadline: ~October 2026 — strong target, allows comprehensive evaluation and concurrent work comparison)\",\n    \"ICRA 2027 (deadline: ~September 2026 — robotics venue, good fit for empirical contribution)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations [Causal-ACT] (arXiv 2507.22380, July 2025)\",\n    \"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling [FTM/FLA] (arXiv 2512.02902, Dec 2025)\",\n    \"Learning to Focus: Causal Attention Distillation via Gradient-Guided Token Pruning [LeaF] (NeurIPS 2025, arXiv 2506.07851)\",\n    \"Shortcut Learning in Generalist Robot Policies: The Role of Dataset Diversity and Fragmentation (CoRL 2025, arXiv 2508.06426)\",\n    \"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem? (ACL Findings 2025, arXiv 2502.11501)\",\n    \"When Token Pruning is Worse than Random: Understanding Visual Token Information in VLLMs (ICLR 2026, arXiv 2512.07580)\",\n    \"The Risks of Invariant Risk Minimization (ICLR 2021, arXiv 2010.05761)\",\n    \"Out-of-Distribution Generalization via Risk Extrapolation [V-REx] (ICML 2021, arXiv 2003.00688)\",\n    \"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models (arXiv 2511.15605)\",\n    \"AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention (arXiv 2511.18960)\",\n    \"ACTIVA: Amortized Causal Effect Estimation via Transformer-based Variational Autoencoder (arXiv 2503.01290)\",\n    \"CausalPFN: Amortized Causal Effect Estimation via In-Context Learning (NeurIPS 2025, arXiv 2506.07918)\",\n    \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026, arXiv 2510.13626)\",\n    \"Invariant Causal Imitation Learning for Generalizable Policies [ICIL] (NeurIPS 2021)\",\n    \"DTP: A Simple yet Effective Distracting Token Pruning Framework for VLA Models (arXiv 2601.16065, Jan 2026)\",\n    \"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models (arXiv 2603.28740, Mar 2026)\",\n    \"LightVLA: Towards Efficient VLA Models via Differentiable Token Pruning (ICRA 2026, arXiv 2509.12594)\",\n    \"TIES: Beyond Attention Magnitude — Leveraging Inter-layer Rank Consistency for Efficient VLA Models (arXiv 2603.24941, Mar 2026)\",\n    \"BFA++: Hierarchical Best-Feature-Aware Token Pruning for Multi-View VLA Models (arXiv 2602.20566, Feb 2026)\",\n    \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation (arXiv 2511.18950)\",\n    \"Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation (arXiv 2603.23202, Mar 2026)\",\n    \"LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models (arXiv 2604.23950, Apr 2026)\",\n    \"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations [RobustVLA] (ICLR 2026, arXiv 2510.00037)\",\n    \"Mask World Model: Predicting What Matters for Robust Robot Policy Learning (arXiv 2604.19683, April 2026)\",\n    \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient VLA Inference (arXiv 2511.16449)\",\n    \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for VLA Models (arXiv 2603.22991, March 2026)\",\n    \"Learning Invariant Causal Mechanism from Vision-Language Models [CLIP-ICM] (ICML 2025, arXiv 2405.15289)\",\n    \"OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport (arXiv 2602.20205)\",\n    \"Wasserstein Distributionally Robust Optimization and Variation Regularization (Operations Research, 2024)\",\n    \"Finite-Sample Guarantees for Wasserstein DRO: Breaking the Curse of Dimensionality (Operations Research, 2023)\",\n    \"Vision Transformers Need More Than Registers (arXiv 2602.22394, Feb 2026)\",\n    \"Bounding the Estimation Error of Sampling-based Shapley Value Approximation (arXiv 1306.4265)\",\n    \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success [OpenVLA-OFT] (arXiv 2025)\",\n    \"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration (ICLR 2026, arXiv 2506.12723)\",\n    \"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning (arXiv 2509.05614)\",\n    \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching (NeurIPS 2025, arXiv 2502.02175)\",\n    \"InSpire: Vision-Language-Action Models with Intrinsic Spatial Reasoning (arXiv 2505.13888, May 2025)\",\n    \"Causality-Inspired Robustness for Nonlinear Models via Representation Learning [CIRRL] (arXiv 2505.12868, May 2025)\",\n    \"Learning to Estimate Shapley Values with Vision Transformers [ViT-Shapley] (ICLR 2023 Oral, arXiv 2206.05282)\",\n    \"Mechanistic Interpretability for Steering Vision-Language-Action Models (CoRL 2025, arXiv 2509.00328)\",\n    \"Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models [PDF] (arXiv 2604.18107, April 2026)\",\n    \"Causal Shapley Values: Exploiting Causal Knowledge to Explain Individual Predictions of Complex Models (NeurIPS 2020, arXiv 2011.01625)\"\n  ],\n  \"description\": \"VLA models suffer catastrophic failures under visual distribution shifts, yet a proliferation of concurrent token pruning methods (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, Compressor-VLA, Gaze-VLA — all 2025-2026) each propose different heuristic criteria without formal justification, and recent work shows many attention-based methods underperform random selection (arXiv 2502.11501) due to 'vanishing token information' in deep layers (arXiv 2512.07580). We propose Causal Token Selection (CaTS) v3, bridging three disconnected threads: VLA token pruning, causal intervention for imitation learning (Causal-ACT, ICIL), and causal attention distillation (LeaF), while drawing theoretical inspiration from CIRRL's (arXiv 2505.12868) breakthrough showing that representation-level identifiability enables nonlinear causal robustness guarantees. CaTS defines a formal SCM over the VLA token-action pipeline with a revised *encoder-level spatial locality* assumption — grounded in empirical findings that DINOv2/SigLIP encoder outputs preserve spatial correspondence (a form of patch-level identifiability analogous to CIRRL's affine identifiability) while LLM self-attention progressively mixes token information. Key advances over v2: (1) Multi-layer scoring at vision encoder output (where spatial locality is empirically validated) with optional intermediate-layer refinement. (2) Concrete ε-invariance bound with approximate constants: ε = C₁/√M + C₂·exp(-c·N_env/d_E) + C₃·α_leak·g(τ) + ε_amort, with order-of-magnitude estimates (M=200 Shapley samples → estimation error ~0.096; N_env=35 across d_E=7 dimensions → coverage term ~0.01; encoder-level α_leak≈0.1 → locality term ~0.10; overall ε≈0.26, a testable prediction against the observed ~50-65% gap for unmodified VLAs). (3) Honest composite robustness objective combining V-REx (practical heuristic) with Wasserstein DRO (finite-sample guarantees), including explicit analysis of their interaction: complementary for moderate DRO radius ρ (V-REx stabilizes known environments, DRO guards against unseen shifts; for small ρ, Wasserstein DRO approximates variation regularization, aligning with V-REx), with potential conflict at large ρ resolved by operating in the moderate-ρ regime calibrated to LIBERO-Plus perturbation magnitudes. (4) Quantified amortization gap: ε_amort ≤ O(1/√W) + O(1/√n_train) ≈ 0.054 for W=512, n_train=10K, with central validation protocol (Spearman ρ > 0.8). (5) Explicit differentiation from ViT-Shapley (ICLR 2023 Oral) — CaTS's amortized scorer extends the ViT-Shapley paradigm from observational Shapley values for model explanation to interventional causal effects for cross-environment invariance. (6) Acknowledgment that the 'vanishing token information' finding (arXiv 2512.07580) was validated on VLMs, not VLAs — verifying the information horizon in VLA architectures is part of the empirical contribution. (7) Integration with mechanistic interpretability evidence (CoRL 2025) validating that interventional methods identify causal structure in VLA representations, and positioning against test-time adaptation approaches (PDF, arXiv 2604.18107) as complementary training-time vs. test-time methods for the same spurious correlation problem. Formal statistical protocol against random pruning with a priori 5/7 dimension criterion. Evaluated against 8 core baselines (streamlined from 11 with explicit code availability assessment: VLA-Pruner and DTP have public code; TIES is training-free and reimplementable; FTM is trivially reimplementable) including SRPO (82.1% SOTA), DTP, TIES, and VLA-Pruner. Concurrent efficiency-focused methods (SP-VLA ICLR 2026, SpecPrune-VLA, VLA-Cache NeurIPS 2025) are discussed as complementary — targeting temporal/spatial redundancy rather than causal robustness. InSpire (arXiv 2505.13888) is discussed as a complementary prompting-based approach to the same spurious correlation problem. GPU costs updated to current May 2026 market rates ($0.80/hr A100 spot from specialized providers). Primary targets: AAAI 2027 and ICLR 2027.\",\n  \"project_name\": \"causal_token_sel_vla\",\n  \"source\": \"web_research\"\n}\n```\n\n---\n\nHere is a summary of all changes integrated into this v4 revision, mapping to the reviewer's 4 issues:\n\n**Opportunity field** -- Added ViT-Shapley as a \"fourth thread\" (amortized Shapley estimation for vision transformers, observational vs. interventional distinction). Added mechanistic interpretability (CoRL 2025) as a fifth thread. Renumbered CIRRL from \"fourth\" to \"sixth thread.\"\n\n**Landscape field** -- Added three new sections: (1) \"Amortized Shapley estimation for vision transformers\" covering ViT-Shapley's pipeline, architectural analogy to CaTS, and the observational vs. interventional Shapley distinction with reference to Heskes et al. NeurIPS 2020. (2) \"Mechanistic interpretability for VLA\" covering the CoRL 2025 paper's activation projection approach, complementarity with CaTS. (3) \"Test-time adaptation\" covering PDF (arXiv 2604.18107) and its complementary positioning vs. CaTS.\n\n**Approach field** -- Added the VLM-not-VLA caveat after the spatial locality justification paragraph, noting that ablation (b) explicitly tests this. Added the \"Relationship to ViT-Shapley (ICLR 2023)\" subsection in the ACS section. Added two new \"vs.\" entries in Key differentiations: vs. ViT-Shapley and vs. Mechanistic Interpretability for VLA Steering.\n\n**Key references** -- Added all 4 new references: ViT-Shapley, Mechanistic Interpretability for VLA Steering, PDF, and Causal Shapley Values (Heskes et al.).\n\n**Description** -- Added points (5), (6), and (7) after \"Key advances over v2:\" covering ViT-Shapley differentiation, VLM-not-VLA acknowledgment, and mechanistic interpretability/PDF positioning.\n\n**Other fields** -- `change_type` set to `\"minor\"`. All other fields (title, core_problem, resource_estimate, target_venues, level, project_name, source) preserved identically from v3."
5	  },
6	  {
7	    "type": "text",
8	    "text": "agentId: ad283643819abe769 (use SendMessage with to: 'ad283643819abe769' to continue this agent)\n&lt;usage>total_tokens: 94912\ntool_uses: 31\nduration_ms: 990140&lt;/usage>"
9	  }
10	]
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "4041e574-e9b4-4cde-b753-bfd566e59ec8",
  "isSidechain": false,
  "promptId": "c18dd896-5585-4f7b-b0bc-42c2f8ad78d2",
  "type": "user",
  "uuid": "1b77a948-cee4-4365-a296-b70a13cba601",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-/d1da6575-a77d-4a5e-984b-7ebc8af7dd82/tool-results/toolu_01DrprPHVpyidUfCuAfRhyri.json",
      "content": "[\n  {\n    \"type\": \"text\",\n    \"text\": \"The file write needs permission. Let me verify the JSON is valid by outputting it directly. Here is the complete revised JSON with all changes integrated:\\n\\n```json\\n{\\n  \\\"title\\\": \\\"Causal Token Selection for Invariant VLA Policies via Amortized Interventional Scoring\\\",\\n  \\\"change_type\\\": \\\"minor\\\",\\n  \\\"core_problem\\\": \\\"VLA models learn spurious visual correlations — attending to background textures, lighting conditions, and distractor objects that co-occur with target actions in training data — causing catastrophic failure under visual distribution shifts. Recent work (arXiv 2502.11501, ACL Findings 2025; arXiv 2512.07580, ICLR 2026) reveals two critical findings: (1) many attention-based token pruning methods underperform even naive random selection due to flawed scoring criteria, and (2) visual token information 'vanishes' in deep LLM layers, becoming uniformly uninformative beyond an 'information horizon' — meaning that any token selection must operate before this horizon. Meanwhile, a proliferation of concurrent VLA token selection methods (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, Compressor-VLA, Gaze-VLA — all 2025-2026) each propose different heuristic criteria (attention intersection, cross-attention TopK, Gumbel softmax, Kendall rank consistency, spatio-semantic dual-aware scoring, hierarchical importance, instruction-guided compression, gaze alignment), yet none provide formal justification for why their criterion identifies task-relevant tokens rather than merely attention-salient tokens. A complementary line of work addresses VLA spurious correlations via language-guided spatial reasoning (InSpire, arXiv 2505.13888), redirecting attention through prompting rather than principled token selection. Simple adaptation methods like FTM (arXiv 2512.02902) can recover substantial robustness with only 4K parameters, raising the question: can we identify *why* certain tokens matter and provide interpretable, formally grounded selection criteria rather than black-box affine recalibration?\\\",\\n  \\\"opportunity\\\": \\\"Three research threads have developed in isolation: (1) causal intervention for imitation learning robustness (Causal-ACT, arXiv 2507.22380; ICIL, NeurIPS 2021), operating at the feature level in smaller architectures, (2) VLA token pruning for efficiency and robustness (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, VLA-Pruner, VLA-IAP, OTPrune, Compressor-VLA, SpecPrune-VLA, VLA-Cache), using attention/gradient/geometric/rank/temporal heuristics without causal grounding, and (3) causal attention distillation (LeaF, NeurIPS 2025) and learnable pruning (LearnPruner, arXiv 2604.23950), which move beyond pure attention heuristics but lack formal causal intervention criteria. A fourth thread — amortized Shapley estimation for vision transformers — demonstrates the feasibility of training a lightweight explainer model to predict per-patch importance scores in a single forward pass (ViT-Shapley, ICLR 2023 Oral, arXiv 2206.05282), but targets observational Shapley values for model explanation rather than interventional causal effects for cross-environment robustness. Mechanistic interpretability work (arXiv 2509.00328, CoRL 2025) has independently validated that interventional methods can identify causally relevant structure in VLA representations — activation projection identifies sparse semantic directions in OpenVLA and Pi0 that are causally linked to action selection — but operates at the neuron/direction level for behavioral steering rather than the token level for robustness-oriented selection. A sixth thread — causality-inspired robustness theory — has recently achieved a breakthrough: CIRRL (arXiv 2505.12868) provides the first finite-radius robustness guarantee in nonlinear settings by combining identifiable representation learning with anchor regression, showing that operating at the representation level (where latent variables are identifiable up to affine transformation) is the key to extending causal robustness beyond linear models. A critical empirical finding connects these threads to VLA architectures specifically: visual tokens in VLA architectures preserve spatial correspondence to image patches at the vision encoder output (where SigLIP provides semantic and DINOv2 provides spatial features), but this spatial structure degrades progressively through LLM layers due to self-attention mixing, ultimately vanishing at an 'information horizon' (arXiv 2512.07580). This means token-level causal selection must operate at or near the vision encoder output — where spatial locality is preserved by construction — rather than at deep LLM layers where existing attention-based methods struggle (explaining why they often underperform random selection). The vision encoder output provides a form of identifiable representation (spatial correspondence = patch-level identifiability), analogous to CIRRL's requirement for identifiable latent variables, suggesting that representation-level causal robustness can extend to the VLA setting. Formalizing this insight via a structural causal model over the token-action pipeline, with amortized interventional scoring operating at the pre-LLM representation layer, would provide the principled criterion that existing pruning methods lack while operating in the representation space where the criterion is most valid.\\\",\\n  \\\"landscape\\\": \\\"**Robustness benchmarking**: LIBERO-Plus (arXiv 2510.13626, CVPR 2026) demonstrates VLA catastrophic failures across 7 perturbation dimensions, with the current SOTA at 82.1% average success (SRPO, arXiv 2511.15605) — SRPO achieves 167% improvement over one-shot SFT baseline via self-referential RL without token selection. **Causal approaches in imitation learning**: Causal-ACT (arXiv 2507.22380, July 2025) integrates causal structure learning into ACT by learning binary causal graphs over ResNet features — achieving 0.82 OOD success on ALOHA cube transfer vs. 0.23 for standard ACT. However, it operates at the feature level in small architectures, uses heuristic energy-based graph search, and evaluates on a single simple task. ICIL (NeurIPS 2021) learns domain-invariant features for imitation but not at the token level. CLIP-ICM (ICML 2025) applies causal invariance to VLMs via SCMs but for classification, not action policies. **Spurious correlation mitigation via prompting**: InSpire (arXiv 2505.13888, May 2025) mitigates VLA spurious correlations by boosting spatial reasoning — prepending directional questions ('In which direction is [object] relative to the robot?') to redirect attention to task-relevant features. Achieves +6.2%/+10% on seen/unseen LIBERO tasks for miniVLA-VQ and +25%/+26% in real-world tasks for π0-FAST. Complementary approach (prompting-based attention redirection vs. CaTS's principled token selection); evaluated on standard LIBERO, not LIBERO-Plus perturbation dimensions. **Simple adaptation baselines**: FTM (arXiv 2512.02902) achieves 87.1% on LIBERO viewpoint with just 4K parameters via global affine token modulation; FLA extends to 90.8% with 4.7M parameters. Neither evaluated on full LIBERO-Plus; neither provides interpretability. **Active attention**: AVA-VLA (arXiv 2511.18960) dynamically reweights visual tokens via active attention, achieving 74.7% on LIBERO-Plus. **Causality-inspired robustness theory**: CIRRL (arXiv 2505.12868, May 2025) provides the first causality-inspired finite-radius robustness guarantee in nonlinear settings, using identifiable representation learning (Distributional Principal Autoencoders) to recover latent variables up to affine transformation, then applying anchor regression in the identifiable latent space. Key theorem: the two-step estimator achieves optimal worst-case risk among all L²-integrable functions under elliptical noise. Directly relevant to CaTS's theoretical framework — CIRRL validates the principle that representation-level causal robustness can overcome IRM/V-REx limitations, though its elliptical distribution assumptions and tabular data focus limit direct application to high-dimensional VLA visual tokens. CaTS's encoder-level scoring operates at a representation layer where spatial identifiability holds (analogous to CIRRL's affine identifiability), providing an empirical bridge between CIRRL's theory and VLA practice. **Amortized Shapley estimation for vision transformers**: ViT-Shapley (ICLR 2023 Oral, arXiv 2206.05282) trains a separate explainer model to predict per-patch Shapley values in a single forward pass, using a three-stage pipeline: (1) train ViT classifier, (2) fine-tune a surrogate with attention masking to handle partial inputs, (3) train the explainer to amortize Shapley computation. The explainer produces 196 per-patch importance scores (14×14 grid) and outperforms attention rollout, GradCAM, and LRP for ViT explanation. Publicly available code (github.com/suinleelab/vit-shapley). CaTS's amortized causal scoring head is architecturally analogous — both train a lightweight model to predict per-token importance from embeddings in a single forward pass. The critical difference: ViT-Shapley estimates observational Shapley values (how much does masking patch i change the model's prediction?) for post-hoc explanation of a fixed model on a single distribution, while CaTS estimates interventional causal effects (how much does replacing token i with environment-marginal statistics change action predictions across environments?) for cross-environment invariance during training. This distinction parallels the broader observational vs. interventional Shapley literature (Heskes et al., NeurIPS 2020): observational Shapley captures feature relevance within a distribution, while interventional Shapley captures causal influence robust to distribution shift. CaTS's intervention mechanism (environment-marginal replacement across LIBERO-Plus perturbation dimensions) is specifically designed to distinguish causal from spuriously correlated tokens — a distinction that observational Shapley cannot make when spurious correlations are present in the training distribution. ViT-Shapley's attention masking approach for evaluating ViTs with partial information is directly applicable to CaTS's intervention mechanism and informs implementation. **Mechanistic interpretability for VLA**: Mechanistic interpretability for VLA steering (CoRL 2025, arXiv 2509.00328) projects feedforward activations onto the token embedding basis to identify sparse semantic directions — such as speed and direction — that are causally linked to action selection in OpenVLA and Pi0. Enables zero-shot behavioral steering on LIBERO and real UR5 robot without fine-tuning. This validates CaTS's core premise: interventional methods can identify causally relevant structure in VLA representations. Key differentiation: operates at the neuron/direction level for behavioral steering (which directions in activation space control speed/direction?), while CaTS operates at the token level for robustness-oriented selection (which input patches contain causal vs. spurious visual information?). The two approaches are complementary — mechanistic interpretability explains how VLA representations encode action semantics, while CaTS identifies which visual tokens should feed into those representations for cross-environment robustness. **Test-time adaptation**: PDF (arXiv 2604.18107, April 2026) addresses VLA spurious correlations ('trajectory overfitting where VLAs over-attend to spurious correlation between actions and entities') via test-time perturbation learning with delayed feedback. Uses uncertainty-based data augmentation and action voting without fine-tuning, achieving +7.4% on LIBERO. Complementary to CaTS: PDF is a test-time adaptation method that corrects overconfident action predictions post-hoc, while CaTS is a training-time causal selection method that prevents spurious correlations from entering the policy. The two could be combined — CaTS for principled token selection during training, PDF for residual correction at test time. **Concurrent VLA token pruning/selection methods (2025-2026) — all using heuristic criteria**: (i) SP-VLA (arXiv 2506.12723, ICLR 2026) jointly addresses temporal and spatial redundancy via action-aware model scheduling (switching between VLA and lightweight generator for deliberative vs. intuitive actions) and spatio-semantic dual-aware token pruning. Achieves 1.5× lossless acceleration on LIBERO and 2.4× on SimplerEnv with up to 6% performance gain. As an ICLR 2026 accepted paper, it represents the strongest efficiency-focused VLA pruning method. However, its spatio-semantic scoring criterion is designed for efficiency (removing redundant tokens) rather than robustness (removing spuriously correlated tokens) — a token may be spatially/semantically important yet causally spurious (e.g., a distinctive background element near the target object). Not evaluated under distribution shift. Code available on GitHub. (ii) DTP (arXiv 2601.16065, Jan 2026) prunes 'distracting tokens' via attention intersection scoring — tokens in task-irrelevant regions exceeding a scaled threshold of the maximum attention in task-relevant regions are pruned. Evaluated on SIMPLER, not LIBERO-Plus. Directly analogous motivation to CaTS (removing spuriously correlated tokens), but uses attention heuristics without formal justification that attention-salient ≠ causally relevant. Code available. (iii) FocusVLA (arXiv 2603.28740, Mar 2026) uses cross-attention-based TopK patch selection with modality cascaded attention, achieving 98.7% on standard LIBERO. Not evaluated on LIBERO-Plus; assumes cross-attention scores identify task relevance without causal validation. (iv) LightVLA (arXiv 2509.12594, ICRA 2026) uses Gumbel softmax for differentiable token selection, reducing FLOPs by 59.1% with 2.9% success rate improvement on LIBERO. End-to-end learned selection but criterion is implicitly defined by task loss — no interpretability or formal robustness criterion. (v) TIES (arXiv 2603.24941, Mar 2026) introduces Kendall rank consistency across layers as a stability metric, improving average success by 6% on CogACT+SIMPLER while reducing tokens by 78%. Most relevant concurrent work: uses rank consistency as a robustness signal, but this is a statistical regularity heuristic, not a causal criterion — rank consistency does not distinguish causal from spuriously consistent tokens. Not evaluated under environmental perturbations. (vi) BFA++ (arXiv 2602.20566, Feb 2026) uses hierarchical intra-view and inter-view importance predictors for multi-view VLAs. (vii) Compressor-VLA (arXiv 2511.18950) uses instruction-guided semantic and spatial compression modules, reducing visual tokens by 3× on LIBERO. (viii) Gaze-Regularized VLA (arXiv 2603.23202, Mar 2026) aligns attention with human gaze heatmaps via KL divergence. Requires human gaze data; provides indirect causal signal. (ix) LearnPruner (arXiv 2604.23950, Apr 2026) trains a learnable pruning module after the vision encoder, retaining only 5.5% of tokens while preserving ~95% performance. (x) SpecPrune-VLA (arXiv 2509.05614) uses action-aware self-speculative pruning with global history context, combining static action-level and dynamic layer-level pruning with an action-aware controller that classifies actions as coarse/fine-grained. Achieves 1.57× speedup on LIBERO and 1.70× in real-world with negligible degradation. Primarily efficiency-focused, exploiting temporal redundancy. (xi) VLA-Cache (arXiv 2502.02175, NeurIPS 2025) adaptively caches and reuses static visual tokens across consecutive frames via layer-adaptive token reusing, achieving 1.7× speedup with negligible success rate loss. Exploits temporal redundancy between adjacent observations — complementary to CaTS which addresses spatial token selection within a single frame for robustness rather than efficiency. **Token information dynamics**: arXiv 2512.07580 (ICLR 2026) discovers 'vanishing token information' — visual tokens progressively lose discriminative salience in deep LLM layers, becoming uniformly uninformative beyond an 'information horizon' (~layer 20 for general tasks, deeper for OCR). This explains why attention-based pruning in late layers underperforms random selection and motivates scoring at early/intermediate layers where spatial information is preserved. **Token pruning critique**: arXiv 2502.11501 (ACL Findings 2025) systematically shows many attention-based pruning methods underperform random selection due to position bias and flawed attention-as-importance assumptions. **Causal token pruning in NLP**: LeaF (NeurIPS 2025, arXiv 2506.07851) uses gradient-based teacher-student comparison to identify confounding tokens. Analogous in spirit but targets LLM reasoning, not embodied action; uses gradient heuristics, not formal interventions. **Robustness training**: RobustVLA (ICLR 2026, arXiv 2510.00037) uses offline robust optimization with 12.6% absolute gains on π0 backbone. **World models**: Mask World Model (arXiv 2604.19683) achieves 98.3% on standard LIBERO via geometric information bottleneck but not evaluated on LIBERO-Plus. **Shortcut learning**: arXiv 2508.06426 (CoRL 2025) identifies dataset diversity as root cause — complementary data-side approach. **Invariance theory limitations**: Rosenfeld et al. (ICLR 2021) demonstrate IRM fails in non-linear settings. V-REx (Krueger et al., ICML 2021) proposes variance-based risk extrapolation as simpler alternative but suffers similar non-linear limitations. CIRRL (arXiv 2505.12868) overcomes these limitations via identifiable representation learning but requires elliptical distribution assumptions. Wasserstein DRO (Kuhn et al., 2024) provides genuine finite-sample guarantees without requiring linear/invariance assumptions. **Amortized causal estimation**: CausalPFN (NeurIPS 2025) demonstrates amortized causal effect estimation via in-context learning with asymptotic consistency guarantees; ACTIVA (arXiv 2503.01290) uses transformer-based VAEs but is limited to tabular data. Amortized Shapley estimation (SurroShap, SimSHAP) provides non-asymptotic convergence bounds: Pr(|ϕ̂ − ϕ| ≥ ε) ≤ 2·exp(−2mε²/r²) for m samples and marginal contribution range r (Maleki et al., 2013). **No existing work combines formal token-level causal intervention criteria with amortized estimation in VLA transformers, operating at the vision encoder output where spatial locality is empirically validated, for cross-environment policy invariance.**\\\",\\n  \\\"approach\\\": \\\"We propose Causal Token Selection (CaTS) v3, which identifies and retains visual tokens whose causal effect on action predictions is significant and stable across visual environments, using an amortized interventional scoring framework operating at the vision encoder output where spatial locality is empirically grounded.\\\\n\\\\n**Formal SCM for VLA Token-Action Pipeline.** We define a structural causal model: observation O is processed by the vision encoder into T(O) = {t_1,...,t_N} (N=256 for OpenVLA's SigLIP+DINOv2 encoder); each token t_i corresponds to an image patch and carries causal content C_i (object geometry, gripper state, contact regions) and spurious content S_i (background texture, lighting, distractor appearance); environment variable E influences S_i but not C_i; action A = π(f(T)) where f is the LLM backbone. We formalize the *encoder-level spatial locality* assumption (revised from the original spatial locality assumption): at the vision encoder output — before LLM self-attention layers mix token representations — causal content C_i is concentrated in a subset T* ⊂ T corresponding to image patches containing task-relevant objects, while spurious content S_i is distributed across patches containing background and distractors. **Justification**: this is grounded in two empirical findings: (a) DINOv2's attention maps show foreground object concentration by layers 3-6, with the CLS token primarily aggregating foreground tokens (arXiv 2602.22394); (b) the 'vanishing token information' phenomenon (arXiv 2512.07580) confirms that spatial discriminability is maximal at the vision encoder output and degrades through LLM depth. **Important caveat**: arXiv 2512.07580 evaluates VLMs (Qwen2.5-VL, LLaVA-1.5), not VLAs. While VLAs share the VLM backbone architecture making extrapolation reasonable, VLA models have different training objectives (action prediction vs. text generation) and potentially different attention patterns — action tokens may attend to visual tokens differently than text tokens. The information horizon position may differ for VLAs. Verifying the information horizon in VLA architectures is an explicit part of our empirical contribution (ablation b: encoder-level vs. intermediate-layer vs. late-layer scoring directly tests where spatial information degrades in VLA models). By scoring at the encoder output, CaTS operates precisely where the assumption is most valid, unlike methods scoring at deep LLM layers where information mixing undermines spatial selectivity. This encoder-level identifiability is analogous to CIRRL's (arXiv 2505.12868) key insight that robustness guarantees extend to nonlinear settings when operating on identifiable representations — the vision encoder's spatial correspondence provides patch-level identifiability that enables causal reasoning at the token level.\\\\n\\\\n**Multi-Layer Scoring Architecture.** Rather than scoring tokens at a single layer (where the spatial locality / information quality tradeoff is unclear), CaTS employs a two-stage scoring approach: (1) *Primary scoring* at the vision encoder output (post-MLP projection, pre-LLM), where spatial locality is strongest. (2) *Optional refinement scoring* at an intermediate LLM layer (before the information horizon, empirically determined per-model via the protocol of arXiv 2512.07580 — typically layer 8-15 for 7B models), capturing cross-modal relevance signals that emerge only after some language-vision interaction. The two scores are combined via a learned convex combination α·s_encoder + (1-α)·s_intermediate, where α is a learnable scalar. **Degradation analysis**: we formally analyze how the ε-invariance bound degrades as spatial locality weakens (parameterized by α_leak = fraction of causal information C_i that 'leaks' to non-corresponding tokens through self-attention). When α_leak is high (poor spatial locality at the scoring layer), the bound degrades gracefully — the theory predicts diminishing returns of causal selection over random pruning, which is empirically testable.\\\\n\\\\n**Theorem (Conditional Invariance) with Approximate Constants.** Under four assumptions — (A1) causal sufficiency: A ⊥ E | C(T*); (A2) token-level identifiability: do(t_i) changes C(T*) with positive probability for t_i ∈ T*; (A3) environment diversity: training environments span relevant E dimensions; (A4) bounded amortization error of the causal scorer — the causal token selection operator S_τ with threshold τ satisfies:\\\\n\\\\n*Concrete bound*: max_{e,e'} |R(π,e) - R(π,e')| ≤ ε(N_env, M, τ, α_leak) where:\\\\nε = C₁/√M + C₂·exp(-c·N_env/d_E) + C₃·α_leak·g(τ) + ε_amort\\\\n\\\\n**Approximate constant estimates (order-of-magnitude):**\\\\n\\\\n- *C₁/√M (Shapley estimation error)*: Using the Hoeffding-based bound from Maleki et al. (2013): Pr(|ϕ̂ − ϕ| ≥ ε) ≤ 2·exp(−2Mε²/r²), where r is the range of marginal contributions. With action loss normalized to [0,1] (r=1) and confidence δ=0.05: C₁ = r·√(ln(2/δ)/2) ≈ 1.36. With M=200 Shapley samples per token: C₁/√M ≈ 0.096. With M=500: ≈ 0.061. **Practical implication**: M=200 samples (200 forward passes per scored token, feasible with batch inference) yields estimation error below 0.1, sufficient for reliable token ranking.\\\\n\\\\n- *C₂·exp(-c·N_env/d_E) (environment coverage gap)*: d_E ≈ 7 for LIBERO-Plus's 7 perturbation dimensions (camera, robot, language, light, background, noise, layout). With N_env = 35 distinct environments (7 dimensions × 5 perturbation levels each) and c ≈ 0.5-1.0 (standard covering-number scaling for bounded domains): exp(-c·35/7) = exp(-2.5 to -5.0) ≈ 0.007-0.082. With C₂ ≈ 1 (bounded loss): this term contributes ≈ 0.01-0.08. **Practical implication**: 35 environments across 7 dimensions make this term small; the bound suggests N_env = Ω(d_E · log(1/δ)) ≈ 21 environments suffice for δ=0.05, which LIBERO-Plus comfortably exceeds.\\\\n\\\\n- *C₃·α_leak·g(τ) (spatial locality violation)*: α_leak is empirically measurable — at the vision encoder output, we estimate α_leak ≈ 0.05-0.15 (based on DINOv2's foreground concentration in layers 3-6, arXiv 2602.22394); at intermediate LLM layer ~10, α_leak ≈ 0.3-0.5; beyond the information horizon (layer 20+), α_leak → 1.0. With g(τ) ≈ (1-τ)/τ for pruning ratio τ and C₃ ≈ 1: at encoder output with τ=0.5 (50% pruning), C₃·α_leak·g(τ) ≈ 0.1·1.0 = 0.10. At layer 20+ with α_leak ≈ 1.0: this term ≈ 1.0, dominating the bound and explaining why late-layer pruning degenerates to random selection.\\\\n\\\\n- *ε_amort (amortization gap)*: ε_amort ≤ ε_approx(W,d) + ε_stat(n_train). For a 2-layer MLP scorer with W=512 hidden units on d=1024-dimensional token embeddings: ε_approx = O(1/√W) ≈ 0.044 (for Barron-class functions); ε_stat = O(1/√n_train) ≈ 0.01 for n_train=10,000 training interventions. Total ε_amort ≈ 0.054.\\\\n\\\\n**Overall bound estimate**: At the vision encoder output with M=200, N_env=35, α_leak=0.1, τ=0.5: ε ≈ 0.096 + 0.01 + 0.10 + 0.054 ≈ 0.26. This predicts a maximum cross-environment performance gap of ~26% — a testable prediction against the empirically observed ~50-65% gap for unmodified VLAs on LIBERO-Plus. The bound tightens substantially with M=500 (ε ≈ 0.22) and with higher pruning threshold τ=0.7 (ε ≈ 0.20).\\\\n\\\\n**Full proof strategy**: The proof proceeds in three steps: (1) show that under A1-A2, exact token-level ACE identifies T* (follows from standard do-calculus); (2) bound the approximation error when ACE is estimated from M samples via Shapley decomposition (using Hoeffding-type concentration on bounded action losses, directly applying the non-asymptotic bound from Maleki et al., 2013); (3) bound the error from amortizing the Shapley estimates via a neural network (using universal approximation for Barron-class functions + Rademacher complexity of the MLP hypothesis class). Step (3) yields the ε_amort term.\\\\n\\\\n**Failure modes (explicit with analysis):** (F1) Insufficient environment diversity violates A3 — same limitation as IRM/V-REx, partially addressed by CIRRL's identifiable representation approach but CIRRL requires elliptical distribution assumptions that may not hold for VLA visual tokens. Mitigation: LIBERO-Plus provides 7 perturbation dimensions with ~35 environments; we report per-dimension results to identify which dimensions have sufficient diversity. (F2) Spatial locality violation at scoring layer (high α_leak). Mitigation: multi-layer scoring allows operating at the layer with lowest α_leak; we empirically measure α_leak by comparing per-token ACE computed at encoder output vs. intermediate LLM layers. (F3) Amortization gap (see detailed analysis below). (F4) V-REx variance penalty limitations in non-linear settings — see honest framing below.\\\\n\\\\n**Amortized Causal Scoring (ACS) with Quantified Amortization Gap.** We train a lightweight causal scoring head attached to the frozen VLA backbone. Training data is generated via *batch stochastic interventions*: for randomly sampled token subsets across LIBERO-Plus perturbation environments, we replace token embeddings with environment-marginal statistics and measure KL divergence in action distributions. A Shapley-value-inspired decomposition attributes group effects to individual tokens. The scorer (2-layer MLP with width 512, <1M parameters) learns to predict token-level causal effects from token embeddings.\\\\n\\\\n**Relationship to ViT-Shapley (ICLR 2023)**: CaTS's amortized scoring architecture draws on the ViT-Shapley paradigm of training a separate model to predict per-token importance in a single forward pass. However, CaTS departs in three key ways: (a) the scoring target is interventional causal effects computed via environment-marginal token replacement across LIBERO-Plus perturbation dimensions, not observational Shapley values computed via masking on a single distribution; (b) the surrogate stage uses multi-environment intervention data rather than random masking, training the scorer to predict action distribution stability across environments rather than prediction change under masking; (c) the scorer is integrated into a training-time robustness objective (composite V-REx + DRO loss), not used for post-hoc explanation. ViT-Shapley's attention masking approach for evaluating ViTs with partial information informs our intervention mechanism — we adapt their masking strategy to implement environment-marginal token replacement, replacing masked tokens with marginal statistics pooled across perturbation environments rather than zeroing them out.\\\\n\\\\n**Amortization gap analysis**: The gap between the learned scorer s_θ(t_i) and the true ACE(t_i) is bounded by: ε_amort ≤ ε_approx(W, d) + ε_stat(n_train) where ε_approx(W, d) = O(1/√W) ≈ 0.044 for W=512 (for Barron-class functions on compact domains), and ε_stat(n_train) = O(1/√n_train) ≈ 0.01 for n_train=10,000 training interventions. **Central validation protocol** (not merely an ablation): we compute exact ACE on a validation set of 50 tokens × 5 environments (250 forward passes per token = 12,500 total, feasible) and report: (a) Pearson/Spearman correlation between s_θ and exact ACE; (b) mean absolute error; (c) rank agreement (does s_θ rank tokens in the same order as exact ACE?). The amortized scorer is considered validated if rank-order Spearman ρ > 0.8 and the scoring threshold τ selects a token set overlapping ≥ 85% with the exact-ACE-selected set. If validation fails, we fall back to exact ACE computation at inference (trading efficiency for correctness), which remains a viable contribution.\\\\n\\\\n**Composite Robustness Objective (honest framing with V-REx/DRO interaction analysis).** We do NOT claim to solve the non-linear invariance problem. Instead, we use a *composite robustness objective* combining three components: (1) Standard action prediction loss on selected tokens: L_task = E_e[L(π(S_τ(T)), a*)]. (2) V-REx-style variance penalty: L_var = Var_e(L(π(S_τ(T)), a*)), which penalizes cross-environment loss variance. We frame this honestly as a *practical heuristic* that is simpler and more stable than IRMv1 (Krueger et al., ICML 2021) but shares the same fundamental limitation in non-linear settings: it does not distinguish between underfitting and inherent noise, and can fail under heteroskedastic environments. (3) Wasserstein DRO regularization: L_DRO = sup_{Q: W(Q,P̂)≤ρ} E_Q[L], providing finite-sample robustness guarantees (Kuhn et al., 2024) that do not require linear assumptions.\\\\n\\\\n**V-REx and DRO interaction analysis.** The two regularizers target complementary failure modes but can interact non-trivially. *When complementary*: V-REx stabilizes performance across *known* training environments by penalizing loss variance — preventing environment-specific overfitting where the model excels in one environment but fails in others. DRO provides robustness to *unseen* environments within the Wasserstein ball — guarding against distributional shift at test time. Together, they create a 'robust-within-uniform' objective: the policy must perform uniformly across training environments (V-REx) while being robust to perturbations of each environment's distribution (DRO). *When potentially conflicting*: DRO with large radius ρ may concentrate model capacity on worst-case distributions, potentially increasing cross-environment variance to better handle the hardest cases — precisely what V-REx penalizes. *Resolution*: for small-to-moderate DRO radius ρ, Wasserstein DRO is equivalent to variation regularization (Kuhn et al., 2024), making the two objectives approximately aligned. In practice, we operate with moderate ρ where the Wasserstein ball captures realistic perturbations (calibrated to LIBERO-Plus perturbation magnitudes) rather than adversarial worst cases. The sensitivity analysis (ablation c) explicitly measures the V-REx/DRO tradeoff by sweeping λ_var and λ_DRO independently and jointly, reporting both average performance and cross-environment variance to identify the Pareto frontier. We note that CIRRL (arXiv 2505.12868) offers a principled alternative — identifiable representation learning followed by anchor regression — that avoids the V-REx/DRO tension entirely, but requires elliptical distribution assumptions that we cannot verify for VLA visual tokens; adapting CIRRL's framework to VLA architectures is an important direction for future work.\\\\n\\\\nThe combined loss is L = L_task + λ_var·L_var + λ_DRO·L_DRO, where λ_var and λ_DRO are hyperparameters with explicit sensitivity analysis. We expect V-REx to provide better empirical performance in practice (as observed in prior work) while DRO provides the theoretical safety net.\\\\n\\\\n**Architecture.** Frozen OpenVLA-OFT backbone (7B). The ACS head operates at the vision encoder output (post-projection), with optional refinement at an intermediate LLM layer. Total trainable parameters: ACS scoring head (~0.5M) + thin LoRA adaptation (~3.5M) = ~4M total. At inference, the scorer assigns causal scores to all visual tokens in a single forward pass; tokens below threshold τ are pruned before entering the LLM backbone, providing both robustness and efficiency.\\\\n\\\\n**Evaluation with Formal Statistical Protocol.** Primary benchmark: LIBERO-Plus across all 7 perturbation dimensions. Primary metric: average success rate under distribution shift.\\\\n\\\\n**Statistical protocol against random pruning** (addressing arXiv 2502.11501's findings): We adopt a paired bootstrap protocol with bias-corrected accelerated (BCa) confidence intervals and sign-flip permutation tests (following arXiv 2511.19794). Specifically: (a) train CaTS and random-pruning variants under identical conditions with 5 random seeds; (b) record per-seed, per-task success rate differences; (c) compute BCa 95% confidence intervals on the mean difference; (d) perform sign-flip permutation test (10,000 permutations) for each perturbation dimension. CaTS claims significant improvement only if the BCa interval lies entirely above zero AND the permutation p-value < 0.05. *A priori success criterion*: CaTS must significantly outperform random pruning on at least 5 of 7 perturbation dimensions. If this criterion is not met, we report the negative result transparently and analyze which perturbation types resist causal selection (contributing understanding of when causal criteria matter vs. when random suffices).\\\\n\\\\n**Baselines (8 core, with code availability assessment).** We streamline from 11 to 8 core baselines, prioritizing those with available code or reproducible implementations on LIBERO-Plus, and dropping baselines requiring non-trivial cross-architecture adaptation:\\\\n\\\\n(1) SRPO (arXiv 2511.15605) — current LIBERO-Plus SOTA (82.1%). Evaluated in original LIBERO-Plus paper; results directly comparable. (2) FTM/FLA (arXiv 2512.02902) — simple adaptation baseline. Reproduced on LIBERO-Plus; FTM requires only 4K trainable parameters, making reproduction straightforward even without official code (single affine transform layer). (3) AVA-VLA (arXiv 2511.18960) — active visual attention, 74.7% on LIBERO-Plus. Already evaluated on LIBERO-Plus in original work. (4) RobustVLA (ICLR 2026, arXiv 2510.00037) — offline robust optimization, directly targets VLA robustness. ICLR 2026 accepted, code expected. (5) DTP (arXiv 2601.16065) — most directly analogous concurrent work (attention-based distractor identification). Code available at anonymous repository. Requires adaptation to LIBERO-Plus (originally evaluated on SIMPLER). (6) TIES (arXiv 2603.24941) — most sophisticated heuristic baseline (inter-layer rank consistency). Code availability: pending. Method is training-free and well-specified, making reimplementation feasible. (7) VLA-Pruner (arXiv 2511.16449) — temporal-aware dual-level pruning. Code available on GitHub (MINT-SJTU/VLA-Pruner). (8) Random token pruning — critical control baseline, trivial to implement.\\\\n\\\\n**Baselines discussed but not reproduced (with justification)**: Causal-ACT (feature-level ResNet+ACT architecture → token-level OpenVLA adaptation requires non-trivial architectural changes beyond a fair comparison). LeaF-adapted (NLP reasoning → VLA action policies requires speculative adaptation with unclear design choices). FocusVLA, LightVLA, BFA++, Compressor-VLA (not evaluated on LIBERO-Plus; codebases target different VLA architectures). SP-VLA, SpecPrune-VLA, VLA-Cache (efficiency-focused methods exploiting temporal redundancy; not evaluated under distribution shift; complementary rather than competing with CaTS's robustness objective). InSpire (prompting-based approach, orthogonal mechanism targeting same problem; could be combined with CaTS in future work). These are all discussed in the landscape section with explicit differentiation.\\\\n\\\\n**Ablations**: (a) amortized vs. exact ACE (central validation, not just ablation); (b) encoder-level vs. intermediate-layer vs. late-layer scoring (testing spatial locality assumption directly); (c) V-REx only vs. DRO only vs. composite objective (including joint λ_var × λ_DRO sensitivity sweep to characterize the interaction frontier and identify the complementary vs. conflicting regime); (d) variance penalty weight sensitivity; (e) DRO radius ρ sensitivity (calibrated against LIBERO-Plus perturbation magnitudes); (f) pruning ratio sweep (10-90%); (g) per-perturbation-dimension analysis; (h) causal score interpretability analysis (do high-scoring tokens correspond to task-relevant regions via IoU with ground-truth object masks?); (i) α_leak measurement across layers.\\\\n\\\\n**Key differentiations from all concurrent work.** The central claim is not merely that causal criteria exist, but that they provide *measurably better token selection than heuristic alternatives* — the burden of proof is on CaTS, and the evaluation is designed to test this rigorously.\\\\n\\\\nvs. SP-VLA (ICLR 2026): SP-VLA jointly optimizes temporal scheduling and spatial token pruning for efficiency — its spatio-semantic criterion identifies tokens that are spatially/semantically redundant but not necessarily causally spurious. A background token near the target object may have high spatio-semantic importance (spatially close, semantically related to the scene) yet be causally irrelevant to the action. CaTS's interventional criterion tests causal relevance directly via environment-marginal replacement. The two approaches are potentially complementary: SP-VLA for temporal efficiency, CaTS for causal robustness within each selected frame.\\\\n\\\\nvs. DTP (arXiv 2601.16065): DTP uses attention intersection heuristics (tokens in irrelevant regions with attention exceeding scaled threshold are pruned). CaTS uses formal causal intervention criteria. DTP's attention-based scoring is exactly the type shown to be unreliable by arXiv 2502.11501; CaTS's causal scoring is designed to be the principled alternative. Empirical comparison on LIBERO-Plus will directly test whether causal grounding outperforms attention-based distractor identification.\\\\n\\\\nvs. FocusVLA (arXiv 2603.28740): FocusVLA uses cross-attention TopK selection + modality cascaded attention, achieving strong results on standard LIBERO (98.7%) but without robustness evaluation. CaTS targets robustness under distribution shift specifically. FocusVLA's TopK is a differentiable selection mechanism but provides no criterion for *which* tokens matter for cross-environment generalization.\\\\n\\\\nvs. LightVLA (arXiv 2509.12594): LightVLA learns token selection end-to-end via Gumbel softmax — the selection criterion is implicitly defined by the training loss and may overfit to spurious correlations in training environments. CaTS's explicit causal criterion is designed to prevent exactly this overfitting.\\\\n\\\\nvs. TIES (arXiv 2603.24941): TIES uses inter-layer rank consistency (Kendall τ) as a stability signal — an innovative heuristic that captures token 'reliability' across layers. However, rank consistency does not distinguish between causally relevant tokens and tokens that are consistently spurious (e.g., a distinctive background element present in all training scenes would have high rank consistency but is causally irrelevant). CaTS's interventional scoring directly tests causal relevance via environment-marginal replacement.\\\\n\\\\nvs. InSpire (arXiv 2505.13888): InSpire redirects VLA attention via language prompting (spatial reasoning questions), achieving an indirect form of spurious correlation mitigation without token-level selection. CaTS operates at the token level with formal causal criteria. The two approaches are complementary — InSpire provides a zero-cost attention redirect while CaTS provides principled token selection with theoretical guarantees. Future work could combine InSpire's spatial prompting with CaTS's causal scoring.\\\\n\\\\nvs. CIRRL (arXiv 2505.12868): CIRRL provides finite-radius nonlinear robustness via identifiable representation learning, but operates on tabular data with elliptical distribution assumptions. CaTS draws theoretical inspiration from CIRRL's key insight (representation-level identifiability enables causal robustness) while adapting to the VLA setting where visual encoder outputs provide spatial patch-level identifiability. CaTS's DRO component provides analogous finite-sample guarantees without requiring elliptical assumptions.\\\\n\\\\nvs. Gaze-VLA (arXiv 2603.23202): Uses human gaze as an indirect causal signal (humans look at task-relevant regions). Requires gaze data collection; gaze provides a noisy proxy for causal relevance (humans also look at salient distractors). CaTS derives causal relevance from the model's own action predictions under intervention.\\\\n\\\\nvs. Causal-ACT (arXiv 2507.22380): Token-level in 7B VLA (not feature-level in ResNet+ACT); amortized scoring (not heuristic graph search); comprehensive LIBERO-Plus evaluation; concrete ε-invariance bound with approximate constants.\\\\n\\\\nvs. FTM: Interpretable per-token causal scores (not black-box affine transform); selective token removal (not global recalibration); formal robustness criterion.\\\\n\\\\nvs. LeaF (NeurIPS 2025): VLA action policies (not NLP reasoning); cross-environment interventional scoring (not single-domain gradient heuristics); formal SCM (not teacher-student comparison).\\\\n\\\\nvs. ViT-Shapley (ICLR 2023): CaTS's amortized scorer is architecturally analogous to ViT-Shapley's learned explainer — both predict per-token importance from embeddings in one forward pass. The fundamental difference is the scoring target: ViT-Shapley estimates observational Shapley values for explaining a model's predictions within a single distribution; CaTS estimates interventional causal effects across environments to identify tokens whose influence on actions is invariant to visual distribution shifts. Observational Shapley values cannot distinguish causal from spuriously correlated tokens when both correlate with the outcome in the training distribution. CaTS's environment-marginal replacement directly probes cross-environment invariance, providing the causal grounding that ViT-Shapley's masking-based approach lacks.\\\\n\\\\nvs. Mechanistic Interpretability for VLA Steering (CoRL 2025): Both use interventional methods on VLA representations. The steering work identifies neuron-level semantic directions (speed, direction) for zero-shot behavioral control; CaTS identifies token-level causal importance for robustness under visual distribution shift. Complementary: steering explains internal action semantics, CaTS determines which visual inputs matter.\\\",\\n  \\\"resource_estimate\\\": {\\n    \\\"manual\\\": {\\n      \\\"gpu_hours\\\": \\\"~800h A100 (80GB): ~350h for 22-28 LoRA fine-tuning runs with ACS head at ~14h each (including multi-layer scoring variants and composite objective hyperparameter search), ~250h for batch intervention data generation, amortized scorer training, and exact ACE validation (12,500 forward passes for validation set + systematic coverage across 7 perturbation types), ~200h for baseline reproduction (DTP and TIES reproduction on LIBERO-Plus, FTM on LIBERO-Plus, 8 baselines total with 5 seeds each for statistical protocol) and ablations\\\",\\n      \\\"gpu_utilization\\\": \\\"Low (~25-30%). GPUs sit idle during code development, causal scoring pipeline debugging, statistical protocol implementation, α_leak measurement analysis, and theorem proof development.\\\",\\n      \\\"timeline\\\": \\\"4-6 months\\\",\\n      \\\"team\\\": \\\"1-2 researchers (one with causal inference/DRO background for theorem formalization and proof, one with VLA/robotics experience for implementation and evaluation)\\\",\\n      \\\"estimated_gpu_cost\\\": \\\"~$640 (800h × $0.80/hr A100 spot/discount pricing from specialized providers such as Thunder Compute or TensorDock, May 2026 market rate; range $0.78-$1.07/hr across providers)\\\"\\n    },\\n    \\\"human_in_loop\\\": {\\n      \\\"gpu_hours\\\": \\\"~1200h A100 (80GB): agent explores ~40-50 training configurations more systematically, runs comprehensive ablations across all 7 perturbation dimensions with 5 seeds, evaluates all 8 baselines, and performs extensive α_leak measurements across layers\\\",\\n      \\\"gpu_utilization\\\": \\\"Moderate (~50-60%). Agent queues experiments faster but pauses at approval gates for: multi-layer scoring architecture decisions, DRO radius selection, amortization validation thresholds, theorem assumption checking.\\\",\\n      \\\"timeline\\\": \\\"2-4 months\\\",\\n      \\\"team\\\": \\\"1 researcher, ~45min/day check-in for approving experiment plans, reviewing causal score visualizations, validating amortization gap measurements, and verifying theorem proof steps\\\",\\n      \\\"claude_api_cost\\\": \\\"$500-700 (5000-7000 conversation turns for experiment design, code generation, theorem checking, statistical protocol implementation, result analysis)\\\",\\n      \\\"estimated_gpu_cost\\\": \\\"~$960 (1200h × $0.80/hr)\\\",\\n      \\\"risk_note\\\": \\\"Amortized scorer validation (Spearman ρ > 0.8 threshold) requires careful human judgment — if the scorer barely misses the threshold, the decision to proceed with amortized vs. exact scoring has significant downstream implications. DRO radius selection and the V-REx/DRO tradeoff require human expertise. Theorem proof needs verification by someone with expertise in both causal inference and approximation theory.\\\"\\n    },\\n    \\\"auto_research\\\": {\\n      \\\"gpu_hours\\\": \\\"~2500h A100 (80GB): agent runs 120-150 experiment configurations including aggressive sweeps for scoring layer selection, V-REx/DRO weight ratios, pruning ratios, Shapley approximation methods, scorer architectures (varying width W), plus all baseline reproductions with 5 seeds and failed exploration runs\\\",\\n      \\\"gpu_utilization\\\": \\\"High (~90%+). Agent queues next experiment immediately upon completion. Continuous 24/7 execution.\\\",\\n      \\\"timeline\\\": \\\"3-5 weeks with 4-8 concurrent A100s; as few as 8-10 days with 16 concurrent GPUs\\\",\\n      \\\"team\\\": \\\"0 (initial setup: configure LIBERO-Plus environments, OpenVLA-OFT checkpoint, define intervention distribution, implement statistical testing protocol, implement α_leak measurement)\\\",\\n      \\\"claude_api_cost\\\": \\\"$700-1100 (7000-11000 turns for autonomous experiment design, debugging, statistical analysis, and paper drafting)\\\",\\n      \\\"estimated_gpu_cost\\\": \\\"~$2,000 (2500h × $0.80/hr)\\\",\\n      \\\"speed_bottleneck\\\": \\\"Number of concurrent A100 GPU instances. Secondary: intervention data generation is I/O-intensive (requires rendering perturbation environments). Statistical protocol with 5 seeds × 8 baselines × 7 perturbation dimensions requires organized experiment management.\\\",\\n      \\\"risk_note\\\": \\\"Without human gates, agent may over-explore suboptimal scoring layer combinations or DRO radius values. The theorem formalization cannot be fully automated — agent-generated proofs require expert verification, especially the amortization gap bound (step 3 of the proof involving Rademacher complexity). The statistical protocol is automatable but interpretation of borderline results (e.g., CaTS significant on 4/7 dimensions vs. the a priori 5/7 criterion) requires human judgment. Risk mitigation: pre-define structured search space with early stopping on amortization validation metrics; halt if Spearman ρ < 0.6 after initial scorer training.\\\"\\n    }\\n  },\\n  \\\"target_venues\\\": [\\n    \\\"AAAI 2027 (deadline: ~August 1, 2026 — primary target, sufficient time for theoretical development, multi-layer scoring implementation, and statistical evaluation)\\\",\\n    \\\"ICLR 2027 (deadline: ~October 2026 — strong target, allows comprehensive evaluation and concurrent work comparison)\\\",\\n    \\\"ICRA 2027 (deadline: ~September 2026 — robotics venue, good fit for empirical contribution)\\\"\\n  ],\\n  \\\"level\\\": \\\"top-tier\\\",\\n  \\\"key_references\\\": [\\n    \\\"Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations [Causal-ACT] (arXiv 2507.22380, July 2025)\\\",\\n    \\\"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling [FTM/FLA] (arXiv 2512.02902, Dec 2025)\\\",\\n    \\\"Learning to Focus: Causal Attention Distillation via Gradient-Guided Token Pruning [LeaF] (NeurIPS 2025, arXiv 2506.07851)\\\",\\n    \\\"Shortcut Learning in Generalist Robot Policies: The Role of Dataset Diversity and Fragmentation (CoRL 2025, arXiv 2508.06426)\\\",\\n    \\\"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem? (ACL Findings 2025, arXiv 2502.11501)\\\",\\n    \\\"When Token Pruning is Worse than Random: Understanding Visual Token Information in VLLMs (ICLR 2026, arXiv 2512.07580)\\\",\\n    \\\"The Risks of Invariant Risk Minimization (ICLR 2021, arXiv 2010.05761)\\\",\\n    \\\"Out-of-Distribution Generalization via Risk Extrapolation [V-REx] (ICML 2021, arXiv 2003.00688)\\\",\\n    \\\"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models (arXiv 2511.15605)\\\",\\n    \\\"AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention (arXiv 2511.18960)\\\",\\n    \\\"ACTIVA: Amortized Causal Effect Estimation via Transformer-based Variational Autoencoder (arXiv 2503.01290)\\\",\\n    \\\"CausalPFN: Amortized Causal Effect Estimation via In-Context Learning (NeurIPS 2025, arXiv 2506.07918)\\\",\\n    \\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026, arXiv 2510.13626)\\\",\\n    \\\"Invariant Causal Imitation Learning for Generalizable Policies [ICIL] (NeurIPS 2021)\\\",\\n    \\\"DTP: A Simple yet Effective Distracting Token Pruning Framework for VLA Models (arXiv 2601.16065, Jan 2026)\\\",\\n    \\\"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models (arXiv 2603.28740, Mar 2026)\\\",\\n    \\\"LightVLA: Towards Efficient VLA Models via Differentiable Token Pruning (ICRA 2026, arXiv 2509.12594)\\\",\\n    \\\"TIES: Beyond Attention Magnitude — Leveraging Inter-layer Rank Consistency for Efficient VLA Models (arXiv 2603.24941, Mar 2026)\\\",\\n    \\\"BFA++: Hierarchical Best-Feature-Aware Token Pruning for Multi-View VLA Models (arXiv 2602.20566, Feb 2026)\\\",\\n    \\\"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation (arXiv 2511.18950)\\\",\\n    \\\"Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation (arXiv 2603.23202, Mar 2026)\\\",\\n    \\\"LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models (arXiv 2604.23950, Apr 2026)\\\",\\n    \\\"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations [RobustVLA] (ICLR 2026, arXiv 2510.00037)\\\",\\n    \\\"Mask World Model: Predicting What Matters for Robust Robot Policy Learning (arXiv 2604.19683, April 2026)\\\",\\n    \\\"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient VLA Inference (arXiv 2511.16449)\\\",\\n    \\\"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for VLA Models (arXiv 2603.22991, March 2026)\\\",\\n    \\\"Learning Invariant Causal Mechanism from Vision-Language Models [CLIP-ICM] (ICML 2025, arXiv 2405.15289)\\\",\\n    \\\"OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport (arXiv 2602.20205)\\\",\\n    \\\"Wasserstein Distributionally Robust Optimization and Variation Regularization (Operations Research, 2024)\\\",\\n    \\\"Finite-Sample Guarantees for Wasserstein DRO: Breaking the Curse of Dimensionality (Operations Research, 2023)\\\",\\n    \\\"Vision Transformers Need More Than Registers (arXiv 2602.22394, Feb 2026)\\\",\\n    \\\"Bounding the Estimation Error of Sampling-based Shapley Value Approximation (arXiv 1306.4265)\\\",\\n    \\\"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success [OpenVLA-OFT] (arXiv 2025)\\\",\\n    \\\"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration (ICLR 2026, arXiv 2506.12723)\\\",\\n    \\\"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning (arXiv 2509.05614)\\\",\\n    \\\"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching (NeurIPS 2025, arXiv 2502.02175)\\\",\\n    \\\"InSpire: Vision-Language-Action Models with Intrinsic Spatial Reasoning (arXiv 2505.13888, May 2025)\\\",\\n    \\\"Causality-Inspired Robustness for Nonlinear Models via Representation Learning [CIRRL] (arXiv 2505.12868, May 2025)\\\",\\n    \\\"Learning to Estimate Shapley Values with Vision Transformers [ViT-Shapley] (ICLR 2023 Oral, arXiv 2206.05282)\\\",\\n    \\\"Mechanistic Interpretability for Steering Vision-Language-Action Models (CoRL 2025, arXiv 2509.00328)\\\",\\n    \\\"Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models [PDF] (arXiv 2604.18107, April 2026)\\\",\\n    \\\"Causal Shapley Values: Exploiting Causal Knowledge to Explain Individual Predictions of Complex Models (NeurIPS 2020, arXiv 2011.01625)\\\"\\n  ],\\n  \\\"description\\\": \\\"VLA models suffer catastrophic failures under visual distribution shifts, yet a proliferation of concurrent token pruning methods (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, Compressor-VLA, Gaze-VLA — all 2025-2026) each propose different heuristic criteria without formal justification, and recent work shows many attention-based methods underperform random selection (arXiv 2502.11501) due to 'vanishing token information' in deep layers (arXiv 2512.07580). We propose Causal Token Selection (CaTS) v3, bridging three disconnected threads: VLA token pruning, causal intervention for imitation learning (Causal-ACT, ICIL), and causal attention distillation (LeaF), while drawing theoretical inspiration from CIRRL's (arXiv 2505.12868) breakthrough showing that representation-level identifiability enables nonlinear causal robustness guarantees. CaTS defines a formal SCM over the VLA token-action pipeline with a revised *encoder-level spatial locality* assumption — grounded in empirical findings that DINOv2/SigLIP encoder outputs preserve spatial correspondence (a form of patch-level identifiability analogous to CIRRL's affine identifiability) while LLM self-attention progressively mixes token information. Key advances over v2: (1) Multi-layer scoring at vision encoder output (where spatial locality is empirically validated) with optional intermediate-layer refinement. (2) Concrete ε-invariance bound with approximate constants: ε = C₁/√M + C₂·exp(-c·N_env/d_E) + C₃·α_leak·g(τ) + ε_amort, with order-of-magnitude estimates (M=200 Shapley samples → estimation error ~0.096; N_env=35 across d_E=7 dimensions → coverage term ~0.01; encoder-level α_leak≈0.1 → locality term ~0.10; overall ε≈0.26, a testable prediction against the observed ~50-65% gap for unmodified VLAs). (3) Honest composite robustness objective combining V-REx (practical heuristic) with Wasserstein DRO (finite-sample guarantees), including explicit analysis of their interaction: complementary for moderate DRO radius ρ (V-REx stabilizes known environments, DRO guards against unseen shifts; for small ρ, Wasserstein DRO approximates variation regularization, aligning with V-REx), with potential conflict at large ρ resolved by operating in the moderate-ρ regime calibrated to LIBERO-Plus perturbation magnitudes. (4) Quantified amortization gap: ε_amort ≤ O(1/√W) + O(1/√n_train) ≈ 0.054 for W=512, n_train=10K, with central validation protocol (Spearman ρ > 0.8). (5) Explicit differentiation from ViT-Shapley (ICLR 2023 Oral) — CaTS's amortized scorer extends the ViT-Shapley paradigm from observational Shapley values for model explanation to interventional causal effects for cross-environment invariance. (6) Acknowledgment that the 'vanishing token information' finding (arXiv 2512.07580) was validated on VLMs, not VLAs — verifying the information horizon in VLA architectures is part of the empirical contribution. (7) Integration with mechanistic interpretability evidence (CoRL 2025) validating that interventional methods identify causal structure in VLA representations, and positioning against test-time adaptation approaches (PDF, arXiv 2604.18107) as complementary training-time vs. test-time methods for the same spurious correlation problem. Formal statistical protocol against random pruning with a priori 5/7 dimension criterion. Evaluated against 8 core baselines (streamlined from 11 with explicit code availability assessment: VLA-Pruner and DTP have public code; TIES is training-free and reimplementable; FTM is trivially reimplementable) including SRPO (82.1% SOTA), DTP, TIES, and VLA-Pruner. Concurrent efficiency-focused methods (SP-VLA ICLR 2026, SpecPrune-VLA, VLA-Cache NeurIPS 2025) are discussed as complementary — targeting temporal/spatial redundancy rather than causal robustness. InSpire (arXiv 2505.13888) is discussed as a complementary prompting-based approach to the same spurious correlation problem. GPU costs updated to current May 2026 market rates ($0.80/hr A100 spot from specialized providers). Primary targets: AAAI 2027 and ICLR 2027.\\\",\\n  \\\"project_name\\\": \\\"causal_token_sel_vla\\\",\\n  \\\"source\\\": \\\"web_research\\\"\\n}\\n```\\n\\n---\\n\\nHere is a summary of all changes integrated into this v4 revision, mapping to the reviewer's 4 issues:\\n\\n**Opportunity field** -- Added ViT-Shapley as a \\\"fourth thread\\\" (amortized Shapley estimation for vision transformers, observational vs. interventional distinction). Added mechanistic interpretability (CoRL 2025) as a fifth thread. Renumbered CIRRL from \\\"fourth\\\" to \\\"sixth thread.\\\"\\n\\n**Landscape field** -- Added three new sections: (1) \\\"Amortized Shapley estimation for vision transformers\\\" covering ViT-Shapley's pipeline, architectural analogy to CaTS, and the observational vs. interventional Shapley distinction with reference to Heskes et al. NeurIPS 2020. (2) \\\"Mechanistic interpretability for VLA\\\" covering the CoRL 2025 paper's activation projection approach, complementarity with CaTS. (3) \\\"Test-time adaptation\\\" covering PDF (arXiv 2604.18107) and its complementary positioning vs. CaTS.\\n\\n**Approach field** -- Added the VLM-not-VLA caveat after the spatial locality justification paragraph, noting that ablation (b) explicitly tests this. Added the \\\"Relationship to ViT-Shapley (ICLR 2023)\\\" subsection in the ACS section. Added two new \\\"vs.\\\" entries in Key differentiations: vs. ViT-Shapley and vs. Mechanistic Interpretability for VLA Steering.\\n\\n**Key references** -- Added all 4 new references: ViT-Shapley, Mechanistic Interpretability for VLA Steering, PDF, and Causal Shapley Values (Heskes et al.).\\n\\n**Description** -- Added points (5), (6), and (7) after \\\"Key advances over v2:\\\" covering ViT-Shapley differentiation, VLM-not-VLA acknowledgment, and mechanistic interpretability/PDF positioning.\\n\\n**Other fields** -- `change_type` set to `\\\"minor\\\"`. All other fields (title, core_problem, resource_estimate, target_venues, level, project_name, source) preserved identically from v3.\"\n  },\n  {\n    \"type\": \"text\",\n    \"text\": \"agentId: ad283643819abe769 (use SendMessage with to: 'ad283643819abe769' to continue this agent)\\n&lt;usage>total_tokens: 94912\\ntool_uses: 31\\nduration_ms: 990140&lt;/usage>\"\n  }\n]",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "4041e574-e9b4-4cde-b753-bfd566e59ec8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 51_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"Causal Token Selection for Invariant VLA Policies via Amortized Interv…",
  "leafUuid": "1b77a948-cee4-4365-a296-b70a13cba601",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise VLA causal token selection with ViT-Shapley differentiation",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82"
}
```

---

### Assistant

_source line 53 · 2026-05-13T06:05:48.779Z_

<details><summary>Logged reasoning block</summary>

```text
The agent produced the complete JSON. Let me verify the key changes are all present and correctly integrated:

1. ViT-Shapley (ICLR 2023 Oral) - ✅ Added to opportunity (4th thread), landscape (new section), approach (relationship subsection + key differentiation), key_references, description
2. Mechanistic Interpretability for VLA Steering (CoRL 2025) - ✅ Added to opportunity, landscape (new section), approach (key differentiation), key_references, description
3. VLM→VLA caveat - ✅ Added in approach after spatial locality justification


4. PDF (arXiv 2604.18107) - ✅ Added to landscape (new section), key_references, description
5. Causal Shapley Values (NeurIPS 2020) - ✅ Added to key_references, referenced in landscape

The change_type is "minor" which is correct. Now I'm extracting the complete JSON from the agent's response.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b77a948-cee4-4365-a296-b70a13cba601",
  "isSidechain": false,
  "requestId": "req_011Caz4iG1ct9Cry97kEgJ2P",
  "type": "assistant",
  "uuid": "52f485dd-7eda-49ea-b880-f05278138bf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FeiZmvKWLtE9bHv2xo1DG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16805,
      "cache_read_input_tokens": 47015,
      "output_tokens": 16525,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16525,
          "cache_read_input_tokens": 47015,
          "cache_creation_input_tokens": 16805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16805
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

_source line 54 · 2026-05-13T06:12:50.220Z_

All four reviewer issues have been researched and integrated. Here's the complete revised JSON:

```json
{
  "title": "Causal Token Selection for Invariant VLA Policies via Amortized Interventional Scoring",
  "change_type": "minor",
  "core_problem": "VLA models learn spurious visual correlations — attending to background textures, lighting conditions, and distractor objects that co-occur with target actions in training data — causing catastrophic failure under visual distribution shifts. Recent work (arXiv 2502.11501, ACL Findings 2025; arXiv 2512.07580, ICLR 2026) reveals two critical findings: (1) many attention-based token pruning methods underperform even naive random selection due to flawed scoring criteria, and (2) visual token information 'vanishes' in deep LLM layers, becoming uniformly uninformative beyond an 'information horizon' — meaning that any token selection must operate before this horizon. Meanwhile, a proliferation of concurrent VLA token selection methods (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, Compressor-VLA, Gaze-VLA — all 2025-2026) each propose different heuristic criteria (attention intersection, cross-attention TopK, Gumbel softmax, Kendall rank consistency, spatio-semantic dual-aware scoring, hierarchical importance, instruction-guided compression, gaze alignment), yet none provide formal justification for why their criterion identifies task-relevant tokens rather than merely attention-salient tokens. A complementary line of work addresses VLA spurious correlations via language-guided spatial reasoning (InSpire, arXiv 2505.13888), redirecting attention through prompting rather than principled token selection. Simple adaptation methods like FTM (arXiv 2512.02902) can recover substantial robustness with only 4K parameters, raising the question: can we identify *why* certain tokens matter and provide interpretable, formally grounded selection criteria rather than black-box affine recalibration?",
  "opportunity": "Three research threads have developed in isolation: (1) causal intervention for imitation learning robustness (Causal-ACT, arXiv 2507.22380; ICIL, NeurIPS 2021), operating at the feature level in smaller architectures, (2) VLA token pruning for efficiency and robustness (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, VLA-Pruner, VLA-IAP, OTPrune, Compressor-VLA, SpecPrune-VLA, VLA-Cache), using attention/gradient/geometric/rank/temporal heuristics without causal grounding, and (3) causal attention distillation (LeaF, NeurIPS 2025) and learnable pruning (LearnPruner, arXiv 2604.23950), which move beyond pure attention heuristics but lack formal causal intervention criteria. A fourth thread — amortized Shapley estimation for vision transformers — demonstrates the feasibility of training a lightweight explainer model to predict per-patch importance scores in a single forward pass (ViT-Shapley, ICLR 2023 Oral, arXiv 2206.05282), but targets observational Shapley values for model explanation rather than interventional causal effects for cross-environment robustness. A fifth thread — mechanistic interpretability work (arXiv 2509.00328, CoRL 2025) — has independently validated that interventional methods can identify causally relevant structure in VLA representations — activation projection identifies sparse semantic directions in OpenVLA and Pi0 that are causally linked to action selection — but operates at the neuron/direction level for behavioral steering rather than the token level for robustness-oriented selection. A sixth thread — causality-inspired robustness theory — has recently achieved a breakthrough: CIRRL (arXiv 2505.12868) provides the first finite-radius robustness guarantee in nonlinear settings by combining identifiable representation learning with anchor regression, showing that operating at the representation level (where latent variables are identifiable up to affine transformation) is the key to extending causal robustness beyond linear models. A critical empirical finding connects these threads to VLA architectures specifically: visual tokens in VLA architectures preserve spatial correspondence to image patches at the vision encoder output (where SigLIP provides semantic and DINOv2 provides spatial features), but this spatial structure degrades progressively through LLM layers due to self-attention mixing, ultimately vanishing at an 'information horizon' (arXiv 2512.07580). This means token-level causal selection must operate at or near the vision encoder output — where spatial locality is preserved by construction — rather than at deep LLM layers where existing attention-based methods struggle (explaining why they often underperform random selection). The vision encoder output provides a form of identifiable representation (spatial correspondence = patch-level identifiability), analogous to CIRRL's requirement for identifiable latent variables, suggesting that representation-level causal robustness can extend to the VLA setting. Formalizing this insight via a structural causal model over the token-action pipeline, with amortized interventional scoring operating at the pre-LLM representation layer, would provide the principled criterion that existing pruning methods lack while operating in the representation space where the criterion is most valid.",
  "landscape": "**Robustness benchmarking**: LIBERO-Plus (arXiv 2510.13626, CVPR 2026) demonstrates VLA catastrophic failures across 7 perturbation dimensions, with the current SOTA at 82.1% average success (SRPO, arXiv 2511.15605) — SRPO achieves 167% improvement over one-shot SFT baseline via self-referential RL without token selection. **Causal approaches in imitation learning**: Causal-ACT (arXiv 2507.22380, July 2025) integrates causal structure learning into ACT by learning binary causal graphs over ResNet features — achieving 0.82 OOD success on ALOHA cube transfer vs. 0.23 for standard ACT. However, it operates at the feature level in small architectures, uses heuristic energy-based graph search, and evaluates on a single simple task. ICIL (NeurIPS 2021) learns domain-invariant features for imitation but not at the token level. CLIP-ICM (ICML 2025) applies causal invariance to VLMs via SCMs but for classification, not action policies. **Spurious correlation mitigation via prompting**: InSpire (arXiv 2505.13888, May 2025) mitigates VLA spurious correlations by boosting spatial reasoning — prepending directional questions ('In which direction is [object] relative to the robot?') to redirect attention to task-relevant features. Achieves +6.2%/+10% on seen/unseen LIBERO tasks for miniVLA-VQ and +25%/+26% in real-world tasks for π0-FAST. Complementary approach (prompting-based attention redirection vs. CaTS's principled token selection); evaluated on standard LIBERO, not LIBERO-Plus perturbation dimensions. **Simple adaptation baselines**: FTM (arXiv 2512.02902) achieves 87.1% on LIBERO viewpoint with just 4K parameters via global affine token modulation; FLA extends to 90.8% with 4.7M parameters. Neither evaluated on full LIBERO-Plus; neither provides interpretability. **Active attention**: AVA-VLA (arXiv 2511.18960) dynamically reweights visual tokens via active attention, achieving 74.7% on LIBERO-Plus. **Causality-inspired robustness theory**: CIRRL (arXiv 2505.12868, May 2025) provides the first causality-inspired finite-radius robustness guarantee in nonlinear settings, using identifiable representation learning (Distributional Principal Autoencoders) to recover latent variables up to affine transformation, then applying anchor regression in the identifiable latent space. Key theorem: the two-step estimator achieves optimal worst-case risk among all L²-integrable functions under elliptical noise. Directly relevant to CaTS's theoretical framework — CIRRL validates the principle that representation-level causal robustness can overcome IRM/V-REx limitations, though its elliptical distribution assumptions and tabular data focus limit direct application to high-dimensional VLA visual tokens. CaTS's encoder-level scoring operates at a representation layer where spatial identifiability holds (analogous to CIRRL's affine identifiability), providing an empirical bridge between CIRRL's theory and VLA practice. **Amortized Shapley estimation for vision transformers**: ViT-Shapley (ICLR 2023 Oral, arXiv 2206.05282) trains a separate explainer model to predict per-patch Shapley values in a single forward pass, using a three-stage pipeline: (1) train ViT classifier, (2) fine-tune a surrogate with attention masking to handle partial inputs, (3) train the explainer to amortize Shapley computation. The explainer produces 196 per-patch importance scores (14×14 grid) and outperforms attention rollout, GradCAM, and LRP for ViT explanation. Publicly available code (github.com/suinleelab/vit-shapley). CaTS's amortized causal scoring head is architecturally analogous — both train a lightweight model to predict per-token importance from embeddings in a single forward pass. The critical difference: ViT-Shapley estimates observational Shapley values (how much does masking patch i change the model's prediction?) for post-hoc explanation of a fixed model on a single distribution, while CaTS estimates interventional causal effects (how much does replacing token i with environment-marginal statistics change action predictions across environments?) for cross-environment invariance during training. This distinction parallels the broader observational vs. interventional Shapley literature (Heskes et al., NeurIPS 2020): observational Shapley captures feature relevance within a distribution, while interventional Shapley captures causal influence robust to distribution shift. CaTS's intervention mechanism (environment-marginal replacement across LIBERO-Plus perturbation dimensions) is specifically designed to distinguish causal from spuriously correlated tokens — a distinction that observational Shapley cannot make when spurious correlations are present in the training distribution. ViT-Shapley's attention masking approach for evaluating ViTs with partial information is directly applicable to CaTS's intervention mechanism and informs implementation. **Mechanistic interpretability for VLA**: Mechanistic interpretability for VLA steering (CoRL 2025, arXiv 2509.00328) projects feedforward activations onto the token embedding basis to identify sparse semantic directions — such as speed and direction — that are causally linked to action selection in OpenVLA and Pi0. Enables zero-shot behavioral steering on LIBERO and real UR5 robot without fine-tuning. This validates CaTS's core premise: interventional methods can identify causally relevant structure in VLA representations. Key differentiation: operates at the neuron/direction level for behavioral steering (which directions in activation space control speed/direction?), while CaTS operates at the token level for robustness-oriented selection (which input patches contain causal vs. spurious visual information?). The two approaches are complementary — mechanistic interpretability explains how VLA representations encode action semantics, while CaTS identifies which visual tokens should feed into those representations for cross-environment robustness. **Test-time adaptation for VLA robustness**: PDF (arXiv 2604.18107, April 2026) addresses VLA spurious correlations ('trajectory overfitting where VLAs over-attend to spurious correlation between actions and entities') via test-time perturbation learning with delayed feedback. Uses uncertainty-based data augmentation and action voting without fine-tuning, achieving +7.4% on LIBERO. Complementary to CaTS: PDF is a test-time adaptation method that corrects overconfident action predictions post-hoc, while CaTS is a training-time causal selection method that prevents spurious correlations from entering the policy. The two could be combined — CaTS for principled token selection during training, PDF for residual correction at test time. **Concurrent VLA token pruning/selection methods (2025-2026) — all using heuristic criteria**: (i) SP-VLA (arXiv 2506.12723, ICLR 2026) jointly addresses temporal and spatial redundancy via action-aware model scheduling (switching between VLA and lightweight generator for deliberative vs. intuitive actions) and spatio-semantic dual-aware token pruning. Achieves 1.5× lossless acceleration on LIBERO and 2.4× on SimplerEnv with up to 6% performance gain. As an ICLR 2026 accepted paper, it represents the strongest efficiency-focused VLA pruning method. However, its spatio-semantic scoring criterion is designed for efficiency (removing redundant tokens) rather than robustness (removing spuriously correlated tokens) — a token may be spatially/semantically important yet causally spurious (e.g., a distinctive background element near the target object). Not evaluated under distribution shift. Code available on GitHub. (ii) DTP (arXiv 2601.16065, Jan 2026) prunes 'distracting tokens' via attention intersection scoring — tokens in task-irrelevant regions exceeding a scaled threshold of the maximum attention in task-relevant regions are pruned. Evaluated on SIMPLER, not LIBERO-Plus. Directly analogous motivation to CaTS (removing spuriously correlated tokens), but uses attention heuristics without formal justification that attention-salient ≠ causally relevant. Code available. (iii) FocusVLA (arXiv 2603.28740, Mar 2026) uses cross-attention-based TopK patch selection with modality cascaded attention, achieving 98.7% on standard LIBERO. Not evaluated on LIBERO-Plus; assumes cross-attention scores identify task relevance without causal validation. (iv) LightVLA (arXiv 2509.12594, ICRA 2026) uses Gumbel softmax for differentiable token selection, reducing FLOPs by 59.1% with 2.9% success rate improvement on LIBERO. End-to-end learned selection but criterion is implicitly defined by task loss — no interpretability or formal robustness criterion. (v) TIES (arXiv 2603.24941, Mar 2026) introduces Kendall rank consistency across layers as a stability metric, improving average success by 6% on CogACT+SIMPLER while reducing tokens by 78%. Most relevant concurrent work: uses rank consistency as a robustness signal, but this is a statistical regularity heuristic, not a causal criterion — rank consistency does not distinguish causal from spuriously consistent tokens. Not evaluated under environmental perturbations. (vi) BFA++ (arXiv 2602.20566, Feb 2026) uses hierarchical intra-view and inter-view importance predictors for multi-view VLAs. (vii) Compressor-VLA (arXiv 2511.18950) uses instruction-guided semantic and spatial compression modules, reducing visual tokens by 3× on LIBERO. (viii) Gaze-Regularized VLA (arXiv 2603.23202, Mar 2026) aligns attention with human gaze heatmaps via KL divergence. Requires human gaze data; provides indirect causal signal. (ix) LearnPruner (arXiv 2604.23950, Apr 2026) trains a learnable pruning module after the vision encoder, retaining only 5.5% of tokens while preserving ~95% performance. (x) SpecPrune-VLA (arXiv 2509.05614) uses action-aware self-speculative pruning with global history context, combining static action-level and dynamic layer-level pruning with an action-aware controller that classifies actions as coarse/fine-grained. Achieves 1.57× speedup on LIBERO and 1.70× in real-world with negligible degradation. Primarily efficiency-focused, exploiting temporal redundancy. (xi) VLA-Cache (arXiv 2502.02175, NeurIPS 2025) adaptively caches and reuses static visual tokens across consecutive frames via layer-adaptive token reusing, achieving 1.7× speedup with negligible success rate loss. Exploits temporal redundancy between adjacent observations — complementary to CaTS which addresses spatial token selection within a single frame for robustness rather than efficiency. **Token information dynamics**: arXiv 2512.07580 (ICLR 2026) discovers 'vanishing token information' — visual tokens progressively lose discriminative salience in deep LLM layers, becoming uniformly uninformative beyond an 'information horizon' (~layer 20 for general tasks, deeper for OCR). This explains why attention-based pruning in late layers underperforms random selection and motivates scoring at early/intermediate layers where spatial information is preserved. **Token pruning critique**: arXiv 2502.11501 (ACL Findings 2025) systematically shows many attention-based pruning methods underperform random selection due to position bias and flawed attention-as-importance assumptions. **Causal token pruning in NLP**: LeaF (NeurIPS 2025, arXiv 2506.07851) uses gradient-based teacher-student comparison to identify confounding tokens. Analogous in spirit but targets LLM reasoning, not embodied action; uses gradient heuristics, not formal interventions. **Robustness training**: RobustVLA (ICLR 2026, arXiv 2510.00037) uses offline robust optimization with 12.6% absolute gains on π0 backbone. **World models**: Mask World Model (arXiv 2604.19683) achieves 98.3% on standard LIBERO via geometric information bottleneck but not evaluated on LIBERO-Plus. **Shortcut learning**: arXiv 2508.06426 (CoRL 2025) identifies dataset diversity as root cause — complementary data-side approach. **Invariance theory limitations**: Rosenfeld et al. (ICLR 2021) demonstrate IRM fails in non-linear settings. V-REx (Krueger et al., ICML 2021) proposes variance-based risk extrapolation as simpler alternative but suffers similar non-linear limitations. CIRRL (arXiv 2505.12868) overcomes these limitations via identifiable representation learning but requires elliptical distribution assumptions. Wasserstein DRO (Kuhn et al., 2024) provides genuine finite-sample guarantees without requiring linear/invariance assumptions. **Amortized causal estimation**: CausalPFN (NeurIPS 2025) demonstrates amortized causal effect estimation via in-context learning with asymptotic consistency guarantees; ACTIVA (arXiv 2503.01290) uses transformer-based VAEs but is limited to tabular data. Amortized Shapley estimation (SurroShap, SimSHAP) provides non-asymptotic convergence bounds: Pr(|ϕ̂ − ϕ| ≥ ε) ≤ 2·exp(−2mε²/r²) for m samples and marginal contribution range r (Maleki et al., 2013). **No existing work combines formal token-level causal intervention criteria with amortized estimation in VLA transformers, operating at the vision encoder output where spatial locality is empirically validated, for cross-environment policy invariance.**",
  "approach": "We propose Causal Token Selection (CaTS) v3, which identifies and retains visual tokens whose causal effect on action predictions is significant and stable across visual environments, using an amortized interventional scoring framework operating at the vision encoder output where spatial locality is empirically grounded.\n\n**Formal SCM for VLA Token-Action Pipeline.** We define a structural causal model: observation O is processed by the vision encoder into T(O) = {t_1,...,t_N} (N=256 for OpenVLA's SigLIP+DINOv2 encoder); each token t_i corresponds to an image patch and carries causal content C_i (object geometry, gripper state, contact regions) and spurious content S_i (background texture, lighting, distractor appearance); environment variable E influences S_i but not C_i; action A = π(f(T)) where f is the LLM backbone. We formalize the *encoder-level spatial locality* assumption (revised from the original spatial locality assumption): at the vision encoder output — before LLM self-attention layers mix token representations — causal content C_i is concentrated in a subset T* ⊂ T corresponding to image patches containing task-relevant objects, while spurious content S_i is distributed across patches containing background and distractors. **Justification**: this is grounded in two empirical findings: (a) DINOv2's attention maps show foreground object concentration by layers 3-6, with the CLS token primarily aggregating foreground tokens (arXiv 2602.22394); (b) the 'vanishing token information' phenomenon (arXiv 2512.07580) confirms that spatial discriminability is maximal at the vision encoder output and degrades through LLM depth. **Important caveat**: arXiv 2512.07580 evaluates VLMs (Qwen2.5-VL, LLaVA-1.5), not VLAs. While VLAs share the VLM backbone architecture making extrapolation reasonable, VLA models have different training objectives (action prediction vs. text generation) and potentially different attention patterns — action tokens may attend to visual tokens differently than text tokens. The information horizon position may differ for VLAs. Verifying the information horizon in VLA architectures is an explicit part of our empirical contribution (ablation b: encoder-level vs. intermediate-layer vs. late-layer scoring directly tests where spatial information degrades in VLA models). By scoring at the encoder output, CaTS operates precisely where the assumption is most valid, unlike methods scoring at deep LLM layers where information mixing undermines spatial selectivity. This encoder-level identifiability is analogous to CIRRL's (arXiv 2505.12868) key insight that robustness guarantees extend to nonlinear settings when operating on identifiable representations — the vision encoder's spatial correspondence provides patch-level identifiability that enables causal reasoning at the token level.\n\n**Multi-Layer Scoring Architecture.** Rather than scoring tokens at a single layer (where the spatial locality / information quality tradeoff is unclear), CaTS employs a two-stage scoring approach: (1) *Primary scoring* at the vision encoder output (post-MLP projection, pre-LLM), where spatial locality is strongest. (2) *Optional refinement scoring* at an intermediate LLM layer (before the information horizon, empirically determined per-model via the protocol of arXiv 2512.07580 — typically layer 8-15 for 7B models), capturing cross-modal relevance signals that emerge only after some language-vision interaction. The two scores are combined via a learned convex combination α·s_encoder + (1-α)·s_intermediate, where α is a learnable scalar. **Degradation analysis**: we formally analyze how the ε-invariance bound degrades as spatial locality weakens (parameterized by α_leak = fraction of causal information C_i that 'leaks' to non-corresponding tokens through self-attention). When α_leak is high (poor spatial locality at the scoring layer), the bound degrades gracefully — the theory predicts diminishing returns of causal selection over random pruning, which is empirically testable.\n\n**Theorem (Conditional Invariance) with Approximate Constants.** Under four assumptions — (A1) causal sufficiency: A ⊥ E | C(T*); (A2) token-level identifiability: do(t_i) changes C(T*) with positive probability for t_i ∈ T*; (A3) environment diversity: training environments span relevant E dimensions; (A4) bounded amortization error of the causal scorer — the causal token selection operator S_τ with threshold τ satisfies:\n\n*Concrete bound*: max_{e,e'} |R(π,e) - R(π,e')| ≤ ε(N_env, M, τ, α_leak) where:\nε = C₁/√M + C₂·exp(-c·N_env/d_E) + C₃·α_leak·g(τ) + ε_amort\n\n**Approximate constant estimates (order-of-magnitude):**\n\n- *C₁/√M (Shapley estimation error)*: Using the Hoeffding-based bound from Maleki et al. (2013): Pr(|ϕ̂ − ϕ| ≥ ε) ≤ 2·exp(−2Mε²/r²), where r is the range of marginal contributions. With action loss normalized to [0,1] (r=1) and confidence δ=0.05: C₁ = r·√(ln(2/δ)/2) ≈ 1.36. With M=200 Shapley samples per token: C₁/√M ≈ 0.096. With M=500: ≈ 0.061. **Practical implication**: M=200 samples (200 forward passes per scored token, feasible with batch inference) yields estimation error below 0.1, sufficient for reliable token ranking.\n\n- *C₂·exp(-c·N_env/d_E) (environment coverage gap)*: d_E ≈ 7 for LIBERO-Plus's 7 perturbation dimensions (camera, robot, language, light, background, noise, layout). With N_env = 35 distinct environments (7 dimensions × 5 perturbation levels each) and c ≈ 0.5-1.0 (standard covering-number scaling for bounded domains): exp(-c·35/7) = exp(-2.5 to -5.0) ≈ 0.007-0.082. With C₂ ≈ 1 (bounded loss): this term contributes ≈ 0.01-0.08. **Practical implication**: 35 environments across 7 dimensions make this term small; the bound suggests N_env = Ω(d_E · log(1/δ)) ≈ 21 environments suffice for δ=0.05, which LIBERO-Plus comfortably exceeds.\n\n- *C₃·α_leak·g(τ) (spatial locality violation)*: α_leak is empirically measurable — at the vision encoder output, we estimate α_leak ≈ 0.05-0.15 (based on DINOv2's foreground concentration in layers 3-6, arXiv 2602.22394); at intermediate LLM layer ~10, α_leak ≈ 0.3-0.5; beyond the information horizon (layer 20+), α_leak → 1.0. With g(τ) ≈ (1-τ)/τ for pruning ratio τ and C₃ ≈ 1: at encoder output with τ=0.5 (50% pruning), C₃·α_leak·g(τ) ≈ 0.1·1.0 = 0.10. At layer 20+ with α_leak ≈ 1.0: this term ≈ 1.0, dominating the bound and explaining why late-layer pruning degenerates to random selection.\n\n- *ε_amort (amortization gap)*: ε_amort ≤ ε_approx(W,d) + ε_stat(n_train). For a 2-layer MLP scorer with W=512 hidden units on d=1024-dimensional token embeddings: ε_approx = O(1/√W) ≈ 0.044 (for Barron-class functions); ε_stat = O(1/√n_train) ≈ 0.01 for n_train=10,000 training interventions. Total ε_amort ≈ 0.054.\n\n**Overall bound estimate**: At the vision encoder output with M=200, N_env=35, α_leak=0.1, τ=0.5: ε ≈ 0.096 + 0.01 + 0.10 + 0.054 ≈ 0.26. This predicts a maximum cross-environment performance gap of ~26% — a testable prediction against the empirically observed ~50-65% gap for unmodified VLAs on LIBERO-Plus. The bound tightens substantially with M=500 (ε ≈ 0.22) and with higher pruning threshold τ=0.7 (ε ≈ 0.20).\n\n**Full proof strategy**: The proof proceeds in three steps: (1) show that under A1-A2, exact token-level ACE identifies T* (follows from standard do-calculus); (2) bound the approximation error when ACE is estimated from M samples via Shapley decomposition (using Hoeffding-type concentration on bounded action losses, directly applying the non-asymptotic bound from Maleki et al., 2013); (3) bound the error from amortizing the Shapley estimates via a neural network (using universal approximation for Barron-class functions + Rademacher complexity of the MLP hypothesis class). Step (3) yields the ε_amort term.\n\n**Failure modes (explicit with analysis):** (F1) Insufficient environment diversity violates A3 — same limitation as IRM/V-REx, partially addressed by CIRRL's identifiable representation approach but CIRRL requires elliptical distribution assumptions that may not hold for VLA visual tokens. Mitigation: LIBERO-Plus provides 7 perturbation dimensions with ~35 environments; we report per-dimension results to identify which dimensions have sufficient diversity. (F2) Spatial locality violation at scoring layer (high α_leak). Mitigation: multi-layer scoring allows operating at the layer with lowest α_leak; we empirically measure α_leak by comparing per-token ACE computed at encoder output vs. intermediate LLM layers. (F3) Amortization gap (see detailed analysis below). (F4) V-REx variance penalty limitations in non-linear settings — see honest framing below.\n\n**Amortized Causal Scoring (ACS) with Quantified Amortization Gap.** We train a lightweight causal scoring head attached to the frozen VLA backbone. Training data is generated via *batch stochastic interventions*: for randomly sampled token subsets across LIBERO-Plus perturbation environments, we replace token embeddings with environment-marginal statistics and measure KL divergence in action distributions. A Shapley-value-inspired decomposition attributes group effects to individual tokens. The scorer (2-layer MLP with width 512, <1M parameters) learns to predict token-level causal effects from token embeddings.\n\n**Relationship to ViT-Shapley (ICLR 2023)**: CaTS's amortized scoring architecture draws on the ViT-Shapley paradigm of training a separate model to predict per-token importance in a single forward pass. However, CaTS departs in three key ways: (a) the scoring target is interventional causal effects computed via environment-marginal token replacement across LIBERO-Plus perturbation dimensions, not observational Shapley values computed via masking on a single distribution; (b) the surrogate stage uses multi-environment intervention data rather than random masking, training the scorer to predict action distribution stability across environments rather than prediction change under masking; (c) the scorer is integrated into a training-time robustness objective (composite V-REx + DRO loss), not used for post-hoc explanation. ViT-Shapley's attention masking approach for evaluating ViTs with partial information informs our intervention mechanism — we adapt their masking strategy to implement environment-marginal token replacement, replacing masked tokens with marginal statistics pooled across perturbation environments rather than zeroing them out.\n\n**Amortization gap analysis**: The gap between the learned scorer s_θ(t_i) and the true ACE(t_i) is bounded by: ε_amort ≤ ε_approx(W, d) + ε_stat(n_train) where ε_approx(W, d) = O(1/√W) ≈ 0.044 for W=512 (for Barron-class functions on compact domains), and ε_stat(n_train) = O(1/√n_train) ≈ 0.01 for n_train=10,000 training interventions. **Central validation protocol** (not merely an ablation): we compute exact ACE on a validation set of 50 tokens × 5 environments (250 forward passes per token = 12,500 total, feasible) and report: (a) Pearson/Spearman correlation between s_θ and exact ACE; (b) mean absolute error; (c) rank agreement (does s_θ rank tokens in the same order as exact ACE?). The amortized scorer is considered validated if rank-order Spearman ρ > 0.8 and the scoring threshold τ selects a token set overlapping ≥ 85% with the exact-ACE-selected set. If validation fails, we fall back to exact ACE computation at inference (trading efficiency for correctness), which remains a viable contribution.\n\n**Composite Robustness Objective (honest framing with V-REx/DRO interaction analysis).** We do NOT claim to solve the non-linear invariance problem. Instead, we use a *composite robustness objective* combining three components: (1) Standard action prediction loss on selected tokens: L_task = E_e[L(π(S_τ(T)), a*)]. (2) V-REx-style variance penalty: L_var = Var_e(L(π(S_τ(T)), a*)), which penalizes cross-environment loss variance. We frame this honestly as a *practical heuristic* that is simpler and more stable than IRMv1 (Krueger et al., ICML 2021) but shares the same fundamental limitation in non-linear settings: it does not distinguish between underfitting and inherent noise, and can fail under heteroskedastic environments. (3) Wasserstein DRO regularization: L_DRO = sup_{Q: W(Q,P̂)≤ρ} E_Q[L], providing finite-sample robustness guarantees (Kuhn et al., 2024) that do not require linear assumptions.\n\n**V-REx and DRO interaction analysis.** The two regularizers target complementary failure modes but can interact non-trivially. *When complementary*: V-REx stabilizes performance across *known* training environments by penalizing loss variance — preventing environment-specific overfitting where the model excels in one environment but fails in others. DRO provides robustness to *unseen* environments within the Wasserstein ball — guarding against distributional shift at test time. Together, they create a 'robust-within-uniform' objective: the policy must perform uniformly across training environments (V-REx) while being robust to perturbations of each environment's distribution (DRO). *When potentially conflicting*: DRO with large radius ρ may concentrate model capacity on worst-case distributions, potentially increasing cross-environment variance to better handle the hardest cases — precisely what V-REx penalizes. *Resolution*: for small-to-moderate DRO radius ρ, Wasserstein DRO is equivalent to variation regularization (Kuhn et al., 2024), making the two objectives approximately aligned. In practice, we operate with moderate ρ where the Wasserstein ball captures realistic perturbations (calibrated to LIBERO-Plus perturbation magnitudes) rather than adversarial worst cases. The sensitivity analysis (ablation c) explicitly measures the V-REx/DRO tradeoff by sweeping λ_var and λ_DRO independently and jointly, reporting both average performance and cross-environment variance to identify the Pareto frontier. We note that CIRRL (arXiv 2505.12868) offers a principled alternative — identifiable representation learning followed by anchor regression — that avoids the V-REx/DRO tension entirely, but requires elliptical distribution assumptions that we cannot verify for VLA visual tokens; adapting CIRRL's framework to VLA architectures is an important direction for future work.\n\nThe combined loss is L = L_task + λ_var·L_var + λ_DRO·L_DRO, where λ_var and λ_DRO are hyperparameters with explicit sensitivity analysis. We expect V-REx to provide better empirical performance in practice (as observed in prior work) while DRO provides the theoretical safety net.\n\n**Architecture.** Frozen OpenVLA-OFT backbone (7B). The ACS head operates at the vision encoder output (post-projection), with optional refinement at an intermediate LLM layer. Total trainable parameters: ACS scoring head (~0.5M) + thin LoRA adaptation (~3.5M) = ~4M total. At inference, the scorer assigns causal scores to all visual tokens in a single forward pass; tokens below threshold τ are pruned before entering the LLM backbone, providing both robustness and efficiency.\n\n**Evaluation with Formal Statistical Protocol.** Primary benchmark: LIBERO-Plus across all 7 perturbation dimensions. Primary metric: average success rate under distribution shift.\n\n**Statistical protocol against random pruning** (addressing arXiv 2502.11501's findings): We adopt a paired bootstrap protocol with bias-corrected accelerated (BCa) confidence intervals and sign-flip permutation tests (following arXiv 2511.19794). Specifically: (a) train CaTS and random-pruning variants under identical conditions with 5 random seeds; (b) record per-seed, per-task success rate differences; (c) compute BCa 95% confidence intervals on the mean difference; (d) perform sign-flip permutation test (10,000 permutations) for each perturbation dimension. CaTS claims significant improvement only if the BCa interval lies entirely above zero AND the permutation p-value < 0.05. *A priori success criterion*: CaTS must significantly outperform random pruning on at least 5 of 7 perturbation dimensions. If this criterion is not met, we report the negative result transparently and analyze which perturbation types resist causal selection (contributing understanding of when causal criteria matter vs. when random suffices).\n\n**Baselines (8 core, with code availability assessment).** We streamline from 11 to 8 core baselines, prioritizing those with available code or reproducible implementations on LIBERO-Plus, and dropping baselines requiring non-trivial cross-architecture adaptation:\n\n(1) SRPO (arXiv 2511.15605) — current LIBERO-Plus SOTA (82.1%). Evaluated in original LIBERO-Plus paper; results directly comparable. (2) FTM/FLA (arXiv 2512.02902) — simple adaptation baseline. Reproduced on LIBERO-Plus; FTM requires only 4K trainable parameters, making reproduction straightforward even without official code (single affine transform layer). (3) AVA-VLA (arXiv 2511.18960) — active visual attention, 74.7% on LIBERO-Plus. Already evaluated on LIBERO-Plus in original work. (4) RobustVLA (ICLR 2026, arXiv 2510.00037) — offline robust optimization, directly targets VLA robustness. ICLR 2026 accepted, code expected. (5) DTP (arXiv 2601.16065) — most directly analogous concurrent work (attention-based distractor identification). Code available at anonymous repository. Requires adaptation to LIBERO-Plus (originally evaluated on SIMPLER). (6) TIES (arXiv 2603.24941) — most sophisticated heuristic baseline (inter-layer rank consistency). Code availability: pending. Method is training-free and well-specified, making reimplementation feasible. (7) VLA-Pruner (arXiv 2511.16449) — temporal-aware dual-level pruning. Code available on GitHub (MINT-SJTU/VLA-Pruner). (8) Random token pruning — critical control baseline, trivial to implement.\n\n**Baselines discussed but not reproduced (with justification)**: Causal-ACT (feature-level ResNet+ACT architecture → token-level OpenVLA adaptation requires non-trivial architectural changes beyond a fair comparison). LeaF-adapted (NLP reasoning → VLA action policies requires speculative adaptation with unclear design choices). FocusVLA, LightVLA, BFA++, Compressor-VLA (not evaluated on LIBERO-Plus; codebases target different VLA architectures). SP-VLA, SpecPrune-VLA, VLA-Cache (efficiency-focused methods exploiting temporal redundancy; not evaluated under distribution shift; complementary rather than competing with CaTS's robustness objective). InSpire (prompting-based approach, orthogonal mechanism targeting same problem; could be combined with CaTS in future work). PDF (test-time adaptation approach; complementary rather than competing — could be combined with CaTS). These are all discussed in the landscape section with explicit differentiation.\n\n**Ablations**: (a) amortized vs. exact ACE (central validation, not just ablation); (b) encoder-level vs. intermediate-layer vs. late-layer scoring (testing spatial locality assumption directly, and implicitly verifying the VLM-derived information horizon finding in VLA architectures); (c) V-REx only vs. DRO only vs. composite objective (including joint λ_var × λ_DRO sensitivity sweep to characterize the interaction frontier and identify the complementary vs. conflicting regime); (d) variance penalty weight sensitivity; (e) DRO radius ρ sensitivity (calibrated against LIBERO-Plus perturbation magnitudes); (f) pruning ratio sweep (10-90%); (g) per-perturbation-dimension analysis; (h) causal score interpretability analysis (do high-scoring tokens correspond to task-relevant regions via IoU with ground-truth object masks?); (i) α_leak measurement across layers.\n\n**Key differentiations from all concurrent work.** The central claim is not merely that causal criteria exist, but that they provide *measurably better token selection than heuristic alternatives* — the burden of proof is on CaTS, and the evaluation is designed to test this rigorously.\n\nvs. ViT-Shapley (ICLR 2023): CaTS's amortized scorer is architecturally analogous to ViT-Shapley's learned explainer — both predict per-token importance from embeddings in one forward pass. The fundamental difference is the scoring target: ViT-Shapley estimates observational Shapley values for explaining a model's predictions within a single distribution; CaTS estimates interventional causal effects across environments to identify tokens whose influence on actions is invariant to visual distribution shifts. Observational Shapley values cannot distinguish causal from spuriously correlated tokens when both correlate with the outcome in the training distribution. CaTS's environment-marginal replacement directly probes cross-environment invariance, providing the causal grounding that ViT-Shapley's masking-based approach lacks.\n\nvs. Mechanistic Interpretability for VLA Steering (CoRL 2025): Both use interventional methods on VLA representations. The steering work identifies neuron-level semantic directions (speed, direction) for zero-shot behavioral control; CaTS identifies token-level causal importance for robustness under visual distribution shift. Complementary: steering explains internal action semantics, CaTS determines which visual inputs matter.\n\nvs. SP-VLA (ICLR 2026): SP-VLA jointly optimizes temporal scheduling and spatial token pruning for efficiency — its spatio-semantic criterion identifies tokens that are spatially/semantically redundant but not necessarily causally spurious. A background token near the target object may have high spatio-semantic importance (spatially close, semantically related to the scene) yet be causally irrelevant to the action. CaTS's interventional criterion tests causal relevance directly via environment-marginal replacement. The two approaches are potentially complementary: SP-VLA for temporal efficiency, CaTS for causal robustness within each selected frame.\n\nvs. DTP (arXiv 2601.16065): DTP uses attention intersection heuristics (tokens in irrelevant regions with attention exceeding scaled threshold are pruned). CaTS uses formal causal intervention criteria. DTP's attention-based scoring is exactly the type shown to be unreliable by arXiv 2502.11501; CaTS's causal scoring is designed to be the principled alternative. Empirical comparison on LIBERO-Plus will directly test whether causal grounding outperforms attention-based distractor identification.\n\nvs. FocusVLA (arXiv 2603.28740): FocusVLA uses cross-attention TopK selection + modality cascaded attention, achieving strong results on standard LIBERO (98.7%) but without robustness evaluation. CaTS targets robustness under distribution shift specifically. FocusVLA's TopK is a differentiable selection mechanism but provides no criterion for *which* tokens matter for cross-environment generalization.\n\nvs. LightVLA (arXiv 2509.12594): LightVLA learns token selection end-to-end via Gumbel softmax — the selection criterion is implicitly defined by the training loss and may overfit to spurious correlations in training environments. CaTS's explicit causal criterion is designed to prevent exactly this overfitting.\n\nvs. TIES (arXiv 2603.24941): TIES uses inter-layer rank consistency (Kendall τ) as a stability signal — an innovative heuristic that captures token 'reliability' across layers. However, rank consistency does not distinguish between causally relevant tokens and tokens that are consistently spurious (e.g., a distinctive background element present in all training scenes would have high rank consistency but is causally irrelevant). CaTS's interventional scoring directly tests causal relevance via environment-marginal replacement.\n\nvs. InSpire (arXiv 2505.13888): InSpire redirects VLA attention via language prompting (spatial reasoning questions), achieving an indirect form of spurious correlation mitigation without token-level selection. CaTS operates at the token level with formal causal criteria. The two approaches are complementary — InSpire provides a zero-cost attention redirect while CaTS provides principled token selection with theoretical guarantees. Future work could combine InSpire's spatial prompting with CaTS's causal scoring.\n\nvs. PDF (arXiv 2604.18107): PDF addresses the same spurious correlation problem via test-time perturbation learning with delayed feedback — a post-hoc correction approach. CaTS is a training-time causal selection method that prevents spurious correlations from entering the policy. The two are complementary and could be combined: CaTS for principled token selection during training, PDF for residual correction at test time.\n\nvs. CIRRL (arXiv 2505.12868): CIRRL provides finite-radius nonlinear robustness via identifiable representation learning, but operates on tabular data with elliptical distribution assumptions. CaTS draws theoretical inspiration from CIRRL's key insight (representation-level identifiability enables causal robustness) while adapting to the VLA setting where visual encoder outputs provide spatial patch-level identifiability. CaTS's DRO component provides analogous finite-sample guarantees without requiring elliptical assumptions.\n\nvs. Gaze-VLA (arXiv 2603.23202): Uses human gaze as an indirect causal signal (humans look at task-relevant regions). Requires gaze data collection; gaze provides a noisy proxy for causal relevance (humans also look at salient distractors). CaTS derives causal relevance from the model's own action predictions under intervention.\n\nvs. Causal-ACT (arXiv 2507.22380): Token-level in 7B VLA (not feature-level in ResNet+ACT); amortized scoring (not heuristic graph search); comprehensive LIBERO-Plus evaluation; concrete ε-invariance bound with approximate constants.\n\nvs. FTM: Interpretable per-token causal scores (not black-box affine transform); selective token removal (not global recalibration); formal robustness criterion.\n\nvs. LeaF (NeurIPS 2025): VLA action policies (not NLP reasoning); cross-environment interventional scoring (not single-domain gradient heuristics); formal SCM (not teacher-student comparison).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~800h A100 (80GB): ~350h for 22-28 LoRA fine-tuning runs with ACS head at ~14h each (including multi-layer scoring variants and composite objective hyperparameter search), ~250h for batch intervention data generation, amortized scorer training, and exact ACE validation (12,500 forward passes for validation set + systematic coverage across 7 perturbation types), ~200h for baseline reproduction (DTP and TIES reproduction on LIBERO-Plus, FTM on LIBERO-Plus, 8 baselines total with 5 seeds each for statistical protocol) and ablations",
      "gpu_utilization": "Low (~25-30%). GPUs sit idle during code development, causal scoring pipeline debugging, statistical protocol implementation, α_leak measurement analysis, and theorem proof development.",
      "timeline": "4-6 months",
      "team": "1-2 researchers (one with causal inference/DRO background for theorem formalization and proof, one with VLA/robotics experience for implementation and evaluation)",
      "estimated_gpu_cost": "~$640 (800h × $0.80/hr A100 spot/discount pricing from specialized providers such as Thunder Compute or TensorDock, May 2026 market rate; range $0.78-$1.07/hr across providers)"
    },
    "human_in_loop": {
      "gpu_hours": "~1200h A100 (80GB): agent explores ~40-50 training configurations more systematically, runs comprehensive ablations across all 7 perturbation dimensions with 5 seeds, evaluates all 8 baselines, and performs extensive α_leak measurements across layers",
      "gpu_utilization": "Moderate (~50-60%). Agent queues experiments faster but pauses at approval gates for: multi-layer scoring architecture decisions, DRO radius selection, amortization validation thresholds, theorem assumption checking.",
      "timeline": "2-4 months",
      "team": "1 researcher, ~45min/day check-in for approving experiment plans, reviewing causal score visualizations, validating amortization gap measurements, and verifying theorem proof steps",
      "claude_api_cost": "$500-700 (5000-7000 conversation turns for experiment design, code generation, theorem checking, statistical protocol implementation, result analysis)",
      "estimated_gpu_cost": "~$960 (1200h × $0.80/hr)",
      "risk_note": "Amortized scorer validation (Spearman ρ > 0.8 threshold) requires careful human judgment — if the scorer barely misses the threshold, the decision to proceed with amortized vs. exact scoring has significant downstream implications. DRO radius selection and the V-REx/DRO tradeoff require human expertise. Theorem proof needs verification by someone with expertise in both causal inference and approximation theory."
    },
    "auto_research": {
      "gpu_hours": "~2500h A100 (80GB): agent runs 120-150 experiment configurations including aggressive sweeps for scoring layer selection, V-REx/DRO weight ratios, pruning ratios, Shapley approximation methods, scorer architectures (varying width W), plus all baseline reproductions with 5 seeds and failed exploration runs",
      "gpu_utilization": "High (~90%+). Agent queues next experiment immediately upon completion. Continuous 24/7 execution.",
      "timeline": "3-5 weeks with 4-8 concurrent A100s; as few as 8-10 days with 16 concurrent GPUs",
      "team": "0 (initial setup: configure LIBERO-Plus environments, OpenVLA-OFT checkpoint, define intervention distribution, implement statistical testing protocol, implement α_leak measurement)",
      "claude_api_cost": "$700-1100 (7000-11000 turns for autonomous experiment design, debugging, statistical analysis, and paper drafting)",
      "estimated_gpu_cost": "~$2,000 (2500h × $0.80/hr)",
      "speed_bottleneck": "Number of concurrent A100 GPU instances. Secondary: intervention data generation is I/O-intensive (requires rendering perturbation environments). Statistical protocol with 5 seeds × 8 baselines × 7 perturbation dimensions requires organized experiment management.",
      "risk_note": "Without human gates, agent may over-explore suboptimal scoring layer combinations or DRO radius values. The theorem formalization cannot be fully automated — agent-generated proofs require expert verification, especially the amortization gap bound (step 3 of the proof involving Rademacher complexity). The statistical protocol is automatable but interpretation of borderline results (e.g., CaTS significant on 4/7 dimensions vs. the a priori 5/7 criterion) requires human judgment. Risk mitigation: pre-define structured search space with early stopping on amortization validation metrics; halt if Spearman ρ < 0.6 after initial scorer training."
    }
  },
  "target_venues": [
    "AAAI 2027 (deadline: ~August 1, 2026 — primary target, sufficient time for theoretical development, multi-layer scoring implementation, and statistical evaluation)",
    "ICLR 2027 (deadline: ~October 2026 — strong target, allows comprehensive evaluation and concurrent work comparison)",
    "ICRA 2027 (deadline: ~September 2026 — robotics venue, good fit for empirical contribution)"
  ],
  "level": "top-tier",
  "key_references": [
    "Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations [Causal-ACT] (arXiv 2507.22380, July 2025)",
    "VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling [FTM/FLA] (arXiv 2512.02902, Dec 2025)",
    "Learning to Focus: Causal Attention Distillation via Gradient-Guided Token Pruning [LeaF] (NeurIPS 2025, arXiv 2506.07851)",
    "Shortcut Learning in Generalist Robot Policies: The Role of Dataset Diversity and Fragmentation (CoRL 2025, arXiv 2508.06426)",
    "Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem? (ACL Findings 2025, arXiv 2502.11501)",
    "When Token Pruning is Worse than Random: Understanding Visual Token Information in VLLMs (ICLR 2026, arXiv 2512.07580)",
    "The Risks of Invariant Risk Minimization (ICLR 2021, arXiv 2010.05761)",
    "Out-of-Distribution Generalization via Risk Extrapolation [V-REx] (ICML 2021, arXiv 2003.00688)",
    "SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models (arXiv 2511.15605)",
    "AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention (arXiv 2511.18960)",
    "ACTIVA: Amortized Causal Effect Estimation via Transformer-based Variational Autoencoder (arXiv 2503.01290)",
    "CausalPFN: Amortized Causal Effect Estimation via In-Context Learning (NeurIPS 2025, arXiv 2506.07918)",
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026, arXiv 2510.13626)",
    "Invariant Causal Imitation Learning for Generalizable Policies [ICIL] (NeurIPS 2021)",
    "DTP: A Simple yet Effective Distracting Token Pruning Framework for VLA Models (arXiv 2601.16065, Jan 2026)",
    "FocusVLA: Focused Visual Utilization for Vision-Language-Action Models (arXiv 2603.28740, Mar 2026)",
    "LightVLA: Towards Efficient VLA Models via Differentiable Token Pruning (ICRA 2026, arXiv 2509.12594)",
    "TIES: Beyond Attention Magnitude — Leveraging Inter-layer Rank Consistency for Efficient VLA Models (arXiv 2603.24941, Mar 2026)",
    "BFA++: Hierarchical Best-Feature-Aware Token Pruning for Multi-View VLA Models (arXiv 2602.20566, Feb 2026)",
    "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation (arXiv 2511.18950)",
    "Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation (arXiv 2603.23202, Mar 2026)",
    "LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models (arXiv 2604.23950, Apr 2026)",
    "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations [RobustVLA] (ICLR 2026, arXiv 2510.00037)",
    "Mask World Model: Predicting What Matters for Robust Robot Policy Learning (arXiv 2604.19683, April 2026)",
    "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient VLA Inference (arXiv 2511.16449)",
    "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for VLA Models (arXiv 2603.22991, March 2026)",
    "Learning Invariant Causal Mechanism from Vision-Language Models [CLIP-ICM] (ICML 2025, arXiv 2405.15289)",
    "OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport (arXiv 2602.20205)",
    "Wasserstein Distributionally Robust Optimization and Variation Regularization (Operations Research, 2024)",
    "Finite-Sample Guarantees for Wasserstein DRO: Breaking the Curse of Dimensionality (Operations Research, 2023)",
    "Vision Transformers Need More Than Registers (arXiv 2602.22394, Feb 2026)",
    "Bounding the Estimation Error of Sampling-based Shapley Value Approximation (arXiv 1306.4265)",
    "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success [OpenVLA-OFT] (arXiv 2025)",
    "SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration (ICLR 2026, arXiv 2506.12723)",
    "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning (arXiv 2509.05614)",
    "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching (NeurIPS 2025, arXiv 2502.02175)",
    "InSpire: Vision-Language-Action Models with Intrinsic Spatial Reasoning (arXiv 2505.13888, May 2025)",
    "Causality-Inspired Robustness for Nonlinear Models via Representation Learning [CIRRL] (arXiv 2505.12868, May 2025)",
    "Learning to Estimate Shapley Values with Vision Transformers [ViT-Shapley] (ICLR 2023 Oral, arXiv 2206.05282)",
    "Mechanistic Interpretability for Steering Vision-Language-Action Models (CoRL 2025, arXiv 2509.00328)",
    "Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models [PDF] (arXiv 2604.18107, April 2026)",
    "Causal Shapley Values: Exploiting Causal Knowledge to Explain Individual Predictions of Complex Models (NeurIPS 2020, arXiv 2011.01625)"
  ],
  "description": "VLA models suffer catastrophic failures under visual distribution shifts, yet a proliferation of concurrent token pruning methods (DTP, FocusVLA, LightVLA, TIES, SP-VLA, BFA++, Compressor-VLA, Gaze-VLA — all 2025-2026) each propose different heuristic criteria without formal justification, and recent work shows many attention-based methods underperform random selection (arXiv 2502.11501) due to 'vanishing token information' in deep layers (arXiv 2512.07580). We propose Causal Token Selection (CaTS) v3, bridging three disconnected threads: VLA token pruning, causal intervention for imitation learning (Causal-ACT, ICIL), and causal attention distillation (LeaF), while drawing theoretical inspiration from CIRRL's (arXiv 2505.12868) breakthrough showing that representation-level identifiability enables nonlinear causal robustness guarantees. CaTS defines a formal SCM over the VLA token-action pipeline with a revised *encoder-level spatial locality* assumption — grounded in empirical findings that DINOv2/SigLIP encoder outputs preserve spatial correspondence (a form of patch-level identifiability analogous to CIRRL's affine identifiability) while LLM self-attention progressively mixes token information. Key advances over v2: (1) Multi-layer scoring at vision encoder output (where spatial locality is empirically validated) with optional intermediate-layer refinement. (2) Concrete ε-invariance bound with approximate constants: ε = C₁/√M + C₂·exp(-c·N_env/d_E) + C₃·α_leak·g(τ) + ε_amort, with order-of-magnitude estimates (M=200 Shapley samples → estimation error ~0.096; N_env=35 across d_E=7 dimensions → coverage term ~0.01; encoder-level α_leak≈0.1 → locality term ~0.10; overall ε≈0.26, a testable prediction against the observed ~50-65% gap for unmodified VLAs). (3) Honest composite robustness objective combining V-REx (practical heuristic) with Wasserstein DRO (finite-sample guarantees), including explicit analysis of their interaction: complementary for moderate DRO radius ρ (V-REx stabilizes known environments, DRO guards against unseen shifts; for small ρ, Wasserstein DRO approximates variation regularization, aligning with V-REx), with potential conflict at large ρ resolved by operating in the moderate-ρ regime calibrated to LIBERO-Plus perturbation magnitudes. (4) Quantified amortization gap: ε_amort ≤ O(1/√W) + O(1/√n_train) ≈ 0.054 for W=512, n_train=10K, with central validation protocol (Spearman ρ > 0.8). (5) Explicit differentiation from ViT-Shapley (ICLR 2023 Oral) — CaTS's amortized scorer extends the ViT-Shapley paradigm from observational Shapley values for model explanation to interventional causal effects for cross-environment invariance. (6) Acknowledgment that the 'vanishing token information' finding (arXiv 2512.07580) was validated on VLMs, not VLAs — verifying the information horizon in VLA architectures is part of the empirical contribution. (7) Integration with mechanistic interpretability evidence (CoRL 2025) validating that interventional methods identify causal structure in VLA representations, and positioning against test-time adaptation approaches (PDF, arXiv 2604.18107) as complementary training-time vs. test-time methods for the same spurious correlation problem. Formal statistical protocol against random pruning with a priori 5/7 dimension criterion. Evaluated against 8 core baselines (streamlined from 11 with explicit code availability assessment: VLA-Pruner and DTP have public code; TIES is training-free and reimplementable; FTM is trivially reimplementable) including SRPO (82.1% SOTA), DTP, TIES, and VLA-Pruner. Concurrent efficiency-focused methods (SP-VLA ICLR 2026, SpecPrune-VLA, VLA-Cache NeurIPS 2025) are discussed as complementary — targeting temporal/spatial redundancy rather than causal robustness. InSpire (arXiv 2505.13888) is discussed as a complementary prompting-based approach to the same spurious correlation problem. GPU costs updated to current May 2026 market rates ($0.80/hr A100 spot from specialized providers). Primary targets: AAAI 2027 and ICLR 2027.",
  "project_name": "causal_token_sel_vla",
  "source": "web_research"
}
```

**Summary of changes (minor fix addressing 4 reviewer issues):**

1. **ViT-Shapley (ICLR 2023 Oral)** — Added as the most direct technical predecessor. Integrated into opportunity (4th thread), landscape (new detailed section covering the 3-stage pipeline, observational vs. interventional Shapley distinction citing Heskes et al. NeurIPS 2020), approach (new "Relationship to ViT-Shapley" subsection + key differentiation entry), and key_references (both ViT-Shapley and Causal Shapley Values).

2. **Mechanistic Interpretability for VLA Steering (CoRL 2025)** — Added as validation of CaTS's core premise. Integrated into opportunity (5th thread), landscape (new section), approach (key differentiation entry), and key_references. Differentiated: neuron/direction level for steering vs. token level for robustness.

3. **VLM→VLA extrapolation caveat** — Added explicit acknowledgment in the approach section that arXiv 2512.07580 evaluates VLMs not VLAs, noting that ablation (b) directly tests this assumption in VLA architectures.

4. **PDF (arXiv 2604.18107)** — Added to landscape as complementary test-time adaptation approach, approach (key differentiation entry + baselines-discussed-but-not-reproduced), and key_references. Positioned as combinable with CaTS (training-time selection + test-time correction).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52f485dd-7eda-49ea-b880-f05278138bf0",
  "isSidechain": false,
  "requestId": "req_011Caz4iG1ct9Cry97kEgJ2P",
  "type": "assistant",
  "uuid": "93394efb-2fe3-4a29-837a-d7c79c8d1753",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FeiZmvKWLtE9bHv2xo1DG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16805,
      "cache_read_input_tokens": 47015,
      "output_tokens": 16525,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16525,
          "cache_read_input_tokens": 47015,
          "cache_creation_input_tokens": 16805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16805
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

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"Causal Token Selection for Invariant VLA Policies via Amortized Interv…",
  "leafUuid": "93394efb-2fe3-4a29-837a-d7c79c8d1753",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise VLA causal token selection with ViT-Shapley differentiation",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"Causal Token Selection for Invariant VLA Policies via Amortized Interv…",
  "leafUuid": "93394efb-2fe3-4a29-837a-d7c79c8d1753",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise VLA causal token selection with ViT-Shapley differentiation",
  "sessionId": "d1da6575-a77d-4a5e-984b-7ebc8af7dd82"
}
```

---
