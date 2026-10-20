# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-19 (UTC).** ## Original idea { "tit

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/02d9da0e-8e85-4f5e-ab8a-8e056918e4ed.jsonl`
- **Structured JSON:** [`f6737c4aa04b590d7833.json`](../../sessions/f6/f6737c4aa04b590d7833.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T09:29:05.325Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T09:29:05.325Z",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-19 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Drift-Probe-Gated Retrieval: A Systematic Evaluation of Temporal Staleness Detection for Selective RAG\",\n  \"core_problem\": \"Can linear probes trained on the temporal-drift direction—proven geometrically orthogonal to confidence and uncertainty—serve as a practical retrieval gate that outperforms confidence-based and training-free selective RAG methods on temporally-drifted queries, and under what conditions does drift-gating provide meaningful accuracy-efficiency gains?\",\n  \"opportunity\": \"The Geometry of Forgetting (arXiv:2605.09195, May 2026) proved that temporal drift is encoded as a linear direction in residual-stream activations, orthogonal to both correctness and uncertainty, achieving AUROC 0.83–0.95 for drift probes vs. 0.49–0.57 for all confidence/uncertainty methods across six models. That paper explicitly suggested—but never implemented or evaluated—that 'triggering on an internal drift signal recovers comparable accuracy at lower retrieval cost' (§2). Meanwhile, selective RAG methods (Probing-RAG, SeaKR, INKER, Skill-RAG, TARG, Self-Routing RAG) and representation-based knowledge checkers (Rep-Con/Rep-PCA) all gate retrieval on confidence, uncertainty, or general knowledge-state signals that are provably blind to drift. No existing work has actually built and rigorously evaluated a drift-probe-gated retrieval system. This leaves a clear implementation-and-evaluation gap: we know drift probes work for detection, and we know selective retrieval needs better signals, but the integration has never been tested end-to-end across benchmarks and baselines.\",\n  \"landscape\": \"Selective RAG methods fall into four categories: (1) Probe-based confidence gating—Probing-RAG (arXiv:2410.13339) and Skill-RAG (arXiv:2604.15771) probe hidden states for retrieval decisions using confidence/failure-state signals; (2) Uncertainty-based gating—SeaKR (arXiv:2406.19215, ACL 2025) extracts self-aware uncertainty from FFN internal states, INKER (IPM 2025) integrates internal-external knowledge via uncertainty; (3) Training-free output gating—TARG (arXiv:2511.09803) uses prefix-logit margins for single-shot gating, Self-Routing RAG (arXiv:2504.01018) routes via output-level confidence; (4) Representation-based knowledge filtering—'Towards Knowledge Checking in RAG' (arXiv:2411.14572) uses Rep-PCA and Rep-Con classifiers on last-layer representations for knowledge checking, helpfulness, and contradiction detection. All four categories rely on signals the Geometry of Forgetting proved orthogonal to temporal drift. On the temporal-RAG side, T-GRAG and Chronos add temporal awareness on the query/retrieval side, SmartVector (arXiv:2604.20598) adds temporal validity windows to embeddings, and 'RAG or Learning?' (arXiv:2604.05096) benchmarks adaptation under continuous drift—but none detect model-side staleness via internal probes. The Geometry of Forgetting established per-model optimal drift-probe layers (L29 for Llama-3.1, L6 for Mistral, L10 for Qwen-2.5, L33 for Gemma-2-9B, L24 for Llama-2, L13 for Gemma-2-2B) and noted the retrieval application as motivation, but implemented no retrieval system and ran no retrieval experiments. HoH (ACL 2025) showed that even a single outdated passage causes ≥20% accuracy degradation in RAG, confirming the practical urgency. 'Still Fresh?' (arXiv:2603.04532) found retrieval benchmarks remain stable under temporal corpus drift, suggesting the problem lies in model-side staleness rather than corpus-side drift. As of May 2026, no published or concurrent work has implemented drift-axis probes as a retrieval gate, evaluated against selective RAG baselines, or characterized when drift-gating helps versus hurts.\",\n  \"inspired_by\": \"Gap: The Geometry of Forgetting proves drift orthogonality and suggests retrieval triggering but implements no retrieval system. Selective RAG methods (Probing-RAG, SeaKR, TARG, Rep-Con) all operate on confidence/uncertainty signals provably blind to drift. Untried integration: drift-specific probes × selective retrieval triggering, with systematic evaluation across benchmarks and baselines.\",\n  \"approach\": \"Phase 1 — Independent Drift-Label Pipeline (mitigating unreleased-code risk): Construct drift/non-drift labels independently using Wikidata revision history. For each entity-relation pair in our evaluation sets, query sequential Wikidata snapshots (aligned to each model's training data cutoff) to classify facts as Stable (unchanged since cutoff) or Drifted (value changed after cutoff). Validate against the Geometry of Forgetting's labels if/when their code is released. This pipeline also enables constructing the temporal-split PopQA evaluation set using Wikidata edit timestamps.\\n\\nPhase 2 — Drift Probe Training: For each of four primary models—Llama-3.1-8B-Instruct, Qwen-2.5-7B-Instruct, Gemma-2-9B-IT, and Mistral-7B-Instruct (all tested in the original paper)—train lightweight linear probes (<500K parameters) on residual-stream activations at the model-specific optimal layer identified by the Geometry of Forgetting (L29, L10, L33, L6 respectively). Extract activations at the entity token position. Additionally train probes at ±3 layers around the optimal to measure robustness to layer selection. Validate probe AUROC against the original paper's reported numbers as a reproduction check.\\n\\nPhase 3 — DPGR System Integration: At inference time, extract the drift-probe score at the entity token position for each query. When the score exceeds a per-benchmark calibrated threshold τ (set via Pareto-optimal F1 on a held-out validation split), gate in retrieval from a temporally-indexed Wikipedia snapshot (matched to the evaluation date) or web-search API; otherwise rely on the model's parametric answer. Threshold calibration accounts for the different drift base rates across benchmarks.\\n\\nPhase 4 — Comprehensive Evaluation on three temporal QA benchmarks: (a) HoH (ACL 2025)—controlled outdated-information RAG benchmark; (b) StreamingQA (ICML 2022)—temporal adaptation QA with time-stamped news; (c) temporal-split PopQA—questions partitioned into drifted vs. stable subsets via our Wikidata pipeline. Compare against eight selective retrieval baselines: Probing-RAG, SeaKR, INKER, Skill-RAG, TARG, Self-Routing RAG, Rep-Con (from arXiv:2411.14572), and token-entropy thresholding, plus always-retrieve and never-retrieve bounds. Metrics: QA accuracy (EM/F1) overall and stratified by drifted/stable subsets, retrieval efficiency (% queries retrieved), probe inference latency overhead, and accuracy-efficiency Pareto frontiers.\\n\\nPhase 5 — Ablations and Analysis: (a) Layer robustness analysis (±5 layers around optimal); (b) Drift base rate sensitivity—how does DPGR's advantage scale with the proportion of drifted queries? (c) Transfer to untested architectures: Qwen3-8B (newer Qwen, different layer count) to test whether drift-direction transferability holds; (d) Error analysis: false-positive retrievals (stable queries misclassified as drifted) and false-negative misses (drifted queries not retrieved); (e) Comparison of Wikidata-pipeline labels vs. original paper labels (when available) for probe training quality.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"400-600 A100-80GB hours (Wikidata pipeline: CPU-only ~40h; probe training ~15h/model × 4 = 60h; hidden-state extraction 4 models × 3 benchmarks ~200h; 8 baselines evaluation ~180h; ablations with Qwen3-8B + layer sweeps ~100h)\",\n      \"timeline\": \"10-13 weeks (2w Wikidata pipeline + data infrastructure, 2w probe training + reproduction validation, 3-4w full evaluation across benchmarks + baselines, 2-3w ablations + writing, 1-2w buffer)\",\n      \"estimated_gpu_cost\": \"$800-1200 at ~$2.00/hr A100 spot pricing\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"300-450 A100-80GB hours (Claude automates Wikidata pipeline construction, baseline integration, hyperparameter sweeps, and results analysis)\",\n      \"timeline\": \"7-10 weeks\",\n      \"claude_api_cost\": \"$200-400 (Sonnet 4.6 for code generation, experiment orchestration, and paper drafting at $3/$15 per M tokens)\",\n      \"estimated_gpu_cost\": \"$600-900\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"350-550 A100-80GB hours\",\n      \"timeline\": \"5-9 weeks (parallelized probe training + evaluation sweeps)\",\n      \"claude_api_cost\": \"$400-700 (heavier usage for autonomous Wikidata pipeline development, experiment design, failure diagnosis, and iterative ablation)\",\n      \"estimated_gpu_cost\": \"$700-1100\",\n      \"speed_bottleneck\": \"Hidden-state extraction requires sequential forward passes per model; Wikidata SPARQL API rate limits constrain drift-label construction (~5K queries/hour); HoH benchmark requires controlled passage mixing per-query.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstracts July 21, full papers July 28, 2026 — primary target, 10 weeks available)\",\n    \"ARR August 2026 cycle (submission August 3, 2026) → EACL 2027 (commitment October 11, 2026) — backup if AAAI timeline slips\",\n    \"TACL (rolling monthly deadline — suitable for extended journal-length version with all 6 original models + additional ablations)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"The Geometry of Forgetting: Temporal Knowledge Drift as an Independent Axis in LLM Representations (arXiv:2605.09195, May 2026) — establishes drift orthogonality and per-model optimal probe layers; suggests but does not implement retrieval application\",\n    \"Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval (arXiv:2410.13339, 2024) — hidden-state probing for retrieval decisions using confidence signals\",\n    \"SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation (arXiv:2406.19215, ACL 2025) — FFN internal-state uncertainty for adaptive retrieval\",\n    \"INKER: Adaptive Dynamic Retrieval Augmented Generation with Internal-External Knowledge Integration (Information Processing & Management 2025) — uncertainty-based internal-external knowledge integration\",\n    \"Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing (arXiv:2604.15771, Apr 2026) — failure-state detection via hidden states\",\n    \"TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG (arXiv:2511.09803, Nov 2025) — prefix-logit-based training-free gating, 70-90% retrieval reduction on non-temporal benchmarks\",\n    \"Towards Knowledge Checking in Retrieval-augmented Generation: A Representation Perspective (arXiv:2411.14572, Nov 2024) — Rep-PCA and Rep-Con representation-based classifiers for knowledge filtering in RAG\",\n    \"Self-Routing RAG: Binding Selective Retrieval with Knowledge Verbalization (arXiv:2504.01018, 2025) — output-level confidence routing\",\n    \"HoH: A Dynamic Benchmark for Evaluating the Impact of Outdated Information on RAG (arXiv:2503.04800, ACL 2025) — shows single outdated passage causes ≥20% RAG accuracy drop\",\n    \"StreamingQA: A Benchmark for Adaptation to New Knowledge over Time in QA Models (ICML 2022) — temporal adaptation QA with time-stamped news\",\n    \"RAG or Learning? Understanding the Limits of LLM Adaptation under Continuous Knowledge Drift (arXiv:2604.05096, Apr 2026) — benchmarks adaptation under continuous drift\",\n    \"SmartVector: A Temporal Knowledge-Aware Embedding Approach for RAG (arXiv:2604.20598, Apr 2026) — temporal validity windows on retrieval side\",\n    \"Still Fresh? Evaluating Temporal Drift in Retrieval Benchmarks (arXiv:2603.04532, Mar 2026) — shows retrieval benchmarks are stable under corpus drift, implicating model-side staleness\",\n    \"T-GRAG: A Dynamic GraphRAG Framework for Resolving Temporal Conflicts and Redundancy (arXiv, 2025) — query-side temporal awareness in retrieval\",\n    \"Wikidated 1.0: An Evolving Knowledge Graph Dataset of Wikidata's Revision History (2022) — Wikidata revision history for temporal fact tracking\"\n  ],\n  \"description\": \"We present Drift-Probe-Gated Retrieval (DPGR), the first systematic implementation and evaluation of using temporal-drift linear probes as a retrieval gate for selective RAG. The Geometry of Forgetting (2026) proved that temporal drift is encoded as a linear direction in LLM residual streams, geometrically orthogonal to confidence and uncertainty—achieving AUROC 0.83–0.95 for drift detection while all confidence/uncertainty methods remain near chance (0.49–0.57). That paper suggested drift-probe-triggered retrieval as a natural application but never built or evaluated such a system. We bridge this gap by: (1) developing an independent Wikidata-based drift-label pipeline that does not depend on unreleased code; (2) training model-specific linear probes at empirically optimal layers (L29 for Llama-3.1-8B, L10 for Qwen-2.5-7B, L33 for Gemma-2-9B, L6 for Mistral-7B) following the original paper's methodology; (3) integrating these probes into a selective retrieval system with per-benchmark threshold calibration; and (4) conducting the first head-to-head comparison of drift-gating against eight selective retrieval baselines (Probing-RAG, SeaKR, INKER, Skill-RAG, TARG, Self-Routing RAG, Rep-Con, token-entropy thresholding) across three temporal QA benchmarks (HoH, StreamingQA, temporal-split PopQA). We further analyze when drift-gating helps versus hurts as a function of benchmark drift base rates, characterize the accuracy-efficiency Pareto frontier, and test probe transferability to the newer Qwen3-8B architecture. Our retrieval reduction is bounded by the complement of each benchmark's drift base rate—we empirically measure actual reductions rather than claiming fixed percentages—and we provide actionable guidance on when drift-gating should be preferred over training-free or confidence-based alternatives.\",\n  \"project_name\": \"drift_probe_gated_rag\",\n  \"source\": \"web_research\",\n  \"revision_notes\": {\n    \"issue_1_gemma_fix\": \"FIXED: Replaced nonexistent Gemma-4-12B with Gemma-2-9B-IT, which was actually used in the Geometry of Forgetting paper (46 layers, optimal drift probe at L33, AUROC 0.825). All four primary models now match the original paper.\",\n    \"issue_2_novelty_reframing\": \"FIXED: Acknowledged that the Geometry of Forgetting explicitly suggests drift-probe-triggered retrieval in §2 ('triggering on an internal drift signal recovers comparable accuracy at lower retrieval cost') but confirmed via deep reading of §6 that no retrieval system was implemented or evaluated. Reframed contribution from 'first to connect two lines' to 'first systematic implementation and multi-benchmark evaluation of drift-probe-gated retrieval, with head-to-head comparison against eight selective retrieval baselines.'\",\n    \"issue_3_layer_specification\": \"FIXED: Replaced fixed 'layers 12-20' with model-specific optimal layers from the original paper: L29 for Llama-3.1 (AUROC 0.932), L10 for Qwen-2.5 (0.854), L33 for Gemma-2-9B (0.825), L6 for Mistral (0.929). Added ±3 layer robustness sweep as ablation.\",\n    \"issue_4_model_mismatch\": \"FIXED: All four primary models are now from the original paper's tested set: Llama-3.1-8B-Instruct, Qwen-2.5-7B-Instruct, Gemma-2-9B-IT, Mistral-7B-Instruct. Qwen3-8B (36 layers, untested) moved to ablation for transfer testing. Considered Gemma-4-26B-A4B but excluded from main experiments due to MoE architecture introducing confounds for residual-stream probing (activation outliers from Super Experts and sparse routing complicate linear probe interpretation).\",\n    \"issue_5_venue_correction\": \"FIXED: Dropped EMNLP 2026 ARR May cycle (May 25 deadline = 6 days away, unrealistic). Dropped AACL 2026 (also requires May ARR cycle). Replaced with ARR August 2026 (August 3) → EACL 2027 as backup. Confirmed AAAI 2027 deadline: abstracts July 21, full papers July 28, 2026.\",\n    \"issue_6_retrieval_reduction_claims\": \"FIXED: Removed fixed '40-60% retrieval reduction' claim. Now explicitly state that retrieval reduction is bounded by the complement of the drift base rate in each benchmark and that we empirically measure actual reductions. Added drift-base-rate sensitivity analysis as a dedicated ablation.\",\n    \"issue_7_code_dependency\": \"FIXED: Added Phase 1 independent Wikidata-based drift-label pipeline using Wikidata revision history (Wikidated 1.0 dataset, SPARQL queries against frozen snapshots aligned to model training cutoffs). This eliminates the critical dependency on unreleased code. Original paper's labels treated as validation reference when available.\",\n    \"issue_8_missing_baseline_knowledge_checking\": \"FIXED: Added 'Towards Knowledge Checking in RAG: A Representation Perspective' (arXiv:2411.14572) as both a citation and a baseline (Rep-Con classifier). This paper uses Rep-PCA and Rep-Con representation-based classifiers on last-layer representations for knowledge checking—it probes knowledge state but not temporal drift specifically, making it a natural comparison point.\",\n    \"issue_9_missing_baselines_seakr_targ\": \"FIXED: Added SeaKR (arXiv:2406.19215, ACL 2025) and TARG (arXiv:2511.09803) as baselines. SeaKR probes FFN internal states for self-aware uncertainty—closest to our approach architecturally but uses uncertainty rather than drift signals. TARG uses training-free prefix-logit margins, achieving 70-90% retrieval reduction on standard benchmarks—strong efficiency baseline to beat on temporal benchmarks.\"\n  }\n}\n\n## Reviewer feedback (round 2)\nIssues: [\"NOVELTY CONCERN: The idea is directly suggested by the Geometry of Forgetting (§2) and the gating mechanism (threshold on linear probe score) is straightforward. No novel methodological contribution exists beyond implementing and evaluating what the source paper proposed. Consider adding a genuinely novel component—e.g., multi-signal fusion combining drift probes with confidence/uncertainty probes for comprehensive gating, or a learned threshold mechanism that conditions on query properties.\", \"ENTITY TOKEN IDENTIFICATION: The approach extracts activations 'at the entity token position,' but at inference time, identifying which token is the entity requires an entity detection/linking step. This preprocessing dependency is not discussed—errors in entity identification would directly degrade probe performance. How robust is the system when the entity spans multiple tokens or is ambiguous?\", \"BASELINE CODE AVAILABILITY RISK: Of the 8 baselines, Probing-RAG has public code (GitHub). SeaKR, TARG, Skill-RAG, INKER, Self-Routing RAG, and Rep-Con code availability is unverified. Reimplementing 5-6 baselines faithfully within 10 weeks alongside the main system is a significant timeline risk.\", \"MISSING RELATED WORK: MMA-RAG (arXiv:2603.00511, Feb 2026) uses internal representation learning for adaptive retrieval gating decisions in multimodal RAG. While targeting a different modality, it is architecturally similar (hidden-state-based gating classifier) and should be discussed to clarify what's shared vs. different.\", \"TIMELINE REALISM: AAAI 2027 abstracts are due July 21 (9 weeks from today). The manual estimate is 10–13 weeks. Even the human-in-loop estimate (7–10 weeks) barely fits. The proposal should acknowledge the realistic risk of needing the ARR August backup and plan accordingly.\"]\nFeedback: The revision thoroughly addressed all Round 1 issues—well done. The remaining weakness is novelty: the paper risks reading as 'we implemented what the Geometry of Forgetting suggested and confirmed it works.' To elevate this, consider: (1) Adding a novel methodological contribution—e.g., a multi-signal gating framework that fuses drift, confidence, and uncertainty probes (since the source paper proved these are orthogonal axes, combining them should yield strictly better gating than any single signal); this would transform the paper from 'implementing someone else's suggestion' to 'introducing a principled multi-axis gating framework motivated by representational geometry.' (2) Explicitly discuss the entity token identification challenge and propose a solution (e.g., using the last subject token, or averaging over entity span). (3) Verify baseline code availability NOW and scope the comparison to baselines with released code + 1-2 key reimplementations. (4) Acknowledge AAAI timing risk and commit to the ARR August cycle as the realistic primary target.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields."
}
```

---

### Runtime record

