# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Decomposing Context Rot: A Factor

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/a9ca1c93-6056-4bd1-a2ea-b979c103d16b.jsonl`
- **Structured JSON:** [`2a06f5062cfe2b664af3.json`](../../sessions/2a/2a06f5062cfe2b664af3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:53:39.910Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:53:39.910Z",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs\n\n## Description\nWe propose PI-ContextRot, the first diagnostic benchmark designed to causally decompose context rot — the well-documented degradation of LLM performance as input context grows — into its constituent factors: proactive interference, position bias, semantic distractor similarity, and raw length. While Chroma (2025) documented context rot across 18 models, PI-LLM (2025) demonstrated log-linear accuracy collapse under synthetic interference, and EMB-S (2026) showed semantic discrimination is the dominant bottleneck for long-context retrieval, these threads remain disconnected: no work has measured the relative contribution of each factor to realistic task degradation. Our balanced 3⁴ factorial design (3 interference levels × 3 positions × 3 similarity levels × 3 context lengths = 81 cells, 35 instances per cell per task, 8,505 total instances across multi-document QA, entity tracking, and temporal reasoning) is formally powered (≥0.95 for medium effects, ≥0.80 for small effects on two-way interactions). Evaluating 12 models across dense (Qwen3.5-9B/27B), MoE (Llama-4-Scout, Qwen3.5-122B-A10B, DeepSeek-V4-Flash), SSM-hybrid (Jamba-1.5-Mini/Large), and frontier API architectures (GPT-4.1, Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini 2.5 Pro, Qwen3.5-397B-A17B), we report partial η² effect sizes quantifying each factor's contribution and their interactions. A tiered mechanistic analysis — attention entropy on all open-weight models plus attribution patching (AtP*) on dense models ≤27B — identifies the causal circuits underlying each factor. This decomposition directly informs practical context engineering: the effect-size rankings reveal whether mitigation efforts should prioritize interference-aware retrieval (as Sculptor assumes), position debiasing, or length management, resolving an implicit disagreement across the three literatures.\n\n## Core Problem\nWhat are the relative contributions of proactive interference, position bias, semantic distractor similarity, and raw context length to observed context rot in LLMs, and how do these factors interact across dense, MoE, and SSM-hybrid architectures?\n\n## Opportunity\nThree active research threads have developed independently: the context rot literature (Chroma 2025, documenting non-uniform degradation across 18 models), the proactive interference literature (PI-LLM arXiv:2506.08184, showing log-linear accuracy decline; Dual-Process arXiv:2603.00270, showing PI dominates over RI in LLMs opposite to humans), and the semantic interference literature (EMB-S arXiv:2601.20276, showing semantic discrimination — not context length — is the dominant bottleneck for long-context retrieval at 326M-token scale). These threads have never been connected into a unified quantitative decomposition. PI-LLM uses only synthetic key-value pairs; Chroma documents degradation without controlling for interference; EMB-S decouples access from usage but does not measure the relative contribution of PI versus position versus length; Sculptor (ICLR 2026) proposes active context management to mitigate PI but does not quantify PI's share of overall degradation. A hypothesis-neutral factorial study — measuring each factor's contribution via ANOVA with effect sizes — would provide the first causal decomposition of context rot into component factors, informing whether mitigation efforts should prioritize interference-aware retrieval, position debiasing, or length management.\n\n## Landscape\nChroma Research (2025) systematically documented context rot across 18 models but noted that 'investigating mechanistic interpretability is beyond scope.' PI-LLM (arXiv:2506.08184) demonstrated log-linear retrieval accuracy decline under proactive interference but only tested synthetic key-value retrieval. The Dual-Process paper (arXiv:2603.00270) found PI and RI are uncorrelated (R²=0.044) with distinct mechanisms across 39 models, and crucially that PI resistance doesn't scale with model size (R²=0.06). EMB-S (arXiv:2601.20276) introduced adversarial NIAH with collision-tested near-miss hard negatives at 326M-token scale, decoupling evidence access from usage under semantic interference — but measures access degradation rather than decomposing the contributing factors. CogniLoad (arXiv:2509.18458) provides factorial control over length, difficulty, and distractor density but NOT position bias or proactive interference load. LONGPIBENCH controls position but not interference. Sculptor (arXiv:2508.04664, ICLR 2026) proposes active context management tools to mitigate PI but does not quantify PI's relative contribution to overall degradation — it assumes PI is the dominant problem without measuring its effect size against position bias or raw length. The noise decomposition framework of 'When Does Divide and Conquer Work' (arXiv:2506.16411, ICLR 2026) decomposes long-context failures into task/model/aggregator noise for chunking strategies but does not manipulate interference or position as controlled factors. Concurrent work update (May 2026): LongMINT (arXiv:2605.18565) evaluates memory under multi-target interference in long-horizon agent systems but focuses on agent memory architectures. Cross-Component Interference (arXiv:2605.05716) demonstrates context-window crowding in LLM agent scaffolding via a full factorial experiment, but manipulates scaffolding components (planning, tools, memory) rather than the interference-position-similarity-length factors we target. SleepGate (arXiv:2603.14517) proposes a KV-cache consolidation mechanism for resolving PI but addresses mitigation rather than diagnosis. Intelligence Degradation (arXiv:2601.15300) identifies critical context-length thresholds via natural length distribution analysis but does not control for interference or semantic similarity. No existing work performs a joint factorial decomposition of context rot into interference, position, similarity, and length components with effect sizes on realistic NLP tasks across multiple architectures.\n\n## Approach\nConstruct PI-ContextRot, a diagnostic benchmark with factorial control over four orthogonal factors in a balanced 3⁴ design: (1) proactive interference load — number of semantically similar but superseded passages preceding the target (0/3/8 levels, spanning from no interference through moderate to severe based on PI-LLM's log-linear curve), (2) target information position (early/middle/late tercile), (3) semantic similarity between distractors and target (low/medium/high, controlled via embedding cosine similarity using BGE-M3 with validated thresholds at cosine <0.3, 0.5–0.7, and >0.85), and (4) context length (8K/32K/128K tokens). The 81-cell design generates 8,505 instances (35 per cell × 3 realistic NLP task types: multi-document QA, entity state tracking, temporal reasoning over news articles), sourcing base documents from Wikipedia and CommonCrawl-News. Formal power analysis (G*Power, F-test family, fixed-effects ANOVA) confirms ≥0.95 power for detecting medium effects (partial η² ≥ 0.06, Cohen's f = 0.253) on all main effects and two-way interactions, and ≥0.80 power for small effects (partial η² ≥ 0.01, f = 0.100) on two-way interactions, at α = 0.05 with n = 35 per cell per task (N_task = 2,835). Evaluate 12 models spanning three architecture families and three scale tiers: dense transformers (Qwen3.5-9B, Qwen3.5-27B), MoE architectures (Llama-4-Scout-17B-16E, Qwen3.5-122B-A10B, DeepSeek-V4-Flash), SSM hybrids (Jamba-1.5-Mini, Jamba-1.5-Large), and frontier APIs (GPT-4.1, Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini 2.5 Pro, Qwen3.5-397B-A17B). Run a full-factorial ANOVA reporting partial η² effect sizes for each factor and all two-way interactions, with Bonferroni-corrected post-hoc contrasts, providing the first quantitative decomposition of context rot into component causes. Supplement with a tiered mechanistic analysis: (a) attention entropy measurement across all open-weight models (forward-pass only, O(1) overhead per inference, following the HEAD-ENTROPY methodology for identifying correctness-predictive attention patterns), and (b) attribution patching via AtP* (gradient-based approximation requiring only 2 forward + 1 backward pass, computationally tractable) on dense models ≤27B (Qwen3.5-9B, Qwen3.5-27B) to identify interference-sensitive versus position-sensitive attention heads. This tiered strategy replaces the original activation patching plan, which is computationally prohibitive on MoE models (cost scales linearly in the number of model components, requiring millions of forward passes on 100B+ parameter models).\n\n## Resource Estimate\n{'manual': {'gpu_hours': '1,000–1,300 (inference on 7 open-weight models across 8,505 instances at up to 128K context; large MoE/SSM models on 4–8×H100 nodes; AtP* probing on 2 dense models adds ~150 hrs; attention entropy adds ~50 hrs)', 'timeline': '12–14 weeks (2 wks benchmark construction with power-analysis validation, 4.5 wks inference runs, 2.5 wks mechanistic analysis, 3 wks writing)', 'estimated_gpu_cost': '$2,500–$4,000 at $2–3/H100-hr (Lambda Labs $2.99/hr, RunPod $1.99–$2.39/hr; market range $1.49–$6.98/hr depending on provider and commitment)', 'api_model_cost': '$400–$600 (8,505 instances × 5 API models at varying context lengths)'}, 'human_in_loop': {'gpu_hours': '650–850 (Claude handles data generation QA, similarity filtering via BGE-M3, and statistical analysis pipeline; human designs experiments and interprets mechanistic probes)', 'timeline': '8–10 weeks (1.5 wks benchmark construction with Claude-assisted template generation and power-analysis validation, 3 wks inference, 2 wks analysis, 2 wks writing)', 'claude_api_cost': '$500–$700 (data generation with quality verification: ~$200 for 8,505 instances at Sonnet 4.6 rates; similarity computation and filtering: ~$100; statistical analysis pipeline: ~$150; writing assistance: ~$250)', 'estimated_gpu_cost': '$1,600–$2,600', 'api_model_cost': '$400–$600'}, 'auto_research': {'gpu_hours': '1,300–1,700 (full 12-model evaluation including parallel sweeps across all 81 factorial cells; automated AtP* pipeline; attention entropy computation)', 'timeline': '4–6 weeks (parallelized benchmark generation and inference; automated statistical pipeline; human review at checkpoints)', 'claude_api_cost': '$900–$1,300 (benchmark generation with multi-pass verification: ~$350; orchestration and analysis: ~$400; draft generation and iteration: ~$350; quality assurance: ~$200)', 'estimated_gpu_cost': '$3,250–$5,100', 'api_model_cost': '$500–$800 (5 API models × 8,505 instances with retries)', 'speed_bottleneck': 'Sequential evaluation of large models at 128K context — DeepSeek-V4-Flash (284B, 4–8×H100) and Jamba-1.5-Large (398B total, 4–8×H100) at ~60–120 sec per 128K inference; 8,505 instances × 2 large models at 8× parallelism ≈ 300–500 GPU-hours that cannot be further distributed without additional nodes'}}\n\n## Inspired By\nField guide Section 3 (Context Rot) + Section 6 (Reasoning vs Retrieval) + the disconnect between PI-LLM's interference findings, EMB-S's semantic discrimination findings, and Chroma's context rot characterization + CogniLoad's explicit acknowledgment that 'current benchmarks do not offer the factorial control needed to disentangle these loads' + Sculptor's implicit assumption that PI is dominant without quantification\n\n## Target Venues\n- AAAI 2027 (abstract: July 21, 2026 AoE; full paper: July 28, 2026 AoE — primary target, 9 weeks from today; supplementary/code: July 31, 2026)\n- NeurIPS 2026 Workshops (suggested paper deadline: August 29, 2026 AoE — ideal for preliminary results or workshop-length version with subset of models)\n- ICLR 2027 (estimated submission: September–October 2026 — ample time for full study with complete mechanistic analysis across all architectures)\n- ACL 2027 via ARR (estimated ARR cycle: October–November 2026 — backup venue if additional experiments or reviewer-requested analyses extend the timeline)\n\n## Key References\n- Context Rot: Evaluating LLM Performance Degradation with Increasing Input Tokens (Chroma Research 2025)\n- Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length (arXiv 2025, Wang et al., arXiv:2506.08184)\n- Transformers Remember First, Forget Last: Dual-Process Interference in LLMs (arXiv 2026, Chattaraj & Raj, arXiv:2603.00270)\n- Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale (arXiv 2026, EMB-S, arXiv:2601.20276)\n- Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management (ICLR 2026, arXiv:2508.04664)\n- CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density (arXiv 2025, Kaiser et al., arXiv:2509.18458)\n- Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs (arXiv 2024, LongPiBench)\n- When Does Divide and Conquer Work for Long Context LLM? A Noise Decomposition Framework (ICLR 2026, arXiv:2506.16411)\n- AtP*: An Efficient and Scalable Method for Localizing LLM Behaviour to Components (Google DeepMind, arXiv:2403.00745)\n- Learning to Forget: Sleep-Inspired Memory Consolidation for Resolving Proactive Interference in Large Language Models (arXiv 2026, Xie, arXiv:2603.14517)\n- Intelligence Degradation in Long-Context LLMs: Critical Threshold Determination via Natural Length Distribution Analysis (arXiv 2026, arXiv:2601.15300)\n- LongMINT: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems (arXiv 2026, Lee et al., arXiv:2605.18565)\n- More Is Not Always Better: Cross-Component Interference in LLM Agent Scaffolding (arXiv 2026, arXiv:2605.05716)\n- Long-Context Generalization with Sparse Attention (ICLR 2026)\n- Applying Statistics to LLM Evaluations (Wolfe 2025 — methodological reference for power analysis in LLM benchmarks)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T04:53:39.914Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:53:39.914Z",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-20T04:53:39.940Z_

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
  "promptId": "745ae244-26b0-401e-950f-101a518ae495",
  "type": "user",
  "uuid": "bf10ea29-a0cd-4c72-a0eb-2d7ec4e2777e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:53:39.938Z_

```json
{
  "parentUuid": "bf10ea29-a0cd-4c72-a0eb-2d7ec4e2777e",
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
  "uuid": "492013eb-71f9-4b68-8ade-b71dc3245009",
  "timestamp": "2026-05-20T04:53:39.938Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:53:39.938Z_

```json
{
  "parentUuid": "492013eb-71f9-4b68-8ade-b71dc3245009",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ed7dc857-eb4b-45fb-a8fd-e393c54268c5",
  "timestamp": "2026-05-20T04:53:39.938Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
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
  "leafUuid": "ed7dc857-eb4b-45fb-a8fd-e393c54268c5",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Factorial analysis of context rot factors in LLMs",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:53:44.116Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for EMNLP 2026 submission. I need to first do thorough web searches to understand the current landscape, then evaluate the proposal's idea quality across Novelty, Significance, and Related Work dimensions.

Let me start by doing several targeted web searches to understand the field.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed7dc857-eb4b-45fb-a8fd-e393c54268c5",
  "isSidechain": false,
  "requestId": "req_011CbDDtH9x2TKZj8yg5oJZn",
  "type": "assistant",
  "uuid": "02c9783d-1d8c-4806-85e1-94f7504bbc39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hUj2ECAUnUeogtoqC3pLU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5353,
      "cache_read_input_tokens": 14333,
      "output_tokens": 213,
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
          "output_tokens": 213,
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

### Assistant

_source line 9 · 2026-05-20T04:53:46.121Z_

I'll start by conducting thorough web searches to understand the current landscape before evaluating this proposal. Let me search for the key related works and the state of research on context rot, proactive interference in LLMs, and factorial benchmark designs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02c9783d-1d8c-4806-85e1-94f7504bbc39",
  "isSidechain": false,
  "requestId": "req_011CbDDtH9x2TKZj8yg5oJZn",
  "type": "assistant",
  "uuid": "1d2c3b60-5321-4a43-a27a-3fc47db7b6e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hUj2ECAUnUeogtoqC3pLU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5353,
      "cache_read_input_tokens": 14333,
      "output_tokens": 213,
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
          "output_tokens": 213,
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

_source line 10 · 2026-05-20T04:53:46.341Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SbxZj9VbHkeWGx8PScNVZv`</summary>

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
  "parentUuid": "1d2c3b60-5321-4a43-a27a-3fc47db7b6e4",
  "isSidechain": false,
  "requestId": "req_011CbDDtH9x2TKZj8yg5oJZn",
  "type": "assistant",
  "uuid": "59c48bdc-3d41-4834-969c-638c3b1ec66c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hUj2ECAUnUeogtoqC3pLU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5353,
      "cache_read_input_tokens": 14333,
      "output_tokens": 213,
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
          "output_tokens": 213,
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

_source line 11 · 2026-05-20T04:53:46.349Z_

<details><summary>↩ Tool result · `toolu_01SbxZj9VbHkeWGx8PScNVZv`</summary>

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
  "parentUuid": "59c48bdc-3d41-4834-969c-638c3b1ec66c",
  "isSidechain": false,
  "promptId": "745ae244-26b0-401e-950f-101a518ae495",
  "type": "user",
  "uuid": "01180236-4e32-47e1-9de0-f977dffa1b65",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "59c48bdc-3d41-4834-969c-638c3b1ec66c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T04:53:52.739Z_

Now let me conduct my targeted searches. I'll run multiple searches in parallel to cover the key areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01180236-4e32-47e1-9de0-f977dffa1b65",
  "isSidechain": false,
  "requestId": "req_011CbDDtkaiN2hbKuw3eVuA9",
  "type": "assistant",
  "uuid": "85d9ca80-37bc-4caf-82a2-a6c7d22235ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018C6qeg7KYDyYRRaGo4jugG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 740,
      "cache_read_input_tokens": 19686,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 740,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 19686,
          "cache_creation_input_tokens": 740,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 740
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

_source line 13 · 2026-05-20T04:53:53.178Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013e1paURiMHM6oUVuZSVNBp`</summary>

```json
{
  "query": "proactive interference LLMs context rot factorial decomposition 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85d9ca80-37bc-4caf-82a2-a6c7d22235ac",
  "isSidechain": false,
  "requestId": "req_011CbDDtkaiN2hbKuw3eVuA9",
  "type": "assistant",
  "uuid": "d5752ddb-246b-46d1-95e0-bef4689ca385",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018C6qeg7KYDyYRRaGo4jugG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 740,
      "cache_read_input_tokens": 19686,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 740,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 19686,
          "cache_creation_input_tokens": 740,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 740
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

_source line 14 · 2026-05-20T04:54:00.461Z_

<details><summary>↩ Tool result · `toolu_013e1paURiMHM6oUVuZSVNBp`</summary>

```text
Web search results for query: "proactive interference LLMs context rot factorial decomposition 2025 2026"

Links: [{"title":"Proactive Interference Limits LLM Working Memory","url":"https://www.emergentmind.com/papers/2506.08184"},{"title":"[2506.08184v3] Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://www.arxiv.org/abs/2506.08184v3"},{"title":"[2506.08184] Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://arxiv.org/abs/2506.08184"},{"title":"Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length | OpenReview","url":"https://openreview.net/forum?id=y8jS7mDurI"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length | OpenReview","url":"https://openreview.net/forum?id=YUHksmL8aw"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250608184W/abstract"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length","url":"https://arxiv.org/html/2506.08184v1"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits in","url":"https://arxiv.org/pdf/2506.08184"},{"title":"Unable to Forget: Proactive Interference Reveals Working Memory Limits","url":"https://openreview.net/pdf?id=YUHksmL8aw"}]

Based on the search results, I found relevant recent research on proactive interference in LLMs. Here are the key findings:

## Main Study: "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length"

The research adapts the proactive interference (PI) paradigm from cognitive science, where earlier information disrupts recall of newer updates, with susceptibility in humans being inversely linked to working memory capacity.

The researchers introduced PI-LLM, an evaluation that sequentially streams semantically related key-value updates and queries only the final values, finding that LLM retrieval accuracy declines log-linearly toward zero as interference accumulates, with errors arising from retrieving previously overwritten values.

The study revealed a log-linear decline in retrieval accuracy as accumulated interference increases across models from small scales to 600B parameters.

The study proposes the Interference Endurance Score and suggests new architectural strategies to enhance LLM memory management.

The paper was accepted at ICML 2025 Workshop on Long Context Foundation Models (ICFM) and addresses a fundamental gap in understanding LLM limitations—showing that proactive interference, not context length, chiefly limits LLM memory.

**Note:** The search results do not contain information about "context rot" or "factorial decomposition" in relation to these topics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5752ddb-246b-46d1-95e0-bef4689ca385",
  "isSidechain": false,
  "promptId": "745ae244-26b0-401e-950f-101a518ae495",
  "type": "user",
  "uuid": "90f61d6d-0777-44d8-a931-ec0141a2061c",
  "toolUseResult": {
    "query": "proactive interference LLMs context rot factorial decomposition 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BFSP23kqnJ8X1mDHMsXs8P",
        "content": [
          {
            "title": "Proactive Interference Limits LLM Working Memory",
            "url": "https://www.emergentmind.com/papers/2506.08184"
          },
          {
            "title": "[2506.08184v3] Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length",
            "url": "https://www.arxiv.org/abs/2506.08184v3"
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
            "title": "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length | OpenReview",
            "url": "https://openreview.net/forum?id=YUHksmL8aw"
          },
          {
            "title": "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250608184W/abstract"
          },
          {
            "title": "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length",
            "url": "https://arxiv.org/html/2506.08184v1"
          },
          {
            "title": "Unable to Forget: Proactive Interference Reveals Working Memory Limits in",
            "url": "https://arxiv.org/pdf/2506.08184"
          },
          {
            "title": "Unable to Forget: Proactive Interference Reveals Working Memory Limits",
            "url": "https://openreview.net/pdf?id=YUHksmL8aw"
          }
        ]
      },
      "Based on the search results, I found relevant recent research on proactive interference in LLMs. Here are the key findings:\n\n## Main Study: \"Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length\"\n\nThe research adapts the proactive interference (PI) paradigm from cognitive science, where earlier information disrupts recall of newer updates, with susceptibility in humans being inversely linked to working memory capacity.\n\nThe researchers introduced PI-LLM, an evaluation that sequentially streams semantically related key-value updates and queries only the final values, finding that LLM retrieval accuracy declines log-linearly toward zero as interference accumulates, with errors arising from retrieving previously overwritten values.\n\nThe study revealed a log-linear decline in retrieval accuracy as accumulated interference increases across models from small scales to 600B parameters.\n\nThe study proposes the Interference Endurance Score and suggests new architectural strategies to enhance LLM memory management.\n\nThe paper was accepted at ICML 2025 Workshop on Long Context Foundation Models (ICFM) and addresses a fundamental gap in understanding LLM limitations—showing that proactive interference, not context length, chiefly limits LLM memory.\n\n**Note:** The search results do not contain information about \"context rot\" or \"factorial decomposition\" in relation to these topics."
    ],
    "durationSeconds": 7.278750825000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d5752ddb-246b-46d1-95e0-bef4689ca385",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T04:54:03.997Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KnwchDwBUU3krenfvfwN6w`</summary>

```json
{
  "query": "EMB-S semantic interference long-context retrieval 326M token arXiv 2601.20276"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90f61d6d-0777-44d8-a931-ec0141a2061c",
  "isSidechain": false,
  "requestId": "req_011CbDDundGaZvLxczpqfxVm",
  "type": "assistant",
  "uuid": "9742c678-75e1-4db9-b6fc-25f6f1e5ac15",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ThB5SWQJo3zrDTVWRh5Nzw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 889,
      "cache_read_input_tokens": 20426,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 889,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 20426,
          "cache_creation_input_tokens": 889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 889
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

_source line 16 · 2026-05-20T04:54:10.923Z_

<details><summary>↩ Tool result · `toolu_01KnwchDwBUU3krenfvfwN6w`</summary>

```text
Web search results for query: "EMB-S semantic interference long-context retrieval 326M token arXiv 2601.20276"

Links: [{"title":"[2601.20276] Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale","url":"https://arxiv.org/abs/2601.20276"},{"title":"Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale","url":"https://arxiv.org/pdf/2601.20276"},{"title":"Beyond the Needle’s Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale","url":"https://arxiv.org/html/2601.20276"},{"title":"LongEmbed: Extending Embedding Models for Long Context Retrieval","url":"https://arxiv.org/pdf/2404.12096"},{"title":"Emulating Retrieval Augmented Generation via Prompt Engineering for   Enhanced Long Context Comprehension in LLMs","url":"https://arxiv.org/pdf/2502.12462"}]

The search has found the paper you're looking for. Here's what I found:

EverMemBench-S (EMB-S) is an adversarial NIAH-style benchmark built on a 326M-token MemoryBank. EMB-S pairs queries with collision-tested near-miss hard negatives and gold evidence sets spanning one or more documents, validated via human screening and LLM verification.

The research addresses limitations with traditional evaluation methods. The popular Needle-in-a-Haystack (NIAH) evaluation mostly measures benign span localization. In contrast, the authors propose a decoupled diagnostic protocol that reports evidence access (document-ID localization) separately from end-to-end QA quality under full-context prompting.

Key findings include: Systems that saturate benign NIAH degrade sharply in evidence access under semantic interference, indicating that semantic discrimination, not context length alone, is the dominant bottleneck for long-context memory at scale.

The paper is titled "Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale" and was published on January 28, 2026 (arXiv:2601.20276).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9742c678-75e1-4db9-b6fc-25f6f1e5ac15",
  "isSidechain": false,
  "promptId": "745ae244-26b0-401e-950f-101a518ae495",
  "type": "user",
  "uuid": "3fe06841-0cb8-4949-bf3c-bff3c7a0a5f0",
  "toolUseResult": {
    "query": "EMB-S semantic interference long-context retrieval 326M token arXiv 2601.20276",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MsCTQpfLsC3r79Ac8CNSAL",
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
            "title": "LongEmbed: Extending Embedding Models for Long Context Retrieval",
            "url": "https://arxiv.org/pdf/2404.12096"
          },
          {
            "title": "Emulating Retrieval Augmented Generation via Prompt Engineering for   Enhanced Long Context Comprehension in LLMs",
            "url": "https://arxiv.org/pdf/2502.12462"
          }
        ]
      },
      "The search has found the paper you're looking for. Here's what I found:\n\nEverMemBench-S (EMB-S) is an adversarial NIAH-style benchmark built on a 326M-token MemoryBank. EMB-S pairs queries with collision-tested near-miss hard negatives and gold evidence sets spanning one or more documents, validated via human screening and LLM verification.\n\nThe research addresses limitations with traditional evaluation methods. The popular Needle-in-a-Haystack (NIAH) evaluation mostly measures benign span localization. In contrast, the authors propose a decoupled diagnostic protocol that reports evidence access (document-ID localization) separately from end-to-end QA quality under full-context prompting.\n\nKey findings include: Systems that saturate benign NIAH degrade sharply in evidence access under semantic interference, indicating that semantic discrimination, not context length alone, is the dominant bottleneck for long-context memory at scale.\n\nThe paper is titled \"Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale\" and was published on January 28, 2026 (arXiv:2601.20276)."
    ],
    "durationSeconds": 6.92121644,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9742c678-75e1-4db9-b6fc-25f6f1e5ac15",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T04:54:13.317Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SfcWhNLjkkV6zuLcAKSfT8`</summary>

