# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Does Reducing Conversational Iner

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/07bb135d-16d1-47ac-8e33-f1e9e2720236.jsonl`
- **Structured JSON:** [`36406066a13c45347bc0.json`](../../sessions/36/36406066a13c45347bc0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:40:49.039Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:40:49.039Z",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Does Reducing Conversational Inertia Improve Multi-Turn Safety? Testing the Attention Capacity Competition Hypothesis\n\n## Description\nThis project conducts the first controlled interventional study testing whether mitigating conversational inertia — diagonal attention to previous outputs (Wan et al., ICML 2026) — causally reduces multi-turn safety erosion, organized around a refined three-level 'attention capacity competition hypothesis.' We build on DETAM's proof that inference-time attention reallocation improves safety (ASR 46%→1.2%) and ASGuard's demonstration that training-time head modification is feasible for specific vulnerabilities, testing whether CPL achieves broad attention reallocation through untargeted discourse training — addressing the progressive multi-turn erosion that DETAM (single-turn, requires runtime intent localization) and ASGuard (targets specific localizable circuits) structurally cannot. In multi-turn crescendo attacks, malicious intent is distributed across turns, making DETAM's intent-token identification ill-defined; CPL instead reduces the cumulative inertia that pushes systems past Johnson & Huo's tipping point. A novel Phase 0.5 provides the first per-head decomposition of diagonal attention (Wan et al. explicitly averages all heads) and measures overlap with safety-critical heads using triple triangulation (Ships score, DETAM sensitivity, AISA spatiotemporal analysis), cross-validated against published head sets (Zhou et al., Depth Charge, ASGuard — whose 4 Layer-13 vulnerable heads independently corroborate the continuation-safety nexus). Our five-phase causal design tests CPL against five confound controls including XGuard-Train SFT at both published and CPL-matched ranks. Mechanistic verification tests whether CPL achieves 'implicit DETAM' (same heads, same direction) and 'implicit circuit modification' (affecting ASGuard's identified vulnerable heads without targeting them). The study is designed for informative outcomes at all three competition levels, with the per-head diagonal attention decomposition, triple-method head identification comparison, and DETAM/ASGuard mechanistic comparison constituting standalone contributions.\n\n## Core Problem\nMulti-turn agent interactions exhibit systematic safety degradation (16% higher attack success rates), and while recent work has identified attention-level mechanisms — attention dispersion on safety keywords (ASJA, AAAI 2025), competition between safety and continuation heads (Deng et al., 2026), and attention reallocation as a defense (DETAM, ACL 2025 Findings) — and developed multi-turn safety defenses (MUSE-D turn-level DPO, EMNLP 2025; XGuard-Train SFT, COLM 2025; X-Boundary representation boundaries, EMNLP 2025; MTSA RL-based alignment, ACL 2025), and even training-time attention head interventions for specific vulnerability types (ASGuard circuit-targeted scaling, ICLR 2026), these studies are either attack-oriented, single-turn, operate at inference time, target specific localizable vulnerabilities, or train directly on safety-labeled data without testing whether discourse-level mechanisms causally drive safety erosion. Critically, DETAM (Li et al., ACL 2025 Findings) demonstrates that simply reallocating attention from attack tokens toward safety-relevant tokens at inference time — without any weight changes — reduces ASR from 46% to 1.2% on LLaMA-2, providing the strongest existing evidence that attention redistribution causally improves safety. Yet DETAM requires explicit identification of 'intent tokens' at runtime and operates only in single-turn settings — in multi-turn crescendo attacks where malicious intent is progressively distributed across turns, the notion of localizable 'intent tokens' breaks down fundamentally. ASGuard (Park et al., ICLR 2026) demonstrates that training-time modification of safety-relevant heads is feasible via circuit-targeted scaling vectors, but its efficacy 'hinges on localizable causal circuits' for specific attack types (tense jailbreaking) — multi-turn safety erosion through cumulative discourse dynamics may not produce such localizable circuits. No work has tested whether a training-time discourse intervention (reducing conversational inertia) achieves broad attention reallocation indirectly, nor whether the specific attention heads carrying diagonal inertia patterns overlap with safety-critical heads — a prerequisite for the softmax zero-sum competition mechanism to operate at the head level. Notably, the only characterization of diagonal attention (Wan et al., ICML 2026) reports aggregate-level patterns averaged across all heads; no per-head decomposition exists, leaving the head-level competition question empirically open. Additionally, the response-length confound in DPO-based interventions has never been explicitly controlled for in safety evaluations of discourse-level interventions.\n\n## Opportunity\nSix independent research threads have converged to make a controlled causal study newly feasible: (1) Conversational Inertia (Wan et al., ICML 2026) identifies diagonal attention where the i-th token attends to the i-th previous output position and provides Context Preference Learning (CPL) as a parameter-efficient intervention (0.4% params, LoRA rank-16 DPO with beta=0.01), validated on Qwen3-8B and Llama 3.1-8B-Instruct across eight agentic environments but never evaluated for safety — crucially, the diagonal attention pattern is characterized only at the aggregate level (averaged across all heads), so the per-head distribution remains unknown; (2) DETAM (Li et al., ACL 2025 Findings) provides direct causal evidence that attention reallocation toward safety-relevant tokens improves safety — reducing ASR by 97%+ without weight modification — but requires runtime intent token identification and is single-turn only, creating a fundamental limitation for multi-turn settings where intent is distributed across turns; (3) ASGuard (Park et al., ICLR 2026) demonstrates that training-time modification of safety-relevant attention heads is feasible via circuit-targeted channel-wise scaling vectors and preventative fine-tuning — crucially, ASGuard identifies 4 vulnerable heads at Layer 13 in Llama-3.1-8B (L13H8, L13H18, L13H25, L13H30), exactly where Deng et al. find continuation heads, providing independent corroboration that Layer 13 is a nexus of safety-relevant competition — but ASGuard targets specific localizable vulnerability circuits (tense jailbreaking) rather than discourse-level dynamics; (4) Multi-turn safety erosion is now well-benchmarked via MT-AgentRisk (365 tasks, 5 tools, avg 3.19 turns) with ToolShield as a defense baseline, and supplemented by OpenAgentSafety (ICLR 2026, 356 real-tool tasks with multi-turn multi-user dynamics); (5) Multi-turn safety training has mature baselines spanning multiple paradigms: XGuard-Train SFT (COLM 2025, up to 48.3% vulnerability reduction), MUSE-D turn-level DPO (EMNLP 2025, 24% ASR reduction), X-Boundary representation-level boundaries (EMNLP 2025, ASR reduction to 16-25%), and MTSA RL with future rewards (ACL 2025, ASR 74.5% to 23.5%) — but all train directly on safety-labeled data; (6) AISA (Song et al., arXiv:2602.13547) provides a third complementary method for localizing safety-critical attention heads via spatiotemporal analysis — identifying that safety-discriminative signals concentrate in middle-layer head outputs with K=16 heads achieving 0.92 detection accuracy — enabling methodological triangulation in our head overlap analysis. This six-thread convergence, combined with Johnson & Huo's (2026) formalization of attention competition tipping points and the layered distribution of safety mechanisms across layers 2-27, motivates a three-level attention capacity competition hypothesis testable through a novel Phase 0.5 head overlap analysis.\n\n## Landscape\n**Attention reallocation defenses:** DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562) is the most directly relevant inference-time prior work. It identifies attention heads sensitive to jailbreaks by computing attention score differences between successful and unsuccessful defenses (threshold alpha: 0.1 for LLaMA-2, 0.03 for Vicuna). During inference, it modifies the causal mask matrix by multiplying mask values at intent token positions by beta=5.0, amplifying attention to the user's core intention. DETAM reduces average ASR from 46.0% to 1.2% on LLaMA-2-7b-chat and from 81.8% to 4.0% on Vicuna-13b-v1.5. Cross-model transferability: sensitive heads from LLaMA-2 transferred to Meta-LLaMA-3 achieve 4% ASR vs. 96% vanilla. However, DETAM has three fundamental limitations for multi-turn agent settings: (a) it requires runtime identification of 'intent tokens' — in multi-turn crescendo attacks (Russinovich et al., USENIX Security 2025) where harmful intent is progressively distributed across turns, no single set of tokens constitutes 'the intent,' making DETAM's token-level localization fundamentally ill-defined; (b) it is tested only in single-turn settings and cannot address the cumulative attention shift across turns that Johnson & Huo's tipping point theory predicts; (c) it imposes per-turn computational overhead for mask modification in each forward pass across all turns of agent interaction. Our study tests whether CPL achieves DETAM-like attention redistribution persistently through training, addressing a failure mode DETAM structurally cannot: the gradual accumulation of continuation pressure across turns that progressively dilutes safety attention below the tipping point. **Training-time attention head intervention:** ASGuard (Park et al., ICLR 2026, arXiv:2509.25843) is the closest existing work to training-time attention head modification for safety. It uses Edge Attribution Patching with Integrated Gradients (EAP-IG) to identify attention heads causally linked to specific jailbreaking vulnerabilities, trains channel-wise activation scaling vectors (s_j ∈ R^{d_head}, applied via Hadamard product H'_{l,j} = H_{l,j} ⊙ s_j) on identified heads, and applies preventative fine-tuning with scaling vectors frozen. On tense jailbreaking, ASGuard reduces ASR from 42% to 8% on Llama-3.1-8B and 51% to 8% on Qwen2.5-7B, achieving Pareto-optimal safety-utility balance. Critically, ASGuard identifies 11 vulnerable heads in Llama-3.1-8B, of which 4 are at Layer 13 (L13H8, L13H18, L13H25, L13H30) — exactly where Deng et al. find continuation heads — providing independent corroboration that Layer 13 is a nexus of safety-relevant attention competition. However, ASGuard differs from our approach in three key ways: (a) it targets specific, localizable vulnerability circuits ('efficacy hinges on localizable causal circuits' — their Limitations, Section 7) — multi-turn safety erosion through cumulative discourse dynamics may not produce such localizable circuits, as the failure is progressive rather than circuit-specific; (b) it surgically fixes known attack types (tense jailbreaking, GCG, LogiBreak) one at a time, whereas CPL is an untargeted discourse intervention testing whether reducing general inertia achieves broad safety benefits; (c) it is single-turn only. ASGuard's success actually supports a key premise of our hypothesis: training-time modification of attention heads CAN improve safety. Our study tests whether indirect, untargeted discourse training achieves what targeted head intervention achieves — and whether it generalizes to the multi-turn progressive erosion that targeted approaches cannot address. **Safety head localization methods:** AISA (Song et al., arXiv:2602.13547) provides a third complementary approach to localizing safety-critical heads via spatiotemporal analysis — large-scale linear probing across 15 positions per layer identifies that attention head outputs demonstrate superior safety separability, with top-K=16 heads (concentrated in middle layers) achieving 0.92 detection accuracy and O(1) runtime overhead. AISA's finding that safety heads cluster in middle layers in standard models but shift toward higher layers in strongly safety-aligned models adds nuance to the competition hypothesis — the relevant layers may differ by alignment strength. **Attack-side mechanisms:** Du et al. (ASJA, AAAI 2025) show that successful multi-turn jailbreaks correlate with attention dispersion away from safety keywords (p=4.38e-07), achieving 44.9% higher ASR. Deng et al. (arXiv:2603.08234) identify competing safety and continuation attention heads — safety heads concentrated in layers 25-27, continuation heads in middle layers (~Layer 13) — whose antagonistic interaction determines jailbreak success. Notably, continuation heads at Layer 13 occupy the same layer range as both induction/copying mechanisms AND ASGuard's identified vulnerable heads, suggesting this layer is a critical nexus where diagonal attention patterns, continuation signals, and safety vulnerability converge. Depth Charge (Wu et al., arXiv:2603.05772, March 2026) introduces SAHA using Ablation-Impact Ranking and Layer-Wise Perturbation, achieving 82-91% ASR, revealing layer-specific safety head concentrations (layer 7 for Llama 3.1-8B, layer 5 for Qwen 1.5-7B, head 31 universally important) and sharp threshold behavior. Attention Eclipse (Zaree et al., arXiv:2502.15334) achieves 91.2% ASR by manipulating attention to strengthen harmful content focus and weaken safety focus. **Attention competition theory:** Johnson & Huo (arXiv:2602.14370, Feb 2026) formalize the competition-for-attention mechanism mathematically, showing that dot-product competition creates dynamical tipping points (n*) where behavior transitions from safe to unsafe — providing the theoretical framework for why cumulative inertia across turns can push the system past a tipping point that single-turn defenses like DETAM cannot prevent. **Multi-turn safety benchmarking:** Yang et al. (arXiv 2026) document 16% average ASR increase on MT-AgentRisk and propose ToolShield (~30% ASR reduction). OpenAgentSafety (ICLR 2026) provides 356 multi-turn, multi-user tasks with real tools. Li et al. (STAR, arXiv:2603.15684) show monotonic drift from refusal representations. MultiBreak (arXiv:2605.01687) provides 10,389 multi-turn adversarial prompts. **Multi-turn safety defenses:** X-Teaming (COLM 2025, arXiv:2504.13203) introduces XGuard-Train, a 30K multi-turn safety training dataset. Models SFT-trained on a 14K subset with LoRA rank-8, lr=1e-4, 3 epochs achieve up to 48.3% vulnerability reduction on Llama-3.1-8B and Qwen-2.5-7B. MUSE-D (EMNLP 2025, arXiv:2509.14651) applies turn-level DPO achieving 24% ASR reduction. X-Boundary (Lu et al., EMNLP 2025, arXiv:2502.09990) operates at the representation level, reducing multi-turn ASR from 58.5-76.0% to 16.0-25.0% while reducing over-refusal by ~20%. MTSA (Guo et al., ACL 2025, arXiv:2505.17147) performs RL with future rewards, reducing ASR from 74.5% to 23.5%, with the finding that maximum attack effectiveness peaks at round 5 — confirming multi-turn pressure accumulates through discourse dynamics. Agent Safety Alignment (Sha et al., arXiv:2507.08270) proposes unified sandboxed RL with benign/malicious/sensitive taxonomy. STREAM (arXiv:2506.00668) proposes safety reasoning moderator reducing ASR by 51.2%. TurnGate (arXiv:2605.05630) introduces turn-level harm detection. **Discourse dynamics:** Wan et al. (ICML 2026, arXiv:2602.03664; note: also submitted to ICLR 2026 as OpenReview #UubLs3lUfk, subsequently published in PMLR 306 at ICML 2026, Seoul, July 6-11) identify conversational inertia and propose CPL. The paper characterizes diagonal attention only at the aggregate level — explicitly stating 'All attention heads are averaged to create a unified attention matrix' and 'the trend of diagonal attention in the final layer is similar to other layers' — with no per-head decomposition. Code not released. **Safety attention head mechanisms:** Zhou et al. (ICLR 2025, arXiv:2410.13708) show the single most critical head in Llama-2-7B-Chat is Head (2, 26) at Layer 2. Wei et al. identify safety layers at layers 9-14. The refusal direction (Arditi et al.) is strongest around layer 15. Safety Alignment Should Be Made More Than Just A Few Attention Heads (arXiv:2508.19697) proposes distributed safety head training. **Safety persistence:** Plaut (arXiv:2603.02229) shows LoRA safety DPO persists with 90-94% retention, Pareto frontier R-squared=0.77, slope=-0.83. **DPO length bias:** Park et al. (2024) and Meng et al. (2024) document hidden length dependence. **Gap:** Despite convergent progress on inference-time attention reallocation (DETAM), training-time targeted head intervention (ASGuard), training-time safety defenses (XGuard-Train, MUSE-D, X-Boundary, MTSA), safety head localization (Zhou et al., AISA, Depth Charge), attention competition theory (Johnson & Huo), and discourse dynamics (conversational inertia), no work has: (a) tested whether a training-time discourse intervention achieves broad DETAM-like attention reallocation and causally reduces safety erosion in multi-turn settings — addressing the progressive accumulation that both DETAM (single-turn only) and ASGuard (circuit-specific only) cannot; (b) provided a per-head decomposition of diagonal attention to determine whether inertia heads overlap with safety heads; (c) compared discourse-targeted vs. safety-targeted training under matched parameter budgets; or (d) controlled for DPO response-length confounds in discourse-safety evaluations.\n\n## Approach\nWe run a five-phase causal study on MT-AgentRisk (primary) and OpenAgentSafety (secondary) benchmarks using Qwen3-8B and Llama 3.1-8B-Instruct, organized around the 'attention capacity competition hypothesis' and motivated by a specific gap that neither DETAM nor ASGuard can address: progressive multi-turn safety erosion through cumulative discourse dynamics.\n\n**Why Training-Time Discourse Intervention? The Multi-Turn Intent Distribution Problem.** DETAM achieves 97%+ ASR reduction in single-turn settings at zero training cost — but it requires identifying 'intent tokens' at runtime. In multi-turn crescendo attacks where harmful intent is progressively distributed across 3-10 turns (MTSA finds peak attack at round 5), no single set of tokens constitutes 'the intent.' The malicious instruction at turn 7 is only harmful in the context of the innocuous-seeming turns 1-6 that established the frame. DETAM cannot solve this because its mechanism — amplifying attention to intent tokens in sensitive heads — presupposes that intent is localizable within a single turn. ASGuard demonstrates training-time head modification is feasible but targets specific localizable circuits (tense jailbreaking), and its own Limitations section notes 'efficacy hinges on localizable causal circuits.' Multi-turn safety erosion through cumulative inertia is NOT a localizable circuit — it's a progressive process where each turn incrementally shifts the attention distribution. CPL's advantage is that it operates at the discourse dynamics level: reducing the cumulative inertia that progressively dilutes safety attention across turns, without needing to identify which tokens are 'intent' tokens or which circuits carry a specific vulnerability. It addresses the ROOT CAUSE (attention inertia accumulation across turns) rather than the SYMPTOM (misallocated attention at any single turn). This is the failure mode that Johnson & Huo's tipping point theory predicts: gradual accumulation of continuation pressure pushes the system past n* — and the only way to prevent reaching the tipping point is to reduce the per-turn accumulation rate, which is exactly what CPL does.\n\n**The Attention Capacity Competition Hypothesis (Three-Level Framework):** We theorize that diagonal attention (the inertia mechanism) competes with safety-keyword attention at three distinct levels: **Level 1 (Head-level, strong form):** If diagonal attention and safety attention share the same heads, softmax's zero-sum constraint directly displaces safety-keyword attention. Given that safety heads span layers 2-27 and induction/copying mechanisms typically concentrate in middle layers, partial overlap is plausible. **Level 2 (Layer-level, medium form):** If diagonal and safety attention occupy different heads within the same or adjacent layers, competition occurs through the residual stream. This is supported by Deng et al.'s finding that continuation heads (Layer 13) antagonize safety heads (Layers 25-27), and strikingly corroborated by ASGuard's identification of 4 vulnerable heads at Layer 13 in Llama-3.1-8B (L13H8, L13H18, L13H25, L13H30) — the same layer where continuation heads reside, independently confirming Layer 13 as a nexus of safety-relevant competition. **Level 3 (Representation-level, weak form):** Competition mediated through accumulated representation drift, validated by X-Boundary's success (ASR 58.5% to 16.5%). Phase 0.5 empirically determines which level(s) apply.\n\n**Phase 0 — CPL Acquisition/Reproduction + Baseline Preparation (weeks 1-3):** Contact Wan et al. for CPL checkpoints (ICML 2026 July 6-11). Simultaneously reproduce CPL using TRL DPOTrainer + PEFT: LoRA rank-16, alpha-16, 0.4% params, DPO with beta=0.01, sigmoid loss, 2 epochs, lr=5e-7, AdamW, 1000 preference pairs per environment. The training recipe maps directly to TRL v1.0+ (sigmoid loss is the default DPOConfig, all hyperparameters natively supported); the main reproduction risk is the preference pair construction pipeline (dual-rollout with long-context vs. short-context on AgentGym environments) rather than the training loop itself. Estimated: ~40 A100-hours per model. In parallel, prepare XGuard-Train SFT baselines: (a) LoRA rank-8 with lr=1e-4, 3 epochs (matching published configuration from X-Teaming, validated on Llama-3.1-8B and Qwen-2.5-7B); (b) LoRA rank-16 with CPL-matched hyperparameters for parameter-matched comparison. Construct extended-turn variants: prepend 4-6 benign tool-use turns to 50 representative MT-AgentRisk tasks.\n\n**Hard Go/No-Go Checkpoint at Week 3:** The project proceeds to Phase 0.5 only if ALL criteria are met: (1) AgentGym environment setup working for >=3 of 8 environments (prioritizing ALFWorld, WebShop, HotpotQA); (2) dual-rollout preference pair generation produces pairs where long-context trajectories show measurably higher diagonal attention scores than short-context trajectories (statistically significant at p<0.05 on at least 2 environments); (3) DPO training pipeline converges (decreasing loss, increasing reward margins over 2 epochs); (4) base model evaluation on >=2 environments matches Wan et al.'s published baselines within 1 SEM. **Fallback paths:** (a) environment failure: proceed with 2-3 most reliable environments; (b) inertia differential failure: pivot to correlational-only study (Phases 1 and 4 only); (c) training failure: debug 1 additional week — if still failing by week 4, pivot to 'DETAM in multi-turn settings' (extending DETAM's mechanism to MT-AgentRisk, testing whether Focus Loss intensifies across turns).\n\n**Phase 0.5 — Head Overlap Test and Per-Head Diagonal Attention Decomposition (weeks 3-4, ~20 A100-hours):** This phase provides the first per-head decomposition of diagonal attention patterns and tests the prerequisite assumption of the competition hypothesis. Using both base models on 50 MT-AgentRisk tasks: (a) **Novel per-head diagonal attention decomposition:** Compute diagonal attention scores per head (not just aggregate) using Wan et al.'s metric (attention between current output position i and previous assistant output position i +/- 5 tokens) — this is the first such decomposition, given that Wan et al. explicitly average all heads ('All attention heads are averaged to create a unified attention matrix'). Identify which heads carry the strongest diagonal patterns and their layer distribution. (b) **Safety head identification via triple triangulation:** Apply three complementary methods: (i) Ships score (Zhou et al., ICLR 2025) via KL divergence after head ablation; (ii) DETAM's sensitivity metric (attention score differences between successful/unsuccessful safety responses); (iii) AISA's spatiotemporal analysis — linear probing on head outputs at final structural tokens to identify safety-discriminative heads (K=16). Cross-validate against published localizations: Zhou et al.'s Head (2,26) for Llama-2-family; Depth Charge's layer-specific data (layer 7 for Llama 3.1-8B); ASGuard's EAP-IG identified heads (11 heads for Llama-3.1-8B including 4 at Layer 13). Using three independent methods plus cross-validation against three published head sets provides robust head identification. (c) **Overlap analysis:** Compute Jaccard index between top-k diagonal attention heads and top-k safety heads (k = 5, 10, 20, 50) with permutation tests. Also measure layer-level co-occurrence (same layer, different heads). Cross-reference against ASGuard's Layer 13 vulnerable heads — if diagonal attention heads concentrate at Layer 13, this would connect conversational inertia to the continuation-safety competition nexus identified by both Deng et al. and ASGuard independently. (d) **Level determination:** Level 1 (>30% head overlap) — proceed with strong per-head softmax hypothesis; Level 2 (same layers, <30% head overlap) — reformulate around residual stream competition, particularly the Layer 13 continuation-inertia-safety nexus; Level 3 (<10% overlap in both heads and layers) — reformulate around representation-level competition. Each determination shapes subsequent analysis. This phase costs ~20 A100-hours but de-risks the project and provides standalone novel contributions (first per-head diagonal attention map; first triple-method safety head identification comparison).\n\n**Phase 1 — Correlational with Attention Capacity Analysis (weeks 4-7):** Measure diagonal attention (per-head, informed by Phase 0.5) AND safety-keyword attention concentration at each turn on 365 MT-AgentRisk tasks and 50 extended-turn variants. Calibrate analysis to competition level from Phase 0.5. Fit mixed-effects regressions testing P1 (diagonal attention negatively correlates with safety attention at the operative level), controlling for turn position, task category, model, and response token count. Test Granger causality for temporal dynamics.\n\n**Phase 2 — Interventional with Confound Controls (weeks 7-11):** Apply CPL and re-evaluate on MT-AgentRisk. Five control conditions: (a) **Random-Preference LoRA** — shuffled preference labels, same architecture; (b) **Reversed-CPL** — prefer long-context over short-context; (c) **XGuard-Train SFT (rank-8)** — published configuration for validation against published results; (d) **XGuard-Train SFT (rank-16)** — CPL-matched parameters for direct paradigm comparison (discourse-targeted vs. safety-targeted training); (e) **Response-Length Analysis** — ASR stratified by length quartiles, per-100-token normalization, regression with length covariate (testing P3: CPL's safety effect, if any, is not explained by response-length changes). Frame CPL's effect relative to both DETAM and ASGuard: test whether CPL affects the same heads DETAM identifies as sensitive and shifts attention in the same direction (implicit DETAM test), and whether it affects ASGuard's identified vulnerable heads at Layer 13 (implicit untargeted circuit modification test). Compare against ToolShield baseline and MUSE-D's published results.\n\n**Phase 3 — Autonomy Tax Audit (weeks 9-11, parallel):** Step-1 completion rate, cascade failure rate, end-to-end success, over-refusal. Report safety-competence Pareto frontier extending Plaut's analysis. Compare CPL's frontier position with X-Boundary's ~20% over-refusal reduction, ASGuard's Pareto-optimal balance, and XGuard-SFT's published results.\n\n**Phase 4 — Mechanistic Verification (weeks 10-14):** (a) SRI signal framework for step-wise refusal dynamics; (b) Head-level analysis extending Deng et al.'s safety-continuation head identification to multi-turn, calibrated by Phase 0.5 overlap findings — test whether CPL modulates the Layer 13 continuation vs. Layer 25-27 safety head balance across conversation turns; (c) **DETAM-informed analysis:** Apply DETAM's sensitivity metric to CPL-treated models — does CPL training shift attention in the same heads and direction that DETAM targets at inference time? If so, CPL achieves 'implicit DETAM' through discourse training, but persistently and without runtime intent localization; (d) **ASGuard-informed analysis:** Test whether CPL affects ASGuard's identified vulnerable heads (particularly the 4 at Layer 13) despite not targeting them — this would demonstrate that untargeted discourse training can modify the same heads that targeted circuit analysis identifies, but as a side effect of reducing general inertia rather than through explicit circuit surgery; (e) Level-appropriate analysis: Level 2 — residual stream composition analysis at shared layers; Level 3 — representation trajectory analysis following X-Boundary's framework.\n\n**Secondary Evaluation — OpenAgentSafety (weeks 12-14):** Best-performing config and XGuard-SFT on a subset for ecological validity.\n\n**Null-Result Framing Strategy:** (1) First per-head decomposition of diagonal attention patterns and their overlap (or non-overlap) with safety heads — novel regardless of CPL results; (2) First triple-method safety head identification comparison (Ships + DETAM sensitivity + AISA spatiotemporal), cross-validated against three published head sets (Zhou et al., Depth Charge, ASGuard); (3) Empirical evidence for or against the three-level competition hierarchy; (4) First confound-controlled causal framework for discourse-safety evaluation; (5) First discourse-targeted vs. safety-targeted training comparison under matched parameters; (6) First multi-turn extension of DETAM's Focus Loss analysis; (7) Empirical test of whether CPL-like untargeted training affects the same heads as ASGuard's targeted circuit intervention.\n\n**Extended-Turn Variant Validity (Limitation):** Acknowledged with mitigations: OpenAgentSafety for ecological validity, attention pattern validation, conservative amplification framing.\n\nAll primary experiments use MT-AgentRisk (365 tasks), ToolShield codebase (GitHub: CHATS-lab/ToolShield), XGuard-Train (HuggingFace: marslabucla/XGuard-Train), and the CPL training recipe from Wan et al. (ICML 2026).\n\n## Resource Estimate\n{'manual': {'gpu_hours': '720-900 A100-hours (CPL reproduction 2 models ~80h, XGuard-SFT rank-8 + rank-16 training 2 models ~60h, 2 control LoRAs for 2 models ~80h, Phase 0.5 head overlap test with AISA probing ~25h, MT-AgentRisk evaluation across 6 conditions x 2 models ~240h, extended-turn evaluation ~40h, OpenAgentSafety subset ~60h, SRI signal analysis ~30h, attention analysis including per-head diagonal decomposition + DETAM-informed + ASGuard-informed metrics ~85h, head-level safety-continuation analysis ~40h, response-length analysis ~10h)', 'timeline': '15-17 weeks (3 weeks Phase 0 + go/no-go, 1 week Phase 0.5, 3 weeks Phase 1, 4 weeks Phase 2 + Phase 3 parallel, 4 weeks Phase 4 + OpenAgentSafety, 3 weeks writing; comfortable for ICLR 2027)', 'estimated_gpu_cost': '$1080-1350 at $1.50/A100-hr spot pricing'}, 'human_in_loop': {'gpu_hours': '720-900 A100-hours', 'timeline': '13-15 weeks (Claude accelerates CPL reproduction, Phase 0.5 triple-method pipeline, DETAM/ASGuard comparison metrics, statistical analysis)', 'claude_api_cost': '$300-450 (CPL reproduction, per-head diagonal decomposition, triple-method head overlap analysis, DETAM/ASGuard-informed metrics, experiment orchestration, statistical modeling)', 'estimated_gpu_cost': '$1080-1350 at $1.50/A100-hr spot pricing'}, 'auto_research': {'gpu_hours': '920-1140 A100-hours (additional automated sweeps, full OpenAgentSafety evaluation, extended ablation across competition levels, comprehensive per-head analysis with triple methods)', 'timeline': '9-11 weeks (parallelized execution, automated Phase 0.5 -> Phase 1 pipeline)', 'claude_api_cost': '$600-850 (end-to-end orchestration including CPL reproduction, triple-method head analysis, DETAM/ASGuard comparison, control sweeps, result interpretation, draft generation)', 'estimated_gpu_cost': '$1380-1710 at $1.50/A100-hr spot pricing', 'speed_bottleneck': 'Sequential multi-turn interaction generation; 12 model configurations (2 models x 6 conditions); Phase 0.5 is a serial dependency before Phase 1; triple-method safety head analysis computationally intensive'}}\n\n## Inspired By\nField guide Section 4 (cascading failures, production gap) + Section 5.2 (error propagation as primary bottleneck). Key insight: DETAM's demonstration that inference-time attention reallocation dramatically improves safety (ASR 46% to 1.2%) establishes the empirical foundation for our hypothesis — if explicitly redirecting attention works, does implicit redirection via discourse training also work? ASGuard's demonstration that training-time head modification is feasible for specific vulnerabilities raises the natural question: can untargeted discourse training achieve what targeted circuit intervention achieves, but for the progressive multi-turn erosion that circuit-based approaches cannot address? The three-level competition hierarchy was motivated by the finding that Wan et al. only characterizes diagonal attention at the aggregate level (explicitly averaging all heads into a unified matrix) and that safety heads span multiple layer ranges (L2, L9-14, L25-27), while continuation heads at Layer 13 overlap with both induction/copying head territory and ASGuard's identified vulnerable heads (4 of 11 Llama-3.1-8B vulnerable heads are at L13). Johnson & Huo's (2026) formalization of attention competition tipping points provides the theoretical framework for why cumulative discourse inertia can push multi-turn interactions past a safety threshold that per-turn defenses cannot prevent. The reviewer's observation about per-head specificity led to Phase 0.5, which provides the first per-head decomposition of diagonal attention — a novel contribution regardless of results. AISA's spatiotemporal analysis provides methodological triangulation for safety head identification, strengthening Phase 0.5's robustness.\n\n## Target Venues\n- ICLR 2027 (abstract September 19 2026, full paper September 24 2026 [estimated] — primary target, ~18 weeks from project start, comfortable timeline with 3+ weeks buffer including Phase 0.5)\n- AAAI 2027 (abstract July 21 2026, full paper July 28 2026 — stretch target, ~10 weeks; feasible only if CPL checkpoints obtained by week 2, Phase 0.5 shows Level 1 or 2 overlap, and Phase 1 results are clean)\n\n## Key References\n- DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification (Li et al., ACL 2025 Findings, arXiv:2504.13562)\n- ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack (Park et al., ICLR 2026, arXiv:2509.25843)\n- AISA: Awakening Intrinsic Safety Awareness in Large Language Models against Jailbreak Attacks (Song et al., arXiv:2602.13547, Feb 2026)\n- Multi-Turn Jailbreaking Large Language Models via Attention Shifting (ASJA, AAAI 2025)\n- Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., ICML 2026, arXiv:2602.03664)\n- Unsafer in Many Turns: Benchmarking and Defending Multi-Turn Safety Risks in Tool-Using Agents (Yang et al., arXiv 2026)\n- X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents (COLM 2025, arXiv:2504.13203)\n- MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety (EMNLP 2025, arXiv:2509.14651)\n- X-Boundary: Establishing Exact Safety Boundary to Shield LLMs from Multi-Turn Jailbreaks without Compromising Usability (Lu et al., EMNLP 2025, arXiv:2502.09990)\n- MTSA: Multi-turn Safety Alignment for LLMs through Multi-round Red-teaming (Guo et al., ACL 2025, arXiv:2505.17147)\n- Agent Safety Alignment via Reinforcement Learning (Sha et al., arXiv:2507.08270)\n- Safety Training Persists Through Helpfulness Optimization in LLM Agents (Plaut, arXiv:2603.02229, March 2026)\n- The Struggle Between Continuation and Refusal (Deng et al., arXiv:2603.08234, Mar 2026)\n- The Autonomy Tax: Defense Training Breaks LLM Agents (Li & Zhao, arXiv:2603.19423, Mar 2026)\n- On the Role of Attention Heads in Large Language Model Safety (Zhou et al., ICLR 2025, arXiv:2410.13708)\n- Depth Charge: Jailbreak Large Language Models from Deep Safety Attention Heads (Wu et al., arXiv:2603.05772, Mar 2026)\n- Safety Alignment Should Be Made More Than Just A Few Attention Heads (Huang et al., arXiv:2508.19697, 2025)\n- Competition for attention predicts good-to-bad tipping in AI (Johnson & Huo, arXiv:2602.14370, Feb 2026)\n- Attention Eclipse: Manipulating Attention to Bypass LLM Safety-Alignment (Zaree et al., arXiv:2502.15334, Feb 2025)\n- Safety Layers in Aligned Large Language Models (Wei et al., arXiv:2408.17003, 2024)\n- Refusal in Language Models Is Mediated by a Single Direction (Arditi et al., arXiv:2406.11717, 2024)\n- State-Dependent Safety Failures in Multi-Turn Language Model Interaction (STAR, arXiv:2603.15684, Mar 2026)\n- OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety (ICLR 2026, arXiv:2507.06134)\n- One Turn Too Late: Response-Aware Defense Against Hidden Malicious Intent in Multi-Turn Dialogue (TurnGate, arXiv:2605.05630, May 2026)\n- MultiBreak: A Scalable and Diverse Multi-turn Jailbreak Benchmark (arXiv:2605.01687, May 2026)\n- STREAM: SafeTy Reasoning Elicitation Alignment for Multi-Turn Dialogues (arXiv:2506.00668, May 2025)\n- Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions (arXiv 2026)\n- Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks (arXiv 2026)\n- TRUTH DECAY: Quantifying Multi-Turn Sycophancy in Language Models (arXiv 2025)\n- Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction (arXiv 2026)\n- SafetyDrift: Predicting When AI Agents Cross the Line Before They Actually Do (arXiv 2026)\n- Token Statistics Reveal Conversational Drift in Multi-turn LLM Interaction (arXiv 2026)\n- Asking Forever: Universal Activations Behind Turn Amplification (arXiv:2602.17778, Feb 2026)\n- Step-Wise Refusal Dynamics in Autoregressive and Diffusion Language Models (arXiv:2602.02600, Feb 2026)\n- Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection (arXiv:2604.28129, Apr 2026)\n- Many-Turn Jailbreaking (arXiv:2508.06755, Aug 2025)\n- Disentangling Length from Quality in Direct Preference Optimization (Park et al., arXiv:2403.19159, 2024)\n- Length Desensitization in Direct Preference Optimization (Meng et al., arXiv:2409.06411, 2024)\n- Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack (Russinovich et al., USENIX Security 2025, arXiv:2404.01833)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T03:40:49.054Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:40:49.054Z",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236"
}
```