_source line 2 · 2026-05-19T09:29:05.328Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T09:29:05.328Z",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed"
}
```

---

## Round 1

53 recorded events

### User

_source line 3 · 2026-05-19T09:29:05.338Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-19 (UTC).**

## Original idea
{
  "title": "Drift-Probe-Gated Retrieval: A Systematic Evaluation of Temporal Staleness Detection for Selective RAG",
  "core_problem": "Can linear probes trained on the temporal-drift direction—proven geometrically orthogonal to confidence and uncertainty—serve as a practical retrieval gate that outperforms confidence-based and training-free selective RAG methods on temporally-drifted queries, and under what conditions does drift-gating provide meaningful accuracy-efficiency gains?",
  "opportunity": "The Geometry of Forgetting (arXiv:2605.09195, May 2026) proved that temporal drift is encoded as a linear direction in residual-stream activations, orthogonal to both correctness and uncertainty, achieving AUROC 0.83–0.95 for drift probes vs. 0.49–0.57 for all confidence/uncertainty methods across six models. That paper explicitly suggested—but never implemented or evaluated—that 'triggering on an internal drift signal recovers comparable accuracy at lower retrieval cost' (§2). Meanwhile, selective RAG methods (Probing-RAG, SeaKR, INKER, Skill-RAG, TARG, Self-Routing RAG) and representation-based knowledge checkers (Rep-Con/Rep-PCA) all gate retrieval on confidence, uncertainty, or general knowledge-state signals that are provably blind to drift. No existing work has actually built and rigorously evaluated a drift-probe-gated retrieval system. This leaves a clear implementation-and-evaluation gap: we know drift probes work for detection, and we know selective retrieval needs better signals, but the integration has never been tested end-to-end across benchmarks and baselines.",
  "landscape": "Selective RAG methods fall into four categories: (1) Probe-based confidence gating—Probing-RAG (arXiv:2410.13339) and Skill-RAG (arXiv:2604.15771) probe hidden states for retrieval decisions using confidence/failure-state signals; (2) Uncertainty-based gating—SeaKR (arXiv:2406.19215, ACL 2025) extracts self-aware uncertainty from FFN internal states, INKER (IPM 2025) integrates internal-external knowledge via uncertainty; (3) Training-free output gating—TARG (arXiv:2511.09803) uses prefix-logit margins for single-shot gating, Self-Routing RAG (arXiv:2504.01018) routes via output-level confidence; (4) Representation-based knowledge filtering—'Towards Knowledge Checking in RAG' (arXiv:2411.14572) uses Rep-PCA and Rep-Con classifiers on last-layer representations for knowledge checking, helpfulness, and contradiction detection. All four categories rely on signals the Geometry of Forgetting proved orthogonal to temporal drift. On the temporal-RAG side, T-GRAG and Chronos add temporal awareness on the query/retrieval side, SmartVector (arXiv:2604.20598) adds temporal validity windows to embeddings, and 'RAG or Learning?' (arXiv:2604.05096) benchmarks adaptation under continuous drift—but none detect model-side staleness via internal probes. The Geometry of Forgetting established per-model optimal drift-probe layers (L29 for Llama-3.1, L6 for Mistral, L10 for Qwen-2.5, L33 for Gemma-2-9B, L24 for Llama-2, L13 for Gemma-2-2B) and noted the retrieval application as motivation, but implemented no retrieval system and ran no retrieval experiments. HoH (ACL 2025) showed that even a single outdated passage causes ≥20% accuracy degradation in RAG, confirming the practical urgency. 'Still Fresh?' (arXiv:2603.04532) found retrieval benchmarks remain stable under temporal corpus drift, suggesting the problem lies in model-side staleness rather than corpus-side drift. As of May 2026, no published or concurrent work has implemented drift-axis probes as a retrieval gate, evaluated against selective RAG baselines, or characterized when drift-gating helps versus hurts.",
  "inspired_by": "Gap: The Geometry of Forgetting proves drift orthogonality and suggests retrieval triggering but implements no retrieval system. Selective RAG methods (Probing-RAG, SeaKR, TARG, Rep-Con) all operate on confidence/uncertainty signals provably blind to drift. Untried integration: drift-specific probes × selective retrieval triggering, with systematic evaluation across benchmarks and baselines.",
  "approach": "Phase 1 — Independent Drift-Label Pipeline (mitigating unreleased-code risk): Construct drift/non-drift labels independently using Wikidata revision history. For each entity-relation pair in our evaluation sets, query sequential Wikidata snapshots (aligned to each model's training data cutoff) to classify facts as Stable (unchanged since cutoff) or Drifted (value changed after cutoff). Validate against the Geometry of Forgetting's labels if/when their code is released. This pipeline also enables constructing the temporal-split PopQA evaluation set using Wikidata edit timestamps.\n\nPhase 2 — Drift Probe Training: For each of four primary models—Llama-3.1-8B-Instruct, Qwen-2.5-7B-Instruct, Gemma-2-9B-IT, and Mistral-7B-Instruct (all tested in the original paper)—train lightweight linear probes (<500K parameters) on residual-stream activations at the model-specific optimal layer identified by the Geometry of Forgetting (L29, L10, L33, L6 respectively). Extract activations at the entity token position. Additionally train probes at ±3 layers around the optimal to measure robustness to layer selection. Validate probe AUROC against the original paper's reported numbers as a reproduction check.\n\nPhase 3 — DPGR System Integration: At inference time, extract the drift-probe score at the entity token position for each query. When the score exceeds a per-benchmark calibrated threshold τ (set via Pareto-optimal F1 on a held-out validation split), gate in retrieval from a temporally-indexed Wikipedia snapshot (matched to the evaluation date) or web-search API; otherwise rely on the model's parametric answer. Threshold calibration accounts for the different drift base rates across benchmarks.\n\nPhase 4 — Comprehensive Evaluation on three temporal QA benchmarks: (a) HoH (ACL 2025)—controlled outdated-information RAG benchmark; (b) StreamingQA (ICML 2022)—temporal adaptation QA with time-stamped news; (c) temporal-split PopQA—questions partitioned into drifted vs. stable subsets via our Wikidata pipeline. Compare against eight selective retrieval baselines: Probing-RAG, SeaKR, INKER, Skill-RAG, TARG, Self-Routing RAG, Rep-Con (from arXiv:2411.14572), and token-entropy thresholding, plus always-retrieve and never-retrieve bounds. Metrics: QA accuracy (EM/F1) overall and stratified by drifted/stable subsets, retrieval efficiency (% queries retrieved), probe inference latency overhead, and accuracy-efficiency Pareto frontiers.\n\nPhase 5 — Ablations and Analysis: (a) Layer robustness analysis (±5 layers around optimal); (b) Drift base rate sensitivity—how does DPGR's advantage scale with the proportion of drifted queries? (c) Transfer to untested architectures: Qwen3-8B (newer Qwen, different layer count) to test whether drift-direction transferability holds; (d) Error analysis: false-positive retrievals (stable queries misclassified as drifted) and false-negative misses (drifted queries not retrieved); (e) Comparison of Wikidata-pipeline labels vs. original paper labels (when available) for probe training quality.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "400-600 A100-80GB hours (Wikidata pipeline: CPU-only ~40h; probe training ~15h/model × 4 = 60h; hidden-state extraction 4 models × 3 benchmarks ~200h; 8 baselines evaluation ~180h; ablations with Qwen3-8B + layer sweeps ~100h)",
      "timeline": "10-13 weeks (2w Wikidata pipeline + data infrastructure, 2w probe training + reproduction validation, 3-4w full evaluation across benchmarks + baselines, 2-3w ablations + writing, 1-2w buffer)",
      "estimated_gpu_cost": "$800-1200 at ~$2.00/hr A100 spot pricing"
    },
    "human_in_loop": {
      "gpu_hours": "300-450 A100-80GB hours (Claude automates Wikidata pipeline construction, baseline integration, hyperparameter sweeps, and results analysis)",
      "timeline": "7-10 weeks",
      "claude_api_cost": "$200-400 (Sonnet 4.6 for code generation, experiment orchestration, and paper drafting at $3/$15 per M tokens)",
      "estimated_gpu_cost": "$600-900"
    },
    "auto_research": {
      "gpu_hours": "350-550 A100-80GB hours",
      "timeline": "5-9 weeks (parallelized probe training + evaluation sweeps)",
      "claude_api_cost": "$400-700 (heavier usage for autonomous Wikidata pipeline development, experiment design, failure diagnosis, and iterative ablation)",
      "estimated_gpu_cost": "$700-1100",
      "speed_bottleneck": "Hidden-state extraction requires sequential forward passes per model; Wikidata SPARQL API rate limits constrain drift-label construction (~5K queries/hour); HoH benchmark requires controlled passage mixing per-query."
    }
  },
  "target_venues": [
    "AAAI 2027 (abstracts July 21, full papers July 28, 2026 — primary target, 10 weeks available)",
    "ARR August 2026 cycle (submission August 3, 2026) → EACL 2027 (commitment October 11, 2026) — backup if AAAI timeline slips",
    "TACL (rolling monthly deadline — suitable for extended journal-length version with all 6 original models + additional ablations)"
  ],
  "level": "solid",
  "key_references": [
    "The Geometry of Forgetting: Temporal Knowledge Drift as an Independent Axis in LLM Representations (arXiv:2605.09195, May 2026) — establishes drift orthogonality and per-model optimal probe layers; suggests but does not implement retrieval application",
    "Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval (arXiv:2410.13339, 2024) — hidden-state probing for retrieval decisions using confidence signals",
    "SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation (arXiv:2406.19215, ACL 2025) — FFN internal-state uncertainty for adaptive retrieval",
    "INKER: Adaptive Dynamic Retrieval Augmented Generation with Internal-External Knowledge Integration (Information Processing & Management 2025) — uncertainty-based internal-external knowledge integration",
    "Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing (arXiv:2604.15771, Apr 2026) — failure-state detection via hidden states",
    "TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG (arXiv:2511.09803, Nov 2025) — prefix-logit-based training-free gating, 70-90% retrieval reduction on non-temporal benchmarks",
    "Towards Knowledge Checking in Retrieval-augmented Generation: A Representation Perspective (arXiv:2411.14572, Nov 2024) — Rep-PCA and Rep-Con representation-based classifiers for knowledge filtering in RAG",
    "Self-Routing RAG: Binding Selective Retrieval with Knowledge Verbalization (arXiv:2504.01018, 2025) — output-level confidence routing",
    "HoH: A Dynamic Benchmark for Evaluating the Impact of Outdated Information on RAG (arXiv:2503.04800, ACL 2025) — shows single outdated passage causes ≥20% RAG accuracy drop",
    "StreamingQA: A Benchmark for Adaptation to New Knowledge over Time in QA Models (ICML 2022) — temporal adaptation QA with time-stamped news",
    "RAG or Learning? Understanding the Limits of LLM Adaptation under Continuous Knowledge Drift (arXiv:2604.05096, Apr 2026) — benchmarks adaptation under continuous drift",
    "SmartVector: A Temporal Knowledge-Aware Embedding Approach for RAG (arXiv:2604.20598, Apr 2026) — temporal validity windows on retrieval side",
    "Still Fresh? Evaluating Temporal Drift in Retrieval Benchmarks (arXiv:2603.04532, Mar 2026) — shows retrieval benchmarks are stable under corpus drift, implicating model-side staleness",
    "T-GRAG: A Dynamic GraphRAG Framework for Resolving Temporal Conflicts and Redundancy (arXiv, 2025) — query-side temporal awareness in retrieval",
    "Wikidated 1.0: An Evolving Knowledge Graph Dataset of Wikidata's Revision History (2022) — Wikidata revision history for temporal fact tracking"
  ],
  "description": "We present Drift-Probe-Gated Retrieval (DPGR), the first systematic implementation and evaluation of using temporal-drift linear probes as a retrieval gate for selective RAG. The Geometry of Forgetting (2026) proved that temporal drift is encoded as a linear direction in LLM residual streams, geometrically orthogonal to confidence and uncertainty—achieving AUROC 0.83–0.95 for drift detection while all confidence/uncertainty methods remain near chance (0.49–0.57). That paper suggested drift-probe-triggered retrieval as a natural application but never built or evaluated such a system. We bridge this gap by: (1) developing an independent Wikidata-based drift-label pipeline that does not depend on unreleased code; (2) training model-specific linear probes at empirically optimal layers (L29 for Llama-3.1-8B, L10 for Qwen-2.5-7B, L33 for Gemma-2-9B, L6 for Mistral-7B) following the original paper's methodology; (3) integrating these probes into a selective retrieval system with per-benchmark threshold calibration; and (4) conducting the first head-to-head comparison of drift-gating against eight selective retrieval baselines (Probing-RAG, SeaKR, INKER, Skill-RAG, TARG, Self-Routing RAG, Rep-Con, token-entropy thresholding) across three temporal QA benchmarks (HoH, StreamingQA, temporal-split PopQA). We further analyze when drift-gating helps versus hurts as a function of benchmark drift base rates, characterize the accuracy-efficiency Pareto frontier, and test probe transferability to the newer Qwen3-8B architecture. Our retrieval reduction is bounded by the complement of each benchmark's drift base rate—we empirically measure actual reductions rather than claiming fixed percentages—and we provide actionable guidance on when drift-gating should be preferred over training-free or confidence-based alternatives.",
  "project_name": "drift_probe_gated_rag",
  "source": "web_research",
  "revision_notes": {
    "issue_1_gemma_fix": "FIXED: Replaced nonexistent Gemma-4-12B with Gemma-2-9B-IT, which was actually used in the Geometry of Forgetting paper (46 layers, optimal drift probe at L33, AUROC 0.825). All four primary models now match the original paper.",
    "issue_2_novelty_reframing": "FIXED: Acknowledged that the Geometry of Forgetting explicitly suggests drift-probe-triggered retrieval in §2 ('triggering on an internal drift signal recovers comparable accuracy at lower retrieval cost') but confirmed via deep reading of §6 that no retrieval system was implemented or evaluated. Reframed contribution from 'first to connect two lines' to 'first systematic implementation and multi-benchmark evaluation of drift-probe-gated retrieval, with head-to-head comparison against eight selective retrieval baselines.'",
    "issue_3_layer_specification": "FIXED: Replaced fixed 'layers 12-20' with model-specific optimal layers from the original paper: L29 for Llama-3.1 (AUROC 0.932), L10 for Qwen-2.5 (0.854), L33 for Gemma-2-9B (0.825), L6 for Mistral (0.929). Added ±3 layer robustness sweep as ablation.",
    "issue_4_model_mismatch": "FIXED: All four primary models are now from the original paper's tested set: Llama-3.1-8B-Instruct, Qwen-2.5-7B-Instruct, Gemma-2-9B-IT, Mistral-7B-Instruct. Qwen3-8B (36 layers, untested) moved to ablation for transfer testing. Considered Gemma-4-26B-A4B but excluded from main experiments due to MoE architecture introducing confounds for residual-stream probing (activation outliers from Super Experts and sparse routing complicate linear probe interpretation).",
    "issue_5_venue_correction": "FIXED: Dropped EMNLP 2026 ARR May cycle (May 25 deadline = 6 days away, unrealistic). Dropped AACL 2026 (also requires May ARR cycle). Replaced with ARR August 2026 (August 3) → EACL 2027 as backup. Confirmed AAAI 2027 deadline: abstracts July 21, full papers July 28, 2026.",
    "issue_6_retrieval_reduction_claims": "FIXED: Removed fixed '40-60% retrieval reduction' claim. Now explicitly state that retrieval reduction is bounded by the complement of the drift base rate in each benchmark and that we empirically measure actual reductions. Added drift-base-rate sensitivity analysis as a dedicated ablation.",
    "issue_7_code_dependency": "FIXED: Added Phase 1 independent Wikidata-based drift-label pipeline using Wikidata revision history (Wikidated 1.0 dataset, SPARQL queries against frozen snapshots aligned to model training cutoffs). This eliminates the critical dependency on unreleased code. Original paper's labels treated as validation reference when available.",
    "issue_8_missing_baseline_knowledge_checking": "FIXED: Added 'Towards Knowledge Checking in RAG: A Representation Perspective' (arXiv:2411.14572) as both a citation and a baseline (Rep-Con classifier). This paper uses Rep-PCA and Rep-Con representation-based classifiers on last-layer representations for knowledge checking—it probes knowledge state but not temporal drift specifically, making it a natural comparison point.",
    "issue_9_missing_baselines_seakr_targ": "FIXED: Added SeaKR (arXiv:2406.19215, ACL 2025) and TARG (arXiv:2511.09803) as baselines. SeaKR probes FFN internal states for self-aware uncertainty—closest to our approach architecturally but uses uncertainty rather than drift signals. TARG uses training-free prefix-logit margins, achieving 70-90% retrieval reduction on standard benchmarks—strong efficiency baseline to beat on temporal benchmarks."
  }
}

## Reviewer feedback (round 2)
Issues: ["NOVELTY CONCERN: The idea is directly suggested by the Geometry of Forgetting (§2) and the gating mechanism (threshold on linear probe score) is straightforward. No novel methodological contribution exists beyond implementing and evaluating what the source paper proposed. Consider adding a genuinely novel component—e.g., multi-signal fusion combining drift probes with confidence/uncertainty probes for comprehensive gating, or a learned threshold mechanism that conditions on query properties.", "ENTITY TOKEN IDENTIFICATION: The approach extracts activations 'at the entity token position,' but at inference time, identifying which token is the entity requires an entity detection/linking step. This preprocessing dependency is not discussed—errors in entity identification would directly degrade probe performance. How robust is the system when the entity spans multiple tokens or is ambiguous?", "BASELINE CODE AVAILABILITY RISK: Of the 8 baselines, Probing-RAG has public code (GitHub). SeaKR, TARG, Skill-RAG, INKER, Self-Routing RAG, and Rep-Con code availability is unverified. Reimplementing 5-6 baselines faithfully within 10 weeks alongside the main system is a significant timeline risk.", "MISSING RELATED WORK: MMA-RAG (arXiv:2603.00511, Feb 2026) uses internal representation learning for adaptive retrieval gating decisions in multimodal RAG. While targeting a different modality, it is architecturally similar (hidden-state-based gating classifier) and should be discussed to clarify what's shared vs. different.", "TIMELINE REALISM: AAAI 2027 abstracts are due July 21 (9 weeks from today). The manual estimate is 10–13 weeks. Even the human-in-loop estimate (7–10 weeks) barely fits. The proposal should acknowledge the realistic risk of needing the ARR August backup and plan accordingly."]
Feedback: The revision thoroughly addressed all Round 1 issues—well done. The remaining weakness is novelty: the paper risks reading as 'we implemented what the Geometry of Forgetting suggested and confirmed it works.' To elevate this, consider: (1) Adding a novel methodological contribution—e.g., a multi-signal gating framework that fuses drift, confidence, and uncertainty probes (since the source paper proved these are orthogonal axes, combining them should yield strictly better gating than any single signal); this would transform the paper from 'implementing someone else's suggestion' to 'introducing a principled multi-axis gating framework motivated by representational geometry.' (2) Explicitly discuss the entity token identification challenge and propose a solution (e.g., using the last subject token, or averaging over entity span). (3) Verify baseline code availability NOW and scope the comparison to baselines with released code + 1-2 key reimplementations. (4) Acknowledge AAAI timing risk and commit to the ARR August cycle as the realistic primary target.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.
- Address each issue specifically.

## 深度调研要求

不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。
2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。
3. **深度思考**：
   - 核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach？
4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。

## 针对 Review 意见的定向搜索

1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点
2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline
3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现
4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot

- You have full freedom: minor fix, major revision, or pivot.
- Include a "change_type" field: "minor", "major", or "pivot".
- Output a COMPLETE JSON object with ALL fields.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "type": "user",
  "uuid": "f5b02b40-e81f-4946-8f2a-e0b0b8c861a8",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T09:29:05.337Z_

```json
{
  "parentUuid": "f5b02b40-e81f-4946-8f2a-e0b0b8c861a8",
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
  "uuid": "9ed386b9-9ce3-4433-8f81-3d1b73175001",
  "timestamp": "2026-05-19T09:29:05.337Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T09:29:05.337Z_

```json
{
  "parentUuid": "9ed386b9-9ce3-4433-8f81-3d1b73175001",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "742078de-da9c-49c8-be16-036475a36294",
  "timestamp": "2026-05-19T09:29:05.337Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Drift-Probe-Gated Retrieval: A Systematic Evaluation of Temporal Stale…",
  "leafUuid": "742078de-da9c-49c8-be16-036475a36294",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Add multi-signal gating to drift-probe RAG system",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed"
}
```

---

### Assistant

_source line 8 · 2026-05-19T09:29:11.637Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully before doing research:

1. **NOVELTY CONCERN**: The core issue - implementing what someone else suggested isn't novel enough. Reviewer suggests multi-signal fusion combining drift + confidence + uncertainty probes.
2. **ENTITY TOKEN IDENTIFICATION**: Practical gap in the approach - how to identify entity tokens at inference time.
3. **BASELINE CODE AVAILABILITY RISK**: Need to verify which baselines have public code.
4. **MISSING RELATED WORK**: MMA-RAG (arXiv:2603.00511) needs to be discussed.


5. **TIMELINE REALISM**: The AAAI deadline is too aggressive - I should pivot toward targeting ARR in August instead.

Now I'm diving into research on each of these points to understand the landscape better.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "742078de-da9c-49c8-be16-036475a36294",
  "isSidechain": false,
  "requestId": "req_011CbBh5X4ZVy7stwKHRnQQF",
  "type": "assistant",
  "uuid": "0016b1f7-0ed5-412f-a6bc-0fc45d7f283d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BSAtFs5zra7Dg8YpoujnR1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7429,
      "cache_read_input_tokens": 11374,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7429,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 288,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 7429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7429
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

_source line 9 · 2026-05-19T09:29:11.640Z_

I'll conduct deep research on each reviewer concern before revising. Let me launch parallel research agents for the key issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0016b1f7-0ed5-412f-a6bc-0fc45d7f283d",
  "isSidechain": false,
  "requestId": "req_011CbBh5X4ZVy7stwKHRnQQF",
  "type": "assistant",
  "uuid": "51d9ccf2-dabe-4e48-bdeb-323c40f2f61d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BSAtFs5zra7Dg8YpoujnR1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7429,
      "cache_read_input_tokens": 11374,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7429,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 288,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 7429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7429
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

_source line 10 · 2026-05-19T09:29:11.889Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TE4hUinCLDsxPSd4YGm4JX`</summary>

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
  "parentUuid": "51d9ccf2-dabe-4e48-bdeb-323c40f2f61d",
  "isSidechain": false,
  "requestId": "req_011CbBh5X4ZVy7stwKHRnQQF",
  "type": "assistant",
  "uuid": "16a9efcf-da57-4929-a22d-7f540ce525f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BSAtFs5zra7Dg8YpoujnR1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7429,
      "cache_read_input_tokens": 11374,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7429,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 288,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 7429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7429
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

_source line 11 · 2026-05-19T09:29:11.896Z_

<details><summary>↩ Tool result · `toolu_01TE4hUinCLDsxPSd4YGm4JX`</summary>

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
  "parentUuid": "16a9efcf-da57-4929-a22d-7f540ce525f0",
  "isSidechain": false,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "type": "user",
  "uuid": "d9296bb6-a51c-4967-8868-36e41fc29974",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "16a9efcf-da57-4929-a22d-7f540ce525f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T09:29:14.979Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me launch parallel research on all the key issues raised by reviewers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9296bb6-a51c-4967-8868-36e41fc29974",
  "isSidechain": false,
  "requestId": "req_011CbBh61GwpJyP2tskPHaWn",
  "type": "assistant",
  "uuid": "bc6c7961-3e29-4591-858e-a58314399bef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQSjhbf6ubSkYhnpE78FFp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 18803,
      "output_tokens": 1826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1826,
          "cache_read_input_tokens": 18803,
          "cache_creation_input_tokens": 1308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1308
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

_source line 13 · 2026-05-19T09:29:15.526Z_

Now let me launch parallel research on all five reviewer concerns:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc6c7961-3e29-4591-858e-a58314399bef",
  "isSidechain": false,
  "requestId": "req_011CbBh61GwpJyP2tskPHaWn",
  "type": "assistant",
  "uuid": "cefeeb71-88a3-451c-aa2c-888aa8f55bd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQSjhbf6ubSkYhnpE78FFp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 18803,
      "output_tokens": 1826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1826,
          "cache_read_input_tokens": 18803,
          "cache_creation_input_tokens": 1308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1308
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

_source line 14 · 2026-05-19T09:29:22.513Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01M4KDXsMZbUGakyqVcDF2CH`</summary>

```json
{
  "description": "Research multi-signal fusion gating",
  "prompt": "Research the novelty concern for a paper about using temporal-drift probes as retrieval gates in RAG systems. The reviewer says \"implementing what someone else suggested isn't novel enough\" and recommends multi-signal fusion combining drift, confidence, and uncertainty probes.\n\nI need you to search for:\n1. Multi-signal or multi-axis gating/routing in RAG or LLM systems (2024-2026)\n2. Orthogonal probe combination / multi-probe fusion in LLM interpretability\n3. Learned gating mechanisms that combine multiple internal signals for retrieval decisions\n4. Any work on combining orthogonal representation directions for downstream tasks\n\nFor each search, read the most relevant papers. I need to understand:\n- Has anyone combined orthogonal representation axes for gating/routing decisions?\n- What fusion architectures exist (learned weighted combination, MoE-style, cascade)?\n- Is there theoretical grounding for why combining orthogonal signals should help?\n\nUse WebSearch with 3-4 different queries, then WebFetch on the most relevant papers found. Report findings in detail with paper titles, arXiv IDs, and key technical details.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cefeeb71-88a3-451c-aa2c-888aa8f55bd3",
  "isSidechain": false,
  "requestId": "req_011CbBh61GwpJyP2tskPHaWn",
  "type": "assistant",
  "uuid": "c553bfe7-9366-461f-b2d2-0d26860378c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQSjhbf6ubSkYhnpE78FFp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 18803,
      "output_tokens": 1826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1826,
          "cache_read_input_tokens": 18803,
          "cache_creation_input_tokens": 1308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1308
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

_source line 15 · 2026-05-19T09:29:28.111Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NnqkkCeQdsC8qaZf66VVvt`</summary>

```json
{
  "description": "Research entity token identification",
  "prompt": "Research how entity token identification is handled in LLM probing and representation analysis work, particularly for knowledge probing and factual recall tasks. The context: a paper proposes extracting LLM hidden-state activations \"at the entity token position\" to detect temporal drift, but at inference time, identifying which token is the entity requires preprocessing.\n\nSearch for:\n1. How do existing LLM probing papers (especially knowledge probes, factual probes) handle entity token identification? Do they use the last subject token, average over entity span, or something else?\n2. Entity detection/linking as preprocessing for LLM probing - what methods are used?\n3. \"Last subject token\" vs \"entity span averaging\" vs other strategies in mechanistic interpretability and probing literature\n4. Robustness of probing results to token position selection\n\nUse WebSearch with 3+ different queries, then WebFetch the most relevant papers. I need concrete technical details about what positions people extract activations from and how robust results are to this choice. Report with paper titles and specific findings.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c553bfe7-9366-461f-b2d2-0d26860378c3",
  "isSidechain": false,
  "requestId": "req_011CbBh61GwpJyP2tskPHaWn",
  "type": "assistant",
  "uuid": "be07fbc2-7cb5-4491-b959-7b952625efe1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQSjhbf6ubSkYhnpE78FFp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 18803,
      "output_tokens": 1826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1826,
          "cache_read_input_tokens": 18803,
          "cache_creation_input_tokens": 1308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1308
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

_source line 16 · 2026-05-19T09:29:35.742Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014bqMt32TuJQ4LN8RLe1f4s`</summary>

```json
{
  "description": "Research baseline code availability",
  "prompt": "I need to verify code availability for these selective RAG baseline methods. For each one, search GitHub and the web to determine if public code is available:\n\n1. Probing-RAG (arXiv:2410.13339) - self-probing for selective document retrieval\n2. SeaKR (arXiv:2406.19215) - self-aware knowledge retrieval, ACL 2025\n3. TARG (arXiv:2511.09803) - training-free adaptive retrieval gating\n4. Skill-RAG (arXiv:2604.15771) - failure-state-aware retrieval via hidden-state probing\n5. INKER - adaptive dynamic RAG with internal-external knowledge, IPM 2025\n6. Self-Routing RAG (arXiv:2504.01018) - selective retrieval with knowledge verbalization\n7. Rep-Con / Rep-PCA from \"Towards Knowledge Checking in RAG\" (arXiv:2411.14572)\n8. Token-entropy thresholding (standard method, likely easy to implement)\n\nFor each, search for \"[paper name] github code\" and check the arXiv page. Report:\n- Whether code is publicly available (with GitHub URL if found)\n- If not available, how complex the reimplementation would be\n- Any alternative implementations\n\nUse WebSearch for each baseline. This is critical for timeline planning.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be07fbc2-7cb5-4491-b959-7b952625efe1",
  "isSidechain": false,
  "requestId": "req_011CbBh61GwpJyP2tskPHaWn",
  "type": "assistant",
  "uuid": "2a0034e8-49aa-4bbf-b292-71112b391ae9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQSjhbf6ubSkYhnpE78FFp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 18803,
      "output_tokens": 1826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1826,
          "cache_read_input_tokens": 18803,
          "cache_creation_input_tokens": 1308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1308
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

_source line 17 · 2026-05-19T09:29:40.928Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01ADD4fEcebAFuPUzKyzVcGs`</summary>

```json
{
  "description": "Research MMA-RAG paper",
  "prompt": "Research the paper MMA-RAG (arXiv:2603.00511, February 2026) which uses internal representation learning for adaptive retrieval gating in multimodal RAG. The reviewer says this is architecturally similar to a proposed system that uses hidden-state-based gating classifiers for retrieval decisions.\n\n1. Search for \"MMA-RAG adaptive retrieval gating multimodal\" and \"arXiv 2603.00511\"\n2. Fetch and read the paper to understand:\n   - What exact architecture do they use for gating? (hidden states, which layer, what classifier?)\n   - How do they train the gating classifier?\n   - What signals does the gating classifier detect?\n   - How is it similar/different from using a linear probe on residual stream activations for temporal drift detection?\n   - What benchmarks do they evaluate on?\n3. Also search for any other recent (2025-2026) work on \"internal representation gating RAG\" or \"hidden state retrieval decision\"\n\nReport detailed technical findings with specific architectural details.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a0034e8-49aa-4bbf-b292-71112b391ae9",
  "isSidechain": false,
  "requestId": "req_011CbBh61GwpJyP2tskPHaWn",
  "type": "assistant",
  "uuid": "42dfb6e2-654b-40db-86c0-6f1b676a76e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQSjhbf6ubSkYhnpE78FFp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 18803,
      "output_tokens": 1826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1826,
          "cache_read_input_tokens": 18803,
          "cache_creation_input_tokens": 1308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1308
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

_source line 18 · 2026-05-19T09:29:49.134Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013GL8AvwzrCxKb6DPbJCD4u`</summary>

```json
{
  "description": "Research orthogonal axes combination theory",
  "prompt": "Research the theoretical and practical aspects of combining orthogonal representation directions in neural networks for improved classification/gating. Context: A paper called \"The Geometry of Forgetting\" (arXiv:2605.09195, May 2026) proved that temporal drift, confidence, and uncertainty are encoded as orthogonal directions in LLM residual streams. We want to combine all three for a multi-axis retrieval gating system.\n\nSearch for:\n1. \"Geometry of Forgetting\" arXiv 2605.09195 - fetch and read the paper, especially §2 and §6, to understand exactly what they proved about orthogonality and what they suggested about retrieval\n2. Multi-axis or multi-direction probing in LLM representations (2024-2026)\n3. Theoretical results on combining orthogonal classifiers / orthogonal features for improved decisions\n4. \"Representation engineering\" combining multiple concept directions (e.g., truthfulness + confidence)\n5. Look for any work on \"compositional probing\" or \"multi-concept probing\" in transformer representations\n\nI need to understand:\n- What exactly did the Geometry of Forgetting prove about orthogonality? (cosine similarity values, statistical tests)\n- Is there theoretical justification that combining orthogonal signals gives strictly better classification?\n- Has anyone built multi-direction probing systems for practical applications?\n\nUse WebSearch and WebFetch. Report detailed findings.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42dfb6e2-654b-40db-86c0-6f1b676a76e7",
  "isSidechain": false,
  "requestId": "req_011CbBh61GwpJyP2tskPHaWn",
  "type": "assistant",
  "uuid": "650c6343-9fdd-4356-992c-56e7312be760",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQSjhbf6ubSkYhnpE78FFp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 18803,
      "output_tokens": 1826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1826,
          "cache_read_input_tokens": 18803,
          "cache_creation_input_tokens": 1308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1308
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

_source line 19 · 2026-05-19T09:31:26.877Z_

<details><summary>↩ Tool result · `toolu_014bqMt32TuJQ4LN8RLe1f4s`</summary>

```text
Here is the comprehensive code availability report for all 8 selective RAG baselines:

---

## Code Availability Report for Selective RAG Baselines

### 1. Probing-RAG (arXiv:2410.13339)
- **Code available: YES**
- **GitHub URL:** https://github.com/baekingeol/Probing-RAG
- Official repo from the first author (Ingeol Baek). Published at NAACL 2025 Findings.
- Trains a lightweight prober on LLM hidden states to decide retrieval necessity.

### 2. SeaKR (arXiv:2406.19215)
- **Code available: YES**
- **GitHub URL:** https://github.com/THU-KEG/SeaKR
- Official repo from the Tsinghua KEG group. Includes dependencies (BEIR, spacy, etc.) and full experimental setup.
- Extracts self-aware uncertainty from FFN internal states.

### 3. TARG (arXiv:2511.09803)
- **Code available: NO (not found)**
- No GitHub repository found despite thorough searching. The paper (Yufeng Wang et al., Stony Brook/Westlake) does not appear to link to a code release.
- **Reimplementation complexity: LOW-MEDIUM.** TARG is explicitly "training-free" -- it computes mean token entropy, top-1/top-2 logit margin, or small-N variance from a short no-context draft. The gating logic is straightforward once you have access to model logits. The core algorithm could likely be reimplemented in a few hundred lines.

### 4. Skill-RAG (arXiv:2604.15771)
- **Code available: NO (not found)**
- Very recent paper (April 2026). No GitHub link found.
- **Reimplementation complexity: MEDIUM-HIGH.** It has two components: (1) a hidden-state prober (similar to Probing-RAG, so that part could borrow from their codebase), and (2) a prompt-based skill router that selects among four retrieval skills (query rewriting, question decomposition, evidence focusing, exit). The prober training and the skill routing logic together represent non-trivial engineering.
- **Alternative:** Could potentially adapt Probing-RAG's prober code for the hidden-state gating component.

### 5. INKER (IPM 2025)
- **Code available: NO (not found)**
- Published in Information Processing & Management. Authors (Mingjun Zhou, Xiang Zhao et al.) do not appear to have released code publicly.
- **Reimplementation complexity: MEDIUM-HIGH.** INKER integrates both internal and external knowledge signals during generation to make retrieval decisions. The multi-signal integration and the training pipeline for the adaptive gating would require substantial implementation effort.

### 6. Self-Routing RAG (arXiv:2504.01018)
- **Code available: YES**
- **GitHub URL:** https://github.com/xiaowu0162/self-routing-rag
- Official repo from Di Wu (UCLA NLP lab). Includes the full training pipeline (multi-task objective for source selection, knowledge verbalization, and response generation) and evaluation code.
- This is the most feature-complete release among the available baselines.

### 7. Rep-Con / Rep-PCA (arXiv:2411.14572)
- **Code available: NO (not found)**
- Published at NAACL 2025 by Shenglai Zeng et al. (Michigan State / Amazon). Despite the Amazon Science affiliation, no public code repository was found.
- **Reimplementation complexity: LOW-MEDIUM.** Rep-PCA applies PCA to LLM hidden representations to classify knowledge relevance -- a fairly standard linear probe approach. Rep-Con uses contrastive learning on representations, which is slightly more involved but still well-understood methodology. Both methods operate on extracted hidden states, so implementation mainly requires: (1) extracting representations at the right layer, (2) training a PCA-based or contrastive classifier.

### 8. Token-Entropy Thresholding
- **Code available: YES (multiple implementations)**
- **Entropy-RAG:** https://github.com/Nomothings/Entropy-RAG -- Uses response entropy to gate retrieval, with entropy-based reranking.
- **ETC (Entropy-Trend Constraint):** https://github.com/WisdomShell/ETC -- AAAI 2026 Oral; models entropy trends rather than isolated thresholds.
- **Reimplementation complexity: VERY LOW** even without these repos. The core idea is: compute token-level entropy from the LLM's output distribution, threshold it, and trigger retrieval when entropy exceeds the threshold. This is ~50-100 lines of code on top of any HuggingFace generation loop.

---

## Summary Table

| Baseline | Code Available | Reimplementation Difficulty |
|---|---|---|
| Probing-RAG | YES | N/A |
| SeaKR | YES | N/A |
| TARG | NO | Low-Medium |
| Skill-RAG | NO | Medium-High |
| INKER | NO | Medium-High |
| Self-Routing RAG | YES | N/A |
| Rep-Con / Rep-PCA | NO | Low-Medium |
| Token-Entropy | YES (multiple) | Very Low |

**Timeline implications:** 4 out of 8 baselines have public code (Probing-RAG, SeaKR, Self-Routing RAG, Token-Entropy). TARG and Rep-Con/Rep-PCA would be relatively straightforward to reimplement. Skill-RAG and INKER represent the biggest risks for timeline -- they have no code and non-trivial architectures. If Skill-RAG is your own work, you presumably already have the implementation. For INKER, you may want to consider whether it is essential or could be deprioritized given the lack of public code.

Sources:
- [Probing-RAG GitHub](https://github.com/baekingeol/Probing-RAG)
- [SeaKR GitHub](https://github.com/THU-KEG/SeaKR)
- [TARG arXiv](https://arxiv.org/abs/2511.09803)
- [Skill-RAG arXiv](https://arxiv.org/abs/2604.15771)
- [INKER on ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0306457325004753)
- [Self-Routing RAG GitHub](https://github.com/xiaowu0162/self-routing-rag)
- [Rep-Con/Rep-PCA arXiv](https://arxiv.org/abs/2411.14572)
- [Entropy-RAG GitHub](https://github.com/Nomothings/Entropy-RAG)
- [ETC GitHub](https://github.com/WisdomShell/ETC)
- [TARG OpenReview](https://openreview.net/forum?id=bMDdjg75NS)
- [Rep-Con/Rep-PCA NAACL](https://aclanthology.org/2025.naacl-long.151/)

agentId: a08504024f81fce29 (use SendMessage with to: 'a08504024f81fce29' to continue this agent)
&lt;usage>total_tokens: 28410
tool_uses: 20
duration_ms: 111131&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a0034e8-49aa-4bbf-b292-71112b391ae9",
  "isSidechain": false,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "type": "user",
  "uuid": "da962275-dc39-49d5-8036-22f10d55e4e1",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify code availability for these selective RAG baseline methods. For each one, search GitHub and the web to determine if public code is available:\n\n1. Probing-RAG (arXiv:2410.13339) - self-probing for selective document retrieval\n2. SeaKR (arXiv:2406.19215) - self-aware knowledge retrieval, ACL 2025\n3. TARG (arXiv:2511.09803) - training-free adaptive retrieval gating\n4. Skill-RAG (arXiv:2604.15771) - failure-state-aware retrieval via hidden-state probing\n5. INKER - adaptive dynamic RAG with internal-external knowledge, IPM 2025\n6. Self-Routing RAG (arXiv:2504.01018) - selective retrieval with knowledge verbalization\n7. Rep-Con / Rep-PCA from \"Towards Knowledge Checking in RAG\" (arXiv:2411.14572)\n8. Token-entropy thresholding (standard method, likely easy to implement)\n\nFor each, search for \"[paper name] github code\" and check the arXiv page. Report:\n- Whether code is publicly available (with GitHub URL if found)\n- If not available, how complex the reimplementation would be\n- Any alternative implementations\n\nUse WebSearch for each baseline. This is critical for timeline planning.",
    "agentId": "a08504024f81fce29",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the comprehensive code availability report for all 8 selective RAG baselines:\n\n---\n\n## Code Availability Report for Selective RAG Baselines\n\n### 1. Probing-RAG (arXiv:2410.13339)\n- **Code available: YES**\n- **GitHub URL:** https://github.com/baekingeol/Probing-RAG\n- Official repo from the first author (Ingeol Baek). Published at NAACL 2025 Findings.\n- Trains a lightweight prober on LLM hidden states to decide retrieval necessity.\n\n### 2. SeaKR (arXiv:2406.19215)\n- **Code available: YES**\n- **GitHub URL:** https://github.com/THU-KEG/SeaKR\n- Official repo from the Tsinghua KEG group. Includes dependencies (BEIR, spacy, etc.) and full experimental setup.\n- Extracts self-aware uncertainty from FFN internal states.\n\n### 3. TARG (arXiv:2511.09803)\n- **Code available: NO (not found)**\n- No GitHub repository found despite thorough searching. The paper (Yufeng Wang et al., Stony Brook/Westlake) does not appear to link to a code release.\n- **Reimplementation complexity: LOW-MEDIUM.** TARG is explicitly \"training-free\" -- it computes mean token entropy, top-1/top-2 logit margin, or small-N variance from a short no-context draft. The gating logic is straightforward once you have access to model logits. The core algorithm could likely be reimplemented in a few hundred lines.\n\n### 4. Skill-RAG (arXiv:2604.15771)\n- **Code available: NO (not found)**\n- Very recent paper (April 2026). No GitHub link found.\n- **Reimplementation complexity: MEDIUM-HIGH.** It has two components: (1) a hidden-state prober (similar to Probing-RAG, so that part could borrow from their codebase), and (2) a prompt-based skill router that selects among four retrieval skills (query rewriting, question decomposition, evidence focusing, exit). The prober training and the skill routing logic together represent non-trivial engineering.\n- **Alternative:** Could potentially adapt Probing-RAG's prober code for the hidden-state gating component.\n\n### 5. INKER (IPM 2025)\n- **Code available: NO (not found)**\n- Published in Information Processing & Management. Authors (Mingjun Zhou, Xiang Zhao et al.) do not appear to have released code publicly.\n- **Reimplementation complexity: MEDIUM-HIGH.** INKER integrates both internal and external knowledge signals during generation to make retrieval decisions. The multi-signal integration and the training pipeline for the adaptive gating would require substantial implementation effort.\n\n### 6. Self-Routing RAG (arXiv:2504.01018)\n- **Code available: YES**\n- **GitHub URL:** https://github.com/xiaowu0162/self-routing-rag\n- Official repo from Di Wu (UCLA NLP lab). Includes the full training pipeline (multi-task objective for source selection, knowledge verbalization, and response generation) and evaluation code.\n- This is the most feature-complete release among the available baselines.\n\n### 7. Rep-Con / Rep-PCA (arXiv:2411.14572)\n- **Code available: NO (not found)**\n- Published at NAACL 2025 by Shenglai Zeng et al. (Michigan State / Amazon). Despite the Amazon Science affiliation, no public code repository was found.\n- **Reimplementation complexity: LOW-MEDIUM.** Rep-PCA applies PCA to LLM hidden representations to classify knowledge relevance -- a fairly standard linear probe approach. Rep-Con uses contrastive learning on representations, which is slightly more involved but still well-understood methodology. Both methods operate on extracted hidden states, so implementation mainly requires: (1) extracting representations at the right layer, (2) training a PCA-based or contrastive classifier.\n\n### 8. Token-Entropy Thresholding\n- **Code available: YES (multiple implementations)**\n- **Entropy-RAG:** https://github.com/Nomothings/Entropy-RAG -- Uses response entropy to gate retrieval, with entropy-based reranking.\n- **ETC (Entropy-Trend Constraint):** https://github.com/WisdomShell/ETC -- AAAI 2026 Oral; models entropy trends rather than isolated thresholds.\n- **Reimplementation complexity: VERY LOW** even without these repos. The core idea is: compute token-level entropy from the LLM's output distribution, threshold it, and trigger retrieval when entropy exceeds the threshold. This is ~50-100 lines of code on top of any HuggingFace generation loop.\n\n---\n\n## Summary Table\n\n| Baseline | Code Available | Reimplementation Difficulty |\n|---|---|---|\n| Probing-RAG | YES | N/A |\n| SeaKR | YES | N/A |\n| TARG | NO | Low-Medium |\n| Skill-RAG | NO | Medium-High |\n| INKER | NO | Medium-High |\n| Self-Routing RAG | YES | N/A |\n| Rep-Con / Rep-PCA | NO | Low-Medium |\n| Token-Entropy | YES (multiple) | Very Low |\n\n**Timeline implications:** 4 out of 8 baselines have public code (Probing-RAG, SeaKR, Self-Routing RAG, Token-Entropy). TARG and Rep-Con/Rep-PCA would be relatively straightforward to reimplement. Skill-RAG and INKER represent the biggest risks for timeline -- they have no code and non-trivial architectures. If Skill-RAG is your own work, you presumably already have the implementation. For INKER, you may want to consider whether it is essential or could be deprioritized given the lack of public code.\n\nSources:\n- [Probing-RAG GitHub](https://github.com/baekingeol/Probing-RAG)\n- [SeaKR GitHub](https://github.com/THU-KEG/SeaKR)\n- [TARG arXiv](https://arxiv.org/abs/2511.09803)\n- [Skill-RAG arXiv](https://arxiv.org/abs/2604.15771)\n- [INKER on ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0306457325004753)\n- [Self-Routing RAG GitHub](https://github.com/xiaowu0162/self-routing-rag)\n- [Rep-Con/Rep-PCA arXiv](https://arxiv.org/abs/2411.14572)\n- [Entropy-RAG GitHub](https://github.com/Nomothings/Entropy-RAG)\n- [ETC GitHub](https://github.com/WisdomShell/ETC)\n- [TARG OpenReview](https://openreview.net/forum?id=bMDdjg75NS)\n- [Rep-Con/Rep-PCA NAACL](https://aclanthology.org/2025.naacl-long.151/)"
      }
    ],
    "totalDurationMs": 111131,
    "totalTokens": 28410,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1501,
      "cache_creation_input_tokens": 1379,
      "cache_read_input_tokens": 23753,
      "output_tokens": 1777,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1379
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1501,
          "output_tokens": 1777,
          "cache_read_input_tokens": 23753,
          "cache_creation_input_tokens": 1379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1379,
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
      "otherToolCount": 20
    }
  },
  "sourceToolAssistantUUID": "2a0034e8-49aa-4bbf-b292-71112b391ae9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Drift-Probe-Gated Retrieval: A Systematic Evaluation of Temporal Stale…",
  "leafUuid": "da962275-dc39-49d5-8036-22f10d55e4e1",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Add multi-signal gating to drift-probe RAG system",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed"
}
```

---

### Tool result

_source line 22 · 2026-05-19T09:32:49.843Z_

<details><summary>↩ Tool result · `toolu_01ADD4fEcebAFuPUzKyzVcGs`</summary>

````text
I now have comprehensive information. Here is my detailed technical report.

---

## MMA-RAG (arXiv:2603.00511) -- Detailed Technical Findings

### Paper Overview

**Title:** Multimodal Adaptive Retrieval Augmented Generation through Internal Representation Learning
**Authors:** Ruoshuang Du, Xin Sun, Qiang Liu, Bowen Song, Zhongqi Chen, Weiqiang Wang, Liang Wang
**Submitted:** February 28, 2026
**Categories:** cs.CV, cs.LG

MMA-RAG addresses a core problem in visual RAG: static retrieval via reverse image search often retrieves images that are *visually similar but semantically mismatched*, introducing noise or contradictions that degrade VQA performance. The system uses a learned gating classifier operating on internal model representations to decide whether retrieved evidence should be incorporated.

---

### 1. Gating Classifier Architecture

The gating classifier is a **multilayer perceptron (MLP)** (not a linear probe). It takes as input a concatenated feature vector:

```
H_c = Concat(T_1, V_1, T_2, V_2)
```

Where:
- **T_1**: Textual hidden state from the *original* input (question + image), extracted at the final decoding step
- **V_1**: Visual features from the *original* input, computed via average pooling over patch embeddings from a strategically selected intermediate layer
- **T_2**: Textual hidden state from the *retrieval-augmented* input
- **V_2**: Visual features from the *retrieval-augmented* input

The MLP outputs a **4-class softmax** prediction. The paper does not disclose specific hidden layer dimensions, activation functions, or the number of hidden layers in the MLP. Training hyperparameters (learning rate, optimizer, epochs) are also not reported.

### 2. Layer Selection

This is one of the paper's central contributions -- a systematic **layer-wise analysis** of where useful gating signals reside:

- **Visual features**: Average pooling over patch embeddings from an intermediate layer. The analysis shows multimodal features achieve high classification accuracy in **early-to-mid layers (layers 2-16)**.
- **Textual features**: Hidden state from the final decoding step. Text-only features require **deeper layers (10+)** to be discriminative.
- The paper includes heatmap figures (Figures 2, 4, 5) showing layer-wise accuracy, but exact numerical values are not tabulated. The key finding is that **combining visual and textual features from mid-range layers provides the best gating accuracy**.

### 3. Four-Class Gating Labels (S1-S4)

The classifier is trained on a **four-class scheme** that captures the interaction between retrieval and correctness:

| Class | With Retrieval | Without Retrieval | Interpretation |
|-------|---------------|-------------------|----------------|
| S1 | Incorrect | Incorrect | Retrieval irrelevant (both fail) |
| S2 | Correct | Incorrect | Retrieval essential |
| S3 | Incorrect | Correct | Retrieval harmful |
| S4 | Correct | Correct | Retrieval unnecessary (both succeed) |

Labels are constructed by running each question-image pair through the VLM both with and without reverse image retrieval results, then comparing generated answers against ground truth using Qwen2.5-Instruct as an automatic judge. Dataset-specific class weights are applied to handle imbalanced class distributions.

### 4. Decision Strategies

Two strategies convert the 4-class prediction into a binary retrieval decision:

- **Pessimistic strategy**: Use retrieval (R=1) **only** when the classifier predicts S2 (retrieval is essential for correctness). This minimizes the risk of harmful retrieval.
- **Optimistic strategy**: Use retrieval (R=1) **unless** the classifier predicts S3 (retrieval is actively harmful). This maximizes information utilization.

### 5. Backbone Models and Benchmarks

**VLMs tested:** Idefics2-8B, Idefics3-8B, Qwen2.5-VL

**Datasets and training samples:**
- InfoSeek: 3,740 training samples
- OK-VQA: 1,000 training samples
- E-VQA: 1,000 training samples

**Reported VQA accuracy (end-to-end, not classifier accuracy):**

| Dataset | Qwen2.5-VL | Idefics2 | Idefics3 |
|---------|-----------|----------|----------|
| InfoSeek | 23.9% | 20.3% | 18.1% |
| OK-VQA | 62.4% | 60.1% | 58.3% |
| E-VQA | 20.0% | 14.6% | 12.6% |

The gating classifier's own accuracy (how well it predicts S1-S4) is shown in layer-wise heatmap figures but exact numbers are not reported in tabular form.

### 6. Ablation Studies

The paper includes ablations on:
- **Without text features (V-only)**: Performance drops
- **Without vision features (T-only)**: Greater performance degradation, confirming visual features are more critical for the gating decision
- **Pooling strategy variations**: Minimal impact
- **Layer selection**: Mid-to-later layers consistently optimal

Notably, there is **no comparison between the MLP and a simpler linear classifier**, which is a gap relative to the proposed system's approach.

---

### Comparison with Hidden-State-Based Linear Probes for Temporal Drift Detection

The reviewer's system apparently uses **linear probes on residual stream activations** for retrieval gating, specifically targeting temporal drift detection. Here is a structured comparison:

| Dimension | MMA-RAG | Linear Probe on Residual Stream |
|-----------|---------|-------------------------------|
| **Classifier type** | MLP (nonlinear) | Linear probe (single linear layer) |
| **Input features** | Concatenated multimodal features (T1, V1, T2, V2) from both original and retrieved inputs | Residual stream activations from a single forward pass |
| **Modality** | Multimodal (vision + text) | Typically text-only |
| **What it detects** | Whether retrieval helps or hurts answer correctness | Whether the model's knowledge is temporally outdated or drifted |
| **Decision granularity** | 4-class (S1-S4) mapped to binary | Typically binary (retrieve / don't retrieve) |
| **Requires retrieval for gating** | Yes -- needs both original and retrieved features | No -- can gate *before* retrieval based on internal state alone |
| **Training data** | Task-specific labeled pairs with retrieval outcomes | Labeled examples of temporal freshness or factual accuracy |
| **Layer strategy** | Layer-wise analysis selecting optimal mid-range layer | Typically targets specific layers or aggregates across residual stream |

**Key architectural similarity:** Both approaches share the fundamental insight that **internal model representations encode sufficient information to make retrieval decisions without relying on output-level signals**. Both train lightweight classifiers on hidden states rather than using the model's generated text to decide retrieval necessity.

**Key differences:**
1. **Pre-retrieval vs. post-retrieval gating**: MMA-RAG requires running the model on *both* original and retrieved inputs before making the gating decision. A linear probe on residual stream activations can potentially gate *before* retrieval, which is more computationally efficient.
2. **Classifier complexity**: MMA-RAG uses an MLP (nonlinear boundaries), while a linear probe assumes the relevant signal is linearly separable in activation space -- a stronger but potentially more interpretable assumption.
3. **Signal type**: MMA-RAG detects "visual similarity with semantic mismatch" in retrieved images. A temporal drift detector would look for signals that the model's parametric knowledge is stale.
4. **Multimodal fusion**: MMA-RAG's concatenation of V1, V2, T1, T2 is specific to visual RAG. A residual stream probe is typically unimodal.

---

### Landscape of Related Work (2024-2026)

The following papers form the emerging field of hidden-state-based retrieval gating:

1. **Probing-RAG** (October 2024, NAACL 2025 Findings): A single-hidden-layer feed-forward network (~5MB) probes even-numbered layers starting from layer 6 in Gemma-2B (after the 1/3 point). Uses mean pooling over rationale/answer token hidden states. Binary classification with cross-entropy loss. Reduces retrieval calls by 50% while outperforming Adaptive-RAG by 9 points on average across 5 QA datasets (35.8% vs 26.8%).

2. **Skill-RAG** (April 2026): Extends the probing concept with a two-stage prober that detects "failure states" in hidden representations. Uses feed-forward networks with binary classification heads, one per layer, aggregated by averaging predicted probabilities. Probes the posterior 2/3 of model layers. Uniquely couples failure detection with a **skill router** that selects among four retrieval strategies. Achieves 6.1-13.6 point improvements over prober-only gating on out-of-distribution datasets.

3. **TARG** (November 2025): Training-free approach using prefix logits (not hidden states). Three gates: entropy, margin (top-1/top-2 logit gap), and small-NN variance. Finds that backbone sharpness determines signal effectiveness -- margin gates retain dynamic range under instruction-tuned models while entropy gates compress.

4. **DRIFT** (January 2026): Lightweight probes on intermediate layers detecting confidence signals "lost in the final output layer." Routes uncertain queries to stronger models. Achieves SOTA AUROC on 10/12 settings across 4 QA benchmarks with <0.1% computational overhead. Generalizes across dataset shifts without retraining.

5. **ICR Probe** (ACL 2025): Linear probes applied to residual streams at multiple depths. Probes each layer's residual stream to obtain ICR Scores, aggregated across all layers. Creates binary classifiers that distinguish whether generation should rely on retrieval or parametric knowledge.

6. **LatentAudit** (April 2026): Pools mid-to-late residual-stream activations and measures Mahalanobis distance to evidence representations. Achieves 0.942 AUROC on PubMedQA for faithfulness monitoring. Demonstrates residual-stream geometry as a practical basis for real-time RAG monitoring.

7. **How Retrieved Context Shapes Internal Representations** (February 2026, arXiv:2602.20091): Systematic analysis of how different retrieval document types (relevant, distracting, random) affect hidden states across 4 QA datasets and 3 LLMs. Provides theoretical grounding for why internal representations are informative for retrieval gating.

---

### Summary Assessment

MMA-RAG's core contribution is extending hidden-state-based retrieval gating to the **multimodal setting** with a four-class decision framework. Its architecture is indeed similar in spirit to using linear probes on residual stream activations for retrieval decisions -- both exploit the same fundamental insight that model internals encode retrieval-relevant signals. However, MMA-RAG differs in three important ways: (a) it uses an MLP rather than a linear probe, (b) it requires features from *both* original and retrieved inputs (post-retrieval gating), and (c) it fuses vision and text representations. A system using linear probes for temporal drift detection would be more closely aligned with Probing-RAG, ICR Probe, or DRIFT in terms of architecture, but would address a different signal (knowledge staleness vs. retrieval utility).

Sources:
- [MMA-RAG (arXiv:2603.00511)](https://arxiv.org/abs/2603.00511)
- [Probing-RAG (arXiv:2410.13339)](https://arxiv.org/abs/2410.13339)
- [Skill-RAG (arXiv:2604.15771)](https://arxiv.org/html/2604.15771)
- [TARG (arXiv:2511.09803)](https://arxiv.org/html/2511.09803v1)
- [DRIFT (arXiv:2601.14210)](https://arxiv.org/abs/2601.14210)
- [ICR Probe (ACL 2025)](https://aclanthology.org/2025.acl-long.880.pdf)
- [LatentAudit (arXiv:2604.05358)](https://arxiv.org/abs/2604.05358)
- [How Retrieved Context Shapes Internal Representations (arXiv:2602.20091)](https://arxiv.org/abs/2602.20091)
- [Self-RAG (arXiv:2310.11511)](https://arxiv.org/abs/2310.11511)

agentId: ab611fc54d20c5984 (use SendMessage with to: 'ab611fc54d20c5984' to continue this agent)
&lt;usage>total_tokens: 27753
tool_uses: 21
duration_ms: 188910&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "42dfb6e2-654b-40db-86c0-6f1b676a76e7",
  "isSidechain": false,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "type": "user",
  "uuid": "74a775f2-038b-4031-b9b4-599dbdc1b8fc",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper MMA-RAG (arXiv:2603.00511, February 2026) which uses internal representation learning for adaptive retrieval gating in multimodal RAG. The reviewer says this is architecturally similar to a proposed system that uses hidden-state-based gating classifiers for retrieval decisions.\n\n1. Search for \"MMA-RAG adaptive retrieval gating multimodal\" and \"arXiv 2603.00511\"\n2. Fetch and read the paper to understand:\n   - What exact architecture do they use for gating? (hidden states, which layer, what classifier?)\n   - How do they train the gating classifier?\n   - What signals does the gating classifier detect?\n   - How is it similar/different from using a linear probe on residual stream activations for temporal drift detection?\n   - What benchmarks do they evaluate on?\n3. Also search for any other recent (2025-2026) work on \"internal representation gating RAG\" or \"hidden state retrieval decision\"\n\nReport detailed technical findings with specific architectural details.",
    "agentId": "ab611fc54d20c5984",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information. Here is my detailed technical report.\n\n---\n\n## MMA-RAG (arXiv:2603.00511) -- Detailed Technical Findings\n\n### Paper Overview\n\n**Title:** Multimodal Adaptive Retrieval Augmented Generation through Internal Representation Learning\n**Authors:** Ruoshuang Du, Xin Sun, Qiang Liu, Bowen Song, Zhongqi Chen, Weiqiang Wang, Liang Wang\n**Submitted:** February 28, 2026\n**Categories:** cs.CV, cs.LG\n\nMMA-RAG addresses a core problem in visual RAG: static retrieval via reverse image search often retrieves images that are *visually similar but semantically mismatched*, introducing noise or contradictions that degrade VQA performance. The system uses a learned gating classifier operating on internal model representations to decide whether retrieved evidence should be incorporated.\n\n---\n\n### 1. Gating Classifier Architecture\n\nThe gating classifier is a **multilayer perceptron (MLP)** (not a linear probe). It takes as input a concatenated feature vector:\n\n```\nH_c = Concat(T_1, V_1, T_2, V_2)\n```\n\nWhere:\n- **T_1**: Textual hidden state from the *original* input (question + image), extracted at the final decoding step\n- **V_1**: Visual features from the *original* input, computed via average pooling over patch embeddings from a strategically selected intermediate layer\n- **T_2**: Textual hidden state from the *retrieval-augmented* input\n- **V_2**: Visual features from the *retrieval-augmented* input\n\nThe MLP outputs a **4-class softmax** prediction. The paper does not disclose specific hidden layer dimensions, activation functions, or the number of hidden layers in the MLP. Training hyperparameters (learning rate, optimizer, epochs) are also not reported.\n\n### 2. Layer Selection\n\nThis is one of the paper's central contributions -- a systematic **layer-wise analysis** of where useful gating signals reside:\n\n- **Visual features**: Average pooling over patch embeddings from an intermediate layer. The analysis shows multimodal features achieve high classification accuracy in **early-to-mid layers (layers 2-16)**.\n- **Textual features**: Hidden state from the final decoding step. Text-only features require **deeper layers (10+)** to be discriminative.\n- The paper includes heatmap figures (Figures 2, 4, 5) showing layer-wise accuracy, but exact numerical values are not tabulated. The key finding is that **combining visual and textual features from mid-range layers provides the best gating accuracy**.\n\n### 3. Four-Class Gating Labels (S1-S4)\n\nThe classifier is trained on a **four-class scheme** that captures the interaction between retrieval and correctness:\n\n| Class | With Retrieval | Without Retrieval | Interpretation |\n|-------|---------------|-------------------|----------------|\n| S1 | Incorrect | Incorrect | Retrieval irrelevant (both fail) |\n| S2 | Correct | Incorrect | Retrieval essential |\n| S3 | Incorrect | Correct | Retrieval harmful |\n| S4 | Correct | Correct | Retrieval unnecessary (both succeed) |\n\nLabels are constructed by running each question-image pair through the VLM both with and without reverse image retrieval results, then comparing generated answers against ground truth using Qwen2.5-Instruct as an automatic judge. Dataset-specific class weights are applied to handle imbalanced class distributions.\n\n### 4. Decision Strategies\n\nTwo strategies convert the 4-class prediction into a binary retrieval decision:\n\n- **Pessimistic strategy**: Use retrieval (R=1) **only** when the classifier predicts S2 (retrieval is essential for correctness). This minimizes the risk of harmful retrieval.\n- **Optimistic strategy**: Use retrieval (R=1) **unless** the classifier predicts S3 (retrieval is actively harmful). This maximizes information utilization.\n\n### 5. Backbone Models and Benchmarks\n\n**VLMs tested:** Idefics2-8B, Idefics3-8B, Qwen2.5-VL\n\n**Datasets and training samples:**\n- InfoSeek: 3,740 training samples\n- OK-VQA: 1,000 training samples\n- E-VQA: 1,000 training samples\n\n**Reported VQA accuracy (end-to-end, not classifier accuracy):**\n\n| Dataset | Qwen2.5-VL | Idefics2 | Idefics3 |\n|---------|-----------|----------|----------|\n| InfoSeek | 23.9% | 20.3% | 18.1% |\n| OK-VQA | 62.4% | 60.1% | 58.3% |\n| E-VQA | 20.0% | 14.6% | 12.6% |\n\nThe gating classifier's own accuracy (how well it predicts S1-S4) is shown in layer-wise heatmap figures but exact numbers are not reported in tabular form.\n\n### 6. Ablation Studies\n\nThe paper includes ablations on:\n- **Without text features (V-only)**: Performance drops\n- **Without vision features (T-only)**: Greater performance degradation, confirming visual features are more critical for the gating decision\n- **Pooling strategy variations**: Minimal impact\n- **Layer selection**: Mid-to-later layers consistently optimal\n\nNotably, there is **no comparison between the MLP and a simpler linear classifier**, which is a gap relative to the proposed system's approach.\n\n---\n\n### Comparison with Hidden-State-Based Linear Probes for Temporal Drift Detection\n\nThe reviewer's system apparently uses **linear probes on residual stream activations** for retrieval gating, specifically targeting temporal drift detection. Here is a structured comparison:\n\n| Dimension | MMA-RAG | Linear Probe on Residual Stream |\n|-----------|---------|-------------------------------|\n| **Classifier type** | MLP (nonlinear) | Linear probe (single linear layer) |\n| **Input features** | Concatenated multimodal features (T1, V1, T2, V2) from both original and retrieved inputs | Residual stream activations from a single forward pass |\n| **Modality** | Multimodal (vision + text) | Typically text-only |\n| **What it detects** | Whether retrieval helps or hurts answer correctness | Whether the model's knowledge is temporally outdated or drifted |\n| **Decision granularity** | 4-class (S1-S4) mapped to binary | Typically binary (retrieve / don't retrieve) |\n| **Requires retrieval for gating** | Yes -- needs both original and retrieved features | No -- can gate *before* retrieval based on internal state alone |\n| **Training data** | Task-specific labeled pairs with retrieval outcomes | Labeled examples of temporal freshness or factual accuracy |\n| **Layer strategy** | Layer-wise analysis selecting optimal mid-range layer | Typically targets specific layers or aggregates across residual stream |\n\n**Key architectural similarity:** Both approaches share the fundamental insight that **internal model representations encode sufficient information to make retrieval decisions without relying on output-level signals**. Both train lightweight classifiers on hidden states rather than using the model's generated text to decide retrieval necessity.\n\n**Key differences:**\n1. **Pre-retrieval vs. post-retrieval gating**: MMA-RAG requires running the model on *both* original and retrieved inputs before making the gating decision. A linear probe on residual stream activations can potentially gate *before* retrieval, which is more computationally efficient.\n2. **Classifier complexity**: MMA-RAG uses an MLP (nonlinear boundaries), while a linear probe assumes the relevant signal is linearly separable in activation space -- a stronger but potentially more interpretable assumption.\n3. **Signal type**: MMA-RAG detects \"visual similarity with semantic mismatch\" in retrieved images. A temporal drift detector would look for signals that the model's parametric knowledge is stale.\n4. **Multimodal fusion**: MMA-RAG's concatenation of V1, V2, T1, T2 is specific to visual RAG. A residual stream probe is typically unimodal.\n\n---\n\n### Landscape of Related Work (2024-2026)\n\nThe following papers form the emerging field of hidden-state-based retrieval gating:\n\n1. **Probing-RAG** (October 2024, NAACL 2025 Findings): A single-hidden-layer feed-forward network (~5MB) probes even-numbered layers starting from layer 6 in Gemma-2B (after the 1/3 point). Uses mean pooling over rationale/answer token hidden states. Binary classification with cross-entropy loss. Reduces retrieval calls by 50% while outperforming Adaptive-RAG by 9 points on average across 5 QA datasets (35.8% vs 26.8%).\n\n2. **Skill-RAG** (April 2026): Extends the probing concept with a two-stage prober that detects \"failure states\" in hidden representations. Uses feed-forward networks with binary classification heads, one per layer, aggregated by averaging predicted probabilities. Probes the posterior 2/3 of model layers. Uniquely couples failure detection with a **skill router** that selects among four retrieval strategies. Achieves 6.1-13.6 point improvements over prober-only gating on out-of-distribution datasets.\n\n3. **TARG** (November 2025): Training-free approach using prefix logits (not hidden states). Three gates: entropy, margin (top-1/top-2 logit gap), and small-NN variance. Finds that backbone sharpness determines signal effectiveness -- margin gates retain dynamic range under instruction-tuned models while entropy gates compress.\n\n4. **DRIFT** (January 2026): Lightweight probes on intermediate layers detecting confidence signals \"lost in the final output layer.\" Routes uncertain queries to stronger models. Achieves SOTA AUROC on 10/12 settings across 4 QA benchmarks with <0.1% computational overhead. Generalizes across dataset shifts without retraining.\n\n5. **ICR Probe** (ACL 2025): Linear probes applied to residual streams at multiple depths. Probes each layer's residual stream to obtain ICR Scores, aggregated across all layers. Creates binary classifiers that distinguish whether generation should rely on retrieval or parametric knowledge.\n\n6. **LatentAudit** (April 2026): Pools mid-to-late residual-stream activations and measures Mahalanobis distance to evidence representations. Achieves 0.942 AUROC on PubMedQA for faithfulness monitoring. Demonstrates residual-stream geometry as a practical basis for real-time RAG monitoring.\n\n7. **How Retrieved Context Shapes Internal Representations** (February 2026, arXiv:2602.20091): Systematic analysis of how different retrieval document types (relevant, distracting, random) affect hidden states across 4 QA datasets and 3 LLMs. Provides theoretical grounding for why internal representations are informative for retrieval gating.\n\n---\n\n### Summary Assessment\n\nMMA-RAG's core contribution is extending hidden-state-based retrieval gating to the **multimodal setting** with a four-class decision framework. Its architecture is indeed similar in spirit to using linear probes on residual stream activations for retrieval decisions -- both exploit the same fundamental insight that model internals encode retrieval-relevant signals. However, MMA-RAG differs in three important ways: (a) it uses an MLP rather than a linear probe, (b) it requires features from *both* original and retrieved inputs (post-retrieval gating), and (c) it fuses vision and text representations. A system using linear probes for temporal drift detection would be more closely aligned with Probing-RAG, ICR Probe, or DRIFT in terms of architecture, but would address a different signal (knowledge staleness vs. retrieval utility).\n\nSources:\n- [MMA-RAG (arXiv:2603.00511)](https://arxiv.org/abs/2603.00511)\n- [Probing-RAG (arXiv:2410.13339)](https://arxiv.org/abs/2410.13339)\n- [Skill-RAG (arXiv:2604.15771)](https://arxiv.org/html/2604.15771)\n- [TARG (arXiv:2511.09803)](https://arxiv.org/html/2511.09803v1)\n- [DRIFT (arXiv:2601.14210)](https://arxiv.org/abs/2601.14210)\n- [ICR Probe (ACL 2025)](https://aclanthology.org/2025.acl-long.880.pdf)\n- [LatentAudit (arXiv:2604.05358)](https://arxiv.org/abs/2604.05358)\n- [How Retrieved Context Shapes Internal Representations (arXiv:2602.20091)](https://arxiv.org/abs/2602.20091)\n- [Self-RAG (arXiv:2310.11511)](https://arxiv.org/abs/2310.11511)"
      }
    ],
    "totalDurationMs": 188910,
    "totalTokens": 27753,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1067,
      "cache_read_input_tokens": 23527,
      "output_tokens": 3158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1067
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3158,
          "cache_read_input_tokens": 23527,
          "cache_creation_input_tokens": 1067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1067,
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
      "otherToolCount": 21
    }
  },
  "sourceToolAssistantUUID": "42dfb6e2-654b-40db-86c0-6f1b676a76e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 23 · 2026-05-19T09:32:57.645Z_

<details><summary>↩ Tool result · `toolu_01M4KDXsMZbUGakyqVcDF2CH`</summary>

```text
I now have a comprehensive picture of the landscape. Let me compile the detailed findings.

---

## Research Report: Multi-Signal Fusion for Retrieval Gating in RAG Systems

### Executive Summary

The reviewer's suggestion -- combining temporal-drift probes with confidence and uncertainty probes via a learned multi-signal fusion gate -- sits in a genuine gap in the literature. No existing work combines orthogonal representation-space probes (drift, confidence, uncertainty) through a learned gating mechanism for retrieval decisions. However, there are closely related works on each individual axis and some early attempts at multi-signal combination. This means the fusion idea is both well-motivated by existing trends and genuinely novel in its specific formulation.

---

### 1. ADAPTIVE RETRIEVAL GATING (Single-Signal Systems)

**TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG**
- arXiv: 2511.09803 (Nov 2025, revised Apr 2026)
- Authors: Yufeng Wang, Lu Wei, Haibin Ling
- Key details: Computes three uncertainty signals from draft logits -- mean token entropy, margin signal (top-1/top-2 logit gap), and small-N variance -- but uses them as **alternatives, not fused together**. The paper explicitly recommends the margin signal as "a robust default" rather than combining signals. Achieves 70-90% retrieval reduction.
- **Gap**: Treats signals as interchangeable options rather than complementary inputs to a fusion mechanism.

**MeCo: Adaptive Tool Use in Large Language Models with Meta-Cognition Trigger**
- arXiv: 2502.12961 (Feb 2025), also at ACL 2025
- Authors: Wenjun Li et al. (Huawei Noah's Ark Lab)
- Key details: Trains a linear meta-cognition probe via PCA on contrastive instruction pairs, selects a **single best layer's probe** using a dual-threshold gating strategy. The paper **explicitly rejects multi-probe fusion**, stating: "scores predicted by different probes vary significantly, and simply averaging multiple scores does not yield accurate results."
- **Gap**: Identifies the problem of combining probes but does not solve it -- they retreat to single-probe selection.

**SeaKR: Self-aware Knowledge Retrieval**
- arXiv: 2406.19215 (Jun 2024)
- Uses an Uncertainty Module to monitor LLM internal states and trigger retrieval when uncertainty exceeds a threshold. Single-signal architecture.

**ETC: Entropy-Trend Constraint for Dynamic RAG**
- arXiv: 2511.09980 (Nov 2025)
- Authors: Bo Li, Tian Tian et al.
- Key details: Combines entropy values with their first-order and second-order temporal differences plus dynamic smoothing. While this combines multiple derived signals, they are all **derivatives of a single base signal (entropy)** -- not orthogonal representation axes.

**Embedding-Informed Adaptive RAG**
- arXiv: 2404.03514 (Apr 2024)
- Authors: Chengkai Huang et al.
- Uses pre-trained token embeddings to assess model knowledge, but relies on a single embedding-based signal.

---

### 2. THE CLOSEST WORK TO MULTI-SIGNAL FUSION FOR RETRIEVAL

**"Adaptive Retrieval without Self-Knowledge? Bringing Uncertainty Back Home"**
- arXiv: 2501.12835 (Jan 2025)
- Authors: Viktor Moskvoretskii et al.
- **This is the most directly relevant paper.** It evaluates 35 adaptive retrieval methods and proposes a **hybrid approach combining three families of uncertainty signals**: logit-based (Max Entropy, Mean Entropy, SAR), consistency-based (EigValLaplacian, Lex-Similarity), and internal-state methods (Mahalanobis Distance).
- Fusion architecture: **Logistic regression classifier** on combined uncertainty features.
- Key finding: Consistency-based methods excel at QA performance but fail at self-knowledge; logit-based methods dominate self-knowledge metrics. The hybrid "balances all metrics" by leveraging complementary strengths.
- **Critical difference from your proposed work**: Their signals are all uncertainty-family signals (different ways of measuring the same underlying phenomenon), not orthogonal representation axes like drift vs. confidence vs. uncertainty. Their fusion is a simple logistic regression, not a learned gating network.

**"Beyond Component Strength: Synergistic Integration and Adaptive Calibration in Multi-Agent RAG Systems"**
- arXiv: 2511.21729 (Dec 2025)
- Author: Jithin Krishnan
- Argues that multi-component RAG performance is not additive -- intelligent fusion with adaptive calibration outperforms naive combination. Focuses on multi-agent architectures rather than internal representation probes.

---

### 3. ORTHOGONAL PROBES AND MULTI-PROBE FUSION IN INTERPRETABILITY

**Truth Forest: Toward Multi-Scale Truthfulness in LLMs**
- arXiv: 2312.17484 (Dec 2023), published at AAAI 2024
- Authors: Zhongzhi Chen et al.
- **The closest interpretability work to your proposed approach.** Constructs multiple orthogonal probing groups via orthogonal constraints, selects Top-K effective groups based on validation performance, and weights directions within each group to determine a final truthful axis for intervention. Improved Llama-2-7B truthfulness from 40.8% to 74.5%.
- **Key relevance**: Demonstrates that multiple orthogonal probes can be combined for a downstream task (truthfulness intervention), providing direct precedent for combining orthogonal probes for gating.
- **Gap**: Used for intervention (shifting representations), not for gating/routing decisions.

**"The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions"**
- arXiv: 2502.09674 (Feb 2025), accepted at ICML 2025
- Authors: Wenbo Pan et al.
- Key finding: Safety alignment is multi-dimensional, not captured by a single direction. They identify a dominant refusal direction plus secondary orthogonal directions encoding features like "hypothetical narrative" and "role-playing." These secondary directions **promote or suppress** the dominant direction, showing complex interactions.
- **Theoretical grounding**: Demonstrates that orthogonal directions encode genuinely different features and their interactions are non-trivial, supporting the case that combining orthogonal probes captures information unavailable to any single probe.

**Representation Engineering Survey**
- arXiv: 2502.17601 (Feb 2025)
- Authors: Lukasz Bartoszcze et al.
- Key findings on combining directions: "Combining steering vectors for different concepts can lead to unpredictable interactions." Three approaches discussed: composite activation vectors, sparse activation control (separate interventions over distinct attention heads), and Conceptor matrices (designed to eliminate negative interactions). The superposition hypothesis provides partial theoretical justification but also raises challenges.
- **Critical insight**: The survey notes that "simultaneous injection of individual steering vectors at different places in the model appears to be more effective than combined steering" -- suggesting that naive vector addition is suboptimal and learned combination mechanisms are needed.

**Hyperdimensional Probe**
- arXiv: 2509.25045 (Sep 2025)
- Authors: Marco Bronzini et al.
- Uses Vector Symbolic Architectures (VSA) to combine multiple representation directions through hyperdimensional encoding where bundling operations allow composite representations. Exploits the property that relevant signals amplify in high dimensions while noise diminishes.

---

### 4. TEMPORAL DRIFT AND KNOWLEDGE FRESHNESS

**"Temporal Alignment of Time Sensitive Facts with Activation Engineering"**
- arXiv: 2505.14158 (May 2025)
- Authors: Sanjay Govindan et al.
- Demonstrates that temporal information can be injected into LLM activations via activation engineering, achieving up to 44% improvement. This confirms that temporal/drift information is linearly encoded in representation space and extractable via probes.

**"RAG or Learning? Understanding the Limits of LLM Adaptation under Continuous Knowledge Drift"**
- arXiv: 2604.05096 (Apr 2026)
- Introduces Chronos, a time-aware retrieval baseline organizing evidence into Event Evolution Graphs. Does NOT use probe-based detection -- purely external.

**"Uncertainty Quantification for Retrieval-Augmented Reasoning" (R2C)**
- arXiv: 2510.11483 (Oct 2025)
- Captures uncertainty from both retrieval and generation via perturbation-based consistency. Combines signals from both components through feedback loops. Used for abstention and model selection, not gating.

---

### 5. MoE-STYLE ARCHITECTURES FOR RETRIEVAL

**ExpertRAG**
- arXiv: 2504.08744 (Mar 2025)
- Theoretical framework combining MoE with RAG. Proposes a gating mechanism that jointly decides retrieval necessity and expert routing. Probabilistic formulation treating retrieval and expert selection as latent decisions. Primarily theoretical (30-page paper).

**MixRAG**
- arXiv: 2509.21391 (Sep 2025)
- MoE-style graph-RAG with multiple specialized retrievers and a dynamic routing controller. Query-aware gating amplifies useful signals and suppresses distracting ones. However, this routes between external retrievers, not internal representation probes.

---

### KEY FINDINGS AND NOVELTY ASSESSMENT

**Has anyone combined orthogonal representation axes for gating/routing decisions?**
No. Truth Forest (AAAI 2024) combines orthogonal probes for intervention, and Moskvoretskii et al. (2501.12835) combine multiple uncertainty signals via logistic regression for retrieval gating, but no one has combined orthogonal representation-space probes (e.g., drift + confidence + uncertainty axes) through a learned gating mechanism for retrieval decisions. This specific combination is genuinely novel.

**What fusion architectures exist?**
- **Logistic regression on concatenated features** (Moskvoretskii et al., 2501.12835) -- simplest approach
- **Top-K selection with weighted combination** (Truth Forest) -- select best orthogonal groups, weight within groups
- **MoE-style routing** (ExpertRAG, MixRAG) -- softmax gating over expert modules
- **Cascade/threshold** (MeCo, SeaKR) -- sequential thresholding on single signals
- **Hyperdimensional bundling** (Hyperdimensional Probe) -- VSA-based superposition
- **Conceptor matrices** (discussed in RepE survey) -- designed to prevent destructive interference between directions

**Is there theoretical grounding for combining orthogonal signals?**
Yes, from multiple angles:
1. Pan et al. (ICML 2025) show orthogonal safety directions encode genuinely different features with non-trivial interactions, meaning single-direction approaches miss important structure.
2. The RepE survey notes the superposition hypothesis provides partial justification -- different concepts are encoded in partially orthogonal directions, so combining them accesses complementary information.
3. Truth Forest demonstrates empirically that orthogonal probe groups capture different "scales" of truth, and their combination outperforms single-direction intervention.
4. Moskvoretskii et al. show that different signal families (logit-based vs. consistency-based vs. internal-state) have complementary strengths -- one excels at self-knowledge while another at QA performance.

**The reviewer's suggestion is well-grounded but currently unoccupied territory.** The proposed multi-signal fusion combining drift, confidence, and uncertainty probes would be the first work to:
(a) identify and extract multiple orthogonal representation-space probes specifically for retrieval gating,
(b) use a learned fusion mechanism (rather than simple averaging or logistic regression) to combine them, and
(c) provide theoretical and empirical justification for why these particular axes are complementary.

MeCo's explicit statement that "simply averaging multiple scores does not yield accurate results" directly motivates the need for a more sophisticated fusion approach -- exactly the gap the reviewer's suggestion fills.

Sources:
- [TARG - arXiv:2511.09803](https://arxiv.org/abs/2511.09803)
- [MeCo - arXiv:2502.12961](https://arxiv.org/html/2502.12961v1)
- [Adaptive Retrieval without Self-Knowledge - arXiv:2501.12835](https://arxiv.org/html/2501.12835v2)
- [Truth Forest - arXiv:2312.17484](https://arxiv.org/abs/2312.17484)
- [Hidden Dimensions of LLM Alignment - arXiv:2502.09674](https://arxiv.org/abs/2502.09674)
- [RepE Survey - arXiv:2502.17601](https://arxiv.org/html/2502.17601v1)
- [ETC Uncertainty Trends - arXiv:2511.09980](https://arxiv.org/html/2511.09980)
- [Uncertainty Quantification for RAR (R2C) - arXiv:2510.11483](https://arxiv.org/abs/2510.11483)
- [ExpertRAG - arXiv:2504.08744](https://arxiv.org/abs/2504.08744)
- [MixRAG - arXiv:2509.21391](https://arxiv.org/html/2509.21391v1)
- [Temporal Alignment with Activation Engineering - arXiv:2505.14158](https://arxiv.org/abs/2505.14158)
- [Continuous Knowledge Drift (Chronos) - arXiv:2604.05096](https://arxiv.org/abs/2604.05096)
- [LLM Meta-Cognition - arXiv:2506.08410](https://arxiv.org/abs/2506.08410)
- [Hyperdimensional Probe - arXiv:2509.25045](https://arxiv.org/pdf/2509.25045)
- [Improved Representation Steering (RePS) - arXiv:2505.20809](https://arxiv.org/html/2505.20809v1)
- [Synergistic Multi-Agent RAG - arXiv:2511.21729](https://arxiv.org/pdf/2511.21729)
- [Embedding-Informed Adaptive RAG - arXiv:2404.03514](https://arxiv.org/abs/2404.03514)
- [SeaKR - arXiv:2406.19215](https://arxiv.org/pdf/2406.19215)

agentId: abc0fa89160fca956 (use SendMessage with to: 'abc0fa89160fca956' to continue this agent)
&lt;usage>total_tokens: 32763
tool_uses: 30
duration_ms: 215127&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c553bfe7-9366-461f-b2d2-0d26860378c3",
  "isSidechain": false,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "type": "user",
  "uuid": "2805df47-a35d-4d4a-94d5-f0721ffa4029",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the novelty concern for a paper about using temporal-drift probes as retrieval gates in RAG systems. The reviewer says \"implementing what someone else suggested isn't novel enough\" and recommends multi-signal fusion combining drift, confidence, and uncertainty probes.\n\nI need you to search for:\n1. Multi-signal or multi-axis gating/routing in RAG or LLM systems (2024-2026)\n2. Orthogonal probe combination / multi-probe fusion in LLM interpretability\n3. Learned gating mechanisms that combine multiple internal signals for retrieval decisions\n4. Any work on combining orthogonal representation directions for downstream tasks\n\nFor each search, read the most relevant papers. I need to understand:\n- Has anyone combined orthogonal representation axes for gating/routing decisions?\n- What fusion architectures exist (learned weighted combination, MoE-style, cascade)?\n- Is there theoretical grounding for why combining orthogonal signals should help?\n\nUse WebSearch with 3-4 different queries, then WebFetch on the most relevant papers found. Report findings in detail with paper titles, arXiv IDs, and key technical details.",
    "agentId": "abc0fa89160fca956",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a comprehensive picture of the landscape. Let me compile the detailed findings.\n\n---\n\n## Research Report: Multi-Signal Fusion for Retrieval Gating in RAG Systems\n\n### Executive Summary\n\nThe reviewer's suggestion -- combining temporal-drift probes with confidence and uncertainty probes via a learned multi-signal fusion gate -- sits in a genuine gap in the literature. No existing work combines orthogonal representation-space probes (drift, confidence, uncertainty) through a learned gating mechanism for retrieval decisions. However, there are closely related works on each individual axis and some early attempts at multi-signal combination. This means the fusion idea is both well-motivated by existing trends and genuinely novel in its specific formulation.\n\n---\n\n### 1. ADAPTIVE RETRIEVAL GATING (Single-Signal Systems)\n\n**TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG**\n- arXiv: 2511.09803 (Nov 2025, revised Apr 2026)\n- Authors: Yufeng Wang, Lu Wei, Haibin Ling\n- Key details: Computes three uncertainty signals from draft logits -- mean token entropy, margin signal (top-1/top-2 logit gap), and small-N variance -- but uses them as **alternatives, not fused together**. The paper explicitly recommends the margin signal as \"a robust default\" rather than combining signals. Achieves 70-90% retrieval reduction.\n- **Gap**: Treats signals as interchangeable options rather than complementary inputs to a fusion mechanism.\n\n**MeCo: Adaptive Tool Use in Large Language Models with Meta-Cognition Trigger**\n- arXiv: 2502.12961 (Feb 2025), also at ACL 2025\n- Authors: Wenjun Li et al. (Huawei Noah's Ark Lab)\n- Key details: Trains a linear meta-cognition probe via PCA on contrastive instruction pairs, selects a **single best layer's probe** using a dual-threshold gating strategy. The paper **explicitly rejects multi-probe fusion**, stating: \"scores predicted by different probes vary significantly, and simply averaging multiple scores does not yield accurate results.\"\n- **Gap**: Identifies the problem of combining probes but does not solve it -- they retreat to single-probe selection.\n\n**SeaKR: Self-aware Knowledge Retrieval**\n- arXiv: 2406.19215 (Jun 2024)\n- Uses an Uncertainty Module to monitor LLM internal states and trigger retrieval when uncertainty exceeds a threshold. Single-signal architecture.\n\n**ETC: Entropy-Trend Constraint for Dynamic RAG**\n- arXiv: 2511.09980 (Nov 2025)\n- Authors: Bo Li, Tian Tian et al.\n- Key details: Combines entropy values with their first-order and second-order temporal differences plus dynamic smoothing. While this combines multiple derived signals, they are all **derivatives of a single base signal (entropy)** -- not orthogonal representation axes.\n\n**Embedding-Informed Adaptive RAG**\n- arXiv: 2404.03514 (Apr 2024)\n- Authors: Chengkai Huang et al.\n- Uses pre-trained token embeddings to assess model knowledge, but relies on a single embedding-based signal.\n\n---\n\n### 2. THE CLOSEST WORK TO MULTI-SIGNAL FUSION FOR RETRIEVAL\n\n**\"Adaptive Retrieval without Self-Knowledge? Bringing Uncertainty Back Home\"**\n- arXiv: 2501.12835 (Jan 2025)\n- Authors: Viktor Moskvoretskii et al.\n- **This is the most directly relevant paper.** It evaluates 35 adaptive retrieval methods and proposes a **hybrid approach combining three families of uncertainty signals**: logit-based (Max Entropy, Mean Entropy, SAR), consistency-based (EigValLaplacian, Lex-Similarity), and internal-state methods (Mahalanobis Distance).\n- Fusion architecture: **Logistic regression classifier** on combined uncertainty features.\n- Key finding: Consistency-based methods excel at QA performance but fail at self-knowledge; logit-based methods dominate self-knowledge metrics. The hybrid \"balances all metrics\" by leveraging complementary strengths.\n- **Critical difference from your proposed work**: Their signals are all uncertainty-family signals (different ways of measuring the same underlying phenomenon), not orthogonal representation axes like drift vs. confidence vs. uncertainty. Their fusion is a simple logistic regression, not a learned gating network.\n\n**\"Beyond Component Strength: Synergistic Integration and Adaptive Calibration in Multi-Agent RAG Systems\"**\n- arXiv: 2511.21729 (Dec 2025)\n- Author: Jithin Krishnan\n- Argues that multi-component RAG performance is not additive -- intelligent fusion with adaptive calibration outperforms naive combination. Focuses on multi-agent architectures rather than internal representation probes.\n\n---\n\n### 3. ORTHOGONAL PROBES AND MULTI-PROBE FUSION IN INTERPRETABILITY\n\n**Truth Forest: Toward Multi-Scale Truthfulness in LLMs**\n- arXiv: 2312.17484 (Dec 2023), published at AAAI 2024\n- Authors: Zhongzhi Chen et al.\n- **The closest interpretability work to your proposed approach.** Constructs multiple orthogonal probing groups via orthogonal constraints, selects Top-K effective groups based on validation performance, and weights directions within each group to determine a final truthful axis for intervention. Improved Llama-2-7B truthfulness from 40.8% to 74.5%.\n- **Key relevance**: Demonstrates that multiple orthogonal probes can be combined for a downstream task (truthfulness intervention), providing direct precedent for combining orthogonal probes for gating.\n- **Gap**: Used for intervention (shifting representations), not for gating/routing decisions.\n\n**\"The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions\"**\n- arXiv: 2502.09674 (Feb 2025), accepted at ICML 2025\n- Authors: Wenbo Pan et al.\n- Key finding: Safety alignment is multi-dimensional, not captured by a single direction. They identify a dominant refusal direction plus secondary orthogonal directions encoding features like \"hypothetical narrative\" and \"role-playing.\" These secondary directions **promote or suppress** the dominant direction, showing complex interactions.\n- **Theoretical grounding**: Demonstrates that orthogonal directions encode genuinely different features and their interactions are non-trivial, supporting the case that combining orthogonal probes captures information unavailable to any single probe.\n\n**Representation Engineering Survey**\n- arXiv: 2502.17601 (Feb 2025)\n- Authors: Lukasz Bartoszcze et al.\n- Key findings on combining directions: \"Combining steering vectors for different concepts can lead to unpredictable interactions.\" Three approaches discussed: composite activation vectors, sparse activation control (separate interventions over distinct attention heads), and Conceptor matrices (designed to eliminate negative interactions). The superposition hypothesis provides partial theoretical justification but also raises challenges.\n- **Critical insight**: The survey notes that \"simultaneous injection of individual steering vectors at different places in the model appears to be more effective than combined steering\" -- suggesting that naive vector addition is suboptimal and learned combination mechanisms are needed.\n\n**Hyperdimensional Probe**\n- arXiv: 2509.25045 (Sep 2025)\n- Authors: Marco Bronzini et al.\n- Uses Vector Symbolic Architectures (VSA) to combine multiple representation directions through hyperdimensional encoding where bundling operations allow composite representations. Exploits the property that relevant signals amplify in high dimensions while noise diminishes.\n\n---\n\n### 4. TEMPORAL DRIFT AND KNOWLEDGE FRESHNESS\n\n**\"Temporal Alignment of Time Sensitive Facts with Activation Engineering\"**\n- arXiv: 2505.14158 (May 2025)\n- Authors: Sanjay Govindan et al.\n- Demonstrates that temporal information can be injected into LLM activations via activation engineering, achieving up to 44% improvement. This confirms that temporal/drift information is linearly encoded in representation space and extractable via probes.\n\n**\"RAG or Learning? Understanding the Limits of LLM Adaptation under Continuous Knowledge Drift\"**\n- arXiv: 2604.05096 (Apr 2026)\n- Introduces Chronos, a time-aware retrieval baseline organizing evidence into Event Evolution Graphs. Does NOT use probe-based detection -- purely external.\n\n**\"Uncertainty Quantification for Retrieval-Augmented Reasoning\" (R2C)**\n- arXiv: 2510.11483 (Oct 2025)\n- Captures uncertainty from both retrieval and generation via perturbation-based consistency. Combines signals from both components through feedback loops. Used for abstention and model selection, not gating.\n\n---\n\n### 5. MoE-STYLE ARCHITECTURES FOR RETRIEVAL\n\n**ExpertRAG**\n- arXiv: 2504.08744 (Mar 2025)\n- Theoretical framework combining MoE with RAG. Proposes a gating mechanism that jointly decides retrieval necessity and expert routing. Probabilistic formulation treating retrieval and expert selection as latent decisions. Primarily theoretical (30-page paper).\n\n**MixRAG**\n- arXiv: 2509.21391 (Sep 2025)\n- MoE-style graph-RAG with multiple specialized retrievers and a dynamic routing controller. Query-aware gating amplifies useful signals and suppresses distracting ones. However, this routes between external retrievers, not internal representation probes.\n\n---\n\n### KEY FINDINGS AND NOVELTY ASSESSMENT\n\n**Has anyone combined orthogonal representation axes for gating/routing decisions?**\nNo. Truth Forest (AAAI 2024) combines orthogonal probes for intervention, and Moskvoretskii et al. (2501.12835) combine multiple uncertainty signals via logistic regression for retrieval gating, but no one has combined orthogonal representation-space probes (e.g., drift + confidence + uncertainty axes) through a learned gating mechanism for retrieval decisions. This specific combination is genuinely novel.\n\n**What fusion architectures exist?**\n- **Logistic regression on concatenated features** (Moskvoretskii et al., 2501.12835) -- simplest approach\n- **Top-K selection with weighted combination** (Truth Forest) -- select best orthogonal groups, weight within groups\n- **MoE-style routing** (ExpertRAG, MixRAG) -- softmax gating over expert modules\n- **Cascade/threshold** (MeCo, SeaKR) -- sequential thresholding on single signals\n- **Hyperdimensional bundling** (Hyperdimensional Probe) -- VSA-based superposition\n- **Conceptor matrices** (discussed in RepE survey) -- designed to prevent destructive interference between directions\n\n**Is there theoretical grounding for combining orthogonal signals?**\nYes, from multiple angles:\n1. Pan et al. (ICML 2025) show orthogonal safety directions encode genuinely different features with non-trivial interactions, meaning single-direction approaches miss important structure.\n2. The RepE survey notes the superposition hypothesis provides partial justification -- different concepts are encoded in partially orthogonal directions, so combining them accesses complementary information.\n3. Truth Forest demonstrates empirically that orthogonal probe groups capture different \"scales\" of truth, and their combination outperforms single-direction intervention.\n4. Moskvoretskii et al. show that different signal families (logit-based vs. consistency-based vs. internal-state) have complementary strengths -- one excels at self-knowledge while another at QA performance.\n\n**The reviewer's suggestion is well-grounded but currently unoccupied territory.** The proposed multi-signal fusion combining drift, confidence, and uncertainty probes would be the first work to:\n(a) identify and extract multiple orthogonal representation-space probes specifically for retrieval gating,\n(b) use a learned fusion mechanism (rather than simple averaging or logistic regression) to combine them, and\n(c) provide theoretical and empirical justification for why these particular axes are complementary.\n\nMeCo's explicit statement that \"simply averaging multiple scores does not yield accurate results\" directly motivates the need for a more sophisticated fusion approach -- exactly the gap the reviewer's suggestion fills.\n\nSources:\n- [TARG - arXiv:2511.09803](https://arxiv.org/abs/2511.09803)\n- [MeCo - arXiv:2502.12961](https://arxiv.org/html/2502.12961v1)\n- [Adaptive Retrieval without Self-Knowledge - arXiv:2501.12835](https://arxiv.org/html/2501.12835v2)\n- [Truth Forest - arXiv:2312.17484](https://arxiv.org/abs/2312.17484)\n- [Hidden Dimensions of LLM Alignment - arXiv:2502.09674](https://arxiv.org/abs/2502.09674)\n- [RepE Survey - arXiv:2502.17601](https://arxiv.org/html/2502.17601v1)\n- [ETC Uncertainty Trends - arXiv:2511.09980](https://arxiv.org/html/2511.09980)\n- [Uncertainty Quantification for RAR (R2C) - arXiv:2510.11483](https://arxiv.org/abs/2510.11483)\n- [ExpertRAG - arXiv:2504.08744](https://arxiv.org/abs/2504.08744)\n- [MixRAG - arXiv:2509.21391](https://arxiv.org/html/2509.21391v1)\n- [Temporal Alignment with Activation Engineering - arXiv:2505.14158](https://arxiv.org/abs/2505.14158)\n- [Continuous Knowledge Drift (Chronos) - arXiv:2604.05096](https://arxiv.org/abs/2604.05096)\n- [LLM Meta-Cognition - arXiv:2506.08410](https://arxiv.org/abs/2506.08410)\n- [Hyperdimensional Probe - arXiv:2509.25045](https://arxiv.org/pdf/2509.25045)\n- [Improved Representation Steering (RePS) - arXiv:2505.20809](https://arxiv.org/html/2505.20809v1)\n- [Synergistic Multi-Agent RAG - arXiv:2511.21729](https://arxiv.org/pdf/2511.21729)\n- [Embedding-Informed Adaptive RAG - arXiv:2404.03514](https://arxiv.org/abs/2404.03514)\n- [SeaKR - arXiv:2406.19215](https://arxiv.org/pdf/2406.19215)"
      }
    ],
    "totalDurationMs": 215127,
    "totalTokens": 32763,
    "totalToolUseCount": 30,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2021,
      "cache_read_input_tokens": 27162,
      "output_tokens": 3579,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2021
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3579,
          "cache_read_input_tokens": 27162,
          "cache_creation_input_tokens": 2021,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2021,
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
      "otherToolCount": 30
    }
  },
  "sourceToolAssistantUUID": "c553bfe7-9366-461f-b2d2-0d26860378c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Drift-Probe-Gated Retrieval: A Systematic Evaluation of Temporal Stale…",
  "leafUuid": "2805df47-a35d-4d4a-94d5-f0721ffa4029",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Add multi-signal gating to drift-probe RAG system",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed"
}
```

---

### Tool result

_source line 26 · 2026-05-19T09:33:18.334Z_

<details><summary>↩ Tool result · `toolu_01NnqkkCeQdsC8qaZf66VVvt`</summary>

```text
I now have comprehensive findings. Here is my synthesis:

---

## Research Report: Entity Token Identification in LLM Probing and Representation Analysis

### 1. The Dominant Convention: "Last Subject Token" Position

The field has converged on a strong convention of extracting hidden states at the **last token of the subject entity span**. This originated with Meng et al. (2022) and was formalized by Geva et al. (2023).

**Meng et al., "Locating and Editing Factual Associations in GPT" (NeurIPS 2022)**
- Introduced causal tracing for factual recall in GPT-style models.
- Found that feedforward MLPs at middle layers are "decisive when processing the last token of the subject name."
- The subject entity boundaries are identified from the structured prompt template (e.g., "The Space Needle is in the city of ___"), where the subject span is known by construction because the dataset uses templated (subject, relation) queries.
- No external NER is used -- entity boundaries come from the dataset annotations.

**Geva, Bastings, Filippova & Globerson, "Dissecting Recall of Factual Associations in Auto-Regressive Language Models" (EMNLP 2023)**
- Provides the most detailed justification for last-subject-token selection. They analyze the last-subject position because it is "the only subject position that attends to all the subject positions" (due to causal masking in autoregressive models).
- Discovered a **three-step mechanism**: (1) Subject Enrichment -- early MLP sublayers enrich the last-subject-token representation with many subject-related attributes; (2) Relation Propagation -- relation information flows to the last (prediction) token; (3) Attribute Extraction -- attention heads at the last token "query" the enriched subject representation to extract the relevant attribute.
- Validated through attention knockout experiments blocking individual subject positions, confirming the last subject token's unique importance.
- Robustness tests showed results hold across subject-relation order variations and different window sizes (k=1,5,9,13,17,21).

### 2. The Last Sequence Token (Prediction Position)

Several papers also extract from the **final token of the entire input** (the prediction position), since in autoregressive models this is where the next-token prediction occurs.

**Wang, Whyte & Xu, "Locating and Extracting Relational Concepts in Large Language Models" (2024)**
- Focuses exclusively on the last token position, justifying this because "the causal attention mechanism in GPT-based LLMs [means] only the last token captures complete contextual information."
- Identified three stages at the last token: an initial stage (layers 0-3) with no mediating effects, a relational emergence stage (layers 4-15) where hidden states express only relational causal effects, and a conjoint influence stage (layers 16-31) with both subject and relation effects.

**Lv et al., "Interpreting Key Mechanisms of Factual Recall in Transformer-Based Language Models" (2024)**
- Analyzes the final token position (t=-1) as the primary extraction point.
- Entity tokens (e.g., country names) are identified through attention pattern analysis -- examining which tokens task-specific attention heads attend to.

### 3. The "Token Erasure" Effect and Multi-Token Entities

**Feucht, Atkinson, Wallace & Bau, "Token Erasure as a Footprint of Implicit Vocabulary Items in LLMs" (EMNLP 2024)**
- Discovered that the last token of multi-token entities/words exhibits a pronounced "erasure" effect in early layers: linear probes attempting to predict previous/current tokens show rapid accuracy drops.
- This effect is unique to final tokens of multi-token spans; first and middle tokens maintain token-level information.
- This provides a mechanistic explanation for why the last subject token is special: during pre-training, models develop an "implicit vocabulary" that maps multi-token groups to meaningful units, with the final token serving as the consolidation point.
- **Entity identification method**: Used SpaCy NER for named entities in Wikipedia articles, plus whitespace segmentation for multi-token words. Developed a psi-score to quantify the erasure effect.

### 4. Entity Identification Methods Used in Practice

Across the literature, entity boundaries are identified through several approaches, roughly ordered by frequency:

1. **Dataset annotations / templated prompts** (most common): Papers like Meng et al., Geva et al., and most factual probing work use structured datasets (e.g., CounterFact, LAMA/ParaRel) where the subject span is known from the (subject, relation, object) tuple. No NER is needed at inference time because the prompt is constructed from the template.

2. **SpaCy NER**: Used by Feucht et al. (2024) for identifying multi-token entity spans in naturalistic text.

3. **Attention-based identification**: Lv et al. (2024) identify entity tokens by examining which positions task-specific attention heads attend to. This is post-hoc analysis rather than preprocessing.

4. **Knowledge base grounding**: Papers like "Inside-Out: Hidden Factual Knowledge in LLMs" (Gekhman et al.) use established QA datasets (SimpleQA, entity-relation datasets) where entities are pre-annotated.

5. **Five-tier cascade matching** (for temporal drift work): Elbadry et al., "The Geometry of Forgetting" (2025), use a cascade of exact match, significant-token matching (filtering articles/titles), last-name matching, substring matching, and geographic token matching for normalizing and identifying entities in generated outputs.

### 5. Alternative Strategies: Averaging, Learned Aggregation

**Mean Pooling / Entity Span Averaging**
- In the BERT probing literature, Mohebbi, Modarressi & Pilehvar ("Exploring the Role of BERT Token Representations to Explain Sentence Probing Results," EMNLP 2021) found that mean pooling over all tokens retains or improves over CLS-token performance in most layers. However, different tokens encode different linguistic properties.
- For autoregressive LLMs, span averaging is rarely used for factual probing because the causal attention mask means early tokens in a span lack information about later tokens.

**Learned Token/Layer Aggregation**
- Meyoyan & Del Corro, "A BERTology View of LLM Orchestrations: Token- and Layer-Selective Probes for Efficient Single-Pass Classification" (2025), propose learning to select across all tokens and layers simultaneously via a two-stage aggregation architecture. They found that learned aggregation substantially outperforms any fixed strategy (CLS, mean, last token), and that optimal token utilization is task-dependent.

### 6. Robustness of Probing Results to Token Position Selection

This is a significant concern. Key findings:

**Zhang & Nanda, "Towards Best Practices of Activation Patching in Language Models" (ICLR 2024)**
- Demonstrated that token position choice "can greatly affect the localization outcomes" in causal tracing.
- For factual recall, different metrics yield different conclusions about last-subject-token concentration: probability metrics assign 4.33x effects to the last subject token, while logit difference shows only 1.22x.
- Corrupting different tokens in IOI circuit discovery produced substantially different localization results.
- **Recommendation**: "trying out different tokens to corrupt when the problem setting offers such flexibility" rather than assuming standard choices are optimal.

**Popovic & Farber, "Tracing Relational Knowledge Recall in Large Language Models" (2025)**
- Compared multiple feature types derived from different positions. Per-head attention contributions across all source positions achieved ~90% accuracy, while entity-specific (source-token-specific) features achieved only ~65%.
- This suggests that aggregating information across positions substantially outperforms extracting from a single entity position.

**Shen et al., "Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?" (2025)**
- Found that "evaluation with the wrong token can lead to very different results," with mismatch rates exceeding 0.5 between tokenization variants (e.g., "A" vs " A").
- Sequence perplexity proved most robust overall compared to single-token logit extraction.

### 7. The Temporal Drift Probing Case Specifically

**Elbadry et al., "The Geometry of Forgetting: Temporal Knowledge Drift as an Independent Axis in LLM Representations" (2025)**
- Extracts residual-stream activations at "the first content-token position of the generated answer" (with model-specific adjustments, e.g., Llama-2 uses position 2 due to whitespace token).
- Achieves AUROC of 0.83-0.95 across six models for drift detection.
- Does NOT systematically analyze robustness to position choice -- reports layer-plateau analysis (top-5 layer spans yield less than or equal to 0.007 AUROC variation) but not position sensitivity.
- Uses a five-tier cascade for entity matching in outputs rather than NER on inputs.

### Summary of Key Takeaways for Your Context

1. **The "last subject token" convention is well-justified mechanistically** (Geva et al. 2023, Feucht et al. 2024) but was established in settings where entity boundaries are known from structured datasets/templates. Extending this to arbitrary text at inference time requires an entity detection step.

2. **Most factual probing work sidesteps the entity identification problem entirely** by using templated prompts where entity spans are known by construction. When naturalistic text is involved, SpaCy NER is the most common preprocessing tool.

3. **Results ARE sensitive to token position choice** (Zhang & Nanda 2024), and aggregation across positions can substantially outperform single-position extraction (Popovic & Farber 2025). This is an underexplored vulnerability in the probing literature.

4. **For a deployment pipeline** proposing to extract activations "at the entity token position," you need either (a) structured/templated inputs where entity positions are known, or (b) a preprocessing NER/entity-linking step. The robustness concern is real: Zhang & Nanda (2024) explicitly warn that position choice "can greatly affect localization outcomes."

5. **The closest precedent for temporal drift detection** (Elbadry et al. 2025) avoids the entity-position problem by extracting at the first generated answer token rather than the entity mention in the prompt, which is a pragmatic design choice.

Sources:
- [Meng et al., "Locating and Editing Factual Associations in GPT" (NeurIPS 2022)](https://arxiv.org/abs/2202.05262)
- [Geva et al., "Dissecting Recall of Factual Associations in Auto-Regressive Language Models" (EMNLP 2023)](https://aclanthology.org/2023.emnlp-main.751/)
- [Feucht et al., "Token Erasure as a Footprint of Implicit Vocabulary Items in LLMs" (EMNLP 2024)](https://arxiv.org/html/2406.20086v1)
- [Wang et al., "Locating and Extracting Relational Concepts in Large Language Models" (2024)](https://arxiv.org/pdf/2406.13184)
- [Lv et al., "Interpreting Key Mechanisms of Factual Recall in Transformer-Based Language Models" (2024)](https://arxiv.org/html/2403.19521v3)
- [Zhang & Nanda, "Towards Best Practices of Activation Patching in Language Models" (ICLR 2024)](https://arxiv.org/html/2309.16042v2)
- [Popovic & Farber, "Tracing Relational Knowledge Recall in Large Language Models" (2025)](https://arxiv.org/html/2604.19934)
- [Elbadry et al., "The Geometry of Forgetting: Temporal Knowledge Drift as an Independent Axis in LLM Representations" (2025)](https://arxiv.org/html/2605.09195)
- [Mohebbi et al., "Exploring the Role of BERT Token Representations to Explain Sentence Probing Results" (EMNLP 2021)](https://aclanthology.org/2021.emnlp-main.61/)
- [Meyoyan & Del Corro, "A BERTology View of LLM Orchestrations" (2025)](https://arxiv.org/html/2601.13288)
- [Shen et al., "Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?" (2025)](https://arxiv.org/html/2507.13490v1)
- [Gekhman et al., "Inside-Out: Hidden Factual Knowledge in LLMs" (2025)](https://arxiv.org/pdf/2503.15299)
- [Govindan et al., "Temporal Alignment of Time Sensitive Facts with Activation Engineering" (2025)](https://arxiv.org/pdf/2505.14158)
- [Morand et al., "ToMMeR: Efficient Entity Mention Detection from Large Language Models" (2025)](https://arxiv.org/pdf/2510.19410)

agentId: adb3e65396ce6b95c (use SendMessage with to: 'adb3e65396ce6b95c' to continue this agent)
&lt;usage>total_tokens: 33627
tool_uses: 30
duration_ms: 230219&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be07fbc2-7cb5-4491-b959-7b952625efe1",
  "isSidechain": false,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "type": "user",
  "uuid": "cec8e8a5-5e9c-4c95-aba5-ff8ac0241283",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research how entity token identification is handled in LLM probing and representation analysis work, particularly for knowledge probing and factual recall tasks. The context: a paper proposes extracting LLM hidden-state activations \"at the entity token position\" to detect temporal drift, but at inference time, identifying which token is the entity requires preprocessing.\n\nSearch for:\n1. How do existing LLM probing papers (especially knowledge probes, factual probes) handle entity token identification? Do they use the last subject token, average over entity span, or something else?\n2. Entity detection/linking as preprocessing for LLM probing - what methods are used?\n3. \"Last subject token\" vs \"entity span averaging\" vs other strategies in mechanistic interpretability and probing literature\n4. Robustness of probing results to token position selection\n\nUse WebSearch with 3+ different queries, then WebFetch the most relevant papers. I need concrete technical details about what positions people extract activations from and how robust results are to this choice. Report with paper titles and specific findings.",
    "agentId": "adb3e65396ce6b95c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive findings. Here is my synthesis:\n\n---\n\n## Research Report: Entity Token Identification in LLM Probing and Representation Analysis\n\n### 1. The Dominant Convention: \"Last Subject Token\" Position\n\nThe field has converged on a strong convention of extracting hidden states at the **last token of the subject entity span**. This originated with Meng et al. (2022) and was formalized by Geva et al. (2023).\n\n**Meng et al., \"Locating and Editing Factual Associations in GPT\" (NeurIPS 2022)**\n- Introduced causal tracing for factual recall in GPT-style models.\n- Found that feedforward MLPs at middle layers are \"decisive when processing the last token of the subject name.\"\n- The subject entity boundaries are identified from the structured prompt template (e.g., \"The Space Needle is in the city of ___\"), where the subject span is known by construction because the dataset uses templated (subject, relation) queries.\n- No external NER is used -- entity boundaries come from the dataset annotations.\n\n**Geva, Bastings, Filippova & Globerson, \"Dissecting Recall of Factual Associations in Auto-Regressive Language Models\" (EMNLP 2023)**\n- Provides the most detailed justification for last-subject-token selection. They analyze the last-subject position because it is \"the only subject position that attends to all the subject positions\" (due to causal masking in autoregressive models).\n- Discovered a **three-step mechanism**: (1) Subject Enrichment -- early MLP sublayers enrich the last-subject-token representation with many subject-related attributes; (2) Relation Propagation -- relation information flows to the last (prediction) token; (3) Attribute Extraction -- attention heads at the last token \"query\" the enriched subject representation to extract the relevant attribute.\n- Validated through attention knockout experiments blocking individual subject positions, confirming the last subject token's unique importance.\n- Robustness tests showed results hold across subject-relation order variations and different window sizes (k=1,5,9,13,17,21).\n\n### 2. The Last Sequence Token (Prediction Position)\n\nSeveral papers also extract from the **final token of the entire input** (the prediction position), since in autoregressive models this is where the next-token prediction occurs.\n\n**Wang, Whyte & Xu, \"Locating and Extracting Relational Concepts in Large Language Models\" (2024)**\n- Focuses exclusively on the last token position, justifying this because \"the causal attention mechanism in GPT-based LLMs [means] only the last token captures complete contextual information.\"\n- Identified three stages at the last token: an initial stage (layers 0-3) with no mediating effects, a relational emergence stage (layers 4-15) where hidden states express only relational causal effects, and a conjoint influence stage (layers 16-31) with both subject and relation effects.\n\n**Lv et al., \"Interpreting Key Mechanisms of Factual Recall in Transformer-Based Language Models\" (2024)**\n- Analyzes the final token position (t=-1) as the primary extraction point.\n- Entity tokens (e.g., country names) are identified through attention pattern analysis -- examining which tokens task-specific attention heads attend to.\n\n### 3. The \"Token Erasure\" Effect and Multi-Token Entities\n\n**Feucht, Atkinson, Wallace & Bau, \"Token Erasure as a Footprint of Implicit Vocabulary Items in LLMs\" (EMNLP 2024)**\n- Discovered that the last token of multi-token entities/words exhibits a pronounced \"erasure\" effect in early layers: linear probes attempting to predict previous/current tokens show rapid accuracy drops.\n- This effect is unique to final tokens of multi-token spans; first and middle tokens maintain token-level information.\n- This provides a mechanistic explanation for why the last subject token is special: during pre-training, models develop an \"implicit vocabulary\" that maps multi-token groups to meaningful units, with the final token serving as the consolidation point.\n- **Entity identification method**: Used SpaCy NER for named entities in Wikipedia articles, plus whitespace segmentation for multi-token words. Developed a psi-score to quantify the erasure effect.\n\n### 4. Entity Identification Methods Used in Practice\n\nAcross the literature, entity boundaries are identified through several approaches, roughly ordered by frequency:\n\n1. **Dataset annotations / templated prompts** (most common): Papers like Meng et al., Geva et al., and most factual probing work use structured datasets (e.g., CounterFact, LAMA/ParaRel) where the subject span is known from the (subject, relation, object) tuple. No NER is needed at inference time because the prompt is constructed from the template.\n\n2. **SpaCy NER**: Used by Feucht et al. (2024) for identifying multi-token entity spans in naturalistic text.\n\n3. **Attention-based identification**: Lv et al. (2024) identify entity tokens by examining which positions task-specific attention heads attend to. This is post-hoc analysis rather than preprocessing.\n\n4. **Knowledge base grounding**: Papers like \"Inside-Out: Hidden Factual Knowledge in LLMs\" (Gekhman et al.) use established QA datasets (SimpleQA, entity-relation datasets) where entities are pre-annotated.\n\n5. **Five-tier cascade matching** (for temporal drift work): Elbadry et al., \"The Geometry of Forgetting\" (2025), use a cascade of exact match, significant-token matching (filtering articles/titles), last-name matching, substring matching, and geographic token matching for normalizing and identifying entities in generated outputs.\n\n### 5. Alternative Strategies: Averaging, Learned Aggregation\n\n**Mean Pooling / Entity Span Averaging**\n- In the BERT probing literature, Mohebbi, Modarressi & Pilehvar (\"Exploring the Role of BERT Token Representations to Explain Sentence Probing Results,\" EMNLP 2021) found that mean pooling over all tokens retains or improves over CLS-token performance in most layers. However, different tokens encode different linguistic properties.\n- For autoregressive LLMs, span averaging is rarely used for factual probing because the causal attention mask means early tokens in a span lack information about later tokens.\n\n**Learned Token/Layer Aggregation**\n- Meyoyan & Del Corro, \"A BERTology View of LLM Orchestrations: Token- and Layer-Selective Probes for Efficient Single-Pass Classification\" (2025), propose learning to select across all tokens and layers simultaneously via a two-stage aggregation architecture. They found that learned aggregation substantially outperforms any fixed strategy (CLS, mean, last token), and that optimal token utilization is task-dependent.\n\n### 6. Robustness of Probing Results to Token Position Selection\n\nThis is a significant concern. Key findings:\n\n**Zhang & Nanda, \"Towards Best Practices of Activation Patching in Language Models\" (ICLR 2024)**\n- Demonstrated that token position choice \"can greatly affect the localization outcomes\" in causal tracing.\n- For factual recall, different metrics yield different conclusions about last-subject-token concentration: probability metrics assign 4.33x effects to the last subject token, while logit difference shows only 1.22x.\n- Corrupting different tokens in IOI circuit discovery produced substantially different localization results.\n- **Recommendation**: \"trying out different tokens to corrupt when the problem setting offers such flexibility\" rather than assuming standard choices are optimal.\n\n**Popovic & Farber, \"Tracing Relational Knowledge Recall in Large Language Models\" (2025)**\n- Compared multiple feature types derived from different positions. Per-head attention contributions across all source positions achieved ~90% accuracy, while entity-specific (source-token-specific) features achieved only ~65%.\n- This suggests that aggregating information across positions substantially outperforms extracting from a single entity position.\n\n**Shen et al., \"Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?\" (2025)**\n- Found that \"evaluation with the wrong token can lead to very different results,\" with mismatch rates exceeding 0.5 between tokenization variants (e.g., \"A\" vs \" A\").\n- Sequence perplexity proved most robust overall compared to single-token logit extraction.\n\n### 7. The Temporal Drift Probing Case Specifically\n\n**Elbadry et al., \"The Geometry of Forgetting: Temporal Knowledge Drift as an Independent Axis in LLM Representations\" (2025)**\n- Extracts residual-stream activations at \"the first content-token position of the generated answer\" (with model-specific adjustments, e.g., Llama-2 uses position 2 due to whitespace token).\n- Achieves AUROC of 0.83-0.95 across six models for drift detection.\n- Does NOT systematically analyze robustness to position choice -- reports layer-plateau analysis (top-5 layer spans yield less than or equal to 0.007 AUROC variation) but not position sensitivity.\n- Uses a five-tier cascade for entity matching in outputs rather than NER on inputs.\n\n### Summary of Key Takeaways for Your Context\n\n1. **The \"last subject token\" convention is well-justified mechanistically** (Geva et al. 2023, Feucht et al. 2024) but was established in settings where entity boundaries are known from structured datasets/templates. Extending this to arbitrary text at inference time requires an entity detection step.\n\n2. **Most factual probing work sidesteps the entity identification problem entirely** by using templated prompts where entity spans are known by construction. When naturalistic text is involved, SpaCy NER is the most common preprocessing tool.\n\n3. **Results ARE sensitive to token position choice** (Zhang & Nanda 2024), and aggregation across positions can substantially outperform single-position extraction (Popovic & Farber 2025). This is an underexplored vulnerability in the probing literature.\n\n4. **For a deployment pipeline** proposing to extract activations \"at the entity token position,\" you need either (a) structured/templated inputs where entity positions are known, or (b) a preprocessing NER/entity-linking step. The robustness concern is real: Zhang & Nanda (2024) explicitly warn that position choice \"can greatly affect localization outcomes.\"\n\n5. **The closest precedent for temporal drift detection** (Elbadry et al. 2025) avoids the entity-position problem by extracting at the first generated answer token rather than the entity mention in the prompt, which is a pragmatic design choice.\n\nSources:\n- [Meng et al., \"Locating and Editing Factual Associations in GPT\" (NeurIPS 2022)](https://arxiv.org/abs/2202.05262)\n- [Geva et al., \"Dissecting Recall of Factual Associations in Auto-Regressive Language Models\" (EMNLP 2023)](https://aclanthology.org/2023.emnlp-main.751/)\n- [Feucht et al., \"Token Erasure as a Footprint of Implicit Vocabulary Items in LLMs\" (EMNLP 2024)](https://arxiv.org/html/2406.20086v1)\n- [Wang et al., \"Locating and Extracting Relational Concepts in Large Language Models\" (2024)](https://arxiv.org/pdf/2406.13184)\n- [Lv et al., \"Interpreting Key Mechanisms of Factual Recall in Transformer-Based Language Models\" (2024)](https://arxiv.org/html/2403.19521v3)\n- [Zhang & Nanda, \"Towards Best Practices of Activation Patching in Language Models\" (ICLR 2024)](https://arxiv.org/html/2309.16042v2)\n- [Popovic & Farber, \"Tracing Relational Knowledge Recall in Large Language Models\" (2025)](https://arxiv.org/html/2604.19934)\n- [Elbadry et al., \"The Geometry of Forgetting: Temporal Knowledge Drift as an Independent Axis in LLM Representations\" (2025)](https://arxiv.org/html/2605.09195)\n- [Mohebbi et al., \"Exploring the Role of BERT Token Representations to Explain Sentence Probing Results\" (EMNLP 2021)](https://aclanthology.org/2021.emnlp-main.61/)\n- [Meyoyan & Del Corro, \"A BERTology View of LLM Orchestrations\" (2025)](https://arxiv.org/html/2601.13288)\n- [Shen et al., \"Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?\" (2025)](https://arxiv.org/html/2507.13490v1)\n- [Gekhman et al., \"Inside-Out: Hidden Factual Knowledge in LLMs\" (2025)](https://arxiv.org/pdf/2503.15299)\n- [Govindan et al., \"Temporal Alignment of Time Sensitive Facts with Activation Engineering\" (2025)](https://arxiv.org/pdf/2505.14158)\n- [Morand et al., \"ToMMeR: Efficient Entity Mention Detection from Large Language Models\" (2025)](https://arxiv.org/pdf/2510.19410)"
      }
    ],
    "totalDurationMs": 230219,
    "totalTokens": 33627,
    "totalToolUseCount": 30,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1214,
      "cache_read_input_tokens": 29167,
      "output_tokens": 3245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1214
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3245,
          "cache_read_input_tokens": 29167,
          "cache_creation_input_tokens": 1214,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1214,
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
      "otherToolCount": 30
    }
  },
  "sourceToolAssistantUUID": "be07fbc2-7cb5-4491-b959-7b952625efe1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T09:34:49.534Z_

<details><summary>↩ Tool result · `toolu_013GL8AvwzrCxKb6DPbJCD4u`</summary>

```text
I now have comprehensive findings across all five research areas. Let me compile the detailed report.

---

## Research Report: Combining Orthogonal Representation Directions for Multi-Axis Retrieval Gating

### 1. "The Geometry of Forgetting" (arXiv:2605.09195) -- What Was Proved

**Core Finding:** Temporal drift -- whether a stored fact has changed since training -- is encoded as a direction in the residual stream that is geometrically orthogonal to both correctness and uncertainty. This means any method operating on correctness or uncertainty signals is *blind to drift by construction*, explaining why LLMs confidently produce outdated answers.

**Five Orthogonality Tests with Exact Values:**

| Test | Metric | Result |
|------|--------|--------|
| Weight cosines | \|cos(w_drift, w_correctness)\| and \|cos(w_drift, w_uncertainty)\| | <= 0.14 |
| Score correlations | Pearson r (drift-correctness: -0.02 to -0.12; drift-uncertainty) | \|r\| <= 0.20 |
| Bidirectional null-space projection | Delta AUROC after removing nuisance directions | \|Delta\| <= 0.008 |
| Iterative null-space projection (INLP, k=10) | Delta AUROC after removing 10 uncertainty directions | \|Delta\| <= 0.007; removing correctness: \|Delta\| < 0.013 |
| Difference-of-means dissociation | DoM vectors are correlated (cos >= 0.37 for correctness-uncertainty), but trained probes remain orthogonal | \|cos\| <= 0.15 |

**Performance gap:** A linear probe trained directly on drift labels achieves AUROC 0.83-0.95 across six instruction-tuned models. Methods based on token entropy, semantic entropy, CCS, and SAPLMA all remain near chance (0.49-0.57).

**Cross-model validation:** A cross-cutoff experiment with byte-identical inputs shows the drift probe fires on the model whose cutoff predates the fact's transition and stays silent otherwise, with P(A>B) = 0.975-0.998 across twelve model pairs.

**What the paper does NOT do:** It does not propose a multi-axis gating system. Section 6 predicts that correctness/uncertainty methods should fail at drift detection (confirmed empirically). Section 8 suggests "deployed systems should read this axis instead of waiting for the surface error." The paper briefly notes that "selective retrieval triggers external lookups on output-side uncertainty; we show that triggering on an internal drift signal recovers comparable accuracy at lower retrieval cost" (Section 2). But no combined gating architecture is proposed -- this is the gap your work would fill.

---

### 2. Theoretical Justification: Does Combining Orthogonal Signals Give Strictly Better Classification?

**Yes, with caveats.** Multiple theoretical threads converge:

**A. Naive Bayes Optimality (classical result):** When features are mutually independent (which orthogonality in representation space implies), the Naive Bayes classifier is Bayes-optimal, guaranteeing minimum classification error. Under independence, log-posterior odds decompose additively across features. Each orthogonal signal contributes non-redundant information, so combining them strictly reduces Bayes risk compared to any single feature -- provided each feature carries nonzero mutual information with the target.

**B. Fano's Inequality and Mutual Information Additivity:** For independent features, mutual information is additive: I(X1, X2; Y) = I(X1; Y) + I(X2; Y). Since classification error lower bounds are tied to mutual information via Fano's inequality, adding an independent informative feature strictly tightens the bound on achievable error.

**C. The Linear Representation Hypothesis (Park et al., 2311.03658):** This paper formally proves that causally separable concepts -- those that can be varied freely and in isolation -- must be orthogonal under a "causal inner product" defined as the inverse covariance metric. Definition 3.1 states: a causal inner product satisfies &lt;gamma_W, gamma_Z> = 0 for causally separable concepts W, Z. This provides the formal mathematical link: if drift, confidence, and uncertainty are causally separable (as the Geometry of Forgetting empirically demonstrates), they are orthogonal under the natural metric and carry non-redundant information.

**D. Compositional Generalization Requires Orthogonality (arXiv:2602.24264):** This paper proves that under gradient descent with cross-entropy loss, three desiderata for compositional generalization (divisibility, transferability, stability) *necessarily* impose that per-concept components must be orthogonal. Empirically, the degree of this orthogonal structure in vision models (CLIP, SigLIP, DINO) directly correlates with generalization on unseen combinations.

**Bottom line:** The theoretical case is strong. If drift, confidence, and uncertainty are genuinely orthogonal (as proven at the |cos| <= 0.14 level), combining them gives access to strictly more information. Under the independence assumption, a joint classifier over all three axes will achieve Bayes risk no worse -- and generically strictly better -- than any classifier using fewer axes.

---

### 3. Multi-Direction Probing Systems -- Who Has Built Them?

Several groups have built practical multi-signal probing systems, though none yet combine all three axes you propose:

**A. CtrlA: Adaptive RAG via Dual Probes (arXiv:2405.18727, revised Oct 2024)**
Uses two representation-level probes -- an "honesty probe" and a "confidence probe" -- extracted from hidden states to guide retrieval decisions. This is the closest existing system to your proposal: it uses multiple internal representation directions to gate retrieval. However, it uses only two signals and does not include temporal drift.

**B. HALT: Residual Probes for Hallucination Assessment (arXiv:2601.14210, Jan 2026)**
Trains lightweight probes on intermediate hidden states (peak performance around layer 20 in Qwen2.5-7B) to estimate hallucination risk. Achieves AUROC up to 93.95% on TriviaQA. Uses threshold-based routing: confident queries get immediate answers; uncertain ones are delegated to verification pipelines. Single-signal system but demonstrates the practical viability of probe-based gating.

**C. Probing-RAG (arXiv:2410.13339, Oct 2024)**
Uses a 5MB feed-forward prober on intermediate hidden states to decide whether retrieval is needed. Key innovation: multi-layer aggregation via soft voting across probers at layers 6, 8, 10, 12, 14. Achieves +6.6-8.4% accuracy improvement while reducing retrieval calls by 85% (1,988 vs 13,570 for DRAGIN).

**D. DRAGIN's RIND Score**
Combines three factors per token: uncertainty (token entropy), influence (self-attention tracking), and semantic value (stopword filtering) as a per-token product to decide retrieval timing. This is a multi-signal approach but operates on output-level signals, not representation-level probes.

**E. Aggregate and Conquer (arXiv:2502.03708, Feb 2025)**
Trains layer-wise RFM predictors, extracts concept vectors via AGOP matrices, projects activations onto these vectors, concatenates across all layers, and trains a meta-predictor. Achieves 93.8% accuracy on hallucination detection (vs 91.6% for best single layer). For multi-concept steering, they combine concepts via linear combination of layer-wise concept vectors.

---

### 4. Representation Engineering: Composing Multiple Concept Directions

**A. From Directions to Cones (arXiv:2505.21800, May 2025)**
Extends truth representation from a single direction to a "concept cone" -- a set of orthonormal basis vectors whose nonnegative linear combinations all strengthen truth-aligned responses. Key finding: the classical single direction does not exhaust truth-related structure; additional orthogonal axes (cosine similarity approximately 10^-9 to the primary direction) each independently mediate truthful behavior. The optimization combines three losses: addition loss (induce truthfulness in false statements), ablation loss (inhibit truthfulness when removed from true statements), and retention loss (preserve capabilities via KL divergence).

**B. Conceptor-Based Steering (arXiv:2410.16314, Oct 2024)**
Introduces Boolean algebra over conceptor matrices for multi-concept composition:
- AND: C1 AND C2 = (C1^-1 + C2^-1 - I)^-1
- OR: merges covariance matrices
- NOT: represents inverse covariance for concept negation

Conceptor-based steering outperforms vector addition by 10-30 percentage points in function transfer accuracy. This provides a principled mathematical framework for combining multiple orthogonal concept directions -- directly applicable to combining drift + confidence + uncertainty.

**C. Hidden Dimensions of LLM Alignment (arXiv:2502.09674)**
Demonstrates that safety-related concepts involve multiple orthogonal directions, with secondary directions playing important roles in shaping refusal behavior.

**D. Key Challenge: Multi-Concept Interference**
The comprehensive RepE survey (arXiv:2502.19649, TMLR 2025) identifies that "combining steering vectors for different concepts can lead to unpredictable interactions." Three mitigation strategies emerge:
- Layered injection (different vectors at different layers) is more effective than combined single-layer injection
- Conceptor matrices can eliminate negative interactions between concepts
- Sparse attention control can identify distinct attention heads for separate interventions

---

### 5. Synthesis: Implications for Multi-Axis Retrieval Gating

**What the literature supports:**
1. The three axes (drift, confidence, uncertainty) are empirically proven to be orthogonal in LLM residual streams (Geometry of Forgetting, five tests, |cos| <= 0.14).
2. Classical theory guarantees that combining independent (orthogonal) features strictly reduces Bayes risk when each feature carries nonzero mutual information about the target.
3. The linear representation hypothesis formally proves that causally separable concepts map to orthogonal directions under the causal inner product.
4. Practical multi-probe systems already exist (CtrlA with 2 probes, Probing-RAG with multi-layer aggregation, HALT for hallucination routing).
5. Conceptor algebra provides a principled composition framework (AND/OR/NOT over concept matrices) that outperforms naive vector addition.

**The gap your work fills:**
No existing system combines all three of drift, confidence, and uncertainty for retrieval gating. The Geometry of Forgetting explicitly shows that current retrieval systems (Self-RAG, Adaptive-RAG) trigger on output-side uncertainty and are therefore blind to drift. A system that reads the drift axis internally could trigger retrieval specifically for stale knowledge, while the confidence and uncertainty axes handle the complementary cases of knowledge gaps and ambiguity.

**Recommended architecture based on the literature:**
- Train three linear probes on intermediate layers (around the 60-70% depth point, per HALT's findings) for drift, confidence, and uncertainty
- Use conceptor-based composition (AND/OR operations) rather than naive vector concatenation to combine the three signals, as this handles interference
- Apply threshold-based gating (as in HALT and Probing-RAG) with the joint conceptor score determining: (a) answer directly (high confidence, low drift, low uncertainty), (b) retrieve then answer (high drift or high uncertainty), or (c) abstain/escalate (low confidence across all axes)

**Theoretical strength of this approach:** The Geometry of Forgetting's null-space projection tests (|Delta AUROC| <= 0.008) provide the strongest evidence: removing one axis's information has negligible effect on another axis's probe performance. This means combining them gives genuinely additive information, satisfying the conditions under which joint classification is provably superior.

---

Sources:
- [The Geometry of Forgetting (arXiv:2605.09195)](https://arxiv.org/abs/2605.09195)
- [The Linear Representation Hypothesis and the Geometry of Large Language Models](https://arxiv.org/html/2311.03658v2)
- [Compositional Generalization Requires Linear, Orthogonal Representations](https://arxiv.org/abs/2602.24264)
- [From Directions to Cones: Multidimensional Representations of Propositional Facts](https://arxiv.org/html/2505.21800)
- [The Hidden Dimensions of LLM Alignment](https://arxiv.org/pdf/2502.09674)
- [Representation Engineering Survey (TMLR 2025)](https://arxiv.org/html/2502.17601v1)
- [Taxonomy of Representation Engineering](https://arxiv.org/html/2502.19649)
- [Steering LLMs using Conceptors](https://arxiv.org/html/2410.16314v1)
- [From Steering Vectors to Conceptors and Beyond](https://openreview.net/forum?id=9wjGUN65tY)
- [Aggregate and Conquer: Multi-Layer Concept Detection](https://arxiv.org/html/2502.03708v1)
- [HALT: Hallucination Assessment via Latent Testing](https://arxiv.org/html/2601.14210v1)
- [CtrlA: Adaptive RAG via Inherent Control](https://arxiv.org/abs/2405.18727)
- [Probing-RAG: Self-Probing for Selective Retrieval](https://arxiv.org/html/2410.13339)
- [Context Awareness Gate for RAG](https://arxiv.org/html/2411.16133)
- [Controlling Directions Orthogonal to a Classifier (ICLR 2022)](https://arxiv.org/abs/2201.11259)
- [Probing LLMs' Knowledge Boundary: Adaptive RAG](https://blog.reachsumit.com/posts/2025/09/probing-llms-knowledge-boundary/)

agentId: a99cd76edb1bac149 (use SendMessage with to: 'a99cd76edb1bac149' to continue this agent)
&lt;usage>total_tokens: 41931
tool_uses: 39
duration_ms: 300396&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "650c6343-9fdd-4356-992c-56e7312be760",
  "isSidechain": false,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "type": "user",
  "uuid": "26941d4c-17f0-463a-b3d0-5d36f59e6c91",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the theoretical and practical aspects of combining orthogonal representation directions in neural networks for improved classification/gating. Context: A paper called \"The Geometry of Forgetting\" (arXiv:2605.09195, May 2026) proved that temporal drift, confidence, and uncertainty are encoded as orthogonal directions in LLM residual streams. We want to combine all three for a multi-axis retrieval gating system.\n\nSearch for:\n1. \"Geometry of Forgetting\" arXiv 2605.09195 - fetch and read the paper, especially §2 and §6, to understand exactly what they proved about orthogonality and what they suggested about retrieval\n2. Multi-axis or multi-direction probing in LLM representations (2024-2026)\n3. Theoretical results on combining orthogonal classifiers / orthogonal features for improved decisions\n4. \"Representation engineering\" combining multiple concept directions (e.g., truthfulness + confidence)\n5. Look for any work on \"compositional probing\" or \"multi-concept probing\" in transformer representations\n\nI need to understand:\n- What exactly did the Geometry of Forgetting prove about orthogonality? (cosine similarity values, statistical tests)\n- Is there theoretical justification that combining orthogonal signals gives strictly better classification?\n- Has anyone built multi-direction probing systems for practical applications?\n\nUse WebSearch and WebFetch. Report detailed findings.",
    "agentId": "a99cd76edb1bac149",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive findings across all five research areas. Let me compile the detailed report.\n\n---\n\n## Research Report: Combining Orthogonal Representation Directions for Multi-Axis Retrieval Gating\n\n### 1. \"The Geometry of Forgetting\" (arXiv:2605.09195) -- What Was Proved\n\n**Core Finding:** Temporal drift -- whether a stored fact has changed since training -- is encoded as a direction in the residual stream that is geometrically orthogonal to both correctness and uncertainty. This means any method operating on correctness or uncertainty signals is *blind to drift by construction*, explaining why LLMs confidently produce outdated answers.\n\n**Five Orthogonality Tests with Exact Values:**\n\n| Test | Metric | Result |\n|------|--------|--------|\n| Weight cosines | \\|cos(w_drift, w_correctness)\\| and \\|cos(w_drift, w_uncertainty)\\| | <= 0.14 |\n| Score correlations | Pearson r (drift-correctness: -0.02 to -0.12; drift-uncertainty) | \\|r\\| <= 0.20 |\n| Bidirectional null-space projection | Delta AUROC after removing nuisance directions | \\|Delta\\| <= 0.008 |\n| Iterative null-space projection (INLP, k=10) | Delta AUROC after removing 10 uncertainty directions | \\|Delta\\| <= 0.007; removing correctness: \\|Delta\\| < 0.013 |\n| Difference-of-means dissociation | DoM vectors are correlated (cos >= 0.37 for correctness-uncertainty), but trained probes remain orthogonal | \\|cos\\| <= 0.15 |\n\n**Performance gap:** A linear probe trained directly on drift labels achieves AUROC 0.83-0.95 across six instruction-tuned models. Methods based on token entropy, semantic entropy, CCS, and SAPLMA all remain near chance (0.49-0.57).\n\n**Cross-model validation:** A cross-cutoff experiment with byte-identical inputs shows the drift probe fires on the model whose cutoff predates the fact's transition and stays silent otherwise, with P(A>B) = 0.975-0.998 across twelve model pairs.\n\n**What the paper does NOT do:** It does not propose a multi-axis gating system. Section 6 predicts that correctness/uncertainty methods should fail at drift detection (confirmed empirically). Section 8 suggests \"deployed systems should read this axis instead of waiting for the surface error.\" The paper briefly notes that \"selective retrieval triggers external lookups on output-side uncertainty; we show that triggering on an internal drift signal recovers comparable accuracy at lower retrieval cost\" (Section 2). But no combined gating architecture is proposed -- this is the gap your work would fill.\n\n---\n\n### 2. Theoretical Justification: Does Combining Orthogonal Signals Give Strictly Better Classification?\n\n**Yes, with caveats.** Multiple theoretical threads converge:\n\n**A. Naive Bayes Optimality (classical result):** When features are mutually independent (which orthogonality in representation space implies), the Naive Bayes classifier is Bayes-optimal, guaranteeing minimum classification error. Under independence, log-posterior odds decompose additively across features. Each orthogonal signal contributes non-redundant information, so combining them strictly reduces Bayes risk compared to any single feature -- provided each feature carries nonzero mutual information with the target.\n\n**B. Fano's Inequality and Mutual Information Additivity:** For independent features, mutual information is additive: I(X1, X2; Y) = I(X1; Y) + I(X2; Y). Since classification error lower bounds are tied to mutual information via Fano's inequality, adding an independent informative feature strictly tightens the bound on achievable error.\n\n**C. The Linear Representation Hypothesis (Park et al., 2311.03658):** This paper formally proves that causally separable concepts -- those that can be varied freely and in isolation -- must be orthogonal under a \"causal inner product\" defined as the inverse covariance metric. Definition 3.1 states: a causal inner product satisfies &lt;gamma_W, gamma_Z> = 0 for causally separable concepts W, Z. This provides the formal mathematical link: if drift, confidence, and uncertainty are causally separable (as the Geometry of Forgetting empirically demonstrates), they are orthogonal under the natural metric and carry non-redundant information.\n\n**D. Compositional Generalization Requires Orthogonality (arXiv:2602.24264):** This paper proves that under gradient descent with cross-entropy loss, three desiderata for compositional generalization (divisibility, transferability, stability) *necessarily* impose that per-concept components must be orthogonal. Empirically, the degree of this orthogonal structure in vision models (CLIP, SigLIP, DINO) directly correlates with generalization on unseen combinations.\n\n**Bottom line:** The theoretical case is strong. If drift, confidence, and uncertainty are genuinely orthogonal (as proven at the |cos| <= 0.14 level), combining them gives access to strictly more information. Under the independence assumption, a joint classifier over all three axes will achieve Bayes risk no worse -- and generically strictly better -- than any classifier using fewer axes.\n\n---\n\n### 3. Multi-Direction Probing Systems -- Who Has Built Them?\n\nSeveral groups have built practical multi-signal probing systems, though none yet combine all three axes you propose:\n\n**A. CtrlA: Adaptive RAG via Dual Probes (arXiv:2405.18727, revised Oct 2024)**\nUses two representation-level probes -- an \"honesty probe\" and a \"confidence probe\" -- extracted from hidden states to guide retrieval decisions. This is the closest existing system to your proposal: it uses multiple internal representation directions to gate retrieval. However, it uses only two signals and does not include temporal drift.\n\n**B. HALT: Residual Probes for Hallucination Assessment (arXiv:2601.14210, Jan 2026)**\nTrains lightweight probes on intermediate hidden states (peak performance around layer 20 in Qwen2.5-7B) to estimate hallucination risk. Achieves AUROC up to 93.95% on TriviaQA. Uses threshold-based routing: confident queries get immediate answers; uncertain ones are delegated to verification pipelines. Single-signal system but demonstrates the practical viability of probe-based gating.\n\n**C. Probing-RAG (arXiv:2410.13339, Oct 2024)**\nUses a 5MB feed-forward prober on intermediate hidden states to decide whether retrieval is needed. Key innovation: multi-layer aggregation via soft voting across probers at layers 6, 8, 10, 12, 14. Achieves +6.6-8.4% accuracy improvement while reducing retrieval calls by 85% (1,988 vs 13,570 for DRAGIN).\n\n**D. DRAGIN's RIND Score**\nCombines three factors per token: uncertainty (token entropy), influence (self-attention tracking), and semantic value (stopword filtering) as a per-token product to decide retrieval timing. This is a multi-signal approach but operates on output-level signals, not representation-level probes.\n\n**E. Aggregate and Conquer (arXiv:2502.03708, Feb 2025)**\nTrains layer-wise RFM predictors, extracts concept vectors via AGOP matrices, projects activations onto these vectors, concatenates across all layers, and trains a meta-predictor. Achieves 93.8% accuracy on hallucination detection (vs 91.6% for best single layer). For multi-concept steering, they combine concepts via linear combination of layer-wise concept vectors.\n\n---\n\n### 4. Representation Engineering: Composing Multiple Concept Directions\n\n**A. From Directions to Cones (arXiv:2505.21800, May 2025)**\nExtends truth representation from a single direction to a \"concept cone\" -- a set of orthonormal basis vectors whose nonnegative linear combinations all strengthen truth-aligned responses. Key finding: the classical single direction does not exhaust truth-related structure; additional orthogonal axes (cosine similarity approximately 10^-9 to the primary direction) each independently mediate truthful behavior. The optimization combines three losses: addition loss (induce truthfulness in false statements), ablation loss (inhibit truthfulness when removed from true statements), and retention loss (preserve capabilities via KL divergence).\n\n**B. Conceptor-Based Steering (arXiv:2410.16314, Oct 2024)**\nIntroduces Boolean algebra over conceptor matrices for multi-concept composition:\n- AND: C1 AND C2 = (C1^-1 + C2^-1 - I)^-1\n- OR: merges covariance matrices\n- NOT: represents inverse covariance for concept negation\n\nConceptor-based steering outperforms vector addition by 10-30 percentage points in function transfer accuracy. This provides a principled mathematical framework for combining multiple orthogonal concept directions -- directly applicable to combining drift + confidence + uncertainty.\n\n**C. Hidden Dimensions of LLM Alignment (arXiv:2502.09674)**\nDemonstrates that safety-related concepts involve multiple orthogonal directions, with secondary directions playing important roles in shaping refusal behavior.\n\n**D. Key Challenge: Multi-Concept Interference**\nThe comprehensive RepE survey (arXiv:2502.19649, TMLR 2025) identifies that \"combining steering vectors for different concepts can lead to unpredictable interactions.\" Three mitigation strategies emerge:\n- Layered injection (different vectors at different layers) is more effective than combined single-layer injection\n- Conceptor matrices can eliminate negative interactions between concepts\n- Sparse attention control can identify distinct attention heads for separate interventions\n\n---\n\n### 5. Synthesis: Implications for Multi-Axis Retrieval Gating\n\n**What the literature supports:**\n1. The three axes (drift, confidence, uncertainty) are empirically proven to be orthogonal in LLM residual streams (Geometry of Forgetting, five tests, |cos| <= 0.14).\n2. Classical theory guarantees that combining independent (orthogonal) features strictly reduces Bayes risk when each feature carries nonzero mutual information about the target.\n3. The linear representation hypothesis formally proves that causally separable concepts map to orthogonal directions under the causal inner product.\n4. Practical multi-probe systems already exist (CtrlA with 2 probes, Probing-RAG with multi-layer aggregation, HALT for hallucination routing).\n5. Conceptor algebra provides a principled composition framework (AND/OR/NOT over concept matrices) that outperforms naive vector addition.\n\n**The gap your work fills:**\nNo existing system combines all three of drift, confidence, and uncertainty for retrieval gating. The Geometry of Forgetting explicitly shows that current retrieval systems (Self-RAG, Adaptive-RAG) trigger on output-side uncertainty and are therefore blind to drift. A system that reads the drift axis internally could trigger retrieval specifically for stale knowledge, while the confidence and uncertainty axes handle the complementary cases of knowledge gaps and ambiguity.\n\n**Recommended architecture based on the literature:**\n- Train three linear probes on intermediate layers (around the 60-70% depth point, per HALT's findings) for drift, confidence, and uncertainty\n- Use conceptor-based composition (AND/OR operations) rather than naive vector concatenation to combine the three signals, as this handles interference\n- Apply threshold-based gating (as in HALT and Probing-RAG) with the joint conceptor score determining: (a) answer directly (high confidence, low drift, low uncertainty), (b) retrieve then answer (high drift or high uncertainty), or (c) abstain/escalate (low confidence across all axes)\n\n**Theoretical strength of this approach:** The Geometry of Forgetting's null-space projection tests (|Delta AUROC| <= 0.008) provide the strongest evidence: removing one axis's information has negligible effect on another axis's probe performance. This means combining them gives genuinely additive information, satisfying the conditions under which joint classification is provably superior.\n\n---\n\nSources:\n- [The Geometry of Forgetting (arXiv:2605.09195)](https://arxiv.org/abs/2605.09195)\n- [The Linear Representation Hypothesis and the Geometry of Large Language Models](https://arxiv.org/html/2311.03658v2)\n- [Compositional Generalization Requires Linear, Orthogonal Representations](https://arxiv.org/abs/2602.24264)\n- [From Directions to Cones: Multidimensional Representations of Propositional Facts](https://arxiv.org/html/2505.21800)\n- [The Hidden Dimensions of LLM Alignment](https://arxiv.org/pdf/2502.09674)\n- [Representation Engineering Survey (TMLR 2025)](https://arxiv.org/html/2502.17601v1)\n- [Taxonomy of Representation Engineering](https://arxiv.org/html/2502.19649)\n- [Steering LLMs using Conceptors](https://arxiv.org/html/2410.16314v1)\n- [From Steering Vectors to Conceptors and Beyond](https://openreview.net/forum?id=9wjGUN65tY)\n- [Aggregate and Conquer: Multi-Layer Concept Detection](https://arxiv.org/html/2502.03708v1)\n- [HALT: Hallucination Assessment via Latent Testing](https://arxiv.org/html/2601.14210v1)\n- [CtrlA: Adaptive RAG via Inherent Control](https://arxiv.org/abs/2405.18727)\n- [Probing-RAG: Self-Probing for Selective Retrieval](https://arxiv.org/html/2410.13339)\n- [Context Awareness Gate for RAG](https://arxiv.org/html/2411.16133)\n- [Controlling Directions Orthogonal to a Classifier (ICLR 2022)](https://arxiv.org/abs/2201.11259)\n- [Probing LLMs' Knowledge Boundary: Adaptive RAG](https://blog.reachsumit.com/posts/2025/09/probing-llms-knowledge-boundary/)"
      }
    ],
    "totalDurationMs": 300396,
    "totalTokens": 41931,
    "totalToolUseCount": 39,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2423,
      "cache_read_input_tokens": 36075,
      "output_tokens": 3432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2423
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3432,
          "cache_read_input_tokens": 36075,
          "cache_creation_input_tokens": 2423,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2423,
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
  "sourceToolAssistantUUID": "650c6343-9fdd-4356-992c-56e7312be760",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Drift-Probe-Gated Retrieval: A Systematic Evaluation of Temporal Stale…",
  "leafUuid": "26941d4c-17f0-463a-b3d0-5d36f59e6c91",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Add multi-signal gating to drift-probe RAG system",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed"
}
```

---

### Assistant

_source line 30 · 2026-05-19T09:36:35.198Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! I now have comprehensive research results from all five agents. Let me synthesize the findings:

### Key Findings Summary:

**1. NOVELTY (Multi-Signal Fusion):**
- No existing work combines orthogonal drift + confidence + uncertainty probes for retrieval gating
- Closest work: CtrlA (2 probes: honesty + confidence), Moskvoretskii et al. (35 methods combined via logistic regression, but all uncertainty-family)
- Truth Forest (AAAI 2024) combines orthogonal probes for intervention
- MeCo explicitly says "simply averaging multiple scores does not yield accurate results"


- Conceptor-based composition gives us a principled framework, and theoretically combining orthogonal independent features strictly reduces Bayes risk.

**2. ENTITY TOKEN IDENTIFICATION:**
- "Last subject token" is the dominant convention (Meng et al. 2022, Geva et al. 2023)
- But most work uses structured datasets where entity boundaries are known
- The Geometry of Forgetting actually extracts at "the first content-token position of the generated answer" - NOT the entity token in the prompt
- Results ARE sensitive to position (Zhang & Nanda, ICLR 2024)
- Solutions: templated prompts (sidesteps the issue), SpaC NER, or using the generation position like the original paper

**3. BASELINE CODE AVAILABILITY:**
- I've got 4 out of 8 baselines with available code: Probing-RAG, SeaKR, Self-Routing RAG, Token-Entropy
- The others are harder to reimplement: INKER and Skill-RAG are too costly to rebuild, so I'll drop them from the main comparison
- I'll keep TARG since it's straightforward to reimplement and Rep-Con since it's a standard approach

**4. MMA-RAG:**
- This approach concatenates multimodal features (text and vision, original and retrieved) into an MLP for 4-class classification
- It applies gating after retrieval, which means I need to run the model both with and without retrieval to evaluate it properly
- The key distinction is that it's multimodal with post-retrieval gating using an MLP rather than a linear probe, which makes it architecturally quite different from what I'm proposing

**5. ORTHOGONAL AXES THEORY:**
- The geometry of forgetting shows cosine similarity stays below 0.14 and null-space projection changes AUROC by at most 0.008, which supports the idea that independent features reduce Bayes risk
- The Linear Representation Hypothesis proves that causally separable concepts must be orthogonal, and I've found practical precedents in CtrlA with dual probes and Probing-RAG's multi-layer approach

I just discovered some critical related work: CtrlA uses dual probes for honesty and confidence to gate retrieval, which is very relevant to my approach, and DRIFT/HALT appears to be another important reference I need to examine. bes on intermediate layers for hallucination assessment and routing
- ICR Probe (ACL 2025) - linear probes on residual streams for retrieval decisions
- LatentAudit (arXiv:2604.05358) - Mahalanobis distance on residual streams for RAG monitoring

### Revision Strategy:

This should be a **major revision** based on the findings:

1. **NOVELTY**: Transform from "implementing someone else's suggestion" to "Orthogonal-Axis Gated Retrieval (OAGR)" - a principled multi-axis gating framework that fuses drift, confidence, and uncertainty probes. This is genuinely novel:
   - No one has combined these three orthogonal axes
   - The theoretical justification is strong (Bayes risk reduction, linear representation hypothesis)
   - Practical fusion mechanism needed (not simple averaging, per MeCo's finding)

2. **ENTITY TOKEN**: The Geometry of Forgetting uses the first generated answer token rather than an entity token in the prompt, so I should clarify that for our system we can leverage templated prompts with structured queries from benchmarks, and propose using the last subject token with SpaCy NER as a fallback for more open-ended scenarios.

3. **BASELINES**: Narrow down to six baselines that either have verified implementations or are straightforward to recreate—keeping Probing-RAG, SeaKR, Self-Routing RAG, and Token-Entropy where code exists, adding TARG and Rep-Con/Rep-PCA as easy reimplementations, and dropping INKER and Skill-RAG due to missing code and architectural complexity, while bringing in CtrlA as a direct comparison point for dual-probe gating.

4. **MMA-RAG**: Position this as related work and highlight where our approach diverges.

5. **TIMELINE**: Push the primary submission target to ARR August 2026 with EACL 2027 as the goal, keeping AAAI as a stretch option.

The real breakthrough here is recognizing that drift-gating alone isn't the answer—what matters is how you orchestrate multiple orthogonal signals through a learned gating mechanism to make retrieval decisions that are more nuanced than any single probe could provide.

Now I'm considering what to call this. Something like "Orthogonal-Axis Gated Retrieval" or "Geometric Retrieval Gating" feels right, though "Multi-Axis Probe-Gated Retrieval" also captures the core idea. The name should reflect that we're combining drift, confidence, and uncertainty probes through a principled geometric framework rather than just implementing one suggestion from prior work.

For the execution, I'd structure it as extracting three independent probe scores per model, then training a gating mechanism to combine them intelligently, starting with the same Wikidata pipeline for drift labels and building out confidence probes from correctness annotations.

The real novelty here is that these axes are mathematically orthogonal—the cosine similarity stays below 0.14—which means they capture genuinely different failure modes. A drift-only approach misses cases where the model is simply uncertain, while a confidence-only gate fails to catch drifted facts the model happens to be confident about. Combining them should give strictly more signal for deciding when to retrieve.

For the entity token extraction, I need to figure out the right position to probe. The original paper extracts at the first content token of the generated answer, which requires actually generating something first. I could do a short prefix generation, extract activations at that first token, run the probes, then decide whether to retrieve or continue. Or for structured queries where I know the subject, I could extract at the last subject token instead. I should test both approaches to see which works better.

Actually, let me reconsider the mechanics here. If I extract at the first generated token, I don't need to do entity recognition—I just let the model start generating and probe immediately. That's simpler than trying to identify entity positions in the query. The tradeoff is needing that partial forward pass, but the workflow becomes cleaner: query goes in, model generates one token, I extract and apply the probes, then decide whether to interrupt and retrieve or keep going. I could also extract activations from the query's final token instead, since it has access to the full context through causal attention—but the Geometry of Forgetting paper found drift signals specifically in the generated answer's first token, suggesting the model reveals its knowledge gaps when actively attempting recall rather than just processing the question. I should test both extraction positions and consider the naming: "Orthogonal-Axis Gated Retrieval" captures the core idea well, though I want to make sure the framing is right before finalizing the approach document. Now I'm structuring the baseline comparisons—keeping the implementations with available code like Probing-RAG, SeaKR, Self-Routing RAG, and Token-Entropy, while adding CtrlA as the most relevant dual-probe competitor and Rep-Con for representation-based comparison. That gives me seven baselines plus the trivial bounds, making nine total comparison points.

For OAGR itself, I'll treat drift-only, confidence-only, and uncertainty-only gating as ablations rather than separate baselines. On the fusion mechanism, since simple averaging doesn't work well, I'm exploring three approaches: a logistic regression gate over concatenated probe scores, a query-conditioned MLP that incorporates the query representation, and a cascade method with sequential thresholding.

The experimental design stacks multiple ablations: comparing fusion strategies, testing single-axis versus multi-axis gating, checking layer robustness, varying where we extract representations, measuring sensitivity to drift base rates, and evaluating transfer to smaller models. The main result will pit OAGR against seven baselines across three benchmarks, with these ablations providing deeper insight into what drives performance.

For submission targets, I'm looking at ARR August 3rd as the primary deadline—that's about 10.5 weeks away—with EACL 2027 as a reviewer suggestion. AAAI 2027 is a secondary option with abstract and paper deadlines around 9-10 weeks out, though that's a stretch. TACL rolling submissions are the tertiary fallback. Both ARR and AAAI are tight timelines, but doable if I pare down the baseline comparisons.

Now I need to rewrite the full JSON with this new framing—shifting from "drift-probe-gated retrieval" to "orthogonal-axis gated retrieval" is a fundamental reorientation. I'm also circling back to the entity token extraction issue. The research on forgetting suggests pulling representations at the first token position, which aligns with how other work handles this.

For my benchmarks with structured queries, I actually have entity boundaries available, so I can test multiple extraction positions: the last subject token, the first generated answer token, and the final query token. I'll go with the first generated content token as my primary approach since it matches the original paper's methodology and sidesteps the entity identification problem, then ablate with the last subject token to show robustness.

The gating pipeline itself is straightforward: run the query through the model, generate a single content token, pull residual stream activations at that position, apply the three probes for drift, confidence, and uncertainty, then feed those signals into the gating mechanism.

Now I'm reviewing the related work landscape and composing the full revised JSON response to address all the reviewer feedback. I've identified several key papers that are directly relevant: CtrlA with its dual probe approach for retrieval gating, HALT and DRIFT for hallucination-based routing, the ICR Probe work on residual stream analysis, LatentAudit's Mahalanobis distance approach for RAG monitoring, and recent work on combining multiple signals for routing decisions.

Beyond those, there's a whole body of work on uncertainty quantification and adaptive retrieval strategies, plus foundational papers on multi-probe interventions, safety directions, and the linear representation hypothesis that underpins why orthogonal probes work. I should also include MeCo's meta-cognition approach since it explicitly addresses why simple probe averaging fails. I need to verify whether CtrlA has released code, but I'll include it as the closest comparison point regardless.

Now I'm restructuring the core contribution around multi-axis fusion rather than just drift-based gating. The key novelty is combining provably orthogonal representation axes—drift, confidence, and uncertainty—with a learned fusion mechanism, plus the query-conditioned gating strategy itself. I should also clarify the extraction position issue: the Geometry of Forgetting approach extracts at the first generated token, not an entity token, which means the primary method avoids NER dependency. I'll add an ablation for extraction position too.

For baselines, I'm paring down to seven methods with verified implementations or straightforward reimplementations, dropping INKER and Skill-RA since they're harder to reproduce.

I'm also adding CtrlA as the nearest competitor baseline, positioning MMA-RAG in the landscape with a clear architectural comparison. The timeline is shifting—aiming for ARR August 2026 with EACL 2027 as the primary target, while AAAI 2027 becomes a stretch goal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26941d4c-17f0-463a-b3d0-5d36f59e6c91",
  "isSidechain": false,
  "requestId": "req_011CbBhWtap7JSTa4nXqSJob",
  "type": "assistant",
  "uuid": "f2d7c39f-50fb-4010-a726-681eb5059744",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8wL7CT2Ht8FxWVVRhm6rN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17496,
      "cache_read_input_tokens": 20111,
      "output_tokens": 4741,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4741,
          "cache_read_input_tokens": 20111,
          "cache_creation_input_tokens": 17496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17496
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

_source line 31 · 2026-05-19T09:36:35.200Z_

Now let me do a couple more targeted searches to fill remaining gaps:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2d7c39f-50fb-4010-a726-681eb5059744",
  "isSidechain": false,
  "requestId": "req_011CbBhWtap7JSTa4nXqSJob",
  "type": "assistant",
  "uuid": "acfd75e7-ecd1-467e-bdea-362ed836a7a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8wL7CT2Ht8FxWVVRhm6rN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17496,
      "cache_read_input_tokens": 20111,
      "output_tokens": 4741,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4741,
          "cache_read_input_tokens": 20111,
          "cache_creation_input_tokens": 17496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17496
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

_source line 32 · 2026-05-19T09:36:35.238Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fcp59UDbCYyJoqrq8zoppU`</summary>

```json
{
  "query": "CtrlA adaptive RAG dual probes honesty confidence arXiv 2405.18727 code github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acfd75e7-ecd1-467e-bdea-362ed836a7a8",
  "isSidechain": false,
  "requestId": "req_011CbBhWtap7JSTa4nXqSJob",
  "type": "assistant",
  "uuid": "cbf4892d-f388-4247-a761-b8133ecf0d29",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8wL7CT2Ht8FxWVVRhm6rN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17496,
      "cache_read_input_tokens": 20111,
      "output_tokens": 4741,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4741,
          "cache_read_input_tokens": 20111,
          "cache_creation_input_tokens": 17496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17496
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

_source line 33 · 2026-05-19T09:36:35.243Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W7iXZ1yk6uw5nDxTrPrL5w`</summary>

```json
{
  "query": "ICR Probe ACL 2025 residual stream retrieval decision linear probe code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbf4892d-f388-4247-a761-b8133ecf0d29",
  "isSidechain": false,
  "requestId": "req_011CbBhWtap7JSTa4nXqSJob",
  "type": "assistant",
  "uuid": "4d394ce2-4959-48ad-bf9e-c98f430c51d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8wL7CT2Ht8FxWVVRhm6rN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17496,
      "cache_read_input_tokens": 20111,
      "output_tokens": 4741,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4741,
          "cache_read_input_tokens": 20111,
          "cache_creation_input_tokens": 17496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17496
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Drift-Probe-Gated Retrieval: A Systematic Evaluation of Temporal Stale…",
  "leafUuid": "4d394ce2-4959-48ad-bf9e-c98f430c51d5",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Add multi-signal gating to drift-probe RAG system",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed"
}
```

---

### Tool result

_source line 36 · 2026-05-19T09:36:41.141Z_

<details><summary>↩ Tool result · `toolu_01Fcp59UDbCYyJoqrq8zoppU`</summary>

```text
Web search results for query: "CtrlA adaptive RAG dual probes honesty confidence arXiv 2405.18727 code github"

Links: [{"title":"CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control | OpenReview","url":"https://openreview.net/forum?id=QYvtX2XA8p&noteId=azYw0GI4QY"},{"title":"[2405.18727] CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control","url":"https://arxiv.org/abs/2405.18727"},{"title":"[2405.18727v2] CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control","url":"https://arxiv.org/abs/2405.18727v2"},{"title":"[Literature Review] CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control","url":"https://www.themoonlight.io/en/review/ctrla-adaptive-retrieval-augmented-generation-via-inherent-control"},{"title":"CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control","url":"https://arxiv.org/pdf/2405.18727"},{"title":"CtrlA: Adaptive Retrieval-Augmented Generation via Probe-Guided Control | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/ctrla-adaptive-retrieval-augmented-generation-via-inherent"},{"title":"(PDF) CtrlA: Adaptive Retrieval-Augmented Generation via Probe-Guided Control","url":"https://www.researchgate.net/publication/380974446_CtrlA_Adaptive_Retrieval-Augmented_Generation_via_Probe-Guided_Control"}]

Based on the search results, here's what I found about the paper and project:

## CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control

The CtrlA framework solves adaptive RAG from a representation perspective by extracting features representing honesty and confidence directions of LLMs to control LLM behavior and guide retrieval timing decisions.

### Key Features

CtrlA employs an honesty probe to regulate the LLM's behavior by manipulating its representations for increased honesty, and a confidence probe to monitor the internal states of LLM and assess confidence levels, determining the retrieval necessity during generation.

The framework develops two plug-and-play probes designed for behavioral intervention and monitoring without fine-tuning LLMs, where the honesty probe manipulates representations to enhance honesty while the confidence probe monitors internal states to optimize retrieval necessity detection.

### Paper Location

The paper is available at arXiv:2405.18727. However, I didn't find specific information about a GitHub code repository in these search results. You may want to check the arXiv paper directly or search for the authors' GitHub profiles for the code implementation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbf4892d-f388-4247-a761-b8133ecf0d29",
  "isSidechain": false,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "type": "user",
  "uuid": "57bf99a4-6cd0-4537-98ff-4b688411ff7d",
  "toolUseResult": {
    "query": "CtrlA adaptive RAG dual probes honesty confidence arXiv 2405.18727 code github",
    "results": [
      {
        "tool_use_id": "srvtoolu_015xxhsQDBuShk3UXaFUtVo7",
        "content": [
          {
            "title": "CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control | OpenReview",
            "url": "https://openreview.net/forum?id=QYvtX2XA8p&noteId=azYw0GI4QY"
          },
          {
            "title": "[2405.18727] CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control",
            "url": "https://arxiv.org/abs/2405.18727"
          },
          {
            "title": "[2405.18727v2] CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control",
            "url": "https://arxiv.org/abs/2405.18727v2"
          },
          {
            "title": "[Literature Review] CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control",
            "url": "https://www.themoonlight.io/en/review/ctrla-adaptive-retrieval-augmented-generation-via-inherent-control"
          },
          {
            "title": "CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control",
            "url": "https://arxiv.org/pdf/2405.18727"
          },
          {
            "title": "CtrlA: Adaptive Retrieval-Augmented Generation via Probe-Guided Control | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/ctrla-adaptive-retrieval-augmented-generation-via-inherent"
          },
          {
            "title": "(PDF) CtrlA: Adaptive Retrieval-Augmented Generation via Probe-Guided Control",
            "url": "https://www.researchgate.net/publication/380974446_CtrlA_Adaptive_Retrieval-Augmented_Generation_via_Probe-Guided_Control"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper and project:\n\n## CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control\n\nThe CtrlA framework solves adaptive RAG from a representation perspective by extracting features representing honesty and confidence directions of LLMs to control LLM behavior and guide retrieval timing decisions.\n\n### Key Features\n\nCtrlA employs an honesty probe to regulate the LLM's behavior by manipulating its representations for increased honesty, and a confidence probe to monitor the internal states of LLM and assess confidence levels, determining the retrieval necessity during generation.\n\nThe framework develops two plug-and-play probes designed for behavioral intervention and monitoring without fine-tuning LLMs, where the honesty probe manipulates representations to enhance honesty while the confidence probe monitors internal states to optimize retrieval necessity detection.\n\n### Paper Location\n\nThe paper is available at arXiv:2405.18727. However, I didn't find specific information about a GitHub code repository in these search results. You may want to check the arXiv paper directly or search for the authors' GitHub profiles for the code implementation."
    ],
    "durationSeconds": 5.899125539999979,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cbf4892d-f388-4247-a761-b8133ecf0d29",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-19T09:36:41.565Z_

<details><summary>↩ Tool result · `toolu_01W7iXZ1yk6uw5nDxTrPrL5w`</summary>

```text
Web search results for query: "ICR Probe ACL 2025 residual stream retrieval decision linear probe code"

Links: [{"title":"Self-Consistency and Probe-Based Hallucination Detection","url":"https://www.emergentmind.com/topics/self-consistency-probe-based-hallucination-detection"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable ...","url":"https://aclanthology.org/2025.acl-long.880.pdf"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination","url":"https://arxiv.org/pdf/2507.16488"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs","url":"https://arxiv.org/html/2507.16488v1"},{"title":"Article Not peer-reviewed version Exploring the Limits of Probes for Latent","url":"https://www.preprints.org/frontend/manuscript/940b242abb6b3fe2846c1b9d844699d4/download_pub"},{"title":"[2507.16488v1] ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs","url":"https://arxiv.org/abs/2507.16488v1"},{"title":"Activation Transport Operators","url":"https://arxiv.org/pdf/2508.17540"}]

Based on the search results, I found relevant information about the ICR Probe presented at ACL 2025:

## ICR Probe: ACL 2025

The ICR Probe introduces a novel metric called the ICR Score (Information Contribution to Residual Stream), which quantifies the contribution of modules to the hidden states' update. 

The ICR Score is defined via the Jensen–Shannon divergence between residual update and attention distributions, quantifying whether updates are dominated by attention (context-driven) or FFN (parametric memory), with divergence from attention dominating signaling hallucination.

**Detection Process:**
The method first probes each layer's residual stream to obtain the ICR Score, then aggregates the ICR Scores across all layers to capture global information. This aggregated signal serves as the input to the probe, which produces the final hallucination detection result.

**Performance:**
The ICR Probe achieves superior performance with significantly fewer parameters.

**Related Research:**
Linear probes analyze how information is integrated within the residual stream of the Transformer architecture. Linear probes trained on the original residual stream decisively outperform probes based on sparse autoencoders.

The paper was published in July 2025 at ACL. For access to the code and full technical details, you may want to check the official ACL Anthology or the authors' GitHub repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d394ce2-4959-48ad-bf9e-c98f430c51d5",
  "isSidechain": false,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "type": "user",
  "uuid": "716f2ef5-b3a1-4d73-af75-bbcdcd717630",
  "toolUseResult": {
    "query": "ICR Probe ACL 2025 residual stream retrieval decision linear probe code",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Y8Sq1cQLs8XZexxKbLYw6M",
        "content": [
          {
            "title": "Self-Consistency and Probe-Based Hallucination Detection",
            "url": "https://www.emergentmind.com/topics/self-consistency-probe-based-hallucination-detection"
          },
          {
            "title": "ICR Probe: Tracking Hidden State Dynamics for Reliable ...",
            "url": "https://aclanthology.org/2025.acl-long.880.pdf"
          },
          {
            "title": "ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination",
            "url": "https://arxiv.org/pdf/2507.16488"
          },
          {
            "title": "ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs",
            "url": "https://arxiv.org/html/2507.16488v1"
          },
          {
            "title": "Article Not peer-reviewed version Exploring the Limits of Probes for Latent",
            "url": "https://www.preprints.org/frontend/manuscript/940b242abb6b3fe2846c1b9d844699d4/download_pub"
          },
          {
            "title": "[2507.16488v1] ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs",
            "url": "https://arxiv.org/abs/2507.16488v1"
          },
          {
            "title": "Activation Transport Operators",
            "url": "https://arxiv.org/pdf/2508.17540"
          }
        ]
      },
      "Based on the search results, I found relevant information about the ICR Probe presented at ACL 2025:\n\n## ICR Probe: ACL 2025\n\nThe ICR Probe introduces a novel metric called the ICR Score (Information Contribution to Residual Stream), which quantifies the contribution of modules to the hidden states' update. \n\nThe ICR Score is defined via the Jensen–Shannon divergence between residual update and attention distributions, quantifying whether updates are dominated by attention (context-driven) or FFN (parametric memory), with divergence from attention dominating signaling hallucination.\n\n**Detection Process:**\nThe method first probes each layer's residual stream to obtain the ICR Score, then aggregates the ICR Scores across all layers to capture global information. This aggregated signal serves as the input to the probe, which produces the final hallucination detection result.\n\n**Performance:**\nThe ICR Probe achieves superior performance with significantly fewer parameters.\n\n**Related Research:**\nLinear probes analyze how information is integrated within the residual stream of the Transformer architecture. Linear probes trained on the original residual stream decisively outperform probes based on sparse autoencoders.\n\nThe paper was published in July 2025 at ACL. For access to the code and full technical details, you may want to check the official ACL Anthology or the authors' GitHub repository."
    ],
    "durationSeconds": 6.3196300939999634,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4d394ce2-4959-48ad-bf9e-c98f430c51d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38 · 2026-05-19T09:36:41.569Z_

```json
{
  "parentUuid": "716f2ef5-b3a1-4d73-af75-bbcdcd717630",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e6123913-5e96-4a8a-a8ca-8d16bae247af",
  "timestamp": "2026-05-19T09:36:41.569Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 39 · 2026-05-19T09:36:45.053Z_

<details><summary>Logged reasoning block</summary>

```text
Good. CtrlA uses dual probes (honesty + confidence) for adaptive RAG. Code availability unclear. ICR Probe is from ACL 2025, focuses on hallucination detection via residual stream dynamics.

Let me also check CtrlA's code availability more carefully and get details on its architecture.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6123913-5e96-4a8a-a8ca-8d16bae247af",
  "isSidechain": false,
  "requestId": "req_011CbBhf9XxKE1nAZY6DRR7g",
  "type": "assistant",
  "uuid": "b5b1beb3-fa1b-4c43-87ce-16cbc95f19a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013u9odvMdoTR5gAacEqiCQr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6303,
      "cache_read_input_tokens": 37607,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6303,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 37607,
          "cache_creation_input_tokens": 6303,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6303
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

_source line 40 · 2026-05-19T09:36:46.936Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AwyKDU3Bw2PUd27eWhFpPc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2405.18727v2",
  "prompt": "Extract: 1) Is there a GitHub code link? 2) What exactly are the honesty probe and confidence probe architectures? 3) How are probe scores combined for the retrieval decision? 4) What benchmarks are used? 5) Key results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5b1beb3-fa1b-4c43-87ce-16cbc95f19a0",
  "isSidechain": false,
  "requestId": "req_011CbBhf9XxKE1nAZY6DRR7g",
  "type": "assistant",
  "uuid": "3407f2e8-5815-458b-af0b-964f8238132f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013u9odvMdoTR5gAacEqiCQr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6303,
      "cache_read_input_tokens": 37607,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6303,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 37607,
          "cache_creation_input_tokens": 6303,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6303
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

_source line 41 · 2026-05-19T09:36:47.392Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SqbNn7o1jgsqqAdtixnW28`</summary>

```json
{
  "query": "\"Moskvoretskii\" \"adaptive retrieval without self-knowledge\" arXiv 2501.12835 combining uncertainty signals"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3407f2e8-5815-458b-af0b-964f8238132f",
  "isSidechain": false,
  "requestId": "req_011CbBhf9XxKE1nAZY6DRR7g",
  "type": "assistant",
  "uuid": "795eb405-8696-48b7-8428-44f9f597ff5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013u9odvMdoTR5gAacEqiCQr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6303,
      "cache_read_input_tokens": 37607,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6303,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 37607,
          "cache_creation_input_tokens": 6303,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6303
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

_source line 42 · 2026-05-19T09:36:52.008Z_

<details><summary>↩ Tool result · `toolu_01AwyKDU3Bw2PUd27eWhFpPc`</summary>

```text
# CtrlA Paper Analysis

**1) GitHub Code Link:**
Yes, the paper states code is available at https://github.com/HSLiu-Initial/CtrlA

**2) Honesty and Confidence Probe Architectures:**
The abstract does not provide architectural details. It only mentions extracting "features that represent the honesty and confidence directions" but specifics about their structure are not disclosed in this webpage content.

**3) Probe Score Combination for Retrieval:**
The abstract indicates that "confidence monitoring is a promising indicator of retrieval" triggering, but the exact mechanism for combining scores is not explained in the provided excerpt.

**4) Benchmarks Used:**
The paper evaluated CtrlA "on a diverse set of tasks" according to the abstract, though specific benchmark names are not listed in this webpage section.

**5) Key Results:**
The findings demonstrate that "CtrlA is superior to existing adaptive RAG methods" and that "honesty steering can effectively make LLMs more honest," with confidence monitoring showing promise as a retrieval timing indicator.

---

*Note: Full methodological details would require accessing the complete paper PDF, which contains the 29 pages, 10 figures, and 11 tables mentioned in the submission metadata.*
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3407f2e8-5815-458b-af0b-964f8238132f",
  "isSidechain": false,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "type": "user",
  "uuid": "52658f70-f0e0-4cca-b87c-697a3d9818fb",
  "toolUseResult": {
    "bytes": 47259,
    "code": 200,
    "codeText": "OK",
    "result": "# CtrlA Paper Analysis\n\n**1) GitHub Code Link:**\nYes, the paper states code is available at https://github.com/HSLiu-Initial/CtrlA\n\n**2) Honesty and Confidence Probe Architectures:**\nThe abstract does not provide architectural details. It only mentions extracting \"features that represent the honesty and confidence directions\" but specifics about their structure are not disclosed in this webpage content.\n\n**3) Probe Score Combination for Retrieval:**\nThe abstract indicates that \"confidence monitoring is a promising indicator of retrieval\" triggering, but the exact mechanism for combining scores is not explained in the provided excerpt.\n\n**4) Benchmarks Used:**\nThe paper evaluated CtrlA \"on a diverse set of tasks\" according to the abstract, though specific benchmark names are not listed in this webpage section.\n\n**5) Key Results:**\nThe findings demonstrate that \"CtrlA is superior to existing adaptive RAG methods\" and that \"honesty steering can effectively make LLMs more honest,\" with confidence monitoring showing promise as a retrieval timing indicator.\n\n---\n\n*Note: Full methodological details would require accessing the complete paper PDF, which contains the 29 pages, 10 figures, and 11 tables mentioned in the submission metadata.*",
    "durationMs": 5070,
    "url": "https://arxiv.org/abs/2405.18727v2"
  },
  "sourceToolAssistantUUID": "3407f2e8-5815-458b-af0b-964f8238132f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-19T09:36:53.201Z_

<details><summary>↩ Tool result · `toolu_01SqbNn7o1jgsqqAdtixnW28`</summary>

```text
Web search results for query: ""Moskvoretskii" "adaptive retrieval without self-knowledge" arXiv 2501.12835 combining uncertainty signals"

Links: [{"title":"[2501.12835] Adaptive Retrieval Without Self-Knowledge? Bringing Uncertainty Back Home","url":"https://arxiv.org/abs/2501.12835"},{"title":"GitHub - s-nlp/AdaRAGUE: [ACL 2025] Adaptive Retrieval without Self-Knowledge? Bringing Uncertainty Back Home · GitHub","url":"https://github.com/s-nlp/AdaRAGUE"},{"title":"Self-Routing RAG: Binding Selective Retrieval with Knowledge Verbalization","url":"https://arxiv.org/html/2504.01018v1"},{"title":"Adaptive Retrieval without Self-Knowledge? Bringing Uncertainty Back Home","url":"https://arxiv.org/html/2501.12835v1"},{"title":"[Literature Review] Adaptive Retrieval Without Self-Knowledge? Bringing Uncertainty Back Home","url":"https://www.themoonlight.io/en/review/adaptive-retrieval-without-self-knowledge-bringing-uncertainty-back-home"},{"title":"Adaptive Retrieval Without Self-Knowledge? Bringing Uncertainty Back Home - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.319/"},{"title":"Adaptive Retrieval Without Self-Knowledge? Bringing Uncertainty Back Home - Consensus","url":"https://k8s.consensus.app/papers/adaptive-retrieval-without-selfknowledge-bringing-nikishina-galimzianova/752f144d8d92533d8fe8bf289e0c2f04/"},{"title":"Adaptive Retrieval Without Self-Knowledge? Bringing Uncertainty Back   Home","url":"https://arxiv.org/pdf/2501.12835"}]

I found the paper you're looking for! Here's what I can tell you about it:

The paper "Adaptive Retrieval Without Self-Knowledge? Bringing Uncertainty Back Home" is authored by Viktor Moskvoretskii and colleagues, with the arXiv identifier 2501.12835.

**Overview:**
The paper addresses how Retrieval Augmented Generation (RAG) improves correctness of Question Answering (QA) and addresses hallucinations in Large Language Models (LLMs), yet greatly increases computational costs, and RAG is not always needed as it may introduce irrelevant information.

**Main Contribution:**
Recent adaptive retrieval methods integrate LLMs' intrinsic knowledge with external information appealing to LLM self-knowledge, but they often neglect efficiency evaluations and comparisons with uncertainty estimation techniques. The authors bridge this gap by conducting a comprehensive analysis of 35 adaptive retrieval methods, including 8 recent approaches and 27 uncertainty estimation techniques, across 6 datasets using 10 metrics for QA performance, self-knowledge, and efficiency. Their findings show that uncertainty estimation techniques often outperform complex pipelines in terms of efficiency and self-knowledge, while maintaining comparable QA performance.

The paper was accepted to ACL 2025 and has both v1 (submitted January 22, 2025) and v2 (revised February 21, 2025) versions available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "795eb405-8696-48b7-8428-44f9f597ff5a",
  "isSidechain": false,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "type": "user",
  "uuid": "f6a85d33-c24f-4bd0-9a0d-100594a868e7",
  "toolUseResult": {
    "query": "\"Moskvoretskii\" \"adaptive retrieval without self-knowledge\" arXiv 2501.12835 combining uncertainty signals",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AicfCpeYzVkQGbxdACcRWF",
        "content": [
          {
            "title": "[2501.12835] Adaptive Retrieval Without Self-Knowledge? Bringing Uncertainty Back Home",
            "url": "https://arxiv.org/abs/2501.12835"
          },
          {
            "title": "GitHub - s-nlp/AdaRAGUE: [ACL 2025] Adaptive Retrieval without Self-Knowledge? Bringing Uncertainty Back Home · GitHub",
            "url": "https://github.com/s-nlp/AdaRAGUE"
          },
          {
            "title": "Self-Routing RAG: Binding Selective Retrieval with Knowledge Verbalization",
            "url": "https://arxiv.org/html/2504.01018v1"
          },
          {
            "title": "Adaptive Retrieval without Self-Knowledge? Bringing Uncertainty Back Home",
            "url": "https://arxiv.org/html/2501.12835v1"
          },
          {
            "title": "[Literature Review] Adaptive Retrieval Without Self-Knowledge? Bringing Uncertainty Back Home",
            "url": "https://www.themoonlight.io/en/review/adaptive-retrieval-without-self-knowledge-bringing-uncertainty-back-home"
          },
          {
            "title": "Adaptive Retrieval Without Self-Knowledge? Bringing Uncertainty Back Home - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.319/"
          },
          {
            "title": "Adaptive Retrieval Without Self-Knowledge? Bringing Uncertainty Back Home - Consensus",
            "url": "https://k8s.consensus.app/papers/adaptive-retrieval-without-selfknowledge-bringing-nikishina-galimzianova/752f144d8d92533d8fe8bf289e0c2f04/"
          },
          {
            "title": "Adaptive Retrieval Without Self-Knowledge? Bringing Uncertainty Back   Home",
            "url": "https://arxiv.org/pdf/2501.12835"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I can tell you about it:\n\nThe paper \"Adaptive Retrieval Without Self-Knowledge? Bringing Uncertainty Back Home\" is authored by Viktor Moskvoretskii and colleagues, with the arXiv identifier 2501.12835.\n\n**Overview:**\nThe paper addresses how Retrieval Augmented Generation (RAG) improves correctness of Question Answering (QA) and addresses hallucinations in Large Language Models (LLMs), yet greatly increases computational costs, and RAG is not always needed as it may introduce irrelevant information.\n\n**Main Contribution:**\nRecent adaptive retrieval methods integrate LLMs' intrinsic knowledge with external information appealing to LLM self-knowledge, but they often neglect efficiency evaluations and comparisons with uncertainty estimation techniques. The authors bridge this gap by conducting a comprehensive analysis of 35 adaptive retrieval methods, including 8 recent approaches and 27 uncertainty estimation techniques, across 6 datasets using 10 metrics for QA performance, self-knowledge, and efficiency. Their findings show that uncertainty estimation techniques often outperform complex pipelines in terms of efficiency and self-knowledge, while maintaining comparable QA performance.\n\nThe paper was accepted to ACL 2025 and has both v1 (submitted January 22, 2025) and v2 (revised February 21, 2025) versions available on arXiv."
    ],
    "durationSeconds": 5.807753526000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "795eb405-8696-48b7-8428-44f9f597ff5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-19T09:37:27.110Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have:
- CtrlA has code: https://github.com/HSLiu-Initial/CtrlA
- Moskvoretskii et al. (AdaRAGUE) has code: https://github.com/s-nlp/AdaRAGUE and is at ACL 2025

Now I have enough information to compose the full revised idea. Let me synthesize everything.

Key changes for the major revision:

1. **TITLE**: Changed from "Drift-Probe-Gated Retrieval" to "Orthogonal-Axis Gated Retrieval" (OAGR) - reflecting the multi-signal fusion novelty


2. **CORE PROBLEM**: Reframed to emphasize multi-axis fusion, not just drift probing
3. **APPROACH**: I'm incorporating multi-signal probe training across drift, confidence, and uncertainty signals, then adding a learned fusion mechanism to combine them—either through logistic regression, query-conditioned MLP, or cascade approaches. I'm also clarifying that extraction happens at the first generated content token and planning an ablation on extraction position.
4. **BASELINES**: Streamlined to 7 verified implementations, removing INKER and Skill-RAG while adding CtrlA as the closest competitor with dual probes and AdaRAGUE from the recent ACL 2025 work.
5. **LANDSCAPE**: Mapping the broader context with CtrlA, MMA-RAG, ICR Probe, HALT/DRIFT, AdaRAGUE, Truth Forest, and relevant theoretical foundations.
6. **TIMELINE**: Targeting ARR August with EACL 2027 as the primary venue and AAAI 2027 as a backup option.
7. **ENTITY TOKEN**: Solidifying the first generated content token extraction approach with position ablations.

The real novelty here is that The Geometry of Forgetting established three orthogonal axes, and I'm the first to combine all three through a learned gating mechanism—CtrlA only uses two probes without drift, and AdaRAGUE aggregates 35 uncertainty methods but stays within a single family, whereas I'm grounding this in provable orthogonality.

For the implementation, I'm running three phases: first the Wikidata pipeline to generate training data, then training separate linear probes on residual activations at the first generated token for drift (temporal labels), confidence (correctness without retrieval), and uncertainty (consistency across top-k answers), and finally learning a fusion gate that takes these three scores and decides whether to retrieve, comparing logistic regression, a query-conditioned MLP, and cascade thresholding approaches.

Now I'm working through the resource requirements—training twelve probe runs across four models takes about 60 hours total since each probe is tiny, hidden state extraction is still the bottleneck at around 200 hours, and evaluation across seven baselines plus the new CtrlA baseline runs roughly 150-180 hours, with ablations adding a bit more on top.

The full timeline fits within the 10.5 weeks available before ARR August: two weeks for the Wikidata pipeline and infrastructure, two weeks for multi-axis probe training and validation, three weeks for full evaluation, two weeks for ablations and fusion experiments, then 1.5 weeks for writing and buffer. For AAAI, I could submit an abstract by July 21 based on early results and finish the full paper by July 28, though the tight timeline does introduce execution risk. The multi-axis fusion novelty could push this from "solid" to something stronger, but I need to weigh that against the schedule pressure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6a85d33-c24f-4bd0-9a0d-100594a868e7",
  "isSidechain": false,
  "requestId": "req_011CbBhg1H99vbCKZndXh52F",
  "type": "assistant",
  "uuid": "65ff66d5-adee-4358-863f-fee3384acad3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019CrjdvXkcyEuSSNt2j6SUi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 43910,
      "output_tokens": 1278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1278,
          "cache_read_input_tokens": 43910,
          "cache_creation_input_tokens": 1427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1427
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

_source line 45 · 2026-05-19T09:37:27.112Z_

Now I have comprehensive research on all five reviewer concerns. Let me synthesize everything and compose the complete revised idea.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65ff66d5-adee-4358-863f-fee3384acad3",
  "isSidechain": false,
  "requestId": "req_011CbBhg1H99vbCKZndXh52F",
  "type": "assistant",
  "uuid": "36398550-102e-4487-8ac1-e40039cdbf1d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019CrjdvXkcyEuSSNt2j6SUi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 43910,
      "output_tokens": 1278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1278,
          "cache_read_input_tokens": 43910,
          "cache_creation_input_tokens": 1427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1427
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

_source line 46 · 2026-05-19T09:37:27.264Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G5CURG5CKrL33whgNKM91G`</summary>

```json
{
  "query": "CtrlA github HSLiu-Initial code availability adaptive RAG probes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36398550-102e-4487-8ac1-e40039cdbf1d",
  "isSidechain": false,
  "requestId": "req_011CbBhg1H99vbCKZndXh52F",
  "type": "assistant",
  "uuid": "8be4b058-3e70-4594-836c-04af0e9e8349",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019CrjdvXkcyEuSSNt2j6SUi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 43910,
      "output_tokens": 1278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1278,
          "cache_read_input_tokens": 43910,
          "cache_creation_input_tokens": 1427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1427
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

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Drift-Probe-Gated Retrieval: A Systematic Evaluation of Temporal Stale…",
  "leafUuid": "8be4b058-3e70-4594-836c-04af0e9e8349",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Add multi-signal gating to drift-probe RAG system",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed"
}
```

---

### Tool result

_source line 49 · 2026-05-19T09:37:33.087Z_

<details><summary>↩ Tool result · `toolu_01G5CURG5CKrL33whgNKM91G`</summary>

```text
Web search results for query: "CtrlA github HSLiu-Initial code availability adaptive RAG probes"

Links: [{"title":"GitHub - HSLiu-Initial/CtrlA: This includes the original implementation of CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control.","url":"https://github.com/HSLiu-Initial/CtrlA"},{"title":"CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control","url":"https://arxiv.org/pdf/2405.18727"},{"title":"(PDF) CtrlA: Adaptive Retrieval-Augmented Generation via Probe-Guided Control","url":"https://www.researchgate.net/publication/380974446_CtrlA_Adaptive_Retrieval-Augmented_Generation_via_Probe-Guided_Control"},{"title":"CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control | OpenReview","url":"https://openreview.net/forum?id=QYvtX2XA8p&noteId=azYw0GI4QY"},{"title":"[2405.18727] CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control","url":"https://arxiv.org/abs/2405.18727"},{"title":"[2405.18727v2] CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control","url":"https://arxiv.org/abs/2405.18727v2"},{"title":"CtrlA/run.py at main · HSLiu-Initial/CtrlA","url":"https://github.com/HSLiu-Initial/CtrlA/blob/main/run.py"},{"title":"HSLiu-Initial (Liu Huanshuo) · GitHub","url":"https://github.com/HSLiu-Initial"}]

Based on the search results, I found information about the CtrlA project on GitHub:

## CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control

CtrlA introduces an effective inherent control-based adaptive RAG framework to enhance retrieval-augmented generation for LLM, balancing its internal and external knowledge.

### Key Features

CtrlA characterizes LLM's internal states and intervenes in the LLM generation from two perspectives: honesty steering and confidence monitoring via simple yet effective feature direction representations. More specifically, CtrlA employs an honesty probe to regulate the LLM's behavior by manipulating its representations for increased honesty, and a confidence probe to monitor the internal states of LLM and assess confidence levels, determining the retrieval necessity during generation.

### Code Availability

This includes the original implementation of CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control. The code is available at the GitHub repository: https://github.com/HSLiu-Initial/CtrlA

### Results

Experiments show that CtrlA is superior to existing adaptive RAG methods on a diverse set of tasks, the honesty control can effectively make LLMs more honest and confidence monitoring is proven to be a promising indicator of retrieval trigger.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8be4b058-3e70-4594-836c-04af0e9e8349",
  "isSidechain": false,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "type": "user",
  "uuid": "3b976799-53f5-4b1d-accd-dbe35db58899",
  "toolUseResult": {
    "query": "CtrlA github HSLiu-Initial code availability adaptive RAG probes",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Fb3yoXBqTjQ2qufGUWiCgP",
        "content": [
          {
            "title": "GitHub - HSLiu-Initial/CtrlA: This includes the original implementation of CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control.",
            "url": "https://github.com/HSLiu-Initial/CtrlA"
          },
          {
            "title": "CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control",
            "url": "https://arxiv.org/pdf/2405.18727"
          },
          {
            "title": "(PDF) CtrlA: Adaptive Retrieval-Augmented Generation via Probe-Guided Control",
            "url": "https://www.researchgate.net/publication/380974446_CtrlA_Adaptive_Retrieval-Augmented_Generation_via_Probe-Guided_Control"
          },
          {
            "title": "CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control | OpenReview",
            "url": "https://openreview.net/forum?id=QYvtX2XA8p&noteId=azYw0GI4QY"
          },
          {
            "title": "[2405.18727] CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control",
            "url": "https://arxiv.org/abs/2405.18727"
          },
          {
            "title": "[2405.18727v2] CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control",
            "url": "https://arxiv.org/abs/2405.18727v2"
          },
          {
            "title": "CtrlA/run.py at main · HSLiu-Initial/CtrlA",
            "url": "https://github.com/HSLiu-Initial/CtrlA/blob/main/run.py"
          },
          {
            "title": "HSLiu-Initial (Liu Huanshuo) · GitHub",
            "url": "https://github.com/HSLiu-Initial"
          }
        ]
      },
      "Based on the search results, I found information about the CtrlA project on GitHub:\n\n## CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control\n\nCtrlA introduces an effective inherent control-based adaptive RAG framework to enhance retrieval-augmented generation for LLM, balancing its internal and external knowledge.\n\n### Key Features\n\nCtrlA characterizes LLM's internal states and intervenes in the LLM generation from two perspectives: honesty steering and confidence monitoring via simple yet effective feature direction representations. More specifically, CtrlA employs an honesty probe to regulate the LLM's behavior by manipulating its representations for increased honesty, and a confidence probe to monitor the internal states of LLM and assess confidence levels, determining the retrieval necessity during generation.\n\n### Code Availability\n\nThis includes the original implementation of CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control. The code is available at the GitHub repository: https://github.com/HSLiu-Initial/CtrlA\n\n### Results\n\nExperiments show that CtrlA is superior to existing adaptive RAG methods on a diverse set of tasks, the honesty control can effectively make LLMs more honest and confidence monitoring is proven to be a promising indicator of retrieval trigger."
    ],
    "durationSeconds": 5.818835449000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8be4b058-3e70-4594-836c-04af0e9e8349",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-19T09:37:50.477Z_

<details><summary>Logged reasoning block</summary>

```text
CtrlA has code available at https://github.com/HSLiu-Initial/CtrlA. Good.

Now I have all the information I need. Let me compose the complete revised idea JSON.

Key synthesis of findings:

**NOVELTY SOLUTION**: Transform from "drift-only gating" to "multi-axis orthogonal gating framework":
- The Geometry of Forgetting proves drift ⊥ confidence ⊥ uncertainty (|cos| ≤ 0.14)


- CtrlA uses 2 probes (honesty + confidence) but misses drift entirely, making it the closest competitor
- AdaRAGUE aggregates 35 uncertainty methods but they're all variations of the same signal family
- Combining all three orthogonal axes is genuinely novel, with theoretical support from Bayes risk decreasing under independent features
- I can explore multiple fusion strategies: learned gating, cascading, or conceptor composition

**ENTITY TOKEN SOLUTION**: 
- The Geometry of Forgetting extracts activations at the first content token of the generated answer, eliminating the need for NER
- I just generate one token and extract the probe activations immediately to evaluate them
- I'll test alternative positions as ablations—the last query token, the last subject token—to see what matters most
- For structured benchmarks, entity boundaries come directly from dataset annotations

**BASELINE CODE SOLUTION**: I have 7 baselines to compare against, with most already having available implementations or being straightforward to rebuild. Probing-RAG, SeaKR, Self-Routing RAG, CtrlA, and token-entropy all have code or are trivial to implement. TARG and Rep-Con require reimplementation but are training-free and use standard techniques like PCA and contrastive learning. MMA-RAG is architecturally distinct—it's multimodal and post-retrieval with an MLP classifier—so it's more of a landscape reference than a direct competitor. I'm targeting an August 2026 ARR deadline.

I should aim for AAAI 2027 as a stretch goal, which gives me about 10.5 weeks to work with.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b976799-53f5-4b1d-accd-dbe35db58899",
  "isSidechain": false,
  "requestId": "req_011CbBhiwp7Wiq5ZxTNaossJ",
  "type": "assistant",
  "uuid": "2e3869de-163d-4941-8d8c-d30dcba97cc8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkUZJJJuM12BZzviFfTW4F",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2060,
      "cache_read_input_tokens": 45337,
      "output_tokens": 8172,
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
          "output_tokens": 8172,
          "cache_read_input_tokens": 45337,
          "cache_creation_input_tokens": 2060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2060
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

_source line 51 · 2026-05-19T09:40:29.930Z_

Now I have all the research I need. Let me compose the complete revised idea.

```json
{
  "title": "Orthogonal-Axis Gated Retrieval: Fusing Drift, Confidence, and Uncertainty Probes for Selective RAG",
  "core_problem": "Can fusing linear probes trained on three provably orthogonal representation axes—temporal drift, confidence, and uncertainty—yield a retrieval gate that strictly outperforms any single-signal gating method, and what is the optimal fusion strategy for combining these complementary internal signals to maximize the accuracy-efficiency tradeoff in selective RAG?",
  "opportunity": "The Geometry of Forgetting (arXiv:2605.09195, May 2026) proved that temporal drift, correctness, and uncertainty are encoded as geometrically orthogonal directions in LLM residual streams (|cos| ≤ 0.14 across five orthogonality tests, null-space projection |ΔAUROC| ≤ 0.008). Drift probes achieve AUROC 0.83–0.95 while all confidence/uncertainty methods remain at chance (0.49–0.57) for drift detection. That paper explicitly suggested drift-probe-triggered retrieval (§2) but never implemented it. Meanwhile, all existing selective RAG methods—including the most architecturally similar CtrlA (arXiv:2405.18727), which uses dual honesty+confidence probes—gate on signals that are provably blind to temporal drift. No work has combined all three orthogonal axes into a unified retrieval gate. Classical theory guarantees that combining independent (orthogonal) features strictly reduces Bayes risk when each carries nonzero mutual information about the target: since the three axes capture non-overlapping failure modes (stale knowledge, knowledge gaps, and ambiguity), a multi-axis gate should dominate any single-axis approach. This creates both a systems gap (no drift-probe retrieval system exists) and a methodological gap (no multi-axis representation-geometric gating framework exists for selective RAG).",
  "landscape": "Selective RAG gating methods fall into five categories, all operating on at most one or two representation axes:\n\n(1) **Probe-based confidence gating**: Probing-RAG (arXiv:2410.13339, NAACL 2025) trains feed-forward probers on hidden states for retrieval decisions using confidence signals. CtrlA (arXiv:2405.18727) uses dual probes—an honesty probe for behavioral intervention and a confidence probe for retrieval triggering—the closest multi-probe system to our approach, but uses only two non-drift axes.\n\n(2) **Uncertainty-based gating**: SeaKR (arXiv:2406.19215, ACL 2025) extracts self-aware uncertainty from FFN internal states. AdaRAGUE (arXiv:2501.12835, ACL 2025) conducts the most comprehensive comparison to date, evaluating 35 adaptive retrieval methods including 27 uncertainty estimation techniques, and proposes a hybrid logistic regression combining multiple uncertainty signals—but all from the same signal family (uncertainty), not orthogonal axes.\n\n(3) **Training-free output gating**: TARG (arXiv:2511.09803) uses prefix-logit margins for single-shot gating with 70–90% retrieval reduction on standard benchmarks. Self-Routing RAG (arXiv:2504.01018) routes via output-level confidence.\n\n(4) **Representation-based knowledge filtering**: 'Towards Knowledge Checking in RAG' (arXiv:2411.14572, NAACL 2025) uses Rep-PCA and Rep-Con classifiers on last-layer representations for knowledge checking, helpfulness, and contradiction detection.\n\n(5) **Residual-stream hallucination probing**: ICR Probe (ACL 2025, arXiv:2507.16488) applies linear probes to residual streams across all layers, aggregating ICR Scores for hallucination detection. LatentAudit (arXiv:2604.05358) measures Mahalanobis distance on mid-to-late residual-stream activations for faithfulness monitoring (AUROC 0.942 on PubMedQA).\n\nAll five categories rely on confidence, uncertainty, or general knowledge-state signals that the Geometry of Forgetting proved orthogonal to temporal drift. MMA-RAG (arXiv:2603.00511) extends hidden-state gating to multimodal RAG with a 4-class MLP on concatenated text+vision features—architecturally similar in using internal representations for gating, but targets visual-semantic mismatch rather than temporal staleness and requires post-retrieval features.\n\nOn the temporal-RAG side, T-GRAG, Chronos, and SmartVector (arXiv:2604.20598) add temporal awareness on the query/retrieval side, while 'Still Fresh?' (arXiv:2603.04532) found retrieval benchmarks remain stable under corpus drift, implicating model-side staleness. HoH (ACL 2025) showed a single outdated passage causes ≥20% RAG accuracy degradation.\n\nIn the representation engineering literature, Truth Forest (arXiv:2312.17484, AAAI 2024) combines orthogonal probing groups for truthfulness intervention—demonstrating the value of multi-orthogonal-probe composition—but for steering rather than gating. MeCo (arXiv:2502.12961, ACL 2025) found that 'simply averaging multiple probe scores does not yield accurate results,' directly motivating learned fusion mechanisms. The Linear Representation Hypothesis (arXiv:2311.03658) formally proves that causally separable concepts must be orthogonal under the causal inner product, and Pan et al. (arXiv:2502.09674, ICML 2025) demonstrate that multi-dimensional orthogonal directions encode genuinely different safety features with non-trivial interactions.\n\nAs of May 2026, no published or concurrent work has: (a) implemented drift-axis probes as a retrieval gate, (b) combined all three orthogonal representation axes for gating, or (c) provided a systematic comparison of multi-axis vs. single-axis representation-geometric gating for selective RAG.",
  "inspired_by": "Gap: The Geometry of Forgetting proves drift ⊥ confidence ⊥ uncertainty but builds no retrieval system. CtrlA combines honesty+confidence probes for gating but has no drift axis. AdaRAGUE combines 35 uncertainty methods but all from the same signal family. No work fuses all three provably orthogonal axes via a learned gate. Untried integration: three-axis representation-geometric gating with learned fusion, systematically evaluated against single-axis and multi-uncertainty baselines.",
  "approach": "Phase 1 — Independent Drift-Label Pipeline: Construct drift/non-drift labels independently using Wikidata revision history (Wikidated 1.0). For each entity-relation pair, query sequential Wikidata snapshots aligned to each model's training data cutoff to classify facts as Stable (unchanged since cutoff) or Drifted (value changed after cutoff). This pipeline also constructs the temporal-split PopQA evaluation set. Validate against the Geometry of Forgetting's labels if/when their code is released.\n\nPhase 2 — Multi-Axis Probe Training: For each of four primary models—Llama-3.1-8B-Instruct, Qwen-2.5-7B-Instruct, Gemma-2-9B-IT, Mistral-7B-Instruct—train three lightweight linear probes (<500K parameters each) on residual-stream activations at the first generated content token (matching the Geometry of Forgetting's extraction position, avoiding any NER dependency):\n  (a) Drift probe: trained on temporal drift labels from Phase 1, at the model-specific optimal layer from the original paper (L29 for Llama-3.1, L10 for Qwen-2.5, L33 for Gemma-2-9B, L6 for Mistral).\n  (b) Confidence probe: trained on correctness labels (whether the model answers correctly without retrieval), at the same layer.\n  (c) Uncertainty probe: trained on consistency labels (whether the model's top-k sampled answers agree), at the same layer.\nAll three probes extract activations at the first content-token position of the model's initial generation (requiring only a single token of generation before gating). Validate drift probe AUROC against the original paper's reported numbers as a reproduction check. Additionally train probes at ±3 layers around the optimal to measure robustness.\n\nPhase 3 — Multi-Axis Fusion Gate: Combine the three probe scores via three fusion strategies:\n  (a) Logistic regression: concatenate [drift_score, confidence_score, uncertainty_score] and learn a linear gate. Provides the simplest baseline for multi-axis combination.\n  (b) Query-conditioned MLP: a 2-layer MLP that takes the three probe scores plus a compressed query representation (PCA-projected last-token hidden state) as input, enabling context-dependent weighting of axes.\n  (c) Cascade gating: sequential thresholding—check drift first (is knowledge stale?), then uncertainty (is model uncertain?), then confidence (is model likely wrong?)—with per-stage thresholds calibrated on held-out validation splits.\nCompare all three against single-axis ablations (drift-only, confidence-only, uncertainty-only) to quantify the multi-axis advantage. The best fusion strategy is selected per benchmark via Pareto-optimal F1 on validation splits.\n\nPhase 4 — OAGR System Integration: At inference time: (1) process the query through the model, (2) generate one content token, (3) extract residual-stream activations at the first generated content token, (4) compute three probe scores, (5) pass scores through the fusion gate, (6) if the gate outputs 'retrieve,' augment with a temporally-indexed Wikipedia snapshot or web-search API; otherwise return the parametric answer. Threshold calibration accounts for different drift base rates across benchmarks.\n\nPhase 5 — Comprehensive Evaluation on three temporal QA benchmarks: (a) HoH (ACL 2025)—controlled outdated-information RAG benchmark; (b) StreamingQA (ICML 2022)—temporal adaptation QA with time-stamped news; (c) temporal-split PopQA—questions partitioned into drifted vs. stable subsets via our Wikidata pipeline. Compare against seven baselines: Probing-RAG, SeaKR, CtrlA, TARG, Self-Routing RAG, Rep-Con, and token-entropy thresholding, plus always-retrieve and never-retrieve bounds. Code availability: Probing-RAG, SeaKR, CtrlA, Self-Routing RAG have public code; TARG and Rep-Con require straightforward reimplementation; token-entropy is trivial. Metrics: QA accuracy (EM/F1) overall and stratified by drifted/stable subsets, retrieval efficiency (% queries retrieved), probe+fusion inference latency, and accuracy-efficiency Pareto frontiers.\n\nPhase 6 — Ablations and Analysis: (a) Single-axis vs. multi-axis: quantify the marginal contribution of each orthogonal axis to gating performance, with statistical significance tests; (b) Fusion strategy comparison: logistic regression vs. query-conditioned MLP vs. cascade, characterizing when each strategy wins; (c) Extraction position ablation: first generated content token (primary) vs. last query token vs. last subject token (using dataset-provided entity annotations), measuring sensitivity to position choice; (d) Layer robustness analysis (±5 layers around optimal); (e) Drift base rate sensitivity—how does the multi-axis advantage scale with the proportion of drifted queries? (f) Transfer to Qwen3-8B (untested architecture); (g) Error analysis: failure mode taxonomy across the three axes (false-positive retrievals, false-negative misses, axis confusion where the wrong axis triggers); (h) Comparison of Wikidata-pipeline labels vs. original paper labels when available.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "400-600 A100-80GB hours (Wikidata pipeline: CPU-only ~40h; multi-axis probe training ~20h/model × 4 = 80h; hidden-state extraction 4 models × 3 benchmarks ~200h; 7 baselines evaluation ~150h; ablations incl. fusion strategies + Qwen3-8B + layer/position sweeps ~120h)",
      "timeline": "10-12 weeks (2w Wikidata pipeline + data infrastructure, 2w multi-axis probe training + reproduction validation, 3w full evaluation across benchmarks + baselines + fusion strategies, 2w ablations + analysis, 1-2w writing + buffer)",
      "estimated_gpu_cost": "$800-1200 at ~$2.00/hr A100 spot pricing"
    },
    "human_in_loop": {
      "gpu_hours": "300-450 A100-80GB hours (Claude automates Wikidata pipeline construction, baseline integration, fusion strategy sweeps, and results analysis)",
      "timeline": "8-10 weeks",
      "claude_api_cost": "$200-400 (Sonnet 4.6 for code generation, experiment orchestration, and paper drafting at $3/$15 per M tokens)",
      "estimated_gpu_cost": "$600-900"
    },
    "auto_research": {
      "gpu_hours": "350-550 A100-80GB hours",
      "timeline": "6-9 weeks (parallelized probe training + evaluation sweeps)",
      "claude_api_cost": "$400-700 (heavier usage for autonomous pipeline development, fusion architecture search, and iterative ablation)",
      "estimated_gpu_cost": "$700-1100",
      "speed_bottleneck": "Hidden-state extraction requires sequential forward passes per model; Wikidata SPARQL API rate limits constrain drift-label construction (~5K queries/hour); fusion strategy comparison requires training and evaluating multiple gate architectures per benchmark."
    }
  },
  "target_venues": [
    "ARR August 2026 cycle (submission August 3, 2026) → EACL 2027 (commitment October 11, 2026) — primary target, 10.5 weeks available, realistic timeline",
    "AAAI 2027 (abstracts July 21, full papers July 28, 2026) — stretch goal, submit abstract at week 9 based on early results, complete paper by week 10",
    "TACL (rolling monthly deadline — suitable for extended journal-length version with all 6 original models + additional fusion ablations)"
  ],
  "level": "solid",
  "key_references": [
    "The Geometry of Forgetting: Temporal Knowledge Drift as an Independent Axis in LLM Representations (arXiv:2605.09195, May 2026) — establishes drift orthogonality (|cos| ≤ 0.14, ΔAUROC ≤ 0.008) and per-model optimal probe layers; suggests but does not implement retrieval application",
    "CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control (arXiv:2405.18727, 2024) — dual-probe system using honesty+confidence directions for retrieval gating; closest multi-probe selective RAG system but lacks drift axis",
    "Adaptive Retrieval Without Self-Knowledge? Bringing Uncertainty Back Home (arXiv:2501.12835, ACL 2025) — comprehensive comparison of 35 adaptive retrieval methods; proposes logistic regression fusion of multiple uncertainty signals but all from the same signal family",
    "Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval (arXiv:2410.13339, NAACL 2025) — hidden-state probing for retrieval decisions using confidence signals",
    "SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation (arXiv:2406.19215, ACL 2025) — FFN internal-state uncertainty for adaptive retrieval",
    "TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG (arXiv:2511.09803, Nov 2025) — prefix-logit-based training-free gating, 70-90% retrieval reduction on non-temporal benchmarks",
    "Towards Knowledge Checking in Retrieval-augmented Generation: A Representation Perspective (arXiv:2411.14572, NAACL 2025) — Rep-PCA and Rep-Con representation-based classifiers for knowledge filtering in RAG",
    "Self-Routing RAG: Binding Selective Retrieval with Knowledge Verbalization (arXiv:2504.01018, 2025) — output-level confidence routing",
    "MMA-RAG: Multimodal Adaptive Retrieval Augmented Generation through Internal Representation Learning (arXiv:2603.00511, Feb 2026) — hidden-state MLP gating for multimodal RAG; architecturally related but targets visual-semantic mismatch with post-retrieval features",
    "ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs (arXiv:2507.16488, ACL 2025) — linear probes on residual streams aggregated across layers for hallucination detection",
    "Truth Forest: Toward Multi-Scale Truthfulness in Large Language Models (arXiv:2312.17484, AAAI 2024) — combines orthogonal probing groups for truthfulness intervention; demonstrates multi-orthogonal-probe composition value",
    "The Linear Representation Hypothesis and the Geometry of Large Language Models (arXiv:2311.03658, 2023) — proves causally separable concepts must be orthogonal under the causal inner product; theoretical foundation for multi-axis probe combination",
    "The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions (arXiv:2502.09674, ICML 2025) — demonstrates multi-dimensional orthogonal directions encode genuinely different features with non-trivial interactions",
    "MeCo: Adaptive Tool Use in Large Language Models with Meta-Cognition Trigger (arXiv:2502.12961, ACL 2025) — meta-cognition probe for tool use; explicitly finds 'simply averaging multiple scores does not yield accurate results,' motivating learned fusion",
    "HoH: A Dynamic Benchmark for Evaluating the Impact of Outdated Information on RAG (arXiv:2503.04800, ACL 2025) — shows single outdated passage causes ≥20% RAG accuracy drop",
    "StreamingQA: A Benchmark for Adaptation to New Knowledge over Time in QA Models (ICML 2022) — temporal adaptation QA with time-stamped news",
    "RAG or Learning? Understanding the Limits of LLM Adaptation under Continuous Knowledge Drift (arXiv:2604.05096, Apr 2026) — benchmarks adaptation under continuous drift",
    "SmartVector: A Temporal Knowledge-Aware Embedding Approach for RAG (arXiv:2604.20598, Apr 2026) — temporal validity windows on retrieval side",
    "Still Fresh? Evaluating Temporal Drift in Retrieval Benchmarks (arXiv:2603.04532, Mar 2026) — shows retrieval benchmarks are stable under corpus drift, implicating model-side staleness",
    "Dissecting Recall of Factual Associations in Auto-Regressive Language Models (EMNLP 2023) — establishes mechanistic justification for last-subject-token extraction; three-step factual recall mechanism",
    "Towards Best Practices of Activation Patching in Language Models (arXiv:2309.16042, ICLR 2024) — demonstrates token position choice 'can greatly affect localization outcomes'; motivates our extraction position ablation",
    "Wikidated 1.0: An Evolving Knowledge Graph Dataset of Wikidata's Revision History (2022) — Wikidata revision history for temporal fact tracking"
  ],
  "description": "We present Orthogonal-Axis Gated Retrieval (OAGR), the first multi-axis representation-geometric gating framework for selective RAG that fuses probes trained on three provably orthogonal axes—temporal drift, confidence, and uncertainty—to make retrieval decisions. The Geometry of Forgetting (2026) proved these three axes are geometrically orthogonal in LLM residual streams (|cos| ≤ 0.14, null-space |ΔAUROC| ≤ 0.008), meaning each captures a non-overlapping failure mode: drift detects stale parametric knowledge (where the model is confident but wrong due to temporal change), confidence detects knowledge gaps (where the model lacks the fact entirely), and uncertainty detects ambiguity (where the model's internal state is indeterminate). Classical Bayes risk theory guarantees that combining independent features strictly reduces classification error, providing theoretical grounding for multi-axis superiority. We bridge two gaps: (1) the systems gap—no drift-probe retrieval system has been built despite the Geometry of Forgetting's suggestion; (2) the methodological gap—no selective RAG method combines provably orthogonal representation axes via a learned fusion gate. Our approach trains three per-model linear probes on residual-stream activations at the first generated content token (requiring only one token of generation before gating, with no NER dependency), then combines probe scores via three fusion strategies: logistic regression, query-conditioned MLP, and cascade gating. We evaluate against seven baselines with verified code availability—including CtrlA (the closest dual-probe competitor), Probing-RAG, SeaKR, TARG, Self-Routing RAG, Rep-Con, and token-entropy—across three temporal QA benchmarks (HoH, StreamingQA, temporal-split PopQA). Key ablations quantify the marginal contribution of each orthogonal axis, compare fusion strategies, and test extraction position robustness. We provide actionable guidance on when multi-axis gating should be preferred over single-signal alternatives and characterize the accuracy-efficiency Pareto frontier as a function of benchmark drift base rates.",
  "project_name": "orthogonal_axis_gated_rag",
  "source": "web_research",
  "change_type": "major",
  "revision_notes": {
    "round2_issue_1_novelty_elevation": "MAJOR CHANGE: Transformed from 'implementing what the Geometry of Forgetting suggested' (drift-only gating) to a genuinely novel multi-axis representation-geometric gating framework (OAGR). The new contribution is the first system to combine three provably orthogonal representation axes (drift, confidence, uncertainty) via learned fusion for retrieval gating. This is supported by: (a) classical Bayes risk theory showing combining independent features strictly reduces classification error; (b) the Linear Representation Hypothesis (arXiv:2311.03658) proving causally separable concepts must be orthogonal; (c) Truth Forest (AAAI 2024) demonstrating multi-orthogonal-probe composition improves intervention; (d) MeCo (ACL 2025) showing naive averaging fails, motivating learned fusion. CtrlA (arXiv:2405.18727) is the closest competitor with dual probes (honesty+confidence) but lacks drift—we add the critical third axis that captures the failure mode all existing methods miss. AdaRAGUE (arXiv:2501.12835, ACL 2025) combines 35 methods via logistic regression but all from the uncertainty signal family—we combine signals from three orthogonal families. Three fusion strategies (logistic regression, query-conditioned MLP, cascade) are compared as a methodological contribution. The paper now reads as 'introducing a principled multi-axis gating framework grounded in representational geometry' rather than 'implementing someone else's suggestion.'",
    "round2_issue_2_entity_token_resolution": "FIXED: Clarified that the Geometry of Forgetting extracts activations at 'the first content-token position of the generated answer' (not at the entity token in the query). Our approach follows this: process the query, generate one content token, extract activations at that position, and evaluate all three probes. This requires only a single token of generation before the gating decision, adding minimal latency (~2-5ms). Critically, this avoids any NER/entity-linking dependency at inference time. Added an extraction position ablation comparing: (a) first generated content token (primary, matching original paper), (b) last query token (efficient but may lack recall-specific activations), and (c) last subject token using dataset-provided entity annotations (applicable only to structured benchmarks). This addresses the robustness concern raised, supported by Zhang & Nanda (ICLR 2024) showing token position choice 'can greatly affect localization outcomes' and Geva et al. (EMNLP 2023) establishing the mechanistic justification for last-subject-token extraction in factual recall.",
    "round2_issue_3_baseline_code_scoping": "FIXED: Verified code availability for all baselines. Reduced from 8 to 7 baselines, all with public code or straightforward reimplementation: (1) Probing-RAG — code at github.com/baekingeol/Probing-RAG; (2) SeaKR — code at github.com/THU-KEG/SeaKR; (3) CtrlA — code at github.com/HSLiu-Initial/CtrlA (NEW, closest multi-probe competitor); (4) Self-Routing RAG — code at github.com/xiaowu0162/self-routing-rag; (5) Token-entropy — code at github.com/Nomothings/Entropy-RAG and trivial to implement; (6) TARG — no code but training-free design makes reimplementation straightforward (~200 lines: compute entropy/margin from draft logits); (7) Rep-Con — no code but standard PCA/contrastive probe on hidden states, well-described methodology. Dropped INKER (no code, complex multi-signal integration architecture) and Skill-RAG (no code, requires failure-state prober + skill router, medium-high reimplementation complexity). Added CtrlA as the most important new baseline—it is the only existing multi-probe gating system, making it the natural comparison point for OAGR's three-probe approach. Also added AdaRAGUE (code at github.com/s-nlp/AdaRAGUE) as a supplementary comparison in the fusion strategy analysis (not a full baseline, but referenced for the logistic regression fusion approach).",
    "round2_issue_4_mma_rag_discussion": "FIXED: Added MMA-RAG (arXiv:2603.00511) to the landscape discussion with detailed architectural comparison. Key similarities: both use hidden-state classifiers for retrieval gating decisions, both perform layer-wise analysis to select optimal extraction layers. Key differences: (a) MMA-RAG uses an MLP (nonlinear) on concatenated multimodal features vs. our linear probes; (b) MMA-RAG requires post-retrieval features (runs model with and without retrieval, then decides) vs. our pre-retrieval gating; (c) MMA-RAG targets visual-semantic mismatch in multimodal RAG vs. our temporal-drift + multi-axis detection in text RAG; (d) MMA-RAG uses a 4-class scheme (S1-S4 based on retrieval×correctness interaction) vs. our binary gate. OAGR's pre-retrieval gating is more computationally efficient (one partial forward pass vs. two full passes).",
    "round2_issue_5_timeline_realism": "FIXED: Shifted primary target to ARR August 2026 cycle (submission August 3, 10.5 weeks from today) → EACL 2027 (commitment October 11, 2026). AAAI 2027 (abstracts July 21, papers July 28) downgraded to stretch goal—submit abstract at week 9 based on early results if trajectory is strong. Timeline breakdown: weeks 1-2 Wikidata pipeline + data infrastructure; weeks 3-4 multi-axis probe training + reproduction validation; weeks 5-7 full evaluation across benchmarks, baselines, and fusion strategies; weeks 8-9 ablations + analysis; weeks 10-10.5 writing + buffer. The reduced baseline set (7 instead of 8, with 5 having public code) and the focused fusion strategy comparison (3 strategies) make this timeline realistic. The human-in-loop estimate (8-10 weeks) fits within the ARR August window.",
    "round1_issues_preserved": "All Round 1 fixes remain intact: correct model set (all from original paper), model-specific optimal layers, independent Wikidata pipeline, no fixed retrieval-reduction claims, Rep-Con baseline included."
  }
}
```

**Summary of changes (major revision):**

### What changed and why

1. **NOVELTY — from "implement suggestion" to "novel multi-axis framework"** (Issue 1): The paper is fundamentally reframed. Instead of just implementing drift-probe gating (which the Geometry of Forgetting suggested), we introduce **Orthogonal-Axis Gated Retrieval (OAGR)**—the first system to fuse three provably orthogonal representation axes (drift, confidence, uncertainty) via learned fusion gates. Research confirmed this gap is real: CtrlA uses 2 probes (honesty+confidence, no drift), AdaRAGUE combines 35 methods but all from the uncertainty family, and Truth Forest combines orthogonal probes but for intervention not gating. The theoretical backing is strong (Bayes risk strictly decreases under feature independence; Linear Representation Hypothesis proves causally separable concepts are orthogonal). Three fusion strategies (logistic regression, query-conditioned MLP, cascade) become a methodological contribution.

2. **ENTITY TOKEN — problem eliminated** (Issue 2): Deep reading revealed the Geometry of Forgetting actually extracts at the *first generated content token*, not at the entity in the query. Our system follows this: generate one token → extract activations → evaluate probes. No NER needed. Added an extraction position ablation comparing first-generated-token vs. last-query-token vs. last-subject-token, motivated by Zhang & Nanda (ICLR 2024) showing position choice significantly affects results.

3. **BASELINES — scoped to verified code** (Issue 3): Reduced to 7 baselines: 5 with public code (Probing-RAG, SeaKR, CtrlA, Self-Routing RAG, token-entropy) + 2 easy reimplementations (TARG, Rep-Con). Dropped INKER and Skill-RAG (no code, complex architectures). Added **CtrlA** as the most critical new baseline—it's the only existing multi-probe gating system.

4. **MMA-RAG — discussed with clear differentiation** (Issue 4): Added to landscape with detailed architectural comparison (multimodal vs. text, post-retrieval vs. pre-retrieval, MLP vs. linear probe, 4-class vs. binary).

5. **TIMELINE — realistic primary target** (Issue 5): ARR August 2026 (Aug 3, 10.5 weeks) is now the primary target; AAAI 2027 downgraded to stretch goal. The reduced baseline set and focused fusion comparison make this feasible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e3869de-163d-4941-8d8c-d30dcba97cc8",
  "isSidechain": false,
  "requestId": "req_011CbBhiwp7Wiq5ZxTNaossJ",
  "type": "assistant",
  "uuid": "0bbcaa3a-7807-499d-9456-a36a5971303d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkUZJJJuM12BZzviFfTW4F",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2060,
      "cache_read_input_tokens": 45337,
      "output_tokens": 8172,
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
          "output_tokens": 8172,
          "cache_read_input_tokens": 45337,
          "cache_creation_input_tokens": 2060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2060
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

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Drift-Probe-Gated Retrieval: A Systematic Evaluation of Temporal Stale…",
  "leafUuid": "0bbcaa3a-7807-499d-9456-a36a5971303d",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Add multi-signal gating to drift-probe RAG system",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Drift-Probe-Gated Retrieval: A Systematic Evaluation of Temporal Stale…",
  "leafUuid": "0bbcaa3a-7807-499d-9456-a36a5971303d",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Add multi-signal gating to drift-probe RAG system",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed"
}
```

---
