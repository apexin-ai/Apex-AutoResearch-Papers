# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-11 (UTC).** ## Original idea { "tit

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/bc7e3bfc-1b8a-4420-a244-c7c2364ab284.jsonl`
- **Structured JSON:** [`4b1b3c287cba829c8ca6.json`](../../sessions/4b/4b1b3c287cba829c8ca6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T01:29:13.206Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T01:29:13.206Z",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-11 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Trajectory-Aware Joint Compression for Long-Horizon Agentic KV Caches\",\n  \"core_problem\": \"Agentic LLM systems (coding agents, research agents, tool-use agents) maintain KV caches that grow across dozens of reasoning-and-action steps, often exceeding 100K tokens. Current KV cache compression methods — including strong joint quantization-eviction approaches like ThinKV, HqeKV, and ARKV, as well as future-aware eviction methods like NGC and LookaheadKV — were designed for single-turn or single-model inference and optimize per-step reconstruction error or per-step eviction quality independently. In multi-step agentic workloads, compression errors compound across planning steps: PM-KVQ (ICLR 2026) demonstrates that directly quantizing KV cache at each decoding step causes cumulative quantization error that degrades long-CoT reasoning by up to 8% versus progressive strategies; 'Hold Onto That Thought' (under review, ICLR 2026) empirically shows that existing KV compression strategies designed for prefill-phase long-context tasks degrade significantly on reasoning tasks requiring extended decoding. Theoretical analysis from 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) proves lower bounds showing exponential error growth Ω((n/s)^(T-1)) for oblivious cache strategies across T reasoning stages in k-hop pointer chasing; we note that this bound applies specifically to single-model multi-step reasoning with locality-respecting cache controllers, not directly to agentic tool-use workflows with external observation injection — the analogy is suggestive but not a formal proof. The empirical evidence from PM-KVQ and 'Hold Onto That Thought' provides the primary, more directly applicable motivation. No existing work formulates joint quantization-eviction that explicitly minimizes cumulative trajectory-level error for agentic workloads.\",\n  \"opportunity\": \"Two converging trends expose a clear research gap. First, agentic inference is now the dominant LLM deployment pattern (SWE-bench, GAIA, τ-bench), but KV cache compression research overwhelmingly targets single-turn inference. Existing agentic KV cache works address only parts of the problem: SideQuest (Feb 2026) uses model-driven eviction but not quantization; CodeComp (April 2026) leverages structural code priors for eviction only; CacheTTL (Nov 2025) manages cache scheduling without compression; PBKV (May 2026) predicts future agent invocations for cache management but performs no within-request compression; KVFlow (NeurIPS 2025) optimizes prefix caching for multi-agent workflows without compression; EpiCache (Apple, Sep 2025) manages episodic multi-turn cache but targets conversational QA, not agentic tool-use. NGC (April 2026) learns trajectory-aware KV eviction via RL within single-model reasoning chains, jointly optimizing reasoning and memory management from task reward alone — the closest conceptual competitor, but it requires RL training, is eviction-only (no quantization), and operates on single-model reasoning traces without explicit agent step boundaries or external observation injection. CapKV (April 2026) derives information-theoretic KV eviction via the Information Bottleneck principle with capacity-aware scoring — theoretically grounded but eviction-only and per-step.\\n\\nSecond, single-turn KV cache compression has matured across multiple fronts: (a) joint quantization-eviction via ThinKV (ICLR 2026 Oral, 20x compression), HqeKV (per-element compression actions), ARKV (tri-state assignment); (b) future-aware eviction via NGC (RL-based trajectory-aware eviction for single-model reasoning), LookaheadKV (ICLR 2026, predictive eviction via lookahead tokens + LoRA); (c) optimal bit allocation via RateQuant (rate-distortion reverse waterfilling, May 2026) and MixedDimKV (Lagrangian dual decomposition for per-token dimensions); (d) temporal and structural KV management via TTKV (temporal tiering with heterogeneous precision), TRIM-KV/Cache What Lasts (ICLR 2026, learned retention gates with temporal decay), and Transactional Attention (structural anchor protection for value-bearing tokens); (e) information-theoretic eviction via CapKV (Information Bottleneck with statistical leverage scores). However, none model how compression decisions at step t propagate errors to steps t+1 through T in multi-step agentic workflows with external tool observations. The key insight: in agentic workloads, token importance is cross-step structured in ways that single-turn methods cannot exploit. Instruction and plan tokens maintain importance across all steps; current-step observations are critical but rapidly decay; historical tool outputs become redundant as new observations arrive. This temporal structure, combined with the empirically-grounded error compounding problem (PM-KVQ, 'Hold Onto That Thought'), demands a fundamentally different optimization objective: minimizing trajectory-level degradation rather than per-step reconstruction error.\",\n  \"landscape\": \"**Joint quantization-eviction (single-turn):** ThinKV (ICLR 2026 Oral) applies thought-adaptive hybrid quantization-eviction achieving 20x compression with <5% KV cache — the strongest single-turn baseline. HqeKV (ACL ARR Jan 2026) provides an integrated optimizer selecting optimal compression actions (quantization level or eviction) per cached element under memory constraints. ARKV (arXiv Feb 2026) dynamically assigns tokens to Original/Quantization/Eviction states based on per-layer attention statistics. KVTC (ICLR 2026) achieves 20x via PCA + adaptive quantization + entropy coding.\\n\\n**Constrained optimization for KV compression:** MixedDimKV (March 2026) formulates KV cache compression as a constrained optimization problem using Lagrangian dual decomposition with bisection search over λ, allocating per-token dimensions under a memory budget. This uses the same Lagrangian optimization technique as TrajComp. The critical difference: MixedDimKV minimizes per-step reconstruction error (single-step objective), while TrajComp minimizes trajectory-level error accumulation across T agent steps (multi-step objective). The trajectory extension is non-trivial because: (i) the search space expands from per-step to cross-step — compressing token i at step t affects attention distributions at steps t+1...T; (ii) the objective changes from reconstruction fidelity to trajectory success rate; (iii) the importance model must account for temporal structure (persistent vs. decaying tokens) absent in single-turn settings. RateQuant (May 2026) applies rate-distortion theory with reverse waterfilling for optimal per-head bit allocation — a complementary per-step optimization that TrajComp could incorporate as a sub-routine for within-step bit allocation.\\n\\n**Trajectory-aware and future-aware eviction:** NGC (April 2026, arXiv:2604.18002) learns trajectory-aware KV eviction via RL, treating both reasoning tokens and cache-eviction decisions as discrete actions sampled from the language model, trained end-to-end from outcome-based task reward alone. On Countdown, AMC, and AIME, NGC achieves 2-3x peak KV cache compression while maintaining strong accuracy. TrajComp differs from NGC in three key ways: (1) training-free (Lagrangian optimization vs. RL training required), (2) joint quantization-eviction (vs. eviction-only), and (3) designed for multi-step agentic workflows with explicit step boundaries and external observation injection (vs. single-model reasoning traces where the model interleaves thinking and eviction). LookaheadKV (ICLR 2026, Samsung) predicts future attention patterns via trainable lookahead tokens + LoRA, achieving <0.7% drop at 81% compression — also eviction-only and single-turn.\\n\\n**Information-theoretic eviction:** CapKV (April 2026, arXiv:2604.25975) derives capacity-aware KV eviction via the Information Bottleneck principle, using a log-determinant approximation with statistical leverage scores under a linear-Gaussian surrogate of attention. It provides a theoretically grounded mechanism that replaces heuristic selection with capacity-maximization. TrajComp differs: joint quantization-eviction with a trajectory-level multi-step objective vs. CapKV's per-step information-theoretic eviction-only framework.\\n\\n**Temporal and structural KV management:** TTKV (March 2026) partitions KV cache into temporal tiers with heterogeneous precision across HBM/DRAM, achieving 76% latency reduction on 128K contexts. Its temporal tiering directly overlaps with TrajComp's 'decaying context' category — but TTKV is a system-level memory hierarchy approach without trajectory-aware error optimization. TRIM-KV/Cache What Lasts (ICLR 2026) learns per-token retention gates with temporal decay via distillation — conceptually similar to cross-step importance decay, but training-required, eviction-only, and single-turn. Transactional Attention (April 2026) protects structural anchor tokens (credentials, API keys) from eviction via semantic sponsorship — overlaps with TrajComp's 'persistent anchors' category, but is domain-specific to credential/configuration retention and does not perform compression.\\n\\n**Agentic KV cache management:** SideQuest (Feb 2026) uses the reasoning model itself to identify dispensable tokens, achieving 65% peak token reduction on agentic tasks — eviction only, no quantization. CodeComp (April 2026) uses Code Property Graph priors for structure-aware eviction in agentic coding — domain-specific and eviction only. CacheTTL/Continuum (Nov 2025) manages multi-turn cache scheduling with TTL-based retention. PBKV (May 2026) predicts future agent invocations and manages cache across workflow steps — system-level scheduling without within-request compression. KVFlow (NeurIPS 2025) optimizes prefix caching for multi-agent workflows. EpiCache (Apple, Sep 2025) manages episodic multi-turn cache for conversational QA. Agent Memory Below the Prompt (Feb 2026) persists Q4 KV caches across agents on edge devices. KVComm (Oct 2025) enables cross-context KV sharing.\\n\\n**Other relevant methods:** TriAttention (MIT/NVIDIA, April 2026) achieves 10.7x via trigonometric key importance scoring. R-KV (NeurIPS 2025) achieves 100% accuracy at 10% KV via redundancy-aware eviction with public code. DMS (NeurIPS 2025) achieves 8x with lightweight training. EVICPRESS (Microsoft, Dec 2025) jointly optimizes compression and eviction across storage tiers. PM-KVQ shows progressive mixed-precision reduces cumulative quantization error in long-CoT. TurboQuant (ICLR 2026) addresses inner-product estimation bias compounding across attention computations. 'Not All Bits Are Equal' (ICLR 2026) shows optimal compression strategy is scale-dependent.\\n\\n**Error compounding theory and evidence:** 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) proves that under k-hop pointer chasing with cache size s, oblivious caches suffer exponential error growth Ω((n/s)^(T-1)). We note this bound applies specifically to k-hop pointer chasing with locality-respecting cache controllers in single-model multi-step reasoning; its extension to agentic tool-use with external observation injection is an analogy, not a formal proof. The empirical evidence from PM-KVQ (cumulative quantization error degrades long-CoT by up to 8%) and 'Hold Onto That Thought' (compression designed for prefill degrades extended-decoding reasoning) provides the primary and more directly applicable motivation for trajectory-aware compression.\\n\\nNo prior work formulates a trajectory-level objective for joint quantization-eviction in agentic KV caches with explicit cross-step error accumulation control. The closest works are NGC (trajectory-aware but RL-required, eviction-only, single-model) and MixedDimKV (same Lagrangian technique but per-step objective). TrajComp uniquely combines: (1) joint quant-eviction, (2) trajectory-level multi-step objective, (3) training-free Lagrangian optimization, (4) agentic workflow structure exploitation.\",\n  \"approach\": \"We propose TrajComp (Trajectory-Aware Joint Compression), which formulates a single dual-constrained Lagrangian objective jointly optimizing token retention probabilities and per-token bit allocation under memory and cumulative trajectory-error budgets.\\n\\n**(1) Cross-step error propagation model:** Unlike ThinKV/HqeKV/MixedDimKV which minimize per-step reconstruction error independently, and unlike NGC which learns trajectory-aware eviction through RL training, TrajComp models error propagation across agent steps in a training-free manner. Compressing token i at step t contributes weighted error proportional to Σ_{s=t+1}^{T} γ^{s-t} × importance_i, where γ is the empirically-calibrated step-wise error propagation rate. The dual-constrained Lagrangian L = Σ_t error_t(s,q) + λ_mem(M(s,q) - B_mem) + λ_err(E_cumul(s,q,γ) - B_err) enables smooth Pareto-optimal tradeoffs via dual gradient descent on both multipliers. Note: MixedDimKV uses Lagrangian dual decomposition with bisection for a single memory constraint and per-step objective; TrajComp extends this to dual constraints (memory + trajectory error) with a cross-step objective, requiring the error propagation model as additional machinery.\\n\\n**γ calibration procedure:** For each target model, run N=10 agent trajectories per benchmark (SWE-bench Lite subset, τ-bench) with full (uncompressed) KV cache and with uniformly 4-bit quantized KV cache. At each agent step boundary t, measure KL divergence D_KL(P_full^t || P_compressed^t) of the attention distributions. Compute per-step propagation ratios r_t = D_KL^{t+1} / D_KL^t across all steps and trajectories. Set γ = median(r_t) across steps and trajectories. Report sensitivity analysis: if γ varies by >20% across tasks within a benchmark, use per-benchmark γ and budget the additional calibration cost (~2h per model-benchmark pair). Based on PM-KVQ's observations of progressive error accumulation, we expect γ ∈ [0.7, 0.95]. Total calibration cost: ~10 H100-hours for 2 models × 2 agentic benchmarks × 10 trajectories.\\n\\n**(2) Agent-phase token categorization:** Rather than ThinKV's within-turn thought types, TrajComp defines categories by agentic workflow structure: (a) Persistent anchors — system prompts, instructions, plans — never compressed (analogous to Transactional Attention's structural anchors, but generalized beyond credentials to all instruction-bearing tokens); (b) Active context — current tool output and recent reasoning — retained at 4-bit; (c) Decaying context — older observations — progressively compressed (4-bit → 2-bit → evict) with schedule determined by the Lagrangian solver based on temporal distance and cross-step importance (analogous to TTKV's temporal tiering, but driven by trajectory-level optimization rather than fixed temporal heuristics); (d) Ephemeral tokens — intermediate tool formatting, API boilerplate — immediately evicted.\\n\\n**Phase detection strategy:** For structured agent frameworks (ReAct, function-calling with explicit Thought/Action/Observation tags), use lightweight pattern matching on special tokens and turn boundaries (zero overhead). For free-form reasoning models where thinking and acting interleave without clear delimiters, fall back to attention entropy thresholds: compute per-token attention entropy at step boundaries; tokens with consistently high entropy across recent steps are classified as ephemeral, tokens with low entropy as active/persistent. This dual strategy is benchmarked explicitly: we report phase classification accuracy and its impact on trajectory success for both detection methods.\\n\\n**Agent scaffold specification:** For SWE-bench Lite evaluation, we use SWE-agent with ReAct prompting, max 30 turns, 16K tokens per turn, matching standard evaluation protocols. For τ-bench, we use the official τ-bench evaluation harness (github.com/sierra-research/tau-bench) with default configuration across retail and airline domains.\\n\\n**(3) GQA-aware compression:** Both evaluation models (Qwen3-8B: 32 query heads, 8 KV heads; DeepSeek-R1-Distill-Qwen3-8B: 32 query heads, 8 KV heads) use Grouped Query Attention (GQA), where multiple query heads share KV heads. TrajComp allocates compression budgets at the KV-head group level, accounting for the fact that compressing a single KV head affects all query heads in its group. MLA adaptation (for full DeepSeek-V3/R1 671B models) is left as future work, as MLA's latent-space KV representation requires a fundamentally different compression strategy that cannot be validated on our GQA-only evaluation models.\\n\\nThe dual gradient descent operates at agent step boundaries (not every token), making it lightweight. A single re-optimization pass over the full KV cache occurs when a new agent step begins.\\n\\n**Wall-clock and throughput reporting:** We report: (a) Lagrangian solver time per agent step as a function of KV cache size — expected to be <10ms for dual gradient descent over ~100K tokens, dominated by importance score computation not the optimization itself; (b) end-to-end latency per agent step (including compression overhead) vs. baselines on H100-80GB; (c) tokens/second throughput at matched compression ratios. The solver adds negligible overhead relative to the LLM forward pass (~500ms-2s per agent step for 8B models).\\n\\n**8B model capability consideration:** We acknowledge that 8B models achieve relatively low base success rates on SWE-bench (e.g., RepoForge-8B: ~17% on SWE-bench Verified). To ensure meaningful compression comparisons despite low base rates: (a) we report not only binary task success but also trajectory-quality metrics — steps completed before failure, tool-call coherence, and reasoning degradation measured via attention distribution divergence from full-cache trajectories; (b) τ-bench serves as the primary agentic benchmark, where 8B models may achieve higher success rates on the structured customer-service tasks; (c) if both models achieve <10% success on SWE-bench Lite 100-instance subset, we supplement with a subset of 50 instances known to be solvable by 8B models (identified via full-cache runs).\\n\\n**User-requested benchmark gap table:**\\n| Benchmark | Status | Est. Cost | Reason |\\n|---|---|---|---|\\n| MMLU | Included | 5h | General capability check |\\n| LongBench | Included | 20h | Long-context evaluation |\\n| AIME 2025 | Included | 8h | Reasoning evaluation |\\n| MATH-500 | Included | 7h | Reasoning evaluation |\\n| HumanEval | **Added** | 2h | Code generation, low cost |\\n| MT-Bench | **Added** | 2h | Multi-turn chat quality, low cost |\\n| Perplexity (Wiki/C4) | **Added** | 3h | Language modeling quality, low cost |\\n| SWE-bench Lite (100 instances) | Included | ~167h | Primary agentic benchmark (reduced from 300; 10 min/instance realistic) |\\n| τ-bench (164 tasks) | Included | ~55h | Primary agentic benchmark |\\n| RULER | Dropped | ~100h | Compute-prohibitive for 2 models × 5 methods |\\n| GAIA | Dropped | ~80h | Too expensive per instance |\\n| LiveCodeBench | Dropped | ~40h | Compute-prohibitive |\\n| GPQA | Dropped | ~15h | Lower priority vs. AIME/MATH |\\n\\n**Evaluation scope (designed for ~350 H100-hours):** Models: Qwen3-8B, DeepSeek-R1-Distill-Qwen3-8B (2 models, both using GQA attention). Baselines: ThinKV, HqeKV, SideQuest, R-KV (4 baselines — R-KV replaces ForesightKV, which lacks public code or checkpoints; R-KV has public code at github.com/Zefan-Cai/R-KV and provides a strong redundancy-aware eviction baseline from NeurIPS 2025). NGC and CapKV are discussed as related work but not re-implemented as baselines: NGC requires RL training (~30-50 H100-hours to reproduce per model) and CapKV's leverage-score computation is complementary to but not directly comparable with joint quant-eviction methods. Dropped baselines: ARKV, KVTC, DMS, CodeComp, ForesightKV (reported as ablation references from literature, not re-implemented; ForesightKV lacks public code/checkpoints and reproducing its supervised + RL training pipeline would cost ~40-60 H100-hours for 2 models). Benchmarks: 2 agentic (SWE-bench Lite 100 instances, τ-bench 164 tasks), 2 reasoning (AIME 2025, MATH-500), 1 long-context (LongBench), 1 general (MMLU), 1 code (HumanEval), 1 chat (MT-Bench), 1 perplexity (WikiText/C4). The key metric is trajectory-level success rate at matched compression ratio for agentic benchmarks, and standard accuracy/perplexity for non-agentic benchmarks.\\n\\n**Compute breakdown (revised with realistic SWE-bench timing):** SWE-bench Lite: 100 instances × 2 models × 5 methods × ~10 min/instance ≈ 167h. τ-bench: 164 tasks × 2 models × 5 methods × ~2 min ≈ 55h. AIME 2025 + MATH-500: ~15h. LongBench: ~20h. MMLU: ~5h. HumanEval: ~2h. MT-Bench: ~2h. Perplexity (Wiki/C4): ~3h. γ calibration: ~10h. Ablations (phase detection, γ sensitivity, anchor ratio): ~25h. Wall-clock benchmarking: ~5h. Development/debugging buffer: ~40h. Total: ~350 H100-hours.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~350h H100-80GB\",\n      \"gpu_utilization\": \"35-45% effective — idle time during Lagrangian solver implementation, γ calibration analysis, and phase detection debugging\",\n      \"timeline\": \"3-4 months\",\n      \"team\": \"1-2 researchers (systems ML + optimization background)\",\n      \"estimated_gpu_cost\": \"$875 (350h × ~$2.50/h H100 spot pricing)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~350h H100-80GB\",\n      \"gpu_utilization\": \"55-65% — agent handles baseline reproduction (R-KV from public code, ThinKV/HqeKV reimplementation), agentic benchmark setup (SWE-agent docker, τ-bench harness), γ calibration sweeps, and wall-clock benchmarking; human guides Lagrangian formulation, error propagation model design, and phase detection strategy\",\n      \"timeline\": \"2-3 months\",\n      \"team\": \"1 researcher, ~45min/day review\",\n      \"claude_api_cost\": \"$250-400 (~2500-4000 turns for agent pipeline development, experiment orchestration, result analysis)\",\n      \"estimated_gpu_cost\": \"$875 (350h × ~$2.50/h)\",\n      \"risk_note\": \"Primary risk is SWE-bench evaluation infrastructure — SWE-agent requires docker environments and tool sandboxing that may need debugging. γ calibration may require more trajectories than budgeted if variance is high across task types. 8B model low success rates on SWE-bench may limit statistical power; τ-bench results may be more informative for the agentic contribution.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~500h H100-80GB (sweeping γ calibration, phase boundary thresholds, dual multiplier schedules, SWE-bench at 10 min/instance, and wall-clock profiling across configurations)\",\n      \"gpu_utilization\": \"65-75% — SWE-bench instances at ~10 min each create pipeline gaps; agent queues ablation studies during these gaps\",\n      \"timeline\": \"3-5 weeks with 2-4 concurrent H100s\",\n      \"team\": \"0 (initial 3-hour setup: agent harness configs, model downloads, SWE-agent docker verification, baseline code checkout)\",\n      \"claude_api_cost\": \"$500-800 (~5000-8000 turns including SWE-agent docker debugging and failed exploration paths)\",\n      \"estimated_gpu_cost\": \"$1250 (500h × ~$2.50/h)\",\n      \"speed_bottleneck\": \"SWE-bench Lite instances average ~10 minutes each. With 100 instances × 10 configurations (2 models × 5 methods) ≈ 1000 runs. At 10 min avg on H100, this is ~167h — the dominant compute cost. τ-bench adds ~55h.\",\n      \"risk_note\": \"Agent may struggle with SWE-agent docker orchestration without human intervention. Risk of over-exploring γ sensitivity without converging on the key narrative. 8B model failure rates on SWE-bench may lead agent to cycle through debugging steps rather than accepting low base rates.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (expected deadline: ~August 2026 based on historical pattern; primary target, ~82 days from today — tight given 350h compute budget but feasible with 2-4 concurrent GPUs)\",\n    \"ICLR 2027 (expected abstract deadline: ~September 19, 2026 based on ICLR 2026 pattern; primary target, more comfortable timeline)\",\n    \"EMNLP 2026 (ARR deadline: May 25, 2026) — NOT FEASIBLE at 14 days given 350h compute requirement and no pre-existing implementation\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models (ICLR 2026 Oral)\",\n    \"HqeKV: Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference (ACL ARR Jan 2026)\",\n    \"ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget (arXiv Feb 2026)\",\n    \"NGC: Neural Garbage Collection: Learning to Forget while Learning to Reason (arXiv April 2026, arXiv:2604.18002) — RL-based trajectory-aware KV eviction for single-model reasoning, eviction-only, 2-3x compression on Countdown/AMC/AIME\",\n    \"CapKV: Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective (arXiv April 2026, arXiv:2604.25975) — Information Bottleneck principle with statistical leverage scores, eviction-only, per-step\",\n    \"LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation (ICLR 2026 Poster, Samsung, arXiv:2603.10899) — predictive eviction via lookahead tokens + LoRA\",\n    \"TTKV: Temporal-Tiered KV Cache for Long-Context LLM Inference (arXiv March 2026, arXiv:2604.19769) — temporal tiering with heterogeneous precision across HBM/DRAM\",\n    \"TRIM-KV / Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs (ICLR 2026, arXiv:2512.03324) — learned per-token retention gates with temporal decay\",\n    \"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory (arXiv May 2026, arXiv:2605.06675) — reverse waterfilling for per-head bit allocation\",\n    \"Transactional Attention: Semantic Sponsorship for KV-Cache Retention (arXiv April 2026, arXiv:2604.11288) — structural anchor protection for value-bearing tokens\",\n    \"Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression [MixedDimKV] (arXiv March 2026, arXiv:2603.20616) — Lagrangian dual decomposition for per-token dimension allocation\",\n    \"PBKV: Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management (arXiv May 2026, arXiv:2605.06472) — prediction-based agent cache scheduling\",\n    \"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows (NeurIPS 2025, arXiv:2507.07400) — workflow-aware prefix caching\",\n    \"EpiCache: Episodic KV Cache Management for Long Conversational Question Answering (Apple, arXiv Sep 2025, arXiv:2509.17396) — episodic multi-turn cache management\",\n    \"SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning (arXiv Feb 2026)\",\n    \"CodeComp: Structural KV Cache Compression for Agentic Coding (arXiv April 2026)\",\n    \"CacheTTL/Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live (arXiv Nov 2025)\",\n    \"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models (NeurIPS 2025, github.com/Zefan-Cai/R-KV) — redundancy-aware eviction with public code, used as baseline\",\n    \"How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers (arXiv April 2026, arXiv:2604.17935) — theoretical bounds on cache compression vs. reasoning depth (k-hop pointer chasing; analogy to agentic setting, not direct proof)\",\n    \"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs (arXiv May 2025, OpenReview Oct 2025) — empirical evidence of cumulative quantization error in long-CoT\",\n    \"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning (arXiv Dec 2025, arXiv:2512.12008) — empirical assessment of compression degradation on reasoning tasks\",\n    \"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression (MIT/NVIDIA, arXiv April 2026)\",\n    \"KV Cache Transform Coding [KVTC] for Compact Storage in LLM Inference (NVIDIA, ICLR 2026)\",\n    \"Inference-Time Hyper-Scaling with KV Cache Compression [DMS] (NeurIPS 2025)\",\n    \"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving (Microsoft, arXiv Dec 2025)\",\n    \"Not All Bits Are Equal: How Model Scale Changes Memory-Optimal Reasoning (ICLR 2026)\",\n    \"TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate (ICLR 2026) — inner-product bias compounding\",\n    \"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution (arXiv Feb 2026, arXiv:2602.03203) — RL-based future-aware eviction, eviction-only, single-turn; no public code/checkpoints available, discussed as related work only\",\n    \"Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices (arXiv Feb 2026, arXiv:2603.04428)\",\n    \"KVComm: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems (arXiv Oct 2025)\",\n    \"Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys (AAAI 2026)\"\n  ],\n  \"description\": \"We propose TrajComp (Trajectory-Aware Joint Compression), a training-free method that jointly optimizes token eviction and per-token bit allocation for KV caches in long-horizon agentic LLM workloads through a dual-constrained Lagrangian objective that explicitly minimizes trajectory-level error accumulation. The empirical motivation comes from PM-KVQ (ICLR 2026), which demonstrates that cumulative quantization error degrades long-CoT reasoning by up to 8% versus progressive strategies, and from 'Hold Onto That Thought' (2025), which shows that compression strategies designed for prefill degrade on extended-decoding reasoning. Theoretical analysis from 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) proves exponential error growth Ω((n/s)^(T-1)) for oblivious cache strategies in k-hop pointer chasing; we note this bound applies to single-model reasoning with locality-respecting cache controllers — its extension to agentic tool-use with external observation injection is a suggestive analogy, not a formal proof.\\n\\nThe landscape includes strong single-turn methods across multiple fronts: joint quant-eviction (ThinKV at 20x, HqeKV, ARKV), future-aware and trajectory-aware eviction (NGC via RL-based eviction for single-model reasoning achieving 2-3x compression, LookaheadKV via predictive attention), information-theoretic eviction (CapKV via Information Bottleneck with statistical leverage scores), optimal bit allocation (RateQuant via rate-distortion, MixedDimKV via Lagrangian dual), and temporal/structural management (TTKV temporal tiering, TRIM-KV learned retention, Transactional Attention anchor protection). Agentic-specific works (SideQuest, CodeComp, PBKV, KVFlow, EpiCache) address scheduling and eviction but not joint compression. NGC is the closest conceptual competitor but differs fundamentally: it requires RL training (vs. training-free), is eviction-only (vs. joint quant-eviction), and operates on single-model reasoning traces (vs. multi-step agentic workflows with external observations). No prior work combines joint quant-eviction with a trajectory-level multi-step objective for agentic workloads.\\n\\nTrajComp fills this gap with two core contributions: (1) A cross-step error propagation model that weights compression decisions by their γ-discounted impact across all future agent steps, formalized as a dual-constrained Lagrangian with separate memory and trajectory-error budget multipliers. γ is calibrated empirically via KL divergence propagation measurement. This extends MixedDimKV's Lagrangian dual (which uses the same optimization technique but minimizes per-step reconstruction error) to a trajectory-level objective — a non-trivial extension because the search space expands cross-step and the importance model must capture temporal structure. (2) Agent-phase token categorization (persistent anchors, active context, decaying context, ephemeral tokens) that exploits cross-step importance structure unique to agentic workflows, with dual detection strategies: pattern matching for structured frameworks (ReAct in SWE-agent) and attention entropy fallback for free-form reasoning. Both contributions are training-free, unlike NGC's RL approach. MLA adaptation is identified as future work.\\n\\nEvaluation uses 2 models (Qwen3-8B, DeepSeek-R1-Distill-Qwen3-8B — both GQA attention), 4 baselines (ThinKV, HqeKV, SideQuest, R-KV; R-KV replaces ForesightKV which lacks public code), and 9 benchmarks: 2 agentic (SWE-bench Lite 100 instances via SWE-agent with ReAct/30 turns/16K tokens, τ-bench 164 tasks via official harness), 2 reasoning (AIME 2025, MATH-500), 1 long-context (LongBench), 1 general (MMLU), 1 code (HumanEval), 1 chat (MT-Bench), 1 perplexity (WikiText/C4) — scoped to ~350 H100-hours with realistic 10 min/instance SWE-bench timing. We acknowledge 8B models achieve low base success rates on SWE-bench (~17%) and supplement binary success with trajectory-quality metrics. Reports include wall-clock latency, Lagrangian solver overhead per agent step, and tokens/second throughput on H100. Primary targets are AAAI 2027 (~August 2026) and ICLR 2027 (~September 2026).\",\n  \"project_name\": \"trajcomp_agentic_kvcache\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 8)\nIssues: [\"BASELINE REPRODUCTION RISK — ThinKV AND SideQuest HAVE NO PUBLIC CODE: Independent verification confirms neither ThinKV (ICLR 2026 Oral) nor SideQuest (Feb 2026) have released code, checkpoints, or implementations as of May 2026. ThinKV involves custom Triton kernels extending PagedAttention — reimplementation is non-trivial and could cost 20-40 H100-hours per baseline. Only R-KV and HqeKV have confirmed public code. Using 2 baselines without code in a 4-baseline plan creates significant execution risk.\", \"COMPUTE BUDGET 75% OVER USER CONSTRAINT: User specified ≤200 H100-hours as a HARD CONSTRAINT. Proposal requires ~350h. A concrete path to ~200h exists: reduce SWE-bench Lite to 50 instances (saves ~83h), reduce baselines from 4 to 3 by dropping either ThinKV or SideQuest (saves ~30-50h given no public code anyway), and tighten dev/debug buffer to 25h. Revised estimate: 50 SWE-bench × 2 models × 4 methods × 10min ≈ 67h + τ-bench 164 × 2 × 4 × 2min ≈ 44h + standard benchmarks ~40h + calibration 10h + ablations 15h + dev/debug 25h ≈ 201h.\", \"MODEL NAME ERROR: 'DeepSeek-R1-Distill-Qwen3-8B' does not exist. The correct model is 'DeepSeek-R1-0528-Qwen3-8B' (HuggingFace: deepseek-ai/DeepSeek-R1-0528-Qwen3-8B). It uses Qwen3-8B architecture with DeepSeek-R1-0528 tokenizer and achieves 86.0% on AIME 2024. The 'Distill' naming convention was used for Qwen2.5-based distillations, not Qwen3-based ones.\", \"VENUE AND TIMELINE MISMATCH: User's HARD CONSTRAINTS were ≤16 days and EMNLP 2026 (ARR May 25). Proposal explicitly declares EMNLP 2026 'NOT FEASIBLE' and targets AAAI 2027/ICLR 2027 — an honest acknowledgment, but this fundamentally fails to meet user requirements. The proposal should either commit to a drastically reduced EMNLP 2026 Findings sprint plan (1 model, 2 baselines with public code, 3 benchmarks, 4-page short paper, ~60h) or explicitly justify why this idea cannot serve the user's stated deadline.\"]\nFeedback: This is a dramatically improved proposal — all 7 Round 7 feedback items are fully addressed for the first time, the landscape is exceptional (30+ papers), NGC and CapKV are properly cited and differentiated, the MLA error is fixed, the agent scaffold is specified, and the benchmark gap table is included. The core contribution (trajectory-level Lagrangian for agentic KV caches) is confirmed novel via exhaustive search. The proposal is close to pass quality but blocked by feasibility concerns:\n\n1. **Fix baseline plan**: Replace ThinKV and/or SideQuest (no public code) with baselines that have confirmed code. Recommended 3-baseline plan: R-KV (public code, NeurIPS 2025), HqeKV (public code, ACL ARR 2026), and either (a) reimplemented ThinKV with 20-30h budgeted for Triton kernel development, or (b) a simpler proxy: uniform mixed-precision baseline (e.g., 4-bit/2-bit with attention-score-based partitioning) implementable in <8h. If ThinKV code releases before experiments begin (ICLR oral papers often release within months), add it.\n\n2. **Fit within 200 H100-hours**: Reduce SWE-bench Lite to 50 instances (still statistically meaningful for pass-rate differences >5%), reduce baselines to 3 (only those with public code or easy reimplementation), and tighten dev/debug to 25h. This yields ~200h.\n\n3. **Fix model name**: Change 'DeepSeek-R1-Distill-Qwen3-8B' to 'DeepSeek-R1-0528-Qwen3-8B' throughout. Verify tokenizer compatibility since it uses DeepSeek-R1-0528's tokenizer, not Qwen3's default.\n\n4. **Resolve venue**: Either (a) commit to EMNLP 2026 Findings with a concrete 14-day sprint: Day 1-4 implement Lagrangian solver + phase detection on vLLM, Day 5-8 run experiments (Qwen3-8B only, 2 baselines with public code: R-KV + HqeKV, 3 benchmarks: 30 SWE-bench instances + MMLU + LongBench), Day 9-12 write 4-page short paper, Day 13-14 polish. ~60 H100-hours. OR (b) explicitly state EMNLP 2026 is not achievable and present this as an AAAI 2027/ICLR 2027 submission, accepting the user may choose a different idea for their EMNLP deadline.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 8 轮修订，近 3 轮的平均分从 3.8 到 3.5，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-12T01:29:13.211Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T01:29:13.211Z",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284"
}
```

