# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-14 (UTC).** ## Original idea { "tit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 94
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-2/58a2f634-1766-42cc-9986-03afe86809d4.jsonl`
- **Structured JSON:** [`19c82bda2f8de4ea73a4.json`](../../sessions/19/19c82bda2f8de4ea73a4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T16:44:52.134Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T16:44:52.134Z",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-14 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Counterfactual Probing Disentangles Evidence Gaps from Reasoning Difficulty for Step-Level Retrieval Gating\",\n  \"core_problem\": \"Current adaptive retrieval methods for reasoning LLMs use signals that conflate two fundamentally different failure modes: evidence gaps (the model lacks factual knowledge for a step) and reasoning difficulty (the step is logically complex, and retrieval introduces noise). Probing-RAG gates retrieval via hidden-state probes with binary correctness labels. Skill-RAG routes among retrieval skills based on failure-state probing but diagnoses query-evidence misalignment, not whether retrieval should occur. ProbeRAG/CLEAR (arXiv 2510.12460; ACL 2026 Findings) uses a 3-layer MLP probe on decoder hidden states for sentence-level knowledge conflict detection in RAG — achieving 97–98% accuracy on MQuAKE — but targets parametric-contextual conflict, not whether a step fails due to missing knowledge vs. reasoning complexity. ReaLM-Retrieve's composite RSUS score cannot distinguish missing knowledge from logical complexity. DeepControl's information utility (novelty + effectiveness) addresses when to continue retrieving but conflates both failure sources into a single scalar. IG-Search's counterfactual baseline (random documents vs. retrieved documents) provides step-level credit assignment for search quality but does not classify WHY a step benefits from retrieval. TIPS (arXiv 2603.22293) assigns dense turn-level rewards via potential-based shaping, achieving 11.8% EM improvement — addressing credit assignment for search decisions but through RL training signals, not inference-time diagnosis. DART demonstrates that reasoning and tool-use compete during joint RL training — gradient interference between the two capabilities is measurable and harmful — but proposes an architectural fix (disentangled LoRA) rather than diagnosing failure modes at inference time. 'Disentangling Memory and Reasoning Ability in Large Language Models' (arXiv 2411.13504; ACL 2025) introduces explicit &lt;memory> and &lt;reason> tokens to decompose LLM inference into knowledge retrieval vs. logical reasoning steps, achieving 83.3% disentanglement accuracy and finding that 78–98% of errors on commonsense tasks stem from reasoning rather than memory — directly validating that the knowledge-vs-reasoning axis is trainable and separable. 'Knowledge or Reasoning?' (arXiv 2506.02126) shows that knowledge correctness and reasoning quality are separable dimensions at the step level (knowledge-accuracy correlation 0.998 vs. reasoning-accuracy 0.698 in medical QA), validating the axis we target — but operates as an offline evaluation framework using GPT-4o judges, not as an inference-time retrieval gating mechanism. 'Where Does Reasoning Break?' (arXiv 2605.13772) detects step-level hallucinations via hidden-state transport geometry with strong in-domain performance (91.0% AUROC on ProcessBench), but classifies binary correctness (hallucinated vs. correct), not failure-mode type (evidence gap vs. reasoning difficulty), and its student model collapses under distribution shift (cross-model AUROC drops to 33–58%). PRISM (arXiv 2604.16909) disentangles hallucinations into knowledge-missing, knowledge-error, reasoning-error, and instruction-following dimensions, but operates as an evaluation benchmark, not an inference-time mechanism. Critically, while 'Disentangling Memory and Reasoning' measured error distributions on commonsense tasks (finding reasoning errors dominate at 78–98%), no work has measured this distribution for multi-hop factual QA where retrieval is available — a setting where we hypothesize evidence gaps are substantially more prevalent. No existing method provides counterfactually supervised, step-level classification of evidence gaps vs. reasoning difficulty in hidden-state space for inference-time retrieval gating.\",\n  \"opportunity\": \"Four converging lines of evidence make this the right moment for counterfactual probing of retrieval failure modes: (1) The evidence-vs-reasoning axis is real, trainable, and task-dependent — 'Disentangling Memory and Reasoning' achieves 83.3% disentanglement accuracy with explicit memory/reason tokens on Qwen2.5-7B and finds error distributions vary dramatically by task (98.3% reasoning errors on StrategyQA vs. 78.4% on CommonsenseQA), 'Knowledge or Reasoning?' achieves step-level separation with high correlation, PRISM's four-way hallucination taxonomy validates knowledge-vs-reasoning as a meaningful diagnostic axis, a PubMedBERT classifier separates knowledge-heavy from reasoning-heavy medical questions at 81% accuracy (arXiv 2505.11462), and Skill-RAG's representation analysis confirms failure states occupy 'structured, separable regions' in hidden-state space. (2) Hidden-state probing for RAG is technically mature — ProbeRAG/CLEAR demonstrates that 3-layer MLP probes on decoder hidden states achieve 97–98% accuracy for knowledge conflict detection, confirming that fine-grained RAG-relevant signals are linearly separable in latent space; however, no existing probe targets failure-mode type (evidence gap vs. reasoning difficulty). (3) Indiscriminate retrieval demonstrably harms reasoning — non-retrieval traces achieve 84.2% on GSM8K vs. lower with retrieval (arXiv 2602.07213), DART quantifies that reasoning and tool-use produce misaligned gradients during joint training, and IG-Search shows models adaptively learn to search conservatively on single-hop questions (1.3 calls) vs. actively on multi-hop (2.4 calls), implying retrieval value varies by step type. (4) Counterfactual and geometric methodology for step-level analysis is maturing — IG-Search uses counterfactual random-document baselines for step-level credit, TIPS demonstrates that turn-level credit assignment substantially improves training stability (11.8% EM improvement), CF-RAG (ICLR 2026) applies counterfactual reasoning to distinguish causal from correlated evidence, and 'Where Does Reasoning Break?' demonstrates that hidden-state trajectories encode step-level correctness with high fidelity (teacher AUROC 91–98%), though its cross-model generalization failure (student AUROC 33–58% under shift) motivates our within-checkpoint probing design. However, no prior work uses counterfactual branching (forking each step into retrieval vs. no-retrieval paths) to generate causal labels for training an inference-time probe that classifies failure mode type. This combination — counterfactual causal supervision + hidden-state probing + step-level failure-mode classification — fills a specific gap. Crucially, while 'Disentangling Memory and Reasoning' found that reasoning errors dominate on commonsense tasks (78–98%), this distribution is unknown for multi-hop factual QA where retrieval is available. We hypothesize the distribution is substantially different: multi-hop factual questions require chaining specific facts (entities, dates, relationships) that are more likely to exceed the model's parametric knowledge, shifting the distribution toward evidence gaps. The step-level failure distribution itself is a novel empirical measurement with direct implications for how the field designs adaptive retrieval systems.\",\n  \"landscape\": \"**Hidden-state probing for retrieval:** Probing-RAG (NAACL 2025) is a direct predecessor: a 5MB FC probe on intermediate layers gates retrieval at query level with binary correctness labels, reducing retrieval by ~50%. Skill-RAG (arXiv 2604.15771) extends this with per-layer probers on Gemma2-9B's posterior-2/3 layers plus a prompt-based skill router selecting among query rewriting, decomposition, evidence focusing, or exit — achieving 46.8% average accuracy and +13.6 on 2WikiMultiHopQA over Probing-RAG. ProbeRAG/CLEAR (arXiv 2510.12460; ACL 2026 Findings) probes decoder hidden states at the sentence level for knowledge conflict detection in RAG, using a 3-layer MLP probe (with 2-layer and 5-layer variants) trained on MQuAKE conflict pairs; achieves 97–98% accuracy on MQuAKE and 79–88% cross-benchmark, confirming that fine-grained RAG-relevant signals are extractable from hidden states. ProbeRAG's three-stage framework (knowledge pruning → latent conflict probing → conflict-aware attention) is methodologically adjacent but targets parametric-contextual knowledge conflicts, not failure-mode classification (evidence gap vs. reasoning difficulty). LAnR (arXiv 2604.17866) uses a lightweight MLP control head over hidden-state entropy for adaptive retrieval stopping within a latent-space RAG framework, demonstrating another instance of learned retrieval control but in a fundamentally different architecture (unified encoder-retriever-generator). **Knowledge-reasoning disentanglement:** 'Disentangling Memory and Reasoning Ability in Large Language Models' (arXiv 2411.13504; ACL 2025) is the most direct validation of our target axis: it introduces &lt;memory> and &lt;reason> tokens to decompose LLM inference, achieving 83.3% disentanglement accuracy via LoRA fine-tuning on GPT-4o-generated labels. Its error analysis reveals that reasoning errors dominate on commonsense tasks (78–98%), but the method operates via explicit token-guided generation (training-time decomposition), not via post-hoc hidden-state probing, and evaluates on commonsense QA (StrategyQA, CommonsenseQA, TruthfulQA), not multi-hop factual QA where retrieval is available. The open question — whether multi-hop factual QA shows a similar or inverted distribution — is the empirical gap we address. 'Knowledge or Reasoning?' (arXiv 2506.02126) decomposes step-level reasoning into Knowledge Index and Information Gain, finding knowledge-accuracy correlation of 0.998 vs. reasoning-accuracy of 0.698. The medical disentanglement work (arXiv 2505.11462) achieves 81% accuracy separating question types with PubMedBERT. **Hidden-state probing for step-level failures:** 'Where Does Reasoning Break?' (arXiv 2605.13772) frames step-level hallucination as transport-cost excursions in hidden-state space, achieving 91.0% AUROC (teacher) on ProcessBench. Its BiLSTM student achieves strong in-domain results (75–99.8% AUROC) but collapses under distribution shift (cross-model AUROC 33–58%). This validates that hidden states encode step-level correctness signals but targets binary correctness, not failure-mode classification. Reasoning Theater (arXiv 2603.05488) shows linear probes detect CoT divergence from internal beliefs, further confirming probing viability. PRISM (arXiv 2604.16909) decomposes hallucinations into knowledge-missing, knowledge-error, reasoning-error, and instruction-following dimensions as an evaluation framework, confirming the diagnostic axis we operationalize for inference-time use. **RL-based retrieval timing:** Search-R1 (arXiv 2503.09516) trains retrieval timing via GRPO with outcome-only reward, achieving 41% improvement on Qwen2.5-7B. SLATE (arXiv 2602.23440) adds decomposed process rewards (reasoning, query, answer quality), reaching 0.461 avg EM on 7B. IG-Search (arXiv 2604.15148) introduces step-level information gain rewards using a counterfactual baseline of random documents, measuring how much retrieved documents improve answer confidence — achieving 0.430 avg EM on Qwen2.5-3B with 1.3–2.4 search calls per rollout. IG-Search's counterfactual is conceptually adjacent but serves a different purpose: it evaluates search query quality (good retrieval vs. random), not whether retrieval itself is needed vs. harmful. TIPS (arXiv 2603.22293) assigns dense turn-level rewards via potential-based reward shaping using a teacher model's answer likelihood, achieving 11.8% EM and 13.6% F1 improvements over PPO on Qwen2.5-7B across seven QA benchmarks. TIPS addresses credit assignment for search decisions through RL training, while we address it through inference-time probing — complementary approaches to the same underlying problem. **Adaptive information control:** DeepControl (arXiv 2602.01672) defines information utility U(e) = ρ·Novelty + (1-ρ)·Effectiveness and uses stopping/continuation rules, achieving 9.4% improvement over RL baselines on Qwen2.5-7B. DeepControl addresses 'when to stop retrieving' via a training-time utility signal but cannot diagnose failure mode type at inference time. **Reasoning-tool competition:** DART (arXiv 2602.00994) introduces LEAS to quantify gradient interference between reasoning and tool-use, showing they induce misaligned gradient directions. DART's disentangled LoRA achieves 6.35% avg improvement. DART validates our core premise — reasoning and retrieval compete — but proposes architectural separation during training, while we propose a diagnostic probe for inference-time gating. **Other related:** FLARE (EMNLP 2023) uses token probability thresholds. ReaLM-Retrieve (arXiv 2604.26649) achieves 71.2% F1 on MuSiQue with composite RSUS. GRADE (arXiv 2604.02830) probes knowledge gaps via gradient subspace dynamics but requires backpropagation (unsuitable for inference). SynthWorlds (arXiv 2510.24427) disentangles knowledge from reasoning at task level via synthetic corpora. **Gap:** No existing work provides counterfactually supervised, step-level probing that classifies evidence gaps vs. reasoning difficulty in hidden-state space for post-hoc inference-time retrieval gating, nor has any work empirically measured the step-level distribution of these failure modes in multi-hop factual QA (as opposed to commonsense QA, where 'Disentangling Memory and Reasoning' found reasoning errors dominate at 78–98%).\",\n  \"approach\": \"We propose a focused empirical study with two first-class contributions: (1) a counterfactual labeling methodology that produces the first step-level failure-mode distribution for multi-hop factual QA (measuring what fraction of reasoning steps are knowledge-limited vs. reasoning-limited — extending the commonsense findings of 'Disentangling Memory and Reasoning' to a retrieval-augmented setting), and (2) inference-time retrieval gating via lightweight probes trained on these counterfactual labels. This is scoped as a short paper; RL integration is deferred to follow-up work.\\n\\n**Step 0 — Infrastructure Setup & Sanity Check (Day 0-1, ~2 H100h):** We pre-download the Search-R1 Qwen2.5-7B checkpoint and configure the vLLM + veRL environment following the Search-R1 repository setup. We pre-index the Wikipedia retrieval corpus in the required jsonl format (id + contents). A minimal sanity check (10 questions, 2 rollouts per condition) validates the counterfactual generation pipeline end-to-end before committing to full-scale experiments. This front-loads infrastructure risk and ensures the remaining 9 days are dedicated to research.\\n\\n**Step 1 — Counterfactual Data Generation (~8-12 H100h):** Starting from the publicly released Search-R1 Qwen2.5-7B checkpoint, we generate reasoning traces on ~800 questions sampled from HotpotQA (400), MuSiQue (200), and 2WikiMultiHopQA (200). We identify retrieval decision points using two complementary heuristics:\\n\\n*(a) Search-present positions:* At each token where the model generates `&lt;search>` in the trace, we create a no-retrieval counterfactual by suppressing the search token and forcing continued reasoning within `&lt;think>`. These are naturally occurring decision points (~2-3 per question based on IG-Search's finding of 1.3-2.4 search calls per rollout for multi-hop tasks).\\n\\n*(b) Search-absent positions:* At sentence boundaries within `&lt;think>` blocks (detected via regex `[.?!]\\\\s` or newline-delimited segments, following the step-boundary convention in 'Where Does Reasoning Break?'), we sample up to 2 candidate insertion points per trace where the model did NOT search. Selection prioritizes sentences containing entity mentions or factual claims (detected via simple NER heuristics on the preceding sentence). At each candidate, we create a retrieval counterfactual by inserting a `&lt;search>` call using the preceding reasoning context as the query. This yields ~4-5 decision points per question and ~3,500-4,000 step instances total.\\n\\nAt each decision point, we fork execution into retrieval and no-retrieval conditions with k=5 independent rollouts per condition using vLLM batch inference (temperature=0.7, consistent with Search-R1 training). Final answer correctness is propagated backward to each fork point. Labeling uses the correctness rates r_ret and r_no_ret across rollouts: steps where r_ret ≥ 4/5 AND r_no_ret ≤ 2/5 are labeled 'evidence-gap'; steps where r_no_ret ≥ 3/5 AND r_ret ≤ r_no_ret are labeled 'reasoning-difficulty'; remaining steps are labeled 'mixed.' We additionally compute soft labels (evidence_gap_score = r_ret − r_no_ret) for regression-based probe training. **The three-class distribution is reported as a first-class empirical finding** — contrasting with 'Disentangling Memory and Reasoning's finding that 78–98% of commonsense errors are reasoning-limited, we hypothesize multi-hop factual QA shows a substantially higher proportion of evidence gaps due to the requirement for chaining specific factual knowledge.\\n\\n**Pre-committed framing alternative:** If >50% of steps are labeled 'mixed,' we transition to a soft-label regression framework using the continuous evidence-gap score as the target, and evaluate retrieval gating via threshold on this continuous score rather than three-class classification. The failure-mode distribution analysis remains a valid contribution regardless.\\n\\n**Step 2 — Hidden-State Extraction & Probe Training (~3-5 H100h):** For each step instance, we extract hidden states from the Qwen2.5-7B model at the decision-point token position across the posterior 2/3 of layers (following Skill-RAG's methodology; informed by ProbeRAG/CLEAR's finding that deeper layers better capture RAG-relevant signals). We train two probe architectures: (a) a per-layer linear probe (comparable to the linear probe baseline in 'Where Does Reasoning Break?'), and (b) a per-layer 3-layer MLP (following ProbeRAG/CLEAR's architecture for hidden-state probing in RAG settings). Training uses 70/15/15 train/dev/test splits stratified by dataset and label class. We evaluate probe accuracy on the three-class task and on the binary gating task (retrieve = evidence-gap ∪ mixed, skip = reasoning-difficulty). **Go/no-go gate: if binary gating probe accuracy on held-out steps < 65%, we report the separability analysis and failure distribution as the primary findings (still a contribution) rather than proceeding to gating experiments.**\\n\\n**Step 3 — Inference-Time Gating Evaluation (~5-8 H100h):** Assuming probe validation succeeds, we apply the trained probe as a hard retrieval gate on the same Search-R1 checkpoint during inference (no retraining): at each step where the model generates a `&lt;search>` token, the probe classifies the hidden state; retrieval executes only if the probe predicts 'evidence-gap' or 'mixed' (above a calibrated threshold), otherwise the model continues reasoning without external input. We evaluate on held-out test portions of HotpotQA, MuSiQue, and 2WikiMultiHopQA, reporting F1, EM, and retrieval calls per question. Baselines: (1) no retrieval, (2) always retrieve (standard Search-R1), (3) Probing-RAG-style binary probe (trained on observational correctness labels rather than counterfactual labels — this is the critical ablation of causal supervision), (4) FLARE-style token probability threshold. The counterfactual-vs.-observational comparison (baseline #3) is the central experiment validating whether counterfactual labels provide signal beyond observational correctness.\\n\\n**Pre-committed significance thresholds:** We define minimum effect sizes for the counterfactual-vs.-observational comparison (baseline #3): counterfactual labels must yield ≥3 percentage points absolute improvement in binary gating accuracy on held-out steps, OR achieve ≥5% reduction in retrieval calls per question at matched downstream F1 (within 0.5 F1 points). If both thresholds are missed, we report this as a negative result — that counterfactual supervision does not meaningfully improve over simpler observational labels — which is itself informative for the field. In this case, the paper pivots to frame the failure-mode distribution as the primary contribution and the gating comparison as a secondary finding establishing that observational labels are sufficient. This pre-commitment ensures the paper produces a clear finding regardless of outcome.\\n\\n**Step 4 — Targeted Ablations & Analysis (~3-5 H100h):** We prioritize ablations that fit within 4 pages + appendix. **Main paper:** (a) Counterfactual vs. observational labels with pre-committed thresholds (key contribution validation). (b) Probe architecture comparison (linear vs. 3-layer MLP). (c) Failure-mode distribution analysis across datasets (evidence-gap vs. reasoning-difficulty vs. mixed proportions), with explicit comparison to 'Disentangling Memory and Reasoning's commonsense findings. **Appendix:** (d) Gating threshold sensitivity (precision-recall curve). (e) Cross-dataset transfer (train on HotpotQA, evaluate on MuSiQue). (f) t-SNE/UMAP visualization of hidden-state clusters by failure-mode type. (g) Qualitative error analysis of 'mixed' steps.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~24-35 H100h (infrastructure setup ~2h, counterfactual generation ~10h, hidden state extraction ~3h, probe training <1h, evaluation ~5h, ablations ~5h, buffer ~5h)\",\n      \"gpu_utilization\": \"40-55% — GPUs idle during analysis, visualization, and paper writing\",\n      \"timeline\": \"11 days (May 14-25, 2026); Day 0-1 dedicated to infrastructure setup and sanity check, Day 2-5 counterfactual generation, Day 5-7 probing and evaluation, Day 7-9 ablations, Day 9-11 writing\",\n      \"team\": \"2 researchers (1 on data generation/evaluation pipeline, 1 on probing/analysis/writing)\",\n      \"estimated_gpu_cost\": \"$60-88 at ~$2.50/hr mid-range H100 rental\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~30-40 H100h (agent handles pipeline orchestration, human reviews label distributions and go/no-go)\",\n      \"gpu_utilization\": \"60-75% — agent queues batch jobs efficiently, human reviews at checkpoints\",\n      \"timeline\": \"9-11 days; Day 0-1 infrastructure (pre-download checkpoint, index corpus, sanity check), Day 2-5 generation, Day 6 go/no-go review, Day 7-9 evaluation, Day 10-11 writing\",\n      \"team\": \"1 researcher, ~1-2hr/day reviewing label quality, probe results, go/no-go, and writing\",\n      \"claude_api_cost\": \"$30-60 (~300-600 turns for code generation, experiment orchestration, analysis)\",\n      \"estimated_gpu_cost\": \"$75-100 at ~$2.50/hr\",\n      \"risk_note\": \"Primary risk is label distribution skew — if >60% of steps are 'mixed,' we pivot to soft-label regression as pre-committed. Human judgment on the go/no-go is essential by Day 6. Infrastructure risk mitigated by Day 0-1 sanity check.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~34-45 H100h (agent explores more threshold configurations and probe architectures)\",\n      \"gpu_utilization\": \"80-90% — agent pipelines generation → extraction → training → evaluation as continuous jobs\",\n      \"timeline\": \"7-9 days with 4 H100s; Day 0-1 infrastructure, Day 2-4 generation, Day 5-6 probing/evaluation, Day 7-9 ablations/writing\",\n      \"team\": \"0 (initial setup only: configure Search-R1/veRL/vLLM environment, dataset loading, retrieval corpus indexing — front-loaded to Day 0-1)\",\n      \"claude_api_cost\": \"$80-150 (~800-1500 turns for autonomous experiment design, debugging, analysis, paper drafting)\",\n      \"estimated_gpu_cost\": \"$85-113 at ~$2.50/hr\",\n      \"speed_bottleneck\": \"Counterfactual generation is the bottleneck (~2-3h wall time on 4 H100s with vLLM batch); probe training and evaluation are fast (<1h each)\",\n      \"risk_note\": \"Without human judgment on whether the 'mixed' class distribution warrants pivoting the paper framing, agent may produce a mechanically correct but uncompelling paper\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 short paper via ARR May 25, 2026 (11 days — primary and only target, track: Information Retrieval and Text Mining or Question Answering)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval (NAACL 2025 Findings)\",\n    \"Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing (Preprint 2026, arXiv 2604.15771)\",\n    \"Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation [ProbeRAG/CLEAR] (ACL 2026 Findings, arXiv 2510.12460)\",\n    \"When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models [ReaLM-Retrieve] (Preprint 2026, arXiv 2604.26649)\",\n    \"Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning (Preprint 2025, arXiv 2503.09516)\",\n    \"SLATE: Truncated Step-Level Sampling with Process Rewards for Retrieval-Augmented Reasoning (Preprint 2026, arXiv 2602.23440)\",\n    \"IG-Search: Step-Level Information Gain Rewards for Search-Augmented Reasoning (Preprint 2026, arXiv 2604.15148)\",\n    \"TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs (Preprint 2026, arXiv 2603.22293)\",\n    \"DeepControl: Scaling Search-Augmented LLM Reasoning via Adaptive Information Control (ICLR 2026 SPOT Workshop, arXiv 2602.01672)\",\n    \"DART: Reasoning and Tool-use Compete in Agentic RL — From Quantifying Interference to Disentangled Tuning (Preprint 2026, arXiv 2602.00994)\",\n    \"Disentangling Memory and Reasoning Ability in Large Language Models (ACL 2025, arXiv 2411.13504)\",\n    \"Knowledge or Reasoning? A Close Look at How LLMs Think Across Domains (Preprint 2025, arXiv 2506.02126)\",\n    \"Adaptive Retrieval helps Reasoning in LLMs — but mostly if it's not used (Preprint 2025, arXiv 2602.07213)\",\n    \"Active Retrieval Augmented Generation [FLARE] (EMNLP 2023)\",\n    \"Counterfactual Reasoning for Retrieval-Augmented Generation [CF-RAG] (ICLR 2026)\",\n    \"Disentangling Knowledge and Reasoning in Medical Large Language Models (Preprint 2025, arXiv 2505.11462)\",\n    \"Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Preprint 2026, arXiv 2603.05488)\",\n    \"SynthWorlds: Controlled Parallel Worlds for Disentangling Knowledge from Reasoning (Preprint 2025, arXiv 2510.24427)\",\n    \"GRADE: Probing Knowledge Gaps in LLMs through Gradient Subspace Dynamics (Preprint 2026, arXiv 2604.02830)\",\n    \"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (Preprint 2026, arXiv 2605.13772)\",\n    \"PRISM: Probing Reasoning, Instruction, and Source Memory in LLM Hallucinations (Preprint 2026, arXiv 2604.16909)\",\n    \"Latent Abstraction for Retrieval-Augmented Generation [LAnR] (Preprint 2026, arXiv 2604.17866)\"\n  ],\n  \"description\": \"Current adaptive retrieval methods for reasoning LLMs use signals (uncertainty, token probability, composite scores) that conflate evidence gaps with reasoning difficulty, yet recent work confirms these are separable and task-dependent: 'Disentangling Memory and Reasoning' (ACL 2025) achieves 83.3% disentanglement accuracy with explicit memory/reason tokens and finds 78–98% of commonsense errors stem from reasoning rather than memory; 'Knowledge or Reasoning?' shows step-level knowledge-accuracy correlation of 0.998 vs. reasoning-accuracy 0.698; DART proves reasoning and tool-use produce competing gradients; ProbeRAG/CLEAR demonstrates 97–98% accuracy for sentence-level knowledge conflict detection via hidden-state probing; Skill-RAG finds failure states occupy structured regions in hidden-state space; and 'Where Does Reasoning Break?' demonstrates hidden states encode step-level correctness with 91% AUROC (though targeting binary correctness, not failure-mode type). We present a focused empirical study with two first-class contributions. First, we introduce a counterfactual labeling methodology that produces the first step-level failure-mode distribution for multi-hop factual QA: using a Search-R1 Qwen2.5-7B checkpoint, we fork ~3,500-4,000 reasoning steps into retrieval and no-retrieval paths with k=5 rollouts each, generating causal labels ('evidence-gap,' 'reasoning-difficulty,' 'mixed'). Decision points are identified via two complementary heuristics: (a) positions where the model generated `&lt;search>` tokens (natural retrieval decisions), and (b) sentence-boundary sampling within `&lt;think>` blocks where the model did NOT search (counterfactual insertion points selected via entity/claim detection). The resulting failure-mode distribution — what fraction of multi-hop factual QA reasoning steps are knowledge-limited vs. reasoning-limited — is itself a novel empirical finding that extends 'Disentangling Memory and Reasoning's commonsense-task analysis to a retrieval-augmented setting, with direct implications for adaptive retrieval design. We hypothesize multi-hop factual QA shows a substantially different distribution (more evidence gaps) than commonsense QA. Second, we train lightweight probes (linear and 3-layer MLP, following ProbeRAG/CLEAR's architecture) on hidden states to classify failure mode type, then apply the probe as an inference-time retrieval gate on the existing checkpoint without retraining: retrieve only when the probe predicts 'evidence-gap' or 'mixed,' skip retrieval when reasoning is the bottleneck. We pre-commit to significance thresholds for the central counterfactual-vs.-observational comparison: counterfactual labels must yield ≥3 percentage points absolute improvement in binary gating accuracy OR ≥5% reduction in retrieval calls at matched downstream F1 (within 0.5 F1 points); if both are missed, we report a negative result, pivoting the paper to frame the failure-mode distribution as the primary contribution. If >50% of steps are 'mixed,' we pre-commit to soft-label regression on a continuous evidence-gap score. Key novelty vs. existing methods: (1) counterfactual causal labels rather than observational correctness (Probing-RAG), RL reward shaping (IG-Search, TIPS, DeepControl), or explicit token-guided generation ('Disentangling Memory and Reasoning'), (2) failure-mode classification (evidence gap vs. reasoning difficulty) rather than binary correctness detection ('Where Does Reasoning Break?'), knowledge conflict detection (ProbeRAG/CLEAR), or hallucination taxonomy (PRISM), (3) post-hoc inference-time applicability without retraining. Evaluation on HotpotQA, MuSiQue, and 2WikiMultiHopQA with baselines: no-retrieval, always-retrieve, Probing-RAG-style observational probe (critical ablation with pre-committed thresholds), and FLARE threshold. Infrastructure setup front-loaded to Day 0-1 with sanity check. Scoped as a short paper (~24-45 H100h total); RL integration deferred to follow-up.\",\n  \"project_name\": \"evid_reason_disentangle\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 5)\nIssues: [\"MINOR: ProbeRAG/CLEAR venue claim is unverifiable. The proposal states 'ACL 2026 Findings, arXiv 2510.12460' but the paper was submitted to ICLR 2026 (OpenReview ID NhO6iEUISf) and subsequently withdrawn. It does not appear in the ACL Anthology for 2026 Findings. Either verify the venue or cite it as a preprint only.\", \"MINOR: Missing related work — KRUX (arXiv 2508.19202, 'Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning') probes the knowledge-vs-reasoning bottleneck in LLMs by injecting Knowledge Ingredients (KIs) in-context and measuring performance delta. While black-box and purely diagnostic (not a competitor), it validates the knowledge-vs-reasoning separation axis and should be cited alongside 'Disentangling Memory and Reasoning' and 'Knowledge or Reasoning?' as converging evidence.\", \"MINOR: Potential naming confusion — 'Counterfactual Probing for Hallucination Detection and Mitigation in Large Language Models' (arXiv 2508.01862) uses 'counterfactual probing' in its title but means probing with counterfactual statements, not probing hidden states after counterfactual branching. Since the proposal uses 'counterfactual probing' prominently, consider citing this paper to explicitly differentiate the two meanings, or refine the terminology (e.g., 'counterfactual-branching probe' or 'fork-and-probe').\", \"MINOR: Impact framing could be stronger. The failure-mode distribution finding is positioned as a first-class contribution, but the paper doesn't articulate what design principles it would inform beyond 'retrieve less when reasoning is the bottleneck.' Spell out: if 70% of multi-hop steps are evidence-gap, what does that concretely change about how the field should build adaptive retrieval systems? If the distribution varies dramatically by dataset or question difficulty, what are the implications for per-query adaptive strategies?\"]\nFeedback: The proposal has improved dramatically over four rounds and is close to passing. The core novelty is verified — no existing work does counterfactual failure-mode probing for retrieval gating. The main blocker is the impact score (3/5), which drags the average to 3.75. Specific fixes to cross the threshold:\n\n1. **Fix ProbeRAG/CLEAR venue claim**: I found it was withdrawn from ICLR 2026 and cannot confirm ACL 2026 Findings acceptance. Either provide evidence of the ACL 2026 Findings acceptance or cite it as 'arXiv 2510.12460' only. This is a reference accuracy issue that reviewers will check.\n\n2. **Add KRUX citation**: KRUX (arXiv 2508.19202) separates knowledge from reasoning via controlled KI injection in scientific tasks. It validates the same axis your probe targets, providing additional converging evidence. Cite it briefly in the opportunity section alongside 'Disentangling Memory and Reasoning.'\n\n3. **Disambiguate 'counterfactual probing'**: arXiv 2508.01862 uses this exact phrase for a different technique. Either cite it to differentiate or slightly adjust your terminology.\n\n4. **Strengthen impact framing**: The failure-mode distribution is your most robust contribution (it's informative regardless of gating results). Push harder on WHY it matters:\n   - If multi-hop factual QA shows predominantly evidence gaps (vs. commonsense QA's 78-98% reasoning errors), this directly challenges the assumption that reasoning-side improvements alone can solve multi-hop QA.\n   - The distribution variance across datasets (HotpotQA vs. MuSiQue vs. 2WikiMultiHopQA) could reveal that different benchmarks have fundamentally different bottleneck structures, with implications for benchmark selection in future adaptive retrieval work.\n   - Frame the gating experiment as a proof-of-concept that validates the distribution's actionability, not as the primary contribution.\n\n5. **Consider adding one generalizability signal**: Even within the 11-day scope, extracting hidden states from a second checkpoint (e.g., the Qwen2.5-3B Search-R1 checkpoint, which is also publicly available) and checking whether the probe's failure-mode distribution is consistent across model sizes would substantially strengthen the paper's generalizability claim. This adds ~2-3 H100h (well within budget) and addresses the single-checkpoint limitation.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 5 轮修订，近 3 轮的平均分从 4.0 到 3.8，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T16:44:52.139Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T16:44:52.139Z",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

## Round 1

92 recorded events

### User

_source line 3 · 2026-05-14T16:44:52.270Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-14 (UTC).**

## Original idea
{
  "title": "Counterfactual Probing Disentangles Evidence Gaps from Reasoning Difficulty for Step-Level Retrieval Gating",
  "core_problem": "Current adaptive retrieval methods for reasoning LLMs use signals that conflate two fundamentally different failure modes: evidence gaps (the model lacks factual knowledge for a step) and reasoning difficulty (the step is logically complex, and retrieval introduces noise). Probing-RAG gates retrieval via hidden-state probes with binary correctness labels. Skill-RAG routes among retrieval skills based on failure-state probing but diagnoses query-evidence misalignment, not whether retrieval should occur. ProbeRAG/CLEAR (arXiv 2510.12460; ACL 2026 Findings) uses a 3-layer MLP probe on decoder hidden states for sentence-level knowledge conflict detection in RAG — achieving 97–98% accuracy on MQuAKE — but targets parametric-contextual conflict, not whether a step fails due to missing knowledge vs. reasoning complexity. ReaLM-Retrieve's composite RSUS score cannot distinguish missing knowledge from logical complexity. DeepControl's information utility (novelty + effectiveness) addresses when to continue retrieving but conflates both failure sources into a single scalar. IG-Search's counterfactual baseline (random documents vs. retrieved documents) provides step-level credit assignment for search quality but does not classify WHY a step benefits from retrieval. TIPS (arXiv 2603.22293) assigns dense turn-level rewards via potential-based shaping, achieving 11.8% EM improvement — addressing credit assignment for search decisions but through RL training signals, not inference-time diagnosis. DART demonstrates that reasoning and tool-use compete during joint RL training — gradient interference between the two capabilities is measurable and harmful — but proposes an architectural fix (disentangled LoRA) rather than diagnosing failure modes at inference time. 'Disentangling Memory and Reasoning Ability in Large Language Models' (arXiv 2411.13504; ACL 2025) introduces explicit &lt;memory> and &lt;reason> tokens to decompose LLM inference into knowledge retrieval vs. logical reasoning steps, achieving 83.3% disentanglement accuracy and finding that 78–98% of errors on commonsense tasks stem from reasoning rather than memory — directly validating that the knowledge-vs-reasoning axis is trainable and separable. 'Knowledge or Reasoning?' (arXiv 2506.02126) shows that knowledge correctness and reasoning quality are separable dimensions at the step level (knowledge-accuracy correlation 0.998 vs. reasoning-accuracy 0.698 in medical QA), validating the axis we target — but operates as an offline evaluation framework using GPT-4o judges, not as an inference-time retrieval gating mechanism. 'Where Does Reasoning Break?' (arXiv 2605.13772) detects step-level hallucinations via hidden-state transport geometry with strong in-domain performance (91.0% AUROC on ProcessBench), but classifies binary correctness (hallucinated vs. correct), not failure-mode type (evidence gap vs. reasoning difficulty), and its student model collapses under distribution shift (cross-model AUROC drops to 33–58%). PRISM (arXiv 2604.16909) disentangles hallucinations into knowledge-missing, knowledge-error, reasoning-error, and instruction-following dimensions, but operates as an evaluation benchmark, not an inference-time mechanism. Critically, while 'Disentangling Memory and Reasoning' measured error distributions on commonsense tasks (finding reasoning errors dominate at 78–98%), no work has measured this distribution for multi-hop factual QA where retrieval is available — a setting where we hypothesize evidence gaps are substantially more prevalent. No existing method provides counterfactually supervised, step-level classification of evidence gaps vs. reasoning difficulty in hidden-state space for inference-time retrieval gating.",
  "opportunity": "Four converging lines of evidence make this the right moment for counterfactual probing of retrieval failure modes: (1) The evidence-vs-reasoning axis is real, trainable, and task-dependent — 'Disentangling Memory and Reasoning' achieves 83.3% disentanglement accuracy with explicit memory/reason tokens on Qwen2.5-7B and finds error distributions vary dramatically by task (98.3% reasoning errors on StrategyQA vs. 78.4% on CommonsenseQA), 'Knowledge or Reasoning?' achieves step-level separation with high correlation, PRISM's four-way hallucination taxonomy validates knowledge-vs-reasoning as a meaningful diagnostic axis, a PubMedBERT classifier separates knowledge-heavy from reasoning-heavy medical questions at 81% accuracy (arXiv 2505.11462), and Skill-RAG's representation analysis confirms failure states occupy 'structured, separable regions' in hidden-state space. (2) Hidden-state probing for RAG is technically mature — ProbeRAG/CLEAR demonstrates that 3-layer MLP probes on decoder hidden states achieve 97–98% accuracy for knowledge conflict detection, confirming that fine-grained RAG-relevant signals are linearly separable in latent space; however, no existing probe targets failure-mode type (evidence gap vs. reasoning difficulty). (3) Indiscriminate retrieval demonstrably harms reasoning — non-retrieval traces achieve 84.2% on GSM8K vs. lower with retrieval (arXiv 2602.07213), DART quantifies that reasoning and tool-use produce misaligned gradients during joint training, and IG-Search shows models adaptively learn to search conservatively on single-hop questions (1.3 calls) vs. actively on multi-hop (2.4 calls), implying retrieval value varies by step type. (4) Counterfactual and geometric methodology for step-level analysis is maturing — IG-Search uses counterfactual random-document baselines for step-level credit, TIPS demonstrates that turn-level credit assignment substantially improves training stability (11.8% EM improvement), CF-RAG (ICLR 2026) applies counterfactual reasoning to distinguish causal from correlated evidence, and 'Where Does Reasoning Break?' demonstrates that hidden-state trajectories encode step-level correctness with high fidelity (teacher AUROC 91–98%), though its cross-model generalization failure (student AUROC 33–58% under shift) motivates our within-checkpoint probing design. However, no prior work uses counterfactual branching (forking each step into retrieval vs. no-retrieval paths) to generate causal labels for training an inference-time probe that classifies failure mode type. This combination — counterfactual causal supervision + hidden-state probing + step-level failure-mode classification — fills a specific gap. Crucially, while 'Disentangling Memory and Reasoning' found that reasoning errors dominate on commonsense tasks (78–98%), this distribution is unknown for multi-hop factual QA where retrieval is available. We hypothesize the distribution is substantially different: multi-hop factual questions require chaining specific facts (entities, dates, relationships) that are more likely to exceed the model's parametric knowledge, shifting the distribution toward evidence gaps. The step-level failure distribution itself is a novel empirical measurement with direct implications for how the field designs adaptive retrieval systems.",
  "landscape": "**Hidden-state probing for retrieval:** Probing-RAG (NAACL 2025) is a direct predecessor: a 5MB FC probe on intermediate layers gates retrieval at query level with binary correctness labels, reducing retrieval by ~50%. Skill-RAG (arXiv 2604.15771) extends this with per-layer probers on Gemma2-9B's posterior-2/3 layers plus a prompt-based skill router selecting among query rewriting, decomposition, evidence focusing, or exit — achieving 46.8% average accuracy and +13.6 on 2WikiMultiHopQA over Probing-RAG. ProbeRAG/CLEAR (arXiv 2510.12460; ACL 2026 Findings) probes decoder hidden states at the sentence level for knowledge conflict detection in RAG, using a 3-layer MLP probe (with 2-layer and 5-layer variants) trained on MQuAKE conflict pairs; achieves 97–98% accuracy on MQuAKE and 79–88% cross-benchmark, confirming that fine-grained RAG-relevant signals are extractable from hidden states. ProbeRAG's three-stage framework (knowledge pruning → latent conflict probing → conflict-aware attention) is methodologically adjacent but targets parametric-contextual knowledge conflicts, not failure-mode classification (evidence gap vs. reasoning difficulty). LAnR (arXiv 2604.17866) uses a lightweight MLP control head over hidden-state entropy for adaptive retrieval stopping within a latent-space RAG framework, demonstrating another instance of learned retrieval control but in a fundamentally different architecture (unified encoder-retriever-generator). **Knowledge-reasoning disentanglement:** 'Disentangling Memory and Reasoning Ability in Large Language Models' (arXiv 2411.13504; ACL 2025) is the most direct validation of our target axis: it introduces &lt;memory> and &lt;reason> tokens to decompose LLM inference, achieving 83.3% disentanglement accuracy via LoRA fine-tuning on GPT-4o-generated labels. Its error analysis reveals that reasoning errors dominate on commonsense tasks (78–98%), but the method operates via explicit token-guided generation (training-time decomposition), not via post-hoc hidden-state probing, and evaluates on commonsense QA (StrategyQA, CommonsenseQA, TruthfulQA), not multi-hop factual QA where retrieval is available. The open question — whether multi-hop factual QA shows a similar or inverted distribution — is the empirical gap we address. 'Knowledge or Reasoning?' (arXiv 2506.02126) decomposes step-level reasoning into Knowledge Index and Information Gain, finding knowledge-accuracy correlation of 0.998 vs. reasoning-accuracy of 0.698. The medical disentanglement work (arXiv 2505.11462) achieves 81% accuracy separating question types with PubMedBERT. **Hidden-state probing for step-level failures:** 'Where Does Reasoning Break?' (arXiv 2605.13772) frames step-level hallucination as transport-cost excursions in hidden-state space, achieving 91.0% AUROC (teacher) on ProcessBench. Its BiLSTM student achieves strong in-domain results (75–99.8% AUROC) but collapses under distribution shift (cross-model AUROC 33–58%). This validates that hidden states encode step-level correctness signals but targets binary correctness, not failure-mode classification. Reasoning Theater (arXiv 2603.05488) shows linear probes detect CoT divergence from internal beliefs, further confirming probing viability. PRISM (arXiv 2604.16909) decomposes hallucinations into knowledge-missing, knowledge-error, reasoning-error, and instruction-following dimensions as an evaluation framework, confirming the diagnostic axis we operationalize for inference-time use. **RL-based retrieval timing:** Search-R1 (arXiv 2503.09516) trains retrieval timing via GRPO with outcome-only reward, achieving 41% improvement on Qwen2.5-7B. SLATE (arXiv 2602.23440) adds decomposed process rewards (reasoning, query, answer quality), reaching 0.461 avg EM on 7B. IG-Search (arXiv 2604.15148) introduces step-level information gain rewards using a counterfactual baseline of random documents, measuring how much retrieved documents improve answer confidence — achieving 0.430 avg EM on Qwen2.5-3B with 1.3–2.4 search calls per rollout. IG-Search's counterfactual is conceptually adjacent but serves a different purpose: it evaluates search query quality (good retrieval vs. random), not whether retrieval itself is needed vs. harmful. TIPS (arXiv 2603.22293) assigns dense turn-level rewards via potential-based reward shaping using a teacher model's answer likelihood, achieving 11.8% EM and 13.6% F1 improvements over PPO on Qwen2.5-7B across seven QA benchmarks. TIPS addresses credit assignment for search decisions through RL training, while we address it through inference-time probing — complementary approaches to the same underlying problem. **Adaptive information control:** DeepControl (arXiv 2602.01672) defines information utility U(e) = ρ·Novelty + (1-ρ)·Effectiveness and uses stopping/continuation rules, achieving 9.4% improvement over RL baselines on Qwen2.5-7B. DeepControl addresses 'when to stop retrieving' via a training-time utility signal but cannot diagnose failure mode type at inference time. **Reasoning-tool competition:** DART (arXiv 2602.00994) introduces LEAS to quantify gradient interference between reasoning and tool-use, showing they induce misaligned gradient directions. DART's disentangled LoRA achieves 6.35% avg improvement. DART validates our core premise — reasoning and retrieval compete — but proposes architectural separation during training, while we propose a diagnostic probe for inference-time gating. **Other related:** FLARE (EMNLP 2023) uses token probability thresholds. ReaLM-Retrieve (arXiv 2604.26649) achieves 71.2% F1 on MuSiQue with composite RSUS. GRADE (arXiv 2604.02830) probes knowledge gaps via gradient subspace dynamics but requires backpropagation (unsuitable for inference). SynthWorlds (arXiv 2510.24427) disentangles knowledge from reasoning at task level via synthetic corpora. **Gap:** No existing work provides counterfactually supervised, step-level probing that classifies evidence gaps vs. reasoning difficulty in hidden-state space for post-hoc inference-time retrieval gating, nor has any work empirically measured the step-level distribution of these failure modes in multi-hop factual QA (as opposed to commonsense QA, where 'Disentangling Memory and Reasoning' found reasoning errors dominate at 78–98%).",
  "approach": "We propose a focused empirical study with two first-class contributions: (1) a counterfactual labeling methodology that produces the first step-level failure-mode distribution for multi-hop factual QA (measuring what fraction of reasoning steps are knowledge-limited vs. reasoning-limited — extending the commonsense findings of 'Disentangling Memory and Reasoning' to a retrieval-augmented setting), and (2) inference-time retrieval gating via lightweight probes trained on these counterfactual labels. This is scoped as a short paper; RL integration is deferred to follow-up work.\n\n**Step 0 — Infrastructure Setup & Sanity Check (Day 0-1, ~2 H100h):** We pre-download the Search-R1 Qwen2.5-7B checkpoint and configure the vLLM + veRL environment following the Search-R1 repository setup. We pre-index the Wikipedia retrieval corpus in the required jsonl format (id + contents). A minimal sanity check (10 questions, 2 rollouts per condition) validates the counterfactual generation pipeline end-to-end before committing to full-scale experiments. This front-loads infrastructure risk and ensures the remaining 9 days are dedicated to research.\n\n**Step 1 — Counterfactual Data Generation (~8-12 H100h):** Starting from the publicly released Search-R1 Qwen2.5-7B checkpoint, we generate reasoning traces on ~800 questions sampled from HotpotQA (400), MuSiQue (200), and 2WikiMultiHopQA (200). We identify retrieval decision points using two complementary heuristics:\n\n*(a) Search-present positions:* At each token where the model generates `&lt;search>` in the trace, we create a no-retrieval counterfactual by suppressing the search token and forcing continued reasoning within `&lt;think>`. These are naturally occurring decision points (~2-3 per question based on IG-Search's finding of 1.3-2.4 search calls per rollout for multi-hop tasks).\n\n*(b) Search-absent positions:* At sentence boundaries within `&lt;think>` blocks (detected via regex `[.?!]\\s` or newline-delimited segments, following the step-boundary convention in 'Where Does Reasoning Break?'), we sample up to 2 candidate insertion points per trace where the model did NOT search. Selection prioritizes sentences containing entity mentions or factual claims (detected via simple NER heuristics on the preceding sentence). At each candidate, we create a retrieval counterfactual by inserting a `&lt;search>` call using the preceding reasoning context as the query. This yields ~4-5 decision points per question and ~3,500-4,000 step instances total.\n\nAt each decision point, we fork execution into retrieval and no-retrieval conditions with k=5 independent rollouts per condition using vLLM batch inference (temperature=0.7, consistent with Search-R1 training). Final answer correctness is propagated backward to each fork point. Labeling uses the correctness rates r_ret and r_no_ret across rollouts: steps where r_ret ≥ 4/5 AND r_no_ret ≤ 2/5 are labeled 'evidence-gap'; steps where r_no_ret ≥ 3/5 AND r_ret ≤ r_no_ret are labeled 'reasoning-difficulty'; remaining steps are labeled 'mixed.' We additionally compute soft labels (evidence_gap_score = r_ret − r_no_ret) for regression-based probe training. **The three-class distribution is reported as a first-class empirical finding** — contrasting with 'Disentangling Memory and Reasoning's finding that 78–98% of commonsense errors are reasoning-limited, we hypothesize multi-hop factual QA shows a substantially higher proportion of evidence gaps due to the requirement for chaining specific factual knowledge.\n\n**Pre-committed framing alternative:** If >50% of steps are labeled 'mixed,' we transition to a soft-label regression framework using the continuous evidence-gap score as the target, and evaluate retrieval gating via threshold on this continuous score rather than three-class classification. The failure-mode distribution analysis remains a valid contribution regardless.\n\n**Step 2 — Hidden-State Extraction & Probe Training (~3-5 H100h):** For each step instance, we extract hidden states from the Qwen2.5-7B model at the decision-point token position across the posterior 2/3 of layers (following Skill-RAG's methodology; informed by ProbeRAG/CLEAR's finding that deeper layers better capture RAG-relevant signals). We train two probe architectures: (a) a per-layer linear probe (comparable to the linear probe baseline in 'Where Does Reasoning Break?'), and (b) a per-layer 3-layer MLP (following ProbeRAG/CLEAR's architecture for hidden-state probing in RAG settings). Training uses 70/15/15 train/dev/test splits stratified by dataset and label class. We evaluate probe accuracy on the three-class task and on the binary gating task (retrieve = evidence-gap ∪ mixed, skip = reasoning-difficulty). **Go/no-go gate: if binary gating probe accuracy on held-out steps < 65%, we report the separability analysis and failure distribution as the primary findings (still a contribution) rather than proceeding to gating experiments.**\n\n**Step 3 — Inference-Time Gating Evaluation (~5-8 H100h):** Assuming probe validation succeeds, we apply the trained probe as a hard retrieval gate on the same Search-R1 checkpoint during inference (no retraining): at each step where the model generates a `&lt;search>` token, the probe classifies the hidden state; retrieval executes only if the probe predicts 'evidence-gap' or 'mixed' (above a calibrated threshold), otherwise the model continues reasoning without external input. We evaluate on held-out test portions of HotpotQA, MuSiQue, and 2WikiMultiHopQA, reporting F1, EM, and retrieval calls per question. Baselines: (1) no retrieval, (2) always retrieve (standard Search-R1), (3) Probing-RAG-style binary probe (trained on observational correctness labels rather than counterfactual labels — this is the critical ablation of causal supervision), (4) FLARE-style token probability threshold. The counterfactual-vs.-observational comparison (baseline #3) is the central experiment validating whether counterfactual labels provide signal beyond observational correctness.\n\n**Pre-committed significance thresholds:** We define minimum effect sizes for the counterfactual-vs.-observational comparison (baseline #3): counterfactual labels must yield ≥3 percentage points absolute improvement in binary gating accuracy on held-out steps, OR achieve ≥5% reduction in retrieval calls per question at matched downstream F1 (within 0.5 F1 points). If both thresholds are missed, we report this as a negative result — that counterfactual supervision does not meaningfully improve over simpler observational labels — which is itself informative for the field. In this case, the paper pivots to frame the failure-mode distribution as the primary contribution and the gating comparison as a secondary finding establishing that observational labels are sufficient. This pre-commitment ensures the paper produces a clear finding regardless of outcome.\n\n**Step 4 — Targeted Ablations & Analysis (~3-5 H100h):** We prioritize ablations that fit within 4 pages + appendix. **Main paper:** (a) Counterfactual vs. observational labels with pre-committed thresholds (key contribution validation). (b) Probe architecture comparison (linear vs. 3-layer MLP). (c) Failure-mode distribution analysis across datasets (evidence-gap vs. reasoning-difficulty vs. mixed proportions), with explicit comparison to 'Disentangling Memory and Reasoning's commonsense findings. **Appendix:** (d) Gating threshold sensitivity (precision-recall curve). (e) Cross-dataset transfer (train on HotpotQA, evaluate on MuSiQue). (f) t-SNE/UMAP visualization of hidden-state clusters by failure-mode type. (g) Qualitative error analysis of 'mixed' steps.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~24-35 H100h (infrastructure setup ~2h, counterfactual generation ~10h, hidden state extraction ~3h, probe training <1h, evaluation ~5h, ablations ~5h, buffer ~5h)",
      "gpu_utilization": "40-55% — GPUs idle during analysis, visualization, and paper writing",
      "timeline": "11 days (May 14-25, 2026); Day 0-1 dedicated to infrastructure setup and sanity check, Day 2-5 counterfactual generation, Day 5-7 probing and evaluation, Day 7-9 ablations, Day 9-11 writing",
      "team": "2 researchers (1 on data generation/evaluation pipeline, 1 on probing/analysis/writing)",
      "estimated_gpu_cost": "$60-88 at ~$2.50/hr mid-range H100 rental"
    },
    "human_in_loop": {
      "gpu_hours": "~30-40 H100h (agent handles pipeline orchestration, human reviews label distributions and go/no-go)",
      "gpu_utilization": "60-75% — agent queues batch jobs efficiently, human reviews at checkpoints",
      "timeline": "9-11 days; Day 0-1 infrastructure (pre-download checkpoint, index corpus, sanity check), Day 2-5 generation, Day 6 go/no-go review, Day 7-9 evaluation, Day 10-11 writing",
      "team": "1 researcher, ~1-2hr/day reviewing label quality, probe results, go/no-go, and writing",
      "claude_api_cost": "$30-60 (~300-600 turns for code generation, experiment orchestration, analysis)",
      "estimated_gpu_cost": "$75-100 at ~$2.50/hr",
      "risk_note": "Primary risk is label distribution skew — if >60% of steps are 'mixed,' we pivot to soft-label regression as pre-committed. Human judgment on the go/no-go is essential by Day 6. Infrastructure risk mitigated by Day 0-1 sanity check."
    },
    "auto_research": {
      "gpu_hours": "~34-45 H100h (agent explores more threshold configurations and probe architectures)",
      "gpu_utilization": "80-90% — agent pipelines generation → extraction → training → evaluation as continuous jobs",
      "timeline": "7-9 days with 4 H100s; Day 0-1 infrastructure, Day 2-4 generation, Day 5-6 probing/evaluation, Day 7-9 ablations/writing",
      "team": "0 (initial setup only: configure Search-R1/veRL/vLLM environment, dataset loading, retrieval corpus indexing — front-loaded to Day 0-1)",
      "claude_api_cost": "$80-150 (~800-1500 turns for autonomous experiment design, debugging, analysis, paper drafting)",
      "estimated_gpu_cost": "$85-113 at ~$2.50/hr",
      "speed_bottleneck": "Counterfactual generation is the bottleneck (~2-3h wall time on 4 H100s with vLLM batch); probe training and evaluation are fast (<1h each)",
      "risk_note": "Without human judgment on whether the 'mixed' class distribution warrants pivoting the paper framing, agent may produce a mechanically correct but uncompelling paper"
    }
  },
  "target_venues": [
    "EMNLP 2026 short paper via ARR May 25, 2026 (11 days — primary and only target, track: Information Retrieval and Text Mining or Question Answering)"
  ],
  "level": "top-tier",
  "key_references": [
    "Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval (NAACL 2025 Findings)",
    "Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing (Preprint 2026, arXiv 2604.15771)",
    "Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation [ProbeRAG/CLEAR] (ACL 2026 Findings, arXiv 2510.12460)",
    "When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models [ReaLM-Retrieve] (Preprint 2026, arXiv 2604.26649)",
    "Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning (Preprint 2025, arXiv 2503.09516)",
    "SLATE: Truncated Step-Level Sampling with Process Rewards for Retrieval-Augmented Reasoning (Preprint 2026, arXiv 2602.23440)",
    "IG-Search: Step-Level Information Gain Rewards for Search-Augmented Reasoning (Preprint 2026, arXiv 2604.15148)",
    "TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs (Preprint 2026, arXiv 2603.22293)",
    "DeepControl: Scaling Search-Augmented LLM Reasoning via Adaptive Information Control (ICLR 2026 SPOT Workshop, arXiv 2602.01672)",
    "DART: Reasoning and Tool-use Compete in Agentic RL — From Quantifying Interference to Disentangled Tuning (Preprint 2026, arXiv 2602.00994)",
    "Disentangling Memory and Reasoning Ability in Large Language Models (ACL 2025, arXiv 2411.13504)",
    "Knowledge or Reasoning? A Close Look at How LLMs Think Across Domains (Preprint 2025, arXiv 2506.02126)",
    "Adaptive Retrieval helps Reasoning in LLMs — but mostly if it's not used (Preprint 2025, arXiv 2602.07213)",
    "Active Retrieval Augmented Generation [FLARE] (EMNLP 2023)",
    "Counterfactual Reasoning for Retrieval-Augmented Generation [CF-RAG] (ICLR 2026)",
    "Disentangling Knowledge and Reasoning in Medical Large Language Models (Preprint 2025, arXiv 2505.11462)",
    "Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Preprint 2026, arXiv 2603.05488)",
    "SynthWorlds: Controlled Parallel Worlds for Disentangling Knowledge from Reasoning (Preprint 2025, arXiv 2510.24427)",
    "GRADE: Probing Knowledge Gaps in LLMs through Gradient Subspace Dynamics (Preprint 2026, arXiv 2604.02830)",
    "Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (Preprint 2026, arXiv 2605.13772)",
    "PRISM: Probing Reasoning, Instruction, and Source Memory in LLM Hallucinations (Preprint 2026, arXiv 2604.16909)",
    "Latent Abstraction for Retrieval-Augmented Generation [LAnR] (Preprint 2026, arXiv 2604.17866)"
  ],
  "description": "Current adaptive retrieval methods for reasoning LLMs use signals (uncertainty, token probability, composite scores) that conflate evidence gaps with reasoning difficulty, yet recent work confirms these are separable and task-dependent: 'Disentangling Memory and Reasoning' (ACL 2025) achieves 83.3% disentanglement accuracy with explicit memory/reason tokens and finds 78–98% of commonsense errors stem from reasoning rather than memory; 'Knowledge or Reasoning?' shows step-level knowledge-accuracy correlation of 0.998 vs. reasoning-accuracy 0.698; DART proves reasoning and tool-use produce competing gradients; ProbeRAG/CLEAR demonstrates 97–98% accuracy for sentence-level knowledge conflict detection via hidden-state probing; Skill-RAG finds failure states occupy structured regions in hidden-state space; and 'Where Does Reasoning Break?' demonstrates hidden states encode step-level correctness with 91% AUROC (though targeting binary correctness, not failure-mode type). We present a focused empirical study with two first-class contributions. First, we introduce a counterfactual labeling methodology that produces the first step-level failure-mode distribution for multi-hop factual QA: using a Search-R1 Qwen2.5-7B checkpoint, we fork ~3,500-4,000 reasoning steps into retrieval and no-retrieval paths with k=5 rollouts each, generating causal labels ('evidence-gap,' 'reasoning-difficulty,' 'mixed'). Decision points are identified via two complementary heuristics: (a) positions where the model generated `&lt;search>` tokens (natural retrieval decisions), and (b) sentence-boundary sampling within `&lt;think>` blocks where the model did NOT search (counterfactual insertion points selected via entity/claim detection). The resulting failure-mode distribution — what fraction of multi-hop factual QA reasoning steps are knowledge-limited vs. reasoning-limited — is itself a novel empirical finding that extends 'Disentangling Memory and Reasoning's commonsense-task analysis to a retrieval-augmented setting, with direct implications for adaptive retrieval design. We hypothesize multi-hop factual QA shows a substantially different distribution (more evidence gaps) than commonsense QA. Second, we train lightweight probes (linear and 3-layer MLP, following ProbeRAG/CLEAR's architecture) on hidden states to classify failure mode type, then apply the probe as an inference-time retrieval gate on the existing checkpoint without retraining: retrieve only when the probe predicts 'evidence-gap' or 'mixed,' skip retrieval when reasoning is the bottleneck. We pre-commit to significance thresholds for the central counterfactual-vs.-observational comparison: counterfactual labels must yield ≥3 percentage points absolute improvement in binary gating accuracy OR ≥5% reduction in retrieval calls at matched downstream F1 (within 0.5 F1 points); if both are missed, we report a negative result, pivoting the paper to frame the failure-mode distribution as the primary contribution. If >50% of steps are 'mixed,' we pre-commit to soft-label regression on a continuous evidence-gap score. Key novelty vs. existing methods: (1) counterfactual causal labels rather than observational correctness (Probing-RAG), RL reward shaping (IG-Search, TIPS, DeepControl), or explicit token-guided generation ('Disentangling Memory and Reasoning'), (2) failure-mode classification (evidence gap vs. reasoning difficulty) rather than binary correctness detection ('Where Does Reasoning Break?'), knowledge conflict detection (ProbeRAG/CLEAR), or hallucination taxonomy (PRISM), (3) post-hoc inference-time applicability without retraining. Evaluation on HotpotQA, MuSiQue, and 2WikiMultiHopQA with baselines: no-retrieval, always-retrieve, Probing-RAG-style observational probe (critical ablation with pre-committed thresholds), and FLARE threshold. Infrastructure setup front-loaded to Day 0-1 with sanity check. Scoped as a short paper (~24-45 H100h total); RL integration deferred to follow-up.",
  "project_name": "evid_reason_disentangle",
  "source": "web_research"
}

## Reviewer feedback (round 5)
Issues: ["MINOR: ProbeRAG/CLEAR venue claim is unverifiable. The proposal states 'ACL 2026 Findings, arXiv 2510.12460' but the paper was submitted to ICLR 2026 (OpenReview ID NhO6iEUISf) and subsequently withdrawn. It does not appear in the ACL Anthology for 2026 Findings. Either verify the venue or cite it as a preprint only.", "MINOR: Missing related work — KRUX (arXiv 2508.19202, 'Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning') probes the knowledge-vs-reasoning bottleneck in LLMs by injecting Knowledge Ingredients (KIs) in-context and measuring performance delta. While black-box and purely diagnostic (not a competitor), it validates the knowledge-vs-reasoning separation axis and should be cited alongside 'Disentangling Memory and Reasoning' and 'Knowledge or Reasoning?' as converging evidence.", "MINOR: Potential naming confusion — 'Counterfactual Probing for Hallucination Detection and Mitigation in Large Language Models' (arXiv 2508.01862) uses 'counterfactual probing' in its title but means probing with counterfactual statements, not probing hidden states after counterfactual branching. Since the proposal uses 'counterfactual probing' prominently, consider citing this paper to explicitly differentiate the two meanings, or refine the terminology (e.g., 'counterfactual-branching probe' or 'fork-and-probe').", "MINOR: Impact framing could be stronger. The failure-mode distribution finding is positioned as a first-class contribution, but the paper doesn't articulate what design principles it would inform beyond 'retrieve less when reasoning is the bottleneck.' Spell out: if 70% of multi-hop steps are evidence-gap, what does that concretely change about how the field should build adaptive retrieval systems? If the distribution varies dramatically by dataset or question difficulty, what are the implications for per-query adaptive strategies?"]
Feedback: The proposal has improved dramatically over four rounds and is close to passing. The core novelty is verified — no existing work does counterfactual failure-mode probing for retrieval gating. The main blocker is the impact score (3/5), which drags the average to 3.75. Specific fixes to cross the threshold:

1. **Fix ProbeRAG/CLEAR venue claim**: I found it was withdrawn from ICLR 2026 and cannot confirm ACL 2026 Findings acceptance. Either provide evidence of the ACL 2026 Findings acceptance or cite it as 'arXiv 2510.12460' only. This is a reference accuracy issue that reviewers will check.

2. **Add KRUX citation**: KRUX (arXiv 2508.19202) separates knowledge from reasoning via controlled KI injection in scientific tasks. It validates the same axis your probe targets, providing additional converging evidence. Cite it briefly in the opportunity section alongside 'Disentangling Memory and Reasoning.'

3. **Disambiguate 'counterfactual probing'**: arXiv 2508.01862 uses this exact phrase for a different technique. Either cite it to differentiate or slightly adjust your terminology.

4. **Strengthen impact framing**: The failure-mode distribution is your most robust contribution (it's informative regardless of gating results). Push harder on WHY it matters:
   - If multi-hop factual QA shows predominantly evidence gaps (vs. commonsense QA's 78-98% reasoning errors), this directly challenges the assumption that reasoning-side improvements alone can solve multi-hop QA.
   - The distribution variance across datasets (HotpotQA vs. MuSiQue vs. 2WikiMultiHopQA) could reveal that different benchmarks have fundamentally different bottleneck structures, with implications for benchmark selection in future adaptive retrieval work.
   - Frame the gating experiment as a proof-of-concept that validates the distribution's actionability, not as the primary contribution.

5. **Consider adding one generalizability signal**: Even within the 11-day scope, extracting hidden states from a second checkpoint (e.g., the Qwen2.5-3B Search-R1 checkpoint, which is also publicly available) and checking whether the probe's failure-mode distribution is consistent across model sizes would substantially strengthen the paper's generalizability claim. This adds ~2-3 H100h (well within budget) and addresses the single-checkpoint limitation.

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
这个 idea 已经经过 5 轮修订，近 3 轮的平均分从 4.0 到 3.8，没有明显改善。

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
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "87a1ea26-cad3-4870-af7b-9058cfa5e7b9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T16:44:52.267Z_

```json
{
  "parentUuid": "87a1ea26-cad3-4870-af7b-9058cfa5e7b9",
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
  "uuid": "c809440a-a88b-4fa5-8728-11165915ca98",
  "timestamp": "2026-05-14T16:44:52.267Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T16:44:52.267Z_

```json
{
  "parentUuid": "c809440a-a88b-4fa5-8728-11165915ca98",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "dd1cf8cb-6516-45c1-a73f-c53f9f7b12e2",
  "timestamp": "2026-05-14T16:44:52.267Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Counterfactual Probing Disentangles Evidence Gaps from Reasoning Diffi…",
  "leafUuid": "dd1cf8cb-6516-45c1-a73f-c53f9f7b12e2",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Counterfactual step-level failure-mode classification for retrieval gating",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Assistant

_source line 8 · 2026-05-14T16:45:05.355Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully before making any changes. The reviewer says the proposal is "close to passing" with the main blocker being the impact score (3/5). The issues are all MINOR, and the feedback is specific and actionable. Let me think about whether this needs a minor fix, major revision, or pivot.

The reviewer's feedback:
1. Fix ProbeRAG/CLEAR venue claim - reference accuracy issue
2. Add KRUX citation - missing related work
3. Disambiguate 'counterfactual probing' terminology
4. Strengthen impact framing - the main blocker


5. Consider adding a second checkpoint for generalizability

The score trajectory shows a slight decline from 4.0 to 3.8 over three rounds, but the reviewer's explicit "close to passing" assessment combined with the specificity of these fixes suggests targeted revisions could push this over. The core novelty is solid, so I need to focus on the impact framing as the critical lever, while also verifying the venue claims and filling in the missing citations and terminology clarifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd1cf8cb-6516-45c1-a73f-c53f9f7b12e2",
  "isSidechain": false,
  "requestId": "req_011Cb2oGLwa6snQxR6DBeC5P",
  "type": "assistant",
  "uuid": "f2f4590b-d0c9-45dd-bd4f-bcee573a8cf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ffvf46LNqczRB7PuUMhL1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15868,
      "cache_read_input_tokens": 11841,
      "output_tokens": 440,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15868,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 440,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15868,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15868
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

_source line 9 · 2026-05-14T16:45:05.384Z_

I'll research each reviewer issue systematically before revising. Let me start with parallel searches for the key items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2f4590b-d0c9-45dd-bd4f-bcee573a8cf2",
  "isSidechain": false,
  "requestId": "req_011Cb2oGLwa6snQxR6DBeC5P",
  "type": "assistant",
  "uuid": "2436e2c6-6193-4fb4-90a5-dea6d3f639c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ffvf46LNqczRB7PuUMhL1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15868,
      "cache_read_input_tokens": 11841,
      "output_tokens": 440,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15868,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 440,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15868,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15868
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

_source line 10 · 2026-05-14T16:45:05.492Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0159k2yvMk4UaxUdTJFzQ3TW`</summary>

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
  "parentUuid": "2436e2c6-6193-4fb4-90a5-dea6d3f639c9",
  "isSidechain": false,
  "requestId": "req_011Cb2oGLwa6snQxR6DBeC5P",
  "type": "assistant",
  "uuid": "d1763448-3581-4a7c-9cb8-2f3b81aac2be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ffvf46LNqczRB7PuUMhL1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15868,
      "cache_read_input_tokens": 11841,
      "output_tokens": 440,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15868,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 440,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15868,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15868
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

_source line 11 · 2026-05-14T16:45:05.504Z_

<details><summary>↩ Tool result · `toolu_0159k2yvMk4UaxUdTJFzQ3TW`</summary>

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
  "parentUuid": "d1763448-3581-4a7c-9cb8-2f3b81aac2be",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "b1a7bb06-38c8-4cf9-bb1d-27d55db00c26",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "d1763448-3581-4a7c-9cb8-2f3b81aac2be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-14T16:45:08.273Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now run parallel searches for all the key items the reviewer flagged.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1a7bb06-38c8-4cf9-bb1d-27d55db00c26",
  "isSidechain": false,
  "requestId": "req_011Cb2oHKbF2KmnQwJC798dd",
  "type": "assistant",
  "uuid": "0ca2bc5d-2916-4694-b8d1-746e76349826",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012LHfqqfjXnim8zL9FDhruu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 27709,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1460,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 27709,
          "cache_creation_input_tokens": 1460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1460
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

_source line 13 · 2026-05-14T16:45:08.975Z_

Starting research on all reviewer issues in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ca2bc5d-2916-4694-b8d1-746e76349826",
  "isSidechain": false,
  "requestId": "req_011Cb2oHKbF2KmnQwJC798dd",
  "type": "assistant",
  "uuid": "4fac9a80-38c2-4dc4-8f97-b52785b490f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012LHfqqfjXnim8zL9FDhruu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 27709,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1460,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 27709,
          "cache_creation_input_tokens": 1460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1460
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

_source line 14 · 2026-05-14T16:45:09.249Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H4dYEBwWXqPnifMPLf5mTD`</summary>

```json
{
  "query": "ProbeRAG CLEAR arXiv 2510.12460 venue ACL 2026 ICLR 2026 withdrawn"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fac9a80-38c2-4dc4-8f97-b52785b490f3",
  "isSidechain": false,
  "requestId": "req_011Cb2oHKbF2KmnQwJC798dd",
  "type": "assistant",
  "uuid": "69d097bd-f632-466c-aa1b-b4aed8b58d7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012LHfqqfjXnim8zL9FDhruu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 27709,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1460,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 27709,
          "cache_creation_input_tokens": 1460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1460
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

_source line 15 · 2026-05-14T16:45:15.650Z_

<details><summary>↩ Tool result · `toolu_01H4dYEBwWXqPnifMPLf5mTD`</summary>

```text
Web search results for query: "ProbeRAG CLEAR arXiv 2510.12460 venue ACL 2026 ICLR 2026 withdrawn"

Links: [{"title":"Beyond Black-Box Interventions: Latent Probing for Faithful Retrieval-Augmented Generation","url":"https://arxiv.org/html/2510.12460"},{"title":"[2510.12460] Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2510.12460"},{"title":"Multi-Stream LLMs: Unblocking Language Models with Parallel Streams of Thoughts, Inputs and Outputs","url":"https://arxiv.org/html/2605.12460"},{"title":"GitHub - google-research/arxiv-latex-cleaner: arXiv LaTeX Cleaner: Easily clean the LaTeX code of your paper to submit to arXiv · GitHub","url":"https://github.com/google-research/arxiv-latex-cleaner"},{"title":"[2509.12460] Computational design of intrinsically disordered proteins","url":"https://arxiv.org/abs/2509.12460"},{"title":"Binarization-Aware Adjuster: Bridging Continuous Optimization and Binary Inference in Edge Detection","url":"https://arxiv.org/html/2506.12460"},{"title":"[2502.12460] LMN: A Tool for Generating Machine Enforceable Policies from Natural Language Access Control Rules using LLMs","url":"https://arxiv.org/abs/2502.12460"},{"title":"[2510.04160] CLEAR: A Closed-Form Minimal-Sensor TDOA/FDOA Estimator for Moving-Source IoT Localization","url":"https://arxiv.org/abs/2510.04160"},{"title":"Cosmological Simulation with Population III Stellar Feedback and Metal Enrichment I: Model Description And Convergence Test","url":"https://arxiv.org/html/2602.12460"},{"title":"[2605.12460] Multi-Stream LLMs: Unblocking Language Models with Parallel Streams of Thoughts, Inputs and Outputs","url":"https://arxiv.org/abs/2605.12460"}]

Based on the search results, I found information about the paper with arXiv ID 2510.12460:

The paper is titled "Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation". The paper appears to have two related names for its proposed framework - the search results show references to both "ProbeRAG" and "CLEAR (Conflict-Localized and Enhanced Attention for RAG)".

CLEAR is described as a framework that (i) decomposes context into fine-grained sentence-level knowledge, (ii) employs hidden-state probing to localize conflicting knowledge, and (iii) introduces conflict-aware fine-tuning to guide the model to accurately integrate retrieved evidence. Experiments across three benchmarks demonstrate that CLEAR substantially improves both accuracy and contextual faithfulness, consistently outperforming strong baselines under diverse conflict conditions.

However, the search results do not contain specific information about the paper's submission status to ACL 2026, ICLR 2026, or whether it has been withdrawn from any venues. To find that information, you may need to check the paper's submission history on OpenReview.net or contact the authors directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69d097bd-f632-466c-aa1b-b4aed8b58d7f",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "3b7ee095-88ac-4c90-bdc9-c38827002a23",
  "toolUseResult": {
    "query": "ProbeRAG CLEAR arXiv 2510.12460 venue ACL 2026 ICLR 2026 withdrawn",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FCPJHX2e4etVc1NHD8AK3h",
        "content": [
          {
            "title": "Beyond Black-Box Interventions: Latent Probing for Faithful Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2510.12460"
          },
          {
            "title": "[2510.12460] Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2510.12460"
          },
          {
            "title": "Multi-Stream LLMs: Unblocking Language Models with Parallel Streams of Thoughts, Inputs and Outputs",
            "url": "https://arxiv.org/html/2605.12460"
          },
          {
            "title": "GitHub - google-research/arxiv-latex-cleaner: arXiv LaTeX Cleaner: Easily clean the LaTeX code of your paper to submit to arXiv · GitHub",
            "url": "https://github.com/google-research/arxiv-latex-cleaner"
          },
          {
            "title": "[2509.12460] Computational design of intrinsically disordered proteins",
            "url": "https://arxiv.org/abs/2509.12460"
          },
          {
            "title": "Binarization-Aware Adjuster: Bridging Continuous Optimization and Binary Inference in Edge Detection",
            "url": "https://arxiv.org/html/2506.12460"
          },
          {
            "title": "[2502.12460] LMN: A Tool for Generating Machine Enforceable Policies from Natural Language Access Control Rules using LLMs",
            "url": "https://arxiv.org/abs/2502.12460"
          },
          {
            "title": "[2510.04160] CLEAR: A Closed-Form Minimal-Sensor TDOA/FDOA Estimator for Moving-Source IoT Localization",
            "url": "https://arxiv.org/abs/2510.04160"
          },
          {
            "title": "Cosmological Simulation with Population III Stellar Feedback and Metal Enrichment I: Model Description And Convergence Test",
            "url": "https://arxiv.org/html/2602.12460"
          },
          {
            "title": "[2605.12460] Multi-Stream LLMs: Unblocking Language Models with Parallel Streams of Thoughts, Inputs and Outputs",
            "url": "https://arxiv.org/abs/2605.12460"
          }
        ]
      },
      "Based on the search results, I found information about the paper with arXiv ID 2510.12460:\n\nThe paper is titled \"Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation\". The paper appears to have two related names for its proposed framework - the search results show references to both \"ProbeRAG\" and \"CLEAR (Conflict-Localized and Enhanced Attention for RAG)\".\n\nCLEAR is described as a framework that (i) decomposes context into fine-grained sentence-level knowledge, (ii) employs hidden-state probing to localize conflicting knowledge, and (iii) introduces conflict-aware fine-tuning to guide the model to accurately integrate retrieved evidence. Experiments across three benchmarks demonstrate that CLEAR substantially improves both accuracy and contextual faithfulness, consistently outperforming strong baselines under diverse conflict conditions.\n\nHowever, the search results do not contain specific information about the paper's submission status to ACL 2026, ICLR 2026, or whether it has been withdrawn from any venues. To find that information, you may need to check the paper's submission history on OpenReview.net or contact the authors directly."
    ],
    "durationSeconds": 6.395976922000002
  },
  "sourceToolAssistantUUID": "69d097bd-f632-466c-aa1b-b4aed8b58d7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T16:45:18.729Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YSgSn3iQUFpmB5buFjCwkY`</summary>

```json
{
  "query": "KRUX arXiv 2508.19202 \"Demystifying Scientific Problem-Solving\" probing knowledge reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b7ee095-88ac-4c90-bdc9-c38827002a23",
  "isSidechain": false,
  "requestId": "req_011Cb2oJ4mnmzjXitiTUnpzN",
  "type": "assistant",
  "uuid": "ceba43b4-a5c4-47b4-9e98-164d5e9d8f15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMN1WRAMr4QxxJDGyjbbj9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 979,
      "cache_read_input_tokens": 29169,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 979,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 29169,
          "cache_creation_input_tokens": 979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 979
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

_source line 17 · 2026-05-14T16:45:27.216Z_

<details><summary>↩ Tool result · `toolu_01YSgSn3iQUFpmB5buFjCwkY`</summary>

```text
Web search results for query: "KRUX arXiv 2508.19202 "Demystifying Scientific Problem-Solving" probing knowledge reasoning"

Links: [{"title":"[2508.19202] Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning","url":"https://arxiv.org/abs/2508.19202"},{"title":"Demystifying Scientific Problem-Solving in LLMs by ...","url":"https://arxiv.org/pdf/2508.19202"},{"title":"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning","url":"https://arxiv.org/html/2508.19202"},{"title":"Paper page - Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning","url":"https://huggingface.co/papers/2508.19202"},{"title":"Demystifying Scientific Problem-Solving in LLMs by ...","url":"https://www.alphaxiv.org/abs/2508.19202"},{"title":"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning","url":"https://www.researchgate.net/publication/394978757_Demystifying_Scientific_Problem-Solving_in_LLMs_by_Probing_Knowledge_and_Reasoning"},{"title":"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning - Paper Details","url":"https://www.chatpaper.ai/dashboard/paper/3fe2e09a-65f7-4cf6-8cf5-db2a2f43fc25"},{"title":"Demystifying Scientific Problem-Solving in LLMs by Probing ...","url":"https://openreview.net/pdf?id=B8a3UW5VHf"},{"title":"DEMYSTIFYING SCIENTIFIC PROBLEM-SOLVING IN LLMS BY ...","url":"https://openreview.net/pdf/f153e37d4d00dd5a399f4b0f4757c352b93fb965.pdf"},{"title":"Demystifying Scientific Problem-Solving in LLMs ...","url":"https://deeplearn.org/arxiv/632302/demystifying-scientific-problem-solving-in-llms-by-probing-knowledge-and-reasoning"}]

I've successfully found comprehensive information about the paper. Here's what I found:

## Paper Summary

The paper is titled "Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning" (arXiv:2508.19202).

### Main Contributions

The paper addresses scientific problem solving, which poses unique challenges for LLMs, requiring both deep domain knowledge and the ability to apply such knowledge through complex reasoning. While automated scientific reasoners hold great promise for assisting human scientists, there is currently no widely adopted holistic benchmark for evaluating scientific reasoning, and few approaches systematically disentangle the distinct roles of knowledge and reasoning in these tasks.

### Key Datasets and Framework

The researchers introduce SciReas, a diverse suite of existing benchmarks for scientific reasoning tasks, and SciReas-Pro, a selective subset that requires more complex reasoning.

They propose KRUX, a probing framework for studying the distinct roles of reasoning and knowledge in scientific tasks.

### Key Findings

The in-depth analysis yields three key findings: (1) Retrieving task-relevant knowledge from model parameters is a critical bottleneck for LLMs in scientific reasoning; (2) Reasoning models consistently benefit from external knowledge added in-context on top of the reasoning enhancement; (3) Enhancing verbalized reasoning improves LLMs' ability to surface task-relevant knowledge.

### Authors and Details

The paper was submitted on August 26, 2025 (v1) and last revised on January 19, 2026 (v2), with authors Alan Li, Yixin Liu, Arpan Sarkar, Doug Downey, and Arman Cohan.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ceba43b4-a5c4-47b4-9e98-164d5e9d8f15",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "a2e44f16-ecf7-437e-886a-e060f240653b",
  "toolUseResult": {
    "query": "KRUX arXiv 2508.19202 \"Demystifying Scientific Problem-Solving\" probing knowledge reasoning",
    "results": [
      {
        "tool_use_id": "srvtoolu_0158CT8TPzuzXdiMTyuposXr",
        "content": [
          {
            "title": "[2508.19202] Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning",
            "url": "https://arxiv.org/abs/2508.19202"
          },
          {
            "title": "Demystifying Scientific Problem-Solving in LLMs by ...",
            "url": "https://arxiv.org/pdf/2508.19202"
          },
          {
            "title": "Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning",
            "url": "https://arxiv.org/html/2508.19202"
          },
          {
            "title": "Paper page - Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning",
            "url": "https://huggingface.co/papers/2508.19202"
          },
          {
            "title": "Demystifying Scientific Problem-Solving in LLMs by ...",
            "url": "https://www.alphaxiv.org/abs/2508.19202"
          },
          {
            "title": "Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning",
            "url": "https://www.researchgate.net/publication/394978757_Demystifying_Scientific_Problem-Solving_in_LLMs_by_Probing_Knowledge_and_Reasoning"
          },
          {
            "title": "Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning - Paper Details",
            "url": "https://www.chatpaper.ai/dashboard/paper/3fe2e09a-65f7-4cf6-8cf5-db2a2f43fc25"
          },
          {
            "title": "Demystifying Scientific Problem-Solving in LLMs by Probing ...",
            "url": "https://openreview.net/pdf?id=B8a3UW5VHf"
          },
          {
            "title": "DEMYSTIFYING SCIENTIFIC PROBLEM-SOLVING IN LLMS BY ...",
            "url": "https://openreview.net/pdf/f153e37d4d00dd5a399f4b0f4757c352b93fb965.pdf"
          },
          {
            "title": "Demystifying Scientific Problem-Solving in LLMs ...",
            "url": "https://deeplearn.org/arxiv/632302/demystifying-scientific-problem-solving-in-llms-by-probing-knowledge-and-reasoning"
          }
        ]
      },
      "I've successfully found comprehensive information about the paper. Here's what I found:\n\n## Paper Summary\n\nThe paper is titled \"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning\" (arXiv:2508.19202).\n\n### Main Contributions\n\nThe paper addresses scientific problem solving, which poses unique challenges for LLMs, requiring both deep domain knowledge and the ability to apply such knowledge through complex reasoning. While automated scientific reasoners hold great promise for assisting human scientists, there is currently no widely adopted holistic benchmark for evaluating scientific reasoning, and few approaches systematically disentangle the distinct roles of knowledge and reasoning in these tasks.\n\n### Key Datasets and Framework\n\nThe researchers introduce SciReas, a diverse suite of existing benchmarks for scientific reasoning tasks, and SciReas-Pro, a selective subset that requires more complex reasoning.\n\nThey propose KRUX, a probing framework for studying the distinct roles of reasoning and knowledge in scientific tasks.\n\n### Key Findings\n\nThe in-depth analysis yields three key findings: (1) Retrieving task-relevant knowledge from model parameters is a critical bottleneck for LLMs in scientific reasoning; (2) Reasoning models consistently benefit from external knowledge added in-context on top of the reasoning enhancement; (3) Enhancing verbalized reasoning improves LLMs' ability to surface task-relevant knowledge.\n\n### Authors and Details\n\nThe paper was submitted on August 26, 2025 (v1) and last revised on January 19, 2026 (v2), with authors Alan Li, Yixin Liu, Arpan Sarkar, Doug Downey, and Arman Cohan."
    ],
    "durationSeconds": 8.481588956000003
  },
  "sourceToolAssistantUUID": "ceba43b4-a5c4-47b4-9e98-164d5e9d8f15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T16:45:29.865Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dmmy3HggbH8jaCwDdrZ1n7`</summary>

```json
{
  "query": "arXiv 2508.01862 \"Counterfactual Probing for Hallucination Detection\" large language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2e44f16-ecf7-437e-886a-e060f240653b",
  "isSidechain": false,
  "requestId": "req_011Cb2oJvBPWptimxEE3Ct7x",
  "type": "assistant",
  "uuid": "5a042a6e-b5f5-4b24-a814-2cf088cbbeab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MXD664KdqKi5wr6B1vaD5Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1052,
      "cache_read_input_tokens": 30148,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 30148,
          "cache_creation_input_tokens": 1052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1052
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

_source line 19 · 2026-05-14T16:45:35.928Z_

<details><summary>↩ Tool result · `toolu_01Dmmy3HggbH8jaCwDdrZ1n7`</summary>

```text
Web search results for query: "arXiv 2508.01862 "Counterfactual Probing for Hallucination Detection" large language models"

Links: [{"title":"[2508.01862] Counterfactual Probing for Hallucination Detection and Mitigation in Large Language Models","url":"https://arxiv.org/abs/2508.01862"},{"title":"Counterfactual Probing for Hallucination Detection and Mitigation in Large","url":"https://arxiv.org/pdf/2508.01862"},{"title":"Counterfactual Probing for Hallucination Detection and Mitigation in Large Language Models","url":"https://arxiv.org/html/2508.01862"},{"title":"Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping","url":"https://arxiv.org/html/2601.17467"},{"title":"Analyzing and Mitigating Object Hallucination: A Training Bias Perspective","url":"https://arxiv.org/html/2508.04567"},{"title":"Principled Detection of Hallucinations in Large Language Models via Multiple Testing","url":"https://arxiv.org/html/2508.18473"},{"title":"HalCECE: A Framework for Explainable Hallucination Detection through Conceptual Counterfactuals in Image Captioning","url":"https://arxiv.org/html/2503.00436v1"},{"title":"HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/html/2603.05465v1"},{"title":"Breaking the Illusion: When Positive Meets Negative in Multimodal Decoding","url":"https://arxiv.org/html/2605.06679"},{"title":"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry","url":"https://arxiv.org/html/2605.13772"}]

Based on the search results, I found the paper you're looking for. Here's information about arXiv 2508.01862:

## Counterfactual Probing for Hallucination Detection and Mitigation in Large Language Models

The paper proposes Counterfactual Probing, a novel approach for detecting and mitigating hallucinations in LLM outputs.

**Core Methodology:**

The method dynamically generates counterfactual statements that appear plausible but contain subtle factual errors, then evaluates the model's sensitivity to these perturbations. The hypothesis is that genuine knowledge exhibits robustness to counterfactual variations, while hallucinated content shows inconsistent confidence patterns when confronted with plausible alternatives.

**Key Results:**

Comprehensive evaluation on TruthfulQA, factual statement datasets, and curated hallucination examples demonstrates that counterfactual probing achieves superior detection performance compared to baseline methods, while adaptive mitigation strategies reduce hallucination scores by an average of 24.5%.

**Practical Advantages:**

The approach requires no model retraining and can be integrated into existing LLM pipelines as a real-time verification mechanism.

**Author:** The paper was submitted on August 3, 2025, by Yijun Feng.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a042a6e-b5f5-4b24-a814-2cf088cbbeab",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "43f4922c-929e-441d-b268-a3eb23e14519",
  "toolUseResult": {
    "query": "arXiv 2508.01862 \"Counterfactual Probing for Hallucination Detection\" large language models",
    "results": [
      {
        "tool_use_id": "srvtoolu_011ut9aD8ftPjenXVTKg64kS",
        "content": [
          {
            "title": "[2508.01862] Counterfactual Probing for Hallucination Detection and Mitigation in Large Language Models",
            "url": "https://arxiv.org/abs/2508.01862"
          },
          {
            "title": "Counterfactual Probing for Hallucination Detection and Mitigation in Large",
            "url": "https://arxiv.org/pdf/2508.01862"
          },
          {
            "title": "Counterfactual Probing for Hallucination Detection and Mitigation in Large Language Models",
            "url": "https://arxiv.org/html/2508.01862"
          },
          {
            "title": "Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping",
            "url": "https://arxiv.org/html/2601.17467"
          },
          {
            "title": "Analyzing and Mitigating Object Hallucination: A Training Bias Perspective",
            "url": "https://arxiv.org/html/2508.04567"
          },
          {
            "title": "Principled Detection of Hallucinations in Large Language Models via Multiple Testing",
            "url": "https://arxiv.org/html/2508.18473"
          },
          {
            "title": "HalCECE: A Framework for Explainable Hallucination Detection through Conceptual Counterfactuals in Image Captioning",
            "url": "https://arxiv.org/html/2503.00436v1"
          },
          {
            "title": "HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token",
            "url": "https://arxiv.org/html/2603.05465v1"
          },
          {
            "title": "Breaking the Illusion: When Positive Meets Negative in Multimodal Decoding",
            "url": "https://arxiv.org/html/2605.06679"
          },
          {
            "title": "Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry",
            "url": "https://arxiv.org/html/2605.13772"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's information about arXiv 2508.01862:\n\n## Counterfactual Probing for Hallucination Detection and Mitigation in Large Language Models\n\nThe paper proposes Counterfactual Probing, a novel approach for detecting and mitigating hallucinations in LLM outputs.\n\n**Core Methodology:**\n\nThe method dynamically generates counterfactual statements that appear plausible but contain subtle factual errors, then evaluates the model's sensitivity to these perturbations. The hypothesis is that genuine knowledge exhibits robustness to counterfactual variations, while hallucinated content shows inconsistent confidence patterns when confronted with plausible alternatives.\n\n**Key Results:**\n\nComprehensive evaluation on TruthfulQA, factual statement datasets, and curated hallucination examples demonstrates that counterfactual probing achieves superior detection performance compared to baseline methods, while adaptive mitigation strategies reduce hallucination scores by an average of 24.5%.\n\n**Practical Advantages:**\n\nThe approach requires no model retraining and can be integrated into existing LLM pipelines as a real-time verification mechanism.\n\n**Author:** The paper was submitted on August 3, 2025, by Yijun Feng."
    ],
    "durationSeconds": 6.05155197
  },
  "sourceToolAssistantUUID": "5a042a6e-b5f5-4b24-a814-2cf088cbbeab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Counterfactual Probing Disentangles Evidence Gaps from Reasoning Diffi…",
  "leafUuid": "43f4922c-929e-441d-b268-a3eb23e14519",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Counterfactual step-level failure-mode classification for retrieval gating",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Tool call

_source line 22 · 2026-05-14T16:45:38.505Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016nYeBfUjTgVfJTPhaS6tXK`</summary>

```json
{
  "query": "Search-R1 Qwen2.5-3B checkpoint publicly available GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43f4922c-929e-441d-b268-a3eb23e14519",
  "isSidechain": false,
  "requestId": "req_011Cb2oKZYSEWGHS9xUC5xDB",
  "type": "assistant",
  "uuid": "459c31cc-837d-4e6f-9386-bdfbd2fa9d90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MuF5kYcqQbgozGMVGn5ZQy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 31200,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 885,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 31200,
          "cache_creation_input_tokens": 885,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 885
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

_source line 23 · 2026-05-14T16:45:45.658Z_

<details><summary>↩ Tool result · `toolu_016nYeBfUjTgVfJTPhaS6tXK`</summary>

```text
Web search results for query: "Search-R1 Qwen2.5-3B checkpoint publicly available GitHub"

Links: [{"title":"GitHub - jklj077/Qwen2.5: Qwen2.5 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/jklj077/Qwen2.5"},{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen3"},{"title":"deep-learning-pytorch-huggingface/training/receipes/grpo-qwen-2.5-3b-deepseek-r1-countdown.yaml at main · philschmid/deep-learning-pytorch-huggingface","url":"https://github.com/philschmid/deep-learning-pytorch-huggingface/blob/main/training/receipes/grpo-qwen-2.5-3b-deepseek-r1-countdown.yaml"},{"title":"GitHub - deepseek-ai/DeepSeek-R1 · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-R1"},{"title":"GitHub - QwenLM/Qwen3-Coder: Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team. · GitHub","url":"https://github.com/QwenLM/Qwen3-Coder"},{"title":"GitHub - PeterGriffinJin/Search-R1: Search-R1: An Efficient, Scalable RL Training Framework for Reasoning & Search Engine Calling interleaved LLM based on veRL · GitHub","url":"https://github.com/PeterGriffinJin/Search-R1"},{"title":"GitHub - QwenLM/Qwen2.5-Omni: Qwen2.5-Omni is an end-to-end multimodal model by Qwen team at Alibaba Cloud, capable of understanding text, audio, vision, video, and performing real-time speech generation. · GitHub","url":"https://github.com/QwenLM/Qwen2.5-Omni"},{"title":"Qwen2.5: A Party of Foundation Models! | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5/"},{"title":"GitHub - huggingface/open-r1: Fully open reproduction of DeepSeek-R1 · GitHub","url":"https://github.com/huggingface/open-r1"},{"title":"GitHub - QwenLM/Qwen2.5-Math: A series of math-specific large language models of our Qwen2 series. · GitHub","url":"https://github.com/QwenLM/Qwen2.5-Math"}]

Based on the search results, I found information about Search-R1 and Qwen2.5 models:

## Search-R1 Overview

Search-R1 is an RL training framework that supports different RL methods (e.g., PPO, GRPO, reinforce), different LLMs (e.g., llama3, Qwen2.5, etc) and different search engines (e.g., local sparse/dense retrievers and online search engines).

## Qwen2.5-3B Availability

Regarding the Qwen2.5-3B checkpoint, checkpoints with names starting with Qwen2.5- can be found on Hugging Face or ModelScope organizations.

## Model and Data References

According to the Search-R1 GitHub repository, model and data are available through provided links.

The Search-R1 project GitHub repository is available at: https://github.com/PeterGriffinJin/Search-R1

For accessing Qwen2.5-3B models, you can visit the Hugging Face or ModelScope organizations directly, where the Qwen2.5 checkpoints are publicly available for download and use.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "459c31cc-837d-4e6f-9386-bdfbd2fa9d90",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "5c034c1a-a73a-4676-b2f1-39d7d43690c1",
  "toolUseResult": {
    "query": "Search-R1 Qwen2.5-3B checkpoint publicly available GitHub",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VTMojDhWRrVMzCgTpAFTws",
        "content": [
          {
            "title": "GitHub - jklj077/Qwen2.5: Qwen2.5 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub",
            "url": "https://github.com/jklj077/Qwen2.5"
          },
          {
            "title": "GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub",
            "url": "https://github.com/QwenLM/Qwen3"
          },
          {
            "title": "deep-learning-pytorch-huggingface/training/receipes/grpo-qwen-2.5-3b-deepseek-r1-countdown.yaml at main · philschmid/deep-learning-pytorch-huggingface",
            "url": "https://github.com/philschmid/deep-learning-pytorch-huggingface/blob/main/training/receipes/grpo-qwen-2.5-3b-deepseek-r1-countdown.yaml"
          },
          {
            "title": "GitHub - deepseek-ai/DeepSeek-R1 · GitHub",
            "url": "https://github.com/deepseek-ai/DeepSeek-R1"
          },
          {
            "title": "GitHub - QwenLM/Qwen3-Coder: Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team. · GitHub",
            "url": "https://github.com/QwenLM/Qwen3-Coder"
          },
          {
            "title": "GitHub - PeterGriffinJin/Search-R1: Search-R1: An Efficient, Scalable RL Training Framework for Reasoning & Search Engine Calling interleaved LLM based on veRL · GitHub",
            "url": "https://github.com/PeterGriffinJin/Search-R1"
          },
          {
            "title": "GitHub - QwenLM/Qwen2.5-Omni: Qwen2.5-Omni is an end-to-end multimodal model by Qwen team at Alibaba Cloud, capable of understanding text, audio, vision, video, and performing real-time speech generation. · GitHub",
            "url": "https://github.com/QwenLM/Qwen2.5-Omni"
          },
          {
            "title": "Qwen2.5: A Party of Foundation Models! | Qwen",
            "url": "https://qwenlm.github.io/blog/qwen2.5/"
          },
          {
            "title": "GitHub - huggingface/open-r1: Fully open reproduction of DeepSeek-R1 · GitHub",
            "url": "https://github.com/huggingface/open-r1"
          },
          {
            "title": "GitHub - QwenLM/Qwen2.5-Math: A series of math-specific large language models of our Qwen2 series. · GitHub",
            "url": "https://github.com/QwenLM/Qwen2.5-Math"
          }
        ]
      },
      "Based on the search results, I found information about Search-R1 and Qwen2.5 models:\n\n## Search-R1 Overview\n\nSearch-R1 is an RL training framework that supports different RL methods (e.g., PPO, GRPO, reinforce), different LLMs (e.g., llama3, Qwen2.5, etc) and different search engines (e.g., local sparse/dense retrievers and online search engines).\n\n## Qwen2.5-3B Availability\n\nRegarding the Qwen2.5-3B checkpoint, checkpoints with names starting with Qwen2.5- can be found on Hugging Face or ModelScope organizations.\n\n## Model and Data References\n\nAccording to the Search-R1 GitHub repository, model and data are available through provided links.\n\nThe Search-R1 project GitHub repository is available at: https://github.com/PeterGriffinJin/Search-R1\n\nFor accessing Qwen2.5-3B models, you can visit the Hugging Face or ModelScope organizations directly, where the Qwen2.5 checkpoints are publicly available for download and use."
    ],
    "durationSeconds": 7.146562000999999
  },
  "sourceToolAssistantUUID": "459c31cc-837d-4e6f-9386-bdfbd2fa9d90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T16:45:50.178Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01K7qaa9r1CTREUfG4P5ZTVV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.12460",
  "prompt": "What is the venue/publication status of this paper? Is it published at any conference (ACL, ICLR, EMNLP, etc.)? Look for any mention of conference acceptance, proceedings, or publication venue. Also check the submission/revision dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c034c1a-a73a-4676-b2f1-39d7d43690c1",
  "isSidechain": false,
  "requestId": "req_011Cb2oLH3Xth9wLNnJhbeSh",
  "type": "assistant",
  "uuid": "a36eb520-e74b-4a95-81f4-2654faa8f205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WC34CSx3FsvtHQJA3UMYum",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 32085,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1099,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 32085,
          "cache_creation_input_tokens": 1099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1099
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

_source line 25 · 2026-05-14T16:45:53.022Z_

<details><summary>↩ Tool result · `toolu_01K7qaa9r1CTREUfG4P5ZTVV`</summary>

```text
# Publication Status

Based on the webpage content, this paper has been accepted to **ACL 2026 Findings**. 

The submission history shows the paper was initially submitted on October 14, 2025, with subsequent revisions in April 2026. The comments section explicitly states: "ACL 2026 Findings; Code is available at [this https URL](https://github.com/LinfengGao/ProbeRAG)"

This indicates the work will appear in the findings track of the 2026 Association for Computational Linguistics conference, which is a prestigious venue in the field of computational linguistics and NLP.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a36eb520-e74b-4a95-81f4-2654faa8f205",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "30a20542-ba33-4d24-8fd3-91ec5277cda4",
  "toolUseResult": {
    "bytes": 49003,
    "code": 200,
    "codeText": "OK",
    "result": "# Publication Status\n\nBased on the webpage content, this paper has been accepted to **ACL 2026 Findings**. \n\nThe submission history shows the paper was initially submitted on October 14, 2025, with subsequent revisions in April 2026. The comments section explicitly states: \"ACL 2026 Findings; Code is available at [this https URL](https://github.com/LinfengGao/ProbeRAG)\"\n\nThis indicates the work will appear in the findings track of the 2026 Association for Computational Linguistics conference, which is a prestigious venue in the field of computational linguistics and NLP.",
    "durationMs": 2840,
    "url": "https://arxiv.org/abs/2510.12460"
  },
  "sourceToolAssistantUUID": "a36eb520-e74b-4a95-81f4-2654faa8f205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T16:45:57.231Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GLNbjiFS1YvRUfgiXEVCPy`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.19202",
  "prompt": "Extract: 1) The full title, 2) The authors, 3) The core methodology (what is KRUX and how does it work - especially the Knowledge Ingredients injection approach), 4) Key findings about knowledge vs reasoning bottlenecks, 5) Any venue/publication status (conference acceptance), 6) What benchmarks were used."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30a20542-ba33-4d24-8fd3-91ec5277cda4",
  "isSidechain": false,
  "requestId": "req_011Cb2oLpVPaBsaUUcjFvjy4",
  "type": "assistant",
  "uuid": "6f882d39-92e4-481f-9194-13b0685aebb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NJBX8F8i7BJb29yQoMsU9A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 33184,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 33184,
          "cache_creation_input_tokens": 287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 287
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

_source line 27 · 2026-05-14T16:46:01.459Z_

<details><summary>↩ Tool result · `toolu_01GLNbjiFS1YvRUfgiXEVCPy`</summary>

```text
# Research Paper Summary

**1) Full Title:**
"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning"

**2) Authors:**
Alan Li, Yixin Liu, Arpan Sarkar, Doug Downey, and Arman Cohan

**3) Core Methodology:**
The researchers introduced KRUX, a probing framework designed to examine how knowledge and reasoning operate distinctly within scientific tasks. While the page provides limited implementation details, the framework enables systematic investigation of these components' separate contributions to problem-solving performance.

**4) Key Findings on Knowledge vs. Reasoning:**
- "Retrieving task-relevant knowledge from model parameters is a critical bottleneck"
- Models consistently gain advantages when external knowledge is supplied alongside reasoning enhancements
- Improved verbalized reasoning helps models access task-relevant knowledge more effectively

**5) Venue/Publication Status:**
The page does not indicate conference acceptance. The paper was submitted August 26, 2025, with a revision on January 19, 2026, suggesting it remains under review or pre-publication on arXiv.

**6) Benchmarks Used:**
The authors created SciReas (a comprehensive suite of existing scientific reasoning benchmarks) and SciReas-Pro (a more challenging subset emphasizing complex reasoning).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f882d39-92e4-481f-9194-13b0685aebb5",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "02b6170f-6504-4728-b632-2db56df0329a",
  "toolUseResult": {
    "bytes": 46783,
    "code": 200,
    "codeText": "OK",
    "result": "# Research Paper Summary\n\n**1) Full Title:**\n\"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning\"\n\n**2) Authors:**\nAlan Li, Yixin Liu, Arpan Sarkar, Doug Downey, and Arman Cohan\n\n**3) Core Methodology:**\nThe researchers introduced KRUX, a probing framework designed to examine how knowledge and reasoning operate distinctly within scientific tasks. While the page provides limited implementation details, the framework enables systematic investigation of these components' separate contributions to problem-solving performance.\n\n**4) Key Findings on Knowledge vs. Reasoning:**\n- \"Retrieving task-relevant knowledge from model parameters is a critical bottleneck\"\n- Models consistently gain advantages when external knowledge is supplied alongside reasoning enhancements\n- Improved verbalized reasoning helps models access task-relevant knowledge more effectively\n\n**5) Venue/Publication Status:**\nThe page does not indicate conference acceptance. The paper was submitted August 26, 2025, with a revision on January 19, 2026, suggesting it remains under review or pre-publication on arXiv.\n\n**6) Benchmarks Used:**\nThe authors created SciReas (a comprehensive suite of existing scientific reasoning benchmarks) and SciReas-Pro (a more challenging subset emphasizing complex reasoning).",
    "durationMs": 4225,
    "url": "https://arxiv.org/abs/2508.19202"
  },
  "sourceToolAssistantUUID": "6f882d39-92e4-481f-9194-13b0685aebb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T16:46:05.485Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NmdnHkeZZPb7mnnUuajUun`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.01862",
  "prompt": "Extract: 1) The full title, 2) What exactly does 'counterfactual probing' mean in this paper - how do they use counterfactuals? 3) Is it about hidden-state probing or something else? 4) Key methodology differences from probing hidden states after counterfactual branching. 5) Venue/publication status."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02b6170f-6504-4728-b632-2db56df0329a",
  "isSidechain": false,
  "requestId": "req_011Cb2oMSaYEpLUFBrD5Z4hd",
  "type": "assistant",
  "uuid": "af7c49c3-7eaf-4c2b-8e51-ff3ec111c19c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmNSo99s3JrB4CLPtVs3zh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 33471,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 465,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 33471,
          "cache_creation_input_tokens": 465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 465
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

_source line 29 · 2026-05-14T16:46:10.742Z_

<details><summary>↩ Tool result · `toolu_01NmdnHkeZZPb7mnnUuajUun`</summary>

```text
# Counterfactual Probing for Hallucination Detection

**1) Full Title:**
"Counterfactual Probing for Hallucination Detection and Mitigation in Large Language Models"

**2) Counterfactual Probing Methodology:**
The approach involves generating plausible but factually incorrect statements and evaluating how the model responds. According to the abstract, they "dynamically generate counterfactual statements that appear plausible but contain subtle factual errors, then evaluates the model's sensitivity to these perturbations." The underlying hypothesis is that genuine knowledge remains stable when confronted with such alternatives, while hallucinated content shows inconsistent confidence.

**3) Hidden-State Probing:**
The abstract does not discuss hidden-state probing. This method appears to focus on behavioral responses to counterfactual inputs rather than examining internal model representations.

**4) Key Methodological Distinction:**
The paper doesn't explicitly compare against hidden-state probing approaches. Its distinguishing feature is the adaptive mitigation component—it reduces hallucination scores by an average of 24.5% and operates without model retraining.

**5) Venue/Publication Status:**
This is a preprint submitted to arXiv on August 3, 2025 (identifier: arXiv:2508.01862). No traditional publication venue is listed; it remains in preprint form without conference or journal acceptance noted.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af7c49c3-7eaf-4c2b-8e51-ff3ec111c19c",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "9b815204-0823-462f-8264-dd594e88492a",
  "toolUseResult": {
    "bytes": 45203,
    "code": 200,
    "codeText": "OK",
    "result": "# Counterfactual Probing for Hallucination Detection\n\n**1) Full Title:**\n\"Counterfactual Probing for Hallucination Detection and Mitigation in Large Language Models\"\n\n**2) Counterfactual Probing Methodology:**\nThe approach involves generating plausible but factually incorrect statements and evaluating how the model responds. According to the abstract, they \"dynamically generate counterfactual statements that appear plausible but contain subtle factual errors, then evaluates the model's sensitivity to these perturbations.\" The underlying hypothesis is that genuine knowledge remains stable when confronted with such alternatives, while hallucinated content shows inconsistent confidence.\n\n**3) Hidden-State Probing:**\nThe abstract does not discuss hidden-state probing. This method appears to focus on behavioral responses to counterfactual inputs rather than examining internal model representations.\n\n**4) Key Methodological Distinction:**\nThe paper doesn't explicitly compare against hidden-state probing approaches. Its distinguishing feature is the adaptive mitigation component—it reduces hallucination scores by an average of 24.5% and operates without model retraining.\n\n**5) Venue/Publication Status:**\nThis is a preprint submitted to arXiv on August 3, 2025 (identifier: arXiv:2508.01862). No traditional publication venue is listed; it remains in preprint form without conference or journal acceptance noted.",
    "durationMs": 5254,
    "url": "https://arxiv.org/abs/2508.01862"
  },
  "sourceToolAssistantUUID": "af7c49c3-7eaf-4c2b-8e51-ff3ec111c19c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-14T16:46:10.746Z_

```json
{
  "parentUuid": "9b815204-0823-462f-8264-dd594e88492a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "0582320d-69c1-4aa6-a63d-b3763fe7bdad",
  "timestamp": "2026-05-14T16:46:10.746Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-14T16:46:14.473Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QQeUVaEcEGhBiWN3CAsb7V`</summary>

```json
{
  "query": "KRUX \"knowledge ingredients\" scientific reasoning LLMs probing framework methodology 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0582320d-69c1-4aa6-a63d-b3763fe7bdad",
  "isSidechain": false,
  "requestId": "req_011Cb2oN8GFCFMDr5qMzH1bG",
  "type": "assistant",
  "uuid": "4c67602c-89f3-4500-b10b-c48ce7c7520f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JJMK5gG4shXGhvkHQH6ixF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 33936,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 592,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 33936,
          "cache_creation_input_tokens": 592,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 592
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

_source line 32 · 2026-05-14T16:46:22.644Z_

<details><summary>↩ Tool result · `toolu_01QQeUVaEcEGhBiWN3CAsb7V`</summary>

```text
Web search results for query: "KRUX "knowledge ingredients" scientific reasoning LLMs probing framework methodology 2025 2026"

Links: [{"title":"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning","url":"https://arxiv.org/html/2508.19202v2"},{"title":"Demystifying Scientific Problem-Solving in LLMs by ...","url":"https://arxiv.org/pdf/2508.19202"},{"title":"Demystifying Scientific Problem-Solving in LLMs by Probing ...","url":"https://openreview.net/pdf?id=B8a3UW5VHf"},{"title":"[2508.19202] Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning","url":"https://arxiv.org/abs/2508.19202"},{"title":"SciReas: Scientific Reasoning Benchmark","url":"https://www.emergentmind.com/topics/scireas"},{"title":"DEMYSTIFYING SCIENTIFIC PROBLEM-SOLVING IN LLMS BY ...","url":"https://openreview.net/pdf?id=l852J55j9n"},{"title":"Paper page - Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning","url":"https://huggingface.co/papers/2508.19202"},{"title":"[Literature Review] Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning","url":"https://www.themoonlight.io/en/review/demystifying-scientific-problem-solving-in-llms-by-probing-knowledge-and-reasoning"},{"title":"Computation and Language - Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning | PaperLedge","url":"https://www.paperledge.com/e/computation-and-language-demystifying-scientific-problem-solving-in-llms-by-probing-knowledge-and-reasoning/"},{"title":"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning | OpenReview","url":"https://openreview.net/forum?id=B8a3UW5VHf"}]

## Search Results: KRUX Framework for Scientific Reasoning in LLMs

I found comprehensive information about the KRUX framework and its methodology. Here's what the research reveals:

### Framework Overview

KRUX is a novel investigative framework to study the role of knowledge and long CoT reasoning in scientific problem solving. The framework supplies models with atomic "knowledge ingredients" (KIs) extracted from other models' reasoning traces.

### Methodology

The KRUX framework operates through a systematic approach:

- The framework holds knowledge availability fixed by injecting compact, answer-agnostic knowledge ingredients (KIs) in-context.

- Knowledge Ingredient Extraction involves KRUX algorithmically identifying "knowledge ingredients" (KIs)—atomic statements of fact, definition, or principle that are answer-agnostic.

- Model performance is compared across three regimes: (i) solving with only model-internal knowledge; (ii) solving with only in-context KIs; (iii) solving with both reasoning and KIs.

### Key Findings

Gains over a no-KI baseline indicate a knowledge bottleneck, while persistent errors point to reasoning limits. 

Base models, when provided with high-quality in-context KIs, can substantially outperform their reasoning-enhanced counterparts by ≥10% across various benchmarks and model families, suggesting that internally retrieving task-relevant knowledge from model parameters is a critical bottleneck for LLMs in scientific reasoning.

### Supporting Benchmark

The research introduces SciReas, a diverse suite of existing benchmarks for scientific reasoning tasks, and SciReas-Pro, a selective subset that requires more complex reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c67602c-89f3-4500-b10b-c48ce7c7520f",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "c1aed95c-dba7-4afa-aee3-12cab15fdfa0",
  "toolUseResult": {
    "query": "KRUX \"knowledge ingredients\" scientific reasoning LLMs probing framework methodology 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01P3JF3vtCTzbjUvPmCoLGLh",
        "content": [
          {
            "title": "Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning",
            "url": "https://arxiv.org/html/2508.19202v2"
          },
          {
            "title": "Demystifying Scientific Problem-Solving in LLMs by ...",
            "url": "https://arxiv.org/pdf/2508.19202"
          },
          {
            "title": "Demystifying Scientific Problem-Solving in LLMs by Probing ...",
            "url": "https://openreview.net/pdf?id=B8a3UW5VHf"
          },
          {
            "title": "[2508.19202] Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning",
            "url": "https://arxiv.org/abs/2508.19202"
          },
          {
            "title": "SciReas: Scientific Reasoning Benchmark",
            "url": "https://www.emergentmind.com/topics/scireas"
          },
          {
            "title": "DEMYSTIFYING SCIENTIFIC PROBLEM-SOLVING IN LLMS BY ...",
            "url": "https://openreview.net/pdf?id=l852J55j9n"
          },
          {
            "title": "Paper page - Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning",
            "url": "https://huggingface.co/papers/2508.19202"
          },
          {
            "title": "[Literature Review] Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning",
            "url": "https://www.themoonlight.io/en/review/demystifying-scientific-problem-solving-in-llms-by-probing-knowledge-and-reasoning"
          },
          {
            "title": "Computation and Language - Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning | PaperLedge",
            "url": "https://www.paperledge.com/e/computation-and-language-demystifying-scientific-problem-solving-in-llms-by-probing-knowledge-and-reasoning/"
          },
          {
            "title": "Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=B8a3UW5VHf"
          }
        ]
      },
      "## Search Results: KRUX Framework for Scientific Reasoning in LLMs\n\nI found comprehensive information about the KRUX framework and its methodology. Here's what the research reveals:\n\n### Framework Overview\n\nKRUX is a novel investigative framework to study the role of knowledge and long CoT reasoning in scientific problem solving. The framework supplies models with atomic \"knowledge ingredients\" (KIs) extracted from other models' reasoning traces.\n\n### Methodology\n\nThe KRUX framework operates through a systematic approach:\n\n- The framework holds knowledge availability fixed by injecting compact, answer-agnostic knowledge ingredients (KIs) in-context.\n\n- Knowledge Ingredient Extraction involves KRUX algorithmically identifying \"knowledge ingredients\" (KIs)—atomic statements of fact, definition, or principle that are answer-agnostic.\n\n- Model performance is compared across three regimes: (i) solving with only model-internal knowledge; (ii) solving with only in-context KIs; (iii) solving with both reasoning and KIs.\n\n### Key Findings\n\nGains over a no-KI baseline indicate a knowledge bottleneck, while persistent errors point to reasoning limits. \n\nBase models, when provided with high-quality in-context KIs, can substantially outperform their reasoning-enhanced counterparts by ≥10% across various benchmarks and model families, suggesting that internally retrieving task-relevant knowledge from model parameters is a critical bottleneck for LLMs in scientific reasoning.\n\n### Supporting Benchmark\n\nThe research introduces SciReas, a diverse suite of existing benchmarks for scientific reasoning tasks, and SciReas-Pro, a selective subset that requires more complex reasoning."
    ],
    "durationSeconds": 8.16594700700001
  },
  "sourceToolAssistantUUID": "4c67602c-89f3-4500-b10b-c48ce7c7520f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T16:46:27.746Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TLyNBGpLPtvyzDnisuLVJ5`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.19202v2",
  "prompt": "Extract the key methodology details of KRUX: 1) How are Knowledge Ingredients (KIs) defined and extracted? 2) What specific experiments compare knowledge-bottleneck vs reasoning-bottleneck? 3) What are the key quantitative findings about the relative importance of knowledge vs reasoning? 4) Does the paper propose any inference-time mechanism or is it purely diagnostic? 5) Has this paper been accepted at any venue (check for any mention of conference/workshop)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1aed95c-dba7-4afa-aee3-12cab15fdfa0",
  "isSidechain": false,
  "requestId": "req_011Cb2oP1Fqyo2thBgb16Zui",
  "type": "assistant",
  "uuid": "b9c5aadb-108f-4fe7-9630-9e91488cf4a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177LN8AXLDm7namX4xMgfni",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1011,
      "cache_read_input_tokens": 34528,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1011,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 34528,
          "cache_creation_input_tokens": 1011,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1011
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

_source line 34 · 2026-05-14T16:46:34.838Z_

<details><summary>↩ Tool result · `toolu_01TLyNBGpLPtvyzDnisuLVJ5`</summary>

```text
# KRUX Methodology Analysis

## 1) Knowledge Ingredients (KIs): Definition & Extraction

**Definition:** KIs are "standalone statement[s] conveying an explicit fact, definition, mechanism, relationship, or insight that can be generalized beyond the specific question." They must be "self-contained, generalizable sentence[s]" without contextual details.

**Extraction Process:** The framework extracts KIs from reasoning traces of LLMs (typically DeepSeek-R1) using a strong reasoning model as the extractor. A carefully tuned prompt guides extraction, validated through manual inspection. Quality checks ensure KIs are: (a) task-agnostic, (b) answer-neutral, and (c) faithful to source traces.

## 2) Knowledge vs. Reasoning Bottleneck Experiments

Three research questions structure the comparison:

- **RQ1:** Base models augmented with high-quality external KIs from DeepSeek-R1 versus reasoning-fine-tuned variants
- **RQ2:** Reasoning-enhanced models receiving external KIs from DeepSeek-R1 
- **RQ3:** Whether reasoning fine-tuning improves knowledge surfacing via synthetic knowledge recall probing

## 3) Key Quantitative Findings

- Base models with KIs "outperform reasoning variants without KIs by ≥10%" across benchmarks
- Vanilla instruct models can "outperform their reasoning counterparts by ≥10% once KIs are provided"
- On GPQA: Qwen base + R1 KIs achieves 47.19% vs. Qwen-BOTH's 40.81%
- Reasoning models retain performance advantages when both receive identical KIs

## 4) Inference-Time Mechanism

KRUX is **purely diagnostic**—not an inference mechanism. It prepends extracted KIs in-context to evaluate models, functioning as an analytical framework rather than a deployed system.

## 5) Venue Acceptance

The paper header indicates **"Machine Learning, ICML"** (International Conference on Machine Learning), suggesting acceptance at ICML.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9c5aadb-108f-4fe7-9630-9e91488cf4a5",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "0843e1e5-166a-44f2-ac6f-c13ab3954412",
  "toolUseResult": {
    "bytes": 646760,
    "code": 200,
    "codeText": "OK",
    "result": "# KRUX Methodology Analysis\n\n## 1) Knowledge Ingredients (KIs): Definition & Extraction\n\n**Definition:** KIs are \"standalone statement[s] conveying an explicit fact, definition, mechanism, relationship, or insight that can be generalized beyond the specific question.\" They must be \"self-contained, generalizable sentence[s]\" without contextual details.\n\n**Extraction Process:** The framework extracts KIs from reasoning traces of LLMs (typically DeepSeek-R1) using a strong reasoning model as the extractor. A carefully tuned prompt guides extraction, validated through manual inspection. Quality checks ensure KIs are: (a) task-agnostic, (b) answer-neutral, and (c) faithful to source traces.\n\n## 2) Knowledge vs. Reasoning Bottleneck Experiments\n\nThree research questions structure the comparison:\n\n- **RQ1:** Base models augmented with high-quality external KIs from DeepSeek-R1 versus reasoning-fine-tuned variants\n- **RQ2:** Reasoning-enhanced models receiving external KIs from DeepSeek-R1 \n- **RQ3:** Whether reasoning fine-tuning improves knowledge surfacing via synthetic knowledge recall probing\n\n## 3) Key Quantitative Findings\n\n- Base models with KIs \"outperform reasoning variants without KIs by ≥10%\" across benchmarks\n- Vanilla instruct models can \"outperform their reasoning counterparts by ≥10% once KIs are provided\"\n- On GPQA: Qwen base + R1 KIs achieves 47.19% vs. Qwen-BOTH's 40.81%\n- Reasoning models retain performance advantages when both receive identical KIs\n\n## 4) Inference-Time Mechanism\n\nKRUX is **purely diagnostic**—not an inference mechanism. It prepends extracted KIs in-context to evaluate models, functioning as an analytical framework rather than a deployed system.\n\n## 5) Venue Acceptance\n\nThe paper header indicates **\"Machine Learning, ICML\"** (International Conference on Machine Learning), suggesting acceptance at ICML.",
    "durationMs": 7088,
    "url": "https://arxiv.org/html/2508.19202v2"
  },
  "sourceToolAssistantUUID": "b9c5aadb-108f-4fe7-9630-9e91488cf4a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Counterfactual Probing Disentangles Evidence Gaps from Reasoning Diffi…",
  "leafUuid": "0843e1e5-166a-44f2-ac6f-c13ab3954412",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Counterfactual step-level failure-mode classification for retrieval gating",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Tool call

_source line 37 · 2026-05-14T16:46:37.526Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tr1eiYTjMuSgeJGRzWJvdi`</summary>

```json
{
  "query": "KRUX \"Demystifying Scientific Problem-Solving\" ICML 2026 accepted venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0843e1e5-166a-44f2-ac6f-c13ab3954412",
  "isSidechain": false,
  "requestId": "req_011Cb2oPuGxND3ih1U4rPjTN",
  "type": "assistant",
  "uuid": "bb0c7499-8a35-4727-813a-e7217fc2dad5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016x2rqiuEodawuKU1is8B1i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 673,
      "cache_read_input_tokens": 35539,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 673,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 35539,
          "cache_creation_input_tokens": 673,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 673
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

_source line 38 · 2026-05-14T16:46:42.131Z_

<details><summary>↩ Tool result · `toolu_01Tr1eiYTjMuSgeJGRzWJvdi`</summary>

```text
Web search results for query: "KRUX "Demystifying Scientific Problem-Solving" ICML 2026 accepted venue"

Links: [{"title":"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning","url":"https://arxiv.org/html/2508.19202"},{"title":"[2508.19202] Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning","url":"https://arxiv.org/abs/2508.19202"},{"title":"Demystifying Scientific Problem-Solving in LLMs by ...","url":"https://arxiv.org/pdf/2508.19202"},{"title":"Paper page - Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning","url":"https://huggingface.co/papers/2508.19202"},{"title":"[Literature Review] Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning","url":"https://www.themoonlight.io/en/review/demystifying-scientific-problem-solving-in-llms-by-probing-knowledge-and-reasoning"},{"title":"Computation and Language - Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning | PaperLedge","url":"https://www.paperledge.com/e/computation-and-language-demystifying-scientific-problem-solving-in-llms-by-probing-knowledge-and-reasoning/"},{"title":"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and\\n Reasoning [논문 퀵 리뷰]","url":"https://liner.com/ko/review/demystifying-scientific-problemsolving-in-llms-by-probing-knowledge-and-reasoning"}]

Based on the search results, I found information about the paper "Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning" and the KRUX framework. However, the search results show that this is a preprint from January 21, 2026, and the results do not contain specific information about an ICML 2026 accepted venue status.

KRUX (Knowledge & Reasoning Utilization eXams) is a probing framework which supplies models with atomic "knowledge ingredients" (KIs) extracted from other models' reasoning traces. The paper appears to be available on arXiv, but the search results do not confirm whether it has been officially accepted to ICML 2026. To verify the acceptance status at ICML 2026, you may want to check the official ICML 2026 conference proceedings or acceptance list directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb0c7499-8a35-4727-813a-e7217fc2dad5",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "96045084-5508-417b-8237-892b94427615",
  "toolUseResult": {
    "query": "KRUX \"Demystifying Scientific Problem-Solving\" ICML 2026 accepted venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RUxStBQgsHTRDBEv5pLXEG",
        "content": [
          {
            "title": "Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning",
            "url": "https://arxiv.org/html/2508.19202"
          },
          {
            "title": "[2508.19202] Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning",
            "url": "https://arxiv.org/abs/2508.19202"
          },
          {
            "title": "Demystifying Scientific Problem-Solving in LLMs by ...",
            "url": "https://arxiv.org/pdf/2508.19202"
          },
          {
            "title": "Paper page - Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning",
            "url": "https://huggingface.co/papers/2508.19202"
          },
          {
            "title": "[Literature Review] Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning",
            "url": "https://www.themoonlight.io/en/review/demystifying-scientific-problem-solving-in-llms-by-probing-knowledge-and-reasoning"
          },
          {
            "title": "Computation and Language - Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning | PaperLedge",
            "url": "https://www.paperledge.com/e/computation-and-language-demystifying-scientific-problem-solving-in-llms-by-probing-knowledge-and-reasoning/"
          },
          {
            "title": "Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and\\n Reasoning [논문 퀵 리뷰]",
            "url": "https://liner.com/ko/review/demystifying-scientific-problemsolving-in-llms-by-probing-knowledge-and-reasoning"
          }
        ]
      },
      "Based on the search results, I found information about the paper \"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning\" and the KRUX framework. However, the search results show that this is a preprint from January 21, 2026, and the results do not contain specific information about an ICML 2026 accepted venue status.\n\nKRUX (Knowledge & Reasoning Utilization eXams) is a probing framework which supplies models with atomic \"knowledge ingredients\" (KIs) extracted from other models' reasoning traces. The paper appears to be available on arXiv, but the search results do not confirm whether it has been officially accepted to ICML 2026. To verify the acceptance status at ICML 2026, you may want to check the official ICML 2026 conference proceedings or acceptance list directly."
    ],
    "durationSeconds": 4.601354817999993
  },
  "sourceToolAssistantUUID": "bb0c7499-8a35-4727-813a-e7217fc2dad5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T16:46:45.060Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Nrq1dwd837Qwtno2J55uBq`</summary>

```json
{
  "query": "ProbeRAG \"ACL 2026 Findings\" \"Probing Latent Knowledge Conflict\" accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96045084-5508-417b-8237-892b94427615",
  "isSidechain": false,
  "requestId": "req_011Cb2oQSWuZ2QeJvFQf1acQ",
  "type": "assistant",
  "uuid": "e4ebde37-81c3-43a9-be5a-eadd73971130",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015onXn9ChVar2zdGnzVfmN8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 743,
      "cache_read_input_tokens": 36212,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 743,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 36212,
          "cache_creation_input_tokens": 743,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 743
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

_source line 40 · 2026-05-14T16:46:51.411Z_

<details><summary>↩ Tool result · `toolu_01Nrq1dwd837Qwtno2J55uBq`</summary>

```text
Web search results for query: "ProbeRAG "ACL 2026 Findings" "Probing Latent Knowledge Conflict" accepted"

Links: [{"title":"[2510.12460v1] Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2510.12460v1"},{"title":"Beyond Black-Box Interventions: Latent Probing for Faithful Retrieval-Augmented Generation","url":"https://arxiv.org/html/2510.12460"},{"title":"Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation | OpenReview","url":"https://openreview.net/forum?id=NhO6iEUISf"},{"title":"[2510.12460] Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2510.12460"},{"title":"PROBING LATENT KNOWLEDGE CONFLICT FOR FAITHFUL RETRIEVAL-AUGMENTED GENERATION","url":"https://arxiv.org/pdf/2510.12460"},{"title":"Findings of the Association for Computational Linguistics (2026) - ACL Anthology","url":"https://aclanthology.org/events/findings-2026/"},{"title":"(PDF) PROBING LATENT KNOWLEDGE CONFLICT FOR FAITHFUL RETRIEVAL-AUGMENTED GENERATION","url":"https://www.researchgate.net/publication/396745926_PROBING_LATENT_KNOWLEDGE_CONFLICT_FOR_FAITHFUL_RETRIEVAL-AUGMENTED_GENERATION"},{"title":"Findings - ACL 2026","url":"https://2026.aclweb.org/program/findings/"},{"title":"KnowFM Workshop @ ACL 2026 — Towards Knowledgeable Foundation Models","url":"https://knowledgeable-lm.github.io/"},{"title":"Findings of the Association for Computational Linguistics: EACL 2026 - ACL Anthology","url":"https://aclanthology.org/volumes/2026.findings-eacl/"}]

Based on the search results, I found relevant information about the paper "Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation." Here's what I discovered:

## Overview

ProbeRAG is a novel framework for faithful RAG that operates in three stages: (i) fine-grained knowledge pruning to filter irrelevant context, (ii) latent conflict probing to identify hard conflicts in the model's latent space, and (iii) conflict-aware attention to modulate attention heads toward faithful context integration.

## Key Findings

The research found that knowledge integration occurs hierarchically, conflicts manifest as latent signals at the sentence level, and irrelevant context is often amplified when aligned with parametric knowledge.

The work discovered that conflicting and aligned knowledge states are linearly separable in the model's latent space, and contextual noise systematically increases the entropy of these representations.

## Publication Status

The paper appears on arXiv with submission date October 14, 2025. However, I should note that while the search results reference ACL venues, the specific mention of an "ACL 2026 Findings" acceptance was not explicitly confirmed in the search results. The OpenReview listing shows it was submitted to ICLR 2026 but was withdrawn.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4ebde37-81c3-43a9-be5a-eadd73971130",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "33fa2c0d-67f9-4e59-8c74-3484a3533845",
  "toolUseResult": {
    "query": "ProbeRAG \"ACL 2026 Findings\" \"Probing Latent Knowledge Conflict\" accepted",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HMrJYXMXHHvT1rwRDLXCcy",
        "content": [
          {
            "title": "[2510.12460v1] Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2510.12460v1"
          },
          {
            "title": "Beyond Black-Box Interventions: Latent Probing for Faithful Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2510.12460"
          },
          {
            "title": "Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation | OpenReview",
            "url": "https://openreview.net/forum?id=NhO6iEUISf"
          },
          {
            "title": "[2510.12460] Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2510.12460"
          },
          {
            "title": "PROBING LATENT KNOWLEDGE CONFLICT FOR FAITHFUL RETRIEVAL-AUGMENTED GENERATION",
            "url": "https://arxiv.org/pdf/2510.12460"
          },
          {
            "title": "Findings of the Association for Computational Linguistics (2026) - ACL Anthology",
            "url": "https://aclanthology.org/events/findings-2026/"
          },
          {
            "title": "(PDF) PROBING LATENT KNOWLEDGE CONFLICT FOR FAITHFUL RETRIEVAL-AUGMENTED GENERATION",
            "url": "https://www.researchgate.net/publication/396745926_PROBING_LATENT_KNOWLEDGE_CONFLICT_FOR_FAITHFUL_RETRIEVAL-AUGMENTED_GENERATION"
          },
          {
            "title": "Findings - ACL 2026",
            "url": "https://2026.aclweb.org/program/findings/"
          },
          {
            "title": "KnowFM Workshop @ ACL 2026 — Towards Knowledgeable Foundation Models",
            "url": "https://knowledgeable-lm.github.io/"
          },
          {
            "title": "Findings of the Association for Computational Linguistics: EACL 2026 - ACL Anthology",
            "url": "https://aclanthology.org/volumes/2026.findings-eacl/"
          }
        ]
      },
      "Based on the search results, I found relevant information about the paper \"Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation.\" Here's what I discovered:\n\n## Overview\n\nProbeRAG is a novel framework for faithful RAG that operates in three stages: (i) fine-grained knowledge pruning to filter irrelevant context, (ii) latent conflict probing to identify hard conflicts in the model's latent space, and (iii) conflict-aware attention to modulate attention heads toward faithful context integration.\n\n## Key Findings\n\nThe research found that knowledge integration occurs hierarchically, conflicts manifest as latent signals at the sentence level, and irrelevant context is often amplified when aligned with parametric knowledge.\n\nThe work discovered that conflicting and aligned knowledge states are linearly separable in the model's latent space, and contextual noise systematically increases the entropy of these representations.\n\n## Publication Status\n\nThe paper appears on arXiv with submission date October 14, 2025. However, I should note that while the search results reference ACL venues, the specific mention of an \"ACL 2026 Findings\" acceptance was not explicitly confirmed in the search results. The OpenReview listing shows it was submitted to ICLR 2026 but was withdrawn."
    ],
    "durationSeconds": 6.347719297000003
  },
  "sourceToolAssistantUUID": "e4ebde37-81c3-43a9-be5a-eadd73971130",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T16:46:54.576Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WQR8JKTX7H983nbwf8X84x`</summary>

```json
{
  "url": "https://openreview.net/forum?id=NhO6iEUISf",
  "prompt": "What is the status of this paper submission? Was it accepted, rejected, or withdrawn? What venue was it submitted to? Any details about its review outcome."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33fa2c0d-67f9-4e59-8c74-3484a3533845",
  "isSidechain": false,
  "requestId": "req_011Cb2oR89PMaWPzLWXtF8vb",
  "type": "assistant",
  "uuid": "93bd0147-7886-48cd-acd9-74f28fa375e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRCx2GRciavRxW1Cc4uAHY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 920,
      "cache_read_input_tokens": 36955,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 36955,
          "cache_creation_input_tokens": 920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 920
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

_source line 42 · 2026-05-14T16:46:57.143Z_

<details><summary>↩ Tool result · `toolu_01WQR8JKTX7H983nbwf8X84x`</summary>

```text
# Paper Submission Status

**Venue:** ICLR 2026 Conference

**Status:** Withdrawn

The submission page indicates this is a "Withdrawn Submission" for ICLR 2026. The paper, titled "Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation," was submitted on September 20, 2025, with a modification date of November 25, 2025, but ultimately was not accepted to the conference. No specific details about the review outcome or reasons for withdrawal are provided on the page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93bd0147-7886-48cd-acd9-74f28fa375e6",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "49e35702-ee19-4c33-8d4c-5c143097b726",
  "toolUseResult": {
    "bytes": 72313,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Submission Status\n\n**Venue:** ICLR 2026 Conference\n\n**Status:** Withdrawn\n\nThe submission page indicates this is a \"Withdrawn Submission\" for ICLR 2026. The paper, titled \"Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation,\" was submitted on September 20, 2025, with a modification date of November 25, 2025, but ultimately was not accepted to the conference. No specific details about the review outcome or reasons for withdrawal are provided on the page.",
    "durationMs": 2564,
    "url": "https://openreview.net/forum?id=NhO6iEUISf"
  },
  "sourceToolAssistantUUID": "93bd0147-7886-48cd-acd9-74f28fa375e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T16:47:00.953Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011wNnjaetHgQ2D2SmNWEurm`</summary>

```json
{
  "url": "https://aclanthology.org/events/findings-2026/",
  "prompt": "Search for \"ProbeRAG\" or \"Probing Latent Knowledge Conflict\" or \"CLEAR\" in the ACL 2026 Findings proceedings. Is there any paper by Linfeng Gao or related to probing knowledge conflicts in RAG? List any matching papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49e35702-ee19-4c33-8d4c-5c143097b726",
  "isSidechain": false,
  "requestId": "req_011Cb2oRYe36FXvEduAiw5vf",
  "type": "assistant",
  "uuid": "2612ca78-52e7-46cb-a47d-3b8212fa34a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKXT4jFjLSvVx9ECVPyLa5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 254,
      "cache_read_input_tokens": 37875,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 254,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 37875,
          "cache_creation_input_tokens": 254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 254
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

_source line 44 · 2026-05-14T16:47:06.101Z_

<details><summary>↩ Tool result · `toolu_011wNnjaetHgQ2D2SmNWEurm`</summary>

```text
Based on my search through the provided ACL 2026 Findings content, I found **no papers** matching your criteria:

- No paper titled "ProbeRAG" or "Probing Latent Knowledge Conflict"
- No paper titled "CLEAR" related to knowledge conflicts in RAG
- No papers authored by Linfeng Gao

The content provided covers 355 papers from the Findings of the Association for Computational Linguistics: EACL 2026 proceedings, but none of the papers shown in this excerpt match your search parameters. To locate these specific papers, you would need to search the complete ACL Anthology database directly or access the full proceedings listing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2612ca78-52e7-46cb-a47d-3b8212fa34a5",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "23be4633-767d-435e-9edd-07d5e37fba7d",
  "toolUseResult": {
    "bytes": 1042336,
    "code": 200,
    "codeText": "OK",
    "result": "Based on my search through the provided ACL 2026 Findings content, I found **no papers** matching your criteria:\n\n- No paper titled \"ProbeRAG\" or \"Probing Latent Knowledge Conflict\"\n- No paper titled \"CLEAR\" related to knowledge conflicts in RAG\n- No papers authored by Linfeng Gao\n\nThe content provided covers 355 papers from the Findings of the Association for Computational Linguistics: EACL 2026 proceedings, but none of the papers shown in this excerpt match your search parameters. To locate these specific papers, you would need to search the complete ACL Anthology database directly or access the full proceedings listing.",
    "durationMs": 5143,
    "url": "https://aclanthology.org/events/findings-2026/"
  },
  "sourceToolAssistantUUID": "2612ca78-52e7-46cb-a47d-3b8212fa34a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-14T16:47:18.205Z_

<details><summary>Logged reasoning block</summary>

```text
Interesting - so the ACL Anthology for findings-2026 shows EACL 2026 findings, not ACL 2026 findings. ACL 2026 might not have happened yet since we're in May 2026. Let me check what date ACL 2026 is scheduled for and whether their findings have been published yet.

Wait, the arXiv page for 2510.12460 says "ACL 2026 Findings" in the comments. The WebFetch earlier confirmed that. But the reviewer says it was withdrawn from ICLR 2026 and they can't confirm ACL 2026 Findings. 

ACL 2026 is typically scheduled for July or August, so in May the papers might be accepted but not yet in the anthology. The arXiv update from April mentioning ACL 2026 Findings makes sense - authors update their preprints after acceptance, but the official anthology publication comes later.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23be4633-767d-435e-9edd-07d5e37fba7d",
  "isSidechain": false,
  "requestId": "req_011Cb2oSD2rDgBefiK5CUM8p",
  "type": "assistant",
  "uuid": "ce447be6-df2d-47d1-976e-ef25cc177078",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011M29E7vfbdZKWJodi3dbnU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 310,
      "cache_read_input_tokens": 38129,
      "output_tokens": 533,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 310,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 533,
          "cache_read_input_tokens": 38129,
          "cache_creation_input_tokens": 310,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 310
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

_source line 46 · 2026-05-14T16:47:18.466Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FjXFRUkAtN1fH5aXGYmk7h`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.12460",
  "prompt": "Look at the submission history and comments field. What does the comments field say about the venue? When was the most recent version submitted? Is there any mention of ACL 2026 Findings in the comments?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce447be6-df2d-47d1-976e-ef25cc177078",
  "isSidechain": false,
  "requestId": "req_011Cb2oSD2rDgBefiK5CUM8p",
  "type": "assistant",
  "uuid": "ba161764-beb4-4894-b18c-682ad168ff39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011M29E7vfbdZKWJodi3dbnU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 310,
      "cache_read_input_tokens": 38129,
      "output_tokens": 533,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 310,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 533,
          "cache_read_input_tokens": 38129,
          "cache_creation_input_tokens": 310,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 310
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

_source line 47 · 2026-05-14T16:47:20.768Z_

<details><summary>↩ Tool result · `toolu_01FjXFRUkAtN1fH5aXGYmk7h`</summary>

```text
# Response

**Venue Information:**
The comments field states: "ACL 2026 Findings; Code is available at [this https URL](https://github.com/LinfengGao/ProbeRAG)"

**Most Recent Submission:**
The latest version (v3) was submitted on Wednesday, April 15, 2026 at 12:28:12 UTC.

**ACL 2026 Findings Mention:**
Yes, the comments explicitly reference "ACL 2026 Findings," indicating this paper has been accepted to the Findings track of the Association for Computational Linguistics 2026 conference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba161764-beb4-4894-b18c-682ad168ff39",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "030cdb50-699f-43ca-a225-c72e644738a5",
  "toolUseResult": {
    "bytes": 49003,
    "code": 200,
    "codeText": "OK",
    "result": "# Response\n\n**Venue Information:**\nThe comments field states: \"ACL 2026 Findings; Code is available at [this https URL](https://github.com/LinfengGao/ProbeRAG)\"\n\n**Most Recent Submission:**\nThe latest version (v3) was submitted on Wednesday, April 15, 2026 at 12:28:12 UTC.\n\n**ACL 2026 Findings Mention:**\nYes, the comments explicitly reference \"ACL 2026 Findings,\" indicating this paper has been accepted to the Findings track of the Association for Computational Linguistics 2026 conference.",
    "durationMs": 2300,
    "url": "https://arxiv.org/abs/2510.12460"
  },
  "sourceToolAssistantUUID": "ba161764-beb4-4894-b18c-682ad168ff39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T16:47:23.500Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NW7KVyDc785wuPWSPCgJBP`</summary>

```json
{
  "query": "ACL 2026 conference date location schedule July August 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "030cdb50-699f-43ca-a225-c72e644738a5",
  "isSidechain": false,
  "requestId": "req_011Cb2oTHj9pi6qWGWZr4wHE",
  "type": "assistant",
  "uuid": "5c32855f-70dc-49a4-a5ac-13389d589f5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pP5cehichrfBZK3XpT8jK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 38439,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 38439,
          "cache_creation_input_tokens": 685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 685
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

_source line 49 · 2026-05-14T16:47:27.215Z_

<details><summary>↩ Tool result · `toolu_01NW7KVyDc785wuPWSPCgJBP`</summary>

```text
Web search results for query: "ACL 2026 conference date location schedule July August 2026"

Links: [{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"The 19th Conference of the European Chapter of the Association for Computational LinguisticsRabat, MoroccoMarch 24-29, 2026 -","url":"https://2026.eacl.org/"},{"title":"ACL: Meeting of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=37"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Upcoming ACL-Sponsored Events | ACL Member Portal","url":"https://www.aclweb.org/portal/acl_sponsored_events?order=field_event_date&sort=desc"},{"title":"Annual Meetings of the Association for Computational Linguistics | ACL Member Portal","url":"https://www.aclweb.org/portal/acl"},{"title":"Austin City Limits Music Festival | Oct 2-4 & 9-11, 2026 | Austin, TX","url":"https://www.aclfestival.com/"},{"title":"ACL 2026","url":"https://conferences-basecamp.informatik.uni-hamburg.de/conference/?id=acl26"},{"title":"ACL 2026 in California: Dates, Deadline, Fees & Registration Steps - Conference Inc.","url":"https://conferenceinc.net/post/acl/"}]

Based on the search results, here's the information about ACL 2026:

**Conference Details:**

The 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026) will take place in San Diego, California, from July 2 - 7, 2026.

**Venue:**

The Grand Hyatt Manchester San Diego is the official conference hotel for ACL 2026.

**Hotel Booking:**

The cutoff date for booking the special hotel room block is June 8, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c32855f-70dc-49a4-a5ac-13389d589f5f",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "98b88f6b-1bf8-4a86-87b6-4c5c515ea3e1",
  "toolUseResult": {
    "query": "ACL 2026 conference date location schedule July August 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QEovWvNYbmNwoBHXaxzjJk",
        "content": [
          {
            "title": "The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026",
            "url": "https://2026.aclweb.org/"
          },
          {
            "title": "Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/dates"
          },
          {
            "title": "The 19th Conference of the European Chapter of the Association for Computational LinguisticsRabat, MoroccoMarch 24-29, 2026 -",
            "url": "https://2026.eacl.org/"
          },
          {
            "title": "ACL: Meeting of the Association for Computational Linguistics 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=37"
          },
          {
            "title": "2026 *ACL Conference Dates | Computational Linguistics",
            "url": "https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"
          },
          {
            "title": "Upcoming ACL-Sponsored Events | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/acl_sponsored_events?order=field_event_date&sort=desc"
          },
          {
            "title": "Annual Meetings of the Association for Computational Linguistics | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/acl"
          },
          {
            "title": "Austin City Limits Music Festival | Oct 2-4 & 9-11, 2026 | Austin, TX",
            "url": "https://www.aclfestival.com/"
          },
          {
            "title": "ACL 2026",
            "url": "https://conferences-basecamp.informatik.uni-hamburg.de/conference/?id=acl26"
          },
          {
            "title": "ACL 2026 in California: Dates, Deadline, Fees & Registration Steps - Conference Inc.",
            "url": "https://conferenceinc.net/post/acl/"
          }
        ]
      },
      "Based on the search results, here's the information about ACL 2026:\n\n**Conference Details:**\n\nThe 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026) will take place in San Diego, California, from July 2 - 7, 2026.\n\n**Venue:**\n\nThe Grand Hyatt Manchester San Diego is the official conference hotel for ACL 2026.\n\n**Hotel Booking:**\n\nThe cutoff date for booking the special hotel room block is June 8, 2026."
    ],
    "durationSeconds": 3.7077467619999953
  },
  "sourceToolAssistantUUID": "5c32855f-70dc-49a4-a5ac-13389d589f5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Counterfactual Probing Disentangles Evidence Gaps from Reasoning Diffi…",
  "leafUuid": "98b88f6b-1bf8-4a86-87b6-4c5c515ea3e1",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Counterfactual step-level failure-mode classification for retrieval gating",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Assistant

_source line 52 · 2026-05-14T16:47:51.513Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the key information:

1. **ProbeRAG/CLEAR venue**: The arXiv paper (v3, updated April 15, 2026) explicitly says "ACL 2026 Findings" in comments. The paper was indeed withdrawn from ICLR 2026 (OpenReview confirms), but was subsequently accepted at ACL 2026 Findings. ACL 2026 is scheduled for July 2-7, 2026 in San Diego, so the proceedings haven't been published yet (it's May 2026). The ACL Anthology wouldn't have it yet. The reviewer was wrong - the paper WAS accepted at ACL 2026 Findings after being withdrawn from ICLR 2026. 

The arXiv comments are self-reported by authors, which is the standard way acceptance gets communicated before the conference, so I should treat this as reliable.

2. **KRUX**: The paper is "Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning" (arXiv 2508.19202). It introduces KRUX framework that injects Knowledge Ingredients (KIs) to separate knowledge vs. reasoning bottlenecks. Key finding: base models with KIs outperform reasoning-enhanced variants by ≥10%, suggesting knowledge retrieval is the critical bottleneck for scientific reasoning. Purely diagnostic (black-box),

not an inference-time mechanism. The WebFetch from the HTML version suggested ICML acceptance, but I should cite it conservatively until verified.

3. **Counterfactual probing disambiguation**: arXiv 2508.01862 uses "counterfactual probing" to mean generating counterfactual statements and testing model sensitivity. This is completely different from what I'm doing—probing hidden states after counterfactual branching (forking execution paths). I should cite it and adopt clearer terminology like "counterfactual-branching probes" or "fork-and-probe" to avoid confusion.

4. **Search-R1 3B checkpoint**: The Search-R1 GitHub repo exists and supports Qwen2.5 models of different sizes, so I need to verify whether the 3B checkpoint is actually available.

5. **Impact framing**: This is the main blocker. Let me think deeply about this.

The key insight is that the failure-mode distribution directly determines what the field should prioritize. If multi-hop factual QA shows predominantly evidence gaps, that signals the field has been underinvesting in retrieval quality and overinvesting in reasoning improvements. If it's mostly reasoning difficulty, then retrieval-heavy approaches are misguided. Cross-dataset variance would mean benchmarks aren't interchangeable—a system optimized on HotpotQA could be fundamentally mistuned for MuSiQue. The distribution also determines the maximum ROI of adaptive retrieval: if only 30% of steps need retrieval, an always-retrieve system wastes 70% of retrieval calls and potentially degrades performance on those steps. So the design principles flow directly from the distribution—evidence gaps dominate means invest in retrieval quality; reasoning difficulty dominates means invest in reasoning robustness against retrieval noise.

I should verify that Qwen2.5-3B is available and add it to the plan, then search for any other recent work I might have missed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98b88f6b-1bf8-4a86-87b6-4c5c515ea3e1",
  "isSidechain": false,
  "requestId": "req_011Cb2oTmENs8dRC78e1XmFt",
  "type": "assistant",
  "uuid": "0d3732fd-3377-4934-8da4-4fae7ba5559a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SixNiwVoNnv6djQFtFvpLo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 39124,
      "output_tokens": 967,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 967,
          "cache_read_input_tokens": 39124,
          "cache_creation_input_tokens": 692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 692
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

_source line 53 · 2026-05-14T16:47:51.515Z_

Now let me check the Search-R1 repo for 3B checkpoint availability and do one more search for recent related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d3732fd-3377-4934-8da4-4fae7ba5559a",
  "isSidechain": false,
  "requestId": "req_011Cb2oTmENs8dRC78e1XmFt",
  "type": "assistant",
  "uuid": "8aa4cf56-3032-40d3-91b1-44153992d5ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SixNiwVoNnv6djQFtFvpLo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 39124,
      "output_tokens": 967,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 967,
          "cache_read_input_tokens": 39124,
          "cache_creation_input_tokens": 692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 692
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

_source line 54 · 2026-05-14T16:47:51.815Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G4M6rKCDCdunacnN9vJQ2T`</summary>

```json
{
  "url": "https://github.com/PeterGriffinJin/Search-R1",
  "prompt": "What model checkpoints are available? Specifically, is there a Qwen2.5-3B trained checkpoint available, or only Qwen2.5-7B? List all available pre-trained checkpoints and their sizes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8aa4cf56-3032-40d3-91b1-44153992d5ff",
  "isSidechain": false,
  "requestId": "req_011Cb2oTmENs8dRC78e1XmFt",
  "type": "assistant",
  "uuid": "7c2de4c2-d53e-4405-bd93-d6093af47619",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SixNiwVoNnv6djQFtFvpLo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 39124,
      "output_tokens": 967,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 967,
          "cache_read_input_tokens": 39124,
          "cache_creation_input_tokens": 692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 692
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

_source line 55 · 2026-05-14T16:47:56.353Z_

<details><summary>↩ Tool result · `toolu_01G4M6rKCDCdunacnN9vJQ2T`</summary>

```text
# Available Model Checkpoints

Based on the provided GitHub repository content, **specific checkpoint sizes and availability are not detailed in the documentation shown**. 

The repository mentions that "Model and data" are available via a Hugging Face collection link, but the actual checkpoint specifications aren't listed in this page content. The documentation references training examples with:

- Llama-3.2-3B-base
- Qwen2.5-7B-base

However, there is "no information confirming whether a Qwen2.5-3B checkpoint exists" in the material provided. To find complete checkpoint availability, you would need to visit the linked Hugging Face collection directly at: https://huggingface.co/collections/PeterJinGo/search-r1-67d1a021202731cb065740f5
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c2de4c2-d53e-4405-bd93-d6093af47619",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "9d9acc44-2d3f-4aa3-b6b4-93ed00d11a7d",
  "toolUseResult": {
    "bytes": 387120,
    "code": 200,
    "codeText": "OK",
    "result": "# Available Model Checkpoints\n\nBased on the provided GitHub repository content, **specific checkpoint sizes and availability are not detailed in the documentation shown**. \n\nThe repository mentions that \"Model and data\" are available via a Hugging Face collection link, but the actual checkpoint specifications aren't listed in this page content. The documentation references training examples with:\n\n- Llama-3.2-3B-base\n- Qwen2.5-7B-base\n\nHowever, there is \"no information confirming whether a Qwen2.5-3B checkpoint exists\" in the material provided. To find complete checkpoint availability, you would need to visit the linked Hugging Face collection directly at: https://huggingface.co/collections/PeterJinGo/search-r1-67d1a021202731cb065740f5",
    "durationMs": 4533,
    "url": "https://github.com/PeterGriffinJin/Search-R1"
  },
  "sourceToolAssistantUUID": "7c2de4c2-d53e-4405-bd93-d6093af47619",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 56 · 2026-05-14T16:47:56.357Z_

```json
{
  "parentUuid": "9d9acc44-2d3f-4aa3-b6b4-93ed00d11a7d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "bdc592d1-056b-4ad8-9dc6-87b66477b10b",
  "timestamp": "2026-05-14T16:47:56.357Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 57 · 2026-05-14T16:47:59.865Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M2geeT9g8FCHKWwwKdgEXt`</summary>

```json
{
  "url": "https://huggingface.co/collections/PeterJinGo/search-r1-67d1a021202731cb065740f5",
  "prompt": "List all available model checkpoints in this collection. What model sizes are available (3B, 7B, etc.)? Is there a Qwen2.5-3B checkpoint?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdc592d1-056b-4ad8-9dc6-87b66477b10b",
  "isSidechain": false,
  "requestId": "req_011Cb2oVuqbzhmKUWS8X2ZeL",
  "type": "assistant",
  "uuid": "7ab3246c-f117-4eaa-8b50-a32f2318ba0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011UhHfGAUmPQ3BJ7V5M2oJM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1265,
      "cache_read_input_tokens": 39816,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1265,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 39816,
          "cache_creation_input_tokens": 1265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1265
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

_source line 58 · 2026-05-14T16:48:04.301Z_

<details><summary>↩ Tool result · `toolu_01M2geeT9g8FCHKWwwKdgEXt`</summary>

```text
# Search-R1 Model Checkpoints

## Available Model Sizes

The collection includes checkpoints in the following sizes:

- **3B models** (Llama 3.2 and Qwen 2.5)
- **7B models** (Qwen 2.5)
- **8B models** (listed in the collection)

## Qwen2.5-3B Checkpoints

Yes, there are **multiple Qwen2.5-3B checkpoints** available:

1. **PeterJinGo/SearchR1-nq_hotpotqa_train-qwen2.5-3b-em-ppo** (248 likes)
2. **PeterJinGo/SearchR1-nq_hotpotqa_train-qwen2.5-3b-em-grpo** (254 likes)
3. **PeterJinGo/SearchR1-nq_hotpotqa_train-qwen2.5-3b-it-em-ppo** (151 likes)
4. **PeterJinGo/SearchR1-nq_hotpotqa_train-qwen2.5-3b-it-em-grpo** (566 likes)

## Summary of All Checkpoints

| Model | Training Method | Variants | Count |
|-------|-----------------|----------|-------|
| Llama 3.2-3B | PPO, GRPO | base + instruction-tuned | 4 |
| Qwen 2.5-3B | PPO, GRPO | base + instruction-tuned | 4 |
| Qwen 2.5-7B | PPO | base + instruction-tuned | 2 |

All checkpoints were trained using outcome-only RL and updated on **March 12, 2025**.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ab3246c-f117-4eaa-8b50-a32f2318ba0b",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "0b188e19-d27d-4d27-b3d0-88abfa019ce4",
  "toolUseResult": {
    "bytes": 108705,
    "code": 200,
    "codeText": "OK",
    "result": "# Search-R1 Model Checkpoints\n\n## Available Model Sizes\n\nThe collection includes checkpoints in the following sizes:\n\n- **3B models** (Llama 3.2 and Qwen 2.5)\n- **7B models** (Qwen 2.5)\n- **8B models** (listed in the collection)\n\n## Qwen2.5-3B Checkpoints\n\nYes, there are **multiple Qwen2.5-3B checkpoints** available:\n\n1. **PeterJinGo/SearchR1-nq_hotpotqa_train-qwen2.5-3b-em-ppo** (248 likes)\n2. **PeterJinGo/SearchR1-nq_hotpotqa_train-qwen2.5-3b-em-grpo** (254 likes)\n3. **PeterJinGo/SearchR1-nq_hotpotqa_train-qwen2.5-3b-it-em-ppo** (151 likes)\n4. **PeterJinGo/SearchR1-nq_hotpotqa_train-qwen2.5-3b-it-em-grpo** (566 likes)\n\n## Summary of All Checkpoints\n\n| Model | Training Method | Variants | Count |\n|-------|-----------------|----------|-------|\n| Llama 3.2-3B | PPO, GRPO | base + instruction-tuned | 4 |\n| Qwen 2.5-3B | PPO, GRPO | base + instruction-tuned | 4 |\n| Qwen 2.5-7B | PPO | base + instruction-tuned | 2 |\n\nAll checkpoints were trained using outcome-only RL and updated on **March 12, 2025**.",
    "durationMs": 4434,
    "url": "https://huggingface.co/collections/PeterJinGo/search-r1-67d1a021202731cb065740f5"
  },
  "sourceToolAssistantUUID": "7ab3246c-f117-4eaa-8b50-a32f2318ba0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-14T16:48:06.916Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G7jsx8UY7BbGnKVff12vLq`</summary>

```json
{
  "query": "KRUX \"Demystifying Scientific\" ICML 2026 accepted paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b188e19-d27d-4d27-b3d0-88abfa019ce4",
  "isSidechain": false,
  "requestId": "req_011Cb2oWVnXPqSkgwxcrncsa",
  "type": "assistant",
  "uuid": "cf7793ed-e74d-4cf2-8ea2-1b7b63c96f3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01REPAWS7WGzGisSr56XdU1B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 593,
      "cache_read_input_tokens": 41081,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 41081,
          "cache_creation_input_tokens": 593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 593
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

_source line 60 · 2026-05-14T16:48:11.617Z_

<details><summary>↩ Tool result · `toolu_01G7jsx8UY7BbGnKVff12vLq`</summary>

```text
Web search results for query: "KRUX "Demystifying Scientific" ICML 2026 accepted paper"

Links: [{"title":"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning","url":"https://arxiv.org/html/2508.19202"}]

Based on the search results, I found information about the paper:

KRUX (Knowledge & Reasoning Utilization eXams) is a probing framework which supplies models with atomic "knowledge ingredients" (KIs) extracted from other models' reasoning traces. 

The work introduces SciReas, a diverse suite of existing benchmarks for scientific reasoning tasks, and SciReas-Pro, a selective subset that requires more complex reasoning.

The paper presents three key findings: (i) knowledge retrieval is a bottleneck; (ii) in-context knowledge consistently benefits reasoning models; and (iii) long CoT improves knowledge surfacing.

The paper titled "Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning" appears to be available on arXiv. However, I should note that while the search returned this arXiv preprint from January 2026, I wasn't able to confirm from the search results whether it has been officially accepted to ICML 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf7793ed-e74d-4cf2-8ea2-1b7b63c96f3b",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "7d432c6d-3b50-4685-a6ca-2129d30e4ef7",
  "toolUseResult": {
    "query": "KRUX \"Demystifying Scientific\" ICML 2026 accepted paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RevFkajL55kFEmK8RnqNUn",
        "content": [
          {
            "title": "Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning",
            "url": "https://arxiv.org/html/2508.19202"
          }
        ]
      },
      "Based on the search results, I found information about the paper:\n\nKRUX (Knowledge & Reasoning Utilization eXams) is a probing framework which supplies models with atomic \"knowledge ingredients\" (KIs) extracted from other models' reasoning traces. \n\nThe work introduces SciReas, a diverse suite of existing benchmarks for scientific reasoning tasks, and SciReas-Pro, a selective subset that requires more complex reasoning.\n\nThe paper presents three key findings: (i) knowledge retrieval is a bottleneck; (ii) in-context knowledge consistently benefits reasoning models; and (iii) long CoT improves knowledge surfacing.\n\nThe paper titled \"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning\" appears to be available on arXiv. However, I should note that while the search returned this arXiv preprint from January 2026, I wasn't able to confirm from the search results whether it has been officially accepted to ICML 2026."
    ],
    "durationSeconds": 4.697303499000001
  },
  "sourceToolAssistantUUID": "cf7793ed-e74d-4cf2-8ea2-1b7b63c96f3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T16:48:14.545Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KZj1cpMkrvK5Aqj6Kjqxjw`</summary>

```json
{
  "query": "adaptive retrieval multi-hop QA knowledge gap reasoning difficulty distribution analysis 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d432c6d-3b50-4685-a6ca-2129d30e4ef7",
  "isSidechain": false,
  "requestId": "req_011Cb2oX3fB7z8TX2RdUabP3",
  "type": "assistant",
  "uuid": "4044eb43-ec45-4e7b-b427-0c18c1efc640",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZRxwUqbRdtdfPxs49qUJG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 400,
      "cache_read_input_tokens": 41674,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 400,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 41674,
          "cache_creation_input_tokens": 400,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 400
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

_source line 62 · 2026-05-14T16:48:24.297Z_

<details><summary>↩ Tool result · `toolu_01KZj1cpMkrvK5Aqj6Kjqxjw`</summary>

```text
Web search results for query: "adaptive retrieval multi-hop QA knowledge gap reasoning difficulty distribution analysis 2026"

Links: [{"title":"Improving Retrieval-Augmented Generation for Multi-Hop ...","url":"https://arxiv.org/pdf/2601.11255"},{"title":"Reasoning in Trees: Improving Retrieval-Augmented Generation for Multi-Hop Question Answering","url":"https://arxiv.org/html/2601.11255v1"},{"title":"Generating multi-hop QA and fine-gRAined Difficulty matrix ...","url":"https://aclanthology.org/2025.findings-emnlp.236.pdf"},{"title":"Retrieval–Reasoning Processes for Multi-hop Question Answering: A Four-Axis Design Framework and Empirical Trends","url":"https://arxiv.org/html/2601.00536v1"},{"title":"CREDIBLE PLAN-DRIVEN RAG METHOD FOR MULTI-HOP QUESTION ANSWERING","url":"https://arxiv.org/pdf/2504.16787"},{"title":"damr: efficient and adaptive context-aware knowledge ...","url":"https://openreview.net/pdf?id=mUx7WLC8q6"},{"title":"StepChain GraphRAG: Reasoning Over Knowledge Graphs for Multi-Hop Question Answering","url":"https://arxiv.org/html/2510.02827v1"},{"title":"Adaptive Retrieval without Self-Knowledge? Bringing ...","url":"https://aclanthology.org/2025.acl-long.319.pdf"},{"title":"MultiHop-RAG: Benchmarking Retrieval-Augmented Generation for Multi-Hop Queries | OpenReview","url":"https://openreview.net/forum?id=t4eB3zYWBK"},{"title":"Reasoning Processes for Multi-hop Question Answering","url":"https://arxiv.org/pdf/2601.00536"}]

Based on the search results, here's what I found about adaptive retrieval, multi-hop QA, knowledge gaps, and reasoning difficulty distribution analysis:

## Key Research Areas (2026)

### Adaptive Retrieval in Multi-Hop QA

Recent research introduces Reasoning Tree Guided RAG (RT-RAG), a novel hierarchical framework that imposes explicit tree structure on the multi-hop reasoning process to improve how AI systems retrieve and synthesize information from Web-scale knowledge sources.

### Knowledge Gap Handling

When retrieval encounters missing information, RT-RAG dynamically restructures the reasoning path—when retrieval returns no answer, its parent node is converted into a new leaf node, enabling the model to bypass the missing information and seek alternative paths.

### Difficulty Distribution Analysis

Recent work employs multi-hop reasoning paths in a directed acyclic graph to generate QA pairs, with each query assigned a difficulty label based on reasoning depth and retrieval difficulty, and RAG system performance is assessed via cell-wise error rates across a 2D difficulty matrix considering both generator-side and retriever-side complexity.

### Adaptive Stopping Mechanisms

Most systems still rely on static hop, token, or latency budgets, while adaptive stopping based on confidence, sufficiency, or value estimates is evaluated on limited benchmarks and remains poorly calibrated under distribution shift, with an important open problem being to develop stop/continue criteria that remain calibrated across retrievers, corpora, and LLM backbones.

### Complexity-Aware Planning

While prior methods provide various techniques for structure and reasoning, none provides a principled end-to-end mechanism that uses semantic complexity to condition exemplar selection and plan granularity, with PAR-RAG addressing this by threading semantic complexity across Plan-then-Act-and-Review stages where verification adapts to instance difficulty.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4044eb43-ec45-4e7b-b427-0c18c1efc640",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "8c1c5bd4-ea31-486b-842e-94601b08bf97",
  "toolUseResult": {
    "query": "adaptive retrieval multi-hop QA knowledge gap reasoning difficulty distribution analysis 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xrpc6B17wAKZxdDJUFmGPW",
        "content": [
          {
            "title": "Improving Retrieval-Augmented Generation for Multi-Hop ...",
            "url": "https://arxiv.org/pdf/2601.11255"
          },
          {
            "title": "Reasoning in Trees: Improving Retrieval-Augmented Generation for Multi-Hop Question Answering",
            "url": "https://arxiv.org/html/2601.11255v1"
          },
          {
            "title": "Generating multi-hop QA and fine-gRAined Difficulty matrix ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.236.pdf"
          },
          {
            "title": "Retrieval–Reasoning Processes for Multi-hop Question Answering: A Four-Axis Design Framework and Empirical Trends",
            "url": "https://arxiv.org/html/2601.00536v1"
          },
          {
            "title": "CREDIBLE PLAN-DRIVEN RAG METHOD FOR MULTI-HOP QUESTION ANSWERING",
            "url": "https://arxiv.org/pdf/2504.16787"
          },
          {
            "title": "damr: efficient and adaptive context-aware knowledge ...",
            "url": "https://openreview.net/pdf?id=mUx7WLC8q6"
          },
          {
            "title": "StepChain GraphRAG: Reasoning Over Knowledge Graphs for Multi-Hop Question Answering",
            "url": "https://arxiv.org/html/2510.02827v1"
          },
          {
            "title": "Adaptive Retrieval without Self-Knowledge? Bringing ...",
            "url": "https://aclanthology.org/2025.acl-long.319.pdf"
          },
          {
            "title": "MultiHop-RAG: Benchmarking Retrieval-Augmented Generation for Multi-Hop Queries | OpenReview",
            "url": "https://openreview.net/forum?id=t4eB3zYWBK"
          },
          {
            "title": "Reasoning Processes for Multi-hop Question Answering",
            "url": "https://arxiv.org/pdf/2601.00536"
          }
        ]
      },
      "Based on the search results, here's what I found about adaptive retrieval, multi-hop QA, knowledge gaps, and reasoning difficulty distribution analysis:\n\n## Key Research Areas (2026)\n\n### Adaptive Retrieval in Multi-Hop QA\n\nRecent research introduces Reasoning Tree Guided RAG (RT-RAG), a novel hierarchical framework that imposes explicit tree structure on the multi-hop reasoning process to improve how AI systems retrieve and synthesize information from Web-scale knowledge sources.\n\n### Knowledge Gap Handling\n\nWhen retrieval encounters missing information, RT-RAG dynamically restructures the reasoning path—when retrieval returns no answer, its parent node is converted into a new leaf node, enabling the model to bypass the missing information and seek alternative paths.\n\n### Difficulty Distribution Analysis\n\nRecent work employs multi-hop reasoning paths in a directed acyclic graph to generate QA pairs, with each query assigned a difficulty label based on reasoning depth and retrieval difficulty, and RAG system performance is assessed via cell-wise error rates across a 2D difficulty matrix considering both generator-side and retriever-side complexity.\n\n### Adaptive Stopping Mechanisms\n\nMost systems still rely on static hop, token, or latency budgets, while adaptive stopping based on confidence, sufficiency, or value estimates is evaluated on limited benchmarks and remains poorly calibrated under distribution shift, with an important open problem being to develop stop/continue criteria that remain calibrated across retrievers, corpora, and LLM backbones.\n\n### Complexity-Aware Planning\n\nWhile prior methods provide various techniques for structure and reasoning, none provides a principled end-to-end mechanism that uses semantic complexity to condition exemplar selection and plan granularity, with PAR-RAG addressing this by threading semantic complexity across Plan-then-Act-and-Review stages where verification adapts to instance difficulty."
    ],
    "durationSeconds": 9.748254478000018
  },
  "sourceToolAssistantUUID": "4044eb43-ec45-4e7b-b427-0c18c1efc640",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T16:48:27.691Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012jxRNpR76KiUJq3B2mZ8hm`</summary>

```json
{
  "query": "\"counterfactual branching\" OR \"fork-and-probe\" hidden states retrieval gating reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c1c5bd4-ea31-486b-842e-94601b08bf97",
  "isSidechain": false,
  "requestId": "req_011Cb2oXyTwQAukisXR2AXUf",
  "type": "assistant",
  "uuid": "dab15034-33b7-47bd-ba05-981a3d332d1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhzNC9oVRKrpJsAK93FXcJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 42074,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 42074,
          "cache_creation_input_tokens": 976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 976
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

_source line 64_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Counterfactual Probing Disentangles Evidence Gaps from Reasoning Diffi…",
  "leafUuid": "dab15034-33b7-47bd-ba05-981a3d332d1b",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "Counterfactual step-level failure-mode classification for retrieval gating",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Tool result

_source line 66 · 2026-05-14T16:48:36.133Z_

<details><summary>↩ Tool result · `toolu_012jxRNpR76KiUJq3B2mZ8hm`</summary>

```text
Web search results for query: ""counterfactual branching" OR "fork-and-probe" hidden states retrieval gating reasoning 2025 2026"

Links: [{"title":"Counterfactual Reasoning for Retrieval-Augmented Generation | OpenReview","url":"https://openreview.net/forum?id=9U51rOnGko"},{"title":"[2504.05419v1] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/abs/2504.05419v1"},{"title":"[2504.05419] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/abs/2504.05419"},{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/html/2504.05419v1"},{"title":"A Survey on the Mechanisms of Multi-Step Reasoning in ...","url":"https://www.preprints.org/frontend/manuscript/11cab45ab0d578f7080de19423eb6ffe/download_pub"},{"title":"Reasoning Models Know When They’re Right: NYU Researchers Introduce a Hidden-State Probe That Enables Efficient Self-Verification and Reduces Token Usage by 24% - MarkTechPost","url":"https://www.marktechpost.com/2025/04/13/reasoning-models-know-when-theyre-right-nyu-researchers-introduce-a-hidden-state-probe-that-enables-efficient-self-verification-and-reduces-token-usage-by-24/"},{"title":"Next Week Tonight: Simulating Counterfactual Narratives ...","url":"https://dspace.mit.edu/bitstream/handle/1721.1/164132/agarwal-gauri_al-SM-MAS-2025-thesis.pdf?sequence=1&isAllowed=y"},{"title":"They train a binary probe on hidden states from intermediate reasoning steps, which accurately predicts answer correctness before generation, enabling early-exit to reduce test-time compute without compromise. Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification https://arxiv.org/abs/2504.05419v1","url":"https://www.threads.com/@sung.kim.mw/post/DTxYmJ4EWAp/they-train-a-binary-probe-on-hidden-states-from-intermediate-reasoning-steps"},{"title":"Computational basis of hierarchical and counterfactual information processing | Nature Human Behaviour","url":"https://www.nature.com/articles/s41562-025-02232-3"},{"title":"Branching Space-Time, Modal Logic and the Counterfactual Conditional | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-94-010-0385-8_18"}]

I found several relevant research papers from 2025-2026 related to your search query. Here are the key findings:

## Hidden States & Reasoning Models

Research published in April 2025 studies whether reasoning models encode information about answer correctness through probing the model's hidden states, with the resulting probe verifying intermediate answers with high accuracy and producing highly calibrated scores. Models' hidden states encode correctness of future answers, enabling early prediction of the correctness before the intermediate answer is fully formulated. This approach trains a binary probe on hidden states from intermediate reasoning steps, which accurately predicts answer correctness before generation, enabling early-exit to reduce test-time compute without compromise.

## Counterfactual Reasoning for Retrieval-Augmented Generation

Counterfactual RAG (CF-RAG) is a framework that operationalizes causal reasoning, systematically generating and evaluating counterfactual queries to identify causally relevant distinctions, and employing a parallel arbitration mechanism to reconcile conflicting evidence without interference. CF-RAG substantially improves robustness against the Correlation Trap, achieving state-of-the-art performance while maintaining comparable efficiency to standard RAG models. This framework was presented in October 2025.

## Multi-Step Reasoning Mechanisms

A comprehensive survey identifies seven pivotal research questions covering analytical methods and key findings from the hidden internal dynamics of latent reasoning to the visible mechanisms of explicit chain-of-thought reasoning.

The search results contain more recent work on probing mechanisms and counterfactual approaches to reasoning, though the specific "fork-and-probe" terminology you mentioned doesn't appear directly in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dab15034-33b7-47bd-ba05-981a3d332d1b",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "5fd96299-fdfa-4592-b3d7-78e8a5b25005",
  "toolUseResult": {
    "query": "\"counterfactual branching\" OR \"fork-and-probe\" hidden states retrieval gating reasoning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Skg2zW4Dkxk6oAS8iQGyXG",
        "content": [
          {
            "title": "Counterfactual Reasoning for Retrieval-Augmented Generation | OpenReview",
            "url": "https://openreview.net/forum?id=9U51rOnGko"
          },
          {
            "title": "[2504.05419v1] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification",
            "url": "https://arxiv.org/abs/2504.05419v1"
          },
          {
            "title": "[2504.05419] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification",
            "url": "https://arxiv.org/abs/2504.05419"
          },
          {
            "title": "Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification",
            "url": "https://arxiv.org/html/2504.05419v1"
          },
          {
            "title": "A Survey on the Mechanisms of Multi-Step Reasoning in ...",
            "url": "https://www.preprints.org/frontend/manuscript/11cab45ab0d578f7080de19423eb6ffe/download_pub"
          },
          {
            "title": "Reasoning Models Know When They’re Right: NYU Researchers Introduce a Hidden-State Probe That Enables Efficient Self-Verification and Reduces Token Usage by 24% - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/04/13/reasoning-models-know-when-theyre-right-nyu-researchers-introduce-a-hidden-state-probe-that-enables-efficient-self-verification-and-reduces-token-usage-by-24/"
          },
          {
            "title": "Next Week Tonight: Simulating Counterfactual Narratives ...",
            "url": "https://dspace.mit.edu/bitstream/handle/1721.1/164132/agarwal-gauri_al-SM-MAS-2025-thesis.pdf?sequence=1&isAllowed=y"
          },
          {
            "title": "They train a binary probe on hidden states from intermediate reasoning steps, which accurately predicts answer correctness before generation, enabling early-exit to reduce test-time compute without compromise. Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification https://arxiv.org/abs/2504.05419v1",
            "url": "https://www.threads.com/@sung.kim.mw/post/DTxYmJ4EWAp/they-train-a-binary-probe-on-hidden-states-from-intermediate-reasoning-steps"
          },
          {
            "title": "Computational basis of hierarchical and counterfactual information processing | Nature Human Behaviour",
            "url": "https://www.nature.com/articles/s41562-025-02232-3"
          },
          {
            "title": "Branching Space-Time, Modal Logic and the Counterfactual Conditional | SpringerLink",
            "url": "https://link.springer.com/chapter/10.1007/978-94-010-0385-8_18"
          }
        ]
      },
      "I found several relevant research papers from 2025-2026 related to your search query. Here are the key findings:\n\n## Hidden States & Reasoning Models\n\nResearch published in April 2025 studies whether reasoning models encode information about answer correctness through probing the model's hidden states, with the resulting probe verifying intermediate answers with high accuracy and producing highly calibrated scores. Models' hidden states encode correctness of future answers, enabling early prediction of the correctness before the intermediate answer is fully formulated. This approach trains a binary probe on hidden states from intermediate reasoning steps, which accurately predicts answer correctness before generation, enabling early-exit to reduce test-time compute without compromise.\n\n## Counterfactual Reasoning for Retrieval-Augmented Generation\n\nCounterfactual RAG (CF-RAG) is a framework that operationalizes causal reasoning, systematically generating and evaluating counterfactual queries to identify causally relevant distinctions, and employing a parallel arbitration mechanism to reconcile conflicting evidence without interference. CF-RAG substantially improves robustness against the Correlation Trap, achieving state-of-the-art performance while maintaining comparable efficiency to standard RAG models. This framework was presented in October 2025.\n\n## Multi-Step Reasoning Mechanisms\n\nA comprehensive survey identifies seven pivotal research questions covering analytical methods and key findings from the hidden internal dynamics of latent reasoning to the visible mechanisms of explicit chain-of-thought reasoning.\n\nThe search results contain more recent work on probing mechanisms and counterfactual approaches to reasoning, though the specific \"fork-and-probe\" terminology you mentioned doesn't appear directly in these results."
    ],
    "durationSeconds": 8.43708036999998
  },
  "sourceToolAssistantUUID": "dab15034-33b7-47bd-ba05-981a3d332d1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-14T16:49:53.955Z_

<details><summary>Logged reasoning block</summary>

```text
Good. I've gathered enough information now. Let me synthesize my findings and think about the revisions:

## Research findings summary:

1. **ProbeRAG/CLEAR venue**: The arXiv page (v3, April 15, 2026) explicitly says "ACL 2026 Findings" in comments. It was withdrawn from ICLR 2026, then accepted at ACL 2026 Findings. ACL 2026 is July 2-7, 2026 in San Diego. The ACL Anthology doesn't have it yet because the conference hasn't happened. The reviewer's concern was based on the ICLR withdrawal, but the authors self-reported ACL 2026 Findings acceptance. 

I should be precise here: the arXiv v3 comments claim ACL 2026 Findings acceptance, which I verified directly, though this can't be independently confirmed until the conference occurs. The ICLR 2026 withdrawal is accurate, but the paper found acceptance at ACL 2026 Findings afterward.

2. **KRUX**: Good

3. **Counterfactual probing disambiguation**: I need to differentiate our approach from arXiv 2508.01862, which uses "counterfactual probing" for behavioral testing with counterfactual statements, whereas we're probing hidden states after counterfactual branching—I'll adopt "counterfactual-branching probes" to make this distinction clear.

4. **Search-R1 3B checkpoints**: Multiple Qwen2.5-3B variants are confirmed available, including PPO and GRPO versions in both base and instruction-tuned forms, which validates the reviewer's suggestion.

5. **Impact framing**: The key insight is that failure-mode distributions have direct implications for how the field should allocate resources. If evidence gaps dominate multi-hop reasoning (60-70%), then retrieval precision becomes the priority over reasoning robustness; if reasoning difficulty is the bottleneck, the focus shifts to retrieval noise reduction. This also means different benchmarks like HotpotQA and MuSiQue likely have distinct failure profiles, so a system validated on one may not generalize well to another.

The practical consequences extend further: adaptive retrieval should be conditioned on question-level features, not just step-level signals, since questions with primarily reasoning-difficulty steps need different gating strategies than those with evidence gaps. Current single-threshold approaches like FLARE can't simultaneously optimize for both failure modes—you'd need a multi-dimensional decision space. This connects to DART's observation that reasoning and tool-use create competing training gradients.

Now I see why: mixing evidence-gap steps (where retrieval helps) with reasoning-difficulty steps (where it hurts) during training produces exactly the gradient interference DART documented, and the relative proportion of each type determines how severe the conflict becomes.

The reviewer flagged impact framing as the main issue (3/5 score), but called the core novelty verified and the fixes actionable—this reads like a genuine minor revision case. The stagnation warning is worth examining though: the evidence-reasoning conflation is measurable and real, multiple papers converge on this opportunity, and the approach is sound, but I should verify whether the stagnation stems from something more fundamental.

The real bottleneck is impact, not the core idea. The reviewer's suggestions are concrete: adding a Qwen2.5-3B checkpoint is straightforward and valuable, and reframing the impact narrative directly addresses the scoring gap. These aren't cosmetic tweaks—they target the actual weakness.

For the revisions, I need to handle the ProbeRAG/CLEAR citation carefully by verifying the evidence from arXiv comments rather than relying on the ACL 2026 Findings status, add KRUX to the opportunity section, shift the terminology to "counterfactual-branching probes" with the proper arXiv reference, and work through the remaining changes.

Now I'm weighing terminology options—"counterfactual-branching probes" is precise but verbose, while "fork-and-probe" is catchier but less clear. I'll stick with the longer form as the primary term and use the shorthand strategically. The title itself might need adjustment to better signal the disambiguation and impact. I'm settling on "Counterfactual-Branching Probes Disentangle Evidence Gaps from Reasoning Difficulty for Step-Level Retrieval Gating" since it directly addresses the naming confusion the reviewer flagged while keeping the established structure intact. Now I need to strengthen the impact framing by articulating concrete implications—specifically, if evidence gaps are indeed the dominant failure mode in multi-hop factual QA, then current adaptive retrieval systems that suppress retrieval based on confidence scores might be missing opportunities to improve performance. The key insight is that different datasets have fundamentally different retrieval needs—HotpotQA's entity-centric structure likely benefits from aggressive retrieval to fill evidence gaps, while MuSiQue's compositional reasoning might require more selective retrieval to avoid disrupting logical chains. This means adaptive retrieval strategies need to be tuned per-benchmark rather than treating "multi-hop QA" as a single category. The gating experiment is crucial here because it moves beyond just describing the failure mode distribution to proving that this knowledge is actionable—a probe trained on these labels outperforms observational baselines, which validates that understanding *why* the model fails translates to practical improvements.

Now I'm integrating the reviewer feedback and strengthening the impact framing for the revision. For the ProbeRAG/CLEAR venue issue, I've confirmed the ICLR 2026 withdrawal through OpenReview, and the arXiv v3 from April lists "ACL 2026 Findings" in the comments—which is standard practice for authors updating after acceptance. Since ACL 2026 hasn't published proceedings yet, I'll cite it as "ACL 2026 Findings" while noting this is based on the arXiv self-report, which satisfies the reviewer's request to verify the venue.

Now I'm structuring the full JSON response with stronger framing around the core insight: failure-mode distribution shapes optimal retrieval design, and current systems treat all failures identically when they should differentiate between evidence gaps versus reasoning difficulty.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fd96299-fdfa-4592-b3d7-78e8a5b25005",
  "isSidechain": false,
  "requestId": "req_011Cb2oYqx2oBaHM3GiwFSJ4",
  "type": "assistant",
  "uuid": "857c7f91-6e4b-4e3b-889e-7e947f67d732",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMBpwxC7zCJXwZgWPmRafN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1180,
      "cache_read_input_tokens": 43050,
      "output_tokens": 3373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1180,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3373,
          "cache_read_input_tokens": 43050,
          "cache_creation_input_tokens": 1180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1180
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

_source line 68 · 2026-05-14T16:49:54.369Z_

Good, I now have solid research findings. Let me verify one more thing about KRUX's venue, then I'll synthesize everything.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "857c7f91-6e4b-4e3b-889e-7e947f67d732",
  "isSidechain": false,
  "requestId": "req_011Cb2oYqx2oBaHM3GiwFSJ4",
  "type": "assistant",
  "uuid": "ecd43c06-9bf8-4921-8c46-39f42188aeb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMBpwxC7zCJXwZgWPmRafN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1180,
      "cache_read_input_tokens": 43050,
      "output_tokens": 3373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1180,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3373,
          "cache_read_input_tokens": 43050,
          "cache_creation_input_tokens": 1180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1180
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

_source line 69 · 2026-05-14T16:49:55.852Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017G19RefzB29c6j5Dbbktzh`</summary>

```json
{
  "url": "https://openreview.net/forum?id=B8a3UW5VHf",
  "prompt": "What venue was this paper submitted to? What is the decision - accepted, rejected, or under review? What are the review scores?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecd43c06-9bf8-4921-8c46-39f42188aeb1",
  "isSidechain": false,
  "requestId": "req_011Cb2oYqx2oBaHM3GiwFSJ4",
  "type": "assistant",
  "uuid": "bbe388d2-0253-4aaa-8da9-fe67039ec907",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMBpwxC7zCJXwZgWPmRafN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1180,
      "cache_read_input_tokens": 43050,
      "output_tokens": 3373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1180,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3373,
          "cache_read_input_tokens": 43050,
          "cache_creation_input_tokens": 1180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1180
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

_source line 70_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Counterfactual Probing Disentangles Evidence Gaps from Reasoning Diffi…",
  "leafUuid": "bbe388d2-0253-4aaa-8da9-fe67039ec907",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Counterfactual step-level failure-mode classification for retrieval gating",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Tool result

_source line 72 · 2026-05-14T16:49:58.030Z_

<details><summary>↩ Tool result · `toolu_017G19RefzB29c6j5Dbbktzh`</summary>

```text
Based on the provided content, here's what can be determined:

**Venue:** The paper was submitted to "NeurIPS 2025 Workshop FoRLM" (Foundations of Reasoning in Language Models workshop at NeurIPS 2025).

**Decision and Review Scores:** The webpage does not contain information about the paper's acceptance decision or any review scores. While the paper shows a publication date of "23 Sept 2025," the content provided does not indicate whether it was accepted, rejected, or remains under review, nor does it display reviewer scores or comments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbe388d2-0253-4aaa-8da9-fe67039ec907",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "9f5d71ac-6b6e-486b-b0f1-8194d97b6fd3",
  "toolUseResult": {
    "bytes": 67387,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the provided content, here's what can be determined:\n\n**Venue:** The paper was submitted to \"NeurIPS 2025 Workshop FoRLM\" (Foundations of Reasoning in Language Models workshop at NeurIPS 2025).\n\n**Decision and Review Scores:** The webpage does not contain information about the paper's acceptance decision or any review scores. While the paper shows a publication date of \"23 Sept 2025,\" the content provided does not indicate whether it was accepted, rejected, or remains under review, nor does it display reviewer scores or comments.",
    "durationMs": 2172,
    "url": "https://openreview.net/forum?id=B8a3UW5VHf"
  },
  "sourceToolAssistantUUID": "bbe388d2-0253-4aaa-8da9-fe67039ec907",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-14T16:50:00.744Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MRjRz2iZeWM7EzLjuEBRXs`</summary>

```json
{
  "query": "\"Demystifying Scientific Problem-Solving\" KRUX ICML 2026 accepted openreview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f5d71ac-6b6e-486b-b0f1-8194d97b6fd3",
  "isSidechain": false,
  "requestId": "req_011Cb2oet2iNvKdGpienkcdn",
  "type": "assistant",
  "uuid": "a88fa3a5-8e7c-40fe-b3c4-b0c02a825c5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWnoePr7ifoYEceWAd7PRd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 44230,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3509,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 44230,
          "cache_creation_input_tokens": 3509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3509
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

_source line 74 · 2026-05-14T16:50:06.137Z_

<details><summary>↩ Tool result · `toolu_01MRjRz2iZeWM7EzLjuEBRXs`</summary>

```text
Web search results for query: ""Demystifying Scientific Problem-Solving" KRUX ICML 2026 accepted openreview"

Links: [{"title":"DEMYSTIFYING SCIENTIFIC PROBLEM-SOLVING IN LLMS BY ...","url":"https://openreview.net/pdf?id=l852J55j9n"},{"title":"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning","url":"https://arxiv.org/html/2508.19202"},{"title":"ICML 2026 | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026"},{"title":"[2508.19202] Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning","url":"https://arxiv.org/abs/2508.19202"},{"title":"ICML 2026 Workshop | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop"},{"title":"ICML 2026 Workshop AI4Science | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FAI4Science"},{"title":"ICML 2026 Workshop EIML | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FEIML"},{"title":"ICML 2026 Workshop CompLearn | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FCompLearn"},{"title":"ICML 2026 Workshop Forecast | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FForecast"},{"title":"ICML 2026 Workshop FMSD | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FFMSD"}]

I found the paper "Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning" which includes the KRUX framework. Based on the search results:

KRUX (Knowledge & Reasoning Utilization eXams) is a probing framework which supplies models with atomic "knowledge ingredients" (KIs) extracted from other models' reasoning traces. 

The paper introduces SciReas, a diverse suite of existing benchmarks for scientific reasoning tasks, and SciReas-Pro, a selective subset that requires more complex reasoning.

The key findings are: (i) knowledge retrieval is a bottleneck; (ii) in-context knowledge consistently benefits reasoning models; and (iii) long CoT improves knowledge surfacing.

The paper is available on OpenReview (https://openreview.net/pdf?id=l852J55j9n) and also on arXiv. The arxiv version shows a metadata date of January 19, 2026, indicating this is a recent work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a88fa3a5-8e7c-40fe-b3c4-b0c02a825c5c",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "2cded46f-a6c7-4ea7-99eb-a2a3744cfe9f",
  "toolUseResult": {
    "query": "\"Demystifying Scientific Problem-Solving\" KRUX ICML 2026 accepted openreview",
    "results": [
      {
        "tool_use_id": "srvtoolu_019mhBYkShUCWg1S1w5dG9SE",
        "content": [
          {
            "title": "DEMYSTIFYING SCIENTIFIC PROBLEM-SOLVING IN LLMS BY ...",
            "url": "https://openreview.net/pdf?id=l852J55j9n"
          },
          {
            "title": "Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning",
            "url": "https://arxiv.org/html/2508.19202"
          },
          {
            "title": "ICML 2026 | OpenReview",
            "url": "https://openreview.net/group?id=ICML.cc%2F2026"
          },
          {
            "title": "[2508.19202] Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning",
            "url": "https://arxiv.org/abs/2508.19202"
          },
          {
            "title": "ICML 2026 Workshop | OpenReview",
            "url": "https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop"
          },
          {
            "title": "ICML 2026 Workshop AI4Science | OpenReview",
            "url": "https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FAI4Science"
          },
          {
            "title": "ICML 2026 Workshop EIML | OpenReview",
            "url": "https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FEIML"
          },
          {
            "title": "ICML 2026 Workshop CompLearn | OpenReview",
            "url": "https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FCompLearn"
          },
          {
            "title": "ICML 2026 Workshop Forecast | OpenReview",
            "url": "https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FForecast"
          },
          {
            "title": "ICML 2026 Workshop FMSD | OpenReview",
            "url": "https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FFMSD"
          }
        ]
      },
      "I found the paper \"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning\" which includes the KRUX framework. Based on the search results:\n\nKRUX (Knowledge & Reasoning Utilization eXams) is a probing framework which supplies models with atomic \"knowledge ingredients\" (KIs) extracted from other models' reasoning traces. \n\nThe paper introduces SciReas, a diverse suite of existing benchmarks for scientific reasoning tasks, and SciReas-Pro, a selective subset that requires more complex reasoning.\n\nThe key findings are: (i) knowledge retrieval is a bottleneck; (ii) in-context knowledge consistently benefits reasoning models; and (iii) long CoT improves knowledge surfacing.\n\nThe paper is available on OpenReview (https://openreview.net/pdf?id=l852J55j9n) and also on arXiv. The arxiv version shows a metadata date of January 19, 2026, indicating this is a recent work."
    ],
    "durationSeconds": 5.389283913000021
  },
  "sourceToolAssistantUUID": "a88fa3a5-8e7c-40fe-b3c4-b0c02a825c5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-14T16:50:09.239Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BCYLCVwsqkLFiMRXRuTVSi`</summary>

```json
{
  "url": "https://openreview.net/forum?id=l852J55j9n",
  "prompt": "What venue was this paper submitted to? What is the decision status - accepted, rejected, under review? Show any relevant details about the submission."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cded46f-a6c7-4ea7-99eb-a2a3744cfe9f",
  "isSidechain": false,
  "requestId": "req_011Cb2ofUh3f8FKrjJZQGmRc",
  "type": "assistant",
  "uuid": "2e61fe03-5d20-4d08-8280-d1ceb549416a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012shyYiw2z6qQXdL6Ypcmaa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 47739,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 875,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 47739,
          "cache_creation_input_tokens": 875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 875
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

_source line 76 · 2026-05-14T16:50:11.448Z_

<details><summary>↩ Tool result · `toolu_01BCYLCVwsqkLFiMRXRuTVSi`</summary>

```text
# Submission Details

**Venue:** ICLR 2026 Conference

**Decision Status:** Desk Rejected

The page indicates this is a "Desk Rejected Submission," meaning the paper was rejected at an early review stage without undergoing full peer review.

**Submission Number:** 22637

**Submission Date:** September 20, 2025 (modified February 12, 2026)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e61fe03-5d20-4d08-8280-d1ceb549416a",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "e3e4f743-a059-4157-8631-e54895b5c6b1",
  "toolUseResult": {
    "bytes": 69329,
    "code": 200,
    "codeText": "OK",
    "result": "# Submission Details\n\n**Venue:** ICLR 2026 Conference\n\n**Decision Status:** Desk Rejected\n\nThe page indicates this is a \"Desk Rejected Submission,\" meaning the paper was rejected at an early review stage without undergoing full peer review.\n\n**Submission Number:** 22637\n\n**Submission Date:** September 20, 2025 (modified February 12, 2026)",
    "durationMs": 2206,
    "url": "https://openreview.net/forum?id=l852J55j9n"
  },
  "sourceToolAssistantUUID": "2e61fe03-5d20-4d08-8280-d1ceb549416a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-14T16:50:18.466Z_

<details><summary>Logged reasoning block</summary>

```text
OK so the KRUX paper was desk-rejected at ICLR 2026. The arXiv HTML version mentioned "ICML" in a header, but that might just be a formatting thing. Let me check the arXiv more carefully for any venue claim.

Actually, let me just look at what the arXiv v2 comments say.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3e4f743-a059-4157-8631-e54895b5c6b1",
  "isSidechain": false,
  "requestId": "req_011Cb2ofsPYWSSn5zKKSgiZm",
  "type": "assistant",
  "uuid": "de522484-f3a0-4ad9-8e81-73122ce1ab05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVYdChGai3iiXE1Vr3fton",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 217,
      "cache_read_input_tokens": 48614,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 217,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 48614,
          "cache_creation_input_tokens": 217,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 217
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

_source line 78 · 2026-05-14T16:50:18.834Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016bZpS6zxC613i6yPG7noNg`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.19202",
  "prompt": "What does the Comments field say? Is there any mention of a conference venue (ICML, ACL, NeurIPS, etc.)? What is the submission history - what dates were different versions uploaded?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de522484-f3a0-4ad9-8e81-73122ce1ab05",
  "isSidechain": false,
  "requestId": "req_011Cb2ofsPYWSSn5zKKSgiZm",
  "type": "assistant",
  "uuid": "6a7b5765-e32b-4a23-9de6-1cf9b9444aea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVYdChGai3iiXE1Vr3fton",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 217,
      "cache_read_input_tokens": 48614,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 217,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 48614,
          "cache_creation_input_tokens": 217,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 217
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

_source line 79 · 2026-05-14T16:50:21.855Z_

<details><summary>↩ Tool result · `toolu_016bZpS6zxC613i6yPG7noNg`</summary>

```text
# Paper Submission Details

**Comments field:** States "32 pages, 18 figures" with no conference venue mentioned.

**Conference venue:** No specific conference (ICML, ACL, NeurIPS, etc.) is referenced in the provided content.

**Submission history:**
- **Version 1:** Submitted Tuesday, August 26, 2025 at 17:04:23 UTC (296 KB)
- **Version 2:** Revised Monday, January 19, 2026 at 17:18:14 UTC (295 KB)

This appears to be an arXiv preprint without an explicitly stated conference publication venue on this page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a7b5765-e32b-4a23-9de6-1cf9b9444aea",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "2cb28fe5-996e-4e19-a957-130ef358ac33",
  "toolUseResult": {
    "bytes": 46783,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Submission Details\n\n**Comments field:** States \"32 pages, 18 figures\" with no conference venue mentioned.\n\n**Conference venue:** No specific conference (ICML, ACL, NeurIPS, etc.) is referenced in the provided content.\n\n**Submission history:**\n- **Version 1:** Submitted Tuesday, August 26, 2025 at 17:04:23 UTC (296 KB)\n- **Version 2:** Revised Monday, January 19, 2026 at 17:18:14 UTC (295 KB)\n\nThis appears to be an arXiv preprint without an explicitly stated conference publication venue on this page.",
    "durationMs": 3012,
    "url": "https://arxiv.org/abs/2508.19202"
  },
  "sourceToolAssistantUUID": "6a7b5765-e32b-4a23-9de6-1cf9b9444aea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 80 · 2026-05-14T16:50:50.820Z_

<details><summary>Logged reasoning block</summary>

```text
Good - so KRUX (arXiv 2508.19202) is a preprint only. It was desk-rejected at ICLR 2026 and doesn't claim any other venue. The earlier WebFetch that mentioned "ICML" was likely just formatting from the HTML rendering. I'll cite it as a preprint.

Now I have all the information I need. Let me compile the revised JSON.

Summary of changes needed:

1. **ProbeRAG/CLEAR venue**: Keep "ACL 2026 Findings" - arXiv v3 (April 2026) explicitly claims this. 

2. **KRUX**: Add as preprint (arXiv 2508.19202). Cite in opportunity and landscape as converging evidence for knowledge-vs-reasoning separation.

3. **Terminology**: Change "Counterfactual Probing" to "Counterfactual-Branching Probes" in title and throughout. Cite arXiv 2508.01862 to differentiate.

4. **Impact framing**: This is the big one. Need to articulate concrete design implications:
   - If evidence gaps dominate: challenges

The ICLR 2026 submission was withdrawn before acceptance, but the work found a home at ACL 2026 Findings afterward - a common trajectory for papers that don't make the cut at their first venue. Now I need to work through the design implications section, particularly how to frame the impact when evidence gaps are the dominant finding.

For the empirical side, I'm adding Qwen2.5-3B as a second checkpoint in the ablations since it's readily available on HuggingFace, which means budgeting an extra 2-3 H100 hours for that experiment. I should also incorporate findings about how confidence-based gating fails to distinguish hallucinations from genuine knowledge, and how distribution variance across benchmarks affects retrieval budget allocation - these are key insights for the reasoning-first approach to multi-hop QA.

On the references front, I'm being selective. The "Reasoning Models Know When They're Right" paper is interesting for its work on hidden state probes during reasoning, but the proposal is already dense with citations, so I'll stick with adding KRUX and the terminology disambiguation paper rather than overloading it further.

Now I'm drafting the full revised proposal as a minor change since the core problem and approach remain intact - I'm mainly strengthening the framing, fixing references, adding citations, clarifying terminology, and introducing the 3B checkpoint experiment. I need to weave KRUX in naturally, make the impact framing feel genuine rather than defensive, keep terminology consistent throughout, present the 3B experiment as a natural part of the design, and address the ProbeRAG venue concern directly.

For the title, I'm shifting from "Counterfactual Probing" to "Counterfactual-Branching Probes" to better disambiguate what we're actually doing. I also need to refine the description field to reflect all these updates, and I'm noticing the reviewer flagged an issue with the ProbeRAG/CLEAR venue claim - the paper was submitted to ICLR 2026 and withdrawn, not published in ACL 2026 Findings, so I need to correct that transparently in the proposal. on the arXiv v3 comments from April 2026, since the actual proceedings won't be available until after the conference in July. Now I'm moving on to structure the JSON response with a focus on highlighting the paper's impact.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cb28fe5-996e-4e19-a957-130ef358ac33",
  "isSidechain": false,
  "requestId": "req_011Cb2ogdtDUNo8pLdU5PD7J",
  "type": "assistant",
  "uuid": "75478f93-a8f3-4e7b-b9e3-b937e69fb2d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3h7byLGndgCJGBERfyZqB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 380,
      "cache_read_input_tokens": 48831,
      "output_tokens": 12124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 380,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12124,
          "cache_read_input_tokens": 48831,
          "cache_creation_input_tokens": 380,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 380
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

_source line 81 · 2026-05-14T16:50:55.877Z_

Now I have all the information needed. Let me synthesize the findings:

1. **ProbeRAG/CLEAR**: arXiv v3 (April 15, 2026) explicitly states "ACL 2026 Findings" in comments. ICLR 2026 was withdrawn, but ACL 2026 (July 2-7, San Diego) hasn't happened yet — proceedings aren't published. The self-reported venue claim is standard pre-conference practice.

2. **KRUX**: Preprint only (desk-rejected at ICLR 2026). Provides key converging evidence: knowledge retrieval is the critical bottleneck in scientific reasoning, with base models + KIs outperforming reasoning-enhanced models by ≥10%.

3. **Counterfactual probing** (2508.01862): Behavioral testing with counterfactual statements — completely different from our hidden-state probing after execution forking. Clear disambiguation needed.

4. **Search-R1 3B**: Confirmed — multiple Qwen2.5-3B checkpoints available on HuggingFace (PPO and GRPO variants).

The main blocker is impact framing. The reviewer wants concrete "so what" — I'll articulate specific design principles the distribution measurement enables, frame cross-dataset variance implications, and add the 3B cross-scale experiment. Let me draft the complete revision now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75478f93-a8f3-4e7b-b9e3-b937e69fb2d1",
  "isSidechain": false,
  "requestId": "req_011Cb2ogdtDUNo8pLdU5PD7J",
  "type": "assistant",
  "uuid": "6f91a2b8-d3c8-43fd-8ac7-24baa0137ba1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3h7byLGndgCJGBERfyZqB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 380,
      "cache_read_input_tokens": 48831,
      "output_tokens": 12124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 380,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12124,
          "cache_read_input_tokens": 48831,
          "cache_creation_input_tokens": 380,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 380
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

_source line 82 · 2026-05-14T16:55:09.928Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KStyQN3tmh1b9YHRGsRuhG`</summary>

````json
{
  "description": "Draft revised research JSON",
  "prompt": "I need you to help me compose a very large JSON object. I'll provide the structure and content for each field. Please output ONLY the complete JSON — no commentary before or after.\n\nHere is the complete revised research idea JSON:\n\n```json\n{\n  \"change_type\": \"minor\",\n  \"title\": \"Counterfactual-Branching Probes Disentangle Evidence Gaps from Reasoning Difficulty for Step-Level Retrieval Gating\",\n  \"core_problem\": \"Current adaptive retrieval methods for reasoning LLMs use signals that conflate two fundamentally different failure modes: evidence gaps (the model lacks factual knowledge for a step) and reasoning difficulty (the step is logically complex, and retrieval introduces noise). This conflation is not merely imprecise — it leads to systematically suboptimal retrieval decisions: a confidence-based gate cannot distinguish a model that is confidently wrong (hallucinating a missing fact) from one that genuinely knows the answer, nor can it distinguish genuine uncertainty about a logical step from uncertainty caused by a knowledge gap. The optimal action for these failure modes is opposite: evidence gaps demand retrieval even when the model appears confident, while reasoning difficulty demands suppressing retrieval even when the model appears uncertain. Probing-RAG gates retrieval via hidden-state probes with binary correctness labels. Skill-RAG routes among retrieval skills based on failure-state probing but diagnoses query-evidence misalignment, not whether retrieval should occur. ProbeRAG/CLEAR (arXiv 2510.12460; ACL 2026 Findings per arXiv v3 author-reported comments, April 2026; proceedings not yet published as ACL 2026 is July 2-7) uses a 3-layer MLP probe on decoder hidden states for sentence-level knowledge conflict detection in RAG — achieving 97–98% accuracy on MQuAKE — but targets parametric-contextual conflict, not whether a step fails due to missing knowledge vs. reasoning complexity. ReaLM-Retrieve's composite RSUS score cannot distinguish missing knowledge from logical complexity. DeepControl's information utility (novelty + effectiveness) addresses when to continue retrieving but conflates both failure sources into a single scalar. IG-Search's counterfactual baseline (random documents vs. retrieved documents) provides step-level credit assignment for search quality but does not classify WHY a step benefits from retrieval. TIPS (arXiv 2603.22293) assigns dense turn-level rewards via potential-based shaping, achieving 11.8% EM improvement — addressing credit assignment for search decisions but through RL training signals, not inference-time diagnosis. DART demonstrates that reasoning and tool-use compete during joint RL training — gradient interference between the two capabilities is measurable and harmful — but proposes an architectural fix (disentangled LoRA) rather than diagnosing failure modes at inference time. 'Disentangling Memory and Reasoning Ability in Large Language Models' (arXiv 2411.13504; ACL 2025) introduces explicit &lt;memory> and &lt;reason> tokens to decompose LLM inference into knowledge retrieval vs. logical reasoning steps, achieving 83.3% disentanglement accuracy and finding that 78–98% of errors on commonsense tasks stem from reasoning rather than memory — directly validating that the knowledge-vs-reasoning axis is trainable and separable. 'Knowledge or Reasoning?' (arXiv 2506.02126) shows that knowledge correctness and reasoning quality are separable dimensions at the step level (knowledge-accuracy correlation 0.998 vs. reasoning-accuracy 0.698 in medical QA), validating the axis we target — but operates as an offline evaluation framework using GPT-4o judges, not as an inference-time retrieval gating mechanism. KRUX (arXiv 2508.19202) probes the knowledge-vs-reasoning bottleneck by injecting Knowledge Ingredients (KIs) in-context and measuring performance delta, finding that base models with KIs outperform reasoning-enhanced models by ≥10% on scientific tasks — further validating that knowledge retrieval from parameters is a critical, separable bottleneck. 'Where Does Reasoning Break?' (arXiv 2605.13772) detects step-level hallucinations via hidden-state transport geometry with strong in-domain performance (91.0% AUROC on ProcessBench), but classifies binary correctness (hallucinated vs. correct), not failure-mode type (evidence gap vs. reasoning difficulty), and its student model collapses under distribution shift (cross-model AUROC drops to 33–58%). PRISM (arXiv 2604.16909) disentangles hallucinations into knowledge-missing, knowledge-error, reasoning-error, and instruction-following dimensions, but operates as an evaluation benchmark, not an inference-time mechanism. Critically, while 'Disentangling Memory and Reasoning' measured error distributions on commonsense tasks (finding reasoning errors dominate at 78–98%) and KRUX found knowledge is the bottleneck for scientific reasoning, no work has measured this distribution for multi-hop factual QA where retrieval is available — a setting where the failure-mode distribution directly determines the optimal design of adaptive retrieval systems. Without this measurement, the field is building retrieval gates blind to the underlying failure structure they are trying to address. No existing method provides counterfactual-branching, step-level classification of evidence gaps vs. reasoning difficulty in hidden-state space for inference-time retrieval gating.\",\n  \"opportunity\": \"Four converging lines of evidence make this the right moment for counterfactual-branching probes of retrieval failure modes, and a fifth consideration — the actionability of the resulting distribution — elevates this from a diagnostic exercise to a design-informing measurement: (1) The evidence-vs-reasoning axis is real, trainable, and task-dependent — 'Disentangling Memory and Reasoning' achieves 83.3% disentanglement accuracy with explicit memory/reason tokens on Qwen2.5-7B and finds error distributions vary dramatically by task (98.3% reasoning errors on StrategyQA vs. 78.4% on CommonsenseQA), 'Knowledge or Reasoning?' achieves step-level separation with high correlation, KRUX demonstrates that injecting task-relevant Knowledge Ingredients in-context boosts base models by ≥10% over reasoning-enhanced variants on scientific benchmarks (confirming knowledge retrieval from parameters as a separable bottleneck), PRISM's four-way hallucination taxonomy validates knowledge-vs-reasoning as a meaningful diagnostic axis, a PubMedBERT classifier separates knowledge-heavy from reasoning-heavy medical questions at 81% accuracy (arXiv 2505.11462), and Skill-RAG's representation analysis confirms failure states occupy 'structured, separable regions' in hidden-state space. (2) Hidden-state probing for RAG is technically mature — ProbeRAG/CLEAR demonstrates that 3-layer MLP probes on decoder hidden states achieve 97–98% accuracy for knowledge conflict detection, confirming that fine-grained RAG-relevant signals are linearly separable in latent space; however, no existing probe targets failure-mode type (evidence gap vs. reasoning difficulty). (3) Indiscriminate retrieval demonstrably harms reasoning — non-retrieval traces achieve 84.2% on GSM8K vs. lower with retrieval (arXiv 2602.07213), DART quantifies that reasoning and tool-use produce misaligned gradients during joint training, and IG-Search shows models adaptively learn to search conservatively on single-hop questions (1.3 calls) vs. actively on multi-hop (2.4 calls), implying retrieval value varies by step type. (4) Counterfactual and geometric methodology for step-level analysis is maturing — IG-Search uses counterfactual random-document baselines for step-level credit, TIPS demonstrates that turn-level credit assignment substantially improves training stability (11.8% EM improvement), CF-RAG (ICLR 2026) applies counterfactual reasoning to distinguish causal from correlated evidence, and 'Where Does Reasoning Break?' demonstrates that hidden-state trajectories encode step-level correctness with high fidelity (teacher AUROC 91–98%), though its cross-model generalization failure (student AUROC 33–58% under shift) motivates our within-checkpoint probing design. Note: Feng (arXiv 2508.01862) also uses the phrase 'counterfactual probing' but to mean probing model sensitivity to counterfactual input statements for hallucination detection — a behavioral technique unrelated to our approach of probing hidden states after counterfactual execution branching. We adopt the term 'counterfactual-branching probes' to clearly distinguish the two methodologies. (5) The failure-mode distribution is directly actionable for system design — if multi-hop factual QA is predominantly evidence-gap limited, this challenges the implicit assumption behind reasoning-focused approaches (e.g., longer CoT, more compute at inference) that reasoning improvement alone can solve multi-hop QA; conversely, it would validate retrieval-heavy architectures. If the distribution varies across benchmarks (e.g., HotpotQA vs. MuSiQue vs. 2WikiMultiHopQA), this reveals that these benchmarks stress fundamentally different bottlenecks, with direct implications for benchmark selection in future adaptive retrieval research and for per-dataset retrieval strategy calibration. The distribution also explains DART's finding of gradient interference: if a training corpus mixes evidence-gap steps (where retrieval helps) and reasoning-difficulty steps (where retrieval hurts), the resulting conflicting gradient signals are a predictable consequence of the mixture proportions. However, no prior work uses counterfactual branching (forking each step into retrieval vs. no-retrieval paths) to generate causal labels for training an inference-time probe that classifies failure mode type. This combination — counterfactual causal supervision + hidden-state probing + step-level failure-mode classification — fills a specific gap. Crucially, while 'Disentangling Memory and Reasoning' found that reasoning errors dominate on commonsense tasks (78–98%) and KRUX found knowledge is the primary bottleneck for scientific reasoning, this distribution is unknown for multi-hop factual QA where retrieval is available. We hypothesize the distribution is substantially different: multi-hop factual questions require chaining specific facts (entities, dates, relationships) that are more likely to exceed the model's parametric knowledge, shifting the distribution toward evidence gaps. The step-level failure distribution itself is a novel empirical measurement with direct implications for how the field designs adaptive retrieval systems — it determines the ceiling of retrieval-gating improvement, the optimal aggressiveness of retrieval, and whether single-signal gating approaches are fundamentally adequate.\",\n  \"landscape\": \"**Hidden-state probing for retrieval:** Probing-RAG (NAACL 2025) is a direct predecessor: a 5MB FC probe on intermediate layers gates retrieval at query level with binary correctness labels, reducing retrieval by ~50%. Skill-RAG (arXiv 2604.15771) extends this with per-layer probers on Gemma2-9B's posterior-2/3 layers plus a prompt-based skill router selecting among query rewriting, decomposition, evidence focusing, or exit — achieving 46.8% average accuracy and +13.6 on 2WikiMultiHopQA over Probing-RAG. ProbeRAG/CLEAR (arXiv 2510.12460; ACL 2026 Findings per arXiv v3 comments, April 2026; note: previously submitted to ICLR 2026 and withdrawn, subsequently accepted at ACL 2026 Findings; proceedings not yet published as ACL 2026 is July 2-7, 2026) probes decoder hidden states at the sentence level for knowledge conflict detection in RAG, using a 3-layer MLP probe (with 2-layer and 5-layer variants) trained on MQuAKE conflict pairs; achieves 97–98% accuracy on MQuAKE and 79–88% cross-benchmark, confirming that fine-grained RAG-relevant signals are extractable from hidden states. ProbeRAG's three-stage framework (knowledge pruning → latent conflict probing → conflict-aware attention) is methodologically adjacent but targets parametric-contextual knowledge conflicts, not failure-mode classification (evidence gap vs. reasoning difficulty). LAnR (arXiv 2604.17866) uses a lightweight MLP control head over hidden-state entropy for adaptive retrieval stopping within a latent-space RAG framework, demonstrating another instance of learned retrieval control but in a fundamentally different architecture (unified encoder-retriever-generator). **Knowledge-reasoning disentanglement:** 'Disentangling Memory and Reasoning Ability in Large Language Models' (arXiv 2411.13504; ACL 2025) is the most direct validation of our target axis: it introduces &lt;memory> and &lt;reason> tokens to decompose LLM inference, achieving 83.3% disentanglement accuracy via LoRA fine-tuning on GPT-4o-generated labels. Its error analysis reveals that reasoning errors dominate on commonsense tasks (78–98%), but the method operates via explicit token-guided generation (training-time decomposition), not via post-hoc hidden-state probing, and evaluates on commonsense QA (StrategyQA, CommonsenseQA, TruthfulQA), not multi-hop factual QA where retrieval is available. The open question — whether multi-hop factual QA shows a similar or inverted distribution — is the empirical gap we address. 'Knowledge or Reasoning?' (arXiv 2506.02126) decomposes step-level reasoning into Knowledge Index and Information Gain, finding knowledge-accuracy correlation of 0.998 vs. reasoning-accuracy of 0.698. The medical disentanglement work (arXiv 2505.11462) achieves 81% accuracy separating question types with PubMedBERT. KRUX (arXiv 2508.19202) takes a complementary black-box approach: by injecting Knowledge Ingredients (KIs) — atomic, answer-agnostic factual statements extracted from reasoning traces — in-context, it measures whether providing external knowledge resolves failures. On scientific benchmarks (SciReas/SciReas-Pro), base models with KIs outperform reasoning-enhanced models by ≥10%, establishing that parametric knowledge retrieval is the dominant bottleneck for scientific tasks. While KRUX is purely diagnostic (not an inference-time mechanism) and operates via in-context KI injection rather than hidden-state probing, it validates the same axis we target and provides a complementary data point on task-dependent failure-mode distributions: scientific tasks are knowledge-limited, commonsense tasks are reasoning-limited — we measure where multi-hop factual QA falls on this spectrum. **Hidden-state probing for step-level failures:** 'Where Does Reasoning Break?' (arXiv 2605.13772) frames step-level hallucination as transport-cost excursions in hidden-state space, achieving 91.0% AUROC (teacher) on ProcessBench. Its BiLSTM student achieves strong in-domain results (75–99.8% AUROC) but collapses under distribution shift (cross-model AUROC 33–58%). This validates that hidden states encode step-level correctness signals but targets binary correctness, not failure-mode classification. Reasoning Theater (arXiv 2603.05488) shows linear probes detect CoT divergence from internal beliefs, further confirming probing viability. PRISM (arXiv 2604.16909) decomposes hallucinations into knowledge-missing, knowledge-error, reasoning-error, and instruction-following dimensions as an evaluation framework, confirming the diagnostic axis we operationalize for inference-time use. **Terminology note:** Feng (arXiv 2508.01862) uses 'counterfactual probing' to describe probing model behavior with counterfactual input statements (generated plausible-but-incorrect claims that test model sensitivity) for hallucination detection. This is a behavioral approach operating on model outputs, fundamentally different from our counterfactual-branching probes that fork execution into retrieval/no-retrieval paths and probe the resulting hidden states. We adopt 'counterfactual-branching probes' throughout to avoid conflation. **RL-based retrieval timing:** Search-R1 (arXiv 2503.09516) trains retrieval timing via GRPO with outcome-only reward, achieving 41% improvement on Qwen2.5-7B. SLATE (arXiv 2602.23440) adds decomposed process rewards (reasoning, query, answer quality), reaching 0.461 avg EM on 7B. IG-Search (arXiv 2604.15148) introduces step-level information gain rewards using a counterfactual baseline of random documents, measuring how much retrieved documents improve answer confidence — achieving 0.430 avg EM on Qwen2.5-3B with 1.3–2.4 search calls per rollout. IG-Search's counterfactual is conceptually adjacent but serves a different purpose: it evaluates search query quality (good retrieval vs. random), not whether retrieval itself is needed vs. harmful. TIPS (arXiv 2603.22293) assigns dense turn-level rewards via potential-based reward shaping using a teacher model's answer likelihood, achieving 11.8% EM and 13.6% F1 improvements over PPO on Qwen2.5-7B across seven QA benchmarks. TIPS addresses credit assignment for search decisions through RL training, while we address it through inference-time probing — complementary approaches to the same underlying problem. **Adaptive information control:** DeepControl (arXiv 2602.01672) defines information utility U(e) = ρ·Novelty + (1-ρ)·Effectiveness and uses stopping/continuation rules, achieving 9.4% improvement over RL baselines on Qwen2.5-7B. DeepControl addresses 'when to stop retrieving' via a training-time utility signal but cannot diagnose failure mode type at inference time. **Reasoning-tool competition:** DART (arXiv 2602.00994) introduces LEAS to quantify gradient interference between reasoning and tool-use, showing they induce misaligned gradient directions. DART's disentangled LoRA achieves 6.35% avg improvement. DART validates our core premise — reasoning and retrieval compete — but proposes architectural separation during training, while we propose a diagnostic probe for inference-time gating. Our failure-mode distribution directly explains the gradient interference DART observes: the proportion of evidence-gap vs. reasoning-difficulty steps in a training corpus determines the severity of competing gradients. **Other related:** FLARE (EMNLP 2023) uses token probability thresholds. ReaLM-Retrieve (arXiv 2604.26649) achieves 71.2% F1 on MuSiQue with composite RSUS. GRADE (arXiv 2604.02830) probes knowledge gaps via gradient subspace dynamics but requires backpropagation (unsuitable for inference). SynthWorlds (arXiv 2510.24427) disentangles knowledge from reasoning at task level via synthetic corpora. **Gap:** No existing work provides counterfactual-branching, step-level probing that classifies evidence gaps vs. reasoning difficulty in hidden-state space for post-hoc inference-time retrieval gating, nor has any work empirically measured the step-level distribution of these failure modes in multi-hop factual QA — the task category where adaptive retrieval has the highest practical impact and where the distribution has direct design implications for the field.\",\n  \"approach\": \"We propose a focused empirical study with two first-class contributions: (1) a counterfactual-branching labeling methodology that produces the first step-level failure-mode distribution for multi-hop factual QA (measuring what fraction of reasoning steps are knowledge-limited vs. reasoning-limited — extending the commonsense findings of 'Disentangling Memory and Reasoning' and the scientific-task findings of KRUX to a retrieval-augmented setting), and (2) inference-time retrieval gating via lightweight probes trained on these counterfactual labels, serving as a proof-of-concept that the distribution is actionable. This is scoped as a short paper; RL integration is deferred to follow-up work.\\n\\n**Step 0 — Infrastructure Setup & Sanity Check (Day 0-1, ~2 H100h):** We pre-download the Search-R1 Qwen2.5-7B checkpoint (primary) and Qwen2.5-3B checkpoint (cross-scale validation) and configure the vLLM + veRL environment following the Search-R1 repository setup. We pre-index the Wikipedia retrieval corpus in the required jsonl format (id + contents). A minimal sanity check (10 questions, 2 rollouts per condition) validates the counterfactual generation pipeline end-to-end before committing to full-scale experiments. This front-loads infrastructure risk and ensures the remaining 9 days are dedicated to research.\\n\\n**Step 1 — Counterfactual Data Generation (~8-12 H100h):** Starting from the publicly released Search-R1 Qwen2.5-7B checkpoint, we generate reasoning traces on ~800 questions sampled from HotpotQA (400), MuSiQue (200), and 2WikiMultiHopQA (200). We identify retrieval decision points using two complementary heuristics:\\n\\n*(a) Search-present positions:* At each token where the model generates `&lt;search>` in the trace, we create a no-retrieval counterfactual by suppressing the search token and forcing continued reasoning within `&lt;think>`. These are naturally occurring decision points (~2-3 per question based on IG-Search's finding of 1.3-2.4 search calls per rollout for multi-hop tasks).\\n\\n*(b) Search-absent positions:* At sentence boundaries within `&lt;think>` blocks (detected via regex `[.?!]\\\\s` or newline-delimited segments, following the step-boundary convention in 'Where Does Reasoning Break?'), we sample up to 2 candidate insertion points per trace where the model did NOT search. Selection prioritizes sentences containing entity mentions or factual claims (detected via simple NER heuristics on the preceding sentence). At each candidate, we create a retrieval counterfactual by inserting a `&lt;search>` call using the preceding reasoning context as the query. This yields ~4-5 decision points per question and ~3,500-4,000 step instances total.\\n\\nAt each decision point, we fork execution into retrieval and no-retrieval conditions with k=5 independent rollouts per condition using vLLM batch inference (temperature=0.7, consistent with Search-R1 training). Final answer correctness is propagated backward to each fork point. Labeling uses the correctness rates r_ret and r_no_ret across rollouts: steps where r_ret ≥ 4/5 AND r_no_ret ≤ 2/5 are labeled 'evidence-gap'; steps where r_no_ret ≥ 3/5 AND r_ret ≤ r_no_ret are labeled 'reasoning-difficulty'; remaining steps are labeled 'mixed.' We additionally compute soft labels (evidence_gap_score = r_ret − r_no_ret) for regression-based probe training. **The three-class distribution is reported as a first-class empirical finding** — extending 'Disentangling Memory and Reasoning's commonsense finding (78–98% reasoning errors) and KRUX's scientific-task finding (knowledge is the dominant bottleneck) to multi-hop factual QA. We hypothesize multi-hop factual QA shows a substantially higher proportion of evidence gaps than commonsense QA, due to the requirement for chaining specific factual knowledge (entities, dates, relationships) that is more likely to exceed parametric capacity.\\n\\n**Concrete design implications of the distribution (pre-committed analyses):** (a) If evidence gaps constitute >50% of failure steps, this directly challenges the assumption that reasoning improvements alone (longer CoT, more inference compute) can substantially improve multi-hop QA — retrieval quality and timing are the binding constraint. (b) If the distribution differs significantly across HotpotQA, MuSiQue, and 2WikiMultiHopQA, this reveals that these benchmarks stress fundamentally different bottlenecks: a retrieval system optimized on one benchmark may be systematically miscalibrated for another, with implications for benchmark selection and cross-dataset evaluation in future adaptive retrieval work. (c) The proportion of evidence-gap steps sets an upper bound on the improvement achievable by adaptive retrieval gating — if only 30% of retrieval calls address evidence gaps, even a perfect gate can only reduce unnecessary retrieval by 70%, and this ceiling is itself an important measurement. (d) The mixture of evidence-gap and reasoning-difficulty steps in a dataset quantitatively predicts the severity of DART's gradient interference problem during RL training: a dataset with 50/50 split creates maximal competing gradients, while a skewed distribution (e.g., 80% evidence gaps) suggests RL training can be more stable with appropriately weighted rewards.\\n\\n**Pre-committed framing alternative:** If >50% of steps are labeled 'mixed,' we transition to a soft-label regression framework using the continuous evidence-gap score as the target, and evaluate retrieval gating via threshold on this continuous score rather than three-class classification. The failure-mode distribution analysis remains a valid contribution regardless.\\n\\n**Step 2 — Hidden-State Extraction & Probe Training (~3-5 H100h):** For each step instance, we extract hidden states from the Qwen2.5-7B model at the decision-point token position across the posterior 2/3 of layers (following Skill-RAG's methodology; informed by ProbeRAG/CLEAR's finding that deeper layers better capture RAG-relevant signals). We train two probe architectures: (a) a per-layer linear probe (comparable to the linear probe baseline in 'Where Does Reasoning Break?'), and (b) a per-layer 3-layer MLP (following ProbeRAG/CLEAR's architecture for hidden-state probing in RAG settings). Training uses 70/15/15 train/dev/test splits stratified by dataset and label class. We evaluate probe accuracy on the three-class task and on the binary gating task (retrieve = evidence-gap ∪ mixed, skip = reasoning-difficulty). **Go/no-go gate: if binary gating probe accuracy on held-out steps < 65%, we report the separability analysis and failure distribution as the primary findings (still a contribution) rather than proceeding to gating experiments.**\\n\\n**Step 3 — Inference-Time Gating Evaluation (~5-8 H100h):** Assuming probe validation succeeds, we apply the trained probe as a hard retrieval gate on the same Search-R1 checkpoint during inference (no retraining): at each step where the model generates a `&lt;search>` token, the probe classifies the hidden state; retrieval executes only if the probe predicts 'evidence-gap' or 'mixed' (above a calibrated threshold), otherwise the model continues reasoning without external input. We evaluate on held-out test portions of HotpotQA, MuSiQue, and 2WikiMultiHopQA, reporting F1, EM, and retrieval calls per question. Baselines: (1) no retrieval, (2) always retrieve (standard Search-R1), (3) Probing-RAG-style binary probe (trained on observational correctness labels rather than counterfactual-branching labels — this is the critical ablation of causal supervision), (4) FLARE-style token probability threshold. The counterfactual-vs.-observational comparison (baseline #3) is the central experiment validating whether counterfactual-branching labels provide signal beyond observational correctness.\\n\\n**Pre-committed significance thresholds:** We define minimum effect sizes for the counterfactual-vs.-observational comparison (baseline #3): counterfactual-branching labels must yield ≥3 percentage points absolute improvement in binary gating accuracy on held-out steps, OR achieve ≥5% reduction in retrieval calls per question at matched downstream F1 (within 0.5 F1 points). If both thresholds are missed, we report this as a negative result — that counterfactual supervision does not meaningfully improve over simpler observational labels — which is itself informative for the field. In this case, the paper pivots to frame the failure-mode distribution as the primary contribution and the gating comparison as a secondary finding establishing that observational labels are sufficient. This pre-commitment ensures the paper produces a clear finding regardless of outcome.\\n\\n**Step 4 — Targeted Ablations & Analysis (~5-8 H100h):** We prioritize ablations that fit within 4 pages + appendix. **Main paper:** (a) Counterfactual-branching vs. observational labels with pre-committed thresholds (key contribution validation). (b) Probe architecture comparison (linear vs. 3-layer MLP). (c) Failure-mode distribution analysis across datasets (evidence-gap vs. reasoning-difficulty vs. mixed proportions), with explicit comparison to 'Disentangling Memory and Reasoning's commonsense findings and KRUX's scientific-task findings, including concrete design implications for adaptive retrieval. **(d) Cross-scale validation: we repeat the counterfactual labeling procedure on the Search-R1 Qwen2.5-3B checkpoint (publicly available on HuggingFace, ~2-3 H100h additional) and compare the failure-mode distribution across model sizes. If the distribution is consistent (e.g., both show >50% evidence gaps), this strengthens the generalizability of the finding. If it differs (e.g., 3B shows more evidence gaps due to smaller parametric capacity), this is itself informative about scale-dependent failure modes.** **Appendix:** (e) Gating threshold sensitivity (precision-recall curve). (f) Cross-dataset transfer (train on HotpotQA, evaluate on MuSiQue). (g) t-SNE/UMAP visualization of hidden-state clusters by failure-mode type. (h) Qualitative error analysis of 'mixed' steps.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~28-40 H100h (infrastructure setup ~2h, counterfactual generation 7B ~10h + 3B ~3h, hidden state extraction ~3h, probe training <1h, evaluation ~5h, ablations ~5h, buffer ~5h)\",\n      \"gpu_utilization\": \"40-55% — GPUs idle during analysis, visualization, and paper writing\",\n      \"timeline\": \"11 days (May 14-25, 2026); Day 0-1 dedicated to infrastructure setup and sanity check, Day 2-5 counterfactual generation (7B primary, 3B parallel on Day 4-5), Day 5-7 probing and evaluation, Day 7-9 ablations including cross-scale analysis, Day 9-11 writing\",\n      \"team\": \"2 researchers (1 on data generation/evaluation pipeline, 1 on probing/analysis/writing)\",\n      \"estimated_gpu_cost\": \"$70-100 at ~$2.50/hr mid-range H100 rental\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~34-45 H100h (agent handles pipeline orchestration, human reviews label distributions and go/no-go)\",\n      \"gpu_utilization\": \"60-75% — agent queues batch jobs efficiently, human reviews at checkpoints\",\n      \"timeline\": \"9-11 days; Day 0-1 infrastructure (pre-download both checkpoints, index corpus, sanity check), Day 2-5 generation (7B + 3B), Day 6 go/no-go review, Day 7-9 evaluation, Day 10-11 writing\",\n      \"team\": \"1 researcher, ~1-2hr/day reviewing label quality, probe results, go/no-go, and writing\",\n      \"claude_api_cost\": \"$30-60 (~300-600 turns for code generation, experiment orchestration, analysis)\",\n      \"estimated_gpu_cost\": \"$85-113 at ~$2.50/hr\",\n      \"risk_note\": \"Primary risk is label distribution skew — if >60% of steps are 'mixed,' we pivot to soft-label regression as pre-committed. Human judgment on the go/no-go is essential by Day 6. Infrastructure risk mitigated by Day 0-1 sanity check.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~38-50 H100h (agent explores more threshold configurations and probe architectures, runs both 7B and 3B pipelines)\",\n      \"gpu_utilization\": \"80-90% — agent pipelines generation → extraction → training → evaluation as continuous jobs\",\n      \"timeline\": \"7-9 days with 4 H100s; Day 0-1 infrastructure, Day 2-4 generation (7B + 3B parallel), Day 5-6 probing/evaluation, Day 7-9 ablations/writing\",\n      \"team\": \"0 (initial setup only: configure Search-R1/veRL/vLLM environment, dataset loading, retrieval corpus indexing — front-loaded to Day 0-1)\",\n      \"claude_api_cost\": \"$80-150 (~800-1500 turns for autonomous experiment design, debugging, analysis, paper drafting)\",\n      \"estimated_gpu_cost\": \"$95-125 at ~$2.50/hr\",\n      \"speed_bottleneck\": \"Counterfactual generation is the bottleneck (~2-3h wall time on 4 H100s with vLLM batch for 7B; 3B runs ~40% faster); probe training and evaluation are fast (<1h each)\",\n      \"risk_note\": \"Without human judgment on whether the 'mixed' class distribution warrants pivoting the paper framing, agent may produce a mechanically correct but uncompelling paper\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 short paper via ARR May 25, 2026 (11 days — primary and only target, track: Information Retrieval and Text Mining or Question Answering)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval (NAACL 2025 Findings)\",\n    \"Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing (Preprint 2026, arXiv 2604.15771)\",\n    \"Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation [ProbeRAG/CLEAR] (ACL 2026 Findings per arXiv v3 April 2026 comments, arXiv 2510.12460)\",\n    \"When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models [ReaLM-Retrieve] (Preprint 2026, arXiv 2604.26649)\",\n    \"Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning (Preprint 2025, arXiv 2503.09516)\",\n    \"SLATE: Truncated Step-Level Sampling with Process Rewards for Retrieval-Augmented Reasoning (Preprint 2026, arXiv 2602.23440)\",\n    \"IG-Search: Step-Level Information Gain Rewards for Search-Augmented Reasoning (Preprint 2026, arXiv 2604.15148)\",\n    \"TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs (Preprint 2026, arXiv 2603.22293)\",\n    \"DeepControl: Scaling Search-Augmented LLM Reasoning via Adaptive Information Control (ICLR 2026 SPOT Workshop, arXiv 2602.01672)\",\n    \"DART: Reasoning and Tool-use Compete in Agentic RL — From Quantifying Interference to Disentangled Tuning (Preprint 2026, arXiv 2602.00994)\",\n    \"Disentangling Memory and Reasoning Ability in Large Language Models (ACL 2025, arXiv 2411.13504)\",\n    \"Knowledge or Reasoning? A Close Look at How LLMs Think Across Domains (Preprint 2025, arXiv 2506.02126)\",\n    \"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning [KRUX] (Preprint 2025, arXiv 2508.19202)\",\n    \"Counterfactual Probing for Hallucination Detection and Mitigation in Large Language Models (Preprint 2025, arXiv 2508.01862)\",\n    \"Adaptive Retrieval helps Reasoning in LLMs — but mostly if it's not used (Preprint 2025, arXiv 2602.07213)\",\n    \"Active Retrieval Augmented Generation [FLARE] (EMNLP 2023)\",\n    \"Counterfactual Reasoning for Retrieval-Augmented Generation [CF-RAG] (ICLR 2026)\",\n    \"Disentangling Knowledge and Reasoning in Medical Large Language Models (Preprint 2025, arXiv 2505.11462)\",\n    \"Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Preprint 2026, arXiv 2603.05488)\",\n    \"SynthWorlds: Controlled Parallel Worlds for Disentangling Knowledge from Reasoning (Preprint 2025, arXiv 2510.24427)\",\n    \"GRADE: Probing Knowledge Gaps in LLMs through Gradient Subspace Dynamics (Preprint 2026, arXiv 2604.02830)\",\n    \"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (Preprint 2026, arXiv 2605.13772)\",\n    \"PRISM: Probing Reasoning, Instruction, and Source Memory in LLM Hallucinations (Preprint 2026, arXiv 2604.16909)\",\n    \"Latent Abstraction for Retrieval-Augmented Generation [LAnR] (Preprint 2026, arXiv 2604.17866)\"\n  ],\n  \"description\": \"Current adaptive retrieval methods for reasoning LLMs use signals (uncertainty, token probability, composite scores) that conflate evidence gaps with reasoning difficulty, yet recent work confirms these are separable, task-dependent, and carry opposite optimal actions: evidence gaps demand retrieval even when the model appears confident (masking hallucinated knowledge), while reasoning difficulty demands suppressing retrieval even when the model appears uncertain (as retrieved context introduces noise). 'Disentangling Memory and Reasoning' (ACL 2025) achieves 83.3% disentanglement accuracy with explicit memory/reason tokens and finds 78–98% of commonsense errors stem from reasoning; KRUX (arXiv 2508.19202) finds knowledge retrieval from parameters is the dominant bottleneck for scientific tasks (base models with KIs outperform reasoning-enhanced models by ≥10%); 'Knowledge or Reasoning?' shows step-level knowledge-accuracy correlation of 0.998 vs. reasoning-accuracy 0.698; DART proves reasoning and tool-use produce competing gradients; ProbeRAG/CLEAR demonstrates 97–98% accuracy for sentence-level knowledge conflict detection via hidden-state probing; Skill-RAG finds failure states occupy structured regions in hidden-state space; and 'Where Does Reasoning Break?' demonstrates hidden states encode step-level correctness with 91% AUROC (though targeting binary correctness, not failure-mode type). We adopt the term 'counterfactual-branching probes' to distinguish from Feng (arXiv 2508.01862), who uses 'counterfactual probing' for a behavioral technique (testing model sensitivity to counterfactual input statements) unrelated to our hidden-state probing after execution forking. We present a focused empirical study with two first-class contributions. First, we introduce a counterfactual-branching labeling methodology that produces the first step-level failure-mode distribution for multi-hop factual QA: using Search-R1 checkpoints (Qwen2.5-7B primary, Qwen2.5-3B for cross-scale validation), we fork ~3,500-4,000 reasoning steps into retrieval and no-retrieval paths with k=5 rollouts each, generating causal labels ('evidence-gap,' 'reasoning-difficulty,' 'mixed'). Decision points are identified via two complementary heuristics: (a) positions where the model generated `&lt;search>` tokens (natural retrieval decisions), and (b) sentence-boundary sampling within `&lt;think>` blocks where the model did NOT search (counterfactual insertion points selected via entity/claim detection). The resulting distribution is directly actionable for system design: if evidence gaps dominate, this challenges reasoning-first approaches to multi-hop QA and validates retrieval-heavy architectures; if the distribution varies across HotpotQA, MuSiQue, and 2WikiMultiHopQA, this reveals that these benchmarks stress fundamentally different bottlenecks, with implications for benchmark selection and per-dataset strategy calibration; the evidence-gap proportion sets an upper bound on adaptive gating improvement; and the failure-mode mixture quantitatively predicts the severity of DART's gradient interference during RL training. Cross-scale comparison (7B vs. 3B) tests whether the distribution is a property of the task or the model capacity. Second, we train lightweight counterfactual-branching probes (linear and 3-layer MLP, following ProbeRAG/CLEAR's architecture) on hidden states to classify failure mode type, then apply the probe as an inference-time retrieval gate on the existing checkpoint without retraining — a proof-of-concept that the distribution is actionable: retrieve only when the probe predicts 'evidence-gap' or 'mixed,' skip retrieval when reasoning is the bottleneck. We pre-commit to significance thresholds for the central counterfactual-vs.-observational comparison: counterfactual-branching labels must yield ≥3 percentage points absolute improvement in binary gating accuracy OR ≥5% reduction in retrieval calls at matched downstream F1 (within 0.5 F1 points); if both are missed, we report a negative result, pivoting the paper to frame the failure-mode distribution as the primary contribution. If >50% of steps are 'mixed,' we pre-commit to soft-label regression on a continuous evidence-gap score. Key novelty vs. existing methods: (1) counterfactual-branching causal labels rather than observational correctness (Probing-RAG), RL reward shaping (IG-Search, TIPS, DeepControl), or explicit token-guided generation ('Disentangling Memory and Reasoning'), (2) failure-mode classification (evidence gap vs. reasoning difficulty) rather than binary correctness detection ('Where Does Reasoning Break?'), knowledge conflict detection (ProbeRAG/CLEAR), or hallucination taxonomy (PRISM), (3) post-hoc inference-time applicability without retraining, (4) cross-scale validation (7B + 3B) testing generalizability. Evaluation on HotpotQA, MuSiQue, and 2WikiMultiHopQA with baselines: no-retrieval, always-retrieve, Probing-RAG-style observational probe (critical ablation with pre-committed thresholds), and FLARE threshold. Infrastructure setup front-loaded to Day 0-1 with sanity check. Scoped as a short paper (~28-50 H100h total); RL integration deferred to follow-up.\",\n  \"project_name\": \"evid_reason_disentangle\",\n  \"source\": \"web_research\"\n}\n```\n\nPlease output this JSON exactly as-is, preserving all formatting, escape sequences, and content. Output ONLY the JSON object with no surrounding text.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f91a2b8-d3c8-43fd-8ac7-24baa0137ba1",
  "isSidechain": false,
  "requestId": "req_011Cb2ogdtDUNo8pLdU5PD7J",
  "type": "assistant",
  "uuid": "77c95cca-a9e3-48c3-a195-06204dad29b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3h7byLGndgCJGBERfyZqB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 380,
      "cache_read_input_tokens": 48831,
      "output_tokens": 12124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 380,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12124,
          "cache_read_input_tokens": 48831,
          "cache_creation_input_tokens": 380,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 380
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

_source line 83_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Counterfactual Probing Disentangles Evidence Gaps from Reasoning Diffi…",
  "leafUuid": "77c95cca-a9e3-48c3-a195-06204dad29b3",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Runtime record

_source line 84_

```json
{
  "type": "ai-title",
  "aiTitle": "Counterfactual step-level failure-mode classification for retrieval gating",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Tool result

_source line 85 · 2026-05-14T16:58:57.376Z_

<details><summary>↩ Tool result · `toolu_01KStyQN3tmh1b9YHRGsRuhG`</summary>

````text


```json
{
  "change_type": "minor",
  "title": "Counterfactual-Branching Probes Disentangle Evidence Gaps from Reasoning Difficulty for Step-Level Retrieval Gating",
  "core_problem": "Current adaptive retrieval methods for reasoning LLMs use signals that conflate two fundamentally different failure modes: evidence gaps (the model lacks factual knowledge for a step) and reasoning difficulty (the step is logically complex, and retrieval introduces noise). This conflation is not merely imprecise — it leads to systematically suboptimal retrieval decisions: a confidence-based gate cannot distinguish a model that is confidently wrong (hallucinating a missing fact) from one that genuinely knows the answer, nor can it distinguish genuine uncertainty about a logical step from uncertainty caused by a knowledge gap. The optimal action for these failure modes is opposite: evidence gaps demand retrieval even when the model appears confident, while reasoning difficulty demands suppressing retrieval even when the model appears uncertain. Probing-RAG gates retrieval via hidden-state probes with binary correctness labels. Skill-RAG routes among retrieval skills based on failure-state probing but diagnoses query-evidence misalignment, not whether retrieval should occur. ProbeRAG/CLEAR (arXiv 2510.12460; ACL 2026 Findings per arXiv v3 author-reported comments, April 2026; proceedings not yet published as ACL 2026 is July 2-7) uses a 3-layer MLP probe on decoder hidden states for sentence-level knowledge conflict detection in RAG — achieving 97–98% accuracy on MQuAKE — but targets parametric-contextual conflict, not whether a step fails due to missing knowledge vs. reasoning complexity. ReaLM-Retrieve's composite RSUS score cannot distinguish missing knowledge from logical complexity. DeepControl's information utility (novelty + effectiveness) addresses when to continue retrieving but conflates both failure sources into a single scalar. IG-Search's counterfactual baseline (random documents vs. retrieved documents) provides step-level credit assignment for search quality but does not classify WHY a step benefits from retrieval. TIPS (arXiv 2603.22293) assigns dense turn-level rewards via potential-based shaping, achieving 11.8% EM improvement — addressing credit assignment for search decisions but through RL training signals, not inference-time diagnosis. DART demonstrates that reasoning and tool-use compete during joint RL training — gradient interference between the two capabilities is measurable and harmful — but proposes an architectural fix (disentangled LoRA) rather than diagnosing failure modes at inference time. 'Disentangling Memory and Reasoning Ability in Large Language Models' (arXiv 2411.13504; ACL 2025) introduces explicit &lt;memory> and &lt;reason> tokens to decompose LLM inference into knowledge retrieval vs. logical reasoning steps, achieving 83.3% disentanglement accuracy and finding that 78–98% of errors on commonsense tasks stem from reasoning rather than memory — directly validating that the knowledge-vs-reasoning axis is trainable and separable. 'Knowledge or Reasoning?' (arXiv 2506.02126) shows that knowledge correctness and reasoning quality are separable dimensions at the step level (knowledge-accuracy correlation 0.998 vs. reasoning-accuracy 0.698 in medical QA), validating the axis we target — but operates as an offline evaluation framework using GPT-4o judges, not as an inference-time retrieval gating mechanism. KRUX (arXiv 2508.19202) probes the knowledge-vs-reasoning bottleneck by injecting Knowledge Ingredients (KIs) in-context and measuring performance delta, finding that base models with KIs outperform reasoning-enhanced models by ≥10% on scientific tasks — further validating that knowledge retrieval from parameters is a critical, separable bottleneck. 'Where Does Reasoning Break?' (arXiv 2605.13772) detects step-level hallucinations via hidden-state transport geometry with strong in-domain performance (91.0% AUROC on ProcessBench), but classifies binary correctness (hallucinated vs. correct), not failure-mode type (evidence gap vs. reasoning difficulty), and its student model collapses under distribution shift (cross-model AUROC drops to 33–58%). PRISM (arXiv 2604.16909) disentangles hallucinations into knowledge-missing, knowledge-error, reasoning-error, and instruction-following dimensions, but operates as an evaluation benchmark, not an inference-time mechanism. Critically, while 'Disentangling Memory and Reasoning' measured error distributions on commonsense tasks (finding reasoning errors dominate at 78–98%) and KRUX found knowledge is the bottleneck for scientific reasoning, no work has measured this distribution for multi-hop factual QA where retrieval is available — a setting where the failure-mode distribution directly determines the optimal design of adaptive retrieval systems. Without this measurement, the field is building retrieval gates blind to the underlying failure structure they are trying to address. No existing method provides counterfactual-branching, step-level classification of evidence gaps vs. reasoning difficulty in hidden-state space for inference-time retrieval gating.",
  "opportunity": "Four converging lines of evidence make this the right moment for counterfactual-branching probes of retrieval failure modes, and a fifth consideration — the actionability of the resulting distribution — elevates this from a diagnostic exercise to a design-informing measurement: (1) The evidence-vs-reasoning axis is real, trainable, and task-dependent — 'Disentangling Memory and Reasoning' achieves 83.3% disentanglement accuracy with explicit memory/reason tokens on Qwen2.5-7B and finds error distributions vary dramatically by task (98.3% reasoning errors on StrategyQA vs. 78.4% on CommonsenseQA), 'Knowledge or Reasoning?' achieves step-level separation with high correlation, KRUX demonstrates that injecting task-relevant Knowledge Ingredients in-context boosts base models by ≥10% over reasoning-enhanced variants on scientific benchmarks (confirming knowledge retrieval from parameters as a separable bottleneck), PRISM's four-way hallucination taxonomy validates knowledge-vs-reasoning as a meaningful diagnostic axis, a PubMedBERT classifier separates knowledge-heavy from reasoning-heavy medical questions at 81% accuracy (arXiv 2505.11462), and Skill-RAG's representation analysis confirms failure states occupy 'structured, separable regions' in hidden-state space. (2) Hidden-state probing for RAG is technically mature — ProbeRAG/CLEAR demonstrates that 3-layer MLP probes on decoder hidden states achieve 97–98% accuracy for knowledge conflict detection, confirming that fine-grained RAG-relevant signals are linearly separable in latent space; however, no existing probe targets failure-mode type (evidence gap vs. reasoning difficulty). (3) Indiscriminate retrieval demonstrably harms reasoning — non-retrieval traces achieve 84.2% on GSM8K vs. lower with retrieval (arXiv 2602.07213), DART quantifies that reasoning and tool-use produce misaligned gradients during joint training, and IG-Search shows models adaptively learn to search conservatively on single-hop questions (1.3 calls) vs. actively on multi-hop (2.4 calls), implying retrieval value varies by step type. (4) Counterfactual and geometric methodology for step-level analysis is maturing — IG-Search uses counterfactual random-document baselines for step-level credit, TIPS demonstrates that turn-level credit assignment substantially improves training stability (11.8% EM improvement), CF-RAG (ICLR 2026) applies counterfactual reasoning to distinguish causal from correlated evidence, and 'Where Does Reasoning Break?' demonstrates that hidden-state trajectories encode step-level correctness with high fidelity (teacher AUROC 91–98%), though its cross-model generalization failure (student AUROC 33–58% under shift) motivates our within-checkpoint probing design. Note: Feng (arXiv 2508.01862) also uses the phrase 'counterfactual probing' but to mean probing model sensitivity to counterfactual input statements for hallucination detection — a behavioral technique unrelated to our approach of probing hidden states after counterfactual execution branching. We adopt the term 'counterfactual-branching probes' to clearly distinguish the two methodologies. (5) The failure-mode distribution is directly actionable for system design — if multi-hop factual QA is predominantly evidence-gap limited, this challenges the implicit assumption behind reasoning-focused approaches (e.g., longer CoT, more compute at inference) that reasoning improvement alone can solve multi-hop QA; conversely, it would validate retrieval-heavy architectures. If the distribution varies across benchmarks (e.g., HotpotQA vs. MuSiQue vs. 2WikiMultiHopQA), this reveals that these benchmarks stress fundamentally different bottlenecks, with direct implications for benchmark selection in future adaptive retrieval research and for per-dataset retrieval strategy calibration. The distribution also explains DART's finding of gradient interference: if a training corpus mixes evidence-gap steps (where retrieval helps) and reasoning-difficulty steps (where retrieval hurts), the resulting conflicting gradient signals are a predictable consequence of the mixture proportions. However, no prior work uses counterfactual branching (forking each step into retrieval vs. no-retrieval paths) to generate causal labels for training an inference-time probe that classifies failure mode type. This combination — counterfactual causal supervision + hidden-state probing + step-level failure-mode classification — fills a specific gap. Crucially, while 'Disentangling Memory and Reasoning' found that reasoning errors dominate on commonsense tasks (78–98%) and KRUX found knowledge is the primary bottleneck for scientific reasoning, this distribution is unknown for multi-hop factual QA where retrieval is available. We hypothesize the distribution is substantially different: multi-hop factual questions require chaining specific facts (entities, dates, relationships) that are more likely to exceed the model's parametric knowledge, shifting the distribution toward evidence gaps. The step-level failure distribution itself is a novel empirical measurement with direct implications for how the field designs adaptive retrieval systems — it determines the ceiling of retrieval-gating improvement, the optimal aggressiveness of retrieval, and whether single-signal gating approaches are fundamentally adequate.",
  "landscape": "**Hidden-state probing for retrieval:** Probing-RAG (NAACL 2025) is a direct predecessor: a 5MB FC probe on intermediate layers gates retrieval at query level with binary correctness labels, reducing retrieval by ~50%. Skill-RAG (arXiv 2604.15771) extends this with per-layer probers on Gemma2-9B's posterior-2/3 layers plus a prompt-based skill router selecting among query rewriting, decomposition, evidence focusing, or exit — achieving 46.8% average accuracy and +13.6 on 2WikiMultiHopQA over Probing-RAG. ProbeRAG/CLEAR (arXiv 2510.12460; ACL 2026 Findings per arXiv v3 comments, April 2026; note: previously submitted to ICLR 2026 and withdrawn, subsequently accepted at ACL 2026 Findings; proceedings not yet published as ACL 2026 is July 2-7, 2026) probes decoder hidden states at the sentence level for knowledge conflict detection in RAG, using a 3-layer MLP probe (with 2-layer and 5-layer variants) trained on MQuAKE conflict pairs; achieves 97–98% accuracy on MQuAKE and 79–88% cross-benchmark, confirming that fine-grained RAG-relevant signals are extractable from hidden states. ProbeRAG's three-stage framework (knowledge pruning → latent conflict probing → conflict-aware attention) is methodologically adjacent but targets parametric-contextual knowledge conflicts, not failure-mode classification (evidence gap vs. reasoning difficulty). LAnR (arXiv 2604.17866) uses a lightweight MLP control head over hidden-state entropy for adaptive retrieval stopping within a latent-space RAG framework, demonstrating another instance of learned retrieval control but in a fundamentally different architecture (unified encoder-retriever-generator). **Knowledge-reasoning disentanglement:** 'Disentangling Memory and Reasoning Ability in Large Language Models' (arXiv 2411.13504; ACL 2025) is the most direct validation of our target axis: it introduces &lt;memory> and &lt;reason> tokens to decompose LLM inference, achieving 83.3% disentanglement accuracy via LoRA fine-tuning on GPT-4o-generated labels. Its error analysis reveals that reasoning errors dominate on commonsense tasks (78–98%), but the method operates via explicit token-guided generation (training-time decomposition), not via post-hoc hidden-state probing, and evaluates on commonsense QA (StrategyQA, CommonsenseQA, TruthfulQA), not multi-hop factual QA where retrieval is available. The open question — whether multi-hop factual QA shows a similar or inverted distribution — is the empirical gap we address. 'Knowledge or Reasoning?' (arXiv 2506.02126) decomposes step-level reasoning into Knowledge Index and Information Gain, finding knowledge-accuracy correlation of 0.998 vs. reasoning-accuracy of 0.698. The medical disentanglement work (arXiv 2505.11462) achieves 81% accuracy separating question types with PubMedBERT. KRUX (arXiv 2508.19202) takes a complementary black-box approach: by injecting Knowledge Ingredients (KIs) — atomic, answer-agnostic factual statements extracted from reasoning traces — in-context, it measures whether providing external knowledge resolves failures. On scientific benchmarks (SciReas/SciReas-Pro), base models with KIs outperform reasoning-enhanced models by ≥10%, establishing that parametric knowledge retrieval is the dominant bottleneck for scientific tasks. While KRUX is purely diagnostic (not an inference-time mechanism) and operates via in-context KI injection rather than hidden-state probing, it validates the same axis we target and provides a complementary data point on task-dependent failure-mode distributions: scientific tasks are knowledge-limited, commonsense tasks are reasoning-limited — we measure where multi-hop factual QA falls on this spectrum. **Hidden-state probing for step-level failures:** 'Where Does Reasoning Break?' (arXiv 2605.13772) frames step-level hallucination as transport-cost excursions in hidden-state space, achieving 91.0% AUROC (teacher) on ProcessBench. Its BiLSTM student achieves strong in-domain results (75–99.8% AUROC) but collapses under distribution shift (cross-model AUROC 33–58%). This validates that hidden states encode step-level correctness signals but targets binary correctness, not failure-mode classification. Reasoning Theater (arXiv 2603.05488) shows linear probes detect CoT divergence from internal beliefs, further confirming probing viability. PRISM (arXiv 2604.16909) decomposes hallucinations into knowledge-missing, knowledge-error, reasoning-error, and instruction-following dimensions as an evaluation framework, confirming the diagnostic axis we operationalize for inference-time use. **Terminology note:** Feng (arXiv 2508.01862) uses 'counterfactual probing' to describe probing model behavior with counterfactual input statements (generated plausible-but-incorrect claims that test model sensitivity) for hallucination detection. This is a behavioral approach operating on model outputs, fundamentally different from our counterfactual-branching probes that fork execution into retrieval/no-retrieval paths and probe the resulting hidden states. We adopt 'counterfactual-branching probes' throughout to avoid conflation. **RL-based retrieval timing:** Search-R1 (arXiv 2503.09516) trains retrieval timing via GRPO with outcome-only reward, achieving 41% improvement on Qwen2.5-7B. SLATE (arXiv 2602.23440) adds decomposed process rewards (reasoning, query, answer quality), reaching 0.461 avg EM on 7B. IG-Search (arXiv 2604.15148) introduces step-level information gain rewards using a counterfactual baseline of random documents, measuring how much retrieved documents improve answer confidence — achieving 0.430 avg EM on Qwen2.5-3B with 1.3–2.4 search calls per rollout. IG-Search's counterfactual is conceptually adjacent but serves a different purpose: it evaluates search query quality (good retrieval vs. random), not whether retrieval itself is needed vs. harmful. TIPS (arXiv 2603.22293) assigns dense turn-level rewards via potential-based reward shaping using a teacher model's answer likelihood, achieving 11.8% EM and 13.6% F1 improvements over PPO on Qwen2.5-7B across seven QA benchmarks. TIPS addresses credit assignment for search decisions through RL training, while we address it through inference-time probing — complementary approaches to the same underlying problem. **Adaptive information control:** DeepControl (arXiv 2602.01672) defines information utility U(e) = ρ·Novelty + (1-ρ)·Effectiveness and uses stopping/continuation rules, achieving 9.4% improvement over RL baselines on Qwen2.5-7B. DeepControl addresses 'when to stop retrieving' via a training-time utility signal but cannot diagnose failure mode type at inference time. **Reasoning-tool competition:** DART (arXiv 2602.00994) introduces LEAS to quantify gradient interference between reasoning and tool-use, showing they induce misaligned gradient directions. DART's disentangled LoRA achieves 6.35% avg improvement. DART validates our core premise — reasoning and retrieval compete — but proposes architectural separation during training, while we propose a diagnostic probe for inference-time gating. Our failure-mode distribution directly explains the gradient interference DART observes: the proportion of evidence-gap vs. reasoning-difficulty steps in a training corpus determines the severity of competing gradients. **Other related:** FLARE (EMNLP 2023) uses token probability thresholds. ReaLM-Retrieve (arXiv 2604.26649) achieves 71.2% F1 on MuSiQue with composite RSUS. GRADE (arXiv 2604.02830) probes knowledge gaps via gradient subspace dynamics but requires backpropagation (unsuitable for inference). SynthWorlds (arXiv 2510.24427) disentangles knowledge from reasoning at task level via synthetic corpora. **Gap:** No existing work provides counterfactual-branching, step-level probing that classifies evidence gaps vs. reasoning difficulty in hidden-state space for post-hoc inference-time retrieval gating, nor has any work empirically measured the step-level distribution of these failure modes in multi-hop factual QA — the task category where adaptive retrieval has the highest practical impact and where the distribution has direct design implications for the field.",
  "approach": "We propose a focused empirical study with two first-class contributions: (1) a counterfactual-branching labeling methodology that produces the first step-level failure-mode distribution for multi-hop factual QA (measuring what fraction of reasoning steps are knowledge-limited vs. reasoning-limited — extending the commonsense findings of 'Disentangling Memory and Reasoning' and the scientific-task findings of KRUX to a retrieval-augmented setting), and (2) inference-time retrieval gating via lightweight probes trained on these counterfactual labels, serving as a proof-of-concept that the distribution is actionable. This is scoped as a short paper; RL integration is deferred to follow-up work.\n\n**Step 0 — Infrastructure Setup & Sanity Check (Day 0-1, ~2 H100h):** We pre-download the Search-R1 Qwen2.5-7B checkpoint (primary) and Qwen2.5-3B checkpoint (cross-scale validation) and configure the vLLM + veRL environment following the Search-R1 repository setup. We pre-index the Wikipedia retrieval corpus in the required jsonl format (id + contents). A minimal sanity check (10 questions, 2 rollouts per condition) validates the counterfactual generation pipeline end-to-end before committing to full-scale experiments. This front-loads infrastructure risk and ensures the remaining 9 days are dedicated to research.\n\n**Step 1 — Counterfactual Data Generation (~8-12 H100h):** Starting from the publicly released Search-R1 Qwen2.5-7B checkpoint, we generate reasoning traces on ~800 questions sampled from HotpotQA (400), MuSiQue (200), and 2WikiMultiHopQA (200). We identify retrieval decision points using two complementary heuristics:\n\n*(a) Search-present positions:* At each token where the model generates `&lt;search>` in the trace, we create a no-retrieval counterfactual by suppressing the search token and forcing continued reasoning within `&lt;think>`. These are naturally occurring decision points (~2-3 per question based on IG-Search's finding of 1.3-2.4 search calls per rollout for multi-hop tasks).\n\n*(b) Search-absent positions:* At sentence boundaries within `&lt;think>` blocks (detected via regex `[.?!]\\s` or newline-delimited segments, following the step-boundary convention in 'Where Does Reasoning Break?'), we sample up to 2 candidate insertion points per trace where the model did NOT search. Selection prioritizes sentences containing entity mentions or factual claims (detected via simple NER heuristics on the preceding sentence). At each candidate, we create a retrieval counterfactual by inserting a `&lt;search>` call using the preceding reasoning context as the query. This yields ~4-5 decision points per question and ~3,500-4,000 step instances total.\n\nAt each decision point, we fork execution into retrieval and no-retrieval conditions with k=5 independent rollouts per condition using vLLM batch inference (temperature=0.7, consistent with Search-R1 training). Final answer correctness is propagated backward to each fork point. Labeling uses the correctness rates r_ret and r_no_ret across rollouts: steps where r_ret ≥ 4/5 AND r_no_ret ≤ 2/5 are labeled 'evidence-gap'; steps where r_no_ret ≥ 3/5 AND r_ret ≤ r_no_ret are labeled 'reasoning-difficulty'; remaining steps are labeled 'mixed.' We additionally compute soft labels (evidence_gap_score = r_ret − r_no_ret) for regression-based probe training. **The three-class distribution is reported as a first-class empirical finding** — extending 'Disentangling Memory and Reasoning's commonsense finding (78–98% reasoning errors) and KRUX's scientific-task finding (knowledge is the dominant bottleneck) to multi-hop factual QA. We hypothesize multi-hop factual QA shows a substantially higher proportion of evidence gaps than commonsense QA, due to the requirement for chaining specific factual knowledge (entities, dates, relationships) that is more likely to exceed parametric capacity.\n\n**Concrete design implications of the distribution (pre-committed analyses):** (a) If evidence gaps constitute >50% of failure steps, this directly challenges the assumption that reasoning improvements alone (longer CoT, more inference compute) can substantially improve multi-hop QA — retrieval quality and timing are the binding constraint. (b) If the distribution differs significantly across HotpotQA, MuSiQue, and 2WikiMultiHopQA, this reveals that these benchmarks stress fundamentally different bottlenecks: a retrieval system optimized on one benchmark may be systematically miscalibrated for another, with implications for benchmark selection and cross-dataset evaluation in future adaptive retrieval work. (c) The proportion of evidence-gap steps sets an upper bound on the improvement achievable by adaptive retrieval gating — if only 30% of retrieval calls address evidence gaps, even a perfect gate can only reduce unnecessary retrieval by 70%, and this ceiling is itself an important measurement. (d) The mixture of evidence-gap and reasoning-difficulty steps in a dataset quantitatively predicts the severity of DART's gradient interference problem during RL training: a dataset with 50/50 split creates maximal competing gradients, while a skewed distribution (e.g., 80% evidence gaps) suggests RL training can be more stable with appropriately weighted rewards.\n\n**Pre-committed framing alternative:** If >50% of steps are labeled 'mixed,' we transition to a soft-label regression framework using the continuous evidence-gap score as the target, and evaluate retrieval gating via threshold on this continuous score rather than three-class classification. The failure-mode distribution analysis remains a valid contribution regardless.\n\n**Step 2 — Hidden-State Extraction & Probe Training (~3-5 H100h):** For each step instance, we extract hidden states from the Qwen2.5-7B model at the decision-point token position across the posterior 2/3 of layers (following Skill-RAG's methodology; informed by ProbeRAG/CLEAR's finding that deeper layers better capture RAG-relevant signals). We train two probe architectures: (a) a per-layer linear probe (comparable to the linear probe baseline in 'Where Does Reasoning Break?'), and (b) a per-layer 3-layer MLP (following ProbeRAG/CLEAR's architecture for hidden-state probing in RAG settings). Training uses 70/15/15 train/dev/test splits stratified by dataset and label class. We evaluate probe accuracy on the three-class task and on the binary gating task (retrieve = evidence-gap ∪ mixed, skip = reasoning-difficulty). **Go/no-go gate: if binary gating probe accuracy on held-out steps < 65%, we report the separability analysis and failure distribution as the primary findings (still a contribution) rather than proceeding to gating experiments.**\n\n**Step 3 — Inference-Time Gating Evaluation (~5-8 H100h):** Assuming probe validation succeeds, we apply the trained probe as a hard retrieval gate on the same Search-R1 checkpoint during inference (no retraining): at each step where the model generates a `&lt;search>` token, the probe classifies the hidden state; retrieval executes only if the probe predicts 'evidence-gap' or 'mixed' (above a calibrated threshold), otherwise the model continues reasoning without external input. We evaluate on held-out test portions of HotpotQA, MuSiQue, and 2WikiMultiHopQA, reporting F1, EM, and retrieval calls per question. Baselines: (1) no retrieval, (2) always retrieve (standard Search-R1), (3) Probing-RAG-style binary probe (trained on observational correctness labels rather than counterfactual-branching labels — this is the critical ablation of causal supervision), (4) FLARE-style token probability threshold. The counterfactual-vs.-observational comparison (baseline #3) is the central experiment validating whether counterfactual-branching labels provide signal beyond observational correctness.\n\n**Pre-committed significance thresholds:** We define minimum effect sizes for the counterfactual-vs.-observational comparison (baseline #3): counterfactual-branching labels must yield ≥3 percentage points absolute improvement in binary gating accuracy on held-out steps, OR achieve ≥5% reduction in retrieval calls per question at matched downstream F1 (within 0.5 F1 points). If both thresholds are missed, we report this as a negative result — that counterfactual supervision does not meaningfully improve over simpler observational labels — which is itself informative for the field. In this case, the paper pivots to frame the failure-mode distribution as the primary contribution and the gating comparison as a secondary finding establishing that observational labels are sufficient. This pre-commitment ensures the paper produces a clear finding regardless of outcome.\n\n**Step 4 — Targeted Ablations & Analysis (~5-8 H100h):** We prioritize ablations that fit within 4 pages + appendix. **Main paper:** (a) Counterfactual-branching vs. observational labels with pre-committed thresholds (key contribution validation). (b) Probe architecture comparison (linear vs. 3-layer MLP). (c) Failure-mode distribution analysis across datasets (evidence-gap vs. reasoning-difficulty vs. mixed proportions), with explicit comparison to 'Disentangling Memory and Reasoning's commonsense findings and KRUX's scientific-task findings, including concrete design implications for adaptive retrieval. **(d) Cross-scale validation: we repeat the counterfactual labeling procedure on the Search-R1 Qwen2.5-3B checkpoint (publicly available on HuggingFace, ~2-3 H100h additional) and compare the failure-mode distribution across model sizes. If the distribution is consistent (e.g., both show >50% evidence gaps), this strengthens the generalizability of the finding. If it differs (e.g., 3B shows more evidence gaps due to smaller parametric capacity), this is itself informative about scale-dependent failure modes.** **Appendix:** (e) Gating threshold sensitivity (precision-recall curve). (f) Cross-dataset transfer (train on HotpotQA, evaluate on MuSiQue). (g) t-SNE/UMAP visualization of hidden-state clusters by failure-mode type. (h) Qualitative error analysis of 'mixed' steps.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~28-40 H100h (infrastructure setup ~2h, counterfactual generation 7B ~10h + 3B ~3h, hidden state extraction ~3h, probe training <1h, evaluation ~5h, ablations ~5h, buffer ~5h)",
      "gpu_utilization": "40-55% — GPUs idle during analysis, visualization, and paper writing",
      "timeline": "11 days (May 14-25, 2026); Day 0-1 dedicated to infrastructure setup and sanity check, Day 2-5 counterfactual generation (7B primary, 3B parallel on Day 4-5), Day 5-7 probing and evaluation, Day 7-9 ablations including cross-scale analysis, Day 9-11 writing",
      "team": "2 researchers (1 on data generation/evaluation pipeline, 1 on probing/analysis/writing)",
      "estimated_gpu_cost": "$70-100 at ~$2.50/hr mid-range H100 rental"
    },
    "human_in_loop": {
      "gpu_hours": "~34-45 H100h (agent handles pipeline orchestration, human reviews label distributions and go/no-go)",
      "gpu_utilization": "60-75% — agent queues batch jobs efficiently, human reviews at checkpoints",
      "timeline": "9-11 days; Day 0-1 infrastructure (pre-download both checkpoints, index corpus, sanity check), Day 2-5 generation (7B + 3B), Day 6 go/no-go review, Day 7-9 evaluation, Day 10-11 writing",
      "team": "1 researcher, ~1-2hr/day reviewing label quality, probe results, go/no-go, and writing",
      "claude_api_cost": "$30-60 (~300-600 turns for code generation, experiment orchestration, analysis)",
      "estimated_gpu_cost": "$85-113 at ~$2.50/hr",
      "risk_note": "Primary risk is label distribution skew — if >60% of steps are 'mixed,' we pivot to soft-label regression as pre-committed. Human judgment on the go/no-go is essential by Day 6. Infrastructure risk mitigated by Day 0-1 sanity check."
    },
    "auto_research": {
      "gpu_hours": "~38-50 H100h (agent explores more threshold configurations and probe architectures, runs both 7B and 3B pipelines)",
      "gpu_utilization": "80-90% — agent pipelines generation → extraction → training → evaluation as continuous jobs",
      "timeline": "7-9 days with 4 H100s; Day 0-1 infrastructure, Day 2-4 generation (7B + 3B parallel), Day 5-6 probing/evaluation, Day 7-9 ablations/writing",
      "team": "0 (initial setup only: configure Search-R1/veRL/vLLM environment, dataset loading, retrieval corpus indexing — front-loaded to Day 0-1)",
      "claude_api_cost": "$80-150 (~800-1500 turns for autonomous experiment design, debugging, analysis, paper drafting)",
      "estimated_gpu_cost": "$95-125 at ~$2.50/hr",
      "speed_bottleneck": "Counterfactual generation is the bottleneck (~2-3h wall time on 4 H100s with vLLM batch for 7B; 3B runs ~40% faster); probe training and evaluation are fast (<1h each)",
      "risk_note": "Without human judgment on whether the 'mixed' class distribution warrants pivoting the paper framing, agent may produce a mechanically correct but uncompelling paper"
    }
  },
  "target_venues": [
    "EMNLP 2026 short paper via ARR May 25, 2026 (11 days — primary and only target, track: Information Retrieval and Text Mining or Question Answering)"
  ],
  "level": "top-tier",
  "key_references": [
    "Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval (NAACL 2025 Findings)",
    "Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing (Preprint 2026, arXiv 2604.15771)",
    "Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation [ProbeRAG/CLEAR] (ACL 2026 Findings per arXiv v3 April 2026 comments, arXiv 2510.12460)",
    "When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models [ReaLM-Retrieve] (Preprint 2026, arXiv 2604.26649)",
    "Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning (Preprint 2025, arXiv 2503.09516)",
    "SLATE: Truncated Step-Level Sampling with Process Rewards for Retrieval-Augmented Reasoning (Preprint 2026, arXiv 2602.23440)",
    "IG-Search: Step-Level Information Gain Rewards for Search-Augmented Reasoning (Preprint 2026, arXiv 2604.15148)",
    "TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs (Preprint 2026, arXiv 2603.22293)",
    "DeepControl: Scaling Search-Augmented LLM Reasoning via Adaptive Information Control (ICLR 2026 SPOT Workshop, arXiv 2602.01672)",
    "DART: Reasoning and Tool-use Compete in Agentic RL — From Quantifying Interference to Disentangled Tuning (Preprint 2026, arXiv 2602.00994)",
    "Disentangling Memory and Reasoning Ability in Large Language Models (ACL 2025, arXiv 2411.13504)",
    "Knowledge or Reasoning? A Close Look at How LLMs Think Across Domains (Preprint 2025, arXiv 2506.02126)",
    "Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning [KRUX] (Preprint 2025, arXiv 2508.19202)",
    "Counterfactual Probing for Hallucination Detection and Mitigation in Large Language Models (Preprint 2025, arXiv 2508.01862)",
    "Adaptive Retrieval helps Reasoning in LLMs — but mostly if it's not used (Preprint 2025, arXiv 2602.07213)",
    "Active Retrieval Augmented Generation [FLARE] (EMNLP 2023)",
    "Counterfactual Reasoning for Retrieval-Augmented Generation [CF-RAG] (ICLR 2026)",
    "Disentangling Knowledge and Reasoning in Medical Large Language Models (Preprint 2025, arXiv 2505.11462)",
    "Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Preprint 2026, arXiv 2603.05488)",
    "SynthWorlds: Controlled Parallel Worlds for Disentangling Knowledge from Reasoning (Preprint 2025, arXiv 2510.24427)",
    "GRADE: Probing Knowledge Gaps in LLMs through Gradient Subspace Dynamics (Preprint 2026, arXiv 2604.02830)",
    "Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (Preprint 2026, arXiv 2605.13772)",
    "PRISM: Probing Reasoning, Instruction, and Source Memory in LLM Hallucinations (Preprint 2026, arXiv 2604.16909)",
    "Latent Abstraction for Retrieval-Augmented Generation [LAnR] (Preprint 2026, arXiv 2604.17866)"
  ],
  "description": "Current adaptive retrieval methods for reasoning LLMs use signals (uncertainty, token probability, composite scores) that conflate evidence gaps with reasoning difficulty, yet recent work confirms these are separable, task-dependent, and carry opposite optimal actions: evidence gaps demand retrieval even when the model appears confident (masking hallucinated knowledge), while reasoning difficulty demands suppressing retrieval even when the model appears uncertain (as retrieved context introduces noise). 'Disentangling Memory and Reasoning' (ACL 2025) achieves 83.3% disentanglement accuracy with explicit memory/reason tokens and finds 78–98% of commonsense errors stem from reasoning; KRUX (arXiv 2508.19202) finds knowledge retrieval from parameters is the dominant bottleneck for scientific tasks (base models with KIs outperform reasoning-enhanced models by ≥10%); 'Knowledge or Reasoning?' shows step-level knowledge-accuracy correlation of 0.998 vs. reasoning-accuracy 0.698; DART proves reasoning and tool-use produce competing gradients; ProbeRAG/CLEAR demonstrates 97–98% accuracy for sentence-level knowledge conflict detection via hidden-state probing; Skill-RAG finds failure states occupy structured regions in hidden-state space; and 'Where Does Reasoning Break?' demonstrates hidden states encode step-level correctness with 91% AUROC (though targeting binary correctness, not failure-mode type). We adopt the term 'counterfactual-branching probes' to distinguish from Feng (arXiv 2508.01862), who uses 'counterfactual probing' for a behavioral technique (testing model sensitivity to counterfactual input statements) unrelated to our hidden-state probing after execution forking. We present a focused empirical study with two first-class contributions. First, we introduce a counterfactual-branching labeling methodology that produces the first step-level failure-mode distribution for multi-hop factual QA: using Search-R1 checkpoints (Qwen2.5-7B primary, Qwen2.5-3B for cross-scale validation), we fork ~3,500-4,000 reasoning steps into retrieval and no-retrieval paths with k=5 rollouts each, generating causal labels ('evidence-gap,' 'reasoning-difficulty,' 'mixed'). Decision points are identified via two complementary heuristics: (a) positions where the model generated `&lt;search>` tokens (natural retrieval decisions), and (b) sentence-boundary sampling within `&lt;think>` blocks where the model did NOT search (counterfactual insertion points selected via entity/claim detection). The resulting distribution is directly actionable for system design: if evidence gaps dominate, this challenges reasoning-first approaches to multi-hop QA and validates retrieval-heavy architectures; if the distribution varies across HotpotQA, MuSiQue, and 2WikiMultiHopQA, this reveals that these benchmarks stress fundamentally different bottlenecks, with implications for benchmark selection and per-dataset strategy calibration; the evidence-gap proportion sets an upper bound on adaptive gating improvement; and the failure-mode mixture quantitatively predicts the severity of DART's gradient interference during RL training. Cross-scale comparison (7B vs. 3B) tests whether the distribution is a property of the task or the model capacity. Second, we train lightweight counterfactual-branching probes (linear and 3-layer MLP, following ProbeRAG/CLEAR's architecture) on hidden states to classify failure mode type, then apply the probe as an inference-time retrieval gate on the existing checkpoint without retraining — a proof-of-concept that the distribution is actionable: retrieve only when the probe predicts 'evidence-gap' or 'mixed,' skip retrieval when reasoning is the bottleneck. We pre-commit to significance thresholds for the central counterfactual-vs.-observational comparison: counterfactual-branching labels must yield ≥3 percentage points absolute improvement in binary gating accuracy OR ≥5% reduction in retrieval calls at matched downstream F1 (within 0.5 F1 points); if both are missed, we report a negative result, pivoting the paper to frame the failure-mode distribution as the primary contribution. If >50% of steps are 'mixed,' we pre-commit to soft-label regression on a continuous evidence-gap score. Key novelty vs. existing methods: (1) counterfactual-branching causal labels rather than observational correctness (Probing-RAG), RL reward shaping (IG-Search, TIPS, DeepControl), or explicit token-guided generation ('Disentangling Memory and Reasoning'), (2) failure-mode classification (evidence gap vs. reasoning difficulty) rather than binary correctness detection ('Where Does Reasoning Break?'), knowledge conflict detection (ProbeRAG/CLEAR), or hallucination taxonomy (PRISM), (3) post-hoc inference-time applicability without retraining, (4) cross-scale validation (7B + 3B) testing generalizability. Evaluation on HotpotQA, MuSiQue, and 2WikiMultiHopQA with baselines: no-retrieval, always-retrieve, Probing-RAG-style observational probe (critical ablation with pre-committed thresholds), and FLARE threshold. Infrastructure setup front-loaded to Day 0-1 with sanity check. Scoped as a short paper (~28-50 H100h total); RL integration deferred to follow-up.",
  "project_name": "evid_reason_disentangle",
  "source": "web_research"
}
```

agentId: ae17f914326d3d490 (use SendMessage with to: 'ae17f914326d3d490' to continue this agent)
&lt;usage>total_tokens: 29703
tool_uses: 0
duration_ms: 227438&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "77c95cca-a9e3-48c3-a195-06204dad29b3",
  "isSidechain": false,
  "promptId": "9f2a0e8e-882a-4c06-86a8-ece4145c2bae",
  "type": "user",
  "uuid": "80a20f18-fd44-421a-9820-a7355d2c4c14",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to help me compose a very large JSON object. I'll provide the structure and content for each field. Please output ONLY the complete JSON — no commentary before or after.\n\nHere is the complete revised research idea JSON:\n\n```json\n{\n  \"change_type\": \"minor\",\n  \"title\": \"Counterfactual-Branching Probes Disentangle Evidence Gaps from Reasoning Difficulty for Step-Level Retrieval Gating\",\n  \"core_problem\": \"Current adaptive retrieval methods for reasoning LLMs use signals that conflate two fundamentally different failure modes: evidence gaps (the model lacks factual knowledge for a step) and reasoning difficulty (the step is logically complex, and retrieval introduces noise). This conflation is not merely imprecise — it leads to systematically suboptimal retrieval decisions: a confidence-based gate cannot distinguish a model that is confidently wrong (hallucinating a missing fact) from one that genuinely knows the answer, nor can it distinguish genuine uncertainty about a logical step from uncertainty caused by a knowledge gap. The optimal action for these failure modes is opposite: evidence gaps demand retrieval even when the model appears confident, while reasoning difficulty demands suppressing retrieval even when the model appears uncertain. Probing-RAG gates retrieval via hidden-state probes with binary correctness labels. Skill-RAG routes among retrieval skills based on failure-state probing but diagnoses query-evidence misalignment, not whether retrieval should occur. ProbeRAG/CLEAR (arXiv 2510.12460; ACL 2026 Findings per arXiv v3 author-reported comments, April 2026; proceedings not yet published as ACL 2026 is July 2-7) uses a 3-layer MLP probe on decoder hidden states for sentence-level knowledge conflict detection in RAG — achieving 97–98% accuracy on MQuAKE — but targets parametric-contextual conflict, not whether a step fails due to missing knowledge vs. reasoning complexity. ReaLM-Retrieve's composite RSUS score cannot distinguish missing knowledge from logical complexity. DeepControl's information utility (novelty + effectiveness) addresses when to continue retrieving but conflates both failure sources into a single scalar. IG-Search's counterfactual baseline (random documents vs. retrieved documents) provides step-level credit assignment for search quality but does not classify WHY a step benefits from retrieval. TIPS (arXiv 2603.22293) assigns dense turn-level rewards via potential-based shaping, achieving 11.8% EM improvement — addressing credit assignment for search decisions but through RL training signals, not inference-time diagnosis. DART demonstrates that reasoning and tool-use compete during joint RL training — gradient interference between the two capabilities is measurable and harmful — but proposes an architectural fix (disentangled LoRA) rather than diagnosing failure modes at inference time. 'Disentangling Memory and Reasoning Ability in Large Language Models' (arXiv 2411.13504; ACL 2025) introduces explicit &lt;memory> and &lt;reason> tokens to decompose LLM inference into knowledge retrieval vs. logical reasoning steps, achieving 83.3% disentanglement accuracy and finding that 78–98% of errors on commonsense tasks stem from reasoning rather than memory — directly validating that the knowledge-vs-reasoning axis is trainable and separable. 'Knowledge or Reasoning?' (arXiv 2506.02126) shows that knowledge correctness and reasoning quality are separable dimensions at the step level (knowledge-accuracy correlation 0.998 vs. reasoning-accuracy 0.698 in medical QA), validating the axis we target — but operates as an offline evaluation framework using GPT-4o judges, not as an inference-time retrieval gating mechanism. KRUX (arXiv 2508.19202) probes the knowledge-vs-reasoning bottleneck by injecting Knowledge Ingredients (KIs) in-context and measuring performance delta, finding that base models with KIs outperform reasoning-enhanced models by ≥10% on scientific tasks — further validating that knowledge retrieval from parameters is a critical, separable bottleneck. 'Where Does Reasoning Break?' (arXiv 2605.13772) detects step-level hallucinations via hidden-state transport geometry with strong in-domain performance (91.0% AUROC on ProcessBench), but classifies binary correctness (hallucinated vs. correct), not failure-mode type (evidence gap vs. reasoning difficulty), and its student model collapses under distribution shift (cross-model AUROC drops to 33–58%). PRISM (arXiv 2604.16909) disentangles hallucinations into knowledge-missing, knowledge-error, reasoning-error, and instruction-following dimensions, but operates as an evaluation benchmark, not an inference-time mechanism. Critically, while 'Disentangling Memory and Reasoning' measured error distributions on commonsense tasks (finding reasoning errors dominate at 78–98%) and KRUX found knowledge is the bottleneck for scientific reasoning, no work has measured this distribution for multi-hop factual QA where retrieval is available — a setting where the failure-mode distribution directly determines the optimal design of adaptive retrieval systems. Without this measurement, the field is building retrieval gates blind to the underlying failure structure they are trying to address. No existing method provides counterfactual-branching, step-level classification of evidence gaps vs. reasoning difficulty in hidden-state space for inference-time retrieval gating.\",\n  \"opportunity\": \"Four converging lines of evidence make this the right moment for counterfactual-branching probes of retrieval failure modes, and a fifth consideration — the actionability of the resulting distribution — elevates this from a diagnostic exercise to a design-informing measurement: (1) The evidence-vs-reasoning axis is real, trainable, and task-dependent — 'Disentangling Memory and Reasoning' achieves 83.3% disentanglement accuracy with explicit memory/reason tokens on Qwen2.5-7B and finds error distributions vary dramatically by task (98.3% reasoning errors on StrategyQA vs. 78.4% on CommonsenseQA), 'Knowledge or Reasoning?' achieves step-level separation with high correlation, KRUX demonstrates that injecting task-relevant Knowledge Ingredients in-context boosts base models by ≥10% over reasoning-enhanced variants on scientific benchmarks (confirming knowledge retrieval from parameters as a separable bottleneck), PRISM's four-way hallucination taxonomy validates knowledge-vs-reasoning as a meaningful diagnostic axis, a PubMedBERT classifier separates knowledge-heavy from reasoning-heavy medical questions at 81% accuracy (arXiv 2505.11462), and Skill-RAG's representation analysis confirms failure states occupy 'structured, separable regions' in hidden-state space. (2) Hidden-state probing for RAG is technically mature — ProbeRAG/CLEAR demonstrates that 3-layer MLP probes on decoder hidden states achieve 97–98% accuracy for knowledge conflict detection, confirming that fine-grained RAG-relevant signals are linearly separable in latent space; however, no existing probe targets failure-mode type (evidence gap vs. reasoning difficulty). (3) Indiscriminate retrieval demonstrably harms reasoning — non-retrieval traces achieve 84.2% on GSM8K vs. lower with retrieval (arXiv 2602.07213), DART quantifies that reasoning and tool-use produce misaligned gradients during joint training, and IG-Search shows models adaptively learn to search conservatively on single-hop questions (1.3 calls) vs. actively on multi-hop (2.4 calls), implying retrieval value varies by step type. (4) Counterfactual and geometric methodology for step-level analysis is maturing — IG-Search uses counterfactual random-document baselines for step-level credit, TIPS demonstrates that turn-level credit assignment substantially improves training stability (11.8% EM improvement), CF-RAG (ICLR 2026) applies counterfactual reasoning to distinguish causal from correlated evidence, and 'Where Does Reasoning Break?' demonstrates that hidden-state trajectories encode step-level correctness with high fidelity (teacher AUROC 91–98%), though its cross-model generalization failure (student AUROC 33–58% under shift) motivates our within-checkpoint probing design. Note: Feng (arXiv 2508.01862) also uses the phrase 'counterfactual probing' but to mean probing model sensitivity to counterfactual input statements for hallucination detection — a behavioral technique unrelated to our approach of probing hidden states after counterfactual execution branching. We adopt the term 'counterfactual-branching probes' to clearly distinguish the two methodologies. (5) The failure-mode distribution is directly actionable for system design — if multi-hop factual QA is predominantly evidence-gap limited, this challenges the implicit assumption behind reasoning-focused approaches (e.g., longer CoT, more compute at inference) that reasoning improvement alone can solve multi-hop QA; conversely, it would validate retrieval-heavy architectures. If the distribution varies across benchmarks (e.g., HotpotQA vs. MuSiQue vs. 2WikiMultiHopQA), this reveals that these benchmarks stress fundamentally different bottlenecks, with direct implications for benchmark selection in future adaptive retrieval research and for per-dataset retrieval strategy calibration. The distribution also explains DART's finding of gradient interference: if a training corpus mixes evidence-gap steps (where retrieval helps) and reasoning-difficulty steps (where retrieval hurts), the resulting conflicting gradient signals are a predictable consequence of the mixture proportions. However, no prior work uses counterfactual branching (forking each step into retrieval vs. no-retrieval paths) to generate causal labels for training an inference-time probe that classifies failure mode type. This combination — counterfactual causal supervision + hidden-state probing + step-level failure-mode classification — fills a specific gap. Crucially, while 'Disentangling Memory and Reasoning' found that reasoning errors dominate on commonsense tasks (78–98%) and KRUX found knowledge is the primary bottleneck for scientific reasoning, this distribution is unknown for multi-hop factual QA where retrieval is available. We hypothesize the distribution is substantially different: multi-hop factual questions require chaining specific facts (entities, dates, relationships) that are more likely to exceed the model's parametric knowledge, shifting the distribution toward evidence gaps. The step-level failure distribution itself is a novel empirical measurement with direct implications for how the field designs adaptive retrieval systems — it determines the ceiling of retrieval-gating improvement, the optimal aggressiveness of retrieval, and whether single-signal gating approaches are fundamentally adequate.\",\n  \"landscape\": \"**Hidden-state probing for retrieval:** Probing-RAG (NAACL 2025) is a direct predecessor: a 5MB FC probe on intermediate layers gates retrieval at query level with binary correctness labels, reducing retrieval by ~50%. Skill-RAG (arXiv 2604.15771) extends this with per-layer probers on Gemma2-9B's posterior-2/3 layers plus a prompt-based skill router selecting among query rewriting, decomposition, evidence focusing, or exit — achieving 46.8% average accuracy and +13.6 on 2WikiMultiHopQA over Probing-RAG. ProbeRAG/CLEAR (arXiv 2510.12460; ACL 2026 Findings per arXiv v3 comments, April 2026; note: previously submitted to ICLR 2026 and withdrawn, subsequently accepted at ACL 2026 Findings; proceedings not yet published as ACL 2026 is July 2-7, 2026) probes decoder hidden states at the sentence level for knowledge conflict detection in RAG, using a 3-layer MLP probe (with 2-layer and 5-layer variants) trained on MQuAKE conflict pairs; achieves 97–98% accuracy on MQuAKE and 79–88% cross-benchmark, confirming that fine-grained RAG-relevant signals are extractable from hidden states. ProbeRAG's three-stage framework (knowledge pruning → latent conflict probing → conflict-aware attention) is methodologically adjacent but targets parametric-contextual knowledge conflicts, not failure-mode classification (evidence gap vs. reasoning difficulty). LAnR (arXiv 2604.17866) uses a lightweight MLP control head over hidden-state entropy for adaptive retrieval stopping within a latent-space RAG framework, demonstrating another instance of learned retrieval control but in a fundamentally different architecture (unified encoder-retriever-generator). **Knowledge-reasoning disentanglement:** 'Disentangling Memory and Reasoning Ability in Large Language Models' (arXiv 2411.13504; ACL 2025) is the most direct validation of our target axis: it introduces &lt;memory> and &lt;reason> tokens to decompose LLM inference, achieving 83.3% disentanglement accuracy via LoRA fine-tuning on GPT-4o-generated labels. Its error analysis reveals that reasoning errors dominate on commonsense tasks (78–98%), but the method operates via explicit token-guided generation (training-time decomposition), not via post-hoc hidden-state probing, and evaluates on commonsense QA (StrategyQA, CommonsenseQA, TruthfulQA), not multi-hop factual QA where retrieval is available. The open question — whether multi-hop factual QA shows a similar or inverted distribution — is the empirical gap we address. 'Knowledge or Reasoning?' (arXiv 2506.02126) decomposes step-level reasoning into Knowledge Index and Information Gain, finding knowledge-accuracy correlation of 0.998 vs. reasoning-accuracy of 0.698. The medical disentanglement work (arXiv 2505.11462) achieves 81% accuracy separating question types with PubMedBERT. KRUX (arXiv 2508.19202) takes a complementary black-box approach: by injecting Knowledge Ingredients (KIs) — atomic, answer-agnostic factual statements extracted from reasoning traces — in-context, it measures whether providing external knowledge resolves failures. On scientific benchmarks (SciReas/SciReas-Pro), base models with KIs outperform reasoning-enhanced models by ≥10%, establishing that parametric knowledge retrieval is the dominant bottleneck for scientific tasks. While KRUX is purely diagnostic (not an inference-time mechanism) and operates via in-context KI injection rather than hidden-state probing, it validates the same axis we target and provides a complementary data point on task-dependent failure-mode distributions: scientific tasks are knowledge-limited, commonsense tasks are reasoning-limited — we measure where multi-hop factual QA falls on this spectrum. **Hidden-state probing for step-level failures:** 'Where Does Reasoning Break?' (arXiv 2605.13772) frames step-level hallucination as transport-cost excursions in hidden-state space, achieving 91.0% AUROC (teacher) on ProcessBench. Its BiLSTM student achieves strong in-domain results (75–99.8% AUROC) but collapses under distribution shift (cross-model AUROC 33–58%). This validates that hidden states encode step-level correctness signals but targets binary correctness, not failure-mode classification. Reasoning Theater (arXiv 2603.05488) shows linear probes detect CoT divergence from internal beliefs, further confirming probing viability. PRISM (arXiv 2604.16909) decomposes hallucinations into knowledge-missing, knowledge-error, reasoning-error, and instruction-following dimensions as an evaluation framework, confirming the diagnostic axis we operationalize for inference-time use. **Terminology note:** Feng (arXiv 2508.01862) uses 'counterfactual probing' to describe probing model behavior with counterfactual input statements (generated plausible-but-incorrect claims that test model sensitivity) for hallucination detection. This is a behavioral approach operating on model outputs, fundamentally different from our counterfactual-branching probes that fork execution into retrieval/no-retrieval paths and probe the resulting hidden states. We adopt 'counterfactual-branching probes' throughout to avoid conflation. **RL-based retrieval timing:** Search-R1 (arXiv 2503.09516) trains retrieval timing via GRPO with outcome-only reward, achieving 41% improvement on Qwen2.5-7B. SLATE (arXiv 2602.23440) adds decomposed process rewards (reasoning, query, answer quality), reaching 0.461 avg EM on 7B. IG-Search (arXiv 2604.15148) introduces step-level information gain rewards using a counterfactual baseline of random documents, measuring how much retrieved documents improve answer confidence — achieving 0.430 avg EM on Qwen2.5-3B with 1.3–2.4 search calls per rollout. IG-Search's counterfactual is conceptually adjacent but serves a different purpose: it evaluates search query quality (good retrieval vs. random), not whether retrieval itself is needed vs. harmful. TIPS (arXiv 2603.22293) assigns dense turn-level rewards via potential-based reward shaping using a teacher model's answer likelihood, achieving 11.8% EM and 13.6% F1 improvements over PPO on Qwen2.5-7B across seven QA benchmarks. TIPS addresses credit assignment for search decisions through RL training, while we address it through inference-time probing — complementary approaches to the same underlying problem. **Adaptive information control:** DeepControl (arXiv 2602.01672) defines information utility U(e) = ρ·Novelty + (1-ρ)·Effectiveness and uses stopping/continuation rules, achieving 9.4% improvement over RL baselines on Qwen2.5-7B. DeepControl addresses 'when to stop retrieving' via a training-time utility signal but cannot diagnose failure mode type at inference time. **Reasoning-tool competition:** DART (arXiv 2602.00994) introduces LEAS to quantify gradient interference between reasoning and tool-use, showing they induce misaligned gradient directions. DART's disentangled LoRA achieves 6.35% avg improvement. DART validates our core premise — reasoning and retrieval compete — but proposes architectural separation during training, while we propose a diagnostic probe for inference-time gating. Our failure-mode distribution directly explains the gradient interference DART observes: the proportion of evidence-gap vs. reasoning-difficulty steps in a training corpus determines the severity of competing gradients. **Other related:** FLARE (EMNLP 2023) uses token probability thresholds. ReaLM-Retrieve (arXiv 2604.26649) achieves 71.2% F1 on MuSiQue with composite RSUS. GRADE (arXiv 2604.02830) probes knowledge gaps via gradient subspace dynamics but requires backpropagation (unsuitable for inference). SynthWorlds (arXiv 2510.24427) disentangles knowledge from reasoning at task level via synthetic corpora. **Gap:** No existing work provides counterfactual-branching, step-level probing that classifies evidence gaps vs. reasoning difficulty in hidden-state space for post-hoc inference-time retrieval gating, nor has any work empirically measured the step-level distribution of these failure modes in multi-hop factual QA — the task category where adaptive retrieval has the highest practical impact and where the distribution has direct design implications for the field.\",\n  \"approach\": \"We propose a focused empirical study with two first-class contributions: (1) a counterfactual-branching labeling methodology that produces the first step-level failure-mode distribution for multi-hop factual QA (measuring what fraction of reasoning steps are knowledge-limited vs. reasoning-limited — extending the commonsense findings of 'Disentangling Memory and Reasoning' and the scientific-task findings of KRUX to a retrieval-augmented setting), and (2) inference-time retrieval gating via lightweight probes trained on these counterfactual labels, serving as a proof-of-concept that the distribution is actionable. This is scoped as a short paper; RL integration is deferred to follow-up work.\\n\\n**Step 0 — Infrastructure Setup & Sanity Check (Day 0-1, ~2 H100h):** We pre-download the Search-R1 Qwen2.5-7B checkpoint (primary) and Qwen2.5-3B checkpoint (cross-scale validation) and configure the vLLM + veRL environment following the Search-R1 repository setup. We pre-index the Wikipedia retrieval corpus in the required jsonl format (id + contents). A minimal sanity check (10 questions, 2 rollouts per condition) validates the counterfactual generation pipeline end-to-end before committing to full-scale experiments. This front-loads infrastructure risk and ensures the remaining 9 days are dedicated to research.\\n\\n**Step 1 — Counterfactual Data Generation (~8-12 H100h):** Starting from the publicly released Search-R1 Qwen2.5-7B checkpoint, we generate reasoning traces on ~800 questions sampled from HotpotQA (400), MuSiQue (200), and 2WikiMultiHopQA (200). We identify retrieval decision points using two complementary heuristics:\\n\\n*(a) Search-present positions:* At each token where the model generates `&lt;search>` in the trace, we create a no-retrieval counterfactual by suppressing the search token and forcing continued reasoning within `&lt;think>`. These are naturally occurring decision points (~2-3 per question based on IG-Search's finding of 1.3-2.4 search calls per rollout for multi-hop tasks).\\n\\n*(b) Search-absent positions:* At sentence boundaries within `&lt;think>` blocks (detected via regex `[.?!]\\\\s` or newline-delimited segments, following the step-boundary convention in 'Where Does Reasoning Break?'), we sample up to 2 candidate insertion points per trace where the model did NOT search. Selection prioritizes sentences containing entity mentions or factual claims (detected via simple NER heuristics on the preceding sentence). At each candidate, we create a retrieval counterfactual by inserting a `&lt;search>` call using the preceding reasoning context as the query. This yields ~4-5 decision points per question and ~3,500-4,000 step instances total.\\n\\nAt each decision point, we fork execution into retrieval and no-retrieval conditions with k=5 independent rollouts per condition using vLLM batch inference (temperature=0.7, consistent with Search-R1 training). Final answer correctness is propagated backward to each fork point. Labeling uses the correctness rates r_ret and r_no_ret across rollouts: steps where r_ret ≥ 4/5 AND r_no_ret ≤ 2/5 are labeled 'evidence-gap'; steps where r_no_ret ≥ 3/5 AND r_ret ≤ r_no_ret are labeled 'reasoning-difficulty'; remaining steps are labeled 'mixed.' We additionally compute soft labels (evidence_gap_score = r_ret − r_no_ret) for regression-based probe training. **The three-class distribution is reported as a first-class empirical finding** — extending 'Disentangling Memory and Reasoning's commonsense finding (78–98% reasoning errors) and KRUX's scientific-task finding (knowledge is the dominant bottleneck) to multi-hop factual QA. We hypothesize multi-hop factual QA shows a substantially higher proportion of evidence gaps than commonsense QA, due to the requirement for chaining specific factual knowledge (entities, dates, relationships) that is more likely to exceed parametric capacity.\\n\\n**Concrete design implications of the distribution (pre-committed analyses):** (a) If evidence gaps constitute >50% of failure steps, this directly challenges the assumption that reasoning improvements alone (longer CoT, more inference compute) can substantially improve multi-hop QA — retrieval quality and timing are the binding constraint. (b) If the distribution differs significantly across HotpotQA, MuSiQue, and 2WikiMultiHopQA, this reveals that these benchmarks stress fundamentally different bottlenecks: a retrieval system optimized on one benchmark may be systematically miscalibrated for another, with implications for benchmark selection and cross-dataset evaluation in future adaptive retrieval work. (c) The proportion of evidence-gap steps sets an upper bound on the improvement achievable by adaptive retrieval gating — if only 30% of retrieval calls address evidence gaps, even a perfect gate can only reduce unnecessary retrieval by 70%, and this ceiling is itself an important measurement. (d) The mixture of evidence-gap and reasoning-difficulty steps in a dataset quantitatively predicts the severity of DART's gradient interference problem during RL training: a dataset with 50/50 split creates maximal competing gradients, while a skewed distribution (e.g., 80% evidence gaps) suggests RL training can be more stable with appropriately weighted rewards.\\n\\n**Pre-committed framing alternative:** If >50% of steps are labeled 'mixed,' we transition to a soft-label regression framework using the continuous evidence-gap score as the target, and evaluate retrieval gating via threshold on this continuous score rather than three-class classification. The failure-mode distribution analysis remains a valid contribution regardless.\\n\\n**Step 2 — Hidden-State Extraction & Probe Training (~3-5 H100h):** For each step instance, we extract hidden states from the Qwen2.5-7B model at the decision-point token position across the posterior 2/3 of layers (following Skill-RAG's methodology; informed by ProbeRAG/CLEAR's finding that deeper layers better capture RAG-relevant signals). We train two probe architectures: (a) a per-layer linear probe (comparable to the linear probe baseline in 'Where Does Reasoning Break?'), and (b) a per-layer 3-layer MLP (following ProbeRAG/CLEAR's architecture for hidden-state probing in RAG settings). Training uses 70/15/15 train/dev/test splits stratified by dataset and label class. We evaluate probe accuracy on the three-class task and on the binary gating task (retrieve = evidence-gap ∪ mixed, skip = reasoning-difficulty). **Go/no-go gate: if binary gating probe accuracy on held-out steps < 65%, we report the separability analysis and failure distribution as the primary findings (still a contribution) rather than proceeding to gating experiments.**\\n\\n**Step 3 — Inference-Time Gating Evaluation (~5-8 H100h):** Assuming probe validation succeeds, we apply the trained probe as a hard retrieval gate on the same Search-R1 checkpoint during inference (no retraining): at each step where the model generates a `&lt;search>` token, the probe classifies the hidden state; retrieval executes only if the probe predicts 'evidence-gap' or 'mixed' (above a calibrated threshold), otherwise the model continues reasoning without external input. We evaluate on held-out test portions of HotpotQA, MuSiQue, and 2WikiMultiHopQA, reporting F1, EM, and retrieval calls per question. Baselines: (1) no retrieval, (2) always retrieve (standard Search-R1), (3) Probing-RAG-style binary probe (trained on observational correctness labels rather than counterfactual-branching labels — this is the critical ablation of causal supervision), (4) FLARE-style token probability threshold. The counterfactual-vs.-observational comparison (baseline #3) is the central experiment validating whether counterfactual-branching labels provide signal beyond observational correctness.\\n\\n**Pre-committed significance thresholds:** We define minimum effect sizes for the counterfactual-vs.-observational comparison (baseline #3): counterfactual-branching labels must yield ≥3 percentage points absolute improvement in binary gating accuracy on held-out steps, OR achieve ≥5% reduction in retrieval calls per question at matched downstream F1 (within 0.5 F1 points). If both thresholds are missed, we report this as a negative result — that counterfactual supervision does not meaningfully improve over simpler observational labels — which is itself informative for the field. In this case, the paper pivots to frame the failure-mode distribution as the primary contribution and the gating comparison as a secondary finding establishing that observational labels are sufficient. This pre-commitment ensures the paper produces a clear finding regardless of outcome.\\n\\n**Step 4 — Targeted Ablations & Analysis (~5-8 H100h):** We prioritize ablations that fit within 4 pages + appendix. **Main paper:** (a) Counterfactual-branching vs. observational labels with pre-committed thresholds (key contribution validation). (b) Probe architecture comparison (linear vs. 3-layer MLP). (c) Failure-mode distribution analysis across datasets (evidence-gap vs. reasoning-difficulty vs. mixed proportions), with explicit comparison to 'Disentangling Memory and Reasoning's commonsense findings and KRUX's scientific-task findings, including concrete design implications for adaptive retrieval. **(d) Cross-scale validation: we repeat the counterfactual labeling procedure on the Search-R1 Qwen2.5-3B checkpoint (publicly available on HuggingFace, ~2-3 H100h additional) and compare the failure-mode distribution across model sizes. If the distribution is consistent (e.g., both show >50% evidence gaps), this strengthens the generalizability of the finding. If it differs (e.g., 3B shows more evidence gaps due to smaller parametric capacity), this is itself informative about scale-dependent failure modes.** **Appendix:** (e) Gating threshold sensitivity (precision-recall curve). (f) Cross-dataset transfer (train on HotpotQA, evaluate on MuSiQue). (g) t-SNE/UMAP visualization of hidden-state clusters by failure-mode type. (h) Qualitative error analysis of 'mixed' steps.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~28-40 H100h (infrastructure setup ~2h, counterfactual generation 7B ~10h + 3B ~3h, hidden state extraction ~3h, probe training <1h, evaluation ~5h, ablations ~5h, buffer ~5h)\",\n      \"gpu_utilization\": \"40-55% — GPUs idle during analysis, visualization, and paper writing\",\n      \"timeline\": \"11 days (May 14-25, 2026); Day 0-1 dedicated to infrastructure setup and sanity check, Day 2-5 counterfactual generation (7B primary, 3B parallel on Day 4-5), Day 5-7 probing and evaluation, Day 7-9 ablations including cross-scale analysis, Day 9-11 writing\",\n      \"team\": \"2 researchers (1 on data generation/evaluation pipeline, 1 on probing/analysis/writing)\",\n      \"estimated_gpu_cost\": \"$70-100 at ~$2.50/hr mid-range H100 rental\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~34-45 H100h (agent handles pipeline orchestration, human reviews label distributions and go/no-go)\",\n      \"gpu_utilization\": \"60-75% — agent queues batch jobs efficiently, human reviews at checkpoints\",\n      \"timeline\": \"9-11 days; Day 0-1 infrastructure (pre-download both checkpoints, index corpus, sanity check), Day 2-5 generation (7B + 3B), Day 6 go/no-go review, Day 7-9 evaluation, Day 10-11 writing\",\n      \"team\": \"1 researcher, ~1-2hr/day reviewing label quality, probe results, go/no-go, and writing\",\n      \"claude_api_cost\": \"$30-60 (~300-600 turns for code generation, experiment orchestration, analysis)\",\n      \"estimated_gpu_cost\": \"$85-113 at ~$2.50/hr\",\n      \"risk_note\": \"Primary risk is label distribution skew — if >60% of steps are 'mixed,' we pivot to soft-label regression as pre-committed. Human judgment on the go/no-go is essential by Day 6. Infrastructure risk mitigated by Day 0-1 sanity check.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~38-50 H100h (agent explores more threshold configurations and probe architectures, runs both 7B and 3B pipelines)\",\n      \"gpu_utilization\": \"80-90% — agent pipelines generation → extraction → training → evaluation as continuous jobs\",\n      \"timeline\": \"7-9 days with 4 H100s; Day 0-1 infrastructure, Day 2-4 generation (7B + 3B parallel), Day 5-6 probing/evaluation, Day 7-9 ablations/writing\",\n      \"team\": \"0 (initial setup only: configure Search-R1/veRL/vLLM environment, dataset loading, retrieval corpus indexing — front-loaded to Day 0-1)\",\n      \"claude_api_cost\": \"$80-150 (~800-1500 turns for autonomous experiment design, debugging, analysis, paper drafting)\",\n      \"estimated_gpu_cost\": \"$95-125 at ~$2.50/hr\",\n      \"speed_bottleneck\": \"Counterfactual generation is the bottleneck (~2-3h wall time on 4 H100s with vLLM batch for 7B; 3B runs ~40% faster); probe training and evaluation are fast (<1h each)\",\n      \"risk_note\": \"Without human judgment on whether the 'mixed' class distribution warrants pivoting the paper framing, agent may produce a mechanically correct but uncompelling paper\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 short paper via ARR May 25, 2026 (11 days — primary and only target, track: Information Retrieval and Text Mining or Question Answering)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval (NAACL 2025 Findings)\",\n    \"Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing (Preprint 2026, arXiv 2604.15771)\",\n    \"Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation [ProbeRAG/CLEAR] (ACL 2026 Findings per arXiv v3 April 2026 comments, arXiv 2510.12460)\",\n    \"When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models [ReaLM-Retrieve] (Preprint 2026, arXiv 2604.26649)\",\n    \"Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning (Preprint 2025, arXiv 2503.09516)\",\n    \"SLATE: Truncated Step-Level Sampling with Process Rewards for Retrieval-Augmented Reasoning (Preprint 2026, arXiv 2602.23440)\",\n    \"IG-Search: Step-Level Information Gain Rewards for Search-Augmented Reasoning (Preprint 2026, arXiv 2604.15148)\",\n    \"TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs (Preprint 2026, arXiv 2603.22293)\",\n    \"DeepControl: Scaling Search-Augmented LLM Reasoning via Adaptive Information Control (ICLR 2026 SPOT Workshop, arXiv 2602.01672)\",\n    \"DART: Reasoning and Tool-use Compete in Agentic RL — From Quantifying Interference to Disentangled Tuning (Preprint 2026, arXiv 2602.00994)\",\n    \"Disentangling Memory and Reasoning Ability in Large Language Models (ACL 2025, arXiv 2411.13504)\",\n    \"Knowledge or Reasoning? A Close Look at How LLMs Think Across Domains (Preprint 2025, arXiv 2506.02126)\",\n    \"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning [KRUX] (Preprint 2025, arXiv 2508.19202)\",\n    \"Counterfactual Probing for Hallucination Detection and Mitigation in Large Language Models (Preprint 2025, arXiv 2508.01862)\",\n    \"Adaptive Retrieval helps Reasoning in LLMs — but mostly if it's not used (Preprint 2025, arXiv 2602.07213)\",\n    \"Active Retrieval Augmented Generation [FLARE] (EMNLP 2023)\",\n    \"Counterfactual Reasoning for Retrieval-Augmented Generation [CF-RAG] (ICLR 2026)\",\n    \"Disentangling Knowledge and Reasoning in Medical Large Language Models (Preprint 2025, arXiv 2505.11462)\",\n    \"Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Preprint 2026, arXiv 2603.05488)\",\n    \"SynthWorlds: Controlled Parallel Worlds for Disentangling Knowledge from Reasoning (Preprint 2025, arXiv 2510.24427)\",\n    \"GRADE: Probing Knowledge Gaps in LLMs through Gradient Subspace Dynamics (Preprint 2026, arXiv 2604.02830)\",\n    \"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (Preprint 2026, arXiv 2605.13772)\",\n    \"PRISM: Probing Reasoning, Instruction, and Source Memory in LLM Hallucinations (Preprint 2026, arXiv 2604.16909)\",\n    \"Latent Abstraction for Retrieval-Augmented Generation [LAnR] (Preprint 2026, arXiv 2604.17866)\"\n  ],\n  \"description\": \"Current adaptive retrieval methods for reasoning LLMs use signals (uncertainty, token probability, composite scores) that conflate evidence gaps with reasoning difficulty, yet recent work confirms these are separable, task-dependent, and carry opposite optimal actions: evidence gaps demand retrieval even when the model appears confident (masking hallucinated knowledge), while reasoning difficulty demands suppressing retrieval even when the model appears uncertain (as retrieved context introduces noise). 'Disentangling Memory and Reasoning' (ACL 2025) achieves 83.3% disentanglement accuracy with explicit memory/reason tokens and finds 78–98% of commonsense errors stem from reasoning; KRUX (arXiv 2508.19202) finds knowledge retrieval from parameters is the dominant bottleneck for scientific tasks (base models with KIs outperform reasoning-enhanced models by ≥10%); 'Knowledge or Reasoning?' shows step-level knowledge-accuracy correlation of 0.998 vs. reasoning-accuracy 0.698; DART proves reasoning and tool-use produce competing gradients; ProbeRAG/CLEAR demonstrates 97–98% accuracy for sentence-level knowledge conflict detection via hidden-state probing; Skill-RAG finds failure states occupy structured regions in hidden-state space; and 'Where Does Reasoning Break?' demonstrates hidden states encode step-level correctness with 91% AUROC (though targeting binary correctness, not failure-mode type). We adopt the term 'counterfactual-branching probes' to distinguish from Feng (arXiv 2508.01862), who uses 'counterfactual probing' for a behavioral technique (testing model sensitivity to counterfactual input statements) unrelated to our hidden-state probing after execution forking. We present a focused empirical study with two first-class contributions. First, we introduce a counterfactual-branching labeling methodology that produces the first step-level failure-mode distribution for multi-hop factual QA: using Search-R1 checkpoints (Qwen2.5-7B primary, Qwen2.5-3B for cross-scale validation), we fork ~3,500-4,000 reasoning steps into retrieval and no-retrieval paths with k=5 rollouts each, generating causal labels ('evidence-gap,' 'reasoning-difficulty,' 'mixed'). Decision points are identified via two complementary heuristics: (a) positions where the model generated `&lt;search>` tokens (natural retrieval decisions), and (b) sentence-boundary sampling within `&lt;think>` blocks where the model did NOT search (counterfactual insertion points selected via entity/claim detection). The resulting distribution is directly actionable for system design: if evidence gaps dominate, this challenges reasoning-first approaches to multi-hop QA and validates retrieval-heavy architectures; if the distribution varies across HotpotQA, MuSiQue, and 2WikiMultiHopQA, this reveals that these benchmarks stress fundamentally different bottlenecks, with implications for benchmark selection and per-dataset strategy calibration; the evidence-gap proportion sets an upper bound on adaptive gating improvement; and the failure-mode mixture quantitatively predicts the severity of DART's gradient interference during RL training. Cross-scale comparison (7B vs. 3B) tests whether the distribution is a property of the task or the model capacity. Second, we train lightweight counterfactual-branching probes (linear and 3-layer MLP, following ProbeRAG/CLEAR's architecture) on hidden states to classify failure mode type, then apply the probe as an inference-time retrieval gate on the existing checkpoint without retraining — a proof-of-concept that the distribution is actionable: retrieve only when the probe predicts 'evidence-gap' or 'mixed,' skip retrieval when reasoning is the bottleneck. We pre-commit to significance thresholds for the central counterfactual-vs.-observational comparison: counterfactual-branching labels must yield ≥3 percentage points absolute improvement in binary gating accuracy OR ≥5% reduction in retrieval calls at matched downstream F1 (within 0.5 F1 points); if both are missed, we report a negative result, pivoting the paper to frame the failure-mode distribution as the primary contribution. If >50% of steps are 'mixed,' we pre-commit to soft-label regression on a continuous evidence-gap score. Key novelty vs. existing methods: (1) counterfactual-branching causal labels rather than observational correctness (Probing-RAG), RL reward shaping (IG-Search, TIPS, DeepControl), or explicit token-guided generation ('Disentangling Memory and Reasoning'), (2) failure-mode classification (evidence gap vs. reasoning difficulty) rather than binary correctness detection ('Where Does Reasoning Break?'), knowledge conflict detection (ProbeRAG/CLEAR), or hallucination taxonomy (PRISM), (3) post-hoc inference-time applicability without retraining, (4) cross-scale validation (7B + 3B) testing generalizability. Evaluation on HotpotQA, MuSiQue, and 2WikiMultiHopQA with baselines: no-retrieval, always-retrieve, Probing-RAG-style observational probe (critical ablation with pre-committed thresholds), and FLARE threshold. Infrastructure setup front-loaded to Day 0-1 with sanity check. Scoped as a short paper (~28-50 H100h total); RL integration deferred to follow-up.\",\n  \"project_name\": \"evid_reason_disentangle\",\n  \"source\": \"web_research\"\n}\n```\n\nPlease output this JSON exactly as-is, preserving all formatting, escape sequences, and content. Output ONLY the JSON object with no surrounding text.\n",
    "agentId": "ae17f914326d3d490",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\n```json\n{\n  \"change_type\": \"minor\",\n  \"title\": \"Counterfactual-Branching Probes Disentangle Evidence Gaps from Reasoning Difficulty for Step-Level Retrieval Gating\",\n  \"core_problem\": \"Current adaptive retrieval methods for reasoning LLMs use signals that conflate two fundamentally different failure modes: evidence gaps (the model lacks factual knowledge for a step) and reasoning difficulty (the step is logically complex, and retrieval introduces noise). This conflation is not merely imprecise — it leads to systematically suboptimal retrieval decisions: a confidence-based gate cannot distinguish a model that is confidently wrong (hallucinating a missing fact) from one that genuinely knows the answer, nor can it distinguish genuine uncertainty about a logical step from uncertainty caused by a knowledge gap. The optimal action for these failure modes is opposite: evidence gaps demand retrieval even when the model appears confident, while reasoning difficulty demands suppressing retrieval even when the model appears uncertain. Probing-RAG gates retrieval via hidden-state probes with binary correctness labels. Skill-RAG routes among retrieval skills based on failure-state probing but diagnoses query-evidence misalignment, not whether retrieval should occur. ProbeRAG/CLEAR (arXiv 2510.12460; ACL 2026 Findings per arXiv v3 author-reported comments, April 2026; proceedings not yet published as ACL 2026 is July 2-7) uses a 3-layer MLP probe on decoder hidden states for sentence-level knowledge conflict detection in RAG — achieving 97–98% accuracy on MQuAKE — but targets parametric-contextual conflict, not whether a step fails due to missing knowledge vs. reasoning complexity. ReaLM-Retrieve's composite RSUS score cannot distinguish missing knowledge from logical complexity. DeepControl's information utility (novelty + effectiveness) addresses when to continue retrieving but conflates both failure sources into a single scalar. IG-Search's counterfactual baseline (random documents vs. retrieved documents) provides step-level credit assignment for search quality but does not classify WHY a step benefits from retrieval. TIPS (arXiv 2603.22293) assigns dense turn-level rewards via potential-based shaping, achieving 11.8% EM improvement — addressing credit assignment for search decisions but through RL training signals, not inference-time diagnosis. DART demonstrates that reasoning and tool-use compete during joint RL training — gradient interference between the two capabilities is measurable and harmful — but proposes an architectural fix (disentangled LoRA) rather than diagnosing failure modes at inference time. 'Disentangling Memory and Reasoning Ability in Large Language Models' (arXiv 2411.13504; ACL 2025) introduces explicit &lt;memory> and &lt;reason> tokens to decompose LLM inference into knowledge retrieval vs. logical reasoning steps, achieving 83.3% disentanglement accuracy and finding that 78–98% of errors on commonsense tasks stem from reasoning rather than memory — directly validating that the knowledge-vs-reasoning axis is trainable and separable. 'Knowledge or Reasoning?' (arXiv 2506.02126) shows that knowledge correctness and reasoning quality are separable dimensions at the step level (knowledge-accuracy correlation 0.998 vs. reasoning-accuracy 0.698 in medical QA), validating the axis we target — but operates as an offline evaluation framework using GPT-4o judges, not as an inference-time retrieval gating mechanism. KRUX (arXiv 2508.19202) probes the knowledge-vs-reasoning bottleneck by injecting Knowledge Ingredients (KIs) in-context and measuring performance delta, finding that base models with KIs outperform reasoning-enhanced models by ≥10% on scientific tasks — further validating that knowledge retrieval from parameters is a critical, separable bottleneck. 'Where Does Reasoning Break?' (arXiv 2605.13772) detects step-level hallucinations via hidden-state transport geometry with strong in-domain performance (91.0% AUROC on ProcessBench), but classifies binary correctness (hallucinated vs. correct), not failure-mode type (evidence gap vs. reasoning difficulty), and its student model collapses under distribution shift (cross-model AUROC drops to 33–58%). PRISM (arXiv 2604.16909) disentangles hallucinations into knowledge-missing, knowledge-error, reasoning-error, and instruction-following dimensions, but operates as an evaluation benchmark, not an inference-time mechanism. Critically, while 'Disentangling Memory and Reasoning' measured error distributions on commonsense tasks (finding reasoning errors dominate at 78–98%) and KRUX found knowledge is the bottleneck for scientific reasoning, no work has measured this distribution for multi-hop factual QA where retrieval is available — a setting where the failure-mode distribution directly determines the optimal design of adaptive retrieval systems. Without this measurement, the field is building retrieval gates blind to the underlying failure structure they are trying to address. No existing method provides counterfactual-branching, step-level classification of evidence gaps vs. reasoning difficulty in hidden-state space for inference-time retrieval gating.\",\n  \"opportunity\": \"Four converging lines of evidence make this the right moment for counterfactual-branching probes of retrieval failure modes, and a fifth consideration — the actionability of the resulting distribution — elevates this from a diagnostic exercise to a design-informing measurement: (1) The evidence-vs-reasoning axis is real, trainable, and task-dependent — 'Disentangling Memory and Reasoning' achieves 83.3% disentanglement accuracy with explicit memory/reason tokens on Qwen2.5-7B and finds error distributions vary dramatically by task (98.3% reasoning errors on StrategyQA vs. 78.4% on CommonsenseQA), 'Knowledge or Reasoning?' achieves step-level separation with high correlation, KRUX demonstrates that injecting task-relevant Knowledge Ingredients in-context boosts base models by ≥10% over reasoning-enhanced variants on scientific benchmarks (confirming knowledge retrieval from parameters as a separable bottleneck), PRISM's four-way hallucination taxonomy validates knowledge-vs-reasoning as a meaningful diagnostic axis, a PubMedBERT classifier separates knowledge-heavy from reasoning-heavy medical questions at 81% accuracy (arXiv 2505.11462), and Skill-RAG's representation analysis confirms failure states occupy 'structured, separable regions' in hidden-state space. (2) Hidden-state probing for RAG is technically mature — ProbeRAG/CLEAR demonstrates that 3-layer MLP probes on decoder hidden states achieve 97–98% accuracy for knowledge conflict detection, confirming that fine-grained RAG-relevant signals are linearly separable in latent space; however, no existing probe targets failure-mode type (evidence gap vs. reasoning difficulty). (3) Indiscriminate retrieval demonstrably harms reasoning — non-retrieval traces achieve 84.2% on GSM8K vs. lower with retrieval (arXiv 2602.07213), DART quantifies that reasoning and tool-use produce misaligned gradients during joint training, and IG-Search shows models adaptively learn to search conservatively on single-hop questions (1.3 calls) vs. actively on multi-hop (2.4 calls), implying retrieval value varies by step type. (4) Counterfactual and geometric methodology for step-level analysis is maturing — IG-Search uses counterfactual random-document baselines for step-level credit, TIPS demonstrates that turn-level credit assignment substantially improves training stability (11.8% EM improvement), CF-RAG (ICLR 2026) applies counterfactual reasoning to distinguish causal from correlated evidence, and 'Where Does Reasoning Break?' demonstrates that hidden-state trajectories encode step-level correctness with high fidelity (teacher AUROC 91–98%), though its cross-model generalization failure (student AUROC 33–58% under shift) motivates our within-checkpoint probing design. Note: Feng (arXiv 2508.01862) also uses the phrase 'counterfactual probing' but to mean probing model sensitivity to counterfactual input statements for hallucination detection — a behavioral technique unrelated to our approach of probing hidden states after counterfactual execution branching. We adopt the term 'counterfactual-branching probes' to clearly distinguish the two methodologies. (5) The failure-mode distribution is directly actionable for system design — if multi-hop factual QA is predominantly evidence-gap limited, this challenges the implicit assumption behind reasoning-focused approaches (e.g., longer CoT, more compute at inference) that reasoning improvement alone can solve multi-hop QA; conversely, it would validate retrieval-heavy architectures. If the distribution varies across benchmarks (e.g., HotpotQA vs. MuSiQue vs. 2WikiMultiHopQA), this reveals that these benchmarks stress fundamentally different bottlenecks, with direct implications for benchmark selection in future adaptive retrieval research and for per-dataset retrieval strategy calibration. The distribution also explains DART's finding of gradient interference: if a training corpus mixes evidence-gap steps (where retrieval helps) and reasoning-difficulty steps (where retrieval hurts), the resulting conflicting gradient signals are a predictable consequence of the mixture proportions. However, no prior work uses counterfactual branching (forking each step into retrieval vs. no-retrieval paths) to generate causal labels for training an inference-time probe that classifies failure mode type. This combination — counterfactual causal supervision + hidden-state probing + step-level failure-mode classification — fills a specific gap. Crucially, while 'Disentangling Memory and Reasoning' found that reasoning errors dominate on commonsense tasks (78–98%) and KRUX found knowledge is the primary bottleneck for scientific reasoning, this distribution is unknown for multi-hop factual QA where retrieval is available. We hypothesize the distribution is substantially different: multi-hop factual questions require chaining specific facts (entities, dates, relationships) that are more likely to exceed the model's parametric knowledge, shifting the distribution toward evidence gaps. The step-level failure distribution itself is a novel empirical measurement with direct implications for how the field designs adaptive retrieval systems — it determines the ceiling of retrieval-gating improvement, the optimal aggressiveness of retrieval, and whether single-signal gating approaches are fundamentally adequate.\",\n  \"landscape\": \"**Hidden-state probing for retrieval:** Probing-RAG (NAACL 2025) is a direct predecessor: a 5MB FC probe on intermediate layers gates retrieval at query level with binary correctness labels, reducing retrieval by ~50%. Skill-RAG (arXiv 2604.15771) extends this with per-layer probers on Gemma2-9B's posterior-2/3 layers plus a prompt-based skill router selecting among query rewriting, decomposition, evidence focusing, or exit — achieving 46.8% average accuracy and +13.6 on 2WikiMultiHopQA over Probing-RAG. ProbeRAG/CLEAR (arXiv 2510.12460; ACL 2026 Findings per arXiv v3 comments, April 2026; note: previously submitted to ICLR 2026 and withdrawn, subsequently accepted at ACL 2026 Findings; proceedings not yet published as ACL 2026 is July 2-7, 2026) probes decoder hidden states at the sentence level for knowledge conflict detection in RAG, using a 3-layer MLP probe (with 2-layer and 5-layer variants) trained on MQuAKE conflict pairs; achieves 97–98% accuracy on MQuAKE and 79–88% cross-benchmark, confirming that fine-grained RAG-relevant signals are extractable from hidden states. ProbeRAG's three-stage framework (knowledge pruning → latent conflict probing → conflict-aware attention) is methodologically adjacent but targets parametric-contextual knowledge conflicts, not failure-mode classification (evidence gap vs. reasoning difficulty). LAnR (arXiv 2604.17866) uses a lightweight MLP control head over hidden-state entropy for adaptive retrieval stopping within a latent-space RAG framework, demonstrating another instance of learned retrieval control but in a fundamentally different architecture (unified encoder-retriever-generator). **Knowledge-reasoning disentanglement:** 'Disentangling Memory and Reasoning Ability in Large Language Models' (arXiv 2411.13504; ACL 2025) is the most direct validation of our target axis: it introduces &lt;memory> and &lt;reason> tokens to decompose LLM inference, achieving 83.3% disentanglement accuracy via LoRA fine-tuning on GPT-4o-generated labels. Its error analysis reveals that reasoning errors dominate on commonsense tasks (78–98%), but the method operates via explicit token-guided generation (training-time decomposition), not via post-hoc hidden-state probing, and evaluates on commonsense QA (StrategyQA, CommonsenseQA, TruthfulQA), not multi-hop factual QA where retrieval is available. The open question — whether multi-hop factual QA shows a similar or inverted distribution — is the empirical gap we address. 'Knowledge or Reasoning?' (arXiv 2506.02126) decomposes step-level reasoning into Knowledge Index and Information Gain, finding knowledge-accuracy correlation of 0.998 vs. reasoning-accuracy of 0.698. The medical disentanglement work (arXiv 2505.11462) achieves 81% accuracy separating question types with PubMedBERT. KRUX (arXiv 2508.19202) takes a complementary black-box approach: by injecting Knowledge Ingredients (KIs) — atomic, answer-agnostic factual statements extracted from reasoning traces — in-context, it measures whether providing external knowledge resolves failures. On scientific benchmarks (SciReas/SciReas-Pro), base models with KIs outperform reasoning-enhanced models by ≥10%, establishing that parametric knowledge retrieval is the dominant bottleneck for scientific tasks. While KRUX is purely diagnostic (not an inference-time mechanism) and operates via in-context KI injection rather than hidden-state probing, it validates the same axis we target and provides a complementary data point on task-dependent failure-mode distributions: scientific tasks are knowledge-limited, commonsense tasks are reasoning-limited — we measure where multi-hop factual QA falls on this spectrum. **Hidden-state probing for step-level failures:** 'Where Does Reasoning Break?' (arXiv 2605.13772) frames step-level hallucination as transport-cost excursions in hidden-state space, achieving 91.0% AUROC (teacher) on ProcessBench. Its BiLSTM student achieves strong in-domain results (75–99.8% AUROC) but collapses under distribution shift (cross-model AUROC 33–58%). This validates that hidden states encode step-level correctness signals but targets binary correctness, not failure-mode classification. Reasoning Theater (arXiv 2603.05488) shows linear probes detect CoT divergence from internal beliefs, further confirming probing viability. PRISM (arXiv 2604.16909) decomposes hallucinations into knowledge-missing, knowledge-error, reasoning-error, and instruction-following dimensions as an evaluation framework, confirming the diagnostic axis we operationalize for inference-time use. **Terminology note:** Feng (arXiv 2508.01862) uses 'counterfactual probing' to describe probing model behavior with counterfactual input statements (generated plausible-but-incorrect claims that test model sensitivity) for hallucination detection. This is a behavioral approach operating on model outputs, fundamentally different from our counterfactual-branching probes that fork execution into retrieval/no-retrieval paths and probe the resulting hidden states. We adopt 'counterfactual-branching probes' throughout to avoid conflation. **RL-based retrieval timing:** Search-R1 (arXiv 2503.09516) trains retrieval timing via GRPO with outcome-only reward, achieving 41% improvement on Qwen2.5-7B. SLATE (arXiv 2602.23440) adds decomposed process rewards (reasoning, query, answer quality), reaching 0.461 avg EM on 7B. IG-Search (arXiv 2604.15148) introduces step-level information gain rewards using a counterfactual baseline of random documents, measuring how much retrieved documents improve answer confidence — achieving 0.430 avg EM on Qwen2.5-3B with 1.3–2.4 search calls per rollout. IG-Search's counterfactual is conceptually adjacent but serves a different purpose: it evaluates search query quality (good retrieval vs. random), not whether retrieval itself is needed vs. harmful. TIPS (arXiv 2603.22293) assigns dense turn-level rewards via potential-based reward shaping using a teacher model's answer likelihood, achieving 11.8% EM and 13.6% F1 improvements over PPO on Qwen2.5-7B across seven QA benchmarks. TIPS addresses credit assignment for search decisions through RL training, while we address it through inference-time probing — complementary approaches to the same underlying problem. **Adaptive information control:** DeepControl (arXiv 2602.01672) defines information utility U(e) = ρ·Novelty + (1-ρ)·Effectiveness and uses stopping/continuation rules, achieving 9.4% improvement over RL baselines on Qwen2.5-7B. DeepControl addresses 'when to stop retrieving' via a training-time utility signal but cannot diagnose failure mode type at inference time. **Reasoning-tool competition:** DART (arXiv 2602.00994) introduces LEAS to quantify gradient interference between reasoning and tool-use, showing they induce misaligned gradient directions. DART's disentangled LoRA achieves 6.35% avg improvement. DART validates our core premise — reasoning and retrieval compete — but proposes architectural separation during training, while we propose a diagnostic probe for inference-time gating. Our failure-mode distribution directly explains the gradient interference DART observes: the proportion of evidence-gap vs. reasoning-difficulty steps in a training corpus determines the severity of competing gradients. **Other related:** FLARE (EMNLP 2023) uses token probability thresholds. ReaLM-Retrieve (arXiv 2604.26649) achieves 71.2% F1 on MuSiQue with composite RSUS. GRADE (arXiv 2604.02830) probes knowledge gaps via gradient subspace dynamics but requires backpropagation (unsuitable for inference). SynthWorlds (arXiv 2510.24427) disentangles knowledge from reasoning at task level via synthetic corpora. **Gap:** No existing work provides counterfactual-branching, step-level probing that classifies evidence gaps vs. reasoning difficulty in hidden-state space for post-hoc inference-time retrieval gating, nor has any work empirically measured the step-level distribution of these failure modes in multi-hop factual QA — the task category where adaptive retrieval has the highest practical impact and where the distribution has direct design implications for the field.\",\n  \"approach\": \"We propose a focused empirical study with two first-class contributions: (1) a counterfactual-branching labeling methodology that produces the first step-level failure-mode distribution for multi-hop factual QA (measuring what fraction of reasoning steps are knowledge-limited vs. reasoning-limited — extending the commonsense findings of 'Disentangling Memory and Reasoning' and the scientific-task findings of KRUX to a retrieval-augmented setting), and (2) inference-time retrieval gating via lightweight probes trained on these counterfactual labels, serving as a proof-of-concept that the distribution is actionable. This is scoped as a short paper; RL integration is deferred to follow-up work.\\n\\n**Step 0 — Infrastructure Setup & Sanity Check (Day 0-1, ~2 H100h):** We pre-download the Search-R1 Qwen2.5-7B checkpoint (primary) and Qwen2.5-3B checkpoint (cross-scale validation) and configure the vLLM + veRL environment following the Search-R1 repository setup. We pre-index the Wikipedia retrieval corpus in the required jsonl format (id + contents). A minimal sanity check (10 questions, 2 rollouts per condition) validates the counterfactual generation pipeline end-to-end before committing to full-scale experiments. This front-loads infrastructure risk and ensures the remaining 9 days are dedicated to research.\\n\\n**Step 1 — Counterfactual Data Generation (~8-12 H100h):** Starting from the publicly released Search-R1 Qwen2.5-7B checkpoint, we generate reasoning traces on ~800 questions sampled from HotpotQA (400), MuSiQue (200), and 2WikiMultiHopQA (200). We identify retrieval decision points using two complementary heuristics:\\n\\n*(a) Search-present positions:* At each token where the model generates `&lt;search>` in the trace, we create a no-retrieval counterfactual by suppressing the search token and forcing continued reasoning within `&lt;think>`. These are naturally occurring decision points (~2-3 per question based on IG-Search's finding of 1.3-2.4 search calls per rollout for multi-hop tasks).\\n\\n*(b) Search-absent positions:* At sentence boundaries within `&lt;think>` blocks (detected via regex `[.?!]\\\\s` or newline-delimited segments, following the step-boundary convention in 'Where Does Reasoning Break?'), we sample up to 2 candidate insertion points per trace where the model did NOT search. Selection prioritizes sentences containing entity mentions or factual claims (detected via simple NER heuristics on the preceding sentence). At each candidate, we create a retrieval counterfactual by inserting a `&lt;search>` call using the preceding reasoning context as the query. This yields ~4-5 decision points per question and ~3,500-4,000 step instances total.\\n\\nAt each decision point, we fork execution into retrieval and no-retrieval conditions with k=5 independent rollouts per condition using vLLM batch inference (temperature=0.7, consistent with Search-R1 training). Final answer correctness is propagated backward to each fork point. Labeling uses the correctness rates r_ret and r_no_ret across rollouts: steps where r_ret ≥ 4/5 AND r_no_ret ≤ 2/5 are labeled 'evidence-gap'; steps where r_no_ret ≥ 3/5 AND r_ret ≤ r_no_ret are labeled 'reasoning-difficulty'; remaining steps are labeled 'mixed.' We additionally compute soft labels (evidence_gap_score = r_ret − r_no_ret) for regression-based probe training. **The three-class distribution is reported as a first-class empirical finding** — extending 'Disentangling Memory and Reasoning's commonsense finding (78–98% reasoning errors) and KRUX's scientific-task finding (knowledge is the dominant bottleneck) to multi-hop factual QA. We hypothesize multi-hop factual QA shows a substantially higher proportion of evidence gaps than commonsense QA, due to the requirement for chaining specific factual knowledge (entities, dates, relationships) that is more likely to exceed parametric capacity.\\n\\n**Concrete design implications of the distribution (pre-committed analyses):** (a) If evidence gaps constitute >50% of failure steps, this directly challenges the assumption that reasoning improvements alone (longer CoT, more inference compute) can substantially improve multi-hop QA — retrieval quality and timing are the binding constraint. (b) If the distribution differs significantly across HotpotQA, MuSiQue, and 2WikiMultiHopQA, this reveals that these benchmarks stress fundamentally different bottlenecks: a retrieval system optimized on one benchmark may be systematically miscalibrated for another, with implications for benchmark selection and cross-dataset evaluation in future adaptive retrieval work. (c) The proportion of evidence-gap steps sets an upper bound on the improvement achievable by adaptive retrieval gating — if only 30% of retrieval calls address evidence gaps, even a perfect gate can only reduce unnecessary retrieval by 70%, and this ceiling is itself an important measurement. (d) The mixture of evidence-gap and reasoning-difficulty steps in a dataset quantitatively predicts the severity of DART's gradient interference problem during RL training: a dataset with 50/50 split creates maximal competing gradients, while a skewed distribution (e.g., 80% evidence gaps) suggests RL training can be more stable with appropriately weighted rewards.\\n\\n**Pre-committed framing alternative:** If >50% of steps are labeled 'mixed,' we transition to a soft-label regression framework using the continuous evidence-gap score as the target, and evaluate retrieval gating via threshold on this continuous score rather than three-class classification. The failure-mode distribution analysis remains a valid contribution regardless.\\n\\n**Step 2 — Hidden-State Extraction & Probe Training (~3-5 H100h):** For each step instance, we extract hidden states from the Qwen2.5-7B model at the decision-point token position across the posterior 2/3 of layers (following Skill-RAG's methodology; informed by ProbeRAG/CLEAR's finding that deeper layers better capture RAG-relevant signals). We train two probe architectures: (a) a per-layer linear probe (comparable to the linear probe baseline in 'Where Does Reasoning Break?'), and (b) a per-layer 3-layer MLP (following ProbeRAG/CLEAR's architecture for hidden-state probing in RAG settings). Training uses 70/15/15 train/dev/test splits stratified by dataset and label class. We evaluate probe accuracy on the three-class task and on the binary gating task (retrieve = evidence-gap ∪ mixed, skip = reasoning-difficulty). **Go/no-go gate: if binary gating probe accuracy on held-out steps < 65%, we report the separability analysis and failure distribution as the primary findings (still a contribution) rather than proceeding to gating experiments.**\\n\\n**Step 3 — Inference-Time Gating Evaluation (~5-8 H100h):** Assuming probe validation succeeds, we apply the trained probe as a hard retrieval gate on the same Search-R1 checkpoint during inference (no retraining): at each step where the model generates a `&lt;search>` token, the probe classifies the hidden state; retrieval executes only if the probe predicts 'evidence-gap' or 'mixed' (above a calibrated threshold), otherwise the model continues reasoning without external input. We evaluate on held-out test portions of HotpotQA, MuSiQue, and 2WikiMultiHopQA, reporting F1, EM, and retrieval calls per question. Baselines: (1) no retrieval, (2) always retrieve (standard Search-R1), (3) Probing-RAG-style binary probe (trained on observational correctness labels rather than counterfactual-branching labels — this is the critical ablation of causal supervision), (4) FLARE-style token probability threshold. The counterfactual-vs.-observational comparison (baseline #3) is the central experiment validating whether counterfactual-branching labels provide signal beyond observational correctness.\\n\\n**Pre-committed significance thresholds:** We define minimum effect sizes for the counterfactual-vs.-observational comparison (baseline #3): counterfactual-branching labels must yield ≥3 percentage points absolute improvement in binary gating accuracy on held-out steps, OR achieve ≥5% reduction in retrieval calls per question at matched downstream F1 (within 0.5 F1 points). If both thresholds are missed, we report this as a negative result — that counterfactual supervision does not meaningfully improve over simpler observational labels — which is itself informative for the field. In this case, the paper pivots to frame the failure-mode distribution as the primary contribution and the gating comparison as a secondary finding establishing that observational labels are sufficient. This pre-commitment ensures the paper produces a clear finding regardless of outcome.\\n\\n**Step 4 — Targeted Ablations & Analysis (~5-8 H100h):** We prioritize ablations that fit within 4 pages + appendix. **Main paper:** (a) Counterfactual-branching vs. observational labels with pre-committed thresholds (key contribution validation). (b) Probe architecture comparison (linear vs. 3-layer MLP). (c) Failure-mode distribution analysis across datasets (evidence-gap vs. reasoning-difficulty vs. mixed proportions), with explicit comparison to 'Disentangling Memory and Reasoning's commonsense findings and KRUX's scientific-task findings, including concrete design implications for adaptive retrieval. **(d) Cross-scale validation: we repeat the counterfactual labeling procedure on the Search-R1 Qwen2.5-3B checkpoint (publicly available on HuggingFace, ~2-3 H100h additional) and compare the failure-mode distribution across model sizes. If the distribution is consistent (e.g., both show >50% evidence gaps), this strengthens the generalizability of the finding. If it differs (e.g., 3B shows more evidence gaps due to smaller parametric capacity), this is itself informative about scale-dependent failure modes.** **Appendix:** (e) Gating threshold sensitivity (precision-recall curve). (f) Cross-dataset transfer (train on HotpotQA, evaluate on MuSiQue). (g) t-SNE/UMAP visualization of hidden-state clusters by failure-mode type. (h) Qualitative error analysis of 'mixed' steps.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~28-40 H100h (infrastructure setup ~2h, counterfactual generation 7B ~10h + 3B ~3h, hidden state extraction ~3h, probe training <1h, evaluation ~5h, ablations ~5h, buffer ~5h)\",\n      \"gpu_utilization\": \"40-55% — GPUs idle during analysis, visualization, and paper writing\",\n      \"timeline\": \"11 days (May 14-25, 2026); Day 0-1 dedicated to infrastructure setup and sanity check, Day 2-5 counterfactual generation (7B primary, 3B parallel on Day 4-5), Day 5-7 probing and evaluation, Day 7-9 ablations including cross-scale analysis, Day 9-11 writing\",\n      \"team\": \"2 researchers (1 on data generation/evaluation pipeline, 1 on probing/analysis/writing)\",\n      \"estimated_gpu_cost\": \"$70-100 at ~$2.50/hr mid-range H100 rental\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~34-45 H100h (agent handles pipeline orchestration, human reviews label distributions and go/no-go)\",\n      \"gpu_utilization\": \"60-75% — agent queues batch jobs efficiently, human reviews at checkpoints\",\n      \"timeline\": \"9-11 days; Day 0-1 infrastructure (pre-download both checkpoints, index corpus, sanity check), Day 2-5 generation (7B + 3B), Day 6 go/no-go review, Day 7-9 evaluation, Day 10-11 writing\",\n      \"team\": \"1 researcher, ~1-2hr/day reviewing label quality, probe results, go/no-go, and writing\",\n      \"claude_api_cost\": \"$30-60 (~300-600 turns for code generation, experiment orchestration, analysis)\",\n      \"estimated_gpu_cost\": \"$85-113 at ~$2.50/hr\",\n      \"risk_note\": \"Primary risk is label distribution skew — if >60% of steps are 'mixed,' we pivot to soft-label regression as pre-committed. Human judgment on the go/no-go is essential by Day 6. Infrastructure risk mitigated by Day 0-1 sanity check.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~38-50 H100h (agent explores more threshold configurations and probe architectures, runs both 7B and 3B pipelines)\",\n      \"gpu_utilization\": \"80-90% — agent pipelines generation → extraction → training → evaluation as continuous jobs\",\n      \"timeline\": \"7-9 days with 4 H100s; Day 0-1 infrastructure, Day 2-4 generation (7B + 3B parallel), Day 5-6 probing/evaluation, Day 7-9 ablations/writing\",\n      \"team\": \"0 (initial setup only: configure Search-R1/veRL/vLLM environment, dataset loading, retrieval corpus indexing — front-loaded to Day 0-1)\",\n      \"claude_api_cost\": \"$80-150 (~800-1500 turns for autonomous experiment design, debugging, analysis, paper drafting)\",\n      \"estimated_gpu_cost\": \"$95-125 at ~$2.50/hr\",\n      \"speed_bottleneck\": \"Counterfactual generation is the bottleneck (~2-3h wall time on 4 H100s with vLLM batch for 7B; 3B runs ~40% faster); probe training and evaluation are fast (<1h each)\",\n      \"risk_note\": \"Without human judgment on whether the 'mixed' class distribution warrants pivoting the paper framing, agent may produce a mechanically correct but uncompelling paper\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 short paper via ARR May 25, 2026 (11 days — primary and only target, track: Information Retrieval and Text Mining or Question Answering)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval (NAACL 2025 Findings)\",\n    \"Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing (Preprint 2026, arXiv 2604.15771)\",\n    \"Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation [ProbeRAG/CLEAR] (ACL 2026 Findings per arXiv v3 April 2026 comments, arXiv 2510.12460)\",\n    \"When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models [ReaLM-Retrieve] (Preprint 2026, arXiv 2604.26649)\",\n    \"Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning (Preprint 2025, arXiv 2503.09516)\",\n    \"SLATE: Truncated Step-Level Sampling with Process Rewards for Retrieval-Augmented Reasoning (Preprint 2026, arXiv 2602.23440)\",\n    \"IG-Search: Step-Level Information Gain Rewards for Search-Augmented Reasoning (Preprint 2026, arXiv 2604.15148)\",\n    \"TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs (Preprint 2026, arXiv 2603.22293)\",\n    \"DeepControl: Scaling Search-Augmented LLM Reasoning via Adaptive Information Control (ICLR 2026 SPOT Workshop, arXiv 2602.01672)\",\n    \"DART: Reasoning and Tool-use Compete in Agentic RL — From Quantifying Interference to Disentangled Tuning (Preprint 2026, arXiv 2602.00994)\",\n    \"Disentangling Memory and Reasoning Ability in Large Language Models (ACL 2025, arXiv 2411.13504)\",\n    \"Knowledge or Reasoning? A Close Look at How LLMs Think Across Domains (Preprint 2025, arXiv 2506.02126)\",\n    \"Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning [KRUX] (Preprint 2025, arXiv 2508.19202)\",\n    \"Counterfactual Probing for Hallucination Detection and Mitigation in Large Language Models (Preprint 2025, arXiv 2508.01862)\",\n    \"Adaptive Retrieval helps Reasoning in LLMs — but mostly if it's not used (Preprint 2025, arXiv 2602.07213)\",\n    \"Active Retrieval Augmented Generation [FLARE] (EMNLP 2023)\",\n    \"Counterfactual Reasoning for Retrieval-Augmented Generation [CF-RAG] (ICLR 2026)\",\n    \"Disentangling Knowledge and Reasoning in Medical Large Language Models (Preprint 2025, arXiv 2505.11462)\",\n    \"Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Preprint 2026, arXiv 2603.05488)\",\n    \"SynthWorlds: Controlled Parallel Worlds for Disentangling Knowledge from Reasoning (Preprint 2025, arXiv 2510.24427)\",\n    \"GRADE: Probing Knowledge Gaps in LLMs through Gradient Subspace Dynamics (Preprint 2026, arXiv 2604.02830)\",\n    \"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (Preprint 2026, arXiv 2605.13772)\",\n    \"PRISM: Probing Reasoning, Instruction, and Source Memory in LLM Hallucinations (Preprint 2026, arXiv 2604.16909)\",\n    \"Latent Abstraction for Retrieval-Augmented Generation [LAnR] (Preprint 2026, arXiv 2604.17866)\"\n  ],\n  \"description\": \"Current adaptive retrieval methods for reasoning LLMs use signals (uncertainty, token probability, composite scores) that conflate evidence gaps with reasoning difficulty, yet recent work confirms these are separable, task-dependent, and carry opposite optimal actions: evidence gaps demand retrieval even when the model appears confident (masking hallucinated knowledge), while reasoning difficulty demands suppressing retrieval even when the model appears uncertain (as retrieved context introduces noise). 'Disentangling Memory and Reasoning' (ACL 2025) achieves 83.3% disentanglement accuracy with explicit memory/reason tokens and finds 78–98% of commonsense errors stem from reasoning; KRUX (arXiv 2508.19202) finds knowledge retrieval from parameters is the dominant bottleneck for scientific tasks (base models with KIs outperform reasoning-enhanced models by ≥10%); 'Knowledge or Reasoning?' shows step-level knowledge-accuracy correlation of 0.998 vs. reasoning-accuracy 0.698; DART proves reasoning and tool-use produce competing gradients; ProbeRAG/CLEAR demonstrates 97–98% accuracy for sentence-level knowledge conflict detection via hidden-state probing; Skill-RAG finds failure states occupy structured regions in hidden-state space; and 'Where Does Reasoning Break?' demonstrates hidden states encode step-level correctness with 91% AUROC (though targeting binary correctness, not failure-mode type). We adopt the term 'counterfactual-branching probes' to distinguish from Feng (arXiv 2508.01862), who uses 'counterfactual probing' for a behavioral technique (testing model sensitivity to counterfactual input statements) unrelated to our hidden-state probing after execution forking. We present a focused empirical study with two first-class contributions. First, we introduce a counterfactual-branching labeling methodology that produces the first step-level failure-mode distribution for multi-hop factual QA: using Search-R1 checkpoints (Qwen2.5-7B primary, Qwen2.5-3B for cross-scale validation), we fork ~3,500-4,000 reasoning steps into retrieval and no-retrieval paths with k=5 rollouts each, generating causal labels ('evidence-gap,' 'reasoning-difficulty,' 'mixed'). Decision points are identified via two complementary heuristics: (a) positions where the model generated `&lt;search>` tokens (natural retrieval decisions), and (b) sentence-boundary sampling within `&lt;think>` blocks where the model did NOT search (counterfactual insertion points selected via entity/claim detection). The resulting distribution is directly actionable for system design: if evidence gaps dominate, this challenges reasoning-first approaches to multi-hop QA and validates retrieval-heavy architectures; if the distribution varies across HotpotQA, MuSiQue, and 2WikiMultiHopQA, this reveals that these benchmarks stress fundamentally different bottlenecks, with implications for benchmark selection and per-dataset strategy calibration; the evidence-gap proportion sets an upper bound on adaptive gating improvement; and the failure-mode mixture quantitatively predicts the severity of DART's gradient interference during RL training. Cross-scale comparison (7B vs. 3B) tests whether the distribution is a property of the task or the model capacity. Second, we train lightweight counterfactual-branching probes (linear and 3-layer MLP, following ProbeRAG/CLEAR's architecture) on hidden states to classify failure mode type, then apply the probe as an inference-time retrieval gate on the existing checkpoint without retraining — a proof-of-concept that the distribution is actionable: retrieve only when the probe predicts 'evidence-gap' or 'mixed,' skip retrieval when reasoning is the bottleneck. We pre-commit to significance thresholds for the central counterfactual-vs.-observational comparison: counterfactual-branching labels must yield ≥3 percentage points absolute improvement in binary gating accuracy OR ≥5% reduction in retrieval calls at matched downstream F1 (within 0.5 F1 points); if both are missed, we report a negative result, pivoting the paper to frame the failure-mode distribution as the primary contribution. If >50% of steps are 'mixed,' we pre-commit to soft-label regression on a continuous evidence-gap score. Key novelty vs. existing methods: (1) counterfactual-branching causal labels rather than observational correctness (Probing-RAG), RL reward shaping (IG-Search, TIPS, DeepControl), or explicit token-guided generation ('Disentangling Memory and Reasoning'), (2) failure-mode classification (evidence gap vs. reasoning difficulty) rather than binary correctness detection ('Where Does Reasoning Break?'), knowledge conflict detection (ProbeRAG/CLEAR), or hallucination taxonomy (PRISM), (3) post-hoc inference-time applicability without retraining, (4) cross-scale validation (7B + 3B) testing generalizability. Evaluation on HotpotQA, MuSiQue, and 2WikiMultiHopQA with baselines: no-retrieval, always-retrieve, Probing-RAG-style observational probe (critical ablation with pre-committed thresholds), and FLARE threshold. Infrastructure setup front-loaded to Day 0-1 with sanity check. Scoped as a short paper (~28-50 H100h total); RL integration deferred to follow-up.\",\n  \"project_name\": \"evid_reason_disentangle\",\n  \"source\": \"web_research\"\n}\n```"
      }
    ],
    "totalDurationMs": 227438,
    "totalTokens": 29703,
    "totalToolUseCount": 0,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19272,
      "cache_read_input_tokens": 0,
      "output_tokens": 10429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19272
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 10429,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 19272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19272,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  },
  "sourceToolAssistantUUID": "77c95cca-a9e3-48c3-a195-06204dad29b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 86 · 2026-05-14T16:58:57.385Z_

```json
{
  "parentUuid": "80a20f18-fd44-421a-9820-a7355d2c4c14",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "72d1b87b-369b-433b-b4cd-bc09f8446587",
  "timestamp": "2026-05-14T16:58:57.385Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 87_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Counterfactual Probing Disentangles Evidence Gaps from Reasoning Diffi…",
  "leafUuid": "72d1b87b-369b-433b-b4cd-bc09f8446587",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Runtime record

_source line 88_

```json
{
  "type": "ai-title",
  "aiTitle": "Counterfactual step-level failure-mode classification for retrieval gating",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Assistant

_source line 89 · 2026-05-14T16:59:15.552Z_

<details><summary>Logged reasoning block</summary>

```text
The agent returned the complete JSON. Let me now verify the output and present it to the user. Let me review the key changes made:

1. **ProbeRAG/CLEAR venue**: Fixed. Now says "ACL 2026 Findings per arXiv v3 author-reported comments, April 2026; proceedings not yet published as ACL 2026 is July 2-7" in core_problem, and "previously submitted to ICLR 2026 and withdrawn, subsequently accepted at ACL 2026 Findings" in landscape. Transparent about the evidence.

2. **KRUX citation**: Added throughout - in core_problem, opportunity, landscape, approach, and description. 

3. **Terminology disambiguation**: Title changed to "Counterfactual-Branching Probes". Added explicit disambiguation from Feng (arXiv 2508.01862) in opportunity, landscape, and description. The term "counterfactual-branching" is used consistently. KRUX is properly described as a black-box diagnostic framework that validates the knowledge-vs-reasoning axis via knowledge injection.

4. **Impact framing**: Substantially strengthened. Added in core_problem that conflating knowledge and reasoning failures leads to systematically suboptimal retrieval decisions, with the insight that optimal actions are opposite for the two failure modes.

5. **Cross-scale validation (Qwen2.5-3B)**: Added as Step 4(d) in approach with confirmed checkpoint availability and updated resource estimates to reflect the additional 3B experiment (~2-3 H100h).

6. **Actionability and design implications**: New point on actionability with concrete design implications, plus a dedicated section spelling out 4 pre-committed analyses and their implications for retrieval gate design.

7. **Landscape connections**: Added connection to DART's gradient interference and updated references to include KRUX and Feng (2508.01862).

The core approach remains unchanged, but the framing is substantially strengthened throughout.

Outputting the final JSON...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72d1b87b-369b-433b-b4cd-bc09f8446587",
  "isSidechain": false,
  "requestId": "req_011Cb2pLe5gRHFYBY82fcua1",
  "type": "assistant",
  "uuid": "81e8e241-11da-4bce-a064-092642d543af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017AJcdYjWWfpT1UTyhjqcWU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22733,
      "cache_read_input_tokens": 49211,
      "output_tokens": 11708,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 11708,
          "cache_read_input_tokens": 49211,
          "cache_creation_input_tokens": 22733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22733
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

_source line 90 · 2026-05-14T17:03:21.413Z_

Here is the revised research idea addressing all five reviewer issues. Key changes:

**1. ProbeRAG/CLEAR venue (fixed):** I verified the arXiv page directly — v3 (April 15, 2026) explicitly states "ACL 2026 Findings" in comments. The ICLR 2026 submission was withdrawn, but the paper was subsequently accepted at ACL 2026 Findings. ACL 2026 is July 2-7 in San Diego (proceedings not yet published). The citation now transparently notes the evidence trail.

**2. KRUX added:** Integrated throughout (core_problem, opportunity, landscape, approach, description) as converging evidence. KRUX validates the knowledge-vs-reasoning axis via KI injection on scientific tasks, complementing commonsense findings — we now position multi-hop factual QA as the missing third data point.

**3. Terminology disambiguated:** Title and all references changed to "counterfactual-branching probes." Feng (arXiv 2508.01862) explicitly cited and differentiated in opportunity, landscape, and description.

**4. Impact framing strengthened (main blocker fix):** Added concrete, pre-committed design implications throughout:
- Evidence-gap dominance challenges reasoning-first approaches to multi-hop QA
- Cross-dataset distribution variance reveals benchmarks stress different bottlenecks (benchmark selection implications)
- Evidence-gap proportion sets upper bound on adaptive gating improvement (ceiling measurement)
- Failure-mode mixture quantitatively predicts DART's gradient interference severity
- Gating experiment reframed as "proof-of-concept that the distribution is actionable"

**5. Cross-scale validation added:** Qwen2.5-3B checkpoint confirmed available on HuggingFace (4 variants). Added as Step 4(d) ablation (~2-3 H100h additional). Tests whether the distribution is a task property or model-capacity dependent.

```json
{
  "change_type": "minor",
  "title": "Counterfactual-Branching Probes Disentangle Evidence Gaps from Reasoning Difficulty for Step-Level Retrieval Gating",
  "core_problem": "Current adaptive retrieval methods for reasoning LLMs use signals that conflate two fundamentally different failure modes: evidence gaps (the model lacks factual knowledge for a step) and reasoning difficulty (the step is logically complex, and retrieval introduces noise). This conflation is not merely imprecise — it leads to systematically suboptimal retrieval decisions: a confidence-based gate cannot distinguish a model that is confidently wrong (hallucinating a missing fact) from one that genuinely knows the answer, nor can it distinguish genuine uncertainty about a logical step from uncertainty caused by a knowledge gap. The optimal action for these failure modes is opposite: evidence gaps demand retrieval even when the model appears confident, while reasoning difficulty demands suppressing retrieval even when the model appears uncertain. Probing-RAG gates retrieval via hidden-state probes with binary correctness labels. Skill-RAG routes among retrieval skills based on failure-state probing but diagnoses query-evidence misalignment, not whether retrieval should occur. ProbeRAG/CLEAR (arXiv 2510.12460; ACL 2026 Findings per arXiv v3 author-reported comments, April 2026; proceedings not yet published as ACL 2026 is July 2-7) uses a 3-layer MLP probe on decoder hidden states for sentence-level knowledge conflict detection in RAG — achieving 97–98% accuracy on MQuAKE — but targets parametric-contextual conflict, not whether a step fails due to missing knowledge vs. reasoning complexity. ReaLM-Retrieve's composite RSUS score cannot distinguish missing knowledge from logical complexity. DeepControl's information utility (novelty + effectiveness) addresses when to continue retrieving but conflates both failure sources into a single scalar. IG-Search's counterfactual baseline (random documents vs. retrieved documents) provides step-level credit assignment for search quality but does not classify WHY a step benefits from retrieval. TIPS (arXiv 2603.22293) assigns dense turn-level rewards via potential-based shaping, achieving 11.8% EM improvement — addressing credit assignment for search decisions but through RL training signals, not inference-time diagnosis. DART demonstrates that reasoning and tool-use compete during joint RL training — gradient interference between the two capabilities is measurable and harmful — but proposes an architectural fix (disentangled LoRA) rather than diagnosing failure modes at inference time. 'Disentangling Memory and Reasoning Ability in Large Language Models' (arXiv 2411.13504; ACL 2025) introduces explicit &lt;memory> and &lt;reason> tokens to decompose LLM inference into knowledge retrieval vs. logical reasoning steps, achieving 83.3% disentanglement accuracy and finding that 78–98% of errors on commonsense tasks stem from reasoning rather than memory — directly validating that the knowledge-vs-reasoning axis is trainable and separable. 'Knowledge or Reasoning?' (arXiv 2506.02126) shows that knowledge correctness and reasoning quality are separable dimensions at the step level (knowledge-accuracy correlation 0.998 vs. reasoning-accuracy 0.698 in medical QA), validating the axis we target — but operates as an offline evaluation framework using GPT-4o judges, not as an inference-time retrieval gating mechanism. KRUX (arXiv 2508.19202) probes the knowledge-vs-reasoning bottleneck by injecting Knowledge Ingredients (KIs) in-context and measuring performance delta, finding that base models with KIs outperform reasoning-enhanced models by ≥10% on scientific tasks — further validating that knowledge retrieval from parameters is a critical, separable bottleneck. 'Where Does Reasoning Break?' (arXiv 2605.13772) detects step-level hallucinations via hidden-state transport geometry with strong in-domain performance (91.0% AUROC on ProcessBench), but classifies binary correctness (hallucinated vs. correct), not failure-mode type (evidence gap vs. reasoning difficulty), and its student model collapses under distribution shift (cross-model AUROC drops to 33–58%). PRISM (arXiv 2604.16909) disentangles hallucinations into knowledge-missing, knowledge-error, reasoning-error, and instruction-following dimensions, but operates as an evaluation benchmark, not an inference-time mechanism. Critically, while 'Disentangling Memory and Reasoning' measured error distributions on commonsense tasks (finding reasoning errors dominate at 78–98%) and KRUX found knowledge is the bottleneck for scientific reasoning, no work has measured this distribution for multi-hop factual QA where retrieval is available — a setting where the failure-mode distribution directly determines the optimal design of adaptive retrieval systems. Without this measurement, the field is building retrieval gates blind to the underlying failure structure they are trying to address. No existing method provides counterfactual-branching, step-level classification of evidence gaps vs. reasoning difficulty in hidden-state space for inference-time retrieval gating.",
  "opportunity": "Four converging lines of evidence make this the right moment for counterfactual-branching probes of retrieval failure modes, and a fifth consideration — the actionability of the resulting distribution — elevates this from a diagnostic exercise to a design-informing measurement: (1) The evidence-vs-reasoning axis is real, trainable, and task-dependent — 'Disentangling Memory and Reasoning' achieves 83.3% disentanglement accuracy with explicit memory/reason tokens on Qwen2.5-7B and finds error distributions vary dramatically by task (98.3% reasoning errors on StrategyQA vs. 78.4% on CommonsenseQA), 'Knowledge or Reasoning?' achieves step-level separation with high correlation, KRUX demonstrates that injecting task-relevant Knowledge Ingredients in-context boosts base models by ≥10% over reasoning-enhanced variants on scientific benchmarks (confirming knowledge retrieval from parameters as a separable bottleneck), PRISM's four-way hallucination taxonomy validates knowledge-vs-reasoning as a meaningful diagnostic axis, a PubMedBERT classifier separates knowledge-heavy from reasoning-heavy medical questions at 81% accuracy (arXiv 2505.11462), and Skill-RAG's representation analysis confirms failure states occupy 'structured, separable regions' in hidden-state space. (2) Hidden-state probing for RAG is technically mature — ProbeRAG/CLEAR demonstrates that 3-layer MLP probes on decoder hidden states achieve 97–98% accuracy for knowledge conflict detection, confirming that fine-grained RAG-relevant signals are linearly separable in latent space; however, no existing probe targets failure-mode type (evidence gap vs. reasoning difficulty). (3) Indiscriminate retrieval demonstrably harms reasoning — non-retrieval traces achieve 84.2% on GSM8K vs. lower with retrieval (arXiv 2602.07213), DART quantifies that reasoning and tool-use produce misaligned gradients during joint training, and IG-Search shows models adaptively learn to search conservatively on single-hop questions (1.3 calls) vs. actively on multi-hop (2.4 calls), implying retrieval value varies by step type. (4) Counterfactual and geometric methodology for step-level analysis is maturing — IG-Search uses counterfactual random-document baselines for step-level credit, TIPS demonstrates that turn-level credit assignment substantially improves training stability (11.8% EM improvement), CF-RAG (ICLR 2026) applies counterfactual reasoning to distinguish causal from correlated evidence, and 'Where Does Reasoning Break?' demonstrates that hidden-state trajectories encode step-level correctness with high fidelity (teacher AUROC 91–98%), though its cross-model generalization failure (student AUROC 33–58% under shift) motivates our within-checkpoint probing design. Note: Feng (arXiv 2508.01862) also uses the phrase 'counterfactual probing' but to mean probing model sensitivity to counterfactual input statements for hallucination detection — a behavioral technique unrelated to our approach of probing hidden states after counterfactual execution branching. We adopt the term 'counterfactual-branching probes' to clearly distinguish the two methodologies. (5) The failure-mode distribution is directly actionable for system design — if multi-hop factual QA is predominantly evidence-gap limited, this challenges the implicit assumption behind reasoning-focused approaches (e.g., longer CoT, more compute at inference) that reasoning improvement alone can solve multi-hop QA; conversely, it would validate retrieval-heavy architectures. If the distribution varies across benchmarks (e.g., HotpotQA vs. MuSiQue vs. 2WikiMultiHopQA), this reveals that these benchmarks stress fundamentally different bottlenecks, with direct implications for benchmark selection in future adaptive retrieval research and for per-dataset retrieval strategy calibration. The distribution also explains DART's finding of gradient interference: if a training corpus mixes evidence-gap steps (where retrieval helps) and reasoning-difficulty steps (where retrieval hurts), the resulting conflicting gradient signals are a predictable consequence of the mixture proportions. However, no prior work uses counterfactual branching (forking each step into retrieval vs. no-retrieval paths) to generate causal labels for training an inference-time probe that classifies failure mode type. This combination — counterfactual causal supervision + hidden-state probing + step-level failure-mode classification — fills a specific gap. Crucially, while 'Disentangling Memory and Reasoning' found that reasoning errors dominate on commonsense tasks (78–98%) and KRUX found knowledge is the primary bottleneck for scientific reasoning, this distribution is unknown for multi-hop factual QA where retrieval is available. We hypothesize the distribution is substantially different: multi-hop factual questions require chaining specific facts (entities, dates, relationships) that are more likely to exceed the model's parametric knowledge, shifting the distribution toward evidence gaps. The step-level failure distribution itself is a novel empirical measurement with direct implications for how the field designs adaptive retrieval systems — it determines the ceiling of retrieval-gating improvement, the optimal aggressiveness of retrieval, and whether single-signal gating approaches are fundamentally adequate.",
  "landscape": "**Hidden-state probing for retrieval:** Probing-RAG (NAACL 2025) is a direct predecessor: a 5MB FC probe on intermediate layers gates retrieval at query level with binary correctness labels, reducing retrieval by ~50%. Skill-RAG (arXiv 2604.15771) extends this with per-layer probers on Gemma2-9B's posterior-2/3 layers plus a prompt-based skill router selecting among query rewriting, decomposition, evidence focusing, or exit — achieving 46.8% average accuracy and +13.6 on 2WikiMultiHopQA over Probing-RAG. ProbeRAG/CLEAR (arXiv 2510.12460; ACL 2026 Findings per arXiv v3 comments, April 2026; note: previously submitted to ICLR 2026 and withdrawn, subsequently accepted at ACL 2026 Findings; proceedings not yet published as ACL 2026 is July 2-7, 2026) probes decoder hidden states at the sentence level for knowledge conflict detection in RAG, using a 3-layer MLP probe (with 2-layer and 5-layer variants) trained on MQuAKE conflict pairs; achieves 97–98% accuracy on MQuAKE and 79–88% cross-benchmark, confirming that fine-grained RAG-relevant signals are extractable from hidden states. ProbeRAG's three-stage framework (knowledge pruning → latent conflict probing → conflict-aware attention) is methodologically adjacent but targets parametric-contextual knowledge conflicts, not failure-mode classification (evidence gap vs. reasoning difficulty). LAnR (arXiv 2604.17866) uses a lightweight MLP control head over hidden-state entropy for adaptive retrieval stopping within a latent-space RAG framework, demonstrating another instance of learned retrieval control but in a fundamentally different architecture (unified encoder-retriever-generator). **Knowledge-reasoning disentanglement:** 'Disentangling Memory and Reasoning Ability in Large Language Models' (arXiv 2411.13504; ACL 2025) is the most direct validation of our target axis: it introduces &lt;memory> and &lt;reason> tokens to decompose LLM inference, achieving 83.3% disentanglement accuracy via LoRA fine-tuning on GPT-4o-generated labels. Its error analysis reveals that reasoning errors dominate on commonsense tasks (78–98%), but the method operates via explicit token-guided generation (training-time decomposition), not via post-hoc hidden-state probing, and evaluates on commonsense QA (StrategyQA, CommonsenseQA, TruthfulQA), not multi-hop factual QA where retrieval is available. The open question — whether multi-hop factual QA shows a similar or inverted distribution — is the empirical gap we address. 'Knowledge or Reasoning?' (arXiv 2506.02126) decomposes step-level reasoning into Knowledge Index and Information Gain, finding knowledge-accuracy correlation of 0.998 vs. reasoning-accuracy of 0.698. The medical disentanglement work (arXiv 2505.11462) achieves 81% accuracy separating question types with PubMedBERT. KRUX (arXiv 2508.19202) takes a complementary black-box approach: by injecting Knowledge Ingredients (KIs) — atomic, answer-agnostic factual statements extracted from reasoning traces — in-context, it measures whether providing external knowledge resolves failures. On scientific benchmarks (SciReas/SciReas-Pro), base models with KIs outperform reasoning-enhanced models by ≥10%, establishing that parametric knowledge retrieval is the dominant bottleneck for scientific tasks. While KRUX is purely diagnostic (not an inference-time mechanism) and operates via in-context KI injection rather than hidden-state probing, it validates the same axis we target and provides a complementary data point on task-dependent failure-mode distributions: scientific tasks are knowledge-limited, commonsense tasks are reasoning-limited — we measure where multi-hop factual QA falls on this spectrum. **Hidden-state probing for step-level failures:** 'Where Does Reasoning Break?' (arXiv 2605.13772) frames step-level hallucination as transport-cost excursions in hidden-state space, achieving 91.0% AUROC (teacher) on ProcessBench. Its BiLSTM student achieves strong in-domain results (75–99.8% AUROC) but collapses under distribution shift (cross-model AUROC 33–58%). This validates that hidden states encode step-level correctness signals but targets binary correctness, not failure-mode classification. Reasoning Theater (arXiv 2603.05488) shows linear probes detect CoT divergence from internal beliefs, further confirming probing viability. PRISM (arXiv 2604.16909) decomposes hallucinations into knowledge-missing, knowledge-error, reasoning-error, and instruction-following dimensions as an evaluation framework, confirming the diagnostic axis we operationalize for inference-time use. **Terminology note:** Feng (arXiv 2508.01862) uses 'counterfactual probing' to describe probing model behavior with counterfactual input statements (generated plausible-but-incorrect claims that test model sensitivity) for hallucination detection. This is a behavioral approach operating on model outputs, fundamentally different from our counterfactual-branching probes that fork execution into retrieval/no-retrieval paths and probe the resulting hidden states. We adopt 'counterfactual-branching probes' throughout to avoid conflation. **RL-based retrieval timing:** Search-R1 (arXiv 2503.09516) trains retrieval timing via GRPO with outcome-only reward, achieving 41% improvement on Qwen2.5-7B. SLATE (arXiv 2602.23440) adds decomposed process rewards (reasoning, query, answer quality), reaching 0.461 avg EM on 7B. IG-Search (arXiv 2604.15148) introduces step-level information gain rewards using a counterfactual baseline of random documents, measuring how much retrieved documents improve answer confidence — achieving 0.430 avg EM on Qwen2.5-3B with 1.3–2.4 search calls per rollout. IG-Search's counterfactual is conceptually adjacent but serves a different purpose: it evaluates search query quality (good retrieval vs. random), not whether retrieval itself is needed vs. harmful. TIPS (arXiv 2603.22293) assigns dense turn-level rewards via potential-based reward shaping using a teacher model's answer likelihood, achieving 11.8% EM and 13.6% F1 improvements over PPO on Qwen2.5-7B across seven QA benchmarks. TIPS addresses credit assignment for search decisions through RL training, while we address it through inference-time probing — complementary approaches to the same underlying problem. **Adaptive information control:** DeepControl (arXiv 2602.01672) defines information utility U(e) = ρ·Novelty + (1-ρ)·Effectiveness and uses stopping/continuation rules, achieving 9.4% improvement over RL baselines on Qwen2.5-7B. DeepControl addresses 'when to stop retrieving' via a training-time utility signal but cannot diagnose failure mode type at inference time. **Reasoning-tool competition:** DART (arXiv 2602.00994) introduces LEAS to quantify gradient interference between reasoning and tool-use, showing they induce misaligned gradient directions. DART's disentangled LoRA achieves 6.35% avg improvement. DART validates our core premise — reasoning and retrieval compete — but proposes architectural separation during training, while we propose a diagnostic probe for inference-time gating. Our failure-mode distribution directly explains the gradient interference DART observes: the proportion of evidence-gap vs. reasoning-difficulty steps in a training corpus determines the severity of competing gradients. **Other related:** FLARE (EMNLP 2023) uses token probability thresholds. ReaLM-Retrieve (arXiv 2604.26649) achieves 71.2% F1 on MuSiQue with composite RSUS. GRADE (arXiv 2604.02830) probes knowledge gaps via gradient subspace dynamics but requires backpropagation (unsuitable for inference). SynthWorlds (arXiv 2510.24427) disentangles knowledge from reasoning at task level via synthetic corpora. **Gap:** No existing work provides counterfactual-branching, step-level probing that classifies evidence gaps vs. reasoning difficulty in hidden-state space for post-hoc inference-time retrieval gating, nor has any work empirically measured the step-level distribution of these failure modes in multi-hop factual QA — the task category where adaptive retrieval has the highest practical impact and where the distribution has direct design implications for the field.",
  "approach": "We propose a focused empirical study with two first-class contributions: (1) a counterfactual-branching labeling methodology that produces the first step-level failure-mode distribution for multi-hop factual QA (measuring what fraction of reasoning steps are knowledge-limited vs. reasoning-limited — extending the commonsense findings of 'Disentangling Memory and Reasoning' and the scientific-task findings of KRUX to a retrieval-augmented setting), and (2) inference-time retrieval gating via lightweight probes trained on these counterfactual labels, serving as a proof-of-concept that the distribution is actionable. This is scoped as a short paper; RL integration is deferred to follow-up work.\n\n**Step 0 — Infrastructure Setup & Sanity Check (Day 0-1, ~2 H100h):** We pre-download the Search-R1 Qwen2.5-7B checkpoint (primary) and Qwen2.5-3B checkpoint (cross-scale validation) and configure the vLLM + veRL environment following the Search-R1 repository setup. We pre-index the Wikipedia retrieval corpus in the required jsonl format (id + contents). A minimal sanity check (10 questions, 2 rollouts per condition) validates the counterfactual generation pipeline end-to-end before committing to full-scale experiments. This front-loads infrastructure risk and ensures the remaining 9 days are dedicated to research.\n\n**Step 1 — Counterfactual Data Generation (~8-12 H100h):** Starting from the publicly released Search-R1 Qwen2.5-7B checkpoint, we generate reasoning traces on ~800 questions sampled from HotpotQA (400), MuSiQue (200), and 2WikiMultiHopQA (200). We identify retrieval decision points using two complementary heuristics:\n\n*(a) Search-present positions:* At each token where the model generates `&lt;search>` in the trace, we create a no-retrieval counterfactual by suppressing the search token and forcing continued reasoning within `&lt;think>`. These are naturally occurring decision points (~2-3 per question based on IG-Search's finding of 1.3-2.4 search calls per rollout for multi-hop tasks).\n\n*(b) Search-absent positions:* At sentence boundaries within `&lt;think>` blocks (detected via regex `[.?!]\\s` or newline-delimited segments, following the step-boundary convention in 'Where Does Reasoning Break?'), we sample up to 2 candidate insertion points per trace where the model did NOT search. Selection prioritizes sentences containing entity mentions or factual claims (detected via simple NER heuristics on the preceding sentence). At each candidate, we create a retrieval counterfactual by inserting a `&lt;search>` call using the preceding reasoning context as the query. This yields ~4-5 decision points per question and ~3,500-4,000 step instances total.\n\nAt each decision point, we fork execution into retrieval and no-retrieval conditions with k=5 independent rollouts per condition using vLLM batch inference (temperature=0.7, consistent with Search-R1 training). Final answer correctness is propagated backward to each fork point. Labeling uses the correctness rates r_ret and r_no_ret across rollouts: steps where r_ret ≥ 4/5 AND r_no_ret ≤ 2/5 are labeled 'evidence-gap'; steps where r_no_ret ≥ 3/5 AND r_ret ≤ r_no_ret are labeled 'reasoning-difficulty'; remaining steps are labeled 'mixed.' We additionally compute soft labels (evidence_gap_score = r_ret − r_no_ret) for regression-based probe training. **The three-class distribution is reported as a first-class empirical finding** — extending 'Disentangling Memory and Reasoning's commonsense finding (78–98% reasoning errors) and KRUX's scientific-task finding (knowledge is the dominant bottleneck) to multi-hop factual QA. We hypothesize multi-hop factual QA shows a substantially higher proportion of evidence gaps than commonsense QA, due to the requirement for chaining specific factual knowledge (entities, dates, relationships) that is more likely to exceed parametric capacity.\n\n**Concrete design implications of the distribution (pre-committed analyses):** (a) If evidence gaps constitute >50% of failure steps, this directly challenges the assumption that reasoning improvements alone (longer CoT, more inference compute) can substantially improve multi-hop QA — retrieval quality and timing are the binding constraint. (b) If the distribution differs significantly across HotpotQA, MuSiQue, and 2WikiMultiHopQA, this reveals that these benchmarks stress fundamentally different bottlenecks: a retrieval system optimized on one benchmark may be systematically miscalibrated for another, with implications for benchmark selection and cross-dataset evaluation in future adaptive retrieval work. (c) The proportion of evidence-gap steps sets an upper bound on the improvement achievable by adaptive retrieval gating — if only 30% of retrieval calls address evidence gaps, even a perfect gate can only reduce unnecessary retrieval by 70%, and this ceiling is itself an important measurement. (d) The mixture of evidence-gap and reasoning-difficulty steps in a dataset quantitatively predicts the severity of DART's gradient interference problem during RL training: a dataset with 50/50 split creates maximal competing gradients, while a skewed distribution (e.g., 80% evidence gaps) suggests RL training can be more stable with appropriately weighted rewards.\n\n**Pre-committed framing alternative:** If >50% of steps are labeled 'mixed,' we transition to a soft-label regression framework using the continuous evidence-gap score as the target, and evaluate retrieval gating via threshold on this continuous score rather than three-class classification. The failure-mode distribution analysis remains a valid contribution regardless.\n\n**Step 2 — Hidden-State Extraction & Probe Training (~3-5 H100h):** For each step instance, we extract hidden states from the Qwen2.5-7B model at the decision-point token position across the posterior 2/3 of layers (following Skill-RAG's methodology; informed by ProbeRAG/CLEAR's finding that deeper layers better capture RAG-relevant signals). We train two probe architectures: (a) a per-layer linear probe (comparable to the linear probe baseline in 'Where Does Reasoning Break?'), and (b) a per-layer 3-layer MLP (following ProbeRAG/CLEAR's architecture for hidden-state probing in RAG settings). Training uses 70/15/15 train/dev/test splits stratified by dataset and label class. We evaluate probe accuracy on the three-class task and on the binary gating task (retrieve = evidence-gap ∪ mixed, skip = reasoning-difficulty). **Go/no-go gate: if binary gating probe accuracy on held-out steps < 65%, we report the separability analysis and failure distribution as the primary findings (still a contribution) rather than proceeding to gating experiments.**\n\n**Step 3 — Inference-Time Gating Evaluation (~5-8 H100h):** Assuming probe validation succeeds, we apply the trained probe as a hard retrieval gate on the same Search-R1 checkpoint during inference (no retraining): at each step where the model generates a `&lt;search>` token, the probe classifies the hidden state; retrieval executes only if the probe predicts 'evidence-gap' or 'mixed' (above a calibrated threshold), otherwise the model continues reasoning without external input. We evaluate on held-out test portions of HotpotQA, MuSiQue, and 2WikiMultiHopQA, reporting F1, EM, and retrieval calls per question. Baselines: (1) no retrieval, (2) always retrieve (standard Search-R1), (3) Probing-RAG-style binary probe (trained on observational correctness labels rather than counterfactual-branching labels — this is the critical ablation of causal supervision), (4) FLARE-style token probability threshold. The counterfactual-vs.-observational comparison (baseline #3) is the central experiment validating whether counterfactual-branching labels provide signal beyond observational correctness.\n\n**Pre-committed significance thresholds:** We define minimum effect sizes for the counterfactual-vs.-observational comparison (baseline #3): counterfactual-branching labels must yield ≥3 percentage points absolute improvement in binary gating accuracy on held-out steps, OR achieve ≥5% reduction in retrieval calls per question at matched downstream F1 (within 0.5 F1 points). If both thresholds are missed, we report this as a negative result — that counterfactual supervision does not meaningfully improve over simpler observational labels — which is itself informative for the field. In this case, the paper pivots to frame the failure-mode distribution as the primary contribution and the gating comparison as a secondary finding establishing that observational labels are sufficient. This pre-commitment ensures the paper produces a clear finding regardless of outcome.\n\n**Step 4 — Targeted Ablations & Analysis (~5-8 H100h):** We prioritize ablations that fit within 4 pages + appendix. **Main paper:** (a) Counterfactual-branching vs. observational labels with pre-committed thresholds (key contribution validation). (b) Probe architecture comparison (linear vs. 3-layer MLP). (c) Failure-mode distribution analysis across datasets (evidence-gap vs. reasoning-difficulty vs. mixed proportions), with explicit comparison to 'Disentangling Memory and Reasoning's commonsense findings and KRUX's scientific-task findings, including concrete design implications for adaptive retrieval. **(d) Cross-scale validation: we repeat the counterfactual labeling procedure on the Search-R1 Qwen2.5-3B checkpoint (publicly available on HuggingFace, ~2-3 H100h additional) and compare the failure-mode distribution across model sizes. If the distribution is consistent (e.g., both show >50% evidence gaps), this strengthens the generalizability of the finding. If it differs (e.g., 3B shows more evidence gaps due to smaller parametric capacity), this is itself informative about scale-dependent failure modes.** **Appendix:** (e) Gating threshold sensitivity (precision-recall curve). (f) Cross-dataset transfer (train on HotpotQA, evaluate on MuSiQue). (g) t-SNE/UMAP visualization of hidden-state clusters by failure-mode type. (h) Qualitative error analysis of 'mixed' steps.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~28-40 H100h (infrastructure setup ~2h, counterfactual generation 7B ~10h + 3B ~3h, hidden state extraction ~3h, probe training <1h, evaluation ~5h, ablations ~5h, buffer ~5h)",
      "gpu_utilization": "40-55% — GPUs idle during analysis, visualization, and paper writing",
      "timeline": "11 days (May 14-25, 2026); Day 0-1 dedicated to infrastructure setup and sanity check, Day 2-5 counterfactual generation (7B primary, 3B parallel on Day 4-5), Day 5-7 probing and evaluation, Day 7-9 ablations including cross-scale analysis, Day 9-11 writing",
      "team": "2 researchers (1 on data generation/evaluation pipeline, 1 on probing/analysis/writing)",
      "estimated_gpu_cost": "$70-100 at ~$2.50/hr mid-range H100 rental"
    },
    "human_in_loop": {
      "gpu_hours": "~34-45 H100h (agent handles pipeline orchestration, human reviews label distributions and go/no-go)",
      "gpu_utilization": "60-75% — agent queues batch jobs efficiently, human reviews at checkpoints",
      "timeline": "9-11 days; Day 0-1 infrastructure (pre-download both checkpoints, index corpus, sanity check), Day 2-5 generation (7B + 3B), Day 6 go/no-go review, Day 7-9 evaluation, Day 10-11 writing",
      "team": "1 researcher, ~1-2hr/day reviewing label quality, probe results, go/no-go, and writing",
      "claude_api_cost": "$30-60 (~300-600 turns for code generation, experiment orchestration, analysis)",
      "estimated_gpu_cost": "$85-113 at ~$2.50/hr",
      "risk_note": "Primary risk is label distribution skew — if >60% of steps are 'mixed,' we pivot to soft-label regression as pre-committed. Human judgment on the go/no-go is essential by Day 6. Infrastructure risk mitigated by Day 0-1 sanity check."
    },
    "auto_research": {
      "gpu_hours": "~38-50 H100h (agent explores more threshold configurations and probe architectures, runs both 7B and 3B pipelines)",
      "gpu_utilization": "80-90% — agent pipelines generation → extraction → training → evaluation as continuous jobs",
      "timeline": "7-9 days with 4 H100s; Day 0-1 infrastructure, Day 2-4 generation (7B + 3B parallel), Day 5-6 probing/evaluation, Day 7-9 ablations/writing",
      "team": "0 (initial setup only: configure Search-R1/veRL/vLLM environment, dataset loading, retrieval corpus indexing — front-loaded to Day 0-1)",
      "claude_api_cost": "$80-150 (~800-1500 turns for autonomous experiment design, debugging, analysis, paper drafting)",
      "estimated_gpu_cost": "$95-125 at ~$2.50/hr",
      "speed_bottleneck": "Counterfactual generation is the bottleneck (~2-3h wall time on 4 H100s with vLLM batch for 7B; 3B runs ~40% faster); probe training and evaluation are fast (<1h each)",
      "risk_note": "Without human judgment on whether the 'mixed' class distribution warrants pivoting the paper framing, agent may produce a mechanically correct but uncompelling paper"
    }
  },
  "target_venues": [
    "EMNLP 2026 short paper via ARR May 25, 2026 (11 days — primary and only target, track: Information Retrieval and Text Mining or Question Answering)"
  ],
  "level": "top-tier",
  "key_references": [
    "Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval (NAACL 2025 Findings)",
    "Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing (Preprint 2026, arXiv 2604.15771)",
    "Probing Latent Knowledge Conflict for Faithful Retrieval-Augmented Generation [ProbeRAG/CLEAR] (ACL 2026 Findings per arXiv v3 April 2026 comments, arXiv 2510.12460)",
    "When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models [ReaLM-Retrieve] (Preprint 2026, arXiv 2604.26649)",
    "Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning (Preprint 2025, arXiv 2503.09516)",
    "SLATE: Truncated Step-Level Sampling with Process Rewards for Retrieval-Augmented Reasoning (Preprint 2026, arXiv 2602.23440)",
    "IG-Search: Step-Level Information Gain Rewards for Search-Augmented Reasoning (Preprint 2026, arXiv 2604.15148)",
    "TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs (Preprint 2026, arXiv 2603.22293)",
    "DeepControl: Scaling Search-Augmented LLM Reasoning via Adaptive Information Control (ICLR 2026 SPOT Workshop, arXiv 2602.01672)",
    "DART: Reasoning and Tool-use Compete in Agentic RL — From Quantifying Interference to Disentangled Tuning (Preprint 2026, arXiv 2602.00994)",
    "Disentangling Memory and Reasoning Ability in Large Language Models (ACL 2025, arXiv 2411.13504)",
    "Knowledge or Reasoning? A Close Look at How LLMs Think Across Domains (Preprint 2025, arXiv 2506.02126)",
    "Demystifying Scientific Problem-Solving in LLMs by Probing Knowledge and Reasoning [KRUX] (Preprint 2025, arXiv 2508.19202)",
    "Counterfactual Probing for Hallucination Detection and Mitigation in Large Language Models (Preprint 2025, arXiv 2508.01862)",
    "Adaptive Retrieval helps Reasoning in LLMs — but mostly if it's not used (Preprint 2025, arXiv 2602.07213)",
    "Active Retrieval Augmented Generation [FLARE] (EMNLP 2023)",
    "Counterfactual Reasoning for Retrieval-Augmented Generation [CF-RAG] (ICLR 2026)",
    "Disentangling Knowledge and Reasoning in Medical Large Language Models (Preprint 2025, arXiv 2505.11462)",
    "Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Preprint 2026, arXiv 2603.05488)",
    "SynthWorlds: Controlled Parallel Worlds for Disentangling Knowledge from Reasoning (Preprint 2025, arXiv 2510.24427)",
    "GRADE: Probing Knowledge Gaps in LLMs through Gradient Subspace Dynamics (Preprint 2026, arXiv 2604.02830)",
    "Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (Preprint 2026, arXiv 2605.13772)",
    "PRISM: Probing Reasoning, Instruction, and Source Memory in LLM Hallucinations (Preprint 2026, arXiv 2604.16909)",
    "Latent Abstraction for Retrieval-Augmented Generation [LAnR] (Preprint 2026, arXiv 2604.17866)"
  ],
  "description": "Current adaptive retrieval methods for reasoning LLMs use signals (uncertainty, token probability, composite scores) that conflate evidence gaps with reasoning difficulty, yet recent work confirms these are separable, task-dependent, and carry opposite optimal actions: evidence gaps demand retrieval even when the model appears confident (masking hallucinated knowledge), while reasoning difficulty demands suppressing retrieval even when the model appears uncertain (as retrieved context introduces noise). 'Disentangling Memory and Reasoning' (ACL 2025) achieves 83.3% disentanglement accuracy with explicit memory/reason tokens and finds 78–98% of commonsense errors stem from reasoning; KRUX (arXiv 2508.19202) finds knowledge retrieval from parameters is the dominant bottleneck for scientific tasks (base models with KIs outperform reasoning-enhanced models by ≥10%); 'Knowledge or Reasoning?' shows step-level knowledge-accuracy correlation of 0.998 vs. reasoning-accuracy 0.698; DART proves reasoning and tool-use produce competing gradients; ProbeRAG/CLEAR demonstrates 97–98% accuracy for sentence-level knowledge conflict detection via hidden-state probing; Skill-RAG finds failure states occupy structured regions in hidden-state space; and 'Where Does Reasoning Break?' demonstrates hidden states encode step-level correctness with 91% AUROC (though targeting binary correctness, not failure-mode type). We adopt the term 'counterfactual-branching probes' to distinguish from Feng (arXiv 2508.01862), who uses 'counterfactual probing' for a behavioral technique (testing model sensitivity to counterfactual input statements) unrelated to our hidden-state probing after execution forking. We present a focused empirical study with two first-class contributions. First, we introduce a counterfactual-branching labeling methodology that produces the first step-level failure-mode distribution for multi-hop factual QA: using Search-R1 checkpoints (Qwen2.5-7B primary, Qwen2.5-3B for cross-scale validation), we fork ~3,500-4,000 reasoning steps into retrieval and no-retrieval paths with k=5 rollouts each, generating causal labels ('evidence-gap,' 'reasoning-difficulty,' 'mixed'). Decision points are identified via two complementary heuristics: (a) positions where the model generated `&lt;search>` tokens (natural retrieval decisions), and (b) sentence-boundary sampling within `&lt;think>` blocks where the model did NOT search (counterfactual insertion points selected via entity/claim detection). The resulting distribution is directly actionable for system design: if evidence gaps dominate, this challenges reasoning-first approaches to multi-hop QA and validates retrieval-heavy architectures; if the distribution varies across HotpotQA, MuSiQue, and 2WikiMultiHopQA, this reveals that these benchmarks stress fundamentally different bottlenecks, with implications for benchmark selection and per-dataset strategy calibration; the evidence-gap proportion sets an upper bound on adaptive gating improvement; and the failure-mode mixture quantitatively predicts the severity of DART's gradient interference during RL training. Cross-scale comparison (7B vs. 3B) tests whether the distribution is a property of the task or the model capacity. Second, we train lightweight counterfactual-branching probes (linear and 3-layer MLP, following ProbeRAG/CLEAR's architecture) on hidden states to classify failure mode type, then apply the probe as an inference-time retrieval gate on the existing checkpoint without retraining — a proof-of-concept that the distribution is actionable: retrieve only when the probe predicts 'evidence-gap' or 'mixed,' skip retrieval when reasoning is the bottleneck. We pre-commit to significance thresholds for the central counterfactual-vs.-observational comparison: counterfactual-branching labels must yield ≥3 percentage points absolute improvement in binary gating accuracy OR ≥5% reduction in retrieval calls at matched downstream F1 (within 0.5 F1 points); if both are missed, we report a negative result, pivoting the paper to frame the failure-mode distribution as the primary contribution. If >50% of steps are 'mixed,' we pre-commit to soft-label regression on a continuous evidence-gap score. Key novelty vs. existing methods: (1) counterfactual-branching causal labels rather than observational correctness (Probing-RAG), RL reward shaping (IG-Search, TIPS, DeepControl), or explicit token-guided generation ('Disentangling Memory and Reasoning'), (2) failure-mode classification (evidence gap vs. reasoning difficulty) rather than binary correctness detection ('Where Does Reasoning Break?'), knowledge conflict detection (ProbeRAG/CLEAR), or hallucination taxonomy (PRISM), (3) post-hoc inference-time applicability without retraining, (4) cross-scale validation (7B + 3B) testing generalizability. Evaluation on HotpotQA, MuSiQue, and 2WikiMultiHopQA with baselines: no-retrieval, always-retrieve, Probing-RAG-style observational probe (critical ablation with pre-committed thresholds), and FLARE threshold. Infrastructure setup front-loaded to Day 0-1 with sanity check. Scoped as a short paper (~28-50 H100h total); RL integration deferred to follow-up.",
  "project_name": "evid_reason_disentangle",
  "source": "web_research"
}
```

**Summary of research findings that informed this revision:**

- **ProbeRAG/CLEAR venue verified**: arXiv v3 (April 15, 2026) explicitly claims "ACL 2026 Findings". The ICLR 2026 submission (OpenReview NhO6iEUISf) was withdrawn. ACL 2026 is July 2-7 in San Diego — proceedings aren't published yet, which explains the Anthology absence. Citation retained with transparent provenance.
- **KRUX (arXiv 2508.19202)**: Confirmed as a purely diagnostic framework using KI injection. Key finding: knowledge is the dominant bottleneck for scientific reasoning (≥10% gain). Desk-rejected at ICLR 2026, no other venue claimed — cited as preprint.
- **Feng 2508.01862**: Confirmed to use "counterfactual probing" for behavioral sensitivity testing with counterfactual statements — completely different methodology from our execution-forking approach.
- **Search-R1 Qwen2.5-3B**: Confirmed 4 checkpoints available on HuggingFace (PPO/GRPO × base/IT), making cross-scale validation feasible within budget.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81e8e241-11da-4bce-a064-092642d543af",
  "isSidechain": false,
  "requestId": "req_011Cb2pLe5gRHFYBY82fcua1",
  "type": "assistant",
  "uuid": "64d52c14-d5fd-45f2-ad29-244cff446107",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017AJcdYjWWfpT1UTyhjqcWU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22733,
      "cache_read_input_tokens": 49211,
      "output_tokens": 11708,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 11708,
          "cache_read_input_tokens": 49211,
          "cache_creation_input_tokens": 22733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22733
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

_source line 91_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Counterfactual Probing Disentangles Evidence Gaps from Reasoning Diffi…",
  "leafUuid": "64d52c14-d5fd-45f2-ad29-244cff446107",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Runtime record

_source line 92_

```json
{
  "type": "ai-title",
  "aiTitle": "Counterfactual step-level failure-mode classification for retrieval gating",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Runtime record

_source line 93_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-14 (UTC).**  ## Original idea {   \"title\": \"Counterfactual Probing Disentangles Evidence Gaps from Reasoning Diffi…",
  "leafUuid": "64d52c14-d5fd-45f2-ad29-244cff446107",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---

### Runtime record

_source line 94_

```json
{
  "type": "ai-title",
  "aiTitle": "Counterfactual step-level failure-mode classification for retrieval gating",
  "sessionId": "58a2f634-1766-42cc-9986-03afe86809d4"
}
```

---