```json
{
  "query": "Chroma Research \"context rot\" LLM performance degradation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fe06841-0cb8-4949-bf3c-bff3c7a0a5f0",
  "isSidechain": false,
  "requestId": "req_011CbDDvZNaHrq5FPmijgR2T",
  "type": "assistant",
  "uuid": "758e62e2-9065-4658-85ee-706a0c9a23ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQvtcPUJ6jV1RFC2Q4CFoW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 674,
      "cache_read_input_tokens": 21315,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 674,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 21315,
          "cache_creation_input_tokens": 674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 674
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

_source line 18 · 2026-05-20T04:54:20.288Z_

<details><summary>↩ Tool result · `toolu_01SfcWhNLjkkV6zuLcAKSfT8`</summary>

```text
Web search results for query: "Chroma Research "context rot" LLM performance degradation 2025"

Links: [{"title":"Context Rot: Why LLMs Degrade as Context Grows (Complete Guide) | Morph","url":"https://www.morphllm.com/context-rot"},{"title":"Context Rot In LLMs: Why Graphs Are The Promising Fix For Coding Agents? - E-Journal Times Magazine","url":"https://journals-times.com/2025/11/03/context-rot-in-llms-why-graphs-are-the-promising-fix-for-coding-agents/"},{"title":"Context Rot: How Increasing Input Tokens Impacts LLM Performance | Chroma","url":"https://www.trychroma.com/research/context-rot"},{"title":"Context rot: the emerging challenge that could hold back LLM progress","url":"https://www.understandingai.org/p/context-rot-the-emerging-challenge"},{"title":"LLM Context Rot","url":"https://cobusgreyling.substack.com/p/llm-context-rot"},{"title":"LLM Context Rot. The Chroma “Context Rot” study reveals… | by Cobus Greyling | Medium","url":"https://cobusgreyling.medium.com/llm-context-rot-28a6d0399655"},{"title":"ChromaDB: Context Rot: Evaluating LLM Performance Degradation with Increasing Input Tokens - ZenML LLMOps Database","url":"https://www.zenml.io/llmops-database/context-rot-evaluating-llm-performance-degradation-with-increasing-input-tokens"}]