---

## Round 1

21 recorded events

### User

_source line 3 · 2026-05-12T01:29:13.242Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-11 (UTC).**

## Original idea
{
  "title": "Trajectory-Aware Joint Compression for Long-Horizon Agentic KV Caches",
  "core_problem": "Agentic LLM systems (coding agents, research agents, tool-use agents) maintain KV caches that grow across dozens of reasoning-and-action steps, often exceeding 100K tokens. Current KV cache compression methods — including strong joint quantization-eviction approaches like ThinKV, HqeKV, and ARKV, as well as future-aware eviction methods like NGC and LookaheadKV — were designed for single-turn or single-model inference and optimize per-step reconstruction error or per-step eviction quality independently. In multi-step agentic workloads, compression errors compound across planning steps: PM-KVQ (ICLR 2026) demonstrates that directly quantizing KV cache at each decoding step causes cumulative quantization error that degrades long-CoT reasoning by up to 8% versus progressive strategies; 'Hold Onto That Thought' (under review, ICLR 2026) empirically shows that existing KV compression strategies designed for prefill-phase long-context tasks degrade significantly on reasoning tasks requiring extended decoding. Theoretical analysis from 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) proves lower bounds showing exponential error growth Ω((n/s)^(T-1)) for oblivious cache strategies across T reasoning stages in k-hop pointer chasing; we note that this bound applies specifically to single-model multi-step reasoning with locality-respecting cache controllers, not directly to agentic tool-use workflows with external observation injection — the analogy is suggestive but not a formal proof. The empirical evidence from PM-KVQ and 'Hold Onto That Thought' provides the primary, more directly applicable motivation. No existing work formulates joint quantization-eviction that explicitly minimizes cumulative trajectory-level error for agentic workloads.",
  "opportunity": "Two converging trends expose a clear research gap. First, agentic inference is now the dominant LLM deployment pattern (SWE-bench, GAIA, τ-bench), but KV cache compression research overwhelmingly targets single-turn inference. Existing agentic KV cache works address only parts of the problem: SideQuest (Feb 2026) uses model-driven eviction but not quantization; CodeComp (April 2026) leverages structural code priors for eviction only; CacheTTL (Nov 2025) manages cache scheduling without compression; PBKV (May 2026) predicts future agent invocations for cache management but performs no within-request compression; KVFlow (NeurIPS 2025) optimizes prefix caching for multi-agent workflows without compression; EpiCache (Apple, Sep 2025) manages episodic multi-turn cache but targets conversational QA, not agentic tool-use. NGC (April 2026) learns trajectory-aware KV eviction via RL within single-model reasoning chains, jointly optimizing reasoning and memory management from task reward alone — the closest conceptual competitor, but it requires RL training, is eviction-only (no quantization), and operates on single-model reasoning traces without explicit agent step boundaries or external observation injection. CapKV (April 2026) derives information-theoretic KV eviction via the Information Bottleneck principle with capacity-aware scoring — theoretically grounded but eviction-only and per-step.\n\nSecond, single-turn KV cache compression has matured across multiple fronts: (a) joint quantization-eviction via ThinKV (ICLR 2026 Oral, 20x compression), HqeKV (per-element compression actions), ARKV (tri-state assignment); (b) future-aware eviction via NGC (RL-based trajectory-aware eviction for single-model reasoning), LookaheadKV (ICLR 2026, predictive eviction via lookahead tokens + LoRA); (c) optimal bit allocation via RateQuant (rate-distortion reverse waterfilling, May 2026) and MixedDimKV (Lagrangian dual decomposition for per-token dimensions); (d) temporal and structural KV management via TTKV (temporal tiering with heterogeneous precision), TRIM-KV/Cache What Lasts (ICLR 2026, learned retention gates with temporal decay), and Transactional Attention (structural anchor protection for value-bearing tokens); (e) information-theoretic eviction via CapKV (Information Bottleneck with statistical leverage scores). However, none model how compression decisions at step t propagate errors to steps t+1 through T in multi-step agentic workflows with external tool observations. The key insight: in agentic workloads, token importance is cross-step structured in ways that single-turn methods cannot exploit. Instruction and plan tokens maintain importance across all steps; current-step observations are critical but rapidly decay; historical tool outputs become redundant as new observations arrive. This temporal structure, combined with the empirically-grounded error compounding problem (PM-KVQ, 'Hold Onto That Thought'), demands a fundamentally different optimization objective: minimizing trajectory-level degradation rather than per-step reconstruction error.",
  "landscape": "**Joint quantization-eviction (single-turn):** ThinKV (ICLR 2026 Oral) applies thought-adaptive hybrid quantization-eviction achieving 20x compression with <5% KV cache — the strongest single-turn baseline. HqeKV (ACL ARR Jan 2026) provides an integrated optimizer selecting optimal compression actions (quantization level or eviction) per cached element under memory constraints. ARKV (arXiv Feb 2026) dynamically assigns tokens to Original/Quantization/Eviction states based on per-layer attention statistics. KVTC (ICLR 2026) achieves 20x via PCA + adaptive quantization + entropy coding.\n\n**Constrained optimization for KV compression:** MixedDimKV (March 2026) formulates KV cache compression as a constrained optimization problem using Lagrangian dual decomposition with bisection search over λ, allocating per-token dimensions under a memory budget. This uses the same Lagrangian optimization technique as TrajComp. The critical difference: MixedDimKV minimizes per-step reconstruction error (single-step objective), while TrajComp minimizes trajectory-level error accumulation across T agent steps (multi-step objective). The trajectory extension is non-trivial because: (i) the search space expands from per-step to cross-step — compressing token i at step t affects attention distributions at steps t+1...T; (ii) the objective changes from reconstruction fidelity to trajectory success rate; (iii) the importance model must account for temporal structure (persistent vs. decaying tokens) absent in single-turn settings. RateQuant (May 2026) applies rate-distortion theory with reverse waterfilling for optimal per-head bit allocation — a complementary per-step optimization that TrajComp could incorporate as a sub-routine for within-step bit allocation.\n\n**Trajectory-aware and future-aware eviction:** NGC (April 2026, arXiv:2604.18002) learns trajectory-aware KV eviction via RL, treating both reasoning tokens and cache-eviction decisions as discrete actions sampled from the language model, trained end-to-end from outcome-based task reward alone. On Countdown, AMC, and AIME, NGC achieves 2-3x peak KV cache compression while maintaining strong accuracy. TrajComp differs from NGC in three key ways: (1) training-free (Lagrangian optimization vs. RL training required), (2) joint quantization-eviction (vs. eviction-only), and (3) designed for multi-step agentic workflows with explicit step boundaries and external observation injection (vs. single-model reasoning traces where the model interleaves thinking and eviction). LookaheadKV (ICLR 2026, Samsung) predicts future attention patterns via trainable lookahead tokens + LoRA, achieving <0.7% drop at 81% compression — also eviction-only and single-turn.\n\n**Information-theoretic eviction:** CapKV (April 2026, arXiv:2604.25975) derives capacity-aware KV eviction via the Information Bottleneck principle, using a log-determinant approximation with statistical leverage scores under a linear-Gaussian surrogate of attention. It provides a theoretically grounded mechanism that replaces heuristic selection with capacity-maximization. TrajComp differs: joint quantization-eviction with a trajectory-level multi-step objective vs. CapKV's per-step information-theoretic eviction-only framework.\n\n**Temporal and structural KV management:** TTKV (March 2026) partitions KV cache into temporal tiers with heterogeneous precision across HBM/DRAM, achieving 76% latency reduction on 128K contexts. Its temporal tiering directly overlaps with TrajComp's 'decaying context' category — but TTKV is a system-level memory hierarchy approach without trajectory-aware error optimization. TRIM-KV/Cache What Lasts (ICLR 2026) learns per-token retention gates with temporal decay via distillation — conceptually similar to cross-step importance decay, but training-required, eviction-only, and single-turn. Transactional Attention (April 2026) protects structural anchor tokens (credentials, API keys) from eviction via semantic sponsorship — overlaps with TrajComp's 'persistent anchors' category, but is domain-specific to credential/configuration retention and does not perform compression.\n\n**Agentic KV cache management:** SideQuest (Feb 2026) uses the reasoning model itself to identify dispensable tokens, achieving 65% peak token reduction on agentic tasks — eviction only, no quantization. CodeComp (April 2026) uses Code Property Graph priors for structure-aware eviction in agentic coding — domain-specific and eviction only. CacheTTL/Continuum (Nov 2025) manages multi-turn cache scheduling with TTL-based retention. PBKV (May 2026) predicts future agent invocations and manages cache across workflow steps — system-level scheduling without within-request compression. KVFlow (NeurIPS 2025) optimizes prefix caching for multi-agent workflows. EpiCache (Apple, Sep 2025) manages episodic multi-turn cache for conversational QA. Agent Memory Below the Prompt (Feb 2026) persists Q4 KV caches across agents on edge devices. KVComm (Oct 2025) enables cross-context KV sharing.\n\n**Other relevant methods:** TriAttention (MIT/NVIDIA, April 2026) achieves 10.7x via trigonometric key importance scoring. R-KV (NeurIPS 2025) achieves 100% accuracy at 10% KV via redundancy-aware eviction with public code. DMS (NeurIPS 2025) achieves 8x with lightweight training. EVICPRESS (Microsoft, Dec 2025) jointly optimizes compression and eviction across storage tiers. PM-KVQ shows progressive mixed-precision reduces cumulative quantization error in long-CoT. TurboQuant (ICLR 2026) addresses inner-product estimation bias compounding across attention computations. 'Not All Bits Are Equal' (ICLR 2026) shows optimal compression strategy is scale-dependent.\n\n**Error compounding theory and evidence:** 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) proves that under k-hop pointer chasing with cache size s, oblivious caches suffer exponential error growth Ω((n/s)^(T-1)). We note this bound applies specifically to k-hop pointer chasing with locality-respecting cache controllers in single-model multi-step reasoning; its extension to agentic tool-use with external observation injection is an analogy, not a formal proof. The empirical evidence from PM-KVQ (cumulative quantization error degrades long-CoT by up to 8%) and 'Hold Onto That Thought' (compression designed for prefill degrades extended-decoding reasoning) provides the primary and more directly applicable motivation for trajectory-aware compression.\n\nNo prior work formulates a trajectory-level objective for joint quantization-eviction in agentic KV caches with explicit cross-step error accumulation control. The closest works are NGC (trajectory-aware but RL-required, eviction-only, single-model) and MixedDimKV (same Lagrangian technique but per-step objective). TrajComp uniquely combines: (1) joint quant-eviction, (2) trajectory-level multi-step objective, (3) training-free Lagrangian optimization, (4) agentic workflow structure exploitation.",
  "approach": "We propose TrajComp (Trajectory-Aware Joint Compression), which formulates a single dual-constrained Lagrangian objective jointly optimizing token retention probabilities and per-token bit allocation under memory and cumulative trajectory-error budgets.\n\n**(1) Cross-step error propagation model:** Unlike ThinKV/HqeKV/MixedDimKV which minimize per-step reconstruction error independently, and unlike NGC which learns trajectory-aware eviction through RL training, TrajComp models error propagation across agent steps in a training-free manner. Compressing token i at step t contributes weighted error proportional to Σ_{s=t+1}^{T} γ^{s-t} × importance_i, where γ is the empirically-calibrated step-wise error propagation rate. The dual-constrained Lagrangian L = Σ_t error_t(s,q) + λ_mem(M(s,q) - B_mem) + λ_err(E_cumul(s,q,γ) - B_err) enables smooth Pareto-optimal tradeoffs via dual gradient descent on both multipliers. Note: MixedDimKV uses Lagrangian dual decomposition with bisection for a single memory constraint and per-step objective; TrajComp extends this to dual constraints (memory + trajectory error) with a cross-step objective, requiring the error propagation model as additional machinery.\n\n**γ calibration procedure:** For each target model, run N=10 agent trajectories per benchmark (SWE-bench Lite subset, τ-bench) with full (uncompressed) KV cache and with uniformly 4-bit quantized KV cache. At each agent step boundary t, measure KL divergence D_KL(P_full^t || P_compressed^t) of the attention distributions. Compute per-step propagation ratios r_t = D_KL^{t+1} / D_KL^t across all steps and trajectories. Set γ = median(r_t) across steps and trajectories. Report sensitivity analysis: if γ varies by >20% across tasks within a benchmark, use per-benchmark γ and budget the additional calibration cost (~2h per model-benchmark pair). Based on PM-KVQ's observations of progressive error accumulation, we expect γ ∈ [0.7, 0.95]. Total calibration cost: ~10 H100-hours for 2 models × 2 agentic benchmarks × 10 trajectories.\n\n**(2) Agent-phase token categorization:** Rather than ThinKV's within-turn thought types, TrajComp defines categories by agentic workflow structure: (a) Persistent anchors — system prompts, instructions, plans — never compressed (analogous to Transactional Attention's structural anchors, but generalized beyond credentials to all instruction-bearing tokens); (b) Active context — current tool output and recent reasoning — retained at 4-bit; (c) Decaying context — older observations — progressively compressed (4-bit → 2-bit → evict) with schedule determined by the Lagrangian solver based on temporal distance and cross-step importance (analogous to TTKV's temporal tiering, but driven by trajectory-level optimization rather than fixed temporal heuristics); (d) Ephemeral tokens — intermediate tool formatting, API boilerplate — immediately evicted.\n\n**Phase detection strategy:** For structured agent frameworks (ReAct, function-calling with explicit Thought/Action/Observation tags), use lightweight pattern matching on special tokens and turn boundaries (zero overhead). For free-form reasoning models where thinking and acting interleave without clear delimiters, fall back to attention entropy thresholds: compute per-token attention entropy at step boundaries; tokens with consistently high entropy across recent steps are classified as ephemeral, tokens with low entropy as active/persistent. This dual strategy is benchmarked explicitly: we report phase classification accuracy and its impact on trajectory success for both detection methods.\n\n**Agent scaffold specification:** For SWE-bench Lite evaluation, we use SWE-agent with ReAct prompting, max 30 turns, 16K tokens per turn, matching standard evaluation protocols. For τ-bench, we use the official τ-bench evaluation harness (github.com/sierra-research/tau-bench) with default configuration across retail and airline domains.\n\n**(3) GQA-aware compression:** Both evaluation models (Qwen3-8B: 32 query heads, 8 KV heads; DeepSeek-R1-Distill-Qwen3-8B: 32 query heads, 8 KV heads) use Grouped Query Attention (GQA), where multiple query heads share KV heads. TrajComp allocates compression budgets at the KV-head group level, accounting for the fact that compressing a single KV head affects all query heads in its group. MLA adaptation (for full DeepSeek-V3/R1 671B models) is left as future work, as MLA's latent-space KV representation requires a fundamentally different compression strategy that cannot be validated on our GQA-only evaluation models.\n\nThe dual gradient descent operates at agent step boundaries (not every token), making it lightweight. A single re-optimization pass over the full KV cache occurs when a new agent step begins.\n\n**Wall-clock and throughput reporting:** We report: (a) Lagrangian solver time per agent step as a function of KV cache size — expected to be <10ms for dual gradient descent over ~100K tokens, dominated by importance score computation not the optimization itself; (b) end-to-end latency per agent step (including compression overhead) vs. baselines on H100-80GB; (c) tokens/second throughput at matched compression ratios. The solver adds negligible overhead relative to the LLM forward pass (~500ms-2s per agent step for 8B models).\n\n**8B model capability consideration:** We acknowledge that 8B models achieve relatively low base success rates on SWE-bench (e.g., RepoForge-8B: ~17% on SWE-bench Verified). To ensure meaningful compression comparisons despite low base rates: (a) we report not only binary task success but also trajectory-quality metrics — steps completed before failure, tool-call coherence, and reasoning degradation measured via attention distribution divergence from full-cache trajectories; (b) τ-bench serves as the primary agentic benchmark, where 8B models may achieve higher success rates on the structured customer-service tasks; (c) if both models achieve <10% success on SWE-bench Lite 100-instance subset, we supplement with a subset of 50 instances known to be solvable by 8B models (identified via full-cache runs).\n\n**User-requested benchmark gap table:**\n| Benchmark | Status | Est. Cost | Reason |\n|---|---|---|---|\n| MMLU | Included | 5h | General capability check |\n| LongBench | Included | 20h | Long-context evaluation |\n| AIME 2025 | Included | 8h | Reasoning evaluation |\n| MATH-500 | Included | 7h | Reasoning evaluation |\n| HumanEval | **Added** | 2h | Code generation, low cost |\n| MT-Bench | **Added** | 2h | Multi-turn chat quality, low cost |\n| Perplexity (Wiki/C4) | **Added** | 3h | Language modeling quality, low cost |\n| SWE-bench Lite (100 instances) | Included | ~167h | Primary agentic benchmark (reduced from 300; 10 min/instance realistic) |\n| τ-bench (164 tasks) | Included | ~55h | Primary agentic benchmark |\n| RULER | Dropped | ~100h | Compute-prohibitive for 2 models × 5 methods |\n| GAIA | Dropped | ~80h | Too expensive per instance |\n| LiveCodeBench | Dropped | ~40h | Compute-prohibitive |\n| GPQA | Dropped | ~15h | Lower priority vs. AIME/MATH |\n\n**Evaluation scope (designed for ~350 H100-hours):** Models: Qwen3-8B, DeepSeek-R1-Distill-Qwen3-8B (2 models, both using GQA attention). Baselines: ThinKV, HqeKV, SideQuest, R-KV (4 baselines — R-KV replaces ForesightKV, which lacks public code or checkpoints; R-KV has public code at github.com/Zefan-Cai/R-KV and provides a strong redundancy-aware eviction baseline from NeurIPS 2025). NGC and CapKV are discussed as related work but not re-implemented as baselines: NGC requires RL training (~30-50 H100-hours to reproduce per model) and CapKV's leverage-score computation is complementary to but not directly comparable with joint quant-eviction methods. Dropped baselines: ARKV, KVTC, DMS, CodeComp, ForesightKV (reported as ablation references from literature, not re-implemented; ForesightKV lacks public code/checkpoints and reproducing its supervised + RL training pipeline would cost ~40-60 H100-hours for 2 models). Benchmarks: 2 agentic (SWE-bench Lite 100 instances, τ-bench 164 tasks), 2 reasoning (AIME 2025, MATH-500), 1 long-context (LongBench), 1 general (MMLU), 1 code (HumanEval), 1 chat (MT-Bench), 1 perplexity (WikiText/C4). The key metric is trajectory-level success rate at matched compression ratio for agentic benchmarks, and standard accuracy/perplexity for non-agentic benchmarks.\n\n**Compute breakdown (revised with realistic SWE-bench timing):** SWE-bench Lite: 100 instances × 2 models × 5 methods × ~10 min/instance ≈ 167h. τ-bench: 164 tasks × 2 models × 5 methods × ~2 min ≈ 55h. AIME 2025 + MATH-500: ~15h. LongBench: ~20h. MMLU: ~5h. HumanEval: ~2h. MT-Bench: ~2h. Perplexity (Wiki/C4): ~3h. γ calibration: ~10h. Ablations (phase detection, γ sensitivity, anchor ratio): ~25h. Wall-clock benchmarking: ~5h. Development/debugging buffer: ~40h. Total: ~350 H100-hours.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~350h H100-80GB",
      "gpu_utilization": "35-45% effective — idle time during Lagrangian solver implementation, γ calibration analysis, and phase detection debugging",
      "timeline": "3-4 months",
      "team": "1-2 researchers (systems ML + optimization background)",
      "estimated_gpu_cost": "$875 (350h × ~$2.50/h H100 spot pricing)"
    },
    "human_in_loop": {
      "gpu_hours": "~350h H100-80GB",
      "gpu_utilization": "55-65% — agent handles baseline reproduction (R-KV from public code, ThinKV/HqeKV reimplementation), agentic benchmark setup (SWE-agent docker, τ-bench harness), γ calibration sweeps, and wall-clock benchmarking; human guides Lagrangian formulation, error propagation model design, and phase detection strategy",
      "timeline": "2-3 months",
      "team": "1 researcher, ~45min/day review",
      "claude_api_cost": "$250-400 (~2500-4000 turns for agent pipeline development, experiment orchestration, result analysis)",
      "estimated_gpu_cost": "$875 (350h × ~$2.50/h)",
      "risk_note": "Primary risk is SWE-bench evaluation infrastructure — SWE-agent requires docker environments and tool sandboxing that may need debugging. γ calibration may require more trajectories than budgeted if variance is high across task types. 8B model low success rates on SWE-bench may limit statistical power; τ-bench results may be more informative for the agentic contribution."
    },
    "auto_research": {
      "gpu_hours": "~500h H100-80GB (sweeping γ calibration, phase boundary thresholds, dual multiplier schedules, SWE-bench at 10 min/instance, and wall-clock profiling across configurations)",
      "gpu_utilization": "65-75% — SWE-bench instances at ~10 min each create pipeline gaps; agent queues ablation studies during these gaps",
      "timeline": "3-5 weeks with 2-4 concurrent H100s",
      "team": "0 (initial 3-hour setup: agent harness configs, model downloads, SWE-agent docker verification, baseline code checkout)",
      "claude_api_cost": "$500-800 (~5000-8000 turns including SWE-agent docker debugging and failed exploration paths)",
      "estimated_gpu_cost": "$1250 (500h × ~$2.50/h)",
      "speed_bottleneck": "SWE-bench Lite instances average ~10 minutes each. With 100 instances × 10 configurations (2 models × 5 methods) ≈ 1000 runs. At 10 min avg on H100, this is ~167h — the dominant compute cost. τ-bench adds ~55h.",
      "risk_note": "Agent may struggle with SWE-agent docker orchestration without human intervention. Risk of over-exploring γ sensitivity without converging on the key narrative. 8B model failure rates on SWE-bench may lead agent to cycle through debugging steps rather than accepting low base rates."
    }
  },
  "target_venues": [
    "AAAI 2027 (expected deadline: ~August 2026 based on historical pattern; primary target, ~82 days from today — tight given 350h compute budget but feasible with 2-4 concurrent GPUs)",
    "ICLR 2027 (expected abstract deadline: ~September 19, 2026 based on ICLR 2026 pattern; primary target, more comfortable timeline)",
    "EMNLP 2026 (ARR deadline: May 25, 2026) — NOT FEASIBLE at 14 days given 350h compute requirement and no pre-existing implementation"
  ],
  "level": "solid",
  "key_references": [
    "ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models (ICLR 2026 Oral)",
    "HqeKV: Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference (ACL ARR Jan 2026)",
    "ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget (arXiv Feb 2026)",
    "NGC: Neural Garbage Collection: Learning to Forget while Learning to Reason (arXiv April 2026, arXiv:2604.18002) — RL-based trajectory-aware KV eviction for single-model reasoning, eviction-only, 2-3x compression on Countdown/AMC/AIME",
    "CapKV: Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective (arXiv April 2026, arXiv:2604.25975) — Information Bottleneck principle with statistical leverage scores, eviction-only, per-step",
    "LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation (ICLR 2026 Poster, Samsung, arXiv:2603.10899) — predictive eviction via lookahead tokens + LoRA",
    "TTKV: Temporal-Tiered KV Cache for Long-Context LLM Inference (arXiv March 2026, arXiv:2604.19769) — temporal tiering with heterogeneous precision across HBM/DRAM",
    "TRIM-KV / Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs (ICLR 2026, arXiv:2512.03324) — learned per-token retention gates with temporal decay",
    "RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory (arXiv May 2026, arXiv:2605.06675) — reverse waterfilling for per-head bit allocation",
    "Transactional Attention: Semantic Sponsorship for KV-Cache Retention (arXiv April 2026, arXiv:2604.11288) — structural anchor protection for value-bearing tokens",
    "Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression [MixedDimKV] (arXiv March 2026, arXiv:2603.20616) — Lagrangian dual decomposition for per-token dimension allocation",
    "PBKV: Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management (arXiv May 2026, arXiv:2605.06472) — prediction-based agent cache scheduling",
    "KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows (NeurIPS 2025, arXiv:2507.07400) — workflow-aware prefix caching",
    "EpiCache: Episodic KV Cache Management for Long Conversational Question Answering (Apple, arXiv Sep 2025, arXiv:2509.17396) — episodic multi-turn cache management",
    "SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning (arXiv Feb 2026)",
    "CodeComp: Structural KV Cache Compression for Agentic Coding (arXiv April 2026)",
    "CacheTTL/Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live (arXiv Nov 2025)",
    "R-KV: Redundancy-aware KV Cache Compression for Reasoning Models (NeurIPS 2025, github.com/Zefan-Cai/R-KV) — redundancy-aware eviction with public code, used as baseline",
    "How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers (arXiv April 2026, arXiv:2604.17935) — theoretical bounds on cache compression vs. reasoning depth (k-hop pointer chasing; analogy to agentic setting, not direct proof)",
    "PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs (arXiv May 2025, OpenReview Oct 2025) — empirical evidence of cumulative quantization error in long-CoT",
    "Hold Onto That Thought: Assessing KV Cache Compression On Reasoning (arXiv Dec 2025, arXiv:2512.12008) — empirical assessment of compression degradation on reasoning tasks",
    "TriAttention: Efficient Long Reasoning with Trigonometric KV Compression (MIT/NVIDIA, arXiv April 2026)",
    "KV Cache Transform Coding [KVTC] for Compact Storage in LLM Inference (NVIDIA, ICLR 2026)",
    "Inference-Time Hyper-Scaling with KV Cache Compression [DMS] (NeurIPS 2025)",
    "EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving (Microsoft, arXiv Dec 2025)",
    "Not All Bits Are Equal: How Model Scale Changes Memory-Optimal Reasoning (ICLR 2026)",
    "TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate (ICLR 2026) — inner-product bias compounding",
    "ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution (arXiv Feb 2026, arXiv:2602.03203) — RL-based future-aware eviction, eviction-only, single-turn; no public code/checkpoints available, discussed as related work only",
    "Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices (arXiv Feb 2026, arXiv:2603.04428)",
    "KVComm: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems (arXiv Oct 2025)",
    "Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys (AAAI 2026)"
  ],
  "description": "We propose TrajComp (Trajectory-Aware Joint Compression), a training-free method that jointly optimizes token eviction and per-token bit allocation for KV caches in long-horizon agentic LLM workloads through a dual-constrained Lagrangian objective that explicitly minimizes trajectory-level error accumulation. The empirical motivation comes from PM-KVQ (ICLR 2026), which demonstrates that cumulative quantization error degrades long-CoT reasoning by up to 8% versus progressive strategies, and from 'Hold Onto That Thought' (2025), which shows that compression strategies designed for prefill degrade on extended-decoding reasoning. Theoretical analysis from 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) proves exponential error growth Ω((n/s)^(T-1)) for oblivious cache strategies in k-hop pointer chasing; we note this bound applies to single-model reasoning with locality-respecting cache controllers — its extension to agentic tool-use with external observation injection is a suggestive analogy, not a formal proof.\n\nThe landscape includes strong single-turn methods across multiple fronts: joint quant-eviction (ThinKV at 20x, HqeKV, ARKV), future-aware and trajectory-aware eviction (NGC via RL-based eviction for single-model reasoning achieving 2-3x compression, LookaheadKV via predictive attention), information-theoretic eviction (CapKV via Information Bottleneck with statistical leverage scores), optimal bit allocation (RateQuant via rate-distortion, MixedDimKV via Lagrangian dual), and temporal/structural management (TTKV temporal tiering, TRIM-KV learned retention, Transactional Attention anchor protection). Agentic-specific works (SideQuest, CodeComp, PBKV, KVFlow, EpiCache) address scheduling and eviction but not joint compression. NGC is the closest conceptual competitor but differs fundamentally: it requires RL training (vs. training-free), is eviction-only (vs. joint quant-eviction), and operates on single-model reasoning traces (vs. multi-step agentic workflows with external observations). No prior work combines joint quant-eviction with a trajectory-level multi-step objective for agentic workloads.\n\nTrajComp fills this gap with two core contributions: (1) A cross-step error propagation model that weights compression decisions by their γ-discounted impact across all future agent steps, formalized as a dual-constrained Lagrangian with separate memory and trajectory-error budget multipliers. γ is calibrated empirically via KL divergence propagation measurement. This extends MixedDimKV's Lagrangian dual (which uses the same optimization technique but minimizes per-step reconstruction error) to a trajectory-level objective — a non-trivial extension because the search space expands cross-step and the importance model must capture temporal structure. (2) Agent-phase token categorization (persistent anchors, active context, decaying context, ephemeral tokens) that exploits cross-step importance structure unique to agentic workflows, with dual detection strategies: pattern matching for structured frameworks (ReAct in SWE-agent) and attention entropy fallback for free-form reasoning. Both contributions are training-free, unlike NGC's RL approach. MLA adaptation is identified as future work.\n\nEvaluation uses 2 models (Qwen3-8B, DeepSeek-R1-Distill-Qwen3-8B — both GQA attention), 4 baselines (ThinKV, HqeKV, SideQuest, R-KV; R-KV replaces ForesightKV which lacks public code), and 9 benchmarks: 2 agentic (SWE-bench Lite 100 instances via SWE-agent with ReAct/30 turns/16K tokens, τ-bench 164 tasks via official harness), 2 reasoning (AIME 2025, MATH-500), 1 long-context (LongBench), 1 general (MMLU), 1 code (HumanEval), 1 chat (MT-Bench), 1 perplexity (WikiText/C4) — scoped to ~350 H100-hours with realistic 10 min/instance SWE-bench timing. We acknowledge 8B models achieve low base success rates on SWE-bench (~17%) and supplement binary success with trajectory-quality metrics. Reports include wall-clock latency, Lagrangian solver overhead per agent step, and tokens/second throughput on H100. Primary targets are AAAI 2027 (~August 2026) and ICLR 2027 (~September 2026).",
  "project_name": "trajcomp_agentic_kvcache",
  "source": "web_research"
}