---

## Round 1

47 recorded events

### User

_source line 3 · 2026-05-20T03:40:49.124Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Does Reducing Conversational Inertia Improve Multi-Turn Safety? Testing the Attention Capacity Competition Hypothesis

## Description
This project conducts the first controlled interventional study testing whether mitigating conversational inertia — diagonal attention to previous outputs (Wan et al., ICML 2026) — causally reduces multi-turn safety erosion, organized around a refined three-level 'attention capacity competition hypothesis.' We build on DETAM's proof that inference-time attention reallocation improves safety (ASR 46%→1.2%) and ASGuard's demonstration that training-time head modification is feasible for specific vulnerabilities, testing whether CPL achieves broad attention reallocation through untargeted discourse training — addressing the progressive multi-turn erosion that DETAM (single-turn, requires runtime intent localization) and ASGuard (targets specific localizable circuits) structurally cannot. In multi-turn crescendo attacks, malicious intent is distributed across turns, making DETAM's intent-token identification ill-defined; CPL instead reduces the cumulative inertia that pushes systems past Johnson & Huo's tipping point. A novel Phase 0.5 provides the first per-head decomposition of diagonal attention (Wan et al. explicitly averages all heads) and measures overlap with safety-critical heads using triple triangulation (Ships score, DETAM sensitivity, AISA spatiotemporal analysis), cross-validated against published head sets (Zhou et al., Depth Charge, ASGuard — whose 4 Layer-13 vulnerable heads independently corroborate the continuation-safety nexus). Our five-phase causal design tests CPL against five confound controls including XGuard-Train SFT at both published and CPL-matched ranks. Mechanistic verification tests whether CPL achieves 'implicit DETAM' (same heads, same direction) and 'implicit circuit modification' (affecting ASGuard's identified vulnerable heads without targeting them). The study is designed for informative outcomes at all three competition levels, with the per-head diagonal attention decomposition, triple-method head identification comparison, and DETAM/ASGuard mechanistic comparison constituting standalone contributions.

## Core Problem
Multi-turn agent interactions exhibit systematic safety degradation (16% higher attack success rates), and while recent work has identified attention-level mechanisms — attention dispersion on safety keywords (ASJA, AAAI 2025), competition between safety and continuation heads (Deng et al., 2026), and attention reallocation as a defense (DETAM, ACL 2025 Findings) — and developed multi-turn safety defenses (MUSE-D turn-level DPO, EMNLP 2025; XGuard-Train SFT, COLM 2025; X-Boundary representation boundaries, EMNLP 2025; MTSA RL-based alignment, ACL 2025), and even training-time attention head interventions for specific vulnerability types (ASGuard circuit-targeted scaling, ICLR 2026), these studies are either attack-oriented, single-turn, operate at inference time, target specific localizable vulnerabilities, or train directly on safety-labeled data without testing whether discourse-level mechanisms causally drive safety erosion. Critically, DETAM (Li et al., ACL 2025 Findings) demonstrates that simply reallocating attention from attack tokens toward safety-relevant tokens at inference time — without any weight changes — reduces ASR from 46% to 1.2% on LLaMA-2, providing the strongest existing evidence that attention redistribution causally improves safety. Yet DETAM requires explicit identification of 'intent tokens' at runtime and operates only in single-turn settings — in multi-turn crescendo attacks where malicious intent is progressively distributed across turns, the notion of localizable 'intent tokens' breaks down fundamentally. ASGuard (Park et al., ICLR 2026) demonstrates that training-time modification of safety-relevant heads is feasible via circuit-targeted scaling vectors, but its efficacy 'hinges on localizable causal circuits' for specific attack types (tense jailbreaking) — multi-turn safety erosion through cumulative discourse dynamics may not produce such localizable circuits. No work has tested whether a training-time discourse intervention (reducing conversational inertia) achieves broad attention reallocation indirectly, nor whether the specific attention heads carrying diagonal inertia patterns overlap with safety-critical heads — a prerequisite for the softmax zero-sum competition mechanism to operate at the head level. Notably, the only characterization of diagonal attention (Wan et al., ICML 2026) reports aggregate-level patterns averaged across all heads; no per-head decomposition exists, leaving the head-level competition question empirically open. Additionally, the response-length confound in DPO-based interventions has never been explicitly controlled for in safety evaluations of discourse-level interventions.

## Opportunity
Six independent research threads have converged to make a controlled causal study newly feasible: (1) Conversational Inertia (Wan et al., ICML 2026) identifies diagonal attention where the i-th token attends to the i-th previous output position and provides Context Preference Learning (CPL) as a parameter-efficient intervention (0.4% params, LoRA rank-16 DPO with beta=0.01), validated on Qwen3-8B and Llama 3.1-8B-Instruct across eight agentic environments but never evaluated for safety — crucially, the diagonal attention pattern is characterized only at the aggregate level (averaged across all heads), so the per-head distribution remains unknown; (2) DETAM (Li et al., ACL 2025 Findings) provides direct causal evidence that attention reallocation toward safety-relevant tokens improves safety — reducing ASR by 97%+ without weight modification — but requires runtime intent token identification and is single-turn only, creating a fundamental limitation for multi-turn settings where intent is distributed across turns; (3) ASGuard (Park et al., ICLR 2026) demonstrates that training-time modification of safety-relevant attention heads is feasible via circuit-targeted channel-wise scaling vectors and preventative fine-tuning — crucially, ASGuard identifies 4 vulnerable heads at Layer 13 in Llama-3.1-8B (L13H8, L13H18, L13H25, L13H30), exactly where Deng et al. find continuation heads, providing independent corroboration that Layer 13 is a nexus of safety-relevant competition — but ASGuard targets specific localizable vulnerability circuits (tense jailbreaking) rather than discourse-level dynamics; (4) Multi-turn safety erosion is now well-benchmarked via MT-AgentRisk (365 tasks, 5 tools, avg 3.19 turns) with ToolShield as a defense baseline, and supplemented by OpenAgentSafety (ICLR 2026, 356 real-tool tasks with multi-turn multi-user dynamics); (5) Multi-turn safety training has mature baselines spanning multiple paradigms: XGuard-Train SFT (COLM 2025, up to 48.3% vulnerability reduction), MUSE-D turn-level DPO (EMNLP 2025, 24% ASR reduction), X-Boundary representation-level boundaries (EMNLP 2025, ASR reduction to 16-25%), and MTSA RL with future rewards (ACL 2025, ASR 74.5% to 23.5%) — but all train directly on safety-labeled data; (6) AISA (Song et al., arXiv:2602.13547) provides a third complementary method for localizing safety-critical attention heads via spatiotemporal analysis — identifying that safety-discriminative signals concentrate in middle-layer head outputs with K=16 heads achieving 0.92 detection accuracy — enabling methodological triangulation in our head overlap analysis. This six-thread convergence, combined with Johnson & Huo's (2026) formalization of attention competition tipping points and the layered distribution of safety mechanisms across layers 2-27, motivates a three-level attention capacity competition hypothesis testable through a novel Phase 0.5 head overlap analysis.

## Landscape
**Attention reallocation defenses:** DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562) is the most directly relevant inference-time prior work. It identifies attention heads sensitive to jailbreaks by computing attention score differences between successful and unsuccessful defenses (threshold alpha: 0.1 for LLaMA-2, 0.03 for Vicuna). During inference, it modifies the causal mask matrix by multiplying mask values at intent token positions by beta=5.0, amplifying attention to the user's core intention. DETAM reduces average ASR from 46.0% to 1.2% on LLaMA-2-7b-chat and from 81.8% to 4.0% on Vicuna-13b-v1.5. Cross-model transferability: sensitive heads from LLaMA-2 transferred to Meta-LLaMA-3 achieve 4% ASR vs. 96% vanilla. However, DETAM has three fundamental limitations for multi-turn agent settings: (a) it requires runtime identification of 'intent tokens' — in multi-turn crescendo attacks (Russinovich et al., USENIX Security 2025) where harmful intent is progressively distributed across turns, no single set of tokens constitutes 'the intent,' making DETAM's token-level localization fundamentally ill-defined; (b) it is tested only in single-turn settings and cannot address the cumulative attention shift across turns that Johnson & Huo's tipping point theory predicts; (c) it imposes per-turn computational overhead for mask modification in each forward pass across all turns of agent interaction. Our study tests whether CPL achieves DETAM-like attention redistribution persistently through training, addressing a failure mode DETAM structurally cannot: the gradual accumulation of continuation pressure across turns that progressively dilutes safety attention below the tipping point. **Training-time attention head intervention:** ASGuard (Park et al., ICLR 2026, arXiv:2509.25843) is the closest existing work to training-time attention head modification for safety. It uses Edge Attribution Patching with Integrated Gradients (EAP-IG) to identify attention heads causally linked to specific jailbreaking vulnerabilities, trains channel-wise activation scaling vectors (s_j ∈ R^{d_head}, applied via Hadamard product H'_{l,j} = H_{l,j} ⊙ s_j) on identified heads, and applies preventative fine-tuning with scaling vectors frozen. On tense jailbreaking, ASGuard reduces ASR from 42% to 8% on Llama-3.1-8B and 51% to 8% on Qwen2.5-7B, achieving Pareto-optimal safety-utility balance. Critically, ASGuard identifies 11 vulnerable heads in Llama-3.1-8B, of which 4 are at Layer 13 (L13H8, L13H18, L13H25, L13H30) — exactly where Deng et al. find continuation heads — providing independent corroboration that Layer 13 is a nexus of safety-relevant attention competition. However, ASGuard differs from our approach in three key ways: (a) it targets specific, localizable vulnerability circuits ('efficacy hinges on localizable causal circuits' — their Limitations, Section 7) — multi-turn safety erosion through cumulative discourse dynamics may not produce such localizable circuits, as the failure is progressive rather than circuit-specific; (b) it surgically fixes known attack types (tense jailbreaking, GCG, LogiBreak) one at a time, whereas CPL is an untargeted discourse intervention testing whether reducing general inertia achieves broad safety benefits; (c) it is single-turn only. ASGuard's success actually supports a key premise of our hypothesis: training-time modification of attention heads CAN improve safety. Our study tests whether indirect, untargeted discourse training achieves what targeted head intervention achieves — and whether it generalizes to the multi-turn progressive erosion that targeted approaches cannot address. **Safety head localization methods:** AISA (Song et al., arXiv:2602.13547) provides a third complementary approach to localizing safety-critical heads via spatiotemporal analysis — large-scale linear probing across 15 positions per layer identifies that attention head outputs demonstrate superior safety separability, with top-K=16 heads (concentrated in middle layers) achieving 0.92 detection accuracy and O(1) runtime overhead. AISA's finding that safety heads cluster in middle layers in standard models but shift toward higher layers in strongly safety-aligned models adds nuance to the competition hypothesis — the relevant layers may differ by alignment strength. **Attack-side mechanisms:** Du et al. (ASJA, AAAI 2025) show that successful multi-turn jailbreaks correlate with attention dispersion away from safety keywords (p=4.38e-07), achieving 44.9% higher ASR. Deng et al. (arXiv:2603.08234) identify competing safety and continuation attention heads — safety heads concentrated in layers 25-27, continuation heads in middle layers (~Layer 13) — whose antagonistic interaction determines jailbreak success. Notably, continuation heads at Layer 13 occupy the same layer range as both induction/copying mechanisms AND ASGuard's identified vulnerable heads, suggesting this layer is a critical nexus where diagonal attention patterns, continuation signals, and safety vulnerability converge. Depth Charge (Wu et al., arXiv:2603.05772, March 2026) introduces SAHA using Ablation-Impact Ranking and Layer-Wise Perturbation, achieving 82-91% ASR, revealing layer-specific safety head concentrations (layer 7 for Llama 3.1-8B, layer 5 for Qwen 1.5-7B, head 31 universally important) and sharp threshold behavior. Attention Eclipse (Zaree et al., arXiv:2502.15334) achieves 91.2% ASR by manipulating attention to strengthen harmful content focus and weaken safety focus. **Attention competition theory:** Johnson & Huo (arXiv:2602.14370, Feb 2026) formalize the competition-for-attention mechanism mathematically, showing that dot-product competition creates dynamical tipping points (n*) where behavior transitions from safe to unsafe — providing the theoretical framework for why cumulative inertia across turns can push the system past a tipping point that single-turn defenses like DETAM cannot prevent. **Multi-turn safety benchmarking:** Yang et al. (arXiv 2026) document 16% average ASR increase on MT-AgentRisk and propose ToolShield (~30% ASR reduction). OpenAgentSafety (ICLR 2026) provides 356 multi-turn, multi-user tasks with real tools. Li et al. (STAR, arXiv:2603.15684) show monotonic drift from refusal representations. MultiBreak (arXiv:2605.01687) provides 10,389 multi-turn adversarial prompts. **Multi-turn safety defenses:** X-Teaming (COLM 2025, arXiv:2504.13203) introduces XGuard-Train, a 30K multi-turn safety training dataset. Models SFT-trained on a 14K subset with LoRA rank-8, lr=1e-4, 3 epochs achieve up to 48.3% vulnerability reduction on Llama-3.1-8B and Qwen-2.5-7B. MUSE-D (EMNLP 2025, arXiv:2509.14651) applies turn-level DPO achieving 24% ASR reduction. X-Boundary (Lu et al., EMNLP 2025, arXiv:2502.09990) operates at the representation level, reducing multi-turn ASR from 58.5-76.0% to 16.0-25.0% while reducing over-refusal by ~20%. MTSA (Guo et al., ACL 2025, arXiv:2505.17147) performs RL with future rewards, reducing ASR from 74.5% to 23.5%, with the finding that maximum attack effectiveness peaks at round 5 — confirming multi-turn pressure accumulates through discourse dynamics. Agent Safety Alignment (Sha et al., arXiv:2507.08270) proposes unified sandboxed RL with benign/malicious/sensitive taxonomy. STREAM (arXiv:2506.00668) proposes safety reasoning moderator reducing ASR by 51.2%. TurnGate (arXiv:2605.05630) introduces turn-level harm detection. **Discourse dynamics:** Wan et al. (ICML 2026, arXiv:2602.03664; note: also submitted to ICLR 2026 as OpenReview #UubLs3lUfk, subsequently published in PMLR 306 at ICML 2026, Seoul, July 6-11) identify conversational inertia and propose CPL. The paper characterizes diagonal attention only at the aggregate level — explicitly stating 'All attention heads are averaged to create a unified attention matrix' and 'the trend of diagonal attention in the final layer is similar to other layers' — with no per-head decomposition. Code not released. **Safety attention head mechanisms:** Zhou et al. (ICLR 2025, arXiv:2410.13708) show the single most critical head in Llama-2-7B-Chat is Head (2, 26) at Layer 2. Wei et al. identify safety layers at layers 9-14. The refusal direction (Arditi et al.) is strongest around layer 15. Safety Alignment Should Be Made More Than Just A Few Attention Heads (arXiv:2508.19697) proposes distributed safety head training. **Safety persistence:** Plaut (arXiv:2603.02229) shows LoRA safety DPO persists with 90-94% retention, Pareto frontier R-squared=0.77, slope=-0.83. **DPO length bias:** Park et al. (2024) and Meng et al. (2024) document hidden length dependence. **Gap:** Despite convergent progress on inference-time attention reallocation (DETAM), training-time targeted head intervention (ASGuard), training-time safety defenses (XGuard-Train, MUSE-D, X-Boundary, MTSA), safety head localization (Zhou et al., AISA, Depth Charge), attention competition theory (Johnson & Huo), and discourse dynamics (conversational inertia), no work has: (a) tested whether a training-time discourse intervention achieves broad DETAM-like attention reallocation and causally reduces safety erosion in multi-turn settings — addressing the progressive accumulation that both DETAM (single-turn only) and ASGuard (circuit-specific only) cannot; (b) provided a per-head decomposition of diagonal attention to determine whether inertia heads overlap with safety heads; (c) compared discourse-targeted vs. safety-targeted training under matched parameter budgets; or (d) controlled for DPO response-length confounds in discourse-safety evaluations.

