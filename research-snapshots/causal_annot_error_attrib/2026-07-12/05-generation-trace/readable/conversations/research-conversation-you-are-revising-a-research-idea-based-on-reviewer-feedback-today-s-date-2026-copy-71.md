# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-17 (UTC).** ## Original idea { "tit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/e3e6ae49-b321-4c18-9d68-935c3073671e.jsonl`
- **Structured JSON:** [`0fcd3f70b607336807e1.json`](../../sessions/0f/0fcd3f70b607336807e1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T09:18:34.336Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T09:18:34.336Z",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-17 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Entrainment-Aware Gated Fine-Tuning: Query-Conditional Head Gates for Adaptive Context Utilization\",\n  \"core_problem\": \"LLMs' vulnerability to irrelevant context (distraction) is mechanistically localized to entrainment heads (2.9-10.7% of attention heads per relation, ACL 2025 Outstanding Paper). Static ablation of these heads effectively reduces distraction with only 0.2-3% ICL degradation, confirming they are not part of the core ICL circuit. However, static ablation is a permanent, binary intervention: it unconditionally removes context-sensitivity from these heads regardless of whether the context is relevant or irrelevant. The ACL 2025 paper explicitly acknowledges (Finding 2) that context can be beneficial when relevant — e.g., related-domain context steers generation toward correct answers — yet never evaluates ablation's impact on this capability. In real deployment scenarios (RAG with correct retrievals, long-context QA where context IS the answer source, grounded generation), permanently disabling context-sensitivity is counterproductive. Recent work on RAG head reweighting (PEAR, ACM Web 2025) demonstrates that context-suppressing heads should be continuously attenuated rather than removed, and that learned coefficients outperform binary decisions. Dynamic head selection methods (MoH, ICML 2025; QAdA, 2025) further show that adaptive per-query head activation consistently outperforms static head pruning. The gap: no method combines mechanistic entrainment head identification with query-conditional per-head gating to enable adaptive context utilization — suppressing distraction when context is irrelevant while preserving context-sensitivity when context is helpful.\",\n  \"opportunity\": \"Three building blocks now exist but remain uncombined: (1) The ACL 2025 entrainment paper provides differentiable masking for head discovery across 15 knowledge relations, with code available at github.com/frankniujc/entrainment, and crucially identifies heads whose context-sensitivity is harmful for irrelevant context but potentially beneficial for relevant context; (2) The NeurIPS 2025 Best Paper on gated attention proved that query-dependent per-head sigmoid gates (G1 design: query-projected, post-SDPA) enable heads to modulate their output from full contribution to zero, with per-head gating identified as the single most important design choice; (3) PEAR (ACM Web 2025) demonstrated that learned continuous coefficients on context-affecting heads outperform binary ablation for RAG, validating the premise that learned gating is superior to static head removal. The opportunity is to synthesize these into a fine-tuning intervention that adds query-conditional gates ONLY to mechanistically-identified entrainment heads, training with a dual-objective loss to produce a permanently modified model that adaptively modulates context-sensitivity per query. This requires no inference-time steering, adds negligible parameter overhead (<0.1%), and negligible inference overhead (one linear+sigmoid per gated head).\",\n  \"landscape\": \"**Training-based distraction defense (whole-model):** NoisyInstruct + RARE reward (arXiv:2601.07226, Jan 2026) trains models via SFT+RL on noisy data, achieving strong robustness gains but modifying all parameters without mechanistic targeting. Distractor Injection Attacks defense (arXiv:2510.16259) similarly uses SFT+RL on synthetic adversarial data. GSM-DC (EMNLP 2025) showed continued pretraining with distractors is effective for reasoning robustness. **Training-based (layer-level gating):** Grft (ACL 2025, arXiv:2502.14100) is a key baseline — a gated representation fine-tuning approach applying sigmoid gating at a single layer (layer 7 in Llama-2-7B). Grft achieves strong helpful-context preservation (98.23% short, 97.03% long — nearly matching the ~97% baseline) with meaningful adversarial robustness gains (60-73% without requery, 82-98% with requery). Its actual limitations are: (a) operates at layer-level granularity rather than at mechanistically-identified heads, (b) trained exclusively on knowledge-conflict scenarios (ConflictQA/COUNTERFACT) — untested on reasoning distractors (GSM-DC, NoisyBench), (c) gate is hidden-state-conditional rather than query-conditional, (d) limited to single-context evaluation. Only 36.9K parameters (0.0005% of model). **Learned head reweighting for RAG:** PEAR (ACM Web 2025) identifies context-suppressing attention heads and learns continuous reweighting coefficients via a context-copying proxy task, achieving improved RAG accuracy with zero inference overhead. ADR similarly detects and reweights RAG-suppressing heads. Both validate that learned continuous modulation of head outputs outperforms binary decisions, but neither uses mechanistic head identification or query-conditional gating — coefficients are fixed after training. **Dynamic head selection:** MoH (ICML 2025) treats attention heads as MoE experts with a learned router, achieving +2.4% accuracy over LLaMA3-8B on 14 benchmarks using only 75% of heads. QAdA demonstrates that adaptive per-query head selection outperforms even static oracle selection on long-context tasks. SeerAttention (Microsoft, 2025) shows learned attention gating significantly outperforms static/heuristic sparse attention methods. These demonstrate the superiority of dynamic over static head decisions but are general-purpose, not targeted at distraction resistance. **Inference-time methods:** HAVE (arXiv:2509.06596) applies head-adaptive gating at decoding time for hallucination mitigation — parameter-free but incurs per-query overhead. Focus Directions (arXiv:2503.23306) and ContextFocus (arXiv:2601.04131) steer activations at inference without model modification. All require intervention at every forward pass. **Mechanistic fine-tuning (different targets):** ABFT (arXiv:2505.14233) modifies WQ/WK matrices of induction heads to improve ICL — targets different heads with different goals. **Gated attention (new models only):** NeurIPS 2025 Best Paper and Differential Gated Self-Attention (NeurIPS 2025) are architectural innovations for training new models from scratch — not applicable as fine-tuning interventions. **Our unique position:** EAGT is the first to (1) add learnable query-conditional gates specifically to mechanistically-identified entrainment heads (vs. Grft's layer-level intervention, PEAR's fixed coefficients, or MoH's general-purpose routing), (2) train with explicit adaptive context utilization objectives covering both distraction resistance AND relevant-context preservation (vs. Grft's knowledge-conflict-only training), and (3) leverage the NeurIPS 2025 G1 gate design as a surgical fine-tuning tool targeted by mechanistic analysis.\",\n  \"approach\": \"We propose Entrainment-Aware Gated Fine-Tuning (EAGT) in three phases:\\n\\n**Phase 1: Multi-Relation Entrainment Head Discovery.** Using the differentiable masking procedure from the ACL 2025 paper (Gumbel-sigmoid with straight-through estimation, 500 epochs AdamW, sparsity regularization), we identify entrainment heads in Llama-3.1-8B (32 layers × 32 heads = 1024 heads) across the 15 LRE relations used in the original paper. We take the UNION of discovered heads across all relations. Based on the original paper's findings (2.9-10.7% per relation with partial overlap), we estimate the union set at ~15-20% of heads. This is deliberately broader than any single relation's set — the per-head gate mechanism will learn query-specific activation patterns within this candidate set. We also validate on Qwen3-8B as a secondary model, acknowledging that the differentiable masking procedure has not been previously applied to Qwen architectures and may require hyperparameter adjustment.\\n\\n**Phase 2: Gate Insertion and Fine-Tuning.** We surgically insert G1-style gates (following the NeurIPS 2025 gated attention design) exclusively at union-set heads. Each gate is: g_i = σ(W_g · q_i + b_g) where q_i is the query projection for head i at sequence position i, W_g ∈ ℝ^(1×d_head) is a learnable weight, and b_g is bias. The gate produces a scalar per head per sequence position, modulating the ENTIRE attention output of that head at that position: head_output_i = g_i · Attn(Q_i, K_i, V_i). Critically, this is a per-position decision (whether the model uses attended context at position i), NOT a per-attended-token filter — the gate cannot selectively suppress attention to specific key tokens within a single head's computation. Gates are initialized to output ~1.0 (bias initialized to +3.0) to preserve pretrained behavior.\\n\\nFine-tuning uses a three-component loss with corrected per-position semantics:\\n(L_CLM) Standard causal LM loss on clean data to maintain general capabilities.\\n(L_suppress) At answer/reasoning positions in distractor-augmented examples, penalize high gate values: L_suppress = Σ_{i ∈ S_distracted} g_i², where S_distracted is the set of positions where the model should rely on parametric knowledge rather than distractor-contaminated attention. This teaches entrainment head gates to close when their attention output would propagate irrelevant context.\\n(L_preserve) At answer positions in relevant-context examples (ICL demonstrations, RAG with correct retrievals), penalize low gate values: L_preserve = Σ_{i ∈ S_relevant} (1 - g_i)², where S_relevant is the set of positions where the model should use attended context. This teaches gates to stay open when context IS the answer source.\\n\\nOnly gate parameters and optional rank-4 LoRA on entrainment heads' value projections are updated (<0.1% of total parameters).\\n\\n**Phase 3: Training Data Construction.** Following established synthetic distractor methodology: (a) GSM-DC-style symbolic graph problems with controlled distractor injection for math reasoning, with ground-truth distractor positions known by construction; (b) NoisyInstruct-style augmentation with random documents, irrelevant chat histories, and LLM-generated hard negatives for general QA; (c) Clean versions of (a) and (b) without distractors, plus few-shot ICL demonstrations and RAG examples with verified-correct retrievals, for the preservation objective. The key training signal is positional: at answer-generation positions, should the model rely on attention (gate open) or bypass it (gate closed)?\\n\\n**Evaluation — expanded to directly test the static-ablation gap:**\\n(1) Distraction robustness: GSM-NoOp (ICLR 2025), GSM-DC (EMNLP 2025), NoisyBench (arXiv:2601.07226).\\n(2) **Relevant-context utilization (critical new evaluation):** Performance on RAG benchmarks with correct retrievals (Natural Questions open-domain, TriviaQA with gold passages), long-context QA where context contains the answer (NarrativeQA, QuALITY), and few-shot ICL (SST-2, AGNews, DBPedia). We compare EAGT vs. static ablation vs. no intervention on these tasks to quantify the cost of permanent context-sensitivity removal.\\n(3) General capabilities: MMLU, HellaSwag, ARC-Challenge.\\n(4) Ablations: gate-only vs. gate+LoRA, union-set vs. per-relation gating, gate initialization sensitivity, loss weight sweep, static ablation baseline on all benchmarks.\\n(5) Gate behavior analysis: visualization of learned gate patterns across distractor vs. relevant-context examples, per-relation gate specialization analysis.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~200-280h A100 80GB (entrainment discovery on Llama-3.1-8B: ~30h across 15 relations; Qwen3-8B discovery: ~35h with potential hyperparameter iteration; gate training sweeps: ~80h; expanded evaluation suite including RAG benchmarks: ~50h; ablations: ~60h)\",\n      \"gpu_utilization\": \"~25-35% effective; GPU idles during debugging, result analysis, and experiment design\",\n      \"timeline\": \"8-10 weeks (targeting AAAI 2027 July 28 abstract deadline with comfortable buffer)\",\n      \"team\": \"1-2 researchers with mechanistic interpretability experience\",\n      \"estimated_gpu_cost\": \"$300-$420 at ~$1.50/h\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~280-380h A100 80GB (agent runs systematic discovery across all 15 relations, comprehensive loss-weight sweeps, RAG evaluation)\",\n      \"gpu_utilization\": \"~55-65%; agent batches experiments but pauses for human review of union-set topology and gate training stability\",\n      \"timeline\": \"5-7 weeks (comfortably targeting AAAI 2027 July 28 abstract deadline)\",\n      \"team\": \"1 researcher, ~30min/day for reviewing entrainment head maps and loss diagnostics\",\n      \"claude_api_cost\": \"$250-$400 (~3000-5000 turns)\",\n      \"estimated_gpu_cost\": \"$420-$570 at ~$1.50/h\",\n      \"risk_note\": \"Union-set size may require iteration: if too large (>25%), may need overlap-thresholding; if too sparse (<10%), the positional gate signal may be weak. Qwen3-8B discovery may need architecture-specific adjustments to differentiable masking hyperparameters.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~650-950h A100 80GB (exhaustive multi-relation discovery, full gate-design ablations, cross-model validation, Grft reproduction, static ablation baseline across all benchmarks, RAG evaluation suite)\",\n      \"gpu_utilization\": \"~85-95%; agent continuously pipelines experiments with near-zero idle\",\n      \"timeline\": \"2-3 weeks with 4-8 parallel A100 GPUs\",\n      \"team\": \"0 (initial setup ~3h for environment, datasets, and relation probe data)\",\n      \"claude_api_cost\": \"$550-$950 (~6500-12000 turns)\",\n      \"estimated_gpu_cost\": \"$975-$1,425 at ~$1.50/h\",\n      \"speed_bottleneck\": \"Sequential dependency between discovery phase (per model) and gate training phase; 15-relation discovery parallelizes well across GPUs\",\n      \"risk_note\": \"Agent may over-explore gate architectures (MLP vs linear, shared vs independent bias); estimated 15-20% compute on low-value ablations. Risk of reproducing Grft baseline incorrectly due to limited implementation details in the paper.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract deadline July 21, paper deadline July 28, 2026; strong venue for methodological contributions combining mechanistic interpretability + architectural innovation; comfortable timeline for all execution modes; venue change from originally-requested EMNLP 2026 is necessary because the May 25 ARR deadline is too tight for this major revision; AAAI is well-suited for this work's emphasis on novel AI methodology)\",\n    \"EACL 2027 (ARR deadline August 3, 2026; top European NLP venue; only one ARR cycle available for this conference; strong fit for NLP + interpretability work)\",\n    \"ICLR 2027 (deadline expected ~Sep-Oct 2026, not yet announced; highest-tier ML venue; extra time provides buffer for comprehensive experiments and Qwen3 validation)\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs (ACL 2025, Outstanding Paper, arXiv:2505.09338) — entrainment head discovery via differentiable masking; Finding 2: context can be beneficial when relevant; static ablation causes only 0.2-3% ICL degradation, confirming heads are not ICL circuit\",\n    \"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free (NeurIPS 2025, Best Paper, arXiv:2505.06708) — G1 gate design: query-conditional, post-SDPA sigmoid gates producing per-position per-head scalars; per-head gating identified as most important design choice\",\n    \"Towards Context-Robust LLMs: A Gated Representation Fine-tuning Approach (ACL 2025, arXiv:2502.14100) — KEY BASELINE: layer-level gated fine-tuning for context robustness; achieves 98.23%/97.03% on helpful contexts (comparable to baseline); trained on ConflictQA/COUNTERFACT only; hidden-state-conditional gate\",\n    \"PEAR: Position-Embedding-Agnostic Attention Re-weighting Enhances RAG with Zero Inference Overhead (ACM Web Conference 2025, arXiv:2409.19745) — learned continuous reweighting of context-suppressing heads for RAG; validates that learned coefficients outperform binary ablation; fixed post-training coefficients\",\n    \"MoH: Multi-Head Attention as Mixture-of-Head Attention (ICML 2025, arXiv:2410.11842) — dynamic head selection via learned routing achieves +2.4% over LLaMA3-8B with 75% of heads; demonstrates adaptive head selection > static decisions\",\n    \"Unveiling Simplicities of Attention: Adaptive Long-Context Head Identification (QAdA, arXiv:2502.09647) — adaptive per-query head selection outperforms static oracle criterion on long-context benchmarks\",\n    \"Mechanistic Fine-tuning for In-context Learning (arXiv:2505.14233) — ABFT modifies WQ/WK of induction heads; complementary target and method\",\n    \"Lost in the Noise: How Reasoning Models Fail with Contextual Distractors (arXiv:2601.07226, Jan 2026) — NoisyBench evaluation + NoisyInstruct training methodology + RARE reward\",\n    \"GSM-DC: How Is LLM Reasoning Distracted by Irrelevant Context? (EMNLP 2025) — synthetic DAG-based distractor injection benchmark\",\n    \"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in LLMs (ICLR 2025) — GSM-NoOp benchmark showing up to 65% drops from irrelevant information\",\n    \"Distractor Injection Attacks on Large Reasoning Models: Characterization and Defense (arXiv:2510.16259) — SFT+RL defense baseline on synthetic adversarial data\",\n    \"Focus Directions Make Your Language Models Pay More Attention to Relevant Contexts (arXiv:2503.23306) — inference-time steering baseline\",\n    \"HAVE: Head-Adaptive Gating and ValuE Calibration for Hallucination Mitigation (arXiv:2509.06596) — inference-time head-adaptive gating baseline\",\n    \"SeerAttention: Learning Intrinsic Sparse Attention in Your LLMs (Microsoft, arXiv:2410.13276) — learned attention gating significantly outperforms static/heuristic sparse attention\",\n    \"On the Role of Attention Heads in Large Language Model Safety (ICLR 2025, arXiv:2410.13708) — static ablation of safety heads destroys safety while general benchmarks show no degradation; demonstrates hidden costs of static ablation\",\n    \"Differential Gated Self-Attention (NeurIPS 2025, arXiv:2505.24054) — excitatory/inhibitory gating for new model training; per-token per-head attention weight modulation\"\n  ],\n  \"description\": \"Entrainment-Aware Gated Fine-Tuning (EAGT) addresses the limitations of static ablation as a defense against LLM distraction. While static ablation of entrainment heads (ACL 2025) effectively reduces distraction with minimal ICL cost (0.2-3%), it permanently removes context-sensitivity — a capability that is essential when context IS relevant, such as in RAG with correct retrievals, long-context QA, and grounded generation. The ACL 2025 paper itself acknowledges (Finding 2) that related context can be beneficial, steering generation toward correct answers, yet never evaluates ablation's impact on this beneficial capability. PEAR (ACM Web 2025) independently validates that context-affecting heads require continuous learned modulation rather than binary removal, and MoH (ICML 2025) demonstrates that dynamic head selection outperforms static decisions by +2.4%. EAGT fills the gap between static ablation (always suppress) and no intervention (always vulnerable) by: (1) discovering the union set of entrainment heads across 15 knowledge relations via differentiable masking (~15-20% of heads), (2) inserting query-conditional sigmoid gates (NeurIPS 2025 G1 design) exclusively at these heads, initialized to preserve pretrained behavior, and (3) fine-tuning with a positionally-supervised loss — gate suppression at answer positions in distractor-augmented examples, and gate preservation at answer positions in relevant-context examples (RAG with gold passages, ICL demonstrations). The gate operates per-position per-head: at each sequence position, it modulates the entire attention output of the gated head, controlling whether the model uses attended context or relies on the residual stream. Key advantages over Grft: head-level vs layer-level granularity, query-conditional gating, mechanistic targeting, and training on both reasoning distractors and knowledge conflicts (vs. Grft's ConflictQA-only training). Key advantages over static ablation: adaptive per-query context-sensitivity modulation with zero permanent capability loss. Key advantages over inference-time methods (HAVE, Focus Directions): no per-query overhead, permanently improved model. Evaluation on Llama-3.1-8B (primary) and Qwen3-8B (secondary, with acknowledged validation risk) across distraction benchmarks (GSM-NoOp, GSM-DC, NoisyBench), relevant-context benchmarks (NQ open-domain, TriviaQA with gold passages, NarrativeQA), ICL tasks, and general capabilities (MMLU, HellaSwag) will demonstrate that EAGT achieves distraction resistance comparable to static ablation while preserving context utilization that static ablation sacrifices.\",\n  \"project_name\": \"entrainment_gated_ft\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 4)\nIssues: [\"IMPORTANT: Missing key baseline — RetMask (arXiv:2601.11020, Jan 2026) trains models using retrieval head masking-based contrastive signals (SFT+DPO), achieving +2.28 on HELMET at 128K. This is the closest published work to EAGT's premise of 'use mechanistically-identified heads to improve training' and must be discussed as a primary baseline.\", \"IMPORTANT: 'Retrieval Heads are Dynamic' (arXiv:2602.11162, Feb 2026) shows that at any generation step, only 18-46% of dynamically-active retrieval heads overlap with statically-identified top-20 heads. If entrainment heads exhibit similar dynamism, EAGT's approach of targeting a FIXED union set (even with dynamic gates) may be fundamentally limited. The proposal must either argue why entrainment heads are more stable than retrieval heads (plausible: causal identification via differentiable masking vs. heuristic attention-pattern identification) or acknowledge this as a limitation.\", \"MODERATE: Causal Head Gating (CHG, arXiv:2505.13737, NeurIPS 2025) learns per-head static gating values via next-token prediction. This is the natural ablation baseline: comparing EAGT's query-conditional gates against CHG-style static gates directly demonstrates the value of query-conditioning. Currently missing from the baselines.\", \"MODERATE: The 'combination paper' risk is not sufficiently addressed. The proposal combines (A) entrainment head identification + (B) G1 gate design + (C) dual-objective loss. Each building block is from a top-venue paper. Reviewers will ask: 'What is non-trivial about this combination?' The answer should focus on the training signal design challenge — specifically, why positional supervision (gate suppression at answer positions) produces query-conditional behavior rather than collapsing to a static gate value, and what prevents trivial solutions.\", \"MINOR: The user explicitly requested EMNLP 2026 ARR. While the venue change is necessary (May 25 deadline is 8 days away), consider targeting EACL 2027 (ARR August 3) as the PRIMARY venue since it's the closest NLP venue with adequate timeline, rather than AAAI 2027 which is an AI/general venue.\"]\nFeedback: The proposal has substantially improved from previous rounds — the motivation is now correctly framed (static ablation's hidden cost on relevant-context tasks rather than the disproven 'destroys ICL' claim), the gate semantics are properly specified, and the Grft comparison is accurate. Two key additions needed:\n\n1. **Add RetMask (arXiv:2601.11020) as a primary baseline.** RetMask also bridges 'head identification → training improvement' but uses masking for contrastive data generation rather than learned gating. Differentiate: EAGT adds permanent query-conditional gates (architectural modification), while RetMask uses head masking only to generate training signal (behavioral modification via SFT/DPO). EAGT's gates produce a permanently modified model with no inference overhead beyond the gate computation; RetMask trains the full model.\n\n2. **Address the 'dynamic heads' challenge.** Cite 'Retrieval Heads are Dynamic' (arXiv:2602.11162) and argue that entrainment heads, identified via causal differentiable masking (gradient-based, functional), may be more stable than retrieval heads identified via attention-pattern heuristics (activation-based, correlational). The entrainment heads implement a specific mechanism (logit boosting for context-seen tokens) that is architecturally localized, whereas 'retrieval heads' are defined by behavioral patterns that may shift per input. This is actually a STRENGTH of your approach — you target a causally-identified circuit, not a correlational pattern.\n\n3. **Add CHG as a static-gate ablation.** Run EAGT with static (non-query-conditional) per-head gate values as an ablation. If query-conditional gates significantly outperform static gates on the relevant-context preservation task while matching on distraction suppression, this demonstrates the core contribution.\n\n4. **Strengthen the 'non-trivial combination' argument.** Address why the dual-objective loss doesn't collapse to a trivial solution. Key insight: the SAME head appears in both L_suppress (when context is irrelevant) and L_preserve (when context is relevant), so the gate MUST learn query-conditional behavior to minimize both losses simultaneously — it cannot settle on a fixed value. This is the theoretical crux that makes the combination non-trivial.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\")."
}
```

---

### Runtime record

_source line 2 · 2026-05-17T09:18:34.340Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T09:18:34.340Z",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e"
}
```