## Reviewer feedback (round 8)
Issues: ["BASELINE REPRODUCTION RISK — ThinKV AND SideQuest HAVE NO PUBLIC CODE: Independent verification confirms neither ThinKV (ICLR 2026 Oral) nor SideQuest (Feb 2026) have released code, checkpoints, or implementations as of May 2026. ThinKV involves custom Triton kernels extending PagedAttention — reimplementation is non-trivial and could cost 20-40 H100-hours per baseline. Only R-KV and HqeKV have confirmed public code. Using 2 baselines without code in a 4-baseline plan creates significant execution risk.", "COMPUTE BUDGET 75% OVER USER CONSTRAINT: User specified ≤200 H100-hours as a HARD CONSTRAINT. Proposal requires ~350h. A concrete path to ~200h exists: reduce SWE-bench Lite to 50 instances (saves ~83h), reduce baselines from 4 to 3 by dropping either ThinKV or SideQuest (saves ~30-50h given no public code anyway), and tighten dev/debug buffer to 25h. Revised estimate: 50 SWE-bench × 2 models × 4 methods × 10min ≈ 67h + τ-bench 164 × 2 × 4 × 2min ≈ 44h + standard benchmarks ~40h + calibration 10h + ablations 15h + dev/debug 25h ≈ 201h.", "MODEL NAME ERROR: 'DeepSeek-R1-Distill-Qwen3-8B' does not exist. The correct model is 'DeepSeek-R1-0528-Qwen3-8B' (HuggingFace: deepseek-ai/DeepSeek-R1-0528-Qwen3-8B). It uses Qwen3-8B architecture with DeepSeek-R1-0528 tokenizer and achieves 86.0% on AIME 2024. The 'Distill' naming convention was used for Qwen2.5-based distillations, not Qwen3-based ones.", "VENUE AND TIMELINE MISMATCH: User's HARD CONSTRAINTS were ≤16 days and EMNLP 2026 (ARR May 25). Proposal explicitly declares EMNLP 2026 'NOT FEASIBLE' and targets AAAI 2027/ICLR 2027 — an honest acknowledgment, but this fundamentally fails to meet user requirements. The proposal should either commit to a drastically reduced EMNLP 2026 Findings sprint plan (1 model, 2 baselines with public code, 3 benchmarks, 4-page short paper, ~60h) or explicitly justify why this idea cannot serve the user's stated deadline."]
Feedback: This is a dramatically improved proposal — all 7 Round 7 feedback items are fully addressed for the first time, the landscape is exceptional (30+ papers), NGC and CapKV are properly cited and differentiated, the MLA error is fixed, the agent scaffold is specified, and the benchmark gap table is included. The core contribution (trajectory-level Lagrangian for agentic KV caches) is confirmed novel via exhaustive search. The proposal is close to pass quality but blocked by feasibility concerns:

1. **Fix baseline plan**: Replace ThinKV and/or SideQuest (no public code) with baselines that have confirmed code. Recommended 3-baseline plan: R-KV (public code, NeurIPS 2025), HqeKV (public code, ACL ARR 2026), and either (a) reimplemented ThinKV with 20-30h budgeted for Triton kernel development, or (b) a simpler proxy: uniform mixed-precision baseline (e.g., 4-bit/2-bit with attention-score-based partitioning) implementable in <8h. If ThinKV code releases before experiments begin (ICLR oral papers often release within months), add it.

2. **Fit within 200 H100-hours**: Reduce SWE-bench Lite to 50 instances (still statistically meaningful for pass-rate differences >5%), reduce baselines to 3 (only those with public code or easy reimplementation), and tighten dev/debug to 25h. This yields ~200h.

3. **Fix model name**: Change 'DeepSeek-R1-Distill-Qwen3-8B' to 'DeepSeek-R1-0528-Qwen3-8B' throughout. Verify tokenizer compatibility since it uses DeepSeek-R1-0528's tokenizer, not Qwen3's default.

4. **Resolve venue**: Either (a) commit to EMNLP 2026 Findings with a concrete 14-day sprint: Day 1-4 implement Lagrangian solver + phase detection on vLLM, Day 5-8 run experiments (Qwen3-8B only, 2 baselines with public code: R-KV + HqeKV, 3 benchmarks: 30 SWE-bench instances + MMLU + LongBench), Day 9-12 write 4-page short paper, Day 13-14 polish. ~60 H100-hours. OR (b) explicitly state EMNLP 2026 is not achievable and present this as an AAAI 2027/ICLR 2027 submission, accepting the user may choose a different idea for their EMNLP deadline.

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
这个 idea 已经经过 8 轮修订，近 3 轮的平均分从 3.8 到 3.5，没有明显改善。

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
  "promptId": "750c5be4-1e10-4956-bb2a-aaacbea26d97",
  "type": "user",
  "uuid": "352ffe66-bc1e-4024-8a80-196b3a7c7e2e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T01:29:13.239Z_

```json
{
  "parentUuid": "352ffe66-bc1e-4024-8a80-196b3a7c7e2e",
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
  "uuid": "fd293685-7302-4927-a135-05575f805284",
  "timestamp": "2026-05-12T01:29:13.239Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T01:29:13.239Z_

```json
{
  "parentUuid": "fd293685-7302-4927-a135-05575f805284",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3e0354a7-fc2b-4a37-aea1-cd0e67d1427f",
  "timestamp": "2026-05-12T01:29:13.239Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Trajectory-Aware Joint Compression for Long-Horizon Agentic KV Caches\"…",
  "leafUuid": "3e0354a7-fc2b-4a37-aea1-cd0e67d1427f",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 sprint: trajectory-aware KV compression for agentic LLMs",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284"
}
```

---

### Assistant

_source line 8 · 2026-05-12T01:29:28.760Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully before doing any research.

The reviewer has 4 specific issues:
1. **Baseline reproduction risk**: ThinKV and SideQuest have no public code. Need to replace with baselines that have confirmed code.
2. **Compute budget**: 350h exceeds the 200h hard constraint. Need to reduce to ~200h.
3. **Model name error**: "DeepSeek-R1-Distill-Qwen3-8B" doesn't exist. Should be "DeepSeek-R1-0528-Qwen3-8B".


4. **Venue/timeline mismatch**: EMNLP 2026 with ARR deadline May 25 is only 16 days away, but the proposal claims it's not feasible.

The stagnation warning signals 8 rounds without score improvement, yet the reviewer confirms the core contribution is genuinely novel and the research landscape is strong—the real problems are purely about execution and feasibility planning. Since the idea itself is validated, this looks like a major revision where I need to fix the practical constraints rather than rethink the concept.

Now I'm focusing on the specific blockers: checking which baseline implementations are publicly available, correcting the model name, bringing compute requirements down to 200 hours or less, and clarifying the venue situation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e0354a7-fc2b-4a37-aea1-cd0e67d1427f",
  "isSidechain": false,
  "requestId": "req_011CawopjWkmyWdmkB5C2Wpi",
  "type": "assistant",
  "uuid": "40587d94-972b-4b9e-9ef2-6f7d184679d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0189GPSLf971Y8rVDNA2GUy2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17243,
      "cache_read_input_tokens": 11841,
      "output_tokens": 876,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 876,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17243
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

_source line 9 · 2026-05-12T01:29:28.771Z_

I'll research the four specific issues the reviewer raised: baseline code availability, the correct DeepSeek model name, compute budget reduction, and venue feasibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40587d94-972b-4b9e-9ef2-6f7d184679d1",
  "isSidechain": false,
  "requestId": "req_011CawopjWkmyWdmkB5C2Wpi",
  "type": "assistant",
  "uuid": "83e03f8c-1765-4cfa-85be-991660f676d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0189GPSLf971Y8rVDNA2GUy2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17243,
      "cache_read_input_tokens": 11841,
      "output_tokens": 876,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 876,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17243
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

_source line 10 · 2026-05-12T01:29:37.801Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019fRJxFz5woPeQie7zbLhiE`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify baseline code availability",
  "prompt": "I need to verify which KV cache compression baselines have publicly available code as of May 2026. Search for the following and report what you find for EACH:\n\n1. **ThinKV** (ICLR 2026 Oral) - \"Thought-Adaptive KV Cache Compression\" - search GitHub for \"ThinKV\" and any repo associated with this paper\n2. **SideQuest** (Feb 2026) - \"Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning\" - search GitHub for \"SideQuest KV cache\"\n3. **HqeKV** (ACL ARR Jan 2026) - \"Hybrid Quantization and Eviction for KV Cache\" - search GitHub for \"HqeKV\"\n4. **R-KV** (NeurIPS 2025) - \"Redundancy-aware KV Cache Compression\" - verify the repo at github.com/Zefan-Cai/R-KV exists\n5. **EVICPRESS** (Microsoft, Dec 2025) - \"Joint KV-Cache Compression and Eviction\" - search for its code\n6. **DMS** (NeurIPS 2025) - \"Inference-Time Hyper-Scaling with KV Cache Compression\" - search for its code\n\nFor each, use WebSearch to find their GitHub repos. Then use WebFetch to verify if the repos actually exist and contain implementation code. Report: paper name, whether code exists, repo URL if found, and any notes about implementation complexity.\n\nBe thorough - check the paper's arXiv page for code links too."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83e03f8c-1765-4cfa-85be-991660f676d3",
  "isSidechain": false,
  "requestId": "req_011CawopjWkmyWdmkB5C2Wpi",
  "type": "assistant",
  "uuid": "1e3bbb47-6c49-4110-a8f8-8857520a3a7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0189GPSLf971Y8rVDNA2GUy2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17243,
      "cache_read_input_tokens": 11841,
      "output_tokens": 876,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 876,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17243
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

_source line 11 · 2026-05-12T01:33:49.440Z_

<details><summary>↩ Tool result · `toolu_019fRJxFz5woPeQie7zbLhiE`</summary>

```text
Now I have a thorough picture. Let me compile the final report.

---

Here is the comprehensive report on public code availability for each of the six KV cache compression baselines, as of May 2026:

---

## 1. ThinKV (ICLR 2026 Oral) -- "Thought-Adaptive KV Cache Compression"

**Code publicly available: NO (standalone repo not found)**

- No dedicated GitHub repository was found for ThinKV. The lead author (Akshat Ramachandran, Georgia Tech / NVIDIA Research) does not have a ThinKV repo on GitHub. The arXiv page, OpenReview page, and the author's personal website contain no code links.
- **However**, NVIDIA's `kvpress` library (`github.com/NVIDIA/kvpress`) does include a method called **ThinKPress**, which compresses key dimensions based on channel attention scores on the last queries. This appears to be a related but potentially simplified implementation within a broader framework -- it is distinct from the full ThinKV system described in the paper (which includes thought-type classification, hybrid quantization-eviction, and a custom PagedAttention kernel for memory slot reuse).
- **Note:** The full paper describes custom CUDA kernels extending PagedAttention, which is a non-trivial implementation. The `kvpress` integration likely does not include the full thought-adaptive pipeline.

**Partial code via:** `https://github.com/NVIDIA/kvpress` (ThinKPress method)

---

## 2. SideQuest (Feb 2026) -- "Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning"

**Code publicly available: NO**

- No GitHub repository was found. The arXiv page (2602.22603) has no code links. The first author, Sanjay Kariyappa (NVIDIA), has 10 repositories on GitHub -- none are related to SideQuest or KV cache. The paper is very recent (Feb 2026) and code has not been released.
- The approach is architecturally distinctive: it trains a model (with only 215 samples) to reason about which tokens to evict, framing cache management as a parallel auxiliary task. Reproducing this without official code would require implementing the side-channel reasoning mechanism and the training procedure.

---

## 3. HqeKV (ACL ARR Jan 2026) -- "Hybrid Quantization and Eviction for KV Cache"

**Code publicly available: YES**

- **Repo:** `https://github.com/skywclouds/HqeKV`
- **Status:** The repository exists and contains implementation code.
- **Contents:** Python (67.3%) + CUDA (31.8%). Includes `model/`, `quant/` (with CUDA kernels), `config/`, `tests/`, `utils/` directories. Has inference scripts (`pred_long_bench_hq.py`), evaluation scripts (`eval_long_bench.py`), `requirements.txt`, and `pyproject.toml`.
- **Features:** Configurable compression ratios, offline precision ratio optimization via Optuna, memory usage and throughput benchmarking.
- **Community:** 2 stars, 0 forks -- very low adoption so far.
- **Complexity:** Moderate-to-high. The CUDA kernels for quantization comprise ~32% of the codebase, and the Optuna-based optimizer adds configuration complexity.

---

## 4. R-KV (NeurIPS 2025) -- "Redundancy-aware KV Cache Compression"

**Code publicly available: YES**