Based on the search results, here's what I found about Chroma Research's "context rot" study on LLM performance degradation:

## Overview

The term "context rot" was formalized by Chroma's 2025 research, which systematically tested how 18 frontier models handle increasing context lengths. Context rot is the measurable degradation in LLM output quality that occurs as input context length increases.

## Key Findings

Chroma's research tested 18 frontier models and found that every single one gets worse as input length increases. The Chroma study tested 18 top-tier models — GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 — across tasks like Needle in a Haystack (NIAH) extensions, LongMemEval (conversational QA), and a synthetic "repeated words" task.

A model with a 200K token window can exhibit significant degradation at 50K tokens. Different model families exhibit unique behaviours; for instance, OpenAI's GPT series often shows erratic and inconsistent outputs, while others degrade more predictably.

## Real-World Impact

For coding agents, context rot is the primary failure mode, and agents accumulate noise during search, exploration, and backtracking, and that noise directly degrades every subsequent output.

The full technical report was published in July 2025 and is available on Chroma's official research page.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "758e62e2-9065-4658-85ee-706a0c9a23ac",
  "isSidechain": false,
  "promptId": "745ae244-26b0-401e-950f-101a518ae495",
  "type": "user",
  "uuid": "75f9177e-4287-41c2-87b0-bbe77745a567",
  "toolUseResult": {
    "query": "Chroma Research \"context rot\" LLM performance degradation 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xw8WGmMo7d7vzs3wCTGXo3",
        "content": [
          {
            "title": "Context Rot: Why LLMs Degrade as Context Grows (Complete Guide) | Morph",
            "url": "https://www.morphllm.com/context-rot"
          },
          {
            "title": "Context Rot In LLMs: Why Graphs Are The Promising Fix For Coding Agents? - E-Journal Times Magazine",
            "url": "https://journals-times.com/2025/11/03/context-rot-in-llms-why-graphs-are-the-promising-fix-for-coding-agents/"
          },
          {
            "title": "Context Rot: How Increasing Input Tokens Impacts LLM Performance | Chroma",
            "url": "https://www.trychroma.com/research/context-rot"
          },
          {
            "title": "Context rot: the emerging challenge that could hold back LLM progress",
            "url": "https://www.understandingai.org/p/context-rot-the-emerging-challenge"
          },
          {
            "title": "LLM Context Rot",
            "url": "https://cobusgreyling.substack.com/p/llm-context-rot"
          },
          {
            "title": "LLM Context Rot. The Chroma “Context Rot” study reveals… | by Cobus Greyling | Medium",
            "url": "https://cobusgreyling.medium.com/llm-context-rot-28a6d0399655"
          },
          {
            "title": "ChromaDB: Context Rot: Evaluating LLM Performance Degradation with Increasing Input Tokens - ZenML LLMOps Database",
            "url": "https://www.zenml.io/llmops-database/context-rot-evaluating-llm-performance-degradation-with-increasing-input-tokens"
          }
        ]
      },
      "Based on the search results, here's what I found about Chroma Research's \"context rot\" study on LLM performance degradation:\n\n## Overview\n\nThe term \"context rot\" was formalized by Chroma's 2025 research, which systematically tested how 18 frontier models handle increasing context lengths. Context rot is the measurable degradation in LLM output quality that occurs as input context length increases.\n\n## Key Findings\n\nChroma's research tested 18 frontier models and found that every single one gets worse as input length increases. The Chroma study tested 18 top-tier models — GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 — across tasks like Needle in a Haystack (NIAH) extensions, LongMemEval (conversational QA), and a synthetic \"repeated words\" task.\n\nA model with a 200K token window can exhibit significant degradation at 50K tokens. Different model families exhibit unique behaviours; for instance, OpenAI's GPT series often shows erratic and inconsistent outputs, while others degrade more predictably.\n\n## Real-World Impact\n\nFor coding agents, context rot is the primary failure mode, and agents accumulate noise during search, exploration, and backtracking, and that noise directly degrades every subsequent output.\n\nThe full technical report was published in July 2025 and is available on Chroma's official research page."
    ],
    "durationSeconds": 6.968403440000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "758e62e2-9065-4658-85ee-706a0c9a23ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T04:54:28.255Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SHLCXo7zfGjfazLJhQsLrT`</summary>

```json
{
  "query": "long-context LLM benchmark factorial design ANOVA effect size 2025 2026 diagnostic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75f9177e-4287-41c2-87b0-bbe77745a567",
  "isSidechain": false,
  "requestId": "req_011CbDDwFSbf78rV4Zp4JwPd",
  "type": "assistant",
  "uuid": "39530657-e647-4575-9b57-3fff9e2f9ed7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169QkrTb8YDDNZZpZqsiZcC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 21989,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 21989,
          "cache_creation_input_tokens": 835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 835
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

_source line 20 · 2026-05-20T04:54:36.033Z_

<details><summary>↩ Tool result · `toolu_01SHLCXo7zfGjfazLJhQsLrT`</summary>

```text
Web search results for query: "long-context LLM benchmark factorial design ANOVA effect size 2025 2026 diagnostic"