---

## Round 1

59 recorded events

### User

_source line 3 · 2026-05-17T09:18:34.381Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-17 (UTC).**

## Original idea
{
  "title": "Entrainment-Aware Gated Fine-Tuning: Query-Conditional Head Gates for Adaptive Context Utilization",
  "core_problem": "LLMs' vulnerability to irrelevant context (distraction) is mechanistically localized to entrainment heads (2.9-10.7% of attention heads per relation, ACL 2025 Outstanding Paper). Static ablation of these heads effectively reduces distraction with only 0.2-3% ICL degradation, confirming they are not part of the core ICL circuit. However, static ablation is a permanent, binary intervention: it unconditionally removes context-sensitivity from these heads regardless of whether the context is relevant or irrelevant. The ACL 2025 paper explicitly acknowledges (Finding 2) that context can be beneficial when relevant — e.g., related-domain context steers generation toward correct answers — yet never evaluates ablation's impact on this capability. In real deployment scenarios (RAG with correct retrievals, long-context QA where context IS the answer source, grounded generation), permanently disabling context-sensitivity is counterproductive. Recent work on RAG head reweighting (PEAR, ACM Web 2025) demonstrates that context-suppressing heads should be continuously attenuated rather than removed, and that learned coefficients outperform binary decisions. Dynamic head selection methods (MoH, ICML 2025; QAdA, 2025) further show that adaptive per-query head activation consistently outperforms static head pruning. The gap: no method combines mechanistic entrainment head identification with query-conditional per-head gating to enable adaptive context utilization — suppressing distraction when context is irrelevant while preserving context-sensitivity when context is helpful.",
  "opportunity": "Three building blocks now exist but remain uncombined: (1) The ACL 2025 entrainment paper provides differentiable masking for head discovery across 15 knowledge relations, with code available at github.com/frankniujc/entrainment, and crucially identifies heads whose context-sensitivity is harmful for irrelevant context but potentially beneficial for relevant context; (2) The NeurIPS 2025 Best Paper on gated attention proved that query-dependent per-head sigmoid gates (G1 design: query-projected, post-SDPA) enable heads to modulate their output from full contribution to zero, with per-head gating identified as the single most important design choice; (3) PEAR (ACM Web 2025) demonstrated that learned continuous coefficients on context-affecting heads outperform binary ablation for RAG, validating the premise that learned gating is superior to static head removal. The opportunity is to synthesize these into a fine-tuning intervention that adds query-conditional gates ONLY to mechanistically-identified entrainment heads, training with a dual-objective loss to produce a permanently modified model that adaptively modulates context-sensitivity per query. This requires no inference-time steering, adds negligible parameter overhead (<0.1%), and negligible inference overhead (one linear+sigmoid per gated head).",
  "landscape": "**Training-based distraction defense (whole-model):** NoisyInstruct + RARE reward (arXiv:2601.07226, Jan 2026) trains models via SFT+RL on noisy data, achieving strong robustness gains but modifying all parameters without mechanistic targeting. Distractor Injection Attacks defense (arXiv:2510.16259) similarly uses SFT+RL on synthetic adversarial data. GSM-DC (EMNLP 2025) showed continued pretraining with distractors is effective for reasoning robustness. **Training-based (layer-level gating):** Grft (ACL 2025, arXiv:2502.14100) is a key baseline — a gated representation fine-tuning approach applying sigmoid gating at a single layer (layer 7 in Llama-2-7B). Grft achieves strong helpful-context preservation (98.23% short, 97.03% long — nearly matching the ~97% baseline) with meaningful adversarial robustness gains (60-73% without requery, 82-98% with requery). Its actual limitations are: (a) operates at layer-level granularity rather than at mechanistically-identified heads, (b) trained exclusively on knowledge-conflict scenarios (ConflictQA/COUNTERFACT) — untested on reasoning distractors (GSM-DC, NoisyBench), (c) gate is hidden-state-conditional rather than query-conditional, (d) limited to single-context evaluation. Only 36.9K parameters (0.0005% of model). **Learned head reweighting for RAG:** PEAR (ACM Web 2025) identifies context-suppressing attention heads and learns continuous reweighting coefficients via a context-copying proxy task, achieving improved RAG accuracy with zero inference overhead. ADR similarly detects and reweights RAG-suppressing heads. Both validate that learned continuous modulation of head outputs outperforms binary decisions, but neither uses mechanistic head identification or query-conditional gating — coefficients are fixed after training. **Dynamic head selection:** MoH (ICML 2025) treats attention heads as MoE experts with a learned router, achieving +2.4% accuracy over LLaMA3-8B on 14 benchmarks using only 75% of heads. QAdA demonstrates that adaptive per-query head selection outperforms even static oracle selection on long-context tasks. SeerAttention (Microsoft, 2025) shows learned attention gating significantly outperforms static/heuristic sparse attention methods. These demonstrate the superiority of dynamic over static head decisions but are general-purpose, not targeted at distraction resistance. **Inference-time methods:** HAVE (arXiv:2509.06596) applies head-adaptive gating at decoding time for hallucination mitigation — parameter-free but incurs per-query overhead. Focus Directions (arXiv:2503.23306) and ContextFocus (arXiv:2601.04131) steer activations at inference without model modification. All require intervention at every forward pass. **Mechanistic fine-tuning (different targets):** ABFT (arXiv:2505.14233) modifies WQ/WK matrices of induction heads to improve ICL — targets different heads with different goals. **Gated attention (new models only):** NeurIPS 2025 Best Paper and Differential Gated Self-Attention (NeurIPS 2025) are architectural innovations for training new models from scratch — not applicable as fine-tuning interventions. **Our unique position:** EAGT is the first to (1) add learnable query-conditional gates specifically to mechanistically-identified entrainment heads (vs. Grft's layer-level intervention, PEAR's fixed coefficients, or MoH's general-purpose routing), (2) train with explicit adaptive context utilization objectives covering both distraction resistance AND relevant-context preservation (vs. Grft's knowledge-conflict-only training), and (3) leverage the NeurIPS 2025 G1 gate design as a surgical fine-tuning tool targeted by mechanistic analysis.",
  "approach": "We propose Entrainment-Aware Gated Fine-Tuning (EAGT) in three phases:\n\n**Phase 1: Multi-Relation Entrainment Head Discovery.** Using the differentiable masking procedure from the ACL 2025 paper (Gumbel-sigmoid with straight-through estimation, 500 epochs AdamW, sparsity regularization), we identify entrainment heads in Llama-3.1-8B (32 layers × 32 heads = 1024 heads) across the 15 LRE relations used in the original paper. We take the UNION of discovered heads across all relations. Based on the original paper's findings (2.9-10.7% per relation with partial overlap), we estimate the union set at ~15-20% of heads. This is deliberately broader than any single relation's set — the per-head gate mechanism will learn query-specific activation patterns within this candidate set. We also validate on Qwen3-8B as a secondary model, acknowledging that the differentiable masking procedure has not been previously applied to Qwen architectures and may require hyperparameter adjustment.\n\n**Phase 2: Gate Insertion and Fine-Tuning.** We surgically insert G1-style gates (following the NeurIPS 2025 gated attention design) exclusively at union-set heads. Each gate is: g_i = σ(W_g · q_i + b_g) where q_i is the query projection for head i at sequence position i, W_g ∈ ℝ^(1×d_head) is a learnable weight, and b_g is bias. The gate produces a scalar per head per sequence position, modulating the ENTIRE attention output of that head at that position: head_output_i = g_i · Attn(Q_i, K_i, V_i). Critically, this is a per-position decision (whether the model uses attended context at position i), NOT a per-attended-token filter — the gate cannot selectively suppress attention to specific key tokens within a single head's computation. Gates are initialized to output ~1.0 (bias initialized to +3.0) to preserve pretrained behavior.\n\nFine-tuning uses a three-component loss with corrected per-position semantics:\n(L_CLM) Standard causal LM loss on clean data to maintain general capabilities.\n(L_suppress) At answer/reasoning positions in distractor-augmented examples, penalize high gate values: L_suppress = Σ_{i ∈ S_distracted} g_i², where S_distracted is the set of positions where the model should rely on parametric knowledge rather than distractor-contaminated attention. This teaches entrainment head gates to close when their attention output would propagate irrelevant context.\n(L_preserve) At answer positions in relevant-context examples (ICL demonstrations, RAG with correct retrievals), penalize low gate values: L_preserve = Σ_{i ∈ S_relevant} (1 - g_i)², where S_relevant is the set of positions where the model should use attended context. This teaches gates to stay open when context IS the answer source.\n\nOnly gate parameters and optional rank-4 LoRA on entrainment heads' value projections are updated (<0.1% of total parameters).\n\n**Phase 3: Training Data Construction.** Following established synthetic distractor methodology: (a) GSM-DC-style symbolic graph problems with controlled distractor injection for math reasoning, with ground-truth distractor positions known by construction; (b) NoisyInstruct-style augmentation with random documents, irrelevant chat histories, and LLM-generated hard negatives for general QA; (c) Clean versions of (a) and (b) without distractors, plus few-shot ICL demonstrations and RAG examples with verified-correct retrievals, for the preservation objective. The key training signal is positional: at answer-generation positions, should the model rely on attention (gate open) or bypass it (gate closed)?\n\n**Evaluation — expanded to directly test the static-ablation gap:**\n(1) Distraction robustness: GSM-NoOp (ICLR 2025), GSM-DC (EMNLP 2025), NoisyBench (arXiv:2601.07226).\n(2) **Relevant-context utilization (critical new evaluation):** Performance on RAG benchmarks with correct retrievals (Natural Questions open-domain, TriviaQA with gold passages), long-context QA where context contains the answer (NarrativeQA, QuALITY), and few-shot ICL (SST-2, AGNews, DBPedia). We compare EAGT vs. static ablation vs. no intervention on these tasks to quantify the cost of permanent context-sensitivity removal.\n(3) General capabilities: MMLU, HellaSwag, ARC-Challenge.\n(4) Ablations: gate-only vs. gate+LoRA, union-set vs. per-relation gating, gate initialization sensitivity, loss weight sweep, static ablation baseline on all benchmarks.\n(5) Gate behavior analysis: visualization of learned gate patterns across distractor vs. relevant-context examples, per-relation gate specialization analysis.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~200-280h A100 80GB (entrainment discovery on Llama-3.1-8B: ~30h across 15 relations; Qwen3-8B discovery: ~35h with potential hyperparameter iteration; gate training sweeps: ~80h; expanded evaluation suite including RAG benchmarks: ~50h; ablations: ~60h)",
      "gpu_utilization": "~25-35% effective; GPU idles during debugging, result analysis, and experiment design",
      "timeline": "8-10 weeks (targeting AAAI 2027 July 28 abstract deadline with comfortable buffer)",
      "team": "1-2 researchers with mechanistic interpretability experience",
      "estimated_gpu_cost": "$300-$420 at ~$1.50/h"
    },
    "human_in_loop": {
      "gpu_hours": "~280-380h A100 80GB (agent runs systematic discovery across all 15 relations, comprehensive loss-weight sweeps, RAG evaluation)",
      "gpu_utilization": "~55-65%; agent batches experiments but pauses for human review of union-set topology and gate training stability",
      "timeline": "5-7 weeks (comfortably targeting AAAI 2027 July 28 abstract deadline)",
      "team": "1 researcher, ~30min/day for reviewing entrainment head maps and loss diagnostics",
      "claude_api_cost": "$250-$400 (~3000-5000 turns)",
      "estimated_gpu_cost": "$420-$570 at ~$1.50/h",
      "risk_note": "Union-set size may require iteration: if too large (>25%), may need overlap-thresholding; if too sparse (<10%), the positional gate signal may be weak. Qwen3-8B discovery may need architecture-specific adjustments to differentiable masking hyperparameters."
    },
    "auto_research": {
      "gpu_hours": "~650-950h A100 80GB (exhaustive multi-relation discovery, full gate-design ablations, cross-model validation, Grft reproduction, static ablation baseline across all benchmarks, RAG evaluation suite)",
      "gpu_utilization": "~85-95%; agent continuously pipelines experiments with near-zero idle",
      "timeline": "2-3 weeks with 4-8 parallel A100 GPUs",
      "team": "0 (initial setup ~3h for environment, datasets, and relation probe data)",
      "claude_api_cost": "$550-$950 (~6500-12000 turns)",
      "estimated_gpu_cost": "$975-$1,425 at ~$1.50/h",
      "speed_bottleneck": "Sequential dependency between discovery phase (per model) and gate training phase; 15-relation discovery parallelizes well across GPUs",
      "risk_note": "Agent may over-explore gate architectures (MLP vs linear, shared vs independent bias); estimated 15-20% compute on low-value ablations. Risk of reproducing Grft baseline incorrectly due to limited implementation details in the paper."
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract deadline July 21, paper deadline July 28, 2026; strong venue for methodological contributions combining mechanistic interpretability + architectural innovation; comfortable timeline for all execution modes; venue change from originally-requested EMNLP 2026 is necessary because the May 25 ARR deadline is too tight for this major revision; AAAI is well-suited for this work's emphasis on novel AI methodology)",
    "EACL 2027 (ARR deadline August 3, 2026; top European NLP venue; only one ARR cycle available for this conference; strong fit for NLP + interpretability work)",
    "ICLR 2027 (deadline expected ~Sep-Oct 2026, not yet announced; highest-tier ML venue; extra time provides buffer for comprehensive experiments and Qwen3 validation)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs (ACL 2025, Outstanding Paper, arXiv:2505.09338) — entrainment head discovery via differentiable masking; Finding 2: context can be beneficial when relevant; static ablation causes only 0.2-3% ICL degradation, confirming heads are not ICL circuit",
    "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free (NeurIPS 2025, Best Paper, arXiv:2505.06708) — G1 gate design: query-conditional, post-SDPA sigmoid gates producing per-position per-head scalars; per-head gating identified as most important design choice",
    "Towards Context-Robust LLMs: A Gated Representation Fine-tuning Approach (ACL 2025, arXiv:2502.14100) — KEY BASELINE: layer-level gated fine-tuning for context robustness; achieves 98.23%/97.03% on helpful contexts (comparable to baseline); trained on ConflictQA/COUNTERFACT only; hidden-state-conditional gate",
    "PEAR: Position-Embedding-Agnostic Attention Re-weighting Enhances RAG with Zero Inference Overhead (ACM Web Conference 2025, arXiv:2409.19745) — learned continuous reweighting of context-suppressing heads for RAG; validates that learned coefficients outperform binary ablation; fixed post-training coefficients",
    "MoH: Multi-Head Attention as Mixture-of-Head Attention (ICML 2025, arXiv:2410.11842) — dynamic head selection via learned routing achieves +2.4% over LLaMA3-8B with 75% of heads; demonstrates adaptive head selection > static decisions",
    "Unveiling Simplicities of Attention: Adaptive Long-Context Head Identification (QAdA, arXiv:2502.09647) — adaptive per-query head selection outperforms static oracle criterion on long-context benchmarks",
    "Mechanistic Fine-tuning for In-context Learning (arXiv:2505.14233) — ABFT modifies WQ/WK of induction heads; complementary target and method",
    "Lost in the Noise: How Reasoning Models Fail with Contextual Distractors (arXiv:2601.07226, Jan 2026) — NoisyBench evaluation + NoisyInstruct training methodology + RARE reward",
    "GSM-DC: How Is LLM Reasoning Distracted by Irrelevant Context? (EMNLP 2025) — synthetic DAG-based distractor injection benchmark",
    "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in LLMs (ICLR 2025) — GSM-NoOp benchmark showing up to 65% drops from irrelevant information",
    "Distractor Injection Attacks on Large Reasoning Models: Characterization and Defense (arXiv:2510.16259) — SFT+RL defense baseline on synthetic adversarial data",
    "Focus Directions Make Your Language Models Pay More Attention to Relevant Contexts (arXiv:2503.23306) — inference-time steering baseline",
    "HAVE: Head-Adaptive Gating and ValuE Calibration for Hallucination Mitigation (arXiv:2509.06596) — inference-time head-adaptive gating baseline",
    "SeerAttention: Learning Intrinsic Sparse Attention in Your LLMs (Microsoft, arXiv:2410.13276) — learned attention gating significantly outperforms static/heuristic sparse attention",
    "On the Role of Attention Heads in Large Language Model Safety (ICLR 2025, arXiv:2410.13708) — static ablation of safety heads destroys safety while general benchmarks show no degradation; demonstrates hidden costs of static ablation",
    "Differential Gated Self-Attention (NeurIPS 2025, arXiv:2505.24054) — excitatory/inhibitory gating for new model training; per-token per-head attention weight modulation"
  ],
  "description": "Entrainment-Aware Gated Fine-Tuning (EAGT) addresses the limitations of static ablation as a defense against LLM distraction. While static ablation of entrainment heads (ACL 2025) effectively reduces distraction with minimal ICL cost (0.2-3%), it permanently removes context-sensitivity — a capability that is essential when context IS relevant, such as in RAG with correct retrievals, long-context QA, and grounded generation. The ACL 2025 paper itself acknowledges (Finding 2) that related context can be beneficial, steering generation toward correct answers, yet never evaluates ablation's impact on this beneficial capability. PEAR (ACM Web 2025) independently validates that context-affecting heads require continuous learned modulation rather than binary removal, and MoH (ICML 2025) demonstrates that dynamic head selection outperforms static decisions by +2.4%. EAGT fills the gap between static ablation (always suppress) and no intervention (always vulnerable) by: (1) discovering the union set of entrainment heads across 15 knowledge relations via differentiable masking (~15-20% of heads), (2) inserting query-conditional sigmoid gates (NeurIPS 2025 G1 design) exclusively at these heads, initialized to preserve pretrained behavior, and (3) fine-tuning with a positionally-supervised loss — gate suppression at answer positions in distractor-augmented examples, and gate preservation at answer positions in relevant-context examples (RAG with gold passages, ICL demonstrations). The gate operates per-position per-head: at each sequence position, it modulates the entire attention output of the gated head, controlling whether the model uses attended context or relies on the residual stream. Key advantages over Grft: head-level vs layer-level granularity, query-conditional gating, mechanistic targeting, and training on both reasoning distractors and knowledge conflicts (vs. Grft's ConflictQA-only training). Key advantages over static ablation: adaptive per-query context-sensitivity modulation with zero permanent capability loss. Key advantages over inference-time methods (HAVE, Focus Directions): no per-query overhead, permanently improved model. Evaluation on Llama-3.1-8B (primary) and Qwen3-8B (secondary, with acknowledged validation risk) across distraction benchmarks (GSM-NoOp, GSM-DC, NoisyBench), relevant-context benchmarks (NQ open-domain, TriviaQA with gold passages, NarrativeQA), ICL tasks, and general capabilities (MMLU, HellaSwag) will demonstrate that EAGT achieves distraction resistance comparable to static ablation while preserving context utilization that static ablation sacrifices.",
  "project_name": "entrainment_gated_ft",
  "source": "web_research"
}