- **Repo:** `https://github.com/Zefan-Cai/R-KV`
- **Status:** The repository exists and is actively maintained.
- **Contents:** Python (87%) + CUDA (7.8%) + C++ (2.9%). Includes core `/rkv` package, plus integrations with **HuggingFace**, **vLLM**, **SGLang**, and **FlashInfer** frameworks. Has `setup.py` for pip installation.
- **Community:** 1.2k stars, 192 forks, 16 open issues -- strong adoption.
- **Complexity:** Moderate-to-high. Implements a four-stage compression pipeline (token staging, attention-based importance scoring, cosine similarity redundancy detection, joint selection via hybrid scoring). The multi-framework integration (vLLM, SGLang, FlashInfer) makes it practically deployable.
- **Notes:** This is the most mature and well-supported codebase among all six papers. The plug-and-play design and framework integrations make it straightforward to use.

---

## 5. EVICPRESS (Microsoft, Dec 2025) -- "Joint KV-Cache Compression and Eviction"

**Code publicly available: NO**

- No GitHub repository was found. The arXiv page (2512.14946) has no code links. The Microsoft Research publication page does not link to code. Searches across GitHub and Microsoft's GitHub org turned up nothing.
- The paper describes ~3K lines of code extending **vLLM** and **LMCache** with multi-tier KV-cache placement, compression, and eviction control. This is a systems-level contribution that intercepts KV-cache lookups/retrieval/stores and integrates with vLLM's paged GPU memory management.
- **Complexity note:** Reproducing EVICPRESS without official code would be very challenging, as it requires deep integration with vLLM internals and LMCache, plus a profiling module for adaptive utility-function-based decisions across GPU/CPU/SSD tiers.

---

## 6. DMS (NeurIPS 2025) -- "Inference-Time Hyper-Scaling with KV Cache Compression"

**Code publicly available: YES (via multiple channels)**

- **Official model + inference code:** `https://huggingface.co/nvidia/Qwen3-8B-DMS-8x` -- NVIDIA released the DMS-adapted Qwen3-8B model with inference-time code bundled directly with the checkpoint. Requires `trust_remote_code=True` to load the DMS-specific logic.
- **NVIDIA kvpress integration:** `https://github.com/NVIDIA/kvpress` includes **DMSPress** as a wrapper press method.
- **Community Triton kernels:** `https://github.com/westers/kvcompress` -- a community implementation providing 5 custom Triton kernels for DMS prefill inference optimization (0 stars, Apache-2.0 license). Not an official NVIDIA repo.
- **Complexity:** DMS requires a short fine-tuning step (~1K training steps) to retrofit an existing model. The inference code is relatively straightforward (load model with `trust_remote_code=True`), but training new DMS-adapted models requires the full training pipeline, which is less clearly documented in the public releases.

---

## Summary Table

| Paper | Code Available? | Repo URL | Stars | Notes |
|-------|----------------|----------|-------|-------|
| **ThinKV** | Partial (via kvpress) | `github.com/NVIDIA/kvpress` (ThinKPress) | N/A | No standalone repo; kvpress has a simplified version |
| **SideQuest** | No | -- | -- | Paper only (Feb 2026), no code released |
| **HqeKV** | Yes | `github.com/skywclouds/HqeKV` | 2 | Full implementation with CUDA kernels |
| **R-KV** | Yes | `github.com/Zefan-Cai/R-KV` | 1.2k | Most mature; vLLM/SGLang/FlashInfer integrations |
| **EVICPRESS** | No | -- | -- | Systems paper; no code despite detailed description |
| **DMS** | Yes | HuggingFace + kvpress + community | N/A | Official model weights + inference code on HF; kvpress integration |

agentId: a7af9258743da8b04 (use SendMessage with to: 'a7af9258743da8b04' to continue this agent)
&lt;usage>total_tokens: 39718
tool_uses: 39
duration_ms: 251633&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e3bbb47-6c49-4110-a8f8-8857520a3a7f",
  "isSidechain": false,
  "promptId": "750c5be4-1e10-4956-bb2a-aaacbea26d97",
  "type": "user",
  "uuid": "356a9b01-33e2-4a63-82a7-295ac5949db9",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify which KV cache compression baselines have publicly available code as of May 2026. Search for the following and report what you find for EACH:\n\n1. **ThinKV** (ICLR 2026 Oral) - \"Thought-Adaptive KV Cache Compression\" - search GitHub for \"ThinKV\" and any repo associated with this paper\n2. **SideQuest** (Feb 2026) - \"Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning\" - search GitHub for \"SideQuest KV cache\"\n3. **HqeKV** (ACL ARR Jan 2026) - \"Hybrid Quantization and Eviction for KV Cache\" - search GitHub for \"HqeKV\"\n4. **R-KV** (NeurIPS 2025) - \"Redundancy-aware KV Cache Compression\" - verify the repo at github.com/Zefan-Cai/R-KV exists\n5. **EVICPRESS** (Microsoft, Dec 2025) - \"Joint KV-Cache Compression and Eviction\" - search for its code\n6. **DMS** (NeurIPS 2025) - \"Inference-Time Hyper-Scaling with KV Cache Compression\" - search for its code\n\nFor each, use WebSearch to find their GitHub repos. Then use WebFetch to verify if the repos actually exist and contain implementation code. Report: paper name, whether code exists, repo URL if found, and any notes about implementation complexity.\n\nBe thorough - check the paper's arXiv page for code links too.",
    "agentId": "a7af9258743da8b04",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a thorough picture. Let me compile the final report.\n\n---\n\nHere is the comprehensive report on public code availability for each of the six KV cache compression baselines, as of May 2026:\n\n---\n\n## 1. ThinKV (ICLR 2026 Oral) -- \"Thought-Adaptive KV Cache Compression\"\n\n**Code publicly available: NO (standalone repo not found)**\n\n- No dedicated GitHub repository was found for ThinKV. The lead author (Akshat Ramachandran, Georgia Tech / NVIDIA Research) does not have a ThinKV repo on GitHub. The arXiv page, OpenReview page, and the author's personal website contain no code links.\n- **However**, NVIDIA's `kvpress` library (`github.com/NVIDIA/kvpress`) does include a method called **ThinKPress**, which compresses key dimensions based on channel attention scores on the last queries. This appears to be a related but potentially simplified implementation within a broader framework -- it is distinct from the full ThinKV system described in the paper (which includes thought-type classification, hybrid quantization-eviction, and a custom PagedAttention kernel for memory slot reuse).\n- **Note:** The full paper describes custom CUDA kernels extending PagedAttention, which is a non-trivial implementation. The `kvpress` integration likely does not include the full thought-adaptive pipeline.\n\n**Partial code via:** `https://github.com/NVIDIA/kvpress` (ThinKPress method)\n\n---\n\n## 2. SideQuest (Feb 2026) -- \"Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning\"\n\n**Code publicly available: NO**\n\n- No GitHub repository was found. The arXiv page (2602.22603) has no code links. The first author, Sanjay Kariyappa (NVIDIA), has 10 repositories on GitHub -- none are related to SideQuest or KV cache. The paper is very recent (Feb 2026) and code has not been released.\n- The approach is architecturally distinctive: it trains a model (with only 215 samples) to reason about which tokens to evict, framing cache management as a parallel auxiliary task. Reproducing this without official code would require implementing the side-channel reasoning mechanism and the training procedure.\n\n---\n\n## 3. HqeKV (ACL ARR Jan 2026) -- \"Hybrid Quantization and Eviction for KV Cache\"\n\n**Code publicly available: YES**\n\n- **Repo:** `https://github.com/skywclouds/HqeKV`\n- **Status:** The repository exists and contains implementation code.\n- **Contents:** Python (67.3%) + CUDA (31.8%). Includes `model/`, `quant/` (with CUDA kernels), `config/`, `tests/`, `utils/` directories. Has inference scripts (`pred_long_bench_hq.py`), evaluation scripts (`eval_long_bench.py`), `requirements.txt`, and `pyproject.toml`.\n- **Features:** Configurable compression ratios, offline precision ratio optimization via Optuna, memory usage and throughput benchmarking.\n- **Community:** 2 stars, 0 forks -- very low adoption so far.\n- **Complexity:** Moderate-to-high. The CUDA kernels for quantization comprise ~32% of the codebase, and the Optuna-based optimizer adds configuration complexity.\n\n---\n\n## 4. R-KV (NeurIPS 2025) -- \"Redundancy-aware KV Cache Compression\"\n\n**Code publicly available: YES**\n\n- **Repo:** `https://github.com/Zefan-Cai/R-KV`\n- **Status:** The repository exists and is actively maintained.\n- **Contents:** Python (87%) + CUDA (7.8%) + C++ (2.9%). Includes core `/rkv` package, plus integrations with **HuggingFace**, **vLLM**, **SGLang**, and **FlashInfer** frameworks. Has `setup.py` for pip installation.\n- **Community:** 1.2k stars, 192 forks, 16 open issues -- strong adoption.\n- **Complexity:** Moderate-to-high. Implements a four-stage compression pipeline (token staging, attention-based importance scoring, cosine similarity redundancy detection, joint selection via hybrid scoring). The multi-framework integration (vLLM, SGLang, FlashInfer) makes it practically deployable.\n- **Notes:** This is the most mature and well-supported codebase among all six papers. The plug-and-play design and framework integrations make it straightforward to use.\n\n---\n\n## 5. EVICPRESS (Microsoft, Dec 2025) -- \"Joint KV-Cache Compression and Eviction\"\n\n**Code publicly available: NO**\n\n- No GitHub repository was found. The arXiv page (2512.14946) has no code links. The Microsoft Research publication page does not link to code. Searches across GitHub and Microsoft's GitHub org turned up nothing.\n- The paper describes ~3K lines of code extending **vLLM** and **LMCache** with multi-tier KV-cache placement, compression, and eviction control. This is a systems-level contribution that intercepts KV-cache lookups/retrieval/stores and integrates with vLLM's paged GPU memory management.\n- **Complexity note:** Reproducing EVICPRESS without official code would be very challenging, as it requires deep integration with vLLM internals and LMCache, plus a profiling module for adaptive utility-function-based decisions across GPU/CPU/SSD tiers.\n\n---\n\n## 6. DMS (NeurIPS 2025) -- \"Inference-Time Hyper-Scaling with KV Cache Compression\"\n\n**Code publicly available: YES (via multiple channels)**\n\n- **Official model + inference code:** `https://huggingface.co/nvidia/Qwen3-8B-DMS-8x` -- NVIDIA released the DMS-adapted Qwen3-8B model with inference-time code bundled directly with the checkpoint. Requires `trust_remote_code=True` to load the DMS-specific logic.\n- **NVIDIA kvpress integration:** `https://github.com/NVIDIA/kvpress` includes **DMSPress** as a wrapper press method.\n- **Community Triton kernels:** `https://github.com/westers/kvcompress` -- a community implementation providing 5 custom Triton kernels for DMS prefill inference optimization (0 stars, Apache-2.0 license). Not an official NVIDIA repo.\n- **Complexity:** DMS requires a short fine-tuning step (~1K training steps) to retrofit an existing model. The inference code is relatively straightforward (load model with `trust_remote_code=True`), but training new DMS-adapted models requires the full training pipeline, which is less clearly documented in the public releases.\n\n---\n\n## Summary Table\n\n| Paper | Code Available? | Repo URL | Stars | Notes |\n|-------|----------------|----------|-------|-------|\n| **ThinKV** | Partial (via kvpress) | `github.com/NVIDIA/kvpress` (ThinKPress) | N/A | No standalone repo; kvpress has a simplified version |\n| **SideQuest** | No | -- | -- | Paper only (Feb 2026), no code released |\n| **HqeKV** | Yes | `github.com/skywclouds/HqeKV` | 2 | Full implementation with CUDA kernels |\n| **R-KV** | Yes | `github.com/Zefan-Cai/R-KV` | 1.2k | Most mature; vLLM/SGLang/FlashInfer integrations |\n| **EVICPRESS** | No | -- | -- | Systems paper; no code despite detailed description |\n| **DMS** | Yes | HuggingFace + kvpress + community | N/A | Official model weights + inference code on HF; kvpress integration |"
      }
    ],
    "totalDurationMs": 251633,
    "totalTokens": 39718,
    "totalToolUseCount": 39,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 36496,
      "output_tokens": 1909,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1312
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1909,
          "cache_read_input_tokens": 36496,
          "cache_creation_input_tokens": 1312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1312,
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
      "otherToolCount": 39
    }
  },
  "sourceToolAssistantUUID": "1e3bbb47-6c49-4110-a8f8-8857520a3a7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-12T01:34:00.022Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014N4arxfDgexioykxXgJxZm`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify DeepSeek model name",
  "prompt": "I need to verify the correct name for DeepSeek's Qwen3-8B-based distillation model. The reviewer claims \"DeepSeek-R1-Distill-Qwen3-8B\" does not exist and the correct name is \"DeepSeek-R1-0528-Qwen3-8B\".\n\nPlease:\n1. Use WebSearch to search for \"DeepSeek-R1-0528-Qwen3-8B\" and \"DeepSeek-R1-Distill-Qwen3-8B\"\n2. Use WebFetch to check https://huggingface.co/deepseek-ai to see their model listings\n3. Search for \"DeepSeek R1 Qwen3 8B\" to find any variant\n4. Verify: what is the correct model ID on HuggingFace? Does it use GQA? What tokenizer does it use?\n\nReport the exact HuggingFace model ID, architecture details (attention type: MHA/GQA/MLA, number of KV heads), and tokenizer information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "356a9b01-33e2-4a63-82a7-295ac5949db9",
  "isSidechain": false,
  "requestId": "req_011CawpB5XqMCf6zEitcWzh2",
  "type": "assistant",
  "uuid": "6d3429f1-e7bc-4e40-9b65-439edfbfcb6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191ESP2oyHMSPXLfbsZUYTf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2862,
      "cache_read_input_tokens": 29084,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2862,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 356,
          "cache_read_input_tokens": 29084,
          "cache_creation_input_tokens": 2862,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2862
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

_source line 13 · 2026-05-12T01:35:10.503Z_

<details><summary>↩ Tool result · `toolu_014N4arxfDgexioykxXgJxZm`</summary>

```text
Here are my findings:

## Correct Model Name

The reviewer is correct. **"DeepSeek-R1-Distill-Qwen3-8B" does not exist.** The correct model ID is:

**`deepseek-ai/DeepSeek-R1-0528-Qwen3-8B`**

The naming convention difference is important:
- The older distillation series (based on Qwen2.5 and Llama3) used the `DeepSeek-R1-Distill-Qwen-{size}` pattern (e.g., `DeepSeek-R1-Distill-Qwen-7B`, `DeepSeek-R1-Distill-Qwen-32B`). Note these say "Qwen" (Qwen2.5), not "Qwen3".
- The newer Qwen3-based distillation uses a different naming pattern: `DeepSeek-R1-0528-Qwen3-8B`, incorporating the "0528" date stamp from the parent R1 model version rather than the word "Distill".
- No official DeepSeek model named `DeepSeek-R1-Distill-Qwen3-8B` exists on HuggingFace. Searching for it only returns the `DeepSeek-R1-0528-Qwen3-8B` model and the older Qwen2.5-based distill models.

## Architecture Details

From the `config.json`:

| Parameter | Value |
|---|---|
| **Exact HuggingFace ID** | `deepseek-ai/DeepSeek-R1-0528-Qwen3-8B` |
| **Architecture class** | `Qwen3ForCausalLM` |
| **model_type** | `qwen3` |
| **Attention type** | **GQA (Grouped-Query Attention)** |
| **num_attention_heads** (query heads) | 32 |
| **num_key_value_heads** | 8 |
| **head_dim** | 128 |
| **hidden_size** | 4096 |
| **num_hidden_layers** | 36 |
| **intermediate_size** | 12288 |
| **vocab_size** | 151,936 |
| **max_position_embeddings** | 131,072 (128K context via YaRN rope scaling with factor 4.0) |
| **Activation** | SiLU |
| **Precision** | bfloat16 |

The GQA ratio is 4:1 (32 query heads to 8 KV heads).

## Tokenizer Details

- **Tokenizer class**: `LlamaTokenizerFast` (SentencePiece-based)
- **Vocabulary size**: 151,936 tokens
- **Max length**: 131,072 tokens
- The tokenizer uses **DeepSeek-R1-0528's tokenizer configuration**, NOT the original Qwen3 tokenizer. Special tokens use DeepSeek-style formatting (e.g., `<|begin_of_sentence|>`, `<|User|>`, `<|Assistant|>`, tool call markers).
- The model card explicitly warns: "it is essential to ensure that all configuration files are sourced from our repository rather than the original Qwen3 project."

## Summary

The architecture is identical to Qwen3-8B (same layer count, dimensions, GQA configuration), but the tokenizer and chat template come from DeepSeek-R1-0528. It is NOT called "DeepSeek-R1-Distill-Qwen3-8B" -- the correct name is **DeepSeek-R1-0528-Qwen3-8B**.

Sources:
- [deepseek-ai/DeepSeek-R1-0528-Qwen3-8B (HuggingFace)](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B)
- [DeepSeek-R1 Collection](https://huggingface.co/collections/deepseek-ai/deepseek-r1)
- [deepseek-ai/DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B)
- [deepseek-ai/DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)
- [Artificial Analysis - DeepSeek R1 0528 Qwen3 8B](https://artificialanalysis.ai/models/deepseek-r1-qwen3-8b)

agentId: ac5125f34701c847e (use SendMessage with to: 'ac5125f34701c847e' to continue this agent)
&lt;usage>total_tokens: 20622
tool_uses: 10
duration_ms: 70476&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d3429f1-e7bc-4e40-9b65-439edfbfcb6c",
  "isSidechain": false,
  "promptId": "750c5be4-1e10-4956-bb2a-aaacbea26d97",
  "type": "user",
  "uuid": "e4f7a405-5946-49e9-be4b-7e1841e68a77",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify the correct name for DeepSeek's Qwen3-8B-based distillation model. The reviewer claims \"DeepSeek-R1-Distill-Qwen3-8B\" does not exist and the correct name is \"DeepSeek-R1-0528-Qwen3-8B\".\n\nPlease:\n1. Use WebSearch to search for \"DeepSeek-R1-0528-Qwen3-8B\" and \"DeepSeek-R1-Distill-Qwen3-8B\"\n2. Use WebFetch to check https://huggingface.co/deepseek-ai to see their model listings\n3. Search for \"DeepSeek R1 Qwen3 8B\" to find any variant\n4. Verify: what is the correct model ID on HuggingFace? Does it use GQA? What tokenizer does it use?\n\nReport the exact HuggingFace model ID, architecture details (attention type: MHA/GQA/MLA, number of KV heads), and tokenizer information.",
    "agentId": "ac5125f34701c847e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are my findings:\n\n## Correct Model Name\n\nThe reviewer is correct. **\"DeepSeek-R1-Distill-Qwen3-8B\" does not exist.** The correct model ID is:\n\n**`deepseek-ai/DeepSeek-R1-0528-Qwen3-8B`**\n\nThe naming convention difference is important:\n- The older distillation series (based on Qwen2.5 and Llama3) used the `DeepSeek-R1-Distill-Qwen-{size}` pattern (e.g., `DeepSeek-R1-Distill-Qwen-7B`, `DeepSeek-R1-Distill-Qwen-32B`). Note these say \"Qwen\" (Qwen2.5), not \"Qwen3\".\n- The newer Qwen3-based distillation uses a different naming pattern: `DeepSeek-R1-0528-Qwen3-8B`, incorporating the \"0528\" date stamp from the parent R1 model version rather than the word \"Distill\".\n- No official DeepSeek model named `DeepSeek-R1-Distill-Qwen3-8B` exists on HuggingFace. Searching for it only returns the `DeepSeek-R1-0528-Qwen3-8B` model and the older Qwen2.5-based distill models.\n\n## Architecture Details\n\nFrom the `config.json`:\n\n| Parameter | Value |\n|---|---|\n| **Exact HuggingFace ID** | `deepseek-ai/DeepSeek-R1-0528-Qwen3-8B` |\n| **Architecture class** | `Qwen3ForCausalLM` |\n| **model_type** | `qwen3` |\n| **Attention type** | **GQA (Grouped-Query Attention)** |\n| **num_attention_heads** (query heads) | 32 |\n| **num_key_value_heads** | 8 |\n| **head_dim** | 128 |\n| **hidden_size** | 4096 |\n| **num_hidden_layers** | 36 |\n| **intermediate_size** | 12288 |\n| **vocab_size** | 151,936 |\n| **max_position_embeddings** | 131,072 (128K context via YaRN rope scaling with factor 4.0) |\n| **Activation** | SiLU |\n| **Precision** | bfloat16 |\n\nThe GQA ratio is 4:1 (32 query heads to 8 KV heads).\n\n## Tokenizer Details\n\n- **Tokenizer class**: `LlamaTokenizerFast` (SentencePiece-based)\n- **Vocabulary size**: 151,936 tokens\n- **Max length**: 131,072 tokens\n- The tokenizer uses **DeepSeek-R1-0528's tokenizer configuration**, NOT the original Qwen3 tokenizer. Special tokens use DeepSeek-style formatting (e.g., `<|begin_of_sentence|>`, `<|User|>`, `<|Assistant|>`, tool call markers).\n- The model card explicitly warns: \"it is essential to ensure that all configuration files are sourced from our repository rather than the original Qwen3 project.\"\n\n## Summary\n\nThe architecture is identical to Qwen3-8B (same layer count, dimensions, GQA configuration), but the tokenizer and chat template come from DeepSeek-R1-0528. It is NOT called \"DeepSeek-R1-Distill-Qwen3-8B\" -- the correct name is **DeepSeek-R1-0528-Qwen3-8B**.\n\nSources:\n- [deepseek-ai/DeepSeek-R1-0528-Qwen3-8B (HuggingFace)](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B)\n- [DeepSeek-R1 Collection](https://huggingface.co/collections/deepseek-ai/deepseek-r1)\n- [deepseek-ai/DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B)\n- [deepseek-ai/DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)\n- [Artificial Analysis - DeepSeek R1 0528 Qwen3 8B](https://artificialanalysis.ai/models/deepseek-r1-qwen3-8b)"
      }
    ],
    "totalDurationMs": 70476,
    "totalTokens": 20622,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 17475,
      "output_tokens": 1211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1935
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1211,
          "cache_read_input_tokens": 17475,
          "cache_creation_input_tokens": 1935,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1935,
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
      "otherToolCount": 10
    }
  },
  "sourceToolAssistantUUID": "6d3429f1-e7bc-4e40-9b65-439edfbfcb6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Trajectory-Aware Joint Compression for Long-Horizon Agentic KV Caches\"…",
  "leafUuid": "e4f7a405-5946-49e9-be4b-7e1841e68a77",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 sprint: trajectory-aware KV compression for agentic LLMs",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284"
}
```

