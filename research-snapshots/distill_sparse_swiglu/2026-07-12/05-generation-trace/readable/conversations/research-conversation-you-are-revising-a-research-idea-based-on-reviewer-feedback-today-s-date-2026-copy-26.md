# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-14 (UTC).** ## Original idea { "tit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 105
- **Recorded user turns:** 1
- **Tool calls:** 31
- **Original source:** `logs/chats/exported-trajectories/account-2/85f9b876-59ee-4640-836b-8bde832bc012.jsonl`
- **Structured JSON:** [`2c1417b3233b898e2359.json`](../../sessions/2c/2c1417b3233b898e2359.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T03:20:40.088Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T03:20:40.088Z",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-14 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Beyond Difficulty: Diversity-Aware Dynamic Sampling for Data-Efficient VLA Training\",\n  \"core_problem\": \"VLA behavioral cloning datasets contain massive redundancy — recent work ('On Data Redundancy in VLA Training', 2026) shows VLAs can train on as little as 5% of LIBERO data with minimal performance loss. Yet naive difficulty-based subsampling (e.g., Temporal Surprise Score) actively hurts performance by sacrificing diversity (SmolVLA: 56.25% vs 60.50% random, GR00T: 74.00% vs 81.33% random). Meanwhile, uniform random sampling wastes compute on redundant data. The fundamental tension is: how to reduce redundancy and focus on informative demonstrations WITHOUT losing the diversity that VLA training critically depends on. Existing curation methods either operate pre-training (SCIZOR, CUPID, DataMIL, QoQ) — meaning they cannot adapt their curation to the model's evolving competence — or require expensive environment rollouts for iterative re-curation (Demo-SCORE). No existing method dynamically adjusts what is considered 'redundant' vs. 'informative' during BC training while explicitly preserving demonstration diversity.\",\n  \"opportunity\": \"The 'On Data Redundancy' finding reveals a key insight: what matters for VLA training is not example difficulty but coverage across diverse manipulation behaviors. Random subsampling works well precisely because it implicitly preserves diversity while reducing redundancy. This suggests a principled approach: explicitly maintain diversity while dynamically identifying and downweighting redundant demonstrations based on the model's evolving competence. This is distinct from both PER-style loss-proportional sampling (which sacrifices diversity, as shown empirically) and static curation (which cannot adapt to the model's learning state). The opportunity is uniquely ripe because: (1) VLA architectures (OpenVLA-OFT, SmolVLA) provide rich vision-language embeddings that can measure demonstration diversity without additional models, (2) Dynamic Loss-Based Sample Reweighting (ICLR 2025) proved dynamic reweighting works for LLM pretraining but only at token level for text — the multi-modal, action-chunked setting of VLA BC introduces fundamentally different diversity and redundancy structures, and (3) the growing scale of robot demonstration datasets (Open X-Embodiment) makes training efficiency increasingly critical.\",\n  \"landscape\": \"**Dynamic reweighting for pretraining**: Dynamic Loss-Based Sample Reweighting (ICLR 2025) performs instance-level loss-based reweighting during LLM pretraining with theoretical convergence guarantees. However, it operates at the text token level, does not address multi-modal observation-action pairs, and includes no diversity preservation mechanism — making it inapplicable when diversity loss is the primary failure mode (as in VLA BC). LiLAW (2025) uses three learnable parameters for adaptive sample difficulty weighting but lacks the coverage guarantee needed for multi-task VLA training.\\n\\n**Static/iterative demonstration curation**: SCIZOR (ICRA 2026) uses self-supervised progress prediction and embedding clustering to remove suboptimal and redundant data, achieving ~15% improvement — but curation is performed once before training and cannot adapt as the model learns. CUPID (CoRL 2025) uses influence functions to estimate each demonstration's causal impact on policy performance — a sophisticated one-pass method that captures policy-level effects but requires a fixed policy checkpoint. Demo-SCORE (RSS 2025) performs iterative curation via train→rollout→classify→re-filter cycles, genuinely adapting to model competence — but requires environment rollouts at each iteration, making it expensive and inapplicable without a simulator. DataMIL (2025) is a policy-driven framework using datamodels for end-to-end selection, operating via validation loss as a surrogate — effective but still a pre-training selection method. QoQ (2026) uses influence functions with trajectory-wise aggregation for sample-level curation. FT-NCFM (2025) goes beyond selection to data distillation/synthesis.\\n\\n**VLA-specific data insights**: 'On Data Redundancy in VLA Training' (2026) is the most directly relevant work, showing that (a) LIBERO data is >95% redundant for VLA fine-tuning, and (b) difficulty-based coresets (TSS) underperform random subsampling because they sacrifice diversity. This establishes that diversity preservation is essential for any sampling strategy — a constraint that pure loss-based methods (PER, Dynamic Reweighting) do not satisfy.\\n\\n**Balanced BC and reweighting**: 'Towards Balanced Behavior Cloning from Imbalanced Datasets' (Autonomous Robots 2026) proves that imbalanced data leads to imbalanced policies and proposes meta-gradient rebalancing. This addresses subtask imbalance (e.g., 90% reaching, 10% grasping) but not within-subtask redundancy or dynamic competence adaptation.\\n\\n**PER variants for LLM/VLM**: Freshness-Aware PER (April 2026) shows standard PER fails on LLMs due to priority staleness and proposes age-decay corrections — but only for RL post-training, not BC. Prioritized Replay for RL Post-training (Jan 2026) operates at problem-level granularity in RL, not within BC training. ExpReS-VLA (Nov 2025) uses prioritized experience replay for VLA domain adaptation / continual learning, not pre-training curation.\\n\\n**Robotic RL with filtering**: GR-RL (2025) is a dexterous manipulation framework that includes demo trajectory filtering via offline RL Q-values as one component of a larger pipeline, not a general curation method. RIPT-VLA (2025) uses advantage-based rollout filtering during RL post-training, achieving strong results (97.5% on LIBERO) but addressing a different training phase.\\n\\n**The gap**: No existing method performs dynamic, within-training demonstration sampling for VLA BC that explicitly preserves diversity while adapting to model competence. Static methods cannot adapt; iterative methods require rollouts; loss-only dynamic methods sacrifice diversity; RL post-training methods address a different phase.\",\n  \"approach\": \"We propose DADS (Diversity-Aware Dynamic Sampling), which replaces uniform data sampling in VLA behavioral cloning with a two-stage sampling strategy that couples informativeness (loss-based) with coverage (embedding diversity) at the action-chunk level.\\n\\n**Dual-Score Priority Function**: Each action chunk i receives a priority score updated every k gradient steps:\\n- Informativeness: info_i = L_i (model's current loss on chunk i)\\n- Redundancy: red_i = (1/K) Σ_{j ∈ KNN(i)} σ(-L_j) · sim(e_i, e_j), measuring average similarity to K nearest mastered (low-loss) neighbors in the VLA's frozen vision-language embedding space\\n- Priority: p_i = info_i / (1 + λ · red_i)\\n\\nThis distinguishes three types of chunks: (1) redundant-mastered (low loss, high similarity to other low-loss chunks → low priority), (2) informative (high loss, diverse from mastered chunks → high priority), and (3) noisy/outlier (high loss, but also high redundancy among other high-loss chunks → moderate priority, prevented from dominating). This directly resolves the failure mode identified in 'On Data Redundancy': difficulty-only selection (TSS) conflates types 2 and 3, losing type-1 diversity.\\n\\n**Batch-Level Diversity Constraint**: For each training batch, we use a two-stage construction: (1) sample m × batch_size candidates weighted by priorities from a sum-tree, (2) greedily select the final batch_size items maximizing: Σ p_i + β_div · FL(S), where FL(S) is the facility-location function over observation embeddings of selected set S, ensuring each batch covers diverse state-action regions. This is efficient: O(m·B·log N) for candidate sampling, O(m²·B·d) for greedy diversity selection.\\n\\n**Adaptive Diversity Schedule**: β_div is annealed from high to low during training. Early in training, when the model's loss landscape is poorly calibrated, we emphasize diversity (near-uniform over diverse modes). As training progresses and loss estimates become reliable discriminators of genuine difficulty vs. noise, we reduce β_div to allow more focus on remaining hard demonstrations. We provide a convergence analysis showing this schedule is optimal under mild assumptions about loss calibration rate.\\n\\n**Action-Chunk Granularity**: Unlike token-level reweighting (Dynamic Loss-Based Reweighting, ICLR 2025) which treats each text token independently, DADS operates at the action-chunk level — the natural prediction unit of VLA architectures. Action chunks exhibit spatial/temporal coherence within chunks but high variance across chunks (e.g., a reaching chunk vs. a grasping chunk), making chunk-level priorities more semantically meaningful than token-level. Unlike trajectory-level curation (Demo-SCORE, CUPID), chunk-level granularity allows fine-grained within-trajectory importance variation.\\n\\n**Implementation**: DADS is implemented as a drop-in PyTorch DistributedSampler compatible with OpenVLA-OFT and SmolVLA training pipelines. Priority scores are maintained in a sum-tree with O(log N) updates. Embeddings are computed from the VLA's frozen vision-language encoder (no additional model). KNN is precomputed once in embedding space and reused; only loss-based scores are refreshed every k steps. Overhead is ~10-15% over standard training.\\n\\n**Evaluation**: LIBERO (all 4 suites: Spatial, Object, Goal, Long) as the primary benchmark — directly comparable to 'On Data Redundancy' results — plus SimplerEnv for breadth. We measure: (1) absolute success rate improvement over uniform and random-subsampling baselines, (2) data efficiency curves at 5%, 10%, 25%, 50%, 100% of training data, (3) training efficiency (wall-clock time to reach target success rate). Baselines include: uniform sampling, random subsampling (strong baseline per 'On Data Redundancy'), TSS difficulty-based selection, loss-only prioritization (PER-style, expected to underperform due to diversity loss), Dynamic Loss-Based Reweighting (adapted to action chunks), SCIZOR, and standard curriculum learning. Ablations systematically isolate the contribution of each component: informativeness score alone, redundancy score alone, batch-level diversity constraint, and adaptive β_div schedule.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~600h A100 80GB\",\n      \"gpu_utilization\": \"Low (~20%). GPU idles during implementation of two-stage sampler, embedding-space KNN infrastructure, diversity objective, and analysis of per-component ablations.\",\n      \"timeline\": \"3-4 months\",\n      \"team\": \"1-2 researchers (one ML systems for sampler implementation, one robotics for LIBERO/SimplerEnv evaluation)\",\n      \"estimated_gpu_cost\": \"$900 (600h × ~$1.50/h spot A100 80GB)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~700h A100 80GB\",\n      \"gpu_utilization\": \"Moderate (~55%). Agent queues experiments and auto-generates configs for ablation sweeps; human reviews diversity metrics and batch composition visualizations daily.\",\n      \"timeline\": \"4-6 weeks\",\n      \"team\": \"1 researcher, ~45min/day reviewing experiment results and adjusting λ/β_div sweep ranges\",\n      \"claude_api_cost\": \"$200-300 (~250 conversation turns for implementation, experiment orchestration, and analysis)\",\n      \"estimated_gpu_cost\": \"$1,050 (700h × ~$1.50/h spot A100 80GB)\",\n      \"risk_note\": \"No real-robot experiments; simulation-only results (LIBERO + SimplerEnv) may be sufficient for ICLR but could weaken acceptance at CoRL where real-robot validation is valued.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~1400h A100 80GB (full ablation grid: 5 priority functions × 4 LIBERO suites × 5 data fractions × 3 seeds, plus λ/β_div sweeps and baseline runs)\",\n      \"gpu_utilization\": \"~90%. Agent pipelines experiments continuously; diversity metric computation is CPU-bound and may slightly reduce GPU utilization during batch construction.\",\n      \"timeline\": \"8-14 days with 4-8 A100 GPUs in parallel\",\n      \"team\": \"0 (initial prompt engineering + final review only)\",\n      \"claude_api_cost\": \"$400-600 (~600 conversation turns for end-to-end implementation, experiment orchestration, failure diagnosis, and paper drafting)\",\n      \"estimated_gpu_cost\": \"$2,100 (1400h × ~$1.50/h spot A100 80GB)\",\n      \"speed_bottleneck\": \"GPU count is primary bottleneck. KNN computation and diversity-constrained batch selection are CPU-bound and may require optimization for larger datasets. LIBERO environment rendering is CPU-bound during evaluation rollouts.\",\n      \"risk_note\": \"Cannot run real-robot experiments autonomously. Agent may over-explore λ/β_div combinations without human judgment. Pure simulation scope limits venue acceptance at robotics-focused venues.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (deadline expected ~October 2026 — top-tier ML venue, well-suited for training methodology contributions with systematic empirical analysis)\",\n    \"CoRL 2026 (abstract May 26, paper May 29 — stretch target given major revision scope; only viable if preliminary LIBERO results are strong within ~10 days)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Prioritized Experience Replay (ICLR 2016)\",\n    \"On Data Redundancy in VLA Training (2026)\",\n    \"Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining (ICLR 2025)\",\n    \"Towards Balanced Behavior Cloning from Imbalanced Datasets (Autonomous Robots 2026)\",\n    \"OpenVLA: An Open-Source Vision-Language-Action Model (ICML 2025)\",\n    \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (RSS 2025)\",\n    \"Interactive Post-Training for Vision-Language-Action Models (arXiv 2025)\",\n    \"ALOE: Action-Level Off-Policy Evaluation for VLA Model Post-Training (arXiv 2026)\",\n    \"Curating Demonstrations using Online Experience / Demo-SCORE (RSS 2025)\",\n    \"SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026)\",\n    \"CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)\",\n    \"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (2025)\",\n    \"Quality over Quantity: Demonstration Curation via Influence Functions (arXiv 2026)\",\n    \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (arXiv 2025)\",\n    \"Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning (arXiv 2026)\",\n    \"Prioritized Replay for RL Post-training (arXiv 2026)\",\n    \"ExpReS-VLA: Specializing VLAs Through Experience Replay and Retrieval (arXiv 2025)\",\n    \"Submodular Batch Selection for Training Deep Neural Networks (IJCAI 2019)\",\n    \"Self-Improving VLA Models with Data Generation via Residual RL / PLD (ICLR 2026)\",\n    \"FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models (2025)\",\n    \"LiLAW: Lightweight Learnable Adaptive Weighting (2025)\",\n    \"PIER/ASkDAgger: Active Skill-level Data Aggregation (2025)\",\n    \"GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation (2025)\"\n  ],\n  \"description\": \"We introduce DADS (Diversity-Aware Dynamic Sampling), a method that addresses the fundamental diversity-difficulty tradeoff in VLA behavioral cloning training. Recent evidence ('On Data Redundancy in VLA Training', 2026) shows that difficulty-based demonstration selection actively hurts VLA performance by sacrificing diversity, while random sampling wastes compute on the >95% redundant data typical in VLA datasets. DADS resolves this tension through a dual-score priority function that couples per-chunk informativeness (action prediction loss) with a redundancy penalty (embedding-space similarity to other mastered chunks), ensuring that sampling focuses on genuinely informative demonstrations without losing coverage. A batch-level diversity constraint via facility-location maximization over observation embeddings guarantees that each training batch covers diverse manipulation behaviors. An adaptive diversity schedule starts near-uniform (when loss estimates are unreliable) and progressively allows more loss-driven focus as the model's competence estimates become calibrated. Unlike Dynamic Loss-Based Sample Reweighting (ICLR 2025), which operates at the text-token level without diversity preservation, DADS is designed for the action-chunk granularity and multi-modal structure of VLA architectures. Unlike Demo-SCORE's iterative curation, DADS requires no environment rollouts. Unlike SCIZOR and CUPID's static/one-pass curation, DADS adapts continuously as the model learns. Evaluation on LIBERO (4 suites) and SimplerEnv targets both absolute success rate gains and 2-4× data efficiency improvements, with systematic ablations characterizing when each component (informativeness, redundancy, batch diversity, adaptive schedule) contributes most — providing broader insight into optimal sampling strategies for VLA training.\",\n  \"project_name\": \"diversity_aware_sampling_vla\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 2)\nIssues: [\"CRITICAL — False gap claim: The paper claims 'No existing method performs dynamic, within-training demonstration sampling for VLA BC that explicitly preserves diversity while adapting to model competence.' This is demonstrably false. GLISTER-Online (AAAI 2021) performs online submodular data selection during training with convergence guarantees. CRAIG (ICML 2020) performs online facility-location coreset selection during SGD. UDS (ICML, Zou et al. 2025) performs utility-diversity aware online batch selection during LLM supervised fine-tuning with a combined s_total = s_intra + α·s_inter score. The gap as stated does not exist.\", \"CRITICAL — Major missing related work: The proposal fails to cite at least 7 highly relevant papers: (1) UDS: Utility-Diversity Aware Online Batch Selection (ICML) — combines utility + diversity for online batch selection during SFT, nearly identical framework to DADS; (2) D2 Pruning (ICLR 2024) — balances diversity and difficulty via graph-based message passing; (3) InfoMax (ICLR 2025) — information maximization for data pruning balancing importance and redundancy; (4) D3 (IJCAI 2025) — diversity, difficulty, and dependability-aware data selection; (5) GLISTER-Online (AAAI 2021) — online adaptive submodular selection during training; (6) CRAIG (ICML 2020) — facility-location online coreset selection; (7) Robot Data Curation with Mutual Information Estimators (RSS 2026, Hejna et al.) — embedding-based demonstration quality estimation for robotics.\", \"CRITICAL — Component assembly, not methodological innovation: DADS's dual-score priority = PER loss priority + embedding-similarity redundancy penalty (variants exist in D2 Pruning, InfoMax). DADS's batch-level diversity = facility-location submodular function (CRAIG, IJCAI 2019 Submodular Batch Selection). DADS's adaptive schedule = standard annealing. The combination of these components for online training already exists in UDS and the CORDS ecosystem. The VLA-specific contribution (action-chunk granularity, VLA embeddings) is an application choice, not a methodological advance.\", \"The motivating paper 'On Data Redundancy in VLA Training' appears to be a workshop paper (ICRA 2026 workshop 'From Data to Decisions'), not a main-venue peer-reviewed publication. Building the entire research motivation on unreviewed workshop findings is risky — the 95% redundancy claim and TSS underperformance results may not generalize.\", \"CoRL 2026 timeline is unrealistic: abstract deadline is ~11-12 days away (May 25-26), and the paper has fundamental positioning problems requiring substantial rewrite. The risk_note correctly flags simulation-only concerns but underestimates the timeline problem.\", \"The 'convergence analysis showing this schedule is optimal under mild assumptions about loss calibration rate' is hand-waved with no detail. What are the mild assumptions? How does this compare to existing convergence analyses for online submodular selection (CRAIG, GLISTER)? This claimed theoretical contribution needs substance.\", \"DemoSpeedup (CoRL 2025) performs entropy-guided frame-level selection within demonstrations for visuomotor training — related work that should be cited as it operates at sub-trajectory granularity similar to DADS's action-chunk level.\"]\nFeedback: This revision significantly improved the approach (dual-score priority, batch diversity, adaptive schedule) but fundamentally mischaracterizes the novelty landscape. Here are the required actions:\n\n1. **Completely rewrite the gap claim and landscape.** You MUST cite and position against: (a) UDS (ICML, Zou et al.) — the closest competitor, doing online utility-diversity batch selection for SFT. Explain why VLA BC requires something different from UDS's nuclear-norm utility + Euclidean diversity. (b) GLISTER-Online and CRAIG — both do online submodular/facility-location selection during training with convergence guarantees. Explain what fails when you apply these directly to VLA BC. (c) D2 Pruning and InfoMax — both combine diversity with difficulty for data pruning. Explain why their pre-training approach is insufficient AND why your combination differs from theirs.\n\n2. **Identify a genuinely VLA-specific failure mode.** The current framing ('diversity matters for VLA') is too generic — it's equally true for any learning task. What is it about VLA BC specifically (action-chunk temporal coherence? multi-modal observation-action pairing? cross-task transfer in manipulation?) that makes existing general-purpose diversity-aware selection methods fail? Run GLISTER-Online or CRAIG on LIBERO as baselines — if they fail, that's your motivation; if they work, your contribution narrows to engineering.\n\n3. **Elevate from component assembly to insight.** Consider: (a) A theoretical analysis of WHY the diversity-difficulty tradeoff manifests differently in action-chunked BC than in token-level LLM training (temporal correlations between chunks? action space geometry?). (b) An empirical study comparing multiple diversity-aware selection methods (UDS, GLISTER, CRAIG, D2-style) on VLA BC, revealing which components matter and why. This 'understanding' contribution could be stronger than yet another combined method.\n\n4. **Drop CoRL 2026.** With these fundamental positioning issues, 11-15 days is impossible. Target ICLR 2027 (October deadline) and use the time to run proper baselines including existing diversity-aware methods.\n\n5. **Strengthen the theoretical contribution.** Either provide the convergence analysis in detail (with explicit assumptions and comparison to CRAIG/GLISTER bounds) or drop the claim. Hand-waved theory is worse than no theory at a top venue.\n\n6. **Add the RSS 2026 MI curation paper (Hejna et al.) and DemoSpeedup (CoRL 2025) to related work.** Both operate in the robotics demonstration curation space with embedding-based quality metrics.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\")."
}
```

---

### Runtime record

_source line 2 · 2026-05-14T03:20:40.093Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T03:20:40.093Z",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

## Round 1

103 recorded events

### User

_source line 3 · 2026-05-14T03:20:40.139Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-14 (UTC).**

## Original idea
{
  "title": "Beyond Difficulty: Diversity-Aware Dynamic Sampling for Data-Efficient VLA Training",
  "core_problem": "VLA behavioral cloning datasets contain massive redundancy — recent work ('On Data Redundancy in VLA Training', 2026) shows VLAs can train on as little as 5% of LIBERO data with minimal performance loss. Yet naive difficulty-based subsampling (e.g., Temporal Surprise Score) actively hurts performance by sacrificing diversity (SmolVLA: 56.25% vs 60.50% random, GR00T: 74.00% vs 81.33% random). Meanwhile, uniform random sampling wastes compute on redundant data. The fundamental tension is: how to reduce redundancy and focus on informative demonstrations WITHOUT losing the diversity that VLA training critically depends on. Existing curation methods either operate pre-training (SCIZOR, CUPID, DataMIL, QoQ) — meaning they cannot adapt their curation to the model's evolving competence — or require expensive environment rollouts for iterative re-curation (Demo-SCORE). No existing method dynamically adjusts what is considered 'redundant' vs. 'informative' during BC training while explicitly preserving demonstration diversity.",
  "opportunity": "The 'On Data Redundancy' finding reveals a key insight: what matters for VLA training is not example difficulty but coverage across diverse manipulation behaviors. Random subsampling works well precisely because it implicitly preserves diversity while reducing redundancy. This suggests a principled approach: explicitly maintain diversity while dynamically identifying and downweighting redundant demonstrations based on the model's evolving competence. This is distinct from both PER-style loss-proportional sampling (which sacrifices diversity, as shown empirically) and static curation (which cannot adapt to the model's learning state). The opportunity is uniquely ripe because: (1) VLA architectures (OpenVLA-OFT, SmolVLA) provide rich vision-language embeddings that can measure demonstration diversity without additional models, (2) Dynamic Loss-Based Sample Reweighting (ICLR 2025) proved dynamic reweighting works for LLM pretraining but only at token level for text — the multi-modal, action-chunked setting of VLA BC introduces fundamentally different diversity and redundancy structures, and (3) the growing scale of robot demonstration datasets (Open X-Embodiment) makes training efficiency increasingly critical.",
  "landscape": "**Dynamic reweighting for pretraining**: Dynamic Loss-Based Sample Reweighting (ICLR 2025) performs instance-level loss-based reweighting during LLM pretraining with theoretical convergence guarantees. However, it operates at the text token level, does not address multi-modal observation-action pairs, and includes no diversity preservation mechanism — making it inapplicable when diversity loss is the primary failure mode (as in VLA BC). LiLAW (2025) uses three learnable parameters for adaptive sample difficulty weighting but lacks the coverage guarantee needed for multi-task VLA training.\n\n**Static/iterative demonstration curation**: SCIZOR (ICRA 2026) uses self-supervised progress prediction and embedding clustering to remove suboptimal and redundant data, achieving ~15% improvement — but curation is performed once before training and cannot adapt as the model learns. CUPID (CoRL 2025) uses influence functions to estimate each demonstration's causal impact on policy performance — a sophisticated one-pass method that captures policy-level effects but requires a fixed policy checkpoint. Demo-SCORE (RSS 2025) performs iterative curation via train→rollout→classify→re-filter cycles, genuinely adapting to model competence — but requires environment rollouts at each iteration, making it expensive and inapplicable without a simulator. DataMIL (2025) is a policy-driven framework using datamodels for end-to-end selection, operating via validation loss as a surrogate — effective but still a pre-training selection method. QoQ (2026) uses influence functions with trajectory-wise aggregation for sample-level curation. FT-NCFM (2025) goes beyond selection to data distillation/synthesis.\n\n**VLA-specific data insights**: 'On Data Redundancy in VLA Training' (2026) is the most directly relevant work, showing that (a) LIBERO data is >95% redundant for VLA fine-tuning, and (b) difficulty-based coresets (TSS) underperform random subsampling because they sacrifice diversity. This establishes that diversity preservation is essential for any sampling strategy — a constraint that pure loss-based methods (PER, Dynamic Reweighting) do not satisfy.\n\n**Balanced BC and reweighting**: 'Towards Balanced Behavior Cloning from Imbalanced Datasets' (Autonomous Robots 2026) proves that imbalanced data leads to imbalanced policies and proposes meta-gradient rebalancing. This addresses subtask imbalance (e.g., 90% reaching, 10% grasping) but not within-subtask redundancy or dynamic competence adaptation.\n\n**PER variants for LLM/VLM**: Freshness-Aware PER (April 2026) shows standard PER fails on LLMs due to priority staleness and proposes age-decay corrections — but only for RL post-training, not BC. Prioritized Replay for RL Post-training (Jan 2026) operates at problem-level granularity in RL, not within BC training. ExpReS-VLA (Nov 2025) uses prioritized experience replay for VLA domain adaptation / continual learning, not pre-training curation.\n\n**Robotic RL with filtering**: GR-RL (2025) is a dexterous manipulation framework that includes demo trajectory filtering via offline RL Q-values as one component of a larger pipeline, not a general curation method. RIPT-VLA (2025) uses advantage-based rollout filtering during RL post-training, achieving strong results (97.5% on LIBERO) but addressing a different training phase.\n\n**The gap**: No existing method performs dynamic, within-training demonstration sampling for VLA BC that explicitly preserves diversity while adapting to model competence. Static methods cannot adapt; iterative methods require rollouts; loss-only dynamic methods sacrifice diversity; RL post-training methods address a different phase.",
  "approach": "We propose DADS (Diversity-Aware Dynamic Sampling), which replaces uniform data sampling in VLA behavioral cloning with a two-stage sampling strategy that couples informativeness (loss-based) with coverage (embedding diversity) at the action-chunk level.\n\n**Dual-Score Priority Function**: Each action chunk i receives a priority score updated every k gradient steps:\n- Informativeness: info_i = L_i (model's current loss on chunk i)\n- Redundancy: red_i = (1/K) Σ_{j ∈ KNN(i)} σ(-L_j) · sim(e_i, e_j), measuring average similarity to K nearest mastered (low-loss) neighbors in the VLA's frozen vision-language embedding space\n- Priority: p_i = info_i / (1 + λ · red_i)\n\nThis distinguishes three types of chunks: (1) redundant-mastered (low loss, high similarity to other low-loss chunks → low priority), (2) informative (high loss, diverse from mastered chunks → high priority), and (3) noisy/outlier (high loss, but also high redundancy among other high-loss chunks → moderate priority, prevented from dominating). This directly resolves the failure mode identified in 'On Data Redundancy': difficulty-only selection (TSS) conflates types 2 and 3, losing type-1 diversity.\n\n**Batch-Level Diversity Constraint**: For each training batch, we use a two-stage construction: (1) sample m × batch_size candidates weighted by priorities from a sum-tree, (2) greedily select the final batch_size items maximizing: Σ p_i + β_div · FL(S), where FL(S) is the facility-location function over observation embeddings of selected set S, ensuring each batch covers diverse state-action regions. This is efficient: O(m·B·log N) for candidate sampling, O(m²·B·d) for greedy diversity selection.\n\n**Adaptive Diversity Schedule**: β_div is annealed from high to low during training. Early in training, when the model's loss landscape is poorly calibrated, we emphasize diversity (near-uniform over diverse modes). As training progresses and loss estimates become reliable discriminators of genuine difficulty vs. noise, we reduce β_div to allow more focus on remaining hard demonstrations. We provide a convergence analysis showing this schedule is optimal under mild assumptions about loss calibration rate.\n\n**Action-Chunk Granularity**: Unlike token-level reweighting (Dynamic Loss-Based Reweighting, ICLR 2025) which treats each text token independently, DADS operates at the action-chunk level — the natural prediction unit of VLA architectures. Action chunks exhibit spatial/temporal coherence within chunks but high variance across chunks (e.g., a reaching chunk vs. a grasping chunk), making chunk-level priorities more semantically meaningful than token-level. Unlike trajectory-level curation (Demo-SCORE, CUPID), chunk-level granularity allows fine-grained within-trajectory importance variation.\n\n**Implementation**: DADS is implemented as a drop-in PyTorch DistributedSampler compatible with OpenVLA-OFT and SmolVLA training pipelines. Priority scores are maintained in a sum-tree with O(log N) updates. Embeddings are computed from the VLA's frozen vision-language encoder (no additional model). KNN is precomputed once in embedding space and reused; only loss-based scores are refreshed every k steps. Overhead is ~10-15% over standard training.\n\n**Evaluation**: LIBERO (all 4 suites: Spatial, Object, Goal, Long) as the primary benchmark — directly comparable to 'On Data Redundancy' results — plus SimplerEnv for breadth. We measure: (1) absolute success rate improvement over uniform and random-subsampling baselines, (2) data efficiency curves at 5%, 10%, 25%, 50%, 100% of training data, (3) training efficiency (wall-clock time to reach target success rate). Baselines include: uniform sampling, random subsampling (strong baseline per 'On Data Redundancy'), TSS difficulty-based selection, loss-only prioritization (PER-style, expected to underperform due to diversity loss), Dynamic Loss-Based Reweighting (adapted to action chunks), SCIZOR, and standard curriculum learning. Ablations systematically isolate the contribution of each component: informativeness score alone, redundancy score alone, batch-level diversity constraint, and adaptive β_div schedule.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~600h A100 80GB",
      "gpu_utilization": "Low (~20%). GPU idles during implementation of two-stage sampler, embedding-space KNN infrastructure, diversity objective, and analysis of per-component ablations.",
      "timeline": "3-4 months",
      "team": "1-2 researchers (one ML systems for sampler implementation, one robotics for LIBERO/SimplerEnv evaluation)",
      "estimated_gpu_cost": "$900 (600h × ~$1.50/h spot A100 80GB)"
    },
    "human_in_loop": {
      "gpu_hours": "~700h A100 80GB",
      "gpu_utilization": "Moderate (~55%). Agent queues experiments and auto-generates configs for ablation sweeps; human reviews diversity metrics and batch composition visualizations daily.",
      "timeline": "4-6 weeks",
      "team": "1 researcher, ~45min/day reviewing experiment results and adjusting λ/β_div sweep ranges",
      "claude_api_cost": "$200-300 (~250 conversation turns for implementation, experiment orchestration, and analysis)",
      "estimated_gpu_cost": "$1,050 (700h × ~$1.50/h spot A100 80GB)",
      "risk_note": "No real-robot experiments; simulation-only results (LIBERO + SimplerEnv) may be sufficient for ICLR but could weaken acceptance at CoRL where real-robot validation is valued."
    },
    "auto_research": {
      "gpu_hours": "~1400h A100 80GB (full ablation grid: 5 priority functions × 4 LIBERO suites × 5 data fractions × 3 seeds, plus λ/β_div sweeps and baseline runs)",
      "gpu_utilization": "~90%. Agent pipelines experiments continuously; diversity metric computation is CPU-bound and may slightly reduce GPU utilization during batch construction.",
      "timeline": "8-14 days with 4-8 A100 GPUs in parallel",
      "team": "0 (initial prompt engineering + final review only)",
      "claude_api_cost": "$400-600 (~600 conversation turns for end-to-end implementation, experiment orchestration, failure diagnosis, and paper drafting)",
      "estimated_gpu_cost": "$2,100 (1400h × ~$1.50/h spot A100 80GB)",
      "speed_bottleneck": "GPU count is primary bottleneck. KNN computation and diversity-constrained batch selection are CPU-bound and may require optimization for larger datasets. LIBERO environment rendering is CPU-bound during evaluation rollouts.",
      "risk_note": "Cannot run real-robot experiments autonomously. Agent may over-explore λ/β_div combinations without human judgment. Pure simulation scope limits venue acceptance at robotics-focused venues."
    }
  },
  "target_venues": [
    "ICLR 2027 (deadline expected ~October 2026 — top-tier ML venue, well-suited for training methodology contributions with systematic empirical analysis)",
    "CoRL 2026 (abstract May 26, paper May 29 — stretch target given major revision scope; only viable if preliminary LIBERO results are strong within ~10 days)"
  ],
  "level": "solid",
  "key_references": [
    "Prioritized Experience Replay (ICLR 2016)",
    "On Data Redundancy in VLA Training (2026)",
    "Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining (ICLR 2025)",
    "Towards Balanced Behavior Cloning from Imbalanced Datasets (Autonomous Robots 2026)",
    "OpenVLA: An Open-Source Vision-Language-Action Model (ICML 2025)",
    "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (RSS 2025)",
    "Interactive Post-Training for Vision-Language-Action Models (arXiv 2025)",
    "ALOE: Action-Level Off-Policy Evaluation for VLA Model Post-Training (arXiv 2026)",
    "Curating Demonstrations using Online Experience / Demo-SCORE (RSS 2025)",
    "SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026)",
    "CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)",
    "DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (2025)",
    "Quality over Quantity: Demonstration Curation via Influence Functions (arXiv 2026)",
    "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (arXiv 2025)",
    "Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning (arXiv 2026)",
    "Prioritized Replay for RL Post-training (arXiv 2026)",
    "ExpReS-VLA: Specializing VLAs Through Experience Replay and Retrieval (arXiv 2025)",
    "Submodular Batch Selection for Training Deep Neural Networks (IJCAI 2019)",
    "Self-Improving VLA Models with Data Generation via Residual RL / PLD (ICLR 2026)",
    "FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models (2025)",
    "LiLAW: Lightweight Learnable Adaptive Weighting (2025)",
    "PIER/ASkDAgger: Active Skill-level Data Aggregation (2025)",
    "GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation (2025)"
  ],
  "description": "We introduce DADS (Diversity-Aware Dynamic Sampling), a method that addresses the fundamental diversity-difficulty tradeoff in VLA behavioral cloning training. Recent evidence ('On Data Redundancy in VLA Training', 2026) shows that difficulty-based demonstration selection actively hurts VLA performance by sacrificing diversity, while random sampling wastes compute on the >95% redundant data typical in VLA datasets. DADS resolves this tension through a dual-score priority function that couples per-chunk informativeness (action prediction loss) with a redundancy penalty (embedding-space similarity to other mastered chunks), ensuring that sampling focuses on genuinely informative demonstrations without losing coverage. A batch-level diversity constraint via facility-location maximization over observation embeddings guarantees that each training batch covers diverse manipulation behaviors. An adaptive diversity schedule starts near-uniform (when loss estimates are unreliable) and progressively allows more loss-driven focus as the model's competence estimates become calibrated. Unlike Dynamic Loss-Based Sample Reweighting (ICLR 2025), which operates at the text-token level without diversity preservation, DADS is designed for the action-chunk granularity and multi-modal structure of VLA architectures. Unlike Demo-SCORE's iterative curation, DADS requires no environment rollouts. Unlike SCIZOR and CUPID's static/one-pass curation, DADS adapts continuously as the model learns. Evaluation on LIBERO (4 suites) and SimplerEnv targets both absolute success rate gains and 2-4× data efficiency improvements, with systematic ablations characterizing when each component (informativeness, redundancy, batch diversity, adaptive schedule) contributes most — providing broader insight into optimal sampling strategies for VLA training.",
  "project_name": "diversity_aware_sampling_vla",
  "source": "web_research"
}

## Reviewer feedback (round 2)
Issues: ["CRITICAL — False gap claim: The paper claims 'No existing method performs dynamic, within-training demonstration sampling for VLA BC that explicitly preserves diversity while adapting to model competence.' This is demonstrably false. GLISTER-Online (AAAI 2021) performs online submodular data selection during training with convergence guarantees. CRAIG (ICML 2020) performs online facility-location coreset selection during SGD. UDS (ICML, Zou et al. 2025) performs utility-diversity aware online batch selection during LLM supervised fine-tuning with a combined s_total = s_intra + α·s_inter score. The gap as stated does not exist.", "CRITICAL — Major missing related work: The proposal fails to cite at least 7 highly relevant papers: (1) UDS: Utility-Diversity Aware Online Batch Selection (ICML) — combines utility + diversity for online batch selection during SFT, nearly identical framework to DADS; (2) D2 Pruning (ICLR 2024) — balances diversity and difficulty via graph-based message passing; (3) InfoMax (ICLR 2025) — information maximization for data pruning balancing importance and redundancy; (4) D3 (IJCAI 2025) — diversity, difficulty, and dependability-aware data selection; (5) GLISTER-Online (AAAI 2021) — online adaptive submodular selection during training; (6) CRAIG (ICML 2020) — facility-location online coreset selection; (7) Robot Data Curation with Mutual Information Estimators (RSS 2026, Hejna et al.) — embedding-based demonstration quality estimation for robotics.", "CRITICAL — Component assembly, not methodological innovation: DADS's dual-score priority = PER loss priority + embedding-similarity redundancy penalty (variants exist in D2 Pruning, InfoMax). DADS's batch-level diversity = facility-location submodular function (CRAIG, IJCAI 2019 Submodular Batch Selection). DADS's adaptive schedule = standard annealing. The combination of these components for online training already exists in UDS and the CORDS ecosystem. The VLA-specific contribution (action-chunk granularity, VLA embeddings) is an application choice, not a methodological advance.", "The motivating paper 'On Data Redundancy in VLA Training' appears to be a workshop paper (ICRA 2026 workshop 'From Data to Decisions'), not a main-venue peer-reviewed publication. Building the entire research motivation on unreviewed workshop findings is risky — the 95% redundancy claim and TSS underperformance results may not generalize.", "CoRL 2026 timeline is unrealistic: abstract deadline is ~11-12 days away (May 25-26), and the paper has fundamental positioning problems requiring substantial rewrite. The risk_note correctly flags simulation-only concerns but underestimates the timeline problem.", "The 'convergence analysis showing this schedule is optimal under mild assumptions about loss calibration rate' is hand-waved with no detail. What are the mild assumptions? How does this compare to existing convergence analyses for online submodular selection (CRAIG, GLISTER)? This claimed theoretical contribution needs substance.", "DemoSpeedup (CoRL 2025) performs entropy-guided frame-level selection within demonstrations for visuomotor training — related work that should be cited as it operates at sub-trajectory granularity similar to DADS's action-chunk level."]
Feedback: This revision significantly improved the approach (dual-score priority, batch diversity, adaptive schedule) but fundamentally mischaracterizes the novelty landscape. Here are the required actions:

1. **Completely rewrite the gap claim and landscape.** You MUST cite and position against: (a) UDS (ICML, Zou et al.) — the closest competitor, doing online utility-diversity batch selection for SFT. Explain why VLA BC requires something different from UDS's nuclear-norm utility + Euclidean diversity. (b) GLISTER-Online and CRAIG — both do online submodular/facility-location selection during training with convergence guarantees. Explain what fails when you apply these directly to VLA BC. (c) D2 Pruning and InfoMax — both combine diversity with difficulty for data pruning. Explain why their pre-training approach is insufficient AND why your combination differs from theirs.

2. **Identify a genuinely VLA-specific failure mode.** The current framing ('diversity matters for VLA') is too generic — it's equally true for any learning task. What is it about VLA BC specifically (action-chunk temporal coherence? multi-modal observation-action pairing? cross-task transfer in manipulation?) that makes existing general-purpose diversity-aware selection methods fail? Run GLISTER-Online or CRAIG on LIBERO as baselines — if they fail, that's your motivation; if they work, your contribution narrows to engineering.

3. **Elevate from component assembly to insight.** Consider: (a) A theoretical analysis of WHY the diversity-difficulty tradeoff manifests differently in action-chunked BC than in token-level LLM training (temporal correlations between chunks? action space geometry?). (b) An empirical study comparing multiple diversity-aware selection methods (UDS, GLISTER, CRAIG, D2-style) on VLA BC, revealing which components matter and why. This 'understanding' contribution could be stronger than yet another combined method.

4. **Drop CoRL 2026.** With these fundamental positioning issues, 11-15 days is impossible. Target ICLR 2027 (October deadline) and use the time to run proper baselines including existing diversity-aware methods.

5. **Strengthen the theoretical contribution.** Either provide the convergence analysis in detail (with explicit assumptions and comparison to CRAIG/GLISTER bounds) or drop the claim. Hand-waved theory is worse than no theory at a top venue.

6. **Add the RSS 2026 MI curation paper (Hejna et al.) and DemoSpeedup (CoRL 2025) to related work.** Both operate in the robotics demonstration curation space with embedding-based quality metrics.

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
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "b5097684-eca7-409c-85ec-aa7a4e8edd0c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T03:20:40.136Z_

```json
{
  "parentUuid": "b5097684-eca7-409c-85ec-aa7a4e8edd0c",
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
  "uuid": "2510ddee-87b3-44d6-bb0f-87d2451ec931",
  "timestamp": "2026-05-14T03:20:40.136Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T03:20:40.136Z_

```json
{
  "parentUuid": "2510ddee-87b3-44d6-bb0f-87d2451ec931",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8414b176-79c4-4fb9-91e8-fbc8b93ca73a",
  "timestamp": "2026-05-14T03:20:40.136Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Beyond Difficulty: Diversity-Aware Dynamic Sampling for Data-Efficient…",
  "leafUuid": "8414b176-79c4-4fb9-91e8-fbc8b93ca73a",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Benchmark diversity-aware selection methods on VLA BC",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Assistant

_source line 8 · 2026-05-14T03:20:59.110Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully before diving into research. The reviewers have identified several critical issues:

1. **False gap claim** - The claim that no existing method does dynamic, within-training diversity-aware sampling is wrong. UDS, GLISTER-Online, and CRAIG all do this.

2. **Major missing related work** - 7+ papers not cited, especially UDS which is nearly identical to DADS.

3. **Component assembly, not innovation** - DADS is just combining known components (PER + embedding similarity + facility location + annealing) without genuine methodological novelty.


4. **Weak theoretical foundation** - The workshop paper motivation is questionable, the CoRL timeline doesn't hold up, and the convergence analysis lacks rigor. There are also several missing citations including DemoSpeedup and the RSS 2026 MI curation paper.

The core problem is stark: the claimed gap doesn't actually exist, the method is essentially a recombination of existing techniques, and UDS already does nearly the same thing. This points toward needing a substantial rethinking of the work, possibly a complete pivot.

Before I can chart a path forward, I need to understand what's genuinely novel about VLA BC. The key is figuring out what UDS actually does and how it compares to DADS, what makes VLA BC fundamentally different from standard LLM fine-tuning approaches, and whether there's a deeper principle I'm missing. I should dig into the papers the reviewers flagged—UDS, GLISTER-Online, CRAIG, D2 Pruning, InfoMax, the RSS 2026 mutual information paper on robot data curation, and DemoSpeedup from CoRL 2025—to understand the landscape properly.

Now I'm looking at D3 as a framework combining diversity, difficulty, and dependability—this could be the conceptual anchor I need to ground the approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8414b176-79c4-4fb9-91e8-fbc8b93ca73a",
  "isSidechain": false,
  "requestId": "req_011Cb1jwVZcHrovp6i8Kz9oN",
  "type": "assistant",
  "uuid": "03426166-1288-44e4-8065-3b20d75bc7fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011891cU8YRYNXAXFqGDurT9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12131,
      "cache_read_input_tokens": 11841,
      "output_tokens": 658,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12131,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 658,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12131
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

_source line 9 · 2026-05-14T03:20:59.162Z_

I'll start by deeply researching the papers the reviewers flagged as missing, then reconsider the entire framing. Let me search for the key works in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03426166-1288-44e4-8065-3b20d75bc7fd",
  "isSidechain": false,
  "requestId": "req_011Cb1jwVZcHrovp6i8Kz9oN",
  "type": "assistant",
  "uuid": "934d9cc7-cb52-4526-89de-815ebb82659e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011891cU8YRYNXAXFqGDurT9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12131,
      "cache_read_input_tokens": 11841,
      "output_tokens": 658,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12131,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 658,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12131
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

_source line 10 · 2026-05-14T03:20:59.534Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013T1HgrDd2TV5K4xWkcTa9j`</summary>

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
  "parentUuid": "934d9cc7-cb52-4526-89de-815ebb82659e",
  "isSidechain": false,
  "requestId": "req_011Cb1jwVZcHrovp6i8Kz9oN",
  "type": "assistant",
  "uuid": "25647ef2-5a07-4592-9a35-754943f0d786",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011891cU8YRYNXAXFqGDurT9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12131,
      "cache_read_input_tokens": 11841,
      "output_tokens": 658,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12131,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 658,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12131
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

_source line 11 · 2026-05-14T03:20:59.545Z_

<details><summary>↩ Tool result · `toolu_013T1HgrDd2TV5K4xWkcTa9j`</summary>

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
  "parentUuid": "25647ef2-5a07-4592-9a35-754943f0d786",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "e6469caf-120d-4230-9651-459190c7542a",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "25647ef2-5a07-4592-9a35-754943f0d786",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-14T03:21:04.355Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now search for all the key papers the reviewers mentioned in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6469caf-120d-4230-9651-459190c7542a",
  "isSidechain": false,
  "requestId": "req_011Cb1jxvnghL71oy91jF497",
  "type": "assistant",
  "uuid": "c7c41764-64cf-4fd4-aec1-f48c0b71d8e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bW8wWt2QosFm2qzLxd5dd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1676,
      "cache_read_input_tokens": 23972,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1676,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 23972,
          "cache_creation_input_tokens": 1676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1676
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

_source line 13 · 2026-05-14T03:21:04.821Z_

Let me search for all the critical missing papers the reviewers identified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7c41764-64cf-4fd4-aec1-f48c0b71d8e7",
  "isSidechain": false,
  "requestId": "req_011Cb1jxvnghL71oy91jF497",
  "type": "assistant",
  "uuid": "582dc34a-5538-46c0-b31c-e1d948af6949",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bW8wWt2QosFm2qzLxd5dd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1676,
      "cache_read_input_tokens": 23972,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1676,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 23972,
          "cache_creation_input_tokens": 1676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1676
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

_source line 14 · 2026-05-14T03:21:05.491Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015VKvZnJVvCHXe9CvHiKdTj`</summary>

```json
{
  "query": "UDS Utility-Diversity Aware Online Batch Selection ICML Zou 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "582dc34a-5538-46c0-b31c-e1d948af6949",
  "isSidechain": false,
  "requestId": "req_011Cb1jxvnghL71oy91jF497",
  "type": "assistant",
  "uuid": "9af81036-190b-4550-8144-5c7c1e6d17f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bW8wWt2QosFm2qzLxd5dd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1676,
      "cache_read_input_tokens": 23972,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1676,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 23972,
          "cache_creation_input_tokens": 1676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1676
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

_source line 15 · 2026-05-14T03:21:12.468Z_

<details><summary>↩ Tool result · `toolu_015VKvZnJVvCHXe9CvHiKdTj`</summary>

```text
Web search results for query: "UDS Utility-Diversity Aware Online Batch Selection ICML Zou 2025"

Links: [{"title":"GitHub - gfyddha/UDS: Official implementation of our paper: \"Utility-Diversity Aware Online Batch Selection for LLM Supervised Fine-tuning.\" · GitHub","url":"https://github.com/gfyddha/UDS"},{"title":"[2510.16882] Utility-Diversity Aware Online Batch Selection for LLM Supervised Fine-tuning","url":"https://arxiv.org/abs/2510.16882"},{"title":"Utility-Diversity Aware Online Batch Selection for LLM Supervised Fine-tuning","url":"https://arxiv.org/html/2510.16882"},{"title":"Utility-Diversity Aware Online Batch Selection for LLM ...","url":"https://www.arxiv.org/pdf/2510.16882"},{"title":"UTILITY-DIVERSITY AWARE ONLINE BATCH SELEC","url":"https://openreview.net/pdf/23f1c52237c77369d7eb2bf3c414815adaac14e2.pdf"},{"title":"ICML 2025 Papers","url":"https://icml.cc/virtual/2025/papers.html"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"ICML 2026","url":"https://icml.cc/"},{"title":"ICML 2025 Workshops","url":"https://icml.cc/virtual/2025/events/workshop"},{"title":"Downloads 2024","url":"https://icml.cc/Downloads/2024"}]

Based on the search results, here's information about the UDS (Utility-Diversity Aware Online Batch Selection) paper:

## Paper Overview

The paper is titled "Utility-Diversity Aware Online Batch Selection for LLM Supervised Fine-tuning" by Heming Zou, Yixiu Mao, Yun Qu, Qi Wang, and Xiangyang Ji, published as an arXiv preprint (arXiv:2510.16882).

## Problem and Motivation

The paper addresses supervised fine-tuning (SFT) of large language models, which is computationally expensive and can suffer from overfitting or bias amplification, motivating the need for data curation that prioritizes the most valuable data.

## Technical Approach

UDS leverages the nuclear norm of the logits matrix to capture both data utility and intra-sample diversity, while estimating inter-sample diversity through efficient low-dimensional embedding comparisons with a lightweight memory buffer of historical samples. This design eliminates the need for external resources and unnecessary backpropagation, securing computational efficiency.

## Results

Experiments on multiple benchmarks demonstrate that UDS consistently outperforms state-of-the-art online batch selection methods under varying data budgets, and significantly reduces training time compared to full-dataset fine-tuning. The authors provide example scripts for training and evaluating the Qwen-2.5-7B model on the MMLU benchmark using only 12.5% of the training data.

## Code Availability

Code is available at a GitHub repository maintained by the authors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9af81036-190b-4550-8144-5c7c1e6d17f2",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "98cb3cf8-86ef-4010-b277-f682abc84f67",
  "toolUseResult": {
    "query": "UDS Utility-Diversity Aware Online Batch Selection ICML Zou 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TzsF971vsfmqkGPdey499o",
        "content": [
          {
            "title": "GitHub - gfyddha/UDS: Official implementation of our paper: \"Utility-Diversity Aware Online Batch Selection for LLM Supervised Fine-tuning.\" · GitHub",
            "url": "https://github.com/gfyddha/UDS"
          },
          {
            "title": "[2510.16882] Utility-Diversity Aware Online Batch Selection for LLM Supervised Fine-tuning",
            "url": "https://arxiv.org/abs/2510.16882"
          },
          {
            "title": "Utility-Diversity Aware Online Batch Selection for LLM Supervised Fine-tuning",
            "url": "https://arxiv.org/html/2510.16882"
          },
          {
            "title": "Utility-Diversity Aware Online Batch Selection for LLM ...",
            "url": "https://www.arxiv.org/pdf/2510.16882"
          },
          {
            "title": "UTILITY-DIVERSITY AWARE ONLINE BATCH SELEC",
            "url": "https://openreview.net/pdf/23f1c52237c77369d7eb2bf3c414815adaac14e2.pdf"
          },
          {
            "title": "ICML 2025 Papers",
            "url": "https://icml.cc/virtual/2025/papers.html"
          },
          {
            "title": "ICLR 2025 Papers",
            "url": "https://iclr.cc/virtual/2025/papers.html"
          },
          {
            "title": "ICML 2026",
            "url": "https://icml.cc/"
          },
          {
            "title": "ICML 2025 Workshops",
            "url": "https://icml.cc/virtual/2025/events/workshop"
          },
          {
            "title": "Downloads 2024",
            "url": "https://icml.cc/Downloads/2024"
          }
        ]
      },
      "Based on the search results, here's information about the UDS (Utility-Diversity Aware Online Batch Selection) paper:\n\n## Paper Overview\n\nThe paper is titled \"Utility-Diversity Aware Online Batch Selection for LLM Supervised Fine-tuning\" by Heming Zou, Yixiu Mao, Yun Qu, Qi Wang, and Xiangyang Ji, published as an arXiv preprint (arXiv:2510.16882).\n\n## Problem and Motivation\n\nThe paper addresses supervised fine-tuning (SFT) of large language models, which is computationally expensive and can suffer from overfitting or bias amplification, motivating the need for data curation that prioritizes the most valuable data.\n\n## Technical Approach\n\nUDS leverages the nuclear norm of the logits matrix to capture both data utility and intra-sample diversity, while estimating inter-sample diversity through efficient low-dimensional embedding comparisons with a lightweight memory buffer of historical samples. This design eliminates the need for external resources and unnecessary backpropagation, securing computational efficiency.\n\n## Results\n\nExperiments on multiple benchmarks demonstrate that UDS consistently outperforms state-of-the-art online batch selection methods under varying data budgets, and significantly reduces training time compared to full-dataset fine-tuning. The authors provide example scripts for training and evaluating the Qwen-2.5-7B model on the MMLU benchmark using only 12.5% of the training data.\n\n## Code Availability\n\nCode is available at a GitHub repository maintained by the authors."
    ],
    "durationSeconds": 6.971286614
  },
  "sourceToolAssistantUUID": "9af81036-190b-4550-8144-5c7c1e6d17f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T03:21:15.832Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V9cQdR1TXZvSqee716kpvi`</summary>

```json
{
  "query": "GLISTER Online submodular data selection training AAAI 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98cb3cf8-86ef-4010-b277-f682abc84f67",
  "isSidechain": false,
  "requestId": "req_011Cb1jyrTWwaPRxAmkXFyzm",
  "type": "assistant",
  "uuid": "6a376e36-44b4-4147-98ca-b43103a3c004",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017bJt2yZR6S5SM51B46yitx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 925,
      "cache_read_input_tokens": 25648,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 25648,
          "cache_creation_input_tokens": 925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 925
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

_source line 17 · 2026-05-14T03:21:23.142Z_

<details><summary>↩ Tool result · `toolu_01V9cQdR1TXZvSqee716kpvi`</summary>

```text
Web search results for query: "GLISTER Online submodular data selection training AAAI 2021"

Links: [{"title":"GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/16988"},{"title":"GLISTER: Generalization based Data Subset Selection for Efﬁcient and Robust","url":"https://ojs.aaai.org/index.php/AAAI/article/view/16988/16795"},{"title":"GLISTER: Generalization based Data Subset Selection for Efﬁcient and Robust","url":"https://www.cse.iitb.ac.in/~ganesh/papers/aaai2021.pdf"},{"title":"[2012.10630] GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning","url":"https://arxiv.org/abs/2012.10630"},{"title":"GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning - AAAI","url":"https://aaai.org/papers/08110-glister-generalization-based-data-subset-selection-for-efficient-and-robust-learning/"},{"title":"GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning - NASA/ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv201210630K/abstract"},{"title":"[PDF] GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GLISTER:-Generalization-based-Data-Subset-Selection-Killamsetty-Sivasubramanian/199ac333b1ff37917d1ab4a2e2002d9605b3db1e"},{"title":"GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning | Request PDF","url":"https://www.researchgate.net/publication/363394079_GLISTER_Generalization_based_Data_Subset_Selection_for_Efficient_and_Robust_Learning"},{"title":"GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning | DeepAI","url":"https://deepai.org/publication/glister-generalization-based-data-subset-selection-for-efficient-and-robust-learning"},{"title":"(PDF) GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning","url":"https://www.researchgate.net/publication/347534567_GLISTER_Generalization_based_Data_Subset_Selection_for_Efficient_and_Robust_Learning"}]

Based on the search results, here's what I found about GLISTER Online submodular data selection training at AAAI 2021:

## Overview

GLISTER is a GeneraLIzation based data Subset selecTion for Efficient and Robust learning framework that formulates data subset selection as a mixed discrete-continuous bi-level optimization problem to select a subset of training data, which maximizes the log-likelihood on a held-out validation set.

## GLISTER-ONLINE Algorithm

GLISTER-Online is an iterative online algorithm which performs data selection iteratively along with the parameter updates and can be applied to any loss-based learning algorithm.

## Submodular Optimization Connection

For a rich class of loss functions including cross-entropy, hinge-loss, squared-loss, and logistic-loss, the inner discrete data selection is an instance of (weakly) submodular optimization, and the paper analyzes conditions for which GLISTER-ONLINE reduces the validation loss and converges.

## Applications and Results

The paper proposes GLISTER-ACTIVE, an extension to batch active learning, and empirically demonstrates the performance of GLISTER on data selection to reduce training time, robust learning under label noise and imbalance settings, and batch-active learning. The framework improves upon the state of the art both in efficiency and accuracy.

The paper was published in the Proceedings of the AAAI Conference on Artificial Intelligence 35 (2021), with the full citation showing it appeared on pages 8110-8118. The code for GLISTER is available on GitHub at https://github.com/dssresearch/GLISTER.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a376e36-44b4-4147-98ca-b43103a3c004",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "82732486-aa96-4817-843a-a55f0644f0a0",
  "toolUseResult": {
    "query": "GLISTER Online submodular data selection training AAAI 2021",
    "results": [
      {
        "tool_use_id": "srvtoolu_01P4sgc3sWEV4vTHthya3Hdd",
        "content": [
          {
            "title": "GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/16988"
          },
          {
            "title": "GLISTER: Generalization based Data Subset Selection for Efﬁcient and Robust",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/16988/16795"
          },
          {
            "title": "GLISTER: Generalization based Data Subset Selection for Efﬁcient and Robust",
            "url": "https://www.cse.iitb.ac.in/~ganesh/papers/aaai2021.pdf"
          },
          {
            "title": "[2012.10630] GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning",
            "url": "https://arxiv.org/abs/2012.10630"
          },
          {
            "title": "GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning - AAAI",
            "url": "https://aaai.org/papers/08110-glister-generalization-based-data-subset-selection-for-efficient-and-robust-learning/"
          },
          {
            "title": "GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning - NASA/ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2020arXiv201210630K/abstract"
          },
          {
            "title": "[PDF] GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GLISTER:-Generalization-based-Data-Subset-Selection-Killamsetty-Sivasubramanian/199ac333b1ff37917d1ab4a2e2002d9605b3db1e"
          },
          {
            "title": "GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning | Request PDF",
            "url": "https://www.researchgate.net/publication/363394079_GLISTER_Generalization_based_Data_Subset_Selection_for_Efficient_and_Robust_Learning"
          },
          {
            "title": "GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning | DeepAI",
            "url": "https://deepai.org/publication/glister-generalization-based-data-subset-selection-for-efficient-and-robust-learning"
          },
          {
            "title": "(PDF) GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning",
            "url": "https://www.researchgate.net/publication/347534567_GLISTER_Generalization_based_Data_Subset_Selection_for_Efficient_and_Robust_Learning"
          }
        ]
      },
      "Based on the search results, here's what I found about GLISTER Online submodular data selection training at AAAI 2021:\n\n## Overview\n\nGLISTER is a GeneraLIzation based data Subset selecTion for Efficient and Robust learning framework that formulates data subset selection as a mixed discrete-continuous bi-level optimization problem to select a subset of training data, which maximizes the log-likelihood on a held-out validation set.\n\n## GLISTER-ONLINE Algorithm\n\nGLISTER-Online is an iterative online algorithm which performs data selection iteratively along with the parameter updates and can be applied to any loss-based learning algorithm.\n\n## Submodular Optimization Connection\n\nFor a rich class of loss functions including cross-entropy, hinge-loss, squared-loss, and logistic-loss, the inner discrete data selection is an instance of (weakly) submodular optimization, and the paper analyzes conditions for which GLISTER-ONLINE reduces the validation loss and converges.\n\n## Applications and Results\n\nThe paper proposes GLISTER-ACTIVE, an extension to batch active learning, and empirically demonstrates the performance of GLISTER on data selection to reduce training time, robust learning under label noise and imbalance settings, and batch-active learning. The framework improves upon the state of the art both in efficiency and accuracy.\n\nThe paper was published in the Proceedings of the AAAI Conference on Artificial Intelligence 35 (2021), with the full citation showing it appeared on pages 8110-8118. The code for GLISTER is available on GitHub at https://github.com/dssresearch/GLISTER."
    ],
    "durationSeconds": 7.305670802000001
  },
  "sourceToolAssistantUUID": "6a376e36-44b4-4147-98ca-b43103a3c004",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T03:21:25.799Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H1F43fnviLrF27YtD32sAX`</summary>

```json
{
  "query": "CRAIG coresets weighted matching facility location online SGD ICML 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82732486-aa96-4817-843a-a55f0644f0a0",
  "isSidechain": false,
  "requestId": "req_011Cb1jze69tAhnLTEDbnhEu",
  "type": "assistant",
  "uuid": "4d958718-c7c3-48dd-8d98-47897cc63c3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011sdsUiCDSoQ3asrpu4vW6R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1163,
      "cache_read_input_tokens": 26573,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 26573,
          "cache_creation_input_tokens": 1163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1163
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

_source line 19 · 2026-05-14T03:21:31.571Z_

<details><summary>↩ Tool result · `toolu_01H1F43fnviLrF27YtD32sAX`</summary>

```text
Web search results for query: "CRAIG coresets weighted matching facility location online SGD ICML 2020"

Links: [{"title":"Coresets for Data-efﬁcient Training of Machine Learning Models","url":"https://cs.stanford.edu/people/jure/pubs/craig-icml20.pdf"},{"title":"Data-efficiency | Baharan Mirzasoleiman","url":"https://baharanm.github.io/projects/data_efficient/"},{"title":"[1906.01827] Coresets for Data-efficient Training of Machine Learning Models","url":"https://arxiv.org/abs/1906.01827"},{"title":"[PDF] Coresets for Data-efficient Training of Machine Learning Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Coresets-for-Data-efficient-Training-of-Machine-Mirzasoleiman-Bilmes/790985a4bee821046992ff3d5322ff11dd1b4262"},{"title":"Coresets for Data-efficient Training of Machine Learning ...","url":"https://icml.cc/media/icml-2020/Slides/6325.pdf"},{"title":"ICML 2020","url":"https://icml.cc/Conferences/2020/ScheduleMultitrack?event=6396"},{"title":"Coresets for data-efficient training of machine learning models | Proceedings of the 37th International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3524938.3525583"},{"title":"GRAD-MATCH: Gradient Matching based Data Subset Selection for Efﬁcient","url":"https://arxiv.org/pdf/2103.00123"},{"title":"GitHub - PatrickZH/Awesome-Coreset-Selection: Awesome coreset/core-set/subset/sample selection works. · GitHub","url":"https://github.com/PatrickZH/Awesome-Coreset-Selection"},{"title":"Coresets for Data-efficient Training of Machine Learning Models","url":"http://proceedings.mlr.press/v119/mirzasoleiman20a/mirzasoleiman20a.pdf"}]

Based on the search results, I found comprehensive information about CRAIG and its publication at ICML 2020:

## Summary of CRAIG (ICML 2020)

CRAIG is a method to select a weighted subset (or coreset) of training data that closely estimates the full gradient by maximizing a submodular function. The method proves that applying incremental gradient (IG) to this subset is guaranteed to converge to the (near)optimal solution with the same convergence rate as that of IG for convex optimization.

CRAIG speeds up various IG methods by up to 6x for logistic regression and 3x for training deep neural networks, while achieving practically the same solution.

The paper was published in the International Conference on Machine Learning (ICML) in 2020 with authors Baharan Mirzasoleiman, Jeff Bilmes, and Jure Leskovec.

### Key Features

CRAIG is a recent coreset algorithm that shows promise for both deep learning and classical machine learning models. Unlike other coreset techniques that largely focus on approximating loss functions, CRAIG selects representative subsets of the training data that closely approximate the full gradient.

The paper addresses a fundamental challenge in machine learning: how to select a training data subset that can theoretically and practically perform on par with the full dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d958718-c7c3-48dd-8d98-47897cc63c3b",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "f79e732b-7683-4681-8937-e6c5889c0ddb",
  "toolUseResult": {
    "query": "CRAIG coresets weighted matching facility location online SGD ICML 2020",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CAgLZBkLicFtU4DqvuKzzT",
        "content": [
          {
            "title": "Coresets for Data-efﬁcient Training of Machine Learning Models",
            "url": "https://cs.stanford.edu/people/jure/pubs/craig-icml20.pdf"
          },
          {
            "title": "Data-efficiency | Baharan Mirzasoleiman",
            "url": "https://baharanm.github.io/projects/data_efficient/"
          },
          {
            "title": "[1906.01827] Coresets for Data-efficient Training of Machine Learning Models",
            "url": "https://arxiv.org/abs/1906.01827"
          },
          {
            "title": "[PDF] Coresets for Data-efficient Training of Machine Learning Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Coresets-for-Data-efficient-Training-of-Machine-Mirzasoleiman-Bilmes/790985a4bee821046992ff3d5322ff11dd1b4262"
          },
          {
            "title": "Coresets for Data-efficient Training of Machine Learning ...",
            "url": "https://icml.cc/media/icml-2020/Slides/6325.pdf"
          },
          {
            "title": "ICML 2020",
            "url": "https://icml.cc/Conferences/2020/ScheduleMultitrack?event=6396"
          },
          {
            "title": "Coresets for data-efficient training of machine learning models | Proceedings of the 37th International Conference on Machine Learning",
            "url": "https://dl.acm.org/doi/10.5555/3524938.3525583"
          },
          {
            "title": "GRAD-MATCH: Gradient Matching based Data Subset Selection for Efﬁcient",
            "url": "https://arxiv.org/pdf/2103.00123"
          },
          {
            "title": "GitHub - PatrickZH/Awesome-Coreset-Selection: Awesome coreset/core-set/subset/sample selection works. · GitHub",
            "url": "https://github.com/PatrickZH/Awesome-Coreset-Selection"
          },
          {
            "title": "Coresets for Data-efficient Training of Machine Learning Models",
            "url": "http://proceedings.mlr.press/v119/mirzasoleiman20a/mirzasoleiman20a.pdf"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about CRAIG and its publication at ICML 2020:\n\n## Summary of CRAIG (ICML 2020)\n\nCRAIG is a method to select a weighted subset (or coreset) of training data that closely estimates the full gradient by maximizing a submodular function. The method proves that applying incremental gradient (IG) to this subset is guaranteed to converge to the (near)optimal solution with the same convergence rate as that of IG for convex optimization.\n\nCRAIG speeds up various IG methods by up to 6x for logistic regression and 3x for training deep neural networks, while achieving practically the same solution.\n\nThe paper was published in the International Conference on Machine Learning (ICML) in 2020 with authors Baharan Mirzasoleiman, Jeff Bilmes, and Jure Leskovec.\n\n### Key Features\n\nCRAIG is a recent coreset algorithm that shows promise for both deep learning and classical machine learning models. Unlike other coreset techniques that largely focus on approximating loss functions, CRAIG selects representative subsets of the training data that closely approximate the full gradient.\n\nThe paper addresses a fundamental challenge in machine learning: how to select a training data subset that can theoretically and practically perform on par with the full dataset."
    ],
    "durationSeconds": 5.767449079999999
  },
  "sourceToolAssistantUUID": "4d958718-c7c3-48dd-8d98-47897cc63c3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Beyond Difficulty: Diversity-Aware Dynamic Sampling for Data-Efficient…",
  "leafUuid": "f79e732b-7683-4681-8937-e6c5889c0ddb",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Benchmark diversity-aware selection methods on VLA BC",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Tool call

_source line 22 · 2026-05-14T03:21:38.449Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EUXr5W9ZiqR3sT8Hsxo9h4`</summary>

```json
{
  "query": "D2 Pruning diversity difficulty graph message passing ICLR 2024 data pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f79e732b-7683-4681-8937-e6c5889c0ddb",
  "isSidechain": false,
  "requestId": "req_011Cb1k1G8LUqkxXbhP4f1Yr",
  "type": "assistant",
  "uuid": "15cbf3ec-d490-42d9-82aa-cd626480ec01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCCv8FRyHqyXNrBrkee2cz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 924,
      "cache_read_input_tokens": 27736,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 27736,
          "cache_creation_input_tokens": 924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 924
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

_source line 23 · 2026-05-14T03:21:45.923Z_

<details><summary>↩ Tool result · `toolu_01EUXr5W9ZiqR3sT8Hsxo9h4`</summary>

```text
Web search results for query: "D2 Pruning diversity difficulty graph message passing ICLR 2024 data pruning"

Links: [{"title":"$\\mathbb{D}^2$ Pruning: Message Passing for Balancing Diversity & Difficulty in Data Pruning | OpenReview","url":"https://openreview.net/forum?id=thbtoAkCe9"},{"title":"[2310.07931] D2 Pruning: Message Passing for Balancing Diversity and Difficulty in Data Pruning","url":"https://arxiv.org/abs/2310.07931"},{"title":"PRUNING: MESSAGE PASSING FOR BALANCING ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/f646a4c970799f789e031b63161d018d-Paper-Conference.pdf"},{"title":"Adapt-∞: Scalable Lifelong Multimodal Instruction Tuning via Dynamic Data Selection","url":"https://arxiv.org/html/2410.10636v1"},{"title":"UNC Computer Science presents 14 papers at ICLR 2024 - UNC Computer Science","url":"https://cs.unc.edu/news-article/unc-computer-science-presents-14-papers-at-iclr-2024/"},{"title":"D2 Pruning: Message Passing for Balancing Diversity & Difficulty in Data Pruning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/D2-Pruning:-Message-Passing-for-Balancing-Diversity-Maharana-Yadav/a363d987fc8e22393daf563c955a474ca82d80bc"},{"title":"SCAN: Bootstrapping Contrastive Pre-training for Data Efficiency","url":"https://arxiv.org/html/2411.09126v1"},{"title":"graph-based-deep-learning-literature/conference-publications/folders/years/2024/publications_iclr24/README.md at master · naganandy/graph-based-deep-learning-literature","url":"https://github.com/naganandy/graph-based-deep-learning-literature/blob/master/conference-publications/folders/years/2024/publications_iclr24/README.md"},{"title":"GitHub - adymaharana/d2pruning","url":"https://github.com/adymaharana/d2pruning"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7d848891e365ca623dc8352db9782585-Paper-Conference.pdf"}]

Based on the web search results, I found comprehensive information about the D2 Pruning paper. Here's what I found:

## D2 Pruning: Message Passing for Balancing Diversity & Difficulty in Data Pruning

D2 Pruning is a method for "Message Passing for Balancing Diversity and Difficulty in Data Pruning" published at ICLR 2024.

### Key Contribution

The paper addresses the challenge that there are two dominant approaches in coreset selection: (1) geometry-based data selection for maximizing data diversity in the coreset, and (2) functions that assign difficulty scores to samples based on training dynamics. However, optimizing for data diversity leads to a coreset that is biased towards easier samples, whereas selection by difficulty ranking omits easy samples that are necessary for the training of deep learning models.

### Methodology

The paper represents the dataset as a graph and introduces a novel message-passing algorithm called D2 PRUNING that accounts for both factors when selecting samples for coreset. In this framework, node scores represent a sample's informativeness (such as difficulty or importance), while edges capture the similarities between samples. The data pruning process is formulated as an iterative node selection problem, where at each step, nodes with the highest scores are selected, and the scores of neighboring nodes are reduced to account for redundancy.

### Results

The paper evaluates this pruning method on multiple image classification and natural language processing (NLP) datasets and finds that D2 PRUNING outperforms state-of-art methods for coreset selection at low-to-medium pruning rates.

The analysis shows that D2 PRUNING selects a coreset with a higher distribution of difficult samples for low pruning rates and with equitable distribution over easy and difficult samples for medium-to-high pruning rates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15cbf3ec-d490-42d9-82aa-cd626480ec01",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "50ad502e-d361-44b8-95f9-9fe913961a79",
  "toolUseResult": {
    "query": "D2 Pruning diversity difficulty graph message passing ICLR 2024 data pruning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QwgkxiG7zSmvhYV8hfdPHv",
        "content": [
          {
            "title": "$\\mathbb{D}^2$ Pruning: Message Passing for Balancing Diversity & Difficulty in Data Pruning | OpenReview",
            "url": "https://openreview.net/forum?id=thbtoAkCe9"
          },
          {
            "title": "[2310.07931] D2 Pruning: Message Passing for Balancing Diversity and Difficulty in Data Pruning",
            "url": "https://arxiv.org/abs/2310.07931"
          },
          {
            "title": "PRUNING: MESSAGE PASSING FOR BALANCING ...",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/f646a4c970799f789e031b63161d018d-Paper-Conference.pdf"
          },
          {
            "title": "Adapt-∞: Scalable Lifelong Multimodal Instruction Tuning via Dynamic Data Selection",
            "url": "https://arxiv.org/html/2410.10636v1"
          },
          {
            "title": "UNC Computer Science presents 14 papers at ICLR 2024 - UNC Computer Science",
            "url": "https://cs.unc.edu/news-article/unc-computer-science-presents-14-papers-at-iclr-2024/"
          },
          {
            "title": "D2 Pruning: Message Passing for Balancing Diversity & Difficulty in Data Pruning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/D2-Pruning:-Message-Passing-for-Balancing-Diversity-Maharana-Yadav/a363d987fc8e22393daf563c955a474ca82d80bc"
          },
          {
            "title": "SCAN: Bootstrapping Contrastive Pre-training for Data Efficiency",
            "url": "https://arxiv.org/html/2411.09126v1"
          },
          {
            "title": "graph-based-deep-learning-literature/conference-publications/folders/years/2024/publications_iclr24/README.md at master · naganandy/graph-based-deep-learning-literature",
            "url": "https://github.com/naganandy/graph-based-deep-learning-literature/blob/master/conference-publications/folders/years/2024/publications_iclr24/README.md"
          },
          {
            "title": "GitHub - adymaharana/d2pruning",
            "url": "https://github.com/adymaharana/d2pruning"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/7d848891e365ca623dc8352db9782585-Paper-Conference.pdf"
          }
        ]
      },
      "Based on the web search results, I found comprehensive information about the D2 Pruning paper. Here's what I found:\n\n## D2 Pruning: Message Passing for Balancing Diversity & Difficulty in Data Pruning\n\nD2 Pruning is a method for \"Message Passing for Balancing Diversity and Difficulty in Data Pruning\" published at ICLR 2024.\n\n### Key Contribution\n\nThe paper addresses the challenge that there are two dominant approaches in coreset selection: (1) geometry-based data selection for maximizing data diversity in the coreset, and (2) functions that assign difficulty scores to samples based on training dynamics. However, optimizing for data diversity leads to a coreset that is biased towards easier samples, whereas selection by difficulty ranking omits easy samples that are necessary for the training of deep learning models.\n\n### Methodology\n\nThe paper represents the dataset as a graph and introduces a novel message-passing algorithm called D2 PRUNING that accounts for both factors when selecting samples for coreset. In this framework, node scores represent a sample's informativeness (such as difficulty or importance), while edges capture the similarities between samples. The data pruning process is formulated as an iterative node selection problem, where at each step, nodes with the highest scores are selected, and the scores of neighboring nodes are reduced to account for redundancy.\n\n### Results\n\nThe paper evaluates this pruning method on multiple image classification and natural language processing (NLP) datasets and finds that D2 PRUNING outperforms state-of-art methods for coreset selection at low-to-medium pruning rates.\n\nThe analysis shows that D2 PRUNING selects a coreset with a higher distribution of difficult samples for low pruning rates and with equitable distribution over easy and difficult samples for medium-to-high pruning rates."
    ],
    "durationSeconds": 7.468804925999997
  },
  "sourceToolAssistantUUID": "15cbf3ec-d490-42d9-82aa-cd626480ec01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T03:21:48.854Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AJcBcjmyfYvxA1X7pMCw4N`</summary>

```json
{
  "query": "InfoMax information maximization data pruning ICLR 2025 importance redundancy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50ad502e-d361-44b8-95f9-9fe913961a79",
  "isSidechain": false,
  "requestId": "req_011Cb1k2KX1Eb2M6Lv6NNzvv",
  "type": "assistant",
  "uuid": "fbbb8e1a-9c01-4c1e-b4ce-88f3d49b156e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WnSajpoMHg7rrQFYcVjJ6E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1171,
      "cache_read_input_tokens": 28660,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 28660,
          "cache_creation_input_tokens": 1171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1171
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

_source line 25 · 2026-05-14T03:21:54.881Z_

<details><summary>↩ Tool result · `toolu_01AJcBcjmyfYvxA1X7pMCw4N`</summary>

```text
Web search results for query: "InfoMax information maximization data pruning ICLR 2025 importance redundancy"

Links: [{"title":"Data Pruning by Information Maximization | OpenReview","url":"https://openreview.net/forum?id=93XT0lKOct"},{"title":"DATA PRUNING BY INFORMATION MAXIMIZATION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7d848891e365ca623dc8352db9782585-Paper-Conference.pdf"},{"title":"[2506.01701] Data Pruning by Information Maximization","url":"https://arxiv.org/abs/2506.01701"},{"title":"ICLR Poster Data Pruning by Information Maximization","url":"https://iclr.cc/virtual/2025/poster/30725"},{"title":"(PDF) Data Pruning by Information Maximization","url":"https://www.researchgate.net/publication/392371209_Data_Pruning_by_Information_Maximization"},{"title":"[PDF] Data Pruning by Information Maximization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Data-Pruning-by-Information-Maximization-Tan-Wu/f967b8f25eb569bec0bef80dc403a68a8ae51e8d"},{"title":"Data Pruning by Information Maximization","url":"https://arxiv.org/html/2506.01701"},{"title":"[Literature Review] Data Pruning by Information Maximization","url":"https://www.themoonlight.io/en/review/data-pruning-by-information-maximization"},{"title":"GitHub - hrtan/InfoMax · GitHub","url":"https://github.com/hrtan/InfoMax"},{"title":"Data Pruning by Information Maximization | alphaXiv","url":"https://www.alphaxiv.org/overview/2506.01701v2"}]

I found relevant information about InfoMax. Here are the search results:

## InfoMax: Data Pruning by Information Maximization (ICLR 2025)

InfoMax is a novel data pruning method, also known as coreset selection, designed to maximize the information content of selected samples while minimizing redundancy. The paper was published as a conference paper at ICLR 2025 by authors Haoru Tan, Sitong Wu, Wei Huang, Shizhen Zhao, and Xiaojuan Qi.

### Key Technical Approach

The coreset selection problem is formalized as a discrete quadratic programming (DQP) task, with the objective of maximizing the total information content, represented as the sum of individual sample contributions minus the redundancies introduced by similar samples within the coreset. Individual sample information is measured by importance scores capturing their influence or difficulty in model learning, while redundancy is quantified using pairwise sample similarities based on the premise that similar samples contribute similarly to the learning process.

### Scalability and Methods

To ensure practical scalability, the method introduces an efficient gradient-based solver, complemented by sparsification techniques applied to the similarity matrix and dataset partitioning strategies, enabling InfoMax to seamlessly scale to datasets with millions of samples.

### Applications and Performance

Extensive experiments demonstrate the superior performance of InfoMax in various data pruning tasks, including image classification, vision-language pre-training, and instruction tuning for large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbbb8e1a-9c01-4c1e-b4ce-88f3d49b156e",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "de6359b2-457e-4777-9ed8-e310f6d398f8",
  "toolUseResult": {
    "query": "InfoMax information maximization data pruning ICLR 2025 importance redundancy",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CwuJFXEd6BwU2ActjEaLUJ",
        "content": [
          {
            "title": "Data Pruning by Information Maximization | OpenReview",
            "url": "https://openreview.net/forum?id=93XT0lKOct"
          },
          {
            "title": "DATA PRUNING BY INFORMATION MAXIMIZATION",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/7d848891e365ca623dc8352db9782585-Paper-Conference.pdf"
          },
          {
            "title": "[2506.01701] Data Pruning by Information Maximization",
            "url": "https://arxiv.org/abs/2506.01701"
          },
          {
            "title": "ICLR Poster Data Pruning by Information Maximization",
            "url": "https://iclr.cc/virtual/2025/poster/30725"
          },
          {
            "title": "(PDF) Data Pruning by Information Maximization",
            "url": "https://www.researchgate.net/publication/392371209_Data_Pruning_by_Information_Maximization"
          },
          {
            "title": "[PDF] Data Pruning by Information Maximization | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Data-Pruning-by-Information-Maximization-Tan-Wu/f967b8f25eb569bec0bef80dc403a68a8ae51e8d"
          },
          {
            "title": "Data Pruning by Information Maximization",
            "url": "https://arxiv.org/html/2506.01701"
          },
          {
            "title": "[Literature Review] Data Pruning by Information Maximization",
            "url": "https://www.themoonlight.io/en/review/data-pruning-by-information-maximization"
          },
          {
            "title": "GitHub - hrtan/InfoMax · GitHub",
            "url": "https://github.com/hrtan/InfoMax"
          },
          {
            "title": "Data Pruning by Information Maximization | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2506.01701v2"
          }
        ]
      },
      "I found relevant information about InfoMax. Here are the search results:\n\n## InfoMax: Data Pruning by Information Maximization (ICLR 2025)\n\nInfoMax is a novel data pruning method, also known as coreset selection, designed to maximize the information content of selected samples while minimizing redundancy. The paper was published as a conference paper at ICLR 2025 by authors Haoru Tan, Sitong Wu, Wei Huang, Shizhen Zhao, and Xiaojuan Qi.\n\n### Key Technical Approach\n\nThe coreset selection problem is formalized as a discrete quadratic programming (DQP) task, with the objective of maximizing the total information content, represented as the sum of individual sample contributions minus the redundancies introduced by similar samples within the coreset. Individual sample information is measured by importance scores capturing their influence or difficulty in model learning, while redundancy is quantified using pairwise sample similarities based on the premise that similar samples contribute similarly to the learning process.\n\n### Scalability and Methods\n\nTo ensure practical scalability, the method introduces an efficient gradient-based solver, complemented by sparsification techniques applied to the similarity matrix and dataset partitioning strategies, enabling InfoMax to seamlessly scale to datasets with millions of samples.\n\n### Applications and Performance\n\nExtensive experiments demonstrate the superior performance of InfoMax in various data pruning tasks, including image classification, vision-language pre-training, and instruction tuning for large language models."
    ],
    "durationSeconds": 6.022440146999987
  },
  "sourceToolAssistantUUID": "fbbb8e1a-9c01-4c1e-b4ce-88f3d49b156e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T03:21:57.831Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014oQoj87LPENRFxjT2tE2bh`</summary>

```json
{
  "query": "D3 diversity difficulty dependability data selection IJCAI 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de6359b2-457e-4777-9ed8-e310f6d398f8",
  "isSidechain": false,
  "requestId": "req_011Cb1k2zJt7fnKEDTPxJWFM",
  "type": "assistant",
  "uuid": "0be2d6dc-93f3-4638-ae84-28f7b6d13ba2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WTmPEfPzb2dQGvrmkBF6Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 29831,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 903,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 29831,
          "cache_creation_input_tokens": 903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 903
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

_source line 27 · 2026-05-14T03:22:04.873Z_

<details><summary>↩ Tool result · `toolu_014oQoj87LPENRFxjT2tE2bh`</summary>

```text
Web search results for query: "D3 diversity difficulty dependability data selection IJCAI 2025"

Links: [{"title":"[2503.11441] D3: Diversity, Difficulty, and Dependability-Aware Data Selection for Sample-Efficient LLM Instruction Tuning","url":"https://arxiv.org/abs/2503.11441"},{"title":"D3: Diversity, Difficulty, and Dependability-Aware Data Selection","url":"https://www.ijcai.org/proceedings/2025/0928.pdf"},{"title":"D3: Diversity, Difficulty, and Dependability-Aware Data Selection for Sample-Efficient LLM Instruction Tuning","url":"https://arxiv.org/html/2503.11441v1"},{"title":"D3: Diversity, Difficulty, and Dependability-Aware Data Selection for Sample-Efficient LLM Instruction Tuning | Request PDF","url":"https://www.researchgate.net/publication/395673541_D3_Diversity_Difficulty_and_Dependability-Aware_Data_Selection_for_Sample-Efficient_LLM_Instruction_Tuning"},{"title":"(PDF) D3: Diversity, Difficulty, and Dependability-Aware Data Selection for Sample-Efficient LLM Instruction Tuning","url":"https://www.researchgate.net/publication/389894723_D3_Diversity_Difficulty_and_Dependability-Aware_Data_Selection_for_Sample-Efficient_LLM_Instruction_Tuning"},{"title":"[Literature Review] D3: Diversity, Difficulty, and Dependability-Aware Data Selection for Sample-Efficient LLM Instruction Tuning","url":"https://www.themoonlight.io/en/review/d3-diversity-difficulty-and-dependability-aware-data-selection-for-sample-efficient-llm-instruction-tuning"},{"title":"D3: Diversity, Difficulty, and Dependability-Aware Data Selection ...","url":"https://paperswithcode.com/paper/d3-diversity-difficulty-and-dependability"},{"title":"3DS: Decomposed Difficulty Data Selection’s Case Study on LLM Medical Domain Adaptation | OpenReview","url":"https://openreview.net/forum?id=I5p1Gm8GFS"},{"title":"IJCAI 2025","url":"https://2025.ijcai.org/"},{"title":"[2309.08798] D3: Data Diversity Design for Systematic Generalization in Visual Question Answering","url":"https://arxiv.org/abs/2309.08798"}]

Based on the web search results, I found comprehensive information about the D3 paper for IJCAI 2025:

## Overview

D3 establishes data selection criteria based on three distinct aspects of data value: diversity, difficulty, and dependability, and proposes the D3 method comprising two key steps of scoring and selection.

## Key Components

**Scoring Step:**
The diversity function measures sample distinctiveness and the uncertainty-based prediction difficulty evaluates sample difficulty by mitigating the interference of context-oriented generation diversity. An external LLM is integrated for dependability assessment.

**Selection Step:**
The D3 weighted coreset objective jointly optimizes three aspects of data value to solve for the most valuable subset. The two steps of D3 can iterate multiple rounds, incorporating feedback to refine the selection focus adaptively.

## Results

Experiments on both public datasets and the real-world Taobao Live application demonstrate that D3 endows LLMs with competitive or even superior instruction-following capabilities using less than 10% of the entire dataset.

## Significance

The three criteria correspond to inter-sample, sample-model, and intra-sample perspectives of data value, respectively, providing a comprehensive framework for data selection in LLM instruction tuning. These validate the necessity of comprehensively considering all three criteria in data selection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0be2d6dc-93f3-4638-ae84-28f7b6d13ba2",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "3f77574a-6d01-4b23-a767-aa438ed59437",
  "toolUseResult": {
    "query": "D3 diversity difficulty dependability data selection IJCAI 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VWZCwVRA7fTTUGXfuv7vW8",
        "content": [
          {
            "title": "[2503.11441] D3: Diversity, Difficulty, and Dependability-Aware Data Selection for Sample-Efficient LLM Instruction Tuning",
            "url": "https://arxiv.org/abs/2503.11441"
          },
          {
            "title": "D3: Diversity, Difficulty, and Dependability-Aware Data Selection",
            "url": "https://www.ijcai.org/proceedings/2025/0928.pdf"
          },
          {
            "title": "D3: Diversity, Difficulty, and Dependability-Aware Data Selection for Sample-Efficient LLM Instruction Tuning",
            "url": "https://arxiv.org/html/2503.11441v1"
          },
          {
            "title": "D3: Diversity, Difficulty, and Dependability-Aware Data Selection for Sample-Efficient LLM Instruction Tuning | Request PDF",
            "url": "https://www.researchgate.net/publication/395673541_D3_Diversity_Difficulty_and_Dependability-Aware_Data_Selection_for_Sample-Efficient_LLM_Instruction_Tuning"
          },
          {
            "title": "(PDF) D3: Diversity, Difficulty, and Dependability-Aware Data Selection for Sample-Efficient LLM Instruction Tuning",
            "url": "https://www.researchgate.net/publication/389894723_D3_Diversity_Difficulty_and_Dependability-Aware_Data_Selection_for_Sample-Efficient_LLM_Instruction_Tuning"
          },
          {
            "title": "[Literature Review] D3: Diversity, Difficulty, and Dependability-Aware Data Selection for Sample-Efficient LLM Instruction Tuning",
            "url": "https://www.themoonlight.io/en/review/d3-diversity-difficulty-and-dependability-aware-data-selection-for-sample-efficient-llm-instruction-tuning"
          },
          {
            "title": "D3: Diversity, Difficulty, and Dependability-Aware Data Selection ...",
            "url": "https://paperswithcode.com/paper/d3-diversity-difficulty-and-dependability"
          },
          {
            "title": "3DS: Decomposed Difficulty Data Selection’s Case Study on LLM Medical Domain Adaptation | OpenReview",
            "url": "https://openreview.net/forum?id=I5p1Gm8GFS"
          },
          {
            "title": "IJCAI 2025",
            "url": "https://2025.ijcai.org/"
          },
          {
            "title": "[2309.08798] D3: Data Diversity Design for Systematic Generalization in Visual Question Answering",
            "url": "https://arxiv.org/abs/2309.08798"
          }
        ]
      },
      "Based on the web search results, I found comprehensive information about the D3 paper for IJCAI 2025:\n\n## Overview\n\nD3 establishes data selection criteria based on three distinct aspects of data value: diversity, difficulty, and dependability, and proposes the D3 method comprising two key steps of scoring and selection.\n\n## Key Components\n\n**Scoring Step:**\nThe diversity function measures sample distinctiveness and the uncertainty-based prediction difficulty evaluates sample difficulty by mitigating the interference of context-oriented generation diversity. An external LLM is integrated for dependability assessment.\n\n**Selection Step:**\nThe D3 weighted coreset objective jointly optimizes three aspects of data value to solve for the most valuable subset. The two steps of D3 can iterate multiple rounds, incorporating feedback to refine the selection focus adaptively.\n\n## Results\n\nExperiments on both public datasets and the real-world Taobao Live application demonstrate that D3 endows LLMs with competitive or even superior instruction-following capabilities using less than 10% of the entire dataset.\n\n## Significance\n\nThe three criteria correspond to inter-sample, sample-model, and intra-sample perspectives of data value, respectively, providing a comprehensive framework for data selection in LLM instruction tuning. These validate the necessity of comprehensively considering all three criteria in data selection."
    ],
    "durationSeconds": 7.035203255000001
  },
  "sourceToolAssistantUUID": "0be2d6dc-93f3-4638-ae84-28f7b6d13ba2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T03:22:09.331Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0112n8zWv1e6fvvcoH1wg2tm`</summary>

```json
{
  "query": "Hejna robot data curation mutual information estimators RSS 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f77574a-6d01-4b23-a767-aa438ed59437",
  "isSidechain": false,
  "requestId": "req_011Cb1k3iXdTwAL9rzmYGUES",
  "type": "assistant",
  "uuid": "6279517e-fd32-4156-8d4b-ecae12a1ae24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YHaU1w4kariMkgmHDiDG5b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1031,
      "cache_read_input_tokens": 30734,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 30734,
          "cache_creation_input_tokens": 1031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1031
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

_source line 29 · 2026-05-14T03:22:16.186Z_

<details><summary>↩ Tool result · `toolu_0112n8zWv1e6fvvcoH1wg2tm`</summary>

```text
Web search results for query: "Hejna robot data curation mutual information estimators RSS 2026"

Links: [{"title":"Robot Data Curation with Mutual Information Estimators · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/23/"},{"title":"[2502.08623] Robot Data Curation with Mutual Information Estimators","url":"https://arxiv.org/abs/2502.08623"},{"title":"GitHub - jhejna/demonstration-information: Code for the paper Robot Data Curation with Mutual Information Estimators","url":"https://github.com/jhejna/demonstration-information"},{"title":"Robot Data Curation with Mutual Information Estimators","url":"https://arxiv.org/html/2502.08623v1"},{"title":"[PDF] Robot Data Curation with Mutual Information Estimators | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Robot-Data-Curation-with-Mutual-Information-Hejna-Mirchandani/37cb83dc757f483cfd389c8709b4aee389da8dc6"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"Robot Data Curation with Mutual Information Estimators | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.08623v3"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121v1"},{"title":"(PDF) SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://www.researchgate.net/publication/392167457_SCIZOR_A_Self-Supervised_Approach_to_Data_Curation_for_Large-Scale_Imitation_Learning"},{"title":"Robot Data Curation with Mutual Information Estimators","url":"https://www.researchgate.net/publication/395367864_Robot_Data_Curation_with_Mutual_Information_Estimators"}]

Based on the search results, I found relevant information about the paper you're inquiring about:

## Robot Data Curation with Mutual Information Estimators

The paper is authored by Joey Hejna, Suvir Mirchandani, and colleagues including Manon Devin and Dorsa Sadigh.

**Overview:**
The performance of imitation learning policies often hinges on the datasets with which they are trained. Consequently, investment in data collection for robotics has grown across both industrial and academic labs. However, despite the marked increase in the quantity of demonstrations collected, little work has sought to assess the quality of said data despite mounting evidence of its importance in other areas such as vision and language.

**Research Contribution:**
The paper introduces Demonstration Information Estimation (DemInf), an unsupervised method for curating robot demonstration datasets by using mutual information between states and actions as a proxy for data quality. The method estimates the average contribution of a trajectory towards the mutual information between states and actions in the entire dataset, which captures both the entropy of the marginal action distribution and the state-conditioned action entropy.

**Methodology:**
The approach introduces a novel technique based on k-nearest neighbor estimates of mutual information on top of simple VAE embeddings of states and actions, which leads to a 5-10% improvement in RoboMimic and better performance on real ALOHA and Franka setups.

**Publication:**
The paper appears in the Robotics: Science and Systems (RSS) proceedings, with the preprint dated to early 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6279517e-fd32-4156-8d4b-ecae12a1ae24",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "73aecb54-b0b0-4a00-a295-c3482bfa8ae7",
  "toolUseResult": {
    "query": "Hejna robot data curation mutual information estimators RSS 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XB4Dv112C3YuqLxisR7U2c",
        "content": [
          {
            "title": "Robot Data Curation with Mutual Information Estimators · Robotics: Science and Systems",
            "url": "https://roboticsconference.org/program/papers/23/"
          },
          {
            "title": "[2502.08623] Robot Data Curation with Mutual Information Estimators",
            "url": "https://arxiv.org/abs/2502.08623"
          },
          {
            "title": "GitHub - jhejna/demonstration-information: Code for the paper Robot Data Curation with Mutual Information Estimators",
            "url": "https://github.com/jhejna/demonstration-information"
          },
          {
            "title": "Robot Data Curation with Mutual Information Estimators",
            "url": "https://arxiv.org/html/2502.08623v1"
          },
          {
            "title": "[PDF] Robot Data Curation with Mutual Information Estimators | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Robot-Data-Curation-with-Mutual-Information-Hejna-Mirchandani/37cb83dc757f483cfd389c8709b4aee389da8dc6"
          },
          {
            "title": "Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning",
            "url": "https://arxiv.org/html/2603.09056"
          },
          {
            "title": "Robot Data Curation with Mutual Information Estimators | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2502.08623v3"
          },
          {
            "title": "CUPID: Curating Data your Robot Loves with Influence Functions",
            "url": "https://arxiv.org/html/2506.19121v1"
          },
          {
            "title": "(PDF) SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning",
            "url": "https://www.researchgate.net/publication/392167457_SCIZOR_A_Self-Supervised_Approach_to_Data_Curation_for_Large-Scale_Imitation_Learning"
          },
          {
            "title": "Robot Data Curation with Mutual Information Estimators",
            "url": "https://www.researchgate.net/publication/395367864_Robot_Data_Curation_with_Mutual_Information_Estimators"
          }
        ]
      },
      "Based on the search results, I found relevant information about the paper you're inquiring about:\n\n## Robot Data Curation with Mutual Information Estimators\n\nThe paper is authored by Joey Hejna, Suvir Mirchandani, and colleagues including Manon Devin and Dorsa Sadigh.\n\n**Overview:**\nThe performance of imitation learning policies often hinges on the datasets with which they are trained. Consequently, investment in data collection for robotics has grown across both industrial and academic labs. However, despite the marked increase in the quantity of demonstrations collected, little work has sought to assess the quality of said data despite mounting evidence of its importance in other areas such as vision and language.\n\n**Research Contribution:**\nThe paper introduces Demonstration Information Estimation (DemInf), an unsupervised method for curating robot demonstration datasets by using mutual information between states and actions as a proxy for data quality. The method estimates the average contribution of a trajectory towards the mutual information between states and actions in the entire dataset, which captures both the entropy of the marginal action distribution and the state-conditioned action entropy.\n\n**Methodology:**\nThe approach introduces a novel technique based on k-nearest neighbor estimates of mutual information on top of simple VAE embeddings of states and actions, which leads to a 5-10% improvement in RoboMimic and better performance on real ALOHA and Franka setups.\n\n**Publication:**\nThe paper appears in the Robotics: Science and Systems (RSS) proceedings, with the preprint dated to early 2025."
    ],
    "durationSeconds": 6.849673065999989
  },
  "sourceToolAssistantUUID": "6279517e-fd32-4156-8d4b-ecae12a1ae24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-14T03:22:16.194Z_

```json
{
  "parentUuid": "73aecb54-b0b0-4a00-a295-c3482bfa8ae7",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "388ca050-a192-4b19-b250-b682d2a37997",
  "timestamp": "2026-05-14T03:22:16.194Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Beyond Difficulty: Diversity-Aware Dynamic Sampling for Data-Efficient…",
  "leafUuid": "388ca050-a192-4b19-b250-b682d2a37997",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Benchmark diversity-aware selection methods on VLA BC",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Tool call

_source line 33 · 2026-05-14T03:22:18.960Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014j9GV9jy7mmgRL7fmNVCs7`</summary>

```json
{
  "query": "DemoSpeedup entropy guided frame selection visuomotor CoRL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "388ca050-a192-4b19-b250-b682d2a37997",
  "isSidechain": false,
  "requestId": "req_011Cb1k4YsVDTRMfBYwBVcrr",
  "type": "assistant",
  "uuid": "fdef02c8-6a0c-4fe2-9f04-7241905d15a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBWppVUtREmepgubwVYVRa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1088,
      "cache_read_input_tokens": 31765,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1088,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 31765,
          "cache_creation_input_tokens": 1088,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1088
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

_source line 34 · 2026-05-14T03:22:30.186Z_

<details><summary>↩ Tool result · `toolu_014j9GV9jy7mmgRL7fmNVCs7`</summary>

```text
Web search results for query: "DemoSpeedup entropy guided frame selection visuomotor CoRL 2025"

Links: [{"title":"DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration | OpenReview","url":"https://openreview.net/forum?id=Tl7girqoLi"},{"title":"[2506.05064] DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration","url":"https://arxiv.org/abs/2506.05064"},{"title":"DemoSpeedup","url":"https://demospeedup.github.io/"},{"title":"DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration","url":"https://arxiv.org/html/2506.05064v2"},{"title":"DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration","url":"https://proceedings.mlr.press/v305/guo25a.html"},{"title":"Accelerating Visuomotor Policies via Entropy-Guided ...","url":"https://openreview.net/pdf?id=Tl7girqoLi"},{"title":"DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration | Request PDF","url":"https://www.researchgate.net/publication/392466961_DemoSpeedup_Accelerating_Visuomotor_Policies_via_Entropy-Guided_Demonstration_Acceleration"},{"title":"[Literature Review] DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration","url":"https://www.themoonlight.io/en/review/demospeedup-accelerating-visuomotor-policies-via-entropy-guided-demonstration-acceleration"},{"title":"[PDF] DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DemoSpeedup:-Accelerating-Visuomotor-Policies-via-Guo-Xue/97b2a5e51c679a42ed874f7abf247712cd9f8622"},{"title":"GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more","url":"https://github.com/smallfryy/corl-2025-papers"}]

Based on the search results, here's what I found about DemoSpeedup:

## Overview

DemoSpeedup is a self-supervised method to accelerate visuomotor policy execution via entropy-guided demonstration acceleration. It addresses the issue that imitation learning policies often have unsatisfactorily slow execution due to commonly tardy demonstrations collected by human operators.

## Method

DemoSpeedup starts from training an arbitrary generative policy (e.g., ACT or Diffusion Policy) on normal-speed demonstrations, which serves as a per-frame action entropy estimator. The core insight is that frames with lower action entropy estimates call for more consistent policy behaviors, which often indicate the demands for higher-precision operations, while frames with higher entropy estimates correspond to more casual sections, and therefore can be more safely accelerated. The demonstrations are segmented according to the estimated entropy, and accelerated by down-sampling at rates that increase with the entropy values.

## Results

For tasks that require much accuracy such as Bomb Deposal and Kitchenware, DemoSpeedup achieves at least 160% speedup, while for tasks that are not demanding on precision, it achieves even higher speedup, such as 278% for ACT and 214% for DP in the Sort task. Empirical validation demonstrates that DemoSpeedup effectively accelerates policy execution by 1.7x to 3x while maintaining or even improving task completion success rates.

## Conference

The paper was published in the Proceedings of The 9th Conference on Robot Learning (CoRL 2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdef02c8-6a0c-4fe2-9f04-7241905d15a5",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "c52f6735-206f-4288-b795-603b37830254",
  "toolUseResult": {
    "query": "DemoSpeedup entropy guided frame selection visuomotor CoRL 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WqD7Jc1QUDmdjKBwY7J8Yy",
        "content": [
          {
            "title": "DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration | OpenReview",
            "url": "https://openreview.net/forum?id=Tl7girqoLi"
          },
          {
            "title": "[2506.05064] DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration",
            "url": "https://arxiv.org/abs/2506.05064"
          },
          {
            "title": "DemoSpeedup",
            "url": "https://demospeedup.github.io/"
          },
          {
            "title": "DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration",
            "url": "https://arxiv.org/html/2506.05064v2"
          },
          {
            "title": "DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration",
            "url": "https://proceedings.mlr.press/v305/guo25a.html"
          },
          {
            "title": "Accelerating Visuomotor Policies via Entropy-Guided ...",
            "url": "https://openreview.net/pdf?id=Tl7girqoLi"
          },
          {
            "title": "DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration | Request PDF",
            "url": "https://www.researchgate.net/publication/392466961_DemoSpeedup_Accelerating_Visuomotor_Policies_via_Entropy-Guided_Demonstration_Acceleration"
          },
          {
            "title": "[Literature Review] DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration",
            "url": "https://www.themoonlight.io/en/review/demospeedup-accelerating-visuomotor-policies-via-entropy-guided-demonstration-acceleration"
          },
          {
            "title": "[PDF] DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/DemoSpeedup:-Accelerating-Visuomotor-Policies-via-Guo-Xue/97b2a5e51c679a42ed874f7abf247712cd9f8622"
          },
          {
            "title": "GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more",
            "url": "https://github.com/smallfryy/corl-2025-papers"
          }
        ]
      },
      "Based on the search results, here's what I found about DemoSpeedup:\n\n## Overview\n\nDemoSpeedup is a self-supervised method to accelerate visuomotor policy execution via entropy-guided demonstration acceleration. It addresses the issue that imitation learning policies often have unsatisfactorily slow execution due to commonly tardy demonstrations collected by human operators.\n\n## Method\n\nDemoSpeedup starts from training an arbitrary generative policy (e.g., ACT or Diffusion Policy) on normal-speed demonstrations, which serves as a per-frame action entropy estimator. The core insight is that frames with lower action entropy estimates call for more consistent policy behaviors, which often indicate the demands for higher-precision operations, while frames with higher entropy estimates correspond to more casual sections, and therefore can be more safely accelerated. The demonstrations are segmented according to the estimated entropy, and accelerated by down-sampling at rates that increase with the entropy values.\n\n## Results\n\nFor tasks that require much accuracy such as Bomb Deposal and Kitchenware, DemoSpeedup achieves at least 160% speedup, while for tasks that are not demanding on precision, it achieves even higher speedup, such as 278% for ACT and 214% for DP in the Sort task. Empirical validation demonstrates that DemoSpeedup effectively accelerates policy execution by 1.7x to 3x while maintaining or even improving task completion success rates.\n\n## Conference\n\nThe paper was published in the Proceedings of The 9th Conference on Robot Learning (CoRL 2025)."
    ],
    "durationSeconds": 11.222296218000004
  },
  "sourceToolAssistantUUID": "fdef02c8-6a0c-4fe2-9f04-7241905d15a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-14T03:22:34.324Z_

Now let me read the actual UDS paper in more detail — it's the closest competitor and I need to understand its method deeply.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c52f6735-206f-4288-b795-603b37830254",
  "isSidechain": false,
  "requestId": "req_011Cb1k5aieA6piubT8Y8Htx",
  "type": "assistant",
  "uuid": "0ea70e2c-3fdd-41ff-9b59-398f35137748",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013rBxxxw5RqcNjVwSZQmaxC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1094,
      "cache_read_input_tokens": 32853,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1094,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 32853,
          "cache_creation_input_tokens": 1094,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1094
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

_source line 36 · 2026-05-14T03:22:36.966Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013zqZ3E5pqRoSiYxW3ZfHy3`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.16882",
  "prompt": "Extract the full abstract, the detailed method description (how utility score and diversity score are computed, how they are combined, the batch selection algorithm), and any limitations or failure modes mentioned. Also note what benchmarks they test on and whether they evaluate on robotics or multi-modal tasks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ea70e2c-3fdd-41ff-9b59-398f35137748",
  "isSidechain": false,
  "requestId": "req_011Cb1k5aieA6piubT8Y8Htx",
  "type": "assistant",
  "uuid": "39f671b9-f772-46b5-8673-0ad4389b0408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013rBxxxw5RqcNjVwSZQmaxC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1094,
      "cache_read_input_tokens": 32853,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1094,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 32853,
          "cache_creation_input_tokens": 1094,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1094
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

_source line 37 · 2026-05-14T03:22:43.248Z_

<details><summary>↩ Tool result · `toolu_013zqZ3E5pqRoSiYxW3ZfHy3`</summary>

```text
# Summary of UDS Paper

## Abstract
The work addresses expensive and potentially biased supervised fine-tuning of LLMs through "Utility-Diversity Sampling (UDS), a framework for efficient online batch selection" that avoids relying on external resources or extra backpropagation overhead.

## Method Components

**Utility & Diversity Scoring:**
The approach leverages "the nuclear norm of the logits matrix to capture both data utility and intra-sample diversity," while "estimating inter-sample diversity through efficient low-dimensional embedding comparisons with a lightweight memory buffer."

**Key Design Features:**
- Eliminates need for reference models or validation sets
- Uses historical sample embeddings stored in memory rather than expensive comparisons
- Avoids additional backpropagation passes

**Batch Selection Algorithm:**
The document provided does not contain detailed algorithmic pseudocode or step-by-step selection procedures beyond the general approach of scoring and filtering samples during training.

## Experimental Coverage

**Limitations Noted:**
The abstract does not explicitly enumerate failure modes or inherent limitations of the approach.

**Evaluation Scope:**
- Tests on "multiple benchmarks" with "varying data budgets"
- Comparison against "state-of-the-art online batch selection methods"
- The page content does not specify whether robotics or multi-modal tasks were evaluated

The full technical details would require accessing the complete PDF or HTML versions of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39f671b9-f772-46b5-8673-0ad4389b0408",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "485cefb8-108d-4af8-b654-31b412ff5d87",
  "toolUseResult": {
    "bytes": 48901,
    "code": 200,
    "codeText": "OK",
    "result": "# Summary of UDS Paper\n\n## Abstract\nThe work addresses expensive and potentially biased supervised fine-tuning of LLMs through \"Utility-Diversity Sampling (UDS), a framework for efficient online batch selection\" that avoids relying on external resources or extra backpropagation overhead.\n\n## Method Components\n\n**Utility & Diversity Scoring:**\nThe approach leverages \"the nuclear norm of the logits matrix to capture both data utility and intra-sample diversity,\" while \"estimating inter-sample diversity through efficient low-dimensional embedding comparisons with a lightweight memory buffer.\"\n\n**Key Design Features:**\n- Eliminates need for reference models or validation sets\n- Uses historical sample embeddings stored in memory rather than expensive comparisons\n- Avoids additional backpropagation passes\n\n**Batch Selection Algorithm:**\nThe document provided does not contain detailed algorithmic pseudocode or step-by-step selection procedures beyond the general approach of scoring and filtering samples during training.\n\n## Experimental Coverage\n\n**Limitations Noted:**\nThe abstract does not explicitly enumerate failure modes or inherent limitations of the approach.\n\n**Evaluation Scope:**\n- Tests on \"multiple benchmarks\" with \"varying data budgets\"\n- Comparison against \"state-of-the-art online batch selection methods\"\n- The page content does not specify whether robotics or multi-modal tasks were evaluated\n\nThe full technical details would require accessing the complete PDF or HTML versions of the paper.",
    "durationMs": 6275,
    "url": "https://arxiv.org/abs/2510.16882"
  },
  "sourceToolAssistantUUID": "39f671b9-f772-46b5-8673-0ad4389b0408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T03:22:49.528Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011fi7Mk9W5MBknsa7GSZotH`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.16882",
  "prompt": "Extract the detailed method: \n1. How is the utility score computed (nuclear norm of logits)? \n2. How is intra-sample diversity measured? \n3. How is inter-sample diversity measured (memory buffer, embedding comparison)?\n4. How are the scores combined into a final batch selection decision?\n5. What is the total score formula (s_total = s_intra + alpha * s_inter)?\n6. What datasets/tasks are evaluated (any robotics? any multi-modal)?\n7. What are the stated limitations?\n8. Does this method operate at token level, sample level, or batch level?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "485cefb8-108d-4af8-b654-31b412ff5d87",
  "isSidechain": false,
  "requestId": "req_011Cb1k6YdQaqmzv1oTDQbdA",
  "type": "assistant",
  "uuid": "1b319376-b510-4ad3-923a-6fcc547c685f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YXUt2DG3dPuesPhEos6Pg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 33947,
      "output_tokens": 222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 495,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 222,
          "cache_read_input_tokens": 33947,
          "cache_creation_input_tokens": 495,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 495
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

_source line 39 · 2026-05-14T03:22:58.113Z_

<details><summary>↩ Tool result · `toolu_011fi7Mk9W5MBknsa7GSZotH`</summary>

```text
# UDS: Utility-Diversity Aware Online Batch Selection - Method Overview

## 1. Utility Score Computation (Nuclear Norm)

The intra-sample importance score uses the nuclear norm of the logits matrix:

> "s_intra^{t,i} = ||L(x_t^i; θ_t)||_* = Σ σ_j"

where σ_j represents singular values. This captures both optimization utility and intra-sample diversity, with larger nuclear norms correlating to higher loss reduction potential.

## 2. Intra-Sample Diversity Measurement

Diversity within a sample is reflected through the logits matrix structure. The paper notes that "larger nuclear norm correlates with higher intra-sample diversity" because low rank (repetitive tokens) yields minimum nuclear norm, while full rank with equal singular values yields maximum nuclear norm. This means diverse token predictions across sequences produce higher nuclear norm values.

## 3. Inter-Sample Diversity Measurement

The method maintains a First-In-First-Out memory buffer storing compressed logits embeddings:

> "s_inter^{t,i} = (1/|Q|) Σ ||z_t^i - z_j||_2"

These embeddings are created through bilinear random projections using subsampled randomized Fourier transforms, reducing computational complexity from O(NVd) to O((N+V)d log(NV)).

## 4. Score Combination and Batch Selection

The total score combines both components:

> "s_total^{t,i} = s_intra^{t,i} + α·s_inter^{t,i}"

The top-K samples with highest total scores are selected from the candidate batch.

## 5. Final Scoring Formula

As stated above, the formula integrates intra-sample utility/diversity with weighted inter-sample diversity through hyperparameter α.

## 6. Evaluation Datasets and Tasks

Experiments use four domains:
- **MMLU** (general knowledge)
- **ScienceQA** (scientific reasoning)
- **GSM8K** (mathematical reasoning)
- **HumanEval** (code generation)

No robotics or multimodal tasks are included. Models tested: Llama-3.1-8B and Qwen-2.5-7B with LoRA fine-tuning.

## 7. Stated Limitations

The paper identifies limitations in Appendix F, noting the method operates within existing datasets and architectures, requiring careful hyperparameter tuning (α varies by dataset/model combination).

## 8. Operational Level

This method operates at the **sample level** during training. Decisions are made per-sample within each batch, selecting which training instances participate in parameter updates based on computed importance scores.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b319376-b510-4ad3-923a-6fcc547c685f",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "9256dc1d-bd2a-4b67-8a21-e4f866c1c7ca",
  "toolUseResult": {
    "bytes": 571047,
    "code": 200,
    "codeText": "OK",
    "result": "# UDS: Utility-Diversity Aware Online Batch Selection - Method Overview\n\n## 1. Utility Score Computation (Nuclear Norm)\n\nThe intra-sample importance score uses the nuclear norm of the logits matrix:\n\n> \"s_intra^{t,i} = ||L(x_t^i; θ_t)||_* = Σ σ_j\"\n\nwhere σ_j represents singular values. This captures both optimization utility and intra-sample diversity, with larger nuclear norms correlating to higher loss reduction potential.\n\n## 2. Intra-Sample Diversity Measurement\n\nDiversity within a sample is reflected through the logits matrix structure. The paper notes that \"larger nuclear norm correlates with higher intra-sample diversity\" because low rank (repetitive tokens) yields minimum nuclear norm, while full rank with equal singular values yields maximum nuclear norm. This means diverse token predictions across sequences produce higher nuclear norm values.\n\n## 3. Inter-Sample Diversity Measurement\n\nThe method maintains a First-In-First-Out memory buffer storing compressed logits embeddings:\n\n> \"s_inter^{t,i} = (1/|Q|) Σ ||z_t^i - z_j||_2\"\n\nThese embeddings are created through bilinear random projections using subsampled randomized Fourier transforms, reducing computational complexity from O(NVd) to O((N+V)d log(NV)).\n\n## 4. Score Combination and Batch Selection\n\nThe total score combines both components:\n\n> \"s_total^{t,i} = s_intra^{t,i} + α·s_inter^{t,i}\"\n\nThe top-K samples with highest total scores are selected from the candidate batch.\n\n## 5. Final Scoring Formula\n\nAs stated above, the formula integrates intra-sample utility/diversity with weighted inter-sample diversity through hyperparameter α.\n\n## 6. Evaluation Datasets and Tasks\n\nExperiments use four domains:\n- **MMLU** (general knowledge)\n- **ScienceQA** (scientific reasoning)\n- **GSM8K** (mathematical reasoning)\n- **HumanEval** (code generation)\n\nNo robotics or multimodal tasks are included. Models tested: Llama-3.1-8B and Qwen-2.5-7B with LoRA fine-tuning.\n\n## 7. Stated Limitations\n\nThe paper identifies limitations in Appendix F, noting the method operates within existing datasets and architectures, requiring careful hyperparameter tuning (α varies by dataset/model combination).\n\n## 8. Operational Level\n\nThis method operates at the **sample level** during training. Decisions are made per-sample within each batch, selecting which training instances participate in parameter updates based on computed importance scores.",
    "durationMs": 8580,
    "url": "https://arxiv.org/html/2510.16882"
  },
  "sourceToolAssistantUUID": "1b319376-b510-4ad3-923a-6fcc547c685f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T03:23:08.757Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EFhSUaed19PnEJgn8noGxb`</summary>

```json
{
  "query": "CORDS library coresets data subset selection online training deep learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9256dc1d-bd2a-4b67-8a21-e4f866c1c7ca",
  "isSidechain": false,
  "requestId": "req_011Cb1k7e85rB32RyHW3TScZ",
  "type": "assistant",
  "uuid": "54241887-6c75-4a50-bdcd-4b7fd10f3a85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2YSuXaS58HCcnj6tadyEM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 34442,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 873,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 34442,
          "cache_creation_input_tokens": 873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 873
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

_source line 41 · 2026-05-14T03:23:16.019Z_

<details><summary>↩ Tool result · `toolu_01EFhSUaed19PnEJgn8noGxb`</summary>

```text
Web search results for query: "CORDS library coresets data subset selection online training deep learning"

Links: [{"title":"GitHub - decile-team/cords: Reduce end to end training time from days to hours (or hours to minutes), and energy requirements/costs by an order of magnitude using coresets and data selection. · GitHub","url":"https://github.com/decile-team/cords"},{"title":"Welcome to CORDS’s documentation! — cords v1.0 documentation","url":"https://cords.readthedocs.io/en/latest/"},{"title":"GitHub - PatrickZH/Awesome-Coreset-Selection: Awesome coreset/core-set/subset/sample selection works. · GitHub","url":"https://github.com/PatrickZH/Awesome-Coreset-Selection"},{"title":"cords/README.md at main · decile-team/cords","url":"https://github.com/decile-team/cords/blob/main/README.md"},{"title":"GitHub - gradcshou/cords__cshou: Reduce end to end training time from days to hours (or hours to minutes), and energy requirements/costs by an order of magnitude using coresets and data selection.","url":"https://github.com/gradcshou/cords__cshou"},{"title":"cords/docs/source/index.rst at main · decile-team/cords","url":"https://github.com/decile-team/cords/blob/main/docs/source/index.rst"},{"title":"Awesome-Coreset-Selection/README.md at main · PatrickZH/Awesome-Coreset-Selection","url":"https://github.com/PatrickZH/Awesome-Coreset-Selection/blob/main/README.md"},{"title":"GitHub - rishabhk108/cords: CORDS: COResets and Data Subset selection","url":"https://github.com/rishabhk108/cords"},{"title":"[1906.01827] Coresets for Data-efficient Training of Machine Learning Models","url":"https://arxiv.org/abs/1906.01827"},{"title":"[2204.08499] DeepCore: A Comprehensive Library for Coreset Selection in Deep Learning","url":"https://arxiv.org/abs/2204.08499"}]

Based on the web search results, here's what I found about the CORDS library:

## Overview

CORDS is COReset and Data Selection library for making machine learning time, energy, cost, and compute efficient, built on top of PyTorch.

## Purpose and Goals

The primary purpose of CORDS is to select the suitable representative data subsets from massive datasets, and it does so iteratively. CORDS uses recent advances in data subset selection, particularly ideas of coresets and submodularity to select such subsets.

CORDS implements several state-of-the-art data subset/coreset selection algorithms for efficient supervised learning (SL) and semi-supervised learning (SSL).

## Key Features

The library aims to reduce end-to-end training time from days to hours (or hours to minutes), and energy requirements/costs by an order of magnitude using coresets and data selection.

The data selection algorithms are directly incorporated into data loaders, allowing one to use their own training loop for varied utility scenarios.

## Performance Benefits

On CIFAR-10 dataset using RESNET18, GLISTER (a data subset selection strategy in CORDS) achieves a 6x speedup at 10%, 2.5x speedup at 30%, and 1.5x speedup at 50%, while losing only 3%, 1.2% and 0.2% in terms of accuracy compared to full training.

## Use Cases

CORDS is currently implemented for simple image classification tasks and hyperparameter tuning, with ongoing work on integrating additional use cases like Auto-ML, object detection, speech recognition, and semi-supervised learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54241887-6c75-4a50-bdcd-4b7fd10f3a85",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "cd377661-bd83-40e1-a652-f2d462a51b04",
  "toolUseResult": {
    "query": "CORDS library coresets data subset selection online training deep learning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01D6gfHYU1zXxCNqMUi22CA3",
        "content": [
          {
            "title": "GitHub - decile-team/cords: Reduce end to end training time from days to hours (or hours to minutes), and energy requirements/costs by an order of magnitude using coresets and data selection. · GitHub",
            "url": "https://github.com/decile-team/cords"
          },
          {
            "title": "Welcome to CORDS’s documentation! — cords v1.0 documentation",
            "url": "https://cords.readthedocs.io/en/latest/"
          },
          {
            "title": "GitHub - PatrickZH/Awesome-Coreset-Selection: Awesome coreset/core-set/subset/sample selection works. · GitHub",
            "url": "https://github.com/PatrickZH/Awesome-Coreset-Selection"
          },
          {
            "title": "cords/README.md at main · decile-team/cords",
            "url": "https://github.com/decile-team/cords/blob/main/README.md"
          },
          {
            "title": "GitHub - gradcshou/cords__cshou: Reduce end to end training time from days to hours (or hours to minutes), and energy requirements/costs by an order of magnitude using coresets and data selection.",
            "url": "https://github.com/gradcshou/cords__cshou"
          },
          {
            "title": "cords/docs/source/index.rst at main · decile-team/cords",
            "url": "https://github.com/decile-team/cords/blob/main/docs/source/index.rst"
          },
          {
            "title": "Awesome-Coreset-Selection/README.md at main · PatrickZH/Awesome-Coreset-Selection",
            "url": "https://github.com/PatrickZH/Awesome-Coreset-Selection/blob/main/README.md"
          },
          {
            "title": "GitHub - rishabhk108/cords: CORDS: COResets and Data Subset selection",
            "url": "https://github.com/rishabhk108/cords"
          },
          {
            "title": "[1906.01827] Coresets for Data-efficient Training of Machine Learning Models",
            "url": "https://arxiv.org/abs/1906.01827"
          },
          {
            "title": "[2204.08499] DeepCore: A Comprehensive Library for Coreset Selection in Deep Learning",
            "url": "https://arxiv.org/abs/2204.08499"
          }
        ]
      },
      "Based on the web search results, here's what I found about the CORDS library:\n\n## Overview\n\nCORDS is COReset and Data Selection library for making machine learning time, energy, cost, and compute efficient, built on top of PyTorch.\n\n## Purpose and Goals\n\nThe primary purpose of CORDS is to select the suitable representative data subsets from massive datasets, and it does so iteratively. CORDS uses recent advances in data subset selection, particularly ideas of coresets and submodularity to select such subsets.\n\nCORDS implements several state-of-the-art data subset/coreset selection algorithms for efficient supervised learning (SL) and semi-supervised learning (SSL).\n\n## Key Features\n\nThe library aims to reduce end-to-end training time from days to hours (or hours to minutes), and energy requirements/costs by an order of magnitude using coresets and data selection.\n\nThe data selection algorithms are directly incorporated into data loaders, allowing one to use their own training loop for varied utility scenarios.\n\n## Performance Benefits\n\nOn CIFAR-10 dataset using RESNET18, GLISTER (a data subset selection strategy in CORDS) achieves a 6x speedup at 10%, 2.5x speedup at 30%, and 1.5x speedup at 50%, while losing only 3%, 1.2% and 0.2% in terms of accuracy compared to full training.\n\n## Use Cases\n\nCORDS is currently implemented for simple image classification tasks and hyperparameter tuning, with ongoing work on integrating additional use cases like Auto-ML, object detection, speech recognition, and semi-supervised learning."
    ],
    "durationSeconds": 7.257073657000001
  },
  "sourceToolAssistantUUID": "54241887-6c75-4a50-bdcd-4b7fd10f3a85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T03:23:19.255Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015jSePGuskGd9DDVzskTxCs`</summary>

```json
{
  "query": "\"online data selection\" OR \"online batch selection\" \"vision language action\" OR \"VLA\" OR \"robot imitation learning\" 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd377661-bd83-40e1-a652-f2d462a51b04",
  "isSidechain": false,
  "requestId": "req_011Cb1k8xfpswPWgaRVWLyqC",
  "type": "assistant",
  "uuid": "2e1d4c6f-20a9-47e5-9d39-f12f96ac120f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WyuhHSXRG1ELsuYFavXi1C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1015,
      "cache_read_input_tokens": 35315,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1015,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 35315,
          "cache_creation_input_tokens": 1015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1015
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Beyond Difficulty: Diversity-Aware Dynamic Sampling for Data-Efficient…",
  "leafUuid": "2e1d4c6f-20a9-47e5-9d39-f12f96ac120f",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Benchmark diversity-aware selection methods on VLA BC",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Tool result

_source line 45 · 2026-05-14T03:23:27.773Z_

<details><summary>↩ Tool result · `toolu_015jSePGuskGd9DDVzskTxCs`</summary>

```text
Web search results for query: ""online data selection" OR "online batch selection" "vision language action" OR "VLA" OR "robot imitation learning" 2025 2026"

Links: [{"title":"Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines","url":"https://arxiv.org/html/2604.23001"},{"title":"A Survey on Vision-Language-Action Models for Embodied ...","url":"https://arxiv.org/html/2405.14093v8"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).","url":"https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"},{"title":"Awesome-Robotics-Manipulation/contents/low-level_learning-based_action_modelling.md at main · BaiShuanghao/Awesome-Robotics-Manipulation","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation/blob/main/contents/low-level_learning-based_action_modelling.md"},{"title":"EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos","url":"https://rchalyang.github.io/EgoVLA/"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"10 Open Challenges Steering the Future of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2511.05936"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"}]

I've performed a comprehensive web search on your query about online data selection, online batch selection, vision-language-action models, and robot imitation learning from 2025-2026. Here are the key findings:

## Recent Advances in VLA and Imitation Learning (2025-2026)

Recent advances in robot demonstration datasets and imitation learning have made it more practical to train action policies directly from human demonstrations, with significant progress in the vision-language-action (VLA) field.

### Data Management and Efficiency

Current techniques for efficient data collection address bottlenecks in acquiring and utilizing robotic data through strategies including efficient architectures, model compression, and computational burden reduction during model learning. DataMIL, a method for selecting data for robot imitation learning with datamodels, has been developed, directly addressing the online data selection challenges you asked about.

### Batch Online Approaches

Research on "What Matters for Batch Online Reinforcement Learning in Robotics?" was presented at ICLR 2026, indicating active investigation into batch online learning strategies for robotic systems.

### VLA Model Development

Recent advances have shifted VLA from a largely theoretical direction toward systems that can interact with the physical world and generalize across a wide range of tasks. EgoVLA is a vision-language-action model that combines the broad diversity of human egocentric videos with the precision of robot demonstrations, first pretrained on large-scale human manipulation data.

### Data Generation and Grounding

The primary limitation of current data engines is not generation capacity but grounding reliability, as video-based pipelines depend critically on perception fidelity, and failures in grounding, pose estimation, and depth reconstruction introduce systematic noise that propagates into policy learning.

The search results show active research into more efficient, scalable approaches to robot learning through improved data selection and online learning strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e1d4c6f-20a9-47e5-9d39-f12f96ac120f",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "7b27b91d-4291-4fc9-b447-d8e2c59b4a5b",
  "toolUseResult": {
    "query": "\"online data selection\" OR \"online batch selection\" \"vision language action\" OR \"VLA\" OR \"robot imitation learning\" 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XY4xMttANH2BGaBsoKBbJD",
        "content": [
          {
            "title": "Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines",
            "url": "https://arxiv.org/html/2604.23001"
          },
          {
            "title": "A Survey on Vision-Language-Action Models for Embodied ...",
            "url": "https://arxiv.org/html/2405.14093v8"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).",
            "url": "https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"
          },
          {
            "title": "Awesome-Robotics-Manipulation/contents/low-level_learning-based_action_modelling.md at main · BaiShuanghao/Awesome-Robotics-Manipulation",
            "url": "https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation/blob/main/contents/low-level_learning-based_action_modelling.md"
          },
          {
            "title": "EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos",
            "url": "https://rchalyang.github.io/EgoVLA/"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "World Model for Robot Learning: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2605.00080v1"
          },
          {
            "title": "10 Open Challenges Steering the Future of Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2511.05936"
          },
          {
            "title": "A Survey on Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.24795v1"
          }
        ]
      },
      "I've performed a comprehensive web search on your query about online data selection, online batch selection, vision-language-action models, and robot imitation learning from 2025-2026. Here are the key findings:\n\n## Recent Advances in VLA and Imitation Learning (2025-2026)\n\nRecent advances in robot demonstration datasets and imitation learning have made it more practical to train action policies directly from human demonstrations, with significant progress in the vision-language-action (VLA) field.\n\n### Data Management and Efficiency\n\nCurrent techniques for efficient data collection address bottlenecks in acquiring and utilizing robotic data through strategies including efficient architectures, model compression, and computational burden reduction during model learning. DataMIL, a method for selecting data for robot imitation learning with datamodels, has been developed, directly addressing the online data selection challenges you asked about.\n\n### Batch Online Approaches\n\nResearch on \"What Matters for Batch Online Reinforcement Learning in Robotics?\" was presented at ICLR 2026, indicating active investigation into batch online learning strategies for robotic systems.\n\n### VLA Model Development\n\nRecent advances have shifted VLA from a largely theoretical direction toward systems that can interact with the physical world and generalize across a wide range of tasks. EgoVLA is a vision-language-action model that combines the broad diversity of human egocentric videos with the precision of robot demonstrations, first pretrained on large-scale human manipulation data.\n\n### Data Generation and Grounding\n\nThe primary limitation of current data engines is not generation capacity but grounding reliability, as video-based pipelines depend critically on perception fidelity, and failures in grounding, pose estimation, and depth reconstruction introduce systematic noise that propagates into policy learning.\n\nThe search results show active research into more efficient, scalable approaches to robot learning through improved data selection and online learning strategies."
    ],
    "durationSeconds": 8.513640258999978
  },
  "sourceToolAssistantUUID": "2e1d4c6f-20a9-47e5-9d39-f12f96ac120f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T03:23:30.844Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U6JP8TterHT9bAzCkiQYGU`</summary>

```json
{
  "query": "GLISTER CRAIG coreset selection applied robotics imitation learning multi-modal limitations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b27b91d-4291-4fc9-b447-d8e2c59b4a5b",
  "isSidechain": false,
  "requestId": "req_011Cb1k9qBeW3Q343URShXKo",
  "type": "assistant",
  "uuid": "ad8176f0-1379-4f72-934b-2f71306f5074",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y1Q6pCyMYJxv3V7k2Hi1sR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 36330,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 36330,
          "cache_creation_input_tokens": 1143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1143
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

_source line 47 · 2026-05-14T03:23:37.285Z_

<details><summary>↩ Tool result · `toolu_01U6JP8TterHT9bAzCkiQYGU`</summary>

```text
Web search results for query: "GLISTER CRAIG coreset selection applied robotics imitation learning multi-modal limitations"

Links: [{"title":"GLISTER: Generalization based Data Subset Selection for Efﬁcient and Robust","url":"https://ojs.aaai.org/index.php/AAAI/article/view/16988/16795"},{"title":"A Coreset Selection of Coreset Selection Literature: Introduction and Recent Advances","url":"https://arxiv.org/html/2505.17799v1"},{"title":"GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning | Request PDF","url":"https://www.researchgate.net/publication/363394079_GLISTER_Generalization_based_Data_Subset_Selection_for_Efficient_and_Robust_Learning"},{"title":"[PDF] GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GLISTER:-Generalization-based-Data-Subset-Selection-Killamsetty-Sivasubramanian/199ac333b1ff37917d1ab4a2e2002d9605b3db1e"},{"title":"(PDF) GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning","url":"https://www.researchgate.net/publication/347534567_GLISTER_Generalization_based_Data_Subset_Selection_for_Efficient_and_Robust_Learning"},{"title":"RETRIEVE: Coreset Selection for Efﬁcient and Robust Semi-Supervised Learning","url":"https://par.nsf.gov/servlets/purl/10323505"},{"title":"Robot skill learning: imitation, exploitation and control | RobotSL | Project | Fact Sheet | H2020 | CORDIS | European Commission","url":"https://cordis.europa.eu/project/id/101018395"},{"title":"[2012.10630] GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning","url":"https://arxiv.org/abs/2012.10630"},{"title":"Ch. 21 - Imitation Learning - Underactuated Robotics","url":"https://underactuated.mit.edu/imitation.html"},{"title":"Cross-Modal Instructions for Robot Motion Generation","url":"https://arxiv.org/html/2509.21107"}]

Based on the web search results, I found comprehensive information about GLISTER and CRAIG as coreset selection methods. Here's what I found:

## Overview of GLISTER and CRAIG

CRAIG (Coresets for Accelerating Incremental Gradient Descent) is a coreset selection method designed to select a subset of data points whose weighted gradients closely approximate the gradient of the full dataset.

GLISTER (GeneraLIzation-based data Subset selecTion for Efficient and Robust learning) selects a subset that maximizes log-likelihood performance on a held-out validation set rather than just the training set, which prioritizes generalization while maintaining efficiency.

## Key Comparison

GLISTER and its variants significantly outperform all other baselines (including CRAIG and Random). CRAIG performs very poorly at small data-sizes, while GLISTER-ONLINE performs well even at very small subset sizes.

## Robotics and Imitation Learning Context

While the search results contain general information about coreset selection methods, they don't specifically address applications to robotics imitation learning or multi-modal limitations in detail. The results do show that GLISTER has been demonstrated on a wide range of tasks including data selection to reduce training time, robust learning under label noise and imbalance settings, and batch-active learning with several deep and shallow models.

For specific information about applications to applied robotics with imitation learning and multi-modal data limitations, the current search results don't provide detailed coverage of those particular aspects.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad8176f0-1379-4f72-934b-2f71306f5074",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "1f8aaa5d-2773-4827-8263-73d5a6484ce1",
  "toolUseResult": {
    "query": "GLISTER CRAIG coreset selection applied robotics imitation learning multi-modal limitations",
    "results": [
      {
        "tool_use_id": "srvtoolu_017ECMZYBYfK8vNFRPyYJ1H2",
        "content": [
          {
            "title": "GLISTER: Generalization based Data Subset Selection for Efﬁcient and Robust",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/16988/16795"
          },
          {
            "title": "A Coreset Selection of Coreset Selection Literature: Introduction and Recent Advances",
            "url": "https://arxiv.org/html/2505.17799v1"
          },
          {
            "title": "GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning | Request PDF",
            "url": "https://www.researchgate.net/publication/363394079_GLISTER_Generalization_based_Data_Subset_Selection_for_Efficient_and_Robust_Learning"
          },
          {
            "title": "[PDF] GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GLISTER:-Generalization-based-Data-Subset-Selection-Killamsetty-Sivasubramanian/199ac333b1ff37917d1ab4a2e2002d9605b3db1e"
          },
          {
            "title": "(PDF) GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning",
            "url": "https://www.researchgate.net/publication/347534567_GLISTER_Generalization_based_Data_Subset_Selection_for_Efficient_and_Robust_Learning"
          },
          {
            "title": "RETRIEVE: Coreset Selection for Efﬁcient and Robust Semi-Supervised Learning",
            "url": "https://par.nsf.gov/servlets/purl/10323505"
          },
          {
            "title": "Robot skill learning: imitation, exploitation and control | RobotSL | Project | Fact Sheet | H2020 | CORDIS | European Commission",
            "url": "https://cordis.europa.eu/project/id/101018395"
          },
          {
            "title": "[2012.10630] GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning",
            "url": "https://arxiv.org/abs/2012.10630"
          },
          {
            "title": "Ch. 21 - Imitation Learning - Underactuated Robotics",
            "url": "https://underactuated.mit.edu/imitation.html"
          },
          {
            "title": "Cross-Modal Instructions for Robot Motion Generation",
            "url": "https://arxiv.org/html/2509.21107"
          }
        ]
      },
      "Based on the web search results, I found comprehensive information about GLISTER and CRAIG as coreset selection methods. Here's what I found:\n\n## Overview of GLISTER and CRAIG\n\nCRAIG (Coresets for Accelerating Incremental Gradient Descent) is a coreset selection method designed to select a subset of data points whose weighted gradients closely approximate the gradient of the full dataset.\n\nGLISTER (GeneraLIzation-based data Subset selecTion for Efficient and Robust learning) selects a subset that maximizes log-likelihood performance on a held-out validation set rather than just the training set, which prioritizes generalization while maintaining efficiency.\n\n## Key Comparison\n\nGLISTER and its variants significantly outperform all other baselines (including CRAIG and Random). CRAIG performs very poorly at small data-sizes, while GLISTER-ONLINE performs well even at very small subset sizes.\n\n## Robotics and Imitation Learning Context\n\nWhile the search results contain general information about coreset selection methods, they don't specifically address applications to robotics imitation learning or multi-modal limitations in detail. The results do show that GLISTER has been demonstrated on a wide range of tasks including data selection to reduce training time, robust learning under label noise and imbalance settings, and batch-active learning with several deep and shallow models.\n\nFor specific information about applications to applied robotics with imitation learning and multi-modal data limitations, the current search results don't provide detailed coverage of those particular aspects."
    ],
    "durationSeconds": 6.435801800999994
  },
  "sourceToolAssistantUUID": "ad8176f0-1379-4f72-934b-2f71306f5074",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T03:23:39.837Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012Ssr2rYosZvgWvYf9eFnKr`</summary>

```json
{
  "query": "coreset selection action chunking temporal sequences robot manipulation behavior cloning challenges"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f8aaa5d-2773-4827-8263-73d5a6484ce1",
  "isSidechain": false,
  "requestId": "req_011Cb1kAXb1TJABjUTp4abG3",
  "type": "assistant",
  "uuid": "8a5adc77-c583-4c29-b086-6bb074525b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RjfDb51BXUBam6tnYsF4wJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1033,
      "cache_read_input_tokens": 37473,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 37473,
          "cache_creation_input_tokens": 1033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1033
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

_source line 49 · 2026-05-14T03:23:46.922Z_

<details><summary>↩ Tool result · `toolu_012Ssr2rYosZvgWvYf9eFnKr`</summary>

```text
Web search results for query: "coreset selection action chunking temporal sequences robot manipulation behavior cloning challenges"

Links: [{"title":"ACT Policy Explained (2026): Action Chunking with Transformers | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/blog/act-policy-explained"},{"title":"Revolutionizing Robot Behavior: How Transformers Elevate Imitation Learning with Action Chunking","url":"https://www.trossenrobotics.com/post/revolutionizing-robot-behavior-how-transformers-elevate-imitation-learning-with-action-chunking"},{"title":"[2309.10175] One ACT Play: Single Demonstration Behavior Cloning with Action Chunking Transformers","url":"https://ar5iv.labs.arxiv.org/html/2309.10175"},{"title":"CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation","url":"https://arxiv.org/html/2508.01600"},{"title":"Improving Generative Behavior Cloning via Self-Guidance and Adaptive Chunking","url":"https://arxiv.org/html/2510.12392v1"},{"title":"Bi-ACT: Bilateral Control-Based Imitation Learning Via Action ...","url":"https://ras.papercept.net/images/temp/AIM/files/0129.pdf"},{"title":"Learning Fine-Grained Bimanual Manipulation with Low- ...","url":"https://www.roboticsproceedings.org/rss19/p016.pdf"},{"title":"Improving Generative Behavior Cloning via Self-Guidance and Adaptive Chunking | OpenReview","url":"https://openreview.net/forum?id=GctsZXLCpl"},{"title":"Action chunking with Transformers (ACT) robot policy | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/action-chunking-with-transformers-act-robot-policy-80519fc024bc"},{"title":"Temporal Action Selection for Action Chunking","url":"https://arxiv.org/html/2511.04421"}]

I've completed a web search for your query about action chunking, temporal sequences, robot manipulation, and behavior cloning. Here's a summary of the key findings:

## Key Concepts and Challenges

**Action Chunking Overview:**
Action chunking breaks down the prediction cycle by predicting a sequence of k future actions — typically 50–100 steps at 50 Hz, corresponding to 1–2 seconds of motion. Action chunking is a widely adopted approach in Learning from Demonstration (LfD), where by modeling multi-step action chunks rather than single-step actions, action chunking significantly enhances modeling capabilities for human expert policies.

**Core Challenges with Behavior Cloning:**
At inference time, prediction errors accumulate: each small mistake shifts the robot's state slightly, putting it in a distribution the policy was not trained on, which causes the next prediction to be worse, and so on—this compounding error is the central failure mode of naive BC on fine manipulation tasks.

**Temporal Sequence Handling:**
Time series data inherently contains temporal dependencies, where previous states or actions influence the current state or action, and understanding these dependencies is crucial in imitation learning, particularly for tasks that involve sequences of actions like walking, manipulating objects, or driving.

**Recent Advances:**
Novel techniques to enhance consistency and reactivity include self-guidance, which improves action fidelity by leveraging past observations and implicitly promoting future-aware behavior, and adaptive chunking, which selectively updates action sequences when the benefits of reactivity outweigh the need for temporal consistency.

**Reactivity vs. Consistency Trade-off:**
The reduced decision frequency in action chunking restricts the utilization of recent observations, degrading reactivity—particularly evident in the inadequate adaptation to sensor noise and dynamic environmental changes, and existing efforts have primarily resorted to trading off reactivity against decision consistency, without achieving both.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a5adc77-c583-4c29-b086-6bb074525b17",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "820ea9da-1525-4822-8073-af3cad347e8d",
  "toolUseResult": {
    "query": "coreset selection action chunking temporal sequences robot manipulation behavior cloning challenges",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JFrLM6CxkA3GFqP9mxeoff",
        "content": [
          {
            "title": "ACT Policy Explained (2026): Action Chunking with Transformers | Silicon Valley Robotics Center",
            "url": "https://www.roboticscenter.ai/blog/act-policy-explained"
          },
          {
            "title": "Revolutionizing Robot Behavior: How Transformers Elevate Imitation Learning with Action Chunking",
            "url": "https://www.trossenrobotics.com/post/revolutionizing-robot-behavior-how-transformers-elevate-imitation-learning-with-action-chunking"
          },
          {
            "title": "[2309.10175] One ACT Play: Single Demonstration Behavior Cloning with Action Chunking Transformers",
            "url": "https://ar5iv.labs.arxiv.org/html/2309.10175"
          },
          {
            "title": "CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation",
            "url": "https://arxiv.org/html/2508.01600"
          },
          {
            "title": "Improving Generative Behavior Cloning via Self-Guidance and Adaptive Chunking",
            "url": "https://arxiv.org/html/2510.12392v1"
          },
          {
            "title": "Bi-ACT: Bilateral Control-Based Imitation Learning Via Action ...",
            "url": "https://ras.papercept.net/images/temp/AIM/files/0129.pdf"
          },
          {
            "title": "Learning Fine-Grained Bimanual Manipulation with Low- ...",
            "url": "https://www.roboticsproceedings.org/rss19/p016.pdf"
          },
          {
            "title": "Improving Generative Behavior Cloning via Self-Guidance and Adaptive Chunking | OpenReview",
            "url": "https://openreview.net/forum?id=GctsZXLCpl"
          },
          {
            "title": "Action chunking with Transformers (ACT) robot policy | by Deepthi Karkada | Medium",
            "url": "https://medium.com/@deepkarkada/action-chunking-with-transformers-act-robot-policy-80519fc024bc"
          },
          {
            "title": "Temporal Action Selection for Action Chunking",
            "url": "https://arxiv.org/html/2511.04421"
          }
        ]
      },
      "I've completed a web search for your query about action chunking, temporal sequences, robot manipulation, and behavior cloning. Here's a summary of the key findings:\n\n## Key Concepts and Challenges\n\n**Action Chunking Overview:**\nAction chunking breaks down the prediction cycle by predicting a sequence of k future actions — typically 50–100 steps at 50 Hz, corresponding to 1–2 seconds of motion. Action chunking is a widely adopted approach in Learning from Demonstration (LfD), where by modeling multi-step action chunks rather than single-step actions, action chunking significantly enhances modeling capabilities for human expert policies.\n\n**Core Challenges with Behavior Cloning:**\nAt inference time, prediction errors accumulate: each small mistake shifts the robot's state slightly, putting it in a distribution the policy was not trained on, which causes the next prediction to be worse, and so on—this compounding error is the central failure mode of naive BC on fine manipulation tasks.\n\n**Temporal Sequence Handling:**\nTime series data inherently contains temporal dependencies, where previous states or actions influence the current state or action, and understanding these dependencies is crucial in imitation learning, particularly for tasks that involve sequences of actions like walking, manipulating objects, or driving.\n\n**Recent Advances:**\nNovel techniques to enhance consistency and reactivity include self-guidance, which improves action fidelity by leveraging past observations and implicitly promoting future-aware behavior, and adaptive chunking, which selectively updates action sequences when the benefits of reactivity outweigh the need for temporal consistency.\n\n**Reactivity vs. Consistency Trade-off:**\nThe reduced decision frequency in action chunking restricts the utilization of recent observations, degrading reactivity—particularly evident in the inadequate adaptation to sensor noise and dynamic environmental changes, and existing efforts have primarily resorted to trading off reactivity against decision consistency, without achieving both."
    ],
    "durationSeconds": 7.0791972940000125
  },
  "sourceToolAssistantUUID": "8a5adc77-c583-4c29-b086-6bb074525b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T03:23:49.779Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S6oZPYxrfncku3YDRbGyoh`</summary>

```json
{
  "query": "\"on data redundancy in VLA training\" ICRA 2026 workshop paper LIBERO temporal surprise score"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "820ea9da-1525-4822-8073-af3cad347e8d",
  "isSidechain": false,
  "requestId": "req_011Cb1kBEriQAr9u4jYQ4sK5",
  "type": "assistant",
  "uuid": "18f3a9ea-324d-46ae-95b1-dd332eb082bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NXA8BrARTUBNwA2yToawbZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 38506,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1034,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 38506,
          "cache_creation_input_tokens": 1034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1034
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

_source line 51 · 2026-05-14T03:23:56.911Z_

<details><summary>↩ Tool result · `toolu_01S6oZPYxrfncku3YDRbGyoh`</summary>

```text
Web search results for query: ""on data redundancy in VLA training" ICRA 2026 workshop paper LIBERO temporal surprise score"

Links: [{"title":"ON DATA REDUNDANCY IN VLA TRAINING","url":"https://openreview.net/pdf/ab993a111c866b80680b9e9ba5a435cf58ea3408.pdf"},{"title":"From Data to Decisions: VLA Pipelines for Real Robots - ICRA 2026 Workshop","url":"https://icra2026vlapipeline.github.io/"},{"title":"AIRoA Announces ICRA 2026 Workshop — Launching a Global Competition on VLA Pipelines and Approximately 10,000 Hours of Real-World Robot Data — | AIRoA","url":"https://www.airoa.org/updates/2026-02-10"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"ICRA 2026 Workshop: VLA Pipelines for Real Robot Systems","url":"https://www.linkedin.com/posts/junjungoal_from-data-to-decisions-vla-pipelines-for-activity-7426285548333453312-m_hV"},{"title":"GitHub - Ed1sonChen/DailyArxiv · GitHub","url":"https://github.com/Ed1sonChen/DailyArxiv"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"2026-01-28 Work in progress.","url":"https://arxiv.org/pdf/2601.15197"},{"title":"IEEE ICRA 2026 Workshop From Data to Decisions | OpenReview","url":"https://openreview.net/group?id=IEEE.org%2FICRA%2F2026%2FWorkshop%2FFrom_Data_to_Decisions"},{"title":"GitHub - ZZongzheng0918/Dexora: ICRA 2026: Dexora: Open-source VLA for High-DoF Bimanual Dexterity","url":"https://github.com/ZZongzheng0918/Dexora"}]

Based on the search results, I found the paper you're looking for!

## "On Data Redundancy in VLA Training"

This paper empirically evaluates data selection methods on the LIBERO benchmark, including a temporal surprise score (TSS), which is a difficulty-based sampling approach.

### Key Findings:

**Temporal Surprise Score (TSS):**
The authors hypothesize that an effective data selection strategy should prioritize "temporal surprise", or moments where action trajectories undergo significant shifts, proposing Temporal Surprise Score (TSS) as a metric that scores frames based on a weighted calculation of action change. TSS identifies high-volatility action frames and selects them as dense, continuous clusters (including temporal neighbors) while discarding low-information transit frames.

**Main Results:**
Random sampling shows that a sparse 30% coverage of the dataset is sufficient to match the performance of the full dataset. However, random sampling matches, and in some cases exceeds, full dataset performance, while difficulty-based sampling underperforms both. This suggests that maintaining broad coverage across diverse scenarios is more crucial than targeting difficult frames for VLA training.

### Publication Context:

This workshop paper was accepted for presentation at ICRA 2026, which will be held in Vienna, Austria, from June 1–5, 2026, at the "From Data to Decisions: VLA Pipelines for Real Robots" workshop.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18f3a9ea-324d-46ae-95b1-dd332eb082bf",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "1a161cb3-f21a-46a2-8067-ed787dede4a8",
  "toolUseResult": {
    "query": "\"on data redundancy in VLA training\" ICRA 2026 workshop paper LIBERO temporal surprise score",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MbDBkee9VuhSnJBRqu7xj3",
        "content": [
          {
            "title": "ON DATA REDUNDANCY IN VLA TRAINING",
            "url": "https://openreview.net/pdf/ab993a111c866b80680b9e9ba5a435cf58ea3408.pdf"
          },
          {
            "title": "From Data to Decisions: VLA Pipelines for Real Robots - ICRA 2026 Workshop",
            "url": "https://icra2026vlapipeline.github.io/"
          },
          {
            "title": "AIRoA Announces ICRA 2026 Workshop — Launching a Global Competition on VLA Pipelines and Approximately 10,000 Hours of Real-World Robot Data — | AIRoA",
            "url": "https://www.airoa.org/updates/2026-02-10"
          },
          {
            "title": "EfficientVLA: Training-Free Acceleration and Compression ...",
            "url": "https://openreview.net/pdf?id=SELYlDHZk2"
          },
          {
            "title": "ICRA 2026 Workshop: VLA Pipelines for Real Robot Systems",
            "url": "https://www.linkedin.com/posts/junjungoal_from-data-to-decisions-vla-pipelines-for-activity-7426285548333453312-m_hV"
          },
          {
            "title": "GitHub - Ed1sonChen/DailyArxiv · GitHub",
            "url": "https://github.com/Ed1sonChen/DailyArxiv"
          },
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          },
          {
            "title": "2026-01-28 Work in progress.",
            "url": "https://arxiv.org/pdf/2601.15197"
          },
          {
            "title": "IEEE ICRA 2026 Workshop From Data to Decisions | OpenReview",
            "url": "https://openreview.net/group?id=IEEE.org%2FICRA%2F2026%2FWorkshop%2FFrom_Data_to_Decisions"
          },
          {
            "title": "GitHub - ZZongzheng0918/Dexora: ICRA 2026: Dexora: Open-source VLA for High-DoF Bimanual Dexterity",
            "url": "https://github.com/ZZongzheng0918/Dexora"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for!\n\n## \"On Data Redundancy in VLA Training\"\n\nThis paper empirically evaluates data selection methods on the LIBERO benchmark, including a temporal surprise score (TSS), which is a difficulty-based sampling approach.\n\n### Key Findings:\n\n**Temporal Surprise Score (TSS):**\nThe authors hypothesize that an effective data selection strategy should prioritize \"temporal surprise\", or moments where action trajectories undergo significant shifts, proposing Temporal Surprise Score (TSS) as a metric that scores frames based on a weighted calculation of action change. TSS identifies high-volatility action frames and selects them as dense, continuous clusters (including temporal neighbors) while discarding low-information transit frames.\n\n**Main Results:**\nRandom sampling shows that a sparse 30% coverage of the dataset is sufficient to match the performance of the full dataset. However, random sampling matches, and in some cases exceeds, full dataset performance, while difficulty-based sampling underperforms both. This suggests that maintaining broad coverage across diverse scenarios is more crucial than targeting difficult frames for VLA training.\n\n### Publication Context:\n\nThis workshop paper was accepted for presentation at ICRA 2026, which will be held in Vienna, Austria, from June 1–5, 2026, at the \"From Data to Decisions: VLA Pipelines for Real Robots\" workshop."
    ],
    "durationSeconds": 7.128531702000007
  },
  "sourceToolAssistantUUID": "18f3a9ea-324d-46ae-95b1-dd332eb082bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Beyond Difficulty: Diversity-Aware Dynamic Sampling for Data-Efficient…",
  "leafUuid": "1a161cb3-f21a-46a2-8067-ed787dede4a8",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Benchmark diversity-aware selection methods on VLA BC",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Tool call

_source line 54 · 2026-05-14T03:24:01.182Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019RzPykSooEdYn9pprXoFfK`</summary>

```json
{
  "query": "VLA training data efficiency diversity aware selection 2025 2026 latest methods"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a161cb3-f21a-46a2-8067-ed787dede4a8",
  "isSidechain": false,
  "requestId": "req_011Cb1kByWGD34uLM4fzrQwm",
  "type": "assistant",
  "uuid": "1c3c8808-368b-4e47-a709-05fab98031ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sbLz2uK4fTpnPFcLncePP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1007,
      "cache_read_input_tokens": 39540,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1007,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 39540,
          "cache_creation_input_tokens": 1007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1007
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

_source line 55 · 2026-05-14T03:24:09.511Z_

<details><summary>↩ Tool result · `toolu_019RzPykSooEdYn9pprXoFfK`</summary>

```text
Web search results for query: "VLA training data efficiency diversity aware selection 2025 2026 latest methods"

Links: [{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"A Pragmatic VLA Foundation Model","url":"https://arxiv.org/html/2601.18692v1"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"},{"title":"2025-9-22 A Vision-Language-Action-Critic Model","url":"https://arxiv.org/pdf/2509.15937"},{"title":"What are Vision Language Action (VLA) Models? Complete Guide","url":"https://www.articsledge.com/post/vision-language-action-vla-models"},{"title":"Efficient Vision-Language-Action Models for Embodied ...","url":"https://arxiv.org/pdf/2510.17111"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/html/2512.06951v1"},{"title":"10 Open Challenges Steering the Future of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2511.05936"}]

Based on the search results, here are the latest methods and approaches in VLA (Vision-Language-Action) training data efficiency and diversity-aware selection for 2025-2026:

## Key Recent Approaches

### Diversity-Aware Visual Token Selection

A prominent approach involves anchoring selection with task-critical tokens identified via attention analysis, then augmenting this core set by balancing task relevance with explicit promotion of feature diversity through similarity measures. This systematic reduction in visual sequence length significantly alleviates computational demands while preserving critical task-specific and diverse visual information.

### Large-Scale Diverse Datasets

Recent VLA foundation models are pre-trained on extensive corpora of approximately 20,000 hours of multi-embodiment data characterized by high behavioral diversity, which significantly bolsters the model's generalization capabilities across various robotic manipulation tasks. Large and diverse real-world robot datasets such as Open X-Embodiment (OXE) and DROID provide the data support needed to train increasingly large models.

### Training Efficiency Improvements

OpenVLA can be fine-tuned on consumer GPUs via modern low-rank adaptation methods and served efficiently via quantization without a hit to downstream success rate.

### Multi-Task Training Benefits

Training on multiple tasks improves generalization and enables transfer learning, where large-scale multi-task training shows benefits including the model learning recovery behaviors that aren't explicitly present in single-task demonstrations, hypothesized to result from exposure to a wide variety of states and transitions.

### Recent Architectures

Analysis of 164 Vision-Language-Action model submissions at ICLR 2026 reveal trends in discrete diffusion VLAs, reasoning models, and the gap between frontier and academic research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c3c8808-368b-4e47-a709-05fab98031ac",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "4e5bc3cb-a995-431b-a94f-ffbb88de4bb5",
  "toolUseResult": {
    "query": "VLA training data efficiency diversity aware selection 2025 2026 latest methods",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BoxXdbdyraDmD7tw4wJngN",
        "content": [
          {
            "title": "[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://arxiv.org/abs/2406.09246"
          },
          {
            "title": "A Pragmatic VLA Foundation Model",
            "url": "https://arxiv.org/html/2601.18692v1"
          },
          {
            "title": "EfficientVLA: Training-Free Acceleration and Compression ...",
            "url": "https://openreview.net/pdf?id=SELYlDHZk2"
          },
          {
            "title": "VQ-VLA: Improving Vision-Language-Action Models via Scaling",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"
          },
          {
            "title": "2025-9-22 A Vision-Language-Action-Critic Model",
            "url": "https://arxiv.org/pdf/2509.15937"
          },
          {
            "title": "What are Vision Language Action (VLA) Models? Complete Guide",
            "url": "https://www.articsledge.com/post/vision-language-action-vla-models"
          },
          {
            "title": "Efficient Vision-Language-Action Models for Embodied ...",
            "url": "https://arxiv.org/pdf/2510.17111"
          },
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          },
          {
            "title": "Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge",
            "url": "https://arxiv.org/html/2512.06951v1"
          },
          {
            "title": "10 Open Challenges Steering the Future of Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2511.05936"
          }
        ]
      },
      "Based on the search results, here are the latest methods and approaches in VLA (Vision-Language-Action) training data efficiency and diversity-aware selection for 2025-2026:\n\n## Key Recent Approaches\n\n### Diversity-Aware Visual Token Selection\n\nA prominent approach involves anchoring selection with task-critical tokens identified via attention analysis, then augmenting this core set by balancing task relevance with explicit promotion of feature diversity through similarity measures. This systematic reduction in visual sequence length significantly alleviates computational demands while preserving critical task-specific and diverse visual information.\n\n### Large-Scale Diverse Datasets\n\nRecent VLA foundation models are pre-trained on extensive corpora of approximately 20,000 hours of multi-embodiment data characterized by high behavioral diversity, which significantly bolsters the model's generalization capabilities across various robotic manipulation tasks. Large and diverse real-world robot datasets such as Open X-Embodiment (OXE) and DROID provide the data support needed to train increasingly large models.\n\n### Training Efficiency Improvements\n\nOpenVLA can be fine-tuned on consumer GPUs via modern low-rank adaptation methods and served efficiently via quantization without a hit to downstream success rate.\n\n### Multi-Task Training Benefits\n\nTraining on multiple tasks improves generalization and enables transfer learning, where large-scale multi-task training shows benefits including the model learning recovery behaviors that aren't explicitly present in single-task demonstrations, hypothesized to result from exposure to a wide variety of states and transitions.\n\n### Recent Architectures\n\nAnalysis of 164 Vision-Language-Action model submissions at ICLR 2026 reveal trends in discrete diffusion VLAs, reasoning models, and the gap between frontier and academic research."
    ],
    "durationSeconds": 8.323990172999999
  },
  "sourceToolAssistantUUID": "1c3c8808-368b-4e47-a709-05fab98031ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 56 · 2026-05-14T03:24:09.516Z_

```json
{
  "parentUuid": "4e5bc3cb-a995-431b-a94f-ffbb88de4bb5",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fa6cb4ad-7f1e-4005-81fa-fc96df927701",
  "timestamp": "2026-05-14T03:24:09.516Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 57 · 2026-05-14T03:24:12.814Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Nw2zBBWh24Ns6TMa7CJ3ch`</summary>

```json
{
  "query": "submodular function optimization multi-modal action prediction robot heterogeneous data structure challenges"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa6cb4ad-7f1e-4005-81fa-fc96df927701",
  "isSidechain": false,
  "requestId": "req_011Cb1kCuMWYBMJs9uBqs5kA",
  "type": "assistant",
  "uuid": "e28e6770-c1ac-4266-a89a-851a938f1681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Edm9UN9WLvQ8iREfqxSKk1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1077,
      "cache_read_input_tokens": 40547,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1077,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 40547,
          "cache_creation_input_tokens": 1077,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1077
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

_source line 58 · 2026-05-14T03:24:19.496Z_

<details><summary>↩ Tool result · `toolu_01Nw2zBBWh24Ns6TMa7CJ3ch`</summary>

```text
Web search results for query: "submodular function optimization multi-modal action prediction robot heterogeneous data structure challenges"

Links: [{"title":"[2310.01519] Decision-Oriented Learning Using Differentiable Submodular Maximization for Multi-Robot Coordination","url":"https://arxiv.org/abs/2310.01519"},{"title":"Resource-Aware Distributed Submodular Maximization: A Paradigm for Multi-Robot Decision-Making","url":"https://arxiv.org/html/2204.07520"},{"title":"Decision-Oriented Learning Using Differentiable Submodular Maximization for Multi-Robot Coordination This work is supported in part by National Science Foundation Grant No. 1943368 and Army Grant No. W911NF2120076. 1University of Southern California, Los Angels, CA 90007 USA shig@usc.edu. The author was with the Department of Electrical and Computer Engineering, University of Maryland, College Park, MD, USA, when part of the work was completed. 2University of Maryland, College Park, MD 20742 USA [cshek1, to","url":"https://arxiv.org/html/2310.01519"},{"title":"A Distributed Algorithm for Robust Sequential Submodular Optimization in Multi-robot Systems | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-4839-2_13"},{"title":"A Distributed Algorithm for Robust Sequential Submodular Optimization in Multi-robot Systems","url":"https://www.researchgate.net/publication/399375458_A_Distributed_Algorithm_for_Robust_Sequential_Submodular_Optimization_in_Multi-robot_Systems"},{"title":"Frontiers | Multimodal Hierarchical Dirichlet Process-Based Active Perception by a Robot","url":"https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2018.00022/full"},{"title":"[1910.01208] Distributed Attack-Robust Submodular Maximization for Multi-Robot Planning","url":"https://arxiv.org/abs/1910.01208"},{"title":"(PDF) Distributed Attack-Robust Submodular Maximization for Multi-Robot Planning","url":"https://www.researchgate.net/publication/336251073_Distributed_Attack-Robust_Submodular_Maximization_for_Multi-Robot_Planning"},{"title":"dblp: Fast Semidifferential-based Submodular Function Optimization.","url":"https://dblp.org/rec/conf/icml/IyerJB13.html"},{"title":"[2407.10382] Communication- and Computation-Efficient Distributed Submodular Optimization in Robot Mesh Networks","url":"https://arxiv.org/abs/2407.10382"}]

Based on the web search results, I found several relevant research papers and topics on submodular function optimization in multi-robot systems. Here's what I found:

## Submodular Function Optimization in Multi-Robot Systems

Research in this area is motivated by the future of autonomy that involves heterogeneous robots collaborating in complex tasks, such as image covering, target tracking, and area monitoring.

### Key Challenges with Heterogeneous Data Structures

The robots' heterogeneous capabilities (speed, size, on-board cameras, etc.) offer tremendous advantages; for example, in the image covering scenario, tiny robots offer the advantage of agility for navigating narrow spaces, while larger robots offer the advantages of reliability with higher-resolution cameras. However, heterogeneity in capabilities also implies heterogeneity in on-board resources (tiny robots have limited computation, communication, and memory resources), and mere distributed communication among the robots is insufficient for the success of their tasks.

### Multi-Modal Action Prediction

Information Gain (IG) has a submodular and non-decreasing property as a set function; therefore, greedy and lazy greedy algorithms are guaranteed to be near-optimal strategies. Additionally, the evaluation criterion for multimodal active perception is a submodular and non-decreasing function.

### Resource-Aware Distributed Optimization

Submodularity is a property of diminishing returns that arises in active information gathering such as mapping, surveillance, and target tracking, and Resource-Aware distributed Greedy (RAG) introduces a new distributed optimization paradigm that enables scalable and near-optimal action coordination.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e28e6770-c1ac-4266-a89a-851a938f1681",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "2a954cf9-226e-4627-91ba-345e4ad34bc0",
  "toolUseResult": {
    "query": "submodular function optimization multi-modal action prediction robot heterogeneous data structure challenges",
    "results": [
      {
        "tool_use_id": "srvtoolu_019HoLPQDdwgKeF53yYehy7v",
        "content": [
          {
            "title": "[2310.01519] Decision-Oriented Learning Using Differentiable Submodular Maximization for Multi-Robot Coordination",
            "url": "https://arxiv.org/abs/2310.01519"
          },
          {
            "title": "Resource-Aware Distributed Submodular Maximization: A Paradigm for Multi-Robot Decision-Making",
            "url": "https://arxiv.org/html/2204.07520"
          },
          {
            "title": "Decision-Oriented Learning Using Differentiable Submodular Maximization for Multi-Robot Coordination This work is supported in part by National Science Foundation Grant No. 1943368 and Army Grant No. W911NF2120076. 1University of Southern California, Los Angels, CA 90007 USA shig@usc.edu. The author was with the Department of Electrical and Computer Engineering, University of Maryland, College Park, MD, USA, when part of the work was completed. 2University of Maryland, College Park, MD 20742 USA [cshek1, to",
            "url": "https://arxiv.org/html/2310.01519"
          },
          {
            "title": "A Distributed Algorithm for Robust Sequential Submodular Optimization in Multi-robot Systems | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-981-95-4839-2_13"
          },
          {
            "title": "A Distributed Algorithm for Robust Sequential Submodular Optimization in Multi-robot Systems",
            "url": "https://www.researchgate.net/publication/399375458_A_Distributed_Algorithm_for_Robust_Sequential_Submodular_Optimization_in_Multi-robot_Systems"
          },
          {
            "title": "Frontiers | Multimodal Hierarchical Dirichlet Process-Based Active Perception by a Robot",
            "url": "https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2018.00022/full"
          },
          {
            "title": "[1910.01208] Distributed Attack-Robust Submodular Maximization for Multi-Robot Planning",
            "url": "https://arxiv.org/abs/1910.01208"
          },
          {
            "title": "(PDF) Distributed Attack-Robust Submodular Maximization for Multi-Robot Planning",
            "url": "https://www.researchgate.net/publication/336251073_Distributed_Attack-Robust_Submodular_Maximization_for_Multi-Robot_Planning"
          },
          {
            "title": "dblp: Fast Semidifferential-based Submodular Function Optimization.",
            "url": "https://dblp.org/rec/conf/icml/IyerJB13.html"
          },
          {
            "title": "[2407.10382] Communication- and Computation-Efficient Distributed Submodular Optimization in Robot Mesh Networks",
            "url": "https://arxiv.org/abs/2407.10382"
          }
        ]
      },
      "Based on the web search results, I found several relevant research papers and topics on submodular function optimization in multi-robot systems. Here's what I found:\n\n## Submodular Function Optimization in Multi-Robot Systems\n\nResearch in this area is motivated by the future of autonomy that involves heterogeneous robots collaborating in complex tasks, such as image covering, target tracking, and area monitoring.\n\n### Key Challenges with Heterogeneous Data Structures\n\nThe robots' heterogeneous capabilities (speed, size, on-board cameras, etc.) offer tremendous advantages; for example, in the image covering scenario, tiny robots offer the advantage of agility for navigating narrow spaces, while larger robots offer the advantages of reliability with higher-resolution cameras. However, heterogeneity in capabilities also implies heterogeneity in on-board resources (tiny robots have limited computation, communication, and memory resources), and mere distributed communication among the robots is insufficient for the success of their tasks.\n\n### Multi-Modal Action Prediction\n\nInformation Gain (IG) has a submodular and non-decreasing property as a set function; therefore, greedy and lazy greedy algorithms are guaranteed to be near-optimal strategies. Additionally, the evaluation criterion for multimodal active perception is a submodular and non-decreasing function.\n\n### Resource-Aware Distributed Optimization\n\nSubmodularity is a property of diminishing returns that arises in active information gathering such as mapping, surveillance, and target tracking, and Resource-Aware distributed Greedy (RAG) introduces a new distributed optimization paradigm that enables scalable and near-optimal action coordination."
    ],
    "durationSeconds": 6.6752758719999985
  },
  "sourceToolAssistantUUID": "e28e6770-c1ac-4266-a89a-851a938f1681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-14T03:24:23.314Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0173AX88bpw8ZRDuBgwp9MK2`</summary>

```json
{
  "query": "\"action chunk\" OR \"action chunking\" diversity redundancy VLA training data selection sampling 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a954cf9-226e-4627-91ba-345e4ad34bc0",
  "isSidechain": false,
  "requestId": "req_011Cb1kDe42vxwrU4ZvF3Yis",
  "type": "assistant",
  "uuid": "8f64f3bf-4be6-4bf7-85e5-387bff6e62bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2M8bksvGLLinGySRsMQ1F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1140,
      "cache_read_input_tokens": 41624,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1140,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 41624,
          "cache_creation_input_tokens": 1140,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1140
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

_source line 60 · 2026-05-14T03:24:32.948Z_

<details><summary>↩ Tool result · `toolu_0173AX88bpw8ZRDuBgwp9MK2`</summary>

```text
Web search results for query: ""action chunk" OR "action chunking" diversity redundancy VLA training data selection sampling 2025 2026"

Links: [{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"Action Chunking for Robotics and AV | Igl's Blog","url":"https://www.maximilianigl.com/blog/action-chunking"},{"title":"Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding","url":"https://arxiv.org/html/2503.02310v1"},{"title":"Bidirectional Decoding: Improving Action Chunking via Closed-Loop Resampling","url":"https://arxiv.org/html/2408.17355v1"},{"title":"VLA Knows Its Limits","url":"https://arxiv.org/html/2602.21445"},{"title":"Adaptive Q-Chunking for Offline-to-Online Reinforcement Learning","url":"https://arxiv.org/html/2605.05544"},{"title":"Learning Native Continuation for Action Chunking Flow Policies","url":"https://arxiv.org/html/2602.12978"},{"title":"Action chunking with Transformers (ACT) robot policy | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/action-chunking-with-transformers-act-robot-policy-80519fc024bc"},{"title":"SEAR: Sample Efficient Action Chunking Reinforcement Learning","url":"https://arxiv.org/html/2603.01891v1"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://xiaoxiao0406.github.io/vqvla.github.io/static/pdfs/VQ-VLA.pdf"}]

Based on the web search results, I found several relevant papers and resources on action chunking in Vision-Language-Action (VLA) models for robotics. Here's what the search revealed:

## Key Concepts Found:

**Action Chunking Fundamentals:**
Chunking is effective since actions have a lot of redundancy. This means that these consecutive tokens are highly correlated so they can usually be predicted in parallel.

**Diversity and Data Selection:**
Rather than token counts, we should focus more on the quantity and diversity of video. This relates to your interest in training data selection and sampling strategies.

**Recent Work on Data Diversity (2025-2026):**

Several recent papers address action chunking with different approaches:

1. **Sample Efficient Action Chunking (SEAR)** - Increases the state-action coverage by executing only a random prefix of each action chunk before replanning, complementing a receding-horizon execution mode for fast reactivity.

2. **Adaptive Q-Chunking (AQC)** - Scores multiple candidate chunks at each scale and selects the best prefix via the per-scale advantage criterion, giving the VLA reactive control near contacts while preserving smooth motion in free space.

3. **Bidirectional Decoding (BID)** - Samples multiple predictions at each time step and searches for the optimal one based on two criteria: (i) backward coherence, which favors samples aligned with previous decisions, (ii) forward contrast, which favors samples close to outputs of a stronger policy and distant from those of a weaker policy.

4. **VLA Knows Its Limits** - Reveals two key phenomena in action chunking: intra-chunk actions attend invariantly to vision-language tokens, and initial and terminal action tokens serve as stable anchors, proposing AutoHorizon, the first test-time method that dynamically estimates the execution horizon for each predicted action chunk.

These works from 2025-2026 appear to address redundancy reduction and diversity in action chunking through sampling strategies and data selection during training and inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f64f3bf-4be6-4bf7-85e5-387bff6e62bd",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "957ddb20-aef4-4f7a-be12-2a9978ec9808",
  "toolUseResult": {
    "query": "\"action chunk\" OR \"action chunking\" diversity redundancy VLA training data selection sampling 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0129fbnNgnjsK6pMN8eJvdRt",
        "content": [
          {
            "title": "Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)",
            "url": "https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"
          },
          {
            "title": "Action Chunking for Robotics and AV | Igl's Blog",
            "url": "https://www.maximilianigl.com/blog/action-chunking"
          },
          {
            "title": "Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding",
            "url": "https://arxiv.org/html/2503.02310v1"
          },
          {
            "title": "Bidirectional Decoding: Improving Action Chunking via Closed-Loop Resampling",
            "url": "https://arxiv.org/html/2408.17355v1"
          },
          {
            "title": "VLA Knows Its Limits",
            "url": "https://arxiv.org/html/2602.21445"
          },
          {
            "title": "Adaptive Q-Chunking for Offline-to-Online Reinforcement Learning",
            "url": "https://arxiv.org/html/2605.05544"
          },
          {
            "title": "Learning Native Continuation for Action Chunking Flow Policies",
            "url": "https://arxiv.org/html/2602.12978"
          },
          {
            "title": "Action chunking with Transformers (ACT) robot policy | by Deepthi Karkada | Medium",
            "url": "https://medium.com/@deepkarkada/action-chunking-with-transformers-act-robot-policy-80519fc024bc"
          },
          {
            "title": "SEAR: Sample Efficient Action Chunking Reinforcement Learning",
            "url": "https://arxiv.org/html/2603.01891v1"
          },
          {
            "title": "VQ-VLA: Improving Vision-Language-Action Models via Scaling",
            "url": "https://xiaoxiao0406.github.io/vqvla.github.io/static/pdfs/VQ-VLA.pdf"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers and resources on action chunking in Vision-Language-Action (VLA) models for robotics. Here's what the search revealed:\n\n## Key Concepts Found:\n\n**Action Chunking Fundamentals:**\nChunking is effective since actions have a lot of redundancy. This means that these consecutive tokens are highly correlated so they can usually be predicted in parallel.\n\n**Diversity and Data Selection:**\nRather than token counts, we should focus more on the quantity and diversity of video. This relates to your interest in training data selection and sampling strategies.\n\n**Recent Work on Data Diversity (2025-2026):**\n\nSeveral recent papers address action chunking with different approaches:\n\n1. **Sample Efficient Action Chunking (SEAR)** - Increases the state-action coverage by executing only a random prefix of each action chunk before replanning, complementing a receding-horizon execution mode for fast reactivity.\n\n2. **Adaptive Q-Chunking (AQC)** - Scores multiple candidate chunks at each scale and selects the best prefix via the per-scale advantage criterion, giving the VLA reactive control near contacts while preserving smooth motion in free space.\n\n3. **Bidirectional Decoding (BID)** - Samples multiple predictions at each time step and searches for the optimal one based on two criteria: (i) backward coherence, which favors samples aligned with previous decisions, (ii) forward contrast, which favors samples close to outputs of a stronger policy and distant from those of a weaker policy.\n\n4. **VLA Knows Its Limits** - Reveals two key phenomena in action chunking: intra-chunk actions attend invariantly to vision-language tokens, and initial and terminal action tokens serve as stable anchors, proposing AutoHorizon, the first test-time method that dynamically estimates the execution horizon for each predicted action chunk.\n\nThese works from 2025-2026 appear to address redundancy reduction and diversity in action chunking through sampling strategies and data selection during training and inference."
    ],
    "durationSeconds": 9.624322592000011
  },
  "sourceToolAssistantUUID": "8f64f3bf-4be6-4bf7-85e5-387bff6e62bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T03:24:37.909Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HMsrbCJ2ayYy88w7aeNh2P`</summary>

```json
{
  "query": "LIBERO benchmark latest SOTA results 2025 2026 success rate leaderboard"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "957ddb20-aef4-4f7a-be12-2a9978ec9808",
  "isSidechain": false,
  "requestId": "req_011Cb1kEddkjvHh6w2qBWZiu",
  "type": "assistant",
  "uuid": "0255e0a9-8c61-46bf-b5ed-a6c3509c61d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4T2kEtaWcLEyPqALJQpzu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1051,
      "cache_read_input_tokens": 42764,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1051,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 42764,
          "cache_creation_input_tokens": 1051,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1051
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

_source line 62 · 2026-05-14T03:24:44.492Z_

<details><summary>↩ Tool result · `toolu_01HMsrbCJ2ayYy88w7aeNh2P`</summary>

```text
Web search results for query: "LIBERO benchmark latest SOTA results 2025 2026 success rate leaderboard"

Links: [{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"VLA SOTA Leaderboard","url":"https://sota.evomind-tech.com/benchmarks/libero/"},{"title":"CodeSOTA — Open AI Benchmark Registry and SOTA API","url":"https://www.codesota.com/"},{"title":"AI Coding Benchmark Leaderboard 2026: Code Generation and SWE-bench | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/code-generation"},{"title":"VLA & Dexterous Manipulation SOTA Leaderboard","url":"https://github.com/MINT-SJTU/Evo-SOTA.io/blob/main/README.md"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Speech AI Leaderboard 2026: Best STT, ASR and TTS Models | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/speech"},{"title":"Would you like to set up an online leaderboard for SOTA methods on libero? · Issue #25 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/25"},{"title":"LiveCodeBench Leaderboard - Holistic and Contamination Free Evaluation","url":"https://livecodebench.github.io/leaderboard.html"}]

Based on my search results, I found information about LIBERO benchmark SOTA results:

## LIBERO Benchmark Performance

Reported SOTA figures show success rates exceeding 95%, though these reflect performance under clean, nearly identically distributed train/test splits. However, there's an important caveat: SOTA models collapse to near-zero success under moderate task, language, object, or environment perturbations.

## Available SOTA Leaderboards

A Vision-Language-Action Model Benchmark Rankings leaderboard tracks state-of-the-art VLA models on LIBERO, CALVIN, and Meta-World benchmarks. Additionally, a comprehensive leaderboard tracks the state-of-the-art (SOTA) performance of Vision-Language-Action (VLA) models across multiple robotics benchmarks including LIBERO.

## Notable Updates (2025)

Recent developments include In-context Learning (ICIL) approaches using Transformer and SSM backbones for few-shot adaptation from demonstration prompts, and LIBERO-PRO and LIBERO-Plus variants that systematically inject controlled perturbations to improve evaluation robustness.

For the most current leaderboard rankings with specific success rates, I recommend visiting the VLA SOTA Leaderboard directly at sota.evomind-tech.com/benchmarks/libero/, which appears to maintain live, updated results for LIBERO benchmark submissions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0255e0a9-8c61-46bf-b5ed-a6c3509c61d3",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "78ab5c75-6476-4136-af12-cb51ab6b14e7",
  "toolUseResult": {
    "query": "LIBERO benchmark latest SOTA results 2025 2026 success rate leaderboard",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DmAY4YRcvSgTViYkHoFEeV",
        "content": [
          {
            "title": "LLM Leaderboard 2026 — Compare Top AI Models - Vellum",
            "url": "https://www.vellum.ai/llm-leaderboard"
          },
          {
            "title": "LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA",
            "url": "https://www.codesota.com/llm"
          },
          {
            "title": "VLA SOTA Leaderboard",
            "url": "https://sota.evomind-tech.com/benchmarks/libero/"
          },
          {
            "title": "CodeSOTA — Open AI Benchmark Registry and SOTA API",
            "url": "https://www.codesota.com/"
          },
          {
            "title": "AI Coding Benchmark Leaderboard 2026: Code Generation and SWE-bench | CodeSOTA | CodeSOTA",
            "url": "https://www.codesota.com/code-generation"
          },
          {
            "title": "VLA & Dexterous Manipulation SOTA Leaderboard",
            "url": "https://github.com/MINT-SJTU/Evo-SOTA.io/blob/main/README.md"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "Speech AI Leaderboard 2026: Best STT, ASR and TTS Models | CodeSOTA | CodeSOTA",
            "url": "https://www.codesota.com/speech"
          },
          {
            "title": "Would you like to set up an online leaderboard for SOTA methods on libero? · Issue #25 · Lifelong-Robot-Learning/LIBERO",
            "url": "https://github.com/Lifelong-Robot-Learning/LIBERO/issues/25"
          },
          {
            "title": "LiveCodeBench Leaderboard - Holistic and Contamination Free Evaluation",
            "url": "https://livecodebench.github.io/leaderboard.html"
          }
        ]
      },
      "Based on my search results, I found information about LIBERO benchmark SOTA results:\n\n## LIBERO Benchmark Performance\n\nReported SOTA figures show success rates exceeding 95%, though these reflect performance under clean, nearly identically distributed train/test splits. However, there's an important caveat: SOTA models collapse to near-zero success under moderate task, language, object, or environment perturbations.\n\n## Available SOTA Leaderboards\n\nA Vision-Language-Action Model Benchmark Rankings leaderboard tracks state-of-the-art VLA models on LIBERO, CALVIN, and Meta-World benchmarks. Additionally, a comprehensive leaderboard tracks the state-of-the-art (SOTA) performance of Vision-Language-Action (VLA) models across multiple robotics benchmarks including LIBERO.\n\n## Notable Updates (2025)\n\nRecent developments include In-context Learning (ICIL) approaches using Transformer and SSM backbones for few-shot adaptation from demonstration prompts, and LIBERO-PRO and LIBERO-Plus variants that systematically inject controlled perturbations to improve evaluation robustness.\n\nFor the most current leaderboard rankings with specific success rates, I recommend visiting the VLA SOTA Leaderboard directly at sota.evomind-tech.com/benchmarks/libero/, which appears to maintain live, updated results for LIBERO benchmark submissions."
    ],
    "durationSeconds": 6.577408638000023
  },
  "sourceToolAssistantUUID": "0255e0a9-8c61-46bf-b5ed-a6c3509c61d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 63_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Beyond Difficulty: Diversity-Aware Dynamic Sampling for Data-Efficient…",
  "leafUuid": "78ab5c75-6476-4136-af12-cb51ab6b14e7",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "Benchmark diversity-aware selection methods on VLA BC",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Tool call

_source line 65 · 2026-05-14T03:24:48.210Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012GgmicQidfvYpoCsuwj3ow`</summary>

```json
{
  "url": "https://sota.evomind-tech.com/benchmarks/libero/",
  "prompt": "Extract all the LIBERO benchmark results: model names, success rates on each suite (Spatial, Object, Goal, Long), average success rate. List the top 10 methods with their scores."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78ab5c75-6476-4136-af12-cb51ab6b14e7",
  "isSidechain": false,
  "requestId": "req_011Cb1kFUsBohviGrp8yEv5i",
  "type": "assistant",
  "uuid": "97361556-4e98-4959-bd60-7bf9a81415ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLGHD1LkyCXwcr7fDLVDZS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 894,
      "cache_read_input_tokens": 43815,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 127,
          "cache_read_input_tokens": 43815,
          "cache_creation_input_tokens": 894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 894
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

_source line 66 · 2026-05-14T03:24:50.975Z_

<details><summary>↩ Tool result · `toolu_012GgmicQidfvYpoCsuwj3ow`</summary>

```text
I cannot extract the LIBERO benchmark results you're requesting because the web page content provided does not contain any benchmark data, model names, or success rates.

The page shows only navigation elements and metadata, including:
- "VLA SOTA Leaderboard" (the title)
- Navigation links to "Models," "Methodology," and "Dex / VLA"
- Copyright information stating "Data collected from published papers"
- References to EvoMind and SJTU organizations

To obtain the specific benchmark results you're seeking, you would need to navigate to the actual benchmark data pages on the website, likely through the "Models" or "Benchmarks" sections mentioned in the navigation menu.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97361556-4e98-4959-bd60-7bf9a81415ae",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "1e726813-5f70-4757-be11-80b9722a11fc",
  "toolUseResult": {
    "bytes": 12718,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot extract the LIBERO benchmark results you're requesting because the web page content provided does not contain any benchmark data, model names, or success rates.\n\nThe page shows only navigation elements and metadata, including:\n- \"VLA SOTA Leaderboard\" (the title)\n- Navigation links to \"Models,\" \"Methodology,\" and \"Dex / VLA\"\n- Copyright information stating \"Data collected from published papers\"\n- References to EvoMind and SJTU organizations\n\nTo obtain the specific benchmark results you're seeking, you would need to navigate to the actual benchmark data pages on the website, likely through the \"Models\" or \"Benchmarks\" sections mentioned in the navigation menu.",
    "durationMs": 2762,
    "url": "https://sota.evomind-tech.com/benchmarks/libero/"
  },
  "sourceToolAssistantUUID": "97361556-4e98-4959-bd60-7bf9a81415ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-14T03:24:53.641Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DsESGpkKAmWoNCULQ2dLUP`</summary>

```json
{
  "query": "LIBERO benchmark VLA results table 2026 success rate Spatial Object Goal Long average comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e726813-5f70-4757-be11-80b9722a11fc",
  "isSidechain": false,
  "requestId": "req_011Cb1kFxc3n5t6Ru2rshqVx",
  "type": "assistant",
  "uuid": "6506faec-6853-4187-9849-195ac7341a3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qbj258tzzk1cPSoJ6F2xMe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 289,
      "cache_read_input_tokens": 44709,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 289,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 44709,
          "cache_creation_input_tokens": 289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 289
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

_source line 68 · 2026-05-14T03:25:01.599Z_

<details><summary>↩ Tool result · `toolu_01DsESGpkKAmWoNCULQ2dLUP`</summary>

```text
Web search results for query: "LIBERO benchmark VLA results table 2026 success rate Spatial Object Goal Long average comparison"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"PI-VLA: Adaptive Symmetry-Aware Decision-Making for Long-Horizon Vision–Language–Action Manipulation","url":"https://www.mdpi.com/2073-8994/18/3/394"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO vs CALVIN (2026): Benchmark Comparison | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/datasets/compare/libero-vs-calvin"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/abs/2603.28301"},{"title":"Experiences from Benchmarking Vision–Language–Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2511.11298v1"}]

I found several relevant resources about LIBERO benchmark results for VLA models. Here's what I found:

## Key Results on LIBERO Benchmark (2026)

Strong 2025-era VLA policies (OpenVLA, pi0, Octo variants) typically land in the 70-90 percent success range on Spatial, Object, and Goal tasks, and 30-60 percent on LIBERO-100 depending on training recipe.

PI-VLA achieves state-of-the-art performance, attaining a 73.2% average success rate on the LIBERO benchmark (with particularly strong gains on the Long-Horizon suite).

## Detailed Performance Analysis

A detailed analysis provides success rates across seven perturbation categories (Camera, Robot Initialization, Language Instruction, Lighting, Background, Sensor Noise, and Scene Layout) for various VLA methods, with results further broken down by task suite (Spatial, Object, Goal, and Long).

## Important Caveat

The spread in performance across suites is interesting: policies that do well on the first three suites sometimes fall off a cliff on LIBERO-100, which reveals a generalization gap that a single averaged number would hide. When reading a new paper, always check the per-suite breakdown rather than the mean, as papers that report only the average are hiding something.

The search results indicate that while standard LIBERO benchmark results show high success rates (70-90% on basic suites), more recent 2026 research reveals significant brittleness when models are tested under perturbations and variations from the original benchmark conditions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6506faec-6853-4187-9849-195ac7341a3b",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "0a6d894b-ca92-475c-b211-a1cd65819c1e",
  "toolUseResult": {
    "query": "LIBERO benchmark VLA results table 2026 success rate Spatial Object Goal Long average comparison",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JnR4usB1LCdJhp965T1qyQ",
        "content": [
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "PI-VLA: Adaptive Symmetry-Aware Decision-Making for Long-Horizon Vision–Language–Action Manipulation",
            "url": "https://www.mdpi.com/2073-8994/18/3/394"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models",
            "url": "https://cvpr.thecvf.com/virtual/2026/poster/38735"
          },
          {
            "title": "000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019",
            "url": "https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "LIBERO vs CALVIN (2026): Benchmark Comparison | Silicon Valley Robotics Center",
            "url": "https://www.roboticscenter.ai/datasets/compare/libero-vs-calvin"
          },
          {
            "title": "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/html/2603.28301v1"
          },
          {
            "title": "[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/abs/2603.28301"
          },
          {
            "title": "Experiences from Benchmarking Vision–Language–Action Models for Robotic Manipulation",
            "url": "https://arxiv.org/html/2511.11298v1"
          }
        ]
      },
      "I found several relevant resources about LIBERO benchmark results for VLA models. Here's what I found:\n\n## Key Results on LIBERO Benchmark (2026)\n\nStrong 2025-era VLA policies (OpenVLA, pi0, Octo variants) typically land in the 70-90 percent success range on Spatial, Object, and Goal tasks, and 30-60 percent on LIBERO-100 depending on training recipe.\n\nPI-VLA achieves state-of-the-art performance, attaining a 73.2% average success rate on the LIBERO benchmark (with particularly strong gains on the Long-Horizon suite).\n\n## Detailed Performance Analysis\n\nA detailed analysis provides success rates across seven perturbation categories (Camera, Robot Initialization, Language Instruction, Lighting, Background, Sensor Noise, and Scene Layout) for various VLA methods, with results further broken down by task suite (Spatial, Object, Goal, and Long).\n\n## Important Caveat\n\nThe spread in performance across suites is interesting: policies that do well on the first three suites sometimes fall off a cliff on LIBERO-100, which reveals a generalization gap that a single averaged number would hide. When reading a new paper, always check the per-suite breakdown rather than the mean, as papers that report only the average are hiding something.\n\nThe search results indicate that while standard LIBERO benchmark results show high success rates (70-90% on basic suites), more recent 2026 research reveals significant brittleness when models are tested under perturbations and variations from the original benchmark conditions."
    ],
    "durationSeconds": 7.95599756800002
  },
  "sourceToolAssistantUUID": "6506faec-6853-4187-9849-195ac7341a3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-14T03:27:37.320Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the landscape. Let me synthesize what I've learned before writing the revision:

**Key findings from research:**

1. **UDS (ICML 2025, Zou et al.)** - Very close to DADS. Does online utility-diversity batch selection for LLM SFT. Uses nuclear norm of logits for intra-sample utility/diversity + embedding-based inter-sample diversity with memory buffer. Score: s_total = s_intra + α·s_inter. Applied to LLM text tasks only (MMLU, ScienceQA, GSM8K, HumanEval). 

2. **GLISTER-Online (AAAI 2021)** - Online submodular data selection with convergence guarantees. Maximizes log-likelihood on validation set. Applied to image classification and NLP, but never tested on VLA or robotics tasks.

3. **CRAIG (ICML 2020)** - Facility-location based coreset selection during SGD using gradient-matching. Evaluated on logistic regression and image classification, not VLA or robotics.

4. **D2 Pruning (ICLR 2** - Still reviewing this approach.

5. **InfoMax (ICLR 2025)** - Uses quadratic programming to balance importance and redundancy in pre-training data selection, applied to image classification, vision-language pre-training, and LLM instruction tuning.

6. **D3 (IJCAI 2025)** - Focuses on diversity, difficulty, and dependability for LLM instruction tuning with multi-round iteration capability.

7. **Robot Data Curation with MI (Hejna et al., RSS 2026)** - DemInf method leveraging mutual information between states and actions for unsupervised, embedding-based robotics data curation, though limited to static selection.

8. **DemoSpeedup (CoRL 2025)** - Entropy-guided frame-level selection within demonstrations...

The reviewers correctly identified that my gap claim was overstated—online diversity-aware selection already exists in UDS, GLISTER-Online, and CRAIG. DADS itself is really just combining existing components like PER loss, embedding similarity, facility location, and annealing, which the CORDS ecosystem already does. But there's still a meaningful distinction: none of these methods have actually been applied to vision-language action models or robotic behavior cloning, and VLA tasks have genuinely different structural properties—multi-modal inputs, temporal dependencies within trajectories, action chunking, cross-task transfer, and continuous action spaces—so the real question is whether these differences are substantial enough to warrant a new approach.

I'm considering two paths forward. Option A is a major reframe: instead of claiming novelty through a new method, I'd position this as the first systematic evaluation of existing diversity-aware selection methods on VLA BC, identify where they fail due to VLA-specific properties, and propose targeted adaptations. Option B is a pivot toward a comprehensive benchmark study that compares all these methods on VLA tasks, analyzes why certain approaches succeed or fail given the structural differences, and provides practical recommendations with a lightweight VLA-specific variant.

Option A feels right—the core problem is real and the gap is genuine, but I need to shift from "novel method" framing to "understanding and adaptation." The key insight is that existing methods like GLISTER, CRAIG, and UDS make assumptions that break down in VLA BC: they don't account for temporal autocorrelation within action trajectories where consecutive chunks are highly dependent, and they miss the multi-dimensional nature of diversity in VLA—visual scenes, language instructions, and action types all matter simultaneously in ways that simple embedding similarity can't fully capture.

The action space itself is fundamentally different from classification tasks. Continuous 6-DoF regression has a loss landscape where high loss could mean the demonstration is genuinely hard, noisy, or represents one of multiple valid solutions—that last case is unique to robotics and makes loss-based selection unreliable. Beyond that, LIBERO's structure across task suites introduces another diversity axis that pure embedding methods might miss, and robot demonstrations vary in quality in ways that need explicit handling rather than just implicit loss weighting.

So the real problem is that the standard utility-diversity split breaks down here: loss doesn't reliably indicate utility because of multi-modal actions and demo quality, embedding distance doesn't capture the heterogeneous diversity axes that matter (task, action phase, scene, objects), and the temporal structure within trajectories violates the i.i.d. assumption. This could be the novel angle—not just combining loss and diversity like everyone else, but showing why that decomposition fundamentally fails for VLA behavior cloning.

The contribution would be benchmarking existing online selection methods (UDS, GLISTER, CRAIG, D2) on VLA BC to see if they transfer, then identifying the specific failure modes: loss unreliability from action multimodality, trajectory-level redundancy that per-sample embeddings miss, and the need for multi-granular diversity metrics instead of a single embedding space.

But the reviewer's point is nagging at me — if I'm just adapting existing methods to VLA, that's still application work. The real methodological insight needs to be about action multimodality itself: standard utility measures fail in VLA BC because multiple valid action sequences exist for the same observation, so high loss doesn't actually indicate high value for learning.

This is genuinely VLA-specific in a way that LLM or vision tasks aren't. And it means all existing loss-based selection methods would systematically overweight outlier strategies while underweighting common ones. Beyond that, I'm realizing trajectory-level redundancy matters too — consecutive chunks in VLA datasets often encode the same skill, so I need to account for that when selecting demonstrations.

So the real fix isn't tweaking loss functions, it's building trajectory-aware utility and diversity metrics that capture action multi-modality and ensure coverage across trajectories rather than just embedding space. And I should reframe the whole paper to acknowledge existing diversity-aware methods like UDS, GLISTER, CRAIG, and D2, then pinpoint where they actually fail for VLAs.

For the theory side, instead of just extending convergence proofs, I should focus on proving when loss-based utility breaks down under multi-modal action distributions—that's a concrete claim the existing methods don't handle. Let me start drafting this major revision.

Actually, I need to think through the reviewer's core criticism more carefully. They're right that combining loss priority with embedding similarity and facility-location submodular functions already exists in the literature. If I just apply those pieces to VLA, it reads as an application paper rather than a real contribution. The paper needs to go deeper—the strongest angle is framing this as an empirical investigation into why general-purpose diversity selection fails specifically for robot behavioral cloning, then proposing VLA-tailored solutions that address those failure modes.

But here's the catch: I'm hypothesizing that methods like GLISTER and CRAIG would underperform on LIBERO, but I haven't actually tested it. The reviewer is essentially calling me out to run those baselines first—if they fail, that becomes the empirical motivation; if they work, I need a different angle entirely.

So the paper structure should be flexible: benchmark these existing methods on LIBERO, diagnose what breaks (if anything), then propose VLA-specific fixes. The core contribution becomes understanding *when* and *why* diversity-aware selection works or fails in this domain, not just engineering a solution.

For the actual approach, I'm thinking a three-phase structure: first, systematically test UDS, GLISTER-Online, CRAIG, D2 Pruning, and InfoMax on LIBERO to see what happens; second, analyze any failure modes that emerge; third, develop solutions that address genuinely VLA-specific issues like trajectory redundancy and action multi-modality.

The key VLA-specific challenges I need to tackle are trajectory-level redundancy that simple embedding distance misses, the fact that multiple valid action sequences can come from the same state, and the need for diversity across task, scene, and action-phase levels—so I'd need trajectory-aware deduplication, trajectory-conditioned losses, and hierarchical diversity constraints to handle these properly.

Before I commit to this direction though, I should check whether someone's already done this benchmarking study for VLAs. And regarding the workshop paper concern—the reviewer's right that it's just a workshop paper, but the empirical findings about TSS and random sampling aren't controversial or novel enough to anchor a full conference paper on their own.

Now I'm revising the entire JSON submission. The core shift is reframing this from proposing a novel method to providing empirical understanding plus a VLA-adapted approach. I need to cite the existing work properly—UDS, GLISTER, CRAIG, D2, InfoMax, D3, DemInf, DemoSpeedup—and position these as baselines rather than just comparing against static or random selection. I'm dropping the CoRL 2026 reference, either providing rigorous theory for the convergence claim or removing it entirely, and acknowledging the workshop paper's limitations while noting that its findings align with broader diversity principles.

For the title, I'm considering options that emphasize both the empirical investigation and the practical contribution—something that captures why general diversity methods struggle with VLAs and what we can do about it.

On the methodological side, I'm exploring what genuinely novel contributions I can make beyond reassembling existing ideas. One approach is trajectory-conditioned utility, where instead of using raw loss as the selection signal, I condition it on the trajectory context—computing utility relative to expected loss for action chunks at similar positions in comparable trajectories. This lets me distinguish between difficulty arising from the task itself versus difficulty from something specific about that demonstration.

Another direction is multi-granularity coverage, which breaks down the single diversity constraint into VLA-specific axes: task-level coverage to ensure all task types are represented, action-phase coverage to capture different stages like reaching and grasping, and scene configuration coverage for visual diversity. Rather than applying a generic facility-location approach, this tailors the coverage structure to what actually matters for robot learning.

I'm also considering temporal redundancy pruning, which accounts for the fact that action chunks from the same trajectory are informationally linked—selecting one informative chunk reduces the value of nearby chunks from that same trajectory. By incorporating trajectory identity into the redundancy scoring, chunks within a trajectory compete with each other, which is a structural property unique to demonstration data.

These three components directly address the VLA-specific failure modes I identified earlier, rather than just combining existing techniques. Now I'm thinking about the paper's positioning: should it emphasize the empirical study revealing where current diversity methods fail for VLAs, or focus on the new method itself? I think the strongest angle is leading with the empirical findings about VLA-specific failure modes, then presenting the adapted method as the solution. This framing is robust because it grounds the contribution in concrete problems rather than just proposing a method in isolation.

For the title, I want something that captures both the diagnostic and solution aspects without being too negative or generic. Something like "Understanding Online Data Selection for VLA Training" or "Bridging the Selection Gap" feels right—it signals this is about understanding what breaks and how to fix it, not just another combined approach.

On naming the method itself, I'm torn between keeping something simple versus being more descriptive. VAST or TAOS could work, but they might feel forced. Maybe I should just call the overall benchmarking effort something clear like ODS-Bench and give the VLA-specific adaptations a straightforward name like TACS or DASH that actually describes what it does.

Actually, I'm overthinking this. The real contribution is the benchmarking study that diagnoses why standard data selection fails for VLAs, and then the adapted method that addresses those specific failure modes. I don't need a fancy acronym—I can just call the method something that reflects trajectory awareness and distributional concerns, like TDA-Select, but honestly that's getting unwieldy too. Let me stick with renaming DADS to something the reviewers won't immediately associate with component assembly, maybe TraC-Select to emphasize the trajectory-aware chunk selection aspect, and move forward with the substance rather than getting stuck on nomenclature. I'm settling on "Trajectory-Aware Online Data Selection for Vision-Language-Action Training" as the title since it clearly signals the VLA-specific contribution without relying on an acronym. For the structure, I'll run a benchmarking phase that applies existing methods like UDS and GLISTER-Online to LIBERO tasks, comparing them against random sampling, difficulty-based approaches, and other baselines across different data fractions, then move into a second phase that builds on those findings.

The key insight phase will dig into why each method fails—testing whether loss-based utility overweights action-heavy chunks, whether embedding diversity misses trajectory patterns, or whether single-scale diversity can't capture the multi-level structure VLA tasks need. From there, I'll develop a trajectory-aware method that conditions utility scores on trajectory context, incorporates trajectory identity into similarity calculations, and adds hierarchical diversity across task, trajectory, and observation levels before comparing everything back to the Phase 1 baselines.

Now I'm thinking through the computational cost. Phase 1 alone is substantial—running 5 methods across 4 suites with multiple data fractions and seeds means roughly 180 training runs at 6 hours each on an A100, so around 1000 GPU-hours just for the baseline comparisons. Phase 2 analysis is lighter at maybe 50 hours, but Phase 3 with the proposed method and ablations will need another 300 hours. All told, I'm looking at somewhere between 1500 and 2000 GPU-hours for the full pipeline.

But wait, I should reconsider the actual runtime. LIBERO tasks are relatively compact, and SmolVLA is a smaller model, so fine-tuning shouldn't take as long as I initially thought. Looking back at similar work like the redundancy paper, they were able to run SmolVLA experiments on LIBERO in just a few hours per run, which is much more reasonable.

With that in mind, I'm ready to draft the full revision. The key structural shifts are reframing the title around trajectory-aware online selection, repositioning the core problem as VLA-specific redundancy that existing methods like UDS and GLISTER weren't designed to handle, and highlighting this as the first systematic evaluation of online selection methods in the VLA domain.

I'll need to completely overhaul the related work section to include all the missing papers, restructure the approach as a three-phase study combining benchmarking, analysis, and adaptation, adjust the resource estimates for the additional baselines, target ICLR 2027 instead of splitting between venues, and update the references. The contribution level stays solid since the work is now more comprehensive and grounded.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a6d894b-ca92-475c-b211-a1cd65819c1e",
  "isSidechain": false,
  "requestId": "req_011Cb1kGk5WUurk2XXgdhRfM",
  "type": "assistant",
  "uuid": "21def339-91ec-4bf0-ac50-2227e50ff4d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FAByYNiiZ8TJxZvZ5TK4pR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1005,
      "cache_read_input_tokens": 44998,
      "output_tokens": 6169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6169,
          "cache_read_input_tokens": 44998,
          "cache_creation_input_tokens": 1005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1005
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

_source line 70 · 2026-05-14T03:27:37.323Z_

Now let me search for a couple more things to fully understand the landscape before revising.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21def339-91ec-4bf0-ac50-2227e50ff4d4",
  "isSidechain": false,
  "requestId": "req_011Cb1kGk5WUurk2XXgdhRfM",
  "type": "assistant",
  "uuid": "ac00d5cb-31d0-417c-9afe-983260b21519",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FAByYNiiZ8TJxZvZ5TK4pR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1005,
      "cache_read_input_tokens": 44998,
      "output_tokens": 6169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6169,
          "cache_read_input_tokens": 44998,
          "cache_creation_input_tokens": 1005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1005
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

_source line 71 · 2026-05-14T03:27:37.435Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G5xjH4qHXbAEEhWsFP67o2`</summary>

```json
{
  "query": "online data selection behavioral cloning robotics trajectory structure temporal correlation 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac00d5cb-31d0-417c-9afe-983260b21519",
  "isSidechain": false,
  "requestId": "req_011Cb1kGk5WUurk2XXgdhRfM",
  "type": "assistant",
  "uuid": "486a928c-cccc-4205-9b13-08e16d8078d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FAByYNiiZ8TJxZvZ5TK4pR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1005,
      "cache_read_input_tokens": 44998,
      "output_tokens": 6169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6169,
          "cache_read_input_tokens": 44998,
          "cache_creation_input_tokens": 1005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1005
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

_source line 72_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Beyond Difficulty: Diversity-Aware Dynamic Sampling for Data-Efficient…",
  "leafUuid": "486a928c-cccc-4205-9b13-08e16d8078d9",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Runtime record

_source line 73_

```json
{
  "type": "ai-title",
  "aiTitle": "Benchmark diversity-aware selection methods on VLA BC",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Tool result

_source line 74 · 2026-05-14T03:27:45.261Z_

<details><summary>↩ Tool result · `toolu_01G5xjH4qHXbAEEhWsFP67o2`</summary>

```text
Web search results for query: "online data selection behavioral cloning robotics trajectory structure temporal correlation 2024 2025 2026"

Links: [{"title":"Constrained Behavior Cloning for Robotic Learning","url":"https://arxiv.org/html/2408.10568v1"},{"title":"Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://arxiv.org/html/2502.02853v3"},{"title":"Behavior Cloning","url":"https://www.emergentmind.com/topics/behavior-cloning"},{"title":"Rethinking Latent Representations in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://arxiv.org/html/2502.02853v1"},{"title":"TYPE Review PUBLISHED 18 February 2025 DOI 10.3389/fnbot.2025.1451923","url":"https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2025.1451923/pdf"},{"title":"Towards balanced behavior cloning from imbalanced datasets | Autonomous Robots | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10514-025-10237-0"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2510.12638"},{"title":"Behavioral Cloning Models Reality Check for Autonomous Driving Identify applicable funding agency here. If none, delete this.","url":"https://arxiv.org/html/2409.07218v1"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/130333a7b4a79fe39fe5a69106eba20f113c93df.pdf"},{"title":"Behavioral Cloning from Observation","url":"https://www.ijcai.org/proceedings/2018/0687.pdf"}]

I've found several relevant research papers and resources on online data selection, behavioral cloning, robotics, trajectory structures, and temporal correlations from 2024-2026. Here are the key findings:

## Recent Research on Behavioral Cloning and Temporal Modeling

Traditional behavioral cloning primarily relied on learning state-action pairs from expert demonstrations, often overlooking temporal sequence information, though recent research introduced state sequence encoders or historical trackers to better leverage past state information during decision-making.

Research in 2024 utilized historical trajectory data for decision modeling, demonstrating superior performance over traditional BC methods in diverse tasks.

## Temporal Constraints and Historical Information

Historically constrained BC (HCBC) incorporates action and perception histories, leveraging temporal context to reduce error accumulation, especially in long-horizon manipulation. Current methods employ temporal fusion techniques using Temporal Transformers for temporal fusion.

## Data Selection and Quality

Large-scale robot datasets do not always lead to improved performance unless the data is hand-selected; for example, when training OpenVLA, the DROID dataset was significantly downsampled to improve policy performance.

Common, repetitive behaviors in datasets can dominate the learning process.

## Trajectory Modeling

Recent research focuses on training on extensive and diverse datasets with larger models, such as Internet-scale visual question answering and robot trajectory data, as well as a vast collection of Internet videos.

The search results reveal active research into temporal structure modeling in behavioral cloning, with emphasis on historical constraints and data selection strategies for improving robotic learning efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "486a928c-cccc-4205-9b13-08e16d8078d9",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "f22f8467-f1cb-4342-8ded-bf4337ec2bf1",
  "toolUseResult": {
    "query": "online data selection behavioral cloning robotics trajectory structure temporal correlation 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DsQYW3rtXusGwWWZboZzKp",
        "content": [
          {
            "title": "Constrained Behavior Cloning for Robotic Learning",
            "url": "https://arxiv.org/html/2408.10568v1"
          },
          {
            "title": "Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation",
            "url": "https://arxiv.org/html/2502.02853v3"
          },
          {
            "title": "Behavior Cloning",
            "url": "https://www.emergentmind.com/topics/behavior-cloning"
          },
          {
            "title": "Rethinking Latent Representations in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation",
            "url": "https://arxiv.org/html/2502.02853v1"
          },
          {
            "title": "TYPE Review PUBLISHED 18 February 2025 DOI 10.3389/fnbot.2025.1451923",
            "url": "https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2025.1451923/pdf"
          },
          {
            "title": "Towards balanced behavior cloning from imbalanced datasets | Autonomous Robots | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10514-025-10237-0"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2510.12638"
          },
          {
            "title": "Behavioral Cloning Models Reality Check for Autonomous Driving Identify applicable funding agency here. If none, delete this.",
            "url": "https://arxiv.org/html/2409.07218v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf/130333a7b4a79fe39fe5a69106eba20f113c93df.pdf"
          },
          {
            "title": "Behavioral Cloning from Observation",
            "url": "https://www.ijcai.org/proceedings/2018/0687.pdf"
          }
        ]
      },
      "I've found several relevant research papers and resources on online data selection, behavioral cloning, robotics, trajectory structures, and temporal correlations from 2024-2026. Here are the key findings:\n\n## Recent Research on Behavioral Cloning and Temporal Modeling\n\nTraditional behavioral cloning primarily relied on learning state-action pairs from expert demonstrations, often overlooking temporal sequence information, though recent research introduced state sequence encoders or historical trackers to better leverage past state information during decision-making.\n\nResearch in 2024 utilized historical trajectory data for decision modeling, demonstrating superior performance over traditional BC methods in diverse tasks.\n\n## Temporal Constraints and Historical Information\n\nHistorically constrained BC (HCBC) incorporates action and perception histories, leveraging temporal context to reduce error accumulation, especially in long-horizon manipulation. Current methods employ temporal fusion techniques using Temporal Transformers for temporal fusion.\n\n## Data Selection and Quality\n\nLarge-scale robot datasets do not always lead to improved performance unless the data is hand-selected; for example, when training OpenVLA, the DROID dataset was significantly downsampled to improve policy performance.\n\nCommon, repetitive behaviors in datasets can dominate the learning process.\n\n## Trajectory Modeling\n\nRecent research focuses on training on extensive and diverse datasets with larger models, such as Internet-scale visual question answering and robot trajectory data, as well as a vast collection of Internet videos.\n\nThe search results reveal active research into temporal structure modeling in behavioral cloning, with emphasis on historical constraints and data selection strategies for improving robotic learning efficiency."
    ],
    "durationSeconds": 7.820467201000021
  },
  "sourceToolAssistantUUID": "486a928c-cccc-4205-9b13-08e16d8078d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-14T03:27:48.537Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SY7y773JhbGjxukyiux3vj`</summary>

```json
{
  "query": "\"action multimodality\" OR \"multi-modal action distribution\" behavior cloning robot manipulation loss landscape"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f22f8467-f1cb-4342-8ded-bf4337ec2bf1",
  "isSidechain": false,
  "requestId": "req_011Cb1kUon6BPmH5rcaSztQG",
  "type": "assistant",
  "uuid": "b3b4b8c9-2217-433f-a687-54e51a25057b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWqjfhmf8uD8nywHtVPqLV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7030,
      "cache_read_input_tokens": 46003,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 46003,
          "cache_creation_input_tokens": 7030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7030
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

_source line 76 · 2026-05-14T03:27:56.381Z_

<details><summary>↩ Tool result · `toolu_01SY7y773JhbGjxukyiux3vj`</summary>

```text
Web search results for query: ""action multimodality" OR "multi-modal action distribution" behavior cloning robot manipulation loss landscape"

Links: [{"title":"Ch. 21 - Imitation Learning - Underactuated Robotics","url":"https://underactuated.mit.edu/imitation.html"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion .","url":"https://arxiv.org/pdf/2303.04137"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/diffusion_policy_2023.pdf"},{"title":"Robotics: Science and Systems 2023","url":"https://www.roboticsproceedings.org/rss19/p026.pdf"},{"title":"Exploring multimodal implicit behavior learning for vehicle navigation in simulated cities","url":"https://arxiv.org/html/2509.15400v1"},{"title":"IMLE Policy: Fast and Sample Efficient Visuomotor Policy Learning via Implicit Maximum Likelihood Estimation","url":"https://arxiv.org/html/2502.12371v2"},{"title":"CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation","url":"https://arxiv.org/html/2508.01600v1"},{"title":"[2508.01600] CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation","url":"https://arxiv.org/abs/2508.01600"},{"title":"Flow Matching Imitation Learning for Multi-Support Manipulation","url":"https://arxiv.org/html/2407.12381"},{"title":"A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation","url":"https://arxiv.org/html/2602.01067"}]

Based on the search results, here's what I found about action multimodality, multi-modal action distributions, and behavior cloning in robot manipulation:

## Key Concepts and Approaches

When predicting future actions in robot manipulation, nonlinear plants or policies can result in multimodal predictions. Standard Behavior Cloning (BC) fails to learn multimodal driving decisions, where multiple valid actions exist for the same scenario, and this problem extends to robot manipulation tasks as well.

## Handling Multimodality in Behavior Cloning

Several approaches have been developed to address action multimodality:

1. **Diffusion Models**: Diffusion policy formulation provides stable training, allows the learned policy to accurately model multimodal action distributions, and accommodates high-dimensional action sequences. Diffusion policies are able to express complex multimodal action distributions and possess stable training behavior – requiring little task-specific hyperparameter tuning.

2. **Energy-Based Models (EBMs)**: EBMs learn an energy landscape over the action space, where desirable actions are associated with lower energy values and less favorable ones with higher energy. This formulation naturally accommodates multiple plausible actions by assigning low energy to all feasible choices.

3. **Generative Models**: Recent advances in imitation learning, particularly using generative modelling techniques like diffusion, have enabled policies to capture complex multi-modal action distributions.

## Loss Landscape Properties

Energy landscapes exhibit flatter minima in multimodal settings and sharper minima in unimodal ones, which reveals important structure in how different approaches handle the distribution of valid actions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3b4b8c9-2217-433f-a687-54e51a25057b",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "a552f42c-fe1b-4836-bef7-a84890a099b8",
  "toolUseResult": {
    "query": "\"action multimodality\" OR \"multi-modal action distribution\" behavior cloning robot manipulation loss landscape",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QESwxQWqF8Uo1jiNFHdtFJ",
        "content": [
          {
            "title": "Ch. 21 - Imitation Learning - Underactuated Robotics",
            "url": "https://underactuated.mit.edu/imitation.html"
          },
          {
            "title": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion .",
            "url": "https://arxiv.org/pdf/2303.04137"
          },
          {
            "title": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
            "url": "https://diffusion-policy.cs.columbia.edu/diffusion_policy_2023.pdf"
          },
          {
            "title": "Robotics: Science and Systems 2023",
            "url": "https://www.roboticsproceedings.org/rss19/p026.pdf"
          },
          {
            "title": "Exploring multimodal implicit behavior learning for vehicle navigation in simulated cities",
            "url": "https://arxiv.org/html/2509.15400v1"
          },
          {
            "title": "IMLE Policy: Fast and Sample Efficient Visuomotor Policy Learning via Implicit Maximum Likelihood Estimation",
            "url": "https://arxiv.org/html/2502.12371v2"
          },
          {
            "title": "CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation",
            "url": "https://arxiv.org/html/2508.01600v1"
          },
          {
            "title": "[2508.01600] CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation",
            "url": "https://arxiv.org/abs/2508.01600"
          },
          {
            "title": "Flow Matching Imitation Learning for Multi-Support Manipulation",
            "url": "https://arxiv.org/html/2407.12381"
          },
          {
            "title": "A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation",
            "url": "https://arxiv.org/html/2602.01067"
          }
        ]
      },
      "Based on the search results, here's what I found about action multimodality, multi-modal action distributions, and behavior cloning in robot manipulation:\n\n## Key Concepts and Approaches\n\nWhen predicting future actions in robot manipulation, nonlinear plants or policies can result in multimodal predictions. Standard Behavior Cloning (BC) fails to learn multimodal driving decisions, where multiple valid actions exist for the same scenario, and this problem extends to robot manipulation tasks as well.\n\n## Handling Multimodality in Behavior Cloning\n\nSeveral approaches have been developed to address action multimodality:\n\n1. **Diffusion Models**: Diffusion policy formulation provides stable training, allows the learned policy to accurately model multimodal action distributions, and accommodates high-dimensional action sequences. Diffusion policies are able to express complex multimodal action distributions and possess stable training behavior – requiring little task-specific hyperparameter tuning.\n\n2. **Energy-Based Models (EBMs)**: EBMs learn an energy landscape over the action space, where desirable actions are associated with lower energy values and less favorable ones with higher energy. This formulation naturally accommodates multiple plausible actions by assigning low energy to all feasible choices.\n\n3. **Generative Models**: Recent advances in imitation learning, particularly using generative modelling techniques like diffusion, have enabled policies to capture complex multi-modal action distributions.\n\n## Loss Landscape Properties\n\nEnergy landscapes exhibit flatter minima in multimodal settings and sharper minima in unimodal ones, which reveals important structure in how different approaches handle the distribution of valid actions."
    ],
    "durationSeconds": 7.8401933600000335
  },
  "sourceToolAssistantUUID": "b3b4b8c9-2217-433f-a687-54e51a25057b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-14T03:27:59.710Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019uRLjfS2scoWhPHUTmjPVe`</summary>

```json
{
  "query": "CORDS GRAD-MATCH online data selection convergence guarantee submodular SGD"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a552f42c-fe1b-4836-bef7-a84890a099b8",
  "isSidechain": false,
  "requestId": "req_011Cb1kVdL54viPH3E2h4gEu",
  "type": "assistant",
  "uuid": "008a92d8-369a-4cc8-9ebd-3dcdbdb41e26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ebBxL2TLHZgEPZM7KNrBK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 904,
      "cache_read_input_tokens": 53033,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 904,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 53033,
          "cache_creation_input_tokens": 904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 904
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

_source line 78 · 2026-05-14T03:28:06.137Z_

<details><summary>↩ Tool result · `toolu_019uRLjfS2scoWhPHUTmjPVe`</summary>

```text
Web search results for query: "CORDS GRAD-MATCH online data selection convergence guarantee submodular SGD"

Links: [{"title":"GRAD-MATCH: Gradient Matching based Data Subset Selection for Efﬁcient","url":"https://arxiv.org/pdf/2103.00123"},{"title":"[2103.00123] Grad-Match: Gradient Matching based Data Subset Selection for Efficient Deep Model Training","url":"https://ar5iv.labs.arxiv.org/html/2103.00123"},{"title":"(PDF) GRAD-MATCH: Gradient Matching based Data Subset Selection for Efficient Deep Model Training","url":"https://www.academia.edu/65221413/GRAD_MATCH_Gradient_Matching_based_Data_Subset_Selection_for_Efficient_Deep_Model_Training"},{"title":"(PDF) GRAD-MATCH: A Gradient Matching Based Data Subset Selection for Efficient Learning","url":"https://www.researchgate.net/publication/349704157_GRAD-MATCH_A_Gradient_Matching_Based_Data_Subset_Selection_for_Efficient_Learning"},{"title":"[2103.00123v1] GRAD-MATCH: A Gradient Matching Based Data Subset Selection for Efficient Learning","url":"https://arxiv.org/abs/2103.00123v1"},{"title":"GRAD-MATCH: Gradient Matching based Data Subset Selection for Efficient Deep Model Training","url":"https://papertalk.org/papertalks/32412"},{"title":"[Quick Review] GRAD-MATCH: Gradient Matching based Data Subset Selection for Efficient Deep Model Training","url":"https://liner.com/review/gradmatch-gradient-matching-based-data-subset-selection-for-efficient-deep"},{"title":"[PDF] GRAD-MATCH: Gradient Matching based Data Subset Selection for Efficient Deep Model Training | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GRAD-MATCH:-Gradient-Matching-based-Data-Subset-for-Killamsetty-Sivasubramanian/22bc75c1b758c83a6e29384453a4574c8b78f197"},{"title":"GRAD-MATCH: A Gradient Matching Based Data Subset Selection for Efficient Learning","url":"https://www.catalyzex.com/paper/grad-match-a-gradient-matching-based-data"},{"title":"Bandit Guided Submodular Curriculum for Adaptive Subset Selection","url":"https://openreview.net/pdf/9d49afab3cea887c5be1a1c9d0d3fedee0f9fb3e.pdf"}]

Based on the search results, here's what I found about GRAD-MATCH, CORDS, online data selection, convergence guarantees, and submodular SGD:

## GRAD-MATCH Overview

GRAD-MATCH is a gradient-matching algorithm that directly tries to minimize the gradient matching error. The framework finds subsets that closely match the gradient of the training or validation set using an orthogonal matching pursuit algorithm.

## Convergence Guarantees

The convergence of the general framework critically depends on an additive error term depending on how well the subset's weighted gradients match either the full training gradients or the full validation gradients. GRAD-MATCH extends its results to the case in which SGD is used instead of full GD to update the model, with convergence results and proofs provided.

## Submodular Connection

Minimizing the gradient error can be cast as a weakly submodular maximization problem. GRAD-MATCH achieves tighter convergence guarantees for various convex loss functions by modeling this error as weakly submodular and using OMP.

## CORDS Integration

GRAD-MATCH is available as a part of the CORDS toolkit. The CORDS toolkit is a comprehensive repository that includes this and other data selection methods for efficient deep learning.

The work provides theoretical foundations with rigorous convergence analysis while maintaining practical efficiency through the greedy orthogonal matching pursuit algorithm.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "008a92d8-369a-4cc8-9ebd-3dcdbdb41e26",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "b820d03a-d6a1-44b4-bd47-177477838840",
  "toolUseResult": {
    "query": "CORDS GRAD-MATCH online data selection convergence guarantee submodular SGD",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U2VYc7V2grCtibmHbSTk4W",
        "content": [
          {
            "title": "GRAD-MATCH: Gradient Matching based Data Subset Selection for Efﬁcient",
            "url": "https://arxiv.org/pdf/2103.00123"
          },
          {
            "title": "[2103.00123] Grad-Match: Gradient Matching based Data Subset Selection for Efficient Deep Model Training",
            "url": "https://ar5iv.labs.arxiv.org/html/2103.00123"
          },
          {
            "title": "(PDF) GRAD-MATCH: Gradient Matching based Data Subset Selection for Efficient Deep Model Training",
            "url": "https://www.academia.edu/65221413/GRAD_MATCH_Gradient_Matching_based_Data_Subset_Selection_for_Efficient_Deep_Model_Training"
          },
          {
            "title": "(PDF) GRAD-MATCH: A Gradient Matching Based Data Subset Selection for Efficient Learning",
            "url": "https://www.researchgate.net/publication/349704157_GRAD-MATCH_A_Gradient_Matching_Based_Data_Subset_Selection_for_Efficient_Learning"
          },
          {
            "title": "[2103.00123v1] GRAD-MATCH: A Gradient Matching Based Data Subset Selection for Efficient Learning",
            "url": "https://arxiv.org/abs/2103.00123v1"
          },
          {
            "title": "GRAD-MATCH: Gradient Matching based Data Subset Selection for Efficient Deep Model Training",
            "url": "https://papertalk.org/papertalks/32412"
          },
          {
            "title": "[Quick Review] GRAD-MATCH: Gradient Matching based Data Subset Selection for Efficient Deep Model Training",
            "url": "https://liner.com/review/gradmatch-gradient-matching-based-data-subset-selection-for-efficient-deep"
          },
          {
            "title": "[PDF] GRAD-MATCH: Gradient Matching based Data Subset Selection for Efficient Deep Model Training | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GRAD-MATCH:-Gradient-Matching-based-Data-Subset-for-Killamsetty-Sivasubramanian/22bc75c1b758c83a6e29384453a4574c8b78f197"
          },
          {
            "title": "GRAD-MATCH: A Gradient Matching Based Data Subset Selection for Efficient Learning",
            "url": "https://www.catalyzex.com/paper/grad-match-a-gradient-matching-based-data"
          },
          {
            "title": "Bandit Guided Submodular Curriculum for Adaptive Subset Selection",
            "url": "https://openreview.net/pdf/9d49afab3cea887c5be1a1c9d0d3fedee0f9fb3e.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about GRAD-MATCH, CORDS, online data selection, convergence guarantees, and submodular SGD:\n\n## GRAD-MATCH Overview\n\nGRAD-MATCH is a gradient-matching algorithm that directly tries to minimize the gradient matching error. The framework finds subsets that closely match the gradient of the training or validation set using an orthogonal matching pursuit algorithm.\n\n## Convergence Guarantees\n\nThe convergence of the general framework critically depends on an additive error term depending on how well the subset's weighted gradients match either the full training gradients or the full validation gradients. GRAD-MATCH extends its results to the case in which SGD is used instead of full GD to update the model, with convergence results and proofs provided.\n\n## Submodular Connection\n\nMinimizing the gradient error can be cast as a weakly submodular maximization problem. GRAD-MATCH achieves tighter convergence guarantees for various convex loss functions by modeling this error as weakly submodular and using OMP.\n\n## CORDS Integration\n\nGRAD-MATCH is available as a part of the CORDS toolkit. The CORDS toolkit is a comprehensive repository that includes this and other data selection methods for efficient deep learning.\n\nThe work provides theoretical foundations with rigorous convergence analysis while maintaining practical efficiency through the greedy orthogonal matching pursuit algorithm."
    ],
    "durationSeconds": 6.421619842000014
  },
  "sourceToolAssistantUUID": "008a92d8-369a-4cc8-9ebd-3dcdbdb41e26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 79 · 2026-05-14T03:28:11.056Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding. Let me synthesize and write the revised idea. Let me also quickly search for whether anyone has already done a benchmarking study of data selection methods on VLA/robot BC.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b820d03a-d6a1-44b4-bd47-177477838840",
  "isSidechain": false,
  "requestId": "req_011Cb1kWM2a6ZyKF7p1ZEcPX",
  "type": "assistant",
  "uuid": "b8f0af5b-3fa6-45cd-a5a6-d72c942a591a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019SGqKpPoPuHSZLiDxsQf4T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1072,
      "cache_read_input_tokens": 53937,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1072,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 53937,
          "cache_creation_input_tokens": 1072,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1072
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

_source line 80 · 2026-05-14T03:28:11.588Z_

Let me do one final search to make sure no one has already benchmarked these methods on VLA.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8f0af5b-3fa6-45cd-a5a6-d72c942a591a",
  "isSidechain": false,
  "requestId": "req_011Cb1kWM2a6ZyKF7p1ZEcPX",
  "type": "assistant",
  "uuid": "def23975-757b-466d-89bf-5a2c07b1382b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019SGqKpPoPuHSZLiDxsQf4T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1072,
      "cache_read_input_tokens": 53937,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1072,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 53937,
          "cache_creation_input_tokens": 1072,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1072
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

_source line 81 · 2026-05-14T03:28:12.543Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G35xgTy6vUBdMG8aWkgiJz`</summary>

```json
{
  "query": "benchmark comparison data selection methods robot imitation learning GLISTER CRAIG coreset VLA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "def23975-757b-466d-89bf-5a2c07b1382b",
  "isSidechain": false,
  "requestId": "req_011Cb1kWM2a6ZyKF7p1ZEcPX",
  "type": "assistant",
  "uuid": "d2590724-a44b-4d40-ad5b-972b8ec1b177",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019SGqKpPoPuHSZLiDxsQf4T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1072,
      "cache_read_input_tokens": 53937,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1072,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 53937,
          "cache_creation_input_tokens": 1072,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1072
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

_source line 82 · 2026-05-14T03:28:21.289Z_

<details><summary>↩ Tool result · `toolu_01G35xgTy6vUBdMG8aWkgiJz`</summary>

```text
Web search results for query: "benchmark comparison data selection methods robot imitation learning GLISTER CRAIG coreset VLA 2025 2026"

Links: [{"title":"A Coreset Selection of Coreset Selection Literature: Introduction and Recent Advances","url":"https://arxiv.org/html/2505.17799v1"},{"title":"GitHub - PatrickZH/DeepCore: Code for coreset selection methods · GitHub","url":"https://github.com/PatrickZH/DeepCore"},{"title":"GLISTER: Generalization based Data Subset Selection for Efﬁcient and Robust","url":"https://ojs.aaai.org/index.php/AAAI/article/view/16988/16795"},{"title":"GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning | Request PDF","url":"https://www.researchgate.net/publication/363394079_GLISTER_Generalization_based_Data_Subset_Selection_for_Efficient_and_Robust_Learning"},{"title":"Robotic Manipulation via Imitation Learning: Taxonomy, Evolution, Benchmark, and Challenges","url":"https://arxiv.org/html/2508.17449v1"},{"title":"Sample-Efficient Robot Skill Learning for Construction Tasks:","url":"https://arxiv.org/pdf/2512.14031"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"DataMIL : Selecting Data for Robot Imitation Learning with Datamodels","url":"https://arxiv.org/html/2505.09603"},{"title":"VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.pdf"},{"title":"RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation","url":"https://arxiv.org/html/2412.13877v1"}]

Based on my web search, I found relevant information about benchmark comparisons of data selection methods in the context of coreset selection and robot imitation learning. Here are the key findings:

## Coreset Selection Methods Comparison

Random, Forgetting, GradMatch, Herding, and Craig exhibit the lowest computation times, with k-Center Greedy and DeepFool requiring significantly more time. The most computationally expensive method, GraNd, stands out with a runtime of 125 minutes (for ImageNet-1K, it takes 1.5 days on a single RTXA6000 GPU). Methods like CAL, Glister, GraphCut, and Facility Location fall in the mid-range, balancing computational cost and selection quality.

## GLISTER vs CRAIG Performance

GLISTER still performs better than CRAIG run every epoch for MNIST data selection. On CIFAR-10, GLISTER achieves a 6x speedup at 10%, 2.5x speedup at 30%, and 1.5x speedup at 50%, while losing 3%, 1.2% and 0.2% respectively in accuracy.

## Robot Imitation Learning and VLA

DataMIL is a policy-driven data selection framework built on the datamodels paradigm that reasons about data selection in an end-to-end manner, using the policy itself to identify which data points will most improve performance.

VLABench is a large-scale language-conditioned manipulation benchmark to evaluate the comprehensive skill learning and generalization ability of action policies especially pre-trained vision-language-action models.

The search results provide comparisons of data selection methods across various approaches, though specific benchmark comparisons combining all the methods you mentioned (GLISTER, CRAIG, coreset, and VLA) in a single unified benchmark from 2025-2026 were not found in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2590724-a44b-4d40-ad5b-972b8ec1b177",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "db8893e5-c3cc-4dbe-8367-bd78e946f90b",
  "toolUseResult": {
    "query": "benchmark comparison data selection methods robot imitation learning GLISTER CRAIG coreset VLA 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EW3hvFan5RMuviR9eFCASb",
        "content": [
          {
            "title": "A Coreset Selection of Coreset Selection Literature: Introduction and Recent Advances",
            "url": "https://arxiv.org/html/2505.17799v1"
          },
          {
            "title": "GitHub - PatrickZH/DeepCore: Code for coreset selection methods · GitHub",
            "url": "https://github.com/PatrickZH/DeepCore"
          },
          {
            "title": "GLISTER: Generalization based Data Subset Selection for Efﬁcient and Robust",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/16988/16795"
          },
          {
            "title": "GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning | Request PDF",
            "url": "https://www.researchgate.net/publication/363394079_GLISTER_Generalization_based_Data_Subset_Selection_for_Efficient_and_Robust_Learning"
          },
          {
            "title": "Robotic Manipulation via Imitation Learning: Taxonomy, Evolution, Benchmark, and Challenges",
            "url": "https://arxiv.org/html/2508.17449v1"
          },
          {
            "title": "Sample-Efficient Robot Skill Learning for Construction Tasks:",
            "url": "https://arxiv.org/pdf/2512.14031"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "DataMIL : Selecting Data for Robot Imitation Learning with Datamodels",
            "url": "https://arxiv.org/html/2505.09603"
          },
          {
            "title": "VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.pdf"
          },
          {
            "title": "RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation",
            "url": "https://arxiv.org/html/2412.13877v1"
          }
        ]
      },
      "Based on my web search, I found relevant information about benchmark comparisons of data selection methods in the context of coreset selection and robot imitation learning. Here are the key findings:\n\n## Coreset Selection Methods Comparison\n\nRandom, Forgetting, GradMatch, Herding, and Craig exhibit the lowest computation times, with k-Center Greedy and DeepFool requiring significantly more time. The most computationally expensive method, GraNd, stands out with a runtime of 125 minutes (for ImageNet-1K, it takes 1.5 days on a single RTXA6000 GPU). Methods like CAL, Glister, GraphCut, and Facility Location fall in the mid-range, balancing computational cost and selection quality.\n\n## GLISTER vs CRAIG Performance\n\nGLISTER still performs better than CRAIG run every epoch for MNIST data selection. On CIFAR-10, GLISTER achieves a 6x speedup at 10%, 2.5x speedup at 30%, and 1.5x speedup at 50%, while losing 3%, 1.2% and 0.2% respectively in accuracy.\n\n## Robot Imitation Learning and VLA\n\nDataMIL is a policy-driven data selection framework built on the datamodels paradigm that reasons about data selection in an end-to-end manner, using the policy itself to identify which data points will most improve performance.\n\nVLABench is a large-scale language-conditioned manipulation benchmark to evaluate the comprehensive skill learning and generalization ability of action policies especially pre-trained vision-language-action models.\n\nThe search results provide comparisons of data selection methods across various approaches, though specific benchmark comparisons combining all the methods you mentioned (GLISTER, CRAIG, coreset, and VLA) in a single unified benchmark from 2025-2026 were not found in these results."
    ],
    "durationSeconds": 8.741869371999986
  },
  "sourceToolAssistantUUID": "d2590724-a44b-4d40-ad5b-972b8ec1b177",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 83 · 2026-05-14T03:28:21.316Z_

```json
{
  "parentUuid": "db8893e5-c3cc-4dbe-8367-bd78e946f90b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "bba32eb7-1da6-4010-b979-ca7f34926124",
  "timestamp": "2026-05-14T03:28:21.316Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 84_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Beyond Difficulty: Diversity-Aware Dynamic Sampling for Data-Efficient…",
  "leafUuid": "bba32eb7-1da6-4010-b979-ca7f34926124",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Runtime record

_source line 85_

```json
{
  "type": "ai-title",
  "aiTitle": "Benchmark diversity-aware selection methods on VLA BC",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Assistant

_source line 86 · 2026-05-14T03:28:25.582Z_

Good — no one has benchmarked general-purpose online selection methods (UDS, GLISTER, CRAIG) on VLA BC. That gap is real. Now let me do the deep thinking and write the revision.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bba32eb7-1da6-4010-b979-ca7f34926124",
  "isSidechain": false,
  "requestId": "req_011Cb1kXTtMAL2RVcNkzMWNr",
  "type": "assistant",
  "uuid": "69e24781-505e-430b-9721-e0afbd4d981b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEAanCcSQ3Ns5NmvZ78DAL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 55009,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1269,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 55009,
          "cache_creation_input_tokens": 1269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1269
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

_source line 87 · 2026-05-14T03:28:27.262Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RKq4ytA99eKsYjp2an2Q5o`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.08623",
  "prompt": "Extract the full abstract, the key method details (how mutual information is estimated, what embeddings are used, how trajectories are scored), and what benchmarks/robots they evaluate on. Note any limitations mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69e24781-505e-430b-9721-e0afbd4d981b",
  "isSidechain": false,
  "requestId": "req_011Cb1kXTtMAL2RVcNkzMWNr",
  "type": "assistant",
  "uuid": "2eb1c5f9-4bb7-4394-814d-6b848f21f344",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEAanCcSQ3Ns5NmvZ78DAL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 55009,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1269,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 55009,
          "cache_creation_input_tokens": 1269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1269
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

_source line 88 · 2026-05-14T03:28:34.368Z_

<details><summary>↩ Tool result · `toolu_01RKq4ytA99eKsYjp2an2Q5o`</summary>

```text
# Robot Data Curation with Mutual Information Estimators

## Full Abstract

"The performance of imitation learning policies often hinges on the datasets with which they are trained. Consequently, investment in data collection for robotics has grown across both industrial and academic labs. However, despite the marked increase in the quantity of demonstrations collected, little work has sought to assess the quality of said data despite mounting evidence of its importance in other areas such as vision and language. In this work, we take a critical step towards addressing the data quality in robotics. Given a dataset of demonstrations, we aim to estimate the relative quality of individual demonstrations in terms of both action diversity and predictability. To do so, we estimate the average contribution of a trajectory towards the mutual information between states and actions in the entire dataset, which captures both the entropy of the marginal action distribution and the state-conditioned action entropy. Though commonly used mutual information estimators require vast amounts of data often beyond the scale available in robotics, we introduce a novel technique based on k-nearest neighbor estimates of mutual information on top of simple VAE embeddings of states and actions. Empirically, we demonstrate that our approach is able to partition demonstration datasets by quality according to human expert scores across a diverse set of benchmarks spanning simulation and real world environments. Moreover, training policies based on data filtered by our method leads to a 5-10% improvement in RoboMimic and better performance on real ALOHA and Franka setups."

## Key Method Details

**Mutual Information Estimation:** The authors employ "k-nearest neighbor estimates of mutual information" combined with "simple VAE embeddings of states and actions" to overcome the data scarcity challenges typical in robotics applications.

**Trajectory Scoring:** They calculate each trajectory's contribution toward the mutual information between states and actions, capturing both action distribution entropy and state-conditioned action entropy.

## Benchmarks and Robots Evaluated

- RoboMimic (simulation)
- ALOHA (real robot)
- Franka (real robot)
- Additional diverse simulation and real-world environments

## Limitations

The paper notes that conventional mutual information estimators demand significantly more data than typically available in robotics contexts, which motivated their novel approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2eb1c5f9-4bb7-4394-814d-6b848f21f344",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "751ff30a-91d3-4f0d-bbcb-1f0e4c55a60f",
  "toolUseResult": {
    "bytes": 47429,
    "code": 200,
    "codeText": "OK",
    "result": "# Robot Data Curation with Mutual Information Estimators\n\n## Full Abstract\n\n\"The performance of imitation learning policies often hinges on the datasets with which they are trained. Consequently, investment in data collection for robotics has grown across both industrial and academic labs. However, despite the marked increase in the quantity of demonstrations collected, little work has sought to assess the quality of said data despite mounting evidence of its importance in other areas such as vision and language. In this work, we take a critical step towards addressing the data quality in robotics. Given a dataset of demonstrations, we aim to estimate the relative quality of individual demonstrations in terms of both action diversity and predictability. To do so, we estimate the average contribution of a trajectory towards the mutual information between states and actions in the entire dataset, which captures both the entropy of the marginal action distribution and the state-conditioned action entropy. Though commonly used mutual information estimators require vast amounts of data often beyond the scale available in robotics, we introduce a novel technique based on k-nearest neighbor estimates of mutual information on top of simple VAE embeddings of states and actions. Empirically, we demonstrate that our approach is able to partition demonstration datasets by quality according to human expert scores across a diverse set of benchmarks spanning simulation and real world environments. Moreover, training policies based on data filtered by our method leads to a 5-10% improvement in RoboMimic and better performance on real ALOHA and Franka setups.\"\n\n## Key Method Details\n\n**Mutual Information Estimation:** The authors employ \"k-nearest neighbor estimates of mutual information\" combined with \"simple VAE embeddings of states and actions\" to overcome the data scarcity challenges typical in robotics applications.\n\n**Trajectory Scoring:** They calculate each trajectory's contribution toward the mutual information between states and actions, capturing both action distribution entropy and state-conditioned action entropy.\n\n## Benchmarks and Robots Evaluated\n\n- RoboMimic (simulation)\n- ALOHA (real robot)\n- Franka (real robot)\n- Additional diverse simulation and real-world environments\n\n## Limitations\n\nThe paper notes that conventional mutual information estimators demand significantly more data than typically available in robotics contexts, which motivated their novel approach.",
    "durationMs": 7094,
    "url": "https://arxiv.org/abs/2502.08623"
  },
  "sourceToolAssistantUUID": "2eb1c5f9-4bb7-4394-814d-6b848f21f344",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-14T03:28:39.755Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017PVXJ8AN1a1FWgUxMvGByb`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.16882",
  "prompt": "Find and extract: 1) The exact batch selection algorithm (pseudocode or step-by-step), 2) How alpha (the diversity weight) is set - is it fixed or adaptive?, 3) What happens with temporal/sequential data - does UDS handle correlated samples?, 4) Any discussion of multi-modal outputs (not text), 5) Any acknowledged limitations about applying to non-LLM domains."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "751ff30a-91d3-4f0d-bbcb-1f0e4c55a60f",
  "isSidechain": false,
  "requestId": "req_011Cb1kYRiAC4CbEc8DVGyUC",
  "type": "assistant",
  "uuid": "af715a1a-628f-4f90-a75d-788a133b9897",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUyy3fjQnLnCXTeZTfePvQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 665,
      "cache_read_input_tokens": 56278,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 665,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 56278,
          "cache_creation_input_tokens": 665,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 665
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

_source line 90 · 2026-05-14T03:28:45.809Z_

<details><summary>↩ Tool result · `toolu_017PVXJ8AN1a1FWgUxMvGByb`</summary>

```text
# UDS Framework: Key Technical Details

## 1) Batch Selection Algorithm

The pseudocode is explicitly provided as **Algorithm 1** in the paper. The core steps are:

1. Forward pass to extract logits matrix for each sample
2. Calculate intra-sample score via nuclear norm: `s_intra = ||L||*`
3. Project logits to low-dimensional embedding: `z = vec(Γ₂·L·Γ₁ᵀ)`
4. Calculate inter-sample diversity distance to memory buffer
5. Combine scores: `s_total = s_intra + α·s_inter`
6. Select top-K samples by total score
7. Update FIFO memory buffer with selected sample embeddings

## 2) Alpha (Diversity Weight) Setting

Alpha is **dataset and model-dependent**, not adaptive. The paper states: "The optimal data selection ratio α is highly dependent on both the backbone model and the dataset." Table 5 in Appendix C reports specific α values for different model-dataset combinations, suggesting practitioners must tune this hyperparameter empirically rather than using a fixed value.

## 3) Temporal/Sequential Data Handling

**Not addressed.** The paper focuses on independent batch sampling and doesn't discuss correlated or sequentially-dependent samples. The FIFO buffer is "first-in-first-out" but treats samples as independently selected candidates without explicit temporal dependencies.

## 4) Multi-Modal Outputs

**Not discussed.** The method operates on "logits matrix" from autoregressive language models specifically. No experiments extend to multi-modal or non-text outputs.

## 5) Acknowledged Limitations for Non-LLM Domains

The authors note in Appendix F: "applying to non-LLM domains represents an important avenue for future work," implicitly acknowledging the framework is currently LLM-specific and domain-specific adaptations remain unclear.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af715a1a-628f-4f90-a75d-788a133b9897",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "497501a8-659c-40ee-9721-13db87154c42",
  "toolUseResult": {
    "bytes": 571047,
    "code": 200,
    "codeText": "OK",
    "result": "# UDS Framework: Key Technical Details\n\n## 1) Batch Selection Algorithm\n\nThe pseudocode is explicitly provided as **Algorithm 1** in the paper. The core steps are:\n\n1. Forward pass to extract logits matrix for each sample\n2. Calculate intra-sample score via nuclear norm: `s_intra = ||L||*`\n3. Project logits to low-dimensional embedding: `z = vec(Γ₂·L·Γ₁ᵀ)`\n4. Calculate inter-sample diversity distance to memory buffer\n5. Combine scores: `s_total = s_intra + α·s_inter`\n6. Select top-K samples by total score\n7. Update FIFO memory buffer with selected sample embeddings\n\n## 2) Alpha (Diversity Weight) Setting\n\nAlpha is **dataset and model-dependent**, not adaptive. The paper states: \"The optimal data selection ratio α is highly dependent on both the backbone model and the dataset.\" Table 5 in Appendix C reports specific α values for different model-dataset combinations, suggesting practitioners must tune this hyperparameter empirically rather than using a fixed value.\n\n## 3) Temporal/Sequential Data Handling\n\n**Not addressed.** The paper focuses on independent batch sampling and doesn't discuss correlated or sequentially-dependent samples. The FIFO buffer is \"first-in-first-out\" but treats samples as independently selected candidates without explicit temporal dependencies.\n\n## 4) Multi-Modal Outputs\n\n**Not discussed.** The method operates on \"logits matrix\" from autoregressive language models specifically. No experiments extend to multi-modal or non-text outputs.\n\n## 5) Acknowledged Limitations for Non-LLM Domains\n\nThe authors note in Appendix F: \"applying to non-LLM domains represents an important avenue for future work,\" implicitly acknowledging the framework is currently LLM-specific and domain-specific adaptations remain unclear.",
    "durationMs": 6050,
    "url": "https://arxiv.org/html/2510.16882"
  },
  "sourceToolAssistantUUID": "af715a1a-628f-4f90-a75d-788a133b9897",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 91 · 2026-05-14T03:29:06.870Z_

<details><summary>Logged reasoning block</summary>

```text
This is very useful. UDS explicitly acknowledges that "applying to non-LLM domains represents an important avenue for future work" and doesn't handle temporal/sequential data or multi-modal outputs. This validates my approach of framing the contribution as bridging online data selection from LLM/classification to VLA BC.

Now let me write the full revised idea. I have all the information I need.

Key insights from my research:
1. UDS: Fixed alpha (not adaptive), no temporal handling, LLM-specific (nuclear norm of text logits), acknowledges non-LLM domains as future work
2. GLISTER: Validation-set-based selection, submodular optimization, never applied to multi-modal/robotics


3. CRAIG: Gradient-matching via facility-location, i.i.d. assumption, never applied to sequential demonstration data
4. D2 Pruning: Pre-training static selection (not online), graph message passing
5. InfoMax: Pre-training static selection, QDP formulation
6. D3: LLM instruction tuning specific
7. DemInf (Hejna): Static curation, MI-based, applied to robotics but pre-training
8. DemoSpeedup: Frame-level selection within demos, entropy-guided

The genuine gap here is that none of these methods—UDS, GLISTER, CRAIG, or gradient-matching approaches—have been adapted for online selection in vision-language action models, which is where my contribution sits.

Looking at the specifics, UDS explicitly marks non-LLM domains as future work, and critically, none of these methods account for the temporal dependencies within trajectories or handle the complexity of multi-modal action distributions in continuous control spaces. Whether they'd even transfer to VLA behavior cloning is still an open question.

My revised framing centers on three concrete contributions: systematically evaluating online data selection methods on VLA behavior cloning for the first time, identifying failure modes specific to this setting, and developing trajectory-aware adaptations to address them. This is a substantial reframing of the paper—not just a pivot away from the core problem, but a major revision that changes the landscape analysis, approach, and what I'm actually contributing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "497501a8-659c-40ee-9721-13db87154c42",
  "isSidechain": false,
  "requestId": "req_011Cb1kZGjwEAW1d9b9REo1x",
  "type": "assistant",
  "uuid": "aca566cc-be0a-444e-ac89-1c2b4d20ceb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXxwowULxiuhshbnruJnpH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 56943,
      "output_tokens": 7261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 617,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7261,
          "cache_read_input_tokens": 56943,
          "cache_creation_input_tokens": 617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 617
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

_source line 92 · 2026-05-14T03:29:10.093Z_

Now I have deep understanding of all the key related work. Let me synthesize and write the complete revision. The core findings:

1. **UDS explicitly says non-LLM domains are "future work"** — it doesn't handle temporal correlations or multi-modal outputs
2. **GLISTER/CRAIG** have never been applied to multi-modal robotics data
3. **No one has benchmarked** general-purpose online selection on VLA BC
4. **The genuine gap** is not "no one combines loss + diversity" but "we don't know if/how these methods transfer to VLA BC, which has trajectory structure, action multi-modality, and multi-modal inputs that don't exist in LLM/classification settings"

This requires a **major revision**: complete reframing from "novel method" to "empirical understanding of VLA-specific failure modes + adapted method."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aca566cc-be0a-444e-ac89-1c2b4d20ceb2",
  "isSidechain": false,
  "requestId": "req_011Cb1kZGjwEAW1d9b9REo1x",
  "type": "assistant",
  "uuid": "f14e489d-664e-4f55-823e-247f7f09251d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXxwowULxiuhshbnruJnpH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 56943,
      "output_tokens": 7261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 617,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7261,
          "cache_read_input_tokens": 56943,
          "cache_creation_input_tokens": 617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 617
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

_source line 93 · 2026-05-14T03:31:52.267Z_

<details open><summary>🔧 Tool call — Write · `toolu_01JqXwCs47eLZrdBqjLoSz1z`</summary>

```json
{
  "file_path": "/tmp/revised_idea.json",
  "content": "{\n  \"change_type\": \"major\",\n  \"title\": \"Do Online Data Selection Methods Transfer to VLA Training? A Benchmarking Study with Trajectory-Aware Adaptations\",\n  \"core_problem\": \"VLA behavioral cloning datasets contain massive redundancy — workshop findings ('On Data Redundancy in VLA Training', ICRA 2026 workshop) suggest VLAs can train on as little as 5–30% of LIBERO data with minimal performance loss, and difficulty-based subsampling (TSS) actively hurts by sacrificing diversity. Meanwhile, the broader ML community has developed sophisticated online data selection methods that balance diversity and informativeness during training: UDS (ICML 2025) combines nuclear-norm utility with embedding-based inter-sample diversity for LLM SFT; GLISTER-Online (AAAI 2021) performs submodular selection with convergence guarantees; CRAIG (ICML 2020) uses facility-location coreset selection during SGD; D2 Pruning (ICLR 2024) balances diversity and difficulty via graph message passing; InfoMax (ICLR 2025) maximizes information content while minimizing redundancy. However, ALL of these methods were designed for and evaluated exclusively on classification or language tasks. UDS explicitly acknowledges that 'applying to non-LLM domains represents an important avenue for future work.' None handle the structural properties unique to VLA behavioral cloning: (1) temporal autocorrelation within demonstration trajectories, where consecutive action chunks share redundancy invisible to per-sample embedding distances; (2) action multi-modality, where multiple valid action sequences exist for the same observation, making loss an unreliable proxy for informativeness; and (3) heterogeneous, multi-granularity diversity requirements spanning task type, action phase, scene configuration, and embodiment. The critical open question is not whether to combine diversity with difficulty — that problem is well-studied — but whether existing solutions transfer to VLA BC, where these structural differences may cause systematic failures.\",\n  \"opportunity\": \"No existing work has systematically evaluated whether general-purpose online data selection methods (UDS, GLISTER-Online, CRAIG, GRAD-MATCH) transfer to VLA behavioral cloning. This creates a dual opportunity: (1) An empirical benchmarking contribution — the first head-to-head comparison of online selection methods on VLA BC, revealing which components of existing methods survive the domain transfer and which break. (2) A methodological contribution — VLA-specific adaptations that address the diagnosed failure modes. Three VLA-specific structural properties make this transfer non-trivial and potentially reveal new insights:\\n\\n- **Trajectory-level temporal redundancy**: In VLA datasets, action chunks from the same trajectory are informationally linked (reaching→grasping→placing follows a coherent strategy). Selecting one informative chunk from trajectory T should reduce the utility of nearby chunks in T — but per-sample embedding diversity (as in UDS, CRAIG) treats all chunks as i.i.d. and cannot capture this.\\n\\n- **Action multi-modality**: From the same observation state, multiple valid manipulation strategies exist (approach from left vs. right, different grasp points). High prediction loss may indicate the model hasn't learned a particular strategy — or that the demonstration took an uncommon-but-valid approach. UDS's nuclear-norm utility and GLISTER's loss-based selection both conflate genuine difficulty with action-distributional ambiguity. This is well-documented in the diffusion policy literature (Chi et al., RSS 2023) but has not been connected to data selection.\\n\\n- **Multi-granularity coverage**: VLA training requires coverage across tasks, action phases (reach/grasp/place/insert), scene configurations, and object sets simultaneously. A single embedding-space diversity measure (as in UDS's inter-sample distance or CRAIG's facility-location) may optimize one axis while neglecting others.\\n\\nThese failure modes are testable hypotheses, not assumptions. If existing methods transfer well, the benchmarking study itself is the contribution. If they fail, the failure mode analysis and VLA-adapted solutions become the contribution. Either outcome advances the field.\",\n  \"landscape\": \"**Online diversity-aware data selection for training (the methods we benchmark):**\\n\\n- UDS (ICML 2025, Zou et al.) performs online batch selection during LLM SFT using s_total = s_intra + α·s_inter, where s_intra is the nuclear norm of the logits matrix (capturing both utility and intra-sample diversity) and s_inter is the average L2 distance to a FIFO memory buffer of compressed logits embeddings. α is dataset/model-dependent and fixed per run. Tested on MMLU, ScienceQA, GSM8K, HumanEval with Llama-3.1-8B and Qwen-2.5-7B. Explicitly notes non-LLM domains as future work. Does not handle temporal correlations or multi-modal outputs.\\n\\n- GLISTER-Online (AAAI 2021, Killamsetty et al.) formulates online data selection as bi-level optimization: select a subset maximizing validation log-likelihood while training on it. The inner selection is (weakly) submodular, enabling greedy approximation with convergence guarantees. Tested on image classification (CIFAR-10/100, MNIST) and NLP classification. Requires a held-out validation set, which is non-trivial for multi-task VLA (validation must cover all tasks proportionally).\\n\\n- CRAIG (ICML 2020, Mirzasoleiman et al.) selects weighted coresets whose gradients approximate the full-dataset gradient via facility-location maximization. Proven convergence to (near-)optimal for convex objectives. Tested on logistic regression and image classification. Assumes i.i.d. data; gradient-matching may be ill-conditioned for high-dimensional multi-modal VLA outputs.\\n\\n- GRAD-MATCH (ICML 2021, Killamsetty et al.) extends CRAIG with orthogonal matching pursuit for tighter gradient approximation. Available in the CORDS toolkit alongside GLISTER and CRAIG.\\n\\n**Static/pre-training diversity-difficulty balancing (related but not online):**\\n\\n- D2 Pruning (ICLR 2024, Maharana et al.) represents the dataset as a graph and uses message passing to select subsets balancing diversity (edges) and difficulty (node scores). Effective at low-to-medium pruning rates for image classification and NLP. Static pre-training method — cannot adapt during training.\\n\\n- InfoMax (ICLR 2025, Tan et al.) formulates coreset selection as discrete quadratic programming maximizing information content minus pairwise redundancy. Scales to millions of samples via gradient-based solver with sparsification. Applied to image classification, VL pre-training, and LLM instruction tuning. Static selection.\\n\\n- D3 (IJCAI 2025) combines diversity, difficulty, and dependability for LLM instruction tuning via a weighted coreset objective. Iterative but not truly online (rounds of score-then-select).\\n\\n**Robotics demonstration curation (domain-specific but static/offline):**\\n\\n- SCIZOR (ICRA 2026) uses self-supervised progress prediction and embedding clustering for one-time pre-training curation of robot demonstrations, achieving ~15% improvement.\\n\\n- CUPID (CoRL 2025) estimates each demonstration's causal impact via influence functions at a fixed policy checkpoint. One-pass, not adaptive.\\n\\n- Demo-SCORE (RSS 2025) performs iterative curation via train→rollout→classify→re-filter, genuinely adapting to model competence — but requires environment rollouts.\\n\\n- DemInf (RSS 2026, Hejna et al.) introduces Demonstration Information Estimation using k-nearest-neighbor mutual information estimates over VAE embeddings of states and actions. Unsupervised, embedding-based quality assessment achieving 5-10% improvement on RoboMimic and real-robot tasks. Static curation; does not adapt during training.\\n\\n- DataMIL (2025) uses datamodels for end-to-end policy-driven selection. Pre-training.\\n\\n- QoQ (2026) uses influence functions with trajectory-wise aggregation.\\n\\n**Sub-trajectory and frame-level selection:**\\n\\n- DemoSpeedup (CoRL 2025, Guo et al.) performs entropy-guided frame-level downsampling within demonstrations, accelerating policy execution 1.7-3× while maintaining success rates. Operates at sub-trajectory granularity similar to our action-chunk level, but targets execution speed rather than training efficiency.\\n\\n- 'On Data Redundancy in VLA Training' (ICRA 2026 workshop) evaluates random vs. TSS difficulty-based frame selection on LIBERO, finding random subsampling (preserving diversity) consistently outperforms difficulty-based selection. A workshop paper whose specific quantitative claims (95% redundancy, TSS underperformance) should be verified, but the qualitative finding that diversity matters more than difficulty aligns with broader observations.\\n\\n**Balanced BC and reweighting:**\\n\\n- 'Towards Balanced Behavior Cloning' (Autonomous Robots 2026) addresses subtask imbalance (90% reaching, 10% grasping) via meta-gradient rebalancing — orthogonal to within-subtask redundancy.\\n\\n- Dynamic Loss-Based Sample Reweighting (ICLR 2025) performs token-level reweighting for LLM pretraining with convergence guarantees. No diversity preservation.\\n\\n- Freshness-Aware PER (April 2026) addresses priority staleness in RL post-training.\\n\\n**The gap we address**: Existing online data selection methods (UDS, GLISTER, CRAIG, GRAD-MATCH) have never been evaluated on VLA behavioral cloning. Whether their assumptions (i.i.d. samples, loss-as-utility, single-space embedding diversity) hold in the VLA BC setting — with trajectory temporal structure, action multi-modality, and multi-granularity coverage needs — is an open empirical question with practical implications for the growing scale of robot demonstration datasets.\",\n  \"approach\": \"We propose a three-phase study that first benchmarks existing online data selection methods on VLA BC, then diagnoses failure modes, and finally introduces trajectory-aware adaptations. This structure ensures contributions regardless of whether existing methods transfer well or poorly.\\n\\n**Phase 1: Benchmarking Online Data Selection for VLA BC**\\n\\nWe systematically evaluate existing methods on LIBERO (Spatial, Object, Goal, Long) with SmolVLA and OpenVLA-OFT:\\n\\n- Online methods (our main focus): UDS (adapted from text logits to action-chunk predictions), GLISTER-Online, CRAIG, GRAD-MATCH\\n- Static curation baselines: SCIZOR, DemInf, random subsampling, TSS difficulty-based\\n- Simple dynamic baselines: loss-proportional PER, Dynamic Loss-Based Reweighting (adapted to action chunks)\\n- Reference: full-dataset training, uniform sampling\\n\\nAll methods evaluated at 10%, 25%, 50%, and 100% effective data utilization (for online methods, this means the fraction of each epoch's data used per gradient step). We report per-suite success rates (not just averages, following best practices from LIBERO-Plus) across 3 seeds.\\n\\nAdapting existing methods to VLA requires non-trivial engineering choices that we document carefully: UDS's nuclear-norm utility must be replaced (VLA action heads produce continuous vectors, not logit matrices); GLISTER requires a VLA-appropriate validation set covering all tasks; CRAIG's gradient computation scales with VLA's multi-modal parameter count. These adaptations are themselves informative about domain transfer.\\n\\n**Phase 2: Failure Mode Diagnosis**\\n\\nFor each method, we analyze:\\n\\n(H1) **Loss-utility conflation**: We measure the correlation between per-chunk loss and downstream contribution to policy performance (estimated via leave-one-out or influence-function approximation). In VLA BC, we hypothesize this correlation is weaker than in LLM SFT due to action multi-modality — high-loss chunks may represent valid alternative strategies, not genuine difficulty. We test this by examining whether high-loss chunks cluster around action-multimodal states (states where the dataset contains diverse actions).\\n\\n(H2) **Trajectory-blind redundancy**: We measure whether methods select chunks uniformly across trajectories or cluster selections within a few trajectories. Embedding-based diversity (UDS, CRAIG) may select diverse-looking chunks from the same trajectory (different visual frames as the robot moves) while missing coverage of other trajectories with different strategies.\\n\\n(H3) **Single-scale diversity collapse**: We measure coverage across multiple axes — task identity, action phase (reaching vs. grasping vs. placing, identified via action-velocity thresholds), and scene configuration — for each method's selected subsets. A method that maximizes embedding diversity may achieve good scene coverage but poor action-phase coverage, or vice versa.\\n\\nVisualization: For each method, we produce selection heatmaps showing which chunks are selected across trajectories, tasks, and training epochs, enabling qualitative assessment of selection patterns.\\n\\n**Phase 3: Trajectory-Aware Adaptations (TADS)**\\n\\nBased on Phase 2 findings, we introduce Trajectory-Aware Data Selection (TADS), with each component addressing a diagnosed failure mode:\\n\\n1. **Trajectory-Conditioned Utility (addresses H1)**: Instead of raw per-chunk loss L_i, we compute utility as u_i = L_i / L_bar(traj(i), phase(i)), normalizing by the average loss of chunks at the same action phase within similar trajectories. This distinguishes 'genuinely difficult manipulation' from 'uncommon-but-valid strategy' — a chunk with high absolute loss but average loss-for-its-trajectory-type gets moderate (not high) utility. For VLA architectures using diffusion action heads, we additionally use the variance across denoising samples as a complementary utility signal, as high variance directly indicates action multi-modality.\\n\\n2. **Trajectory-Aware Redundancy (addresses H2)**: We augment per-chunk embedding similarity with a trajectory-identity penalty: red_i = (1/K) Σ_{j ∈ KNN(i)} sim(e_i, e_j) · (1 + γ · 1[traj(i) = traj(j)]), where γ > 0 penalizes within-trajectory neighbors more heavily. This ensures that selecting one informative chunk from a trajectory appropriately reduces the priority of nearby chunks in the same trajectory, even if their embeddings differ due to robot motion.\\n\\n3. **Multi-Granularity Coverage (addresses H3)**: Instead of a single facility-location objective, we decompose batch-level diversity into: FL_task (coverage across task identities) + FL_phase (coverage across action phases) + FL_scene (coverage across scene embeddings), with relative weights {w_task, w_phase, w_scene} tuned on a held-out validation split. For the task and phase axes, this reduces to stratified sampling constraints; for the scene axis, it uses facility-location over observation embeddings.\\n\\nEach TADS component is ablated independently to quantify its marginal contribution. We also test TADS as an augmentation of UDS and GLISTER-Online (replacing their diversity/utility components with our trajectory-aware versions) to isolate VLA-specific vs. framework-specific effects.\\n\\n**Implementation**: All methods implemented within a unified evaluation framework compatible with SmolVLA and OpenVLA-OFT training pipelines. Online selection methods implemented as drop-in DistributedSampler replacements. GLISTER-Online and CRAIG adapted from the CORDS toolkit. UDS re-implemented from the official codebase. Embeddings computed from VLA's frozen vision-language encoder. KNN precomputed; only loss-based scores refreshed online.\\n\\n**Evaluation**: LIBERO (all 4 suites) as primary benchmark, directly comparable to 'On Data Redundancy' results. Per-suite success rates reported separately (following LIBERO-Plus recommendations). SimplerEnv for breadth. Metrics: (1) success rate at each data fraction, (2) data efficiency curves showing sample-efficiency gains, (3) training wall-clock time to reach target success rate, (4) selection overhead as fraction of training time. Statistical significance via 3 seeds with bootstrap confidence intervals.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~1200h A100 80GB (Phase 1: ~600h for 10 methods × 4 suites × 4 fractions × 3 seeds = 480 runs × ~1.2h avg; Phase 2: ~100h analysis; Phase 3: ~500h for TADS + ablations)\",\n      \"gpu_utilization\": \"Low (~25%). Significant implementation effort for adapting UDS/GLISTER/CRAIG to VLA pipelines; building unified evaluation framework; failure mode analysis tooling.\",\n      \"timeline\": \"4-5 months\",\n      \"team\": \"2-3 researchers (one for adapting/implementing online selection methods from CORDS/UDS, one for VLA training infrastructure and LIBERO evaluation, one for failure mode analysis and visualization)\",\n      \"estimated_gpu_cost\": \"$1,800 (1200h × ~$1.50/h spot A100 80GB)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~1400h A100 80GB\",\n      \"gpu_utilization\": \"Moderate (~55%). Agent handles experiment orchestration and config generation; human reviews failure mode visualizations and guides Phase 3 design based on Phase 2 findings.\",\n      \"timeline\": \"6-8 weeks\",\n      \"team\": \"1-2 researchers, ~1hr/day reviewing Phase 2 diagnostics and steering ablation priorities\",\n      \"claude_api_cost\": \"$300-500 (~400 conversation turns for method adaptation, experiment management, analysis)\",\n      \"estimated_gpu_cost\": \"$2,100 (1400h × ~$1.50/h spot A100 80GB)\",\n      \"risk_note\": \"Simulation-only (LIBERO + SimplerEnv). If existing methods transfer well to VLA BC, the contribution narrows to a useful benchmarking paper with smaller TADS improvements. This is still publishable but less impactful — consider adding Open X-Embodiment experiments for broader validation.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~2800h A100 80GB (full benchmarking grid + failure mode sweeps + TADS ablations across all configurations)\",\n      \"gpu_utilization\": \"~85%. Agent pipelines Phase 1→2→3 sequentially with parallel runs within each phase.\",\n      \"timeline\": \"12-18 days with 8 A100 GPUs in parallel\",\n      \"team\": \"0 (initial setup + final review only)\",\n      \"claude_api_cost\": \"$600-900 (~800 turns for end-to-end implementation, adaptation of multiple codebases, experiment orchestration, failure diagnosis, and paper drafting)\",\n      \"estimated_gpu_cost\": \"$4,200 (2800h × ~$1.50/h spot A100 80GB)\",\n      \"speed_bottleneck\": \"Adapting CORDS/UDS codebases to VLA training pipelines requires significant engineering. LIBERO evaluation rollouts are CPU-bound. Phase 2 analysis requires human judgment for interpreting failure modes.\",\n      \"risk_note\": \"Cannot run real-robot experiments. Agent may misinterpret Phase 2 failure mode analysis without human guidance. Pure simulation scope limits venue acceptance at robotics-focused venues.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (deadline expected ~October 2026 — ideal fit: systematic empirical study + method contribution for training methodology, strong precedent for benchmarking papers with insights)\",\n    \"NeurIPS 2026 Datasets & Benchmarks Track (if the benchmarking contribution dominates and TADS improvements are modest, this track values systematic evaluation and reproducible comparisons)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"UDS: Utility-Diversity Aware Online Batch Selection for LLM Supervised Fine-tuning (ICML 2025, Zou et al.) — closest existing work; online utility+diversity selection for LLM SFT\",\n    \"GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning (AAAI 2021, Killamsetty et al.) — online submodular selection with convergence guarantees\",\n    \"Coresets for Data-efficient Training of Machine Learning Models / CRAIG (ICML 2020, Mirzasoleiman et al.) — facility-location online coreset selection\",\n    \"GRAD-MATCH: Gradient Matching based Data Subset Selection (ICML 2021, Killamsetty et al.) — gradient-matching extension of CRAIG\",\n    \"D2 Pruning: Message Passing for Balancing Diversity and Difficulty in Data Pruning (ICLR 2024, Maharana et al.) — graph-based diversity-difficulty balancing\",\n    \"Data Pruning by Information Maximization / InfoMax (ICLR 2025, Tan et al.) — DQP formulation balancing importance and redundancy\",\n    \"D3: Diversity, Difficulty, and Dependability-Aware Data Selection (IJCAI 2025) — three-criteria LLM instruction tuning selection\",\n    \"Robot Data Curation with Mutual Information Estimators / DemInf (RSS 2026, Hejna et al.) — MI-based demonstration quality for robotics\",\n    \"DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration (CoRL 2025, Guo et al.) — sub-trajectory frame selection\",\n    \"On Data Redundancy in VLA Training (ICRA 2026 workshop) — empirical evidence that diversity > difficulty for VLA\",\n    \"Submodular Batch Selection for Training Deep Neural Networks (IJCAI 2019)\",\n    \"Prioritized Experience Replay (ICLR 2016)\",\n    \"Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining (ICLR 2025)\",\n    \"Towards Balanced Behavior Cloning from Imbalanced Datasets (Autonomous Robots 2026)\",\n    \"OpenVLA: An Open-Source Vision-Language-Action Model (ICML 2025)\",\n    \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success / OpenVLA-OFT (RSS 2025)\",\n    \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (arXiv 2025)\",\n    \"SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026)\",\n    \"CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)\",\n    \"Curating Demonstrations using Online Experience / Demo-SCORE (RSS 2025)\",\n    \"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (2025)\",\n    \"Quality over Quantity: Demonstration Curation via Influence Functions / QoQ (arXiv 2026)\",\n    \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (RSS 2023, Chi et al.) — action multi-modality in BC\",\n    \"Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning (arXiv 2026)\",\n    \"CORDS: COResets and Data Subset selection toolkit (Killamsetty et al.)\",\n    \"DeepCore: A Comprehensive Library for Coreset Selection in Deep Learning (2022)\",\n    \"LiLAW: Lightweight Learnable Adaptive Weighting (2025)\",\n    \"FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models (2025)\",\n    \"ExpReS-VLA: Specializing VLAs Through Experience Replay and Retrieval (arXiv 2025)\",\n    \"RIPT-VLA / Interactive Post-Training for Vision-Language-Action Models (arXiv 2025)\",\n    \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026)\"\n  ],\n  \"description\": \"We present the first systematic evaluation of online data selection methods on Vision-Language-Action (VLA) behavioral cloning, addressing a critical gap: while methods like UDS (ICML 2025), GLISTER-Online (AAAI 2021), and CRAIG (ICML 2020) have proven effective for classification and LLM training, none have been tested on VLA BC, where trajectory temporal structure, action multi-modality, and multi-granularity diversity requirements create fundamentally different data characteristics. Our study proceeds in three phases. Phase 1 benchmarks UDS, GLISTER-Online, CRAIG, and GRAD-MATCH against static curation baselines (SCIZOR, DemInf, random subsampling) on LIBERO across 4 suites and 4 data fractions, providing the first head-to-head comparison. Phase 2 diagnoses VLA-specific failure modes through three testable hypotheses: (H1) loss-based utility is unreliable due to action multi-modality — high loss may indicate an alternative valid strategy rather than genuine difficulty; (H2) per-sample embedding diversity misses trajectory-level temporal redundancy — chunks from the same trajectory share informational content invisible to i.i.d. selection; (H3) single-scale diversity metrics collapse coverage along important axes (task type, action phase, scene configuration). Phase 3 introduces Trajectory-Aware Data Selection (TADS), with components targeting each diagnosed failure mode: trajectory-conditioned utility normalization, trajectory-identity-penalized redundancy scoring, and multi-granularity coverage constraints. Each TADS component is ablated independently and tested as augmentations of existing methods (UDS+TADS, GLISTER+TADS) to isolate VLA-specific from framework-specific effects. Unlike the original DADS proposal, which was an assembly of known components (PER + facility-location + annealing) incorrectly claimed as novel, this work makes its contribution through empirical understanding: revealing when and why general-purpose online selection fails for VLA BC, providing diagnostic tools for the failure modes, and demonstrating targeted VLA-specific fixes. The benchmarking contribution is independently valuable regardless of TADS improvement magnitude — if existing methods transfer well, that finding saves the community from re-inventing the wheel; if they fail, the failure mode analysis guides future method development. We target ICLR 2027, with sufficient time for thorough evaluation including potential extension to Open X-Embodiment for cross-embodiment validation.\",\n  \"project_name\": \"diversity_aware_sampling_vla\",\n  \"source\": \"web_research\"\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f14e489d-664e-4f55-823e-247f7f09251d",
  "isSidechain": false,
  "requestId": "req_011Cb1kZGjwEAW1d9b9REo1x",
  "type": "assistant",
  "uuid": "435429d2-184d-419d-813a-6949b882f47c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXxwowULxiuhshbnruJnpH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 56943,
      "output_tokens": 7261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 617,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7261,
          "cache_read_input_tokens": 56943,
          "cache_creation_input_tokens": 617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 617
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

_source line 94 · 2026-05-14T03:31:52.276Z_

<details><summary>↩ Tool result · reported error · `toolu_01JqXwCs47eLZrdBqjLoSz1z`</summary>

```text
Claude requested permissions to write to /tmp/revised_idea.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "435429d2-184d-419d-813a-6949b882f47c",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "1d8a57c2-9207-4a4b-bb69-c0028c952ae3",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revised_idea.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "435429d2-184d-419d-813a-6949b882f47c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 95_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Beyond Difficulty: Diversity-Aware Dynamic Sampling for Data-Efficient…",
  "leafUuid": "1d8a57c2-9207-4a4b-bb69-c0028c952ae3",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Runtime record

_source line 96_

```json
{
  "type": "ai-title",
  "aiTitle": "Benchmark diversity-aware selection methods on VLA BC",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Tool call

_source line 97 · 2026-05-14T03:34:26.556Z_

<details open><summary>🔧 Tool call — Write · `toolu_019oCth2u3wQCTn5xvxHp2zZ`</summary>

```json
{
  "file_path": "/tmp/revised_idea.json",
  "content": "{\n  \"change_type\": \"major\",\n  \"title\": \"Do Online Data Selection Methods Transfer to VLA Training? A Benchmarking Study with Trajectory-Aware Adaptations\",\n  \"core_problem\": \"VLA behavioral cloning datasets contain massive redundancy — workshop findings ('On Data Redundancy in VLA Training', ICRA 2026 workshop) suggest VLAs can train on as little as 5–30% of LIBERO data with minimal performance loss, and difficulty-based subsampling (TSS) actively hurts by sacrificing diversity. Meanwhile, the broader ML community has developed sophisticated online data selection methods that balance diversity and informativeness during training: UDS (ICML 2025) combines nuclear-norm utility with embedding-based inter-sample diversity for LLM SFT; GLISTER-Online (AAAI 2021) performs submodular selection with convergence guarantees; CRAIG (ICML 2020) uses facility-location coreset selection during SGD; D2 Pruning (ICLR 2024) balances diversity and difficulty via graph message passing; InfoMax (ICLR 2025) maximizes information content while minimizing redundancy. However, ALL of these methods were designed for and evaluated exclusively on classification or language tasks. UDS explicitly acknowledges that 'applying to non-LLM domains represents an important avenue for future work.' None handle the structural properties unique to VLA behavioral cloning: (1) temporal autocorrelation within demonstration trajectories, where consecutive action chunks share redundancy invisible to per-sample embedding distances; (2) action multi-modality, where multiple valid action sequences exist for the same observation, making loss an unreliable proxy for informativeness; and (3) heterogeneous, multi-granularity diversity requirements spanning task type, action phase, scene configuration, and embodiment. The critical open question is not whether to combine diversity with difficulty — that problem is well-studied — but whether existing solutions transfer to VLA BC, where these structural differences may cause systematic failures.\",\n  \"opportunity\": \"No existing work has systematically evaluated whether general-purpose online data selection methods (UDS, GLISTER-Online, CRAIG, GRAD-MATCH) transfer to VLA behavioral cloning. This creates a dual opportunity: (1) An empirical benchmarking contribution — the first head-to-head comparison of online selection methods on VLA BC, revealing which components of existing methods survive the domain transfer and which break. (2) A methodological contribution — VLA-specific adaptations that address the diagnosed failure modes. Three VLA-specific structural properties make this transfer non-trivial and potentially reveal new insights:\\n\\n- **Trajectory-level temporal redundancy**: In VLA datasets, action chunks from the same trajectory are informationally linked (reaching→grasping→placing follows a coherent strategy). Selecting one informative chunk from trajectory T should reduce the utility of nearby chunks in T — but per-sample embedding diversity (as in UDS, CRAIG) treats all chunks as i.i.d. and cannot capture this.\\n\\n- **Action multi-modality**: From the same observation state, multiple valid manipulation strategies exist (approach from left vs. right, different grasp points). High prediction loss may indicate the model hasn't learned a particular strategy — or that the demonstration took an uncommon-but-valid approach. UDS's nuclear-norm utility and GLISTER's loss-based selection both conflate genuine difficulty with action-distributional ambiguity. This is well-documented in the diffusion policy literature (Chi et al., RSS 2023) but has not been connected to data selection.\\n\\n- **Multi-granularity coverage**: VLA training requires coverage across tasks, action phases (reach/grasp/place/insert), scene configurations, and object sets simultaneously. A single embedding-space diversity measure (as in UDS's inter-sample distance or CRAIG's facility-location) may optimize one axis while neglecting others.\\n\\nThese failure modes are testable hypotheses, not assumptions. If existing methods transfer well, the benchmarking study itself is the contribution. If they fail, the failure mode analysis and VLA-adapted solutions become the contribution. Either outcome advances the field.\",\n  \"landscape\": \"**Online diversity-aware data selection for training (the methods we benchmark):**\\n\\n- UDS (ICML 2025, Zou et al.) performs online batch selection during LLM SFT using s_total = s_intra + α·s_inter, where s_intra is the nuclear norm of the logits matrix (capturing both utility and intra-sample diversity) and s_inter is the average L2 distance to a FIFO memory buffer of compressed logits embeddings. α is dataset/model-dependent and fixed per run. Tested on MMLU, ScienceQA, GSM8K, HumanEval with Llama-3.1-8B and Qwen-2.5-7B. Explicitly notes non-LLM domains as future work. Does not handle temporal correlations or multi-modal outputs.\\n\\n- GLISTER-Online (AAAI 2021, Killamsetty et al.) formulates online data selection as bi-level optimization: select a subset maximizing validation log-likelihood while training on it. The inner selection is (weakly) submodular, enabling greedy approximation with convergence guarantees. Tested on image classification (CIFAR-10/100, MNIST) and NLP classification. Requires a held-out validation set, which is non-trivial for multi-task VLA (validation must cover all tasks proportionally).\\n\\n- CRAIG (ICML 2020, Mirzasoleiman et al.) selects weighted coresets whose gradients approximate the full-dataset gradient via facility-location maximization. Proven convergence to (near-)optimal for convex objectives. Tested on logistic regression and image classification. Assumes i.i.d. data; gradient-matching may be ill-conditioned for high-dimensional multi-modal VLA outputs.\\n\\n- GRAD-MATCH (ICML 2021, Killamsetty et al.) extends CRAIG with orthogonal matching pursuit for tighter gradient approximation. Available in the CORDS toolkit alongside GLISTER and CRAIG.\\n\\n**Static/pre-training diversity-difficulty balancing (related but not online):**\\n\\n- D2 Pruning (ICLR 2024, Maharana et al.) represents the dataset as a graph and uses message passing to select subsets balancing diversity (edges) and difficulty (node scores). Effective at low-to-medium pruning rates for image classification and NLP. Static pre-training method — cannot adapt during training.\\n\\n- InfoMax (ICLR 2025, Tan et al.) formulates coreset selection as discrete quadratic programming maximizing information content minus pairwise redundancy. Scales to millions of samples via gradient-based solver with sparsification. Applied to image classification, VL pre-training, and LLM instruction tuning. Static selection.\\n\\n- D3 (IJCAI 2025) combines diversity, difficulty, and dependability for LLM instruction tuning via a weighted coreset objective. Iterative but not truly online (rounds of score-then-select).\\n\\n**Robotics demonstration curation (domain-specific but static/offline):**\\n\\n- SCIZOR (ICRA 2026) uses self-supervised progress prediction and embedding clustering for one-time pre-training curation of robot demonstrations, achieving ~15% improvement.\\n\\n- CUPID (CoRL 2025) estimates each demonstration's causal impact via influence functions at a fixed policy checkpoint. One-pass, not adaptive.\\n\\n- Demo-SCORE (RSS 2025) performs iterative curation via train→rollout→classify→re-filter, genuinely adapting to model competence — but requires environment rollouts.\\n\\n- DemInf (RSS 2026, Hejna et al.) introduces Demonstration Information Estimation using k-nearest-neighbor mutual information estimates over VAE embeddings of states and actions. Unsupervised, embedding-based quality assessment achieving 5-10% improvement on RoboMimic and real-robot tasks. Static curation; does not adapt during training.\\n\\n- DataMIL (2025) uses datamodels for end-to-end policy-driven selection. Pre-training.\\n\\n- QoQ (2026) uses influence functions with trajectory-wise aggregation.\\n\\n**Sub-trajectory and frame-level selection:**\\n\\n- DemoSpeedup (CoRL 2025, Guo et al.) performs entropy-guided frame-level downsampling within demonstrations, accelerating policy execution 1.7-3× while maintaining success rates. Operates at sub-trajectory granularity similar to our action-chunk level, but targets execution speed rather than training efficiency.\\n\\n- 'On Data Redundancy in VLA Training' (ICRA 2026 workshop) evaluates random vs. TSS difficulty-based frame selection on LIBERO, finding random subsampling (preserving diversity) consistently outperforms difficulty-based selection. A workshop paper whose specific quantitative claims (95% redundancy, TSS underperformance) should be verified, but the qualitative finding that diversity matters more than difficulty aligns with broader observations.\\n\\n**Balanced BC and reweighting:**\\n\\n- 'Towards Balanced Behavior Cloning' (Autonomous Robots 2026) addresses subtask imbalance via meta-gradient rebalancing — orthogonal to within-subtask redundancy.\\n\\n- Dynamic Loss-Based Sample Reweighting (ICLR 2025) performs token-level reweighting for LLM pretraining with convergence guarantees. No diversity preservation.\\n\\n- Freshness-Aware PER (April 2026) addresses priority staleness in RL post-training.\\n\\n**The gap we address**: Existing online data selection methods (UDS, GLISTER, CRAIG, GRAD-MATCH) have never been evaluated on VLA behavioral cloning. Whether their assumptions (i.i.d. samples, loss-as-utility, single-space embedding diversity) hold in the VLA BC setting — with trajectory temporal structure, action multi-modality, and multi-granularity coverage needs — is an open empirical question with practical implications for the growing scale of robot demonstration datasets.\",\n  \"approach\": \"We propose a three-phase study that first benchmarks existing online data selection methods on VLA BC, then diagnoses failure modes, and finally introduces trajectory-aware adaptations. This structure ensures contributions regardless of whether existing methods transfer well or poorly.\\n\\n**Phase 1: Benchmarking Online Data Selection for VLA BC**\\n\\nWe systematically evaluate existing methods on LIBERO (Spatial, Object, Goal, Long) with SmolVLA and OpenVLA-OFT:\\n\\n- Online methods (our main focus): UDS (adapted from text logits to action-chunk predictions), GLISTER-Online, CRAIG, GRAD-MATCH\\n- Static curation baselines: SCIZOR, DemInf, random subsampling, TSS difficulty-based\\n- Simple dynamic baselines: loss-proportional PER, Dynamic Loss-Based Reweighting (adapted to action chunks)\\n- Reference: full-dataset training, uniform sampling\\n\\nAll methods evaluated at 10%, 25%, 50%, and 100% effective data utilization (for online methods, this means the fraction of each epoch's data used per gradient step). We report per-suite success rates (not just averages, following best practices from LIBERO-Plus) across 3 seeds.\\n\\nAdapting existing methods to VLA requires non-trivial engineering choices that we document carefully: UDS's nuclear-norm utility must be replaced (VLA action heads produce continuous vectors, not logit matrices); GLISTER requires a VLA-appropriate validation set covering all tasks; CRAIG's gradient computation scales with VLA's multi-modal parameter count. These adaptations are themselves informative about domain transfer.\\n\\n**Phase 2: Failure Mode Diagnosis**\\n\\nFor each method, we analyze:\\n\\n(H1) **Loss-utility conflation**: We measure the correlation between per-chunk loss and downstream contribution to policy performance (estimated via leave-one-out or influence-function approximation). In VLA BC, we hypothesize this correlation is weaker than in LLM SFT due to action multi-modality — high-loss chunks may represent valid alternative strategies, not genuine difficulty. We test this by examining whether high-loss chunks cluster around action-multimodal states (states where the dataset contains diverse actions).\\n\\n(H2) **Trajectory-blind redundancy**: We measure whether methods select chunks uniformly across trajectories or cluster selections within a few trajectories. Embedding-based diversity (UDS, CRAIG) may select diverse-looking chunks from the same trajectory (different visual frames as the robot moves) while missing coverage of other trajectories with different strategies.\\n\\n(H3) **Single-scale diversity collapse**: We measure coverage across multiple axes — task identity, action phase (reaching vs. grasping vs. placing, identified via action-velocity thresholds), and scene configuration — for each method's selected subsets. A method that maximizes embedding diversity may achieve good scene coverage but poor action-phase coverage, or vice versa.\\n\\nVisualization: For each method, we produce selection heatmaps showing which chunks are selected across trajectories, tasks, and training epochs, enabling qualitative assessment of selection patterns.\\n\\n**Phase 3: Trajectory-Aware Adaptations (TADS)**\\n\\nBased on Phase 2 findings, we introduce Trajectory-Aware Data Selection (TADS), with each component addressing a diagnosed failure mode:\\n\\n1. **Trajectory-Conditioned Utility (addresses H1)**: Instead of raw per-chunk loss L_i, we compute utility as u_i = L_i / L_bar(traj(i), phase(i)), normalizing by the average loss of chunks at the same action phase within similar trajectories. This distinguishes 'genuinely difficult manipulation' from 'uncommon-but-valid strategy' — a chunk with high absolute loss but average loss-for-its-trajectory-type gets moderate (not high) utility. For VLA architectures using diffusion action heads, we additionally use the variance across denoising samples as a complementary utility signal, as high variance directly indicates action multi-modality.\\n\\n2. **Trajectory-Aware Redundancy (addresses H2)**: We augment per-chunk embedding similarity with a trajectory-identity penalty: red_i = (1/K) Σ_{j ∈ KNN(i)} sim(e_i, e_j) · (1 + γ · 1[traj(i) = traj(j)]), where γ > 0 penalizes within-trajectory neighbors more heavily. This ensures that selecting one informative chunk from a trajectory appropriately reduces the priority of nearby chunks in the same trajectory, even if their embeddings differ due to robot motion.\\n\\n3. **Multi-Granularity Coverage (addresses H3)**: Instead of a single facility-location objective, we decompose batch-level diversity into: FL_task (coverage across task identities) + FL_phase (coverage across action phases) + FL_scene (coverage across scene embeddings), with relative weights {w_task, w_phase, w_scene} tuned on a held-out validation split. For the task and phase axes, this reduces to stratified sampling constraints; for the scene axis, it uses facility-location over observation embeddings.\\n\\nEach TADS component is ablated independently to quantify its marginal contribution. We also test TADS as an augmentation of UDS and GLISTER-Online (replacing their diversity/utility components with our trajectory-aware versions) to isolate VLA-specific vs. framework-specific effects.\\n\\n**Implementation**: All methods implemented within a unified evaluation framework compatible with SmolVLA and OpenVLA-OFT training pipelines. Online selection methods implemented as drop-in DistributedSampler replacements. GLISTER-Online and CRAIG adapted from the CORDS toolkit. UDS re-implemented from the official codebase. Embeddings computed from VLA's frozen vision-language encoder. KNN precomputed; only loss-based scores refreshed online.\\n\\n**Evaluation**: LIBERO (all 4 suites) as primary benchmark, directly comparable to 'On Data Redundancy' results. Per-suite success rates reported separately (following LIBERO-Plus recommendations). SimplerEnv for breadth. Metrics: (1) success rate at each data fraction, (2) data efficiency curves showing sample-efficiency gains, (3) training wall-clock time to reach target success rate, (4) selection overhead as fraction of training time. Statistical significance via 3 seeds with bootstrap confidence intervals.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~1200h A100 80GB (Phase 1: ~600h for 10 methods × 4 suites × 4 fractions × 3 seeds = 480 runs × ~1.2h avg; Phase 2: ~100h analysis; Phase 3: ~500h for TADS + ablations)\",\n      \"gpu_utilization\": \"Low (~25%). Significant implementation effort for adapting UDS/GLISTER/CRAIG to VLA pipelines; building unified evaluation framework; failure mode analysis tooling.\",\n      \"timeline\": \"4-5 months\",\n      \"team\": \"2-3 researchers (one for adapting/implementing online selection methods from CORDS/UDS, one for VLA training infrastructure and LIBERO evaluation, one for failure mode analysis and visualization)\",\n      \"estimated_gpu_cost\": \"$1,800 (1200h × ~$1.50/h spot A100 80GB)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~1400h A100 80GB\",\n      \"gpu_utilization\": \"Moderate (~55%). Agent handles experiment orchestration and config generation; human reviews failure mode visualizations and guides Phase 3 design based on Phase 2 findings.\",\n      \"timeline\": \"6-8 weeks\",\n      \"team\": \"1-2 researchers, ~1hr/day reviewing Phase 2 diagnostics and steering ablation priorities\",\n      \"claude_api_cost\": \"$300-500 (~400 conversation turns for method adaptation, experiment management, analysis)\",\n      \"estimated_gpu_cost\": \"$2,100 (1400h × ~$1.50/h spot A100 80GB)\",\n      \"risk_note\": \"Simulation-only (LIBERO + SimplerEnv). If existing methods transfer well to VLA BC, the contribution narrows to a useful benchmarking paper with smaller TADS improvements. This is still publishable but less impactful — consider adding Open X-Embodiment experiments for broader validation.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~2800h A100 80GB (full benchmarking grid + failure mode sweeps + TADS ablations across all configurations)\",\n      \"gpu_utilization\": \"~85%. Agent pipelines Phase 1→2→3 sequentially with parallel runs within each phase.\",\n      \"timeline\": \"12-18 days with 8 A100 GPUs in parallel\",\n      \"team\": \"0 (initial setup + final review only)\",\n      \"claude_api_cost\": \"$600-900 (~800 turns for end-to-end implementation, adaptation of multiple codebases, experiment orchestration, failure diagnosis, and paper drafting)\",\n      \"estimated_gpu_cost\": \"$4,200 (2800h × ~$1.50/h spot A100 80GB)\",\n      \"speed_bottleneck\": \"Adapting CORDS/UDS codebases to VLA training pipelines requires significant engineering. LIBERO evaluation rollouts are CPU-bound. Phase 2 analysis requires human judgment for interpreting failure modes.\",\n      \"risk_note\": \"Cannot run real-robot experiments. Agent may misinterpret Phase 2 failure mode analysis without human guidance. Pure simulation scope limits venue acceptance at robotics-focused venues.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (deadline expected ~October 2026 — ideal fit: systematic empirical study + method contribution for training methodology, strong precedent for benchmarking papers with insights)\",\n    \"NeurIPS 2026 Datasets & Benchmarks Track (if the benchmarking contribution dominates and TADS improvements are modest, this track values systematic evaluation and reproducible comparisons)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"UDS: Utility-Diversity Aware Online Batch Selection for LLM Supervised Fine-tuning (ICML 2025, Zou et al.) — closest existing work; online utility+diversity selection for LLM SFT\",\n    \"GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning (AAAI 2021, Killamsetty et al.) — online submodular selection with convergence guarantees\",\n    \"Coresets for Data-efficient Training of Machine Learning Models / CRAIG (ICML 2020, Mirzasoleiman et al.) — facility-location online coreset selection\",\n    \"GRAD-MATCH: Gradient Matching based Data Subset Selection (ICML 2021, Killamsetty et al.) — gradient-matching extension of CRAIG\",\n    \"D2 Pruning: Message Passing for Balancing Diversity and Difficulty in Data Pruning (ICLR 2024, Maharana et al.) — graph-based diversity-difficulty balancing\",\n    \"Data Pruning by Information Maximization / InfoMax (ICLR 2025, Tan et al.) — DQP formulation balancing importance and redundancy\",\n    \"D3: Diversity, Difficulty, and Dependability-Aware Data Selection (IJCAI 2025) — three-criteria LLM instruction tuning selection\",\n    \"Robot Data Curation with Mutual Information Estimators / DemInf (RSS 2026, Hejna et al.) — MI-based demonstration quality for robotics\",\n    \"DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration (CoRL 2025, Guo et al.) — sub-trajectory frame selection\",\n    \"On Data Redundancy in VLA Training (ICRA 2026 workshop) — empirical evidence that diversity > difficulty for VLA\",\n    \"Submodular Batch Selection for Training Deep Neural Networks (IJCAI 2019)\",\n    \"Prioritized Experience Replay (ICLR 2016)\",\n    \"Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining (ICLR 2025)\",\n    \"Towards Balanced Behavior Cloning from Imbalanced Datasets (Autonomous Robots 2026)\",\n    \"OpenVLA: An Open-Source Vision-Language-Action Model (ICML 2025)\",\n    \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success / OpenVLA-OFT (RSS 2025)\",\n    \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (arXiv 2025)\",\n    \"SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026)\",\n    \"CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)\",\n    \"Curating Demonstrations using Online Experience / Demo-SCORE (RSS 2025)\",\n    \"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (2025)\",\n    \"Quality over Quantity: Demonstration Curation via Influence Functions / QoQ (arXiv 2026)\",\n    \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (RSS 2023, Chi et al.) — action multi-modality in BC\",\n    \"Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning (arXiv 2026)\",\n    \"CORDS: COResets and Data Subset selection toolkit (Killamsetty et al.)\",\n    \"DeepCore: A Comprehensive Library for Coreset Selection in Deep Learning (2022)\",\n    \"LiLAW: Lightweight Learnable Adaptive Weighting (2025)\",\n    \"FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models (2025)\",\n    \"ExpReS-VLA: Specializing VLAs Through Experience Replay and Retrieval (arXiv 2025)\",\n    \"RIPT-VLA / Interactive Post-Training for Vision-Language-Action Models (arXiv 2025)\",\n    \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026)\"\n  ],\n  \"description\": \"We present the first systematic evaluation of online data selection methods on Vision-Language-Action (VLA) behavioral cloning, addressing a critical gap: while methods like UDS (ICML 2025), GLISTER-Online (AAAI 2021), and CRAIG (ICML 2020) have proven effective for classification and LLM training, none have been tested on VLA BC, where trajectory temporal structure, action multi-modality, and multi-granularity diversity requirements create fundamentally different data characteristics. Our study proceeds in three phases. Phase 1 benchmarks UDS, GLISTER-Online, CRAIG, and GRAD-MATCH against static curation baselines (SCIZOR, DemInf, random subsampling) on LIBERO across 4 suites and 4 data fractions, providing the first head-to-head comparison. Phase 2 diagnoses VLA-specific failure modes through three testable hypotheses: (H1) loss-based utility is unreliable due to action multi-modality — high loss may indicate an alternative valid strategy rather than genuine difficulty; (H2) per-sample embedding diversity misses trajectory-level temporal redundancy — chunks from the same trajectory share informational content invisible to i.i.d. selection; (H3) single-scale diversity metrics collapse coverage along important axes (task type, action phase, scene configuration). Phase 3 introduces Trajectory-Aware Data Selection (TADS), with components targeting each diagnosed failure mode: trajectory-conditioned utility normalization, trajectory-identity-penalized redundancy scoring, and multi-granularity coverage constraints. Each TADS component is ablated independently and tested as augmentations of existing methods (UDS+TADS, GLISTER+TADS) to isolate VLA-specific from framework-specific effects. Unlike the original DADS proposal, which was an assembly of known components (PER + facility-location + annealing) incorrectly claimed as novel, this work makes its contribution through empirical understanding: revealing when and why general-purpose online selection fails for VLA BC, providing diagnostic tools for the failure modes, and demonstrating targeted VLA-specific fixes. The benchmarking contribution is independently valuable regardless of TADS improvement magnitude — if existing methods transfer well, that finding saves the community from re-inventing the wheel; if they fail, the failure mode analysis guides future method development. We target ICLR 2027, with sufficient time for thorough evaluation including potential extension to Open X-Embodiment for cross-embodiment validation.\",\n  \"project_name\": \"diversity_aware_sampling_vla\",\n  \"source\": \"web_research\"\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d8a57c2-9207-4a4b-bb69-c0028c952ae3",
  "isSidechain": false,
  "requestId": "req_011Cb1ko1zK7v6vyYSrVd9GK",
  "type": "assistant",
  "uuid": "b966552c-2556-4a4d-8a3e-6e2d17f5fe7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BdqMxQZh7QHsZRvfkynmx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7301,
      "cache_read_input_tokens": 57560,
      "output_tokens": 6553,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7301,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6553,
          "cache_read_input_tokens": 57560,
          "cache_creation_input_tokens": 7301,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7301
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

_source line 98 · 2026-05-14T03:34:26.562Z_

<details><summary>↩ Tool result · reported error · `toolu_019oCth2u3wQCTn5xvxHp2zZ`</summary>

```text
Claude requested permissions to write to /tmp/revised_idea.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b966552c-2556-4a4d-8a3e-6e2d17f5fe7c",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "6b2f21e7-ceea-4d36-82a7-a299c70f68ab",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revised_idea.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "b966552c-2556-4a4d-8a3e-6e2d17f5fe7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-14T03:34:29.668Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Lp23bPLk9E4Y9Xgxpej9ep`</summary>

```json
{
  "command": "echo \"ready\"",
  "description": "Test bash access"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b2f21e7-ceea-4d36-82a7-a299c70f68ab",
  "isSidechain": false,
  "requestId": "req_011Cb1kzPg6XhRmDK4NWbqnJ",
  "type": "assistant",
  "uuid": "1c60b609-a664-4089-a48f-158a44e4539a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWwXEhPh6DF6aXzCVLSF15",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6595,
      "cache_read_input_tokens": 64861,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6595,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 64861,
          "cache_creation_input_tokens": 6595,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6595
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

_source line 100 · 2026-05-14T03:34:29.864Z_

<details><summary>↩ Tool result · `toolu_01Lp23bPLk9E4Y9Xgxpej9ep`</summary>

```text
ready
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c60b609-a664-4089-a48f-158a44e4539a",
  "isSidechain": false,
  "promptId": "ac994758-2788-4ad5-99bf-093854674e6d",
  "type": "user",
  "uuid": "84721039-d98b-4223-a0e0-fe2be751872b",
  "toolUseResult": {
    "stdout": "ready",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1c60b609-a664-4089-a48f-158a44e4539a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 101 · 2026-05-14T03:37:22.652Z_

Here is the complete revised idea as a JSON object. This is a **major revision** — the entire framing, gap claim, landscape, and approach structure have been substantially redesigned based on deep research into all reviewer-cited papers.

```json
{
  "change_type": "major",
  "title": "Do Online Data Selection Methods Transfer to VLA Training? A Benchmarking Study with Trajectory-Aware Adaptations",
  "core_problem": "VLA behavioral cloning datasets contain massive redundancy — workshop findings ('On Data Redundancy in VLA Training', ICRA 2026 workshop) suggest VLAs can train on as little as 5–30% of LIBERO data with minimal performance loss, and difficulty-based subsampling (TSS) actively hurts by sacrificing diversity. Meanwhile, the broader ML community has developed sophisticated online data selection methods that balance diversity and informativeness during training: UDS (ICML 2025) combines nuclear-norm utility with embedding-based inter-sample diversity for LLM SFT; GLISTER-Online (AAAI 2021) performs submodular selection with convergence guarantees; CRAIG (ICML 2020) uses facility-location coreset selection during SGD; D2 Pruning (ICLR 2024) balances diversity and difficulty via graph message passing; InfoMax (ICLR 2025) maximizes information content while minimizing redundancy. However, ALL of these methods were designed for and evaluated exclusively on classification or language tasks. UDS explicitly acknowledges that 'applying to non-LLM domains represents an important avenue for future work.' None handle the structural properties unique to VLA behavioral cloning: (1) temporal autocorrelation within demonstration trajectories, where consecutive action chunks share redundancy invisible to per-sample embedding distances; (2) action multi-modality, where multiple valid action sequences exist for the same observation, making loss an unreliable proxy for informativeness; and (3) heterogeneous, multi-granularity diversity requirements spanning task type, action phase, scene configuration, and embodiment. The critical open question is not whether to combine diversity with difficulty — that problem is well-studied — but whether existing solutions transfer to VLA BC, where these structural differences may cause systematic failures.",
  "opportunity": "No existing work has systematically evaluated whether general-purpose online data selection methods (UDS, GLISTER-Online, CRAIG, GRAD-MATCH) transfer to VLA behavioral cloning. This creates a dual opportunity: (1) An empirical benchmarking contribution — the first head-to-head comparison of online selection methods on VLA BC, revealing which components of existing methods survive the domain transfer and which break. (2) A methodological contribution — VLA-specific adaptations that address the diagnosed failure modes. Three VLA-specific structural properties make this transfer non-trivial and potentially reveal new insights:\n\n- **Trajectory-level temporal redundancy**: In VLA datasets, action chunks from the same trajectory are informationally linked (reaching→grasping→placing follows a coherent strategy). Selecting one informative chunk from trajectory T should reduce the utility of nearby chunks in T — but per-sample embedding diversity (as in UDS, CRAIG) treats all chunks as i.i.d. and cannot capture this.\n\n- **Action multi-modality**: From the same observation state, multiple valid manipulation strategies exist (approach from left vs. right, different grasp points). High prediction loss may indicate the model hasn't learned a particular strategy — or that the demonstration took an uncommon-but-valid approach. UDS's nuclear-norm utility and GLISTER's loss-based selection both conflate genuine difficulty with action-distributional ambiguity. This is well-documented in the diffusion policy literature (Chi et al., RSS 2023) but has not been connected to data selection.\n\n- **Multi-granularity coverage**: VLA training requires coverage across tasks, action phases (reach/grasp/place/insert), scene configurations, and object sets simultaneously. A single embedding-space diversity measure (as in UDS's inter-sample distance or CRAIG's facility-location) may optimize one axis while neglecting others.\n\nThese failure modes are testable hypotheses, not assumptions. If existing methods transfer well, the benchmarking study itself is the contribution. If they fail, the failure mode analysis and VLA-adapted solutions become the contribution. Either outcome advances the field.",
  "landscape": "**Online diversity-aware data selection for training (the methods we benchmark):**\n\n- UDS (ICML 2025, Zou et al.) performs online batch selection during LLM SFT using s_total = s_intra + α·s_inter, where s_intra is the nuclear norm of the logits matrix (capturing both utility and intra-sample diversity) and s_inter is the average L2 distance to a FIFO memory buffer of compressed logits embeddings. α is dataset/model-dependent and fixed per run. Tested on MMLU, ScienceQA, GSM8K, HumanEval with Llama-3.1-8B and Qwen-2.5-7B. Explicitly notes non-LLM domains as future work. Does not handle temporal correlations or multi-modal outputs.\n\n- GLISTER-Online (AAAI 2021, Killamsetty et al.) formulates online data selection as bi-level optimization: select a subset maximizing validation log-likelihood while training on it. The inner selection is (weakly) submodular, enabling greedy approximation with convergence guarantees. Tested on image classification (CIFAR-10/100, MNIST) and NLP classification. Requires a held-out validation set, which is non-trivial for multi-task VLA (validation must cover all tasks proportionally).\n\n- CRAIG (ICML 2020, Mirzasoleiman et al.) selects weighted coresets whose gradients approximate the full-dataset gradient via facility-location maximization. Proven convergence to (near-)optimal for convex objectives. Tested on logistic regression and image classification. Assumes i.i.d. data; gradient-matching may be ill-conditioned for high-dimensional multi-modal VLA outputs.\n\n- GRAD-MATCH (ICML 2021, Killamsetty et al.) extends CRAIG with orthogonal matching pursuit for tighter gradient approximation. Available in the CORDS toolkit alongside GLISTER and CRAIG.\n\n**Static/pre-training diversity-difficulty balancing (related but not online):**\n\n- D2 Pruning (ICLR 2024, Maharana et al.) represents the dataset as a graph and uses message passing to select subsets balancing diversity (edges) and difficulty (node scores). Effective at low-to-medium pruning rates for image classification and NLP. Static pre-training method — cannot adapt during training.\n\n- InfoMax (ICLR 2025, Tan et al.) formulates coreset selection as discrete quadratic programming maximizing information content minus pairwise redundancy. Scales to millions of samples via gradient-based solver with sparsification. Applied to image classification, VL pre-training, and LLM instruction tuning. Static selection.\n\n- D3 (IJCAI 2025) combines diversity, difficulty, and dependability for LLM instruction tuning via a weighted coreset objective. Iterative but not truly online (rounds of score-then-select).\n\n**Robotics demonstration curation (domain-specific but static/offline):**\n\n- SCIZOR (ICRA 2026) uses self-supervised progress prediction and embedding clustering for one-time pre-training curation of robot demonstrations, achieving ~15% improvement.\n\n- CUPID (CoRL 2025) estimates each demonstration's causal impact via influence functions at a fixed policy checkpoint. One-pass, not adaptive.\n\n- Demo-SCORE (RSS 2025) performs iterative curation via train→rollout→classify→re-filter, genuinely adapting to model competence — but requires environment rollouts.\n\n- DemInf (RSS 2026, Hejna et al.) introduces Demonstration Information Estimation using k-nearest-neighbor mutual information estimates over VAE embeddings of states and actions. Unsupervised, embedding-based quality assessment achieving 5-10% improvement on RoboMimic and real-robot tasks. Static curation; does not adapt during training.\n\n- DataMIL (2025) uses datamodels for end-to-end policy-driven selection. Pre-training.\n\n- QoQ (2026) uses influence functions with trajectory-wise aggregation.\n\n**Sub-trajectory and frame-level selection:**\n\n- DemoSpeedup (CoRL 2025, Guo et al.) performs entropy-guided frame-level downsampling within demonstrations, accelerating policy execution 1.7-3× while maintaining success rates. Operates at sub-trajectory granularity similar to our action-chunk level, but targets execution speed rather than training efficiency.\n\n- 'On Data Redundancy in VLA Training' (ICRA 2026 workshop) evaluates random vs. TSS difficulty-based frame selection on LIBERO, finding random subsampling (preserving diversity) consistently outperforms difficulty-based selection. A workshop paper whose specific quantitative claims (95% redundancy, TSS underperformance) should be verified, but the qualitative finding that diversity matters more than difficulty aligns with broader observations.\n\n**Balanced BC and reweighting:**\n\n- 'Towards Balanced Behavior Cloning' (Autonomous Robots 2026) addresses subtask imbalance via meta-gradient rebalancing — orthogonal to within-subtask redundancy.\n\n- Dynamic Loss-Based Sample Reweighting (ICLR 2025) performs token-level reweighting for LLM pretraining with convergence guarantees. No diversity preservation.\n\n- Freshness-Aware PER (April 2026) addresses priority staleness in RL post-training.\n\n**The gap we address**: Existing online data selection methods (UDS, GLISTER, CRAIG, GRAD-MATCH) have never been evaluated on VLA behavioral cloning. Whether their assumptions (i.i.d. samples, loss-as-utility, single-space embedding diversity) hold in the VLA BC setting — with trajectory temporal structure, action multi-modality, and multi-granularity coverage needs — is an open empirical question with practical implications for the growing scale of robot demonstration datasets.",
  "approach": "We propose a three-phase study that first benchmarks existing online data selection methods on VLA BC, then diagnoses failure modes, and finally introduces trajectory-aware adaptations. This structure ensures contributions regardless of whether existing methods transfer well or poorly.\n\n**Phase 1: Benchmarking Online Data Selection for VLA BC**\n\nWe systematically evaluate existing methods on LIBERO (Spatial, Object, Goal, Long) with SmolVLA and OpenVLA-OFT:\n\n- Online methods (our main focus): UDS (adapted from text logits to action-chunk predictions), GLISTER-Online, CRAIG, GRAD-MATCH\n- Static curation baselines: SCIZOR, DemInf, random subsampling, TSS difficulty-based\n- Simple dynamic baselines: loss-proportional PER, Dynamic Loss-Based Reweighting (adapted to action chunks)\n- Reference: full-dataset training, uniform sampling\n\nAll methods evaluated at 10%, 25%, 50%, and 100% effective data utilization (for online methods, this means the fraction of each epoch's data used per gradient step). We report per-suite success rates (not just averages, following best practices from LIBERO-Plus) across 3 seeds.\n\nAdapting existing methods to VLA requires non-trivial engineering choices that we document carefully: UDS's nuclear-norm utility must be replaced (VLA action heads produce continuous vectors, not logit matrices); GLISTER requires a VLA-appropriate validation set covering all tasks; CRAIG's gradient computation scales with VLA's multi-modal parameter count. These adaptations are themselves informative about domain transfer.\n\n**Phase 2: Failure Mode Diagnosis**\n\nFor each method, we analyze:\n\n(H1) **Loss-utility conflation**: We measure the correlation between per-chunk loss and downstream contribution to policy performance (estimated via leave-one-out or influence-function approximation). In VLA BC, we hypothesize this correlation is weaker than in LLM SFT due to action multi-modality — high-loss chunks may represent valid alternative strategies, not genuine difficulty. We test this by examining whether high-loss chunks cluster around action-multimodal states (states where the dataset contains diverse actions).\n\n(H2) **Trajectory-blind redundancy**: We measure whether methods select chunks uniformly across trajectories or cluster selections within a few trajectories. Embedding-based diversity (UDS, CRAIG) may select diverse-looking chunks from the same trajectory (different visual frames as the robot moves) while missing coverage of other trajectories with different strategies.\n\n(H3) **Single-scale diversity collapse**: We measure coverage across multiple axes — task identity, action phase (reaching vs. grasping vs. placing, identified via action-velocity thresholds), and scene configuration — for each method's selected subsets. A method that maximizes embedding diversity may achieve good scene coverage but poor action-phase coverage, or vice versa.\n\nVisualization: For each method, we produce selection heatmaps showing which chunks are selected across trajectories, tasks, and training epochs, enabling qualitative assessment of selection patterns.\n\n**Phase 3: Trajectory-Aware Adaptations (TADS)**\n\nBased on Phase 2 findings, we introduce Trajectory-Aware Data Selection (TADS), with each component addressing a diagnosed failure mode:\n\n1. **Trajectory-Conditioned Utility (addresses H1)**: Instead of raw per-chunk loss L_i, we compute utility as u_i = L_i / L_bar(traj(i), phase(i)), normalizing by the average loss of chunks at the same action phase within similar trajectories. This distinguishes 'genuinely difficult manipulation' from 'uncommon-but-valid strategy' — a chunk with high absolute loss but average loss-for-its-trajectory-type gets moderate (not high) utility. For VLA architectures using diffusion action heads, we additionally use the variance across denoising samples as a complementary utility signal, as high variance directly indicates action multi-modality.\n\n2. **Trajectory-Aware Redundancy (addresses H2)**: We augment per-chunk embedding similarity with a trajectory-identity penalty: red_i = (1/K) Σ_{j ∈ KNN(i)} sim(e_i, e_j) · (1 + γ · 1[traj(i) = traj(j)]), where γ > 0 penalizes within-trajectory neighbors more heavily. This ensures that selecting one informative chunk from a trajectory appropriately reduces the priority of nearby chunks in the same trajectory, even if their embeddings differ due to robot motion.\n\n3. **Multi-Granularity Coverage (addresses H3)**: Instead of a single facility-location objective, we decompose batch-level diversity into: FL_task (coverage across task identities) + FL_phase (coverage across action phases) + FL_scene (coverage across scene embeddings), with relative weights {w_task, w_phase, w_scene} tuned on a held-out validation split. For the task and phase axes, this reduces to stratified sampling constraints; for the scene axis, it uses facility-location over observation embeddings.\n\nEach TADS component is ablated independently to quantify its marginal contribution. We also test TADS as an augmentation of UDS and GLISTER-Online (replacing their diversity/utility components with our trajectory-aware versions) to isolate VLA-specific vs. framework-specific effects.\n\n**Implementation**: All methods implemented within a unified evaluation framework compatible with SmolVLA and OpenVLA-OFT training pipelines. Online selection methods implemented as drop-in DistributedSampler replacements. GLISTER-Online and CRAIG adapted from the CORDS toolkit. UDS re-implemented from the official codebase. Embeddings computed from VLA's frozen vision-language encoder. KNN precomputed; only loss-based scores refreshed online.\n\n**Evaluation**: LIBERO (all 4 suites) as primary benchmark, directly comparable to 'On Data Redundancy' results. Per-suite success rates reported separately (following LIBERO-Plus recommendations). SimplerEnv for breadth. Metrics: (1) success rate at each data fraction, (2) data efficiency curves showing sample-efficiency gains, (3) training wall-clock time to reach target success rate, (4) selection overhead as fraction of training time. Statistical significance via 3 seeds with bootstrap confidence intervals.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~1200h A100 80GB (Phase 1: ~600h for 10 methods × 4 suites × 4 fractions × 3 seeds = 480 runs × ~1.2h avg; Phase 2: ~100h analysis; Phase 3: ~500h for TADS + ablations)",
      "gpu_utilization": "Low (~25%). Significant implementation effort for adapting UDS/GLISTER/CRAIG to VLA pipelines; building unified evaluation framework; failure mode analysis tooling.",
      "timeline": "4-5 months",
      "team": "2-3 researchers (one for adapting/implementing online selection methods from CORDS/UDS, one for VLA training infrastructure and LIBERO evaluation, one for failure mode analysis and visualization)",
      "estimated_gpu_cost": "$1,800 (1200h × ~$1.50/h spot A100 80GB)"
    },
    "human_in_loop": {
      "gpu_hours": "~1400h A100 80GB",
      "gpu_utilization": "Moderate (~55%). Agent handles experiment orchestration and config generation; human reviews failure mode visualizations and guides Phase 3 design based on Phase 2 findings.",
      "timeline": "6-8 weeks",
      "team": "1-2 researchers, ~1hr/day reviewing Phase 2 diagnostics and steering ablation priorities",
      "claude_api_cost": "$300-500 (~400 conversation turns for method adaptation, experiment management, analysis)",
      "estimated_gpu_cost": "$2,100 (1400h × ~$1.50/h spot A100 80GB)",
      "risk_note": "Simulation-only (LIBERO + SimplerEnv). If existing methods transfer well to VLA BC, the contribution narrows to a useful benchmarking paper with smaller TADS improvements — still publishable at NeurIPS D&B track but less impactful for ICLR main. Consider adding Open X-Embodiment experiments for broader validation."
    },
    "auto_research": {
      "gpu_hours": "~2800h A100 80GB (full benchmarking grid + failure mode sweeps + TADS ablations across all configurations)",
      "gpu_utilization": "~85%. Agent pipelines Phase 1→2→3 sequentially with parallel runs within each phase.",
      "timeline": "12-18 days with 8 A100 GPUs in parallel",
      "team": "0 (initial setup + final review only)",
      "claude_api_cost": "$600-900 (~800 turns for end-to-end implementation, adaptation of multiple codebases, experiment orchestration, failure diagnosis, and paper drafting)",
      "estimated_gpu_cost": "$4,200 (2800h × ~$1.50/h spot A100 80GB)",
      "speed_bottleneck": "Adapting CORDS/UDS codebases to VLA training pipelines requires significant engineering. LIBERO evaluation rollouts are CPU-bound. Phase 2 analysis requires human judgment for interpreting failure modes.",
      "risk_note": "Cannot run real-robot experiments. Agent may misinterpret Phase 2 failure mode analysis without human guidance. Pure simulation scope limits venue acceptance at robotics-focused venues."
    }
  },
  "target_venues": [
    "ICLR 2027 (deadline expected ~October 2026 — ideal fit: systematic empirical study + method contribution for training methodology, strong precedent for benchmarking papers with insights)",
    "NeurIPS 2026 Datasets & Benchmarks Track (if the benchmarking contribution dominates and TADS improvements are modest, this track values systematic evaluation and reproducible comparisons)"
  ],
  "level": "solid",
  "key_references": [
    "UDS: Utility-Diversity Aware Online Batch Selection for LLM Supervised Fine-tuning (ICML 2025, Zou et al.) — closest existing work; online utility+diversity selection for LLM SFT",
    "GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning (AAAI 2021, Killamsetty et al.) — online submodular selection with convergence guarantees",
    "Coresets for Data-efficient Training of Machine Learning Models / CRAIG (ICML 2020, Mirzasoleiman et al.) — facility-location online coreset selection",
    "GRAD-MATCH: Gradient Matching based Data Subset Selection (ICML 2021, Killamsetty et al.) — gradient-matching extension of CRAIG",
    "D2 Pruning: Message Passing for Balancing Diversity and Difficulty in Data Pruning (ICLR 2024, Maharana et al.) — graph-based diversity-difficulty balancing",
    "Data Pruning by Information Maximization / InfoMax (ICLR 2025, Tan et al.) — DQP formulation balancing importance and redundancy",
    "D3: Diversity, Difficulty, and Dependability-Aware Data Selection (IJCAI 2025) — three-criteria LLM instruction tuning selection",
    "Robot Data Curation with Mutual Information Estimators / DemInf (RSS 2026, Hejna et al.) — MI-based demonstration quality for robotics",
    "DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration (CoRL 2025, Guo et al.) — sub-trajectory frame selection",
    "On Data Redundancy in VLA Training (ICRA 2026 workshop) — empirical evidence that diversity > difficulty for VLA",
    "Submodular Batch Selection for Training Deep Neural Networks (IJCAI 2019)",
    "Prioritized Experience Replay (ICLR 2016)",
    "Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining (ICLR 2025)",
    "Towards Balanced Behavior Cloning from Imbalanced Datasets (Autonomous Robots 2026)",
    "OpenVLA: An Open-Source Vision-Language-Action Model (ICML 2025)",
    "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success / OpenVLA-OFT (RSS 2025)",
    "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (arXiv 2025)",
    "SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026)",
    "CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)",
    "Curating Demonstrations using Online Experience / Demo-SCORE (RSS 2025)",
    "DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (2025)",
    "Quality over Quantity: Demonstration Curation via Influence Functions / QoQ (arXiv 2026)",
    "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (RSS 2023, Chi et al.) — action multi-modality in BC",
    "Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning (arXiv 2026)",
    "CORDS: COResets and Data Subset selection toolkit (Killamsetty et al.)",
    "DeepCore: A Comprehensive Library for Coreset Selection in Deep Learning (2022)",
    "LiLAW: Lightweight Learnable Adaptive Weighting (2025)",
    "FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models (2025)",
    "ExpReS-VLA: Specializing VLAs Through Experience Replay and Retrieval (arXiv 2025)",
    "RIPT-VLA / Interactive Post-Training for Vision-Language-Action Models (arXiv 2025)",
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026)"
  ],
  "description": "We present the first systematic evaluation of online data selection methods on Vision-Language-Action (VLA) behavioral cloning, addressing a critical gap: while methods like UDS (ICML 2025), GLISTER-Online (AAAI 2021), and CRAIG (ICML 2020) have proven effective for classification and LLM training, none have been tested on VLA BC, where trajectory temporal structure, action multi-modality, and multi-granularity diversity requirements create fundamentally different data characteristics. Our study proceeds in three phases. Phase 1 benchmarks UDS, GLISTER-Online, CRAIG, and GRAD-MATCH against static curation baselines (SCIZOR, DemInf, random subsampling) on LIBERO across 4 suites and 4 data fractions, providing the first head-to-head comparison. Phase 2 diagnoses VLA-specific failure modes through three testable hypotheses: (H1) loss-based utility is unreliable due to action multi-modality — high loss may indicate an alternative valid strategy rather than genuine difficulty; (H2) per-sample embedding diversity misses trajectory-level temporal redundancy — chunks from the same trajectory share informational content invisible to i.i.d. selection; (H3) single-scale diversity metrics collapse coverage along important axes (task type, action phase, scene configuration). Phase 3 introduces Trajectory-Aware Data Selection (TADS), with components targeting each diagnosed failure mode: trajectory-conditioned utility normalization, trajectory-identity-penalized redundancy scoring, and multi-granularity coverage constraints. Each TADS component is ablated independently and tested as augmentations of existing methods (UDS+TADS, GLISTER+TADS) to isolate VLA-specific from framework-specific effects. Unlike the original DADS proposal, which was an assembly of known components (PER + facility-location + annealing) incorrectly claimed as novel, this work makes its contribution through empirical understanding: revealing when and why general-purpose online selection fails for VLA BC, providing diagnostic tools for the failure modes, and demonstrating targeted VLA-specific fixes. The benchmarking contribution is independently valuable regardless of TADS improvement magnitude — if existing methods transfer well, that finding saves the community from re-inventing the wheel; if they fail, the failure mode analysis guides future method development. We target ICLR 2027, with sufficient time for thorough evaluation including potential extension to Open X-Embodiment for cross-embodiment validation.",
  "project_name": "diversity_aware_sampling_vla",
  "source": "web_research"
}
```

---

## Summary of how each reviewer issue was addressed:

**1. False gap claim** — Completely rewritten. The gap is no longer "no one combines loss + diversity online" (which was false). Instead: "no one has evaluated whether UDS/GLISTER/CRAIG transfer to VLA BC." UDS, GLISTER-Online, and CRAIG are now explicitly cited and positioned as the primary methods to benchmark.

**2. Major missing related work** — All 7 papers added: UDS, D2 Pruning, InfoMax, D3, GLISTER-Online, CRAIG, DemInf (Hejna et al.), DemoSpeedup. Plus GRAD-MATCH, CORDS toolkit, DeepCore, Diffusion Policy (for action multi-modality), and LIBERO-Plus.

**3. Component assembly → empirical understanding** — The contribution is no longer "here's a new combined method." It's restructured as: (Phase 1) systematic benchmarking of existing methods on VLA BC, (Phase 2) diagnosis of VLA-specific failure modes via testable hypotheses, (Phase 3) targeted adaptations (TADS) that address diagnosed failures. TADS components are tested as augmentations of UDS and GLISTER to isolate VLA-specific vs. framework effects.

**4. Workshop paper risk** — Acknowledged explicitly in the landscape: "A workshop paper whose specific quantitative claims should be verified." The motivation no longer depends solely on this paper — the broader observation that diversity matters is supported by multiple sources.

**5. CoRL 2026 dropped** — Removed entirely. Targeting ICLR 2027 (October deadline) with NeurIPS D&B track as fallback.

**6. Hand-waved convergence analysis dropped** — The vague "convergence analysis under mild assumptions" claim is gone. Instead, the paper leverages existing convergence results from GLISTER and CRAIG and focuses on empirical diagnosis of where those guarantees break in VLA BC.

**7. DemoSpeedup and DemInf added** — Both fully integrated into the landscape with accurate descriptions.

Sources:
- [UDS: Utility-Diversity Aware Online Batch Selection](https://arxiv.org/abs/2510.16882)
- [GLISTER (AAAI 2021)](https://ojs.aaai.org/index.php/AAAI/article/view/16988)
- [CRAIG (ICML 2020)](https://arxiv.org/abs/1906.01827)
- [D2 Pruning (ICLR 2024)](https://arxiv.org/abs/2310.07931)
- [InfoMax (ICLR 2025)](https://arxiv.org/abs/2506.01701)
- [D3 (IJCAI 2025)](https://arxiv.org/abs/2503.11441)
- [Robot Data Curation with MI (RSS 2026)](https://arxiv.org/abs/2502.08623)
- [DemoSpeedup (CoRL 2025)](https://arxiv.org/abs/2506.05064)
- [CORDS toolkit](https://github.com/decile-team/cords)
- [UDS GitHub](https://github.com/gfyddha/UDS)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84721039-d98b-4223-a0e0-fe2be751872b",
  "isSidechain": false,
  "requestId": "req_011Cb1kzdhTKqjaRDa8cuM42",
  "type": "assistant",
  "uuid": "0e4e29dc-708a-415b-9e3d-194519e2597b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KMYmCbXXReideRQegQw6Wa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 87,
      "cache_read_input_tokens": 71456,
      "output_tokens": 7335,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 87,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7335,
          "cache_read_input_tokens": 71456,
          "cache_creation_input_tokens": 87,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 87
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

_source line 102_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Beyond Difficulty: Diversity-Aware Dynamic Sampling for Data-Efficient…",
  "leafUuid": "0e4e29dc-708a-415b-9e3d-194519e2597b",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Runtime record

_source line 103_

```json
{
  "type": "ai-title",
  "aiTitle": "Benchmark diversity-aware selection methods on VLA BC",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Runtime record

_source line 104_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Beyond Difficulty: Diversity-Aware Dynamic Sampling for Data-Efficient…",
  "leafUuid": "0e4e29dc-708a-415b-9e3d-194519e2597b",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---

### Runtime record

_source line 105_

```json
{
  "type": "ai-title",
  "aiTitle": "Benchmark diversity-aware selection methods on VLA BC",
  "sessionId": "85f9b876-59ee-4640-836b-8bde832bc012"
}
```

---