## Approach
We run a five-phase causal study on MT-AgentRisk (primary) and OpenAgentSafety (secondary) benchmarks using Qwen3-8B and Llama 3.1-8B-Instruct, organized around the 'attention capacity competition hypothesis' and motivated by a specific gap that neither DETAM nor ASGuard can address: progressive multi-turn safety erosion through cumulative discourse dynamics.

**Why Training-Time Discourse Intervention? The Multi-Turn Intent Distribution Problem.** DETAM achieves 97%+ ASR reduction in single-turn settings at zero training cost — but it requires identifying 'intent tokens' at runtime. In multi-turn crescendo attacks where harmful intent is progressively distributed across 3-10 turns (MTSA finds peak attack at round 5), no single set of tokens constitutes 'the intent.' The malicious instruction at turn 7 is only harmful in the context of the innocuous-seeming turns 1-6 that established the frame. DETAM cannot solve this because its mechanism — amplifying attention to intent tokens in sensitive heads — presupposes that intent is localizable within a single turn. ASGuard demonstrates training-time head modification is feasible but targets specific localizable circuits (tense jailbreaking), and its own Limitations section notes 'efficacy hinges on localizable causal circuits.' Multi-turn safety erosion through cumulative inertia is NOT a localizable circuit — it's a progressive process where each turn incrementally shifts the attention distribution. CPL's advantage is that it operates at the discourse dynamics level: reducing the cumulative inertia that progressively dilutes safety attention across turns, without needing to identify which tokens are 'intent' tokens or which circuits carry a specific vulnerability. It addresses the ROOT CAUSE (attention inertia accumulation across turns) rather than the SYMPTOM (misallocated attention at any single turn). This is the failure mode that Johnson & Huo's tipping point theory predicts: gradual accumulation of continuation pressure pushes the system past n* — and the only way to prevent reaching the tipping point is to reduce the per-turn accumulation rate, which is exactly what CPL does.

**The Attention Capacity Competition Hypothesis (Three-Level Framework):** We theorize that diagonal attention (the inertia mechanism) competes with safety-keyword attention at three distinct levels: **Level 1 (Head-level, strong form):** If diagonal attention and safety attention share the same heads, softmax's zero-sum constraint directly displaces safety-keyword attention. Given that safety heads span layers 2-27 and induction/copying mechanisms typically concentrate in middle layers, partial overlap is plausible. **Level 2 (Layer-level, medium form):** If diagonal and safety attention occupy different heads within the same or adjacent layers, competition occurs through the residual stream. This is supported by Deng et al.'s finding that continuation heads (Layer 13) antagonize safety heads (Layers 25-27), and strikingly corroborated by ASGuard's identification of 4 vulnerable heads at Layer 13 in Llama-3.1-8B (L13H8, L13H18, L13H25, L13H30) — the same layer where continuation heads reside, independently confirming Layer 13 as a nexus of safety-relevant competition. **Level 3 (Representation-level, weak form):** Competition mediated through accumulated representation drift, validated by X-Boundary's success (ASR 58.5% to 16.5%). Phase 0.5 empirically determines which level(s) apply.

**Phase 0 — CPL Acquisition/Reproduction + Baseline Preparation (weeks 1-3):** Contact Wan et al. for CPL checkpoints (ICML 2026 July 6-11). Simultaneously reproduce CPL using TRL DPOTrainer + PEFT: LoRA rank-16, alpha-16, 0.4% params, DPO with beta=0.01, sigmoid loss, 2 epochs, lr=5e-7, AdamW, 1000 preference pairs per environment. The training recipe maps directly to TRL v1.0+ (sigmoid loss is the default DPOConfig, all hyperparameters natively supported); the main reproduction risk is the preference pair construction pipeline (dual-rollout with long-context vs. short-context on AgentGym environments) rather than the training loop itself. Estimated: ~40 A100-hours per model. In parallel, prepare XGuard-Train SFT baselines: (a) LoRA rank-8 with lr=1e-4, 3 epochs (matching published configuration from X-Teaming, validated on Llama-3.1-8B and Qwen-2.5-7B); (b) LoRA rank-16 with CPL-matched hyperparameters for parameter-matched comparison. Construct extended-turn variants: prepend 4-6 benign tool-use turns to 50 representative MT-AgentRisk tasks.

**Hard Go/No-Go Checkpoint at Week 3:** The project proceeds to Phase 0.5 only if ALL criteria are met: (1) AgentGym environment setup working for >=3 of 8 environments (prioritizing ALFWorld, WebShop, HotpotQA); (2) dual-rollout preference pair generation produces pairs where long-context trajectories show measurably higher diagonal attention scores than short-context trajectories (statistically significant at p<0.05 on at least 2 environments); (3) DPO training pipeline converges (decreasing loss, increasing reward margins over 2 epochs); (4) base model evaluation on >=2 environments matches Wan et al.'s published baselines within 1 SEM. **Fallback paths:** (a) environment failure: proceed with 2-3 most reliable environments; (b) inertia differential failure: pivot to correlational-only study (Phases 1 and 4 only); (c) training failure: debug 1 additional week — if still failing by week 4, pivot to 'DETAM in multi-turn settings' (extending DETAM's mechanism to MT-AgentRisk, testing whether Focus Loss intensifies across turns).

**Phase 0.5 — Head Overlap Test and Per-Head Diagonal Attention Decomposition (weeks 3-4, ~20 A100-hours):** This phase provides the first per-head decomposition of diagonal attention patterns and tests the prerequisite assumption of the competition hypothesis. Using both base models on 50 MT-AgentRisk tasks: (a) **Novel per-head diagonal attention decomposition:** Compute diagonal attention scores per head (not just aggregate) using Wan et al.'s metric (attention between current output position i and previous assistant output position i +/- 5 tokens) — this is the first such decomposition, given that Wan et al. explicitly average all heads ('All attention heads are averaged to create a unified attention matrix'). Identify which heads carry the strongest diagonal patterns and their layer distribution. (b) **Safety head identification via triple triangulation:** Apply three complementary methods: (i) Ships score (Zhou et al., ICLR 2025) via KL divergence after head ablation; (ii) DETAM's sensitivity metric (attention score differences between successful/unsuccessful safety responses); (iii) AISA's spatiotemporal analysis — linear probing on head outputs at final structural tokens to identify safety-discriminative heads (K=16). Cross-validate against published localizations: Zhou et al.'s Head (2,26) for Llama-2-family; Depth Charge's layer-specific data (layer 7 for Llama 3.1-8B); ASGuard's EAP-IG identified heads (11 heads for Llama-3.1-8B including 4 at Layer 13). Using three independent methods plus cross-validation against three published head sets provides robust head identification. (c) **Overlap analysis:** Compute Jaccard index between top-k diagonal attention heads and top-k safety heads (k = 5, 10, 20, 50) with permutation tests. Also measure layer-level co-occurrence (same layer, different heads). Cross-reference against ASGuard's Layer 13 vulnerable heads — if diagonal attention heads concentrate at Layer 13, this would connect conversational inertia to the continuation-safety competition nexus identified by both Deng et al. and ASGuard independently. (d) **Level determination:** Level 1 (>30% head overlap) — proceed with strong per-head softmax hypothesis; Level 2 (same layers, <30% head overlap) — reformulate around residual stream competition, particularly the Layer 13 continuation-inertia-safety nexus; Level 3 (<10% overlap in both heads and layers) — reformulate around representation-level competition. Each determination shapes subsequent analysis. This phase costs ~20 A100-hours but de-risks the project and provides standalone novel contributions (first per-head diagonal attention map; first triple-method safety head identification comparison).