---

### Tool call

_source line 16 · 2026-05-12T01:35:21.343Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016qBVV2KYGBAJ2HprXAwfYY`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research EMNLP 2026 ARR deadline feasibility",
  "prompt": "I need to research the feasibility of submitting a short paper to EMNLP 2026 via ACL Rolling Review (ARR). The key question: can a KV cache compression paper be submitted as a 4-page short paper to ARR May 2026 cycle?\n\nPlease search for:\n1. \"ACL Rolling Review May 2026 deadline\" - exact submission date\n2. \"ARR short paper format\" or \"ACL short paper requirements\" - what's expected in a short paper\n3. \"EMNLP 2026 commitment deadline\" - when ARR-reviewed papers can be committed to EMNLP\n4. Whether there's a June 2026 ARR cycle if May is too tight\n5. \"ARR 2026 submission dates\" to see all upcoming cycles\n\nAlso search for: \"KV cache compression short paper\" or similar to see if there are precedents for short papers in this area.\n\nReport: exact ARR May 2026 deadline, short paper page limits and requirements, and whether a June ARR cycle exists that could still feed into EMNLP 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4f7a405-5946-49e9-be4b-7e1841e68a77",
  "isSidechain": false,
  "requestId": "req_011CawpH45vznH3q8oT2nGkH",
  "type": "assistant",
  "uuid": "97983fa8-819f-446b-b046-2e490e83bf32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XRXKWJodWV9rebh393W84y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1641,
      "cache_read_input_tokens": 31946,
      "output_tokens": 357,
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
          "output_tokens": 357,
          "cache_read_input_tokens": 31946,
          "cache_creation_input_tokens": 1641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1641
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

_source line 17 · 2026-05-12T01:37:01.205Z_

<details><summary>↩ Tool result · `toolu_016qBVV2KYGBAJ2HprXAwfYY`</summary>

```text
I now have all the information needed. Here is the full report.

---

## ARR May 2026 + EMNLP 2026 Feasibility Report: KV Cache Compression Short Paper

### 1. ARR May 2026 Deadline

- **Submission deadline: May 25, 2026** (11:59 PM AoE)
- That is **13 days from today** (May 12, 2026).
- Reviews due: June 29, 2026
- Author response window: July 7--13, 2026
- Meta-reviews released: July 30, 2026
- Cycle ends: August 2, 2026

**Critical note for EMNLP 2026:** At submission time for the May cycle, you must explicitly declare that you intend to commit to EMNLP 2026. This declaration is binding -- if you do not select EMNLP 2026 during submission, you will not be able to commit to EMNLP later.

### 2. Short Paper Format and Requirements

- **4 pages of content** (strict limit; desk rejection if exceeded)
- The following do NOT count toward the 4-page limit: Limitations section (required), Ethical Considerations section (optional), References (unlimited), Appendices (after references)
- **Camera-ready: 5 pages** (one extra page to address reviewer feedback), plus unlimited acknowledgments and references
- Must use the official ACL/ARR LaTeX or Overleaf template
- Full anonymization required (no author names, affiliations, or self-identifying links)
- Must include the Responsible NLP Checklist (incomplete/misleading checklist triggers desk rejection since Dec 2024)
- Short papers should be a "small, focused contribution that can be made in a few pages" -- not a condensed long paper. Common types: reproduction reports, negative results, opinion pieces, focused application nuggets.

### 3. EMNLP 2026 Commitment Deadline

- **Commitment deadline: August 2, 2026**
- Acceptance notification: August 20, 2026
- Camera-ready: September 20, 2026
- The May 2026 ARR cycle's meta-reviews are released July 30, giving you **3 days** to decide on commitment before the August 2 deadline.

### 4. Is There a June 2026 ARR Cycle?

**No.** There is no June 2026 cycle. ARR switched to 10-week cycles in mid-2025, resulting in roughly 5 cycles per year. The 2026 schedule is:

| Cycle | Submission Deadline | Cycle End |
|-------|-------------------|-----------|
| January 2026 | Jan 5, 2026 | March 15, 2026 |
| March 2026 | March 16, 2026 | May 24, 2026 |
| **May 2026** | **May 25, 2026** | **August 2, 2026** |
| August 2026 | August 3, 2026 | October 11, 2026 |

The **May 2026 cycle is the last ARR cycle that can feed into EMNLP 2026**. The August cycle ends October 11, well after the EMNLP commitment deadline of August 2. Earlier cycles (January, March) also work, but the paper must already have reviews/meta-review.

### 5. Precedents for KV Cache Compression Papers at ACL/EMNLP

KV cache compression is a **very active** area in *ACL venues. Recent examples:

- "A Simple and Effective L2 Norm-Based Strategy for KV Cache Compression" -- EMNLP 2024 Main (long paper, 24 pages)
- "EvolKV: Evolutionary KV Cache Compression" -- Findings of EMNLP 2025
- "DynamicKV: Task-Aware Adaptive KV Cache Compression" -- Findings of EMNLP 2025
- "MiniKV: Pushing the Limits of 2-Bit KV Cache" -- Findings of ACL 2025
- "XQuant: Ultra-Low Bit KV Cache Quantization" -- EMNLP 2025 Main
- "TailorKV: Hybrid Framework for Long-Context KV Cache Optimization" -- ACL 2025

I did not find a KV cache compression paper published specifically as a **short paper** (4 pages) -- all identified examples were long papers or Findings papers. However, this does not mean the format is inappropriate. A focused, well-scoped contribution (e.g., a single novel compression technique with clear empirical results on a standard benchmark) fits the short paper mold well. The ARR CFP explicitly mentions "interesting application nuggets" and focused contributions as appropriate for short papers.

### Bottom Line

- **You have 13 days** (until May 25, 2026 AoE) to submit to the May ARR cycle.
- **There is no June cycle.** May is the last on-ramp to EMNLP 2026.
- A 4-page short paper is a valid submission format. Keep it tightly scoped: one clear method, concise experiments, strong results.
- KV cache compression is well-represented at *ACL venues, so the topic fits. The novelty and focus of your specific contribution will determine reviewability in 4 pages.
- Remember to select "EMNLP 2026" as your target venue during submission -- this is binding.

