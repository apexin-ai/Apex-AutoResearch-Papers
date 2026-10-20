# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/f0193cec-8a3a-4441-80b6-a0e385e9422b.jsonl`
- **Structured JSON:** [`102bbb2a5e3f197b0253.json`](../../sessions/10/102bbb2a5e3f197b0253.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T20:42:09.770Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T20:42:09.770Z",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Stop-Gradient Intent Reconstruction with Attention-Weighted Pooling for Trainable Text Communication in Multi-Agent GRPO\",\n  \"core_problem\": \"Recent latent-communication methods (LatentMAS, ICML 2026; RecursiveMAS, April 2026; DiffMAS, April 2026) bypass text entirely, achieving 14.6–26.7% accuracy gains over text-based MAS by communicating through hidden-state representations or KV-cache transfers. While effective, abandoning text communication sacrifices human interpretability, debuggability, and interoperability with human-in-the-loop systems. Meanwhile, text-based multi-agent GRPO methods (AT-GRPO, MAGRPO) optimize only task reward, and credit assignment methods (C3, CCPO, CoFi-PGMA) provide agent-level or message-level scalar signals without within-message token differentiation. Can dense, token-differentiated reconstruction supervision on text messages close the performance gap with latent approaches while preserving the interpretability advantages of text-based communication?\",\n  \"opportunity\": \"The multi-agent LLM communication landscape has bifurcated: latent-space methods (LatentMAS, RecursiveMAS, DiffMAS) achieve superior performance by replacing text with continuous representations or KV-cache traces, while text-based RL methods (AT-GRPO, MAGRPO, C3, CCPO) optimize task reward or agent-level credit without training message quality directly. Both families leave an opening. Latent methods sacrifice interpretability—a critical requirement for safety-sensitive deployments, debugging, and human oversight. Text-based RL methods leave message quality to emerge implicitly from sparse task reward. In classical MARL, Lin et al. (NeurIPS 2021) demonstrated that autoencoder reconstruction grounds communication effectively in small networks (state dim ~10-100). However, scaling reconstruction to LLM-scale multi-agent RL introduces distinct challenges absent in the classical setting: (a) hidden states are high-dimensional (2048+), requiring architectural choices for feasible reconstruction; (b) LoRA adapter updates create a continuously shifting reconstruction target; (c) GRPO's group-relative advantage normalization creates optimization dynamics qualitatively different from A3C/PPO used in classical MARL; (d) naive mean-pooling of message tokens yields uniform gradients, failing to differentiate token contributions to intent communication. We propose Stop-Gradient Intent Reconstruction (SGIR) with attention-weighted pooling and EMA target stabilization—a principled approach to make reconstruction-based communication training feasible at LLM scale with genuine token-level gradient differentiation. This is timely because PettingLLMs provides multi-agent GRPO infrastructure with LoRA support, DEPART/HIMPO establishes ALFWorld and WebArena-Lite as multi-agent benchmarks with planner-executor message passing, EMA-PG (Zhang & Ba, Feb 2026) provides theoretical stability conditions for EMA anchors in GRPO-like training, and the interpretability advantages of text communication are increasingly valued in the LLM safety community.\",\n  \"landscape\": \"**Latent communication (bypass text):** LatentMAS (ICML 2026 Spotlight, arXiv 2511.20639) enables training-free latent collaboration via shared working memory of last-layer hidden embeddings, achieving +14.6% accuracy and 70-83% token reduction across 9 benchmarks. RecursiveMAS (April 2026, arXiv 2604.25917) trains lightweight RecursiveLink modules for cross-agent latent state transfer with inner-outer loop optimization, achieving +8.3% accuracy with 2.4x speedup. DiffMAS (April 2026, arXiv 2604.21794) by Yu et al. (UIUC) optimizes inter-agent communication end-to-end via KV-cache trace construction and parameter-efficient supervised training over latent trajectories, achieving +26.7% on AIME24 and consistent gains on GPQA-Diamond and code generation. All three replace text communication entirely with latent representations. **Text-based multi-agent GRPO (task reward only):** AT-GRPO/Stronger-MAS (ICLR 2026) achieves 96-99.5% on cooperative planning and 84% improvement on Sokoban 6x6 via agent-and-turn-wise GRPO. MAGRPO (AAAI 2026) and M-GRPO train multi-agent writing/coding without communication losses. Graph-GRPO (March 2026) optimizes topology, not message content. **Credit assignment (agent-level signal):** C3 (March 2026, arXiv 2603.06859) provides message-level counterfactual credit via fixed-continuation replay. CCPO (March 2026, arXiv 2603.21563) estimates marginal contributions through counterfactual baselines. CoFi-PGMA (April 2026, arXiv 2604.22785) derives leave-one-out difference rewards. Dr. MAS (Feb 2026, arXiv 2602.08847) stabilizes multi-agent GRPO via agent-wise advantage normalization. All provide agent-level or message-level scalar signals, not within-message token-differentiated supervision. **Communication auxiliary losses:** MAPoRL (ACL 2025) trains influence-aware verification rewards (turn-level). Social Deduction LLM (AAMAS 2025) adds belief-change prediction losses in LLM PPO. ThoughtComm (NeurIPS 2025) uses autoencoders on LLM hidden states for inference-time latent thought communication without RL training. **EMA stability theory:** EMA-PG (Feb 2026, arXiv 2602.04417) by Zhang & Ba derives stability conditions for EMA anchors in GRPO-like policy gradient training, showing EMA acts as a slowly-moving reference analogous to target networks in DQN, with theoretical bounds on when τ close to 1 ensures training stability. **Classical reconstruction:** Lin et al. (NeurIPS 2021) showed autoencoder reconstruction grounds communication in small MARL networks with strong task performance. LangGround (NeurIPS 2024) chose language embedding alignment for human interpretability in ad-hoc teamwork. **The gap:** No method provides token-differentiated training signal for text-based inter-agent messages in LLM multi-agent GRPO. DiffMAS is closest in motivation (optimizing communication quality) but replaces text with latent KV-cache transfers. SGIR occupies the specific intersection: reconstruction auxiliary loss with attention-weighted token differentiation and EMA-stabilized stop-gradient targets in LLM GRPO, improving text communication quality rather than replacing it.\",\n  \"approach\": \"We extend AT-GRPO (PettingLLMs) with Stop-Gradient Intent Reconstruction (SGIR), an auxiliary loss providing token-differentiated supervision of inter-agent text message quality during multi-agent GRPO training. **Core mechanism:** (1) When agent i generates a message m = [m_1, ..., m_T], we extract its intent embedding as the EMA-smoothed, stop-gradient-detached last hidden state: e_i = sg(EMA_τ(h_i^L)). The EMA stabilization (τ=0.999) addresses the moving-target problem—as LoRA adapters update, the target distribution shifts slowly enough for the decoder to track. This design is theoretically grounded by EMA-PG (Zhang & Ba, 2026), which derives stability conditions for EMA anchors in policy gradient training: their analysis shows τ close to 1 ensures the anchor tracks the policy smoothly without inducing optimization instability. Stop-gradient prevents reconstruction from distorting the sender's internal representation. (2) A lightweight attention-weighted reconstruction decoder D_φ (~18M params) computes token-differentiated intent reconstruction. Rather than mean-pooling (which yields identical gradients for all tokens), we use learned attention pooling: α_j = softmax(v^T · tanh(W_attn · h_j^msg + b_attn)), pool(m) = Σ_j α_j · h_j^msg, then L_recon = ||MLP(pool(m)) - e_i||². The attention weights α_j create genuine per-token gradient differentiation: ∂L/∂h_j^msg ∝ α_j (tokens attending more to intent receive stronger gradients) plus additional terms from attention weight gradients with respect to inputs. This makes the supervision genuinely token-differentiated—high-attention tokens (intent-carrying content words) receive stronger training signal than low-attention tokens (syntactic filler). The attention weights themselves serve as an interpretability tool, revealing which message tokens carry the most intent information. (3) Total loss: L_GRPO + λ·L_recon, with λ annealed from 0.3→0 over training (dense signal fades as task reward becomes informative). **Key design rationale and differentiation:** Unlike DiffMAS (Yu et al., April 2026) which optimizes communication end-to-end by replacing text with KV-cache latent traces via supervised training, SGIR preserves human-readable text messages while using reconstruction purely as a training-time auxiliary signal—DiffMAS achieves higher raw performance (+26.7%) but sacrifices interpretability, while SGIR targets the interpretability-performance tradeoff. Unlike credit assignment methods (C3, CCPO, CoFi-PGMA) which determine *which agent* or *which message* contributed via scalar signals, SGIR's attention-weighted reconstruction determines *which tokens within a message* best convey the sender's intent, providing gradient differentiation at sub-message granularity. **Architecture note:** Following DEPART, planner and executor share base model weights (Qwen3-1.7B) with agent-specific LoRA adapters (rank=64). This shared-weight design means the reconstruction loss implicitly transfers learning between agents via the shared base, while LoRA specialization maintains role differentiation. **Implementation:** Built on PettingLLMs with DEPART-style hierarchical setup. **Evaluation (3 benchmarks + qualitative):** (1) ALFWorld with DEPART-style planner-executor (on user's allowed benchmark list): planner generates natural language plans, executor acts—SGIR trains the planner's message quality. Baselines: DEPART/HIMPO without SGIR, single-agent HiPER (97.4%). (2) WebArena-Lite with DEPART-style planner-executor (WebArena on user's allowed benchmark list, 165 human-verified tasks): demonstrates generalization to web navigation domains. Baselines: DEPART/HIMPO without SGIR. (3) Sokoban 6x6 from Stronger-MAS (community-standard multi-agent GRPO benchmark with published AT-GRPO baselines—included despite not being on the allowed list because it provides the only existing multi-agent GRPO baselines for controlled comparison; the 6x6 scale is non-trivial unlike 4x4). (4) Qualitative message quality analysis: human evaluation of planner messages in ALFWorld comparing SGIR vs. baseline, measuring informativeness, conciseness, and actionability—this directly demonstrates the interpretability advantage that motivates preserving text over latent communication. **Ablations (4):** (i) Stop-gradient + EMA vs. joint training without stop-gradient (tests whether stop-gradient is necessary at LLM scale); (ii) EMA τ values {0.99, 0.999, 0.9999} informed by EMA-PG stability analysis; (iii) λ annealing schedule (constant 0.1 vs. linear 0.3→0 vs. cosine); (iv) Attention-weighted pooling vs. mean pooling vs. max pooling (directly tests whether token differentiation matters—if mean pooling performs equally, the attention mechanism adds complexity without benefit). **Composability experiment:** SGIR + Dr. MAS agent-wise normalization, testing orthogonality with GRPO stability methods.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~200h H100 (ALFWorld planner-executor: ~60h; WebArena-Lite planner-executor: ~50h; Stronger-MAS Sokoban 6x6: ~40h; 4 ablations on Sokoban: ~40h; composability experiment: ~10h)\",\n      \"gpu_utilization\": \"Low (30-40%): human bottleneck on integration, debugging, analysis\",\n      \"timeline\": \"2.5-3.5 months\",\n      \"team\": \"1-2 researchers (RL + multi-agent expertise)\",\n      \"estimated_gpu_cost\": \"$500-600 (at ~$2.50-3.00/GPU-hr)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~220h H100 (systematic runs with approval gates for attention architecture design and EMA τ selection)\",\n      \"gpu_utilization\": \"Moderate (50-65%): agent queues experiments, pauses for design decisions\",\n      \"timeline\": \"6-8 weeks\",\n      \"team\": \"1 researcher, ~30min/day for reviews + human evaluation of message quality\",\n      \"claude_api_cost\": \"$120-200 (~1800-3000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$550-660 (at ~$2.50-3.00/GPU-hr)\",\n      \"risk_note\": \"Attention pooling architecture and EMA τ selection benefit from expert judgment; WebArena-Lite multi-agent setup requires DEPART-style environment engineering; human message quality evaluation requires annotation protocol\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~250h H100 (budget-capped: systematic sweeps across EMA τ, λ schedules, pooling variants, all three benchmarks; continuous pipeline within budget)\",\n      \"gpu_utilization\": \"High (85-95%): 24/7 operation within 250h cap\",\n      \"timeline\": \"10-14 days with 4 concurrent H100s\",\n      \"team\": \"0 (uses PettingLLMs + DEPART infrastructure)\",\n      \"claude_api_cost\": \"$250-450 (~3500-6000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$625-750 (at ~$2.50-3.00/GPU-hr)\",\n      \"speed_bottleneck\": \"WebArena-Lite environment setup from DEPART codebase; human evaluation requires separate annotation pass; 4 concurrent H100s needed\",\n      \"risk_note\": \"WebArena-Lite multi-agent setup may require non-trivial adaptation from DEPART; fixed 250h cap limits exploration breadth; human eval cannot be fully automated\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract: Jul 25 2026, full paper: Aug 1 2026; Montréal, Feb 16-23 2027) — primary target, realistic timeline for 3-benchmark evaluation\",\n    \"ICLR 2027 (expected ~Oct 2026, deadline TBD) — fallback with additional time for comprehensive experiments\",\n    \"Note: User requested EMNLP 2026 (ARR deadline May 25, 2026), but 15-day timeline is infeasible for proposed 200+ GPU-hour experimental program. AAAI 2027 (Aug 1) provides ~12 weeks, sufficient for full evaluation including human message quality annotation.\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"Latent Collaboration in Multi-Agent Systems — LatentMAS (ICML 2026 Spotlight, arXiv 2511.20639)\",\n    \"Recursive Multi-Agent Systems — RecursiveMAS (April 2026, arXiv 2604.25917)\",\n    \"Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems — DiffMAS (April 2026, arXiv 2604.21794)\",\n    \"EMA Policy Gradient: Taming RL for LLMs with EMA Anchor and Top-k KL — EMA-PG (Feb 2026, arXiv 2602.04417)\",\n    \"Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems (Feb 2026, arXiv 2602.08847)\",\n    \"Counterfactual Credit Policy Optimization — CCPO (March 2026, arXiv 2603.21563)\",\n    \"CoFi-PGMA: Counterfactual Policy Gradients under Filtered Feedback for Multi-Agent LLMs (April 2026, arXiv 2604.22785)\",\n    \"C3: Contextual Counterfactual Credit Assignment for Multi-Agent RL in LLM Collaboration (March 2026, arXiv 2603.06859)\",\n    \"Stronger-MAS: Multi-Agent Reinforcement Learning for Collaborative LLMs — AT-GRPO (ICLR 2026)\",\n    \"LLM Collaboration with Multi-Agent Reinforcement Learning — MAGRPO (AAAI 2026)\",\n    \"Learning to Ground Multi-Agent Communication with Autoencoders — Lin et al. (NeurIPS 2021)\",\n    \"Language Grounded Multi-Agent Communication — LangGround (NeurIPS 2024)\",\n    \"Thought Communication in Multiagent Collaboration — ThoughtComm (NeurIPS 2025)\",\n    \"Why Do Multi-Agent LLM Systems Fail? (NeurIPS 2025)\",\n    \"MAPoRL: Multi-Agent Post-Co-Training for Collaborative LLMs with RL (ACL 2025)\",\n    \"Training Language Models for Social Deduction with Multi-Agent RL (AAMAS 2025)\",\n    \"DEPART: Hierarchical Multi-Agent System for Multi-Turn Interaction — HIMPO (OpenReview 2025-2026)\",\n    \"HiPER: Hierarchical RL with Explicit Credit Assignment for LLM Agents (Feb 2026, arXiv 2602.16165)\",\n    \"Graph-GRPO: Stabilizing Multi-Agent Topology Learning via GRPO (arXiv 2026)\",\n    \"Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems (arXiv 2025)\",\n    \"Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces (May 2026, arXiv 2605.02801)\"\n  ],\n  \"description\": \"We propose Stop-Gradient Intent Reconstruction (SGIR), an auxiliary loss that provides token-differentiated supervision for text-based inter-agent communication during multi-agent GRPO training. Recent latent-communication methods (LatentMAS, ICML 2026; RecursiveMAS, April 2026; DiffMAS, April 2026) show that bypassing text for direct hidden-state or KV-cache transfer yields large gains (+14.6–26.7%), but sacrifices the interpretability, debuggability, and human interoperability of text communication. Text-based multi-agent GRPO methods (AT-GRPO, MAGRPO) and credit assignment approaches (C3, CCPO, CoFi-PGMA) optimize task reward or agent-level credit without within-message token differentiation. SGIR bridges this gap: a lightweight attention-weighted reconstruction decoder reconstructs the sender's EMA-stabilized, stop-gradient-detached intent embedding from each text message, with learned attention weights creating genuine per-token gradient differentiation—intent-carrying tokens receive stronger training signal than syntactic filler. This contrasts with naive mean-pooling which yields identical gradients for all tokens (effectively message-level supervision). The EMA target (τ=0.999) addresses the moving-target problem from continuous LoRA updates, grounded in the stability analysis of EMA-PG (Zhang & Ba, Feb 2026) which derives conditions under which EMA anchors ensure smooth policy tracking in GRPO-like training. Unlike DiffMAS which replaces text with KV-cache latent traces for maximum performance, SGIR preserves human-readable messages—using reconstruction purely as a training signal to encourage informativeness while maintaining the interpretability required for safety-critical deployment and human oversight. Architecture follows DEPART: planner and executor share base model weights (Qwen3-1.7B) with agent-specific LoRA adapters (rank=64). We evaluate on three benchmarks: (1) ALFWorld with DEPART-style planner-executor (allowed list), (2) WebArena-Lite with DEPART-style planner-executor (allowed list, 165 tasks), and (3) Sokoban 6x6 from Stronger-MAS (community standard with published AT-GRPO baselines for controlled comparison). A qualitative human evaluation of planner message quality in ALFWorld directly demonstrates the interpretability advantage motivating text preservation. Four ablations test: (1) stop-gradient necessity at LLM scale, (2) EMA τ informed by EMA-PG stability theory, (3) λ annealing schedule, (4) attention-weighted vs. mean vs. max pooling (testing whether token differentiation provides genuine benefit). A composability experiment combines SGIR with Dr. MAS agent-wise normalization. Estimated compute: ≤250 H100-hours ($500-750). Targets AAAI 2027 (Aug 1, 2026 deadline), providing 12 weeks for full experimental program including human annotation.\",\n  \"project_name\": \"recon_reg_comm_training\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 4)\nIssues: [\"MISSING CITATION — MASIA (NeurIPS 2022): 'Efficient Multi-agent Communication via Self-supervised Information Aggregation' (Guan et al.) uses reconstruction loss (reconstructing global state from messages) combined with attention-based message extraction in multi-agent communication. This is a direct precursor combining two of SGIR's core components (reconstruction + attention aggregation) and must be cited and differentiated.\", \"OVERSTATED ATTENTION POOLING NOVELTY: The attention-weighted pooling mechanism (α_j = softmax(v^T·tanh(W·h_j+b))) is the standard Hierarchical Attention Network formula from Yang et al. (NAACL 2016) and Lin et al. (ICLR 2017). Framing it as 'genuine per-token gradient differentiation' obscures that this is a trivially standard architectural choice. The gradient analysis also omits the softmax Jacobian redistribution term (∂α_k/∂h_j contributions), making the mechanism appear cleaner than it actually is.\", \"MISSING CONCURRENT WORK — Interlat (arXiv 2511.09149, revised April 2026): 'Enabling Agents to Communicate Entirely in Latent Space' by Du et al. proposes inter-agent communication via continuous last hidden states with learned compression. This is another latent communication method that should be in the landscape for completeness.\", \"NARROW NOVELTY GAP: The contribution reduces to 'apply stop-gradient + EMA to make reconstruction work at LLM scale' — the attention pooling is standard, the reconstruction idea is from Lin et al. 2021, and the EMA design is borrowed from EMA-PG. Each 'challenge' at LLM scale is addressed by a known technique. This risks the 'engineering combination' critique at top venues where reviewers expect conceptual novelty.\", \"UNCERTAIN EMPIRICAL IMPACT: No preliminary evidence suggests reconstruction can meaningfully close the text-latent performance gap. If LatentMAS achieves +14.6% by bypassing text and SGIR achieves +2-3% while preserving text, the contribution becomes 'we traded most of the performance for interpretability' — which may not be compelling without a strong interpretability analysis showing concrete debugging/safety benefits.\", \"VENUE DEVIATION PERSISTS: User requested EMNLP 2026 (ARR May 25). Proposal targets AAAI 2027 (Aug 1). While acknowledged and justified, this still does not meet the user's stated constraint.\"]\nFeedback: The proposal has improved substantially over 4 rounds — landscape is now comprehensive, references are verified, benchmark compliance is mostly addressed, and the technical mechanism is clarified. Three specific actions to reach pass quality:\n\n1. **Cite MASIA (NeurIPS 2022) and reframe the novelty narrative**: MASIA already combines reconstruction + attention for multi-agent communication messages. Your differentiation: MASIA reconstructs *global state* from messages in small MARL; SGIR reconstructs *sender intent embeddings* from messages at *LLM scale* with *stop-gradient + EMA* to handle LoRA-induced moving targets. The novelty is NOT attention pooling (standard since 2016) — it's the full architectural framework (stop-gradient isolation + EMA stabilization + λ annealing) that makes reconstruction work in the LLM-GRPO setting where naive approaches fail.\n\n2. **Strengthen the impact argument with concrete interpretability value**: The 'preserve text for interpretability' argument is currently abstract. Make it concrete: (a) include a failure-mode analysis showing how SGIR-trained messages help debug agent errors that latent communication cannot, (b) show that SGIR attention weights identify which tokens carry intent (a free interpretability tool), (c) demonstrate human-in-the-loop intervention scenarios where text messages enable real-time correction. This converts the interpretability claim from a philosophical argument into a demonstrated advantage.\n\n3. **Consider a direct text-vs-latent comparison**: On one benchmark (e.g., ALFWorld), run both LatentMAS (training-free, so cheap to evaluate) and SGIR. If SGIR achieves 70-80% of LatentMAS's gains while preserving readable messages, that's a compelling result. If it achieves only 10-20%, you need the interpretability argument to be ironclad. Having this comparison in hand before writing would let you frame the contribution appropriately.\n\nMinor: fix the gradient analysis to acknowledge the softmax Jacobian term, or simply state 'the dominant gradient term is α_j-weighted' without claiming strict proportionality.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 4 轮修订，近 3 轮的平均分从 3.2 到 3.5，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T20:42:09.774Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T20:42:09.774Z",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b"
}
```

---

## Round 1

29 recorded events

### User

_source line 3 · 2026-05-10T20:42:09.793Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "Stop-Gradient Intent Reconstruction with Attention-Weighted Pooling for Trainable Text Communication in Multi-Agent GRPO",
  "core_problem": "Recent latent-communication methods (LatentMAS, ICML 2026; RecursiveMAS, April 2026; DiffMAS, April 2026) bypass text entirely, achieving 14.6–26.7% accuracy gains over text-based MAS by communicating through hidden-state representations or KV-cache transfers. While effective, abandoning text communication sacrifices human interpretability, debuggability, and interoperability with human-in-the-loop systems. Meanwhile, text-based multi-agent GRPO methods (AT-GRPO, MAGRPO) optimize only task reward, and credit assignment methods (C3, CCPO, CoFi-PGMA) provide agent-level or message-level scalar signals without within-message token differentiation. Can dense, token-differentiated reconstruction supervision on text messages close the performance gap with latent approaches while preserving the interpretability advantages of text-based communication?",
  "opportunity": "The multi-agent LLM communication landscape has bifurcated: latent-space methods (LatentMAS, RecursiveMAS, DiffMAS) achieve superior performance by replacing text with continuous representations or KV-cache traces, while text-based RL methods (AT-GRPO, MAGRPO, C3, CCPO) optimize task reward or agent-level credit without training message quality directly. Both families leave an opening. Latent methods sacrifice interpretability—a critical requirement for safety-sensitive deployments, debugging, and human oversight. Text-based RL methods leave message quality to emerge implicitly from sparse task reward. In classical MARL, Lin et al. (NeurIPS 2021) demonstrated that autoencoder reconstruction grounds communication effectively in small networks (state dim ~10-100). However, scaling reconstruction to LLM-scale multi-agent RL introduces distinct challenges absent in the classical setting: (a) hidden states are high-dimensional (2048+), requiring architectural choices for feasible reconstruction; (b) LoRA adapter updates create a continuously shifting reconstruction target; (c) GRPO's group-relative advantage normalization creates optimization dynamics qualitatively different from A3C/PPO used in classical MARL; (d) naive mean-pooling of message tokens yields uniform gradients, failing to differentiate token contributions to intent communication. We propose Stop-Gradient Intent Reconstruction (SGIR) with attention-weighted pooling and EMA target stabilization—a principled approach to make reconstruction-based communication training feasible at LLM scale with genuine token-level gradient differentiation. This is timely because PettingLLMs provides multi-agent GRPO infrastructure with LoRA support, DEPART/HIMPO establishes ALFWorld and WebArena-Lite as multi-agent benchmarks with planner-executor message passing, EMA-PG (Zhang & Ba, Feb 2026) provides theoretical stability conditions for EMA anchors in GRPO-like training, and the interpretability advantages of text communication are increasingly valued in the LLM safety community.",
  "landscape": "**Latent communication (bypass text):** LatentMAS (ICML 2026 Spotlight, arXiv 2511.20639) enables training-free latent collaboration via shared working memory of last-layer hidden embeddings, achieving +14.6% accuracy and 70-83% token reduction across 9 benchmarks. RecursiveMAS (April 2026, arXiv 2604.25917) trains lightweight RecursiveLink modules for cross-agent latent state transfer with inner-outer loop optimization, achieving +8.3% accuracy with 2.4x speedup. DiffMAS (April 2026, arXiv 2604.21794) by Yu et al. (UIUC) optimizes inter-agent communication end-to-end via KV-cache trace construction and parameter-efficient supervised training over latent trajectories, achieving +26.7% on AIME24 and consistent gains on GPQA-Diamond and code generation. All three replace text communication entirely with latent representations. **Text-based multi-agent GRPO (task reward only):** AT-GRPO/Stronger-MAS (ICLR 2026) achieves 96-99.5% on cooperative planning and 84% improvement on Sokoban 6x6 via agent-and-turn-wise GRPO. MAGRPO (AAAI 2026) and M-GRPO train multi-agent writing/coding without communication losses. Graph-GRPO (March 2026) optimizes topology, not message content. **Credit assignment (agent-level signal):** C3 (March 2026, arXiv 2603.06859) provides message-level counterfactual credit via fixed-continuation replay. CCPO (March 2026, arXiv 2603.21563) estimates marginal contributions through counterfactual baselines. CoFi-PGMA (April 2026, arXiv 2604.22785) derives leave-one-out difference rewards. Dr. MAS (Feb 2026, arXiv 2602.08847) stabilizes multi-agent GRPO via agent-wise advantage normalization. All provide agent-level or message-level scalar signals, not within-message token-differentiated supervision. **Communication auxiliary losses:** MAPoRL (ACL 2025) trains influence-aware verification rewards (turn-level). Social Deduction LLM (AAMAS 2025) adds belief-change prediction losses in LLM PPO. ThoughtComm (NeurIPS 2025) uses autoencoders on LLM hidden states for inference-time latent thought communication without RL training. **EMA stability theory:** EMA-PG (Feb 2026, arXiv 2602.04417) by Zhang & Ba derives stability conditions for EMA anchors in GRPO-like policy gradient training, showing EMA acts as a slowly-moving reference analogous to target networks in DQN, with theoretical bounds on when τ close to 1 ensures training stability. **Classical reconstruction:** Lin et al. (NeurIPS 2021) showed autoencoder reconstruction grounds communication in small MARL networks with strong task performance. LangGround (NeurIPS 2024) chose language embedding alignment for human interpretability in ad-hoc teamwork. **The gap:** No method provides token-differentiated training signal for text-based inter-agent messages in LLM multi-agent GRPO. DiffMAS is closest in motivation (optimizing communication quality) but replaces text with latent KV-cache transfers. SGIR occupies the specific intersection: reconstruction auxiliary loss with attention-weighted token differentiation and EMA-stabilized stop-gradient targets in LLM GRPO, improving text communication quality rather than replacing it.",
  "approach": "We extend AT-GRPO (PettingLLMs) with Stop-Gradient Intent Reconstruction (SGIR), an auxiliary loss providing token-differentiated supervision of inter-agent text message quality during multi-agent GRPO training. **Core mechanism:** (1) When agent i generates a message m = [m_1, ..., m_T], we extract its intent embedding as the EMA-smoothed, stop-gradient-detached last hidden state: e_i = sg(EMA_τ(h_i^L)). The EMA stabilization (τ=0.999) addresses the moving-target problem—as LoRA adapters update, the target distribution shifts slowly enough for the decoder to track. This design is theoretically grounded by EMA-PG (Zhang & Ba, 2026), which derives stability conditions for EMA anchors in policy gradient training: their analysis shows τ close to 1 ensures the anchor tracks the policy smoothly without inducing optimization instability. Stop-gradient prevents reconstruction from distorting the sender's internal representation. (2) A lightweight attention-weighted reconstruction decoder D_φ (~18M params) computes token-differentiated intent reconstruction. Rather than mean-pooling (which yields identical gradients for all tokens), we use learned attention pooling: α_j = softmax(v^T · tanh(W_attn · h_j^msg + b_attn)), pool(m) = Σ_j α_j · h_j^msg, then L_recon = ||MLP(pool(m)) - e_i||². The attention weights α_j create genuine per-token gradient differentiation: ∂L/∂h_j^msg ∝ α_j (tokens attending more to intent receive stronger gradients) plus additional terms from attention weight gradients with respect to inputs. This makes the supervision genuinely token-differentiated—high-attention tokens (intent-carrying content words) receive stronger training signal than low-attention tokens (syntactic filler). The attention weights themselves serve as an interpretability tool, revealing which message tokens carry the most intent information. (3) Total loss: L_GRPO + λ·L_recon, with λ annealed from 0.3→0 over training (dense signal fades as task reward becomes informative). **Key design rationale and differentiation:** Unlike DiffMAS (Yu et al., April 2026) which optimizes communication end-to-end by replacing text with KV-cache latent traces via supervised training, SGIR preserves human-readable text messages while using reconstruction purely as a training-time auxiliary signal—DiffMAS achieves higher raw performance (+26.7%) but sacrifices interpretability, while SGIR targets the interpretability-performance tradeoff. Unlike credit assignment methods (C3, CCPO, CoFi-PGMA) which determine *which agent* or *which message* contributed via scalar signals, SGIR's attention-weighted reconstruction determines *which tokens within a message* best convey the sender's intent, providing gradient differentiation at sub-message granularity. **Architecture note:** Following DEPART, planner and executor share base model weights (Qwen3-1.7B) with agent-specific LoRA adapters (rank=64). This shared-weight design means the reconstruction loss implicitly transfers learning between agents via the shared base, while LoRA specialization maintains role differentiation. **Implementation:** Built on PettingLLMs with DEPART-style hierarchical setup. **Evaluation (3 benchmarks + qualitative):** (1) ALFWorld with DEPART-style planner-executor (on user's allowed benchmark list): planner generates natural language plans, executor acts—SGIR trains the planner's message quality. Baselines: DEPART/HIMPO without SGIR, single-agent HiPER (97.4%). (2) WebArena-Lite with DEPART-style planner-executor (WebArena on user's allowed benchmark list, 165 human-verified tasks): demonstrates generalization to web navigation domains. Baselines: DEPART/HIMPO without SGIR. (3) Sokoban 6x6 from Stronger-MAS (community-standard multi-agent GRPO benchmark with published AT-GRPO baselines—included despite not being on the allowed list because it provides the only existing multi-agent GRPO baselines for controlled comparison; the 6x6 scale is non-trivial unlike 4x4). (4) Qualitative message quality analysis: human evaluation of planner messages in ALFWorld comparing SGIR vs. baseline, measuring informativeness, conciseness, and actionability—this directly demonstrates the interpretability advantage that motivates preserving text over latent communication. **Ablations (4):** (i) Stop-gradient + EMA vs. joint training without stop-gradient (tests whether stop-gradient is necessary at LLM scale); (ii) EMA τ values {0.99, 0.999, 0.9999} informed by EMA-PG stability analysis; (iii) λ annealing schedule (constant 0.1 vs. linear 0.3→0 vs. cosine); (iv) Attention-weighted pooling vs. mean pooling vs. max pooling (directly tests whether token differentiation matters—if mean pooling performs equally, the attention mechanism adds complexity without benefit). **Composability experiment:** SGIR + Dr. MAS agent-wise normalization, testing orthogonality with GRPO stability methods.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~200h H100 (ALFWorld planner-executor: ~60h; WebArena-Lite planner-executor: ~50h; Stronger-MAS Sokoban 6x6: ~40h; 4 ablations on Sokoban: ~40h; composability experiment: ~10h)",
      "gpu_utilization": "Low (30-40%): human bottleneck on integration, debugging, analysis",
      "timeline": "2.5-3.5 months",
      "team": "1-2 researchers (RL + multi-agent expertise)",
      "estimated_gpu_cost": "$500-600 (at ~$2.50-3.00/GPU-hr)"
    },
    "human_in_loop": {
      "gpu_hours": "~220h H100 (systematic runs with approval gates for attention architecture design and EMA τ selection)",
      "gpu_utilization": "Moderate (50-65%): agent queues experiments, pauses for design decisions",
      "timeline": "6-8 weeks",
      "team": "1 researcher, ~30min/day for reviews + human evaluation of message quality",
      "claude_api_cost": "$120-200 (~1800-3000 Opus turns)",
      "estimated_gpu_cost": "$550-660 (at ~$2.50-3.00/GPU-hr)",
      "risk_note": "Attention pooling architecture and EMA τ selection benefit from expert judgment; WebArena-Lite multi-agent setup requires DEPART-style environment engineering; human message quality evaluation requires annotation protocol"
    },
    "auto_research": {
      "gpu_hours": "~250h H100 (budget-capped: systematic sweeps across EMA τ, λ schedules, pooling variants, all three benchmarks; continuous pipeline within budget)",
      "gpu_utilization": "High (85-95%): 24/7 operation within 250h cap",
      "timeline": "10-14 days with 4 concurrent H100s",
      "team": "0 (uses PettingLLMs + DEPART infrastructure)",
      "claude_api_cost": "$250-450 (~3500-6000 Opus turns)",
      "estimated_gpu_cost": "$625-750 (at ~$2.50-3.00/GPU-hr)",
      "speed_bottleneck": "WebArena-Lite environment setup from DEPART codebase; human evaluation requires separate annotation pass; 4 concurrent H100s needed",
      "risk_note": "WebArena-Lite multi-agent setup may require non-trivial adaptation from DEPART; fixed 250h cap limits exploration breadth; human eval cannot be fully automated"
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract: Jul 25 2026, full paper: Aug 1 2026; Montréal, Feb 16-23 2027) — primary target, realistic timeline for 3-benchmark evaluation",
    "ICLR 2027 (expected ~Oct 2026, deadline TBD) — fallback with additional time for comprehensive experiments",
    "Note: User requested EMNLP 2026 (ARR deadline May 25, 2026), but 15-day timeline is infeasible for proposed 200+ GPU-hour experimental program. AAAI 2027 (Aug 1) provides ~12 weeks, sufficient for full evaluation including human message quality annotation."
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Latent Collaboration in Multi-Agent Systems — LatentMAS (ICML 2026 Spotlight, arXiv 2511.20639)",
    "Recursive Multi-Agent Systems — RecursiveMAS (April 2026, arXiv 2604.25917)",
    "Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems — DiffMAS (April 2026, arXiv 2604.21794)",
    "EMA Policy Gradient: Taming RL for LLMs with EMA Anchor and Top-k KL — EMA-PG (Feb 2026, arXiv 2602.04417)",
    "Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems (Feb 2026, arXiv 2602.08847)",
    "Counterfactual Credit Policy Optimization — CCPO (March 2026, arXiv 2603.21563)",
    "CoFi-PGMA: Counterfactual Policy Gradients under Filtered Feedback for Multi-Agent LLMs (April 2026, arXiv 2604.22785)",
    "C3: Contextual Counterfactual Credit Assignment for Multi-Agent RL in LLM Collaboration (March 2026, arXiv 2603.06859)",
    "Stronger-MAS: Multi-Agent Reinforcement Learning for Collaborative LLMs — AT-GRPO (ICLR 2026)",
    "LLM Collaboration with Multi-Agent Reinforcement Learning — MAGRPO (AAAI 2026)",
    "Learning to Ground Multi-Agent Communication with Autoencoders — Lin et al. (NeurIPS 2021)",
    "Language Grounded Multi-Agent Communication — LangGround (NeurIPS 2024)",
    "Thought Communication in Multiagent Collaboration — ThoughtComm (NeurIPS 2025)",
    "Why Do Multi-Agent LLM Systems Fail? (NeurIPS 2025)",
    "MAPoRL: Multi-Agent Post-Co-Training for Collaborative LLMs with RL (ACL 2025)",
    "Training Language Models for Social Deduction with Multi-Agent RL (AAMAS 2025)",
    "DEPART: Hierarchical Multi-Agent System for Multi-Turn Interaction — HIMPO (OpenReview 2025-2026)",
    "HiPER: Hierarchical RL with Explicit Credit Assignment for LLM Agents (Feb 2026, arXiv 2602.16165)",
    "Graph-GRPO: Stabilizing Multi-Agent Topology Learning via GRPO (arXiv 2026)",
    "Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems (arXiv 2025)",
    "Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces (May 2026, arXiv 2605.02801)"
  ],
  "description": "We propose Stop-Gradient Intent Reconstruction (SGIR), an auxiliary loss that provides token-differentiated supervision for text-based inter-agent communication during multi-agent GRPO training. Recent latent-communication methods (LatentMAS, ICML 2026; RecursiveMAS, April 2026; DiffMAS, April 2026) show that bypassing text for direct hidden-state or KV-cache transfer yields large gains (+14.6–26.7%), but sacrifices the interpretability, debuggability, and human interoperability of text communication. Text-based multi-agent GRPO methods (AT-GRPO, MAGRPO) and credit assignment approaches (C3, CCPO, CoFi-PGMA) optimize task reward or agent-level credit without within-message token differentiation. SGIR bridges this gap: a lightweight attention-weighted reconstruction decoder reconstructs the sender's EMA-stabilized, stop-gradient-detached intent embedding from each text message, with learned attention weights creating genuine per-token gradient differentiation—intent-carrying tokens receive stronger training signal than syntactic filler. This contrasts with naive mean-pooling which yields identical gradients for all tokens (effectively message-level supervision). The EMA target (τ=0.999) addresses the moving-target problem from continuous LoRA updates, grounded in the stability analysis of EMA-PG (Zhang & Ba, Feb 2026) which derives conditions under which EMA anchors ensure smooth policy tracking in GRPO-like training. Unlike DiffMAS which replaces text with KV-cache latent traces for maximum performance, SGIR preserves human-readable messages—using reconstruction purely as a training signal to encourage informativeness while maintaining the interpretability required for safety-critical deployment and human oversight. Architecture follows DEPART: planner and executor share base model weights (Qwen3-1.7B) with agent-specific LoRA adapters (rank=64). We evaluate on three benchmarks: (1) ALFWorld with DEPART-style planner-executor (allowed list), (2) WebArena-Lite with DEPART-style planner-executor (allowed list, 165 tasks), and (3) Sokoban 6x6 from Stronger-MAS (community standard with published AT-GRPO baselines for controlled comparison). A qualitative human evaluation of planner message quality in ALFWorld directly demonstrates the interpretability advantage motivating text preservation. Four ablations test: (1) stop-gradient necessity at LLM scale, (2) EMA τ informed by EMA-PG stability theory, (3) λ annealing schedule, (4) attention-weighted vs. mean vs. max pooling (testing whether token differentiation provides genuine benefit). A composability experiment combines SGIR with Dr. MAS agent-wise normalization. Estimated compute: ≤250 H100-hours ($500-750). Targets AAAI 2027 (Aug 1, 2026 deadline), providing 12 weeks for full experimental program including human annotation.",
  "project_name": "recon_reg_comm_training",
  "source": "web_research"
}

## Reviewer feedback (round 4)
Issues: ["MISSING CITATION — MASIA (NeurIPS 2022): 'Efficient Multi-agent Communication via Self-supervised Information Aggregation' (Guan et al.) uses reconstruction loss (reconstructing global state from messages) combined with attention-based message extraction in multi-agent communication. This is a direct precursor combining two of SGIR's core components (reconstruction + attention aggregation) and must be cited and differentiated.", "OVERSTATED ATTENTION POOLING NOVELTY: The attention-weighted pooling mechanism (α_j = softmax(v^T·tanh(W·h_j+b))) is the standard Hierarchical Attention Network formula from Yang et al. (NAACL 2016) and Lin et al. (ICLR 2017). Framing it as 'genuine per-token gradient differentiation' obscures that this is a trivially standard architectural choice. The gradient analysis also omits the softmax Jacobian redistribution term (∂α_k/∂h_j contributions), making the mechanism appear cleaner than it actually is.", "MISSING CONCURRENT WORK — Interlat (arXiv 2511.09149, revised April 2026): 'Enabling Agents to Communicate Entirely in Latent Space' by Du et al. proposes inter-agent communication via continuous last hidden states with learned compression. This is another latent communication method that should be in the landscape for completeness.", "NARROW NOVELTY GAP: The contribution reduces to 'apply stop-gradient + EMA to make reconstruction work at LLM scale' — the attention pooling is standard, the reconstruction idea is from Lin et al. 2021, and the EMA design is borrowed from EMA-PG. Each 'challenge' at LLM scale is addressed by a known technique. This risks the 'engineering combination' critique at top venues where reviewers expect conceptual novelty.", "UNCERTAIN EMPIRICAL IMPACT: No preliminary evidence suggests reconstruction can meaningfully close the text-latent performance gap. If LatentMAS achieves +14.6% by bypassing text and SGIR achieves +2-3% while preserving text, the contribution becomes 'we traded most of the performance for interpretability' — which may not be compelling without a strong interpretability analysis showing concrete debugging/safety benefits.", "VENUE DEVIATION PERSISTS: User requested EMNLP 2026 (ARR May 25). Proposal targets AAAI 2027 (Aug 1). While acknowledged and justified, this still does not meet the user's stated constraint."]
Feedback: The proposal has improved substantially over 4 rounds — landscape is now comprehensive, references are verified, benchmark compliance is mostly addressed, and the technical mechanism is clarified. Three specific actions to reach pass quality:

1. **Cite MASIA (NeurIPS 2022) and reframe the novelty narrative**: MASIA already combines reconstruction + attention for multi-agent communication messages. Your differentiation: MASIA reconstructs *global state* from messages in small MARL; SGIR reconstructs *sender intent embeddings* from messages at *LLM scale* with *stop-gradient + EMA* to handle LoRA-induced moving targets. The novelty is NOT attention pooling (standard since 2016) — it's the full architectural framework (stop-gradient isolation + EMA stabilization + λ annealing) that makes reconstruction work in the LLM-GRPO setting where naive approaches fail.

2. **Strengthen the impact argument with concrete interpretability value**: The 'preserve text for interpretability' argument is currently abstract. Make it concrete: (a) include a failure-mode analysis showing how SGIR-trained messages help debug agent errors that latent communication cannot, (b) show that SGIR attention weights identify which tokens carry intent (a free interpretability tool), (c) demonstrate human-in-the-loop intervention scenarios where text messages enable real-time correction. This converts the interpretability claim from a philosophical argument into a demonstrated advantage.

3. **Consider a direct text-vs-latent comparison**: On one benchmark (e.g., ALFWorld), run both LatentMAS (training-free, so cheap to evaluate) and SGIR. If SGIR achieves 70-80% of LatentMAS's gains while preserving readable messages, that's a compelling result. If it achieves only 10-20%, you need the interpretability argument to be ironclad. Having this comparison in hand before writing would let you frame the contribution appropriately.

Minor: fix the gradient analysis to acknowledge the softmax Jacobian term, or simply state 'the dominant gradient term is α_j-weighted' without claiming strict proportionality.

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
这个 idea 已经经过 4 轮修订，近 3 轮的平均分从 3.2 到 3.5，没有明显改善。

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
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "type": "user",
  "uuid": "80b3b1f4-7737-49e3-a10f-67935a2af03f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T20:42:09.792Z_

```json
{
  "parentUuid": "80b3b1f4-7737-49e3-a10f-67935a2af03f",
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
  "uuid": "e900fab2-4b7c-4e49-bd46-2d8870bbf329",
  "timestamp": "2026-05-10T20:42:09.792Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T20:42:09.792Z_

```json
{
  "parentUuid": "e900fab2-4b7c-4e49-bd46-2d8870bbf329",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4bc0878c-0bd3-405d-9fad-cd2ac4914453",
  "timestamp": "2026-05-10T20:42:09.792Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Stop-Gradient Intent Reconstruction with Attention-Weighted Pooling fo…",
  "leafUuid": "4bc0878c-0bd3-405d-9fad-cd2ac4914453",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising Stop-Gradient Intent Reconstruction for text-based multi-agent communication",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b"
}
```

---

### Assistant

_source line 8 · 2026-05-10T20:43:12.232Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the reviewer feedback and the current state of this research idea. The reviewers have raised several important issues:

1. **Missing MASIA citation** - A NeurIPS 2022 paper that combines reconstruction + attention for multi-agent communication
2. **Overstated attention pooling novelty** - It's standard HAN formula from 2016
3. **Missing Interlat** - Another latent communication method
4. **Narrow novelty gap** - Just engineering combination of known techniques
5. **Uncertain empirical impact** - No evidence reconstruction can close text-latent gap


6. **Venue deviation** - User wanted EMNLP 2026, proposal targets AAAI 2027

The stagnation pattern across four review cycles with scores hovering around 3.2-3.5 suggests I need to confront whether this has deeper structural problems. The "narrow novelty gap" critique cuts to the heart of it—the contribution is essentially stacking existing components: reconstruction loss from prior work, standard attention pooling from 2016, stop-gradient and EMA techniques, all applied to LLM-scale GRPO. Without clear empirical evidence that reconstruction actually bridges the text-latent gap, this feels more like engineering than a meaningful advance.

The empirical results aren't helping either. If SGIR only achieves 2-3% improvement while latent methods show 14-26%, that's a hard sell at top venues. And MASIA's existing combination of reconstruction with attention for multi-agent communication makes the novelty claim even thinner. At this point, I'm facing a real choice: patch it with better framing and citations, fundamentally redesign the approach while keeping the core problem, or step back and find a different angle on interpretable multi-agent communication. The underlying tension—that latent methods are powerful but opaque while text methods are interpretable but weak—is genuinely interesting, but I haven't cracked how to actually solve it.

Rather than just bolting on a reconstruction loss like SGIR does, I should think differently about improving text communication. Distillation from latent to text methods is actually compelling—using latent communication as a teacher to show what effective messages look like in text form directly addresses the opacity-versus-interpretability gap. That feels like a real contribution rather than an incremental tweak.

But the reviewer's feedback is more actionable than I initially thought. They're not saying the work is fundamentally flawed—they're pointing to three concrete fixes: properly situate the novelty within the full LLM-GRPO framework rather than just attention pooling, demonstrate interpretability through specific failure cases, and add a direct empirical comparison between text and latent communication. These feel achievable and the reviewer seems to think the paper can pass with these changes.

That said, the stagnation pattern across three rounds is a real warning sign. I'm torn between following their specific suggestions versus attempting a more fundamental reframing that shifts away from reconstruction entirely and toward something with clearer conceptual novelty. The core problem—training text communication quality in multi-agent LLM systems—is genuinely important and unaddressed, but I need to figure out if reconstruction is actually the right solution or if there's a stronger approach I'm missing.

I'm exploring alternative framings like using the receiver's hidden state changes as a direct measure of message informativeness, which would ground the approach in communication pragmatics rather than reconstruction. But as I work through these ideas, I keep circling back to existing work—MAPoRL's influence-aware verification, SGIR's receiver-side reconstruction—which suggests I haven't quite found the novel angle yet.

The real bottleneck is that text communication in multi-agent LLM systems is fundamentally lossy compared to latent state sharing, and adding reconstruction pressure only partially addresses this. Rather than trying to close that gap, what if I focus on enriching the text channel itself—using structured formats like JSON or learned protocols that remain human-readable while being more information-dense?

But stepping back, I need to think about what would actually strengthen the paper for publication. I'm weighing three paths: doubling down on SGIR with the reviewer's specific feedback, pivoting to latent-to-text distillation where latent methods teach text communication, or optimizing the communication protocols themselves. The first option feels achievable with strong execution since the reviewer gave concrete steps, though I'm concerned about whether that's enough to overcome the sense that it's just combining existing techniques.

What if I introduce something genuinely novel instead—a contrastive intent alignment approach where messages are trained not just to reconstruct the sender's intent but to discriminatively distinguish it from other agents' intents and the same agent's past states? This reframes the problem with clearer information-theoretic grounding and gives the attention mechanism natural token-level gradients, moving beyond simple reconstruction loss.

Before committing to this direction, I should verify whether contrastive methods have already been explored in multi-agent communication and check what the current state-of-the-art looks like on the relevant benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bc0878c-0bd3-405d-9fad-cd2ac4914453",
  "isSidechain": false,
  "requestId": "req_011CauY8CBURA1eRXkreGBBP",
  "type": "assistant",
  "uuid": "b97bddb2-7c21-460e-92d9-73c2edfae890",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1hB7PRbhXNXMRxXukAKzM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12839,
      "cache_read_input_tokens": 11804,
      "output_tokens": 2620,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2620,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 12839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12839
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-10T20:43:12.687Z_

I'll start by deeply researching the reviewer's specific concerns before deciding on the revision strategy. Let me investigate MASIA, Interlat, and the novelty gap issue in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b97bddb2-7c21-460e-92d9-73c2edfae890",
  "isSidechain": false,
  "requestId": "req_011CauY8CBURA1eRXkreGBBP",
  "type": "assistant",
  "uuid": "06ed6604-e1f2-4592-878e-10ff3230e68b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1hB7PRbhXNXMRxXukAKzM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12839,
      "cache_read_input_tokens": 11804,
      "output_tokens": 2620,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2620,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 12839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12839
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T20:43:21.392Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DMc5VaykHy4Z47KPr9cTeE`</summary>

```json
{
  "description": "Research MASIA NeurIPS 2022",
  "prompt": "I need to deeply understand the MASIA paper from NeurIPS 2022: \"Efficient Multi-agent Communication via Self-supervised Information Aggregation\" by Guan et al. \n\nPlease:\n1. Use WebSearch to find this paper (try: \"MASIA NeurIPS 2022 self-supervised information aggregation multi-agent communication\" and \"MASIA Guan multi-agent reconstruction attention\")\n2. Use WebFetch to read the paper's abstract and method section from arXiv or the conference page\n3. Specifically identify:\n   - What reconstruction loss do they use? (Do they reconstruct global state? Local observations? Something else?)\n   - What attention mechanism do they use for message aggregation?\n   - How do these relate to: (a) reconstruction of sender intent from messages, (b) attention-weighted pooling of message tokens\n   - What is their experimental setting? (small MARL with discrete/continuous state spaces? LLM-scale?)\n\nI'm trying to understand how similar MASIA is to a proposed method called SGIR that uses reconstruction loss + attention-weighted pooling for LLM-scale multi-agent communication in GRPO training. The reviewer claims MASIA is a \"direct precursor combining two of SGIR's core components.\"\n\nReport your findings in detail - I need the specifics to properly differentiate.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06ed6604-e1f2-4592-878e-10ff3230e68b",
  "isSidechain": false,
  "requestId": "req_011CauY8CBURA1eRXkreGBBP",
  "type": "assistant",
  "uuid": "dafb64ce-5f8a-4855-8048-ba7228a7db2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1hB7PRbhXNXMRxXukAKzM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12839,
      "cache_read_input_tokens": 11804,
      "output_tokens": 2620,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2620,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 12839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12839
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T20:48:24.244Z_

<details><summary>↩ Tool result · `toolu_01DMc5VaykHy4Z47KPr9cTeE`</summary>

````text
I now have all the information I need. Here is my comprehensive analysis:

---

## MASIA: Detailed Technical Analysis

**Paper**: "Efficient Multi-agent Communication via Self-supervised Information Aggregation" by Cong Guan, Feng Chen, Lei Yuan, Chenghe Wang, Hao Yin, Zongzhang Zhang, Yang Yu. NeurIPS 2022.

---

### 1. Reconstruction Loss: What Is Reconstructed?

MASIA uses **global environment state reconstruction**, not reconstruction of sender intent, local observations, or messages. Specifically:

- The **Information Aggregation Encoder (IAE)** takes as input the **individual observations of all agents** (which serve as "messages" in their broadcast communication setting). It encodes them into a shared latent representation `z`.
- A **decoder** then attempts to reconstruct the **global environment state** `s_t` from this latent `z`.
- The reconstruction loss is **MSE (mean squared error)**:
  ```python
  recons_loss = torch.mean((recons - output) ** 2, dim=-1)
  ```
  where `output` corresponds to the global state `states` from the environment.

In the learner code (`masia_learner.py`), this is computed as:
```python
loss_dict = self.mac.agent.encoder.loss_function(
    recons.reshape(bs*seq_len, -1),
    states.reshape(bs*seq_len, -1)   # <-- global state is the target
)
```

There is also a **VAE variant** (`ob_vae.py`) that adds KL divergence to the reconstruction loss, but the default configuration (`masia.yaml`) uses the `ob_attn_ae` encoder (observation-attention autoencoder) which uses only MSE reconstruction, not KL.

**Critical distinction from SGIR**: MASIA reconstructs the *environment's global state* -- a fixed ground-truth vector available in the simulator. It does NOT reconstruct "sender intent" or any latent communicative goal. This is a fundamentally different reconstruction target.

---

### 2. Attention Mechanism for Message Aggregation

MASIA uses **single-head scaled dot-product self-attention** over agent observations:

```python
energy = torch.bmm(query, key / (attn_dim ** (1/2)))
score = F.softmax(energy, dim=-1)
attn_out = torch.bmm(score, value)
```

Where:
- Query, Key, Value are all linear projections of the individual agent observations
- Attention is computed across the **agent dimension** (each agent attends to all agents' observations)
- The attention output is then passed through an MLP to produce a latent representation

**The attention is NOT used for "message extraction/weighting"** in the way one might expect. Instead:
- The attention produces a shared aggregated representation (common across agents)
- A separate **gating mechanism** (`sigmoid(gate(inputs))`) then weights the aggregated representation per-agent for individual decision-making:
  ```python
  weighted = F.sigmoid(self.gate(inputs))  # per-agent gate
  # element-wise multiplication with latent representation
  ```

**Critical distinction from SGIR**: MASIA's attention operates over raw observations of homogeneous MARL agents (all observations are same-shaped vectors). It is NOT attention-weighted pooling of heterogeneous message tokens as would occur in an LLM communication setting. The "messages" in MASIA are simply agent observations being broadcast, not learned discrete/continuous message vectors, and certainly not natural language tokens.

---

### 3. Additional Self-Supervised Objectives

Beyond reconstruction, MASIA has two more self-supervised losses:

**a) Multi-step prediction loss (SPR)**: A latent forward model predicts future latent states:
```python
spr_loss = F.mse_loss(pred_f, target_f, reduction="none").sum(-1)
```
This uses a momentum-updated target encoder and 2-step prediction horizon.

**b) Reward prediction loss**:
```python
rew_loss = F.mse_loss(pred_rew, env_rew, reduction="none").sum(-1)
```

The total loss combines all components:
```python
repr_loss = masked_vae_loss + spr_coef * tot_spr_loss + rew_pred_coef * tot_rew_loss
tot_loss = rl_loss + repr_coef * repr_loss
```

---

### 4. Experimental Setting

MASIA operates in **small-scale cooperative MARL with discrete action spaces**:

- **Environments**: Hallway, Traffic Junction, Level-Based Foraging (LBF), StarCraft Multi-Agent Challenge (SMAC/SMACv2)
- **Agent counts**: Typically 2-27 agents (e.g., `5m_vs_6m`, `27m_vs_30m`, `MMM2`)
- **State/action spaces**: Low-dimensional continuous state vectors (tens to hundreds of dimensions), discrete actions
- **RL algorithm**: QMIX (value decomposition) with epsilon-greedy exploration
- **Communication**: Full broadcast -- every agent's observation is shared with every other agent. There is no learned message generation; agents simply share their raw observations.
- **Scale**: This is decidedly NOT LLM-scale. The "messages" are fixed-dimension numeric vectors (observation vectors), not natural language. Networks are small MLPs/GRUs. The setting involves 2-27 homogeneous agents in simulated game environments.

The paper also introduced offline MARL communication benchmarks, which was novel at the time.

---

### 5. How Similar Is MASIA to the Proposed SGIR?

Based on the technical details, here are the key differentiators you can use:

| Dimension | MASIA | SGIR (as described) |
|-----------|-------|---------------------|
| **Reconstruction target** | Global environment state (ground-truth simulator state) | Sender intent (latent communicative goal) |
| **What "messages" are** | Raw observation vectors broadcast to all agents | Natural language or token-level communications between LLM agents |
| **Attention purpose** | Self-attention over agent observations to produce shared representation | Attention-weighted pooling of message tokens for selective aggregation |
| **Scale** | 2-27 homogeneous MARL agents, small MLPs/GRUs | LLM-scale multi-agent communication |
| **Training paradigm** | Value decomposition RL (QMIX) + self-supervised auxiliary losses | GRPO training |
| **Communication model** | Full broadcast of raw observations (no learned messages) | Learned natural language communication |
| **Permutation invariance** | Claimed but not truly achieved in code (concatenation of per-agent latents preserves ordering) | Presumably different architecture |
| **Additional objectives** | Multi-step latent prediction + reward prediction | Different |

**Assessment of the reviewer's claim**: Saying MASIA is a "direct precursor combining two of SGIR's core components" is an overstatement. While MASIA does use (a) a reconstruction loss and (b) attention over messages, the *specific instantiation* of both is fundamentally different:

1. Reconstructing a ground-truth global state vector from observations is conceptually and technically different from reconstructing sender intent from natural language messages. The former is a state estimation problem; the latter is a communication grounding problem.

2. Self-attention over homogeneous fixed-dimensional observation vectors in a 5-agent SMAC game is fundamentally different from attention-weighted pooling of variable-length token sequences in LLM-scale multi-agent GRPO.

MASIA is a reasonable **related work** to cite and discuss, but calling it a "direct precursor" conflates the surface-level presence of "reconstruction + attention" with the deep architectural and conceptual differences in what is reconstructed, what is attended to, and at what scale.

---

Sources:
- [MASIA NeurIPS 2022 Paper (PDF)](https://proceedings.neurips.cc/paper_files/paper/2022/file/075b2875e2b671ddd74aeec0ac9f0357-Paper-Conference.pdf)
- [MASIA NeurIPS 2022 Abstract Page](https://papers.nips.cc/paper_files/paper/2022/hash/075b2875e2b671ddd74aeec0ac9f0357-Abstract-Conference.html)
- [MASIA OpenReview](https://openreview.net/forum?id=n4wnZAdBavx)
- [MASIA arXiv (extended version)](https://arxiv.org/abs/2302.09605)
- [MASIA GitHub Repository](https://github.com/chenf-ai/MASIA)
- [M2I2 Paper (cites MASIA)](https://arxiv.org/html/2501.00312)
- [MACTAS Paper (compares to MASIA)](https://arxiv.org/html/2508.13661)

agentId: a3ea8a30fc83798ba (use SendMessage with to: 'a3ea8a30fc83798ba' to continue this agent)
&lt;usage>total_tokens: 36644
tool_uses: 36
duration_ms: 302845&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "dafb64ce-5f8a-4855-8048-ba7228a7db2d",
  "isSidechain": false,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "type": "user",
  "uuid": "3e99c4fa-a808-4688-9356-261b28959fe0",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to deeply understand the MASIA paper from NeurIPS 2022: \"Efficient Multi-agent Communication via Self-supervised Information Aggregation\" by Guan et al. \n\nPlease:\n1. Use WebSearch to find this paper (try: \"MASIA NeurIPS 2022 self-supervised information aggregation multi-agent communication\" and \"MASIA Guan multi-agent reconstruction attention\")\n2. Use WebFetch to read the paper's abstract and method section from arXiv or the conference page\n3. Specifically identify:\n   - What reconstruction loss do they use? (Do they reconstruct global state? Local observations? Something else?)\n   - What attention mechanism do they use for message aggregation?\n   - How do these relate to: (a) reconstruction of sender intent from messages, (b) attention-weighted pooling of message tokens\n   - What is their experimental setting? (small MARL with discrete/continuous state spaces? LLM-scale?)\n\nI'm trying to understand how similar MASIA is to a proposed method called SGIR that uses reconstruction loss + attention-weighted pooling for LLM-scale multi-agent communication in GRPO training. The reviewer claims MASIA is a \"direct precursor combining two of SGIR's core components.\"\n\nReport your findings in detail - I need the specifics to properly differentiate.",
    "agentId": "a3ea8a30fc83798ba",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information I need. Here is my comprehensive analysis:\n\n---\n\n## MASIA: Detailed Technical Analysis\n\n**Paper**: \"Efficient Multi-agent Communication via Self-supervised Information Aggregation\" by Cong Guan, Feng Chen, Lei Yuan, Chenghe Wang, Hao Yin, Zongzhang Zhang, Yang Yu. NeurIPS 2022.\n\n---\n\n### 1. Reconstruction Loss: What Is Reconstructed?\n\nMASIA uses **global environment state reconstruction**, not reconstruction of sender intent, local observations, or messages. Specifically:\n\n- The **Information Aggregation Encoder (IAE)** takes as input the **individual observations of all agents** (which serve as \"messages\" in their broadcast communication setting). It encodes them into a shared latent representation `z`.\n- A **decoder** then attempts to reconstruct the **global environment state** `s_t` from this latent `z`.\n- The reconstruction loss is **MSE (mean squared error)**:\n  ```python\n  recons_loss = torch.mean((recons - output) ** 2, dim=-1)\n  ```\n  where `output` corresponds to the global state `states` from the environment.\n\nIn the learner code (`masia_learner.py`), this is computed as:\n```python\nloss_dict = self.mac.agent.encoder.loss_function(\n    recons.reshape(bs*seq_len, -1),\n    states.reshape(bs*seq_len, -1)   # <-- global state is the target\n)\n```\n\nThere is also a **VAE variant** (`ob_vae.py`) that adds KL divergence to the reconstruction loss, but the default configuration (`masia.yaml`) uses the `ob_attn_ae` encoder (observation-attention autoencoder) which uses only MSE reconstruction, not KL.\n\n**Critical distinction from SGIR**: MASIA reconstructs the *environment's global state* -- a fixed ground-truth vector available in the simulator. It does NOT reconstruct \"sender intent\" or any latent communicative goal. This is a fundamentally different reconstruction target.\n\n---\n\n### 2. Attention Mechanism for Message Aggregation\n\nMASIA uses **single-head scaled dot-product self-attention** over agent observations:\n\n```python\nenergy = torch.bmm(query, key / (attn_dim ** (1/2)))\nscore = F.softmax(energy, dim=-1)\nattn_out = torch.bmm(score, value)\n```\n\nWhere:\n- Query, Key, Value are all linear projections of the individual agent observations\n- Attention is computed across the **agent dimension** (each agent attends to all agents' observations)\n- The attention output is then passed through an MLP to produce a latent representation\n\n**The attention is NOT used for \"message extraction/weighting\"** in the way one might expect. Instead:\n- The attention produces a shared aggregated representation (common across agents)\n- A separate **gating mechanism** (`sigmoid(gate(inputs))`) then weights the aggregated representation per-agent for individual decision-making:\n  ```python\n  weighted = F.sigmoid(self.gate(inputs))  # per-agent gate\n  # element-wise multiplication with latent representation\n  ```\n\n**Critical distinction from SGIR**: MASIA's attention operates over raw observations of homogeneous MARL agents (all observations are same-shaped vectors). It is NOT attention-weighted pooling of heterogeneous message tokens as would occur in an LLM communication setting. The \"messages\" in MASIA are simply agent observations being broadcast, not learned discrete/continuous message vectors, and certainly not natural language tokens.\n\n---\n\n### 3. Additional Self-Supervised Objectives\n\nBeyond reconstruction, MASIA has two more self-supervised losses:\n\n**a) Multi-step prediction loss (SPR)**: A latent forward model predicts future latent states:\n```python\nspr_loss = F.mse_loss(pred_f, target_f, reduction=\"none\").sum(-1)\n```\nThis uses a momentum-updated target encoder and 2-step prediction horizon.\n\n**b) Reward prediction loss**:\n```python\nrew_loss = F.mse_loss(pred_rew, env_rew, reduction=\"none\").sum(-1)\n```\n\nThe total loss combines all components:\n```python\nrepr_loss = masked_vae_loss + spr_coef * tot_spr_loss + rew_pred_coef * tot_rew_loss\ntot_loss = rl_loss + repr_coef * repr_loss\n```\n\n---\n\n### 4. Experimental Setting\n\nMASIA operates in **small-scale cooperative MARL with discrete action spaces**:\n\n- **Environments**: Hallway, Traffic Junction, Level-Based Foraging (LBF), StarCraft Multi-Agent Challenge (SMAC/SMACv2)\n- **Agent counts**: Typically 2-27 agents (e.g., `5m_vs_6m`, `27m_vs_30m`, `MMM2`)\n- **State/action spaces**: Low-dimensional continuous state vectors (tens to hundreds of dimensions), discrete actions\n- **RL algorithm**: QMIX (value decomposition) with epsilon-greedy exploration\n- **Communication**: Full broadcast -- every agent's observation is shared with every other agent. There is no learned message generation; agents simply share their raw observations.\n- **Scale**: This is decidedly NOT LLM-scale. The \"messages\" are fixed-dimension numeric vectors (observation vectors), not natural language. Networks are small MLPs/GRUs. The setting involves 2-27 homogeneous agents in simulated game environments.\n\nThe paper also introduced offline MARL communication benchmarks, which was novel at the time.\n\n---\n\n### 5. How Similar Is MASIA to the Proposed SGIR?\n\nBased on the technical details, here are the key differentiators you can use:\n\n| Dimension | MASIA | SGIR (as described) |\n|-----------|-------|---------------------|\n| **Reconstruction target** | Global environment state (ground-truth simulator state) | Sender intent (latent communicative goal) |\n| **What \"messages\" are** | Raw observation vectors broadcast to all agents | Natural language or token-level communications between LLM agents |\n| **Attention purpose** | Self-attention over agent observations to produce shared representation | Attention-weighted pooling of message tokens for selective aggregation |\n| **Scale** | 2-27 homogeneous MARL agents, small MLPs/GRUs | LLM-scale multi-agent communication |\n| **Training paradigm** | Value decomposition RL (QMIX) + self-supervised auxiliary losses | GRPO training |\n| **Communication model** | Full broadcast of raw observations (no learned messages) | Learned natural language communication |\n| **Permutation invariance** | Claimed but not truly achieved in code (concatenation of per-agent latents preserves ordering) | Presumably different architecture |\n| **Additional objectives** | Multi-step latent prediction + reward prediction | Different |\n\n**Assessment of the reviewer's claim**: Saying MASIA is a \"direct precursor combining two of SGIR's core components\" is an overstatement. While MASIA does use (a) a reconstruction loss and (b) attention over messages, the *specific instantiation* of both is fundamentally different:\n\n1. Reconstructing a ground-truth global state vector from observations is conceptually and technically different from reconstructing sender intent from natural language messages. The former is a state estimation problem; the latter is a communication grounding problem.\n\n2. Self-attention over homogeneous fixed-dimensional observation vectors in a 5-agent SMAC game is fundamentally different from attention-weighted pooling of variable-length token sequences in LLM-scale multi-agent GRPO.\n\nMASIA is a reasonable **related work** to cite and discuss, but calling it a \"direct precursor\" conflates the surface-level presence of \"reconstruction + attention\" with the deep architectural and conceptual differences in what is reconstructed, what is attended to, and at what scale.\n\n---\n\nSources:\n- [MASIA NeurIPS 2022 Paper (PDF)](https://proceedings.neurips.cc/paper_files/paper/2022/file/075b2875e2b671ddd74aeec0ac9f0357-Paper-Conference.pdf)\n- [MASIA NeurIPS 2022 Abstract Page](https://papers.nips.cc/paper_files/paper/2022/hash/075b2875e2b671ddd74aeec0ac9f0357-Abstract-Conference.html)\n- [MASIA OpenReview](https://openreview.net/forum?id=n4wnZAdBavx)\n- [MASIA arXiv (extended version)](https://arxiv.org/abs/2302.09605)\n- [MASIA GitHub Repository](https://github.com/chenf-ai/MASIA)\n- [M2I2 Paper (cites MASIA)](https://arxiv.org/html/2501.00312)\n- [MACTAS Paper (compares to MASIA)](https://arxiv.org/html/2508.13661)"
      }
    ],
    "totalDurationMs": 302845,
    "totalTokens": 36644,
    "totalToolUseCount": 36,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 848,
      "cache_read_input_tokens": 33629,
      "output_tokens": 2166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 848
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2166,
          "cache_read_input_tokens": 33629,
          "cache_creation_input_tokens": 848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 848,
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
      "otherToolCount": 36
    }
  },
  "sourceToolAssistantUUID": "dafb64ce-5f8a-4855-8048-ba7228a7db2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Stop-Gradient Intent Reconstruction with Attention-Weighted Pooling fo…",
  "leafUuid": "3e99c4fa-a808-4688-9356-261b28959fe0",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising Stop-Gradient Intent Reconstruction for text-based multi-agent communication",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b"
}
```

---

### Tool call

_source line 14 · 2026-05-10T20:48:34.469Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016Wi41Vb9ryJ2vEcYKSVtpy`</summary>

```json
{
  "description": "Research Interlat paper",
  "prompt": "I need to understand the Interlat paper: \"Enabling Agents to Communicate Entirely in Latent Space\" by Du et al., arXiv 2511.09149 (revised April 2026).\n\nPlease:\n1. Use WebSearch to find this paper (try: \"Interlat arXiv 2511.09149 Du agents communicate latent space\" and \"enabling agents communicate entirely latent space\")\n2. Use WebFetch to read the paper from arXiv (https://arxiv.org/abs/2511.09149)\n3. Identify:\n   - What is their core mechanism for inter-agent latent communication?\n   - How do they compress/transfer hidden states between agents?\n   - How does this compare to LatentMAS (shared working memory of last-layer embeddings), RecursiveMAS (RecursiveLink modules), and DiffMAS (KV-cache trace construction)?\n   - What benchmarks do they evaluate on and what results do they achieve?\n   - Was it revised in April 2026? What changed?\n\nI need this for a research landscape analysis of latent vs text communication methods in multi-agent LLM systems. Report in detail.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e99c4fa-a808-4688-9356-261b28959fe0",
  "isSidechain": false,
  "requestId": "req_011CauYbnqK9FmQxqSgYs8ha",
  "type": "assistant",
  "uuid": "bfbd4440-8ebe-4e70-9e8e-881ec025ab92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDUyZbhGtfsg8mov1emgwW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4859,
      "cache_read_input_tokens": 24643,
      "output_tokens": 368,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4859,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 368,
          "cache_read_input_tokens": 24643,
          "cache_creation_input_tokens": 4859,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4859
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T20:51:37.216Z_

<details><summary>↩ Tool result · `toolu_016Wi41Vb9ryJ2vEcYKSVtpy`</summary>

```text
I now have comprehensive information. Here is the detailed report.

---

## Interlat: "Enabling Agents to Communicate Entirely in Latent Space" (Du et al., arXiv 2511.09149)

### Paper Metadata
- **Authors:** Zhuoyun Du, Runze Wang, Huiyu Bai, Zouying Cao, Xiaoyong Zhu, Yu Cheng, Bo Zheng, Wei Chen, Haochao Ying
- **Submitted:** November 12, 2025 (v1)
- **Latest revision:** v4, April 16, 2026
- **Venue claim:** The arXiv abstract page states "Accepted to ACL 2026," though the ACL 2026 accepted papers list has not yet been published (it says "Coming soon!"). The OpenReview submission (rmYbgsehTd) shows status "Withdrawn Submission," suggesting the paper may have been withdrawn from one venue (e.g., an ARR cycle) and submitted/accepted elsewhere.

---

### 1. Core Mechanism for Inter-Agent Latent Communication

Interlat replaces natural-language message-passing between agents with **direct transmission of last-layer hidden states**.

**How it works step by step:**

1. **Hidden state extraction:** When an agent generates a response, the system collects the last-layer hidden state **h_l in R^d** from the transformer at each token position (immediately before predicting the next token). These are assembled into a matrix **H in R^(L x d)** where L is the sequence length.

2. **Transmission:** Special boundary tokens `&lt;bop>` (beginning of plan) and `&lt;eop>` (end of plan) demarcate the latent message region. The receiving agent's input becomes: `[e(x_1), ..., e(x_i), h_1, h_2, ..., h_L, e(x_j)]` -- i.e., continuous hidden-state vectors are spliced directly into the embedding sequence in place of discrete token embeddings.

3. **Communication adapter:** A **trainable lightweight self-attention layer + projection layer** sits at the receiver. This adapter rescales and reinterprets the incoming latent states before the receiving model processes them. This is what enables cross-architecture communication.

4. **No parameter sharing or memory coupling required** -- the adapter provides sufficient bridging that latent semantics transfer even across model families.

---

### 2. Compression / Transfer of Hidden States

Interlat includes a dedicated **compression module** for reducing latent message length:

- **Architecture:** A separate reasoning model M_phi generates compact latent messages **H_K in R^(K x d)** where K is much smaller than L. It works by **autoregressive reasoning entirely in latent space** -- feeding its own last hidden state back as the next input embedding through a lightweight projection: `M_phi(E_i) -> h_i, E_{i+1} = E_i + Proj(h_i)`.

- **Compression ratio:** Full messages of 128 latent tokens can be compressed to as few as **8 tokens** while maintaining competitive performance, achieving up to **24x reduction in communication latency** (from 9.19s to 0.39s).

- **Training loss (three components):**
  - **Task loss (L_task):** Cross-entropy ensuring downstream utility of compressed messages.
  - **Preference loss (L_pref):** Uncertainty-weighted KL divergence aligning compressed and full behaviors at positions where latents reduce uncertainty.
  - **Geometry loss (L_geom):** Cosine similarity maintaining directional alignment between compressed and full representations: `L_geom = 1 - cos(z_bar^A, z_bar^D)`.

**Actor training** also uses a multi-component loss: `L_total = L_task + lambda_S * L_sep + lambda_A * L_align`, where:
- **Conditional thought separation (L_sep):** Minimizes weighted Jensen-Shannon divergence between matched and mismatched latent inputs, ensuring the receiver distinguishes relevant from irrelevant latent messages.
- **Plan-aligned regulation (L_align):** Regularizes against language-space plans to prevent exploiting the separation objective.
- A **token-to-latent curriculum** stochastically replaces early communication positions with corresponding plan token embeddings (replacement rate r in {0, 0.1, ..., 1.0}).

---

### 3. Benchmarks and Results

**ALFWorld (embodied household tasks):**

| Model Config | Seen (%) | Unseen (%) | Steps (Succ/All) |
|---|---|---|---|
| Interlat (Qwen2.5-7B) | **70.48** | **65.42** | 9.41 / 12.54 |
| Text CoT (fine-tuned) | 64.29 | 62.44 | 8.76 / 12.77 |
| No Communication | 62.14 | 62.19 | 10.19 / 13.90 |
| CoT (full) | 67.14 | 64.93 | 8.15 / 12.04 |

Consistent gains across three backbones (Qwen2.5-7B, Qwen2.5-0.5B, LLaMA3.1-8B).

**MATH benchmark:**

| Method | Overall | Level-3 | Level-4 | Level-5 |
|---|---|---|---|---|
| Interlat | 36.88% | 40.08% | 27.45% | **15.80%** |
| CoT (full) | 38.35% | 45.65% | 31.19% | 15.05% |
| Text | 34.35% | 37.60% | 26.30% | 14.20% |

Interlat surpasses CoT specifically on the hardest Level-5 problems.

**Compression results (Qwen2.5-7B, ALFWorld):**

| Latent Length | Seen (%) | Unseen (%) | Latency |
|---|---|---|---|
| Full (128) | 68.10 | 62.94 | 2.25s |
| 64 | 67.14 | 61.94 | 1.16s |
| 8 | 66.43 | 60.45 | 0.20s |

**Heterogeneous model results:** Feeding Qwen-derived latents to train a LLaMA actor yielded **70.95% seen / 71.39% unseen** -- actually slightly better than homogeneous Qwen-to-Qwen, demonstrating cross-family latent transfer works.

---

### 4. Comparison to LatentMAS, RecursiveMAS, and DiffMAS (OBF)

Interlat does **not** directly cite or compare against LatentMAS, RecursiveMAS, or DiffMAS. These are all contemporaneous works (late 2025 / early 2026). Here is a structured comparison based on my research:

| Dimension | **Interlat** | **LatentMAS** | **RecursiveMAS** | **DiffMAS/OBF** |
|---|---|---|---|---|
| **Venue** | ACL 2026 (claimed) | ICML 2026 Spotlight | -- | arXiv Apr 2026 |
| **What is transmitted** | Last-layer hidden states (full sequence) | Last-layer hidden embeddings via shared working memory | Last-layer hidden states via RecursiveLink module | Compressed KV-cache with orthogonal residual backfill |
| **Training required?** | Yes (adapter + compression module) | **Training-free** | Yes (lightweight RecursiveLink, 2-layer residual module) | Yes (eviction-style compression) |
| **Compression** | Autoregressive latent-space reasoning; down to 8 tokens (24x speedup) | No explicit compression -- full latent thoughts shared | Implicit via RecursiveLink projection | Orthogonal Backfill (OBF): 79.8-89.4% KV-cache reduction |
| **Cross-architecture** | Yes, via communication adapter (Qwen -> LLaMA demonstrated) | Not emphasized | Yes, outer link handles different hidden dimensions | Not specified |
| **Memory mechanism** | Direct injection into embedding sequence | Shared latent working memory pool | Recursive loop: agents chain via inner/outer links | KV-cache relay with compressed traces |
| **Key insight** | Temporally aligned hidden states as "thought representation"; aggressive compression preserves task utility | Lossless information exchange through shared memory; no training needed | Entire system as unified recursive latent computation; only final round decodes text | Selective information preservation via orthogonal residual from discarded KV states outperforms full relay |
| **Benchmarks** | ALFWorld, MATH (2 benchmarks) | 9 benchmarks (math, science, commonsense, code) | 9 benchmarks | 9 benchmarks |
| **Best claimed gain** | +6% over no-comm on ALFWorld; 24x latency reduction | +14.6% accuracy; 70-84% token reduction; 4-4.3x speedup | +8.3% accuracy; 2.4x speedup; 75.6% fewer tokens | Comparable to full relay at 79-89% communication cost reduction |

**Key architectural distinctions:**

- **Interlat** is the most focused on **compression of latent messages** -- its autoregressive latent-space reasoning module that iteratively generates compact latent summaries is unique. It also provides the most detailed analysis of *what the latent messages encode* (ablations with CrossTask, CovGauss, RandomRot noise showing reliance on geometric structure).

- **LatentMAS** is the only **training-free** approach, using a shared working memory pool. This is a major practical advantage but means it cannot optimize the latent representations for the communication task.

- **RecursiveMAS** casts the multi-agent system as a **single recursive computation graph** with RecursiveLink modules (2-layer residual networks) bridging agents. Its inner/outer link distinction (inner for self-latent-thought, outer for cross-agent transfer) is architecturally distinct from Interlat's single communication adapter.

- **DiffMAS/OBF** operates at the **KV-cache level** rather than hidden-state level, using eviction-style compression with orthogonal residual backfill from discarded states. This is a fundamentally different communication substrate.

---

### 5. Revision History

The paper went through four versions:
- **v1:** November 12, 2025 (initial submission)
- **v2:** January 7, 2026
- **v3:** January 21, 2026
- **v4:** April 16, 2026

The paper provides **no explicit changelog** between versions. The April 2026 revision (v4) likely corresponds to a camera-ready or post-acceptance revision. The comprehensive appendices (A through H) in the current version suggest iterative expansion of experimental analysis and ablation studies across revisions. The OpenReview submission (rmYbgsehTd) is marked "Withdrawn Submission," which is consistent with withdrawing from one review cycle (possibly ICLR or an ARR cycle) to submit to ACL.

---

### 6. Limitations Acknowledged by the Authors

- Experiments focus on a **controlled two-agent setting** with only two benchmarks (ALFWorld, MATH) -- narrower evaluation than LatentMAS/RecursiveMAS (9 benchmarks each).
- Requires **access to internal model representations** -- inapplicable to closed-source or API-only models.
- Latent messages are **not human-readable**, complicating debugging, monitoring, and failure analysis.

---

### Summary for Your Landscape Analysis

Interlat's distinctive contribution to the latent multi-agent communication landscape is its **compression pipeline** -- the autoregressive latent-space reasoning module with the three-component loss (task + preference + geometry) that enables 24x compression while preserving task performance. It is the paper most focused on demonstrating that latent communication can be *aggressively compressed*. However, its evaluation scope is notably narrower than competing methods (2 vs. 9 benchmarks), and it requires training (unlike LatentMAS). The cross-architecture results (Qwen-to-LLaMA) are a strength shared with RecursiveMAS but not demonstrated in LatentMAS or OBF.

Sources:
- [Interlat - arXiv page](https://arxiv.org/abs/2511.09149)
- [Interlat - HTML full text](https://arxiv.org/html/2511.09149v4)
- [Interlat - OpenReview](https://openreview.net/forum?id=rmYbgsehTd)
- [LatentMAS - arXiv](https://arxiv.org/abs/2511.20639)
- [LatentMAS - GitHub](https://github.com/Gen-Verse/LatentMAS)
- [RecursiveMAS - Project page](https://recursivemas.github.io/)
- [OBF/DiffMAS compression - arXiv](https://arxiv.org/abs/2604.13349)
- [ACL 2026 Accepted Papers (not yet published)](https://2026.aclweb.org/program/accepted_papers/)

agentId: a6eccb847c5a694e7 (use SendMessage with to: 'a6eccb847c5a694e7' to continue this agent)
&lt;usage>total_tokens: 25169
tool_uses: 15
duration_ms: 182743&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfbd4440-8ebe-4e70-9e8e-881ec025ab92",
  "isSidechain": false,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "type": "user",
  "uuid": "fe0bb403-6b34-4642-a82c-e05719e5264a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to understand the Interlat paper: \"Enabling Agents to Communicate Entirely in Latent Space\" by Du et al., arXiv 2511.09149 (revised April 2026).\n\nPlease:\n1. Use WebSearch to find this paper (try: \"Interlat arXiv 2511.09149 Du agents communicate latent space\" and \"enabling agents communicate entirely latent space\")\n2. Use WebFetch to read the paper from arXiv (https://arxiv.org/abs/2511.09149)\n3. Identify:\n   - What is their core mechanism for inter-agent latent communication?\n   - How do they compress/transfer hidden states between agents?\n   - How does this compare to LatentMAS (shared working memory of last-layer embeddings), RecursiveMAS (RecursiveLink modules), and DiffMAS (KV-cache trace construction)?\n   - What benchmarks do they evaluate on and what results do they achieve?\n   - Was it revised in April 2026? What changed?\n\nI need this for a research landscape analysis of latent vs text communication methods in multi-agent LLM systems. Report in detail.",
    "agentId": "a6eccb847c5a694e7",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information. Here is the detailed report.\n\n---\n\n## Interlat: \"Enabling Agents to Communicate Entirely in Latent Space\" (Du et al., arXiv 2511.09149)\n\n### Paper Metadata\n- **Authors:** Zhuoyun Du, Runze Wang, Huiyu Bai, Zouying Cao, Xiaoyong Zhu, Yu Cheng, Bo Zheng, Wei Chen, Haochao Ying\n- **Submitted:** November 12, 2025 (v1)\n- **Latest revision:** v4, April 16, 2026\n- **Venue claim:** The arXiv abstract page states \"Accepted to ACL 2026,\" though the ACL 2026 accepted papers list has not yet been published (it says \"Coming soon!\"). The OpenReview submission (rmYbgsehTd) shows status \"Withdrawn Submission,\" suggesting the paper may have been withdrawn from one venue (e.g., an ARR cycle) and submitted/accepted elsewhere.\n\n---\n\n### 1. Core Mechanism for Inter-Agent Latent Communication\n\nInterlat replaces natural-language message-passing between agents with **direct transmission of last-layer hidden states**.\n\n**How it works step by step:**\n\n1. **Hidden state extraction:** When an agent generates a response, the system collects the last-layer hidden state **h_l in R^d** from the transformer at each token position (immediately before predicting the next token). These are assembled into a matrix **H in R^(L x d)** where L is the sequence length.\n\n2. **Transmission:** Special boundary tokens `&lt;bop>` (beginning of plan) and `&lt;eop>` (end of plan) demarcate the latent message region. The receiving agent's input becomes: `[e(x_1), ..., e(x_i), h_1, h_2, ..., h_L, e(x_j)]` -- i.e., continuous hidden-state vectors are spliced directly into the embedding sequence in place of discrete token embeddings.\n\n3. **Communication adapter:** A **trainable lightweight self-attention layer + projection layer** sits at the receiver. This adapter rescales and reinterprets the incoming latent states before the receiving model processes them. This is what enables cross-architecture communication.\n\n4. **No parameter sharing or memory coupling required** -- the adapter provides sufficient bridging that latent semantics transfer even across model families.\n\n---\n\n### 2. Compression / Transfer of Hidden States\n\nInterlat includes a dedicated **compression module** for reducing latent message length:\n\n- **Architecture:** A separate reasoning model M_phi generates compact latent messages **H_K in R^(K x d)** where K is much smaller than L. It works by **autoregressive reasoning entirely in latent space** -- feeding its own last hidden state back as the next input embedding through a lightweight projection: `M_phi(E_i) -> h_i, E_{i+1} = E_i + Proj(h_i)`.\n\n- **Compression ratio:** Full messages of 128 latent tokens can be compressed to as few as **8 tokens** while maintaining competitive performance, achieving up to **24x reduction in communication latency** (from 9.19s to 0.39s).\n\n- **Training loss (three components):**\n  - **Task loss (L_task):** Cross-entropy ensuring downstream utility of compressed messages.\n  - **Preference loss (L_pref):** Uncertainty-weighted KL divergence aligning compressed and full behaviors at positions where latents reduce uncertainty.\n  - **Geometry loss (L_geom):** Cosine similarity maintaining directional alignment between compressed and full representations: `L_geom = 1 - cos(z_bar^A, z_bar^D)`.\n\n**Actor training** also uses a multi-component loss: `L_total = L_task + lambda_S * L_sep + lambda_A * L_align`, where:\n- **Conditional thought separation (L_sep):** Minimizes weighted Jensen-Shannon divergence between matched and mismatched latent inputs, ensuring the receiver distinguishes relevant from irrelevant latent messages.\n- **Plan-aligned regulation (L_align):** Regularizes against language-space plans to prevent exploiting the separation objective.\n- A **token-to-latent curriculum** stochastically replaces early communication positions with corresponding plan token embeddings (replacement rate r in {0, 0.1, ..., 1.0}).\n\n---\n\n### 3. Benchmarks and Results\n\n**ALFWorld (embodied household tasks):**\n\n| Model Config | Seen (%) | Unseen (%) | Steps (Succ/All) |\n|---|---|---|---|\n| Interlat (Qwen2.5-7B) | **70.48** | **65.42** | 9.41 / 12.54 |\n| Text CoT (fine-tuned) | 64.29 | 62.44 | 8.76 / 12.77 |\n| No Communication | 62.14 | 62.19 | 10.19 / 13.90 |\n| CoT (full) | 67.14 | 64.93 | 8.15 / 12.04 |\n\nConsistent gains across three backbones (Qwen2.5-7B, Qwen2.5-0.5B, LLaMA3.1-8B).\n\n**MATH benchmark:**\n\n| Method | Overall | Level-3 | Level-4 | Level-5 |\n|---|---|---|---|---|\n| Interlat | 36.88% | 40.08% | 27.45% | **15.80%** |\n| CoT (full) | 38.35% | 45.65% | 31.19% | 15.05% |\n| Text | 34.35% | 37.60% | 26.30% | 14.20% |\n\nInterlat surpasses CoT specifically on the hardest Level-5 problems.\n\n**Compression results (Qwen2.5-7B, ALFWorld):**\n\n| Latent Length | Seen (%) | Unseen (%) | Latency |\n|---|---|---|---|\n| Full (128) | 68.10 | 62.94 | 2.25s |\n| 64 | 67.14 | 61.94 | 1.16s |\n| 8 | 66.43 | 60.45 | 0.20s |\n\n**Heterogeneous model results:** Feeding Qwen-derived latents to train a LLaMA actor yielded **70.95% seen / 71.39% unseen** -- actually slightly better than homogeneous Qwen-to-Qwen, demonstrating cross-family latent transfer works.\n\n---\n\n### 4. Comparison to LatentMAS, RecursiveMAS, and DiffMAS (OBF)\n\nInterlat does **not** directly cite or compare against LatentMAS, RecursiveMAS, or DiffMAS. These are all contemporaneous works (late 2025 / early 2026). Here is a structured comparison based on my research:\n\n| Dimension | **Interlat** | **LatentMAS** | **RecursiveMAS** | **DiffMAS/OBF** |\n|---|---|---|---|---|\n| **Venue** | ACL 2026 (claimed) | ICML 2026 Spotlight | -- | arXiv Apr 2026 |\n| **What is transmitted** | Last-layer hidden states (full sequence) | Last-layer hidden embeddings via shared working memory | Last-layer hidden states via RecursiveLink module | Compressed KV-cache with orthogonal residual backfill |\n| **Training required?** | Yes (adapter + compression module) | **Training-free** | Yes (lightweight RecursiveLink, 2-layer residual module) | Yes (eviction-style compression) |\n| **Compression** | Autoregressive latent-space reasoning; down to 8 tokens (24x speedup) | No explicit compression -- full latent thoughts shared | Implicit via RecursiveLink projection | Orthogonal Backfill (OBF): 79.8-89.4% KV-cache reduction |\n| **Cross-architecture** | Yes, via communication adapter (Qwen -> LLaMA demonstrated) | Not emphasized | Yes, outer link handles different hidden dimensions | Not specified |\n| **Memory mechanism** | Direct injection into embedding sequence | Shared latent working memory pool | Recursive loop: agents chain via inner/outer links | KV-cache relay with compressed traces |\n| **Key insight** | Temporally aligned hidden states as \"thought representation\"; aggressive compression preserves task utility | Lossless information exchange through shared memory; no training needed | Entire system as unified recursive latent computation; only final round decodes text | Selective information preservation via orthogonal residual from discarded KV states outperforms full relay |\n| **Benchmarks** | ALFWorld, MATH (2 benchmarks) | 9 benchmarks (math, science, commonsense, code) | 9 benchmarks | 9 benchmarks |\n| **Best claimed gain** | +6% over no-comm on ALFWorld; 24x latency reduction | +14.6% accuracy; 70-84% token reduction; 4-4.3x speedup | +8.3% accuracy; 2.4x speedup; 75.6% fewer tokens | Comparable to full relay at 79-89% communication cost reduction |\n\n**Key architectural distinctions:**\n\n- **Interlat** is the most focused on **compression of latent messages** -- its autoregressive latent-space reasoning module that iteratively generates compact latent summaries is unique. It also provides the most detailed analysis of *what the latent messages encode* (ablations with CrossTask, CovGauss, RandomRot noise showing reliance on geometric structure).\n\n- **LatentMAS** is the only **training-free** approach, using a shared working memory pool. This is a major practical advantage but means it cannot optimize the latent representations for the communication task.\n\n- **RecursiveMAS** casts the multi-agent system as a **single recursive computation graph** with RecursiveLink modules (2-layer residual networks) bridging agents. Its inner/outer link distinction (inner for self-latent-thought, outer for cross-agent transfer) is architecturally distinct from Interlat's single communication adapter.\n\n- **DiffMAS/OBF** operates at the **KV-cache level** rather than hidden-state level, using eviction-style compression with orthogonal residual backfill from discarded states. This is a fundamentally different communication substrate.\n\n---\n\n### 5. Revision History\n\nThe paper went through four versions:\n- **v1:** November 12, 2025 (initial submission)\n- **v2:** January 7, 2026\n- **v3:** January 21, 2026\n- **v4:** April 16, 2026\n\nThe paper provides **no explicit changelog** between versions. The April 2026 revision (v4) likely corresponds to a camera-ready or post-acceptance revision. The comprehensive appendices (A through H) in the current version suggest iterative expansion of experimental analysis and ablation studies across revisions. The OpenReview submission (rmYbgsehTd) is marked \"Withdrawn Submission,\" which is consistent with withdrawing from one review cycle (possibly ICLR or an ARR cycle) to submit to ACL.\n\n---\n\n### 6. Limitations Acknowledged by the Authors\n\n- Experiments focus on a **controlled two-agent setting** with only two benchmarks (ALFWorld, MATH) -- narrower evaluation than LatentMAS/RecursiveMAS (9 benchmarks each).\n- Requires **access to internal model representations** -- inapplicable to closed-source or API-only models.\n- Latent messages are **not human-readable**, complicating debugging, monitoring, and failure analysis.\n\n---\n\n### Summary for Your Landscape Analysis\n\nInterlat's distinctive contribution to the latent multi-agent communication landscape is its **compression pipeline** -- the autoregressive latent-space reasoning module with the three-component loss (task + preference + geometry) that enables 24x compression while preserving task performance. It is the paper most focused on demonstrating that latent communication can be *aggressively compressed*. However, its evaluation scope is notably narrower than competing methods (2 vs. 9 benchmarks), and it requires training (unlike LatentMAS). The cross-architecture results (Qwen-to-LLaMA) are a strength shared with RecursiveMAS but not demonstrated in LatentMAS or OBF.\n\nSources:\n- [Interlat - arXiv page](https://arxiv.org/abs/2511.09149)\n- [Interlat - HTML full text](https://arxiv.org/html/2511.09149v4)\n- [Interlat - OpenReview](https://openreview.net/forum?id=rmYbgsehTd)\n- [LatentMAS - arXiv](https://arxiv.org/abs/2511.20639)\n- [LatentMAS - GitHub](https://github.com/Gen-Verse/LatentMAS)\n- [RecursiveMAS - Project page](https://recursivemas.github.io/)\n- [OBF/DiffMAS compression - arXiv](https://arxiv.org/abs/2604.13349)\n- [ACL 2026 Accepted Papers (not yet published)](https://2026.aclweb.org/program/accepted_papers/)"
      }
    ],
    "totalDurationMs": 182743,
    "totalTokens": 25169,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1665,
      "cache_read_input_tokens": 20235,
      "output_tokens": 3268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1665
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3268,
          "cache_read_input_tokens": 20235,
          "cache_creation_input_tokens": 1665,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1665,
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
      "otherToolCount": 15
    }
  },
  "sourceToolAssistantUUID": "bfbd4440-8ebe-4e70-9e8e-881ec025ab92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-10T20:51:51.275Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01BhRWVwcXsPZdM7ApTfGSji`</summary>

```json
{
  "description": "Research novelty gap and contrastive communication",
  "prompt": "I'm researching whether contrastive or mutual-information-based methods have been applied to multi-agent LLM communication training, and whether there are recent works that address the \"text vs latent communication\" gap in multi-agent LLM systems.\n\nPlease search for:\n\n1. \"contrastive learning multi-agent communication\" - any work using contrastive objectives to train communication in MARL or multi-agent LLM systems\n2. \"mutual information multi-agent communication LLM\" - MI-based approaches\n3. \"text communication quality multi-agent LLM training\" - methods specifically targeting text message quality\n4. \"communication grounding large language model multi-agent\" - grounding approaches at LLM scale\n5. \"distillation latent to text multi-agent\" or \"latent teacher text student communication\" - any work distilling latent communication into text\n\nFor each search, use WebSearch, then WebFetch on the most relevant results.\n\nAlso search for:\n6. Any very recent (April-May 2026) papers on multi-agent LLM communication that might be concurrent work\n7. \"hierarchical attention network Yang 2016\" and \"self-attentive sentence embedding Lin 2017\" to confirm the attention pooling mechanism's provenance\n\nI need to understand whether the proposed novelty of \"reconstruction + attention pooling for text communication in LLM GRPO\" is truly novel or if similar ideas exist. Report findings in detail.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe0bb403-6b34-4642-a82c-e05719e5264a",
  "isSidechain": false,
  "requestId": "req_011CauYr2M4LGLkkZwe5i3Qn",
  "type": "assistant",
  "uuid": "3456543d-15bf-4c69-bf07-62939dc45111",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nhpxqpsy7YTuVXDchiQ9XD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3715,
      "cache_read_input_tokens": 29502,
      "output_tokens": 421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 421,
          "cache_read_input_tokens": 29502,
          "cache_creation_input_tokens": 3715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3715
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T20:56:32.012Z_

<details><summary>↩ Tool result · `toolu_01BhRWVwcXsPZdM7ApTfGSji`</summary>

```text
Now I have comprehensive findings. Let me compile the detailed report.

---

Here is a detailed analysis of the literature landscape, organized by your search topics, with an assessment of the proposed novelty of "reconstruction + attention pooling for text communication in LLM GRPO."

---

## 1. Contrastive Learning for Multi-Agent Communication

There is a well-established line of work applying contrastive objectives to multi-agent communication in MARL, but **all of it operates on continuous/latent messages, not text, and none involves LLMs**:

- **CACL (Communication Alignment Contrastive Learning)** -- Lo, Sengupta, Foerster, Noukhovitch (2024, arXiv 2307.01403). Treats agents' messages as incomplete views of the environment state. Uses SupCon loss: messages from the same trajectory within a temporal window are positive pairs; messages from different trajectories are negatives. Messages are continuous D-dimensional vectors (D=4), not text. No reconstruction component. No attention pooling. [Paper](https://arxiv.org/html/2307.01403)

- **TACTIC (Task-Agnostic Contrastive Pre-Training)** -- Yu, Mishra, Zaidi, Tokekar (AAMAS 2025). Two-stage: offline contrastive pre-training + online policy learning. Uses Global Information Alignment (GIA) and Feature Integration Alignment (FIA) via SupCon loss. Critically, it **also includes a reconstruction auxiliary loss** -- a decoder recovers egocentric states from feature embeddings. Additionally uses a dynamics loss for temporal coherence. Messages are continuous vectors. No attention pooling mechanism. [Paper](https://arxiv.org/html/2501.02174)

- **MAGE** -- Learning multi-agent communication via graph contrastive learning (2025, Pattern Recognition). Uses contrast objectives at both feature and topological levels. Continuous messages. [Paper](https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538)

**Key finding for novelty assessment:** TACTIC (AAMAS 2025) already combines contrastive pre-training with reconstruction auxiliary loss for multi-agent communication, though in continuous-message MARL, not in LLM text communication.

---

## 2. Mutual Information Approaches

MI-based methods are widespread in classical MARL communication:

- **MASIA (Multi-Agent Self-supervised Information Aggregation)** -- Guan et al. (NeurIPS 2022). Uses a permutation-invariant message encoder to aggregate received messages, optimized via **reconstructing and predicting ("shooting") future information** in a self-supervised manner. Each agent extracts the most relevant parts of the aggregated representation via a **novel message extraction mechanism**. This is the closest classical MARL precursor combining reconstruction with information extraction from messages. Continuous messages, not LLMs. [Paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/075b2875e2b671ddd74aeec0ac9f0357-Abstract-Conference.html)

- The "Beyond Self-Talk" survey (Yan et al., 2025, arXiv 2502.14321) notes that MI maximization and information-theoretic bottleneck principles are used in classical MARL communication, but these have **not been transferred to LLM-based multi-agent systems**. [Survey](https://arxiv.org/abs/2502.14321)

**Key finding:** MASIA (NeurIPS 2022) combines reconstruction with a message extraction mechanism in classical MARL. However, no work has applied MI-based objectives to text communication between LLM agents.

---

## 3. Text Communication Quality in Multi-Agent LLM Training

This is the most relevant and **most sparsely populated** area:

- **MAGRPO** -- Liu et al. (AAAI 2026). Applies GRPO to multi-agent LLM systems modeled as Dec-POMDP. However, it does **not** use explicit message passing between agents -- agents operate through decentralized execution with implicit coordination via the environment. **No auxiliary loss for message quality, no reconstruction, no attention pooling.** Joint task-dependent reward only. [Paper](https://arxiv.org/html/2508.04652v1)

- **M-GRPO** -- Hong et al. (2025, arXiv 2511.13288). Hierarchical GRPO for main agent + sub-agents. Focuses on credit assignment and trajectory alignment, **not communication quality**. No reconstruction or attention mechanisms for messages. [Paper](https://arxiv.org/abs/2511.13288)

- **MARFT** -- Liao et al. (2025, arXiv 2504.16129). Universal algorithmic framework for LLM-based multi-agent RL. Adapts PPO/GRPO to multi-agent contexts. **Does not address communication quality specifically** -- focuses on KL divergence regularization and policy optimization. [Paper](https://arxiv.org/html/2504.16129v2)

- **MARTI** -- Tsinghua (ICLR 2026). Framework for multi-agent reinforced training and inference. Uses rule-based verifiable rewards and LLM-based generative rewards. **No specific mechanism for communication quality** (reconstruction, contrastive, or attention-based). [Paper](https://openreview.net/forum?id=E7jZqo0A50)

- **Graph-GRPO** -- Cang et al. (March 2026, arXiv 2603.02701). Uses GAT with GRPO for communication **topology** learning (which edges to activate), not message content quality. No reconstruction or contrastive loss. [Paper](https://arxiv.org/html/2603.02701)

- **LTC (Learning through Communication)** -- Wang et al. (ICLR 2024/NAACL 2025). LLM agents learn through communication via PPO with iterative exploration. Designs communication patterns (Monologue, Dialogue, Analogue) but **does not use auxiliary losses for message quality**. [Paper](https://openreview.net/forum?id=wOelVq8fwL)

- The orchestration traces survey (Zhang, May 2026, arXiv 2605.02801) explicitly states: **"explicit counterfactual message-level credit remains especially sparse"** in the literature. The message level of credit assignment is noted as an important open research area. [Paper](https://arxiv.org/abs/2605.02801)

**Key finding:** No existing work applies reconstruction loss or attention pooling as auxiliary objectives to improve text message quality in LLM-based multi-agent GRPO training. This appears to be a genuine gap.

---

## 4. Communication Grounding at LLM Scale

- **Grounding Natural Language for Multi-Agent Decision Making** (2025, arXiv 2508.07466). Focuses on grounding LLM plans in agent actions. [Paper](https://arxiv.org/pdf/2508.07466)

- **ReAd (Reinforced Advantage Feedback)** -- Towards Efficient LLM Grounding for Embodied Multi-Agent Collaboration (2024, arXiv 2405.14314). Addresses plan adjustment through communication but does not use reconstruction or contrastive objectives for message quality. [Paper](https://arxiv.org/abs/2405.14314)

No work bridges classical MARL communication grounding techniques (contrastive, MI-based) to LLM-scale text communication training.

---

## 5. Distillation: Latent-to-Text Communication

This is a very active area, but it goes in the **opposite direction** from what you describe (text-to-latent, or pure latent, rather than improving text communication):

- **LatentMAS** (ICML 2026 Spotlight). Agents communicate entirely in latent space via hidden embeddings and shared working memory. Training-free. 14.6% higher accuracy, 70-83% fewer tokens, 4x faster. **Does not try to improve text communication** -- instead replaces it entirely with latent communication. [Paper](https://arxiv.org/abs/2511.20639)

- **Vision Wormhole** (Liu et al., 2025, arXiv 2602.15382). Teacher-student distillation where text-based communication is the teacher and latent (vision-channel) communication is the student. Uses L2 distance for representational fidelity, KL divergence for output distribution fidelity, and RMS matching for magnitude regularization. **No reconstruction loss.** This is distillation **from text to latent**, not the reverse. [Paper](https://arxiv.org/html/2602.15382v1)

- **Interlat** (Du et al., 2025-2026, arXiv 2511.09149). Inter-agent latent space communication via last hidden states. Includes learned compression. 24x inference speedup. Replaces text entirely. [Paper](https://arxiv.org/abs/2511.09149)

- **OBF (Orthogonal Backfill)** (Li et al., April 2026, arXiv 2604.13349). Information-preserving compression for latent multi-agent collaboration, building on LatentMAS. Reduces communication cost 80-89%. [Paper](https://arxiv.org/abs/2604.13349)

**Key finding:** The field is moving strongly toward latent communication to replace text. No work attempts to **improve text communication quality** by using reconstruction of latent representations as an auxiliary objective. The proposed direction (using reconstruction to make text communication better, rather than abandoning text for latent) is contrarian to the dominant trend.

---

## 6. Recent Concurrent Work (April-May 2026)

- **Graph-GRPO** (March 2026) -- topology optimization, not message content
- **OBF** (April 2026) -- latent compression, not text improvement
- **Orchestration Traces survey** (May 2026) -- identifies message-level credit as an open problem
- **Latent Agents** (April 2026, arXiv 2604.24881) -- internalizes multi-agent debate into latent space via SFT then RL

No concurrent work addresses the specific combination of reconstruction + attention pooling for text communication quality in GRPO.

---

## 7. Provenance of Attention Pooling

- **Yang et al. (2016)** -- "Hierarchical Attention Networks for Document Classification" (NAACL 2016). Introduced hierarchical attention at word and sentence level, attending differentially to important content. This is the canonical reference for attention-based document representation. [Paper](https://aclanthology.org/N16-1174/)

- **Lin et al. (2017)** -- "A Structured Self-Attentive Sentence Embedding" (ICLR 2017, arXiv 1703.03130). Introduced self-attention for sentence embedding with multi-hop attention (r-by-da annotation matrix), producing a 2D matrix representation. Published as a conference paper at ICLR 2017. [Paper](https://arxiv.org/abs/1703.03130)

Both are well-established references for attention pooling. Using them to pool over token-level representations to create a message-level embedding for a reconstruction objective would be a novel application context, though the mechanism itself is well-known.

---

## Novelty Assessment

The proposed idea of "reconstruction + attention pooling for text communication in LLM GRPO" appears to be **genuinely novel** in its specific combination, based on this search. Here is why:

**What exists:**
1. Reconstruction auxiliary losses for communication exist in classical MARL (MASIA, TACTIC) but only for continuous-vector messages in small-scale agents, not LLMs.
2. Contrastive/MI objectives for communication grounding exist in classical MARL (CACL, MAGE) but again only for continuous messages.
3. Multi-agent GRPO variants exist (MAGRPO, M-GRPO, Graph-GRPO, MARFT) but none include auxiliary communication quality objectives.
4. Attention pooling for message aggregation exists in classical MARL (MAGIC, various graph attention methods) but not applied to text message encoding in LLM systems.
5. The dominant direction for LLM multi-agent communication is moving **away from text toward latent** (LatentMAS, Interlat, Vision Wormhole).

**What does not exist (the gap):**
- No work uses reconstruction loss as an auxiliary objective to improve the quality of **text** messages in LLM-based multi-agent systems.
- No work combines attention pooling over text token representations with reconstruction for message-level credit assignment in GRPO.
- The May 2026 orchestration traces survey explicitly identifies message-level credit as "especially sparse," confirming this is an open problem.
- The approach is contrarian to the latent-communication trend -- rather than abandoning text, it seeks to make text communication better via information-theoretic auxiliary objectives borrowed from classical MARL.

**Potential concerns for reviewers:**
- MASIA (NeurIPS 2022) and TACTIC (AAMAS 2025) are close in spirit (reconstruction + information extraction for communication), so clear differentiation from these classical MARL methods will be important.
- The attention pooling mechanism draws from well-known sources (Yang 2016, Lin 2017), so the novelty is in the application context, not the mechanism itself.
- Reviewers familiar with the latent communication trend (LatentMAS at ICML 2026) may question why you would optimize text communication rather than switch to latent.

Sources:
- [CACL - Learning Multi-Agent Communication with Contrastive Learning](https://arxiv.org/html/2307.01403)
- [TACTIC - Task-Agnostic Contrastive Pre-Training](https://arxiv.org/html/2501.02174)
- [MASIA - Self-supervised Information Aggregation (NeurIPS 2022)](https://proceedings.neurips.cc/paper_files/paper/2022/hash/075b2875e2b671ddd74aeec0ac9f0357-Abstract-Conference.html)
- [MAGRPO - LLM Collaboration with MARL (AAAI 2026)](https://arxiv.org/html/2508.04652v1)
- [M-GRPO - Multi-Agent Deep Research](https://arxiv.org/abs/2511.13288)
- [Graph-GRPO](https://arxiv.org/html/2603.02701)
- [MARFT - Multi-Agent Reinforcement Fine-Tuning](https://arxiv.org/html/2504.16129v2)
- [MARTI (ICLR 2026)](https://openreview.net/forum?id=E7jZqo0A50)
- [LatentMAS (ICML 2026)](https://arxiv.org/abs/2511.20639)
- [Vision Wormhole](https://arxiv.org/html/2602.15382v1)
- [Interlat](https://arxiv.org/abs/2511.09149)
- [OBF - Latent Compression](https://arxiv.org/abs/2604.13349)
- [Beyond Self-Talk Survey](https://arxiv.org/abs/2502.14321)
- [Orchestration Traces Survey (May 2026)](https://arxiv.org/abs/2605.02801)
- [LTC - Adapting LLM Agents Through Communication](https://openreview.net/forum?id=wOelVq8fwL)
- [Yang 2016 - Hierarchical Attention Networks](https://aclanthology.org/N16-1174/)
- [Lin 2017 - Self-Attentive Sentence Embedding](https://arxiv.org/abs/1703.03130)
- [MAGE - Graph Contrastive Learning for Communication](https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538)
- [ACORM - Attention-Guided Contrastive Role Representations](https://arxiv.org/abs/2312.04819)

agentId: a7accad31768e0d6c (use SendMessage with to: 'a7accad31768e0d6c' to continue this agent)
&lt;usage>total_tokens: 48912
tool_uses: 44
duration_ms: 280733&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3456543d-15bf-4c69-bf07-62939dc45111",
  "isSidechain": false,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "type": "user",
  "uuid": "d0bb40a7-642d-4f5f-91c8-c67b8f7a770b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm researching whether contrastive or mutual-information-based methods have been applied to multi-agent LLM communication training, and whether there are recent works that address the \"text vs latent communication\" gap in multi-agent LLM systems.\n\nPlease search for:\n\n1. \"contrastive learning multi-agent communication\" - any work using contrastive objectives to train communication in MARL or multi-agent LLM systems\n2. \"mutual information multi-agent communication LLM\" - MI-based approaches\n3. \"text communication quality multi-agent LLM training\" - methods specifically targeting text message quality\n4. \"communication grounding large language model multi-agent\" - grounding approaches at LLM scale\n5. \"distillation latent to text multi-agent\" or \"latent teacher text student communication\" - any work distilling latent communication into text\n\nFor each search, use WebSearch, then WebFetch on the most relevant results.\n\nAlso search for:\n6. Any very recent (April-May 2026) papers on multi-agent LLM communication that might be concurrent work\n7. \"hierarchical attention network Yang 2016\" and \"self-attentive sentence embedding Lin 2017\" to confirm the attention pooling mechanism's provenance\n\nI need to understand whether the proposed novelty of \"reconstruction + attention pooling for text communication in LLM GRPO\" is truly novel or if similar ideas exist. Report findings in detail.",
    "agentId": "a7accad31768e0d6c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive findings. Let me compile the detailed report.\n\n---\n\nHere is a detailed analysis of the literature landscape, organized by your search topics, with an assessment of the proposed novelty of \"reconstruction + attention pooling for text communication in LLM GRPO.\"\n\n---\n\n## 1. Contrastive Learning for Multi-Agent Communication\n\nThere is a well-established line of work applying contrastive objectives to multi-agent communication in MARL, but **all of it operates on continuous/latent messages, not text, and none involves LLMs**:\n\n- **CACL (Communication Alignment Contrastive Learning)** -- Lo, Sengupta, Foerster, Noukhovitch (2024, arXiv 2307.01403). Treats agents' messages as incomplete views of the environment state. Uses SupCon loss: messages from the same trajectory within a temporal window are positive pairs; messages from different trajectories are negatives. Messages are continuous D-dimensional vectors (D=4), not text. No reconstruction component. No attention pooling. [Paper](https://arxiv.org/html/2307.01403)\n\n- **TACTIC (Task-Agnostic Contrastive Pre-Training)** -- Yu, Mishra, Zaidi, Tokekar (AAMAS 2025). Two-stage: offline contrastive pre-training + online policy learning. Uses Global Information Alignment (GIA) and Feature Integration Alignment (FIA) via SupCon loss. Critically, it **also includes a reconstruction auxiliary loss** -- a decoder recovers egocentric states from feature embeddings. Additionally uses a dynamics loss for temporal coherence. Messages are continuous vectors. No attention pooling mechanism. [Paper](https://arxiv.org/html/2501.02174)\n\n- **MAGE** -- Learning multi-agent communication via graph contrastive learning (2025, Pattern Recognition). Uses contrast objectives at both feature and topological levels. Continuous messages. [Paper](https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538)\n\n**Key finding for novelty assessment:** TACTIC (AAMAS 2025) already combines contrastive pre-training with reconstruction auxiliary loss for multi-agent communication, though in continuous-message MARL, not in LLM text communication.\n\n---\n\n## 2. Mutual Information Approaches\n\nMI-based methods are widespread in classical MARL communication:\n\n- **MASIA (Multi-Agent Self-supervised Information Aggregation)** -- Guan et al. (NeurIPS 2022). Uses a permutation-invariant message encoder to aggregate received messages, optimized via **reconstructing and predicting (\"shooting\") future information** in a self-supervised manner. Each agent extracts the most relevant parts of the aggregated representation via a **novel message extraction mechanism**. This is the closest classical MARL precursor combining reconstruction with information extraction from messages. Continuous messages, not LLMs. [Paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/075b2875e2b671ddd74aeec0ac9f0357-Abstract-Conference.html)\n\n- The \"Beyond Self-Talk\" survey (Yan et al., 2025, arXiv 2502.14321) notes that MI maximization and information-theoretic bottleneck principles are used in classical MARL communication, but these have **not been transferred to LLM-based multi-agent systems**. [Survey](https://arxiv.org/abs/2502.14321)\n\n**Key finding:** MASIA (NeurIPS 2022) combines reconstruction with a message extraction mechanism in classical MARL. However, no work has applied MI-based objectives to text communication between LLM agents.\n\n---\n\n## 3. Text Communication Quality in Multi-Agent LLM Training\n\nThis is the most relevant and **most sparsely populated** area:\n\n- **MAGRPO** -- Liu et al. (AAAI 2026). Applies GRPO to multi-agent LLM systems modeled as Dec-POMDP. However, it does **not** use explicit message passing between agents -- agents operate through decentralized execution with implicit coordination via the environment. **No auxiliary loss for message quality, no reconstruction, no attention pooling.** Joint task-dependent reward only. [Paper](https://arxiv.org/html/2508.04652v1)\n\n- **M-GRPO** -- Hong et al. (2025, arXiv 2511.13288). Hierarchical GRPO for main agent + sub-agents. Focuses on credit assignment and trajectory alignment, **not communication quality**. No reconstruction or attention mechanisms for messages. [Paper](https://arxiv.org/abs/2511.13288)\n\n- **MARFT** -- Liao et al. (2025, arXiv 2504.16129). Universal algorithmic framework for LLM-based multi-agent RL. Adapts PPO/GRPO to multi-agent contexts. **Does not address communication quality specifically** -- focuses on KL divergence regularization and policy optimization. [Paper](https://arxiv.org/html/2504.16129v2)\n\n- **MARTI** -- Tsinghua (ICLR 2026). Framework for multi-agent reinforced training and inference. Uses rule-based verifiable rewards and LLM-based generative rewards. **No specific mechanism for communication quality** (reconstruction, contrastive, or attention-based). [Paper](https://openreview.net/forum?id=E7jZqo0A50)\n\n- **Graph-GRPO** -- Cang et al. (March 2026, arXiv 2603.02701). Uses GAT with GRPO for communication **topology** learning (which edges to activate), not message content quality. No reconstruction or contrastive loss. [Paper](https://arxiv.org/html/2603.02701)\n\n- **LTC (Learning through Communication)** -- Wang et al. (ICLR 2024/NAACL 2025). LLM agents learn through communication via PPO with iterative exploration. Designs communication patterns (Monologue, Dialogue, Analogue) but **does not use auxiliary losses for message quality**. [Paper](https://openreview.net/forum?id=wOelVq8fwL)\n\n- The orchestration traces survey (Zhang, May 2026, arXiv 2605.02801) explicitly states: **\"explicit counterfactual message-level credit remains especially sparse\"** in the literature. The message level of credit assignment is noted as an important open research area. [Paper](https://arxiv.org/abs/2605.02801)\n\n**Key finding:** No existing work applies reconstruction loss or attention pooling as auxiliary objectives to improve text message quality in LLM-based multi-agent GRPO training. This appears to be a genuine gap.\n\n---\n\n## 4. Communication Grounding at LLM Scale\n\n- **Grounding Natural Language for Multi-Agent Decision Making** (2025, arXiv 2508.07466). Focuses on grounding LLM plans in agent actions. [Paper](https://arxiv.org/pdf/2508.07466)\n\n- **ReAd (Reinforced Advantage Feedback)** -- Towards Efficient LLM Grounding for Embodied Multi-Agent Collaboration (2024, arXiv 2405.14314). Addresses plan adjustment through communication but does not use reconstruction or contrastive objectives for message quality. [Paper](https://arxiv.org/abs/2405.14314)\n\nNo work bridges classical MARL communication grounding techniques (contrastive, MI-based) to LLM-scale text communication training.\n\n---\n\n## 5. Distillation: Latent-to-Text Communication\n\nThis is a very active area, but it goes in the **opposite direction** from what you describe (text-to-latent, or pure latent, rather than improving text communication):\n\n- **LatentMAS** (ICML 2026 Spotlight). Agents communicate entirely in latent space via hidden embeddings and shared working memory. Training-free. 14.6% higher accuracy, 70-83% fewer tokens, 4x faster. **Does not try to improve text communication** -- instead replaces it entirely with latent communication. [Paper](https://arxiv.org/abs/2511.20639)\n\n- **Vision Wormhole** (Liu et al., 2025, arXiv 2602.15382). Teacher-student distillation where text-based communication is the teacher and latent (vision-channel) communication is the student. Uses L2 distance for representational fidelity, KL divergence for output distribution fidelity, and RMS matching for magnitude regularization. **No reconstruction loss.** This is distillation **from text to latent**, not the reverse. [Paper](https://arxiv.org/html/2602.15382v1)\n\n- **Interlat** (Du et al., 2025-2026, arXiv 2511.09149). Inter-agent latent space communication via last hidden states. Includes learned compression. 24x inference speedup. Replaces text entirely. [Paper](https://arxiv.org/abs/2511.09149)\n\n- **OBF (Orthogonal Backfill)** (Li et al., April 2026, arXiv 2604.13349). Information-preserving compression for latent multi-agent collaboration, building on LatentMAS. Reduces communication cost 80-89%. [Paper](https://arxiv.org/abs/2604.13349)\n\n**Key finding:** The field is moving strongly toward latent communication to replace text. No work attempts to **improve text communication quality** by using reconstruction of latent representations as an auxiliary objective. The proposed direction (using reconstruction to make text communication better, rather than abandoning text for latent) is contrarian to the dominant trend.\n\n---\n\n## 6. Recent Concurrent Work (April-May 2026)\n\n- **Graph-GRPO** (March 2026) -- topology optimization, not message content\n- **OBF** (April 2026) -- latent compression, not text improvement\n- **Orchestration Traces survey** (May 2026) -- identifies message-level credit as an open problem\n- **Latent Agents** (April 2026, arXiv 2604.24881) -- internalizes multi-agent debate into latent space via SFT then RL\n\nNo concurrent work addresses the specific combination of reconstruction + attention pooling for text communication quality in GRPO.\n\n---\n\n## 7. Provenance of Attention Pooling\n\n- **Yang et al. (2016)** -- \"Hierarchical Attention Networks for Document Classification\" (NAACL 2016). Introduced hierarchical attention at word and sentence level, attending differentially to important content. This is the canonical reference for attention-based document representation. [Paper](https://aclanthology.org/N16-1174/)\n\n- **Lin et al. (2017)** -- \"A Structured Self-Attentive Sentence Embedding\" (ICLR 2017, arXiv 1703.03130). Introduced self-attention for sentence embedding with multi-hop attention (r-by-da annotation matrix), producing a 2D matrix representation. Published as a conference paper at ICLR 2017. [Paper](https://arxiv.org/abs/1703.03130)\n\nBoth are well-established references for attention pooling. Using them to pool over token-level representations to create a message-level embedding for a reconstruction objective would be a novel application context, though the mechanism itself is well-known.\n\n---\n\n## Novelty Assessment\n\nThe proposed idea of \"reconstruction + attention pooling for text communication in LLM GRPO\" appears to be **genuinely novel** in its specific combination, based on this search. Here is why:\n\n**What exists:**\n1. Reconstruction auxiliary losses for communication exist in classical MARL (MASIA, TACTIC) but only for continuous-vector messages in small-scale agents, not LLMs.\n2. Contrastive/MI objectives for communication grounding exist in classical MARL (CACL, MAGE) but again only for continuous messages.\n3. Multi-agent GRPO variants exist (MAGRPO, M-GRPO, Graph-GRPO, MARFT) but none include auxiliary communication quality objectives.\n4. Attention pooling for message aggregation exists in classical MARL (MAGIC, various graph attention methods) but not applied to text message encoding in LLM systems.\n5. The dominant direction for LLM multi-agent communication is moving **away from text toward latent** (LatentMAS, Interlat, Vision Wormhole).\n\n**What does not exist (the gap):**\n- No work uses reconstruction loss as an auxiliary objective to improve the quality of **text** messages in LLM-based multi-agent systems.\n- No work combines attention pooling over text token representations with reconstruction for message-level credit assignment in GRPO.\n- The May 2026 orchestration traces survey explicitly identifies message-level credit as \"especially sparse,\" confirming this is an open problem.\n- The approach is contrarian to the latent-communication trend -- rather than abandoning text, it seeks to make text communication better via information-theoretic auxiliary objectives borrowed from classical MARL.\n\n**Potential concerns for reviewers:**\n- MASIA (NeurIPS 2022) and TACTIC (AAMAS 2025) are close in spirit (reconstruction + information extraction for communication), so clear differentiation from these classical MARL methods will be important.\n- The attention pooling mechanism draws from well-known sources (Yang 2016, Lin 2017), so the novelty is in the application context, not the mechanism itself.\n- Reviewers familiar with the latent communication trend (LatentMAS at ICML 2026) may question why you would optimize text communication rather than switch to latent.\n\nSources:\n- [CACL - Learning Multi-Agent Communication with Contrastive Learning](https://arxiv.org/html/2307.01403)\n- [TACTIC - Task-Agnostic Contrastive Pre-Training](https://arxiv.org/html/2501.02174)\n- [MASIA - Self-supervised Information Aggregation (NeurIPS 2022)](https://proceedings.neurips.cc/paper_files/paper/2022/hash/075b2875e2b671ddd74aeec0ac9f0357-Abstract-Conference.html)\n- [MAGRPO - LLM Collaboration with MARL (AAAI 2026)](https://arxiv.org/html/2508.04652v1)\n- [M-GRPO - Multi-Agent Deep Research](https://arxiv.org/abs/2511.13288)\n- [Graph-GRPO](https://arxiv.org/html/2603.02701)\n- [MARFT - Multi-Agent Reinforcement Fine-Tuning](https://arxiv.org/html/2504.16129v2)\n- [MARTI (ICLR 2026)](https://openreview.net/forum?id=E7jZqo0A50)\n- [LatentMAS (ICML 2026)](https://arxiv.org/abs/2511.20639)\n- [Vision Wormhole](https://arxiv.org/html/2602.15382v1)\n- [Interlat](https://arxiv.org/abs/2511.09149)\n- [OBF - Latent Compression](https://arxiv.org/abs/2604.13349)\n- [Beyond Self-Talk Survey](https://arxiv.org/abs/2502.14321)\n- [Orchestration Traces Survey (May 2026)](https://arxiv.org/abs/2605.02801)\n- [LTC - Adapting LLM Agents Through Communication](https://openreview.net/forum?id=wOelVq8fwL)\n- [Yang 2016 - Hierarchical Attention Networks](https://aclanthology.org/N16-1174/)\n- [Lin 2017 - Self-Attentive Sentence Embedding](https://arxiv.org/abs/1703.03130)\n- [MAGE - Graph Contrastive Learning for Communication](https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538)\n- [ACORM - Attention-Guided Contrastive Role Representations](https://arxiv.org/abs/2312.04819)"
      }
    ],
    "totalDurationMs": 280733,
    "totalTokens": 48912,
    "totalToolUseCount": 44,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2928,
      "cache_read_input_tokens": 42049,
      "output_tokens": 3934,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2928
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3934,
          "cache_read_input_tokens": 42049,
          "cache_creation_input_tokens": 2928,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2928,
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
      "otherToolCount": 44
    }
  },
  "sourceToolAssistantUUID": "3456543d-15bf-4c69-bf07-62939dc45111",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Stop-Gradient Intent Reconstruction with Attention-Weighted Pooling fo…",
  "leafUuid": "d0bb40a7-642d-4f5f-91c8-c67b8f7a770b",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising Stop-Gradient Intent Reconstruction for text-based multi-agent communication",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b"
}
```

---

### Assistant

_source line 20 · 2026-05-10T20:58:30.878Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research findings. Let me synthesize what I've learned and decide on the revision strategy.

## Key findings from research:

### MASIA (NeurIPS 2022):
- Reconstructs **global environment state** from agent observations, NOT sender intent
- Uses self-attention over agent observations (inter-agent attention), NOT attention-weighted pooling of message tokens
- Operates in small-scale MARL (SMAC, LBF), not LLM scale
- The reviewer's claim that MASIA is a "direct precursor" is partially valid but overstated - the surface-level similarity (reconstruction + attention) obscures deep architectural differences


- Interlat takes a different approach with last-layer hidden state transfer and learned compression, achieving significant speedups on reasoning tasks like ALFWorld and MATH by replacing text with latent representations

### Novelty landscape:
Looking at the broader context, there's actually no prior work applying reconstruction loss specifically to improve text message quality in LLM-based multi-agent systems. TACTIC combines contrastive and reconstruction losses in classical MARL, but that's for continuous messages in a different setting. The attention pooling mechanism itself is standard, but the key innovation here is using token-differentiated auxiliary signals—that gap is genuine and hasn't been addressed before.

### Strategic assessment:

The strengths are clear: the problem is real and validated across multiple surveys, the contrarian angle of improving text rather than abandoning it is distinctive, and interpretability is increasingly important. But I need to be honest about the weaknesses too—each component is borrowed from existing work, there's genuine uncertainty about whether reconstruction loss can actually close the performance gap, and I shouldn't oversell the attention pooling as novel when it's standard practice.

### Decision: Major revision

I'm keeping the core problem intact—improving text communication quality in multi-agent LLM GRPO—but I need to reframe the novelty narrative. The innovation isn't the attention pooling itself; it's how the full framework uses reconstruction-based training to enable better communication between agents.

I'll add citations to MASIA and Interlat with clear differentiation: MASIA reconstructs global state in small MARL environments while SGIR targets sender intent specifically at LLM scale, operating in a completely different optimization landscape. To genuinely strengthen the novelty, I'm adding a contrastive loss component alongside reconstruction—specifically message-intent contrastive alignment where positive pairs are messages paired with the sender's actual intent, and negatives are messages paired with other agents' intents or the same agent at different timesteps. This addresses the narrow novelty gap because while CACL and TACTIC use contrastive learning in classical MARL, applying it at LLM scale for text message alignment is new. Finally, I need concrete interpretability metrics rather than vague claims—specific evaluation methods that demonstrate how the approach actually improves agent understanding.

But I'm second-guessing myself here. The reviewer feedback shows four rounds stuck at 3.2-3.5 scores, and the core issues are the narrow novelty gap and uncertain empirical impact. Adding contrastive learning helps with novelty but introduces more complexity, which could backfire if the empirical results don't justify it.

The real insight I should lean into is that latent representations can supervise text message quality—that's the genuine bridge between these two communication paradigms. Rather than getting caught up in architectural details, I should reframe this as a paradigm shift: text-based multi-agent communication improves significantly when you use latent representations as auxiliary training signals, and this creates a favorable tradeoff on the performance-interpretability frontier. The specific mechanism is just one way to instantiate this finding, but the core contribution is showing the paradigm itself works.

This means I should keep reconstruction as the natural core mechanism, drop the attention pooling as a "novel" component, and add contrastive intent alignment as an ablation variant to demonstrate the broader paradigm. The text-versus-latent Pareto frontier comparison becomes the central result. Better yet, I could frame the auxiliary objective more broadly as Intent Grounding—a family of losses that ground text messages in the sender's latent intent—which gives me flexibility to explore different instantiations while keeping the core insight front and center. The venue timing is tight—EMNLP 2026 via ARR May 25 gives only 15 days, which won't work for the experimental scope needed. The June 15 ARR deadline is more realistic with 36 days, though still compressed, and papers from that cycle can still reach EMNLP 2026 depending on commitment deadlines.

I could squeeze a minimal version into May 25 using just one benchmark and a small model with reduced ablations, but that would significantly weaken the paper. AAAI 2027 with the full experimental plan is the better call, even if it means pushing back the timeline.

Now I'm working through the major revisions, starting with renaming the approach from SGIR to Intent-Grounded Communication Training (IGCT) to better capture the core concept.

The key insight is that auxiliary intent-grounding losses—both reconstruction and contrastive variants—can improve how well agents communicate through text while maintaining interpretability. I'm planning two specific implementations: one using MSE reconstruction to recover sender intent from messages, another using InfoNCE to align messages with intent. Both will use stop-gradient and EMA for stability. The central experiment compares this against LatentMAS on a Pareto frontier showing the performance-interpretability tradeoff, and I'm adding concrete interpretability evaluation through failure diagnosis, attention-intent correlation analysis, and human correction studies. I should be upfront that attention pooling is a standard architectural choice from prior work, not a novel contribution—the novelty lies elsewhere.

Now I'm refining what makes this work novel. Looking at related approaches like CACL and TACTIC, they both use contrastive and reconstruction losses in classical MARL settings, but neither operates at LLM scale or combines these ideas with GRPO on text messages. So the real contribution is adapting these classical MARL techniques to large language model scale with proper stabilization, plus the broader paradigm of intent grounding for text communication in multi-agent GRPO systems.

The empirical results showing the text-versus-latent Pareto frontier and the interpretability advantages of text communication strengthen this significantly. I should also add LatentMAS as a training-free baseline since that's straightforward to implement.

On the gradient analysis the reviewer flagged, they're right that my claim about ∂L/∂h_j^msg ∝ α_j is incomplete—it ignores the softmax Jacobian redistribution where changes in one message's hidden state affect the attention weights for all other messages. I need to either acknowledge this is the dominant term with the redistribution being secondary, or provide the full gradient expression.

For the contrastive variant, I'm thinking through what negative samples make sense in the multi-agent LLM setting. The natural hard negatives would be pairing a message with an intent from a different agent, or the same agent's intent from a different timestep, or an intent from a different group role. Let me work out the full revised JSON with these considerations. I'm settling on the structural revisions—reframing the core problem around the paradigm gap rather than just reconstruction, emphasizing the Pareto frontier contribution, and expanding the landscape to include MASIA, Interlat, TACTIC, and CACL with more honest treatment of attention pooling. The approach now clearly distinguishes between the reconstruction and contrastive variants with concrete interpretability evaluation plans. I'm leaning toward keeping IGCT as the name since the alternatives feel forced, so let me finalize the JSON with these changes.

On the two-variant question, I think including both reconstruction and contrastive objectives actually strengthens the contribution—it demonstrates the paradigm generalizes across different loss functions rather than being tied to one specific mechanism, and the contrastive variant naturally leverages the GRPO group structure in a novel way. The extra experiments are worth it to elevate this from a single engineering choice to a broader paradigm.

Now I'm designing the interpretability evaluation. I want to test whether IGCT messages actually help humans diagnose agent failures faster and more accurately compared to baseline messages, so I'll run a study where evaluators see agent failures under three conditions: with IGCT text, with baseline text, and with opaque latent representations. I'll also measure how well the learned attention weights correlate with human-annotated important tokens, and simulate human-in-the-loop scenarios where someone reads messages and intervenes to correct plans, comparing how effective those interventions are across conditions.

I should also add OBF and Latent Agents to the related work since they're recent latent compression and multi-agent debate methods. Looking at the timeline, the ARR May 25 deadline is only 15 days away, which is extremely tight for a focused paper, whereas AAAI 2027 gives us about 83 days—that's a much more realistic window.

Actually, checking the typical ARR schedule, June 15 would be the next realistic deadline at 36 days out, which could work for a stripped-down version, but AAAI 2027 remains the better target for the full experimental scope.

Now I'll structure the JSON response. I'm also reconsidering whether Qwen3-1.7B is the right choice given its size, but it aligns with what DEPART uses and keeps things computationally feasible, so I'll stick with it.

For the benchmark suite, I'm planning ALFWorld as the primary evaluation with WebArena-Lite as a secondary option, plus Sokoban 6x6 for direct comparison against published AT-GRPO results. I'll also include LatentMAS as a baseline for the Pareto analysis on ALFWorld.

On the naming front, I think renaming from SGIR to IGCT makes more sense—it better reflects the intent grounding paradigm rather than just the stop-gradient mechanism, and it works for both the reconstruction and contrastive variants while signaling to reviewers that this is a meaningful evolution of the approach.

Now I'm working through the "narrow novelty" critique more carefully. The reviewer's concern is that this just amounts to applying stop-gradient and EMA to scale up reconstruction, with everything else being standard or borrowed. My response is stronger this time: intent grounding for text communication is genuinely novel, the two variants demonstrate it's a general paradigm rather than a one-off technique, the contrastive variant's use of GRPO group structure for negative sampling is original, the text-versus-latent Pareto frontier is a novel experimental angle, and the interpretability evaluation stands as a real contribution on its own.

I need to be more precise about related work positioning. I should clearly distinguish MASIA (global state reconstruction in small MARL) from what I'm doing (sender intent in LLM GRPO), cite TACTIC as the first to combine contrastive and reconstruction in classical MARL, acknowledge CACL for contrastive-only approaches, reference Interlat and OBF as other latent methods, and properly credit the attention pooling lineage. Now I'm putting together the complete JSON response with all these distinctions laid out.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0bb40a7-642d-4f5f-91c8-c67b8f7a770b",
  "isSidechain": false,
  "requestId": "req_011CauZDkEoESN3DixsQ1pWy",
  "type": "assistant",
  "uuid": "1e140ee8-7427-4933-a91a-4f37d4d81135",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WGBsgJgmpqdThRSYwaPpf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4433,
      "cache_read_input_tokens": 33217,
      "output_tokens": 5055,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4433,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5055,
          "cache_read_input_tokens": 33217,
          "cache_creation_input_tokens": 4433,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4433
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T20:58:30.880Z_

Now let me search for one more critical piece - whether there's any very recent work (May 2026) that might affect the landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e140ee8-7427-4933-a91a-4f37d4d81135",
  "isSidechain": false,
  "requestId": "req_011CauZDkEoESN3DixsQ1pWy",
  "type": "assistant",
  "uuid": "d3b0a912-9659-4533-8164-a28b798330b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WGBsgJgmpqdThRSYwaPpf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4433,
      "cache_read_input_tokens": 33217,
      "output_tokens": 5055,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4433,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5055,
          "cache_read_input_tokens": 33217,
          "cache_creation_input_tokens": 4433,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4433
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-10T20:58:37.744Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019ApNE5899tVNiCwDWc86k5`</summary>

```json
{
  "description": "Search recent May 2026 multi-agent LLM communication",
  "prompt": "Search for very recent papers (April-May 2026) on multi-agent LLM communication, especially anything that might be concurrent work to a method that uses auxiliary losses to improve text-based inter-agent communication quality.\n\nUse WebSearch for:\n1. \"multi-agent LLM communication training 2026\" \n2. \"text communication reward shaping multi-agent language model\"\n3. \"arXiv 2605 multi-agent communication language model\"\n4. \"OBF orthogonal backfill latent multi-agent\" (arXiv 2604.13349)\n5. \"Latent Agents arXiv 2604.24881\"\n\nFor each relevant result, use WebFetch to read the abstract. I need to know if anyone has published work in May 2026 that:\n- Uses auxiliary losses (reconstruction, contrastive, or otherwise) for text communication quality in multi-agent LLM systems\n- Bridges the text-latent communication gap\n- Provides token-level or sub-message credit assignment\n\nReport concisely - just the title, key idea, and relevance assessment for each paper found.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3b0a912-9659-4533-8164-a28b798330b1",
  "isSidechain": false,
  "requestId": "req_011CauZDkEoESN3DixsQ1pWy",
  "type": "assistant",
  "uuid": "8badb5d8-17da-4cc1-9dfd-7bdba26d1026",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WGBsgJgmpqdThRSYwaPpf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4433,
      "cache_read_input_tokens": 33217,
      "output_tokens": 5055,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4433,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5055,
          "cache_read_input_tokens": 33217,
          "cache_creation_input_tokens": 4433,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4433
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Stop-Gradient Intent Reconstruction with Attention-Weighted Pooling fo…",
  "leafUuid": "8badb5d8-17da-4cc1-9dfd-7bdba26d1026",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising Stop-Gradient Intent Reconstruction for text-based multi-agent communication",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b"
}
```

---

### Tool result

_source line 25 · 2026-05-10T21:01:47.925Z_

<details><summary>↩ Tool result · `toolu_019ApNE5899tVNiCwDWc86k5`</summary>

```text
I now have a thorough picture. Here is the consolidated report.

---

## Concurrent Work Survey: Multi-Agent LLM Communication (April-May 2026)

I searched across five query strategies and fetched abstracts for all relevant papers. Below are the findings organized by relevance to your three criteria: (1) auxiliary losses for text communication quality, (2) bridging the text-latent gap, and (3) token/sub-message credit assignment.

---

### HIGHLY RELEVANT -- Direct Overlap Risk

**1. Interlat: Enabling Agents to Communicate Entirely in Latent Space**
- arXiv: 2511.09149 (Nov 2025, but under review / actively cited in 2026)
- Authors: Du, Wang, Bai, Cao, Zhu, Zheng, Chen, Ying (Zhejiang U / Alibaba)
- **Key idea:** Agents communicate via last-hidden-state "mind" representations instead of text. Uses multiple auxiliary losses: a **Conditional Mind Separation Loss** (Jensen-Shannon divergence ensuring agents exploit task-relevant info), a **Plan-Alignment Regulation** (KL + cosine aligning latent predictions to language-space plans), and a **Latent Direction Alignment** loss for compression. Curriculum learning progressively replaces text with latent communication.
- **Relevance: HIGH.** This directly addresses the text-latent communication gap using auxiliary losses (reconstruction-flavored alignment + contrastive-flavored separation). If your method uses auxiliary losses to improve text-based communication, this is the closest concurrent work, though Interlat abandons text entirely rather than improving it.

**2. The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems**
- arXiv: 2602.15382 (Feb 2026)
- Authors: Liu, Zhang, Yu, Xiong, He, Wu, Jung, Fredrikson, Wang, Gao (Purdue / CMU / Georgia Tech)
- **Key idea:** Encodes reasoning traces as visual codes injected into VLM vision pathways. Uses a **label-free distillation objective** with three components: hidden-state matching (L2), KL-divergence over logits, and RMS magnitude regularization. Text communication is the "teacher," latent visual channel is the "student."
- **Relevance: HIGH.** Directly bridges text-latent communication with auxiliary distillation losses. Different modality (vision pathway) but the core idea of using reconstruction/alignment losses to transfer text-quality communication into a latent channel is very close.

**3. C3: Contextual Counterfactual Credit Assignment for Multi-Agent RL in LLM Collaboration**
- arXiv: 2603.06859 (March 2026)
- Authors: Chen, Sun, Wang, Zhang, Shen, Li, Zhang
- **Key idea:** Message-level counterfactual credit assignment. Freezes transcript context, evaluates context-matched alternatives via fixed-continuation replay, applies leave-one-out baseline to isolate causal impact of individual messages. Produces unbiased, low-variance marginal advantages for policy gradient.
- **Relevance: HIGH for sub-message credit assignment.** This is the closest work to token/message-level credit assignment for inter-agent communication. It operates at the message level rather than token level, but directly addresses which communications caused outcomes.

---

### MODERATELY RELEVANT -- Related but Different Angle

**4. RecursiveMAS: Recursive Multi-Agent Systems**
- arXiv: 2604.25917 (April 28, 2026)
- Authors: Yang, Zou, Pan, Qiu, Lu, Diao, Jiang, Tong, Zhang, Buehler, He, Zou
- **Key idea:** Casts multi-agent collaboration as unified latent-space recursive computation via "RecursiveLink" module. Uses **shared gradient-based credit assignment** across recursion rounds with inner-outer loop co-optimization.
- **Relevance: MODERATE.** Operates entirely in latent space (bypasses text) with gradient-based credit, but no auxiliary losses for communication quality per se. The credit assignment is system-level, not message-level.

**5. When Less Latent Leads to Better Relay (OBF)**
- arXiv: 2604.13349 (April 14, 2026)
- Authors: Li, An, Du (UC Merced)
- **Key idea:** Orthogonal Backfill (OBF) for KV-cache compression in latent multi-agent LLM collaboration. Decomposes deleted KV values into in-span and orthogonal residual components, injects low-rank residual back. Achieves 79-89% communication cost reduction while maintaining or improving quality on 7/9 benchmarks.
- **Relevance: MODERATE.** Information-preserving compression for latent communication, but no learned auxiliary losses -- it is a geometric/algebraic method. Relevant as it addresses communication fidelity in the latent channel.

**6. Latent Agents: A Post-Training Procedure for Internalized Multi-Agent Debate**
- arXiv: 2604.24881 (April 27, 2026)
- Authors: Yi, Mueller, Lee (Boston U)
- **Key idea:** Distills multi-agent debate into a single LLM via two-stage fine-tuning with dynamic reward scheduling and length clipping. Internalization creates agent-specific subspaces in activation space. 93% token reduction.
- **Relevance: MODERATE.** Collapses multi-agent text communication into latent representations within one model. Uses reward scheduling (not auxiliary reconstruction/contrastive losses). More about eliminating inter-agent communication than improving it.

**7. RL for LLM-based Multi-Agent Systems through Orchestration Traces**
- arXiv: 2605.02801 (May 4, 2026)
- Authors: Zhang
- **Key idea:** Taxonomy/survey of credit assignment in LLM multi-agent RL. Identifies 8 credit-bearing units (token to team level). Notes that **"explicit counterfactual message-level credit remains especially sparse"** in the literature -- flags this as an open problem.
- **Relevance: MODERATE.** Confirms the gap your work may fill. Useful to cite as evidence that message-level credit assignment is under-explored.

---

### LOWER RELEVANCE -- Tangential

**8. TACTIC: Task-Agnostic Contrastive Pre-Training for Inter-Agent Communication** (AAMAS 2025)
- Authors: Yu, Mishra, Zaidi, Tokekar (U Maryland)
- Uses **contrastive losses + reconstruction loss + dynamics loss** for communication pre-training, but in traditional MARL (not LLM agents). The loss structure (L_total = L_supcon + alpha*L_recon + beta*L_dyn) is quite similar to what you describe, but the agents are small networks, not LLMs.
- **Relevance: LOW-MODERATE.** Methodologically close (auxiliary losses for communication) but different setting (non-LLM MARL).

**9. Communicating Activations Between Language Model Agents** (Jan 2025)
- Authors: Ramesh, Li (Harvard/Kempner)
- Agents share mid-forward-pass activations with MSE-trained linear projection. No auxiliary losses beyond the projection training.
- **Relevance: LOW.** Latent communication but minimal training signal story.

**10. LatentMAS: Latent Collaboration in Multi-Agent Systems** (ICML 2026 Spotlight)
- arXiv: 2511.20639
- **Training-free** framework using KV-cache sharing. No learned losses.
- **Relevance: LOW.** Establishes the latent communication paradigm but is explicitly training-free.

**11. CORE: Measuring Multi-Agent LLM Interaction Quality** (EACL 2026)
- A diagnostic metric (cluster entropy, lexical repetition, semantic similarity) for evaluating dialog quality in game-theoretic multi-agent settings. Not a training method.
- **Relevance: LOW.** Evaluation-side only.

**12. LATTE: Improving Efficiency of Language Agent Teams** (May 7, 2026)
- Graph-based coordination framework. No learned communication losses.
- **Relevance: LOW.** Coordination, not communication training.

---

### Summary Assessment

**No paper found in the April-May 2026 window that exactly matches your method** (auxiliary losses to improve *text-based* inter-agent communication in LLM systems with token-level credit assignment). The closest concurrent risks are:

- **Interlat** uses auxiliary losses (separation, alignment) but to *replace* text with latent communication, not improve text.
- **Vision Wormhole** uses distillation losses to bridge text-to-latent but through a visual modality.
- **C3** does message-level credit assignment but without auxiliary communication losses.
- **RecursiveMAS** does gradient-based credit in latent space but at system level.

The combination of (a) keeping text as the communication medium, (b) using auxiliary losses to improve its quality, and (c) providing token/sub-message credit assignment appears to be a distinct and uncovered position in this literature. The 2605.02801 survey explicitly flags message-level credit as "especially sparse," which supports novelty.

Sources:
- [Interlat](https://arxiv.org/abs/2511.09149)
- [Vision Wormhole](https://arxiv.org/abs/2602.15382)
- [C3 Counterfactual Credit](https://arxiv.org/abs/2603.06859)
- [RecursiveMAS](https://arxiv.org/abs/2604.25917)
- [OBF / When Less Latent](https://arxiv.org/abs/2604.13349)
- [Latent Agents](https://arxiv.org/abs/2604.24881)
- [RL for MAS via Orchestration Traces](https://arxiv.org/abs/2605.02801)
- [TACTIC](https://arxiv.org/abs/2501.02174)
- [Communicating Activations](https://arxiv.org/abs/2501.14082)
- [LatentMAS](https://arxiv.org/abs/2511.20639)
- [CORE](https://aclanthology.org/2026.eacl-long.57/)
- [LATTE](https://arxiv.org/abs/2605.06320)
- [Rethinking Token-Level Credit (EAPO)](https://arxiv.org/abs/2604.11056)
- [Why Do AI Agents Communicate in Human Language](https://arxiv.org/abs/2506.02739)
- [From Reasoning to Agentic: Credit Assignment Survey](https://arxiv.org/abs/2604.09459)

agentId: ae034d59b5251667f (use SendMessage with to: 'ae034d59b5251667f' to continue this agent)
&lt;usage>total_tokens: 34795
tool_uses: 31
duration_ms: 190175&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8badb5d8-17da-4cc1-9dfd-7bdba26d1026",
  "isSidechain": false,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "type": "user",
  "uuid": "dfe682ab-0959-463a-97d0-3df3135e01ce",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for very recent papers (April-May 2026) on multi-agent LLM communication, especially anything that might be concurrent work to a method that uses auxiliary losses to improve text-based inter-agent communication quality.\n\nUse WebSearch for:\n1. \"multi-agent LLM communication training 2026\" \n2. \"text communication reward shaping multi-agent language model\"\n3. \"arXiv 2605 multi-agent communication language model\"\n4. \"OBF orthogonal backfill latent multi-agent\" (arXiv 2604.13349)\n5. \"Latent Agents arXiv 2604.24881\"\n\nFor each relevant result, use WebFetch to read the abstract. I need to know if anyone has published work in May 2026 that:\n- Uses auxiliary losses (reconstruction, contrastive, or otherwise) for text communication quality in multi-agent LLM systems\n- Bridges the text-latent communication gap\n- Provides token-level or sub-message credit assignment\n\nReport concisely - just the title, key idea, and relevance assessment for each paper found.",
    "agentId": "ae034d59b5251667f",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a thorough picture. Here is the consolidated report.\n\n---\n\n## Concurrent Work Survey: Multi-Agent LLM Communication (April-May 2026)\n\nI searched across five query strategies and fetched abstracts for all relevant papers. Below are the findings organized by relevance to your three criteria: (1) auxiliary losses for text communication quality, (2) bridging the text-latent gap, and (3) token/sub-message credit assignment.\n\n---\n\n### HIGHLY RELEVANT -- Direct Overlap Risk\n\n**1. Interlat: Enabling Agents to Communicate Entirely in Latent Space**\n- arXiv: 2511.09149 (Nov 2025, but under review / actively cited in 2026)\n- Authors: Du, Wang, Bai, Cao, Zhu, Zheng, Chen, Ying (Zhejiang U / Alibaba)\n- **Key idea:** Agents communicate via last-hidden-state \"mind\" representations instead of text. Uses multiple auxiliary losses: a **Conditional Mind Separation Loss** (Jensen-Shannon divergence ensuring agents exploit task-relevant info), a **Plan-Alignment Regulation** (KL + cosine aligning latent predictions to language-space plans), and a **Latent Direction Alignment** loss for compression. Curriculum learning progressively replaces text with latent communication.\n- **Relevance: HIGH.** This directly addresses the text-latent communication gap using auxiliary losses (reconstruction-flavored alignment + contrastive-flavored separation). If your method uses auxiliary losses to improve text-based communication, this is the closest concurrent work, though Interlat abandons text entirely rather than improving it.\n\n**2. The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems**\n- arXiv: 2602.15382 (Feb 2026)\n- Authors: Liu, Zhang, Yu, Xiong, He, Wu, Jung, Fredrikson, Wang, Gao (Purdue / CMU / Georgia Tech)\n- **Key idea:** Encodes reasoning traces as visual codes injected into VLM vision pathways. Uses a **label-free distillation objective** with three components: hidden-state matching (L2), KL-divergence over logits, and RMS magnitude regularization. Text communication is the \"teacher,\" latent visual channel is the \"student.\"\n- **Relevance: HIGH.** Directly bridges text-latent communication with auxiliary distillation losses. Different modality (vision pathway) but the core idea of using reconstruction/alignment losses to transfer text-quality communication into a latent channel is very close.\n\n**3. C3: Contextual Counterfactual Credit Assignment for Multi-Agent RL in LLM Collaboration**\n- arXiv: 2603.06859 (March 2026)\n- Authors: Chen, Sun, Wang, Zhang, Shen, Li, Zhang\n- **Key idea:** Message-level counterfactual credit assignment. Freezes transcript context, evaluates context-matched alternatives via fixed-continuation replay, applies leave-one-out baseline to isolate causal impact of individual messages. Produces unbiased, low-variance marginal advantages for policy gradient.\n- **Relevance: HIGH for sub-message credit assignment.** This is the closest work to token/message-level credit assignment for inter-agent communication. It operates at the message level rather than token level, but directly addresses which communications caused outcomes.\n\n---\n\n### MODERATELY RELEVANT -- Related but Different Angle\n\n**4. RecursiveMAS: Recursive Multi-Agent Systems**\n- arXiv: 2604.25917 (April 28, 2026)\n- Authors: Yang, Zou, Pan, Qiu, Lu, Diao, Jiang, Tong, Zhang, Buehler, He, Zou\n- **Key idea:** Casts multi-agent collaboration as unified latent-space recursive computation via \"RecursiveLink\" module. Uses **shared gradient-based credit assignment** across recursion rounds with inner-outer loop co-optimization.\n- **Relevance: MODERATE.** Operates entirely in latent space (bypasses text) with gradient-based credit, but no auxiliary losses for communication quality per se. The credit assignment is system-level, not message-level.\n\n**5. When Less Latent Leads to Better Relay (OBF)**\n- arXiv: 2604.13349 (April 14, 2026)\n- Authors: Li, An, Du (UC Merced)\n- **Key idea:** Orthogonal Backfill (OBF) for KV-cache compression in latent multi-agent LLM collaboration. Decomposes deleted KV values into in-span and orthogonal residual components, injects low-rank residual back. Achieves 79-89% communication cost reduction while maintaining or improving quality on 7/9 benchmarks.\n- **Relevance: MODERATE.** Information-preserving compression for latent communication, but no learned auxiliary losses -- it is a geometric/algebraic method. Relevant as it addresses communication fidelity in the latent channel.\n\n**6. Latent Agents: A Post-Training Procedure for Internalized Multi-Agent Debate**\n- arXiv: 2604.24881 (April 27, 2026)\n- Authors: Yi, Mueller, Lee (Boston U)\n- **Key idea:** Distills multi-agent debate into a single LLM via two-stage fine-tuning with dynamic reward scheduling and length clipping. Internalization creates agent-specific subspaces in activation space. 93% token reduction.\n- **Relevance: MODERATE.** Collapses multi-agent text communication into latent representations within one model. Uses reward scheduling (not auxiliary reconstruction/contrastive losses). More about eliminating inter-agent communication than improving it.\n\n**7. RL for LLM-based Multi-Agent Systems through Orchestration Traces**\n- arXiv: 2605.02801 (May 4, 2026)\n- Authors: Zhang\n- **Key idea:** Taxonomy/survey of credit assignment in LLM multi-agent RL. Identifies 8 credit-bearing units (token to team level). Notes that **\"explicit counterfactual message-level credit remains especially sparse\"** in the literature -- flags this as an open problem.\n- **Relevance: MODERATE.** Confirms the gap your work may fill. Useful to cite as evidence that message-level credit assignment is under-explored.\n\n---\n\n### LOWER RELEVANCE -- Tangential\n\n**8. TACTIC: Task-Agnostic Contrastive Pre-Training for Inter-Agent Communication** (AAMAS 2025)\n- Authors: Yu, Mishra, Zaidi, Tokekar (U Maryland)\n- Uses **contrastive losses + reconstruction loss + dynamics loss** for communication pre-training, but in traditional MARL (not LLM agents). The loss structure (L_total = L_supcon + alpha*L_recon + beta*L_dyn) is quite similar to what you describe, but the agents are small networks, not LLMs.\n- **Relevance: LOW-MODERATE.** Methodologically close (auxiliary losses for communication) but different setting (non-LLM MARL).\n\n**9. Communicating Activations Between Language Model Agents** (Jan 2025)\n- Authors: Ramesh, Li (Harvard/Kempner)\n- Agents share mid-forward-pass activations with MSE-trained linear projection. No auxiliary losses beyond the projection training.\n- **Relevance: LOW.** Latent communication but minimal training signal story.\n\n**10. LatentMAS: Latent Collaboration in Multi-Agent Systems** (ICML 2026 Spotlight)\n- arXiv: 2511.20639\n- **Training-free** framework using KV-cache sharing. No learned losses.\n- **Relevance: LOW.** Establishes the latent communication paradigm but is explicitly training-free.\n\n**11. CORE: Measuring Multi-Agent LLM Interaction Quality** (EACL 2026)\n- A diagnostic metric (cluster entropy, lexical repetition, semantic similarity) for evaluating dialog quality in game-theoretic multi-agent settings. Not a training method.\n- **Relevance: LOW.** Evaluation-side only.\n\n**12. LATTE: Improving Efficiency of Language Agent Teams** (May 7, 2026)\n- Graph-based coordination framework. No learned communication losses.\n- **Relevance: LOW.** Coordination, not communication training.\n\n---\n\n### Summary Assessment\n\n**No paper found in the April-May 2026 window that exactly matches your method** (auxiliary losses to improve *text-based* inter-agent communication in LLM systems with token-level credit assignment). The closest concurrent risks are:\n\n- **Interlat** uses auxiliary losses (separation, alignment) but to *replace* text with latent communication, not improve text.\n- **Vision Wormhole** uses distillation losses to bridge text-to-latent but through a visual modality.\n- **C3** does message-level credit assignment but without auxiliary communication losses.\n- **RecursiveMAS** does gradient-based credit in latent space but at system level.\n\nThe combination of (a) keeping text as the communication medium, (b) using auxiliary losses to improve its quality, and (c) providing token/sub-message credit assignment appears to be a distinct and uncovered position in this literature. The 2605.02801 survey explicitly flags message-level credit as \"especially sparse,\" which supports novelty.\n\nSources:\n- [Interlat](https://arxiv.org/abs/2511.09149)\n- [Vision Wormhole](https://arxiv.org/abs/2602.15382)\n- [C3 Counterfactual Credit](https://arxiv.org/abs/2603.06859)\n- [RecursiveMAS](https://arxiv.org/abs/2604.25917)\n- [OBF / When Less Latent](https://arxiv.org/abs/2604.13349)\n- [Latent Agents](https://arxiv.org/abs/2604.24881)\n- [RL for MAS via Orchestration Traces](https://arxiv.org/abs/2605.02801)\n- [TACTIC](https://arxiv.org/abs/2501.02174)\n- [Communicating Activations](https://arxiv.org/abs/2501.14082)\n- [LatentMAS](https://arxiv.org/abs/2511.20639)\n- [CORE](https://aclanthology.org/2026.eacl-long.57/)\n- [LATTE](https://arxiv.org/abs/2605.06320)\n- [Rethinking Token-Level Credit (EAPO)](https://arxiv.org/abs/2604.11056)\n- [Why Do AI Agents Communicate in Human Language](https://arxiv.org/abs/2506.02739)\n- [From Reasoning to Agentic: Credit Assignment Survey](https://arxiv.org/abs/2604.09459)"
      }
    ],
    "totalDurationMs": 190175,
    "totalTokens": 34795,
    "totalToolUseCount": 31,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 584,
      "cache_read_input_tokens": 31561,
      "output_tokens": 2649,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 584
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2649,
          "cache_read_input_tokens": 31561,
          "cache_creation_input_tokens": 584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 584,
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
      "otherToolCount": 31
    }
  },
  "sourceToolAssistantUUID": "8badb5d8-17da-4cc1-9dfd-7bdba26d1026",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-10T21:03:21.609Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent. Now I have comprehensive research findings. Let me synthesize everything and make my decision.

## Summary of research findings:

### MASIA (NeurIPS 2022):
- Reconstructs **global environment state** from agent observations (NOT sender intent)
- Self-attention over agent observation vectors (NOT token-level attention within messages)
- Small MARL (SMAC, LBF), not LLM scale
- Must cite but differentiation is clear and strong

### Interlat (ACL 2026):
- Last-layer hidden state transfer with learned compression (24x)
- Uses auxiliary losses (separation + alignment) but replaces text entirely


- Evaluated on ALFWorld, MATH

### Contrastive in MARL:
- CACL (2024): Contrastive on continuous messages in classical MARL
- TACTIC (AAMAS 2025): Contrastive + reconstruction + dynamics in classical MARL
- Neither operates at LLM scale or on text messages

### Novelty confirmation:
- Exhaustive search confirms NO existing work uses auxiliary losses for text message quality in LLM multi-agent GRPO
- May 2026 orchestration traces survey explicitly flags message-level credit as "especially sparse"
- The gap is genuine and confirmed

### Attention pool
Attention mechanisms have been standard since Yang 2016 and Lin 2017, so I shouldn't position this as a novel contribution. Now I'm reviewing the concurrent works I need to cite: MASIA, Interlat, TACTIC, CACL, OBF, Latent Agents, LATTE, and Vision Wormhole all came out around the same timeframe.

The core idea is solid and addresses a real gap, but the current framing and approach need substantial work to move beyond just combining existing techniques. I'm planning a major revision that includes renaming the method to Intent-Grounded Communication Training to better capture what we're actually doing, and elevating the conceptual contribution beyond the engineering aspects.

The key changes involve introducing two distinct variants—one based on reconstruction and another using contrastive learning with group negatives—and making the text-versus-latent Pareto frontier a central result. I'm also adding a concrete interpretability evaluation protocol as a first-class contribution rather than an afterthought. For baselines, I need to include LatentMAS directly for fair comparison, and I should show how this approach composes orthogonally with message-level credit assignment methods like C3.

Now I'm thinking through the contrastive variant more carefully. In GRPO, we sample multiple completions for the same prompt, and in the multi-agent case, each completion involves an agent generating a message with a particular intent, then the team producing a response. So across the group samples, the same agent has different intents and generates different messages, creating natural negative pairs within the group structure itself.

The key insight is that in-group negatives—pairing a message with a different intent from the same agent on the same prompt—are particularly hard negatives because they force the model to discriminate between specific intents rather than just recognizing generic task relevance. This is something CACL and TACTIC can't leverage because they don't have access to group-relative sampling, so this feels like a genuinely novel contribution tied specifically to GRPO's structure.

Now I'm planning the experimental setup: keeping the core benchmarks (ALFWorld, WebArena-Lite, and Sokoban 6x6 for controlled comparisons), then adding a training-free LatentMAS comparison and an interpretability study. The contrastive variant will increase compute slightly, but since LatentMAS doesn't require training, the GPU overhead stays manageable—mostly concentrated in the ALFWorld experiments with both the regular and contrastive versions plus ablations.

For the ablations, I'm keeping the key ones that test necessity at scale: the stop-gradient and EMA mechanism, different EMA decay rates, the annealing schedule, and comparing the regular versus contrastive variants. The pooling ablation feels less critical, so I'm thinking about swapping that out for something more informative.

Actually, I'll keep the pooling comparison but reframe it as validating an architectural choice rather than claiming it as a novel contribution. Now I need to write out the JSON response carefully, making sure each reviewer concern gets a direct answer: adding the MASIA citation with clear differentiation, honestly reframing the attention pooling claims and fixing the gradient statement, including Interlat in the related work, strengthening the novelty argument through the paradigm shift and contrastive variant, and addressing the empirical impact question with Pareto frontier analysis and concrete interpretability results.

For the title, the current version is too mechanism-heavy. I'm considering something like "Intent Grounding for Trainable Text Communication in Multi-Agent Language Model Systems" or "Bridging Text and Latent Communication in Multi-Agent GRPO via Intent Grounding" — something that emphasizes the core problem we're solving rather than listing every technical component.

Actually, "Intent-Grounded Communication Training for Multi-Agent GRPO: Bridging the Text-Latent Performance Gap" works well because it clearly signals what we're doing, where, and why.

Now I'm thinking through the reviewer's concern about modest gains — if IGCT only achieves 2-3% improvement versus latent methods at 14-26%, the Pareto argument becomes crucial: we're trading some performance for interpretability and trainability, which has real value.

For the two variants, IGCT-R should be the main method since it's more directly aligned with the intent grounding intuition and connects better to classical MARL work.  IGCT-C can be framed as testing whether the paradigm generalizes across different loss functions, with its performance relative to IGCT-R being informative either way. I'll keep the project name as is and now consider the reviewer's suggestion about running a direct text-vs-latent comparison on ALFWorld using LatentMAS and SGIR, since that benchmark was also used for Interlat.

I'm settling on comparing our reconstruction and contrastive variants against LatentMAS as the training-free latent baseline, since getting Interlat's code might be difficult. LatentMAS should work with the planner-executor setup by having the planner share its hidden state with the executor, which is a straightforward adaptation. Now I'll write out the full JSON.

Structuring the project proposal...

**title**: "Intent-Grounded Communication Training for Multi-Agent GRPO: Bridging the Text-Latent Performance Gap"

**core_problem**: There's a clear split in the field—latent-based methods are pulling ahead with 8-27% gains by sidestepping text entirely, while text-focused RL and credit assignment approaches haven't figured out how to improve message quality. Classical MARL showed that reconstruction and contrastive objectives can ground communication effectively, and MASIA demonstrated this with attention-based aggregation, but those worked in simpler continuous-state spaces. The real question is whether intent-grounding auxiliary losses can work in the LLM-GRPO setting, where we're dealing with high-dimensional hidden states, moving targets from LoRA, and group-level optimization—and whether we can do this while keeping the interpretability that text provides.

**opportunity**: &lt;describe the paradigm gap and why now is the right time>

**landscape**: &lt;comprehensive, including MASIA, Interlat, TACTIC, CACL, OBF, etc.>

**approach**: &lt;IGCT with two variants, Pareto comparison, interpretability study>

I'm settling on the title and structuring the full writeup as a JSON response to keep everything organized.

Let me finalize the title. "Intent-Grounded Communication Training: Closing the Text-Latent Gap in Multi-Agent GRPO" captures both the core contribution and the positioning against latent communication approaches.

Now I need to make sure I'm directly addressing each reviewer concern: explicitly positioning MASIA in the landscape with clear differentiation, being honest that attention pooling is standard practice rather than novel, including Interlat in the related work, framing the novelty around the paradigm shift plus the contrastive variant with GRPO-specific negatives, using Pareto comparisons and interpretability analysis to demonstrate concrete impact, and acknowledging the venue timing with ARR June 15 as an aggressive option.

For the gradient analysis fix, I'm working through how to incorporate that into the methodology section.

Generating the final JSON output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfe682ab-0959-463a-97d0-3df3135e01ce",
  "isSidechain": false,
  "requestId": "req_011CauZd2w2cakNs61fTwW2w",
  "type": "assistant",
  "uuid": "42107ee3-8c93-4304-b37d-a732a5375247",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bLFB8X9MyWPKsyjx87BNA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7766,
      "cache_read_input_tokens": 37650,
      "output_tokens": 11552,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7766,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11552,
          "cache_read_input_tokens": 37650,
          "cache_creation_input_tokens": 7766,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7766
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-10T21:06:13.567Z_

Now I have comprehensive research. Let me synthesize the findings and make a strategic decision.

## Key Research Findings

1. **MASIA (NeurIPS 2022)** reconstructs *global environment state* from agent observations, not sender intent. Uses inter-agent self-attention over observation vectors, not token-level attention within messages. Small-scale MARL (SMAC). The reviewer's claim of "direct precursor" is partially valid but overstated — surface similarity in "reconstruction + attention" obscures deep architectural differences.

2. **Interlat (ACL 2026)** uses hidden-state transfer with learned compression (24x). Uses separation + alignment auxiliary losses but replaces text entirely.

3. **TACTIC (AAMAS 2025)** combines contrastive + reconstruction for communication in classical MARL — the closest methodological precedent, but non-LLM.

4. **The gap is confirmed genuine**: exhaustive search finds NO work using auxiliary losses for text message quality in LLM multi-agent GRPO. The May 2026 orchestration traces survey explicitly flags message-level credit as "especially sparse."

5. **Attention pooling** is indeed standard (Yang 2016, Lin 2017) — claiming it as novel was a mistake.

Given the stagnation (4 rounds, scores 3.2→3.5), I'm doing a **major revision** that reframes from "one mechanism" to "a paradigm with two variants," adds a genuinely novel contrastive component leveraging GRPO group structure, and makes the text-vs-latent Pareto comparison a central contribution.

```json
{
  "title": "Intent-Grounded Communication Training: Closing the Text-Latent Performance Gap in Multi-Agent GRPO",
  "core_problem": "Recent latent-communication methods (LatentMAS, ICML 2026; RecursiveMAS, April 2026; DiffMAS, April 2026; Interlat, ACL 2026) achieve 8–27% accuracy gains by replacing text with hidden-state or KV-cache transfers, but sacrifice human interpretability, debuggability, and human-in-the-loop interoperability. Text-based multi-agent GRPO methods (AT-GRPO, MAGRPO) and credit assignment approaches (C3, CCPO, CoFi-PGMA) optimize task reward or agent/message-level credit without training message quality directly. Classical MARL has shown that communication can be grounded via reconstruction (Lin et al., NeurIPS 2021), attention-based aggregation combined with state reconstruction (MASIA, NeurIPS 2022), and contrastive alignment (CACL 2024; TACTIC, AAMAS 2025) — but all operate on continuous-vector messages in small-scale agents (state dim ~10–100). Can the paradigm of intent grounding — training messages to faithfully convey sender intent via auxiliary losses — be adapted to work at LLM scale under GRPO optimization, closing the text-latent performance gap while preserving the interpretability advantages of text communication?",
  "opportunity": "The multi-agent LLM communication landscape has bifurcated into two families that each leave a critical gap. Latent methods (LatentMAS, RecursiveMAS, DiffMAS, Interlat, OBF) achieve superior performance but produce opaque communication channels unsuitable for safety-critical deployment, human oversight, or debugging — a concern increasingly raised in the LLM safety community. Text-based RL methods (AT-GRPO, MAGRPO, C3, CCPO) preserve interpretability but leave message quality to emerge implicitly from sparse task reward. In classical MARL, Lin et al. (NeurIPS 2021) showed reconstruction grounds communication, MASIA (NeurIPS 2022) combined reconstruction with attention-based aggregation for state estimation, and TACTIC (AAMAS 2025) demonstrated contrastive + reconstruction pre-training improves communication quality. However, scaling these ideas to LLM-scale multi-agent GRPO introduces distinct challenges absent in classical settings: (a) hidden states are high-dimensional (2048+), requiring feasible reconstruction targets; (b) LoRA adapter updates create continuously shifting representation spaces; (c) GRPO's group-relative advantage normalization creates optimization dynamics qualitatively different from QMIX/A3C/PPO in classical MARL. We propose Intent-Grounded Communication Training (IGCT), a paradigm for making text communication trainable at LLM scale. IGCT provides two complementary auxiliary loss variants — reconstruction-based (IGCT-R) and contrastive (IGCT-C) — both using stop-gradient isolation and EMA target stabilization grounded in EMA-PG stability theory (Zhang & Ba, Feb 2026). Critically, IGCT-C leverages GRPO's group sampling structure for hard negative mining, a technique unavailable to classical MARL methods. We characterize the performance-interpretability Pareto frontier by directly comparing IGCT against both text-only baselines and training-free latent communication (LatentMAS), and provide concrete interpretability evidence through failure diagnosis studies and human-in-the-loop intervention experiments. This is timely because PettingLLMs provides multi-agent GRPO infrastructure, DEPART/HIMPO establishes planner-executor benchmarks, and the May 2026 orchestration traces survey (Zhang, arXiv 2605.02801) explicitly identifies message-level credit as 'especially sparse' — confirming the gap our work fills.",
  "landscape": "**Latent communication (bypass text):** LatentMAS (ICML 2026 Spotlight, arXiv 2511.20639) enables training-free latent collaboration via shared working memory of last-layer hidden embeddings, achieving +14.6% accuracy and 70–83% token reduction across 9 benchmarks. RecursiveMAS (April 2026, arXiv 2604.25917) trains lightweight RecursiveLink modules for cross-agent latent state transfer with inner-outer loop optimization, achieving +8.3% accuracy with 2.4x speedup. DiffMAS (April 2026, arXiv 2604.21794) optimizes inter-agent communication end-to-end via KV-cache trace construction, achieving +26.7% on AIME24. Interlat (ACL 2026, arXiv 2511.09149) transfers last-layer hidden states with learned compression (128→8 tokens, 24x speedup) using auxiliary separation and alignment losses; evaluated on ALFWorld and MATH. OBF (April 2026, arXiv 2604.13349) achieves 79–89% latent communication cost reduction via orthogonal backfill compression. Latent Agents (April 2026, arXiv 2604.24881) internalizes multi-agent debate into one model's latent space. Vision Wormhole (Feb 2026, arXiv 2602.15382) distills text communication into visual latent channels. All bypass or replace text communication entirely. **Text-based multi-agent GRPO (task reward only):** AT-GRPO/Stronger-MAS (ICLR 2026) achieves 96–99.5% on cooperative planning and 84% improvement on Sokoban 6x6 via agent-and-turn-wise GRPO. MAGRPO (AAAI 2026) trains multi-agent writing/coding without communication losses. Graph-GRPO (March 2026) optimizes topology, not message content. **Credit assignment (agent/message-level scalar signal):** C3 (March 2026, arXiv 2603.06859) provides message-level counterfactual credit via fixed-continuation replay. CCPO (March 2026, arXiv 2603.21563) estimates marginal contributions through counterfactual baselines. CoFi-PGMA (April 2026, arXiv 2604.22785) derives leave-one-out difference rewards. Dr. MAS (Feb 2026, arXiv 2602.08847) stabilizes multi-agent GRPO via agent-wise advantage normalization. All provide scalar credit signals without within-message token differentiation or communication-quality auxiliary objectives. **Communication auxiliary losses in classical MARL:** Lin et al. (NeurIPS 2021) showed autoencoder reconstruction of sender observations grounds communication in small networks. MASIA (NeurIPS 2022, Guan et al.) combined global-state reconstruction with attention-based message aggregation and multi-step prediction in a self-supervised framework for small MARL (SMAC, LBF); however, MASIA reconstructs the environment's global state from agent observation vectors (a state estimation problem), not sender communicative intent from text tokens (a grounding problem), and operates at fundamentally different scale (state dim ~50–200 vs. LLM hidden dim 2048+). TACTIC (AAMAS 2025, Yu et al.) pre-trains communication via contrastive (SupCon) + reconstruction + dynamics losses in small MARL — the first to combine contrastive and reconstruction for communication, but for continuous-vector messages, not text. CACL (2024) uses contrastive alignment on continuous messages. MAPoRL (ACL 2025) trains influence-aware verification rewards (turn-level). ThoughtComm (NeurIPS 2025) uses autoencoders on LLM hidden states for inference-time latent thought communication without RL training. **Attention pooling:** The attention-weighted pooling mechanism (α_j = softmax(v^T·tanh(W·h_j+b))) is the standard formulation from Hierarchical Attention Networks (Yang et al., NAACL 2016) and self-attentive sentence embeddings (Lin et al., ICLR 2017). It is a well-established architectural choice, not a novel contribution. **EMA stability theory:** EMA-PG (Feb 2026, arXiv 2602.04417) derives stability conditions for EMA anchors in GRPO-like policy gradient training, showing τ close to 1 ensures smooth policy tracking. **The gap:** No method provides auxiliary training signal — whether reconstruction-based, contrastive, or otherwise — specifically for text-based inter-agent message quality in LLM multi-agent GRPO. MASIA and TACTIC demonstrate the intent-grounding paradigm works in classical MARL; IGCT adapts it to LLM-GRPO with stop-gradient isolation, EMA stabilization, and GRPO-group contrastive negatives to handle the distinct challenges of high-dimensional hidden states, LoRA-induced moving targets, and group-relative optimization.",
  "approach": "We introduce Intent-Grounded Communication Training (IGCT), a paradigm for improving text-based inter-agent communication during multi-agent GRPO training via auxiliary losses that ground messages in the sender's latent intent. IGCT provides two complementary variants — reconstruction-based (IGCT-R) and contrastive (IGCT-C) — that share a common target stabilization framework. **Shared infrastructure — Intent target extraction:** When agent i generates a message, we extract its intent embedding as the EMA-smoothed, stop-gradient-detached last hidden state: e_i = sg(EMA_τ(h_i^L)). Stop-gradient prevents auxiliary losses from distorting the sender's internal representations. EMA stabilization (τ=0.999) addresses the moving-target problem from continuous LoRA updates, grounded in EMA-PG (Zhang & Ba, 2026) which derives conditions under which τ close to 1 ensures the anchor tracks the policy smoothly without inducing optimization instability. **Message encoding:** Message tokens [m_1,...,m_T] are encoded via their hidden states h_j^msg. We use standard attention pooling (Yang et al. 2016; Lin et al. 2017) to obtain a message representation: α_j = softmax(v^T·tanh(W_attn·h_j^msg + b_attn)), pool(m) = Σ_j α_j·h_j^msg. The attention weights modulate gradient magnitudes across tokens — the dominant gradient term scales with α_j, with additional redistribution through the softmax Jacobian — so intent-carrying tokens receive stronger training signal than syntactic filler. The attention weights also serve as an interpretability tool, revealing which tokens carry the most intent information. **Variant 1 — IGCT-R (Reconstruction):** A lightweight MLP decoder (~18M params) minimizes L_recon = ||MLP(pool(m)) - e_i||². This follows the reconstruction paradigm from Lin et al. (NeurIPS 2021) and MASIA (NeurIPS 2022), adapted to LLM scale: unlike Lin et al. who reconstruct sender observations in small networks, IGCT-R reconstructs high-dimensional sender intent embeddings; unlike MASIA who reconstructs environment global state from agent observation vectors in SMAC/LBF, IGCT-R reconstructs sender communicative intent from natural language tokens in LLM-GRPO, requiring stop-gradient and EMA to handle the LoRA-induced non-stationarity absent in fixed-architecture MARL. **Variant 2 — IGCT-C (Contrastive Intent Alignment):** Uses InfoNCE loss to maximize agreement between messages and their sender's intent while discriminating against negatives: L_contrast = -log[exp(sim(pool(m^k), e_i^k)/τ_c) / Σ_j exp(sim(pool(m^k), e_i^j)/τ_c)]. Critically, IGCT-C exploits GRPO's group sampling structure for hard negative mining: for a given prompt, GRPO samples G completions, each producing different intent embeddings. In-group negatives (m^k, e_i^j) for j≠k are same-agent, same-prompt, different-intent — semantically close but intentionally distinct, forcing messages to be discriminatively informative. This source of hard negatives is structurally unavailable to classical MARL contrastive methods (CACL, TACTIC) which lack group-relative sampling. Cross-agent negatives (m^k, e_j^k) for j≠i provide inter-role discrimination. **Training:** Total loss L = L_GRPO + λ·L_aux (where L_aux is L_recon or L_contrast), with λ annealed from 0.3→0 over training (dense auxiliary signal fades as task reward becomes informative). **Architecture:** Following DEPART, planner and executor share base model weights (Qwen3-1.7B) with agent-specific LoRA adapters (rank=64). Built on PettingLLMs infrastructure. **Evaluation (3 benchmarks + Pareto comparison + interpretability study):** (1) ALFWorld with DEPART-style planner-executor: planner generates natural language plans, executor acts — IGCT trains the planner's message quality. Baselines: DEPART/HIMPO without IGCT, single-agent HiPER (97.4%). (2) WebArena-Lite with DEPART-style planner-executor (165 human-verified tasks). Baselines: DEPART/HIMPO without IGCT. (3) Sokoban 6x6 from Stronger-MAS (published AT-GRPO baselines for controlled comparison). (4) **Text-vs-latent Pareto frontier on ALFWorld:** Run LatentMAS (training-free, publicly available, minimal compute) alongside IGCT-R and IGCT-C to directly characterize the performance-interpretability tradeoff. If IGCT achieves 60–80% of LatentMAS's gains while preserving readable messages, that is a compelling Pareto-optimal result; if gains are modest, the interpretability study becomes the decisive contribution. (5) **Concrete interpretability evaluation (ALFWorld):** (a) Failure diagnosis study: present evaluators with agent failures, comparing time-to-diagnosis and accuracy between IGCT messages, baseline messages, and opaque LatentMAS communication; (b) Attention-intent correlation: measure alignment between learned α_j weights and human-annotated intent-carrying tokens; (c) Human-in-the-loop correction: simulate scenarios where humans read planner messages and intervene to correct wrong plans, comparing intervention success rates. This converts the interpretability argument from philosophical to empirical. **Ablations (5):** (i) IGCT-R vs IGCT-C vs IGCT-R+C combined (tests whether the paradigm is robust to loss function choice); (ii) Stop-gradient + EMA vs joint training without stop-gradient (tests necessity at LLM scale — the key adaptation challenge absent in classical MARL); (iii) EMA τ values {0.99, 0.999, 0.9999} informed by EMA-PG stability analysis; (iv) λ annealing schedule (constant 0.1 vs linear 0.3→0 vs cosine); (v) Attention-weighted vs mean vs max pooling (architectural choice validation, not novelty claim). **Composability:** IGCT + C3 message-level credit (testing orthogonality — IGCT provides within-message token differentiation, C3 provides between-message credit, they operate at complementary granularities). IGCT + Dr. MAS agent-wise normalization (testing GRPO stability compatibility).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~230h H100 (ALFWorld IGCT-R+C planner-executor: ~70h; WebArena-Lite IGCT-R+C: ~55h; Sokoban 6x6 IGCT-R+C: ~45h; ablations on ALFWorld+Sokoban: ~40h; LatentMAS baseline: ~5h; composability: ~15h)",
      "gpu_utilization": "Low (30–40%): human bottleneck on integration, interpretability study design, annotation",
      "timeline": "2.5–3.5 months",
      "team": "1–2 researchers (RL + multi-agent expertise) + 3–5 annotators for interpretability study (~20 person-hours annotation)",
      "estimated_gpu_cost": "$575–690 (at ~$2.50–3.00/GPU-hr)"
    },
    "human_in_loop": {
      "gpu_hours": "~250h H100 (systematic runs with approval gates for variant comparison and EMA τ selection)",
      "gpu_utilization": "Moderate (50–65%): agent queues experiments, pauses for design decisions and annotation review",
      "timeline": "7–9 weeks",
      "team": "1 researcher (~30min/day for reviews), 3–5 annotators for interpretability study",
      "claude_api_cost": "$150–250 (~2000–3500 Opus turns)",
      "estimated_gpu_cost": "$625–750 (at ~$2.50–3.00/GPU-hr)",
      "risk_note": "WebArena-Lite multi-agent setup requires DEPART-style environment engineering; interpretability study requires annotation protocol design and IRB consideration; IGCT-C negative sampling requires PettingLLMs modification for group-level intent access"
    },
    "auto_research": {
      "gpu_hours": "~280h H100 (budget-capped: systematic sweeps across both variants, EMA τ, λ schedules, all three benchmarks; continuous pipeline within budget)",
      "gpu_utilization": "High (85–95%): 24/7 operation within 280h cap",
      "timeline": "12–16 days with 4 concurrent H100s",
      "team": "0 for compute (uses PettingLLMs + DEPART infrastructure); interpretability study requires separate human annotation pass",
      "claude_api_cost": "$300–500 (~4000–7000 Opus turns)",
      "estimated_gpu_cost": "$700–840 (at ~$2.50–3.00/GPU-hr)",
      "speed_bottleneck": "WebArena-Lite environment setup; interpretability annotation cannot be automated; 4 concurrent H100s needed; IGCT-C requires PettingLLMs patch for group-level intent extraction",
      "risk_note": "Fixed 280h cap limits exploration; interpretability study adds ~2 weeks beyond compute timeline"
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract: Jul 25 2026, full paper: Aug 1 2026; Montréal, Feb 16–23 2027) — primary target, provides ~12 weeks for full experimental program including interpretability study and human annotation",
    "ICLR 2027 (expected ~Oct 2026, deadline TBD) — fallback with additional time for comprehensive experiments and cross-benchmark analysis",
    "Note: User requested EMNLP 2026 (ARR May 25), but 15-day timeline is infeasible for the proposed 230+ GPU-hour experimental program with human interpretability evaluation. ARR June 15 cycle could theoretically target EMNLP 2026 commitment deadline if scope is reduced to ALFWorld-only, but this would sacrifice the cross-benchmark generalization and Sokoban controlled-comparison results. AAAI 2027 (Aug 1) is recommended for the full contribution."
  ],
  "level": "strong",
  "key_references": [
    "Latent Collaboration in Multi-Agent Systems — LatentMAS (ICML 2026 Spotlight, arXiv 2511.20639)",
    "Recursive Multi-Agent Systems — RecursiveMAS (April 2026, arXiv 2604.25917)",
    "Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems — DiffMAS (April 2026, arXiv 2604.21794)",
    "Enabling Agents to Communicate Entirely in Latent Space — Interlat (ACL 2026, arXiv 2511.09149)",
    "When Less Latent Leads to Better Relay — OBF (April 2026, arXiv 2604.13349)",
    "Latent Agents: A Post-Training Procedure for Internalized Multi-Agent Debate (April 2026, arXiv 2604.24881)",
    "The Vision Wormhole: Latent-Space Communication in Heterogeneous MAS (Feb 2026, arXiv 2602.15382)",
    "Efficient Multi-agent Communication via Self-supervised Information Aggregation — MASIA (NeurIPS 2022, Guan et al.)",
    "Learning to Ground Multi-Agent Communication with Autoencoders — Lin et al. (NeurIPS 2021)",
    "Task-Agnostic Contrastive Pre-Training for Communication — TACTIC (AAMAS 2025, Yu et al.)",
    "Learning Multi-Agent Communication with Contrastive Learning — CACL (2024, arXiv 2307.01403)",
    "EMA Policy Gradient: Taming RL for LLMs with EMA Anchor and Top-k KL — EMA-PG (Feb 2026, arXiv 2602.04417)",
    "Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems (Feb 2026, arXiv 2602.08847)",
    "Counterfactual Credit Policy Optimization — CCPO (March 2026, arXiv 2603.21563)",
    "CoFi-PGMA: Counterfactual Policy Gradients under Filtered Feedback for Multi-Agent LLMs (April 2026, arXiv 2604.22785)",
    "C3: Contextual Counterfactual Credit Assignment for Multi-Agent RL in LLM Collaboration (March 2026, arXiv 2603.06859)",
    "Stronger-MAS: Multi-Agent Reinforcement Learning for Collaborative LLMs — AT-GRPO (ICLR 2026)",
    "LLM Collaboration with Multi-Agent Reinforcement Learning — MAGRPO (AAAI 2026)",
    "Hierarchical Attention Networks for Document Classification — Yang et al. (NAACL 2016)",
    "A Structured Self-Attentive Sentence Embedding — Lin et al. (ICLR 2017)",
    "Language Grounded Multi-Agent Communication — LangGround (NeurIPS 2024)",
    "Thought Communication in Multiagent Collaboration — ThoughtComm (NeurIPS 2025)",
    "Why Do Multi-Agent LLM Systems Fail? (NeurIPS 2025)",
    "MAPoRL: Multi-Agent Post-Co-Training for Collaborative LLMs with RL (ACL 2025)",
    "Training Language Models for Social Deduction with Multi-Agent RL (AAMAS 2025)",
    "DEPART: Hierarchical Multi-Agent System for Multi-Turn Interaction — HIMPO (OpenReview 2025–2026)",
    "HiPER: Hierarchical RL with Explicit Credit Assignment for LLM Agents (Feb 2026, arXiv 2602.16165)",
    "Graph-GRPO: Stabilizing Multi-Agent Topology Learning via GRPO (arXiv 2026)",
    "Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems (arXiv 2025)",
    "Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces (May 2026, arXiv 2605.02801)"
  ],
  "description": "We introduce Intent-Grounded Communication Training (IGCT), a paradigm for improving text-based inter-agent communication during multi-agent GRPO training via auxiliary losses that ground messages in the sender's latent intent. The multi-agent LLM communication landscape has bifurcated: latent methods (LatentMAS, ICML 2026; RecursiveMAS; DiffMAS; Interlat, ACL 2026) achieve +8–27% by replacing text with hidden-state or KV-cache transfers, but sacrifice interpretability; text-based RL methods (AT-GRPO, MAGRPO) and credit assignment approaches (C3, CCPO, CoFi-PGMA) optimize task reward or agent-level credit without training message quality. Classical MARL demonstrated that reconstruction (Lin et al., NeurIPS 2021), reconstruction + attention aggregation (MASIA, NeurIPS 2022), and contrastive alignment (CACL; TACTIC, AAMAS 2025) can ground communication — but only for continuous-vector messages in small-scale agents. IGCT adapts this intent-grounding paradigm to LLM-GRPO, addressing the distinct challenges of high-dimensional hidden states, LoRA-induced non-stationarity, and group-relative optimization. IGCT provides two complementary variants sharing a common target stabilization framework (stop-gradient isolation + EMA smoothing, grounded in EMA-PG stability theory): (1) IGCT-R (Reconstruction): a lightweight decoder reconstructs the sender's EMA-stabilized intent embedding from the message, adapting Lin et al. (2021) and MASIA's reconstruction paradigm to LLM scale — unlike MASIA which reconstructs environment global state from observation vectors in SMAC, IGCT-R reconstructs sender communicative intent from natural language tokens, requiring stop-gradient + EMA to handle LoRA-induced non-stationarity absent in fixed-architecture MARL; (2) IGCT-C (Contrastive): InfoNCE alignment maximizes agreement between messages and sender intent while discriminating against negatives — critically exploiting GRPO's group sampling structure for hard negative mining (same-agent, same-prompt, different-intent in-group negatives), a source structurally unavailable to classical MARL contrastive methods. Both variants use standard attention pooling (Yang et al. 2016; Lin et al. 2017) — a well-established architectural choice — where attention weights modulate per-token gradient magnitudes (dominant term scales with α_j, with redistribution through the softmax Jacobian). Architecture follows DEPART: Qwen3-1.7B with agent-specific LoRA (rank=64). We evaluate on three benchmarks: (1) ALFWorld with DEPART-style planner-executor, (2) WebArena-Lite (165 tasks), (3) Sokoban 6x6 with published AT-GRPO baselines. A central contribution is the text-vs-latent Pareto frontier comparison: we run training-free LatentMAS alongside IGCT on ALFWorld to directly characterize the performance-interpretability tradeoff. A concrete interpretability evaluation (failure diagnosis study, attention-intent correlation with human annotations, human-in-the-loop correction experiments) converts the interpretability argument from philosophical to empirical. Five ablations test: (i) IGCT-R vs IGCT-C vs combined (paradigm robustness), (ii) stop-gradient necessity, (iii) EMA τ per EMA-PG theory, (iv) λ annealing, (v) pooling architecture. Composability experiments combine IGCT with C3 (complementary granularities: within-message vs between-message credit) and Dr. MAS (GRPO stability). Estimated compute: ≤280 H100-hours ($575–840). Primary target: AAAI 2027 (Aug 1 deadline, 12 weeks).",
  "project_name": "recon_reg_comm_training",
  "source": "web_research",
  "change_type": "major"
}
```

## Summary of changes and how each reviewer issue is addressed

**1. MASIA citation (MISSING CITATION):** Now cited with detailed technical differentiation — MASIA reconstructs environment global state from agent observation vectors in SMAC/LBF (a state estimation problem), while IGCT-R reconstructs sender communicative intent from natural language tokens in LLM-GRPO (a grounding problem at fundamentally different scale requiring stop-gradient + EMA).

**2. Attention pooling novelty (OVERSTATED):** Completely reframed. Now explicitly cited as standard (Yang et al. 2016, Lin et al. 2017) — "a well-established architectural choice, not a novel contribution." Gradient analysis corrected: "dominant term scales with α_j, with redistribution through the softmax Jacobian" instead of the false proportionality claim.

**3. Interlat (MISSING CONCURRENT WORK):** Added to landscape with technical details (ACL 2026, hidden-state transfer, 24x compression, ALFWorld/MATH evaluation).

**4. Narrow novelty gap (ENGINEERING COMBINATION):** Addressed via three structural changes: (a) reframed from one mechanism (SGIR) to a *paradigm* (IGCT) with two variants showing generality; (b) added IGCT-C contrastive variant that exploits GRPO's group sampling structure for hard negative mining — a genuinely novel component structurally unavailable to classical MARL methods (CACL, TACTIC); (c) the text-vs-latent Pareto frontier characterization is itself a novel empirical contribution. The contribution is no longer "apply known technique X at scale Y" but "establish and characterize a paradigm for trainable text communication."

**5. Uncertain empirical impact:** Directly addressed by (a) the LatentMAS Pareto comparison — if IGCT achieves 60–80% of latent gains, it's a compelling tradeoff; if modest, the interpretability study carries the paper; (b) concrete interpretability evaluation protocol (failure diagnosis, attention-intent correlation, human-in-the-loop correction) that provides empirical rather than philosophical evidence for text preservation; (c) two variants increase the chance that at least one yields meaningful gains.

**6. Venue deviation:** Maintained AAAI 2027 as primary (12 weeks is realistic for full program including human evaluation). Added note about ARR June 15 as aggressive reduced-scope option for EMNLP 2026.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42107ee3-8c93-4304-b37d-a732a5375247",
  "isSidechain": false,
  "requestId": "req_011CauZd2w2cakNs61fTwW2w",
  "type": "assistant",
  "uuid": "56be9987-a1bf-4489-945c-a77a74cf03f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bLFB8X9MyWPKsyjx87BNA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7766,
      "cache_read_input_tokens": 37650,
      "output_tokens": 11552,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7766,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11552,
          "cache_read_input_tokens": 37650,
          "cache_creation_input_tokens": 7766,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7766
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Stop-Gradient Intent Reconstruction with Attention-Weighted Pooling fo…",
  "leafUuid": "56be9987-a1bf-4489-945c-a77a74cf03f7",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising Stop-Gradient Intent Reconstruction for text-based multi-agent communication",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Stop-Gradient Intent Reconstruction with Attention-Weighted Pooling fo…",
  "leafUuid": "56be9987-a1bf-4489-945c-a77a74cf03f7",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising Stop-Gradient Intent Reconstruction for text-based multi-agent communication",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b"
}
```

---