**Phase 1 — Correlational with Attention Capacity Analysis (weeks 4-7):** Measure diagonal attention (per-head, informed by Phase 0.5) AND safety-keyword attention concentration at each turn on 365 MT-AgentRisk tasks and 50 extended-turn variants. Calibrate analysis to competition level from Phase 0.5. Fit mixed-effects regressions testing P1 (diagonal attention negatively correlates with safety attention at the operative level), controlling for turn position, task category, model, and response token count. Test Granger causality for temporal dynamics.

**Phase 2 — Interventional with Confound Controls (weeks 7-11):** Apply CPL and re-evaluate on MT-AgentRisk. Five control conditions: (a) **Random-Preference LoRA** — shuffled preference labels, same architecture; (b) **Reversed-CPL** — prefer long-context over short-context; (c) **XGuard-Train SFT (rank-8)** — published configuration for validation against published results; (d) **XGuard-Train SFT (rank-16)** — CPL-matched parameters for direct paradigm comparison (discourse-targeted vs. safety-targeted training); (e) **Response-Length Analysis** — ASR stratified by length quartiles, per-100-token normalization, regression with length covariate (testing P3: CPL's safety effect, if any, is not explained by response-length changes). Frame CPL's effect relative to both DETAM and ASGuard: test whether CPL affects the same heads DETAM identifies as sensitive and shifts attention in the same direction (implicit DETAM test), and whether it affects ASGuard's identified vulnerable heads at Layer 13 (implicit untargeted circuit modification test). Compare against ToolShield baseline and MUSE-D's published results.

**Phase 3 — Autonomy Tax Audit (weeks 9-11, parallel):** Step-1 completion rate, cascade failure rate, end-to-end success, over-refusal. Report safety-competence Pareto frontier extending Plaut's analysis. Compare CPL's frontier position with X-Boundary's ~20% over-refusal reduction, ASGuard's Pareto-optimal balance, and XGuard-SFT's published results.

**Phase 4 — Mechanistic Verification (weeks 10-14):** (a) SRI signal framework for step-wise refusal dynamics; (b) Head-level analysis extending Deng et al.'s safety-continuation head identification to multi-turn, calibrated by Phase 0.5 overlap findings — test whether CPL modulates the Layer 13 continuation vs. Layer 25-27 safety head balance across conversation turns; (c) **DETAM-informed analysis:** Apply DETAM's sensitivity metric to CPL-treated models — does CPL training shift attention in the same heads and direction that DETAM targets at inference time? If so, CPL achieves 'implicit DETAM' through discourse training, but persistently and without runtime intent localization; (d) **ASGuard-informed analysis:** Test whether CPL affects ASGuard's identified vulnerable heads (particularly the 4 at Layer 13) despite not targeting them — this would demonstrate that untargeted discourse training can modify the same heads that targeted circuit analysis identifies, but as a side effect of reducing general inertia rather than through explicit circuit surgery; (e) Level-appropriate analysis: Level 2 — residual stream composition analysis at shared layers; Level 3 — representation trajectory analysis following X-Boundary's framework.

**Secondary Evaluation — OpenAgentSafety (weeks 12-14):** Best-performing config and XGuard-SFT on a subset for ecological validity.

**Null-Result Framing Strategy:** (1) First per-head decomposition of diagonal attention patterns and their overlap (or non-overlap) with safety heads — novel regardless of CPL results; (2) First triple-method safety head identification comparison (Ships + DETAM sensitivity + AISA spatiotemporal), cross-validated against three published head sets (Zhou et al., Depth Charge, ASGuard); (3) Empirical evidence for or against the three-level competition hierarchy; (4) First confound-controlled causal framework for discourse-safety evaluation; (5) First discourse-targeted vs. safety-targeted training comparison under matched parameters; (6) First multi-turn extension of DETAM's Focus Loss analysis; (7) Empirical test of whether CPL-like untargeted training affects the same heads as ASGuard's targeted circuit intervention.

**Extended-Turn Variant Validity (Limitation):** Acknowledged with mitigations: OpenAgentSafety for ecological validity, attention pattern validation, conservative amplification framing.

All primary experiments use MT-AgentRisk (365 tasks), ToolShield codebase (GitHub: CHATS-lab/ToolShield), XGuard-Train (HuggingFace: marslabucla/XGuard-Train), and the CPL training recipe from Wan et al. (ICML 2026).

## Resource Estimate
{'manual': {'gpu_hours': '720-900 A100-hours (CPL reproduction 2 models ~80h, XGuard-SFT rank-8 + rank-16 training 2 models ~60h, 2 control LoRAs for 2 models ~80h, Phase 0.5 head overlap test with AISA probing ~25h, MT-AgentRisk evaluation across 6 conditions x 2 models ~240h, extended-turn evaluation ~40h, OpenAgentSafety subset ~60h, SRI signal analysis ~30h, attention analysis including per-head diagonal decomposition + DETAM-informed + ASGuard-informed metrics ~85h, head-level safety-continuation analysis ~40h, response-length analysis ~10h)', 'timeline': '15-17 weeks (3 weeks Phase 0 + go/no-go, 1 week Phase 0.5, 3 weeks Phase 1, 4 weeks Phase 2 + Phase 3 parallel, 4 weeks Phase 4 + OpenAgentSafety, 3 weeks writing; comfortable for ICLR 2027)', 'estimated_gpu_cost': '$1080-1350 at $1.50/A100-hr spot pricing'}, 'human_in_loop': {'gpu_hours': '720-900 A100-hours', 'timeline': '13-15 weeks (Claude accelerates CPL reproduction, Phase 0.5 triple-method pipeline, DETAM/ASGuard comparison metrics, statistical analysis)', 'claude_api_cost': '$300-450 (CPL reproduction, per-head diagonal decomposition, triple-method head overlap analysis, DETAM/ASGuard-informed metrics, experiment orchestration, statistical modeling)', 'estimated_gpu_cost': '$1080-1350 at $1.50/A100-hr spot pricing'}, 'auto_research': {'gpu_hours': '920-1140 A100-hours (additional automated sweeps, full OpenAgentSafety evaluation, extended ablation across competition levels, comprehensive per-head analysis with triple methods)', 'timeline': '9-11 weeks (parallelized execution, automated Phase 0.5 -> Phase 1 pipeline)', 'claude_api_cost': '$600-850 (end-to-end orchestration including CPL reproduction, triple-method head analysis, DETAM/ASGuard comparison, control sweeps, result interpretation, draft generation)', 'estimated_gpu_cost': '$1380-1710 at $1.50/A100-hr spot pricing', 'speed_bottleneck': 'Sequential multi-turn interaction generation; 12 model configurations (2 models x 6 conditions); Phase 0.5 is a serial dependency before Phase 1; triple-method safety head analysis computationally intensive'}}

## Inspired By
Field guide Section 4 (cascading failures, production gap) + Section 5.2 (error propagation as primary bottleneck). Key insight: DETAM's demonstration that inference-time attention reallocation dramatically improves safety (ASR 46% to 1.2%) establishes the empirical foundation for our hypothesis — if explicitly redirecting attention works, does implicit redirection via discourse training also work? ASGuard's demonstration that training-time head modification is feasible for specific vulnerabilities raises the natural question: can untargeted discourse training achieve what targeted circuit intervention achieves, but for the progressive multi-turn erosion that circuit-based approaches cannot address? The three-level competition hierarchy was motivated by the finding that Wan et al. only characterizes diagonal attention at the aggregate level (explicitly averaging all heads into a unified matrix) and that safety heads span multiple layer ranges (L2, L9-14, L25-27), while continuation heads at Layer 13 overlap with both induction/copying head territory and ASGuard's identified vulnerable heads (4 of 11 Llama-3.1-8B vulnerable heads are at L13). Johnson & Huo's (2026) formalization of attention competition tipping points provides the theoretical framework for why cumulative discourse inertia can push multi-turn interactions past a safety threshold that per-turn defenses cannot prevent. The reviewer's observation about per-head specificity led to Phase 0.5, which provides the first per-head decomposition of diagonal attention — a novel contribution regardless of results. AISA's spatiotemporal analysis provides methodological triangulation for safety head identification, strengthening Phase 0.5's robustness.

## Target Venues
- ICLR 2027 (abstract September 19 2026, full paper September 24 2026 [estimated] — primary target, ~18 weeks from project start, comfortable timeline with 3+ weeks buffer including Phase 0.5)
- AAAI 2027 (abstract July 21 2026, full paper July 28 2026 — stretch target, ~10 weeks; feasible only if CPL checkpoints obtained by week 2, Phase 0.5 shows Level 1 or 2 overlap, and Phase 1 results are clean)

## Key References
- DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification (Li et al., ACL 2025 Findings, arXiv:2504.13562)
- ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack (Park et al., ICLR 2026, arXiv:2509.25843)
- AISA: Awakening Intrinsic Safety Awareness in Large Language Models against Jailbreak Attacks (Song et al., arXiv:2602.13547, Feb 2026)
- Multi-Turn Jailbreaking Large Language Models via Attention Shifting (ASJA, AAAI 2025)
- Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., ICML 2026, arXiv:2602.03664)
- Unsafer in Many Turns: Benchmarking and Defending Multi-Turn Safety Risks in Tool-Using Agents (Yang et al., arXiv 2026)
- X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents (COLM 2025, arXiv:2504.13203)
- MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety (EMNLP 2025, arXiv:2509.14651)
- X-Boundary: Establishing Exact Safety Boundary to Shield LLMs from Multi-Turn Jailbreaks without Compromising Usability (Lu et al., EMNLP 2025, arXiv:2502.09990)
- MTSA: Multi-turn Safety Alignment for LLMs through Multi-round Red-teaming (Guo et al., ACL 2025, arXiv:2505.17147)
- Agent Safety Alignment via Reinforcement Learning (Sha et al., arXiv:2507.08270)
- Safety Training Persists Through Helpfulness Optimization in LLM Agents (Plaut, arXiv:2603.02229, March 2026)
- The Struggle Between Continuation and Refusal (Deng et al., arXiv:2603.08234, Mar 2026)
- The Autonomy Tax: Defense Training Breaks LLM Agents (Li & Zhao, arXiv:2603.19423, Mar 2026)
- On the Role of Attention Heads in Large Language Model Safety (Zhou et al., ICLR 2025, arXiv:2410.13708)
- Depth Charge: Jailbreak Large Language Models from Deep Safety Attention Heads (Wu et al., arXiv:2603.05772, Mar 2026)
- Safety Alignment Should Be Made More Than Just A Few Attention Heads (Huang et al., arXiv:2508.19697, 2025)
- Competition for attention predicts good-to-bad tipping in AI (Johnson & Huo, arXiv:2602.14370, Feb 2026)
- Attention Eclipse: Manipulating Attention to Bypass LLM Safety-Alignment (Zaree et al., arXiv:2502.15334, Feb 2025)
- Safety Layers in Aligned Large Language Models (Wei et al., arXiv:2408.17003, 2024)
- Refusal in Language Models Is Mediated by a Single Direction (Arditi et al., arXiv:2406.11717, 2024)
- State-Dependent Safety Failures in Multi-Turn Language Model Interaction (STAR, arXiv:2603.15684, Mar 2026)
- OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety (ICLR 2026, arXiv:2507.06134)
- One Turn Too Late: Response-Aware Defense Against Hidden Malicious Intent in Multi-Turn Dialogue (TurnGate, arXiv:2605.05630, May 2026)
- MultiBreak: A Scalable and Diverse Multi-turn Jailbreak Benchmark (arXiv:2605.01687, May 2026)
- STREAM: SafeTy Reasoning Elicitation Alignment for Multi-Turn Dialogues (arXiv:2506.00668, May 2025)
- Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions (arXiv 2026)
- Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks (arXiv 2026)
- TRUTH DECAY: Quantifying Multi-Turn Sycophancy in Language Models (arXiv 2025)
- Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction (arXiv 2026)
- SafetyDrift: Predicting When AI Agents Cross the Line Before They Actually Do (arXiv 2026)
- Token Statistics Reveal Conversational Drift in Multi-turn LLM Interaction (arXiv 2026)
- Asking Forever: Universal Activations Behind Turn Amplification (arXiv:2602.17778, Feb 2026)
- Step-Wise Refusal Dynamics in Autoregressive and Diffusion Language Models (arXiv:2602.02600, Feb 2026)
- Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection (arXiv:2604.28129, Apr 2026)
- Many-Turn Jailbreaking (arXiv:2508.06755, Aug 2025)
- Disentangling Length from Quality in Direct Preference Optimization (Park et al., arXiv:2403.19159, 2024)
- Length Desensitization in Direct Preference Optimization (Meng et al., arXiv:2409.06411, 2024)
- Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack (Russinovich et al., USENIX Security 2025, arXiv:2404.01833)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "bcc9484c-086b-4bad-95dd-2a7e464a94a0",
  "type": "user",
  "uuid": "ff64822a-8de4-4070-b28b-035b9a3d6332",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:40:49.113Z_