## Reviewer feedback (round 4)
Issues: ["IMPORTANT: Missing key baseline — RetMask (arXiv:2601.11020, Jan 2026) trains models using retrieval head masking-based contrastive signals (SFT+DPO), achieving +2.28 on HELMET at 128K. This is the closest published work to EAGT's premise of 'use mechanistically-identified heads to improve training' and must be discussed as a primary baseline.", "IMPORTANT: 'Retrieval Heads are Dynamic' (arXiv:2602.11162, Feb 2026) shows that at any generation step, only 18-46% of dynamically-active retrieval heads overlap with statically-identified top-20 heads. If entrainment heads exhibit similar dynamism, EAGT's approach of targeting a FIXED union set (even with dynamic gates) may be fundamentally limited. The proposal must either argue why entrainment heads are more stable than retrieval heads (plausible: causal identification via differentiable masking vs. heuristic attention-pattern identification) or acknowledge this as a limitation.", "MODERATE: Causal Head Gating (CHG, arXiv:2505.13737, NeurIPS 2025) learns per-head static gating values via next-token prediction. This is the natural ablation baseline: comparing EAGT's query-conditional gates against CHG-style static gates directly demonstrates the value of query-conditioning. Currently missing from the baselines.", "MODERATE: The 'combination paper' risk is not sufficiently addressed. The proposal combines (A) entrainment head identification + (B) G1 gate design + (C) dual-objective loss. Each building block is from a top-venue paper. Reviewers will ask: 'What is non-trivial about this combination?' The answer should focus on the training signal design challenge — specifically, why positional supervision (gate suppression at answer positions) produces query-conditional behavior rather than collapsing to a static gate value, and what prevents trivial solutions.", "MINOR: The user explicitly requested EMNLP 2026 ARR. While the venue change is necessary (May 25 deadline is 8 days away), consider targeting EACL 2027 (ARR August 3) as the PRIMARY venue since it's the closest NLP venue with adequate timeline, rather than AAAI 2027 which is an AI/general venue."]
Feedback: The proposal has substantially improved from previous rounds — the motivation is now correctly framed (static ablation's hidden cost on relevant-context tasks rather than the disproven 'destroys ICL' claim), the gate semantics are properly specified, and the Grft comparison is accurate. Two key additions needed:

1. **Add RetMask (arXiv:2601.11020) as a primary baseline.** RetMask also bridges 'head identification → training improvement' but uses masking for contrastive data generation rather than learned gating. Differentiate: EAGT adds permanent query-conditional gates (architectural modification), while RetMask uses head masking only to generate training signal (behavioral modification via SFT/DPO). EAGT's gates produce a permanently modified model with no inference overhead beyond the gate computation; RetMask trains the full model.

2. **Address the 'dynamic heads' challenge.** Cite 'Retrieval Heads are Dynamic' (arXiv:2602.11162) and argue that entrainment heads, identified via causal differentiable masking (gradient-based, functional), may be more stable than retrieval heads identified via attention-pattern heuristics (activation-based, correlational). The entrainment heads implement a specific mechanism (logit boosting for context-seen tokens) that is architecturally localized, whereas 'retrieval heads' are defined by behavioral patterns that may shift per input. This is actually a STRENGTH of your approach — you target a causally-identified circuit, not a correlational pattern.

3. **Add CHG as a static-gate ablation.** Run EAGT with static (non-query-conditional) per-head gate values as an ablation. If query-conditional gates significantly outperform static gates on the relevant-context preservation task while matching on distraction suppression, this demonstrates the core contribution.

4. **Strengthen the 'non-trivial combination' argument.** Address why the dual-objective loss doesn't collapse to a trivial solution. Key insight: the SAME head appears in both L_suppress (when context is irrelevant) and L_preserve (when context is relevant), so the gate MUST learn query-conditional behavior to minimize both losses simultaneously — it cannot settle on a fixed value. This is the theoretical crux that makes the combination non-trivial.

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "8052165b-6c36-40b2-ade0-6fd88ae7524b",
  "type": "user",
  "uuid": "1298c582-214f-4f7d-bf45-69e7db81304a",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T09:18:34.379Z_

```json
{
  "parentUuid": "1298c582-214f-4f7d-bf45-69e7db81304a",
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
  "uuid": "eb691af5-d5fb-49c7-94b5-506ecea27fdc",
  "timestamp": "2026-05-17T09:18:34.379Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T09:18:34.379Z_

```json
{
  "parentUuid": "eb691af5-d5fb-49c7-94b5-506ecea27fdc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "81a493f7-1163-48b1-a5f3-b276cd894e71",
  "timestamp": "2026-05-17T09:18:34.379Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-17 (UTC).**  ## Original idea {   \"title\": \"Entrainment-Aware Gated Fine-Tuning: Query-Conditional Head Gates for…",
  "leafUuid": "81a493f7-1163-48b1-a5f3-b276cd894e71",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise EAGT with RetMask, dynamic heads, and query-conditional ablation",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e"
}
```

---

### Assistant

_source line 8 · 2026-05-17T09:18:42.528Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully before diving into research:

1. **RetMask (arXiv:2601.11020)** - Need to find and read this paper about retrieval head masking-based contrastive signals
2. **"Retrieval Heads are Dynamic" (arXiv:2602.11162)** - Need to find and read this about dynamic nature of retrieval heads
3. **CHG (arXiv:2505.13737)** - Causal Head Gating, need to find and read
4. **"Combination paper" risk** - Need to strengthen the argument for non-trivial combination


5. **Venue suggestion** - EACL 2027 looks like a strong fit as the primary target

Now I'll start searching for these papers to understand what the reviewers are referencing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81a493f7-1163-48b1-a5f3-b276cd894e71",
  "isSidechain": false,
  "requestId": "req_011Cb7tfBJNwkiaU6jErGRUh",
  "type": "assistant",
  "uuid": "ee078fa6-97f1-40f9-8c38-43bfaea14ddb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qmc54zTGgLDojzydtEnJzW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12951,
      "cache_read_input_tokens": 11841,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12951
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

_source line 9 · 2026-05-17T09:18:42.672Z_

I'll research the papers and issues flagged by the reviewer before revising. Let me search for all three key papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee078fa6-97f1-40f9-8c38-43bfaea14ddb",
  "isSidechain": false,
  "requestId": "req_011Cb7tfBJNwkiaU6jErGRUh",
  "type": "assistant",
  "uuid": "a3431e8f-0515-458f-8cc4-46a17efd5423",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qmc54zTGgLDojzydtEnJzW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12951,
      "cache_read_input_tokens": 11841,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12951
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

_source line 10 · 2026-05-17T09:18:43.215Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EAYd619khpozEDknp1KtiP`</summary>

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
  "parentUuid": "a3431e8f-0515-458f-8cc4-46a17efd5423",
  "isSidechain": false,
  "requestId": "req_011Cb7tfBJNwkiaU6jErGRUh",
  "type": "assistant",
  "uuid": "47f503ec-cf14-4586-9d9a-cb03ae7ce7d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qmc54zTGgLDojzydtEnJzW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12951,
      "cache_read_input_tokens": 11841,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12951
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

_source line 11 · 2026-05-17T09:18:43.222Z_

<details><summary>↩ Tool result · `toolu_01EAYd619khpozEDknp1KtiP`</summary>

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
  "parentUuid": "47f503ec-cf14-4586-9d9a-cb03ae7ce7d1",
  "isSidechain": false,
  "promptId": "8052165b-6c36-40b2-ade0-6fd88ae7524b",
  "type": "user",
  "uuid": "9760f35e-c935-42d7-82fa-11fc3ab771c6",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "47f503ec-cf14-4586-9d9a-cb03ae7ce7d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-17T09:18:47.360Z_

Now let me search for all three papers the reviewer flagged, plus do broader landscape searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9760f35e-c935-42d7-82fa-11fc3ab771c6",
  "isSidechain": false,
  "requestId": "req_011Cb7tfqBSLbdK6En21puQM",
  "type": "assistant",
  "uuid": "f1228dca-6526-4c83-b85d-fba36922ae1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3FtVF7sy8Q1tZmfJSqDkX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 24792,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 266,
          "cache_read_input_tokens": 24792,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1319
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

_source line 13 · 2026-05-17T09:18:48.318Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016VtuBeB9KPAMixXyFdBH8H`</summary>

```json
{
  "query": "RetMask arXiv 2601.11020 retrieval head masking contrastive training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1228dca-6526-4c83-b85d-fba36922ae1f",
  "isSidechain": false,
  "requestId": "req_011Cb7tfqBSLbdK6En21puQM",
  "type": "assistant",
  "uuid": "ed1403ce-46da-4c45-b64c-01a964dc0887",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3FtVF7sy8Q1tZmfJSqDkX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 24792,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 266,
          "cache_read_input_tokens": 24792,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1319
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

_source line 14 · 2026-05-17T09:18:49.322Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VfryoDdkrpek7SQQuaGhPE`</summary>

```json
{
  "query": "\"Retrieval Heads are Dynamic\" arXiv 2602.11162 attention heads"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed1403ce-46da-4c45-b64c-01a964dc0887",
  "isSidechain": false,
  "requestId": "req_011Cb7tfqBSLbdK6En21puQM",
  "type": "assistant",
  "uuid": "b9bc2028-51e3-412b-a2af-23d0712badee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3FtVF7sy8Q1tZmfJSqDkX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 24792,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 266,
          "cache_read_input_tokens": 24792,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1319
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

_source line 15 · 2026-05-17T09:18:50.262Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RQFTtaDnTjwWH2Ek1wqorx`</summary>

```json
{
  "query": "Causal Head Gating CHG arXiv 2505.13737 NeurIPS 2025 per-head gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9bc2028-51e3-412b-a2af-23d0712badee",
  "isSidechain": false,
  "requestId": "req_011Cb7tfqBSLbdK6En21puQM",
  "type": "assistant",
  "uuid": "3dd9d936-ea0c-4ebc-95f4-0e587ac186c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3FtVF7sy8Q1tZmfJSqDkX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 24792,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 266,
          "cache_read_input_tokens": 24792,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1319
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

_source line 16 · 2026-05-17T09:18:50.831Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FEaPR3dBQz6d1caVozKrFc`</summary>

```json
{
  "query": "entrainment heads attention mechanism distraction LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dd9d936-ea0c-4ebc-95f4-0e587ac186c0",
  "isSidechain": false,
  "requestId": "req_011Cb7tfqBSLbdK6En21puQM",
  "type": "assistant",
  "uuid": "a7052983-4291-4733-a109-75c2af198d7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3FtVF7sy8Q1tZmfJSqDkX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 24792,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 266,
          "cache_read_input_tokens": 24792,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1319
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

_source line 17 · 2026-05-17T09:18:55.108Z_

<details><summary>↩ Tool result · `toolu_016VtuBeB9KPAMixXyFdBH8H`</summary>

```text
Web search results for query: "RetMask arXiv 2601.11020 retrieval head masking contrastive training"

Links: [{"title":"[2601.11020] From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models","url":"https://arxiv.org/abs/2601.11020"},{"title":"From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models","url":"https://arxiv.org/html/2601.11020"},{"title":"Optimizing Retrieval Heads for Long-Context Language ...","url":"https://www.arxiv.org/pdf/2601.11020"},{"title":"LLM2IR: simple unsupervised contrastive learning makes ...","url":"https://arxiv.org/pdf/2601.05262"},{"title":"Masked Contrastive Reconstruction for Cross-modal Medical Image-Report Retrieval","url":"https://arxiv.org/html/2312.15840v2"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=1179&show=2000"},{"title":"synclipmae: contrastive masked pretrain","url":"https://arxiv.org/pdf/2510.10069"},{"title":"Semantic Noise Reduction via Teacher-Guided Dual-Path Audio-Visual Representation Learning","url":"https://arxiv.org/html/2604.08147v1"},{"title":"Efficient Vision-Language Pre-training by Cluster Masking","url":"https://arxiv.org/html/2405.08815v1"},{"title":"Machine Learning Jun 2024","url":"https://web3.arxiv.org/list/cs.LG/2024-06?skip=1900&show=2000"}]

Based on the search results, I found relevant information about RetMask from arXiv paper 2601.11020. Here's what the paper presents:

## RetMask Overview

RetMask is a method that generates training signals by contrasting normal model outputs with those from an ablated variant in which the retrieval heads are masked.

## Paper Details and Results

The full title of the paper is "From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models." The work builds on advances in mechanistic interpretability that have identified special attention heads, known as retrieval heads, that are responsible for retrieving information from the context.

RetMask achieves substantial improvements: +2.28 points on HELMET at 128K for Llama-3.1, with +70% gains on generation with citation and +32% on passage re-ranking, while preserving performance on general tasks.

## Key Characteristics

RetMask is described as a simple and effective method for improving long-context processing that leverages retrieval heads as a source of contrastive training signals, requiring neither human-crafted criteria nor an LLM judge.

Experiments across four models in three families demonstrate that RetMask consistently improves long-context performance, where gains correlate with the sparsity of the retrieval score distribution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed1403ce-46da-4c45-b64c-01a964dc0887",
  "isSidechain": false,
  "promptId": "8052165b-6c36-40b2-ade0-6fd88ae7524b",
  "type": "user",
  "uuid": "543abd4f-d6bf-4571-b419-d2423280e1bf",
  "toolUseResult": {
    "query": "RetMask arXiv 2601.11020 retrieval head masking contrastive training",
    "results": [
      {
        "tool_use_id": "srvtoolu_014ud2oX3DxJ3RB9ATwF9p9B",
        "content": [
          {
            "title": "[2601.11020] From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models",
            "url": "https://arxiv.org/abs/2601.11020"
          },
          {
            "title": "From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models",
            "url": "https://arxiv.org/html/2601.11020"
          },
          {
            "title": "Optimizing Retrieval Heads for Long-Context Language ...",
            "url": "https://www.arxiv.org/pdf/2601.11020"
          },
          {
            "title": "LLM2IR: simple unsupervised contrastive learning makes ...",
            "url": "https://arxiv.org/pdf/2601.05262"
          },
          {
            "title": "Masked Contrastive Reconstruction for Cross-modal Medical Image-Report Retrieval",
            "url": "https://arxiv.org/html/2312.15840v2"
          },
          {
            "title": "Computer Science",
            "url": "https://arxiv.org/list/cs/pastweek?skip=1179&show=2000"
          },
          {
            "title": "synclipmae: contrastive masked pretrain",
            "url": "https://arxiv.org/pdf/2510.10069"
          },
          {
            "title": "Semantic Noise Reduction via Teacher-Guided Dual-Path Audio-Visual Representation Learning",
            "url": "https://arxiv.org/html/2604.08147v1"
          },
          {
            "title": "Efficient Vision-Language Pre-training by Cluster Masking",
            "url": "https://arxiv.org/html/2405.08815v1"
          },
          {
            "title": "Machine Learning Jun 2024",
            "url": "https://web3.arxiv.org/list/cs.LG/2024-06?skip=1900&show=2000"
          }
        ]
      },
      "Based on the search results, I found relevant information about RetMask from arXiv paper 2601.11020. Here's what the paper presents:\n\n## RetMask Overview\n\nRetMask is a method that generates training signals by contrasting normal model outputs with those from an ablated variant in which the retrieval heads are masked.\n\n## Paper Details and Results\n\nThe full title of the paper is \"From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models.\" The work builds on advances in mechanistic interpretability that have identified special attention heads, known as retrieval heads, that are responsible for retrieving information from the context.\n\nRetMask achieves substantial improvements: +2.28 points on HELMET at 128K for Llama-3.1, with +70% gains on generation with citation and +32% on passage re-ranking, while preserving performance on general tasks.\n\n## Key Characteristics\n\nRetMask is described as a simple and effective method for improving long-context processing that leverages retrieval heads as a source of contrastive training signals, requiring neither human-crafted criteria nor an LLM judge.\n\nExperiments across four models in three families demonstrate that RetMask consistently improves long-context performance, where gains correlate with the sparsity of the retrieval score distribution."
    ],
    "durationSeconds": 6.784929357000001
  },
  "sourceToolAssistantUUID": "ed1403ce-46da-4c45-b64c-01a964dc0887",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T09:18:55.328Z_

<details><summary>↩ Tool result · `toolu_01VfryoDdkrpek7SQQuaGhPE`</summary>

```text
Web search results for query: ""Retrieval Heads are Dynamic" arXiv 2602.11162 attention heads"

Links: [{"title":"[2602.11162] Retrieval Heads are Dynamic","url":"https://arxiv.org/abs/2602.11162"},{"title":"Retrieval Heads are Dynamic","url":"https://arxiv.org/html/2602.11162"},{"title":"Towards Dynamic Dense Retrieval with Routing Strategy","url":"https://arxiv.org/html/2602.22547"},{"title":"vera: Identifying and Leveraging Visual Evidence Retrieval Heads in Long-Context Understanding","url":"https://arxiv.org/html/2602.10146v1"},{"title":"Retrieval Head Mechanistically Explains Long-Context Factuality | OpenReview","url":"https://openreview.net/forum?id=EytBpUGB1Z"},{"title":"Hybrid Memory Architecture with Dynamic Retrieval ...","url":"https://x.com/_reachsumit/status/2023634745737740617"},{"title":"DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads","url":"https://arxiv.org/html/2410.10819v1"},{"title":"Published as a conference paper at ICLR 2025 RETRIEVAL HEAD MECHANISTICALLY","url":"https://openreview.net/pdf?id=EytBpUGB1Z"},{"title":"Retrieval Head Mechanistically Explains Long-Context Factuality","url":"https://arxiv.org/html/2404.15574v1"},{"title":"[2602.22547] Towards Dynamic Dense Retrieval with Routing Strategy","url":"https://arxiv.org/abs/2602.22547"}]

Based on the search results, here's what I found about the paper "Retrieval Heads are Dynamic" (arXiv 2602.11162):

## Overview

The paper investigates "retrieval heads" in Large Language Models (LLMs) responsible for extracting information from input contexts. However, prior works largely rely on static statistics aggregated across datasets, overlooking the fine-grained temporal dynamics of autoregressive generation.

## Core Claims

The paper establishes three main findings:

1. **Dynamism**: Retrieval heads vary dynamically across timesteps.

2. **Irreplaceability**: Dynamic retrieval heads are specific at each timestep and cannot be effectively replaced by static retrieval heads.

3. **Correlation**: The model's hidden state encodes a predictive signal for future retrieval head patterns, indicating an internal planning mechanism.

## Validation

The findings are validated on the Needle-in-a-Haystack task and a multi-hop QA task, with quantification of the differences between dynamic and static retrieval heads in a Dynamic Retrieval-Augmented Generation framework.

The paper was submitted on January 7, 2026, and provides new insights into the internal mechanisms of how LLMs process and retrieve information during text generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9bc2028-51e3-412b-a2af-23d0712badee",
  "isSidechain": false,
  "promptId": "8052165b-6c36-40b2-ade0-6fd88ae7524b",
  "type": "user",
  "uuid": "67e7a28a-653f-47aa-b1bd-609dab0504e9",
  "toolUseResult": {
    "query": "\"Retrieval Heads are Dynamic\" arXiv 2602.11162 attention heads",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EUJGojJUMpXLPU2faUXeXV",
        "content": [
          {
            "title": "[2602.11162] Retrieval Heads are Dynamic",
            "url": "https://arxiv.org/abs/2602.11162"
          },
          {
            "title": "Retrieval Heads are Dynamic",
            "url": "https://arxiv.org/html/2602.11162"
          },
          {
            "title": "Towards Dynamic Dense Retrieval with Routing Strategy",
            "url": "https://arxiv.org/html/2602.22547"
          },
          {
            "title": "vera: Identifying and Leveraging Visual Evidence Retrieval Heads in Long-Context Understanding",
            "url": "https://arxiv.org/html/2602.10146v1"
          },
          {
            "title": "Retrieval Head Mechanistically Explains Long-Context Factuality | OpenReview",
            "url": "https://openreview.net/forum?id=EytBpUGB1Z"
          },
          {
            "title": "Hybrid Memory Architecture with Dynamic Retrieval ...",
            "url": "https://x.com/_reachsumit/status/2023634745737740617"
          },
          {
            "title": "DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads",
            "url": "https://arxiv.org/html/2410.10819v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 RETRIEVAL HEAD MECHANISTICALLY",
            "url": "https://openreview.net/pdf?id=EytBpUGB1Z"
          },
          {
            "title": "Retrieval Head Mechanistically Explains Long-Context Factuality",
            "url": "https://arxiv.org/html/2404.15574v1"
          },
          {
            "title": "[2602.22547] Towards Dynamic Dense Retrieval with Routing Strategy",
            "url": "https://arxiv.org/abs/2602.22547"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper \"Retrieval Heads are Dynamic\" (arXiv 2602.11162):\n\n## Overview\n\nThe paper investigates \"retrieval heads\" in Large Language Models (LLMs) responsible for extracting information from input contexts. However, prior works largely rely on static statistics aggregated across datasets, overlooking the fine-grained temporal dynamics of autoregressive generation.\n\n## Core Claims\n\nThe paper establishes three main findings:\n\n1. **Dynamism**: Retrieval heads vary dynamically across timesteps.\n\n2. **Irreplaceability**: Dynamic retrieval heads are specific at each timestep and cannot be effectively replaced by static retrieval heads.\n\n3. **Correlation**: The model's hidden state encodes a predictive signal for future retrieval head patterns, indicating an internal planning mechanism.\n\n## Validation\n\nThe findings are validated on the Needle-in-a-Haystack task and a multi-hop QA task, with quantification of the differences between dynamic and static retrieval heads in a Dynamic Retrieval-Augmented Generation framework.\n\nThe paper was submitted on January 7, 2026, and provides new insights into the internal mechanisms of how LLMs process and retrieve information during text generation."
    ],
    "durationSeconds": 6.003183101000002
  },
  "sourceToolAssistantUUID": "b9bc2028-51e3-412b-a2af-23d0712badee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-17T09:18:57.476Z_

<details><summary>↩ Tool result · `toolu_01RQFTtaDnTjwWH2Ek1wqorx`</summary>

```text
Web search results for query: "Causal Head Gating CHG arXiv 2505.13737 NeurIPS 2025 per-head gating"

Links: [{"title":"[2505.13737] Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers","url":"https://arxiv.org/abs/2505.13737"},{"title":"Causal Head Gating: A Framework for Interpreting Roles of ...","url":"https://arxiv.org/pdf/2505.13737"},{"title":"Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers","url":"https://arxiv.org/html/2505.13737"},{"title":"(PDF) Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers","url":"https://www.researchgate.net/publication/391910662_Causal_Head_Gating_A_Framework_for_Interpreting_Roles_of_Attention_Heads_in_Transformers"},{"title":"NeurIPS Poster Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers","url":"https://neurips.cc/virtual/2025/poster/116358"},{"title":"Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers | OpenReview","url":"https://openreview.net/forum?id=kgmyjyDFrx"},{"title":"[Literature Review] Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers","url":"https://www.themoonlight.io/en/review/causal-head-gating-a-framework-for-interpreting-roles-of-attention-heads-in-transformers"},{"title":"Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.13737v1"},{"title":"Artificial Intelligence May 2025","url":"https://arxiv.org/list/cs.AI/2025-05?skip=425&show=500"},{"title":"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free | OpenReview","url":"https://openreview.net/forum?id=1b7whO4SfY"}]

I found the paper! Here's what I found about Causal Head Gating (CHG):

## Overview

Causal Head Gating (CHG) is a scalable method for interpreting the functional roles of attention heads in transformer models. CHG learns soft gates over heads and assigns them a causal taxonomy—facilitating, interfering, or irrelevant—based on their impact on task performance.

## Key Features

CHG works by fitting a set of gating values for each attention head that applies a soft ablation to its output using next-token prediction, so that task-facilitating heads remain unaltered while any task-interfering heads are suppressed.

## Advantages Over Previous Approaches

Unlike prior approaches in mechanistic interpretability, which are hypothesis-driven and require prompt templates or target labels, CHG applies directly to any dataset using standard next-token prediction. Additionally, CHG is highly scalable: it introduces only one learnable parameter per attention head and requires no updates to the underlying model weights, so that the CHG parameters can be fitted in minutes using gradient-based optimization, even for LLMs with billions of parameters.

## Evaluation and Results

The work evaluates CHG across multiple large language models (LLMs) in the Llama 3 model family and diverse tasks, including syntax, commonsense, and mathematical reasoning, and shows that CHG scores yield causal, not merely correlational, insight validated via ablation and causal mediation analyses.

## Conference Acceptance

The paper was accepted to the 39th Conference on Neural Information Processing Systems (NeurIPS 2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dd9d936-ea0c-4ebc-95f4-0e587ac186c0",
  "isSidechain": false,
  "promptId": "8052165b-6c36-40b2-ade0-6fd88ae7524b",
  "type": "user",
  "uuid": "24dd575b-8f9b-4ebd-991f-dc319e1a5d53",
  "toolUseResult": {
    "query": "Causal Head Gating CHG arXiv 2505.13737 NeurIPS 2025 per-head gating",
    "results": [
      {
        "tool_use_id": "srvtoolu_01K4qCVKnkkNnfj9N2EtukoQ",
        "content": [
          {
            "title": "[2505.13737] Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers",
            "url": "https://arxiv.org/abs/2505.13737"
          },
          {
            "title": "Causal Head Gating: A Framework for Interpreting Roles of ...",
            "url": "https://arxiv.org/pdf/2505.13737"
          },
          {
            "title": "Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers",
            "url": "https://arxiv.org/html/2505.13737"
          },
          {
            "title": "(PDF) Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers",
            "url": "https://www.researchgate.net/publication/391910662_Causal_Head_Gating_A_Framework_for_Interpreting_Roles_of_Attention_Heads_in_Transformers"
          },
          {
            "title": "NeurIPS Poster Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers",
            "url": "https://neurips.cc/virtual/2025/poster/116358"
          },
          {
            "title": "Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers | OpenReview",
            "url": "https://openreview.net/forum?id=kgmyjyDFrx"
          },
          {
            "title": "[Literature Review] Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers",
            "url": "https://www.themoonlight.io/en/review/causal-head-gating-a-framework-for-interpreting-roles-of-attention-heads-in-transformers"
          },
          {
            "title": "Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2505.13737v1"
          },
          {
            "title": "Artificial Intelligence May 2025",
            "url": "https://arxiv.org/list/cs.AI/2025-05?skip=425&show=500"
          },
          {
            "title": "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free | OpenReview",
            "url": "https://openreview.net/forum?id=1b7whO4SfY"
          }
        ]
      },
      "I found the paper! Here's what I found about Causal Head Gating (CHG):\n\n## Overview\n\nCausal Head Gating (CHG) is a scalable method for interpreting the functional roles of attention heads in transformer models. CHG learns soft gates over heads and assigns them a causal taxonomy—facilitating, interfering, or irrelevant—based on their impact on task performance.\n\n## Key Features\n\nCHG works by fitting a set of gating values for each attention head that applies a soft ablation to its output using next-token prediction, so that task-facilitating heads remain unaltered while any task-interfering heads are suppressed.\n\n## Advantages Over Previous Approaches\n\nUnlike prior approaches in mechanistic interpretability, which are hypothesis-driven and require prompt templates or target labels, CHG applies directly to any dataset using standard next-token prediction. Additionally, CHG is highly scalable: it introduces only one learnable parameter per attention head and requires no updates to the underlying model weights, so that the CHG parameters can be fitted in minutes using gradient-based optimization, even for LLMs with billions of parameters.\n\n## Evaluation and Results\n\nThe work evaluates CHG across multiple large language models (LLMs) in the Llama 3 model family and diverse tasks, including syntax, commonsense, and mathematical reasoning, and shows that CHG scores yield causal, not merely correlational, insight validated via ablation and causal mediation analyses.\n\n## Conference Acceptance\n\nThe paper was accepted to the 39th Conference on Neural Information Processing Systems (NeurIPS 2025)."
    ],
    "durationSeconds": 7.210365836000001
  },
  "sourceToolAssistantUUID": "3dd9d936-ea0c-4ebc-95f4-0e587ac186c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-17 (UTC).**  ## Original idea {   \"title\": \"Entrainment-Aware Gated Fine-Tuning: Query-Conditional Head Gates for…",
  "leafUuid": "24dd575b-8f9b-4ebd-991f-dc319e1a5d53",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise EAGT with RetMask, dynamic heads, and query-conditional ablation",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e"
}
```

---

### Tool result

_source line 22 · 2026-05-17T09:18:57.927Z_

<details><summary>↩ Tool result · `toolu_01FEaPR3dBQz6d1caVozKrFc`</summary>

```text
Web search results for query: "entrainment heads attention mechanism distraction LLM 2025 2026"

Links: [{"title":"A Mechanistic Perspective on Contextual Entrainment and ...","url":"https://aclanthology.org/2025.acl-long.791.pdf"},{"title":"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.791/"},{"title":"Attention Tracker: Detecting Prompt Injection Attacks in LLMs","url":"https://aclanthology.org/2025.findings-naacl.123.pdf"},{"title":"Attention Mechanism in LLMs Explained (2026)","url":"https://www.buildfastwithai.com/blogs/attention-mechanism-llm-explained"},{"title":"Published as a conference paper at COLM 2025","url":"https://arxiv.org/pdf/2504.02732"},{"title":"Writing an LLM from scratch, part 13 -- the 'why' of attention, or: attention heads are dumb :: Giles' blog","url":"https://www.gilesthomas.com/2025/05/llm-from-scratch-13-taking-stock-part-1-attention-heads-are-dumb"},{"title":"Attention heads of large language models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11873009/"},{"title":"Attention heads of large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666389925000248"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=Gg1aPETCL6"},{"title":"[2507.19595] Efficient Attention Mechanisms for Large Language Models: A Survey","url":"https://arxiv.org/abs/2507.19595"}]

Based on the search results, I found several relevant research papers and discussions on entrainment heads, attention mechanisms, and distraction in LLMs from 2025-2026:

## Key Finding: "Llama See, Llama Do" (ACL 2025)

The most directly relevant paper is "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs", published at ACL 2025 by Niu et al.

This research identifies "contextual entrainment" as a key mechanism for how LMs become distracted by "irrelevant" contextual information in the input prompt. The findings are significant: "A small set of attention heads (3.2% to 10.7%) can substantially increase the gap between" model performance. 

When these "entrainment heads" are turned off by setting their outputs to zero, the effect of contextual entrainment is significantly attenuated, causing the model to generate output that capitulates to what it would produce if no distracting context were provided.

## Related Research Areas

Beyond this specific finding, the search results show ongoing work in 2025-2026 on:
- Attention heads playing a pivotal role in reasoning and sharing similarities with human brain functions, with research exploring the roles and mechanisms of attention heads to help demystify internal reasoning processes of LLMs
- Using attention tracking to detect prompt injection attacks by monitoring the distraction effect in LLMs

The work on entrainment heads represents an important step toward understanding and potentially mitigating how LLMs are influenced by contextual information in their inputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7052983-4291-4733-a109-75c2af198d7f",
  "isSidechain": false,
  "promptId": "8052165b-6c36-40b2-ade0-6fd88ae7524b",
  "type": "user",
  "uuid": "77322cb6-e8df-407e-8cf2-40a67f3854b4",
  "toolUseResult": {
    "query": "entrainment heads attention mechanism distraction LLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RMYx5hLb21p8M4Tf6s822v",
        "content": [
          {
            "title": "A Mechanistic Perspective on Contextual Entrainment and ...",
            "url": "https://aclanthology.org/2025.acl-long.791.pdf"
          },
          {
            "title": "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.791/"
          },
          {
            "title": "Attention Tracker: Detecting Prompt Injection Attacks in LLMs",
            "url": "https://aclanthology.org/2025.findings-naacl.123.pdf"
          },
          {
            "title": "Attention Mechanism in LLMs Explained (2026)",
            "url": "https://www.buildfastwithai.com/blogs/attention-mechanism-llm-explained"
          },
          {
            "title": "Published as a conference paper at COLM 2025",
            "url": "https://arxiv.org/pdf/2504.02732"
          },
          {
            "title": "Writing an LLM from scratch, part 13 -- the 'why' of attention, or: attention heads are dumb :: Giles' blog",
            "url": "https://www.gilesthomas.com/2025/05/llm-from-scratch-13-taking-stock-part-1-attention-heads-are-dumb"
          },
          {
            "title": "Attention heads of large language models - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11873009/"
          },
          {
            "title": "Attention heads of large language models - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S2666389925000248"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf?id=Gg1aPETCL6"
          },
          {
            "title": "[2507.19595] Efficient Attention Mechanisms for Large Language Models: A Survey",
            "url": "https://arxiv.org/abs/2507.19595"
          }
        ]
      },
      "Based on the search results, I found several relevant research papers and discussions on entrainment heads, attention mechanisms, and distraction in LLMs from 2025-2026:\n\n## Key Finding: \"Llama See, Llama Do\" (ACL 2025)\n\nThe most directly relevant paper is \"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs\", published at ACL 2025 by Niu et al.\n\nThis research identifies \"contextual entrainment\" as a key mechanism for how LMs become distracted by \"irrelevant\" contextual information in the input prompt. The findings are significant: \"A small set of attention heads (3.2% to 10.7%) can substantially increase the gap between\" model performance. \n\nWhen these \"entrainment heads\" are turned off by setting their outputs to zero, the effect of contextual entrainment is significantly attenuated, causing the model to generate output that capitulates to what it would produce if no distracting context were provided.\n\n## Related Research Areas\n\nBeyond this specific finding, the search results show ongoing work in 2025-2026 on:\n- Attention heads playing a pivotal role in reasoning and sharing similarities with human brain functions, with research exploring the roles and mechanisms of attention heads to help demystify internal reasoning processes of LLMs\n- Using attention tracking to detect prompt injection attacks by monitoring the distraction effect in LLMs\n\nThe work on entrainment heads represents an important step toward understanding and potentially mitigating how LLMs are influenced by contextual information in their inputs."
    ],
    "durationSeconds": 7.093237191
  },
  "sourceToolAssistantUUID": "a7052983-4291-4733-a109-75c2af198d7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-17T09:19:00.779Z_

Good, found all three papers. Now let me read them in detail, plus search for additional related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77322cb6-e8df-407e-8cf2-40a67f3854b4",
  "isSidechain": false,
  "requestId": "req_011Cb7tgumnmNGRuWc5vD8iQ",
  "type": "assistant",
  "uuid": "861a972d-4c00-4589-9b67-26cfa4d10cb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMFafiqUvDRYZ5moYukiWv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3736,
      "cache_read_input_tokens": 26111,
      "output_tokens": 419,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 419,
          "cache_read_input_tokens": 26111,
          "cache_creation_input_tokens": 3736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3736
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

_source line 24 · 2026-05-17T09:19:03.675Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014xUfzfkduJw7VCx62MvDCD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.11020",
  "prompt": "Extract the full abstract, method description, key results (especially HELMET scores), and how RetMask uses retrieval heads for training. What is the training approach (SFT, DPO, contrastive)? What models were tested? How are retrieval heads identified?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "861a972d-4c00-4589-9b67-26cfa4d10cb6",
  "isSidechain": false,
  "requestId": "req_011Cb7tgumnmNGRuWc5vD8iQ",
  "type": "assistant",
  "uuid": "3522f155-c4f9-461f-98da-cf1587be91a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMFafiqUvDRYZ5moYukiWv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3736,
      "cache_read_input_tokens": 26111,
      "output_tokens": 419,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 419,
          "cache_read_input_tokens": 26111,
          "cache_creation_input_tokens": 3736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3736
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

_source line 25 · 2026-05-17T09:19:06.078Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014591VBn6UsmpRoaEfAw1sg`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.11162",
  "prompt": "Extract the full abstract, key findings about dynamic vs static retrieval heads, the overlap statistics (what percentage of dynamic heads overlap with static top-k heads), and how the paper defines and identifies dynamic retrieval heads. What are the implications for methods that target statically-identified heads?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3522f155-c4f9-461f-98da-cf1587be91a3",
  "isSidechain": false,
  "requestId": "req_011Cb7tgumnmNGRuWc5vD8iQ",
  "type": "assistant",
  "uuid": "53cc4c0b-8fce-4afb-94d7-a8aa21377430",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMFafiqUvDRYZ5moYukiWv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3736,
      "cache_read_input_tokens": 26111,
      "output_tokens": 419,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 419,
          "cache_read_input_tokens": 26111,
          "cache_creation_input_tokens": 3736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3736
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

_source line 26 · 2026-05-17T09:19:08.072Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01V3VyLhbcFZnKuMg7z82Nc8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.13737",
  "prompt": "Extract the full abstract, method details for CHG (how gating values are learned, loss function, initialization), key results, and how CHG categorizes heads (facilitating, interfering, irrelevant). How many parameters are added? What is the training cost? How does it compare to ablation-based methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53cc4c0b-8fce-4afb-94d7-a8aa21377430",
  "isSidechain": false,
  "requestId": "req_011Cb7tgumnmNGRuWc5vD8iQ",
  "type": "assistant",
  "uuid": "02d21dee-b033-451a-b78d-541798e4a320",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMFafiqUvDRYZ5moYukiWv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3736,
      "cache_read_input_tokens": 26111,
      "output_tokens": 419,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 419,
          "cache_read_input_tokens": 26111,
          "cache_creation_input_tokens": 3736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3736
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

_source line 27 · 2026-05-17T09:19:08.680Z_

<details><summary>↩ Tool result · `toolu_014xUfzfkduJw7VCx62MvDCD`</summary>

```text
# RetMask: Optimizing Retrieval Heads for Long-Context LLMs

## Abstract Summary
The research explores how "retrieval heads" (specialized attention mechanisms identified through mechanistic interpretability) can enhance long-context capabilities in large language models. The authors propose RetMask to improve performance on context-dependent tasks.

## Method: RetMask Training Approach
RetMask uses a **contrastive learning mechanism**. The system generates training signals by "contrasting normal model outputs with those from an ablated variant in which the retrieval heads are masked." This mechanism-based approach directly leverages mechanistic insights about model internals.

## Key Results
- **HELMET benchmark (128K context, Llama-3.1)**: +2.28 points improvement
- **Generation with citation**: +70% gains
- **Passage re-ranking**: +32% improvement
- General task performance was preserved

## Models Tested
The paper evaluated "four models in three families," demonstrating consistent improvements across different architectures.

## Retrieval Head Identification
The abstract doesn't explicitly detail identification methods, but it notes that gains "correlate with the sparsity of the retrieval score distribution." Models with concentrated retrieval capabilities in fewer heads showed stronger improvements, while less sparse models showed modest gains.

## Training Paradigm
The approach appears **contrastive** rather than standard SFT or DPO, using ablation-based signals to optimize head function during training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3522f155-c4f9-461f-98da-cf1587be91a3",
  "isSidechain": false,
  "promptId": "8052165b-6c36-40b2-ade0-6fd88ae7524b",
  "type": "user",
  "uuid": "9beac394-6850-4a06-ab26-47983984d9fd",
  "toolUseResult": {
    "bytes": 46933,
    "code": 200,
    "codeText": "OK",
    "result": "# RetMask: Optimizing Retrieval Heads for Long-Context LLMs\n\n## Abstract Summary\nThe research explores how \"retrieval heads\" (specialized attention mechanisms identified through mechanistic interpretability) can enhance long-context capabilities in large language models. The authors propose RetMask to improve performance on context-dependent tasks.\n\n## Method: RetMask Training Approach\nRetMask uses a **contrastive learning mechanism**. The system generates training signals by \"contrasting normal model outputs with those from an ablated variant in which the retrieval heads are masked.\" This mechanism-based approach directly leverages mechanistic insights about model internals.\n\n## Key Results\n- **HELMET benchmark (128K context, Llama-3.1)**: +2.28 points improvement\n- **Generation with citation**: +70% gains\n- **Passage re-ranking**: +32% improvement\n- General task performance was preserved\n\n## Models Tested\nThe paper evaluated \"four models in three families,\" demonstrating consistent improvements across different architectures.\n\n## Retrieval Head Identification\nThe abstract doesn't explicitly detail identification methods, but it notes that gains \"correlate with the sparsity of the retrieval score distribution.\" Models with concentrated retrieval capabilities in fewer heads showed stronger improvements, while less sparse models showed modest gains.\n\n## Training Paradigm\nThe approach appears **contrastive** rather than standard SFT or DPO, using ablation-based signals to optimize head function during training.",
    "durationMs": 5001,
    "url": "https://arxiv.org/abs/2601.11020"
  },
  "sourceToolAssistantUUID": "3522f155-c4f9-461f-98da-cf1587be91a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T09:19:11.514Z_

<details><summary>↩ Tool result · `toolu_014591VBn6UsmpRoaEfAw1sg`</summary>

```text
# Analysis of "Retrieval Heads are Dynamic"

## Full Abstract
"Recent studies have identified 'retrieval heads' in Large Language Models (LLMs) responsible for extracting information from input contexts. However, prior works largely rely on static statistics aggregated across datasets, identifying heads that perform retrieval on average. This perspective overlooks the fine-grained temporal dynamics of autoregressive generation. In this paper, we investigate retrieval heads from a dynamic perspective. Through extensive analysis, we establish three core claims: (1) Dynamism: Retrieval heads vary dynamically across timesteps; (2) Irreplaceability: Dynamic retrieval heads are specific at each timestep and cannot be effectively replaced by static retrieval heads; and (3) Correlation: The model's hidden state encodes a predictive signal for future retrieval head patterns, indicating an internal planning mechanism."

## Key Findings

**Three Core Claims:**
1. **Dynamism**: Retrieval heads change across different timesteps during generation
2. **Irreplaceability**: Static heads cannot effectively substitute for dynamic ones at specific timesteps
3. **Correlation**: Hidden states predict future retrieval patterns, suggesting internal planning

## Overlap Statistics & Methodology

The webpage provided does not contain quantitative overlap statistics between dynamic and static heads. The document indicates validation occurred on "Needle-in-a-Haystack task and a multi-hop QA task" with utility differences measured in a "Dynamic Retrieval-Augmented Generation framework," but specific percentages are absent from this content.

## Implications for Static Head Methods

Methods targeting statically-identified heads face a fundamental limitation: they miss the temporal specificity of retrieval behavior. The paper's finding that dynamic heads cannot be effectively replaced by static counterparts suggests existing approaches may systematically underutilize model capabilities during generation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53cc4c0b-8fce-4afb-94d7-a8aa21377430",
  "isSidechain": false,
  "promptId": "8052165b-6c36-40b2-ade0-6fd88ae7524b",
  "type": "user",
  "uuid": "9a15fb96-b358-4552-8875-545aa59c4580",
  "toolUseResult": {
    "bytes": 46468,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of \"Retrieval Heads are Dynamic\"\n\n## Full Abstract\n\"Recent studies have identified 'retrieval heads' in Large Language Models (LLMs) responsible for extracting information from input contexts. However, prior works largely rely on static statistics aggregated across datasets, identifying heads that perform retrieval on average. This perspective overlooks the fine-grained temporal dynamics of autoregressive generation. In this paper, we investigate retrieval heads from a dynamic perspective. Through extensive analysis, we establish three core claims: (1) Dynamism: Retrieval heads vary dynamically across timesteps; (2) Irreplaceability: Dynamic retrieval heads are specific at each timestep and cannot be effectively replaced by static retrieval heads; and (3) Correlation: The model's hidden state encodes a predictive signal for future retrieval head patterns, indicating an internal planning mechanism.\"\n\n## Key Findings\n\n**Three Core Claims:**\n1. **Dynamism**: Retrieval heads change across different timesteps during generation\n2. **Irreplaceability**: Static heads cannot effectively substitute for dynamic ones at specific timesteps\n3. **Correlation**: Hidden states predict future retrieval patterns, suggesting internal planning\n\n## Overlap Statistics & Methodology\n\nThe webpage provided does not contain quantitative overlap statistics between dynamic and static heads. The document indicates validation occurred on \"Needle-in-a-Haystack task and a multi-hop QA task\" with utility differences measured in a \"Dynamic Retrieval-Augmented Generation framework,\" but specific percentages are absent from this content.\n\n## Implications for Static Head Methods\n\nMethods targeting statically-identified heads face a fundamental limitation: they miss the temporal specificity of retrieval behavior. The paper's finding that dynamic heads cannot be effectively replaced by static counterparts suggests existing approaches may systematically underutilize model capabilities during generation.",
    "durationMs": 5433,
    "url": "https://arxiv.org/abs/2602.11162"
  },
  "sourceToolAssistantUUID": "53cc4c0b-8fce-4afb-94d7-a8aa21377430",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-17T09:19:13.348Z_

<details><summary>↩ Tool result · `toolu_01V3VyLhbcFZnKuMg7z82Nc8`</summary>

```text
# Causal Head Gating: Analysis Based on Available Information

## Abstract
The paper introduces "a scalable method for interpreting the functional roles of attention heads in transformer models" that "learns soft gates over heads and assigns them a causal taxonomy."

## Key Limitations
The webpage content provided contains only the abstract and metadata from arXiv. Unfortunately, **the full method details you requested are not included** in this excerpt. Specifically, missing are:

- **How gating values are learned** (mathematical formulation)
- **Loss function specifications**
- **Initialization procedures**
- **Number of parameters added**
- **Training computational costs**
- **Detailed comparisons with ablation-based methods**

## Available Information

**Head Categorization:** The framework assigns heads to three categories: "facilitating, interfering, or irrelevant" based on their impact on task performance.

**Key Finding:** The abstract mentions "multiple sparse task-sufficient sub-circuits" and notes that "individual head roles depend on interactions with others (low modularity)."

**Validation:** The authors claim their "CHG scores yield causal, not merely correlational, insight validated via ablation and causal mediation analyses."

## Recommendation
To access the complete methodological details, parameter counts, and comparative analyses you're seeking, you would need to review the full PDF or HTML version of the paper (linked on the arXiv page).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02d21dee-b033-451a-b78d-541798e4a320",
  "isSidechain": false,
  "promptId": "8052165b-6c36-40b2-ade0-6fd88ae7524b",
  "type": "user",
  "uuid": "932b66fd-38a4-4013-bd9e-71cfbbdbd65d",
  "toolUseResult": {
    "bytes": 46733,
    "code": 200,
    "codeText": "OK",
    "result": "# Causal Head Gating: Analysis Based on Available Information\n\n## Abstract\nThe paper introduces \"a scalable method for interpreting the functional roles of attention heads in transformer models\" that \"learns soft gates over heads and assigns them a causal taxonomy.\"\n\n## Key Limitations\nThe webpage content provided contains only the abstract and metadata from arXiv. Unfortunately, **the full method details you requested are not included** in this excerpt. Specifically, missing are:\n\n- **How gating values are learned** (mathematical formulation)\n- **Loss function specifications**\n- **Initialization procedures**\n- **Number of parameters added**\n- **Training computational costs**\n- **Detailed comparisons with ablation-based methods**\n\n## Available Information\n\n**Head Categorization:** The framework assigns heads to three categories: \"facilitating, interfering, or irrelevant\" based on their impact on task performance.\n\n**Key Finding:** The abstract mentions \"multiple sparse task-sufficient sub-circuits\" and notes that \"individual head roles depend on interactions with others (low modularity).\"\n\n**Validation:** The authors claim their \"CHG scores yield causal, not merely correlational, insight validated via ablation and causal mediation analyses.\"\n\n## Recommendation\nTo access the complete methodological details, parameter counts, and comparative analyses you're seeking, you would need to review the full PDF or HTML version of the paper (linked on the arXiv page).",
    "durationMs": 5273,
    "url": "https://arxiv.org/abs/2505.13737"
  },
  "sourceToolAssistantUUID": "02d21dee-b033-451a-b78d-541798e4a320",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-17T09:19:13.356Z_

```json
{
  "parentUuid": "932b66fd-38a4-4013-bd9e-71cfbbdbd65d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "dd97582f-e172-4a6b-9424-585997c7e857",
  "timestamp": "2026-05-17T09:19:13.356Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-17T09:19:16.351Z_

Let me get more details on the papers — especially the overlap statistics from the dynamic heads paper and the CHG method details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd97582f-e172-4a6b-9424-585997c7e857",
  "isSidechain": false,
  "requestId": "req_011Cb7ti3nXUcjSdiocGdzny",
  "type": "assistant",
  "uuid": "4fdd7ac1-755b-44c2-84a0-31148c6f3f81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXcgYZaBkePviGhab8KWdx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1641,
      "cache_read_input_tokens": 29847,
      "output_tokens": 471,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 471,
          "cache_read_input_tokens": 29847,
          "cache_creation_input_tokens": 1641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1641
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

_source line 32 · 2026-05-17T09:19:19.683Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QAbTsDGtwwPwTRueDyM1Ys`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.11162",
  "prompt": "Find the specific overlap statistics between dynamic and static retrieval heads. The reviewer mentioned \"only 18-46% of dynamically-active retrieval heads overlap with statically-identified top-20 heads.\" Find these exact numbers. Also extract any methodology for how dynamic heads are identified per timestep, and any discussion of implications for head-targeting methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fdd7ac1-755b-44c2-84a0-31148c6f3f81",
  "isSidechain": false,
  "requestId": "req_011Cb7ti3nXUcjSdiocGdzny",
  "type": "assistant",
  "uuid": "b0703e90-ef7c-4929-ae50-7394049a86ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXcgYZaBkePviGhab8KWdx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1641,
      "cache_read_input_tokens": 29847,
      "output_tokens": 471,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 471,
          "cache_read_input_tokens": 29847,
          "cache_creation_input_tokens": 1641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1641
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

_source line 33 · 2026-05-17T09:19:22.608Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UHwfJhKdgREjTNjzpkcK4N`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.13737",
  "prompt": "Extract the full method details for CHG: How are gating values learned? What is the loss function? How many parameters per head (one scalar per head)? What is the initialization? How does it handle task-specific vs general gating? What are the key results comparing CHG-gated models vs full models vs ablated models? How does it compare to static ablation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0703e90-ef7c-4929-ae50-7394049a86ed",
  "isSidechain": false,
  "requestId": "req_011Cb7ti3nXUcjSdiocGdzny",
  "type": "assistant",
  "uuid": "8a84d5d8-f029-4e14-8db4-06a0a96b3550",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXcgYZaBkePviGhab8KWdx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1641,
      "cache_read_input_tokens": 29847,
      "output_tokens": 471,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 471,
          "cache_read_input_tokens": 29847,
          "cache_creation_input_tokens": 1641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1641
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

_source line 34 · 2026-05-17T09:19:25.038Z_

<details><summary>↩ Tool result · `toolu_01QAbTsDGtwwPwTRueDyM1Ys`</summary>

```text
# Overlap Statistics and Dynamic Head Identification

## Overlap Statistics

The paper reports Jaccard similarity between dynamic and static retrieval heads in Table 1:

- **llama3.1-8b**: 0.3512 (35.12% overlap)
- **llama3.2-3b**: 0.3126 (31.26% overlap)
- **qwen3-8b**: 0.4611 (46.11% overlap)
- **llama2-13b**: 0.2077 (20.77% overlap)
- **phi4-mini**: 0.1845 (18.45% overlap)

These values align with the 18-46% range mentioned in your reference.

## Dynamic Head Identification Methodology

Per-timestep identification uses this definition: "an attention head is considered to be performing a retrieval operation if and only if two conditions are satisfied: (1) at the current inference step, the generated token is identical to the token receiving the highest attention weight from that head, and (2) the token with the highest attention weight lies within the 'needle' context."

For reasoning tasks, the paper proposes measuring "the proportion of attention it allocates to all supporting facts (the 'needles') relative to the total attention it distributes across the entire effective context."

## Implications

The low overlap suggests static head identification "risks oversimplifying the model's real-time behavior, as heads that are statistically dominant may not be active at every critical timestep, while 'less significant' heads might play irreplaceable roles in specific contexts."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0703e90-ef7c-4929-ae50-7394049a86ed",
  "isSidechain": false,
  "promptId": "8052165b-6c36-40b2-ade0-6fd88ae7524b",
  "type": "user",
  "uuid": "2dfc1b4f-39bc-4104-9a50-44e43431133d",
  "toolUseResult": {
    "bytes": 254818,
    "code": 200,
    "codeText": "OK",
    "result": "# Overlap Statistics and Dynamic Head Identification\n\n## Overlap Statistics\n\nThe paper reports Jaccard similarity between dynamic and static retrieval heads in Table 1:\n\n- **llama3.1-8b**: 0.3512 (35.12% overlap)\n- **llama3.2-3b**: 0.3126 (31.26% overlap)\n- **qwen3-8b**: 0.4611 (46.11% overlap)\n- **llama2-13b**: 0.2077 (20.77% overlap)\n- **phi4-mini**: 0.1845 (18.45% overlap)\n\nThese values align with the 18-46% range mentioned in your reference.\n\n## Dynamic Head Identification Methodology\n\nPer-timestep identification uses this definition: \"an attention head is considered to be performing a retrieval operation if and only if two conditions are satisfied: (1) at the current inference step, the generated token is identical to the token receiving the highest attention weight from that head, and (2) the token with the highest attention weight lies within the 'needle' context.\"\n\nFor reasoning tasks, the paper proposes measuring \"the proportion of attention it allocates to all supporting facts (the 'needles') relative to the total attention it distributes across the entire effective context.\"\n\n## Implications\n\nThe low overlap suggests static head identification \"risks oversimplifying the model's real-time behavior, as heads that are statistically dominant may not be active at every critical timestep, while 'less significant' heads might play irreplaceable roles in specific contexts.\"",
    "durationMs": 5351,
    "url": "https://arxiv.org/html/2602.11162"
  },
  "sourceToolAssistantUUID": "b0703e90-ef7c-4929-ae50-7394049a86ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T09:19:25.351Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RHzCMvp2hpjoopx4mzYP9g`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.11020",
  "prompt": "Extract the full method for RetMask: How exactly are retrieval heads identified? What is the training procedure — is it SFT, DPO, or both? How are contrastive signals generated from masked vs unmasked outputs? What models and context lengths were tested? What are the detailed results on HELMET subtasks? How many parameters are modified (full model or subset)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dfc1b4f-39bc-4104-9a50-44e43431133d",
  "isSidechain": false,
  "requestId": "req_011Cb7ti3nXUcjSdiocGdzny",
  "type": "assistant",
  "uuid": "16d78559-c4f5-4a13-b5a3-c0b8e45c4d96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXcgYZaBkePviGhab8KWdx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1641,
      "cache_read_input_tokens": 29847,
      "output_tokens": 471,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 471,
          "cache_read_input_tokens": 29847,
          "cache_creation_input_tokens": 1641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1641
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-17 (UTC).**  ## Original idea {   \"title\": \"Entrainment-Aware Gated Fine-Tuning: Query-Conditional Head Gates for…",
  "leafUuid": "16d78559-c4f5-4a13-b5a3-c0b8e45c4d96",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise EAGT with RetMask, dynamic heads, and query-conditional ablation",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e"
}
```

---

### Tool result

_source line 38 · 2026-05-17T09:19:34.183Z_

<details><summary>↩ Tool result · `toolu_01RHzCMvp2hpjoopx4mzYP9g`</summary>

```text
# RetMask Method: Complete Overview

## Retrieval Head Identification

Retrieval heads are identified using the Needle-In-A-Haystack (NIAH) task. During decoding, a head is marked as retrieving when it attends to a token matching the generated output. The retrieval score is calculated as: "RetrievalScore(h)=1|𝒯|∑(gh,k)∈𝒯|gh∩k|/|k|" where gh represents tokens retrieved by head h and k is the needle sequence. Heads exceeding threshold τ are classified as retrieval heads (τ=0.1 for Llama-3.1, τ=0.05 for Qwen3/Olmo-3).

## Training Procedure

The approach uses **Direct Preference Optimization (DPO)** exclusively—not supervised fine-tuning. The training process involves three stages:

1. **Retrieval Head Deactivation**: Zeroing columns in attention output projection matrices for identified retrieval heads
2. **Contrastive Response Generation**: Sampling responses from both the original model and ablated variant
3. **DPO Training**: Using these pairs as preference signals

## Contrastive Signal Generation

For each instruction, two responses are generated:
- **Preferred (yw)**: "y_w ∼ π_θ(·|x)" from the unmodified model
- **Rejected (yl)**: "y_l ∼ π_θ'(·|x)" from the retrieval-head-masked variant

The DPO objective contrasts these responses: "ℒ(π_θ)=−𝔼[log σ(β log π_θ(y_w|x)/π_ref(y_w|x) − β log π_θ(y_l|x)/π_ref(y_l|x))]"

## Models and Context Lengths Tested

Four models across three families:
- Llama-3.1-8B-Instruct
- Qwen3-8B
- OLMo-3-7B-Instruct and OLMo-3-7B-Think

Context lengths: 8K, 16K, 32K, 64K, and 128K tokens

## HELMET Subtask Results (Llama-3.1 at 128K)

Key improvements from baseline:
- Generation with Citation: "3.09 to 5.25" (70% relative gain)
- Passage Re-ranking: "13.73 to 18.16" (32% relative gain)
- Overall average: 46.40 → 48.68 points

Other tasks showed modest changes, with some improvements on general reasoning tasks.

## Parameter Modification Scope

Only attention head parameters are modified. "RetMask masks only 4–10% of attention heads" across tested models, making it a targeted, efficient intervention rather than full-model retraining.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16d78559-c4f5-4a13-b5a3-c0b8e45c4d96",
  "isSidechain": false,
  "promptId": "8052165b-6c36-40b2-ade0-6fd88ae7524b",
  "type": "user",
  "uuid": "70a2fc1c-ef87-4f30-8fde-2bc8fd7ca4a6",
  "toolUseResult": {
    "bytes": 330008,
    "code": 200,
    "codeText": "OK",
    "result": "# RetMask Method: Complete Overview\n\n## Retrieval Head Identification\n\nRetrieval heads are identified using the Needle-In-A-Haystack (NIAH) task. During decoding, a head is marked as retrieving when it attends to a token matching the generated output. The retrieval score is calculated as: \"RetrievalScore(h)=1|𝒯|∑(gh,k)∈𝒯|gh∩k|/|k|\" where gh represents tokens retrieved by head h and k is the needle sequence. Heads exceeding threshold τ are classified as retrieval heads (τ=0.1 for Llama-3.1, τ=0.05 for Qwen3/Olmo-3).\n\n## Training Procedure\n\nThe approach uses **Direct Preference Optimization (DPO)** exclusively—not supervised fine-tuning. The training process involves three stages:\n\n1. **Retrieval Head Deactivation**: Zeroing columns in attention output projection matrices for identified retrieval heads\n2. **Contrastive Response Generation**: Sampling responses from both the original model and ablated variant\n3. **DPO Training**: Using these pairs as preference signals\n\n## Contrastive Signal Generation\n\nFor each instruction, two responses are generated:\n- **Preferred (yw)**: \"y_w ∼ π_θ(·|x)\" from the unmodified model\n- **Rejected (yl)**: \"y_l ∼ π_θ'(·|x)\" from the retrieval-head-masked variant\n\nThe DPO objective contrasts these responses: \"ℒ(π_θ)=−𝔼[log σ(β log π_θ(y_w|x)/π_ref(y_w|x) − β log π_θ(y_l|x)/π_ref(y_l|x))]\"\n\n## Models and Context Lengths Tested\n\nFour models across three families:\n- Llama-3.1-8B-Instruct\n- Qwen3-8B\n- OLMo-3-7B-Instruct and OLMo-3-7B-Think\n\nContext lengths: 8K, 16K, 32K, 64K, and 128K tokens\n\n## HELMET Subtask Results (Llama-3.1 at 128K)\n\nKey improvements from baseline:\n- Generation with Citation: \"3.09 to 5.25\" (70% relative gain)\n- Passage Re-ranking: \"13.73 to 18.16\" (32% relative gain)\n- Overall average: 46.40 → 48.68 points\n\nOther tasks showed modest changes, with some improvements on general reasoning tasks.\n\n## Parameter Modification Scope\n\nOnly attention head parameters are modified. \"RetMask masks only 4–10% of attention heads\" across tested models, making it a targeted, efficient intervention rather than full-model retraining.",
    "durationMs": 8830,
    "url": "https://arxiv.org/html/2601.11020"
  },
  "sourceToolAssistantUUID": "16d78559-c4f5-4a13-b5a3-c0b8e45c4d96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-17T09:19:36.268Z_

<details><summary>↩ Tool result · `toolu_01UHwfJhKdgREjTNjzpkcK4N`</summary>

````text
# Causal Head Gating (CHG) Method Details

## Learning Gating Values

CHG learns soft multiplicative gates applied to attention head outputs. The gating matrix G ∈ [0,1]^(L×H) scales each head's output before the output projection. The approach involves three optimization phases:

1. **Initial fit (λ=0)**: 500 gradient updates establishing a shared initialization
2. **Retention variant (G⁺, λ>0)**: 500 updates encouraging gates toward 1
3. **Removal variant (G⁻, λ<0)**: 500 updates encouraging gates toward 0

## Loss Function

The combined objective is:

```
L(G) = -Σ log P(y|x; M_θ, G) - λ Σ σ⁻¹(G_l,h)
```

Where the first term is standard next-token prediction NLL, and the regularization term uses clipped inverse-sigmoid to nudge irrelevant heads toward extreme values while leaving task-relevant ones relatively stable.

## Parameters Per Head

Exactly **one scalar parameter per attention head** (L×H total parameters), making the approach extremely lightweight and scalable to billion-parameter models.

## Initialization

Gates initialize with uniform random values between 0 and 1, then the λ=0 fit establishes shared starting points for subsequent G⁺ and G⁻ optimizations.

## Task-Specific vs General Gating

CHG fits separate gate matrices for each model-dataset pair independently. The paper reports evaluation across multiple tasks (math, syntax, commonsense) showing substantial task-dependent variation in which heads matter.

## Key Comparative Results

**Performance under ablation**: As shown in Figure 2, sequentially ablating heads in order of facilitation scores degrades performance (negative log-probability changes), while ablating interference scores improves it, validating the causal taxonomy.

**Consistency across models**: "Minimum correlation of 94.92% and an average of 99.2%" across model pair comparisons for head scores, demonstrating robust cross-model alignment.

**Distribution patterns**: Mathematical reasoning activates 52.6% facilitating heads versus only 39% irrelevant; syntax/commonsense show 63-64% irrelevant heads with sparse facilitating subsets.

## Static Ablation Comparison

The paper validates CHG predictions through targeted ablations showing predicted performance patterns align with actual measured effects, confirming causal (not merely correlational) insight into head contributions.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "8a84d5d8-f029-4e14-8db4-06a0a96b3550",
  "isSidechain": false,
  "promptId": "8052165b-6c36-40b2-ade0-6fd88ae7524b",
  "type": "user",
  "uuid": "9a2c9268-8fe1-44ff-b5d6-3cdaa5c1ec71",
  "toolUseResult": {
    "bytes": 215987,
    "code": 200,
    "codeText": "OK",
    "result": "# Causal Head Gating (CHG) Method Details\n\n## Learning Gating Values\n\nCHG learns soft multiplicative gates applied to attention head outputs. The gating matrix G ∈ [0,1]^(L×H) scales each head's output before the output projection. The approach involves three optimization phases:\n\n1. **Initial fit (λ=0)**: 500 gradient updates establishing a shared initialization\n2. **Retention variant (G⁺, λ>0)**: 500 updates encouraging gates toward 1\n3. **Removal variant (G⁻, λ<0)**: 500 updates encouraging gates toward 0\n\n## Loss Function\n\nThe combined objective is:\n\n```\nL(G) = -Σ log P(y|x; M_θ, G) - λ Σ σ⁻¹(G_l,h)\n```\n\nWhere the first term is standard next-token prediction NLL, and the regularization term uses clipped inverse-sigmoid to nudge irrelevant heads toward extreme values while leaving task-relevant ones relatively stable.\n\n## Parameters Per Head\n\nExactly **one scalar parameter per attention head** (L×H total parameters), making the approach extremely lightweight and scalable to billion-parameter models.\n\n## Initialization\n\nGates initialize with uniform random values between 0 and 1, then the λ=0 fit establishes shared starting points for subsequent G⁺ and G⁻ optimizations.\n\n## Task-Specific vs General Gating\n\nCHG fits separate gate matrices for each model-dataset pair independently. The paper reports evaluation across multiple tasks (math, syntax, commonsense) showing substantial task-dependent variation in which heads matter.\n\n## Key Comparative Results\n\n**Performance under ablation**: As shown in Figure 2, sequentially ablating heads in order of facilitation scores degrades performance (negative log-probability changes), while ablating interference scores improves it, validating the causal taxonomy.\n\n**Consistency across models**: \"Minimum correlation of 94.92% and an average of 99.2%\" across model pair comparisons for head scores, demonstrating robust cross-model alignment.\n\n**Distribution patterns**: Mathematical reasoning activates 52.6% facilitating heads versus only 39% irrelevant; syntax/commonsense show 63-64% irrelevant heads with sparse facilitating subsets.\n\n## Static Ablation Comparison\n\nThe paper validates CHG predictions through targeted ablations showing predicted performance patterns align with actual measured effects, confirming causal (not merely correlational) insight into head contributions.",
    "durationMs": 13658,
    "url": "https://arxiv.org/html/2505.13737"
  },
  "sourceToolAssistantUUID": "8a84d5d8-f029-4e14-8db4-06a0a96b3550",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Assistant

_source line 40 · 2026-05-17T09:19:40.756Z_

Excellent — now I have detailed information on all three papers. Let me do a few more searches to check for any additional concurrent work and to verify the venue deadlines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a2c9268-8fe1-44ff-b5d6-3cdaa5c1ec71",
  "isSidechain": false,
  "requestId": "req_011Cb7tjjmN1jtBtM1o31bdi",
  "type": "assistant",
  "uuid": "ca94c486-ea8f-407e-8c6c-3836f63638b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LpaaGtnwjAGjwJH56sQRSc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 731,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 31488,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1464,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 731,
          "output_tokens": 209,
          "cache_read_input_tokens": 31488,
          "cache_creation_input_tokens": 1464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1464
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

_source line 41 · 2026-05-17T09:19:41.703Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012NbDmNMAe2EfLsYhUAUJHx`</summary>

```json
{
  "query": "EACL 2027 ARR deadline submission date August 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca94c486-ea8f-407e-8c6c-3836f63638b9",
  "isSidechain": false,
  "requestId": "req_011Cb7tjjmN1jtBtM1o31bdi",
  "type": "assistant",
  "uuid": "f09eed3d-1a78-49fb-b581-4d36f87c4ae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LpaaGtnwjAGjwJH56sQRSc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 731,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 31488,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1464,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 731,
          "output_tokens": 209,
          "cache_read_input_tokens": 31488,
          "cache_creation_input_tokens": 1464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1464
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

_source line 42 · 2026-05-17T09:19:42.180Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Ldgq6r6z11uJEBR4HiFqd`</summary>

```json
{
  "query": "mechanistic interpretability attention head gating fine-tuning distraction robustness 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f09eed3d-1a78-49fb-b581-4d36f87c4ae0",
  "isSidechain": false,
  "requestId": "req_011Cb7tjjmN1jtBtM1o31bdi",
  "type": "assistant",
  "uuid": "b87a5b52-180f-4047-bd64-03cd95d7371b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LpaaGtnwjAGjwJH56sQRSc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 731,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 31488,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1464,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 731,
          "output_tokens": 209,
          "cache_read_input_tokens": 31488,
          "cache_creation_input_tokens": 1464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1464
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

_source line 43 · 2026-05-17T09:19:42.990Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M3K4u8MSwxHmYYZCEHGt1G`</summary>

```json
{
  "query": "entrainment heads vs retrieval heads stability causal identification differentiable masking"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b87a5b52-180f-4047-bd64-03cd95d7371b",
  "isSidechain": false,
  "requestId": "req_011Cb7tjjmN1jtBtM1o31bdi",
  "type": "assistant",
  "uuid": "4179e828-54ae-45b4-a998-ddd25f384341",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LpaaGtnwjAGjwJH56sQRSc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 731,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 31488,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1464,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 731,
          "output_tokens": 209,
          "cache_read_input_tokens": 31488,
          "cache_creation_input_tokens": 1464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1464
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

_source line 44 · 2026-05-17T09:19:46.851Z_

<details><summary>↩ Tool result · `toolu_012NbDmNMAe2EfLsYhUAUJHx`</summary>

```text
Web search results for query: "EACL 2027 ARR deadline submission date August 2026"

Links: [{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"eaclmeeting on X: \"📢⚠️ IMPORTANT DATE CORRECTION: the ARR deadline for EACL 2027 is Aug 3, 2026 (not Aug 6 as previously announced). EACL is earlier than usual in '27, so this is the only viable ARR cycle! 📚 All areas of CL/NLP + related fields welcome. Full CfP coming soon. #NLProc #EACL2027\" / X","url":"https://x.com/eaclmeeting/status/2051971432171688436"},{"title":"EACL 2027 Call for Main Conference Papers","url":"https://2027.eacl.org/calls/papers/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Where's Dan: Conference and Grant Deadlines","url":"https://web.stanford.edu/~jurafsky/deadlines.html"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"EACL: Conference of the European Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=785"}]

Based on the search results, I found the information you requested:

The ARR submission deadline for EACL 2027 (long & short papers) is August 3, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

It's worth noting that this is an important date correction, as the ARR deadline for EACL 2027 is Aug 3, 2026 (not Aug 6 as previously announced). EACL is earlier than usual in '27, so this is the only viable ARR cycle.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f09eed3d-1a78-49fb-b581-4d36f87c4ae0",
  "isSidechain": false,
  "promptId": "8052165b-6c36-40b2-ade0-6fd88ae7524b",
  "type": "user",
  "uuid": "68a6ff38-add0-4b3d-9b95-0a4ee03f8db7",
  "toolUseResult": {
    "query": "EACL 2027 ARR deadline submission date August 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UiQxZ9JEYNmghFfpznQ7iR",
        "content": [
          {
            "title": "The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -",
            "url": "https://2027.eacl.org/"
          },
          {
            "title": "Dates and Venues",
            "url": "http://aclrollingreview.org/dates"
          },
          {
            "title": "eaclmeeting on X: \"📢⚠️ IMPORTANT DATE CORRECTION: the ARR deadline for EACL 2027 is Aug 3, 2026 (not Aug 6 as previously announced). EACL is earlier than usual in '27, so this is the only viable ARR cycle! 📚 All areas of CL/NLP + related fields welcome. Full CfP coming soon. #NLProc #EACL2027\" / X",
            "url": "https://x.com/eaclmeeting/status/2051971432171688436"
          },
          {
            "title": "EACL 2027 Call for Main Conference Papers",
            "url": "https://2027.eacl.org/calls/papers/"
          },
          {
            "title": "aclrollingreview/dates.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/dates.md"
          },
          {
            "title": "Call for Main Conference Papers -",
            "url": "https://2026.eacl.org/calls/papers/"
          },
          {
            "title": "AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "Where's Dan: Conference and Grant Deadlines",
            "url": "https://web.stanford.edu/~jurafsky/deadlines.html"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "EACL: Conference of the European Chapter of the Association for Computational Linguistics 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=785"
          }
        ]
      },
      "Based on the search results, I found the information you requested:\n\nThe ARR submission deadline for EACL 2027 (long & short papers) is August 3, 2026. All deadlines are 11:59PM UTC-12:00 (\"anywhere on Earth\").\n\nIt's worth noting that this is an important date correction, as the ARR deadline for EACL 2027 is Aug 3, 2026 (not Aug 6 as previously announced). EACL is earlier than usual in '27, so this is the only viable ARR cycle."
    ],
    "durationSeconds": 5.143187425000011
  },
  "sourceToolAssistantUUID": "f09eed3d-1a78-49fb-b581-4d36f87c4ae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-17T09:19:51.646Z_

<details><summary>↩ Tool result · `toolu_013Ldgq6r6z11uJEBR4HiFqd`</summary>

```text
Web search results for query: "mechanistic interpretability attention head gating fine-tuning distraction robustness 2026"

Links: [{"title":"[2503.18762] Mechanistic Interpretability of Fine-Tuned Vision Transformers on Distorted Images: Decoding Attention Head Behavior for Transparent and Trustworthy AI","url":"https://arxiv.org/abs/2503.18762"},{"title":"Unboxing the Black Box: Mechanistic Interpretability for Algorithmic Understanding of Neural Networks","url":"https://arxiv.org/html/2511.19265v1"},{"title":"Sparse Attention Post-Training for Mechanistic Interpretability","url":"https://arxiv.org/html/2512.05865v1"},{"title":"(PDF) Mechanistic Interpretability of Fine-Tuned Vision Transformers on Distorted Images: Decoding Attention Head Behavior for Transparent and Trustworthy AI","url":"https://www.researchgate.net/publication/390142791_Mechanistic_Interpretability_of_Fine-Tuned_Vision_Transformers_on_Distorted_Images_Decoding_Attention_Head_Behavior_for_Transparent_and_Trustworthy_AI"},{"title":"Counting Circuits: Mechanistic Interpretability of Visual Reasoning in Large Vision-Language Models","url":"https://arxiv.org/html/2603.18523v1"},{"title":"Attention and Gating Injection in Neural Networks","url":"https://www.emergentmind.com/topics/attention-and-gating-based-injection"},{"title":"Understanding Mechanistic Interpretability in AI Models | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"},{"title":"Causal Head Gating: A Framework for Interpreting Roles of ...","url":"https://arxiv.org/pdf/2505.13737"},{"title":"Remarkable Robustness of LLMs: Stages of Inference? | OpenReview","url":"https://openreview.net/forum?id=Wxh5Xz7NpJ"},{"title":"2026-01-09 Interpreting Transformers Through Attention Head Intervention","url":"https://www.arxiv.org/pdf/2601.04398"}]

I've found several highly relevant research results for your search query. Here's what the recent literature shows:

## Key Findings

**Vision Transformer Fine-Tuning Study**: A recent study examined individual attention heads in vision transformers (ViTs) fine-tuned on distorted 2D spectrogram images containing non-relevant content (axis labels, titles, color bars). Heads in early layers (1 to 3) showed minimal task impact with ablation increasing MSE loss slightly (μ=0.11%, σ=0.09%), while deeper heads (e.g., layer 6) caused a threefold higher loss increase (μ=0.34%, σ=0.02%), demonstrating greater task importance.

**Attention Head Gating Framework**: A framework called Causal Head Gating (CHG) has been developed for mechanistic interpretability. CHG is a flexible and scalable method for identifying causally relevant attention heads in large language models that assigns each head a graded score for facilitation, interference, or irrelevance based on its effect on task performance.

**Robustness and Layer Sensitivity**: Large language models retain 72–95% of their original top-1 prediction accuracy when undergoing structural interventions without any fine-tuning, with performance degradation not being uniform across layers—models are remarkably robust to dropping middle layers.

**Gating Mechanisms for Interpretability**: Concept-driven gate heads can be trained with weak supervision, enabling efficient knowledge transfer and model debugging without substantial architecture change.

**Attention Head Intervention**: Attention head intervention achieves causal understanding by actively manipulating individual attention heads to establish which ones causally drive behavior, unlike other interpretability methods that observe correlations.

These results highlight the intersection of mechanistic interpretability, attention head analysis, fine-tuning, and model robustness—key themes in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b87a5b52-180f-4047-bd64-03cd95d7371b",
  "isSidechain": false,
  "promptId": "8052165b-6c36-40b2-ade0-6fd88ae7524b",
  "type": "user",
  "uuid": "39c8db2e-d541-4aa3-815a-04765f13e705",
  "toolUseResult": {
    "query": "mechanistic interpretability attention head gating fine-tuning distraction robustness 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ag1SajUiazX12dtQ5SnnTj",
        "content": [
          {
            "title": "[2503.18762] Mechanistic Interpretability of Fine-Tuned Vision Transformers on Distorted Images: Decoding Attention Head Behavior for Transparent and Trustworthy AI",
            "url": "https://arxiv.org/abs/2503.18762"
          },
          {
            "title": "Unboxing the Black Box: Mechanistic Interpretability for Algorithmic Understanding of Neural Networks",
            "url": "https://arxiv.org/html/2511.19265v1"
          },
          {
            "title": "Sparse Attention Post-Training for Mechanistic Interpretability",
            "url": "https://arxiv.org/html/2512.05865v1"
          },
          {
            "title": "(PDF) Mechanistic Interpretability of Fine-Tuned Vision Transformers on Distorted Images: Decoding Attention Head Behavior for Transparent and Trustworthy AI",
            "url": "https://www.researchgate.net/publication/390142791_Mechanistic_Interpretability_of_Fine-Tuned_Vision_Transformers_on_Distorted_Images_Decoding_Attention_Head_Behavior_for_Transparent_and_Trustworthy_AI"
          },
          {
            "title": "Counting Circuits: Mechanistic Interpretability of Visual Reasoning in Large Vision-Language Models",
            "url": "https://arxiv.org/html/2603.18523v1"
          },
          {
            "title": "Attention and Gating Injection in Neural Networks",
            "url": "https://www.emergentmind.com/topics/attention-and-gating-based-injection"
          },
          {
            "title": "Understanding Mechanistic Interpretability in AI Models | IntuitionLabs",
            "url": "https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"
          },
          {
            "title": "Causal Head Gating: A Framework for Interpreting Roles of ...",
            "url": "https://arxiv.org/pdf/2505.13737"
          },
          {
            "title": "Remarkable Robustness of LLMs: Stages of Inference? | OpenReview",
            "url": "https://openreview.net/forum?id=Wxh5Xz7NpJ"
          },
          {
            "title": "2026-01-09 Interpreting Transformers Through Attention Head Intervention",
            "url": "https://www.arxiv.org/pdf/2601.04398"
          }
        ]
      },
      "I've found several highly relevant research results for your search query. Here's what the recent literature shows:\n\n## Key Findings\n\n**Vision Transformer Fine-Tuning Study**: A recent study examined individual attention heads in vision transformers (ViTs) fine-tuned on distorted 2D spectrogram images containing non-relevant content (axis labels, titles, color bars). Heads in early layers (1 to 3) showed minimal task impact with ablation increasing MSE loss slightly (μ=0.11%, σ=0.09%), while deeper heads (e.g., layer 6) caused a threefold higher loss increase (μ=0.34%, σ=0.02%), demonstrating greater task importance.\n\n**Attention Head Gating Framework**: A framework called Causal Head Gating (CHG) has been developed for mechanistic interpretability. CHG is a flexible and scalable method for identifying causally relevant attention heads in large language models that assigns each head a graded score for facilitation, interference, or irrelevance based on its effect on task performance.\n\n**Robustness and Layer Sensitivity**: Large language models retain 72–95% of their original top-1 prediction accuracy when undergoing structural interventions without any fine-tuning, with performance degradation not being uniform across layers—models are remarkably robust to dropping middle layers.\n\n**Gating Mechanisms for Interpretability**: Concept-driven gate heads can be trained with weak supervision, enabling efficient knowledge transfer and model debugging without substantial architecture change.\n\n**Attention Head Intervention**: Attention head intervention achieves causal understanding by actively manipulating individual attention heads to establish which ones causally drive behavior, unlike other interpretability methods that observe correlations.\n\nThese results highlight the intersection of mechanistic interpretability, attention head analysis, fine-tuning, and model robustness—key themes in your query."
    ],
    "durationSeconds": 9.461533167
  },
  "sourceToolAssistantUUID": "b87a5b52-180f-4047-bd64-03cd95d7371b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-17T09:19:54.092Z_

<details><summary>↩ Tool result · `toolu_01M3K4u8MSwxHmYYZCEHGt1G`</summary>

```text
Web search results for query: "entrainment heads vs retrieval heads stability causal identification differentiable masking"

Links: [{"title":"Retrieval Head Mechanistically Explains Long-Context Factuality | OpenReview","url":"https://openreview.net/forum?id=EytBpUGB1Z"},{"title":"Causal Masking in Neural Models","url":"https://www.emergentmind.com/topics/causal-masking"},{"title":"Preference Heads in Large Language Models: A Mechanistic Framework for Interpretable Personalization","url":"https://arxiv.org/html/2604.22345"},{"title":"Retrieval Head Mechanistically Explains Long-Context Factuality [Quick Review]","url":"https://liner.com/review/retrieval-head-mechanistically-explains-longcontext-factuality"},{"title":"Module 12: Attention — Tiny🔥Torch","url":"https://mlsysbook.ai/tinytorch/modules/12_attention_ABOUT.html"},{"title":"Unpacking Attention in Transformers: From Self-Attention to Causal Self-Attention | by Tejaswi kashyap | Medium","url":"https://medium.com/@tejaswi_kashyap/unpacking-attention-in-transformers-from-self-attention-to-causal-self-attention-21fa6824acd8"},{"title":"Masked multi-head self-attention for causal speech enhancement - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0167639320302806"},{"title":"Understanding and Coding Self-Attention, Multi-Head Attention, Causal-Attention, and Cross-Attention in LLMs","url":"https://magazine.sebastianraschka.com/p/understanding-and-coding-self-attention"},{"title":"Adaptive Cross-Attention Masking","url":"https://www.emergentmind.com/topics/adaptive-cross-attention-masking"},{"title":"Decoder Architecture: Causal Masking & Autoregressive Generation - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/decoder-architecture-causal-masking-autoregressive-transformers"}]

Based on the web search results, I found relevant information about retrieval heads and their relationship to stability, causal identification, and differentiable masking. Here are the key findings:

## Retrieval Heads and Causal Identification

Retrieval heads are a special type of attention heads that are largely responsible for retrieving information in transformer-based models. Completely pruning retrieval heads leads to failure in retrieving relevant information and results in hallucination, while pruning random non-retrieval heads does not affect the model's retrieval ability.

## Causal Analysis Through Masking

The research employs differentiable masking to causally isolate the function of these heads. This comparison causally isolates the function of retrieval heads, showing that their specific attention patterns are essential for this task, unlike other attention heads. Specifically, masking out retrieval heads severely degrades performance across all tested models, demonstrating their causal role in information retrieval, with masking the top 20 retrieval heads in LLaMA 2 7B drastically reducing accuracy to 63.6%.

## Entrainment vs. Retrieval Heads

While the search results don't specifically distinguish between "entrainment heads" and "retrieval heads," the research indicates that retrieval heads are sparse, with only less than 5% of attention heads being retrieval.

## Differentiable Masking

Differentiable (soft) masking enables gradient propagation, supporting weak supervision and self-coherent mask refinement in the absence of full supervision. This approach allows researchers to measure causal effects while maintaining differentiability through the model.

The broader context shows that masking-based causal analysis is a key methodology for understanding how specific attention heads contribute to model behavior.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4179e828-54ae-45b4-a998-ddd25f384341",
  "isSidechain": false,
  "promptId": "8052165b-6c36-40b2-ade0-6fd88ae7524b",
  "type": "user",
  "uuid": "6510591b-d850-4cf5-ac09-6bd54541cb05",
  "toolUseResult": {
    "query": "entrainment heads vs retrieval heads stability causal identification differentiable masking",
    "results": [
      {
        "tool_use_id": "srvtoolu_012fQ2XFBRbU5JHTjM2yfpbD",
        "content": [
          {
            "title": "Retrieval Head Mechanistically Explains Long-Context Factuality | OpenReview",
            "url": "https://openreview.net/forum?id=EytBpUGB1Z"
          },
          {
            "title": "Causal Masking in Neural Models",
            "url": "https://www.emergentmind.com/topics/causal-masking"
          },
          {
            "title": "Preference Heads in Large Language Models: A Mechanistic Framework for Interpretable Personalization",
            "url": "https://arxiv.org/html/2604.22345"
          },
          {
            "title": "Retrieval Head Mechanistically Explains Long-Context Factuality [Quick Review]",
            "url": "https://liner.com/review/retrieval-head-mechanistically-explains-longcontext-factuality"
          },
          {
            "title": "Module 12: Attention — Tiny🔥Torch",
            "url": "https://mlsysbook.ai/tinytorch/modules/12_attention_ABOUT.html"
          },
          {
            "title": "Unpacking Attention in Transformers: From Self-Attention to Causal Self-Attention | by Tejaswi kashyap | Medium",
            "url": "https://medium.com/@tejaswi_kashyap/unpacking-attention-in-transformers-from-self-attention-to-causal-self-attention-21fa6824acd8"
          },
          {
            "title": "Masked multi-head self-attention for causal speech enhancement - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0167639320302806"
          },
          {
            "title": "Understanding and Coding Self-Attention, Multi-Head Attention, Causal-Attention, and Cross-Attention in LLMs",
            "url": "https://magazine.sebastianraschka.com/p/understanding-and-coding-self-attention"
          },
          {
            "title": "Adaptive Cross-Attention Masking",
            "url": "https://www.emergentmind.com/topics/adaptive-cross-attention-masking"
          },
          {
            "title": "Decoder Architecture: Causal Masking & Autoregressive Generation - Interactive | Michael Brenndoerfer | Michael Brenndoerfer",
            "url": "https://mbrenndoerfer.com/writing/decoder-architecture-causal-masking-autoregressive-transformers"
          }
        ]
      },
      "Based on the web search results, I found relevant information about retrieval heads and their relationship to stability, causal identification, and differentiable masking. Here are the key findings:\n\n## Retrieval Heads and Causal Identification\n\nRetrieval heads are a special type of attention heads that are largely responsible for retrieving information in transformer-based models. Completely pruning retrieval heads leads to failure in retrieving relevant information and results in hallucination, while pruning random non-retrieval heads does not affect the model's retrieval ability.\n\n## Causal Analysis Through Masking\n\nThe research employs differentiable masking to causally isolate the function of these heads. This comparison causally isolates the function of retrieval heads, showing that their specific attention patterns are essential for this task, unlike other attention heads. Specifically, masking out retrieval heads severely degrades performance across all tested models, demonstrating their causal role in information retrieval, with masking the top 20 retrieval heads in LLaMA 2 7B drastically reducing accuracy to 63.6%.\n\n## Entrainment vs. Retrieval Heads\n\nWhile the search results don't specifically distinguish between \"entrainment heads\" and \"retrieval heads,\" the research indicates that retrieval heads are sparse, with only less than 5% of attention heads being retrieval.\n\n## Differentiable Masking\n\nDifferentiable (soft) masking enables gradient propagation, supporting weak supervision and self-coherent mask refinement in the absence of full supervision. This approach allows researchers to measure causal effects while maintaining differentiability through the model.\n\nThe broader context shows that masking-based causal analysis is a key methodology for understanding how specific attention heads contribute to model behavior."
    ],
    "durationSeconds": 11.099488017000011
  },
  "sourceToolAssistantUUID": "4179e828-54ae-45b4-a998-ddd25f384341",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-17 (UTC).**  ## Original idea {   \"title\": \"Entrainment-Aware Gated Fine-Tuning: Query-Conditional Head Gates for…",
  "leafUuid": "6510591b-d850-4cf5-ac09-6bd54541cb05",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise EAGT with RetMask, dynamic heads, and query-conditional ablation",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e"
}
```

---

### Assistant

_source line 49 · 2026-05-17T09:20:17.522Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also search for any recent work on combining mechanistic interpretability with gating for context robustness that might have appeared in 2026, and also check AAAI 2027 deadline to confirm.

Let me also think about the key differences between entrainment heads and retrieval heads, which is crucial for the "dynamic heads" argument.

Key insights so far:

1. **RetMask** (arXiv:2601.11020): Uses DPO training with contrastive signals from masking retrieval heads. It modifies the full model, not just heads. Key difference from EAGT: RetMask uses head masking to generate training data (behavioral modification via DPO), while EAGT adds permanent architectural gates (architectural modification). RetMask doesn't add query-conditional gates - it trains the full model.


2. **"Retrieval Heads are Dynamic"** (arXiv:2602.11162): Shows only 18-46% Jaccard similarity between dynamic and static heads across models, but this relies on heuristic attention pattern matching for identification. Entrainment heads use causal differentiable masking instead, which identifies heads based on their actual functional contribution to logit boosting rather than just attention patterns—a fundamentally stronger identification method.
3. **CHG** (arXiv:2505.13737): Learns a single scalar gate per head through NTP loss, though these gates remain static rather than query-conditional.

The key insight the reviewer raises is that the same entrainment head must suppress itself when context is irrelevant and activate when it's relevant—something a static gate simply cannot achieve. The dual-objective loss forces query-conditional behavior because no fixed gate value can simultaneously satisfy both the suppression and preservation objectives for the same head across different inputs. The gate has to learn to discriminate based on query features to resolve this tension.

Retrieval heads are fundamentally defined by behavioral patterns—whether they attend to tokens they're about to generate—which is inherently correlational and input-dependent. Entrainment heads, by contrast, are defined causally: whether masking that head actually reduces the model's ability to boost relevant logits.

This distinction is crucial because a head's functional role in the circuit is an architectural property, while which specific tokens it retrieves varies with the input. I'm identifying entrainment heads by their mechanistic function, not just their attention patterns.

Now I should search for any related work I might have overlooked.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6510591b-d850-4cf5-ac09-6bd54541cb05",
  "isSidechain": false,
  "requestId": "req_011Cb7tm3y2Hv3FT1zjiyPTh",
  "type": "assistant",
  "uuid": "47b55c7e-c9fe-4ab2-9303-71d16c0a170d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6m1BmRZaxNbeJr2G6eyiJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3661,
      "cache_read_input_tokens": 32952,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3661,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 32952,
          "cache_creation_input_tokens": 3661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3661
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

_source line 50 · 2026-05-17T09:20:17.524Z_

Let me search for a few more things to ensure comprehensive coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47b55c7e-c9fe-4ab2-9303-71d16c0a170d",
  "isSidechain": false,
  "requestId": "req_011Cb7tm3y2Hv3FT1zjiyPTh",
  "type": "assistant",
  "uuid": "d57d0e06-cc7f-452d-81cd-94a184216cce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6m1BmRZaxNbeJr2G6eyiJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3661,
      "cache_read_input_tokens": 32952,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3661,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 32952,
          "cache_creation_input_tokens": 3661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3661
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

_source line 51 · 2026-05-17T09:20:17.554Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hprh5NC1Kz4i8bBmi4gLDk`</summary>

```json
{
  "query": "AAAI 2027 deadline submission date July 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d57d0e06-cc7f-452d-81cd-94a184216cce",
  "isSidechain": false,
  "requestId": "req_011Cb7tm3y2Hv3FT1zjiyPTh",
  "type": "assistant",
  "uuid": "55a83c0b-d323-43f5-8eac-97398959b40f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6m1BmRZaxNbeJr2G6eyiJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3661,
      "cache_read_input_tokens": 32952,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3661,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 32952,
          "cache_creation_input_tokens": 3661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3661
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

_source line 52 · 2026-05-17T09:20:18.116Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RK8x8eyZfJjT9LCDBS59K1`</summary>

```json
{
  "query": "query-conditional head gating attention heads adaptive context 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55a83c0b-d323-43f5-8eac-97398959b40f",
  "isSidechain": false,
  "requestId": "req_011Cb7tm3y2Hv3FT1zjiyPTh",
  "type": "assistant",
  "uuid": "1eb0d544-15bf-4628-a354-fa43668f5d30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6m1BmRZaxNbeJr2G6eyiJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3661,
      "cache_read_input_tokens": 32952,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3661,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 32952,
          "cache_creation_input_tokens": 3661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3661
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

_source line 53 · 2026-05-17T09:20:21.208Z_

<details><summary>↩ Tool result · `toolu_01Hprh5NC1Kz4i8bBmi4gLDk`</summary>

```text
Web search results for query: "AAAI 2027 deadline submission date July 2026"

Links: [{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"AAAI 2027 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI Conference on Artificial Intelligence","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI 2027 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2027%2FConference"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"Key deadlines in AI and ML conferences | Yutori","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"}]

Based on the search results, here's what I found about AAAI 2027:

The Forty-first Conference on Artificial Intelligence will be held in Montréal, Québec, Canada from February 16-23, 2027.

Regarding the submission deadline, the AAAI 2027 paper submission deadline is TBD (To Be Determined). However, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns, which aligns with your query about July 2026.

The official call for papers information is available at the AAAI website, but the exact submission deadline has not yet been officially announced.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55a83c0b-d323-43f5-8eac-97398959b40f",
  "isSidechain": false,
  "promptId": "8052165b-6c36-40b2-ade0-6fd88ae7524b",
  "type": "user",
  "uuid": "75ddbc55-b9aa-4d7e-9391-3a87c49465e4",
  "toolUseResult": {
    "query": "AAAI 2027 deadline submission date July 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WQiYYj6jHhqmUH9ddmajUp",
        "content": [
          {
            "title": "AAAI Conference on Artificial Intelligence - AAAI",
            "url": "https://aaai.org/conference/aaai/"
          },
          {
            "title": "AAAI 2027 Conference Deadline | Live Countdown Tracker",
            "url": "https://www.getpaperpilot.com/deadlines/aaai-2027.html"
          },
          {
            "title": "AI Deadlines – AI Conference Call For Paper Deadlines",
            "url": "http://aideadlines.org/"
          },
          {
            "title": "Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"
          },
          {
            "title": "AAAI Conference on Artificial Intelligence",
            "url": "http://aideadlines.org/conference/?id=aaai27"
          },
          {
            "title": "AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=3"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "AAAI 2027 Conference | OpenReview",
            "url": "https://openreview.net/group?id=AAAI.org%2F2027%2FConference"
          },
          {
            "title": "AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf",
            "url": "https://www.underleaf.ai/templates/aaai"
          },
          {
            "title": "Key deadlines in AI and ML conferences | Yutori",
            "url": "https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"
          }
        ]
      },
      "Based on the search results, here's what I found about AAAI 2027:\n\nThe Forty-first Conference on Artificial Intelligence will be held in Montréal, Québec, Canada from February 16-23, 2027.\n\nRegarding the submission deadline, the AAAI 2027 paper submission deadline is TBD (To Be Determined). However, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns, which aligns with your query about July 2026.\n\nThe official call for papers information is available at the AAAI website, but the exact submission deadline has not yet been officially announced."
    ],
    "durationSeconds": 3.648499404999995
  },
  "sourceToolAssistantUUID": "55a83c0b-d323-43f5-8eac-97398959b40f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-17T09:20:27.891Z_

<details><summary>↩ Tool result · `toolu_01RK8x8eyZfJjT9LCDBS59K1`</summary>

```text
Web search results for query: "query-conditional head gating attention heads adaptive context 2025 2026 arxiv"

Links: [{"title":"HAVE: Head-Adaptive Gating and ValuE Calibration for Hallucination Mitigation in Large Language Models","url":"https://arxiv.org/html/2509.06596v1"},{"title":"Unveiling Simplicities of Attention: Adaptive Long-Context Head Identification","url":"https://arxiv.org/html/2502.09647"},{"title":"Causal Head Gating: A Framework for Interpreting Roles of ...","url":"https://arxiv.org/pdf/2505.13737"},{"title":"Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers","url":"https://arxiv.org/html/2505.13737v2"},{"title":"[2502.09647] Unveiling Simplicities of Attention: Adaptive Long-Context Head Identification","url":"https://arxiv.org/abs/2502.09647"},{"title":"[2505.13737] Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers","url":"https://arxiv.org/abs/2505.13737"},{"title":"Gated Attention Mechanisms","url":"https://www.emergentmind.com/topics/gated-attention-ga"},{"title":"[2505.15807] The Atlas of In-Context Learning: How Attention Heads Shape In-Context Retrieval Augmentation","url":"https://arxiv.org/abs/2505.15807"},{"title":"Differential Gated Self-Attention","url":"https://arxiv.org/html/2505.24054"},{"title":"SeerAttention-R: Sparse Attention Adaptation for Long Reasoning","url":"https://arxiv.org/html/2506.08889v1"}]

I found several highly relevant papers from arXiv that match your search query about query-conditional head gating, attention heads, and adaptive context. Here are the key results:

## Main Findings

### 1. **Unveiling Simplicities of Attention: Adaptive Long-Context Head Identification** (2502.09647, March 2025)
This paper presents an analysis comparing a query-adaptive oracle criterion, which selects local heads independently for each token, and finds that a query-adaptive oracle criterion allows to label a substantially higher percentage of heads as local heads (up to 90%) without sacrificing performance. The paper proposes a novel query-adaptive attention criterion (QAdA) based on second-order statistics of the attention scores.

### 2. **Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers** (2505.13737, May/October 2025)
This work presents causal head gating (CHG), a scalable method for interpreting the functional roles of attention heads in transformer models that learns soft gates over heads and assigns them a causal taxonomy - facilitating, interfering, or irrelevant - based on their impact on task performance.

### 3. **HAVE: Head-Adaptive Gating and ValuE Calibration** (2509.06596, September 2025)
This framework adaptively reweights attention heads at the instance level and introduces head-adaptive gating, which performs instance-level soft reweighing of attention heads, and value calibration, which augments attention with the magnitude of value vectors to approximate write-back contribution.

### 4. **Multihead Differential Gated Self-Attention** (2505.24054, September 2025)
This proposes Multihead Differential Gated Self-Attention (M-DGSA) that learns per-head input-dependent gating to dynamically suppress attention noise, where each head splits into excitatory and inhibitory branches whose dual softmax maps are fused by a sigmoid gate predicted from the token embedding.

These papers represent recent work (2025-2026) on adaptive, query-conditional mechanisms for managing attention heads in transformers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1eb0d544-15bf-4628-a354-fa43668f5d30",
  "isSidechain": false,
  "promptId": "8052165b-6c36-40b2-ade0-6fd88ae7524b",
  "type": "user",
  "uuid": "83061b54-e9d3-4a82-9b20-81ca4abfcf05",
  "toolUseResult": {
    "query": "query-conditional head gating attention heads adaptive context 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_017hQFvNzZTe8jXr6YdBZWUJ",
        "content": [
          {
            "title": "HAVE: Head-Adaptive Gating and ValuE Calibration for Hallucination Mitigation in Large Language Models",
            "url": "https://arxiv.org/html/2509.06596v1"
          },
          {
            "title": "Unveiling Simplicities of Attention: Adaptive Long-Context Head Identification",
            "url": "https://arxiv.org/html/2502.09647"
          },
          {
            "title": "Causal Head Gating: A Framework for Interpreting Roles of ...",
            "url": "https://arxiv.org/pdf/2505.13737"
          },
          {
            "title": "Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers",
            "url": "https://arxiv.org/html/2505.13737v2"
          },
          {
            "title": "[2502.09647] Unveiling Simplicities of Attention: Adaptive Long-Context Head Identification",
            "url": "https://arxiv.org/abs/2502.09647"
          },
          {
            "title": "[2505.13737] Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers",
            "url": "https://arxiv.org/abs/2505.13737"
          },
          {
            "title": "Gated Attention Mechanisms",
            "url": "https://www.emergentmind.com/topics/gated-attention-ga"
          },
          {
            "title": "[2505.15807] The Atlas of In-Context Learning: How Attention Heads Shape In-Context Retrieval Augmentation",
            "url": "https://arxiv.org/abs/2505.15807"
          },
          {
            "title": "Differential Gated Self-Attention",
            "url": "https://arxiv.org/html/2505.24054"
          },
          {
            "title": "SeerAttention-R: Sparse Attention Adaptation for Long Reasoning",
            "url": "https://arxiv.org/html/2506.08889v1"
          }
        ]
      },
      "I found several highly relevant papers from arXiv that match your search query about query-conditional head gating, attention heads, and adaptive context. Here are the key results:\n\n## Main Findings\n\n### 1. **Unveiling Simplicities of Attention: Adaptive Long-Context Head Identification** (2502.09647, March 2025)\nThis paper presents an analysis comparing a query-adaptive oracle criterion, which selects local heads independently for each token, and finds that a query-adaptive oracle criterion allows to label a substantially higher percentage of heads as local heads (up to 90%) without sacrificing performance. The paper proposes a novel query-adaptive attention criterion (QAdA) based on second-order statistics of the attention scores.\n\n### 2. **Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers** (2505.13737, May/October 2025)\nThis work presents causal head gating (CHG), a scalable method for interpreting the functional roles of attention heads in transformer models that learns soft gates over heads and assigns them a causal taxonomy - facilitating, interfering, or irrelevant - based on their impact on task performance.\n\n### 3. **HAVE: Head-Adaptive Gating and ValuE Calibration** (2509.06596, September 2025)\nThis framework adaptively reweights attention heads at the instance level and introduces head-adaptive gating, which performs instance-level soft reweighing of attention heads, and value calibration, which augments attention with the magnitude of value vectors to approximate write-back contribution.\n\n### 4. **Multihead Differential Gated Self-Attention** (2505.24054, September 2025)\nThis proposes Multihead Differential Gated Self-Attention (M-DGSA) that learns per-head input-dependent gating to dynamically suppress attention noise, where each head splits into excitatory and inhibitory branches whose dual softmax maps are fused by a sigmoid gate predicted from the token embedding.\n\nThese papers represent recent work (2025-2026) on adaptive, query-conditional mechanisms for managing attention heads in transformers."
    ],
    "durationSeconds": 9.771236116
  },
  "sourceToolAssistantUUID": "1eb0d544-15bf-4628-a354-fa43668f5d30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 55 · 2026-05-17T09:20:27.896Z_

```json
{
  "parentUuid": "83061b54-e9d3-4a82-9b20-81ca4abfcf05",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fd92d82b-ebe6-4f5b-bfd6-bba64e1ca27a",
  "timestamp": "2026-05-17T09:20:27.896Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 56 · 2026-05-17T09:20:53.683Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me synthesize what I've learned and draft the revision.

Key changes needed:

1. **Add RetMask as primary baseline** - RetMask uses DPO with contrastive signals from retrieval head masking. Key differentiation: RetMask modifies full model weights via DPO training signal derived from head masking; EAGT adds permanent query-conditional gates to specific heads. RetMask treats head masking as a training signal generator; EAGT treats gates as permanent architectural additions.

2. **Address "dynamic heads" challenge** - The 18-46% overlap (Jaccard) between static and dynamic retrieval heads is based on heuristic attention-pattern identification. 

But entrainment heads are actually defined by their causal functional role—specifically, boosting logits for tokens already seen in context—not by which tokens they attend to. The dynamism I'm observing applies to *which tokens* get retrieved, not to *which heads perform the retrieval mechanism itself*. The gates solve this by handling input-dependent variation, allowing the same entrainment head to activate or deactivate based on the query.

3. **Add CHG as static-gate ablation** - CHG learns one scalar per head, providing a simpler baseline for EAGT's more sophisticated gating approach.

4. **Strengthen "non-trivial combination" argument** - The same head receives conflicting signals from both L_suppress and L_preserve losses. A fixed gate value can't minimize both simultaneously, so the gate *must* learn query-conditional behavior to resolve this tension. This is the theoretical crux.

5. **Venue: EACL 2027 primary** - ARR deadline August 3, 2026. Makes sense as the primary NLP venue with good timeline. AAAI 2027 as secondary (deadline TBD, expected July-Aug 2026). ICLR 2027 as tertiary.

Now I'm constructing the complete revised JSON. The change_type should be "minor" since the core approach remains the same.

For the landscape section, I need to add RetMask in the training-based category, incorporate "Retrieval Heads are Dynamic" into the discussion, and include CHG as a baseline while strengthening the non-trivial combination argument. The approach section needs the CHG static-gate ablation, the theoretical argument for why dual-objective doesn't collapse, and addressing the dynamic heads concern. I'll add the three new papers to key_references and reorder target_venues with EACL 2027 as primary.

Drafting the revision now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd92d82b-ebe6-4f5b-bfd6-bba64e1ca27a",
  "isSidechain": false,
  "requestId": "req_011Cb7toYT63NK8Ww5PWS1yG",
  "type": "assistant",
  "uuid": "9d4961e0-33a5-4854-960b-f53abf3d19bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXbimAFoLQd5LbKrDiasrB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2602,
      "cache_read_input_tokens": 36613,
      "output_tokens": 9628,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2602,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9628,
          "cache_read_input_tokens": 36613,
          "cache_creation_input_tokens": 2602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2602
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

_source line 57 · 2026-05-17T09:24:43.686Z_

Now I have all the information needed. Let me synthesize the findings and produce the revised idea.

Key findings from my research:
- **RetMask**: Uses DPO with contrastive signals from retrieval head masking. Modifies full model, not just heads. Training signal approach vs. EAGT's architectural modification.
- **"Retrieval Heads are Dynamic"**: Jaccard overlap 18-46% between static/dynamic heads, but uses heuristic attention-pattern identification (correlational), unlike entrainment heads' causal differentiable masking (functional).
- **CHG**: One scalar gate per head, task-specific but static. Natural ablation baseline for EAGT's query-conditional gates.

Producing the revised idea now.

```json
{
  "title": "Entrainment-Aware Gated Fine-Tuning: Query-Conditional Head Gates for Adaptive Context Utilization",
  "core_problem": "LLMs' vulnerability to irrelevant context (distraction) is mechanistically localized to entrainment heads (2.9-10.7% of attention heads per relation, ACL 2025 Outstanding Paper). Static ablation of these heads effectively reduces distraction with only 0.2-3% ICL degradation, confirming they are not part of the core ICL circuit. However, static ablation is a permanent, binary intervention: it unconditionally removes context-sensitivity from these heads regardless of whether the context is relevant or irrelevant. The ACL 2025 paper explicitly acknowledges (Finding 2) that context can be beneficial when relevant — e.g., related-domain context steers generation toward correct answers — yet never evaluates ablation's impact on this capability. In real deployment scenarios (RAG with correct retrievals, long-context QA where context IS the answer source, grounded generation), permanently disabling context-sensitivity is counterproductive. Recent work on RAG head reweighting (PEAR, ACM Web 2025) demonstrates that context-suppressing heads should be continuously attenuated rather than removed, and that learned coefficients outperform binary decisions. Dynamic head selection methods (MoH, ICML 2025; QAdA, 2025) further show that adaptive per-query head activation consistently outperforms static head pruning. Crucially, 'Retrieval Heads are Dynamic' (arXiv:2602.11162) shows that at any generation step, only 18-46% of dynamically-active retrieval heads overlap with statically-identified top-k heads (Jaccard similarity), underscoring the inadequacy of static interventions — but this finding applies to heuristically-identified retrieval heads (attention-pattern-based), not to causally-identified entrainment heads (differentiable-masking-based), creating an open question about whether causal circuit identification yields more stable head sets. The gap: no method combines mechanistic entrainment head identification with query-conditional per-head gating to enable adaptive context utilization — suppressing distraction when context is irrelevant while preserving context-sensitivity when context is helpful.",
  "opportunity": "Four building blocks now exist but remain uncombined: (1) The ACL 2025 entrainment paper provides differentiable masking for head discovery across 15 knowledge relations, with code available at github.com/frankniujc/entrainment, and crucially identifies heads whose context-sensitivity is harmful for irrelevant context but potentially beneficial for relevant context — these heads are identified via causal gradient-based optimization (functional role in logit boosting), a stronger identification criterion than the heuristic attention-pattern matching used for retrieval heads; (2) The NeurIPS 2025 Best Paper on gated attention proved that query-dependent per-head sigmoid gates (G1 design: query-projected, post-SDPA) enable heads to modulate their output from full contribution to zero, with per-head gating identified as the single most important design choice; (3) PEAR (ACM Web 2025) demonstrated that learned continuous coefficients on context-affecting heads outperform binary ablation for RAG, validating the premise that learned gating is superior to static head removal; (4) RetMask (arXiv:2601.11020) demonstrated that mechanistically-identified head masking can generate effective training signals for long-context improvement via DPO (+2.28 on HELMET at 128K), validating the broader premise that head-level mechanistic insights translate to training-time gains. The opportunity is to synthesize these into a fine-tuning intervention that adds query-conditional gates ONLY to mechanistically-identified entrainment heads, training with a dual-objective loss to produce a permanently modified model that adaptively modulates context-sensitivity per query. This requires no inference-time steering, adds negligible parameter overhead (<0.1%), and negligible inference overhead (one linear+sigmoid per gated head). The non-trivial insight enabling this synthesis: because the SAME entrainment head receives both suppression signals (from distractor examples) and preservation signals (from relevant-context examples) during training, the gate CANNOT collapse to a fixed value — it must learn query-conditional behavior to minimize both objectives simultaneously.",
  "landscape": "**Training-based distraction defense (whole-model):** NoisyInstruct + RARE reward (arXiv:2601.07226, Jan 2026) trains models via SFT+RL on noisy data, achieving strong robustness gains but modifying all parameters without mechanistic targeting. Distractor Injection Attacks defense (arXiv:2510.16259) similarly uses SFT+RL on synthetic adversarial data. GSM-DC (EMNLP 2025) showed continued pretraining with distractors is effective for reasoning robustness. **Training-based (mechanistic head targeting):** RetMask (arXiv:2601.11020, Jan 2026) is a KEY BASELINE — it bridges 'head identification → training improvement' by using retrieval head masking to generate contrastive training signals for DPO, achieving +2.28 on HELMET at 128K (Llama-3.1), +70% on generation with citation, and +32% on passage re-ranking. RetMask masks 4-10% of attention heads (identified via NIAH heuristics) to produce degraded responses, then trains the full model via DPO to prefer unmasked outputs. Critical differences from EAGT: (a) RetMask uses head masking as a training signal generator (behavioral modification via DPO on all parameters), while EAGT adds permanent query-conditional gates (architectural modification of specific heads only); (b) RetMask identifies retrieval heads via attention-pattern heuristics (NIAH task), while EAGT targets entrainment heads via causal differentiable masking; (c) RetMask optimizes for long-context retrieval performance, while EAGT optimizes for distraction resistance with context-sensitivity preservation; (d) RetMask's DPO training modifies all model parameters — EAGT modifies <0.1%. **Training-based (layer-level gating):** Grft (ACL 2025, arXiv:2502.14100) is another key baseline — a gated representation fine-tuning approach applying sigmoid gating at a single layer (layer 7 in Llama-2-7B). Grft achieves strong helpful-context preservation (98.23% short, 97.03% long — nearly matching the ~97% baseline) with meaningful adversarial robustness gains (60-73% without requery, 82-98% with requery). Its actual limitations are: (a) operates at layer-level granularity rather than at mechanistically-identified heads, (b) trained exclusively on knowledge-conflict scenarios (ConflictQA/COUNTERFACT) — untested on reasoning distractors (GSM-DC, NoisyBench), (c) gate is hidden-state-conditional rather than query-conditional, (d) limited to single-context evaluation. Only 36.9K parameters (0.0005% of model). **Learned head reweighting for RAG:** PEAR (ACM Web 2025) identifies context-suppressing attention heads and learns continuous reweighting coefficients via a context-copying proxy task, achieving improved RAG accuracy with zero inference overhead. ADR similarly detects and reweights RAG-suppressing heads. Both validate that learned continuous modulation of head outputs outperforms binary decisions, but neither uses mechanistic head identification or query-conditional gating — coefficients are fixed after training. **Static head gating (interpretability):** Causal Head Gating (CHG, NeurIPS 2025, arXiv:2505.13737) learns one scalar gate per attention head via next-token prediction loss with inverse-sigmoid regularization, categorizing heads as facilitating, interfering, or irrelevant. CHG is extremely lightweight (one parameter per head) and demonstrates causal insight validated via ablation. Critically, CHG gates are STATIC per task — they cannot adapt per query. CHG serves as the natural ablation baseline for EAGT: comparing EAGT's query-conditional gates against CHG-style static per-head gates directly demonstrates the value of query-conditioning. **Dynamic head selection:** MoH (ICML 2025) treats attention heads as MoE experts with a learned router, achieving +2.4% accuracy over LLaMA3-8B on 14 benchmarks using only 75% of heads. QAdA demonstrates that adaptive per-query head selection outperforms static oracle selection on long-context tasks. SeerAttention (Microsoft, 2025) shows learned attention gating significantly outperforms static/heuristic sparse attention methods. These demonstrate the superiority of dynamic over static head decisions but are general-purpose, not targeted at distraction resistance. **Dynamic head stability:** 'Retrieval Heads are Dynamic' (arXiv:2602.11162, Feb 2026) shows that at any generation step, only 18-46% of dynamically-active retrieval heads overlap with statically-identified top-20 heads (Jaccard similarity: Llama-3.1-8B 35%, Qwen3-8B 46%). This raises a fundamental question for head-targeting methods. However, a critical methodological distinction applies: retrieval heads are identified via heuristic attention-pattern matching (does the head attend to the token it generates?), which captures correlational input-dependent behavior. Entrainment heads are identified via causal differentiable masking (does removing this head reduce logit boosting for context-seen tokens?), which captures functional circuit membership. The dynamism finding shows that WHICH tokens a head retrieves varies per timestep — but entrainment heads are defined by WHETHER they implement the logit-boosting mechanism, an architectural property. Furthermore, EAGT's query-conditional gates handle remaining input-dependent variation: even if a head is architecturally part of the entrainment circuit, its gate learns when that circuit's output should be used vs. suppressed. **Inference-time methods:** HAVE (arXiv:2509.06596) applies head-adaptive gating at decoding time for hallucination mitigation — parameter-free but incurs per-query overhead. Focus Directions (arXiv:2503.23306) and ContextFocus (arXiv:2601.04131) steer activations at inference without model modification. All require intervention at every forward pass. **Mechanistic fine-tuning (different targets):** ABFT (arXiv:2505.14233) modifies WQ/WK matrices of induction heads to improve ICL — targets different heads with different goals. **Gated attention (new models only):** NeurIPS 2025 Best Paper and Differential Gated Self-Attention (NeurIPS 2025) are architectural innovations for training new models from scratch — not applicable as fine-tuning interventions. **Our unique position:** EAGT is the first to (1) add learnable query-conditional gates specifically to causally-identified entrainment heads (vs. RetMask's use of heuristically-identified heads as DPO training signals, Grft's layer-level intervention, PEAR's fixed coefficients, CHG's static per-head gates, or MoH's general-purpose routing), (2) train with explicit adaptive context utilization objectives covering both distraction resistance AND relevant-context preservation (vs. Grft's knowledge-conflict-only training, RetMask's retrieval-focused DPO), (3) leverage the NeurIPS 2025 G1 gate design as a surgical fine-tuning tool targeted by mechanistic analysis, and (4) provide a principled argument for why the dual-objective training cannot collapse to static gating: the same head must simultaneously satisfy suppression (for distractors) and preservation (for relevant context), forcing genuine query-conditional behavior.",
  "approach": "We propose Entrainment-Aware Gated Fine-Tuning (EAGT) in three phases:\n\n**Phase 1: Multi-Relation Entrainment Head Discovery.** Using the differentiable masking procedure from the ACL 2025 paper (Gumbel-sigmoid with straight-through estimation, 500 epochs AdamW, sparsity regularization), we identify entrainment heads in Llama-3.1-8B (32 layers × 32 heads = 1024 heads) across the 15 LRE relations used in the original paper. We take the UNION of discovered heads across all relations. Based on the original paper's findings (2.9-10.7% per relation with partial overlap), we estimate the union set at ~15-20% of heads. This is deliberately broader than any single relation's set — the per-head gate mechanism will learn query-specific activation patterns within this candidate set. We also validate on Qwen3-8B as a secondary model, acknowledging that the differentiable masking procedure has not been previously applied to Qwen architectures and may require hyperparameter adjustment.\n\n**Entrainment head stability analysis (addressing dynamic-heads concern).** We conduct a targeted experiment to verify whether entrainment heads exhibit greater stability than heuristically-identified retrieval heads. Using the ACL 2025 differentiable masking procedure on held-out relation instances (different entities for the same 15 relations), we measure the overlap between entrainment head sets discovered on different data subsets. We predict high overlap because entrainment heads are defined by their causal role in a functional circuit (logit boosting for context-seen tokens), not by input-dependent attention patterns. We also compare the union-set stability against retrieval head stability (using the NIAH-based identification from RetMask) on the same model, directly testing whether causal identification yields more stable head sets than heuristic identification. If entrainment heads show Jaccard similarity >0.7 across data subsets (vs. the 0.18-0.46 reported for retrieval heads), this validates the premise of targeting a fixed head set.\n\n**Phase 2: Gate Insertion and Fine-Tuning.** We surgically insert G1-style gates (following the NeurIPS 2025 gated attention design) exclusively at union-set heads. Each gate is: g_i = σ(W_g · q_i + b_g) where q_i is the query projection for head i at sequence position i, W_g ∈ ℝ^(1×d_head) is a learnable weight, and b_g is bias. The gate produces a scalar per head per sequence position, modulating the ENTIRE attention output of that head at that position: head_output_i = g_i · Attn(Q_i, K_i, V_i). Critically, this is a per-position decision (whether the model uses attended context at position i), NOT a per-attended-token filter — the gate cannot selectively suppress attention to specific key tokens within a single head's computation. Gates are initialized to output ~1.0 (bias initialized to +3.0) to preserve pretrained behavior.\n\n**Why the dual-objective loss forces query-conditional behavior (theoretical crux).** The same entrainment head h appears in BOTH the suppression set (when processing distractor-augmented examples) and the preservation set (when processing relevant-context examples). If the gate for head h collapsed to a static value c, it would incur loss L_suppress ∝ c² on distractor examples AND loss L_preserve ∝ (1-c)² on relevant-context examples. No fixed c minimizes both — the optimal static c ≈ 0.5 is suboptimal for BOTH objectives. To minimize the combined loss, the gate must learn to use input features (the query projection q_i) to discriminate: outputting g_i → 0 when the query context indicates irrelevant information and g_i → 1 when it indicates relevant information. This is not merely a design aspiration — it is a mathematical consequence of the dual-objective setup applied to the same heads. This distinguishes EAGT from simple combination: the training signal design creates a learning problem that REQUIRES query-conditional behavior.\n\nFine-tuning uses a three-component loss:\n(L_CLM) Standard causal LM loss on clean data to maintain general capabilities.\n(L_suppress) At answer/reasoning positions in distractor-augmented examples, penalize high gate values: L_suppress = Σ_{i ∈ S_distracted} g_i², where S_distracted is the set of positions where the model should rely on parametric knowledge rather than distractor-contaminated attention. This teaches entrainment head gates to close when their attention output would propagate irrelevant context.\n(L_preserve) At answer positions in relevant-context examples (ICL demonstrations, RAG with correct retrievals), penalize low gate values: L_preserve = Σ_{i ∈ S_relevant} (1 - g_i)², where S_relevant is the set of positions where the model should use attended context. This teaches gates to stay open when context IS the answer source.\n\nOnly gate parameters and optional rank-4 LoRA on entrainment heads' value projections are updated (<0.1% of total parameters).\n\n**Phase 3: Training Data Construction.** Following established synthetic distractor methodology: (a) GSM-DC-style symbolic graph problems with controlled distractor injection for math reasoning, with ground-truth distractor positions known by construction; (b) NoisyInstruct-style augmentation with random documents, irrelevant chat histories, and LLM-generated hard negatives for general QA; (c) Clean versions of (a) and (b) without distractors, plus few-shot ICL demonstrations and RAG examples with verified-correct retrievals, for the preservation objective. The key training signal is positional: at answer-generation positions, should the model rely on attention (gate open) or bypass it (gate closed)?\n\n**Evaluation — expanded to directly test the static-ablation gap and query-conditionality:**\n(1) Distraction robustness: GSM-NoOp (ICLR 2025), GSM-DC (EMNLP 2025), NoisyBench (arXiv:2601.07226).\n(2) **Relevant-context utilization (critical new evaluation):** Performance on RAG benchmarks with correct retrievals (Natural Questions open-domain, TriviaQA with gold passages), long-context QA where context contains the answer (NarrativeQA, QuALITY), and few-shot ICL (SST-2, AGNews, DBPedia). We compare EAGT vs. static ablation vs. no intervention on these tasks to quantify the cost of permanent context-sensitivity removal.\n(3) **Long-context retrieval (RetMask comparison):** HELMET benchmark at 32K and 128K to directly compare against RetMask's reported improvements.\n(4) General capabilities: MMLU, HellaSwag, ARC-Challenge.\n(5) Ablations:\n  - **CHG-style static gates (critical ablation):** Replace EAGT's query-conditional gates (W_g · q_i + b_g) with CHG-style static scalar gates (one learnable scalar per head, no query dependence), trained with the same dual-objective loss. If query-conditional gates significantly outperform static gates on the relevant-context preservation task while matching on distraction suppression, this demonstrates the core contribution of query-conditioning. We predict that static gates will converge to intermediate values (~0.5) that are suboptimal for both objectives, while query-conditional gates will learn to discriminate.\n  - Gate-only vs. gate+LoRA, union-set vs. per-relation gating, gate initialization sensitivity, loss weight sweep, static ablation baseline on all benchmarks.\n(6) **Entrainment head stability analysis:** Cross-subset overlap of discovered heads (Jaccard similarity) compared to retrieval head stability, validating the premise of targeting a fixed head set.\n(7) Gate behavior analysis: visualization of learned gate patterns across distractor vs. relevant-context examples, per-relation gate specialization analysis, distribution of learned gate values (demonstrating bimodal distribution for query-conditional gates vs. unimodal for static gates).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~240-320h A100 80GB (entrainment discovery on Llama-3.1-8B: ~30h across 15 relations; stability analysis: ~15h; Qwen3-8B discovery: ~35h with potential hyperparameter iteration; gate training sweeps including CHG-static ablation: ~100h; expanded evaluation suite including RAG benchmarks and HELMET: ~60h; remaining ablations: ~60h)",
      "gpu_utilization": "~25-35% effective; GPU idles during debugging, result analysis, and experiment design",
      "timeline": "8-10 weeks (targeting EACL 2027 ARR August 3 deadline with comfortable buffer)",
      "team": "1-2 researchers with mechanistic interpretability experience",
      "estimated_gpu_cost": "$360-$480 at ~$1.50/h"
    },
    "human_in_loop": {
      "gpu_hours": "~320-420h A100 80GB (agent runs systematic discovery across all 15 relations, stability analysis, comprehensive loss-weight sweeps, CHG-static ablation, RAG evaluation, HELMET evaluation)",
      "gpu_utilization": "~55-65%; agent batches experiments but pauses for human review of union-set topology, stability metrics, and gate training stability",
      "timeline": "5-7 weeks (comfortably targeting EACL 2027 ARR August 3 deadline)",
      "team": "1 researcher, ~30min/day for reviewing entrainment head maps and loss diagnostics",
      "claude_api_cost": "$300-$450 (~3500-5500 turns)",
      "estimated_gpu_cost": "$480-$630 at ~$1.50/h",
      "risk_note": "Union-set size may require iteration: if too large (>25%), may need overlap-thresholding; if too sparse (<10%), the positional gate signal may be weak. Qwen3-8B discovery may need architecture-specific adjustments to differentiable masking hyperparameters. Stability analysis may reveal lower-than-expected overlap, requiring revised head selection strategy."
    },
    "auto_research": {
      "gpu_hours": "~750-1100h A100 80GB (exhaustive multi-relation discovery, stability analysis across multiple data subsets, full gate-design ablations including CHG-static comparison, cross-model validation, Grft reproduction, RetMask comparison on HELMET, static ablation baseline across all benchmarks, RAG evaluation suite)",
      "gpu_utilization": "~85-95%; agent continuously pipelines experiments with near-zero idle",
      "timeline": "2-3 weeks with 4-8 parallel A100 GPUs",
      "team": "0 (initial setup ~3h for environment, datasets, and relation probe data)",
      "claude_api_cost": "$600-$1050 (~7000-13000 turns)",
      "estimated_gpu_cost": "$1,125-$1,650 at ~$1.50/h",
      "speed_bottleneck": "Sequential dependency between discovery phase (per model) and gate training phase; 15-relation discovery parallelizes well across GPUs",
      "risk_note": "Agent may over-explore gate architectures (MLP vs linear, shared vs independent bias); estimated 15-20% compute on low-value ablations. Risk of reproducing Grft baseline incorrectly due to limited implementation details in the paper. RetMask reproduction requires NIAH-based retrieval head identification which may not perfectly replicate original results."
    }
  },
  "target_venues": [
    "EACL 2027 (ARR deadline August 3, 2026; top European NLP venue; only one ARR cycle available for this conference; strong fit for NLP + mechanistic interpretability work; closest NLP venue with adequate timeline; venue change from originally-requested EMNLP 2026 is necessary because the May 25 ARR deadline is too tight)",
    "AAAI 2027 (deadline expected ~July-August 2026, not yet officially announced; strong venue for methodological contributions combining mechanistic interpretability + architectural innovation; good fit for the emphasis on novel AI methodology)",
    "ICLR 2027 (deadline expected ~Sep-Oct 2026, not yet announced; highest-tier ML venue; extra time provides buffer for comprehensive experiments and Qwen3 validation)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs (ACL 2025, Outstanding Paper, arXiv:2505.09338) — entrainment head discovery via differentiable masking; Finding 2: context can be beneficial when relevant; static ablation causes only 0.2-3% ICL degradation, confirming heads are not ICL circuit",
    "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free (NeurIPS 2025, Best Paper, arXiv:2505.06708) — G1 gate design: query-conditional, post-SDPA sigmoid gates producing per-position per-head scalars; per-head gating identified as most important design choice",
    "Towards Context-Robust LLMs: A Gated Representation Fine-tuning Approach (Grft, ACL 2025, arXiv:2502.14100) — KEY BASELINE: layer-level gated fine-tuning for context robustness; achieves 98.23%/97.03% on helpful contexts; trained on ConflictQA/COUNTERFACT only; hidden-state-conditional gate",
    "From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models (RetMask, arXiv:2601.11020, Jan 2026) — KEY BASELINE: uses retrieval head masking to generate DPO contrastive training signals, +2.28 on HELMET at 128K; masks 4-10% of heads identified via NIAH heuristics; modifies all model parameters via DPO; validates premise that head-level mechanistic insights → training-time gains",
    "Retrieval Heads are Dynamic (arXiv:2602.11162, Feb 2026) — shows only 18-46% Jaccard overlap between dynamic and static retrieval heads across models (Llama-3.1-8B: 35%, Qwen3-8B: 46%); uses heuristic attention-pattern identification; raises stability concern for static head targeting but applies to correlational (not causal) identification",
    "Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers (CHG, NeurIPS 2025, arXiv:2505.13737) — learns one static scalar gate per head via NTP loss; categorizes heads as facilitating/interfering/irrelevant; natural static-gate ablation baseline for EAGT's query-conditional gates",
    "PEAR: Position-Embedding-Agnostic Attention Re-weighting Enhances RAG with Zero Inference Overhead (ACM Web Conference 2025, arXiv:2409.19745) — learned continuous reweighting of context-suppressing heads for RAG; validates that learned coefficients outperform binary ablation; fixed post-training coefficients",
    "MoH: Multi-Head Attention as Mixture-of-Head Attention (ICML 2025, arXiv:2410.11842) — dynamic head selection via learned routing achieves +2.4% over LLaMA3-8B with 75% of heads; demonstrates adaptive head selection > static decisions",
    "Unveiling Simplicities of Attention: Adaptive Long-Context Head Identification (QAdA, arXiv:2502.09647) — adaptive per-query head selection outperforms static oracle criterion on long-context benchmarks",
    "Mechanistic Fine-tuning for In-context Learning (ABFT, arXiv:2505.14233) — modifies WQ/WK of induction heads; complementary target and method",
    "Lost in the Noise: How Reasoning Models Fail with Contextual Distractors (arXiv:2601.07226, Jan 2026) — NoisyBench evaluation + NoisyInstruct training methodology + RARE reward",
    "GSM-DC: How Is LLM Reasoning Distracted by Irrelevant Context? (EMNLP 2025) — synthetic DAG-based distractor injection benchmark",
    "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in LLMs (ICLR 2025) — GSM-NoOp benchmark showing up to 65% drops from irrelevant information",
    "Distractor Injection Attacks on Large Reasoning Models: Characterization and Defense (arXiv:2510.16259) — SFT+RL defense baseline on synthetic adversarial data",
    "Focus Directions Make Your Language Models Pay More Attention to Relevant Contexts (arXiv:2503.23306) — inference-time steering baseline",
    "HAVE: Head-Adaptive Gating and ValuE Calibration for Hallucination Mitigation (arXiv:2509.06596) — inference-time head-adaptive gating baseline",
    "SeerAttention: Learning Intrinsic Sparse Attention in Your LLMs (Microsoft, arXiv:2410.13276) — learned attention gating significantly outperforms static/heuristic sparse attention",
    "On the Role of Attention Heads in Large Language Model Safety (ICLR 2025, arXiv:2410.13708) — static ablation of safety heads destroys safety while general benchmarks show no degradation; demonstrates hidden costs of static ablation",
    "Differential Gated Self-Attention (NeurIPS 2025, arXiv:2505.24054) — excitatory/inhibitory gating for new model training; per-token per-head attention weight modulation"
  ],
  "description": "Entrainment-Aware Gated Fine-Tuning (EAGT) addresses the limitations of static ablation as a defense against LLM distraction. While static ablation of entrainment heads (ACL 2025) effectively reduces distraction with minimal ICL cost (0.2-3%), it permanently removes context-sensitivity — a capability that is essential when context IS relevant, such as in RAG with correct retrievals, long-context QA, and grounded generation. The ACL 2025 paper itself acknowledges (Finding 2) that related context can be beneficial, steering generation toward correct answers, yet never evaluates ablation's impact on this beneficial capability. RetMask (arXiv:2601.11020) validates the broader premise that head-level mechanistic insights translate to training-time gains, achieving +2.28 on HELMET via DPO with retrieval head masking — but modifies all model parameters and uses heuristic head identification. PEAR (ACM Web 2025) independently validates that context-affecting heads require continuous learned modulation rather than binary removal, and MoH (ICML 2025) demonstrates that dynamic head selection outperforms static decisions by +2.4%. A key concern — 'Retrieval Heads are Dynamic' (arXiv:2602.11162) shows only 18-46% overlap between static and dynamic retrieval heads — is addressed by the distinction between heuristic identification (attention-pattern-based, correlational) and causal identification (differentiable-masking-based, functional): entrainment heads are defined by their role in a logit-boosting circuit, an architectural property, not by input-dependent attention patterns. We include a stability analysis to empirically validate this distinction.\n\nEAGT fills the gap between static ablation (always suppress) and no intervention (always vulnerable) by: (1) discovering the union set of entrainment heads across 15 knowledge relations via differentiable masking (~15-20% of heads), with stability verification; (2) inserting query-conditional sigmoid gates (NeurIPS 2025 G1 design) exclusively at these heads, initialized to preserve pretrained behavior; and (3) fine-tuning with a positionally-supervised dual-objective loss — gate suppression at answer positions in distractor-augmented examples, and gate preservation at answer positions in relevant-context examples (RAG with gold passages, ICL demonstrations). The theoretical crux that makes this combination non-trivial: the SAME entrainment head receives both suppression and preservation signals during training. A static gate value c would incur loss ∝ c² on distractor examples AND ∝ (1-c)² on relevant-context examples — no fixed c minimizes both. The gate MUST learn to use query features to discriminate, producing genuinely query-conditional behavior as a mathematical consequence of the dual-objective setup, not merely a design aspiration.\n\nKey advantages over Grft: head-level vs layer-level granularity, query-conditional gating, mechanistic targeting, and training on both reasoning distractors and knowledge conflicts (vs. Grft's ConflictQA-only training). Key advantages over RetMask: architectural modification with <0.1% parameters vs. full-model DPO, causal head identification vs. heuristic, adaptive per-query gating vs. uniform improvement, distraction-focused vs. retrieval-focused. Key advantages over static ablation: adaptive per-query context-sensitivity modulation with zero permanent capability loss. Key advantages over CHG-style static gates: query-conditional discrimination enables bimodal gate behavior (open/closed per query) vs. compromise intermediate values. Key advantages over inference-time methods (HAVE, Focus Directions): no per-query overhead, permanently improved model.\n\nEvaluation on Llama-3.1-8B (primary) and Qwen3-8B (secondary, with acknowledged validation risk) across distraction benchmarks (GSM-NoOp, GSM-DC, NoisyBench), relevant-context benchmarks (NQ open-domain, TriviaQA with gold passages, NarrativeQA), long-context retrieval (HELMET for RetMask comparison), ICL tasks, and general capabilities (MMLU, HellaSwag) will demonstrate that EAGT achieves distraction resistance comparable to static ablation while preserving context utilization that static ablation sacrifices. The CHG-style static-gate ablation directly demonstrates the value of query-conditioning.",
  "project_name": "entrainment_gated_ft",
  "source": "web_research",
  "change_type": "minor"
}
```

**Summary of changes addressing each reviewer issue:**

1. **RetMask (IMPORTANT):** Added as a primary baseline throughout landscape, with detailed differentiation — RetMask uses head masking as a DPO training signal generator (behavioral modification, all parameters), while EAGT adds permanent query-conditional gates (architectural modification, <0.1% parameters). Different head identification (NIAH heuristic vs. causal differentiable masking) and different optimization targets (retrieval vs. distraction resistance). Added HELMET evaluation for direct comparison.

2. **"Retrieval Heads are Dynamic" (IMPORTANT):** Addressed in core_problem, landscape, and approach. The key argument: the 18-46% overlap finding applies to heuristically-identified retrieval heads (attention-pattern correlation), while entrainment heads are causally identified via differentiable masking (functional circuit membership). Added a concrete stability analysis experiment comparing entrainment head overlap across data subsets against retrieval head overlap, predicting >0.7 Jaccard for entrainment heads.

3. **CHG static-gate ablation (MODERATE):** Added CHG as a baseline in landscape and as a critical ablation in the evaluation plan. The ablation replaces query-conditional gates with CHG-style static scalars trained with the same dual-objective loss, directly testing whether query-conditioning provides value. Predicted outcome: static gates converge to ~0.5 (suboptimal for both objectives), while query-conditional gates learn bimodal behavior.

4. **"Combination paper" risk (MODERATE):** Added the theoretical crux argument in both the opportunity and approach sections. The same head receiving both L_suppress and L_preserve creates a learning problem that mathematically cannot be solved by a static gate — no fixed c minimizes both c² and (1-c)². This forces the gate to use query features, making query-conditional behavior a consequence of the training setup, not just a design choice.

5. **Venue (MINOR):** Reordered to EACL 2027 (ARR August 3, 2026) as primary venue, AAAI 2027 and ICLR 2027 as secondary/tertiary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d4961e0-33a5-4854-960b-f53abf3d19bd",
  "isSidechain": false,
  "requestId": "req_011Cb7toYT63NK8Ww5PWS1yG",
  "type": "assistant",
  "uuid": "2ab26b2b-dc18-461a-8f3c-6e796e2c2ff9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXbimAFoLQd5LbKrDiasrB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2602,
      "cache_read_input_tokens": 36613,
      "output_tokens": 9628,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2602,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9628,
          "cache_read_input_tokens": 36613,
          "cache_creation_input_tokens": 2602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2602
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

_source line 58_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-17 (UTC).**  ## Original idea {   \"title\": \"Entrainment-Aware Gated Fine-Tuning: Query-Conditional Head Gates for…",
  "leafUuid": "2ab26b2b-dc18-461a-8f3c-6e796e2c2ff9",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise EAGT with RetMask, dynamic heads, and query-conditional ablation",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e"
}
```

---

### Runtime record

_source line 60_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-17 (UTC).**  ## Original idea {   \"title\": \"Entrainment-Aware Gated Fine-Tuning: Query-Conditional Head Gates for…",
  "leafUuid": "2ab26b2b-dc18-461a-8f3c-6e796e2c2ff9",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e"
}
```

---

### Runtime record

_source line 61_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise EAGT with RetMask, dynamic heads, and query-conditional ablation",
  "sessionId": "e3e6ae49-b321-4c18-9d68-935c3073671e"
}
```

---
