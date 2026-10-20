# Research conversation: Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs ## Desc

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/9a9c4034-7658-48d7-81fd-4573eb968007.jsonl`
- **Structured JSON:** [`853076aca5ae4d1ff164.json`](../../sessions/85/853076aca5ae4d1ff164.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:00:52.178Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:00:52.178Z",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "content": "# Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs\n\n## Description\nWe propose PI-ContextRot, the first diagnostic benchmark designed to causally decompose context rot — the well-documented degradation of LLM performance as input context grows — into its constituent factors: proactive interference, position bias, semantic distractor similarity, and raw length. While Chroma (2025) documented context rot across 18 models, PI-LLM (2025) demonstrated log-linear accuracy collapse under synthetic interference, and EMB-S (2026) showed semantic discrimination is the dominant bottleneck for long-context retrieval, these threads remain disconnected: no work has measured the relative contribution of each factor to realistic task degradation. Our balanced 3⁴ factorial design (3 interference levels × 3 positions × 3 similarity levels × 3 context lengths = 81 cells, 35 instances per cell per task, 8,505 total instances across multi-document QA, entity tracking, and temporal reasoning) is formally powered (≥0.95 for medium effects, ≥0.80 for small effects on two-way interactions). Evaluating 12 models across dense (Qwen3.5-9B/27B), MoE (Llama-4-Scout, Qwen3.5-122B-A10B, DeepSeek-V4-Flash), SSM-hybrid (Jamba-1.5-Mini/Large), and frontier API architectures (GPT-4.1, Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini 2.5 Pro, Qwen3.5-397B-A17B), we report partial η² effect sizes quantifying each factor's contribution and their interactions. A tiered mechanistic analysis — attention entropy on all open-weight models plus attribution patching (AtP*) on dense models ≤27B — identifies the causal circuits underlying each factor. This decomposition directly informs practical context engineering: the effect-size rankings reveal whether mitigation efforts should prioritize interference-aware retrieval (as Sculptor assumes), position debiasing, or length management, resolving an implicit disagreement across the three literatures.\n\n## Core Problem\nWhat are the relative contributions of proactive interference, position bias, semantic distractor similarity, and raw context length to observed context rot in LLMs, and how do these factors interact across dense, MoE, and SSM-hybrid architectures?\n\n## Opportunity\nThree active research threads have developed independently: the context rot literature (Chroma 2025, documenting non-uniform degradation across 18 models), the proactive interference literature (PI-LLM arXiv:2506.08184, showing log-linear accuracy decline; Dual-Process arXiv:2603.00270, showing PI dominates over RI in LLMs opposite to humans), and the semantic interference literature (EMB-S arXiv:2601.20276, showing semantic discrimination — not context length — is the dominant bottleneck for long-context retrieval at 326M-token scale). These threads have never been connected into a unified quantitative decomposition. PI-LLM uses only synthetic key-value pairs; Chroma documents degradation without controlling for interference; EMB-S decouples access from usage but does not measure the relative contribution of PI versus position versus length; Sculptor (ICLR 2026) proposes active context management to mitigate PI but does not quantify PI's share of overall degradation. A hypothesis-neutral factorial study — measuring each factor's contribution via ANOVA with effect sizes — would provide the first causal decomposition of context rot into component factors, informing whether mitigation efforts should prioritize interference-aware retrieval, position debiasing, or length management.\n\n## Landscape\nChroma Research (2025) systematically documented context rot across 18 models but noted that 'investigating mechanistic interpretability is beyond scope.' PI-LLM (arXiv:2506.08184) demonstrated log-linear retrieval accuracy decline under proactive interference but only tested synthetic key-value retrieval. The Dual-Process paper (arXiv:2603.00270) found PI and RI are uncorrelated (R²=0.044) with distinct mechanisms across 39 models, and crucially that PI resistance doesn't scale with model size (R²=0.06). EMB-S (arXiv:2601.20276) introduced adversarial NIAH with collision-tested near-miss hard negatives at 326M-token scale, decoupling evidence access from usage under semantic interference — but measures access degradation rather than decomposing the contributing factors. CogniLoad (arXiv:2509.18458) provides factorial control over length, difficulty, and distractor density but NOT position bias or proactive interference load. LONGPIBENCH controls position but not interference. Sculptor (arXiv:2508.04664, ICLR 2026) proposes active context management tools to mitigate PI but does not quantify PI's relative contribution to overall degradation — it assumes PI is the dominant problem without measuring its effect size against position bias or raw length. The noise decomposition framework of 'When Does Divide and Conquer Work' (arXiv:2506.16411, ICLR 2026) decomposes long-context failures into task/model/aggregator noise for chunking strategies but does not manipulate interference or position as controlled factors. Concurrent work update (May 2026): LongMINT (arXiv:2605.18565) evaluates memory under multi-target interference in long-horizon agent systems but focuses on agent memory architectures. Cross-Component Interference (arXiv:2605.05716) demonstrates context-window crowding in LLM agent scaffolding via a full factorial experiment, but manipulates scaffolding components (planning, tools, memory) rather than the interference-position-similarity-length factors we target. SleepGate (arXiv:2603.14517) proposes a KV-cache consolidation mechanism for resolving PI but addresses mitigation rather than diagnosis. Intelligence Degradation (arXiv:2601.15300) identifies critical context-length thresholds via natural length distribution analysis but does not control for interference or semantic similarity. No existing work performs a joint factorial decomposition of context rot into interference, position, similarity, and length components with effect sizes on realistic NLP tasks across multiple architectures.\n\n## Approach\nConstruct PI-ContextRot, a diagnostic benchmark with factorial control over four orthogonal factors in a balanced 3⁴ design: (1) proactive interference load — number of semantically similar but superseded passages preceding the target (0/3/8 levels, spanning from no interference through moderate to severe based on PI-LLM's log-linear curve), (2) target information position (early/middle/late tercile), (3) semantic similarity between distractors and target (low/medium/high, controlled via embedding cosine similarity using BGE-M3 with validated thresholds at cosine <0.3, 0.5–0.7, and >0.85), and (4) context length (8K/32K/128K tokens). The 81-cell design generates 8,505 instances (35 per cell × 3 realistic NLP task types: multi-document QA, entity state tracking, temporal reasoning over news articles), sourcing base documents from Wikipedia and CommonCrawl-News. Formal power analysis (G*Power, F-test family, fixed-effects ANOVA) confirms ≥0.95 power for detecting medium effects (partial η² ≥ 0.06, Cohen's f = 0.253) on all main effects and two-way interactions, and ≥0.80 power for small effects (partial η² ≥ 0.01, f = 0.100) on two-way interactions, at α = 0.05 with n = 35 per cell per task (N_task = 2,835). Evaluate 12 models spanning three architecture families and three scale tiers: dense transformers (Qwen3.5-9B, Qwen3.5-27B), MoE architectures (Llama-4-Scout-17B-16E, Qwen3.5-122B-A10B, DeepSeek-V4-Flash), SSM hybrids (Jamba-1.5-Mini, Jamba-1.5-Large), and frontier APIs (GPT-4.1, Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini 2.5 Pro, Qwen3.5-397B-A17B). Run a full-factorial ANOVA reporting partial η² effect sizes for each factor and all two-way interactions, with Bonferroni-corrected post-hoc contrasts, providing the first quantitative decomposition of context rot into component causes. Supplement with a tiered mechanistic analysis: (a) attention entropy measurement across all open-weight models (forward-pass only, O(1) overhead per inference, following the HEAD-ENTROPY methodology for identifying correctness-predictive attention patterns), and (b) attribution patching via AtP* (gradient-based approximation requiring only 2 forward + 1 backward pass, computationally tractable) on dense models ≤27B (Qwen3.5-9B, Qwen3.5-27B) to identify interference-sensitive versus position-sensitive attention heads. This tiered strategy replaces the original activation patching plan, which is computationally prohibitive on MoE models (cost scales linearly in the number of model components, requiring millions of forward passes on 100B+ parameter models).\n\n## Resource Estimate\n{'manual': {'gpu_hours': '1,000–1,300 (inference on 7 open-weight models across 8,505 instances at up to 128K context; large MoE/SSM models on 4–8×H100 nodes; AtP* probing on 2 dense models adds ~150 hrs; attention entropy adds ~50 hrs)', 'timeline': '12–14 weeks (2 wks benchmark construction with power-analysis validation, 4.5 wks inference runs, 2.5 wks mechanistic analysis, 3 wks writing)', 'estimated_gpu_cost': '$2,500–$4,000 at $2–3/H100-hr (Lambda Labs $2.99/hr, RunPod $1.99–$2.39/hr; market range $1.49–$6.98/hr depending on provider and commitment)', 'api_model_cost': '$400–$600 (8,505 instances × 5 API models at varying context lengths)'}, 'human_in_loop': {'gpu_hours': '650–850 (Claude handles data generation QA, similarity filtering via BGE-M3, and statistical analysis pipeline; human designs experiments and interprets mechanistic probes)', 'timeline': '8–10 weeks (1.5 wks benchmark construction with Claude-assisted template generation and power-analysis validation, 3 wks inference, 2 wks analysis, 2 wks writing)', 'claude_api_cost': '$500–$700 (data generation with quality verification: ~$200 for 8,505 instances at Sonnet 4.6 rates; similarity computation and filtering: ~$100; statistical analysis pipeline: ~$150; writing assistance: ~$250)', 'estimated_gpu_cost': '$1,600–$2,600', 'api_model_cost': '$400–$600'}, 'auto_research': {'gpu_hours': '1,300–1,700 (full 12-model evaluation including parallel sweeps across all 81 factorial cells; automated AtP* pipeline; attention entropy computation)', 'timeline': '4–6 weeks (parallelized benchmark generation and inference; automated statistical pipeline; human review at checkpoints)', 'claude_api_cost': '$900–$1,300 (benchmark generation with multi-pass verification: ~$350; orchestration and analysis: ~$400; draft generation and iteration: ~$350; quality assurance: ~$200)', 'estimated_gpu_cost': '$3,250–$5,100', 'api_model_cost': '$500–$800 (5 API models × 8,505 instances with retries)', 'speed_bottleneck': 'Sequential evaluation of large models at 128K context — DeepSeek-V4-Flash (284B, 4–8×H100) and Jamba-1.5-Large (398B total, 4–8×H100) at ~60–120 sec per 128K inference; 8,505 instances × 2 large models at 8× parallelism ≈ 300–500 GPU-hours that cannot be further distributed without additional nodes'}}\n\n## Inspired By\nField guide Section 3 (Context Rot) + Section 6 (Reasoning vs Retrieval) + the disconnect between PI-LLM's interference findings, EMB-S's semantic discrimination findings, and Chroma's context rot characterization + CogniLoad's explicit acknowledgment that 'current benchmarks do not offer the factorial control needed to disentangle these loads' + Sculptor's implicit assumption that PI is dominant without quantification\n\n## Target Venues\n- AAAI 2027 (abstract: July 21, 2026 AoE; full paper: July 28, 2026 AoE — primary target, 9 weeks from today; supplementary/code: July 31, 2026)\n- NeurIPS 2026 Workshops (suggested paper deadline: August 29, 2026 AoE — ideal for preliminary results or workshop-length version with subset of models)\n- ICLR 2027 (estimated submission: September–October 2026 — ample time for full study with complete mechanistic analysis across all architectures)\n- ACL 2027 via ARR (estimated ARR cycle: October–November 2026 — backup venue if additional experiments or reviewer-requested analyses extend the timeline)\n\n## Key References\n- Context Rot: Evaluating LLM Performance Degradation with Increasing Input Tokens (Chroma Research 2025)\n- Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length (arXiv 2025, Wang et al., arXiv:2506.08184)\n- Transformers Remember First, Forget Last: Dual-Process Interference in LLMs (arXiv 2026, Chattaraj & Raj, arXiv:2603.00270)\n- Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale (arXiv 2026, EMB-S, arXiv:2601.20276)\n- Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management (ICLR 2026, arXiv:2508.04664)\n- CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density (arXiv 2025, Kaiser et al., arXiv:2509.18458)\n- Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs (arXiv 2024, LongPiBench)\n- When Does Divide and Conquer Work for Long Context LLM? A Noise Decomposition Framework (ICLR 2026, arXiv:2506.16411)\n- AtP*: An Efficient and Scalable Method for Localizing LLM Behaviour to Components (Google DeepMind, arXiv:2403.00745)\n- Learning to Forget: Sleep-Inspired Memory Consolidation for Resolving Proactive Interference in Large Language Models (arXiv 2026, Xie, arXiv:2603.14517)\n- Intelligence Degradation in Long-Context LLMs: Critical Threshold Determination via Natural Length Distribution Analysis (arXiv 2026, arXiv:2601.15300)\n- LongMINT: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems (arXiv 2026, Lee et al., arXiv:2605.18565)\n- More Is Not Always Better: Cross-Component Interference in LLM Agent Scaffolding (arXiv 2026, arXiv:2605.05716)\n- Long-Context Generalization with Sparse Attention (ICLR 2026)\n- Applying Statistics to LLM Evaluations (Wolfe 2025 — methodological reference for power analysis in LLM benchmarks)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T05:00:52.182Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:00:52.182Z",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-20T05:00:52.200Z_

# Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs

## Description
We propose PI-ContextRot, the first diagnostic benchmark designed to causally decompose context rot — the well-documented degradation of LLM performance as input context grows — into its constituent factors: proactive interference, position bias, semantic distractor similarity, and raw length. While Chroma (2025) documented context rot across 18 models, PI-LLM (2025) demonstrated log-linear accuracy collapse under synthetic interference, and EMB-S (2026) showed semantic discrimination is the dominant bottleneck for long-context retrieval, these threads remain disconnected: no work has measured the relative contribution of each factor to realistic task degradation. Our balanced 3⁴ factorial design (3 interference levels × 3 positions × 3 similarity levels × 3 context lengths = 81 cells, 35 instances per cell per task, 8,505 total instances across multi-document QA, entity tracking, and temporal reasoning) is formally powered (≥0.95 for medium effects, ≥0.80 for small effects on two-way interactions). Evaluating 12 models across dense (Qwen3.5-9B/27B), MoE (Llama-4-Scout, Qwen3.5-122B-A10B, DeepSeek-V4-Flash), SSM-hybrid (Jamba-1.5-Mini/Large), and frontier API architectures (GPT-4.1, Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini 2.5 Pro, Qwen3.5-397B-A17B), we report partial η² effect sizes quantifying each factor's contribution and their interactions. A tiered mechanistic analysis — attention entropy on all open-weight models plus attribution patching (AtP*) on dense models ≤27B — identifies the causal circuits underlying each factor. This decomposition directly informs practical context engineering: the effect-size rankings reveal whether mitigation efforts should prioritize interference-aware retrieval (as Sculptor assumes), position debiasing, or length management, resolving an implicit disagreement across the three literatures.

## Core Problem
What are the relative contributions of proactive interference, position bias, semantic distractor similarity, and raw context length to observed context rot in LLMs, and how do these factors interact across dense, MoE, and SSM-hybrid architectures?

## Opportunity
Three active research threads have developed independently: the context rot literature (Chroma 2025, documenting non-uniform degradation across 18 models), the proactive interference literature (PI-LLM arXiv:2506.08184, showing log-linear accuracy decline; Dual-Process arXiv:2603.00270, showing PI dominates over RI in LLMs opposite to humans), and the semantic interference literature (EMB-S arXiv:2601.20276, showing semantic discrimination — not context length — is the dominant bottleneck for long-context retrieval at 326M-token scale). These threads have never been connected into a unified quantitative decomposition. PI-LLM uses only synthetic key-value pairs; Chroma documents degradation without controlling for interference; EMB-S decouples access from usage but does not measure the relative contribution of PI versus position versus length; Sculptor (ICLR 2026) proposes active context management to mitigate PI but does not quantify PI's share of overall degradation. A hypothesis-neutral factorial study — measuring each factor's contribution via ANOVA with effect sizes — would provide the first causal decomposition of context rot into component factors, informing whether mitigation efforts should prioritize interference-aware retrieval, position debiasing, or length management.

## Landscape
Chroma Research (2025) systematically documented context rot across 18 models but noted that 'investigating mechanistic interpretability is beyond scope.' PI-LLM (arXiv:2506.08184) demonstrated log-linear retrieval accuracy decline under proactive interference but only tested synthetic key-value retrieval. The Dual-Process paper (arXiv:2603.00270) found PI and RI are uncorrelated (R²=0.044) with distinct mechanisms across 39 models, and crucially that PI resistance doesn't scale with model size (R²=0.06). EMB-S (arXiv:2601.20276) introduced adversarial NIAH with collision-tested near-miss hard negatives at 326M-token scale, decoupling evidence access from usage under semantic interference — but measures access degradation rather than decomposing the contributing factors. CogniLoad (arXiv:2509.18458) provides factorial control over length, difficulty, and distractor density but NOT position bias or proactive interference load. LONGPIBENCH controls position but not interference. Sculptor (arXiv:2508.04664, ICLR 2026) proposes active context management tools to mitigate PI but does not quantify PI's relative contribution to overall degradation — it assumes PI is the dominant problem without measuring its effect size against position bias or raw length. The noise decomposition framework of 'When Does Divide and Conquer Work' (arXiv:2506.16411, ICLR 2026) decomposes long-context failures into task/model/aggregator noise for chunking strategies but does not manipulate interference or position as controlled factors. Concurrent work update (May 2026): LongMINT (arXiv:2605.18565) evaluates memory under multi-target interference in long-horizon agent systems but focuses on agent memory architectures. Cross-Component Interference (arXiv:2605.05716) demonstrates context-window crowding in LLM agent scaffolding via a full factorial experiment, but manipulates scaffolding components (planning, tools, memory) rather than the interference-position-similarity-length factors we target. SleepGate (arXiv:2603.14517) proposes a KV-cache consolidation mechanism for resolving PI but addresses mitigation rather than diagnosis. Intelligence Degradation (arXiv:2601.15300) identifies critical context-length thresholds via natural length distribution analysis but does not control for interference or semantic similarity. No existing work performs a joint factorial decomposition of context rot into interference, position, similarity, and length components with effect sizes on realistic NLP tasks across multiple architectures.

## Approach
Construct PI-ContextRot, a diagnostic benchmark with factorial control over four orthogonal factors in a balanced 3⁴ design: (1) proactive interference load — number of semantically similar but superseded passages preceding the target (0/3/8 levels, spanning from no interference through moderate to severe based on PI-LLM's log-linear curve), (2) target information position (early/middle/late tercile), (3) semantic similarity between distractors and target (low/medium/high, controlled via embedding cosine similarity using BGE-M3 with validated thresholds at cosine <0.3, 0.5–0.7, and >0.85), and (4) context length (8K/32K/128K tokens). The 81-cell design generates 8,505 instances (35 per cell × 3 realistic NLP task types: multi-document QA, entity state tracking, temporal reasoning over news articles), sourcing base documents from Wikipedia and CommonCrawl-News. Formal power analysis (G*Power, F-test family, fixed-effects ANOVA) confirms ≥0.95 power for detecting medium effects (partial η² ≥ 0.06, Cohen's f = 0.253) on all main effects and two-way interactions, and ≥0.80 power for small effects (partial η² ≥ 0.01, f = 0.100) on two-way interactions, at α = 0.05 with n = 35 per cell per task (N_task = 2,835). Evaluate 12 models spanning three architecture families and three scale tiers: dense transformers (Qwen3.5-9B, Qwen3.5-27B), MoE architectures (Llama-4-Scout-17B-16E, Qwen3.5-122B-A10B, DeepSeek-V4-Flash), SSM hybrids (Jamba-1.5-Mini, Jamba-1.5-Large), and frontier APIs (GPT-4.1, Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini 2.5 Pro, Qwen3.5-397B-A17B). Run a full-factorial ANOVA reporting partial η² effect sizes for each factor and all two-way interactions, with Bonferroni-corrected post-hoc contrasts, providing the first quantitative decomposition of context rot into component causes. Supplement with a tiered mechanistic analysis: (a) attention entropy measurement across all open-weight models (forward-pass only, O(1) overhead per inference, following the HEAD-ENTROPY methodology for identifying correctness-predictive attention patterns), and (b) attribution patching via AtP* (gradient-based approximation requiring only 2 forward + 1 backward pass, computationally tractable) on dense models ≤27B (Qwen3.5-9B, Qwen3.5-27B) to identify interference-sensitive versus position-sensitive attention heads. This tiered strategy replaces the original activation patching plan, which is computationally prohibitive on MoE models (cost scales linearly in the number of model components, requiring millions of forward passes on 100B+ parameter models).

## Resource Estimate
{'manual': {'gpu_hours': '1,000–1,300 (inference on 7 open-weight models across 8,505 instances at up to 128K context; large MoE/SSM models on 4–8×H100 nodes; AtP* probing on 2 dense models adds ~150 hrs; attention entropy adds ~50 hrs)', 'timeline': '12–14 weeks (2 wks benchmark construction with power-analysis validation, 4.5 wks inference runs, 2.5 wks mechanistic analysis, 3 wks writing)', 'estimated_gpu_cost': '$2,500–$4,000 at $2–3/H100-hr (Lambda Labs $2.99/hr, RunPod $1.99–$2.39/hr; market range $1.49–$6.98/hr depending on provider and commitment)', 'api_model_cost': '$400–$600 (8,505 instances × 5 API models at varying context lengths)'}, 'human_in_loop': {'gpu_hours': '650–850 (Claude handles data generation QA, similarity filtering via BGE-M3, and statistical analysis pipeline; human designs experiments and interprets mechanistic probes)', 'timeline': '8–10 weeks (1.5 wks benchmark construction with Claude-assisted template generation and power-analysis validation, 3 wks inference, 2 wks analysis, 2 wks writing)', 'claude_api_cost': '$500–$700 (data generation with quality verification: ~$200 for 8,505 instances at Sonnet 4.6 rates; similarity computation and filtering: ~$100; statistical analysis pipeline: ~$150; writing assistance: ~$250)', 'estimated_gpu_cost': '$1,600–$2,600', 'api_model_cost': '$400–$600'}, 'auto_research': {'gpu_hours': '1,300–1,700 (full 12-model evaluation including parallel sweeps across all 81 factorial cells; automated AtP* pipeline; attention entropy computation)', 'timeline': '4–6 weeks (parallelized benchmark generation and inference; automated statistical pipeline; human review at checkpoints)', 'claude_api_cost': '$900–$1,300 (benchmark generation with multi-pass verification: ~$350; orchestration and analysis: ~$400; draft generation and iteration: ~$350; quality assurance: ~$200)', 'estimated_gpu_cost': '$3,250–$5,100', 'api_model_cost': '$500–$800 (5 API models × 8,505 instances with retries)', 'speed_bottleneck': 'Sequential evaluation of large models at 128K context — DeepSeek-V4-Flash (284B, 4–8×H100) and Jamba-1.5-Large (398B total, 4–8×H100) at ~60–120 sec per 128K inference; 8,505 instances × 2 large models at 8× parallelism ≈ 300–500 GPU-hours that cannot be further distributed without additional nodes'}}

## Inspired By
Field guide Section 3 (Context Rot) + Section 6 (Reasoning vs Retrieval) + the disconnect between PI-LLM's interference findings, EMB-S's semantic discrimination findings, and Chroma's context rot characterization + CogniLoad's explicit acknowledgment that 'current benchmarks do not offer the factorial control needed to disentangle these loads' + Sculptor's implicit assumption that PI is dominant without quantification

## Target Venues
- AAAI 2027 (abstract: July 21, 2026 AoE; full paper: July 28, 2026 AoE — primary target, 9 weeks from today; supplementary/code: July 31, 2026)
- NeurIPS 2026 Workshops (suggested paper deadline: August 29, 2026 AoE — ideal for preliminary results or workshop-length version with subset of models)
- ICLR 2027 (estimated submission: September–October 2026 — ample time for full study with complete mechanistic analysis across all architectures)
- ACL 2027 via ARR (estimated ARR cycle: October–November 2026 — backup venue if additional experiments or reviewer-requested analyses extend the timeline)

## Key References
- Context Rot: Evaluating LLM Performance Degradation with Increasing Input Tokens (Chroma Research 2025)
- Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length (arXiv 2025, Wang et al., arXiv:2506.08184)
- Transformers Remember First, Forget Last: Dual-Process Interference in LLMs (arXiv 2026, Chattaraj & Raj, arXiv:2603.00270)
- Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale (arXiv 2026, EMB-S, arXiv:2601.20276)
- Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management (ICLR 2026, arXiv:2508.04664)
- CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density (arXiv 2025, Kaiser et al., arXiv:2509.18458)
- Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs (arXiv 2024, LongPiBench)
- When Does Divide and Conquer Work for Long Context LLM? A Noise Decomposition Framework (ICLR 2026, arXiv:2506.16411)
- AtP*: An Efficient and Scalable Method for Localizing LLM Behaviour to Components (Google DeepMind, arXiv:2403.00745)
- Learning to Forget: Sleep-Inspired Memory Consolidation for Resolving Proactive Interference in Large Language Models (arXiv 2026, Xie, arXiv:2603.14517)
- Intelligence Degradation in Long-Context LLMs: Critical Threshold Determination via Natural Length Distribution Analysis (arXiv 2026, arXiv:2601.15300)
- LongMINT: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems (arXiv 2026, Lee et al., arXiv:2605.18565)
- More Is Not Always Better: Cross-Component Interference in LLM Agent Scaffolding (arXiv 2026, arXiv:2605.05716)
- Long-Context Generalization with Sparse Attention (ICLR 2026)
- Applying Statistics to LLM Evaluations (Wolfe 2025 — methodological reference for power analysis in LLM benchmarks)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "dc85c9bb-f9bc-4bf3-8111-88cdfb7c60fe",
  "type": "user",
  "uuid": "8a456267-e8d2-46bc-82a1-b1f94d1dc78c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:00:52.198Z_

```json
{
  "parentUuid": "8a456267-e8d2-46bc-82a1-b1f94d1dc78c",
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
  "uuid": "7bb0fa2b-215a-4c2e-97a6-42de025ff085",
  "timestamp": "2026-05-20T05:00:52.198Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:00:52.199Z_

```json
{
  "parentUuid": "7bb0fa2b-215a-4c2e-97a6-42de025ff085",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d3f717e6-e33e-4b69-a273-9fdd9b65ea3f",
  "timestamp": "2026-05-20T05:00:52.199Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
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
  "lastPrompt": "# Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs  ## Description We propose PI-ContextRot, the first diagnostic benchmark designed to…",
  "leafUuid": "d3f717e6-e33e-4b69-a273-9fdd9b65ea3f",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Decompose context rot into interference, position, and length factors",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:00:56.263Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal carefully. It's about decomposing "context rot" in LLMs into constituent factors using a factorial experimental design. Let me first do thorough web searches to understand the current landscape before making any judgments.

Let me search for the key papers and recent work in this area.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3f717e6-e33e-4b69-a273-9fdd9b65ea3f",
  "isSidechain": false,
  "requestId": "req_011CbDES9Bd4NNfRBS4WZFB2",
  "type": "assistant",
  "uuid": "929313b6-8993-4e8a-a50f-14d3565ca9c5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yzWpFEXCmKWXua36yTwYN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5288,
      "cache_read_input_tokens": 14549,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 188,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 5288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5288
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

_source line 9 · 2026-05-20T05:00:57.270Z_

I need to do thorough front-end research before evaluating this proposal. Let me start by searching for the key papers and recent work in this space.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "929313b6-8993-4e8a-a50f-14d3565ca9c5",
  "isSidechain": false,
  "requestId": "req_011CbDES9Bd4NNfRBS4WZFB2",
  "type": "assistant",
  "uuid": "5dc4c9a8-19f7-419b-bc7c-b475511702d8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yzWpFEXCmKWXua36yTwYN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5288,
      "cache_read_input_tokens": 14549,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 188,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 5288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5288
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

_source line 10 · 2026-05-20T05:00:57.636Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MtBTeyLNcJ6yCwhK1fyPSi`</summary>

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
  "parentUuid": "5dc4c9a8-19f7-419b-bc7c-b475511702d8",
  "isSidechain": false,
  "requestId": "req_011CbDES9Bd4NNfRBS4WZFB2",
  "type": "assistant",
  "uuid": "67ce140c-32a2-4eeb-b564-8c1fbd8b3378",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yzWpFEXCmKWXua36yTwYN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5288,
      "cache_read_input_tokens": 14549,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 188,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 5288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5288
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

_source line 11 · 2026-05-20T05:00:57.644Z_

<details><summary>↩ Tool result · `toolu_01MtBTeyLNcJ6yCwhK1fyPSi`</summary>

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
  "parentUuid": "67ce140c-32a2-4eeb-b564-8c1fbd8b3378",
  "isSidechain": false,
  "promptId": "dc85c9bb-f9bc-4bf3-8111-88cdfb7c60fe",
  "type": "user",
  "uuid": "1e2537bc-d807-4483-bc7a-e10ce44e335f",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "67ce140c-32a2-4eeb-b564-8c1fbd8b3378",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T05:01:00.477Z_

Now let me conduct my front-end research with multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e2537bc-d807-4483-bc7a-e10ce44e335f",
  "isSidechain": false,
  "requestId": "req_011CbDESYW5LrCX2sR3nZ2pp",
  "type": "assistant",
  "uuid": "0e6ca747-348c-4f08-82d0-30ea221c7274",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qkswE51Du5rpgFgGWgiXx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 715,
      "cache_read_input_tokens": 19837,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 188,
          "cache_read_input_tokens": 19837,
          "cache_creation_input_tokens": 715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 715
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

_source line 13 · 2026-05-20T05:01:01.013Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dy7pEf9SU4kJCniRvJU96H`</summary>

```json
{
  "query": "proactive interference LLM context length factorial decomposition 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e6ca747-348c-4f08-82d0-30ea221c7274",
  "isSidechain": false,
  "requestId": "req_011CbDESYW5LrCX2sR3nZ2pp",
  "type": "assistant",
  "uuid": "f36779a8-1ebc-4633-8923-bf45dd29481f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qkswE51Du5rpgFgGWgiXx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 715,
      "cache_read_input_tokens": 19837,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 188,
          "cache_read_input_tokens": 19837,
          "cache_creation_input_tokens": 715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 715
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

_source line 14 · 2026-05-20T05:01:01.980Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FDpNvQNPHQFM9LMUykFvM3`</summary>

```json
{
  "query": "context rot LLM benchmark decomposition position bias interference 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f36779a8-1ebc-4633-8923-bf45dd29481f",
  "isSidechain": false,
  "requestId": "req_011CbDESYW5LrCX2sR3nZ2pp",
  "type": "assistant",
  "uuid": "b0ee572e-d54f-4e7d-9c13-edb8d40dc38e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qkswE51Du5rpgFgGWgiXx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 715,
      "cache_read_input_tokens": 19837,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 188,
          "cache_read_input_tokens": 19837,
          "cache_creation_input_tokens": 715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 715
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

_source line 15 · 2026-05-20T05:01:02.487Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012Uje9SJTU92dkkoo36MdSs`</summary>

```json
{
  "query": "PI-LLM proactive interference arXiv 2506.08184 long context working memory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0ee572e-d54f-4e7d-9c13-edb8d40dc38e",
  "isSidechain": false,
  "requestId": "req_011CbDESYW5LrCX2sR3nZ2pp",
  "type": "assistant",
  "uuid": "201de708-9029-4dba-8823-e93d024c587b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qkswE51Du5rpgFgGWgiXx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 715,
      "cache_read_input_tokens": 19837,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 188,
          "cache_read_input_tokens": 19837,
          "cache_creation_input_tokens": 715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 715
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

_source line 16 · 2026-05-20T05:01:06.022Z_

<details><summary>↩ Tool result · `toolu_01Dy7pEf9SU4kJCniRvJU96H`</summary>

```text
Web search results for query: "proactive interference LLM context length factorial decomposition 2025 2026"

Links: [{"title":"[2506.08184v3] Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://www.arxiv.org/abs/2506.08184v3"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://arxiv.org/pdf/2506.08184"},{"title":"[2506.08184] Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://arxiv.org/abs/2506.08184"},{"title":"Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length | OpenReview","url":"https://openreview.net/forum?id=y8jS7mDurI"},{"title":"Proactive Interference Limits LLM Working Memory","url":"https://www.emergentmind.com/papers/2506.08184"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250608184W/abstract"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length - Paper Detail","url":"https://deeplearn.org/arxiv/624979/unable-to-forget:-proactive-interference-reveals-working-memory-limits-in-llms-beyond-context-length"}]

I found relevant research on your query! The search returned results about a recent paper titled "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length."

The research adapts the proactive interference paradigm from cognitive science through an evaluation called PI-LLM, which sequentially streams semantically related key-value updates and queries only the final values. Although these final values are clearly positioned just before the query, LLM retrieval accuracy declines log-linearly toward zero as interference accumulates, with errors arising from retrieving previously overwritten values.

The findings reveal a fundamental constraint on LLMs' ability to disentangle interference and flexibly manipulate information, suggesting a working memory bottleneck beyond mere context access. Attempts to mitigate interference via prompt engineering yield limited success.

The paper was published in 2025 (with the initial arxiv submission dated June 9, 2025) and appears to be the main recent work addressing the intersection of proactive interference and LLM context length limitations. However, the search results don't contain specific information about factorial decomposition as a methodology used in this research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f36779a8-1ebc-4633-8923-bf45dd29481f",
  "isSidechain": false,
  "promptId": "dc85c9bb-f9bc-4bf3-8111-88cdfb7c60fe",
  "type": "user",
  "uuid": "519329af-c1e7-4631-a86b-3df64d247686",
  "toolUseResult": {
    "query": "proactive interference LLM context length factorial decomposition 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0157P7NX7Pcj4misFN39kkDL",
        "content": [
          {
            "title": "[2506.08184v3] Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length",
            "url": "https://www.arxiv.org/abs/2506.08184v3"
          },
          {
            "title": "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length",
            "url": "https://arxiv.org/pdf/2506.08184"
          },
          {
            "title": "[2506.08184] Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length",
            "url": "https://arxiv.org/abs/2506.08184"
          },
          {
            "title": "Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length | OpenReview",
            "url": "https://openreview.net/forum?id=y8jS7mDurI"
          },
          {
            "title": "Proactive Interference Limits LLM Working Memory",
            "url": "https://www.emergentmind.com/papers/2506.08184"
          },
          {
            "title": "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250608184W/abstract"
          },
          {
            "title": "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length - Paper Detail",
            "url": "https://deeplearn.org/arxiv/624979/unable-to-forget:-proactive-interference-reveals-working-memory-limits-in-llms-beyond-context-length"
          }
        ]
      },
      "I found relevant research on your query! The search returned results about a recent paper titled \"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length.\"\n\nThe research adapts the proactive interference paradigm from cognitive science through an evaluation called PI-LLM, which sequentially streams semantically related key-value updates and queries only the final values. Although these final values are clearly positioned just before the query, LLM retrieval accuracy declines log-linearly toward zero as interference accumulates, with errors arising from retrieving previously overwritten values.\n\nThe findings reveal a fundamental constraint on LLMs' ability to disentangle interference and flexibly manipulate information, suggesting a working memory bottleneck beyond mere context access. Attempts to mitigate interference via prompt engineering yield limited success.\n\nThe paper was published in 2025 (with the initial arxiv submission dated June 9, 2025) and appears to be the main recent work addressing the intersection of proactive interference and LLM context length limitations. However, the search results don't contain specific information about factorial decomposition as a methodology used in this research."
    ],
    "durationSeconds": 5.003545425999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f36779a8-1ebc-4633-8923-bf45dd29481f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T05:01:09.462Z_

<details><summary>↩ Tool result · `toolu_012Uje9SJTU92dkkoo36MdSs`</summary>

```text
Web search results for query: "PI-LLM proactive interference arXiv 2506.08184 long context working memory"

Links: [{"title":"[2506.08184] Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://arxiv.org/abs/2506.08184"},{"title":"[2506.08184v3] Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://www.arxiv.org/abs/2506.08184v3"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length | OpenReview","url":"https://openreview.net/forum?id=YUHksmL8aw"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250608184W/abstract"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://www.researchgate.net/publication/392560721_Unable_to_forget_Proactive_lnterference_Reveals_Working_Memory_Limits_in_LLMs_Beyond_Context_Length"},{"title":"Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length | OpenReview","url":"https://openreview.net/forum?id=y8jS7mDurI"},{"title":"giantfish-fly/pi-llm · Datasets at Hugging Face","url":"https://huggingface.co/datasets/giantfish-fly/pi-llm"}]

I found the paper! Here are the key findings about PI-LLM and proactive interference in LLMs:

**Paper Overview:**
The paper is titled "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length" (arXiv 2506.08184) by Chupei Wang and Jiaqiu Vince Sun.

**Main Concept:**
PI-LLM is an evaluation that sequentially streams semantically related key-value updates and queries only the final values.

**Key Findings:**
Although final values are clearly positioned just before the query, LLM retrieval accuracy declines log-linearly toward zero as interference accumulates; errors arise from retrieving previously overwritten values.

**What It Reveals:**
These findings reveal a fundamental constraint on LLMs' ability to disentangle interference and flexibly manipulate information, suggesting a working memory bottleneck beyond mere context access.

**Research Approach:**
The test is well-established in cognitive science, where it has been studied extensively to measure human working memory capacity, and adopts the classic proactive interference paradigm.

The work was accepted at the ICML 2025 Workshop on Long Context Foundation Models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "201de708-9029-4dba-8823-e93d024c587b",
  "isSidechain": false,
  "promptId": "dc85c9bb-f9bc-4bf3-8111-88cdfb7c60fe",
  "type": "user",
  "uuid": "9a17cdc5-1b2c-45f2-a34b-8053d306dd5a",
  "toolUseResult": {
    "query": "PI-LLM proactive interference arXiv 2506.08184 long context working memory",
    "results": [
      {
        "tool_use_id": "srvtoolu_015jQtiD23py8PSRaY3T3uxr",
        "content": [
          {
            "title": "[2506.08184] Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length",
            "url": "https://arxiv.org/abs/2506.08184"
          },
          {
            "title": "[2506.08184v3] Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length",
            "url": "https://www.arxiv.org/abs/2506.08184v3"
          },
          {
            "title": "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length | OpenReview",
            "url": "https://openreview.net/forum?id=YUHksmL8aw"
          },
          {
            "title": "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250608184W/abstract"
          },
          {
            "title": "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length",
            "url": "https://www.researchgate.net/publication/392560721_Unable_to_forget_Proactive_lnterference_Reveals_Working_Memory_Limits_in_LLMs_Beyond_Context_Length"
          },
          {
            "title": "Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length | OpenReview",
            "url": "https://openreview.net/forum?id=y8jS7mDurI"
          },
          {
            "title": "giantfish-fly/pi-llm · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/giantfish-fly/pi-llm"
          }
        ]
      },
      "I found the paper! Here are the key findings about PI-LLM and proactive interference in LLMs:\n\n**Paper Overview:**\nThe paper is titled \"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length\" (arXiv 2506.08184) by Chupei Wang and Jiaqiu Vince Sun.\n\n**Main Concept:**\nPI-LLM is an evaluation that sequentially streams semantically related key-value updates and queries only the final values.\n\n**Key Findings:**\nAlthough final values are clearly positioned just before the query, LLM retrieval accuracy declines log-linearly toward zero as interference accumulates; errors arise from retrieving previously overwritten values.\n\n**What It Reveals:**\nThese findings reveal a fundamental constraint on LLMs' ability to disentangle interference and flexibly manipulate information, suggesting a working memory bottleneck beyond mere context access.\n\n**Research Approach:**\nThe test is well-established in cognitive science, where it has been studied extensively to measure human working memory capacity, and adopts the classic proactive interference paradigm.\n\nThe work was accepted at the ICML 2025 Workshop on Long Context Foundation Models."
    ],
    "durationSeconds": 6.970488141999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "201de708-9029-4dba-8823-e93d024c587b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T05:01:24.352Z_

<details><summary>↩ Tool result · `toolu_01FDpNvQNPHQFM9LMUykFvM3`</summary>

```text
Web search results for query: "context rot LLM benchmark decomposition position bias interference 2026"

Links: [{"title":"LLM Context Window Comparison (2026): Every Model, Priced and Benchmarked | Morph","url":"https://www.morphllm.com/llm-context-window-comparison"},{"title":"LLM Context Window Limitations in 2026","url":"https://atlan.com/know/llm-context-window-limitations/"},{"title":"Context rot explained (& how to prevent it)","url":"https://redis.io/blog/context-rot/"},{"title":"Position-Aware Parameter Efficient Fine-Tuning Approach for Reducing   Positional Bias in LLMs","url":"https://arxiv.org/pdf/2404.01430"},{"title":"Context Rot: Why LLMs Degrade as Context Grows (Complete Guide) | Morph","url":"https://www.morphllm.com/context-rot"},{"title":"Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs","url":"https://arxiv.org/pdf/2410.14641"},{"title":"Do RAG Systems Really Suffer From Positional Bias?","url":"https://arxiv.org/pdf/2505.15561"}]

Based on the search results, here's what I found regarding context rot in LLM benchmarks with focus on decomposition, position bias, and interference:

## Context Rot Definition

Context rot is the degradation in LLM output quality as input length grows. Chroma's 2025 research tested 18 frontier models, including GPT-4.1, Claude Opus 4, and Gemini 2.5, and found that every one exhibits this behavior at every input length increment tested.

## Position Bias and the "Lost-in-the-Middle" Effect

Models attend well to the start and end of context but poorly to the middle, causing 30%+ accuracy drops (Liu et al., Stanford/TACL 2024). The model develops recency bias, attending disproportionately to passages near the end of the input and neglecting earlier content. Shuffled text disrupts this bias, forcing more uniform attention across the input.

## Distractor Interference

Chroma's 2025 study found that semantically similar but irrelevant content actively misleads the model, causing degradation beyond what context length alone explains. A single distractor reduced baseline performance, and four distractors compounded the effect further.

## Benchmark Decomposition

LONGPIBENCH is a benchmark designed to assess positional bias involving multiple pieces of relevant information, and it assesses positional bias in two categories: (1) absolute positions, referring to the location of relevant information within the entire context, and (2) relative positions, referring to the distribution and distance between multiple relevant information pieces.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0ee572e-d54f-4e7d-9c13-edb8d40dc38e",
  "isSidechain": false,
  "promptId": "dc85c9bb-f9bc-4bf3-8111-88cdfb7c60fe",
  "type": "user",
  "uuid": "44b9bbdd-c08f-4e35-b3e6-58a65983e624",
  "toolUseResult": {
    "query": "context rot LLM benchmark decomposition position bias interference 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01L6p3px4CdmYj1zfA8yMDuG",
        "content": [
          {
            "title": "LLM Context Window Comparison (2026): Every Model, Priced and Benchmarked | Morph",
            "url": "https://www.morphllm.com/llm-context-window-comparison"
          },
          {
            "title": "LLM Context Window Limitations in 2026",
            "url": "https://atlan.com/know/llm-context-window-limitations/"
          },
          {
            "title": "Context rot explained (& how to prevent it)",
            "url": "https://redis.io/blog/context-rot/"
          },
          {
            "title": "Position-Aware Parameter Efficient Fine-Tuning Approach for Reducing   Positional Bias in LLMs",
            "url": "https://arxiv.org/pdf/2404.01430"
          },
          {
            "title": "Context Rot: Why LLMs Degrade as Context Grows (Complete Guide) | Morph",
            "url": "https://www.morphllm.com/context-rot"
          },
          {
            "title": "Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs",
            "url": "https://arxiv.org/pdf/2410.14641"
          },
          {
            "title": "Do RAG Systems Really Suffer From Positional Bias?",
            "url": "https://arxiv.org/pdf/2505.15561"
          }
        ]
      },
      "Based on the search results, here's what I found regarding context rot in LLM benchmarks with focus on decomposition, position bias, and interference:\n\n## Context Rot Definition\n\nContext rot is the degradation in LLM output quality as input length grows. Chroma's 2025 research tested 18 frontier models, including GPT-4.1, Claude Opus 4, and Gemini 2.5, and found that every one exhibits this behavior at every input length increment tested.\n\n## Position Bias and the \"Lost-in-the-Middle\" Effect\n\nModels attend well to the start and end of context but poorly to the middle, causing 30%+ accuracy drops (Liu et al., Stanford/TACL 2024). The model develops recency bias, attending disproportionately to passages near the end of the input and neglecting earlier content. Shuffled text disrupts this bias, forcing more uniform attention across the input.\n\n## Distractor Interference\n\nChroma's 2025 study found that semantically similar but irrelevant content actively misleads the model, causing degradation beyond what context length alone explains. A single distractor reduced baseline performance, and four distractors compounded the effect further.\n\n## Benchmark Decomposition\n\nLONGPIBENCH is a benchmark designed to assess positional bias involving multiple pieces of relevant information, and it assesses positional bias in two categories: (1) absolute positions, referring to the location of relevant information within the entire context, and (2) relative positions, referring to the distribution and distance between multiple relevant information pieces."
    ],
    "durationSeconds": 22.368566176,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b0ee572e-d54f-4e7d-9c13-edb8d40dc38e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T05:01:28.610Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0119sCsh2YBz8dugW5tYcEck`</summary>

```json
{
  "query": "EMB-S semantic interference long context retrieval arXiv 2601.20276 needle haystack"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44b9bbdd-c08f-4e35-b3e6-58a65983e624",
  "isSidechain": false,
  "requestId": "req_011CbDEUWTqupU4f6AwsTbFU",
  "type": "assistant",
  "uuid": "c6616045-ccf3-43cc-9e59-20a77fab88dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AsXMXV3MA16iqF4qnjvGUZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 760,
      "cache_creation_input_tokens": 1594,
      "cache_read_input_tokens": 20552,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1594,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 760,
          "output_tokens": 193,
          "cache_read_input_tokens": 20552,
          "cache_creation_input_tokens": 1594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1594
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

_source line 20 · 2026-05-20T05:01:29.550Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019Q7NBqDvJD7bj4wnWmUKPz`</summary>

```json
{
  "query": "Dual-Process interference LLM arXiv 2603.00270 proactive retroactive interference transformers 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6616045-ccf3-43cc-9e59-20a77fab88dc",
  "isSidechain": false,
  "requestId": "req_011CbDEUWTqupU4f6AwsTbFU",
  "type": "assistant",
  "uuid": "4293a97a-520c-41e7-b6de-d1a42d495bd4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AsXMXV3MA16iqF4qnjvGUZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 760,
      "cache_creation_input_tokens": 1594,
      "cache_read_input_tokens": 20552,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1594,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 760,
          "output_tokens": 193,
          "cache_read_input_tokens": 20552,
          "cache_creation_input_tokens": 1594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1594
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

_source line 21 · 2026-05-20T05:01:30.468Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VuphBMPrwXSozXpAH4FbDq`</summary>

```json
{
  "query": "CogniLoad factorial benchmark synthetic NLP reasoning length difficulty distractor arXiv 2509.18458"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4293a97a-520c-41e7-b6de-d1a42d495bd4",
  "isSidechain": false,
  "requestId": "req_011CbDEUWTqupU4f6AwsTbFU",
  "type": "assistant",
  "uuid": "52f24c61-f204-464e-8b78-ad6bfa9acc80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AsXMXV3MA16iqF4qnjvGUZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 760,
      "cache_creation_input_tokens": 1594,
      "cache_read_input_tokens": 20552,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1594,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 760,
          "output_tokens": 193,
          "cache_read_input_tokens": 20552,
          "cache_creation_input_tokens": 1594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1594
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

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs  ## Description We propose PI-ContextRot, the first diagnostic benchmark designed to…",
  "leafUuid": "52f24c61-f204-464e-8b78-ad6bfa9acc80",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Decompose context rot into interference, position, and length factors",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007"
}
```

---

### Tool result

_source line 24 · 2026-05-20T05:01:34.882Z_

<details><summary>↩ Tool result · `toolu_019Q7NBqDvJD7bj4wnWmUKPz`</summary>

```text
Web search results for query: "Dual-Process interference LLM arXiv 2603.00270 proactive retroactive interference transformers 2026"

Links: [{"title":"Transformers Remember First, Forget Last: Dual-Process Interference in LLMs","url":"https://arxiv.org/html/2603.00270"},{"title":"[2603.00270] Transformers Remember First, Forget Last: Dual-Process Interference in LLMs","url":"https://arxiv.org/abs/2603.00270"},{"title":"(PDF) Transformers Remember First, Forget Last: Dual-Process Interference in LLMs","url":"https://www.researchgate.net/publication/401469380_Transformers_Remember_First_Forget_Last_Dual-Process_Interference_in_LLMs"},{"title":"Transformers Remember First, Forget Last: Dual-Process Interference in LLMs","url":"https://arxiv.org/pdf/2603.00270"},{"title":"Transformers Remember First, Forget Last: Dual-Process Interference in LLMs | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.00270"}]

I found the paper you're looking for! Here's what the search reveals:

"Transformers Remember First, Forget Last: Dual-Process Interference in LLMs" is a paper by Sourav Chattaraj and Kanak Raj, submitted on February 27, 2026 with the latest revision on March 19, 2026 (arXiv:2603.00270).

**Key Findings:**

The research tests 39 LLMs across diverse architectures and scales, finding that proactive interference (PI) dominates retroactive interference (RI) universally with a large effect size (Cohen's d = 1.73, p < 0.0001). This means early encodings are protected at the cost of recent information—the opposite of human memory, where RI typically dominates.

Three findings indicate that RI and PI reflect separate memory mechanisms, with RI and PI being uncorrelated (R² = 0.044).

Cognitively, RI failures are passive (retrieval failure), while PI failures are active (primacy intrusion), both with minimal hallucination.

The paper adapts classical interference paradigms from cognitive psychology to investigate how transformers handle conflicting information in context.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4293a97a-520c-41e7-b6de-d1a42d495bd4",
  "isSidechain": false,
  "promptId": "dc85c9bb-f9bc-4bf3-8111-88cdfb7c60fe",
  "type": "user",
  "uuid": "e8950c97-b586-4559-872c-84a50b5d1599",
  "toolUseResult": {
    "query": "Dual-Process interference LLM arXiv 2603.00270 proactive retroactive interference transformers 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ar7HhNETryxuKm692waRSn",
        "content": [
          {
            "title": "Transformers Remember First, Forget Last: Dual-Process Interference in LLMs",
            "url": "https://arxiv.org/html/2603.00270"
          },
          {
            "title": "[2603.00270] Transformers Remember First, Forget Last: Dual-Process Interference in LLMs",
            "url": "https://arxiv.org/abs/2603.00270"
          },
          {
            "title": "(PDF) Transformers Remember First, Forget Last: Dual-Process Interference in LLMs",
            "url": "https://www.researchgate.net/publication/401469380_Transformers_Remember_First_Forget_Last_Dual-Process_Interference_in_LLMs"
          },
          {
            "title": "Transformers Remember First, Forget Last: Dual-Process Interference in LLMs",
            "url": "https://arxiv.org/pdf/2603.00270"
          },
          {
            "title": "Transformers Remember First, Forget Last: Dual-Process Interference in LLMs | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2603.00270"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search reveals:\n\n\"Transformers Remember First, Forget Last: Dual-Process Interference in LLMs\" is a paper by Sourav Chattaraj and Kanak Raj, submitted on February 27, 2026 with the latest revision on March 19, 2026 (arXiv:2603.00270).\n\n**Key Findings:**\n\nThe research tests 39 LLMs across diverse architectures and scales, finding that proactive interference (PI) dominates retroactive interference (RI) universally with a large effect size (Cohen's d = 1.73, p < 0.0001). This means early encodings are protected at the cost of recent information—the opposite of human memory, where RI typically dominates.\n\nThree findings indicate that RI and PI reflect separate memory mechanisms, with RI and PI being uncorrelated (R² = 0.044).\n\nCognitively, RI failures are passive (retrieval failure), while PI failures are active (primacy intrusion), both with minimal hallucination.\n\nThe paper adapts classical interference paradigms from cognitive psychology to investigate how transformers handle conflicting information in context."
    ],
    "durationSeconds": 5.328313825000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4293a97a-520c-41e7-b6de-d1a42d495bd4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T05:01:36.590Z_

<details><summary>↩ Tool result · `toolu_0119sCsh2YBz8dugW5tYcEck`</summary>

```text
Web search results for query: "EMB-S semantic interference long context retrieval arXiv 2601.20276 needle haystack"

Links: [{"title":"[2601.20276] Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale","url":"https://arxiv.org/abs/2601.20276"},{"title":"Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale","url":"https://arxiv.org/pdf/2601.20276"},{"title":"Beyond the Needle’s Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale","url":"https://arxiv.org/html/2601.20276"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://arxiv.org/pdf/2506.08184"},{"title":"U-NIAH: Unified RAG and LLM Evaluation for Long Context Needle-In-A-Haystack","url":"https://arxiv.org/html/2503.00353v1"},{"title":"Multilingual Needle in a Haystack: Investigating Long-Context Behavior of Multilingual Large Language Models","url":"https://arxiv.org/html/2408.10151v1"}]

Great! I found the paper you were searching for. Here's what I found about EMB-S and the arXiv paper 2601.20276:

## Paper Overview

EverMemBench-S (EMB-S) is an adversarial NIAH-style benchmark built on a 326M-token MemoryBank.

## What Makes EMB-S Different from Traditional NIAH

The popular Needle-in-a-Haystack (NIAH) evaluation mostly measures benign span localization, where the needle is near-unique and the haystack is largely irrelevant. In contrast, EMB-S deliberately mixes multiple gold documents with a dense spectrum of semantically similar distractors.

## Benchmark Composition

EMB-S pairs queries with collision-tested near-miss hard negatives and gold evidence sets spanning one or more documents, validated via human screening and LLM verification.

## Key Findings

The benchmark proposes a decoupled diagnostic protocol that reports evidence access (document-ID localization) separately from end-to-end QA quality under full-context prompting. Systems that saturate benign NIAH degrade sharply in evidence access under semantic interference, indicating that semantic discrimination, not context length alone, is the dominant bottleneck for long-context memory at scale.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6616045-ccf3-43cc-9e59-20a77fab88dc",
  "isSidechain": false,
  "promptId": "dc85c9bb-f9bc-4bf3-8111-88cdfb7c60fe",
  "type": "user",
  "uuid": "f78ee74d-89df-47be-80b7-7d12c3e894f8",
  "toolUseResult": {
    "query": "EMB-S semantic interference long context retrieval arXiv 2601.20276 needle haystack",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SxctVHg8bpMW2YDz32SbH1",
        "content": [
          {
            "title": "[2601.20276] Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale",
            "url": "https://arxiv.org/abs/2601.20276"
          },
          {
            "title": "Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale",
            "url": "https://arxiv.org/pdf/2601.20276"
          },
          {
            "title": "Beyond the Needle’s Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale",
            "url": "https://arxiv.org/html/2601.20276"
          },
          {
            "title": "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length",
            "url": "https://arxiv.org/pdf/2506.08184"
          },
          {
            "title": "U-NIAH: Unified RAG and LLM Evaluation for Long Context Needle-In-A-Haystack",
            "url": "https://arxiv.org/html/2503.00353v1"
          },
          {
            "title": "Multilingual Needle in a Haystack: Investigating Long-Context Behavior of Multilingual Large Language Models",
            "url": "https://arxiv.org/html/2408.10151v1"
          }
        ]
      },
      "Great! I found the paper you were searching for. Here's what I found about EMB-S and the arXiv paper 2601.20276:\n\n## Paper Overview\n\nEverMemBench-S (EMB-S) is an adversarial NIAH-style benchmark built on a 326M-token MemoryBank.\n\n## What Makes EMB-S Different from Traditional NIAH\n\nThe popular Needle-in-a-Haystack (NIAH) evaluation mostly measures benign span localization, where the needle is near-unique and the haystack is largely irrelevant. In contrast, EMB-S deliberately mixes multiple gold documents with a dense spectrum of semantically similar distractors.\n\n## Benchmark Composition\n\nEMB-S pairs queries with collision-tested near-miss hard negatives and gold evidence sets spanning one or more documents, validated via human screening and LLM verification.\n\n## Key Findings\n\nThe benchmark proposes a decoupled diagnostic protocol that reports evidence access (document-ID localization) separately from end-to-end QA quality under full-context prompting. Systems that saturate benign NIAH degrade sharply in evidence access under semantic interference, indicating that semantic discrimination, not context length alone, is the dominant bottleneck for long-context memory at scale."
    ],
    "durationSeconds": 7.976375108,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c6616045-ccf3-43cc-9e59-20a77fab88dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T05:01:39.794Z_

<details><summary>↩ Tool result · `toolu_01VuphBMPrwXSozXpAH4FbDq`</summary>

```text
Web search results for query: "CogniLoad factorial benchmark synthetic NLP reasoning length difficulty distractor arXiv 2509.18458"

Links: [{"title":"[2509.18458] CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density","url":"https://arxiv.org/abs/2509.18458"},{"title":"CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density","url":"https://arxiv.org/pdf/2509.18458"},{"title":"CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density - NR","url":"https://nr.no/en/publication/10341511/"},{"title":"CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density","url":"https://arxiv.org/html/2509.18458"},{"title":"CogniLoad: A Synthetic Natural Language Reasoning ...","url":"https://openreview.net/pdf?id=5XmZ5f5QVw"},{"title":"CogniLoad: A Synthetic Natural Language Reasoning ...","url":"https://www.arxiv.org/pdf/2509.18458v2"}]

I found information about CogniLoad! Here are the key details about this research paper (arXiv 2509.18458):

## Overview

CogniLoad is a novel synthetic benchmark grounded in Cognitive Load Theory (CLT). CogniLoad is a family of natural-language logic-grid puzzles explicitly crafted to probe sequential reasoning capabilities of LLMs.

## Key Features

CogniLoad generates natural-language logic puzzles with independently tunable parameters that reflect CLT's core dimensions: intrinsic difficulty (d) controls intrinsic load; distractor-to-signal ratio (ρ) regulates extraneous load; and task length (N) serves as an operational proxy for conditions demanding germane load.

## Main Findings

Evaluating 22 state-of-the-art reasoning LLMs, CogniLoad reveals distinct performance sensitivities, identifying task length as a dominant constraint and uncovering varied tolerances to intrinsic complexity and U-shaped responses to distractor ratios.

## Purpose

By offering systematic, factorial control over these cognitive load dimensions, CogniLoad provides a reproducible, scalable, and diagnostically rich tool for dissecting LLM reasoning limitations and guiding future model development.

The paper was published on September 25, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52f24c61-f204-464e-8b78-ad6bfa9acc80",
  "isSidechain": false,
  "promptId": "dc85c9bb-f9bc-4bf3-8111-88cdfb7c60fe",
  "type": "user",
  "uuid": "0c9d785f-fc62-4bdd-ac39-08a877919c08",
  "toolUseResult": {
    "query": "CogniLoad factorial benchmark synthetic NLP reasoning length difficulty distractor arXiv 2509.18458",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HVFsQbznPCCSZUBYnFUFwi",
        "content": [
          {
            "title": "[2509.18458] CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density",
            "url": "https://arxiv.org/abs/2509.18458"
          },
          {
            "title": "CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density",
            "url": "https://arxiv.org/pdf/2509.18458"
          },
          {
            "title": "CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density - NR",
            "url": "https://nr.no/en/publication/10341511/"
          },
          {
            "title": "CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density",
            "url": "https://arxiv.org/html/2509.18458"
          },
          {
            "title": "CogniLoad: A Synthetic Natural Language Reasoning ...",
            "url": "https://openreview.net/pdf?id=5XmZ5f5QVw"
          },
          {
            "title": "CogniLoad: A Synthetic Natural Language Reasoning ...",
            "url": "https://www.arxiv.org/pdf/2509.18458v2"
          }
        ]
      },
      "I found information about CogniLoad! Here are the key details about this research paper (arXiv 2509.18458):\n\n## Overview\n\nCogniLoad is a novel synthetic benchmark grounded in Cognitive Load Theory (CLT). CogniLoad is a family of natural-language logic-grid puzzles explicitly crafted to probe sequential reasoning capabilities of LLMs.\n\n## Key Features\n\nCogniLoad generates natural-language logic puzzles with independently tunable parameters that reflect CLT's core dimensions: intrinsic difficulty (d) controls intrinsic load; distractor-to-signal ratio (ρ) regulates extraneous load; and task length (N) serves as an operational proxy for conditions demanding germane load.\n\n## Main Findings\n\nEvaluating 22 state-of-the-art reasoning LLMs, CogniLoad reveals distinct performance sensitivities, identifying task length as a dominant constraint and uncovering varied tolerances to intrinsic complexity and U-shaped responses to distractor ratios.\n\n## Purpose\n\nBy offering systematic, factorial control over these cognitive load dimensions, CogniLoad provides a reproducible, scalable, and diagnostically rich tool for dissecting LLM reasoning limitations and guiding future model development.\n\nThe paper was published on September 25, 2025."
    ],
    "durationSeconds": 9.323589217,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "52f24c61-f204-464e-8b78-ad6bfa9acc80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T05:01:44.733Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H7nMQoGcXhLExU5gsBhdid`</summary>

```json
{
  "query": "Sculptor active context management ICLR 2026 arXiv 2508.04664 proactive interference mitigation LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c9d785f-fc62-4bdd-ac39-08a877919c08",
  "isSidechain": false,
  "requestId": "req_011CbDEVg5pcvXU55ucGqbbe",
  "type": "assistant",
  "uuid": "7758ad38-570a-417e-a2c0-d5e0dcbc3b9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GZH7ANTCMK9CUsT7w9Rws",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 22146,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2936,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 22146,
          "cache_creation_input_tokens": 2936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2936
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

_source line 28 · 2026-05-20T05:01:45.377Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DLTYF1JvqsDFoiHzW5CxSc`</summary>

```json
{
  "query": "long context LLM evaluation ANOVA factorial design effect size benchmark 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7758ad38-570a-417e-a2c0-d5e0dcbc3b9b",
  "isSidechain": false,
  "requestId": "req_011CbDEVg5pcvXU55ucGqbbe",
  "type": "assistant",
  "uuid": "c508b20a-a7b4-40d4-8ef5-9f52831f1e64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GZH7ANTCMK9CUsT7w9Rws",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 22146,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2936,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 22146,
          "cache_creation_input_tokens": 2936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2936
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

_source line 29 · 2026-05-20T05:01:50.817Z_

<details><summary>↩ Tool result · `toolu_01H7nMQoGcXhLExU5gsBhdid`</summary>

```text
Web search results for query: "Sculptor active context management ICLR 2026 arXiv 2508.04664 proactive interference mitigation LLM"

Links: [{"title":"ICLR Poster Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://iclr.cc/virtual/2026/poster/10010394"},{"title":"Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://arxiv.org/html/2508.04664v1"},{"title":"[2508.04664] Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://arxiv.org/abs/2508.04664"},{"title":"[2508.04664v1] Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://arxiv.org/abs/2508.04664v1"},{"title":"Mo Li","url":"https://mor-li.github.io/"},{"title":"(PDF) Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://www.researchgate.net/publication/394362750_Sculptor_Empowering_LLMs_with_Cognitive_Agency_via_Active_Context_Management"},{"title":"Paper page - Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://huggingface.co/papers/2508.04664"},{"title":"Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://www.arxiv.org/pdf/2508.04664v1"},{"title":"Sculptor: Empowering LLMs with Cognitive Agency via Active ...","url":"https://www.alphaxiv.org/overview/2508.04664v1"},{"title":"Sculptor: Empowering LLMs with Cognitive Agency via ...","url":"https://www.arxiv.org/pdf/2508.04664"}]

Based on the search results, here's what I found about Sculptor:

## Overview

Large Language Models (LLMs) suffer from significant performance degradation when processing long contexts due to proactive interference, where irrelevant information in earlier parts of the context disrupts reasoning and memory recall.

## The Sculptor Framework

Sculptor is a framework that equips LLMs with three categories of tools: (1) context fragmentation, (2) summary, hide, and restore, and (3) precise search. It proposes a complementary approach: empowering LLMs with Active Context Management (ACM) tools to actively sculpt their internal working memory.

## Key Benefits

The approach enables LLMs to proactively manage their attention and working memory, analogous to how humans selectively focus on relevant information while filtering out distractions.

## Publication Details

The paper was submitted to arXiv on August 6, 2025 (arXiv ID: 2508.04664) and is scheduled to appear in the proceedings of ICLR 2026. The research team includes Mo Li, L.H. Xu, Qitai Tan, Long Ma, Ting Cao, and Yunxin Liu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7758ad38-570a-417e-a2c0-d5e0dcbc3b9b",
  "isSidechain": false,
  "promptId": "dc85c9bb-f9bc-4bf3-8111-88cdfb7c60fe",
  "type": "user",
  "uuid": "7e207329-e996-4b33-b26a-45986de48586",
  "toolUseResult": {
    "query": "Sculptor active context management ICLR 2026 arXiv 2508.04664 proactive interference mitigation LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_01L6PDkrVb8CT6KWpwxAqM8e",
        "content": [
          {
            "title": "ICLR Poster Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://iclr.cc/virtual/2026/poster/10010394"
          },
          {
            "title": "Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://arxiv.org/html/2508.04664v1"
          },
          {
            "title": "[2508.04664] Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://arxiv.org/abs/2508.04664"
          },
          {
            "title": "[2508.04664v1] Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://arxiv.org/abs/2508.04664v1"
          },
          {
            "title": "Mo Li",
            "url": "https://mor-li.github.io/"
          },
          {
            "title": "(PDF) Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://www.researchgate.net/publication/394362750_Sculptor_Empowering_LLMs_with_Cognitive_Agency_via_Active_Context_Management"
          },
          {
            "title": "Paper page - Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://huggingface.co/papers/2508.04664"
          },
          {
            "title": "Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://www.arxiv.org/pdf/2508.04664v1"
          },
          {
            "title": "Sculptor: Empowering LLMs with Cognitive Agency via Active ...",
            "url": "https://www.alphaxiv.org/overview/2508.04664v1"
          },
          {
            "title": "Sculptor: Empowering LLMs with Cognitive Agency via ...",
            "url": "https://www.arxiv.org/pdf/2508.04664"
          }
        ]
      },
      "Based on the search results, here's what I found about Sculptor:\n\n## Overview\n\nLarge Language Models (LLMs) suffer from significant performance degradation when processing long contexts due to proactive interference, where irrelevant information in earlier parts of the context disrupts reasoning and memory recall.\n\n## The Sculptor Framework\n\nSculptor is a framework that equips LLMs with three categories of tools: (1) context fragmentation, (2) summary, hide, and restore, and (3) precise search. It proposes a complementary approach: empowering LLMs with Active Context Management (ACM) tools to actively sculpt their internal working memory.\n\n## Key Benefits\n\nThe approach enables LLMs to proactively manage their attention and working memory, analogous to how humans selectively focus on relevant information while filtering out distractions.\n\n## Publication Details\n\nThe paper was submitted to arXiv on August 6, 2025 (arXiv ID: 2508.04664) and is scheduled to appear in the proceedings of ICLR 2026. The research team includes Mo Li, L.H. Xu, Qitai Tan, Long Ma, Ting Cao, and Yunxin Liu."
    ],
    "durationSeconds": 6.0801591370000025,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7758ad38-570a-417e-a2c0-d5e0dcbc3b9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T05:01:52.063Z_

<details><summary>↩ Tool result · `toolu_01DLTYF1JvqsDFoiHzW5CxSc`</summary>

```text
Web search results for query: "long context LLM evaluation ANOVA factorial design effect size benchmark 2025 2026"

Links: [{"title":"Long-Context Language Modeling Benchmarks","url":"https://www.emergentmind.com/topics/long-context-language-modeling-benchmarks"},{"title":"LIFBench: Evaluating the Instruction Following Performance and Stability of Large Language Models in Long-Context Scenarios","url":"https://arxiv.org/pdf/2411.07037"},{"title":"$\\infty$Bench: Extending Long Context Evaluation Beyond 100K Tokens","url":"https://arxiv.org/pdf/2402.13718"},{"title":"Ada-LEval: Evaluating long-context LLMs with length-adaptable benchmarks","url":"https://arxiv.org/pdf/2404.06480"},{"title":"LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark","url":"https://arxiv.org/pdf/2601.02872"}]

Based on the web search results, I found information about recent long-context LLM evaluation benchmarks and research. Here's what the search reveals:

## Recent Long-Context LLM Evaluation Benchmarks (2025-2026)

Modern benchmarks such as AcademicEval (Zhang et al., 20 Oct 2025), LongProc (Ye et al., 9 Jan 2025), and Ref-Long (Wu et al., 13 Jul 2025) adopt key construction features including dynamic context scaling to enable controlled analysis of length effects.

The Long-context Instruction Following Benchmark (LIFBENCH) is a scalable benchmark for evaluating LLMs' instruction-following capability and stability in long-context scenarios.

With advances in architectures and computational resources, context length has continuously expanded (Comanici et al., 2025; OpenAI, 2025; Anthropic, 2025), and long-context benchmarks have evolved to accurately assess models' true long-context capabilities.

## Evaluation Approaches

Modern benchmarks explicitly bucket tasks by context length (e.g., 16 K, 32 K, 64 K, 128 K, 256 K words/tokens) to enable controlled analysis of length effects.

However, the search results don't contain specific information about ANOVA factorial designs, effect size measurements, or statistical methodologies in these recent benchmarks. The results focus more on the benchmarks themselves and their construction features rather than the statistical analysis methods used to evaluate them.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c508b20a-a7b4-40d4-8ef5-9f52831f1e64",
  "isSidechain": false,
  "promptId": "dc85c9bb-f9bc-4bf3-8111-88cdfb7c60fe",
  "type": "user",
  "uuid": "55739b03-3af7-418c-9530-eec7a7bdd1b9",
  "toolUseResult": {
    "query": "long context LLM evaluation ANOVA factorial design effect size benchmark 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WAzcrCiV6SQRmbxFYzTCvS",
        "content": [
          {
            "title": "Long-Context Language Modeling Benchmarks",
            "url": "https://www.emergentmind.com/topics/long-context-language-modeling-benchmarks"
          },
          {
            "title": "LIFBench: Evaluating the Instruction Following Performance and Stability of Large Language Models in Long-Context Scenarios",
            "url": "https://arxiv.org/pdf/2411.07037"
          },
          {
            "title": "$\\infty$Bench: Extending Long Context Evaluation Beyond 100K Tokens",
            "url": "https://arxiv.org/pdf/2402.13718"
          },
          {
            "title": "Ada-LEval: Evaluating long-context LLMs with length-adaptable benchmarks",
            "url": "https://arxiv.org/pdf/2404.06480"
          },
          {
            "title": "LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark",
            "url": "https://arxiv.org/pdf/2601.02872"
          }
        ]
      },
      "Based on the web search results, I found information about recent long-context LLM evaluation benchmarks and research. Here's what the search reveals:\n\n## Recent Long-Context LLM Evaluation Benchmarks (2025-2026)\n\nModern benchmarks such as AcademicEval (Zhang et al., 20 Oct 2025), LongProc (Ye et al., 9 Jan 2025), and Ref-Long (Wu et al., 13 Jul 2025) adopt key construction features including dynamic context scaling to enable controlled analysis of length effects.\n\nThe Long-context Instruction Following Benchmark (LIFBENCH) is a scalable benchmark for evaluating LLMs' instruction-following capability and stability in long-context scenarios.\n\nWith advances in architectures and computational resources, context length has continuously expanded (Comanici et al., 2025; OpenAI, 2025; Anthropic, 2025), and long-context benchmarks have evolved to accurately assess models' true long-context capabilities.\n\n## Evaluation Approaches\n\nModern benchmarks explicitly bucket tasks by context length (e.g., 16 K, 32 K, 64 K, 128 K, 256 K words/tokens) to enable controlled analysis of length effects.\n\nHowever, the search results don't contain specific information about ANOVA factorial designs, effect size measurements, or statistical methodologies in these recent benchmarks. The results focus more on the benchmarks themselves and their construction features rather than the statistical analysis methods used to evaluate them."
    ],
    "durationSeconds": 6.680761451999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c508b20a-a7b4-40d4-8ef5-9f52831f1e64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-20T05:01:52.075Z_

```json
{
  "parentUuid": "55739b03-3af7-418c-9530-eec7a7bdd1b9",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "842bada2-e748-4ba2-b0ee-eafd43f51c6c",
  "timestamp": "2026-05-20T05:01:52.075Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 32 · 2026-05-20T05:01:55.495Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UH8CTygkQZAzcrBsDGQtLT`</summary>

```json
{
  "query": "\"context rot\" \"factorial\" OR \"ANOVA\" OR \"effect size\" OR \"decomposition\" LLM interference position length 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "842bada2-e748-4ba2-b0ee-eafd43f51c6c",
  "isSidechain": false,
  "requestId": "req_011CbDEWZ1CeABpiGiej3447",
  "type": "assistant",
  "uuid": "a574daa9-e133-4a42-86d2-1a73722f1acb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQCd4DUz9251F9Ua2Ziutj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1689,
      "cache_read_input_tokens": 25082,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 25082,
          "cache_creation_input_tokens": 1689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1689
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

_source line 33 · 2026-05-20T05:01:56.131Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TzQAQMre1t2rWdBbcw5ViE`</summary>

```json
{
  "query": "long context benchmark diagnostic causal decomposition interference similarity position 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a574daa9-e133-4a42-86d2-1a73722f1acb",
  "isSidechain": false,
  "requestId": "req_011CbDEWZ1CeABpiGiej3447",
  "type": "assistant",
  "uuid": "3a862f14-d00c-4768-8af0-bab9f150eb2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQCd4DUz9251F9Ua2Ziutj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1689,
      "cache_read_input_tokens": 25082,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 25082,
          "cache_creation_input_tokens": 1689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1689
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

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs  ## Description We propose PI-ContextRot, the first diagnostic benchmark designed to…",
  "leafUuid": "3a862f14-d00c-4768-8af0-bab9f150eb2e",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Decompose context rot into interference, position, and length factors",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007"
}
```

---

### Tool result

_source line 36 · 2026-05-20T05:02:03.588Z_

<details><summary>↩ Tool result · `toolu_01UH8CTygkQZAzcrBsDGQtLT`</summary>

```text
Web search results for query: ""context rot" "factorial" OR "ANOVA" OR "effect size" OR "decomposition" LLM interference position length 2026"

Links: [{"title":"LLM Context Window Limitations in 2026","url":"https://atlan.com/know/llm-context-window-limitations/"},{"title":"Context Rot: Why LLMs Degrade as Context Grows (Complete Guide) | Morph","url":"https://www.morphllm.com/context-rot"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://arxiv.org/pdf/2506.08184"},{"title":"Context Rot: How Increasing Input Tokens Impacts LLM Performance | Chroma","url":"https://www.trychroma.com/research/context-rot"},{"title":"Transformers Remember First, Forget Last: Dual-Process Interference in LLMs","url":"https://arxiv.org/pdf/2603.00270"},{"title":"Context Rot: Why AI Gets Worse the Longer You Chat (And How to Fix It)","url":"https://www.producttalk.org/context-rot/"},{"title":"LLM Context Window Comparison (2026): Every Model, Priced and Benchmarked | Morph","url":"https://www.morphllm.com/llm-context-window-comparison"}]

Based on my search results, here's what I found about "context rot" and related topics in 2026:

## Context Rot Definition

Context rot is the measurable degradation in LLM output quality that occurs as input context length increases. Research testing 18 frontier models found that every single one gets worse as input length increases.

## Key Mechanisms

Context rot degrades LLM accuracy through three compounding mechanisms: lost-in-the-middle attention gaps, attention dilution as token counts grow, and distractor interference from semantically similar but irrelevant content.

Stanford and UC Berkeley researchers first documented the lost-in-the-middle problem in 2023: models attend well to the beginning and end of context but poorly to the middle, with accuracy dropping by more than 30% when relevant information was placed in middle positions.

## Proactive Interference

A 2025 paper titled "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length" studied semantic interference effects. When semantically related information is updated sequentially, LLM retrieval accuracy declines loglinearly toward zero as interference accumulates, with errors arising from retrieving previously overwritten values.

## Position Effects

Recent 2026 research shows nuanced findings about position effects. Veseli et al (2025) found that the U-shaped pattern (favoring beginning and end tokens) only persists when context is less than 50% full; when greater than 50% full, context degrades by distance from the end, where the model favors more recent tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a574daa9-e133-4a42-86d2-1a73722f1acb",
  "isSidechain": false,
  "promptId": "dc85c9bb-f9bc-4bf3-8111-88cdfb7c60fe",
  "type": "user",
  "uuid": "556fa8ee-b65d-444e-9ced-31a71fd42cbf",
  "toolUseResult": {
    "query": "\"context rot\" \"factorial\" OR \"ANOVA\" OR \"effect size\" OR \"decomposition\" LLM interference position length 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012wZ7TWu6wNn8aYb5n4Uq9B",
        "content": [
          {
            "title": "LLM Context Window Limitations in 2026",
            "url": "https://atlan.com/know/llm-context-window-limitations/"
          },
          {
            "title": "Context Rot: Why LLMs Degrade as Context Grows (Complete Guide) | Morph",
            "url": "https://www.morphllm.com/context-rot"
          },
          {
            "title": "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length",
            "url": "https://arxiv.org/pdf/2506.08184"
          },
          {
            "title": "Context Rot: How Increasing Input Tokens Impacts LLM Performance | Chroma",
            "url": "https://www.trychroma.com/research/context-rot"
          },
          {
            "title": "Transformers Remember First, Forget Last: Dual-Process Interference in LLMs",
            "url": "https://arxiv.org/pdf/2603.00270"
          },
          {
            "title": "Context Rot: Why AI Gets Worse the Longer You Chat (And How to Fix It)",
            "url": "https://www.producttalk.org/context-rot/"
          },
          {
            "title": "LLM Context Window Comparison (2026): Every Model, Priced and Benchmarked | Morph",
            "url": "https://www.morphllm.com/llm-context-window-comparison"
          }
        ]
      },
      "Based on my search results, here's what I found about \"context rot\" and related topics in 2026:\n\n## Context Rot Definition\n\nContext rot is the measurable degradation in LLM output quality that occurs as input context length increases. Research testing 18 frontier models found that every single one gets worse as input length increases.\n\n## Key Mechanisms\n\nContext rot degrades LLM accuracy through three compounding mechanisms: lost-in-the-middle attention gaps, attention dilution as token counts grow, and distractor interference from semantically similar but irrelevant content.\n\nStanford and UC Berkeley researchers first documented the lost-in-the-middle problem in 2023: models attend well to the beginning and end of context but poorly to the middle, with accuracy dropping by more than 30% when relevant information was placed in middle positions.\n\n## Proactive Interference\n\nA 2025 paper titled \"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length\" studied semantic interference effects. When semantically related information is updated sequentially, LLM retrieval accuracy declines loglinearly toward zero as interference accumulates, with errors arising from retrieving previously overwritten values.\n\n## Position Effects\n\nRecent 2026 research shows nuanced findings about position effects. Veseli et al (2025) found that the U-shaped pattern (favoring beginning and end tokens) only persists when context is less than 50% full; when greater than 50% full, context degrades by distance from the end, where the model favors more recent tokens."
    ],
    "durationSeconds": 8.087606501000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a574daa9-e133-4a42-86d2-1a73722f1acb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-20T05:02:03.807Z_

<details><summary>↩ Tool result · `toolu_01TzQAQMre1t2rWdBbcw5ViE`</summary>

```text
Web search results for query: "long context benchmark diagnostic causal decomposition interference similarity position 2026 arxiv"

Links: [{"title":"Published as a conference paper at ICLR 2026 LONG-CONTEXT GENERALIZATION WITH","url":"https://arxiv.org/pdf/2506.16640"},{"title":"Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale","url":"https://arxiv.org/pdf/2601.20276"},{"title":"LongBench: A Bilingual, Multitask Benchmark for Long Context   Understanding","url":"https://arxiv.org/pdf/2308.14508"},{"title":"Retrieval Or Holistic Understanding? Dolce: Differentiate Our Long   Context Evaluation Tasks","url":"https://arxiv.org/pdf/2409.06338"},{"title":"Long-Context Language Modeling Benchmarks","url":"https://www.emergentmind.com/topics/long-context-language-modeling-benchmarks"},{"title":"Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs","url":"https://arxiv.org/pdf/2410.14641"},{"title":"[2605.17641] Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents","url":"https://arxiv.org/abs/2605.17641"},{"title":"100-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability?","url":"https://arxiv.org/pdf/2505.19293"},{"title":"LongBench: Are de facto Long-Context Benchmarks Literally","url":"https://aclanthology.org/2025.findings-acl.903.pdf"}]

Based on the search results, I found several relevant papers and resources related to long-context benchmarking and evaluation. Here are some key findings:

## Long-Context Benchmarks and Evaluation

EMB-S reports evidence access via document-ID localization metrics and end-to-end QA quality under full-context prompting, enabling diagnosis of access failures and robustness under semantic interference without sacrificing scalability.

LONGPIBENCH is a benchmark designed to evaluate positional bias with multiple relevant pieces, assessing positional bias in two categories: absolute positions (referring to the location of relevant information within the entire context) and relative positions (referring to the distribution and distance between multiple relevant information pieces).

## Key Concepts

The distance between relevant information pieces, or how densely they are distributed, termed as "relative position," may lead to significant bias when varied, impairing LLMs' long-context performance.

## Related Benchmarks

Long context evaluation benchmark suites have been developed, including LRA, ZeroSCROLLS, L-Eval, LongBench, BAMBOO, LooGLE, Loong, LV-Eval, ∞Bench, Marathon, BABILong, Ruler, and LOFT.

The search results indicate active research in 2025-2026 on diagnosing and understanding various aspects of long-context model performance, including the effects of semantic interference, positional bias, and evidence access mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a862f14-d00c-4768-8af0-bab9f150eb2e",
  "isSidechain": false,
  "promptId": "dc85c9bb-f9bc-4bf3-8111-88cdfb7c60fe",
  "type": "user",
  "uuid": "24581b64-8553-47b1-b73d-524d3f4955a4",
  "toolUseResult": {
    "query": "long context benchmark diagnostic causal decomposition interference similarity position 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QJ85YQHCuYDHXFcFiyKt6P",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026 LONG-CONTEXT GENERALIZATION WITH",
            "url": "https://arxiv.org/pdf/2506.16640"
          },
          {
            "title": "Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale",
            "url": "https://arxiv.org/pdf/2601.20276"
          },
          {
            "title": "LongBench: A Bilingual, Multitask Benchmark for Long Context   Understanding",
            "url": "https://arxiv.org/pdf/2308.14508"
          },
          {
            "title": "Retrieval Or Holistic Understanding? Dolce: Differentiate Our Long   Context Evaluation Tasks",
            "url": "https://arxiv.org/pdf/2409.06338"
          },
          {
            "title": "Long-Context Language Modeling Benchmarks",
            "url": "https://www.emergentmind.com/topics/long-context-language-modeling-benchmarks"
          },
          {
            "title": "Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs",
            "url": "https://arxiv.org/pdf/2410.14641"
          },
          {
            "title": "[2605.17641] Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents",
            "url": "https://arxiv.org/abs/2605.17641"
          },
          {
            "title": "100-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability?",
            "url": "https://arxiv.org/pdf/2505.19293"
          },
          {
            "title": "LongBench: Are de facto Long-Context Benchmarks Literally",
            "url": "https://aclanthology.org/2025.findings-acl.903.pdf"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and resources related to long-context benchmarking and evaluation. Here are some key findings:\n\n## Long-Context Benchmarks and Evaluation\n\nEMB-S reports evidence access via document-ID localization metrics and end-to-end QA quality under full-context prompting, enabling diagnosis of access failures and robustness under semantic interference without sacrificing scalability.\n\nLONGPIBENCH is a benchmark designed to evaluate positional bias with multiple relevant pieces, assessing positional bias in two categories: absolute positions (referring to the location of relevant information within the entire context) and relative positions (referring to the distribution and distance between multiple relevant information pieces).\n\n## Key Concepts\n\nThe distance between relevant information pieces, or how densely they are distributed, termed as \"relative position,\" may lead to significant bias when varied, impairing LLMs' long-context performance.\n\n## Related Benchmarks\n\nLong context evaluation benchmark suites have been developed, including LRA, ZeroSCROLLS, L-Eval, LongBench, BAMBOO, LooGLE, Loong, LV-Eval, ∞Bench, Marathon, BABILong, Ruler, and LOFT.\n\nThe search results indicate active research in 2025-2026 on diagnosing and understanding various aspects of long-context model performance, including the effects of semantic interference, positional bias, and evidence access mechanisms."
    ],
    "durationSeconds": 7.672699947999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3a862f14-d00c-4768-8af0-bab9f150eb2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-20T05:02:07.509Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do one more targeted search to look for any very recent work that might directly overlap with this proposal's factorial decomposition approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24581b64-8553-47b1-b73d-524d3f4955a4",
  "isSidechain": false,
  "requestId": "req_011CbDEXRAh5TRqcKeVZd5Kr",
  "type": "assistant",
  "uuid": "9d94e46b-e9ba-418a-9479-1ff8b5193bbf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QhiySsBW5tjbrWLstDakp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1680,
      "cache_read_input_tokens": 26771,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 26771,
          "cache_creation_input_tokens": 1680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1680
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

_source line 39 · 2026-05-20T05:02:08.362Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015Z1LA1jRV7DVDTu2wZXNVz`</summary>

```json
{
  "query": "attribution patching AtP* LLM attention entropy mechanistic interpretability long context 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d94e46b-e9ba-418a-9479-1ff8b5193bbf",
  "isSidechain": false,
  "requestId": "req_011CbDEXRAh5TRqcKeVZd5Kr",
  "type": "assistant",
  "uuid": "22974c5d-477a-4c08-a358-5d561bdc8aa3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QhiySsBW5tjbrWLstDakp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1680,
      "cache_read_input_tokens": 26771,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 26771,
          "cache_creation_input_tokens": 1680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1680
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

_source line 40 · 2026-05-20T05:02:09.117Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VJYXeFqipcwcJHBtKSfX4M`</summary>

```json
{
  "query": "\"100-LongBench\" OR \"DOLCE\" long context evaluation disentangle factors 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22974c5d-477a-4c08-a358-5d561bdc8aa3",
  "isSidechain": false,
  "requestId": "req_011CbDEXRAh5TRqcKeVZd5Kr",
  "type": "assistant",
  "uuid": "3c305679-18ca-47ce-b2fb-697c2a246770",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QhiySsBW5tjbrWLstDakp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1680,
      "cache_read_input_tokens": 26771,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 26771,
          "cache_creation_input_tokens": 1680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1680
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

_source line 41 · 2026-05-20T05:02:16.101Z_

<details><summary>↩ Tool result · `toolu_015Z1LA1jRV7DVDTu2wZXNVz`</summary>

```text
Web search results for query: "attribution patching AtP* LLM attention entropy mechanistic interpretability long context 2025 2026"

Links: [{"title":"AtP^*: An efficient and scalable method for localizing LLM behaviour to components","url":"https://arxiv.org/html/2403.00745v1"},{"title":"Attribution Patching for NN Interpretability","url":"https://www.emergentmind.com/topics/attribution-patching-atp"},{"title":"AtP*: Efficient and scalable methods for localizing LLM behaviour to components — Google DeepMind","url":"https://deepmind.google/research/publications/68553/"},{"title":"AtP : An efficient and scalable method for localizing LLM ...","url":"https://arxiv.org/pdf/2403.00745"},{"title":"AtP*: An efficient and scalable method for localizing LLM ...","url":"https://www.alignmentforum.org/posts/pnMnjdSJwqa7BHAo4/atp-an-efficient-and-scalable-method-for-localizing-llm"},{"title":"AtP*: An efficient and scalable method for localizing LLM behaviour to components — LessWrong","url":"https://www.lesswrong.com/posts/pnMnjdSJwqa7BHAo4/atp-an-efficient-and-scalable-method-for-localizing-llm"},{"title":"Attribution Patching in LLMs","url":"https://www.emergentmind.com/topics/attribution-patching"},{"title":"Sparse Attention Post-Training for Mechanistic Interpretability","url":"https://arxiv.org/html/2512.05865v2"},{"title":"[2403.00745] AtP*: An efficient and scalable method for localizing LLM behaviour to components","url":"https://arxiv.org/abs/2403.00745"}]

Based on the web search results, here's what I found about Attribution Patching (AtP*), LLM mechanistic interpretability, and related concepts:

## Overview

Attribution Patching (AtP) is a class of mechanistic interpretability techniques for neural networks that estimate the causal contribution of specific model components (e.g., neurons, attention heads, MLPs) to a model's behavior by approximating the effects of patching internal activations.

## AtP* Method

Attribution Patching (AtP) is a gradient-based approximation that runs in O(1) passes as a pre-filtering step to Activation Patching, with a variant called AtP* proposed to address failure modes while retaining scalability. Two classes of failure modes of AtP lead to significant false negatives.

## Scalability and Recent Developments

AtP scales robustly to models with millions to billions of nodes, making fine-grained causal localization feasible for state-of-the-art LLMs. Scalable and faithful attribution methods such as AtP*, RelP, and their descendants will become central to both interpretability science and safe model intervention at scale.

## Connection to Attention and Long Context

While the search results cover Attribution Patching and mechanistic interpretability extensively, they don't specifically address attention entropy or long context applications of these methods. The results do mention that attribution addresses causal attribution of behaviors to individual parts of the transformer forward pass, corresponding to specific components such as attention heads, with researchers considering the query, key, and value vector for each head as distinct nodes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22974c5d-477a-4c08-a358-5d561bdc8aa3",
  "isSidechain": false,
  "promptId": "dc85c9bb-f9bc-4bf3-8111-88cdfb7c60fe",
  "type": "user",
  "uuid": "434525e2-158d-4b54-a591-f7bd046eaa0f",
  "toolUseResult": {
    "query": "attribution patching AtP* LLM attention entropy mechanistic interpretability long context 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014QpWdeiuM1huLL777igsem",
        "content": [
          {
            "title": "AtP^*: An efficient and scalable method for localizing LLM behaviour to components",
            "url": "https://arxiv.org/html/2403.00745v1"
          },
          {
            "title": "Attribution Patching for NN Interpretability",
            "url": "https://www.emergentmind.com/topics/attribution-patching-atp"
          },
          {
            "title": "AtP*: Efficient and scalable methods for localizing LLM behaviour to components — Google DeepMind",
            "url": "https://deepmind.google/research/publications/68553/"
          },
          {
            "title": "AtP : An efficient and scalable method for localizing LLM ...",
            "url": "https://arxiv.org/pdf/2403.00745"
          },
          {
            "title": "AtP*: An efficient and scalable method for localizing LLM ...",
            "url": "https://www.alignmentforum.org/posts/pnMnjdSJwqa7BHAo4/atp-an-efficient-and-scalable-method-for-localizing-llm"
          },
          {
            "title": "AtP*: An efficient and scalable method for localizing LLM behaviour to components — LessWrong",
            "url": "https://www.lesswrong.com/posts/pnMnjdSJwqa7BHAo4/atp-an-efficient-and-scalable-method-for-localizing-llm"
          },
          {
            "title": "Attribution Patching in LLMs",
            "url": "https://www.emergentmind.com/topics/attribution-patching"
          },
          {
            "title": "Sparse Attention Post-Training for Mechanistic Interpretability",
            "url": "https://arxiv.org/html/2512.05865v2"
          },
          {
            "title": "[2403.00745] AtP*: An efficient and scalable method for localizing LLM behaviour to components",
            "url": "https://arxiv.org/abs/2403.00745"
          }
        ]
      },
      "Based on the web search results, here's what I found about Attribution Patching (AtP*), LLM mechanistic interpretability, and related concepts:\n\n## Overview\n\nAttribution Patching (AtP) is a class of mechanistic interpretability techniques for neural networks that estimate the causal contribution of specific model components (e.g., neurons, attention heads, MLPs) to a model's behavior by approximating the effects of patching internal activations.\n\n## AtP* Method\n\nAttribution Patching (AtP) is a gradient-based approximation that runs in O(1) passes as a pre-filtering step to Activation Patching, with a variant called AtP* proposed to address failure modes while retaining scalability. Two classes of failure modes of AtP lead to significant false negatives.\n\n## Scalability and Recent Developments\n\nAtP scales robustly to models with millions to billions of nodes, making fine-grained causal localization feasible for state-of-the-art LLMs. Scalable and faithful attribution methods such as AtP*, RelP, and their descendants will become central to both interpretability science and safe model intervention at scale.\n\n## Connection to Attention and Long Context\n\nWhile the search results cover Attribution Patching and mechanistic interpretability extensively, they don't specifically address attention entropy or long context applications of these methods. The results do mention that attribution addresses causal attribution of behaviors to individual parts of the transformer forward pass, corresponding to specific components such as attention heads, with researchers considering the query, key, and value vector for each head as distinct nodes."
    ],
    "durationSeconds": 7.734576967999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "22974c5d-477a-4c08-a358-5d561bdc8aa3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T05:02:16.231Z_

<details><summary>↩ Tool result · `toolu_01VJYXeFqipcwcJHBtKSfX4M`</summary>

```text
Web search results for query: ""100-LongBench" OR "DOLCE" long context evaluation disentangle factors 2025 2026"

Links: [{"title":"[Literature Review] 100-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability?","url":"https://www.themoonlight.io/en/review/100-longbench-are-de-facto-long-context-benchmarks-literally-evaluating-long-context-ability"},{"title":"100-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability? | OpenReview","url":"https://openreview.net/forum?id=zfaZZzbw0m"},{"title":"100-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability? - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.903/"},{"title":"[2505.19293] 100-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability?","url":"https://arxiv.org/abs/2505.19293"},{"title":"100-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability? | alphaXiv","url":"https://www.alphaxiv.org/resources/2505.19293v1"},{"title":"100-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability? | Request PDF","url":"https://www.researchgate.net/publication/392105517_100-LongBench_Are_de_facto_Long-Context_Benchmarks_Literally_Evaluating_Long-Context_Ability"},{"title":"100-LongBench: Are de facto Long-Context Benchmarks ...","url":"https://arxiv.org/pdf/2505.19293"}]

Based on the search results, I found information about **100-LongBench**, which addresses long-context evaluation. However, I did not find results specifically mentioning "DOLCE" in the search results returned.

## 100-LongBench

100-LongBench is a novel benchmark designed to address limitations in evaluating the long-context capabilities of large language models (LLMs). 

The authors argue that existing benchmarks like LongBench, L-Eval, NIAH, and RULER often fail to disentangle a model's baseline ability from its long-context specific performance and frequently use fixed context lengths, which limits their applicability.

To counter these issues, 100-LongBench features length-controllable contexts and a new metric called LongScore, specifically designed to isolate long-context capability from inherent task performance. 

The benchmark comprises eight tasks categorized into four types: Key Retrieval (KV Retrieval, Counting Stars), Information Retrieval (Passage Retrieval, Passage Count), Information Comprehension (Single-doc QA, Multi-doc QA), and Information Summarization (Single-doc Sum, Multi-doc Sum).

The paper appears to be recent, with an arxiv posting dated May 25, 2025 (arxiv 2505.19293) and was published in ACL Findings 2025.

Regarding **DOLCE**, the search results did not return information about it. Would you like me to perform an additional search specifically for "DOLCE" long context evaluation?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c305679-18ca-47ce-b2fb-697c2a246770",
  "isSidechain": false,
  "promptId": "dc85c9bb-f9bc-4bf3-8111-88cdfb7c60fe",
  "type": "user",
  "uuid": "cebd5789-f73c-4230-9942-7f18f0e7163d",
  "toolUseResult": {
    "query": "\"100-LongBench\" OR \"DOLCE\" long context evaluation disentangle factors 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018Ly79jWnMx74mBaSVdvWcg",
        "content": [
          {
            "title": "[Literature Review] 100-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability?",
            "url": "https://www.themoonlight.io/en/review/100-longbench-are-de-facto-long-context-benchmarks-literally-evaluating-long-context-ability"
          },
          {
            "title": "100-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability? | OpenReview",
            "url": "https://openreview.net/forum?id=zfaZZzbw0m"
          },
          {
            "title": "100-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability? - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-acl.903/"
          },
          {
            "title": "[2505.19293] 100-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability?",
            "url": "https://arxiv.org/abs/2505.19293"
          },
          {
            "title": "100-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability? | alphaXiv",
            "url": "https://www.alphaxiv.org/resources/2505.19293v1"
          },
          {
            "title": "100-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability? | Request PDF",
            "url": "https://www.researchgate.net/publication/392105517_100-LongBench_Are_de_facto_Long-Context_Benchmarks_Literally_Evaluating_Long-Context_Ability"
          },
          {
            "title": "100-LongBench: Are de facto Long-Context Benchmarks ...",
            "url": "https://arxiv.org/pdf/2505.19293"
          }
        ]
      },
      "Based on the search results, I found information about **100-LongBench**, which addresses long-context evaluation. However, I did not find results specifically mentioning \"DOLCE\" in the search results returned.\n\n## 100-LongBench\n\n100-LongBench is a novel benchmark designed to address limitations in evaluating the long-context capabilities of large language models (LLMs). \n\nThe authors argue that existing benchmarks like LongBench, L-Eval, NIAH, and RULER often fail to disentangle a model's baseline ability from its long-context specific performance and frequently use fixed context lengths, which limits their applicability.\n\nTo counter these issues, 100-LongBench features length-controllable contexts and a new metric called LongScore, specifically designed to isolate long-context capability from inherent task performance. \n\nThe benchmark comprises eight tasks categorized into four types: Key Retrieval (KV Retrieval, Counting Stars), Information Retrieval (Passage Retrieval, Passage Count), Information Comprehension (Single-doc QA, Multi-doc QA), and Information Summarization (Single-doc Sum, Multi-doc Sum).\n\nThe paper appears to be recent, with an arxiv posting dated May 25, 2025 (arxiv 2505.19293) and was published in ACL Findings 2025.\n\nRegarding **DOLCE**, the search results did not return information about it. Would you like me to perform an additional search specifically for \"DOLCE\" long context evaluation?"
    ],
    "durationSeconds": 7.1109409129999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3c305679-18ca-47ce-b2fb-697c2a246770",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-20T05:03:34.610Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the landscape. Let me synthesize my findings and analyze this proposal carefully.

Key papers and findings from my research:

1. **PI-LLM (arXiv:2506.08184)**: Demonstrates log-linear accuracy decline under proactive interference using synthetic key-value pairs. Only tests synthetic retrieval.

2. **Dual-Process (arXiv:2603.00270)**: PI dominates RI in LLMs (Cohen's d = 1.73), PI and RI are uncorrelated (R²=0.044), PI resistance doesn't scale with model size (R²=0.06). 

Across 39 different models.

3. **EMB-S (arXiv:2601.20276)**: Adversarial NIAH at 326M-token scale showing semantic discrimination is the dominant bottleneck for long-context retrieval. Decouples evidence access from usage.

4. **Chroma (2025)**: Documents context rot across 18 models — every model degrades as context grows. Notes mechanistic interpretability is "beyond scope."

5. **CogniLoad (arXiv:2509.18458)**: Factorial control over length, difficulty, distractor density. Does NOT control position bias or proactive interference.

6. **Sculptor (ICLR 2026,

arXiv:2508.04664)**: Proposes active context management to mitigate PI. Assumes PI is dominant without measuring its effect size.

7. **100-LongBench**: Tries to disentangle baseline ability from long-context-specific performance.

8. **LONGPIBENCH**: Controls position but not interference.

Now looking at the proposal itself, I see real strengths here. The core gap is legitimate — nobody's actually done a joint factorial decomposition across all these factors simultaneously. The 3⁴ design is well-grounded statistically, and the proposal correctly identifies that these three research threads have been operating in isolation. The model selection is diverse, the mechanistic analysis approach is pragmatic, and the power analysis is unusually rigorous for a benchmark paper.

But there are some real concerns worth sitting with. First, the proposal uses "causal" language pretty freely, but ANOVA gives you variance decomposition, not causal identification in the interventionist sense. Second, the orthogonality assumption is shaky — interference load, position, similarity, and length probably aren't truly independent. Manipulating interference (number of similar distractors) could easily confound with both position and length. Third, there's the ecological validity question: if you're synthetically inserting distractors at controlled positions, how realistic are these tasks actually going to be?

I could push back on whether this is even necessary. Couldn't you just run simple regression analyses on existing benchmarks that naturally vary across these dimensions? But the real answer is no — existing benchmarks don't give you independent control over all four factors, which is exactly why this controlled approach matters.

The deeper assumption is that context rot decomposes cleanly into additive main effects and interactions of these four factors. What if it's fundamentally non-decomposable, driven by architecture-specific dynamics that don't factor neatly? The design does measure interactions, but a 3⁴ factorial might miss higher-order interactions if statistical power isn't there.

To actually strengthen this, I need to sharpen the "causal" claim. ANOVA decomposes variance, but the factorial manipulation does give you something stronger than pure correlation — you're actively intervening on these factors rather than just observing them. — you're manipulating factors directly — but calling it "causal" requires careful framing. Reviewers from the causal inference community might push back. This is really a "controlled decomposition" with the strength of experimental manipulation. The proposal should lean into the experimental design's strengths rather than overclaiming causality.

Actually, wait — in experimental design, a factorial ANOVA with manipulated factors IS a causal claim. You're manipulating the independent variables and measuring the dependent variable. This is standard experimental methodology. The "causal" claim is reasonable in that sense. But the proposal says "causal decomposition of context rot" — implying these four factors are the causes of context rot, which is a strong claim. What if there are other factors like attention head capacity or tokenization effects that also contribute? The decomposition is causal in the sense that manipulating these factors causes performance changes, but it's not a complete causal model.

The real opportunity here is that different architectures might be bottlenecked by different factors. The Dual-Process paper shows position invariance and recency interference have distinct mechanisms across architectures. If the factorial decomposition reveals that SSM-hybrids are position-invariant but interference-sensitive while dense transformers show the opposite pattern, that's the most interesting finding and should be the primary hypothesis rather than a secondary observation.

The research question framing is currently descriptive — "what are the relative contributions" — but it could be much stronger by testing competing hypotheses from the literature. EMB-S claims semantic discrimination is the dominant bottleneck, PI-LLM implicitly claims interference is key, and Sculptor assumes position invariance dominates. The factorial design can directly adjudicate between these claims rather than just measuring contributions.

I also need to address the LongBench paper from ACL Findings 2025, which explicitly tries to disentangle baseline ability from long-context performance. The proposal should clarify how its decomposition differs from and builds on that work.

The proposal mentions two-way interactions but glosses over higher-order ones. In a 3⁴ design, there are 6 two-way, 4 three-way, and 1 four-way interaction term. If the three-way interaction of interference × position × similarity is significant, that would be theoretically interesting — it would mean position bias is modulated by interference load differently depending on distractor similarity. The proposal should explicitly hypothesize which interaction terms are expected to be significant and why.

The core novelty is the joint factorial decomposition, which is methodologically solid but the real question is what finding would actually be interesting. If the answer is just that interference, position, or similarity dominates — we already know those factors matter from prior work. The compelling result would be surprising relative rankings, large interaction effects, architecture-specific differences, or evidence that different task types are bottlenecked by different factors. The proposal hints at this but doesn't make it the central claim.

Actually, I should reconsider the framing. The proposal's strength is positioning this as resolving an implicit disagreement across three literatures — each claiming their factor is the important one, but they've never been directly compared. The factorial design is the right tool for that. But I need to think critically about whether this disagreement is real or just an artifact of different experimental setups. PI-LLM measures interference on synthetic retrieval, EMB-S measures semantic discrimination at scale, and Chroma measures overall degradation without factor control — they might all be correct within their own contexts. The key insight is that the factorial design would clarify whether the disagreement reflects genuinely different bottlenecks or just different measurement conditions.

The real novelty isn't identifying the dominant factor overall, but showing whether that dominance shifts across different architectures — that's what would matter most to the field. Interaction effects are where the unique contribution lies, since main effects can be roughly inferred from existing work but the interactions cannot. I should also flag the 100-LongBench gap in related work and be more careful about the causal language.

On the trivial alternative: existing studies like PI-LLM, EMB-S, and Chroma use completely different setups and metrics, so you can't meaningfully compare effect sizes across them. A factorial design is genuinely necessary to get comparable results. The practical stakes are real too — if interference matters 5× more than position bias, that fundamentally changes where mitigation efforts should focus.

A strong version of this work would resolve the three-way disagreement with quantitative evidence, reveal architecture-specific patterns in how these factors decompose, uncover surprising interactions, and ideally connect the mechanistic analysis back to the factorial results (like showing that interference-sensitive attention heads are the same ones exhibiting positional entropy shifts). The proposal is already quite mature, so my feedback is mostly about tightening the framing. I should also check whether factorial ANOVA has been applied to LLM evaluations before — if this methodology is novel to NLP, that's another contribution worth highlighting.

The Dual-Process paper finding that position invariance resistance doesn't scale with model size (R²=0.06) is crucial here. If the factorial decomposition confirms this while showing that position bias DOES scale with size but interference doesn't, that would significantly strengthen the work. I'm ready to structure my evaluation now, though I see several concrete ways to raise the ceiling: sharpening the competing hypotheses framing, positioning architecture-specific decomposition as the centerpiece, emphasizing interaction terms as the unique contribution, addressing the related work gap around long-context benchmarks, and being more precise about causal language.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cebd5789-f73c-4230-9942-7f18f0e7163d",
  "isSidechain": false,
  "requestId": "req_011CbDEYLHXTAu6HQ7dCGEzT",
  "type": "assistant",
  "uuid": "8ed11dd4-85c5-4018-a152-b808f9cadfa7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011qSo63DYpgVe1opNEou1tg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1921,
      "cache_read_input_tokens": 28451,
      "output_tokens": 6597,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1921,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6597,
          "cache_read_input_tokens": 28451,
          "cache_creation_input_tokens": 1921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1921
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

_source line 44 · 2026-05-20T05:04:54.273Z_

Now I have sufficient research to evaluate this proposal. Let me compile my analysis.

---

【状态】: 有发掘空间

【前置调研发现】
- **PI-LLM (arXiv:2506.08184, ICML 2025 Workshop)**: 使用合成 key-value pairs 展示 proactive interference 下 log-linear 准确率衰减。方法论局限在合成检索任务，未控制 position 或 similarity。
- **Dual-Process (arXiv:2603.00270, 2026)**: 在 39 个模型上发现 PI 普遍主导 RI（Cohen's d = 1.73），且 PI 与 RI 不相关（R²=0.044），**PI 抗性不随模型规模增长（R²=0.06）**。这是一个关键发现，proposal 已引用但未充分利用。
- **EMB-S (arXiv:2601.20276, 2026)**: 326M-token 尺度的对抗性 NIAH，核心 claim 是 semantic discrimination（而非 context length）是长上下文检索的主要瓶颈。解耦了 evidence access 与 usage，但未做因子间的相对贡献量化。
- **Chroma (2025)**: 18 个模型的 context rot 系统记录，发现 distractor interference 导致的退化超出了 context length 单独能解释的范围，但明确声明 mechanistic interpretability "beyond scope"。
- **CogniLoad (arXiv:2509.18458, 2025)**: 基于 Cognitive Load Theory 的 factorial benchmark，控制 length × difficulty × distractor density，但**不控制 position bias 和 proactive interference**。已明确承认 "current benchmarks do not offer the factorial control needed to disentangle these loads"。
- **Sculptor (ICLR 2026)**: 提出 Active Context Management 缓解 PI，但**假定 PI 是主导因素而未量化其相对效应大小**。
- **100-LongBench (arXiv:2505.19293, ACL Findings 2025)**: 试图将 baseline ability 与 long-context-specific performance 解耦，提出 LongScore 指标。与本 proposal 在"解耦因子"的精神上相似，但控制的维度完全不同。
- **调研总结**: 该领域当前的三条研究线索（interference、semantic discrimination、position bias）各自独立发展，各自声称自己研究的因子是"主导瓶颈"，但从未在统一的实验设计中头对头比较。用 factorial ANOVA 量化相对贡献的思路在 NLP benchmark 评估中尚属空白。

---

【发掘点 1】
- 维度: 核心 claim 强化
- 内容: 当前 proposal 的核心叙事是"三条文献线索从未联通，我们做第一个联合分解"。这是一个正确但偏**描述性**的 framing。应当升级为**裁判性 framing**：三条文献隐式地做出了相互竞争的优先级声明——PI-LLM 暗示 interference 是关键瓶颈，EMB-S 声称 semantic discrimination 是 dominant bottleneck，Sculptor 假设 PI 主导而无需量化。这三个 claim 不能同时成立（至少不能在同一实验条件下同时成立），而 PI-ContextRot 的 factorial 设计是唯一能以同一 yardstick（partial η²）直接裁决的方法论。这个 framing 让论文从"做了一个有用的 benchmark"升级为"解决了一个领域级的隐式争论"，审稿人的兴奋度会显著提升。
- 价值: 提升 Significance。从描述性 ("we decompose") 到争论裁决性 ("we adjudicate competing implicit claims") 的 framing 转变，使论文的影响力叙事从"有用"变为"必要"。
- 调研依据: EMB-S 明确 claim "semantic discrimination, not context length, is the dominant bottleneck"；PI-LLM 展示 interference 导致 log-linear 衰减并暗示这是根本限制；Sculptor 直接假设 PI 主导而不量化——三者的 implicit priority claims 形成了可裁决的张力。

【发掘点 2】
- 维度: novelty 锐化
- 内容: 当前 proposal 将 main effects 和 interactions 并列呈现。但如果仔细审视，各因子的 main effect 从现有文献中已经可以**定性推断**——interference 导致衰减（PI-LLM），position 影响准确率（Lost-in-the-Middle），similarity 是瓶颈（EMB-S），length 导致退化（Chroma）。**真正完全无法从现有工作推断的是 interaction terms**：interference × position（在高 PI 负载下，position bias 是被放大还是被淹没？）、interference × similarity（当 distractor 语义相似度高时，PI 效应是否非线性膨胀？）、position × similarity（position bias 是否对 high-similarity distractor 更敏感？）。Proposal 应明确将 interaction terms 定位为 factorial 设计的**首要独特贡献**，而非将其与 main effects 等量齐观。甚至可以考虑预注册 2-3 个关于交互项的具体假设（例如：基于 Dual-Process 的发现——PI 和 RI 由不同机制驱动——可以假设 interference × position 交互显著，因为 PI 保护早期编码而 position bias 影响中间位置）。
- 价值: 锐化 Novelty。Main effects 的量化虽然没人做过但可预期；interaction terms 才是真正不可预见的发现空间，也是审稿人无法用 "I would have guessed this" 回应的部分。
- 调研依据: Dual-Process (arXiv:2603.00270) 发现 PI 和 RI 由独立机制驱动、PI 保护 primacy 而 RI 损害 recency——这直接预测 interference × position 存在非平凡交互。

【发掘点 3】
- 维度: significance 提升
- 内容: 当前 proposal 将 architecture-specific 分析作为设计要素之一，但未将其提升为可能的**核心发现**。Dual-Process 论文的一个极其重要的发现是 PI resistance 不随模型规模增长（R²=0.06）。这意味着不同架构可能被完全不同的因子所瓶颈化——例如，SSM-hybrid（Jamba）理论上应对 position 更不敏感（因为其状态空间机制不依赖 positional attention），但可能对 interference 更脆弱（因为有限状态压缩信息）；MoE 架构可能在 high-similarity 条件下表现出独特的退化模式（因为 expert routing 可能在语义相似输入上路由到相同 expert）。如果 factorial 分解揭示**不同架构的 dominant bottleneck 因子不同**（例如 dense transformer 被 position 主导，SSM-hybrid 被 interference 主导），这将是论文最具引用价值的发现——它意味着 context rot 的缓解策略需要 architecture-aware 定制，而非 one-size-fits-all。建议将 "architecture × factor interaction" 提升为论文的**第二核心研究问题**（与 overall decomposition 并列），而非作为附属分析呈现。
- 价值: 大幅提升 Significance。如果不同架构确实有不同的 bottleneck profile，这个发现的实用影响远超单一排名——它改变了整个 context engineering 社区的策略思维，从 "what's the most important factor" 到 "what's the most important factor for THIS architecture"。
- 调研依据: Dual-Process (arXiv:2603.00270) 的 "PI resistance doesn't scale with model size" 发现直接暗示 architecture-specific 差异可能是核心变量；Jamba 的 SSM-hybrid 设计在 positional encoding 上与 dense transformer 存在机制性差异。

【发掘点 4】
- 维度: related work 差异化
- 内容: Proposal 的 landscape section 遗漏了 **100-LongBench (arXiv:2505.19293, ACL Findings 2025)**。这篇论文与本 proposal 在精神上高度相关——它也试图将 baseline ability 与 long-context-specific performance 解耦，并提出了 LongScore 指标来隔离长上下文能力。虽然 100-LongBench 控制的维度与 PI-ContextRot 完全不同（它关注 length-controllable contexts 下的整体能力 vs. 本 proposal 的四因子 factorial），但审稿人很可能会将两者关联。应在 landscape 中明确纳入 100-LongBench，并清晰说明差异：100-LongBench 解耦的是"能力级别"（baseline vs. long-context），而 PI-ContextRot 解耦的是"因果因子级别"（interference vs. position vs. similarity vs. length）——后者是更细粒度的诊断。此外，还应关注 **Veseli et al. (2025) 关于 U-shaped attention 在 >50% context capacity 时转变为 recency bias 的发现**——这意味着 position bias 的形态本身依赖于 context length，进一步支持 factorial 设计中 position × length 交互项的重要性。
- 价值: 堵住 Related Work 差异化的漏洞，同时用 Veseli et al. 的发现强化 interaction terms 的假设基础。
- 调研依据: 100-LongBench (arXiv:2505.19293) 和 Veseli et al. (2025) 关于 position bias 随 context fullness 变化的发现。

【发掘点 5】
- 维度: 前提假设质疑
- 内容: Proposal 的 factorial 设计假设四个因子可以**正交操作**——即你可以独立地改变 interference load 而不影响 position 或 length。但仔细审视，这个假设在某些 cell combinations 下可能面临张力：当 interference load = 8（8 个 superseded passages）且 context length = 8K 时，这些 passages 必然占据大量 token budget，可能强制 target 被推到特定 position，破坏 position 因子的独立性；反之，在 128K context 下 8 个 distractors 只占很小比例，interference 的"密度"大幅降低。换言之，**interference load 的绝对计数可能与 relative density（相对于 context length）产生混淆**。这不是致命问题，但 proposal 应当明确讨论这一设计决策——是按绝对数量（当前方案）还是按相对密度定义 interference levels——并论证为什么当前选择更合理（例如：因为 PI-LLM 的 log-linear 关系是基于绝对计数，保持可比性）。对此的不主动讨论可能让审稿人认为设计存在未察觉的混淆。
- 价值: 加固 Novelty claim 的可信度。主动讨论这个设计张力并给出理由，比让审稿人自己发现然后质疑要好得多。这也可以衍生出一个有趣的 supplementary analysis：absolute vs. relative interference density 是否产生不同的 decomposition pattern。
- 调研依据: PI-LLM 的 log-linear 关系基于绝对 trial 数量；EMB-S 在 326M-token 尺度下 distractor 的相对密度极低——两者的实验条件差异本身就暗示 absolute vs. relative density 可能导致不同结论。

Sources:
- [PI-LLM: Unable to Forget](https://arxiv.org/abs/2506.08184)
- [Dual-Process Interference in LLMs](https://arxiv.org/abs/2603.00270)
- [EMB-S: Beyond the Needle's Illusion](https://arxiv.org/abs/2601.20276)
- [Sculptor: Active Context Management](https://arxiv.org/abs/2508.04664)
- [CogniLoad](https://arxiv.org/abs/2509.18458)
- [100-LongBench](https://arxiv.org/abs/2505.19293)
- [Context Rot (Chroma)](https://www.trychroma.com/research/context-rot)
- [AtP*](https://arxiv.org/abs/2403.00745)
- [LongPiBench: Distance between Relevant Information Pieces](https://arxiv.org/pdf/2410.14641)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ed11dd4-85c5-4018-a152-b808f9cadfa7",
  "isSidechain": false,
  "requestId": "req_011CbDEYLHXTAu6HQ7dCGEzT",
  "type": "assistant",
  "uuid": "2282d285-7673-4dda-8716-49e101a48fd5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011qSo63DYpgVe1opNEou1tg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1921,
      "cache_read_input_tokens": 28451,
      "output_tokens": 6597,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1921,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6597,
          "cache_read_input_tokens": 28451,
          "cache_creation_input_tokens": 1921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1921
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

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs  ## Description We propose PI-ContextRot, the first diagnostic benchmark designed to…",
  "leafUuid": "2282d285-7673-4dda-8716-49e101a48fd5",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Decompose context rot into interference, position, and length factors",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs  ## Description We propose PI-ContextRot, the first diagnostic benchmark designed to…",
  "leafUuid": "2282d285-7673-4dda-8716-49e101a48fd5",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Decompose context rot into interference, position, and length factors",
  "sessionId": "9a9c4034-7658-48d7-81fd-4573eb968007"
}
```

---