```json
{
  "parentUuid": "ff64822a-8de4-4070-b28b-035b9a3d6332",
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
  "uuid": "949dc27a-bbdc-471f-93ac-295aec1592dc",
  "timestamp": "2026-05-20T03:40:49.113Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:40:49.113Z_

```json
{
  "parentUuid": "949dc27a-bbdc-471f-93ac-295aec1592dc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "91903bdc-6792-42cf-9adb-a209982c3d71",
  "timestamp": "2026-05-20T03:40:49.113Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Does Reducing Conversational Inertia Improve Multi-Turn Safety? Testing the Attention Capacity Competition Hypot…",
  "leafUuid": "91903bdc-6792-42cf-9adb-a209982c3d71",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Conversational inertia and multi-turn safety erosion",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:41:01.962Z_

<details><summary>Logged reasoning block</summary>

```text
This is a detailed research proposal about testing whether reducing conversational inertia (via CPL - Context Preference Learning) can improve multi-turn safety in LLMs. Let me break down the core idea before doing my research:

**Core Claim**: Diagonal attention patterns (conversational inertia) compete with safety-relevant attention in a zero-sum softmax competition. Reducing this inertia via CPL (a discourse-level training intervention) should causally reduce multi-turn safety erosion — addressing a gap that DETAM (single-turn, inference-time) and ASGuard (circuit-specific, single-turn) cannot.


I'm identifying the key novel contributions here: analyzing attention patterns at the individual head level rather than in aggregate, proposing a three-level framework for how attention capacity gets competed for, positioning CPL as an untargeted training approach that achieves similar effects to targeted attention modification, and designing the first empirical test of whether discourse-level interventions can actually improve safety across multiple turns. Now I should search the literature to see how this positions against existing work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91903bdc-6792-42cf-9adb-a209982c3d71",
  "isSidechain": false,
  "requestId": "req_011CbD8L6tbPSqa4QsZyRz3v",
  "type": "assistant",
  "uuid": "db4fb37b-dfd9-4977-9e6e-5fdb8ec6d837",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dkcvuiw477EuBJcxf6QR1D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14881,
      "cache_read_input_tokens": 11374,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 353,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 14881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14881
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

_source line 9 · 2026-05-20T03:41:01.975Z_

I need to do thorough literature research before I can evaluate this proposal. Let me search for the key papers and recent developments in this space.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db4fb37b-dfd9-4977-9e6e-5fdb8ec6d837",
  "isSidechain": false,
  "requestId": "req_011CbD8L6tbPSqa4QsZyRz3v",
  "type": "assistant",
  "uuid": "c97431ae-595c-4815-8d2c-55399e6a78d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dkcvuiw477EuBJcxf6QR1D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14881,
      "cache_read_input_tokens": 11374,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 353,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 14881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14881
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

_source line 10 · 2026-05-20T03:41:01.988Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011bGCudMoKSMUSmwC7CTpEa`</summary>

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
  "parentUuid": "c97431ae-595c-4815-8d2c-55399e6a78d3",
  "isSidechain": false,
  "requestId": "req_011CbD8L6tbPSqa4QsZyRz3v",
  "type": "assistant",
  "uuid": "2a3a6da5-d4db-49c7-9760-981789ab711d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dkcvuiw477EuBJcxf6QR1D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14881,
      "cache_read_input_tokens": 11374,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 353,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 14881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14881
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

_source line 11 · 2026-05-20T03:41:02.000Z_

<details><summary>↩ Tool result · `toolu_011bGCudMoKSMUSmwC7CTpEa`</summary>

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
  "parentUuid": "2a3a6da5-d4db-49c7-9760-981789ab711d",
  "isSidechain": false,
  "promptId": "bcc9484c-086b-4bad-95dd-2a7e464a94a0",
  "type": "user",
  "uuid": "365db560-2d8a-4e64-8e8d-b3f2188a455f",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "2a3a6da5-d4db-49c7-9760-981789ab711d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T03:41:04.807Z_

Now let me conduct thorough literature searches on the key topics in this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "365db560-2d8a-4e64-8e8d-b3f2188a455f",
  "isSidechain": false,
  "requestId": "req_011CbD8M32wzLxw3jguMY49k",
  "type": "assistant",
  "uuid": "935751de-dbaa-4e44-a7a9-fbfa2613849c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9NE7XpmPXVigBAkbSYeSR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 26255,
      "output_tokens": 349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 349,
          "cache_read_input_tokens": 26255,
          "cache_creation_input_tokens": 880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 880
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

_source line 13 · 2026-05-20T03:41:06.220Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DRLbKUa8Aq4mYoShKPuGxo`</summary>

```json
{
  "query": "Wan et al. \"conversational inertia\" \"context preference learning\" CPL diagonal attention ICML 2026 arXiv:2602.03664"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "935751de-dbaa-4e44-a7a9-fbfa2613849c",
  "isSidechain": false,
  "requestId": "req_011CbD8M32wzLxw3jguMY49k",
  "type": "assistant",
  "uuid": "bd2bee31-cc05-423e-86fb-c3d296f387fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9NE7XpmPXVigBAkbSYeSR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 26255,
      "output_tokens": 349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 349,
          "cache_read_input_tokens": 26255,
          "cache_creation_input_tokens": 880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 880
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

_source line 14 · 2026-05-20T03:41:06.697Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016rNVUMmprTsqoZqLC6XTT2`</summary>

```json
{
  "query": "DETAM \"targeted attention modification\" jailbreak defense Li et al. ACL 2025 arXiv:2504.13562"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd2bee31-cc05-423e-86fb-c3d296f387fa",
  "isSidechain": false,
  "requestId": "req_011CbD8M32wzLxw3jguMY49k",
  "type": "assistant",
  "uuid": "165e5864-4846-4ecd-a381-0b5a51c31482",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9NE7XpmPXVigBAkbSYeSR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 26255,
      "output_tokens": 349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 349,
          "cache_read_input_tokens": 26255,
          "cache_creation_input_tokens": 880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 880
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

_source line 15 · 2026-05-20T03:41:08.113Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UCnEGtmhwzj6oA4TjMRu2s`</summary>

```json
{
  "query": "ASGuard \"activation scaling guard\" jailbreaking ICLR 2026 Park et al. arXiv:2509.25843"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "165e5864-4846-4ecd-a381-0b5a51c31482",
  "isSidechain": false,
  "requestId": "req_011CbD8M32wzLxw3jguMY49k",
  "type": "assistant",
  "uuid": "c3fdc35d-11ce-42b9-a84a-4f88099b5bcf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9NE7XpmPXVigBAkbSYeSR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 26255,
      "output_tokens": 349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 349,
          "cache_read_input_tokens": 26255,
          "cache_creation_input_tokens": 880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 880
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

_source line 16 · 2026-05-20T03:41:08.579Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018czMC1FyjvkkQW8acwvJ3M`</summary>

```json
{
  "query": "multi-turn LLM safety attention mechanism 2025 2026 erosion defense training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3fdc35d-11ce-42b9-a84a-4f88099b5bcf",
  "isSidechain": false,
  "requestId": "req_011CbD8M32wzLxw3jguMY49k",
  "type": "assistant",
  "uuid": "053669d6-1c3d-4bca-b4f7-953fe2de6e5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9NE7XpmPXVigBAkbSYeSR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 26255,
      "output_tokens": 349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 349,
          "cache_read_input_tokens": 26255,
          "cache_creation_input_tokens": 880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 880
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

_source line 17 · 2026-05-20T03:41:09.438Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G1P6VfzjRnvXeeRyJt86ui`</summary>

```json
{
  "query": "Johnson Huo \"competition for attention\" tipping point AI safety arXiv:2602.14370"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "053669d6-1c3d-4bca-b4f7-953fe2de6e5a",
  "isSidechain": false,
  "requestId": "req_011CbD8M32wzLxw3jguMY49k",
  "type": "assistant",
  "uuid": "66f689f0-0827-4d62-a132-8fd73e72a5fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9NE7XpmPXVigBAkbSYeSR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 26255,
      "output_tokens": 349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 349,
          "cache_read_input_tokens": 26255,
          "cache_creation_input_tokens": 880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 880
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

_source line 18 · 2026-05-20T03:41:13.520Z_

<details><summary>↩ Tool result · `toolu_016rNVUMmprTsqoZqLC6XTT2`</summary>

```text
Web search results for query: "DETAM "targeted attention modification" jailbreak defense Li et al. ACL 2025 arXiv:2504.13562"

Links: [{"title":"DeTAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.613/"},{"title":"[2504.13562v1] DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification","url":"https://arxiv.org/abs/2504.13562v1"},{"title":"[2504.13562] DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification","url":"https://arxiv.org/abs/2504.13562"},{"title":"DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention   Modification","url":"https://arxiv.org/pdf/2504.13562"},{"title":"DeTAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification","url":"https://www.researchgate.net/publication/394272806_DeTAM_Defending_LLMs_Against_Jailbreak_Attacks_via_Targeted_Attention_Modification"},{"title":"DETAM: Defending LLMs Against Jailbreak Attacks via Targeted","url":"https://arxiv.org/pdf/2504.13562v1"}]

I found the paper you're looking for! Here's what I found:

**DeTAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification** is a paper by Yu Li, Han Jiang, and Zhihua Wei, published in the Findings of the Association for Computational Linguistics: ACL 2025. The paper is also available on arXiv as 2504.13562.

**Key aspects of the paper:**

DeTAM is a finetuning-free defense approach that improves the defensive capabilities against jailbreak attacks of LLMs via targeted attention modification. Specifically, the authors analyze the differences in attention scores between successful and unsuccessful defenses to identify the attention heads sensitive to jailbreak attacks. During inference, they reallocate attention to emphasize the user's core intention, minimizing interference from attack tokens.

**Results:**

The experimental results demonstrate that DETAM outperforms various baselines in jailbreak defense and exhibits robust generalization across different attacks and models, maintaining its effectiveness even on in-the-wild jailbreak data. The approach also incorporates over-defense datasets to validate its superior balance between helpfulness and harmlessness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "165e5864-4846-4ecd-a381-0b5a51c31482",
  "isSidechain": false,
  "promptId": "bcc9484c-086b-4bad-95dd-2a7e464a94a0",
  "type": "user",
  "uuid": "6fc08b9b-6fa8-40ab-89c5-00ea9f8dae33",
  "toolUseResult": {
    "query": "DETAM \"targeted attention modification\" jailbreak defense Li et al. ACL 2025 arXiv:2504.13562",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QmHexnz6RefrtwNrmyXeyE",
        "content": [
          {
            "title": "DeTAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-acl.613/"
          },
          {
            "title": "[2504.13562v1] DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification",
            "url": "https://arxiv.org/abs/2504.13562v1"
          },
          {
            "title": "[2504.13562] DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification",
            "url": "https://arxiv.org/abs/2504.13562"
          },
          {
            "title": "DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention   Modification",
            "url": "https://arxiv.org/pdf/2504.13562"
          },
          {
            "title": "DeTAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification",
            "url": "https://www.researchgate.net/publication/394272806_DeTAM_Defending_LLMs_Against_Jailbreak_Attacks_via_Targeted_Attention_Modification"
          },
          {
            "title": "DETAM: Defending LLMs Against Jailbreak Attacks via Targeted",
            "url": "https://arxiv.org/pdf/2504.13562v1"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found:\n\n**DeTAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification** is a paper by Yu Li, Han Jiang, and Zhihua Wei, published in the Findings of the Association for Computational Linguistics: ACL 2025. The paper is also available on arXiv as 2504.13562.\n\n**Key aspects of the paper:**\n\nDeTAM is a finetuning-free defense approach that improves the defensive capabilities against jailbreak attacks of LLMs via targeted attention modification. Specifically, the authors analyze the differences in attention scores between successful and unsuccessful defenses to identify the attention heads sensitive to jailbreak attacks. During inference, they reallocate attention to emphasize the user's core intention, minimizing interference from attack tokens.\n\n**Results:**\n\nThe experimental results demonstrate that DETAM outperforms various baselines in jailbreak defense and exhibits robust generalization across different attacks and models, maintaining its effectiveness even on in-the-wild jailbreak data. The approach also incorporates over-defense datasets to validate its superior balance between helpfulness and harmlessness."
    ],
    "durationSeconds": 6.8193787760000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "165e5864-4846-4ecd-a381-0b5a51c31482",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T03:41:13.631Z_

<details><summary>↩ Tool result · `toolu_01DRLbKUa8Aq4mYoShKPuGxo`</summary>

```text
Web search results for query: "Wan et al. "conversational inertia" "context preference learning" CPL diagonal attention ICML 2026 arXiv:2602.03664"

Links: [{"title":"Mitigating Conversational Inertia in Multi-Turn Agents","url":"https://arxiv.org/html/2602.03664v2"},{"title":"Mitigating Conversational Inertia in Multi-Turn Agents","url":"https://arxiv.org/pdf/2602.03664"},{"title":"Learning in Context, Guided by Choice: A Reward-Free Paradigm for Reinforcement Learning with Transformers","url":"https://arxiv.org/html/2602.08244"},{"title":"Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction","url":"https://arxiv.org/pdf/2603.04783"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"}]

Based on the search results, I found the paper you're looking for:

The paper is titled "Mitigating Conversational Inertia in Multi-Turn Agents" by Yang Wan, Zheng Cao, Zhenhao Zhang, Zhengwen Zeng, Shuheng Shen, Changhua Meng, and Linchao Zhu.

Here are the key aspects of the paper:

**Main Problem:** The paper identifies "conversational inertia," a phenomenon where models exhibit strong diagonal attention to previous responses, which is associated with imitation bias that constrains exploration.

**Core Insight:** For identical states, actions generated with longer contexts exhibit stronger inertia than those with shorter contexts, enabling construction of preference pairs without environment rewards.

**Proposed Solution:** The authors propose Context Preference Learning (CPL) to calibrate model preferences to favor low-inertia responses over high-inertia ones, and further provide context management strategies at inference time to balance exploration and exploitation.

**Results:** Context Preference Learning significantly reduces diagonal attention by over 10% across all context management methods, and experimental results across eight agentic environments and one deep research scenario validate that the framework reduces conversational inertia and achieves performance improvements.

The paper (arXiv:2602.03664) was published on February 5, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd2bee31-cc05-423e-86fb-c3d296f387fa",
  "isSidechain": false,
  "promptId": "bcc9484c-086b-4bad-95dd-2a7e464a94a0",
  "type": "user",
  "uuid": "3245ecc9-5717-4b33-aff2-3559ed106226",
  "toolUseResult": {
    "query": "Wan et al. \"conversational inertia\" \"context preference learning\" CPL diagonal attention ICML 2026 arXiv:2602.03664",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BJCDdxoEcAQVpbqtKKWZzV",
        "content": [
          {
            "title": "Mitigating Conversational Inertia in Multi-Turn Agents",
            "url": "https://arxiv.org/html/2602.03664v2"
          },
          {
            "title": "Mitigating Conversational Inertia in Multi-Turn Agents",
            "url": "https://arxiv.org/pdf/2602.03664"
          },
          {
            "title": "Learning in Context, Guided by Choice: A Reward-Free Paradigm for Reinforcement Learning with Transformers",
            "url": "https://arxiv.org/html/2602.08244"
          },
          {
            "title": "Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction",
            "url": "https://arxiv.org/pdf/2603.04783"
          },
          {
            "title": "ICLR 2026 Orals",
            "url": "https://iclr.cc/virtual/2026/events/oral"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper is titled \"Mitigating Conversational Inertia in Multi-Turn Agents\" by Yang Wan, Zheng Cao, Zhenhao Zhang, Zhengwen Zeng, Shuheng Shen, Changhua Meng, and Linchao Zhu.\n\nHere are the key aspects of the paper:\n\n**Main Problem:** The paper identifies \"conversational inertia,\" a phenomenon where models exhibit strong diagonal attention to previous responses, which is associated with imitation bias that constrains exploration.\n\n**Core Insight:** For identical states, actions generated with longer contexts exhibit stronger inertia than those with shorter contexts, enabling construction of preference pairs without environment rewards.\n\n**Proposed Solution:** The authors propose Context Preference Learning (CPL) to calibrate model preferences to favor low-inertia responses over high-inertia ones, and further provide context management strategies at inference time to balance exploration and exploitation.\n\n**Results:** Context Preference Learning significantly reduces diagonal attention by over 10% across all context management methods, and experimental results across eight agentic environments and one deep research scenario validate that the framework reduces conversational inertia and achieves performance improvements.\n\nThe paper (arXiv:2602.03664) was published on February 5, 2026."
    ],
    "durationSeconds": 7.405743706000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bd2bee31-cc05-423e-86fb-c3d296f387fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T03:41:15.287Z_

<details><summary>↩ Tool result · `toolu_01UCnEGtmhwzj6oA4TjMRu2s`</summary>

```text
Web search results for query: "ASGuard "activation scaling guard" jailbreaking ICLR 2026 Park et al. arXiv:2509.25843"

Links: [{"title":"ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack","url":"https://arxiv.org/html/2509.25843"},{"title":"[2509.25843] ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack","url":"https://arxiv.org/abs/2509.25843"},{"title":"ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack | alphaXiv","url":"https://www.alphaxiv.org/abs/2509.25843"},{"title":"ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack","url":"https://arxiv.org/pdf/2509.25843"},{"title":"ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack | OpenReview","url":"https://openreview.net/forum?id=wmiEXNEXPs"},{"title":"Published as a conference paper at ICLR 2026 ASGUARD: ACTIVATION-SCALING GUARD","url":"https://openreview.net/pdf/2a38643513d111bd2fd478b5ed972d61e6a18ee9.pdf"},{"title":"(PDF) ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack","url":"https://www.researchgate.net/publication/396048977_ASGuard_Activation-Scaling_Guard_to_Mitigate_Targeted_Jailbreaking_Attack"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

ASGuard (Activation-Scaling Guard) is an insightful, mechanistically-informed framework that surgically mitigates targeted jailbreaking vulnerabilities. The paper is authored by Yein Park, Jungwoo Park, and Jaewoo Kang from Korea University and AIGEN Sciences.

**Main Approach:**

The research addresses how safety-aligned LLMs exhibit brittle refusal behaviors that can be circumvented by simple linguistic changes, such as tense jailbreaking where models often comply with harmful requests when rephrased in past tense.

The method works in three steps:
1. Circuit analysis is used to identify specific attention heads causally linked to targeted jailbreaking such as a tense-changing attack
2. A precise, channel-wise scaling vector is trained to recalibrate the activation of tense vulnerable heads
3. This is applied into a "preventative fine-tuning", forcing the model to learn a more robust refusal mechanism

**Results:**

Across four LLMs, ASGuard effectively reduces the attack success rate of targeted jailbreaking while preserving general capabilities and minimizing over refusal, achieving a Pareto-optimal balance between safety and utility.

The paper has been published as a conference paper at ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3fdc35d-11ce-42b9-a84a-4f88099b5bcf",
  "isSidechain": false,
  "promptId": "bcc9484c-086b-4bad-95dd-2a7e464a94a0",
  "type": "user",
  "uuid": "534f15b8-b3e5-4375-a269-fdd519b5fdf8",
  "toolUseResult": {
    "query": "ASGuard \"activation scaling guard\" jailbreaking ICLR 2026 Park et al. arXiv:2509.25843",
    "results": [
      {
        "tool_use_id": "srvtoolu_014NDdXJSnQEpAQPbwhcY2qZ",
        "content": [
          {
            "title": "ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack",
            "url": "https://arxiv.org/html/2509.25843"
          },
          {
            "title": "[2509.25843] ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack",
            "url": "https://arxiv.org/abs/2509.25843"
          },
          {
            "title": "ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2509.25843"
          },
          {
            "title": "ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack",
            "url": "https://arxiv.org/pdf/2509.25843"
          },
          {
            "title": "ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack | OpenReview",
            "url": "https://openreview.net/forum?id=wmiEXNEXPs"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 ASGUARD: ACTIVATION-SCALING GUARD",
            "url": "https://openreview.net/pdf/2a38643513d111bd2fd478b5ed972d61e6a18ee9.pdf"
          },
          {
            "title": "(PDF) ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack",
            "url": "https://www.researchgate.net/publication/396048977_ASGuard_Activation-Scaling_Guard_to_Mitigate_Targeted_Jailbreaking_Attack"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what I found:\n\nASGuard (Activation-Scaling Guard) is an insightful, mechanistically-informed framework that surgically mitigates targeted jailbreaking vulnerabilities. The paper is authored by Yein Park, Jungwoo Park, and Jaewoo Kang from Korea University and AIGEN Sciences.\n\n**Main Approach:**\n\nThe research addresses how safety-aligned LLMs exhibit brittle refusal behaviors that can be circumvented by simple linguistic changes, such as tense jailbreaking where models often comply with harmful requests when rephrased in past tense.\n\nThe method works in three steps:\n1. Circuit analysis is used to identify specific attention heads causally linked to targeted jailbreaking such as a tense-changing attack\n2. A precise, channel-wise scaling vector is trained to recalibrate the activation of tense vulnerable heads\n3. This is applied into a \"preventative fine-tuning\", forcing the model to learn a more robust refusal mechanism\n\n**Results:**\n\nAcross four LLMs, ASGuard effectively reduces the attack success rate of targeted jailbreaking while preserving general capabilities and minimizing over refusal, achieving a Pareto-optimal balance between safety and utility.\n\nThe paper has been published as a conference paper at ICLR 2026."
    ],
    "durationSeconds": 7.168623131999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c3fdc35d-11ce-42b9-a84a-4f88099b5bcf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T03:41:17.763Z_

<details><summary>↩ Tool result · `toolu_018czMC1FyjvkkQW8acwvJ3M`</summary>

```text
Web search results for query: "multi-turn LLM safety attention mechanism 2025 2026 erosion defense training"

Links: [{"title":"Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak","url":"https://arxiv.org/pdf/2507.07146"},{"title":"SafeTy Reasoning Elicitation Alignment for Multi-Turn Dialogues","url":"https://arxiv.org/pdf/2506.00668"},{"title":"Attention Mechanism in LLMs Explained (2026)","url":"https://www.buildfastwithai.com/blogs/attention-mechanism-llm-explained"},{"title":"MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety","url":"https://arxiv.org/pdf/2602.01539"},{"title":"MTSA: Multi-turn Safety Alignment for LLMs through Multi-round Red-teaming","url":"https://arxiv.org/pdf/2505.17147"},{"title":"Speak Out of Turn: Safety Vulnerability of Large Language Models in   Multi-turn Dialogue","url":"https://arxiv.org/pdf/2402.17262"},{"title":"X-Boundary: Establishing Exact Safety Boundary to Shield LLMs from Multi-Turn Jailbreaks without Compromising Usability","url":"https://arxiv.org/pdf/2502.09990"}]

Here are the search results for multi-turn LLM safety with attention mechanisms and defense training from 2025-2026:

## Key Findings:

**Multi-Turn Attack Vulnerabilities:**
Multi-turn attacks can gradually guide LLMs toward generating responses aligned with an attacker's intent, with adversaries strategically misleading models across multiple conversational turns to conceal malicious goals. Traditional LM-based safeguard mechanisms often fail to detect these gradual manipulations, as individual queries may appear benign when viewed in isolation.

**Defense Training Approaches:**
Prior research has focused on enhancing model safety by fine-tuning LLMs on unanswerable queries, training them to issue appropriate refusals, and releasing multi-turn safety training datasets. More recent work includes introducing multiturn reinforcement learning algorithms based on future rewards to improve the robustness of safety alignment.

**Attention-Based Defenses:**
Research has developed attention-aware approaches using GNN-based input defense against multi-turn jailbreaks, which leverages attention mechanisms to detect and block attacks across conversational turns.

**Advanced Defense Methods:**
MAGIC (Multi-Agent Adversarial Game for Improving safety and Compliance) is a novel multi-turn multi-agent reinforcement learning framework. Additionally, recent comprehensive comparisons of defense methods including supervised fine-tuning, Direct Preference Optimization, Gradient Ascent, and circuit breaking show these reduce attack success rates but compromise usability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "053669d6-1c3d-4bca-b4f7-953fe2de6e5a",
  "isSidechain": false,
  "promptId": "bcc9484c-086b-4bad-95dd-2a7e464a94a0",
  "type": "user",
  "uuid": "73ee6fdb-7518-4c0f-ab25-32e2bffb122f",
  "toolUseResult": {
    "query": "multi-turn LLM safety attention mechanism 2025 2026 erosion defense training",
    "results": [
      {
        "tool_use_id": "srvtoolu_018VDLWhJ7BGZ4Jkigbkpjdx",
        "content": [
          {
            "title": "Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak",
            "url": "https://arxiv.org/pdf/2507.07146"
          },
          {
            "title": "SafeTy Reasoning Elicitation Alignment for Multi-Turn Dialogues",
            "url": "https://arxiv.org/pdf/2506.00668"
          },
          {
            "title": "Attention Mechanism in LLMs Explained (2026)",
            "url": "https://www.buildfastwithai.com/blogs/attention-mechanism-llm-explained"
          },
          {
            "title": "MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety",
            "url": "https://arxiv.org/pdf/2602.01539"
          },
          {
            "title": "MTSA: Multi-turn Safety Alignment for LLMs through Multi-round Red-teaming",
            "url": "https://arxiv.org/pdf/2505.17147"
          },
          {
            "title": "Speak Out of Turn: Safety Vulnerability of Large Language Models in   Multi-turn Dialogue",
            "url": "https://arxiv.org/pdf/2402.17262"
          },
          {
            "title": "X-Boundary: Establishing Exact Safety Boundary to Shield LLMs from Multi-Turn Jailbreaks without Compromising Usability",
            "url": "https://arxiv.org/pdf/2502.09990"
          }
        ]
      },
      "Here are the search results for multi-turn LLM safety with attention mechanisms and defense training from 2025-2026:\n\n## Key Findings:\n\n**Multi-Turn Attack Vulnerabilities:**\nMulti-turn attacks can gradually guide LLMs toward generating responses aligned with an attacker's intent, with adversaries strategically misleading models across multiple conversational turns to conceal malicious goals. Traditional LM-based safeguard mechanisms often fail to detect these gradual manipulations, as individual queries may appear benign when viewed in isolation.\n\n**Defense Training Approaches:**\nPrior research has focused on enhancing model safety by fine-tuning LLMs on unanswerable queries, training them to issue appropriate refusals, and releasing multi-turn safety training datasets. More recent work includes introducing multiturn reinforcement learning algorithms based on future rewards to improve the robustness of safety alignment.\n\n**Attention-Based Defenses:**\nResearch has developed attention-aware approaches using GNN-based input defense against multi-turn jailbreaks, which leverages attention mechanisms to detect and block attacks across conversational turns.\n\n**Advanced Defense Methods:**\nMAGIC (Multi-Agent Adversarial Game for Improving safety and Compliance) is a novel multi-turn multi-agent reinforcement learning framework. Additionally, recent comprehensive comparisons of defense methods including supervised fine-tuning, Direct Preference Optimization, Gradient Ascent, and circuit breaking show these reduce attack success rates but compromise usability."
    ],
    "durationSeconds": 9.179914925,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "053669d6-1c3d-4bca-b4f7-953fe2de6e5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Does Reducing Conversational Inertia Improve Multi-Turn Safety? Testing the Attention Capacity Competition Hypot…",
  "leafUuid": "73ee6fdb-7518-4c0f-ab25-32e2bffb122f",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Conversational inertia and multi-turn safety erosion",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236"
}
```

---

### Tool result

_source line 24 · 2026-05-20T03:41:18.934Z_

<details><summary>↩ Tool result · `toolu_01G1P6VfzjRnvXeeRyJt86ui`</summary>

```text
Web search results for query: "Johnson Huo "competition for attention" tipping point AI safety arXiv:2602.14370"

Links: [{"title":"[2602.14370] Competition for attention predicts good-to-bad tipping in AI","url":"https://arxiv.org/abs/2602.14370"},{"title":"Competition for attention predicts good-to-bad tipping in AI","url":"https://arxiv.org/html/2602.14370v1"},{"title":"Competition for attention predicts good-to-bad tipping in AI","url":"https://arxiv.org/pdf/2602.14370"},{"title":"[2504.20980] Jekyll-and-Hyde Tipping Point in an AI's Behavior","url":"https://arxiv.org/abs/2504.20980"},{"title":"Multispin Physics of AI Tipping Points and Hallucinations","url":"https://arxiv.org/html/2508.01097v1"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** Competition for attention predicts good-to-bad tipping in AI

**Authors:** Neil F. Johnson and Frank Yingjie Huo from George Washington University

**Core Contribution:** The paper shows that a large class of potentially dangerous tipping originates at the atomistic scale in edge AI due to competition for the machinery's attention, yielding a mathematical formula for the dynamical tipping point n*, governed by dot-product competition for attention between the conversation's context and competing output basins.

**Motivation:** More than half the global population carries devices that can run ChatGPT-like language models with no Internet connection and minimal safety oversight, while existing safety tools either require cloud connectivity or discover failures only after harm has occurred.

**Scope:** The mechanism is validated against multiple phone-scale AI models and can be instantiated for different definitions of 'good' and 'bad', applying across domains like health, law, finance, and defense.

The paper was published on February 24, 2026 (arXiv:2602.14370).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66f689f0-0827-4d62-a132-8fd73e72a5fb",
  "isSidechain": false,
  "promptId": "bcc9484c-086b-4bad-95dd-2a7e464a94a0",
  "type": "user",
  "uuid": "941dede1-64c8-4af5-acdd-4bcf83dcd957",
  "toolUseResult": {
    "query": "Johnson Huo \"competition for attention\" tipping point AI safety arXiv:2602.14370",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QJjRbeV3x1BshJV4bQYE92",
        "content": [
          {
            "title": "[2602.14370] Competition for attention predicts good-to-bad tipping in AI",
            "url": "https://arxiv.org/abs/2602.14370"
          },
          {
            "title": "Competition for attention predicts good-to-bad tipping in AI",
            "url": "https://arxiv.org/html/2602.14370v1"
          },
          {
            "title": "Competition for attention predicts good-to-bad tipping in AI",
            "url": "https://arxiv.org/pdf/2602.14370"
          },
          {
            "title": "[2504.20980] Jekyll-and-Hyde Tipping Point in an AI's Behavior",
            "url": "https://arxiv.org/abs/2504.20980"
          },
          {
            "title": "Multispin Physics of AI Tipping Points and Hallucinations",
            "url": "https://arxiv.org/html/2508.01097v1"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n**Paper Title:** Competition for attention predicts good-to-bad tipping in AI\n\n**Authors:** Neil F. Johnson and Frank Yingjie Huo from George Washington University\n\n**Core Contribution:** The paper shows that a large class of potentially dangerous tipping originates at the atomistic scale in edge AI due to competition for the machinery's attention, yielding a mathematical formula for the dynamical tipping point n*, governed by dot-product competition for attention between the conversation's context and competing output basins.\n\n**Motivation:** More than half the global population carries devices that can run ChatGPT-like language models with no Internet connection and minimal safety oversight, while existing safety tools either require cloud connectivity or discover failures only after harm has occurred.\n\n**Scope:** The mechanism is validated against multiple phone-scale AI models and can be instantiated for different definitions of 'good' and 'bad', applying across domains like health, law, finance, and defense.\n\nThe paper was published on February 24, 2026 (arXiv:2602.14370)."
    ],
    "durationSeconds": 9.489139314999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "66f689f0-0827-4d62-a132-8fd73e72a5fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-20T03:41:22.530Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've confirmed the key papers exist. Now let me search for more specific aspects - particularly the AISA paper, Deng et al., and any work that might already bridge the gap this proposal claims to fill.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "941dede1-64c8-4af5-acdd-4bcf83dcd957",
  "isSidechain": false,
  "requestId": "req_011CbD8NHFjjKb8yzPLmNCDq",
  "type": "assistant",
  "uuid": "2017ecc7-71a0-42bb-b214-58823022f91b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dtimy8ZvSJFMVMYdBmubEa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3685,
      "cache_read_input_tokens": 27135,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 27135,
          "cache_creation_input_tokens": 3685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3685
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

_source line 26 · 2026-05-20T03:41:23.659Z_

Good, the key papers are verified. Let me now search for more specific aspects and potential competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2017ecc7-71a0-42bb-b214-58823022f91b",
  "isSidechain": false,
  "requestId": "req_011CbD8NHFjjKb8yzPLmNCDq",
  "type": "assistant",
  "uuid": "af1ff68b-e6cc-4fb0-ac41-28e7dda411ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dtimy8ZvSJFMVMYdBmubEa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3685,
      "cache_read_input_tokens": 27135,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 27135,
          "cache_creation_input_tokens": 3685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3685
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

_source line 27 · 2026-05-20T03:41:24.464Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N4CKsHjF4ypXLvExzfKGPu`</summary>

```json
{
  "query": "AISA \"intrinsic safety awareness\" Song et al. attention head safety arXiv:2602.13547 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af1ff68b-e6cc-4fb0-ac41-28e7dda411ae",
  "isSidechain": false,
  "requestId": "req_011CbD8NHFjjKb8yzPLmNCDq",
  "type": "assistant",
  "uuid": "ab65ba3b-aea2-42f2-9a9a-3f000f0def1e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dtimy8ZvSJFMVMYdBmubEa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3685,
      "cache_read_input_tokens": 27135,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 27135,
          "cache_creation_input_tokens": 3685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3685
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

_source line 28 · 2026-05-20T03:41:25.414Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NKbizLWv6adCPwieTqetgK`</summary>

```json
{
  "query": "Deng et al. \"continuation and refusal\" safety heads continuation heads attention 2026 arXiv:2603.08234"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab65ba3b-aea2-42f2-9a9a-3f000f0def1e",
  "isSidechain": false,
  "requestId": "req_011CbD8NHFjjKb8yzPLmNCDq",
  "type": "assistant",
  "uuid": "7ac4654b-4bc2-4877-848d-75d3d5cdc2d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dtimy8ZvSJFMVMYdBmubEa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3685,
      "cache_read_input_tokens": 27135,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 27135,
          "cache_creation_input_tokens": 3685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3685
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

_source line 29 · 2026-05-20T03:41:26.297Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YSsYspn1S5rahYqFHs4iTq`</summary>

```json
{
  "query": "\"discourse training\" OR \"conversational inertia\" safety multi-turn LLM attention reallocation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ac4654b-4bc2-4877-848d-75d3d5cdc2d5",
  "isSidechain": false,
  "requestId": "req_011CbD8NHFjjKb8yzPLmNCDq",
  "type": "assistant",
  "uuid": "6ab5c291-8d6a-496e-9f3a-64abc7758fa2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dtimy8ZvSJFMVMYdBmubEa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3685,
      "cache_read_input_tokens": 27135,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 27135,
          "cache_creation_input_tokens": 3685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3685
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

_source line 30 · 2026-05-20T03:41:32.121Z_

<details><summary>↩ Tool result · `toolu_01NKbizLWv6adCPwieTqetgK`</summary>

```text
Web search results for query: "Deng et al. "continuation and refusal" safety heads continuation heads attention 2026 arXiv:2603.08234"

Links: [{"title":"[2603.08234] The Struggle Between Continuation and Refusal: A Mechanistic Analysis of the Continuation-Triggered Jailbreak in LLMs","url":"https://arxiv.org/abs/2603.08234"},{"title":"The Struggle Between Continuation and Refusal: A Mechanistic Analysis of the Continuation-Triggered Jailbreak in LLMs","url":"https://arxiv.org/html/2603.08234"},{"title":"The Struggle Between Continuation and Refusal: A Mechanistic Analysis of the Continuation-Triggered Jailbreak in LLMs","url":"https://arxiv.org/pdf/2603.08234"},{"title":"Safety Alignment Should Be Made More Than Just A Few Attention Heads","url":"https://arxiv.org/pdf/2508.19697"},{"title":"[2603.05773v1] Knowing without Acting: The Disentangled Geometry of Safety Mechanisms in Large Language Models","url":"https://arxiv.org/abs/2603.05773v1"}]

I found the paper! Here are the search results:

The paper by Deng et al. (arXiv:2603.08234) focuses on a continuation-triggered jailbreak phenomenon where relocating a continuation-triggered instruction suffix can substantially increase jailbreak success rates, and they conduct a comprehensive mechanistic interpretability analysis at the level of attention heads.

Through causal interventions and activation scaling, the authors show that this jailbreak behavior primarily arises from an inherent competition between the model's intrinsic continuation drive and the safety defenses acquired through alignment training.

The paper includes a detailed behavioral analysis of safety-critical attention heads, revealing notable differences in the functions and behaviors of safety heads across different model architectures.

These findings provide a novel mechanistic perspective for understanding and interpreting jailbreak behaviors in LLMs, offering both theoretical insights and practical implications for improving model safety.

The paper was published on March 9, 2026, and is authored by Yonghong Deng and colleagues from Beijing Institute of Technology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ac4654b-4bc2-4877-848d-75d3d5cdc2d5",
  "isSidechain": false,
  "promptId": "bcc9484c-086b-4bad-95dd-2a7e464a94a0",
  "type": "user",
  "uuid": "ace49bd3-310e-42b8-a7c5-ff07e4bb60a9",
  "toolUseResult": {
    "query": "Deng et al. \"continuation and refusal\" safety heads continuation heads attention 2026 arXiv:2603.08234",
    "results": [
      {
        "tool_use_id": "srvtoolu_016HBDnzCqhLNoopX5NDZgWz",
        "content": [
          {
            "title": "[2603.08234] The Struggle Between Continuation and Refusal: A Mechanistic Analysis of the Continuation-Triggered Jailbreak in LLMs",
            "url": "https://arxiv.org/abs/2603.08234"
          },
          {
            "title": "The Struggle Between Continuation and Refusal: A Mechanistic Analysis of the Continuation-Triggered Jailbreak in LLMs",
            "url": "https://arxiv.org/html/2603.08234"
          },
          {
            "title": "The Struggle Between Continuation and Refusal: A Mechanistic Analysis of the Continuation-Triggered Jailbreak in LLMs",
            "url": "https://arxiv.org/pdf/2603.08234"
          },
          {
            "title": "Safety Alignment Should Be Made More Than Just A Few Attention Heads",
            "url": "https://arxiv.org/pdf/2508.19697"
          },
          {
            "title": "[2603.05773v1] Knowing without Acting: The Disentangled Geometry of Safety Mechanisms in Large Language Models",
            "url": "https://arxiv.org/abs/2603.05773v1"
          }
        ]
      },
      "I found the paper! Here are the search results:\n\nThe paper by Deng et al. (arXiv:2603.08234) focuses on a continuation-triggered jailbreak phenomenon where relocating a continuation-triggered instruction suffix can substantially increase jailbreak success rates, and they conduct a comprehensive mechanistic interpretability analysis at the level of attention heads.\n\nThrough causal interventions and activation scaling, the authors show that this jailbreak behavior primarily arises from an inherent competition between the model's intrinsic continuation drive and the safety defenses acquired through alignment training.\n\nThe paper includes a detailed behavioral analysis of safety-critical attention heads, revealing notable differences in the functions and behaviors of safety heads across different model architectures.\n\nThese findings provide a novel mechanistic perspective for understanding and interpreting jailbreak behaviors in LLMs, offering both theoretical insights and practical implications for improving model safety.\n\nThe paper was published on March 9, 2026, and is authored by Yonghong Deng and colleagues from Beijing Institute of Technology."
    ],
    "durationSeconds": 6.702764790999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7ac4654b-4bc2-4877-848d-75d3d5cdc2d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T03:41:33.178Z_

<details><summary>↩ Tool result · `toolu_01N4CKsHjF4ypXLvExzfKGPu`</summary>

```text
Web search results for query: "AISA "intrinsic safety awareness" Song et al. attention head safety arXiv:2602.13547 2026"

Links: [{"title":"[2602.13547] AISA: Awakening Intrinsic Safety Awareness in Large Language Models against Jailbreak Attacks","url":"https://arxiv.org/abs/2602.13547"},{"title":"AISA: Awakening Intrinsic Safety Awareness in Large Language Models against Jailbreak Attacks","url":"https://arxiv.org/html/2602.13547"},{"title":"AISA: Awakening Intrinsic Safety Awareness in Large ...","url":"https://arxiv.org/pdf/2602.13547"},{"title":"Self-Aware Safety Augmentation: Leveraging Internal Semantic Understanding to Enhance Safety in Vision-Language Models","url":"https://arxiv.org/pdf/2507.21637"},{"title":"Intrinsically safe multi-drop communications link","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4691384"},{"title":"Protection of intrinsically safe circuits","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6751076"}]

Based on the search results, I found the paper you're looking for:

**AISA: Awakening Intrinsic Safety Awareness in Large Language Models against Jailbreak Attacks** is an arXiv paper (2602.13547) submitted on February 14, 2026, by authors Weiming Song, Xuan Xie, and Ruiping Yin.

**Key findings:**

AISA is a lightweight, single-pass defense that activates safety behaviors already latent inside the model rather than treating safety as an add-on. 

AISA localizes intrinsic safety awareness via spatiotemporal analysis and shows that intent-discriminative signals are broadly encoded, with especially strong separability appearing in the scaled dot-product outputs of specific attention heads near the final structural tokens before generation.

Using a compact set of automatically selected heads, AISA extracts an interpretable prompt-risk score with minimal overhead, achieving detector-level performance competitive with strong proprietary baselines on small (7B) models.

AISA performs logits-level steering: it modulates the decoding distribution in proportion to the inferred risk, ranging from normal generation for benign prompts to calibrated refusal for high-risk requests—without changing model parameters, adding auxiliary modules, or requiring multi-pass inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab65ba3b-aea2-42f2-9a9a-3f000f0def1e",
  "isSidechain": false,
  "promptId": "bcc9484c-086b-4bad-95dd-2a7e464a94a0",
  "type": "user",
  "uuid": "0d7f1cb3-cebb-44f1-9813-675284d54b89",
  "toolUseResult": {
    "query": "AISA \"intrinsic safety awareness\" Song et al. attention head safety arXiv:2602.13547 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Rs6QoLEHse82Khe9BZvdjV",
        "content": [
          {
            "title": "[2602.13547] AISA: Awakening Intrinsic Safety Awareness in Large Language Models against Jailbreak Attacks",
            "url": "https://arxiv.org/abs/2602.13547"
          },
          {
            "title": "AISA: Awakening Intrinsic Safety Awareness in Large Language Models against Jailbreak Attacks",
            "url": "https://arxiv.org/html/2602.13547"
          },
          {
            "title": "AISA: Awakening Intrinsic Safety Awareness in Large ...",
            "url": "https://arxiv.org/pdf/2602.13547"
          },
          {
            "title": "Self-Aware Safety Augmentation: Leveraging Internal Semantic Understanding to Enhance Safety in Vision-Language Models",
            "url": "https://arxiv.org/pdf/2507.21637"
          },
          {
            "title": "Intrinsically safe multi-drop communications link",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4691384"
          },
          {
            "title": "Protection of intrinsically safe circuits",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6751076"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**AISA: Awakening Intrinsic Safety Awareness in Large Language Models against Jailbreak Attacks** is an arXiv paper (2602.13547) submitted on February 14, 2026, by authors Weiming Song, Xuan Xie, and Ruiping Yin.\n\n**Key findings:**\n\nAISA is a lightweight, single-pass defense that activates safety behaviors already latent inside the model rather than treating safety as an add-on. \n\nAISA localizes intrinsic safety awareness via spatiotemporal analysis and shows that intent-discriminative signals are broadly encoded, with especially strong separability appearing in the scaled dot-product outputs of specific attention heads near the final structural tokens before generation.\n\nUsing a compact set of automatically selected heads, AISA extracts an interpretable prompt-risk score with minimal overhead, achieving detector-level performance competitive with strong proprietary baselines on small (7B) models.\n\nAISA performs logits-level steering: it modulates the decoding distribution in proportion to the inferred risk, ranging from normal generation for benign prompts to calibrated refusal for high-risk requests—without changing model parameters, adding auxiliary modules, or requiring multi-pass inference."
    ],
    "durationSeconds": 8.709633574,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ab65ba3b-aea2-42f2-9a9a-3f000f0def1e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T03:41:34.725Z_

<details><summary>↩ Tool result · `toolu_01YSsYspn1S5rahYqFHs4iTq`</summary>

```text
Web search results for query: ""discourse training" OR "conversational inertia" safety multi-turn LLM attention reallocation 2026"

Links: [{"title":"Mitigating Conversational Inertia in Multi-Turn Agents","url":"https://arxiv.org/pdf/2602.03664"},{"title":"Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction","url":"https://arxiv.org/pdf/2603.04783"},{"title":"Multi-Turn LLM Evaluation in 2026: What You Need to Know - Confident AI","url":"https://www.confident-ai.com/blog/multi-turn-llm-evaluation-in-2026"},{"title":"Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://arxiv.org/pdf/2512.06869"},{"title":"Speak Out of Turn: Safety Vulnerability of Large Language Models in   Multi-turn Dialogue","url":"https://arxiv.org/pdf/2402.17262"},{"title":"State-Dependent Safety Failures in Multi-Turn Language Model Interaction","url":"https://arxiv.org/pdf/2603.15684"},{"title":"MIRROR: Modular Internal Processing for Personalized Safety in LLM Dialogue","url":"https://arxiv.org/pdf/2506.00430"}]

I found several highly relevant research papers on these topics from 2026. Here's what the search returned:

## Key Findings:

**Conversational Inertia & Multi-Turn Challenges:**

A critical challenge emerges as conversation rounds increase: agent performance degrades significantly even when context remains within the model's capacity, and more dialogue turns do not necessarily lead to better performance. Research shows that for identical states, actions generated with longer contexts exhibit stronger inertia than those with shorter contexts, enabling researchers to propose Context Preference Learning to calibrate model preferences to favor low-inertia responses.

Attention visualization reveals token-to-token correspondence associated with conversational inertia, with models exhibiting strong diagonal attention to previous assistant outputs.

**Related Safety & Contextual Issues:**

Models frequently fail to refresh their reasoning in multi-turn contexts - for instance, when users update constraints, models rigidly adhere to previous plans and produce solutions that violate new requirements.

Current safety mechanisms of LLMs in multi-turn dialogue show inadequacies, exposing vulnerabilities in complex scenarios involving multi-turn dialogue.

**Proposed Solutions:**

Methods like Rhea (Role-aware Heuristic Episodic Attention) significantly alleviate performance decay, achieving state-of-the-art consistency and instruction adherence in multi-turn conversation.

The search returned recent 2026 research papers addressing attention reallocation, discourse issues, and multi-turn safety in LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ab5c291-8d6a-496e-9f3a-64abc7758fa2",
  "isSidechain": false,
  "promptId": "bcc9484c-086b-4bad-95dd-2a7e464a94a0",
  "type": "user",
  "uuid": "d4da139a-b9aa-4517-a688-c7fa6c15ed06",
  "toolUseResult": {
    "query": "\"discourse training\" OR \"conversational inertia\" safety multi-turn LLM attention reallocation 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QbwfPqNEV5HwCxiaqpiwpa",
        "content": [
          {
            "title": "Mitigating Conversational Inertia in Multi-Turn Agents",
            "url": "https://arxiv.org/pdf/2602.03664"
          },
          {
            "title": "Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction",
            "url": "https://arxiv.org/pdf/2603.04783"
          },
          {
            "title": "Multi-Turn LLM Evaluation in 2026: What You Need to Know - Confident AI",
            "url": "https://www.confident-ai.com/blog/multi-turn-llm-evaluation-in-2026"
          },
          {
            "title": "Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs",
            "url": "https://arxiv.org/pdf/2512.06869"
          },
          {
            "title": "Speak Out of Turn: Safety Vulnerability of Large Language Models in   Multi-turn Dialogue",
            "url": "https://arxiv.org/pdf/2402.17262"
          },
          {
            "title": "State-Dependent Safety Failures in Multi-Turn Language Model Interaction",
            "url": "https://arxiv.org/pdf/2603.15684"
          },
          {
            "title": "MIRROR: Modular Internal Processing for Personalized Safety in LLM Dialogue",
            "url": "https://arxiv.org/pdf/2506.00430"
          }
        ]
      },
      "I found several highly relevant research papers on these topics from 2026. Here's what the search returned:\n\n## Key Findings:\n\n**Conversational Inertia & Multi-Turn Challenges:**\n\nA critical challenge emerges as conversation rounds increase: agent performance degrades significantly even when context remains within the model's capacity, and more dialogue turns do not necessarily lead to better performance. Research shows that for identical states, actions generated with longer contexts exhibit stronger inertia than those with shorter contexts, enabling researchers to propose Context Preference Learning to calibrate model preferences to favor low-inertia responses.\n\nAttention visualization reveals token-to-token correspondence associated with conversational inertia, with models exhibiting strong diagonal attention to previous assistant outputs.\n\n**Related Safety & Contextual Issues:**\n\nModels frequently fail to refresh their reasoning in multi-turn contexts - for instance, when users update constraints, models rigidly adhere to previous plans and produce solutions that violate new requirements.\n\nCurrent safety mechanisms of LLMs in multi-turn dialogue show inadequacies, exposing vulnerabilities in complex scenarios involving multi-turn dialogue.\n\n**Proposed Solutions:**\n\nMethods like Rhea (Role-aware Heuristic Episodic Attention) significantly alleviate performance decay, achieving state-of-the-art consistency and instruction adherence in multi-turn conversation.\n\nThe search returned recent 2026 research papers addressing attention reallocation, discourse issues, and multi-turn safety in LLMs."
    ],
    "durationSeconds": 8.423654857,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6ab5c291-8d6a-496e-9f3a-64abc7758fa2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-20T03:41:34.735Z_

```json
{
  "parentUuid": "d4da139a-b9aa-4517-a688-c7fa6c15ed06",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "bcd1595a-7d76-449d-90ae-0fb82edb6987",
  "timestamp": "2026-05-20T03:41:34.735Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 34 · 2026-05-20T03:41:39.246Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do a couple more focused searches to check: (1) whether anyone has already connected conversational inertia to safety, and (2) the Zhou et al. safety heads paper, and (3) any other work that might directly compete with this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcd1595a-7d76-449d-90ae-0fb82edb6987",
  "isSidechain": false,
  "requestId": "req_011CbD8PSnzzpV6u4fsLiUaG",
  "type": "assistant",
  "uuid": "a91e1bdb-b91e-4e31-b170-b02ad5f55a21",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhmoJCPYQjErdxBCAneDbE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2318,
      "cache_read_input_tokens": 30820,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 282,
          "cache_read_input_tokens": 30820,
          "cache_creation_input_tokens": 2318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2318
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

_source line 35 · 2026-05-20T03:41:39.449Z_

Let me do a few more targeted searches to check for directly competing work and verify remaining key claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a91e1bdb-b91e-4e31-b170-b02ad5f55a21",
  "isSidechain": false,
  "requestId": "req_011CbD8PSnzzpV6u4fsLiUaG",
  "type": "assistant",
  "uuid": "866f1bb7-a696-4c27-836a-8dc5f634863c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhmoJCPYQjErdxBCAneDbE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2318,
      "cache_read_input_tokens": 30820,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 282,
          "cache_read_input_tokens": 30820,
          "cache_creation_input_tokens": 2318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2318
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

_source line 36 · 2026-05-20T03:41:40.409Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016vGmLgJn4o71DjvHtGhow9`</summary>

```json
{
  "query": "\"conversational inertia\" safety jailbreak defense CPL \"diagonal attention\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "866f1bb7-a696-4c27-836a-8dc5f634863c",
  "isSidechain": false,
  "requestId": "req_011CbD8PSnzzpV6u4fsLiUaG",
  "type": "assistant",
  "uuid": "54e0474c-ff2b-4ef3-98bc-6f77298d6888",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhmoJCPYQjErdxBCAneDbE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2318,
      "cache_read_input_tokens": 30820,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 282,
          "cache_read_input_tokens": 30820,
          "cache_creation_input_tokens": 2318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2318
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

_source line 37 · 2026-05-20T03:41:41.816Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NRKRiB6WKqPuzM7H5umXRG`</summary>

```json
{
  "query": "Zhou et al. \"role of attention heads\" safety ICLR 2025 arXiv:2410.13708 Ships score"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54e0474c-ff2b-4ef3-98bc-6f77298d6888",
  "isSidechain": false,
  "requestId": "req_011CbD8PSnzzpV6u4fsLiUaG",
  "type": "assistant",
  "uuid": "adec6d4f-56ba-486b-8f75-c3cac426dcfa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhmoJCPYQjErdxBCAneDbE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2318,
      "cache_read_input_tokens": 30820,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 282,
          "cache_read_input_tokens": 30820,
          "cache_creation_input_tokens": 2318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2318
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

_source line 38 · 2026-05-20T03:41:42.238Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EangfTKng3VeCytFT55Q5u`</summary>

```json
{
  "query": "attention head overlap safety inertia continuation heads per-head decomposition multi-turn 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adec6d4f-56ba-486b-8f75-c3cac426dcfa",
  "isSidechain": false,
  "requestId": "req_011CbD8PSnzzpV6u4fsLiUaG",
  "type": "assistant",
  "uuid": "fc4e291a-fd0b-42be-82b0-913068e52dce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhmoJCPYQjErdxBCAneDbE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2318,
      "cache_read_input_tokens": 30820,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 282,
          "cache_read_input_tokens": 30820,
          "cache_creation_input_tokens": 2318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2318
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Does Reducing Conversational Inertia Improve Multi-Turn Safety? Testing the Attention Capacity Competition Hypot…",
  "leafUuid": "fc4e291a-fd0b-42be-82b0-913068e52dce",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Conversational inertia and multi-turn safety erosion",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236"
}
```

---

### Tool result

_source line 41 · 2026-05-20T03:41:47.066Z_

<details><summary>↩ Tool result · `toolu_016vGmLgJn4o71DjvHtGhow9`</summary>

```text
Web search results for query: ""conversational inertia" safety jailbreak defense CPL "diagonal attention" 2026"

Links: [{"title":"Mitigating Conversational Inertia in Multi-Turn Agents","url":"https://arxiv.org/html/2602.03664"},{"title":"DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention   Modification","url":"https://arxiv.org/pdf/2504.13562"},{"title":"AttentionDefense: Leveraging System Prompt Attention for Explainable   Defense Against Novel Jailbreaks","url":"https://arxiv.org/pdf/2504.12321"},{"title":"Beyond Surface-Level Detection: Towards Cognitive-Driven Defense Against Jailbreak Attacks via Meta-Operations Reasoning","url":"https://arxiv.org/pdf/2508.03054"},{"title":"SafeSteer: Adaptive Subspace Steering for Efficient Jailbreak Defense in Vision-Language Models","url":"https://arxiv.org/pdf/2509.21400"},{"title":"Cloudfront","url":"https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176773228.86819800/v1"},{"title":"Mass-Scale Analysis of In-the-Wild Conversations Reveals Complexity Bounds on LLM Jailbreaking","url":"https://arxiv.org/pdf/2507.08014"}]

Based on the search results, I found highly relevant research on this topic. Here's what the search revealed:

The clip context method reduces diagonal attention by 7% for both base and CPL models, decreasing attention to previous corresponding tokens, which is consistent with mitigating conversational inertia. Context Preference Learning significantly reduces diagonal attention by over 10% across all context management methods.

The research specifically focuses on how increasing system attention suggests greater focus on the specific task requirements rather than over-mimicking self-generated content from previous responses. Diagonal attention decreases 10% more than the overall attention to previous assistant responses.

This work appears to be addressing "conversational inertia" as a safety concern where language models overly rely on their previous responses rather than properly following current instructions or safety guidelines. The CPL (Context Preference Learning) method and diagonal attention modifications are being used as technical mechanisms to defend against this type of vulnerability.

The research appears to be from a recent arXiv paper (dated February 5, 2026), indicating this is active research in the LLM safety field focusing on attention mechanisms as a defense against conversational inertia-based jailbreak attempts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54e0474c-ff2b-4ef3-98bc-6f77298d6888",
  "isSidechain": false,
  "promptId": "bcc9484c-086b-4bad-95dd-2a7e464a94a0",
  "type": "user",
  "uuid": "975062e6-629a-4952-844e-c8743f348d07",
  "toolUseResult": {
    "query": "\"conversational inertia\" safety jailbreak defense CPL \"diagonal attention\" 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019cHD9z2Jm8SvSiq1A3zmA3",
        "content": [
          {
            "title": "Mitigating Conversational Inertia in Multi-Turn Agents",
            "url": "https://arxiv.org/html/2602.03664"
          },
          {
            "title": "DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention   Modification",
            "url": "https://arxiv.org/pdf/2504.13562"
          },
          {
            "title": "AttentionDefense: Leveraging System Prompt Attention for Explainable   Defense Against Novel Jailbreaks",
            "url": "https://arxiv.org/pdf/2504.12321"
          },
          {
            "title": "Beyond Surface-Level Detection: Towards Cognitive-Driven Defense Against Jailbreak Attacks via Meta-Operations Reasoning",
            "url": "https://arxiv.org/pdf/2508.03054"
          },
          {
            "title": "SafeSteer: Adaptive Subspace Steering for Efficient Jailbreak Defense in Vision-Language Models",
            "url": "https://arxiv.org/pdf/2509.21400"
          },
          {
            "title": "Cloudfront",
            "url": "https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176773228.86819800/v1"
          },
          {
            "title": "Mass-Scale Analysis of In-the-Wild Conversations Reveals Complexity Bounds on LLM Jailbreaking",
            "url": "https://arxiv.org/pdf/2507.08014"
          }
        ]
      },
      "Based on the search results, I found highly relevant research on this topic. Here's what the search revealed:\n\nThe clip context method reduces diagonal attention by 7% for both base and CPL models, decreasing attention to previous corresponding tokens, which is consistent with mitigating conversational inertia. Context Preference Learning significantly reduces diagonal attention by over 10% across all context management methods.\n\nThe research specifically focuses on how increasing system attention suggests greater focus on the specific task requirements rather than over-mimicking self-generated content from previous responses. Diagonal attention decreases 10% more than the overall attention to previous assistant responses.\n\nThis work appears to be addressing \"conversational inertia\" as a safety concern where language models overly rely on their previous responses rather than properly following current instructions or safety guidelines. The CPL (Context Preference Learning) method and diagonal attention modifications are being used as technical mechanisms to defend against this type of vulnerability.\n\nThe research appears to be from a recent arXiv paper (dated February 5, 2026), indicating this is active research in the LLM safety field focusing on attention mechanisms as a defense against conversational inertia-based jailbreak attempts."
    ],
    "durationSeconds": 6.647857997999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "54e0474c-ff2b-4ef3-98bc-6f77298d6888",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T03:41:50.267Z_

<details><summary>↩ Tool result · `toolu_01NRKRiB6WKqPuzM7H5umXRG`</summary>

```text
Web search results for query: "Zhou et al. "role of attention heads" safety ICLR 2025 arXiv:2410.13708 Ships score"

Links: [{"title":"[2410.13708] On the Role of Attention Heads in Large Language Model Safety","url":"https://arxiv.org/abs/2410.13708"},{"title":"[2410.13708v2] On the Role of Attention Heads in Large Language Model Safety","url":"https://arxiv.org/abs/2410.13708v2"},{"title":"On the Role of Attention Heads in Large Language Model Safety","url":"https://iclr.cc/media/iclr-2025/Slides/28788.pdf"},{"title":"(PDF) On the Role of Attention Heads in Large Language Model Safety","url":"https://www.researchgate.net/publication/385010417_On_the_Role_of_Attention_Heads_in_Large_Language_Model_Safety"},{"title":"ICLR 2025 On the Role of Attention Heads in Large Language Model Safety Oral","url":"https://iclr.cc/virtual/2025/oral/31798"},{"title":"Published as a conference paper at ICLR 2025 ON THE ROLE OF ATTENTION HEADS IN","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf"},{"title":"On the Role of Attention Heads in Large Language Model Safety","url":"https://arxiv.org/html/2410.13708v2"}]

I found the paper! The paper "On the Role of Attention Heads in Large Language Model Safety" is arXiv:2410.13708 by Zhenhong Zhou and co-authors, and it was presented at ICLR 2025.

Regarding the "Ships score" you mentioned: The paper uses a metric called "Ships" (Attack Success Rate/ASR) to evaluate the impact on model safety after ablating important safety attention heads. The Ships metric appears to be used as an evaluation metric in this research to measure how successful jailbreak attacks are after certain attention heads are removed from the model.

The paper's core contribution is addressing the safety impact of multi-head attention mechanisms, despite their crucial role in various model functionalities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "adec6d4f-56ba-486b-8f75-c3cac426dcfa",
  "isSidechain": false,
  "promptId": "bcc9484c-086b-4bad-95dd-2a7e464a94a0",
  "type": "user",
  "uuid": "42c40dcf-cf59-4a4b-a88e-0670b9817024",
  "toolUseResult": {
    "query": "Zhou et al. \"role of attention heads\" safety ICLR 2025 arXiv:2410.13708 Ships score",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VcAeaBBWpvmNGt4izx7wiW",
        "content": [
          {
            "title": "[2410.13708] On the Role of Attention Heads in Large Language Model Safety",
            "url": "https://arxiv.org/abs/2410.13708"
          },
          {
            "title": "[2410.13708v2] On the Role of Attention Heads in Large Language Model Safety",
            "url": "https://arxiv.org/abs/2410.13708v2"
          },
          {
            "title": "On the Role of Attention Heads in Large Language Model Safety",
            "url": "https://iclr.cc/media/iclr-2025/Slides/28788.pdf"
          },
          {
            "title": "(PDF) On the Role of Attention Heads in Large Language Model Safety",
            "url": "https://www.researchgate.net/publication/385010417_On_the_Role_of_Attention_Heads_in_Large_Language_Model_Safety"
          },
          {
            "title": "ICLR 2025 On the Role of Attention Heads in Large Language Model Safety Oral",
            "url": "https://iclr.cc/virtual/2025/oral/31798"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 ON THE ROLE OF ATTENTION HEADS IN",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf"
          },
          {
            "title": "On the Role of Attention Heads in Large Language Model Safety",
            "url": "https://arxiv.org/html/2410.13708v2"
          }
        ]
      },
      "I found the paper! The paper \"On the Role of Attention Heads in Large Language Model Safety\" is arXiv:2410.13708 by Zhenhong Zhou and co-authors, and it was presented at ICLR 2025.\n\nRegarding the \"Ships score\" you mentioned: The paper uses a metric called \"Ships\" (Attack Success Rate/ASR) to evaluate the impact on model safety after ablating important safety attention heads. The Ships metric appears to be used as an evaluation metric in this research to measure how successful jailbreak attacks are after certain attention heads are removed from the model.\n\nThe paper's core contribution is addressing the safety impact of multi-head attention mechanisms, despite their crucial role in various model functionalities."
    ],
    "durationSeconds": 8.44699043099999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "adec6d4f-56ba-486b-8f75-c3cac426dcfa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-20T03:41:50.414Z_

<details><summary>↩ Tool result · `toolu_01EangfTKng3VeCytFT55Q5u`</summary>

```text
Web search results for query: "attention head overlap safety inertia continuation heads per-head decomposition multi-turn 2026"

Links: [{"title":"Multi-head Self-Attention in Neural Models","url":"https://www.emergentmind.com/topics/multi-head-self-attention-mhsa-255cf104-528d-495b-b1c8-8651a1e510b5"},{"title":"[2410.13708] On the Role of Attention Heads in Large Language Model Safety","url":"https://arxiv.org/abs/2410.13708"},{"title":"Attention Mechanism in LLMs Explained (2026)","url":"https://www.buildfastwithai.com/blogs/attention-mechanism-llm-explained"},{"title":"On the Role of Attention Heads in Large Language Model Safety","url":"https://arxiv.org/pdf/2410.13708"},{"title":"Multi-Head Attention Architecture","url":"https://www.emergentmind.com/topics/multi-head-attention-architecture"},{"title":"Safety Alignment Should Be Made More Than Just A Few Attention Heads","url":"https://arxiv.org/pdf/2508.19697"}]

Based on the search results, I found several relevant studies on attention heads, safety mechanisms, and multi-head attention decomposition:

**Safety and Attention Heads:**

Research proposes a Safety Head ImPortant Score (Ships) metric tailored for multi-head attention to assess individual heads' contributions to model safety, and introduces the Safety Attention Head AttRibution Algorithm (Sahara) to identify critical safety attention heads inside models. 

Attention heads primarily function as feature extractors for safety, and models fine-tuned from the same base model exhibit overlapping safety heads. Ablating a single safety head allows an aligned model like Llama-2-7b-chat to respond to 16 times more harmful queries while only modifying 0.006% of the parameters.

**Related Work on Distributed Safety:**

A novel training strategy called AHD (Attention Head Distribution) was proposed to promote distributed encoding of safety capabilities across multiple attention heads, enhancing the robustness and redundancy of safety mechanisms in LLMs.

**Multi-Head Attention Variations:**

Some approaches allow partial overlap with neighbor head dimensions (parameterized by overlap size), empirically improving accuracy at negligible overhead.

The search results focus primarily on safety-related applications of attention heads rather than continuation heads or inertia-specific mechanisms that your query mentions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc4e291a-fd0b-42be-82b0-913068e52dce",
  "isSidechain": false,
  "promptId": "bcc9484c-086b-4bad-95dd-2a7e464a94a0",
  "type": "user",
  "uuid": "9502fa49-6548-4112-813b-3e4a6ff6e275",
  "toolUseResult": {
    "query": "attention head overlap safety inertia continuation heads per-head decomposition multi-turn 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AVnvnzj8wsakxSPn6gTkQ3",
        "content": [
          {
            "title": "Multi-head Self-Attention in Neural Models",
            "url": "https://www.emergentmind.com/topics/multi-head-self-attention-mhsa-255cf104-528d-495b-b1c8-8651a1e510b5"
          },
          {
            "title": "[2410.13708] On the Role of Attention Heads in Large Language Model Safety",
            "url": "https://arxiv.org/abs/2410.13708"
          },
          {
            "title": "Attention Mechanism in LLMs Explained (2026)",
            "url": "https://www.buildfastwithai.com/blogs/attention-mechanism-llm-explained"
          },
          {
            "title": "On the Role of Attention Heads in Large Language Model Safety",
            "url": "https://arxiv.org/pdf/2410.13708"
          },
          {
            "title": "Multi-Head Attention Architecture",
            "url": "https://www.emergentmind.com/topics/multi-head-attention-architecture"
          },
          {
            "title": "Safety Alignment Should Be Made More Than Just A Few Attention Heads",
            "url": "https://arxiv.org/pdf/2508.19697"
          }
        ]
      },
      "Based on the search results, I found several relevant studies on attention heads, safety mechanisms, and multi-head attention decomposition:\n\n**Safety and Attention Heads:**\n\nResearch proposes a Safety Head ImPortant Score (Ships) metric tailored for multi-head attention to assess individual heads' contributions to model safety, and introduces the Safety Attention Head AttRibution Algorithm (Sahara) to identify critical safety attention heads inside models. \n\nAttention heads primarily function as feature extractors for safety, and models fine-tuned from the same base model exhibit overlapping safety heads. Ablating a single safety head allows an aligned model like Llama-2-7b-chat to respond to 16 times more harmful queries while only modifying 0.006% of the parameters.\n\n**Related Work on Distributed Safety:**\n\nA novel training strategy called AHD (Attention Head Distribution) was proposed to promote distributed encoding of safety capabilities across multiple attention heads, enhancing the robustness and redundancy of safety mechanisms in LLMs.\n\n**Multi-Head Attention Variations:**\n\nSome approaches allow partial overlap with neighbor head dimensions (parameterized by overlap size), empirically improving accuracy at negligible overhead.\n\nThe search results focus primarily on safety-related applications of attention heads rather than continuation heads or inertia-specific mechanisms that your query mentions."
    ],
    "durationSeconds": 8.172572959000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fc4e291a-fd0b-42be-82b0-913068e52dce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-20T03:42:59.505Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a fairly comprehensive picture of the field. Let me synthesize my findings and make my assessment.

**Key findings from my research:**

1. **Wan et al. (ICML 2026)** - The CPL paper is real, published at ICML 2026. It identifies conversational inertia (diagonal attention) and proposes CPL as a training-time intervention. The paper explicitly averages all heads for the aggregate attention pattern. CPL reduces diagonal attention by 10%+. The paper is about agent performance, NOT safety.

2. **DETAM (ACL 2025 Findings)** - Real paper. 

An inference-time approach that modifies attention patterns to defend against jailbreaks, achieving dramatic improvements in attack success rates on LLaMA-2, though it only works for single-turn interactions.

3. **ASGuard (ICLR 2026)** - Real paper. Training-time circuit-targeted scaling for specific jailbreaking types. Identifies vulnerable heads.

4. **Johnson & Huo (arXiv 2026)** - Real paper on competition for attention tipping points.

5. **Deng et al. (arXiv 2026)** - Real paper on continuation vs. refusal heads.

6. **AISA (arXiv 2026)** - Real paper on safety heads.

7. **Zhou et al. (ICLR 2025)** - Real paper on safety attention heads with Ships score.

8. **No competing work found** that directly bridges conversational inertia → safety. The search for "conversational inertia safety" only returns the original Wan et al. paper and general attention-based defense papers. This gap appears genuine.

Now assessing the core claim: CPL reduces diagonal attention and conversational inertia to improve multi-turn safety because diagonal attention competes with safety attention in a softmax zero-sum game. The main alternative is whether DETAM could just be applied at each turn in multi-turn settings, but the proposal argues DETAM can't identify "intent tokens" when intent is distributed across multiple turns—a reasonable argument that needs verification.

There's also the question of why a discourse-level intervention would outperform XGuard-Train SFT, though the proposal does include it as a control. The critical untested assumption is whether diagonal attention and safety attention heads actually overlap or compete—this is the entire foundation of the hypothesis, and Phase 0.5 is designed to test it. If they don't overlap significantly, the competitive mechanism weakens. Additionally, CPL was validated on agentic tasks like ALFWorld and Web environments, so whether it actually reduces diagonal attention in the multi-turn safety contexts that matter here remains an open question.

The theoretical framework invoking Johnson & Huo's work on tipping points is also worth scrutinizing—their model addresses edge AI adoption broadly, not specifically diagonal attention patterns in language models. And the core claim that CPL reduces inertia without directly learning safety could be misleading; it might simply alter text generation style without touching safety-relevant representations at all. The per-head decomposition of diagonal attention itself appears novel, though I'm still evaluating the overall contribution. The core contribution boils down to applying an existing method (CPL) to safety evaluation and measuring the results—the mechanistic framing around competition and circuit modification is speculative scaffolding without direct evidence. While the research question is genuine and the experimental design is solid, the novelty is bounded even in the best case, since the paper essentially hinges on whether safety numbers improve, and the authors themselves acknowledge the result could go either way. ulation strategy adds rigor but makes the whole proposal unwieldy for what's essentially a straightforward empirical question. Weighing the genuine research gap and thorough controls against the high likelihood of unsurprising results and the speculative nature of some core assumptions, I'm landing around 25-35% for EMNLP 2026—though I should recalibrate since this is actually targeting ICLR 2027.

For EMNLP specifically, this safety and mechanistic interpretability work fits the scope, but the core contribution hinges on whether reducing conversational inertia improves safety, which could go either way predictably. Since the method itself isn't novel—just applying existing CPL techniques to a new domain—and the elaborate mechanistic framework might feel like over-engineering for a transfer study, I'm settling toward the lower end of that range, around 25-32%.

The strongest case would be if head overlap correlates strongly with safety improvements, but that requires several untested assumptions to align. Reconsidering the full picture though, the per-head decomposition of diagonal attention is genuinely novel, the discourse-safety connection is an important unexplored area, and the experimental rigor with five confound controls is solid. If results come back positive, it'd be significant for the field. But fundamentally this is applying an existing method to a new evaluation—a common paper type that struggles at top venues unless findings are surprising. The three-level hypothesis framework hasn't been validated yet, and the post-hoc narrative around implicit DETAM and ASGuard feels somewhat constructed. I'm landing on 22-32%, with a median around 27%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9502fa49-6548-4112-813b-3e4a6ff6e275",
  "isSidechain": false,
  "requestId": "req_011CbD8Qc58MkXwVjfTX3VHu",
  "type": "assistant",
  "uuid": "688c69bd-fbda-4537-add6-d9495379a0be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KwWQdidBijsDRTVvJrSRvN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2170,
      "cache_read_input_tokens": 33138,
      "output_tokens": 6148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2170,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6148,
          "cache_read_input_tokens": 33138,
          "cache_creation_input_tokens": 2170,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2170
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

_source line 45 · 2026-05-20T03:44:24.648Z_

Now I have sufficient information to make my assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Wan et al. "Mitigating Conversational Inertia in Multi-Turn Agents" arXiv:2602.03664](https://arxiv.org/abs/2602.03664) (ICML 2026): 提出 conversational inertia 概念和 CPL 方法。确认论文存在、已发表于 ICML 2026。关键细节验证：CPL 使用 LoRA rank-16 DPO beta=0.01，减少 diagonal attention 10%+。论文明确声明"All attention heads are averaged to create a unified attention matrix"——per-head decomposition 确实不存在。**但 CPL 仅在 agent 性能（ALFWorld, WebShop 等 8 个环境）上验证，从未评估安全性。**

- [DETAM (Li et al.) arXiv:2504.13562](https://arxiv.org/abs/2504.13562) (ACL 2025 Findings): 确认存在。通过推理时注意力重分配（mask modification, beta=5.0）将 ASR 从 46% 降至 1.2%。确认仅限 single-turn。确认需要运行时识别 intent tokens。

- [ASGuard (Park et al.) arXiv:2509.25843](https://arxiv.org/abs/2509.25843) (ICLR 2026): 确认存在。通过 EAP-IG 识别 vulnerable heads，channel-wise scaling vectors + preventative fine-tuning。确认针对 tense jailbreaking 等特定攻击类型，自述 "efficacy hinges on localizable causal circuits"。

- [Johnson & Huo arXiv:2602.14370](https://arxiv.org/abs/2602.14370) (arXiv Feb 2026): 确认存在。提出 dot-product competition 的 tipping point n* 数学公式。但注意：该论文关注 edge AI 的 good-to-bad tipping，是偏理论/物理学视角的分析，并非专门针对 diagonal attention 或多轮安全。

- [Deng et al. arXiv:2603.08234](https://arxiv.org/abs/2603.08234) (arXiv Mar 2026): 确认存在。分析 continuation vs. refusal heads 的竞争机制。提供了 safety heads (layers 25-27) vs. continuation heads (middle layers ~Layer 13) 的定位。

- [AISA (Song et al.) arXiv:2602.13547](https://arxiv.org/abs/2602.13547) (arXiv Feb 2026): 确认存在。通过 spatiotemporal analysis 定位 safety heads，top-K=16 heads 达到 0.92 检测准确率。

- [Zhou et al. arXiv:2410.13708](https://arxiv.org/abs/2410.13708) (ICLR 2025): 确认存在。Ships score（Safety Head ImPortant Score），Sahara 算法定位安全注意力头。

- **直接竞争检索结果**：搜索 "conversational inertia safety" 未找到任何已有工作将 conversational inertia/CPL 与安全联系起来。该 gap 目前看是真实的。

- 调研总结：多轮安全领域（攻防、机制分析、防御训练）和 attention-level 安全机制分析（safety heads, continuation heads, attention competition）是两个活跃但仍较独立的研究方向。Conversational inertia（Wan et al.）目前仅在 agent 性能维度被研究，尚无人将其连接到安全问题。本 proposal 试图搭建这座桥梁。


【Trivial Alternative 检验】:

**存在两个显著的 trivial alternative 威胁：**

1. **逐轮 DETAM**：虽然 proposal 论证了 DETAM 在多轮场景下 "intent tokens 不可定位"，但这个论证是概念层面的，并未实证验证。一个更 trivial 的做法是：在每一轮都应用 DETAM（将当前轮的 user input 视为 intent），测试是否足够有效。如果逐轮 DETAM 已经很好地解决了多轮安全问题，那么 CPL 的增量价值就很小。Proposal 并未包含"multi-turn DETAM"作为 baseline。

2. **直接在安全数据上做 DPO/SFT**：XGuard-Train SFT 作为 control 被包含了——但核心问题是：为什么一个 **不在安全数据上训练、仅在 agent 环境上训练** 的 discourse intervention (CPL) 会比 **直接在安全数据上训练** 的方法更好？如果 CPL 的安全提升不如 XGuard-Train（这是可能性最高的结果），那 proposal 的故事就变成了"间接方法不如直接方法"——虽然可以 publish 但 significance 大打折扣。

**增量价值的核心依赖**：CPL 的独特价值必须来自"不用安全标注数据就能提升安全性"这个属性——即 unsupervised safety improvement via discourse training。这是有意义的，但需要 CPL 的效果足够大才能让审稿人信服这不只是噪声。


【前提假设检验】:

核心逻辑链存在 **三个关键未验证假设**：

1. **Head Overlap 假设（最关键）**：整个"attention capacity competition"假设的前提是 diagonal attention heads 与 safety heads 在某种程度上重叠（或至少在相同 layer 竞争）。Proposal 正确地在 Phase 0.5 测试这个假设——但如果 overlap 极低（Level 3），整个 softmax zero-sum 竞争机制就不成立，论文的理论叙事从"attention competition"退化为"representation drift"，novelty 大幅下降（representation drift 已被 X-Boundary 研究过）。

2. **CPL 效果迁移假设**：CPL 在 AgentGym 环境（ALFWorld, WebShop 等）上训练和验证。假设它学到的 attention 变化能迁移到完全不同的安全评估场景（MT-AgentRisk, 恶意多轮对话）。这个迁移并非显然——CPL 训练的 preference pairs 来自 agent 任务的 long-context vs. short-context，与安全场景的分布可能相差很大。

3. **因果方向假设**：论文假设 "diagonal attention → 安全下降" 是因果关系。但同样可能的替代解释是：多轮对话本身增加了复杂性/context length，导致 diagonal attention 和安全下降 **同时发生但无因果关系**（confounded by conversation length/complexity）。CPL 减少 diagonal attention 时，如果安全确实提升，还需要排除 CPL 同时引入的其他变化（如 response style changes、length changes 等）。Proposal 包含了 response-length control，但未控制所有可能的 confounds。


【3 维度打分】:

1. **Novelty: 中** — 
   - **确认的真实 novelty delta**：(a) 首次将 conversational inertia 连接到 multi-turn safety——搜索确认此 gap 真实存在；(b) 首个 per-head diagonal attention decomposition（Wan et al. 明确只做 aggregate-level averaging）；(c) 三种 safety head 定位方法的对比研究。
   - **Novelty 的局限**：核心实验本质上是"将一个已有方法（CPL）应用到一个新评估维度（安全）"——这是 transfer/application study 而非新方法提出。三级竞争假说是理论贡献，但它尚未被验证，如果 Phase 0.5 结果不支持 Level 1/2，这个贡献就变成了一个被否决的假设。方法论上未提出新技术（CPL 来自 Wan et al.，Ships 来自 Zhou et al.，DETAM sensitivity 来自 Li et al.，AISA 来自 Song et al.）——所有分析工具都是现成的。
   - **与最近工作的对比**：无直接竞争者（gap 真实），但核心贡献的 novelty 性质偏向 empirical study 而非 methodological innovation。审稿人可能认为这是一个 well-designed empirical investigation，但不是一个 novel approach。

2. **Significance: 中** — 
   - **正面**：多轮安全是一个重要且活跃的问题（16% ASR increase documented by Yang et al.）。如果 CPL 确实能在不使用安全标注数据的情况下显著提升多轮安全，这对 alignment 领域有重要启示——意味着 discourse dynamics 是安全的一个被忽视的维度。
   - **限制**：(a) 最可能的结果是 CPL 有 modest improvement（因为任何改变模型 attention 分布的训练都可能对安全有微弱影响），这不够 surprising 来支撑高 significance；(b) 如果 CPL 效果弱于直接安全训练方法（XGuard-Train, MUSE-D），实际应用价值有限——practitioners 会直接选择用安全数据训练；(c) 即使 positive，结论的可推广性受限于 CPL 这一特定方法——无法确定是 "减少 inertia" 还是 CPL 的某个副作用导致了安全提升。

3. **Related Work: 强** — 
   - 调研确认 proposal 引用的所有关键论文（DETAM, ASGuard, Wan et al., Johnson & Huo, Deng et al., Zhou et al., AISA）都真实存在且描述准确。与现有工作的差异化定位清晰且诚实（DETAM: single-turn + runtime; ASGuard: circuit-specific; XGuard-Train: safety-labeled data）。文献覆盖面在本领域可能是最全面的——涵盖攻击、防御、机制分析、基准测试、理论框架等多个子方向。唯一可能的遗漏：未讨论"逐轮 DETAM"作为一个 straightforward extension 的可行性。


【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
- **Related Work (强)** 提供了坚实的基础，确保论文不会因文献遗漏被拒。
- **Novelty (中)** 是主要限制因素——核心贡献是 "apply existing method to new evaluation dimension"，方法论创新不足。Per-head decomposition 和 triple triangulation 是 solid 但 incremental 的贡献。审稿人可能认为这更像一个 thorough empirical study 而非一个有 conceptual breakthrough 的论文。
- **Significance (中)** 进一步限制上界——最可能的实验结果（CPL 有 modest effect but weaker than direct safety training）会让审稿人说 "I would have guessed this"。只有在 CPL 效果显著且机制分析清晰展示 head overlap 时，才能达到 surprising 的程度，但这需要多个未验证假设同时成立。
- **概率上界受限于**：idea 本质是 application study + hypothesis testing，而非 method proposal。即使执行完美，核心发现的 surprise factor 有上限。
- **概率下界受益于**：gap 真实、实验设计有 5 个 controls、有多个 standalone 贡献（per-head decomposition, head comparison）可以在 negative result 时提供 fallback value。

【主要风险】: 
1. **"I would have guessed this" 风险**：无论 CPL 的安全效果是正向还是负向，审稿人都可能认为结果在预期范围内——正向（"当然，改变 attention 分布会影响安全"）或负向（"当然，不在安全数据上训练不会提升安全"）。缺乏一个 clear a priori reason to expect a *surprising* outcome。
2. **Assumption Cascade 风险**：论文的核心叙事（attention competition hypothesis）依赖一连串未验证假设（head overlap → softmax competition → cumulative tipping → CPL as implicit DETAM）。任何一环断裂，理论框架就需要大幅调整，论文从"验证了一个 elegant theory"变成"做了一个 comprehensive but inconclusive empirical study"。
```

Sources:
- [Wan et al. - Mitigating Conversational Inertia in Multi-Turn Agents (ICML 2026)](https://arxiv.org/abs/2602.03664)
- [DETAM - Li et al. (ACL 2025 Findings)](https://arxiv.org/abs/2504.13562)
- [ASGuard - Park et al. (ICLR 2026)](https://arxiv.org/abs/2509.25843)
- [Johnson & Huo - Competition for attention predicts good-to-bad tipping in AI](https://arxiv.org/abs/2602.14370)
- [Deng et al. - The Struggle Between Continuation and Refusal](https://arxiv.org/abs/2603.08234)
- [AISA - Song et al.](https://arxiv.org/abs/2602.13547)
- [Zhou et al. - On the Role of Attention Heads in LLM Safety (ICLR 2025)](https://arxiv.org/abs/2410.13708)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "688c69bd-fbda-4537-add6-d9495379a0be",
  "isSidechain": false,
  "requestId": "req_011CbD8Qc58MkXwVjfTX3VHu",
  "type": "assistant",
  "uuid": "e6def188-216c-42a3-89c3-28f6e80b23f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KwWQdidBijsDRTVvJrSRvN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2170,
      "cache_read_input_tokens": 33138,
      "output_tokens": 6148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2170,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6148,
          "cache_read_input_tokens": 33138,
          "cache_creation_input_tokens": 2170,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2170
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Does Reducing Conversational Inertia Improve Multi-Turn Safety? Testing the Attention Capacity Competition Hypot…",
  "leafUuid": "e6def188-216c-42a3-89c3-28f6e80b23f6",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Conversational inertia and multi-turn safety erosion",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Does Reducing Conversational Inertia Improve Multi-Turn Safety? Testing the Attention Capacity Competition Hypot…",
  "leafUuid": "e6def188-216c-42a3-89c3-28f6e80b23f6",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "ai-title",
  "aiTitle": "Conversational inertia and multi-turn safety erosion",
  "sessionId": "07bb135d-16d1-47ac-8e33-f1e9e2720236"
}
```

---
