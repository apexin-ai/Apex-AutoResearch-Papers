# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Decomposing Context Rot: A Factor

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/f70f628b-ffed-44b3-abc1-73f1329e1f54.jsonl`
- **Structured JSON:** [`e5e77b38076964a6d627.json`](../../sessions/e5/e5e77b38076964a6d627.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:53:40.058Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:53:40.058Z",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs\n\n## Description\nWe propose PI-ContextRot, the first diagnostic benchmark designed to causally decompose context rot — the well-documented degradation of LLM performance as input context grows — into its constituent factors: proactive interference, position bias, semantic distractor similarity, and raw length. While Chroma (2025) documented context rot across 18 models, PI-LLM (2025) demonstrated log-linear accuracy collapse under synthetic interference, and EMB-S (2026) showed semantic discrimination is the dominant bottleneck for long-context retrieval, these threads remain disconnected: no work has measured the relative contribution of each factor to realistic task degradation. Our balanced 3⁴ factorial design (3 interference levels × 3 positions × 3 similarity levels × 3 context lengths = 81 cells, 35 instances per cell per task, 8,505 total instances across multi-document QA, entity tracking, and temporal reasoning) is formally powered (≥0.95 for medium effects, ≥0.80 for small effects on two-way interactions). Evaluating 12 models across dense (Qwen3.5-9B/27B), MoE (Llama-4-Scout, Qwen3.5-122B-A10B, DeepSeek-V4-Flash), SSM-hybrid (Jamba-1.5-Mini/Large), and frontier API architectures (GPT-4.1, Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini 2.5 Pro, Qwen3.5-397B-A17B), we report partial η² effect sizes quantifying each factor's contribution and their interactions. A tiered mechanistic analysis — attention entropy on all open-weight models plus attribution patching (AtP*) on dense models ≤27B — identifies the causal circuits underlying each factor. This decomposition directly informs practical context engineering: the effect-size rankings reveal whether mitigation efforts should prioritize interference-aware retrieval (as Sculptor assumes), position debiasing, or length management, resolving an implicit disagreement across the three literatures.\n\n## Core Problem\nWhat are the relative contributions of proactive interference, position bias, semantic distractor similarity, and raw context length to observed context rot in LLMs, and how do these factors interact across dense, MoE, and SSM-hybrid architectures?\n\n## Opportunity\nThree active research threads have developed independently: the context rot literature (Chroma 2025, documenting non-uniform degradation across 18 models), the proactive interference literature (PI-LLM arXiv:2506.08184, showing log-linear accuracy decline; Dual-Process arXiv:2603.00270, showing PI dominates over RI in LLMs opposite to humans), and the semantic interference literature (EMB-S arXiv:2601.20276, showing semantic discrimination — not context length — is the dominant bottleneck for long-context retrieval at 326M-token scale). These threads have never been connected into a unified quantitative decomposition. PI-LLM uses only synthetic key-value pairs; Chroma documents degradation without controlling for interference; EMB-S decouples access from usage but does not measure the relative contribution of PI versus position versus length; Sculptor (ICLR 2026) proposes active context management to mitigate PI but does not quantify PI's share of overall degradation. A hypothesis-neutral factorial study — measuring each factor's contribution via ANOVA with effect sizes — would provide the first causal decomposition of context rot into component factors, informing whether mitigation efforts should prioritize interference-aware retrieval, position debiasing, or length management.\n\n## Landscape\nChroma Research (2025) systematically documented context rot across 18 models but noted that 'investigating mechanistic interpretability is beyond scope.' PI-LLM (arXiv:2506.08184) demonstrated log-linear retrieval accuracy decline under proactive interference but only tested synthetic key-value retrieval. The Dual-Process paper (arXiv:2603.00270) found PI and RI are uncorrelated (R²=0.044) with distinct mechanisms across 39 models, and crucially that PI resistance doesn't scale with model size (R²=0.06). EMB-S (arXiv:2601.20276) introduced adversarial NIAH with collision-tested near-miss hard negatives at 326M-token scale, decoupling evidence access from usage under semantic interference — but measures access degradation rather than decomposing the contributing factors. CogniLoad (arXiv:2509.18458) provides factorial control over length, difficulty, and distractor density but NOT position bias or proactive interference load. LONGPIBENCH controls position but not interference. Sculptor (arXiv:2508.04664, ICLR 2026) proposes active context management tools to mitigate PI but does not quantify PI's relative contribution to overall degradation — it assumes PI is the dominant problem without measuring its effect size against position bias or raw length. The noise decomposition framework of 'When Does Divide and Conquer Work' (arXiv:2506.16411, ICLR 2026) decomposes long-context failures into task/model/aggregator noise for chunking strategies but does not manipulate interference or position as controlled factors. Concurrent work update (May 2026): LongMINT (arXiv:2605.18565) evaluates memory under multi-target interference in long-horizon agent systems but focuses on agent memory architectures. Cross-Component Interference (arXiv:2605.05716) demonstrates context-window crowding in LLM agent scaffolding via a full factorial experiment, but manipulates scaffolding components (planning, tools, memory) rather than the interference-position-similarity-length factors we target. SleepGate (arXiv:2603.14517) proposes a KV-cache consolidation mechanism for resolving PI but addresses mitigation rather than diagnosis. Intelligence Degradation (arXiv:2601.15300) identifies critical context-length thresholds via natural length distribution analysis but does not control for interference or semantic similarity. No existing work performs a joint factorial decomposition of context rot into interference, position, similarity, and length components with effect sizes on realistic NLP tasks across multiple architectures.\n\n## Approach\nConstruct PI-ContextRot, a diagnostic benchmark with factorial control over four orthogonal factors in a balanced 3⁴ design: (1) proactive interference load — number of semantically similar but superseded passages preceding the target (0/3/8 levels, spanning from no interference through moderate to severe based on PI-LLM's log-linear curve), (2) target information position (early/middle/late tercile), (3) semantic similarity between distractors and target (low/medium/high, controlled via embedding cosine similarity using BGE-M3 with validated thresholds at cosine <0.3, 0.5–0.7, and >0.85), and (4) context length (8K/32K/128K tokens). The 81-cell design generates 8,505 instances (35 per cell × 3 realistic NLP task types: multi-document QA, entity state tracking, temporal reasoning over news articles), sourcing base documents from Wikipedia and CommonCrawl-News. Formal power analysis (G*Power, F-test family, fixed-effects ANOVA) confirms ≥0.95 power for detecting medium effects (partial η² ≥ 0.06, Cohen's f = 0.253) on all main effects and two-way interactions, and ≥0.80 power for small effects (partial η² ≥ 0.01, f = 0.100) on two-way interactions, at α = 0.05 with n = 35 per cell per task (N_task = 2,835). Evaluate 12 models spanning three architecture families and three scale tiers: dense transformers (Qwen3.5-9B, Qwen3.5-27B), MoE architectures (Llama-4-Scout-17B-16E, Qwen3.5-122B-A10B, DeepSeek-V4-Flash), SSM hybrids (Jamba-1.5-Mini, Jamba-1.5-Large), and frontier APIs (GPT-4.1, Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini 2.5 Pro, Qwen3.5-397B-A17B). Run a full-factorial ANOVA reporting partial η² effect sizes for each factor and all two-way interactions, with Bonferroni-corrected post-hoc contrasts, providing the first quantitative decomposition of context rot into component causes. Supplement with a tiered mechanistic analysis: (a) attention entropy measurement across all open-weight models (forward-pass only, O(1) overhead per inference, following the HEAD-ENTROPY methodology for identifying correctness-predictive attention patterns), and (b) attribution patching via AtP* (gradient-based approximation requiring only 2 forward + 1 backward pass, computationally tractable) on dense models ≤27B (Qwen3.5-9B, Qwen3.5-27B) to identify interference-sensitive versus position-sensitive attention heads. This tiered strategy replaces the original activation patching plan, which is computationally prohibitive on MoE models (cost scales linearly in the number of model components, requiring millions of forward passes on 100B+ parameter models).\n\n## Resource Estimate\n{'manual': {'gpu_hours': '1,000–1,300 (inference on 7 open-weight models across 8,505 instances at up to 128K context; large MoE/SSM models on 4–8×H100 nodes; AtP* probing on 2 dense models adds ~150 hrs; attention entropy adds ~50 hrs)', 'timeline': '12–14 weeks (2 wks benchmark construction with power-analysis validation, 4.5 wks inference runs, 2.5 wks mechanistic analysis, 3 wks writing)', 'estimated_gpu_cost': '$2,500–$4,000 at $2–3/H100-hr (Lambda Labs $2.99/hr, RunPod $1.99–$2.39/hr; market range $1.49–$6.98/hr depending on provider and commitment)', 'api_model_cost': '$400–$600 (8,505 instances × 5 API models at varying context lengths)'}, 'human_in_loop': {'gpu_hours': '650–850 (Claude handles data generation QA, similarity filtering via BGE-M3, and statistical analysis pipeline; human designs experiments and interprets mechanistic probes)', 'timeline': '8–10 weeks (1.5 wks benchmark construction with Claude-assisted template generation and power-analysis validation, 3 wks inference, 2 wks analysis, 2 wks writing)', 'claude_api_cost': '$500–$700 (data generation with quality verification: ~$200 for 8,505 instances at Sonnet 4.6 rates; similarity computation and filtering: ~$100; statistical analysis pipeline: ~$150; writing assistance: ~$250)', 'estimated_gpu_cost': '$1,600–$2,600', 'api_model_cost': '$400–$600'}, 'auto_research': {'gpu_hours': '1,300–1,700 (full 12-model evaluation including parallel sweeps across all 81 factorial cells; automated AtP* pipeline; attention entropy computation)', 'timeline': '4–6 weeks (parallelized benchmark generation and inference; automated statistical pipeline; human review at checkpoints)', 'claude_api_cost': '$900–$1,300 (benchmark generation with multi-pass verification: ~$350; orchestration and analysis: ~$400; draft generation and iteration: ~$350; quality assurance: ~$200)', 'estimated_gpu_cost': '$3,250–$5,100', 'api_model_cost': '$500–$800 (5 API models × 8,505 instances with retries)', 'speed_bottleneck': 'Sequential evaluation of large models at 128K context — DeepSeek-V4-Flash (284B, 4–8×H100) and Jamba-1.5-Large (398B total, 4–8×H100) at ~60–120 sec per 128K inference; 8,505 instances × 2 large models at 8× parallelism ≈ 300–500 GPU-hours that cannot be further distributed without additional nodes'}}\n\n## Inspired By\nField guide Section 3 (Context Rot) + Section 6 (Reasoning vs Retrieval) + the disconnect between PI-LLM's interference findings, EMB-S's semantic discrimination findings, and Chroma's context rot characterization + CogniLoad's explicit acknowledgment that 'current benchmarks do not offer the factorial control needed to disentangle these loads' + Sculptor's implicit assumption that PI is dominant without quantification\n\n## Target Venues\n- AAAI 2027 (abstract: July 21, 2026 AoE; full paper: July 28, 2026 AoE — primary target, 9 weeks from today; supplementary/code: July 31, 2026)\n- NeurIPS 2026 Workshops (suggested paper deadline: August 29, 2026 AoE — ideal for preliminary results or workshop-length version with subset of models)\n- ICLR 2027 (estimated submission: September–October 2026 — ample time for full study with complete mechanistic analysis across all architectures)\n- ACL 2027 via ARR (estimated ARR cycle: October–November 2026 — backup venue if additional experiments or reviewer-requested analyses extend the timeline)\n\n## Key References\n- Context Rot: Evaluating LLM Performance Degradation with Increasing Input Tokens (Chroma Research 2025)\n- Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length (arXiv 2025, Wang et al., arXiv:2506.08184)\n- Transformers Remember First, Forget Last: Dual-Process Interference in LLMs (arXiv 2026, Chattaraj & Raj, arXiv:2603.00270)\n- Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale (arXiv 2026, EMB-S, arXiv:2601.20276)\n- Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management (ICLR 2026, arXiv:2508.04664)\n- CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density (arXiv 2025, Kaiser et al., arXiv:2509.18458)\n- Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs (arXiv 2024, LongPiBench)\n- When Does Divide and Conquer Work for Long Context LLM? A Noise Decomposition Framework (ICLR 2026, arXiv:2506.16411)\n- AtP*: An Efficient and Scalable Method for Localizing LLM Behaviour to Components (Google DeepMind, arXiv:2403.00745)\n- Learning to Forget: Sleep-Inspired Memory Consolidation for Resolving Proactive Interference in Large Language Models (arXiv 2026, Xie, arXiv:2603.14517)\n- Intelligence Degradation in Long-Context LLMs: Critical Threshold Determination via Natural Length Distribution Analysis (arXiv 2026, arXiv:2601.15300)\n- LongMINT: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems (arXiv 2026, Lee et al., arXiv:2605.18565)\n- More Is Not Always Better: Cross-Component Interference in LLM Agent Scaffolding (arXiv 2026, arXiv:2605.05716)\n- Long-Context Generalization with Sparse Attention (ICLR 2026)\n- Applying Statistics to LLM Evaluations (Wolfe 2025 — methodological reference for power analysis in LLM benchmarks)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T04:53:40.063Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:53:40.063Z",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-20T04:53:40.082Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
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
  "promptId": "815e4ab0-d5b7-4745-b32c-ddcee59276dd",
  "type": "user",
  "uuid": "84ec01ca-6a32-42a9-9c26-3516ef2e3c6f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:53:40.080Z_

```json
{
  "parentUuid": "84ec01ca-6a32-42a9-9c26-3516ef2e3c6f",
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
  "uuid": "fff01c48-e12a-4058-b3ea-5e335d42b556",
  "timestamp": "2026-05-20T04:53:40.080Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:53:40.080Z_

```json
{
  "parentUuid": "fff01c48-e12a-4058-b3ea-5e335d42b556",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fe6c6dea-3e96-4d34-8a94-d78dca852863",
  "timestamp": "2026-05-20T04:53:40.080Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs…",
  "leafUuid": "fe6c6dea-3e96-4d34-8a94-d78dca852863",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Decompose context rot factors in LLMs via factorial analysis",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:53:45.293Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for EMNLP 2026 submission potential. I need to follow the rubric carefully:

1. First, do 3-5 WebSearch queries to understand the field
2. Then evaluate Novelty, Significance, and Related Work
3. Answer the Trivial Alternative and Premise Assumption checks
4. Give probability estimate

Let me start by loading the WebSearch tool and doing my research.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe6c6dea-3e96-4d34-8a94-d78dca852863",
  "isSidechain": false,
  "requestId": "req_011CbDDtHigXgFbpZUxEybiG",
  "type": "assistant",
  "uuid": "41c7c3e5-e6ff-4668-96a5-749b8ee6b8ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwczCbS4X8Jos9v82vBk7T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5353,
      "cache_read_input_tokens": 14333,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5353,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 191,
          "cache_read_input_tokens": 14333,
          "cache_creation_input_tokens": 5353,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5353
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

_source line 9 · 2026-05-20T04:53:45.479Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NEQQzJubNcMoQvX7kuc7C9`</summary>

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
  "parentUuid": "41c7c3e5-e6ff-4668-96a5-749b8ee6b8ed",
  "isSidechain": false,
  "requestId": "req_011CbDDtHigXgFbpZUxEybiG",
  "type": "assistant",
  "uuid": "e3b5c177-2e08-4d7c-b558-d2a57e524625",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwczCbS4X8Jos9v82vBk7T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5353,
      "cache_read_input_tokens": 14333,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5353,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 191,
          "cache_read_input_tokens": 14333,
          "cache_creation_input_tokens": 5353,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5353
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

_source line 10 · 2026-05-20T04:53:45.486Z_

<details><summary>↩ Tool result · `toolu_01NEQQzJubNcMoQvX7kuc7C9`</summary>

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
  "parentUuid": "e3b5c177-2e08-4d7c-b558-d2a57e524625",
  "isSidechain": false,
  "promptId": "815e4ab0-d5b7-4745-b32c-ddcee59276dd",
  "type": "user",
  "uuid": "4917a504-f4ad-4e8d-baa6-8601e5820149",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "e3b5c177-2e08-4d7c-b558-d2a57e524625",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T04:53:48.268Z_

Now let me conduct the required field research with 5 targeted searches before making any evaluation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4917a504-f4ad-4e8d-baa6-8601e5820149",
  "isSidechain": false,
  "requestId": "req_011CbDDtgpjzUAgh7qzdibtg",
  "type": "assistant",
  "uuid": "546e087e-99ed-49ea-a347-60994683369b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzSgPNxLpK1uBgLoaoj4ve",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 19686,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 197,
          "cache_read_input_tokens": 19686,
          "cache_creation_input_tokens": 718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 718
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

_source line 12 · 2026-05-20T04:53:48.748Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019AuTt8m6iN3B8mC6iofEyz`</summary>

```json
{
  "query": "proactive interference LLMs context length factorial decomposition 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "546e087e-99ed-49ea-a347-60994683369b",
  "isSidechain": false,
  "requestId": "req_011CbDDtgpjzUAgh7qzdibtg",
  "type": "assistant",
  "uuid": "6900fe43-36e5-49e9-a948-5b0122f3ce44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzSgPNxLpK1uBgLoaoj4ve",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 19686,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 197,
          "cache_read_input_tokens": 19686,
          "cache_creation_input_tokens": 718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 718
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

_source line 13 · 2026-05-20T04:53:49.221Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R1jcWPcxzFRgi5Hr3AKtqX`</summary>

```json
{
  "query": "context rot LLM benchmark degradation long context evaluation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6900fe43-36e5-49e9-a948-5b0122f3ce44",
  "isSidechain": false,
  "requestId": "req_011CbDDtgpjzUAgh7qzdibtg",
  "type": "assistant",
  "uuid": "666fcc9b-229f-4a3a-a664-cf7c8ce68953",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzSgPNxLpK1uBgLoaoj4ve",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 19686,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 197,
          "cache_read_input_tokens": 19686,
          "cache_creation_input_tokens": 718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 718
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

_source line 14 · 2026-05-20T04:53:49.684Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GKhf2z38USLKWQoN2a59nB`</summary>

```json
{
  "query": "PI-LLM proactive interference arXiv 2506.08184 working memory LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "666fcc9b-229f-4a3a-a664-cf7c8ce68953",
  "isSidechain": false,
  "requestId": "req_011CbDDtgpjzUAgh7qzdibtg",
  "type": "assistant",
  "uuid": "e21350c9-8cf2-4ef2-86e1-be1f74471cd7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzSgPNxLpK1uBgLoaoj4ve",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 19686,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 197,
          "cache_read_input_tokens": 19686,
          "cache_creation_input_tokens": 718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 718
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

_source line 15 · 2026-05-20T04:53:55.446Z_

<details><summary>↩ Tool result · `toolu_019AuTt8m6iN3B8mC6iofEyz`</summary>

```text
Web search results for query: "proactive interference LLMs context length factorial decomposition 2025 2026"

Links: [{"title":"[2506.08184v3] Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://www.arxiv.org/abs/2506.08184v3"},{"title":"[2506.08184] Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://arxiv.org/abs/2506.08184"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length | OpenReview","url":"https://openreview.net/forum?id=YUHksmL8aw"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250608184W/abstract"},{"title":"Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length | OpenReview","url":"https://openreview.net/forum?id=y8jS7mDurI"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://arxiv.org/html/2506.08184v3"},{"title":"Proactive Interference Limits LLM Working Memory","url":"https://www.emergentmind.com/papers/2506.08184"},{"title":"(PDF) Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://www.researchgate.net/publication/394362750_Sculptor_Empowering_LLMs_with_Cognitive_Agency_via_Active_Context_Management"},{"title":"Learning to Forget: Sleep-Inspired Memory Consolidation for Resolving Proactive Interference in Large Language Models","url":"https://arxiv.org/pdf/2603.14517"}]

I found several relevant results about proactive interference in LLMs and context length. Here's what the search revealed:

## Key Research Finding

Researchers have adapted the proactive interference paradigm from cognitive science to study LLMs, introducing an evaluation called PI-LLM that sequentially streams semantically related key-value updates and queries only the final values.

## Main Results

Although final values are clearly positioned just before the query, LLM retrieval accuracy declines log-linearly toward zero as interference accumulates, with errors arising from retrieving previously overwritten values. The research reveals a log-linear decline in retrieval accuracy as accumulated interference increases across models from small scales to 600B parameters.

## Significance

The PI-LLM evaluation paradigm shows that proactive interference, not context length, chiefly limits LLM memory. The study proposes the Interference Endurance Score and suggests new architectural strategies to enhance LLM memory management.

## Related Work

The search also revealed a follow-up paper exploring mitigation strategies: Sleep-inspired approaches have been proposed to reduce susceptibility to associative interference in LLMs.

Note: The original PI-LLM paper appears to have been accepted at ICML 2025 Workshop on Long Context Foundation Models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6900fe43-36e5-49e9-a948-5b0122f3ce44",
  "isSidechain": false,
  "promptId": "815e4ab0-d5b7-4745-b32c-ddcee59276dd",
  "type": "user",
  "uuid": "5ea12ad3-cab8-4bdc-96ff-6951b9c28bc1",
  "toolUseResult": {
    "query": "proactive interference LLMs context length factorial decomposition 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NLCqC27zUV4SbH6yrGWJY5",
        "content": [
          {
            "title": "[2506.08184v3] Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length",
            "url": "https://www.arxiv.org/abs/2506.08184v3"
          },
          {
            "title": "[2506.08184] Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length",
            "url": "https://arxiv.org/abs/2506.08184"
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
            "title": "Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length | OpenReview",
            "url": "https://openreview.net/forum?id=y8jS7mDurI"
          },
          {
            "title": "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length",
            "url": "https://arxiv.org/html/2506.08184v3"
          },
          {
            "title": "Proactive Interference Limits LLM Working Memory",
            "url": "https://www.emergentmind.com/papers/2506.08184"
          },
          {
            "title": "(PDF) Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://www.researchgate.net/publication/394362750_Sculptor_Empowering_LLMs_with_Cognitive_Agency_via_Active_Context_Management"
          },
          {
            "title": "Learning to Forget: Sleep-Inspired Memory Consolidation for Resolving Proactive Interference in Large Language Models",
            "url": "https://arxiv.org/pdf/2603.14517"
          }
        ]
      },
      "I found several relevant results about proactive interference in LLMs and context length. Here's what the search revealed:\n\n## Key Research Finding\n\nResearchers have adapted the proactive interference paradigm from cognitive science to study LLMs, introducing an evaluation called PI-LLM that sequentially streams semantically related key-value updates and queries only the final values.\n\n## Main Results\n\nAlthough final values are clearly positioned just before the query, LLM retrieval accuracy declines log-linearly toward zero as interference accumulates, with errors arising from retrieving previously overwritten values. The research reveals a log-linear decline in retrieval accuracy as accumulated interference increases across models from small scales to 600B parameters.\n\n## Significance\n\nThe PI-LLM evaluation paradigm shows that proactive interference, not context length, chiefly limits LLM memory. The study proposes the Interference Endurance Score and suggests new architectural strategies to enhance LLM memory management.\n\n## Related Work\n\nThe search also revealed a follow-up paper exploring mitigation strategies: Sleep-inspired approaches have been proposed to reduce susceptibility to associative interference in LLMs.\n\nNote: The original PI-LLM paper appears to have been accepted at ICML 2025 Workshop on Long Context Foundation Models."
    ],
    "durationSeconds": 6.693103863,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6900fe43-36e5-49e9-a948-5b0122f3ce44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T04:53:56.149Z_

<details><summary>↩ Tool result · `toolu_01GKhf2z38USLKWQoN2a59nB`</summary>

```text
Web search results for query: "PI-LLM proactive interference arXiv 2506.08184 working memory LLM"

Links: [{"title":"[2506.08184] Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://arxiv.org/abs/2506.08184"},{"title":"[2506.08184v3] Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://www.arxiv.org/abs/2506.08184v3"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250608184W/abstract"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://www.researchgate.net/publication/392560721_Unable_to_forget_Proactive_lnterference_Reveals_Working_Memory_Limits_in_LLMs_Beyond_Context_Length"},{"title":"Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length | OpenReview","url":"https://openreview.net/forum?id=y8jS7mDurI"},{"title":"Proactive Interference Limits LLM Working Memory","url":"https://www.emergentmind.com/papers/2506.08184"},{"title":"giantfish-fly/pi-llm · Datasets at Hugging Face","url":"https://huggingface.co/datasets/giantfish-fly/pi-llm"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in","url":"https://arxiv.org/pdf/2506.08184"},{"title":"Cog2ai/pi-llm-bench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Cog2ai/pi-llm-bench"}]

I found the research paper you're looking for! Here are the key findings:

## Overview

PI-LLM is an evaluation that sequentially streams semantically related key-value updates and queries only the final values. The paper is titled "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length."

## Main Results

The research adapts the proactive interference (PI) paradigm from cognitive science, where earlier information disrupts recall of newer updates. Although these final values are clearly positioned just before the query, LLM retrieval accuracy declines log-linearly toward zero as interference accumulates; errors arise from retrieving previously overwritten values.

## Implications

LLM retrieval accuracy declines log-linearly toward zero as interference accumulates, and these findings reveal a fundamental constraint on LLMs' ability to disentangle interference and flexibly manipulate information, suggesting a working memory bottleneck beyond mere context access.

Attempts to mitigate interference via prompt engineering (e.g., instructing models to ignore earlier input) yield limited success.

## Authors and Publication

The paper was authored by Chupei Wang (University of Virginia) and Jiaqiu Vince Sun (New York University) and was accepted at the ICML 2025 Workshop on Long Context Foundation Models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e21350c9-8cf2-4ef2-86e1-be1f74471cd7",
  "isSidechain": false,
  "promptId": "815e4ab0-d5b7-4745-b32c-ddcee59276dd",
  "type": "user",
  "uuid": "ca20b65d-6adc-4642-8ffd-dc3fe9b91b24",
  "toolUseResult": {
    "query": "PI-LLM proactive interference arXiv 2506.08184 working memory LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AB8bSHRH2j3qKGwVnr69mF",
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
            "title": "Proactive Interference Limits LLM Working Memory",
            "url": "https://www.emergentmind.com/papers/2506.08184"
          },
          {
            "title": "giantfish-fly/pi-llm · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/giantfish-fly/pi-llm"
          },
          {
            "title": "Unable to Forget: Proactive Interference Reveals Working Memory Limits in",
            "url": "https://arxiv.org/pdf/2506.08184"
          },
          {
            "title": "Cog2ai/pi-llm-bench · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/Cog2ai/pi-llm-bench"
          }
        ]
      },
      "I found the research paper you're looking for! Here are the key findings:\n\n## Overview\n\nPI-LLM is an evaluation that sequentially streams semantically related key-value updates and queries only the final values. The paper is titled \"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length.\"\n\n## Main Results\n\nThe research adapts the proactive interference (PI) paradigm from cognitive science, where earlier information disrupts recall of newer updates. Although these final values are clearly positioned just before the query, LLM retrieval accuracy declines log-linearly toward zero as interference accumulates; errors arise from retrieving previously overwritten values.\n\n## Implications\n\nLLM retrieval accuracy declines log-linearly toward zero as interference accumulates, and these findings reveal a fundamental constraint on LLMs' ability to disentangle interference and flexibly manipulate information, suggesting a working memory bottleneck beyond mere context access.\n\nAttempts to mitigate interference via prompt engineering (e.g., instructing models to ignore earlier input) yield limited success.\n\n## Authors and Publication\n\nThe paper was authored by Chupei Wang (University of Virginia) and Jiaqiu Vince Sun (New York University) and was accepted at the ICML 2025 Workshop on Long Context Foundation Models."
    ],
    "durationSeconds": 6.448481928,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e21350c9-8cf2-4ef2-86e1-be1f74471cd7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T04:53:57.819Z_

<details><summary>↩ Tool result · `toolu_01R1jcWPcxzFRgi5Hr3AKtqX`</summary>

```text
Web search results for query: "context rot LLM benchmark degradation long context evaluation 2025 2026"

Links: [{"title":"ChromaDB: Context Rot: Evaluating LLM Performance Degradation with Increasing Input Tokens - ZenML LLMOps Database","url":"https://www.zenml.io/llmops-database/context-rot-evaluating-llm-performance-degradation-with-increasing-input-tokens"},{"title":"Context Rot: Why LLMs Degrade as Context Grows (Complete Guide) | Morph","url":"https://www.morphllm.com/context-rot"},{"title":"Context rot: the emerging challenge that could hold back LLM progress","url":"https://www.understandingai.org/p/context-rot-the-emerging-challenge"},{"title":"Context Rot: How Increasing Input Tokens Impacts LLM Performance | Chroma","url":"https://research.trychroma.com/context-rot"},{"title":"LOCA-bench: Benchmarking Language Agents Under Controllable and Extreme Context Growth","url":"https://arxiv.org/pdf/2602.07962"},{"title":"Context Degradation in LLMs","url":"https://www.emergentmind.com/topics/context-degradation-in-large-language-models"},{"title":"Long-Context Language Modeling Benchmarks","url":"https://www.emergentmind.com/topics/long-context-language-modeling-benchmarks"},{"title":"Context Length Alone Hurts LLM Performance Despite Perfect Retrieval","url":"https://arxiv.org/pdf/2510.05381"},{"title":"Intelligence Degradation in Long-Context LLMs: Critical Threshold Determination via Natural Length Distribution Analysis","url":"https://arxiv.org/pdf/2601.15300"}]

Based on the web search results, here's what recent research reveals about context rot, LLM benchmark degradation, and long-context evaluation in 2025-2026:

## Definition and Overview

Context rot is the measurable degradation in LLM output quality that occurs as input context length increases. Even when a model's context window isn't close to full, adding more tokens degrades performance.

## Key Research Findings

Evaluation of 18 state-of-the-art models including GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 across controlled experiments reveals that model reliability decreases significantly with longer inputs, even on simple tasks like retrieval and text replication. Chroma's research tested 18 frontier models and found that every single one gets worse as input length increases.

## Distinctive Characteristics

Context rot is not context window overflow—overflow happens when you exceed the model's maximum token limit, while rot happens well before that. A model with a 200K token window can exhibit significant degradation at 50K tokens.

## Mechanisms of Degradation

Transformers distribute fixed attention across growing tokens, attenuating focus on relevant spans as context length increases. Models are susceptible to being "lured" by coherent but irrelevant context, shifting responses toward distractors.

## Recent Benchmarking Work

LOCAbench evaluates language agents as a combination of models and scaffolds, including various context management strategies. While agent performance generally degrades as the environment states grow more complex, advanced context management techniques can substantially improve the overall success rate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "666fcc9b-229f-4a3a-a664-cf7c8ce68953",
  "isSidechain": false,
  "promptId": "815e4ab0-d5b7-4745-b32c-ddcee59276dd",
  "type": "user",
  "uuid": "7ae416d0-035f-459f-a8a7-86854727639f",
  "toolUseResult": {
    "query": "context rot LLM benchmark degradation long context evaluation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017aFb6ccrGp6L6abZ88Hezv",
        "content": [
          {
            "title": "ChromaDB: Context Rot: Evaluating LLM Performance Degradation with Increasing Input Tokens - ZenML LLMOps Database",
            "url": "https://www.zenml.io/llmops-database/context-rot-evaluating-llm-performance-degradation-with-increasing-input-tokens"
          },
          {
            "title": "Context Rot: Why LLMs Degrade as Context Grows (Complete Guide) | Morph",
            "url": "https://www.morphllm.com/context-rot"
          },
          {
            "title": "Context rot: the emerging challenge that could hold back LLM progress",
            "url": "https://www.understandingai.org/p/context-rot-the-emerging-challenge"
          },
          {
            "title": "Context Rot: How Increasing Input Tokens Impacts LLM Performance | Chroma",
            "url": "https://research.trychroma.com/context-rot"
          },
          {
            "title": "LOCA-bench: Benchmarking Language Agents Under Controllable and Extreme Context Growth",
            "url": "https://arxiv.org/pdf/2602.07962"
          },
          {
            "title": "Context Degradation in LLMs",
            "url": "https://www.emergentmind.com/topics/context-degradation-in-large-language-models"
          },
          {
            "title": "Long-Context Language Modeling Benchmarks",
            "url": "https://www.emergentmind.com/topics/long-context-language-modeling-benchmarks"
          },
          {
            "title": "Context Length Alone Hurts LLM Performance Despite Perfect Retrieval",
            "url": "https://arxiv.org/pdf/2510.05381"
          },
          {
            "title": "Intelligence Degradation in Long-Context LLMs: Critical Threshold Determination via Natural Length Distribution Analysis",
            "url": "https://arxiv.org/pdf/2601.15300"
          }
        ]
      },
      "Based on the web search results, here's what recent research reveals about context rot, LLM benchmark degradation, and long-context evaluation in 2025-2026:\n\n## Definition and Overview\n\nContext rot is the measurable degradation in LLM output quality that occurs as input context length increases. Even when a model's context window isn't close to full, adding more tokens degrades performance.\n\n## Key Research Findings\n\nEvaluation of 18 state-of-the-art models including GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 across controlled experiments reveals that model reliability decreases significantly with longer inputs, even on simple tasks like retrieval and text replication. Chroma's research tested 18 frontier models and found that every single one gets worse as input length increases.\n\n## Distinctive Characteristics\n\nContext rot is not context window overflow—overflow happens when you exceed the model's maximum token limit, while rot happens well before that. A model with a 200K token window can exhibit significant degradation at 50K tokens.\n\n## Mechanisms of Degradation\n\nTransformers distribute fixed attention across growing tokens, attenuating focus on relevant spans as context length increases. Models are susceptible to being \"lured\" by coherent but irrelevant context, shifting responses toward distractors.\n\n## Recent Benchmarking Work\n\nLOCAbench evaluates language agents as a combination of models and scaffolds, including various context management strategies. While agent performance generally degrades as the environment states grow more complex, advanced context management techniques can substantially improve the overall success rate."
    ],
    "durationSeconds": 8.595179726,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "666fcc9b-229f-4a3a-a664-cf7c8ce68953",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T04:54:01.130Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FKrcCxYUdYPXi3qodnCtPp`</summary>

```json
{
  "query": "EMB-S semantic interference long context retrieval arXiv 2601.20276 needle haystack 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ae416d0-035f-459f-a8a7-86854727639f",
  "isSidechain": false,
  "requestId": "req_011CbDDubMrvGqx1PRJm5oGw",
  "type": "assistant",
  "uuid": "edca621e-9205-4eb7-b9e6-b32d3b41320b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012rrR1WvSacvs1bHgTvHS45",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 849,
      "cache_creation_input_tokens": 1861,
      "cache_read_input_tokens": 20404,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1861,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 849,
          "output_tokens": 133,
          "cache_read_input_tokens": 20404,
          "cache_creation_input_tokens": 1861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1861
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

_source line 19 · 2026-05-20T04:54:01.420Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DBp5KkRXU93RUmmAqi3RBU`</summary>

```json
{
  "query": "CogniLoad factorial benchmark distractor density length LLM arXiv 2509.18458"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edca621e-9205-4eb7-b9e6-b32d3b41320b",
  "isSidechain": false,
  "requestId": "req_011CbDDubMrvGqx1PRJm5oGw",
  "type": "assistant",
  "uuid": "5e05445d-e1ad-4dff-a041-3d313555387b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012rrR1WvSacvs1bHgTvHS45",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 849,
      "cache_creation_input_tokens": 1861,
      "cache_read_input_tokens": 20404,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1861,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 849,
          "output_tokens": 133,
          "cache_read_input_tokens": 20404,
          "cache_creation_input_tokens": 1861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1861
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs…",
  "leafUuid": "5e05445d-e1ad-4dff-a041-3d313555387b",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Decompose context rot factors in LLMs via factorial analysis",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54"
}
```

---

### Tool result

_source line 22 · 2026-05-20T04:54:08.512Z_

<details><summary>↩ Tool result · `toolu_01DBp5KkRXU93RUmmAqi3RBU`</summary>

```text
Web search results for query: "CogniLoad factorial benchmark distractor density length LLM arXiv 2509.18458"

Links: [{"title":"[2509.18458] CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density","url":"https://arxiv.org/abs/2509.18458"},{"title":"CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density","url":"https://arxiv.org/pdf/2509.18458"},{"title":"CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density","url":"https://arxiv.org/html/2509.18458"},{"title":"CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density - NR","url":"https://nr.no/en/publication/10341511/"},{"title":"Decomposing Reasoning Efficiency in Large Language Models","url":"https://arxiv.org/html/2602.09805"},{"title":"Decomposing Reasoning Efficiency in Large Language Models","url":"https://openreview.net/pdf?id=mym1D6mIZR"}]

I found the research paper you're looking for. Here's what the search results reveal:

CogniLoad is a novel synthetic benchmark grounded in Cognitive Load Theory (CLT) that addresses how current benchmarks for long-context reasoning in LLMs blur critical factors like intrinsic task complexity, distractor interference, and task length.

The benchmark generates natural-language logic puzzles with independently tunable parameters: intrinsic difficulty (d) controls intrinsic load; distractor-to-signal ratio (ρ) regulates extraneous load; and task length (N) serves as an operational proxy for conditions demanding germane load.

In evaluating 22 state-of-the-art reasoning LLMs, CogniLoad reveals distinct performance sensitivities, identifying task length as a dominant constraint and uncovering varied tolerances to intrinsic complexity and U-shaped responses to distractor ratios.

By offering systematic, factorial control over these cognitive load dimensions, CogniLoad provides a reproducible, scalable, and diagnostically rich tool for dissecting LLM reasoning limitations and guiding future model development.

The paper was authored by Daniel Kaiser and three other collaborators and was published on arXiv (2509.18458) in September 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e05445d-e1ad-4dff-a041-3d313555387b",
  "isSidechain": false,
  "promptId": "815e4ab0-d5b7-4745-b32c-ddcee59276dd",
  "type": "user",
  "uuid": "ec267968-38a8-4d1b-b5aa-cc4e8b4bfc4a",
  "toolUseResult": {
    "query": "CogniLoad factorial benchmark distractor density length LLM arXiv 2509.18458",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Bs6HxArjVtFcSVAjjEYBug",
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
            "title": "CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density",
            "url": "https://arxiv.org/html/2509.18458"
          },
          {
            "title": "CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density - NR",
            "url": "https://nr.no/en/publication/10341511/"
          },
          {
            "title": "Decomposing Reasoning Efficiency in Large Language Models",
            "url": "https://arxiv.org/html/2602.09805"
          },
          {
            "title": "Decomposing Reasoning Efficiency in Large Language Models",
            "url": "https://openreview.net/pdf?id=mym1D6mIZR"
          }
        ]
      },
      "I found the research paper you're looking for. Here's what the search results reveal:\n\nCogniLoad is a novel synthetic benchmark grounded in Cognitive Load Theory (CLT) that addresses how current benchmarks for long-context reasoning in LLMs blur critical factors like intrinsic task complexity, distractor interference, and task length.\n\nThe benchmark generates natural-language logic puzzles with independently tunable parameters: intrinsic difficulty (d) controls intrinsic load; distractor-to-signal ratio (ρ) regulates extraneous load; and task length (N) serves as an operational proxy for conditions demanding germane load.\n\nIn evaluating 22 state-of-the-art reasoning LLMs, CogniLoad reveals distinct performance sensitivities, identifying task length as a dominant constraint and uncovering varied tolerances to intrinsic complexity and U-shaped responses to distractor ratios.\n\nBy offering systematic, factorial control over these cognitive load dimensions, CogniLoad provides a reproducible, scalable, and diagnostically rich tool for dissecting LLM reasoning limitations and guiding future model development.\n\nThe paper was authored by Daniel Kaiser and three other collaborators and was published on arXiv (2509.18458) in September 2025."
    ],
    "durationSeconds": 7.088962553000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5e05445d-e1ad-4dff-a041-3d313555387b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T04:54:08.597Z_

<details><summary>↩ Tool result · `toolu_01FKrcCxYUdYPXi3qodnCtPp`</summary>

```text
Web search results for query: "EMB-S semantic interference long context retrieval arXiv 2601.20276 needle haystack 2026"

Links: [{"title":"[2601.20276] Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale","url":"https://arxiv.org/abs/2601.20276"},{"title":"Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale","url":"https://arxiv.org/pdf/2601.20276"},{"title":"Beyond the Needle’s Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale","url":"https://arxiv.org/html/2601.20276"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://arxiv.org/pdf/2506.08184"},{"title":"The Orthogonality Constraint in Infinite-Context Architectures","url":"https://arxiv.org/pdf/2601.15313"},{"title":"S$^3$-Attention:Attention-Aligned Endogenous Retrieval for Memory-Bounded Long-Context Inference","url":"https://arxiv.org/pdf/2601.17702"},{"title":"SEAL: Scaling to Emphasize Attention for Long-Context Retrieval","url":"https://arxiv.org/pdf/2501.15225"}]

Based on the search results, I found the paper you're looking for:

**EverMemBench-S (EMB-S)** is an adversarial NIAH-style benchmark built on a 326M-token MemoryBank. The popular Needle-in-a-Haystack (NIAH) evaluation mostly measures benign span localization, where the needle is near-unique and the haystack is largely irrelevant.

EMB-S pairs queries with collision-tested near-miss hard negatives and gold evidence sets spanning one or more documents, validated via human screening and LLM verification, and proposes a decoupled diagnostic protocol that reports evidence access (document-ID localization) separately from end-to-end QA quality under full-context prompting.

The research shows that systems that saturate benign NIAH degrade sharply in evidence access under semantic interference, indicating that semantic discrimination, not context length alone, is the dominant bottleneck for long-context memory at scale.

The paper arXiv 2601.20276 was published on January 28, 2026, and is titled "Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edca621e-9205-4eb7-b9e6-b32d3b41320b",
  "isSidechain": false,
  "promptId": "815e4ab0-d5b7-4745-b32c-ddcee59276dd",
  "type": "user",
  "uuid": "ca229797-e352-4a12-8d1b-bb349e98f4e6",
  "toolUseResult": {
    "query": "EMB-S semantic interference long context retrieval arXiv 2601.20276 needle haystack 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MxRmPtpgmM4fpu6zxxgYbT",
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
            "title": "The Orthogonality Constraint in Infinite-Context Architectures",
            "url": "https://arxiv.org/pdf/2601.15313"
          },
          {
            "title": "S$^3$-Attention:Attention-Aligned Endogenous Retrieval for Memory-Bounded Long-Context Inference",
            "url": "https://arxiv.org/pdf/2601.17702"
          },
          {
            "title": "SEAL: Scaling to Emphasize Attention for Long-Context Retrieval",
            "url": "https://arxiv.org/pdf/2501.15225"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**EverMemBench-S (EMB-S)** is an adversarial NIAH-style benchmark built on a 326M-token MemoryBank. The popular Needle-in-a-Haystack (NIAH) evaluation mostly measures benign span localization, where the needle is near-unique and the haystack is largely irrelevant.\n\nEMB-S pairs queries with collision-tested near-miss hard negatives and gold evidence sets spanning one or more documents, validated via human screening and LLM verification, and proposes a decoupled diagnostic protocol that reports evidence access (document-ID localization) separately from end-to-end QA quality under full-context prompting.\n\nThe research shows that systems that saturate benign NIAH degrade sharply in evidence access under semantic interference, indicating that semantic discrimination, not context length alone, is the dominant bottleneck for long-context memory at scale.\n\nThe paper arXiv 2601.20276 was published on January 28, 2026, and is titled \"Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale.\""
    ],
    "durationSeconds": 7.4603138369999975,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "edca621e-9205-4eb7-b9e6-b32d3b41320b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T04:54:11.131Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F1Jzmob53LAe8nfTfAEZhU`</summary>

```json
{
  "query": "ANOVA factorial analysis LLM evaluation benchmark context length position bias 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca229797-e352-4a12-8d1b-bb349e98f4e6",
  "isSidechain": false,
  "requestId": "req_011CbDDvPTGv24XqZR14RFYL",
  "type": "assistant",
  "uuid": "9061cebc-6054-4277-b565-ef4f703ed33e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8kDWDuZn6Y4CBvaB5MaSq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 663,
      "cache_creation_input_tokens": 1693,
      "cache_read_input_tokens": 22265,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1693,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 663,
          "output_tokens": 131,
          "cache_read_input_tokens": 22265,
          "cache_creation_input_tokens": 1693,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1693
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

_source line 25 · 2026-05-20T04:54:12.008Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PUa6dqSeu4CmEuJHAhegXn`</summary>

```json
{
  "query": "Sculptor active context management ICLR 2026 arXiv 2508.04664 proactive interference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9061cebc-6054-4277-b565-ef4f703ed33e",
  "isSidechain": false,
  "requestId": "req_011CbDDvPTGv24XqZR14RFYL",
  "type": "assistant",
  "uuid": "f85edd8c-4d54-4096-8c9b-ccdfc9694991",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8kDWDuZn6Y4CBvaB5MaSq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 663,
      "cache_creation_input_tokens": 1693,
      "cache_read_input_tokens": 22265,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1693,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 663,
          "output_tokens": 131,
          "cache_read_input_tokens": 22265,
          "cache_creation_input_tokens": 1693,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1693
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

_source line 26 · 2026-05-20T04:54:17.946Z_

<details><summary>↩ Tool result · `toolu_01PUa6dqSeu4CmEuJHAhegXn`</summary>

```text
Web search results for query: "Sculptor active context management ICLR 2026 arXiv 2508.04664 proactive interference"

Links: [{"title":"Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://arxiv.org/html/2508.04664v1"},{"title":"[2508.04664v1] Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://arxiv.org/abs/2508.04664v1"},{"title":"ICLR Poster Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://iclr.cc/virtual/2026/poster/10010394"},{"title":"[2508.04664] Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://arxiv.org/abs/2508.04664"},{"title":"Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://www.arxiv.org/pdf/2508.04664v1"},{"title":"Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management | OpenReview","url":"https://openreview.net/forum?id=HPeiH7da0Z"},{"title":"(PDF) Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://www.researchgate.net/publication/394362750_Sculptor_Empowering_LLMs_with_Cognitive_Agency_via_Active_Context_Management"},{"title":"Paper page - Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://huggingface.co/papers/2508.04664"}]

Here are the search results for your query about Sculptor active context management:

LLMs suffer from significant performance degradation when processing long contexts due to proactive interference, where irrelevant information in earlier parts of the context disrupts reasoning and memory recall.

The Sculptor framework proposes a complementary approach by empowering LLMs with Active Context Management (ACM) tools to actively sculpt their internal working memory, equipping them with three categories of tools: (1) context fragmentation, (2) summary, hide, and restore, and (3) precise search.

This approach enables LLMs to proactively manage their attention and working memory, analogous to how humans selectively focus on relevant information while filtering out distractions.

The framework includes a novel dynamic context-aware reinforcement learning (RL) approach that advances the training of an agent that actively modifies its own conversational history.

By enabling Active Context Management, Sculptor mitigates proactive interference and provides a cognitive foundation for more reliable reasoning across diverse long-context tasks, highlighting that explicit context-control strategies, rather than merely larger token windows, are key to robustness at scale.

The paper was presented at ICLR 2026 and was initially posted on arXiv on August 6, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f85edd8c-4d54-4096-8c9b-ccdfc9694991",
  "isSidechain": false,
  "promptId": "815e4ab0-d5b7-4745-b32c-ddcee59276dd",
  "type": "user",
  "uuid": "bd66c187-978a-44f7-88ac-1125c6393b98",
  "toolUseResult": {
    "query": "Sculptor active context management ICLR 2026 arXiv 2508.04664 proactive interference",
    "results": [
      {
        "tool_use_id": "srvtoolu_018zd23TfCimfKA5SxBTRwV9",
        "content": [
          {
            "title": "Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://arxiv.org/html/2508.04664v1"
          },
          {
            "title": "[2508.04664v1] Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://arxiv.org/abs/2508.04664v1"
          },
          {
            "title": "ICLR Poster Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://iclr.cc/virtual/2026/poster/10010394"
          },
          {
            "title": "[2508.04664] Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://arxiv.org/abs/2508.04664"
          },
          {
            "title": "Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://www.arxiv.org/pdf/2508.04664v1"
          },
          {
            "title": "Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management | OpenReview",
            "url": "https://openreview.net/forum?id=HPeiH7da0Z"
          },
          {
            "title": "(PDF) Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://www.researchgate.net/publication/394362750_Sculptor_Empowering_LLMs_with_Cognitive_Agency_via_Active_Context_Management"
          },
          {
            "title": "Paper page - Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://huggingface.co/papers/2508.04664"
          }
        ]
      },
      "Here are the search results for your query about Sculptor active context management:\n\nLLMs suffer from significant performance degradation when processing long contexts due to proactive interference, where irrelevant information in earlier parts of the context disrupts reasoning and memory recall.\n\nThe Sculptor framework proposes a complementary approach by empowering LLMs with Active Context Management (ACM) tools to actively sculpt their internal working memory, equipping them with three categories of tools: (1) context fragmentation, (2) summary, hide, and restore, and (3) precise search.\n\nThis approach enables LLMs to proactively manage their attention and working memory, analogous to how humans selectively focus on relevant information while filtering out distractions.\n\nThe framework includes a novel dynamic context-aware reinforcement learning (RL) approach that advances the training of an agent that actively modifies its own conversational history.\n\nBy enabling Active Context Management, Sculptor mitigates proactive interference and provides a cognitive foundation for more reliable reasoning across diverse long-context tasks, highlighting that explicit context-control strategies, rather than merely larger token windows, are key to robustness at scale.\n\nThe paper was presented at ICLR 2026 and was initially posted on arXiv on August 6, 2025."
    ],
    "durationSeconds": 5.932857760999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f85edd8c-4d54-4096-8c9b-ccdfc9694991",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T04:54:21.216Z_

<details><summary>↩ Tool result · `toolu_01F1Jzmob53LAe8nfTfAEZhU`</summary>

```text
Web search results for query: "ANOVA factorial analysis LLM evaluation benchmark context length position bias 2025 2026"

Links: [{"title":"Positional Biases Shift as Inputs Approach Context Window Limits","url":"https://arxiv.org/pdf/2508.07479"},{"title":"Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs","url":"https://arxiv.org/pdf/2410.14641"},{"title":"Position-Aware Parameter Efficient Fine-Tuning Approach for Reducing   Positional Bias in LLMs","url":"https://arxiv.org/pdf/2404.01430"},{"title":"Video-LevelGauge: Investigating Contextual Positional Bias in Large Video Language Models","url":"https://arxiv.org/pdf/2508.19650"},{"title":"Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems","url":"https://arxiv.org/pdf/2411.01101"},{"title":"Explaining Length Bias in LLM-Based Preference Evaluations","url":"https://arxiv.org/pdf/2407.01085"}]

I found several relevant research papers on LLM evaluation, positional bias, and context length. Here are the key findings:

## Recent Research on Positional Bias and Context Length

**Positional Bias Patterns:**
The "Lost in the Middle" (LiM) effect is strongest when inputs occupy up to 50% of a model's context window, with primacy bias weakening beyond that point while recency bias remains relatively stable, and models showing better performance when information is closer to the end of input.

**Multiple Relevant Information Pieces:**
LONGPIBENCH is a benchmark designed to assess positional bias involving multiple pieces of relevant information across various tasks and input lengths, evaluated with three commercial and six open-source models.

**Video Language Models:**
A comprehensive analysis method combining statistical measures with morphological pattern recognition characterizes bias, with a benchmark comprising 438 manually curated videos yielding 1,177 multiple-choice questions and 120 open-ended questions.

**Long-Context Task Evaluation:**
Recent studies employ automated metrics (ROUGE, F1, accuracy) and LLM judges with bootstrapped 95% confidence intervals to quantify statistical significance rigorously across multiple long-context tasks.

These papers represent recent work (2024-2025) on factorial analysis approaches and systematic evaluation methodologies for understanding positional bias in LLMs handling extended context windows.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9061cebc-6054-4277-b565-ef4f703ed33e",
  "isSidechain": false,
  "promptId": "815e4ab0-d5b7-4745-b32c-ddcee59276dd",
  "type": "user",
  "uuid": "b222a598-fe08-4009-9d5e-4d3eeb74ca4d",
  "toolUseResult": {
    "query": "ANOVA factorial analysis LLM evaluation benchmark context length position bias 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GRKqXntn7eBig763pt8V9q",
        "content": [
          {
            "title": "Positional Biases Shift as Inputs Approach Context Window Limits",
            "url": "https://arxiv.org/pdf/2508.07479"
          },
          {
            "title": "Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs",
            "url": "https://arxiv.org/pdf/2410.14641"
          },
          {
            "title": "Position-Aware Parameter Efficient Fine-Tuning Approach for Reducing   Positional Bias in LLMs",
            "url": "https://arxiv.org/pdf/2404.01430"
          },
          {
            "title": "Video-LevelGauge: Investigating Contextual Positional Bias in Large Video Language Models",
            "url": "https://arxiv.org/pdf/2508.19650"
          },
          {
            "title": "Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems",
            "url": "https://arxiv.org/pdf/2411.01101"
          },
          {
            "title": "Explaining Length Bias in LLM-Based Preference Evaluations",
            "url": "https://arxiv.org/pdf/2407.01085"
          }
        ]
      },
      "I found several relevant research papers on LLM evaluation, positional bias, and context length. Here are the key findings:\n\n## Recent Research on Positional Bias and Context Length\n\n**Positional Bias Patterns:**\nThe \"Lost in the Middle\" (LiM) effect is strongest when inputs occupy up to 50% of a model's context window, with primacy bias weakening beyond that point while recency bias remains relatively stable, and models showing better performance when information is closer to the end of input.\n\n**Multiple Relevant Information Pieces:**\nLONGPIBENCH is a benchmark designed to assess positional bias involving multiple pieces of relevant information across various tasks and input lengths, evaluated with three commercial and six open-source models.\n\n**Video Language Models:**\nA comprehensive analysis method combining statistical measures with morphological pattern recognition characterizes bias, with a benchmark comprising 438 manually curated videos yielding 1,177 multiple-choice questions and 120 open-ended questions.\n\n**Long-Context Task Evaluation:**\nRecent studies employ automated metrics (ROUGE, F1, accuracy) and LLM judges with bootstrapped 95% confidence intervals to quantify statistical significance rigorously across multiple long-context tasks.\n\nThese papers represent recent work (2024-2025) on factorial analysis approaches and systematic evaluation methodologies for understanding positional bias in LLMs handling extended context windows."
    ],
    "durationSeconds": 10.078909438000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9061cebc-6054-4277-b565-ef4f703ed33e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-20T04:55:11.097Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the field. Let me synthesize my findings and evaluate this proposal.

Let me think carefully about this proposal:

**What the proposal is doing:**
- Building a diagnostic benchmark (PI-ContextRot) that uses a 3⁴ factorial design to decompose "context rot" into four factors: proactive interference, position bias, semantic distractor similarity, and raw context length
- Running ANOVA with partial η² effect sizes to quantify each factor's contribution
- Testing 12 models across different architectures
- Adding mechanistic analysis (attention entropy, attribution patching)


- The key tension is whether the factorial design's ability to capture interaction effects justifies the complexity over simpler one-factor-at-a-time ablations, especially if main effects dominate the variance.
- The real contribution isn't just the interactions themselves—it's quantifying the *relative* contribution of each factor with effect sizes, which no single existing study provides. The trivial alternative would be qualitatively synthesizing existing papers, but that lacks rigor.
- Two critical assumptions underpin the proposal: first, that the four factors are truly orthogonal (though length and interference load seem partially confounded at 128K context), and second, that synthetic, precisely-controlled benchmark instances will generalize to real-world retrieval scenarios.
- There's also a statistical assumption that ANOVA is appropriate for LLM accuracy data, which is often binary and may violate normality and homogeneity of variance assumptions—the proposal doesn't address this.
- The novelty is methodological: no prior work has jointly decomposed all four factors in a single factorial design, even though related studies like CogniLoad, PI-LLM, and LongPiBench each control subsets of these variables.
- While the factorial ANOVA approach itself is standard in psychology, applying it to this specific combination of factors represents medium novelty—it fills a real gap but the solution is relatively straightforward once identified.
- The research question matters because knowing the relative contributions of each factor would genuinely guide where to focus effort, but the significance hinges on whether the results generalize beyond the specific operationalizations chosen and whether the findings translate into actionable insights.
- The proposal has solid related work coverage including recent papers, but it risks confirming what we'd already expect from existing work, or at best showing that results vary by architecture—which is interesting but not groundbreaking.
- Benchmark papers without novel methods face acceptance challenges at top venues unless findings are truly surprising, and the artificial factorial design may not translate to real-world settings.
- Weighing novelty (medium), significance (medium-to-strong), and related work (strong), I'm estimating around 25-35% acceptance probability, with a median of 30%.

Reconsidering though—diagnostic benchmark papers at venues like EMNLP can perform well if they're methodologically rigorous, address an important topic, and reveal surprising findings. This proposal checks those boxes with proper power analysis and controls. The real question is whether the results will be unexpected enough. If the paper clearly demonstrates that interference matters 3x more than position or uncovers unexpected interactions, it could be quite influential. The main limitation is that it's descriptive rather than prescriptive—it identifies what matters but doesn't offer solutions, which some reviewers might see as incomplete. I'll stick with 25-35%, median 30%, since the work is genuinely useful but probably not surprising enough to push higher.

The execution quality will ultimately determine where it falls within that range. Though I should note that while the proposal is well-developed with a clear, thorough plan, the core contribution is more of an engineering effort—systematically varying four factors and measuring their relative importance—rather than a novel discovery. The form is excellent, but that doesn't necessarily translate to idea quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b222a598-fe08-4009-9d5e-4d3eeb74ca4d",
  "isSidechain": false,
  "requestId": "req_011CbDDwKPUutHskWqwfT6fd",
  "type": "assistant",
  "uuid": "478d8a78-46e0-4788-8d39-b8718fdc265d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PbgyHA26NxYeAz8aTSrqXV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 762,
      "cache_creation_input_tokens": 1430,
      "cache_read_input_tokens": 23958,
      "output_tokens": 5569,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1430,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 762,
          "output_tokens": 5569,
          "cache_read_input_tokens": 23958,
          "cache_creation_input_tokens": 1430,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1430
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

_source line 29 · 2026-05-20T04:56:32.012Z_

Now I have sufficient research to evaluate this proposal. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length](https://arxiv.org/abs/2506.08184) (ICML 2025 Workshop on Long Context Foundation Models): PI-LLM — the core upstream work. Demonstrates log-linear accuracy decline under proactive interference using synthetic key-value retrieval. Accepted at a workshop (not main conference), which signals the topic is emerging but the individual-factor isolation approach has limited publication ceiling.
- [Context Rot: Evaluating LLM Performance Degradation with Increasing Input Tokens](https://research.trychroma.com/context-rot) (Chroma Research 2025): Industry report (not peer-reviewed) documenting performance degradation across 18 models. Descriptive characterization without causal decomposition. Established the term "context rot" but explicitly deferred mechanistic analysis.
- [Beyond the Needle's Illusion (EMB-S)](https://arxiv.org/abs/2601.20276) (arXiv 2026): Adversarial NIAH benchmark at 326M-token scale showing semantic discrimination is the dominant bottleneck. Decouples access from usage but does not perform relative contribution analysis across multiple factors.
- [CogniLoad](https://arxiv.org/abs/2509.18458) (arXiv 2025): Factorial benchmark with tunable length, intrinsic difficulty, and distractor density. Most methodologically similar to this proposal — it already does factorial control over 3 dimensions. Crucially, it does NOT include position bias or proactive interference as factors, which is the gap this proposal claims to fill.
- [Sculptor](https://arxiv.org/abs/2508.04664) (ICLR 2026 Poster): Active context management framework that assumes PI is the dominant problem and builds mitigation tools. Does not quantify PI's share — this is the "implicit assumption" the proposal wants to test.
- [Transformers Remember First, Forget Last: Dual-Process Interference](https://arxiv.org/abs/2603.00270) (arXiv 2026): Shows PI and RI are uncorrelated with distinct mechanisms; PI resistance doesn't scale with model size. Important supporting evidence that interference is architecturally non-trivial.
- [Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs (LongPiBench)](https://arxiv.org/abs/2410.14641) (arXiv 2024): Controls for position but not interference load — another partial coverage that the proposal aims to unify.
- [Cross-Component Interference in LLM Agent Scaffolding](https://arxiv.org/abs/2605.05716) (arXiv 2026): Uses full factorial experiment but manipulates agent scaffolding components, not the interference-position-similarity-length factors. Shows the factorial methodology is gaining traction in the community.
- [Positional Biases Shift as Inputs Approach Context Window Limits](https://arxiv.org/abs/2508.07479) (arXiv 2025): Shows positional bias is dynamic and dependent on context utilization ratio, adding nuance to the "position" factor.

- **调研总结**: The field has independently established that (a) proactive interference causes log-linear accuracy collapse (PI-LLM), (b) semantic discrimination is a dominant bottleneck (EMB-S), (c) position bias interacts with context utilization (LongPiBench), and (d) context rot is pervasive but unexplained (Chroma). CogniLoad has demonstrated factorial methodology for LLM evaluation but over a different factor set. The gap — a unified quantitative decomposition of all four factors simultaneously — is genuine and well-identified. However, the individual threads are mostly at workshop/preprint stage, and the gap is of the "someone should connect the dots" variety rather than requiring a conceptual leap.

【Trivial Alternative 检验】:
**存在部分 trivial alternative 威胁，但不致命。**

最直接的 trivial alternative 是：不做联合 factorial 设计，而是分别做 4 个 one-factor-at-a-time (OFAT) 控制实验，每个实验固定其他三个因素。这在统计学上是经典对比：OFAT vs. factorial design。Factorial 的增量价值在于能捕获 **交互效应**（例如 interference × position 的交互），OFAT 无法做到这一点。因此，如果核心发现最终是"main effects 占主导，交互效应很小"，那 factorial 的增量价值就大打折扣——本质上做了一个更昂贵版本的 OFAT。但如果交互效应显著且 non-trivial，那 factorial 设计的价值就成立了。

另一个更根本的 trivial alternative：**直接利用现有论文的定量结果做 meta-analysis**。PI-LLM 已经给出了 interference 的效应量级，EMB-S 给出了 semantic discrimination 的效应量级，LongPiBench 给出了 position 的效应量级。一个 meta-analytic 比较（尽管不完美，因为实验设置不同）可以给出粗略的相对重要性排序，而成本几乎为零。这个 proposal 的增量价值在于：(1) 统一实验条件下的直接比较，(2) 交互效应的测量，(3) 跨架构的系统比较。这些增量是真实的，但审稿人可能会质疑是否值得如此大的工程投入。

【前提假设检验】:
核心 claim 的逻辑链中存在以下未经验证的假设：

1. **四因素正交性假设**：Proposal 假设 interference load、position、similarity、length 可以被独立操控。但在实际操作中，增加 interference passages（0→3→8）必然增加 token 数量，与 length 因素部分 confound。在 8K context length 下塞入 8 个 interference passages 可能物理上不可能，或导致信号段落被严重压缩。Proposal 没有讨论如何处理这个 confounding。

2. **ANOVA 适用性假设**：LLM 的准确率数据通常是二值的（correct/incorrect），aggregate 到 cell 均值后样本量为 35。ANOVA 假设正态分布和方差齐性，35 per cell 对 binary data 的 CLT 收敛可能不够充分（尤其在 ceiling/floor cells）。Proposal 没有提到 generalized linear mixed models (GLMM) 或其他适用于二值数据的替代方案。

3. **"因果分解"措辞的合理性**：Proposal 多次使用"causal decomposition"一词，但 factorial ANOVA 提供的是 **variance decomposition**，不是因果推断。即使完美执行，partial η² 告诉你的是每个因素解释了多少方差，而不是因果机制。Mechanistic analysis（attention entropy, AtP*）只在 2 个小模型上做，无法支撑对全部 12 个模型的因果声明。

4. **Similarity 分档的有效性**：用 BGE-M3 embedding cosine similarity 的 <0.3 / 0.5-0.7 / >0.85 阈值来定义 low/medium/high similarity。但这个操作化是否与模型内部的"语义相似度"对齐是一个开放问题。不同模型可能对"相似度"有完全不同的内部表征。

【3 维度打分】:

1. **Novelty: 中** — 
   Gap 是真实的：CogniLoad (arXiv:2509.18458) 做了 factorial 但缺少 position 和 interference 因素；PI-LLM (arXiv:2506.08184) 隔离了 PI 但只用 synthetic KV pairs；EMB-S (arXiv:2601.20276) 隔离了 semantic interference 但不做相对贡献分析；Cross-Component Interference (arXiv:2605.05716) 用 factorial 但操控的是 agent scaffolding 组件。所以"联合四因素 factorial"确实没有人做过。然而，novelty 的**质**需要审视：(a) factorial ANOVA 是心理学/实验科学的标准方法论，将其应用于 LLM evaluation 不是方法论创新；(b) CogniLoad 已经示范了"factorial benchmark for LLMs"的范式，本工作只是换了因素集；(c) 核心 insight 是"应该联合测量这些因素"，这是一个 good observation 但不是 surprising observation——任何同时阅读过 PI-LLM、EMB-S 和 Chroma 的人都会得出这个结论。属于 "fill the gap" 类型的 novelty，而非 "change the paradigm" 类型。

2. **Significance: 中** — 
   研究问题确实重要：理解 context rot 的 factor composition 对 retrieval augmented generation、long-context model deployment 和 context engineering 都有实际指导意义。Sculptor (ICLR 2026) 假设 PI 是主要问题但未量化——如果本研究能证伪这一假设，那影响力就很大。然而，significance 受以下因素限制：(a) 这是 purely diagnostic/descriptive 工作，不提供解决方案或新方法——benchmark 论文的 significance 上限通常低于方法论文；(b) 即使得到了 effect size ranking，其可操作性存疑——知道"PI 贡献 40%、position 贡献 25%"之后，具体该怎么做？Proposal 说"informs whether to prioritize interference-aware retrieval or position debiasing"，但这是一个 false dichotomy，实际中两者可以同时做；(c) 发现的泛化性受制于所选的 task types、factor operationalizations 和 model set。

3. **Related Work: 强** — 
   这是 proposal 最强的部分。对 PI-LLM、EMB-S、CogniLoad、Sculptor、LongPiBench、Dual-Process、SleepGate、Cross-Component Interference、LongMINT 等工作的覆盖非常全面且准确（经调研验证，所有引用的 arXiv ID 和核心发现均与实际论文一致）。差异化定位清晰——proposal 准确指出了每个先前工作覆盖了哪些因素、缺少了哪些因素，并清楚说明了本工作如何填补空白。对 concurrent work（2026 年 5 月的论文）也有覆盖。唯一小缺口：未讨论 "Lost in the Middle" (Liu et al., 2023) 这一 position bias 领域最经典的工作，以及 "Positional Biases Shift as Inputs Approach Context Window Limits" (arXiv:2508.07479) 等后续研究。

【概率估计】: 22% - 33%，中位 27%

【估计理由】: 
Novelty 是中等偏下——gap 是真实的但 approach 是 straightforward 的，属于"connecting the dots"类工作而非概念性突破。CogniLoad 已经建立了"factorial benchmark for LLMs"的范式，本工作是在不同因素集上的复制/扩展。Significance 受限于纯 diagnostic 性质——benchmark 论文如果发现不够 surprising（例如确认了 PI 是主导因素），审稿人会说"interesting but confirmatory"；如果发现 surprising（例如 position bias 才是主导因素，而不是 interference），则可以推向上界。Related Work 是强项，但 related work 的质量只能帮助不被拒（即提高下限），不能大幅提升中稿概率。

**Novelty 是限制上界的主要维度**。即使实验执行完美，核心 finding 是一组 effect sizes 和 interaction plots——除非发现反直觉的结果（如某个被认为重要的因素贡献极小），审稿人不太可能写"surprising"。

【主要风险】:
1. **"Confirmatory finding" 风险**：如果最终发现 PI 和 semantic similarity 是主导因素（这是 PI-LLM 和 EMB-S 已经 separately 暗示的），审稿人会认为结果在意料之中（"I would have guessed this"），大幅降低论文的 impact 评分。
2. **"Variance decomposition ≠ causal" 质疑**：Proposal 反复声称"causal decomposition"，但 factorial ANOVA 只能做 variance decomposition。AtP* 机制分析只覆盖 2 个小模型，无法为 12 个模型的"因果"声明提供充分支撑。审稿人可能会认为"causal"的措辞 overclaim 了方法能提供的东西。
```

Sources:
- [PI-LLM: Unable to Forget](https://arxiv.org/abs/2506.08184)
- [Context Rot - Chroma Research](https://research.trychroma.com/context-rot)
- [EMB-S: Beyond the Needle's Illusion](https://arxiv.org/abs/2601.20276)
- [CogniLoad](https://arxiv.org/abs/2509.18458)
- [Sculptor (ICLR 2026)](https://arxiv.org/abs/2508.04664)
- [Dual-Process Interference in LLMs](https://arxiv.org/abs/2603.00270)
- [LongPiBench](https://arxiv.org/abs/2410.14641)
- [Cross-Component Interference](https://arxiv.org/abs/2605.05716)
- [Positional Biases Shift](https://arxiv.org/abs/2508.07479)
- [SleepGate](https://arxiv.org/abs/2603.14517)
- [Intelligence Degradation](https://arxiv.org/abs/2601.15300)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "478d8a78-46e0-4788-8d39-b8718fdc265d",
  "isSidechain": false,
  "requestId": "req_011CbDDwKPUutHskWqwfT6fd",
  "type": "assistant",
  "uuid": "97329961-dac6-4f14-bd3f-e39526c49add",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PbgyHA26NxYeAz8aTSrqXV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 762,
      "cache_creation_input_tokens": 1430,
      "cache_read_input_tokens": 23958,
      "output_tokens": 5569,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1430,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 762,
          "output_tokens": 5569,
          "cache_read_input_tokens": 23958,
          "cache_creation_input_tokens": 1430,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1430
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

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs…",
  "leafUuid": "97329961-dac6-4f14-bd3f-e39526c49add",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Decompose context rot factors in LLMs via factorial analysis",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs…",
  "leafUuid": "97329961-dac6-4f14-bd3f-e39526c49add",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Decompose context rot factors in LLMs via factorial analysis",
  "sessionId": "f70f628b-ffed-44b3-abc1-73f1329e1f54"
}
```

---