Links: [{"title":"Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs","url":"https://arxiv.org/pdf/2410.14641"},{"title":"Long-Context Language Modeling Benchmarks","url":"https://www.emergentmind.com/topics/long-context-language-modeling-benchmarks"},{"title":"$\\infty$Bench: Extending Long Context Evaluation Beyond 100K Tokens","url":"https://arxiv.org/pdf/2402.13718"},{"title":"100-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability?","url":"https://arxiv.org/pdf/2505.19293"},{"title":"LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark","url":"https://arxiv.org/pdf/2601.02872"},{"title":"LooGLE: Can Long-Context Language Models Understand Long Contexts?","url":"https://arxiv.org/pdf/2311.04939"},{"title":"GSM-Infinite: How Do Your LLMs Behave over Infinitely Increasing Context   Length and Reasoning Complexity?","url":"https://arxiv.org/pdf/2502.05252"}]

I found several relevant sources on long-context LLM benchmarks from 2025-2026. Here's what the search results reveal:

## Long-Context LLM Benchmarks (2025-2026)

Modern benchmarks such as AcademicEval, LongProc, XL-Bench, LV-Eval, Ada-LEval, BAMBOO, LooGLE, and Ref-Long adopt key construction features including dynamic context scaling with datasets explicitly bucketing tasks by context length.

Metrics in context compression efficiency include ROUGE-L for auto-encoding, perplexity for language modeling, pass rate for retrieval, and throughput/memory profiling.

## Evaluation Methodology

LongGenBench introduces CR (Main Task Completion), STIC-1 (execution adherence), and STIC-2 (placement precision), weighted for overall scores. Protocols stress calculation at multiple context-length buckets, strict output format enforcement, position/order sensitivity, and prompt variation experiments to probe model robustness.

## Recent Benchmark Developments

Context length has continuously expanded, making it possible for LLMs to tackle complex long-context tasks, which demands that long-context benchmarks evolve swiftly to accurately assess models' true long-context capabilities.

The search results show active development in long-context evaluation methodologies, though they don't specifically address factorial design or ANOVA effect size analyses in these benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39530657-e647-4575-9b57-3fff9e2f9ed7",
  "isSidechain": false,
  "promptId": "745ae244-26b0-401e-950f-101a518ae495",
  "type": "user",
  "uuid": "e1a7485c-42d3-4508-b170-6b7dbb1abcc0",
  "toolUseResult": {
    "query": "long-context LLM benchmark factorial design ANOVA effect size 2025 2026 diagnostic",
    "results": [
      {
        "tool_use_id": "srvtoolu_01E2xpLNZMfDffRAQ6F11BkW",
        "content": [
          {
            "title": "Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs",
            "url": "https://arxiv.org/pdf/2410.14641"
          },
          {
            "title": "Long-Context Language Modeling Benchmarks",
            "url": "https://www.emergentmind.com/topics/long-context-language-modeling-benchmarks"
          },
          {
            "title": "$\\infty$Bench: Extending Long Context Evaluation Beyond 100K Tokens",
            "url": "https://arxiv.org/pdf/2402.13718"
          },
          {
            "title": "100-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability?",
            "url": "https://arxiv.org/pdf/2505.19293"
          },
          {
            "title": "LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark",
            "url": "https://arxiv.org/pdf/2601.02872"
          },
          {
            "title": "LooGLE: Can Long-Context Language Models Understand Long Contexts?",
            "url": "https://arxiv.org/pdf/2311.04939"
          },
          {
            "title": "GSM-Infinite: How Do Your LLMs Behave over Infinitely Increasing Context   Length and Reasoning Complexity?",
            "url": "https://arxiv.org/pdf/2502.05252"
          }
        ]
      },
      "I found several relevant sources on long-context LLM benchmarks from 2025-2026. Here's what the search results reveal:\n\n## Long-Context LLM Benchmarks (2025-2026)\n\nModern benchmarks such as AcademicEval, LongProc, XL-Bench, LV-Eval, Ada-LEval, BAMBOO, LooGLE, and Ref-Long adopt key construction features including dynamic context scaling with datasets explicitly bucketing tasks by context length.\n\nMetrics in context compression efficiency include ROUGE-L for auto-encoding, perplexity for language modeling, pass rate for retrieval, and throughput/memory profiling.\n\n## Evaluation Methodology\n\nLongGenBench introduces CR (Main Task Completion), STIC-1 (execution adherence), and STIC-2 (placement precision), weighted for overall scores. Protocols stress calculation at multiple context-length buckets, strict output format enforcement, position/order sensitivity, and prompt variation experiments to probe model robustness.\n\n## Recent Benchmark Developments\n\nContext length has continuously expanded, making it possible for LLMs to tackle complex long-context tasks, which demands that long-context benchmarks evolve swiftly to accurately assess models' true long-context capabilities.\n\nThe search results show active development in long-context evaluation methodologies, though they don't specifically address factorial design or ANOVA effect size analyses in these benchmarks."
    ],
    "durationSeconds": 7.7731841070000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "39530657-e647-4575-9b57-3fff9e2f9ed7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs…",
  "leafUuid": "e1a7485c-42d3-4508-b170-6b7dbb1abcc0",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Factorial analysis of context rot factors in LLMs",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b"
}
```

---

### Tool call

_source line 23 · 2026-05-20T04:54:40.242Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01993HTPetewcmsFVhmR7CdU`</summary>

```json
{
  "query": "CogniLoad benchmark synthetic reasoning tunable length distractor density arXiv 2509.18458"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1a7485c-42d3-4508-b170-6b7dbb1abcc0",
  "isSidechain": false,
  "requestId": "req_011CbDDxQhz3bSXQtmG6QRKq",
  "type": "assistant",
  "uuid": "77f7cc06-267c-4913-b604-14abfed588af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Unodh1QoYsmc4ZDc55bx87",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 22824,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 22824,
          "cache_creation_input_tokens": 764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 764
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

_source line 24 · 2026-05-20T04:54:46.805Z_

<details><summary>↩ Tool result · `toolu_01993HTPetewcmsFVhmR7CdU`</summary>

```text
Web search results for query: "CogniLoad benchmark synthetic reasoning tunable length distractor density arXiv 2509.18458"

Links: [{"title":"[2509.18458] CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density","url":"https://arxiv.org/abs/2509.18458"},{"title":"CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density","url":"https://arxiv.org/pdf/2509.18458"},{"title":"CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density - NR","url":"https://nr.no/en/publication/10341511/"},{"title":"CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density","url":"https://arxiv.org/html/2509.18458"},{"title":"Decomposing Reasoning Efficiency in Large Language Models","url":"https://arxiv.org/html/2602.09805"},{"title":"Decomposing Reasoning Efficiency in Large Language Models","url":"https://openreview.net/pdf?id=mym1D6mIZR"},{"title":"Ali Ramezani-Kebrya - About","url":"https://alirk.github.io/"}]

Based on the search results, I found the paper you're looking for:

CogniLoad is a novel synthetic benchmark grounded in Cognitive Load Theory (CLT). CogniLoad generates natural-language logic puzzles with independently tunable parameters that reflect CLT's core dimensions: intrinsic difficulty (d) controls intrinsic load; distractor-to-signal ratio (ρ) regulates extraneous load; and task length (N) serves as an operational proxy for conditions demanding germane load.

Evaluating 22 state-of-the-art reasoning LLMs, CogniLoad reveals distinct performance sensitivities, identifying task length as a dominant constraint and uncovering varied tolerances to intrinsic complexity and U-shaped responses to distractor ratios. By offering systematic, factorial control over these cognitive load dimensions, CogniLoad provides a reproducible, scalable, and diagnostically rich tool for dissecting LLM reasoning limitations and guiding future model development.

The paper was published on arXiv in September 2025 and is authored by Daniel Kaiser, Arnoldo Frigessi, Ali Ramezani-Kebrya, and Benjamin Ricaud.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77f7cc06-267c-4913-b604-14abfed588af",
  "isSidechain": false,
  "promptId": "745ae244-26b0-401e-950f-101a518ae495",
  "type": "user",
  "uuid": "87a3c5d7-09f7-495b-980b-895b89d7448c",
  "toolUseResult": {
    "query": "CogniLoad benchmark synthetic reasoning tunable length distractor density arXiv 2509.18458",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EPDMJaTEqHFnJQh9yyJ3Cj",
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
            "title": "Decomposing Reasoning Efficiency in Large Language Models",
            "url": "https://arxiv.org/html/2602.09805"
          },
          {
            "title": "Decomposing Reasoning Efficiency in Large Language Models",
            "url": "https://openreview.net/pdf?id=mym1D6mIZR"
          },
          {
            "title": "Ali Ramezani-Kebrya - About",
            "url": "https://alirk.github.io/"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nCogniLoad is a novel synthetic benchmark grounded in Cognitive Load Theory (CLT). CogniLoad generates natural-language logic puzzles with independently tunable parameters that reflect CLT's core dimensions: intrinsic difficulty (d) controls intrinsic load; distractor-to-signal ratio (ρ) regulates extraneous load; and task length (N) serves as an operational proxy for conditions demanding germane load.\n\nEvaluating 22 state-of-the-art reasoning LLMs, CogniLoad reveals distinct performance sensitivities, identifying task length as a dominant constraint and uncovering varied tolerances to intrinsic complexity and U-shaped responses to distractor ratios. By offering systematic, factorial control over these cognitive load dimensions, CogniLoad provides a reproducible, scalable, and diagnostically rich tool for dissecting LLM reasoning limitations and guiding future model development.\n\nThe paper was published on arXiv in September 2025 and is authored by Daniel Kaiser, Arnoldo Frigessi, Ali Ramezani-Kebrya, and Benjamin Ricaud."
    ],
    "durationSeconds": 6.5593053290000025,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "77f7cc06-267c-4913-b604-14abfed588af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T04:54:49.393Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HGenzh8PG4bwc77uxuCxyV`</summary>

```json
{
  "query": "Sculptor active context management proactive interference ICLR 2026 arXiv 2508.04664"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87a3c5d7-09f7-495b-980b-895b89d7448c",
  "isSidechain": false,
  "requestId": "req_011CbDDyCnudUJNvrqSLmSzZ",
  "type": "assistant",
  "uuid": "97f87141-b1a5-4bd6-b0c3-9a21a73bfd8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Azm41nex7pvL6ENch3cCxf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 23588,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 731,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 23588,
          "cache_creation_input_tokens": 731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 731
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

_source line 26 · 2026-05-20T04:54:57.348Z_

<details><summary>↩ Tool result · `toolu_01HGenzh8PG4bwc77uxuCxyV`</summary>

```text
Web search results for query: "Sculptor active context management proactive interference ICLR 2026 arXiv 2508.04664"

Links: [{"title":"[2508.04664v1] Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://arxiv.org/abs/2508.04664v1"},{"title":"Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://arxiv.org/html/2508.04664v1"},{"title":"[2508.04664] Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://arxiv.org/abs/2508.04664"},{"title":"ICLR Poster Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://iclr.cc/virtual/2026/poster/10010394"},{"title":"Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://www.arxiv.org/pdf/2508.04664v1"},{"title":"(PDF) Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://www.researchgate.net/publication/394362750_Sculptor_Empowering_LLMs_with_Cognitive_Agency_via_Active_Context_Management"},{"title":"Paper page - Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management","url":"https://huggingface.co/papers/2508.04664"},{"title":"Mo Li","url":"https://mor-li.github.io/"}]