Sources:
- [ARR Dates and Venues](https://aclrollingreview.org/dates)
- [ARR Call for Papers](https://aclrollingreview.org/cfp)
- [ARR Author Guidelines](https://aclrollingreview.org/authors)
- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 Twitter/X announcement](https://x.com/emnlpmeeting/status/2029508292637061462)
- [L2 Norm KV Cache Compression (EMNLP 2024)](https://aclanthology.org/2024.emnlp-main.1027/)
- [EvolKV (Findings EMNLP 2025)](https://aclanthology.org/2025.findings-emnlp.88/)
- [KV Cache Compression Benchmark (Findings EMNLP 2024)](https://aclanthology.org/2024.findings-emnlp.266/)
- [AI Conference Deadlines](https://mlciv.com/ai-deadlines/)

agentId: a5e0944cf8adf362b (use SendMessage with to: 'a5e0944cf8adf362b' to continue this agent)
&lt;usage>total_tokens: 21083
tool_uses: 13
duration_ms: 99857&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97983fa8-819f-446b-b046-2e490e83bf32",
  "isSidechain": false,
  "promptId": "750c5be4-1e10-4956-bb2a-aaacbea26d97",
  "type": "user",
  "uuid": "9b1a8b3a-3ac9-4ff2-acca-b20425e2f8cf",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research the feasibility of submitting a short paper to EMNLP 2026 via ACL Rolling Review (ARR). The key question: can a KV cache compression paper be submitted as a 4-page short paper to ARR May 2026 cycle?\n\nPlease search for:\n1. \"ACL Rolling Review May 2026 deadline\" - exact submission date\n2. \"ARR short paper format\" or \"ACL short paper requirements\" - what's expected in a short paper\n3. \"EMNLP 2026 commitment deadline\" - when ARR-reviewed papers can be committed to EMNLP\n4. Whether there's a June 2026 ARR cycle if May is too tight\n5. \"ARR 2026 submission dates\" to see all upcoming cycles\n\nAlso search for: \"KV cache compression short paper\" or similar to see if there are precedents for short papers in this area.\n\nReport: exact ARR May 2026 deadline, short paper page limits and requirements, and whether a June ARR cycle exists that could still feed into EMNLP 2026.",
    "agentId": "a5e0944cf8adf362b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information needed. Here is the full report.\n\n---\n\n## ARR May 2026 + EMNLP 2026 Feasibility Report: KV Cache Compression Short Paper\n\n### 1. ARR May 2026 Deadline\n\n- **Submission deadline: May 25, 2026** (11:59 PM AoE)\n- That is **13 days from today** (May 12, 2026).\n- Reviews due: June 29, 2026\n- Author response window: July 7--13, 2026\n- Meta-reviews released: July 30, 2026\n- Cycle ends: August 2, 2026\n\n**Critical note for EMNLP 2026:** At submission time for the May cycle, you must explicitly declare that you intend to commit to EMNLP 2026. This declaration is binding -- if you do not select EMNLP 2026 during submission, you will not be able to commit to EMNLP later.\n\n### 2. Short Paper Format and Requirements\n\n- **4 pages of content** (strict limit; desk rejection if exceeded)\n- The following do NOT count toward the 4-page limit: Limitations section (required), Ethical Considerations section (optional), References (unlimited), Appendices (after references)\n- **Camera-ready: 5 pages** (one extra page to address reviewer feedback), plus unlimited acknowledgments and references\n- Must use the official ACL/ARR LaTeX or Overleaf template\n- Full anonymization required (no author names, affiliations, or self-identifying links)\n- Must include the Responsible NLP Checklist (incomplete/misleading checklist triggers desk rejection since Dec 2024)\n- Short papers should be a \"small, focused contribution that can be made in a few pages\" -- not a condensed long paper. Common types: reproduction reports, negative results, opinion pieces, focused application nuggets.\n\n### 3. EMNLP 2026 Commitment Deadline\n\n- **Commitment deadline: August 2, 2026**\n- Acceptance notification: August 20, 2026\n- Camera-ready: September 20, 2026\n- The May 2026 ARR cycle's meta-reviews are released July 30, giving you **3 days** to decide on commitment before the August 2 deadline.\n\n### 4. Is There a June 2026 ARR Cycle?\n\n**No.** There is no June 2026 cycle. ARR switched to 10-week cycles in mid-2025, resulting in roughly 5 cycles per year. The 2026 schedule is:\n\n| Cycle | Submission Deadline | Cycle End |\n|-------|-------------------|-----------|\n| January 2026 | Jan 5, 2026 | March 15, 2026 |\n| March 2026 | March 16, 2026 | May 24, 2026 |\n| **May 2026** | **May 25, 2026** | **August 2, 2026** |\n| August 2026 | August 3, 2026 | October 11, 2026 |\n\nThe **May 2026 cycle is the last ARR cycle that can feed into EMNLP 2026**. The August cycle ends October 11, well after the EMNLP commitment deadline of August 2. Earlier cycles (January, March) also work, but the paper must already have reviews/meta-review.\n\n### 5. Precedents for KV Cache Compression Papers at ACL/EMNLP\n\nKV cache compression is a **very active** area in *ACL venues. Recent examples:\n\n- \"A Simple and Effective L2 Norm-Based Strategy for KV Cache Compression\" -- EMNLP 2024 Main (long paper, 24 pages)\n- \"EvolKV: Evolutionary KV Cache Compression\" -- Findings of EMNLP 2025\n- \"DynamicKV: Task-Aware Adaptive KV Cache Compression\" -- Findings of EMNLP 2025\n- \"MiniKV: Pushing the Limits of 2-Bit KV Cache\" -- Findings of ACL 2025\n- \"XQuant: Ultra-Low Bit KV Cache Quantization\" -- EMNLP 2025 Main\n- \"TailorKV: Hybrid Framework for Long-Context KV Cache Optimization\" -- ACL 2025\n\nI did not find a KV cache compression paper published specifically as a **short paper** (4 pages) -- all identified examples were long papers or Findings papers. However, this does not mean the format is inappropriate. A focused, well-scoped contribution (e.g., a single novel compression technique with clear empirical results on a standard benchmark) fits the short paper mold well. The ARR CFP explicitly mentions \"interesting application nuggets\" and focused contributions as appropriate for short papers.\n\n### Bottom Line\n\n- **You have 13 days** (until May 25, 2026 AoE) to submit to the May ARR cycle.\n- **There is no June cycle.** May is the last on-ramp to EMNLP 2026.\n- A 4-page short paper is a valid submission format. Keep it tightly scoped: one clear method, concise experiments, strong results.\n- KV cache compression is well-represented at *ACL venues, so the topic fits. The novelty and focus of your specific contribution will determine reviewability in 4 pages.\n- Remember to select \"EMNLP 2026\" as your target venue during submission -- this is binding.\n\nSources:\n- [ARR Dates and Venues](https://aclrollingreview.org/dates)\n- [ARR Call for Papers](https://aclrollingreview.org/cfp)\n- [ARR Author Guidelines](https://aclrollingreview.org/authors)\n- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)\n- [EMNLP 2026 Twitter/X announcement](https://x.com/emnlpmeeting/status/2029508292637061462)\n- [L2 Norm KV Cache Compression (EMNLP 2024)](https://aclanthology.org/2024.emnlp-main.1027/)\n- [EvolKV (Findings EMNLP 2025)](https://aclanthology.org/2025.findings-emnlp.88/)\n- [KV Cache Compression Benchmark (Findings EMNLP 2024)](https://aclanthology.org/2024.findings-emnlp.266/)\n- [AI Conference Deadlines](https://mlciv.com/ai-deadlines/)"
      }
    ],
    "totalDurationMs": 99857,
    "totalTokens": 21083,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1232,
      "cache_read_input_tokens": 18225,
      "output_tokens": 1625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1232
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1625,
          "cache_read_input_tokens": 18225,
          "cache_creation_input_tokens": 1232,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1232,
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
      "otherToolCount": 13
    }
  },
  "sourceToolAssistantUUID": "97983fa8-819f-446b-b046-2e490e83bf32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-12T01:38:43.876Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the research I need. Let me synthesize:

**Issue 1: Baseline reproduction risk**
- ThinKV: No standalone repo, but partial via NVIDIA kvpress (ThinKPress). Not a full implementation.
- SideQuest: No code at all.
- HqeKV: Yes, public code (github.com/skywclouds/HqeKV)
- R-KV: Yes, public code, very mature (1.2k stars, github.com/Zefan-Cai/R-KV)


- EVICPRESS: No code
- DMS: Yes, via HuggingFace + kvpress

The reviewer is right—I should stick with R-KV and HqeKV as my reproducible baselines, then add a simple uniform mixed-precision baseline as the third option. That gives me three fully reproducible comparisons without relying on partial implementations or methods that require additional fine-tuning.

For the compute budget, the reviewer's breakdown makes sense: reducing SWE-bench Lite to 50 instances, keeping 3 baselines, and tightening development time to 25 hours gets me to roughly 200 H100-hours. On the model side, DeepSeek-R1-0528-Qwen3-8B is confirmed with the same GQA structure I need.

The real decision point is the venue timing. With the May 25 ARR deadline just 13 days away, I'm looking at either a quick EMNLP 2026 short paper with 1 model and 2 baselines, or pushing for the full ICLR 2027 submission. Given that I've hit 8 rounds without score improvements, I think the best path forward is committing to both: a rapid EMNLP sprint to get something published while building toward the more comprehensive ICLR paper.

Now I'm re-examining the hard constraints the user laid out—200 H100-hours maximum and the May 25 EMNLP deadline are non-negotiable. The full 350-hour proposal won't work in 14 days, but a 4-page short paper with ~60 hours is actually doable. I'm sketching out a concrete plan: stick with Qwen3-8B as the model since it's simpler and better supported, include 2 baselines with public code, and keep everything within the time and compute budget.

The sprint breaks down into implementation work over the first week, experiments in the second week, then writing and polishing before submission. This approach sidesteps all the earlier complications—public baselines only, well under the compute limit, avoids the DeepSeek naming issue, and still hits the conference deadline.

I'm realizing the stagnation came from trying to do too much at once. By accepting the EMNLP 2026 constraint and building a realistic plan around it, I can actually move forward. The full evaluation can always expand for ICLR 2027 later, but right now I need to focus on what's achievable in this sprint window. The EMNLP sprint becomes the foundation for the ICLR extension, so I'm structuring the JSON to reflect this nested approach. I'm updating the model selection to start with Qwen3-8B for the short paper and layer in DeepSeek-R1 for the full version, adjusting baselines to use publicly available implementations initially and adding mixed-precision comparisons later, expanding the benchmark suite progressively, and anchoring everything to the ARR deadline of May 25 for EMNLP 2026 with ICLR 2027 as the natural follow-up.

Now I'm reconsidering the benchmark selection for a 4-page paper—τ-bench is essential for demonstrating trajectory-aware compression on agentic tasks, LongBench and MMLU provide quick validation that we haven't regressed on standard capabilities, and SWE-bench Lite could show coding performance if compute allows, though the 8B model might be limited there. I want fewer benchmarks but with clearer results. The core claim is that TrajComp reduces trajectory-level degradation in agentic workloads compared to per-step compression methods, so I need τ-bench as the primary benchmark, plus LongBench and MMLU to check for regressions—three focused benchmarks instead of spreading thin. For the EMNLP sprint, I'm targeting Qwen3-8B with R-KV and HqeKV baselines across these three benchmarks in about 60 H100-hours over 13 days. If there's time for an ICLR extension, I'd expand to two models, add three more baselines including uniform mixed-precision, and run six benchmarks including SWE-bench Lite and AIME, which would take around 200 H100-hours. Now I need to write out the JSON proposal carefully, addressing each concern while preserving what's working. For the timeline, I'm starting with implementing the core Lagrangian solver and phase detection...

The sprint breaks down into calibration work on Qwen3-8B using a subset of τ-bench, then full experimental runs across all three benchmarks, followed by writing and polishing. For compute, I'm estimating calibration at about an hour, τ-bench at roughly 16 hours across all tasks and methods, LongBench around 5 hours, MMLU around 2 hours, with another 15 hours for development and debugging, and 5 hours reserved for ablations if time permits.

Adding in wall-clock benchmarking and a buffer, the total comes to about 60 hours, which feels feasible. I'll frame the EMNLP sprint as the primary plan in my resource estimate.

For the paper itself, I'm narrowing the focus to one clear contribution: the trajectory-level Lagrangian objective for joint quantization and eviction in agentic KV caches, with agent-phase categorization as the enabling mechanism. That's tight enough for 4 pages. Given the reviewer's concern about venue, I'm committing to the EMNLP 2026 Findings sprint option rather than declaring it unachievable.

I'll adapt the reviewer's suggested sprint timeline but swap SWE-bench for τ-bench since 8B models perform poorly on SWE-bench and τ-bench better showcases the agentic contribution. Though I'm reconsidering whether to include at least some SWE-bench evaluation to demonstrate broader applicability.

Actually, τ-bench is genuinely agentic with its tool-use and multi-turn interactions, and 8B models will likely perform better on its structured tasks than on coding problems. So I'll stick with τ-bench as the primary evaluation and make SWE-bench optional if time allows—maybe 20 Lite instances, though that's risky given the time and success rate constraints.

For the final EMNLP sprint plan, I'm locking in τ-bench, LongBench, and MMLU with Qwen3-8B, comparing against R-KV and HqeKV baselines. This is a major shift from the original 350-hour, 9-benchmark, 2-model plan—I've fundamentally restructured the evaluation, changed which baselines to keep, and committed to a realistic timeline. The core TrajComp Lagrangian idea stays the same, but the scope and approach are substantially different.

Writing the JSON now...

Actually, I need to be careful about what fits in a 4-page short paper versus what gets deferred. The approach section should focus on the Lagrangian objective with γ-discounted cross-step error, the 4-category agent-phase token classification, and pattern matching for ReAct phase detection, with just a brief mention of GQA awareness and solver overhead numbers. Everything else—attention entropy fallback, detailed ablations, multiple trajectory variants—goes into the full paper.

Now I'm ready to write out the complete JSON with the right scope boundaries between the EMNLP sprint and ICLR extension. The key shift here is committing to the EMNLP sprint instead of saying it's infeasible—that's what breaks the cycle that's been holding back progress. By narrowing the scope to a focused short paper with a concrete timeline, I'm resolving the tension between the comprehensive vision and the actual time constraint.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b1a8b3a-3ac9-4ff2-acca-b20425e2f8cf",
  "isSidechain": false,
  "requestId": "req_011CawpRDPzniVkyycEoUqCc",
  "type": "assistant",
  "uuid": "3c3f3c54-e095-487d-998f-ed31b48a8377",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFRfoKU2p6ssYifqMb9QJs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2060,
      "cache_read_input_tokens": 33587,
      "output_tokens": 14721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14721,
          "cache_read_input_tokens": 33587,
          "cache_creation_input_tokens": 2060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2060
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

_source line 19 · 2026-05-12T01:42:50.191Z_

Now I have all the research I need. Let me synthesize the findings:

1. **Baseline code**: Confirmed — ThinKV has no standalone repo (only partial via NVIDIA kvpress), SideQuest has no code. R-KV (1.2k stars) and HqeKV have confirmed public code.
2. **Model name**: Confirmed — correct name is `DeepSeek-R1-0528-Qwen3-8B` (GQA, 32 query / 8 KV heads, DeepSeek tokenizer).
3. **EMNLP venue**: ARR May 25, 2026 deadline is 13 days away. No June cycle. May is the last on-ramp to EMNLP 2026. Short paper = 4 pages.

The core breakthrough for this revision: stop trying to force a comprehensive full paper into an impossible timeline. Commit to a focused 4-page EMNLP short paper sprint with only code-available baselines, 1 model, and 3 benchmarks (~60 H100-hours). This resolves all four issues simultaneously.

```json
{
  "title": "Trajectory-Aware Joint Compression for Long-Horizon Agentic KV Caches",
  "change_type": "major",
  "core_problem": "Agentic LLM systems (coding agents, research agents, tool-use agents) maintain KV caches that grow across dozens of reasoning-and-action steps, often exceeding 100K tokens. Current KV cache compression methods — including strong joint quantization-eviction approaches like ThinKV, HqeKV, and ARKV, as well as future-aware eviction methods like NGC and LookaheadKV — were designed for single-turn or single-model inference and optimize per-step reconstruction error or per-step eviction quality independently. In multi-step agentic workloads, compression errors compound across planning steps: PM-KVQ (ICLR 2026) demonstrates that directly quantizing KV cache at each decoding step causes cumulative quantization error that degrades long-CoT reasoning by up to 8% versus progressive strategies; 'Hold Onto That Thought' (under review, ICLR 2026) empirically shows that existing KV compression strategies designed for prefill-phase long-context tasks degrade significantly on reasoning tasks requiring extended decoding. Theoretical analysis from 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) proves lower bounds showing exponential error growth Ω((n/s)^(T-1)) for oblivious cache strategies across T reasoning stages in k-hop pointer chasing; we note that this bound applies specifically to single-model multi-step reasoning with locality-respecting cache controllers, not directly to agentic tool-use workflows with external observation injection — the analogy is suggestive but not a formal proof. The empirical evidence from PM-KVQ and 'Hold Onto That Thought' provides the primary, more directly applicable motivation. No existing work formulates joint quantization-eviction that explicitly minimizes cumulative trajectory-level error for agentic workloads.",
  "opportunity": "Two converging trends expose a clear research gap. First, agentic inference is now the dominant LLM deployment pattern (SWE-bench, GAIA, τ-bench), but KV cache compression research overwhelmingly targets single-turn inference. Existing agentic KV cache works address only parts of the problem: SideQuest (Feb 2026) uses model-driven eviction but not quantization; CodeComp (April 2026) leverages structural code priors for eviction only; CacheTTL (Nov 2025) manages cache scheduling without compression; PBKV (May 2026) predicts future agent invocations for cache management but performs no within-request compression; KVFlow (NeurIPS 2025) optimizes prefix caching for multi-agent workflows without compression; EpiCache (Apple, Sep 2025) manages episodic multi-turn cache but targets conversational QA, not agentic tool-use. NGC (April 2026) learns trajectory-aware KV eviction via RL within single-model reasoning chains, jointly optimizing reasoning and memory management from task reward alone — the closest conceptual competitor, but it requires RL training, is eviction-only (no quantization), and operates on single-model reasoning traces without explicit agent step boundaries or external observation injection. CapKV (April 2026) derives information-theoretic KV eviction via the Information Bottleneck principle with capacity-aware scoring — theoretically grounded but eviction-only and per-step.\n\nSecond, single-turn KV cache compression has matured across multiple fronts: (a) joint quantization-eviction via ThinKV (ICLR 2026 Oral, 20x compression), HqeKV (per-element compression actions), ARKV (tri-state assignment); (b) future-aware eviction via NGC (RL-based trajectory-aware eviction for single-model reasoning), LookaheadKV (ICLR 2026, predictive eviction via lookahead tokens + LoRA); (c) optimal bit allocation via RateQuant (rate-distortion reverse waterfilling, May 2026) and MixedDimKV (Lagrangian dual decomposition for per-token dimensions); (d) temporal and structural KV management via TTKV (temporal tiering with heterogeneous precision), TRIM-KV/Cache What Lasts (ICLR 2026, learned retention gates with temporal decay), and Transactional Attention (structural anchor protection for value-bearing tokens); (e) information-theoretic eviction via CapKV (Information Bottleneck with statistical leverage scores). However, none model how compression decisions at step t propagate errors to steps t+1 through T in multi-step agentic workflows with external tool observations. The key insight: in agentic workloads, token importance is cross-step structured in ways that single-turn methods cannot exploit. Instruction and plan tokens maintain importance across all steps; current-step observations are critical but rapidly decay; historical tool outputs become redundant as new observations arrive. This temporal structure, combined with the empirically-grounded error compounding problem (PM-KVQ, 'Hold Onto That Thought'), demands a fundamentally different optimization objective: minimizing trajectory-level degradation rather than per-step reconstruction error.",
  "landscape": "**Joint quantization-eviction (single-turn):** ThinKV (ICLR 2026 Oral) applies thought-adaptive hybrid quantization-eviction achieving 20x compression with <5% KV cache — the strongest single-turn baseline, but no public code as of May 2026 (partial proxy available via NVIDIA's kvpress library as 'ThinKPress'). HqeKV (ACL ARR Jan 2026) provides an integrated optimizer selecting optimal compression actions (quantization level or eviction) per cached element under memory constraints; **public code confirmed** (github.com/skywclouds/HqeKV). ARKV (arXiv Feb 2026) dynamically assigns tokens to Original/Quantization/Eviction states based on per-layer attention statistics. KVTC (ICLR 2026) achieves 20x via PCA + adaptive quantization + entropy coding.\n\n**Constrained optimization for KV compression:** MixedDimKV (March 2026) formulates KV cache compression as a constrained optimization problem using Lagrangian dual decomposition with bisection search over λ, allocating per-token dimensions under a memory budget. This uses the same Lagrangian optimization technique as TrajComp. The critical difference: MixedDimKV minimizes per-step reconstruction error (single-step objective), while TrajComp minimizes trajectory-level error accumulation across T agent steps (multi-step objective). The trajectory extension is non-trivial because: (i) the search space expands from per-step to cross-step — compressing token i at step t affects attention distributions at steps t+1...T; (ii) the objective changes from reconstruction fidelity to trajectory success rate; (iii) the importance model must account for temporal structure (persistent vs. decaying tokens) absent in single-turn settings. RateQuant (May 2026) applies rate-distortion theory with reverse waterfilling for optimal per-head bit allocation — a complementary per-step optimization that TrajComp could incorporate as a sub-routine for within-step bit allocation.\n\n**Trajectory-aware and future-aware eviction:** NGC (April 2026, arXiv:2604.18002) learns trajectory-aware KV eviction via RL, treating both reasoning tokens and cache-eviction decisions as discrete actions sampled from the language model, trained end-to-end from outcome-based task reward alone. On Countdown, AMC, and AIME, NGC achieves 2-3x peak KV cache compression while maintaining strong accuracy. TrajComp differs from NGC in three key ways: (1) training-free (Lagrangian optimization vs. RL training required), (2) joint quantization-eviction (vs. eviction-only), and (3) designed for multi-step agentic workflows with explicit step boundaries and external observation injection (vs. single-model reasoning traces where the model interleaves thinking and eviction). LookaheadKV (ICLR 2026, Samsung) predicts future attention patterns via trainable lookahead tokens + LoRA, achieving <0.7% drop at 81% compression — also eviction-only and single-turn.\n\n**Information-theoretic eviction:** CapKV (April 2026, arXiv:2604.25975) derives capacity-aware KV eviction via the Information Bottleneck principle, using a log-determinant approximation with statistical leverage scores under a linear-Gaussian surrogate of attention. It provides a theoretically grounded mechanism that replaces heuristic selection with capacity-maximization. TrajComp differs: joint quantization-eviction with a trajectory-level multi-step objective vs. CapKV's per-step information-theoretic eviction-only framework.\n\n**Temporal and structural KV management:** TTKV (March 2026) partitions KV cache into temporal tiers with heterogeneous precision across HBM/DRAM, achieving 76% latency reduction on 128K contexts. Its temporal tiering directly overlaps with TrajComp's 'decaying context' category — but TTKV is a system-level memory hierarchy approach without trajectory-aware error optimization. TRIM-KV/Cache What Lasts (ICLR 2026) learns per-token retention gates with temporal decay via distillation — conceptually similar to cross-step importance decay, but training-required, eviction-only, and single-turn. Transactional Attention (April 2026) protects structural anchor tokens (credentials, API keys) from eviction via semantic sponsorship — overlaps with TrajComp's 'persistent anchors' category, but is domain-specific to credential/configuration retention and does not perform compression.\n\n**Agentic KV cache management:** SideQuest (Feb 2026) uses the reasoning model itself to identify dispensable tokens, achieving 65% peak token reduction on agentic tasks — eviction only, no quantization, no public code. CodeComp (April 2026) uses Code Property Graph priors for structure-aware eviction in agentic coding — domain-specific and eviction only. CacheTTL/Continuum (Nov 2025) manages multi-turn cache scheduling with TTL-based retention. PBKV (May 2026) predicts future agent invocations and manages cache across workflow steps — system-level scheduling without within-request compression. KVFlow (NeurIPS 2025) optimizes prefix caching for multi-agent workflows. EpiCache (Apple, Sep 2025) manages episodic multi-turn cache for conversational QA. Agent Memory Below the Prompt (Feb 2026) persists Q4 KV caches across agents on edge devices. KVComm (Oct 2025) enables cross-context KV sharing.\n\n**Other relevant methods:** TriAttention (MIT/NVIDIA, April 2026) achieves 10.7x via trigonometric key importance scoring. R-KV (NeurIPS 2025) achieves 100% accuracy at 10% KV via redundancy-aware eviction with **public code** (github.com/Zefan-Cai/R-KV, 1.2k stars, vLLM/SGLang/FlashInfer integrations). DMS (NeurIPS 2025) achieves 8x with lightweight training. EVICPRESS (Microsoft, Dec 2025) jointly optimizes compression and eviction across storage tiers but has no public code. PM-KVQ shows progressive mixed-precision reduces cumulative quantization error in long-CoT. TurboQuant (ICLR 2026) addresses inner-product estimation bias compounding across attention computations. 'Not All Bits Are Equal' (ICLR 2026) shows optimal compression strategy is scale-dependent.\n\n**Error compounding theory and evidence:** 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) proves that under k-hop pointer chasing with cache size s, oblivious caches suffer exponential error growth Ω((n/s)^(T-1)). We note this bound applies specifically to k-hop pointer chasing with locality-respecting cache controllers in single-model multi-step reasoning; its extension to agentic tool-use with external observation injection is an analogy, not a formal proof. The empirical evidence from PM-KVQ (cumulative quantization error degrades long-CoT by up to 8%) and 'Hold Onto That Thought' (compression designed for prefill degrades extended-decoding reasoning) provides the primary and more directly applicable motivation for trajectory-aware compression.\n\n**Code availability summary for baseline selection:** Of the methods considered as baselines, only R-KV (github.com/Zefan-Cai/R-KV, 1.2k stars) and HqeKV (github.com/skywclouds/HqeKV) have confirmed public implementations. ThinKV has a partial proxy (ThinKPress in NVIDIA kvpress) but no full implementation. SideQuest, EVICPRESS, and ForesightKV have no public code. This directly constrains baseline selection to methods with verified reproducibility.\n\nNo prior work formulates a trajectory-level objective for joint quantization-eviction in agentic KV caches with explicit cross-step error accumulation control. The closest works are NGC (trajectory-aware but RL-required, eviction-only, single-model) and MixedDimKV (same Lagrangian technique but per-step objective). TrajComp uniquely combines: (1) joint quant-eviction, (2) trajectory-level multi-step objective, (3) training-free Lagrangian optimization, (4) agentic workflow structure exploitation.",
  "approach": "We propose TrajComp (Trajectory-Aware Joint Compression), which formulates a single dual-constrained Lagrangian objective jointly optimizing token retention probabilities and per-token bit allocation under memory and cumulative trajectory-error budgets. We commit to a two-phase evaluation strategy: a focused EMNLP 2026 short paper sprint (ARR May 25 deadline, 13 days), followed by an extended ICLR 2027 full paper.\n\n**(1) Cross-step error propagation model:** Unlike ThinKV/HqeKV/MixedDimKV which minimize per-step reconstruction error independently, and unlike NGC which learns trajectory-aware eviction through RL training, TrajComp models error propagation across agent steps in a training-free manner. Compressing token i at step t contributes weighted error proportional to Σ_{s=t+1}^{T} γ^{s-t} × importance_i, where γ is the empirically-calibrated step-wise error propagation rate. The dual-constrained Lagrangian L = Σ_t error_t(s,q) + λ_mem(M(s,q) - B_mem) + λ_err(E_cumul(s,q,γ) - B_err) enables smooth Pareto-optimal tradeoffs via dual gradient descent on both multipliers. Note: MixedDimKV uses Lagrangian dual decomposition with bisection for a single memory constraint and per-step objective; TrajComp extends this to dual constraints (memory + trajectory error) with a cross-step objective, requiring the error propagation model as additional machinery.\n\n**γ calibration procedure:** For Qwen3-8B (EMNLP sprint), run N=5 agent trajectories on a τ-bench subset with full (uncompressed) KV cache and with uniformly 4-bit quantized KV cache. At each agent step boundary t, measure KL divergence D_KL(P_full^t || P_compressed^t) of the attention distributions. Compute per-step propagation ratios r_t = D_KL^{t+1} / D_KL^t across all steps and trajectories. Set γ = median(r_t). Based on PM-KVQ's observations of progressive error accumulation, we expect γ ∈ [0.7, 0.95]. Calibration cost: ~2 H100-hours for the EMNLP sprint. For the ICLR extension, expand to N=10 trajectories per model-benchmark pair with sensitivity analysis (~10 H100-hours total for 2 models × 2 agentic benchmarks).\n\n**(2) Agent-phase token categorization:** Rather than ThinKV's within-turn thought types, TrajComp defines categories by agentic workflow structure: (a) Persistent anchors — system prompts, instructions, plans — never compressed (analogous to Transactional Attention's structural anchors, but generalized beyond credentials to all instruction-bearing tokens); (b) Active context — current tool output and recent reasoning — retained at 4-bit; (c) Decaying context — older observations — progressively compressed (4-bit → 2-bit → evict) with schedule determined by the Lagrangian solver based on temporal distance and cross-step importance (analogous to TTKV's temporal tiering, but driven by trajectory-level optimization rather than fixed temporal heuristics); (d) Ephemeral tokens — intermediate tool formatting, API boilerplate — immediately evicted.\n\n**Phase detection strategy:** For structured agent frameworks (ReAct, function-calling with explicit Thought/Action/Observation tags), use lightweight pattern matching on special tokens and turn boundaries (zero overhead). This covers both evaluation settings: τ-bench uses structured tool-calling, and SWE-agent uses ReAct prompting with explicit delimiters. For the EMNLP sprint, pattern matching suffices for all evaluated benchmarks. For the ICLR extension with free-form reasoning models, fall back to attention entropy thresholds: compute per-token attention entropy at step boundaries; tokens with consistently high entropy across recent steps are classified as ephemeral, tokens with low entropy as active/persistent.\n\n**(3) GQA-aware compression:** Qwen3-8B uses Grouped Query Attention (32 query heads, 8 KV heads). TrajComp allocates compression budgets at the KV-head group level, accounting for the fact that compressing a single KV head affects all 4 query heads in its group. For the ICLR extension, DeepSeek-R1-0528-Qwen3-8B uses the same GQA configuration (32 query heads, 8 KV heads, Qwen3 architecture) but with DeepSeek-R1-0528's tokenizer — we verify tokenizer compatibility for phase detection. MLA adaptation (for full DeepSeek-V3/R1 671B models) is left as future work.\n\nThe dual gradient descent operates at agent step boundaries (not every token), making it lightweight. A single re-optimization pass over the full KV cache occurs when a new agent step begins.\n\n**Wall-clock and throughput reporting:** We report: (a) Lagrangian solver time per agent step as a function of KV cache size — expected to be <10ms for dual gradient descent over ~100K tokens, dominated by importance score computation not the optimization itself; (b) end-to-end latency per agent step (including compression overhead) vs. baselines on H100-80GB; (c) tokens/second throughput at matched compression ratios.\n\n---\n\n**EMNLP 2026 SHORT PAPER SPRINT (Primary — ARR May 25, 2026)**\n\n13-day sprint for a 4-page short paper targeting EMNLP 2026 Findings:\n\n**Sprint timeline:**\n- Day 1-3 (May 12-14): Implement Lagrangian solver + phase detection on HuggingFace Transformers. Integrate R-KV (from public repo, pip-installable) and HqeKV (from public repo) as baselines.\n- Day 4-5 (May 15-16): γ calibration on Qwen3-8B with 5 τ-bench trajectories. Validate solver convergence.\n- Day 6-8 (May 17-19): Run experiments — τ-bench full (164 tasks × 3 methods: TrajComp, R-KV, HqeKV), LongBench, MMLU. Collect wall-clock numbers.\n- Day 9-11 (May 20-22): Write 4-page paper. Focus on: (1) trajectory-level Lagrangian formulation, (2) agent-phase categorization, (3) τ-bench results showing trajectory success rate at matched compression ratios.\n- Day 12-13 (May 23-24): Polish, add any ablations completed, finalize submission.\n- Day 14 (May 25): Submit to ARR with EMNLP 2026 venue declaration.\n\n**Sprint evaluation scope:**\n- Model: Qwen3-8B (single model — avoids DeepSeek tokenizer compatibility debugging under time pressure)\n- Baselines: R-KV (public code, github.com/Zefan-Cai/R-KV, 1.2k stars, pip-installable), HqeKV (public code, github.com/skywclouds/HqeKV) — both with confirmed public implementations\n- Benchmarks: τ-bench 164 tasks via official harness (primary agentic benchmark — 8B models achieve meaningful success rates on structured customer-service tasks), LongBench (long-context regression), MMLU (general capability regression)\n- Key metric: trajectory-level success rate at matched compression ratio on τ-bench; standard accuracy on LongBench/MMLU\n- Compression targets: 4x, 8x, 16x (3 operating points)\n\n**Sprint compute budget (~60 H100-hours):**\n- γ calibration: 5 trajectories × 2 configs × ~5 min ≈ 1h\n- τ-bench: 164 tasks × 3 methods × 3 compression ratios × ~2 min ≈ 49h\n- LongBench: ~3h\n- MMLU: ~1h\n- Wall-clock benchmarking: ~1h\n- Development/debugging: ~5h\n- Total: ~60 H100-hours\n\n**Sprint risk mitigation:**\n- R-KV's mature codebase (1.2k stars, vLLM integration) minimizes baseline setup time\n- τ-bench has an official evaluation harness — no custom scaffolding needed\n- Pattern-matching phase detection on τ-bench's structured tool-calling is trivially implementable\n- If HqeKV integration proves difficult (CUDA kernel compilation), fall back to HqeKV's non-CUDA mode or replace with attention-score-based uniform mixed-precision (4-bit/2-bit partitioning, implementable in <4h)\n\n---\n\n**ICLR 2027 FULL PAPER EXTENSION (Secondary — expected deadline ~September 2026)**\n\nExpands the EMNLP sprint results into a full 8-page paper:\n\n- Add model: DeepSeek-R1-0528-Qwen3-8B (same GQA architecture, DeepSeek-R1-0528 tokenizer — verify phase detection compatibility)\n- Add baseline: Uniform mixed-precision (attention-score-based 4-bit/2-bit partitioning, implementable in <8h — serves as ablation baseline showing the value of trajectory-aware optimization over naive mixed-precision)\n- Add benchmarks: SWE-bench Lite 50 instances via SWE-agent (ReAct, 30 turns, 16K tokens/turn), AIME 2025, MATH-500, HumanEval, MT-Bench, WikiText/C4 perplexity\n- Add ablations: phase detection accuracy, γ sensitivity, anchor ratio impact, component-wise ablation\n- Add attention entropy fallback for phase detection (for future free-form reasoning evaluation)\n- If ThinKV releases official code before experiments begin, add as 4th baseline\n\n**ICLR extension compute (~140 additional H100-hours, ~200h total including sprint):**\n- SWE-bench Lite: 50 instances × 2 models × 4 methods × ~10 min ≈ 67h\n- τ-bench extension: 164 tasks × 1 additional model × 4 methods × ~2 min ≈ 22h\n- Additional benchmarks (AIME, MATH-500, HumanEval, MT-Bench, perplexity): ~20h\n- Extended γ calibration: ~8h\n- Ablations: ~15h\n- Dev/debug buffer: ~10h\n- Total extension: ~142h → ~200h cumulative\n\n**8B model capability consideration:** We acknowledge that 8B models achieve relatively low base success rates on SWE-bench (~17%). For the EMNLP sprint, we avoid SWE-bench entirely, using τ-bench as the primary agentic benchmark where 8B models achieve higher success rates on structured tasks. For the ICLR extension, we supplement binary SWE-bench success with trajectory-quality metrics (steps completed before failure, tool-call coherence, attention distribution divergence from full-cache trajectories).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~60h H100-80GB (EMNLP sprint); ~200h total (including ICLR extension)",
      "gpu_utilization": "50-60% effective — τ-bench instances run quickly (~2 min each); gaps filled with MMLU/LongBench evaluation",
      "timeline": "13 days for EMNLP sprint; 4 months total for ICLR extension",
      "team": "1 researcher with systems ML background",
      "estimated_gpu_cost": "$150 (60h × ~$2.50/h EMNLP sprint); $500 total with ICLR extension"
    },
    "human_in_loop": {
      "gpu_hours": "~60h H100-80GB (EMNLP sprint); ~200h total",
      "gpu_utilization": "60-70% — agent handles R-KV/HqeKV integration from public repos, τ-bench harness setup, γ calibration runs; human guides Lagrangian formulation and paper writing",
      "timeline": "13 days for EMNLP sprint (human: ~2h/day for formulation + writing); 3 months for ICLR extension",
      "team": "1 researcher, ~2h/day during sprint, ~45min/day during extension",
      "claude_api_cost": "$80-120 for sprint (~800-1200 turns); $300-500 total with extension",
      "estimated_gpu_cost": "$150 sprint; $500 total",
      "risk_note": "Primary sprint risk: HqeKV CUDA kernel compilation may require debugging. Mitigation: fall back to HqeKV non-CUDA mode or replace with uniform mixed-precision baseline (~4h to implement). R-KV is pip-installable and battle-tested (1.2k stars). τ-bench has an official harness with minimal setup."
    },
    "auto_research": {
      "gpu_hours": "~80h H100-80GB (automated sprint with wider γ sweep); ~250h total with ICLR extension",
      "gpu_utilization": "55-65% — τ-bench instances create pipeline gaps; agent queues MMLU/LongBench during gaps",
      "timeline": "10-12 days for sprint; 4-6 weeks for ICLR extension with 2 concurrent H100s",
      "team": "0 (initial 2-hour setup: model download, R-KV pip install, τ-bench harness verification)",
      "claude_api_cost": "$150-250 for sprint; $500-800 total with extension",
      "estimated_gpu_cost": "$200 sprint; $625 total",
      "speed_bottleneck": "τ-bench: 164 tasks × 9 runs (3 methods × 3 compression ratios) × ~2 min ≈ 49h — the dominant sprint cost. Parallelizable across GPUs.",
      "risk_note": "Agent may struggle with Lagrangian formulation implementation without human guidance. Recommend human review of solver code before experiment runs (Day 3-4 checkpoint)."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR May 25, 2026 — 13 days from today; 4-page short paper; ~60 H100-hours; commit to EMNLP venue at submission; reviews by June 29, commitment deadline August 2)",
    "ICLR 2027 (expected abstract deadline ~September 19, 2026; 8-page full paper extending EMNLP results with 2nd model, additional baselines, SWE-bench, and ablations; ~200 H100-hours total)"
  ],
  "level": "solid",
  "key_references": [
    "ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models (ICLR 2026 Oral) — no public code; partial proxy via NVIDIA kvpress (ThinKPress)",
    "HqeKV: Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference (ACL ARR Jan 2026) — **public code: github.com/skywclouds/HqeKV** — EMNLP sprint baseline",
    "ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget (arXiv Feb 2026)",
    "NGC: Neural Garbage Collection: Learning to Forget while Learning to Reason (arXiv April 2026, arXiv:2604.18002) — RL-based trajectory-aware KV eviction for single-model reasoning, eviction-only, 2-3x compression on Countdown/AMC/AIME",
    "CapKV: Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective (arXiv April 2026, arXiv:2604.25975) — Information Bottleneck principle with statistical leverage scores, eviction-only, per-step",
    "LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation (ICLR 2026 Poster, Samsung, arXiv:2603.10899) — predictive eviction via lookahead tokens + LoRA",
    "TTKV: Temporal-Tiered KV Cache for Long-Context LLM Inference (arXiv March 2026, arXiv:2604.19769) — temporal tiering with heterogeneous precision across HBM/DRAM",
    "TRIM-KV / Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs (ICLR 2026, arXiv:2512.03324) — learned per-token retention gates with temporal decay",
    "RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory (arXiv May 2026, arXiv:2605.06675) — reverse waterfilling for per-head bit allocation",
    "Transactional Attention: Semantic Sponsorship for KV-Cache Retention (arXiv April 2026, arXiv:2604.11288) — structural anchor protection for value-bearing tokens",
    "Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression [MixedDimKV] (arXiv March 2026, arXiv:2603.20616) — Lagrangian dual decomposition for per-token dimension allocation",
    "PBKV: Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management (arXiv May 2026, arXiv:2605.06472) — prediction-based agent cache scheduling",
    "KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows (NeurIPS 2025, arXiv:2507.07400) — workflow-aware prefix caching",
    "EpiCache: Episodic KV Cache Management for Long Conversational Question Answering (Apple, arXiv Sep 2025, arXiv:2509.17396) — episodic multi-turn cache management",
    "SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning (arXiv Feb 2026) — no public code",
    "CodeComp: Structural KV Cache Compression for Agentic Coding (arXiv April 2026)",
    "CacheTTL/Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live (arXiv Nov 2025)",
    "R-KV: Redundancy-aware KV Cache Compression for Reasoning Models (NeurIPS 2025) — **public code: github.com/Zefan-Cai/R-KV, 1.2k stars, vLLM/SGLang/FlashInfer integrations** — EMNLP sprint baseline",
    "How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers (arXiv April 2026, arXiv:2604.17935) — theoretical bounds on cache compression vs. reasoning depth (k-hop pointer chasing; analogy to agentic setting, not direct proof)",
    "PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs (arXiv May 2025, OpenReview Oct 2025) — empirical evidence of cumulative quantization error in long-CoT",
    "Hold Onto That Thought: Assessing KV Cache Compression On Reasoning (arXiv Dec 2025, arXiv:2512.12008) — empirical assessment of compression degradation on reasoning tasks",
    "TriAttention: Efficient Long Reasoning with Trigonometric KV Compression (MIT/NVIDIA, arXiv April 2026)",
    "KV Cache Transform Coding [KVTC] for Compact Storage in LLM Inference (NVIDIA, ICLR 2026)",
    "Inference-Time Hyper-Scaling with KV Cache Compression [DMS] (NeurIPS 2025) — public code via HuggingFace + NVIDIA kvpress",
    "EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving (Microsoft, arXiv Dec 2025) — no public code",
    "Not All Bits Are Equal: How Model Scale Changes Memory-Optimal Reasoning (ICLR 2026)",
    "TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate (ICLR 2026) — inner-product bias compounding",
    "ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution (arXiv Feb 2026, arXiv:2602.03203) — RL-based future-aware eviction, no public code",
    "Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices (arXiv Feb 2026, arXiv:2603.04428)",
    "KVComm: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems (arXiv Oct 2025)",
    "Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys (AAAI 2026)"
  ],
  "description": "We propose TrajComp (Trajectory-Aware Joint Compression), a training-free method that jointly optimizes token eviction and per-token bit allocation for KV caches in long-horizon agentic LLM workloads through a dual-constrained Lagrangian objective that explicitly minimizes trajectory-level error accumulation. The empirical motivation comes from PM-KVQ (ICLR 2026), which demonstrates that cumulative quantization error degrades long-CoT reasoning by up to 8% versus progressive strategies, and from 'Hold Onto That Thought' (2025), which shows that compression strategies designed for prefill degrade on extended-decoding reasoning. Theoretical analysis from 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) proves exponential error growth Ω((n/s)^(T-1)) for oblivious cache strategies in k-hop pointer chasing; we note this bound applies to single-model reasoning with locality-respecting cache controllers — its extension to agentic tool-use with external observation injection is a suggestive analogy, not a formal proof.\n\nThe landscape includes strong single-turn methods across multiple fronts: joint quant-eviction (ThinKV at 20x — no public code, HqeKV — public code, ARKV), future-aware and trajectory-aware eviction (NGC via RL-based eviction for single-model reasoning achieving 2-3x compression, LookaheadKV via predictive attention), information-theoretic eviction (CapKV via Information Bottleneck with statistical leverage scores), optimal bit allocation (RateQuant via rate-distortion, MixedDimKV via Lagrangian dual), and temporal/structural management (TTKV temporal tiering, TRIM-KV learned retention, Transactional Attention anchor protection). Agentic-specific works (SideQuest, CodeComp, PBKV, KVFlow, EpiCache) address scheduling and eviction but not joint compression. No prior work combines joint quant-eviction with a trajectory-level multi-step objective for agentic workloads.\n\nTrajComp fills this gap with two core contributions: (1) A cross-step error propagation model that weights compression decisions by their γ-discounted impact across all future agent steps, formalized as a dual-constrained Lagrangian with separate memory and trajectory-error budget multipliers. γ is calibrated empirically via KL divergence propagation measurement. (2) Agent-phase token categorization (persistent anchors, active context, decaying context, ephemeral tokens) that exploits cross-step importance structure unique to agentic workflows, with pattern-matching detection for structured agent frameworks (ReAct, function-calling). Both contributions are training-free.\n\nWe commit to a dual-track evaluation strategy designed to meet both the EMNLP 2026 deadline and resource constraints:\n\n**EMNLP 2026 short paper (primary, ARR May 25):** 4-page paper, 13-day sprint, ~60 H100-hours. 1 model (Qwen3-8B, GQA), 2 baselines with confirmed public code (R-KV at github.com/Zefan-Cai/R-KV with 1.2k stars and pip-installable vLLM integration; HqeKV at github.com/skywclouds/HqeKV), 3 benchmarks (τ-bench 164 tasks via official harness as primary agentic benchmark, LongBench, MMLU). Sprint: Day 1-3 implement solver + integrate baselines from public repos, Day 4-5 γ calibration, Day 6-8 run experiments, Day 9-11 write paper, Day 12-13 polish, Day 14 submit. Reports trajectory-level success rate at 4x/8x/16x compression on τ-bench plus standard accuracy on LongBench/MMLU.\n\n**ICLR 2027 full paper (extension, ~September 2026):** Expands to 2 models (add DeepSeek-R1-0528-Qwen3-8B — same Qwen3 GQA architecture, DeepSeek-R1-0528 tokenizer), 3 baselines (add uniform mixed-precision; add ThinKV if code releases), 9 benchmarks (add SWE-bench Lite 50 instances via SWE-agent, AIME 2025, MATH-500, HumanEval, MT-Bench, WikiText/C4 perplexity), full ablations, and attention entropy fallback for phase detection. ~200 H100-hours total including sprint work.",
  "project_name": "trajcomp_agentic_kvcache",
  "source": "web_research"
}
```

**Summary of changes (major revision):**

1. **Baseline plan fixed**: Dropped ThinKV and SideQuest (no public code). EMNLP sprint uses only R-KV (1.2k stars, pip-installable) and HqeKV (confirmed public code). ICLR extension adds uniform mixed-precision as a third baseline.

2. **Compute fit within 200h**: EMNLP sprint requires only ~60 H100-hours. ICLR extension totals ~200h including sprint work. Both well within the 200h hard constraint.

3. **Model name fixed**: Changed to `DeepSeek-R1-0528-Qwen3-8B` throughout. Noted it uses DeepSeek-R1-0528's tokenizer (not Qwen3 default). Deferred to ICLR extension to avoid tokenizer debugging under sprint pressure.

4. **Venue resolved**: Committed to EMNLP 2026 ARR May 25 with a concrete 13-day sprint plan for a 4-page short paper. ICLR 2027 serves as the extension target for the full paper. This is the key change that breaks the stagnation — previous rounds kept designing a full paper that couldn't fit the deadline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c3f3c54-e095-487d-998f-ed31b48a8377",
  "isSidechain": false,
  "requestId": "req_011CawpRDPzniVkyycEoUqCc",
  "type": "assistant",
  "uuid": "0c527310-912f-4a51-a089-5837e5be9e18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFRfoKU2p6ssYifqMb9QJs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2060,
      "cache_read_input_tokens": 33587,
      "output_tokens": 14721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14721,
          "cache_read_input_tokens": 33587,
          "cache_creation_input_tokens": 2060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2060
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Trajectory-Aware Joint Compression for Long-Horizon Agentic KV Caches\"…",
  "leafUuid": "0c527310-912f-4a51-a089-5837e5be9e18",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 sprint: trajectory-aware KV compression for agentic LLMs",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Trajectory-Aware Joint Compression for Long-Horizon Agentic KV Caches\"…",
  "leafUuid": "0c527310-912f-4a51-a089-5837e5be9e18",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 sprint: trajectory-aware KV compression for agentic LLMs",
  "sessionId": "bc7e3bfc-1b8a-4420-a244-c7c2364ab284"
}
```

---
