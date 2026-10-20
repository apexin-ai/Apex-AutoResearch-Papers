# Research conversation: I need you to help me compose a large JSON object. I'll provide the complete content — please output ONLY the raw JSON, 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 3
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a4915e1a3d6ae072f.jsonl`
- **Structured JSON:** [`dedf7478066e91f187fd.json`](../../sessions/de/dedf7478066e91f187fd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

3 recorded events

### User

_source line 1 · 2026-05-17T09:17:42.449Z_

I need you to help me compose a large JSON object. I'll provide the complete content — please output ONLY the raw JSON, no markdown code fences, no commentary. This is a research idea revision.

Here is the complete JSON to output:

{
  "change_type": "major",
  "title": "Circuit-DPO: Internalizing Distraction Robustness via Mechanistically-Targeted Preference Optimization",
  "core_problem": "LLMs suffer catastrophic performance degradation (up to 80% on NoisyBench, >45% average on Adaptive Distraction) when contextual distractors are injected into prompts. Mechanistic analysis ('Llama See, Llama Do,' ACL 2025) identifies specific 'entrainment heads' — attention heads that indiscriminately boost previously-seen context tokens — as the causal mechanism. Current defenses split into two paradigms with complementary limitations: (1) Behavioral approaches (EIT, DPO, SFT+RL) optimize output quality without mechanistic targeting. EIT's balanced conflict RL achieves +39.1% on unseen bias types by making bias cues non-predictive of reward. However, recent mechanistic interpretability evidence shows that behavioral training (RLHF, RL) 'primarily affects specific components related to response initiation and style, while core knowledge and reasoning circuits remain largely unchanged' (arXiv:2602.11180). This means behavioral methods likely learn compensatory output strategies that route AROUND the intact entrainment circuit rather than modifying it — a fragile defense that may break when novel distractor patterns overwhelm the compensatory capacity. Furthermore, EIT's own authors note that 'the non-predictiveness guarantee applies specifically to the injected bias signal; it does not preclude reliance on other shortcuts,' and position bias (structural) shows zero transfer (+0% improvement). (2) Inference-time circuit interventions (head ablation from 'Llama See, Llama Do') directly target entrainment heads with only 0.2-3% ICL cost. Ablation is effective precisely BECAUSE entrainment heads are 'not strongly related to how LMs process and utilise contextual information or perform ICL more broadly' — so suppressing them is cheap. But ablation has three practical limitations: (a) entrainment heads are task-specific, not model-specific, requiring per-task head re-identification via differentiable masking before deployment; (b) ablation is binary (all-or-nothing), unable to handle partial entrainment from subtly related distractors; (c) the mechanistic interpretability literature documents that models contain 'multiple overlapping circuits' for the same behavior, suggesting ablation of identified heads may be compensated by backup pathways. The critical gap: no approach INTERNALIZES distraction robustness at the circuit level during training — permanently modifying the entrainment mechanism so that neither per-task head identification at inference time nor fragile behavioral compensation is needed.",
  "opportunity": "Three convergent opportunities enable Circuit-DPO, which we position as a method that INTERNALIZES circuit-level distraction robustness into model weights during preference optimization: (1) The entrainment circuit foundation from 'Llama See, Llama Do' (ACL 2025) — differentiable masking identifies 30-110 task-specific entrainment heads that can be ablated with minimal ICL cost (0.2-3%). The near-zero ablation cost is not a weakness of our approach but a STRENGTH: it demonstrates these heads are modifiable without breaking broader capabilities, establishing the safety of circuit-level intervention. However, inference-time ablation requires per-task head re-identification and cannot propagate its effects to related circuits. Training-time optimization with gradient flow through these heads can both internalize the intervention and indirectly regularize adjacent circuits. (2) Self-supervised attention targets are freely available in distractor-injection settings: the model's own attention patterns on clean inputs provide a reference distribution for entrainment heads. For any task where clean/noisy input pairs can be constructed (all distractor-injection benchmarks by definition), the clean-attention pattern serves as a soft supervision reference. We use 'reference' rather than 'exact target' because softmax attention is jointly computed over all positions — adding tokens legitimately changes the softmax denominator. Our margin-based constraint tolerates small deviations while penalizing the large shifts characteristic of entrainment. (3) The DPO framework is uniquely suited — it operates on paired preferences and avoids RL instability. Augmenting DPO with attention-distribution divergence on entrainment heads is a natural extension. KLAAD (EMNLP 2025, arXiv:2507.19962) establishes the technical precedent that attention-distribution divergence can serve as an effective auxiliary training loss — it uses KL divergence to align attention between stereotype/anti-stereotype pairs for debiasing. Circuit-DPO advances this mechanism in three ways: targeting mechanistically-identified circuit heads (not all heads in a single layer), integrating into preference optimization (not standard training), and using self-supervised clean-input references (not externally-provided paired examples). RetMask (ACL 2026 Findings, arXiv:2601.11020) bridges head identification with DPO indirectly — using retrieval-head-ablated outputs for contrastive pair generation. Circuit-DPO provides direct gradient signal on attention distributions.",
  "landscape": "The distraction robustness landscape has matured rapidly in 2025-2026, with approaches spanning behavioral training, mechanistic analysis, circuit-level methods, and attention-distribution optimization: (1) Behavioral training methods. EIT (arXiv:2602.01528) achieves +39.1% generalization to unseen bias types via balanced conflict RL — the strongest OOD result, but operating purely at the behavioral level with evidence that RL training leaves core reasoning circuits largely unchanged (arXiv:2602.11180). Standard DPO for distraction (NeurIPS 2025, arXiv:2502.01609) achieves strong in-distribution robustness (+0.485 accuracy on Phi-3.5-mini). RARE (arXiv:2601.07226) uses rationale-aware reward shaping. Distractor Injection defense (arXiv:2510.16259) achieves >50-point improvement via SFT+RL. All modify behavior without targeting the entrainment mechanism. (2) Mechanistic and circuit methods. 'Llama See, Llama Do' (ACL 2025) identifies and ablates entrainment heads at inference time — interpretable but binary, task-specific, and requiring per-task head re-identification. CHG (NeurIPS 2025, arXiv:2505.13737) uses contrastive gating for circuit analysis. 'Thinking Sparks!' (arXiv:2509.25758) demonstrates that post-training causes attention heads to emerge, shift, and be pruned. Bali et al. (arXiv:2602.16740) quantify attention-head stability across training, finding middle-layer heads are least stable but most functionally important. (3) Attention-distribution losses in training. KLAAD (EMNLP 2025, arXiv:2507.19962) is the closest TECHNICAL precedent: it uses KL divergence on attention distributions as an auxiliary training loss to align attention between stereotype/anti-stereotype pairs for debiasing. KLAAD targets all attention heads in the final layer during standard (CE+KL+Triplet) training, without head selection or DPO integration. Circuit-DPO differs in: (a) targeting mechanistically-identified entrainment heads across multiple layers rather than all heads in one layer; (b) integrating into preference optimization rather than standard training; (c) using self-supervised clean-input references rather than externally-constructed paired examples. (4) Mechanistic-interpretability-guided preference optimization. RetMask (ACL 2026 Findings, arXiv:2601.11020) identifies retrieval heads, then generates contrastive pairs by comparing original vs. head-ablated outputs for standard DPO — heads inform DATA CURATION, not the loss function. CART (arXiv:2509.24713) uses circuit analysis to guide data augmentation and regularization for reward model robustness but does not apply circuit-targeted losses during policy optimization. RAL (arXiv:2602.04884) optimizes attention via policy gradient for multimodal LLMs — all attention, not circuit-specific. (5) Architectural and representation methods. Gated Attention (NeurIPS 2025 Best Paper, arXiv:2505.06708) introduces per-head sigmoid gates as a pretraining modification. Pref-CTRL (arXiv:2604.23543) and RE-Control (NeurIPS 2024) operate on hidden states. FPO (arXiv:2411.07618) constrains SAE features during DPO. Circuit-DPO uniquely combines direct attention-level gradient supervision on mechanistically-identified heads with preference optimization, framed as INTERNALIZATION of circuit-level distraction robustness.",
  "approach": "Circuit-DPO augments the standard DPO loss with a margin-based attention-distribution divergence term operating specifically on entrainment heads, with periodic head re-identification to account for circuit drift. The method is framed as INTERNALIZATION: permanently embedding distraction robustness into model weights by modifying the entrainment mechanism during training, eliminating inference-time head identification. Four stages with composability-first evaluation: (1) Entrainment head discovery with periodic refresh. Apply differentiable masking from 'Llama See, Llama Do' (github.com/frankniujc/entrainment) to identify entrainment heads in Llama-3-8B and Qwen2.5-7B. For Qwen2.5-7B (28Q/4KV, different GQA ratio from Llama-3-8B's 32Q/8KV), mask at query-head granularity within each KV group. Because post-training causes attention heads to emerge and shift ('Thinking Sparks!'), re-run head discovery every 500 steps using warm-started logit parameters. If head sets shift substantially between intervals — a known risk given middle-layer instability (Bali et al., arXiv:2602.16740) — the warm-start procedure biases toward the previous head set, providing continuity. We track head-set Jaccard similarity across re-identifications; if similarity drops below 0.5, we trigger early re-identification and log the event for analysis. This monitoring addresses whether head discovery is noisy: if different heads appear each time, it signals that the entrainment function is being redistributed across the network — which is itself evidence of successful internalization. (2) Self-supervised attention reference construction. For each training example, construct paired clean/noisy inputs. Run x_clean through the model and extract attention distributions from entrainment heads over shared context tokens (with stop-gradient). These clean-attention patterns define a REFERENCE distribution. The margin-based loss (Stage 3) tolerates small deviations — inherent to softmax recomputation with additional tokens — while penalizing the large shifts characteristic of entrainment. (3) Circuit-DPO training with margin-based attention constraint. L = L_DPO(y_chosen, y_rejected | x_noisy) + λ · Σ_{h ∈ H_ent} max(JSD(A_h^noisy_shared, A_h^clean_shared) - ε, 0). JSD (Jensen-Shannon divergence) is used because: (a) symmetric — no principled reason to prefer one KL direction; (b) bounded in [0, ln 2], preventing gradient explosion; (c) margin ε has interpretable units (bits of divergence). λ annealed linearly from 0 over first 20% of training. Hyperparameter sweep: ε ∈ {0.01, 0.05, 0.1, 0.2}, λ ∈ {0.1, 0.5, 1.0, 2.0}. (4) Evaluation protocol centered on three key comparisons. PRIMARY COMPARISON 1 — Internalization vs. inference-time ablation: Circuit-DPO (no inference-time intervention) vs. inference-time head ablation on MATCHED distractor types AND cross-task transfer. The critical test: on a new task domain where entrainment heads have NOT been identified, Circuit-DPO should maintain robustness (internalized) while ablation cannot be applied (no head identification). This is the key experiment justifying the method's complexity over simple ablation. PRIMARY COMPARISON 2 — Composability: Circuit-DPO + EIT vs. each alone. The concrete mechanistic argument: EIT teaches the model to produce correct outputs despite bias cues, but mechanistic evidence suggests RL training leaves core circuits largely unchanged (arXiv:2602.11180) — so the entrainment circuit likely still activates on distractors, consuming attention capacity and creating fragile compensation. Circuit-DPO modifies the root cause, so EIT has less to compensate for. Concrete failure scenario: when a novel distractor type triggers partial entrainment that EIT's behavioral training has not seen, EIT alone fails because the untrained-for attention pattern disrupts reasoning. Ablation alone fails because heads for this task haven't been identified. Circuit-DPO + EIT succeeds because the internalized circuit modification reduces entrainment activation while EIT provides behavioral robustness to residual effects. PRIMARY COMPARISON 3 — Circuit-DPO vs. output-only DPO and RetMask-style indirect circuit targeting. Benchmarks: the 'Lost in the Noise' evaluation suite (arXiv:2601.07226, referred to as NoisyBench in subsequent literature) with held-out distractor types (train on random documents + irrelevant chat, test on hard negatives), Adaptive Distraction benchmark (NeurIPS 2025, arXiv:2502.01609), and GSM-DC (EMNLP 2025) for math-specific distraction. Baselines: (a) standard DPO, (b) EIT, (c) inference-time head ablation ('Llama See, Llama Do'), (d) RetMask-style head-guided data generation + DPO, (e) KLAAD-style all-head attention divergence during DPO (to isolate circuit-specificity benefit). Key ablations: (a) attention divergence on ALL heads vs. entrainment heads only (KLAAD-style vs. Circuit-DPO — tests circuit targeting vs. general attention regularization), (b) attention divergence on random heads (controls for regularization effect), (c) strict JSD (ε=0) vs. margin-based, (d) periodic head re-identification vs. fixed pre-training heads (tests internalization — if Jaccard similarity decreases over training, the model is redistributing entrainment function), (e) varying re-identification frequency (250/500/1000 steps). Four testable hypotheses: (H1, primary) Composability — Circuit-DPO + EIT yields additive robustness because Circuit-DPO modifies the entrainment mechanism (root cause) while EIT provides behavioral independence from remaining bias cues (compensatory layer), and these operate at orthogonal levels. (H2) Internalization — Circuit-DPO without inference-time intervention outperforms inference-time head ablation on cross-task transfer, because the trained model internalizes distraction resistance that generalizes beyond the specific heads identified during training. (H3) Circuit-DPO achieves stronger within-distraction-type OOD generalization than output-only DPO because it modifies the causal mechanism rather than learning output heuristics. (H4) Circuit-targeted attention divergence (entrainment heads only) outperforms untargeted attention divergence (all heads, KLAAD-style), validating that mechanistic head identification provides value beyond general attention regularization. Task-domain scope: primary claims scoped to within-task-domain transfer (novel distractor types within math reasoning and QA), with cross-domain exploratory experiment (heads discovered on math evaluated on QA and vice versa).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~220h H100 80GB",
      "gpu_utilization": "~25-35%",
      "timeline": "3-4 months",
      "team": "1-2 researchers (mechanistic interpretability + alignment)",
      "estimated_gpu_cost": "$660-880 (at ~$3.00/hr H100 80GB cloud rental)",
      "breakdown": "Head discovery (initial + periodic re-identification infrastructure): 25h. Circuit-DPO training: 70h (35h × 2 models). Baselines (DPO, EIT replication, RetMask-style, inference-time ablation, KLAAD-style all-head divergence): 65h. Ablations (6 variants including head stability, margin vs. strict, re-identification frequency, KLAAD-style comparison): 45h. Evaluation + cross-task transfer experiments: 15h."
    },
    "human_in_loop": {
      "gpu_hours": "~235h H100 80GB",
      "gpu_utilization": "~55-65%",
      "timeline": "8-10 weeks",
      "team": "1 researcher, ~30min/day reviewing agent proposals and results",
      "claude_api_cost": "$150-280",
      "estimated_gpu_cost": "$705-940",
      "risk_note": "Periodic head re-identification adds ~15% training overhead. Qwen2.5-7B GQA ratio requires validation. Head stability during training is the primary technical risk — monitored via Jaccard similarity tracking with early re-identification trigger."
    },
    "auto_research": {
      "gpu_hours": "~260h H100 80GB",
      "gpu_utilization": "~90-95%",
      "timeline": "10-16 days with 4× H100 80GB",
      "team": "0 (initial setup only)",
      "claude_api_cost": "$280-450",
      "estimated_gpu_cost": "$780-1040",
      "speed_bottleneck": "GPU count — with 4× H100, can run 2 models × 2 configurations in parallel. Paired forward passes and periodic head re-identification add ~50% overhead vs. standard DPO",
      "risk_note": "Automated entrainment head discovery may identify spurious circuits without human sanity-checking; Jaccard similarity monitoring partially mitigates this"
    }
  },
  "target_venues": [
    "ARR October 2026 (submission October 12, 2026 — primary target, ~5-month timeline, feeds into ACL 2027 or NAACL 2027)",
    "EACL 2027 (ARR August 3, 2026 — stretch target if progress is rapid, commitment October 11, 2026)"
  ],
  "venue_note": "EMNLP 2026 ARR May 25 deadline is infeasible (8 days from today, 2026-05-17). ARR October 2026 provides a comfortable ~5-month timeline. EACL 2027 (ARR August 3) serves as a stretch target with ~11 weeks.",
  "level": "top-tier",
  "key_references": [
    "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs (ACL 2025, arXiv:2505.09338)",
    "KLAAD: Refining Attention Mechanisms to Reduce Societal Bias in Generative Language Models (EMNLP 2025, arXiv:2507.19962)",
    "From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models [RetMask] (ACL 2026 Findings, arXiv:2601.11020)",
    "Making Bias Non-Predictive: Training Robust LLM Reasoning via Reinforcement Learning [EIT] (arXiv 2026, arXiv:2602.01528)",
    "Mechanistic Interpretability for Large Language Model Alignment: Progress, Challenges, and Future Directions (arXiv 2026, arXiv:2602.11180)",
    "Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search (NeurIPS 2025, arXiv:2502.01609)",
    "Lost in the Noise: How Reasoning Models Fail with Contextual Distractors [RARE/NoisyBench] (arXiv 2025, arXiv:2601.07226)",
    "Thinking Sparks!: Emergent Attention Heads in Reasoning Models During Post Training (arXiv 2025, arXiv:2509.25758)",
    "Quantifying LLM Attention-Head Stability: Implications for Circuit Universality (arXiv 2026, arXiv:2602.16740)",
    "Causal Head Gating: Scalable Attention Head Interpretation [CHG] (NeurIPS 2025, arXiv:2505.13737)",
    "Gated Attention for Large Language Models (NeurIPS 2025 Best Paper, arXiv:2505.06708)",
    "Reinforced Attention Learning [RAL] (arXiv 2026, arXiv:2602.04884)",
    "Distractor Injection Attacks on LLMs: Defense via SFT+RL (arXiv 2025, arXiv:2510.16259)",
    "Circuit-Aware Reward Training [CART] (arXiv 2025, arXiv:2509.24713)",
    "Pref-CTRL: Preference Driven LLM Alignment using Representation Editing (arXiv 2026, arXiv:2604.23543)",
    "Aligning Large Language Models with Representation Editing [RE-Control] (NeurIPS 2024)",
    "Direct Preference Optimization Using Sparse Feature-Level Constraints [FPO] (arXiv 2024, arXiv:2411.07618)",
    "Preference Heads in Large Language Models (arXiv 2026, arXiv:2604.22345)",
    "How Is LLM Reasoning Distracted by Irrelevant Context? [GSM-DC] (EMNLP 2025)",
    "A Comprehensive Survey of Direct Preference Optimization (arXiv 2024, arXiv:2410.15595v3)"
  ],
  "description": "We propose Circuit-DPO, a preference optimization method that INTERNALIZES distraction robustness by augmenting the standard DPO loss with a margin-based Jensen-Shannon divergence term on entrainment heads — attention heads mechanistically responsible for contextual entrainment. Unlike behavioral methods (EIT, standard DPO) that learn compensatory output strategies around the intact entrainment circuit, or inference-time ablation that requires per-task head re-identification and cannot generalize across tasks, Circuit-DPO permanently modifies the entrainment mechanism during training. The near-zero cost of ablation (0.2-3% ICL loss) is not a competing advantage but confirms the SAFETY of circuit-level intervention — these heads can be modified without collateral damage. Our attention reference targets are self-supervised: clean-input attention defines what entrainment heads should approximately do. We use margin-based JSD — L = L_DPO + λ·Σ_h max(JSD(A_h^noisy, A_h^clean) - ε, 0) — tolerating legitimate redistribution while penalizing entrainment. We build on the technical precedent of KLAAD (EMNLP 2025), which established attention-distribution KL as an effective auxiliary training loss for debiasing, but advance beyond it with circuit-specific targeting, DPO integration, and self-supervised references. Periodic head re-identification with Jaccard similarity monitoring tracks circuit drift during training. Our primary hypothesis is twofold: (H1) composability — Circuit-DPO + EIT yields additive robustness because they target orthogonal levels (circuit mechanism vs. behavioral compensation), supported by evidence that RL training leaves core circuits unchanged (arXiv:2602.11180); (H2) internalization — Circuit-DPO without inference-time intervention outperforms inference-time ablation on cross-task transfer, because trained circuit modification generalizes beyond specific identified heads. We explicitly compare against inference-time ablation as a key baseline — the experiment that justifies training-time complexity over inference-time simplicity. Evaluation on the 'Lost in the Noise' evaluation suite (arXiv:2601.07226), Adaptive Distraction benchmark, and GSM-DC, with composability and cross-task transfer as primary analyses. Target: ARR October 2026.",
  "project_name": "circuit_dpo_entrainment",
  "source": "web_research"
}

Output this JSON exactly as provided, with no modifications, no code fences, and no surrounding text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e6de9cf9-ba83-437b-a45e-e1b52f7f1dda",
  "agentId": "a4915e1a3d6ae072f",
  "type": "user",
  "uuid": "6928fbf9-2d7c-4112-80ad-d4a9c577d81e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55cf5ff8-fb6c-4729-a47a-45884b754fea",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T09:17:42.456Z_

```json
{
  "parentUuid": "6928fbf9-2d7c-4112-80ad-d4a9c577d81e",
  "isSidechain": true,
  "agentId": "a4915e1a3d6ae072f",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "454d9525-08ea-42e8-a381-f0f682cf63f6",
  "timestamp": "2026-05-17T09:17:42.456Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55cf5ff8-fb6c-4729-a47a-45884b754fea",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-17T09:19:10.708Z_



{
  "change_type": "major",
  "title": "Circuit-DPO: Internalizing Distraction Robustness via Mechanistically-Targeted Preference Optimization",
  "core_problem": "LLMs suffer catastrophic performance degradation (up to 80% on NoisyBench, >45% average on Adaptive Distraction) when contextual distractors are injected into prompts. Mechanistic analysis ('Llama See, Llama Do,' ACL 2025) identifies specific 'entrainment heads' — attention heads that indiscriminately boost previously-seen context tokens — as the causal mechanism. Current defenses split into two paradigms with complementary limitations: (1) Behavioral approaches (EIT, DPO, SFT+RL) optimize output quality without mechanistic targeting. EIT's balanced conflict RL achieves +39.1% on unseen bias types by making bias cues non-predictive of reward. However, recent mechanistic interpretability evidence shows that behavioral training (RLHF, RL) 'primarily affects specific components related to response initiation and style, while core knowledge and reasoning circuits remain largely unchanged' (arXiv:2602.11180). This means behavioral methods likely learn compensatory output strategies that route AROUND the intact entrainment circuit rather than modifying it — a fragile defense that may break when novel distractor patterns overwhelm the compensatory capacity. Furthermore, EIT's own authors note that 'the non-predictiveness guarantee applies specifically to the injected bias signal; it does not preclude reliance on other shortcuts,' and position bias (structural) shows zero transfer (+0% improvement). (2) Inference-time circuit interventions (head ablation from 'Llama See, Llama Do') directly target entrainment heads with only 0.2-3% ICL cost. Ablation is effective precisely BECAUSE entrainment heads are 'not strongly related to how LMs process and utilise contextual information or perform ICL more broadly' — so suppressing them is cheap. But ablation has three practical limitations: (a) entrainment heads are task-specific, not model-specific, requiring per-task head re-identification via differentiable masking before deployment; (b) ablation is binary (all-or-nothing), unable to handle partial entrainment from subtly related distractors; (c) the mechanistic interpretability literature documents that models contain 'multiple overlapping circuits' for the same behavior, suggesting ablation of identified heads may be compensated by backup pathways. The critical gap: no approach INTERNALIZES distraction robustness at the circuit level during training — permanently modifying the entrainment mechanism so that neither per-task head identification at inference time nor fragile behavioral compensation is needed.",
  "opportunity": "Three convergent opportunities enable Circuit-DPO, which we position as a method that INTERNALIZES circuit-level distraction robustness into model weights during preference optimization: (1) The entrainment circuit foundation from 'Llama See, Llama Do' (ACL 2025) — differentiable masking identifies 30-110 task-specific entrainment heads that can be ablated with minimal ICL cost (0.2-3%). The near-zero ablation cost is not a weakness of our approach but a STRENGTH: it demonstrates these heads are modifiable without breaking broader capabilities, establishing the safety of circuit-level intervention. However, inference-time ablation requires per-task head re-identification and cannot propagate its effects to related circuits. Training-time optimization with gradient flow through these heads can both internalize the intervention and indirectly regularize adjacent circuits. (2) Self-supervised attention targets are freely available in distractor-injection settings: the model's own attention patterns on clean inputs provide a reference distribution for entrainment heads. For any task where clean/noisy input pairs can be constructed (all distractor-injection benchmarks by definition), the clean-attention pattern serves as a soft supervision reference. We use 'reference' rather than 'exact target' because softmax attention is jointly computed over all positions — adding tokens legitimately changes the softmax denominator. Our margin-based constraint tolerates small deviations while penalizing the large shifts characteristic of entrainment. (3) The DPO framework is uniquely suited — it operates on paired preferences and avoids RL instability. Augmenting DPO with attention-distribution divergence on entrainment heads is a natural extension. KLAAD (EMNLP 2025, arXiv:2507.19962) establishes the technical precedent that attention-distribution divergence can serve as an effective auxiliary training loss — it uses KL divergence to align attention between stereotype/anti-stereotype pairs for debiasing. Circuit-DPO advances this mechanism in three ways: targeting mechanistically-identified circuit heads (not all heads in a single layer), integrating into preference optimization (not standard training), and using self-supervised clean-input references (not externally-provided paired examples). RetMask (ACL 2026 Findings, arXiv:2601.11020) bridges head identification with DPO indirectly — using retrieval-head-ablated outputs for contrastive pair generation. Circuit-DPO provides direct gradient signal on attention distributions.",
  "landscape": "The distraction robustness landscape has matured rapidly in 2025-2026, with approaches spanning behavioral training, mechanistic analysis, circuit-level methods, and attention-distribution optimization: (1) Behavioral training methods. EIT (arXiv:2602.01528) achieves +39.1% generalization to unseen bias types via balanced conflict RL — the strongest OOD result, but operating purely at the behavioral level with evidence that RL training leaves core reasoning circuits largely unchanged (arXiv:2602.11180). Standard DPO for distraction (NeurIPS 2025, arXiv:2502.01609) achieves strong in-distribution robustness (+0.485 accuracy on Phi-3.5-mini). RARE (arXiv:2601.07226) uses rationale-aware reward shaping. Distractor Injection defense (arXiv:2510.16259) achieves >50-point improvement via SFT+RL. All modify behavior without targeting the entrainment mechanism. (2) Mechanistic and circuit methods. 'Llama See, Llama Do' (ACL 2025) identifies and ablates entrainment heads at inference time — interpretable but binary, task-specific, and requiring per-task head re-identification. CHG (NeurIPS 2025, arXiv:2505.13737) uses contrastive gating for circuit analysis. 'Thinking Sparks!' (arXiv:2509.25758) demonstrates that post-training causes attention heads to emerge, shift, and be pruned. Bali et al. (arXiv:2602.16740) quantify attention-head stability across training, finding middle-layer heads are least stable but most functionally important. (3) Attention-distribution losses in training. KLAAD (EMNLP 2025, arXiv:2507.19962) is the closest TECHNICAL precedent: it uses KL divergence on attention distributions as an auxiliary training loss to align attention between stereotype/anti-stereotype pairs for debiasing. KLAAD targets all attention heads in the final layer during standard (CE+KL+Triplet) training, without head selection or DPO integration. Circuit-DPO differs in: (a) targeting mechanistically-identified entrainment heads across multiple layers rather than all heads in one layer; (b) integrating into preference optimization rather than standard training; (c) using self-supervised clean-input references rather than externally-constructed paired examples. (4) Mechanistic-interpretability-guided preference optimization. RetMask (ACL 2026 Findings, arXiv:2601.11020) identifies retrieval heads, then generates contrastive pairs by comparing original vs. head-ablated outputs for standard DPO — heads inform DATA CURATION, not the loss function. CART (arXiv:2509.24713) uses circuit analysis to guide data augmentation and regularization for reward model robustness but does not apply circuit-targeted losses during policy optimization. RAL (arXiv:2602.04884) optimizes attention via policy gradient for multimodal LLMs — all attention, not circuit-specific. (5) Architectural and representation methods. Gated Attention (NeurIPS 2025 Best Paper, arXiv:2505.06708) introduces per-head sigmoid gates as a pretraining modification. Pref-CTRL (arXiv:2604.23543) and RE-Control (NeurIPS 2024) operate on hidden states. FPO (arXiv:2411.07618) constrains SAE features during DPO. Circuit-DPO uniquely combines direct attention-level gradient supervision on mechanistically-identified heads with preference optimization, framed as INTERNALIZATION of circuit-level distraction robustness.",
  "approach": "Circuit-DPO augments the standard DPO loss with a margin-based attention-distribution divergence term operating specifically on entrainment heads, with periodic head re-identification to account for circuit drift. The method is framed as INTERNALIZATION: permanently embedding distraction robustness into model weights by modifying the entrainment mechanism during training, eliminating inference-time head identification. Four stages with composability-first evaluation: (1) Entrainment head discovery with periodic refresh. Apply differentiable masking from 'Llama See, Llama Do' (github.com/frankniujc/entrainment) to identify entrainment heads in Llama-3-8B and Qwen2.5-7B. For Qwen2.5-7B (28Q/4KV, different GQA ratio from Llama-3-8B's 32Q/8KV), mask at query-head granularity within each KV group. Because post-training causes attention heads to emerge and shift ('Thinking Sparks!'), re-run head discovery every 500 steps using warm-started logit parameters. If head sets shift substantially between intervals — a known risk given middle-layer instability (Bali et al., arXiv:2602.16740) — the warm-start procedure biases toward the previous head set, providing continuity. We track head-set Jaccard similarity across re-identifications; if similarity drops below 0.5, we trigger early re-identification and log the event for analysis. This monitoring addresses whether head discovery is noisy: if different heads appear each time, it signals that the entrainment function is being redistributed across the network — which is itself evidence of successful internalization. (2) Self-supervised attention reference construction. For each training example, construct paired clean/noisy inputs. Run x_clean through the model and extract attention distributions from entrainment heads over shared context tokens (with stop-gradient). These clean-attention patterns define a REFERENCE distribution. The margin-based loss (Stage 3) tolerates small deviations — inherent to softmax recomputation with additional tokens — while penalizing the large shifts characteristic of entrainment. (3) Circuit-DPO training with margin-based attention constraint. L = L_DPO(y_chosen, y_rejected | x_noisy) + λ · Σ_{h ∈ H_ent} max(JSD(A_h^noisy_shared, A_h^clean_shared) - ε, 0). JSD (Jensen-Shannon divergence) is used because: (a) symmetric — no principled reason to prefer one KL direction; (b) bounded in [0, ln 2], preventing gradient explosion; (c) margin ε has interpretable units (bits of divergence). λ annealed linearly from 0 over first 20% of training. Hyperparameter sweep: ε ∈ {0.01, 0.05, 0.1, 0.2}, λ ∈ {0.1, 0.5, 1.0, 2.0}. (4) Evaluation protocol centered on three key comparisons. PRIMARY COMPARISON 1 — Internalization vs. inference-time ablation: Circuit-DPO (no inference-time intervention) vs. inference-time head ablation on MATCHED distractor types AND cross-task transfer. The critical test: on a new task domain where entrainment heads have NOT been identified, Circuit-DPO should maintain robustness (internalized) while ablation cannot be applied (no head identification). This is the key experiment justifying the method's complexity over simple ablation. PRIMARY COMPARISON 2 — Composability: Circuit-DPO + EIT vs. each alone. The concrete mechanistic argument: EIT teaches the model to produce correct outputs despite bias cues, but mechanistic evidence suggests RL training leaves core circuits largely unchanged (arXiv:2602.11180) — so the entrainment circuit likely still activates on distractors, consuming attention capacity and creating fragile compensation. Circuit-DPO modifies the root cause, so EIT has less to compensate for. Concrete failure scenario: when a novel distractor type triggers partial entrainment that EIT's behavioral training has not seen, EIT alone fails because the untrained-for attention pattern disrupts reasoning. Ablation alone fails because heads for this task haven't been identified. Circuit-DPO + EIT succeeds because the internalized circuit modification reduces entrainment activation while EIT provides behavioral robustness to residual effects. PRIMARY COMPARISON 3 — Circuit-DPO vs. output-only DPO and RetMask-style indirect circuit targeting. Benchmarks: the 'Lost in the Noise' evaluation suite (arXiv:2601.07226, referred to as NoisyBench in subsequent literature) with held-out distractor types (train on random documents + irrelevant chat, test on hard negatives), Adaptive Distraction benchmark (NeurIPS 2025, arXiv:2502.01609), and GSM-DC (EMNLP 2025) for math-specific distraction. Baselines: (a) standard DPO, (b) EIT, (c) inference-time head ablation ('Llama See, Llama Do'), (d) RetMask-style head-guided data generation + DPO, (e) KLAAD-style all-head attention divergence during DPO (to isolate circuit-specificity benefit). Key ablations: (a) attention divergence on ALL heads vs. entrainment heads only (KLAAD-style vs. Circuit-DPO — tests circuit targeting vs. general attention regularization), (b) attention divergence on random heads (controls for regularization effect), (c) strict JSD (ε=0) vs. margin-based, (d) periodic head re-identification vs. fixed pre-training heads (tests internalization — if Jaccard similarity decreases over training, the model is redistributing entrainment function), (e) varying re-identification frequency (250/500/1000 steps). Four testable hypotheses: (H1, primary) Composability — Circuit-DPO + EIT yields additive robustness because Circuit-DPO modifies the entrainment mechanism (root cause) while EIT provides behavioral independence from remaining bias cues (compensatory layer), and these operate at orthogonal levels. (H2) Internalization — Circuit-DPO without inference-time intervention outperforms inference-time head ablation on cross-task transfer, because the trained model internalizes distraction resistance that generalizes beyond the specific heads identified during training. (H3) Circuit-DPO achieves stronger within-distraction-type OOD generalization than output-only DPO because it modifies the causal mechanism rather than learning output heuristics. (H4) Circuit-targeted attention divergence (entrainment heads only) outperforms untargeted attention divergence (all heads, KLAAD-style), validating that mechanistic head identification provides value beyond general attention regularization. Task-domain scope: primary claims scoped to within-task-domain transfer (novel distractor types within math reasoning and QA), with cross-domain exploratory experiment (heads discovered on math evaluated on QA and vice versa).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~220h H100 80GB",
      "gpu_utilization": "~25-35%",
      "timeline": "3-4 months",
      "team": "1-2 researchers (mechanistic interpretability + alignment)",
      "estimated_gpu_cost": "$660-880 (at ~$3.00/hr H100 80GB cloud rental)",
      "breakdown": "Head discovery (initial + periodic re-identification infrastructure): 25h. Circuit-DPO training: 70h (35h × 2 models). Baselines (DPO, EIT replication, RetMask-style, inference-time ablation, KLAAD-style all-head divergence): 65h. Ablations (6 variants including head stability, margin vs. strict, re-identification frequency, KLAAD-style comparison): 45h. Evaluation + cross-task transfer experiments: 15h."
    },
    "human_in_loop": {
      "gpu_hours": "~235h H100 80GB",
      "gpu_utilization": "~55-65%",
      "timeline": "8-10 weeks",
      "team": "1 researcher, ~30min/day reviewing agent proposals and results",
      "claude_api_cost": "$150-280",
      "estimated_gpu_cost": "$705-940",
      "risk_note": "Periodic head re-identification adds ~15% training overhead. Qwen2.5-7B GQA ratio requires validation. Head stability during training is the primary technical risk — monitored via Jaccard similarity tracking with early re-identification trigger."
    },
    "auto_research": {
      "gpu_hours": "~260h H100 80GB",
      "gpu_utilization": "~90-95%",
      "timeline": "10-16 days with 4× H100 80GB",
      "team": "0 (initial setup only)",
      "claude_api_cost": "$280-450",
      "estimated_gpu_cost": "$780-1040",
      "speed_bottleneck": "GPU count — with 4× H100, can run 2 models × 2 configurations in parallel. Paired forward passes and periodic head re-identification add ~50% overhead vs. standard DPO",
      "risk_note": "Automated entrainment head discovery may identify spurious circuits without human sanity-checking; Jaccard similarity monitoring partially mitigates this"
    }
  },
  "target_venues": [
    "ARR October 2026 (submission October 12, 2026 — primary target, ~5-month timeline, feeds into ACL 2027 or NAACL 2027)",
    "EACL 2027 (ARR August 3, 2026 — stretch target if progress is rapid, commitment October 11, 2026)"
  ],
  "venue_note": "EMNLP 2026 ARR May 25 deadline is infeasible (8 days from today, 2026-05-17). ARR October 2026 provides a comfortable ~5-month timeline. EACL 2027 (ARR August 3) serves as a stretch target with ~11 weeks.",
  "level": "top-tier",
  "key_references": [
    "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs (ACL 2025, arXiv:2505.09338)",
    "KLAAD: Refining Attention Mechanisms to Reduce Societal Bias in Generative Language Models (EMNLP 2025, arXiv:2507.19962)",
    "From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models [RetMask] (ACL 2026 Findings, arXiv:2601.11020)",
    "Making Bias Non-Predictive: Training Robust LLM Reasoning via Reinforcement Learning [EIT] (arXiv 2026, arXiv:2602.01528)",
    "Mechanistic Interpretability for Large Language Model Alignment: Progress, Challenges, and Future Directions (arXiv 2026, arXiv:2602.11180)",
    "Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search (NeurIPS 2025, arXiv:2502.01609)",
    "Lost in the Noise: How Reasoning Models Fail with Contextual Distractors [RARE/NoisyBench] (arXiv 2025, arXiv:2601.07226)",
    "Thinking Sparks!: Emergent Attention Heads in Reasoning Models During Post Training (arXiv 2025, arXiv:2509.25758)",
    "Quantifying LLM Attention-Head Stability: Implications for Circuit Universality (arXiv 2026, arXiv:2602.16740)",
    "Causal Head Gating: Scalable Attention Head Interpretation [CHG] (NeurIPS 2025, arXiv:2505.13737)",
    "Gated Attention for Large Language Models (NeurIPS 2025 Best Paper, arXiv:2505.06708)",
    "Reinforced Attention Learning [RAL] (arXiv 2026, arXiv:2602.04884)",
    "Distractor Injection Attacks on LLMs: Defense via SFT+RL (arXiv 2025, arXiv:2510.16259)",
    "Circuit-Aware Reward Training [CART] (arXiv 2025, arXiv:2509.24713)",
    "Pref-CTRL: Preference Driven LLM Alignment using Representation Editing (arXiv 2026, arXiv:2604.23543)",
    "Aligning Large Language Models with Representation Editing [RE-Control] (NeurIPS 2024)",
    "Direct Preference Optimization Using Sparse Feature-Level Constraints [FPO] (arXiv 2024, arXiv:2411.07618)",
    "Preference Heads in Large Language Models (arXiv 2026, arXiv:2604.22345)",
    "How Is LLM Reasoning Distracted by Irrelevant Context? [GSM-DC] (EMNLP 2025)",
    "A Comprehensive Survey of Direct Preference Optimization (arXiv 2024, arXiv:2410.15595v3)"
  ],
  "description": "We propose Circuit-DPO, a preference optimization method that INTERNALIZES distraction robustness by augmenting the standard DPO loss with a margin-based Jensen-Shannon divergence term on entrainment heads — attention heads mechanistically responsible for contextual entrainment. Unlike behavioral methods (EIT, standard DPO) that learn compensatory output strategies around the intact entrainment circuit, or inference-time ablation that requires per-task head re-identification and cannot generalize across tasks, Circuit-DPO permanently modifies the entrainment mechanism during training. The near-zero cost of ablation (0.2-3% ICL loss) is not a competing advantage but confirms the SAFETY of circuit-level intervention — these heads can be modified without collateral damage. Our attention reference targets are self-supervised: clean-input attention defines what entrainment heads should approximately do. We use margin-based JSD — L = L_DPO + λ·Σ_h max(JSD(A_h^noisy, A_h^clean) - ε, 0) — tolerating legitimate redistribution while penalizing entrainment. We build on the technical precedent of KLAAD (EMNLP 2025), which established attention-distribution KL as an effective auxiliary training loss for debiasing, but advance beyond it with circuit-specific targeting, DPO integration, and self-supervised references. Periodic head re-identification with Jaccard similarity monitoring tracks circuit drift during training. Our primary hypothesis is twofold: (H1) composability — Circuit-DPO + EIT yields additive robustness because they target orthogonal levels (circuit mechanism vs. behavioral compensation), supported by evidence that RL training leaves core circuits unchanged (arXiv:2602.11180); (H2) internalization — Circuit-DPO without inference-time intervention outperforms inference-time ablation on cross-task transfer, because trained circuit modification generalizes beyond specific identified heads. We explicitly compare against inference-time ablation as a key baseline — the experiment that justifies training-time complexity over inference-time simplicity. Evaluation on the 'Lost in the Noise' evaluation suite (arXiv:2601.07226), Adaptive Distraction benchmark, and GSM-DC, with composability and cross-task transfer as primary analyses. Target: ARR October 2026.",
  "project_name": "circuit_dpo_entrainment",
  "source": "web_research"
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "454d9525-08ea-42e8-a381-f0f682cf63f6",
  "isSidechain": true,
  "agentId": "a4915e1a3d6ae072f",
  "requestId": "req_011Cb7tbM8cejdMTUmyY51Vu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6fe1a875-ef44-4e8a-b9f3-30a36259b341",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55cf5ff8-fb6c-4729-a47a-45884b754fea",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014WQLd2qbhjQCPrA9j1YHAL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6559,
      "cache_read_input_tokens": 8223,
      "output_tokens": 5942,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6559
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5942,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 6559,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6559,
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