I found comprehensive information about this paper. Here's what I found:

## Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management

Large Language Models suffer from significant performance degradation when processing long contexts due to proactive interference, where irrelevant information in earlier parts of the context disrupts reasoning and memory recall.

### Framework Overview

The paper proposes a complementary approach to external memory systems by empowering LLMs with Active Context Management (ACM) tools to actively sculpt their internal working memory. Sculptor equips LLMs with three categories of tools: (1) context fragmentation, (2) summary, hide, and restore, and (3) intelligent search.

### Key Approach

The approach enables LLMs to proactively manage their attention and working memory, analogous to how humans selectively focus on relevant information while filtering out distractions.

### Results and Impact

Experimental evaluation on information-sparse benchmarks—PI-LLM (proactive interference) and NeedleBench Multi-Needle Reasoning—demonstrates that Sculptor significantly improves performance and provides a cognitive foundation for more reliable reasoning across diverse long-context tasks.

**Paper Details:**
- **ArXiv ID:** 2508.04664
- **Posted:** August 6, 2025
- **Conference:** ICLR 2026
- **Authors:** Mo Li, L. H. Xu, Qitai Tan, Long Ma, Ting Cao, and Yunxin Liu


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97f87141-b1a5-4bd6-b0c3-9a21a73bfd8e",
  "isSidechain": false,
  "promptId": "745ae244-26b0-401e-950f-101a518ae495",
  "type": "user",
  "uuid": "d3f125cc-30ab-496b-ad45-c55c16bdd2fe",
  "toolUseResult": {
    "query": "Sculptor active context management proactive interference ICLR 2026 arXiv 2508.04664",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Pyyoe6KXyEH948TZsdgRuj",
        "content": [
          {
            "title": "[2508.04664v1] Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://arxiv.org/abs/2508.04664v1"
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
            "title": "ICLR Poster Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://iclr.cc/virtual/2026/poster/10010394"
          },
          {
            "title": "Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management",
            "url": "https://www.arxiv.org/pdf/2508.04664v1"
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
            "title": "Mo Li",
            "url": "https://mor-li.github.io/"
          }
        ]
      },
      "I found comprehensive information about this paper. Here's what I found:\n\n## Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management\n\nLarge Language Models suffer from significant performance degradation when processing long contexts due to proactive interference, where irrelevant information in earlier parts of the context disrupts reasoning and memory recall.\n\n### Framework Overview\n\nThe paper proposes a complementary approach to external memory systems by empowering LLMs with Active Context Management (ACM) tools to actively sculpt their internal working memory. Sculptor equips LLMs with three categories of tools: (1) context fragmentation, (2) summary, hide, and restore, and (3) intelligent search.\n\n### Key Approach\n\nThe approach enables LLMs to proactively manage their attention and working memory, analogous to how humans selectively focus on relevant information while filtering out distractions.\n\n### Results and Impact\n\nExperimental evaluation on information-sparse benchmarks—PI-LLM (proactive interference) and NeedleBench Multi-Needle Reasoning—demonstrates that Sculptor significantly improves performance and provides a cognitive foundation for more reliable reasoning across diverse long-context tasks.\n\n**Paper Details:**\n- **ArXiv ID:** 2508.04664\n- **Posted:** August 6, 2025\n- **Conference:** ICLR 2026\n- **Authors:** Mo Li, L. H. Xu, Qitai Tan, Long Ma, Ting Cao, and Yunxin Liu"
    ],
    "durationSeconds": 7.949880569000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "97f87141-b1a5-4bd6-b0c3-9a21a73bfd8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T04:55:00.121Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XKonn35BkrJre4CHkNhpaB`</summary>

```json
{
  "query": "\"context rot\" OR \"long-context degradation\" decomposition causal factors position bias interference benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3f125cc-30ab-496b-ad45-c55c16bdd2fe",
  "isSidechain": false,
  "requestId": "req_011CbDDyyrKKA1xzCwyNpgzB",
  "type": "assistant",
  "uuid": "2ac2374c-7ff3-432c-9ec4-d094bdded42a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjTNnqc2Yd44tvqh2AWAac",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 845,
      "cache_read_input_tokens": 24319,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 845,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 24319,
          "cache_creation_input_tokens": 845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 845
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

_source line 28 · 2026-05-20T04:55:12.827Z_

<details><summary>↩ Tool result · `toolu_01XKonn35BkrJre4CHkNhpaB`</summary>

```text
Web search results for query: ""context rot" OR "long-context degradation" decomposition causal factors position bias interference benchmark 2026"

Links: [{"title":"Context Rot: What a 2 AM Night Taught Me That Benchmarks Never Did | by QuangTran | Apr, 2026 | Medium","url":"https://medium.com/@trmquang3103/context-rot-what-a-2-am-night-taught-me-that-benchmarks-never-did-dfda7df72f40"},{"title":"Context rot explained (& how to prevent it)","url":"https://redis.io/blog/context-rot/"},{"title":"Context Rot: Why LLMs Degrade as Context Grows (Complete Guide) | Morph","url":"https://www.morphllm.com/context-rot"},{"title":"Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems","url":"https://arxiv.org/pdf/2411.01101"},{"title":"Published as a conference paper at ICLR 2026 LONG-CONTEXT GENERALIZATION WITH","url":"https://arxiv.org/pdf/2506.16640"},{"title":"Context Degradation in LLMs","url":"https://www.emergentmind.com/topics/context-degradation-in-large-language-models"},{"title":"ChromaDB: Context Rot: Evaluating LLM Performance Degradation with Increasing Input Tokens - ZenML LLMOps Database","url":"https://www.zenml.io/llmops-database/context-rot-evaluating-llm-performance-degradation-with-increasing-input-tokens"},{"title":"Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs","url":"https://arxiv.org/pdf/2410.14641"}]

I found recent research on context rot and long-context degradation. Here's what the search results show:

## Overview of Context Rot

Context rot is the performance degradation that happens when LLMs have to process increasingly long input contexts, where performance degrades when searching through longer contexts to find relevant information even though that information is technically available in the context window.

## Causal Factors

The research identifies several decomposed causal factors:

**Position Bias:**
The problem shows up through positional bias patterns, with models working best when relevant information sits at the beginning or end of the context window but struggling when information is buried in the middle. Recent work distinguishes between absolute positions (location within entire context) and relative positions (distribution and distance between multiple relevant information pieces).

**Distractor Interference:**
Chroma's study isolated distractor interference as a third mechanism that compounds the first two. Recency bias leads to effective forgetting of earlier facts, especially under in-context interference.

**Structural Effects:**
Models performed better on shuffled haystacks than on logically coherent documents, suggesting the attention mechanism is negatively influenced by logical document flow, possibly because coherent text creates more plausible-seeming distractors.

## Recent Benchmarks (2026)

Chroma Research published a report in July 2025 testing 18 leading models (GPT-4.1, Claude 4, Gemini 2.5, Qwen3, variants) on tasks extended from Needle-in-the-Haystack. The study demonstrates that factors like needle-question similarity, presence of distractors, haystack structure, and semantic relationships all impact performance non-uniformly as context length grows.

LONGPIBENCH is a benchmark designed to assess positional bias involving multiple pieces of relevant information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ac2374c-7ff3-432c-9ec4-d094bdded42a",
  "isSidechain": false,
  "promptId": "745ae244-26b0-401e-950f-101a518ae495",
  "type": "user",
  "uuid": "69f547e3-af33-40e4-896c-10adf73a34ca",
  "toolUseResult": {
    "query": "\"context rot\" OR \"long-context degradation\" decomposition causal factors position bias interference benchmark 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RirFf7cEYxRzGkoVDswmAX",
        "content": [
          {
            "title": "Context Rot: What a 2 AM Night Taught Me That Benchmarks Never Did | by QuangTran | Apr, 2026 | Medium",
            "url": "https://medium.com/@trmquang3103/context-rot-what-a-2-am-night-taught-me-that-benchmarks-never-did-dfda7df72f40"
          },
          {
            "title": "Context rot explained (& how to prevent it)",
            "url": "https://redis.io/blog/context-rot/"
          },
          {
            "title": "Context Rot: Why LLMs Degrade as Context Grows (Complete Guide) | Morph",
            "url": "https://www.morphllm.com/context-rot"
          },
          {
            "title": "Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems",
            "url": "https://arxiv.org/pdf/2411.01101"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 LONG-CONTEXT GENERALIZATION WITH",
            "url": "https://arxiv.org/pdf/2506.16640"
          },
          {
            "title": "Context Degradation in LLMs",
            "url": "https://www.emergentmind.com/topics/context-degradation-in-large-language-models"
          },
          {
            "title": "ChromaDB: Context Rot: Evaluating LLM Performance Degradation with Increasing Input Tokens - ZenML LLMOps Database",
            "url": "https://www.zenml.io/llmops-database/context-rot-evaluating-llm-performance-degradation-with-increasing-input-tokens"
          },
          {
            "title": "Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs",
            "url": "https://arxiv.org/pdf/2410.14641"
          }
        ]
      },
      "I found recent research on context rot and long-context degradation. Here's what the search results show:\n\n## Overview of Context Rot\n\nContext rot is the performance degradation that happens when LLMs have to process increasingly long input contexts, where performance degrades when searching through longer contexts to find relevant information even though that information is technically available in the context window.\n\n## Causal Factors\n\nThe research identifies several decomposed causal factors:\n\n**Position Bias:**\nThe problem shows up through positional bias patterns, with models working best when relevant information sits at the beginning or end of the context window but struggling when information is buried in the middle. Recent work distinguishes between absolute positions (location within entire context) and relative positions (distribution and distance between multiple relevant information pieces).\n\n**Distractor Interference:**\nChroma's study isolated distractor interference as a third mechanism that compounds the first two. Recency bias leads to effective forgetting of earlier facts, especially under in-context interference.\n\n**Structural Effects:**\nModels performed better on shuffled haystacks than on logically coherent documents, suggesting the attention mechanism is negatively influenced by logical document flow, possibly because coherent text creates more plausible-seeming distractors.\n\n## Recent Benchmarks (2026)\n\nChroma Research published a report in July 2025 testing 18 leading models (GPT-4.1, Claude 4, Gemini 2.5, Qwen3, variants) on tasks extended from Needle-in-the-Haystack. The study demonstrates that factors like needle-question similarity, presence of distractors, haystack structure, and semantic relationships all impact performance non-uniformly as context length grows.\n\nLONGPIBENCH is a benchmark designed to assess positional bias involving multiple pieces of relevant information."
    ],
    "durationSeconds": 12.698839678999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2ac2374c-7ff3-432c-9ec4-d094bdded42a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T04:55:12.840Z_

```json
{
  "parentUuid": "69f547e3-af33-40e4-896c-10adf73a34ca",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "26d7de76-b106-41fb-b6c1-3c6979a9a04c",
  "timestamp": "2026-05-20T04:55:12.840Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-20T04:55:18.338Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y7CWC664ATSKYWmtocBDhU`</summary>

```json
{
  "query": "Dual-Process interference LLMs proactive retroactive arXiv 2603.00270 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26d7de76-b106-41fb-b6c1-3c6979a9a04c",
  "isSidechain": false,
  "requestId": "req_011CbDE186SXCA3r47jzC72r",
  "type": "assistant",
  "uuid": "9c5d83cb-844f-4af0-824f-74ab0a1c8311",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5Dd9qUp2scNMtikCz85Yc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1045,
      "cache_read_input_tokens": 25164,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1045,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 25164,
          "cache_creation_input_tokens": 1045,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1045
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

_source line 31 · 2026-05-20T04:55:24.901Z_

<details><summary>↩ Tool result · `toolu_01Y7CWC664ATSKYWmtocBDhU`</summary>

```text
Web search results for query: "Dual-Process interference LLMs proactive retroactive arXiv 2603.00270 2026"

Links: [{"title":"Transformers Remember First, Forget Last: Dual-Process Interference in LLMs","url":"https://arxiv.org/html/2603.00270v1"},{"title":"(PDF) Transformers Remember First, Forget Last: Dual-Process Interference in LLMs","url":"https://www.researchgate.net/publication/401469380_Transformers_Remember_First_Forget_Last_Dual-Process_Interference_in_LLMs"},{"title":"[2603.00270] Transformers Remember First, Forget Last: Dual-Process Interference in LLMs","url":"https://arxiv.org/abs/2603.00270"},{"title":"Transformers Remember First, Forget Last: Dual-Process Interference in LLMs","url":"https://arxiv.org/pdf/2603.00270"},{"title":"Transformers Remember First, Forget Last: Dual-Process Interference in LLMs | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.00270"},{"title":"Learning to Forget: Sleep-Inspired Memory Consolidation for Resolving Proactive Interference in Large Language Models","url":"https://arxiv.org/html/2603.14517"},{"title":"[2603.14517] Learning to Forget: Sleep-Inspired Memory Consolidation for Resolving Proactive Interference in Large Language Models","url":"https://arxiv.org/abs/2603.14517"}]

I found the paper you were searching for. Here are the key findings:

## Paper Overview

"Transformers Remember First, Forget Last: Dual-Process Interference in LLMs" (arXiv:2603.00270) addresses the question of which memories survive when large language models encounter conflicting information in context—early or recent ones.

## Key Findings

The researchers adapted classical interference paradigms from cognitive psychology to test 39 LLMs across diverse architectures and scales. Every model showed the same pattern: proactive interference (PI) dominates retroactive interference (RI) universally (Cohen's d = 1.73, p < 0.0001), meaning early encodings are protected at the cost of recent information—the opposite of human memory, where RI typically dominates.

## Separate Memory Mechanisms

Three findings indicate that RI and PI reflect separate memory mechanisms. RI and PI are uncorrelated (R² = 0.044), rejecting a unified "memory capacity." Model size predicts RI resistance (R² = 0.49) but not PI (R² = 0.06).

The paper was submitted on February 27, 2026, with a revised version on March 19, 2026, by authors Sourav Chattaraj and Kanak Raj from Thomson Reuters.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c5d83cb-844f-4af0-824f-74ab0a1c8311",
  "isSidechain": false,
  "promptId": "745ae244-26b0-401e-950f-101a518ae495",
  "type": "user",
  "uuid": "d146c31e-0fa1-4d2d-8dd6-a06c6d958944",
  "toolUseResult": {
    "query": "Dual-Process interference LLMs proactive retroactive arXiv 2603.00270 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NDpVumUfXgquajBAv1nD2M",
        "content": [
          {
            "title": "Transformers Remember First, Forget Last: Dual-Process Interference in LLMs",
            "url": "https://arxiv.org/html/2603.00270v1"
          },
          {
            "title": "(PDF) Transformers Remember First, Forget Last: Dual-Process Interference in LLMs",
            "url": "https://www.researchgate.net/publication/401469380_Transformers_Remember_First_Forget_Last_Dual-Process_Interference_in_LLMs"
          },
          {
            "title": "[2603.00270] Transformers Remember First, Forget Last: Dual-Process Interference in LLMs",
            "url": "https://arxiv.org/abs/2603.00270"
          },
          {
            "title": "Transformers Remember First, Forget Last: Dual-Process Interference in LLMs",
            "url": "https://arxiv.org/pdf/2603.00270"
          },
          {
            "title": "Transformers Remember First, Forget Last: Dual-Process Interference in LLMs | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2603.00270"
          },
          {
            "title": "Learning to Forget: Sleep-Inspired Memory Consolidation for Resolving Proactive Interference in Large Language Models",
            "url": "https://arxiv.org/html/2603.14517"
          },
          {
            "title": "[2603.14517] Learning to Forget: Sleep-Inspired Memory Consolidation for Resolving Proactive Interference in Large Language Models",
            "url": "https://arxiv.org/abs/2603.14517"
          }
        ]
      },
      "I found the paper you were searching for. Here are the key findings:\n\n## Paper Overview\n\n\"Transformers Remember First, Forget Last: Dual-Process Interference in LLMs\" (arXiv:2603.00270) addresses the question of which memories survive when large language models encounter conflicting information in context—early or recent ones.\n\n## Key Findings\n\nThe researchers adapted classical interference paradigms from cognitive psychology to test 39 LLMs across diverse architectures and scales. Every model showed the same pattern: proactive interference (PI) dominates retroactive interference (RI) universally (Cohen's d = 1.73, p < 0.0001), meaning early encodings are protected at the cost of recent information—the opposite of human memory, where RI typically dominates.\n\n## Separate Memory Mechanisms\n\nThree findings indicate that RI and PI reflect separate memory mechanisms. RI and PI are uncorrelated (R² = 0.044), rejecting a unified \"memory capacity.\" Model size predicts RI resistance (R² = 0.49) but not PI (R² = 0.06).\n\nThe paper was submitted on February 27, 2026, with a revised version on March 19, 2026, by authors Sourav Chattaraj and Kanak Raj from Thomson Reuters."
    ],
    "durationSeconds": 6.557676118999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9c5d83cb-844f-4af0-824f-74ab0a1c8311",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T04:55:27.601Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D3yZZRfFYcqsaqi8M2GmZG`</summary>

```json
{
  "query": "long-context LLM evaluation benchmark decomposing factors ANOVA variance partition 2025 2026 NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d146c31e-0fa1-4d2d-8dd6-a06c6d958944",
  "isSidechain": false,
  "requestId": "req_011CbDE21e2HZsAWdB2VtDuG",
  "type": "assistant",
  "uuid": "dd7b8c29-0257-4da8-94d7-e735ed579db4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VH2VUnGLSLc5M6US2uuUxz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 26209,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 797,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 26209,
          "cache_creation_input_tokens": 797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 797
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

_source line 33 · 2026-05-20T04:55:35.651Z_

<details><summary>↩ Tool result · `toolu_01D3yZZRfFYcqsaqi8M2GmZG`</summary>

```text
Web search results for query: "long-context LLM evaluation benchmark decomposing factors ANOVA variance partition 2025 2026 NLP"

Links: [{"title":"LIFBench: Evaluating the Instruction Following Performance and Stability of Large Language Models in Long-Context Scenarios","url":"https://arxiv.org/pdf/2411.07037"},{"title":"GitHub - EdinburghNLP/MMLongBench: The official repo of the paper \"MMLongBench Benchmarking Long-Context Vision-Language Models Effectively and Thoroughly\" · GitHub","url":"https://github.com/EdinburghNLP/MMLongBench"},{"title":"AcademicEval: Live Long-Context LLM Benchmark","url":"https://arxiv.org/pdf/2510.17725"},{"title":"Long-Context Language Modeling Benchmarks","url":"https://www.emergentmind.com/topics/long-context-language-modeling-benchmarks"},{"title":"Ada-LEval: Evaluating long-context LLMs with length-adaptable benchmarks","url":"https://arxiv.org/pdf/2404.06480"},{"title":"LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark","url":"https://arxiv.org/pdf/2601.02872"}]

Based on the search results, I found relevant recent research on long-context LLM evaluation benchmarks from 2025-2026:

## Key Benchmarks and Developments

Modern benchmarks such as AcademicEval, LongProc, XL-Bench, LV-Eval, Ada-LEval, BAMBOO, LooGLE, and Ref-Long adopt key construction features including dynamic context scaling that explicitly bucket tasks by context length (e.g., 16K, 32K, 64K, 128K, 256K words/tokens) to enable controlled analysis of length effects.

## Recent 2025-2026 Benchmark Updates

MMLongBench V1.1 was released on February 24, 2026 with enhanced LLM-based evaluation and vLLM support. Additionally, ACADEMICEVAL is a live benchmark to evaluate LLMs over long-context generation tasks that adopts arXiv as its data source and features academic writing tasks on each paper including TITLE, ABSTRACT, INTRODUCTION, and RELATED WORK, each with long-context input and hierarchical abstraction levels.

## Evaluation Approaches

Judge scoring using LLM-as-Judge protocols with explicit rubrics or GPT-4/LLM evaluation provide higher-level, if coarse-grained, rubric scores.

However, I note that while the search results discuss various long-context LLM benchmarks and evaluation approaches from 2025-2026, they do not specifically address variance partition through ANOVA or other statistical decomposition methods for analyzing factors in these benchmarks. The results focus more on benchmark construction and evaluation methodologies rather than the specific statistical analysis you're inquiring about.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd7b8c29-0257-4da8-94d7-e735ed579db4",
  "isSidechain": false,
  "promptId": "745ae244-26b0-401e-950f-101a518ae495",
  "type": "user",
  "uuid": "bd25e035-18e3-4ae0-93fd-6dd7a6db2af6",
  "toolUseResult": {
    "query": "long-context LLM evaluation benchmark decomposing factors ANOVA variance partition 2025 2026 NLP",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SGDjrcU6t5owHUL9WTPwrh",
        "content": [
          {
            "title": "LIFBench: Evaluating the Instruction Following Performance and Stability of Large Language Models in Long-Context Scenarios",
            "url": "https://arxiv.org/pdf/2411.07037"
          },
          {
            "title": "GitHub - EdinburghNLP/MMLongBench: The official repo of the paper \"MMLongBench Benchmarking Long-Context Vision-Language Models Effectively and Thoroughly\" · GitHub",
            "url": "https://github.com/EdinburghNLP/MMLongBench"
          },
          {
            "title": "AcademicEval: Live Long-Context LLM Benchmark",
            "url": "https://arxiv.org/pdf/2510.17725"
          },
          {
            "title": "Long-Context Language Modeling Benchmarks",
            "url": "https://www.emergentmind.com/topics/long-context-language-modeling-benchmarks"
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
      "Based on the search results, I found relevant recent research on long-context LLM evaluation benchmarks from 2025-2026:\n\n## Key Benchmarks and Developments\n\nModern benchmarks such as AcademicEval, LongProc, XL-Bench, LV-Eval, Ada-LEval, BAMBOO, LooGLE, and Ref-Long adopt key construction features including dynamic context scaling that explicitly bucket tasks by context length (e.g., 16K, 32K, 64K, 128K, 256K words/tokens) to enable controlled analysis of length effects.\n\n## Recent 2025-2026 Benchmark Updates\n\nMMLongBench V1.1 was released on February 24, 2026 with enhanced LLM-based evaluation and vLLM support. Additionally, ACADEMICEVAL is a live benchmark to evaluate LLMs over long-context generation tasks that adopts arXiv as its data source and features academic writing tasks on each paper including TITLE, ABSTRACT, INTRODUCTION, and RELATED WORK, each with long-context input and hierarchical abstraction levels.\n\n## Evaluation Approaches\n\nJudge scoring using LLM-as-Judge protocols with explicit rubrics or GPT-4/LLM evaluation provide higher-level, if coarse-grained, rubric scores.\n\nHowever, I note that while the search results discuss various long-context LLM benchmarks and evaluation approaches from 2025-2026, they do not specifically address variance partition through ANOVA or other statistical decomposition methods for analyzing factors in these benchmarks. The results focus more on benchmark construction and evaluation methodologies rather than the specific statistical analysis you're inquiring about."
    ],
    "durationSeconds": 8.045612005000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "dd7b8c29-0257-4da8-94d7-e735ed579db4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs…",
  "leafUuid": "bd25e035-18e3-4ae0-93fd-6dd7a6db2af6",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Factorial analysis of context rot factors in LLMs",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b"
}
```

---

### Tool call

_source line 36 · 2026-05-20T04:55:39.232Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016RXpBiXVzu6pC4ymyUJFMQ`</summary>

```json
{
  "query": "\"When Does Divide and Conquer Work\" long context noise decomposition ICLR 2026 arXiv 2506.16411"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd25e035-18e3-4ae0-93fd-6dd7a6db2af6",
  "isSidechain": false,
  "requestId": "req_011CbDE2ofinMEdLExpLtCLa",
  "type": "assistant",
  "uuid": "80f5843f-845f-4b58-903b-19ac87416355",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8p1dyRLfdUtwRnDYMVS2x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 814,
      "cache_read_input_tokens": 27006,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 27006,
          "cache_creation_input_tokens": 814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 814
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

_source line 37 · 2026-05-20T04:55:45.690Z_

<details><summary>↩ Tool result · `toolu_016RXpBiXVzu6pC4ymyUJFMQ`</summary>

```text
Web search results for query: ""When Does Divide and Conquer Work" long context noise decomposition ICLR 2026 arXiv 2506.16411"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.11057"},{"title":"[2506.16411] When Does Divide and Conquer Work for Long Context LLM? A Noise Decomposition Framework","url":"https://arxiv.org/abs/2506.16411"},{"title":"GitHub - nehzux/DivideConquerAgents: [ICLR 2026] When Does Divide and Conquer Work for Long Context LLM? A Noise Decomposition Framework · GitHub","url":"https://github.com/NehzUx/DivideConquerAgents"},{"title":"When Does Divide and Conquer Work for Long Context LLM? A Noise Decomposition Framework","url":"https://arxiv.org/html/2506.16411"},{"title":"An Examination on the Effectiveness of Divide-and-Conquer Prompting in   Large Language Models","url":"https://arxiv.org/pdf/2402.05359"},{"title":"Divide-and-conquer routing for learning heterogeneous individualized capsules","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12310034/"},{"title":"Training LLMs for Divide-and-Conquer Reasoning Elevates Test-Time Scalability","url":"https://arxiv.org/pdf/2602.02477"}]

Based on the search results, I found the paper you're looking for:

"When Does Divide and Conquer Work for Long Context LLM? A Noise Decomposition Framework" (arXiv:2506.16411) was submitted on June 19, 2025 and last revised on February 28, 2026, with authors including Zhen Xu, Shang Zhu, Jue Wang, Junlin Wang, Ben Athiwaratkun, Chi Wang, James Zou, and Ce Zhang.

The paper proposes a theoretical framework that distinguishes the failure modes of long context tasks into three categories: cross-chunk dependence (task noise), confusion that grows with context size (model noise), and the imperfect integration of partial results (aggregator noise).

Under this framework, the authors analyze when it is effective to use multi-agent chunking—dividing a lengthy sequence into smaller chunks and aggregating the processed results of each chunk—and confirm their theoretical analysis with experiments on tasks such as retrieval, question answering, and summarization.

The paper is available on arXiv at https://arxiv.org/abs/2506.16411, with an associated GitHub repository at https://github.com/NehzUx/DivideConquerAgents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80f5843f-845f-4b58-903b-19ac87416355",
  "isSidechain": false,
  "promptId": "745ae244-26b0-401e-950f-101a518ae495",
  "type": "user",
  "uuid": "9b47065e-f9ab-426b-b975-dee88bee4248",
  "toolUseResult": {
    "query": "\"When Does Divide and Conquer Work\" long context noise decomposition ICLR 2026 arXiv 2506.16411",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PacqqDLDh8JYwYsCZrXPTy",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2602.11057"
          },
          {
            "title": "[2506.16411] When Does Divide and Conquer Work for Long Context LLM? A Noise Decomposition Framework",
            "url": "https://arxiv.org/abs/2506.16411"
          },
          {
            "title": "GitHub - nehzux/DivideConquerAgents: [ICLR 2026] When Does Divide and Conquer Work for Long Context LLM? A Noise Decomposition Framework · GitHub",
            "url": "https://github.com/NehzUx/DivideConquerAgents"
          },
          {
            "title": "When Does Divide and Conquer Work for Long Context LLM? A Noise Decomposition Framework",
            "url": "https://arxiv.org/html/2506.16411"
          },
          {
            "title": "An Examination on the Effectiveness of Divide-and-Conquer Prompting in   Large Language Models",
            "url": "https://arxiv.org/pdf/2402.05359"
          },
          {
            "title": "Divide-and-conquer routing for learning heterogeneous individualized capsules",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12310034/"
          },
          {
            "title": "Training LLMs for Divide-and-Conquer Reasoning Elevates Test-Time Scalability",
            "url": "https://arxiv.org/pdf/2602.02477"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"When Does Divide and Conquer Work for Long Context LLM? A Noise Decomposition Framework\" (arXiv:2506.16411) was submitted on June 19, 2025 and last revised on February 28, 2026, with authors including Zhen Xu, Shang Zhu, Jue Wang, Junlin Wang, Ben Athiwaratkun, Chi Wang, James Zou, and Ce Zhang.\n\nThe paper proposes a theoretical framework that distinguishes the failure modes of long context tasks into three categories: cross-chunk dependence (task noise), confusion that grows with context size (model noise), and the imperfect integration of partial results (aggregator noise).\n\nUnder this framework, the authors analyze when it is effective to use multi-agent chunking—dividing a lengthy sequence into smaller chunks and aggregating the processed results of each chunk—and confirm their theoretical analysis with experiments on tasks such as retrieval, question answering, and summarization.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2506.16411, with an associated GitHub repository at https://github.com/NehzUx/DivideConquerAgents."
    ],
    "durationSeconds": 6.452307932000011,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "80f5843f-845f-4b58-903b-19ac87416355",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-20T04:56:33.114Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough context to evaluate this proposal. Let me synthesize my findings and provide a thorough assessment.

Key findings from my research:

1. **PI-LLM (arXiv:2506.08184)** - Showed log-linear accuracy decline under proactive interference in LLMs. Accepted at ICML 2025 Workshop. Uses synthetic key-value pairs only.

2. **EMB-S (arXiv:2601.20276)** - Showed semantic discrimination is the dominant bottleneck for long-context retrieval at 326M-token scale. Decouples evidence access from usage under semantic interference.


3. **Chroma Research (2025)** - Systematically documented context rot across 18 models with various tasks, published in July 2025.

4. **Dual-Process (arXiv:2603.00270)** - Found proactive interference dominates retrieval interference in LLMs with a large effect size, which is opposite to human memory patterns. The two interference types are uncorrelated, and while model size predicts resistance to retrieval interference, it doesn't predict resistance to proactive interference.

5. **CogniLoad (arXiv:2509.18458)** - A factorial benchmark with tunable length, difficulty, and distractor density, though it lacks controls for position bias and proactive interference load.

6. **Sculptor (arXiv:2508.04664, ICLR 2026)** - Proposes active context management to mitigate proactive interference but doesn't quantify how dominant this effect actually is relative to others.

7. **"When Does Divide and Conquer Work" (arXiv:2506.16411, ICLR 2026)** - Uses a noise decomposition framework to analyze chunking strategies by breaking down failures into task, model, and aggregator noise components.

8. **No existing work** performs a joint factorial decomposition of context rot across interference, position, similarity, and length effects with formal effect sizes.

Now I'm checking whether simpler alternatives would work—existing benchmarks don't simultaneously control all four factors, and while pairwise comparisons are possible, they wouldn't capture the interactions between these dimensions the way a full factorial design would.

The real concern is whether I could just post-hoc analyze existing benchmarks instead of building a new one, but that runs into confounding issues since those benchmarks weren't designed with controlled manipulation of all four factors in mind.

I'm also examining the core assumptions: that these four factors are the primary drivers of context rot, that they're orthogonal enough for factorial ANOVA, and that patterns observed in synthetic settings will generalize to realistic NLP tasks—that last one being particularly important to validate.

The novelty here is the unified factorial decomposition connecting three previously separate research areas, which no existing work does comprehensively. CogniLoad gets closest but only covers two of the factors. It's fundamentally a methodological contribution—a well-executed empirical study applying established experimental design principles to this specific problem rather than introducing algorithmic innovation.

The significance hinges on whether the results would surprise reviewers. If I can cleanly decompose context rot into its constituent factors and show their relative contributions, that's practically valuable for prioritizing mitigation strategies. But the ranking of these factors might not be entirely unexpected.

The related work is solid—I've identified the key papers and clearly positioned the gap. My main concern is that benchmark papers face higher acceptance barriers at top venues unless the findings are genuinely surprising. Since we already know all four factors contribute to context rot, the real value lies in the quantitative breakdown and any unexpected interaction effects that emerge.

I'm estimating this around 25-35% acceptance probability. The methodology is sound and the execution is thorough, but factorial ANOVA is standard practice—the novelty hinges on the findings themselves rather than the approach. The mechanistic analysis with attention entropy and AtP* could strengthen the paper, though it might also feel like an add-on depending on how well it integrates.

Let me refocus on idea quality rather than venue fit. The research question is well-motivated and genuinely useful for understanding context rot mechanisms.

The core issue is that this is fundamentally an empirical decomposition study—the methodology is textbook, and while the research question is solid, the novelty lies in the empirical results rather than any methodological innovation. There's a real risk the paper gets dismissed as "just a benchmark" if the findings align with existing intuitions about interference and similarity being the dominant factors.

That said, the factorial design itself fills a genuine gap in the literature, synthesizing three separate research threads into one coherent framework. The mechanistic analysis goes beyond just reporting numbers, and the practical payoff—actually guiding which mitigation strategies to prioritize—gives the work real value. I'm settling on 25-32% with a midpoint around 28%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b47065e-f9ab-426b-b975-dee88bee4248",
  "isSidechain": false,
  "requestId": "req_011CbDE3YaPyTY7wM4neEytn",
  "type": "assistant",
  "uuid": "b570dd22-78d2-41fc-8ba3-8e4f7fabc3a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HT43QRjsfBjm48d4C7F3wP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 27820,
      "output_tokens": 5508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 792,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5508,
          "cache_read_input_tokens": 27820,
          "cache_creation_input_tokens": 792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 792
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

_source line 39 · 2026-05-20T04:57:56.637Z_

Now I have sufficient research to evaluate this proposal. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- PI-LLM "Unable to Forget" (arXiv:2506.08184, ICML 2025 Workshop ICFM): 最直接的前序工作之一。证明了 LLM 检索准确率在 proactive interference 积累下呈 log-linear 下降，但仅使用合成 key-value 对，未考虑 position bias 或 semantic similarity。
- Dual-Process Interference (arXiv:2603.00270, March 2026): 在 39 个模型上发现 PI 普遍主导 RI（Cohen's d=1.73），PI 和 RI 不相关（R²=0.044），模型规模预测 RI 抗性（R²=0.49）但不预测 PI 抗性（R²=0.06）。关键发现：LLM 与人类记忆模式相反。
- EMB-S (arXiv:2601.20276, Jan 2026): 在 326M-token 尺度上证明 semantic discrimination 而非 context length 是 long-context retrieval 的主要瓶颈。引入了 adversarial NIAH 与 collision-tested hard negatives，但关注 evidence access 退化而非因素分解。
- Chroma Research "Context Rot" (July 2025): 系统测试了 18 个前沿模型在不同上下文长度下的表现退化，发现了非均匀退化模式，但明确声明 mechanistic interpretability "beyond scope"。
- CogniLoad (arXiv:2509.18458, Sep 2025): 最接近的 factorial benchmark——提供 length、difficulty、distractor density 的独立可调控制，但明确不包含 position bias 和 proactive interference load。论文本身承认"current benchmarks do not offer the factorial control needed to disentangle these loads"。
- Sculptor (arXiv:2508.04664, ICLR 2026): 提出 Active Context Management 工具缓解 PI，但隐含假设 PI 是主导因素，未量化 PI 相对于 position bias 或 raw length 的 effect size。
- "When Does Divide and Conquer Work" (arXiv:2506.16411, ICLR 2026): 将 long-context 失败分解为 task noise/model noise/aggregator noise，但针对的是 chunking 策略，不操控 interference 或 position 作为控制变量。
- LongPIBench (arXiv:2410.14641, 2024): 控制了多段相关信息之间的 position 和 distance，但未控制 interference load。
- 调研总结: Context rot 的诊断研究在 2025-2026 年非常活跃，已有多条独立线索（PI、position bias、semantic similarity、raw length）分别被研究，但确实没有工作将这四个因素纳入统一的 factorial 框架进行定量分解。该 proposal 精准定位在这个"连接断裂"的缝隙上。然而，这个方向上的工作密度很高，竞争风险不可忽视。

【Trivial Alternative 检验】:
存在两个值得考虑的 trivial alternative：
1. **Post-hoc 分析已有 benchmark 数据**：理论上可以在 Chroma 或 CogniLoad 等已有 benchmark 上做 post-hoc 回归分析，提取各因素的贡献。但这行不通——已有 benchmark 没有同时控制全部四个因素，post-hoc 分析会受到严重混淆变量的影响。Proposal 在这一点上有合理的增量价值。
2. **逐因素消融而非全 factorial**：可以只做 one-factor-at-a-time 消融实验，成本更低。但 one-factor-at-a-time 无法检测交互效应，而交互效应恰恰是这个研究最可能产生 surprising findings 的地方（例如"high similarity × late position 的交互效应是否远大于各自主效应"）。Factorial 设计的增量价值成立。

结论：trivial alternative 存在但确实无法替代 full factorial 设计，proposal 的增量价值主要在于**交互效应的检测能力**和**统一框架的定量比较**。

【前提假设检验】:
核心 claim 的逻辑链中有以下未经验证的假设：

1. **四因素充分性假设**：Proposal 假定 interference、position、similarity、length 是 context rot 的主要组成因素。但 Chroma 的研究还提到了 haystack 的逻辑结构（coherent vs. shuffled documents 表现不同）、task type 差异等因素。如果遗漏的因素贡献了大量方差，factorial 分解的结论就会误导。这一假设有一定经验支撑（引用的文献确实集中在这四个因素上），但并非铁板钉钉。

2. **因素正交性假设**：3⁴ factorial ANOVA 假设因素可以独立操控。但在自然语言数据中，context length 增加时，semantic similarity 和 interference load 的控制可能变得更困难（128K context 下要精确控制 cosine similarity 在 <0.3 vs >0.85 区间，同时控制 interference load 为 0/3/8，实操难度不小）。如果因素间存在未充分消除的混淆，ANOVA 结果的因果解读就会打折扣。

3. **合成 → 自然迁移假设**：PI-LLM 的 log-linear curve 是在 synthetic key-value retrieval 上观察到的。Proposal 声称用"realistic NLP tasks"（multi-doc QA、entity tracking、temporal reasoning）复现类似效应，但从 synthetic 到 realistic 的迁移并不必然成立。这也是 proposal 声称的贡献之一（验证这个迁移），但如果效应在 realistic tasks 上消失或大幅减弱，论文的 narrative 会受到挑战。

4. **ANOVA 适用性假设**：传统 ANOVA 假设残差正态分布和方差齐性。LLM 在 long context 下的表现分布可能高度非正态（例如 catastrophic failure 导致双峰分布）。Proposal 没有讨论这个统计方法论问题。

【3 维度打分】:

1. **Novelty: 中** — 
   核心贡献是将三条独立研究线索（PI-LLM 的 interference、EMB-S 的 semantic discrimination、Chroma 的 context rot 刻画）纳入统一 factorial 框架进行定量分解。经调研确认，确实没有已发表工作同时操控这四个因素并报告 effect sizes。这是真实的 gap。
   
   但"对已知现象用标准统计方法做定量分解"的 novelty 有天花板。Factorial ANOVA 是经典实验设计方法论，不是方法创新；CogniLoad 已经在做类似的 factorial control（虽然少两个因素）；研究问题的 framing（"哪个因素贡献最大"）是自然且可预期的下一步，而非反直觉的洞察。CogniLoad 甚至在论文中明确呼吁了类似方向（"current benchmarks do not offer the factorial control needed..."），这说明 community 已经意识到这个 gap——proposal 是在回应一个已被识别的需求，而非开辟新方向。

2. **Significance: 中** — 
   研究问题有实际价值：Sculptor（ICLR 2026）在没有量化 PI 相对贡献的情况下就假设 PI 是主导因素并据此设计系统，PI-LLM 和 EMB-S 各自声称自己研究的因素是"dominant bottleneck"——这些互相矛盾的 implicit claims 确实需要一个定量仲裁。
   
   但"surprising"程度有限。如果结果显示"semantic similarity 和 interference 是主导因素，position 和 length 贡献较小"，这与 EMB-S 和 PI-LLM 的已有发现一致，审稿人可能会说"I would have guessed this"。论文的价值取决于交互效应是否揭示非显然模式（如"position 在高 similarity 下变得关键"），但这是结果层面的不确定性，不是 idea 本身的属性。此外，mechanistic analysis（attention entropy + AtP*）增加了一定的深度，但属于锦上添花而非核心贡献。

3. **Related Work: 强** — 
   Related work 覆盖面优秀。经调研验证，引用的关键论文均真实存在且描述准确（PI-LLM arXiv:2506.08184 确实在 ICML 2025 Workshop 发表，Sculptor 确实是 ICLR 2026，Dual-Process arXiv:2603.00270 的 R² 数据与原文一致，CogniLoad arXiv:2509.18458 确实只控制 length/difficulty/distractor 不控制 position 和 PI）。
   
   差异化定位非常清晰：明确指出每个前序工作缺少什么（PI-LLM 只用 synthetic data，Chroma 不控制 interference，EMB-S 不做因素分解，CogniLoad 缺 position 和 PI，Sculptor 假设 PI dominant 但不量化）。还包含了 concurrent work（LongMINT、Cross-Component Interference、SleepGate、Intelligence Degradation），表明对领域动态有持续跟踪。这是该 proposal 最强的维度。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
Related Work 维度达到"强"，说明 proposal 对领域的理解和定位是一流的。但 Novelty 和 Significance 都在"中"——核心方法论（factorial ANOVA）是标准工具的应用而非创新，研究问题是 community 已经意识到的自然下一步（CogniLoad 明确呼吁过），核心发现如果 positive 大概率不会被认为"surprising"。

上界被 **Significance** 限制：这是一篇诊断/分析型论文，其价值高度依赖结果是否揭示反直觉模式。如果交互效应强且出人意料，可以逼近上界；如果主效应排名与已有文献一致（interference > position > length），审稿人会认为这只是量化了已知趋势。

下界被 **Related Work 的充分性** 保护：定位清晰、gap 真实、文献覆盖全面，不太可能被简单地以"already done"拒稿。

额外风险因素：该领域在 2025-2026 年极其活跃（从 PI-LLM、Dual-Process、EMB-S、LongMINT 等论文的密度可见），到 EMNLP 2026 截稿时可能出现直接竞争的工作。

【主要风险】:
1. **"Quantifying the obvious" 风险**：审稿人可能认为"interference 和 similarity 是 context rot 的主要因素"这一结论已被 PI-LLM 和 EMB-S 分别证明，factorial 分解只是给了更精确的数字但没有改变我们的理解——导致"solid but incremental"评价。
2. **Benchmark paper 认知偏见**：纯诊断型 benchmark 论文（不提出新方法、不解决问题、只量化现象）在主会审稿中常被质疑 contribution 是否足够——审稿人可能要求"基于你的分解结果，提出针对性的 mitigation method 并验证"，这会大幅增加工作量。
```

Sources:
- [PI-LLM: Unable to Forget (arXiv:2506.08184)](https://arxiv.org/abs/2506.08184)
- [Dual-Process Interference in LLMs (arXiv:2603.00270)](https://arxiv.org/abs/2603.00270)
- [EMB-S: Beyond the Needle's Illusion (arXiv:2601.20276)](https://arxiv.org/abs/2601.20276)
- [Chroma Research: Context Rot](https://www.trychroma.com/research/context-rot)
- [CogniLoad (arXiv:2509.18458)](https://arxiv.org/abs/2509.18458)
- [Sculptor: Active Context Management (arXiv:2508.04664, ICLR 2026)](https://arxiv.org/abs/2508.04664)
- [When Does Divide and Conquer Work (arXiv:2506.16411, ICLR 2026)](https://arxiv.org/abs/2506.16411)
- [LongPIBench: Distance between Relevant Information Pieces](https://arxiv.org/pdf/2410.14641)
- [Context Rot Overview (Morph)](https://www.morphllm.com/context-rot)
- [LongMINT (arXiv:2605.18565)](https://arxiv.org/abs/2605.18565)
- [SleepGate (arXiv:2603.14517)](https://arxiv.org/abs/2603.14517)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b570dd22-78d2-41fc-8ba3-8e4f7fabc3a9",
  "isSidechain": false,
  "requestId": "req_011CbDE3YaPyTY7wM4neEytn",
  "type": "assistant",
  "uuid": "735de3f4-53cf-4960-90f5-d88ce9800316",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HT43QRjsfBjm48d4C7F3wP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 27820,
      "output_tokens": 5508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 792,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5508,
          "cache_read_input_tokens": 27820,
          "cache_creation_input_tokens": 792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 792
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

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs…",
  "leafUuid": "735de3f4-53cf-4960-90f5-d88ce9800316",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Factorial analysis of context rot factors in LLMs",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Decomposing Context Rot: A Factorial Analysis of Interference, Position, and Length Effects in Long-Context LLMs…",
  "leafUuid": "735de3f4-53cf-4960-90f5-d88ce9800316",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Factorial analysis of context rot factors in LLMs",
  "sessionId": "a9ca1c93-6056-4bd1-a2ea-b979c103d16b"
}
```

---
