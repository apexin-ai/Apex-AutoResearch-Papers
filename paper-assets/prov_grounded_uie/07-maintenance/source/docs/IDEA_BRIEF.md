# Idea Brief: ProvUIE: Evidence-Span Co-Prediction as Verifiable Reward for Universal Information Extraction


- **Idea ID**: `idea_009`
- **Created**: 2026-05-12
- **Source**: web_research
- **Level**: top-tier
- **Target Venues**: AAAI 2027 (estimated abstract deadline: ~July 25, 2026; estimated full paper deadline: ~August 1, 2026, based on AAAI 2026 schedule; official AAAI 2027 dates TBD) — primary target, ~11-12 weeks from today, ICLR 2027 (estimated deadline: ~September 24, 2026) — secondary target, ~19 weeks from today, ARR May 2026 cycle → EMNLP 2026 commitment (ARR submission: May 25, 2026; commitment: August 2, 2026) — stretch goal with scoped-down plan: ACE05 + DocRED only (skip SciERC), Qwen3-8B as primary backbone, LoRA rank 32, 3 essential ablations (provenance reward ablation, NLI vs. IoU-only reward, with/without length penalty), total ~80-100 H100-hours; feasible only if the core SFT+GRPO pipeline works on the first attempt within the 14-day window. Recommendation: given the 14-day timeline, we recommend AAAI 2027 as the primary target, with a minimal-viable ARR May 2026 submission as a stretch goal.

## Seed Topic

Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Information Extraction.

Direction: Structured information extraction — named entity recognition, relation extraction, event extraction, document-level IE, end-to-end extraction pipelines. Both LLM-based and non-LLM approaches welcome. In-scope: schema-guided extraction, zero-shot/few-shot IE, cross-document extraction, multimodal IE (text + layout + images), temporal/causal relation extraction.

Contribution type: METHOD ONLY. New extraction architectures, training strategies, or inference algorithms. Not a new dataset or annotation guideline.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. IE work is typically lightweight — most experiments are fine-tuning or in-context learning.
2. Time: ≤16 days. Use existing IE frameworks (GoLLIE, UniNER, USM) or build on open LLMs with structured output.
3. Eval: ACE05, SciERC, TACRED/TACREV, DocRED, MAVEN, Few-NERD, WikiEvents, RAMS.

Look for: schema-guided extraction that generalizes across domains, efficient document-level IE beyond sliding windows, extraction with faithful provenance/citation, structured extraction from semi-structured sources (tables, forms, code). Avoid: basic NER fine-tuning, prompt-only extraction without architectural insight.

Tag: direction=information_extraction, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].

## Generation Journey

1. **Start** — 开始生成，seed: 'Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Information Extraction.\n\nDirection: Structured information extraction — named entity recognition, relation extraction, event extraction, document-level IE, end-to-end extraction pipelines. Both LLM-based and non-LLM approaches welcome. In-scope: schema-guided extraction, zero-shot/few-shot IE, cross-document extraction, multimodal IE (text + layout + images), temporal/causal relation extraction.\n\nContribution type: METHOD ONLY. New extraction architectures, training strategies, or inference algorithms. Not a new dataset or annotation guideline.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. IE work is typically lightweight — most experiments are fine-tuning or in-context learning.\n2. Time: ≤16 days. Use existing IE frameworks (GoLLIE, UniNER, USM) or build on open LLMs with structured output.\n3. Eval: ACE05, SciERC, TACRED/TACREV, DocRED, MAVEN, Few-NERD, WikiEvents, RAMS.\n\nLook for: schema-guided extraction that generalizes across domains, efficient document-level IE beyond sliding windows, extraction with faithful provenance/citation, structured extraction from semi-structured sources (tables, forms, code). Avoid: basic NER fine-tuning, prompt-only extraction without architectural insight.\n\nTag: direction=information_extraction, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].'
2. **Problem Discovery** (959s) — 发现 4 个研究方向
   - Structural Self-Consistency Scaling for Information Extraction
   - Provenance-Grounded Universal Information Extraction
   - Schema-Semantic Constrained Decoding for Information Extraction
   - Process Reward Models for Stepwise IE Verification
3. **Method Synthesis** (618s) — 完成: "Structural Self-Consistency Scaling for Information Extraction" [solid] → EMNLP 2026 (ARR submission deadline: May 25, 2026), AACL-IJCNLP 2026 (ARR submission deadline: May 25, 2026; Nov 6-10 Hengqin, China), AAAI 2027 (abstract: Jul 25, paper: Aug 1, 2026; Feb 16-23 Montréal)
3. **Method Synthesis** (515s) — 完成: "Provenance-Grounded Universal Information Extraction" [top-tier] → EMNLP 2026 (ARR submission deadline: May 25, 2026; commitment deadline: August 2, 2026), AAAI 2027 (expected deadline ~late July 2026, based on AAAI-26 pattern of July 25/Aug 1), ICLR 2027 (expected deadline ~September 2026, based on ICLR 2026 pattern of Sep 24)
3. **Method Synthesis** (490s) — 完成: "Schema-Semantic Constrained Decoding for Information Extraction" [solid] → EMNLP 2026 (ARR submission deadline: May 25, 2026), AACL-IJCNLP 2026 (ARR submission deadline: May 25, 2026), AAAI 2027 (expected deadline: ~August 1, 2026)
3. **Method Synthesis** (659s) — 完成: "Process Reward Models for Stepwise IE Verification" [solid] → EMNLP 2026 (ARR submission May 25, 2026 — very tight, stretch goal only), AACL 2026 (ARR submission May 25, 2026, commitment Aug 26, 2026), AAAI 2027 (submission Aug 1, 2026), ICLR 2027 (submission Sep 24, 2026), NAACL 2027 (submission Oct 16, 2026)

## Core Problem

How can LLM-based UIE systems produce extractions that are verifiably grounded in source text, jointly outputting structured knowledge AND explicit evidence spans — going beyond prompt-level grounding constraints to make provenance a learnable, reward-verified training objective?

## Opportunity / Why Now

Recent RLVR-for-IE work has shown that GRPO can improve extraction quality (R2GRPO for SciIE, R1-RE for cross-domain RE, ReasoningNER for zero-shot NER, ProUIE for unified NER+RE+EE, Extract-0 for document IE), and EvidenceRL demonstrated NLI-based grounding rewards for QA. However, a critical gap persists: (1) ProUIE enforces 'values must be exact substrings of the input' as a prompt instruction but never verifies grounding as a reward signal — its SFR rewards measure structural F1 only; (2) R2GRPO's relevancy reward checks reasoning-trace grounding for single-task RE but does not produce explicit evidence spans as structured output; (3) EvidenceRL uses NLI-based grounding as an internal GRPO reward for QA but does not output evidence spans and does not handle structured IE; (4) Extract-0 applies GRPO with semantic-similarity rewards to document IE but targets schema-free extraction without provenance span output or NER/RE/EE task structure; (5) ReasoningNER and R1-RE apply GRPO to NER and RE respectively without any provenance mechanism; (6) SafePassage co-predicts entity extractions with mandatory context fields verified via Smith-Waterman alignment, but operates as a post-hoc pipeline without RL-based training — evidence fidelity is verified at inference time, not learned as a training objective; (7) TRACE uses GRPO with adaptive rewards to produce evidence-attributed outputs for multi-hop QA, but operates in the RAG domain without structured IE output or multi-task NER/RE/EE support. Critically, LongRLVR (ICLR 2026) formally proves that outcome-only rewards produce vanishing gradients for context grounding, establishing the theoretical necessity of dense evidence-level rewards — which no existing IE system provides. No existing system jointly trains evidence-span co-prediction as structured output with provenance fidelity as a decomposed verifiable reward across the full IE stack (NER+RE+EE).

## Landscape (SOTA & Limitations)

The RLVR-for-IE landscape has advanced rapidly: R1-RE (arXiv 2507.04642) pioneered RLVR for relation extraction using GRPO with format+metric rewards on Qwen2.5-7B, achieving ~70% OOD accuracy rivaling GPT-4o. R2GRPO (arXiv 2505.22068) introduced relevancy and rule-induced rewards for scientific IE on Qwen2.5-7B, where the relevancy reward maps cited reasoning-trace content to gold evidence with a length penalty (achieving 84.36 NER F1 and 66.81 RE F1 on SciERC) — but this checks reasoning grounding, not structured evidence output. ReasoningNER (arXiv 2511.11978) applied GRPO with F1+schema rewards to NER via a three-stage CoT pipeline, achieving 72.4 F1 zero-shot on CrossNER with Qwen3-8B. ProUIE (arXiv 2604.10633) proposed macro-to-micro progressive learning with stepwise fine-grained rewards (SFR) decomposed by entity/relation/argument structural units on Qwen3-4B, enforcing substring grounding via prompt constraint — achieving 86.15 NER F1 on ACE05 and 79.44 average NER F1 across 36 datasets. Extract-0 (arXiv 2509.22906) demonstrated GRPO with a novel semantic-similarity reward (embedding-based field matching via MiniLM) for document information extraction on DeepSeek-R1-Distill-Qwen-7B, achieving 0.573 mean reward surpassing GPT-4.1 (0.457) at only $196 total training cost — demonstrating GRPO's effectiveness for IE with verifiable rewards, though targeting schema-free document extraction rather than the NER/RE/EE stack. MR-UIE applies RL without provenance verification for UIE. In the RLVR-for-attribution space beyond IE, TRACE (arXiv 2505.13258) uses GRPO with adaptive rewards to train LLMs for evidence-attributed multi-hop QA, achieving 10-30% accuracy improvements with structured evidence traceability — demonstrating GRPO's viability for evidence-grounded generation, though applied to RAG/QA rather than structured IE. EviOmni (arXiv 2507.15586) learns rational evidence extraction for RAG via GRPO with verifiable rewards, integrating evidence reasoning and extraction into unified trajectories — again in the RAG domain, not structured IE. In the theoretical foundations for evidence-level rewards, LongRLVR (ICLR 2026, arXiv 2603.02146) formally proves that outcome-only rewards lead to significant vanishing gradients for context grounding in RLVR, demonstrating that dense verifiable context rewards are necessary for effective evidence selection — boosting a 14B model on RULER-QA from 73.17 to 88.90 and LongBench v2 from 39.8 to 46.5. This provides direct theoretical motivation for ProvUIE's provenance fidelity reward design, confirming that evidence-level dense rewards are not merely helpful but theoretically necessary for grounding. In the evidence-co-prediction space, SafePassage (arXiv 2510.00276, Oct 2025) introduced evidence co-prediction for IE by requiring LLMs to output context fields alongside extractions, verified post-hoc via Smith-Waterman character-level alignment and a scoring model, reducing hallucinations by 85% — but operates as a pipeline without RL training, making evidence fidelity a verification criterion rather than a learnable training signal. In the grounding-as-reward space, EvidenceRL (arXiv 2603.19532) demonstrated GRPO with Focus-Then-Verify NLI-based sentence-level entailment checking for medical/legal QA, using PubMedBERT-MNLI and DeBERTa-v3-NLI — but grounding operates purely as an internal reward signal without explicit evidence span output. Faithful GRPO introduced constrained policy optimization for visual grounding. In evidence-annotated IE, DocRED (ACL 2019) provides supporting evidence sentence annotations for document-level relations, with Evi F1 as the established evaluation metric. GEGA (ICASSP 2025, arXiv 2407.21384) advanced document-level RE using GCN and evidence retrieval guided attention, achieving 56.09 Evi F1 (dev) / 55.89 Evi F1 (test) on DocRED — surpassing DREEAM (52.08 dev / 51.71 test) via hand-crafted graph neural network pipelines with explicit evidence retrieval modules to set the current SOTA. CDER (arXiv 2504.06529) proposed collaborative evidence retrieval for DocRE but achieved lower Evi F1 (~52.9) than GEGA. AEVS (2025) demonstrated anchor-constrained provenance tracking for KG triplets. LAQuer (ACL 2025) introduced localized span-level attribution queries for content-grounded generation, enabling user-directed fine-grained attribution — a paradigm complementary to our automatic evidence co-prediction. The fundamental limitation: current UIE systems either (a) use grounding as a prompt constraint without reward verification (ProUIE), (b) verify grounding in reasoning traces without structured evidence output (R2GRPO), (c) apply NLI grounding rewards outside of structured IE (EvidenceRL), (d) use semantic-similarity rewards for document IE without provenance span output or multi-task IE structure (Extract-0), (e) co-predict evidence fields via post-hoc pipeline verification without RL-based training (SafePassage), or (f) use GRPO for evidence-attributed generation in RAG/QA but not structured IE (TRACE, EviOmni). None jointly train evidence-span co-prediction as structured output with provenance fidelity as a verifiable reward dimension across the full IE stack.

## Proposed Approach

We propose ProvUIE, which extends schema-as-code UIE (GoLLIE/KnowCoder paradigm) with mandatory evidence-span co-prediction: for every entity, relation, or event argument, the model must output the minimal source span(s) grounding the extraction as part of the structured output. Motivated by LongRLVR's formal proof that outcome-only rewards produce vanishing gradients for context grounding (ICLR 2026), our provenance fidelity reward provides dense evidence-level supervision during GRPO training — addressing a theoretically established limitation of outcome-only reward designs. For NER specifically, evidence is defined as the disambiguating context window — the minimal surrounding text that makes entity-type classification unambiguous (e.g., for 'Obama' typed as Person, the evidence span includes 'President ... spoke at' rather than the trivially circular mention itself). For RE and EE, evidence spans are the sentence(s) supporting the relation or event argument. Training uses a two-phase protocol on ACE05, SciERC, and DocRED: (1) SFT with LoRA on Qwen3-32B using automatically aligned provenance annotations — for DocRED, we directly leverage its gold supporting-evidence sentence annotations; for ACE05 and SciERC, we derive provenance via gold-label-to-source-span alignment using dependency-parse-guided minimal context extraction; (2) GRPO with a composite verifiable reward decomposed into three dimensions: (a) structural extraction F1 with stepwise granularity at entity/relation/argument levels (building on ProUIE's SFR methodology), (b) provenance fidelity — whether predicted evidence spans support the extraction, verified via character-overlap IoU AND frozen DeBERTa-v3-large NLI entailment scoring, with a length penalty to prevent degenerate full-sentence copying (addressing the reward hacking risk identified in auto-research settings), and (c) format compliance. NLI reward computation overhead: running frozen DeBERTa-v3-large (~400M params) on (evidence_span, extraction) pairs during GRPO rollouts adds an estimated 30-50% compute overhead; this is mitigated by (i) batched NLI inference across all rollouts per batch (DeBERTa-v3-large processes ~2000 pairs/sec on a single H100), (ii) caching NLI scores for identical evidence-extraction pairs across rollouts, and (iii) sampling-based reward estimation when extraction count per input exceeds 10 pairs, scoring a random subset and averaging. This design differs from prior work in five specific ways: unlike ProUIE which relies on prompt-level substring instructions without reward verification, ProvUIE makes grounding a learnable reward signal verified via NLI entailment; unlike R2GRPO which checks relevancy of reasoning traces for single-task RE, ProvUIE requires explicit evidence span output as structured data across the full UIE stack; unlike EvidenceRL which uses NLI grounding internally for QA rewards without evidence output, ProvUIE co-predicts evidence spans as first-class structured output alongside extractions; unlike SafePassage which co-predicts evidence fields with post-hoc Smith-Waterman verification as a pipeline, ProvUIE makes evidence fidelity a learnable reward signal in end-to-end GRPO training; unlike TRACE which uses GRPO for evidence-attributed multi-hop QA, ProvUIE targets the full structured IE stack (NER+RE+EE) with provenance as a decomposed reward across entity/relation/argument granularities. We use Qwen3-32B as the primary backbone with LoRA (rank 64) for parameter-efficient training — providing a larger parameter count and pure Transformer architecture well-established for structured generation. While Qwen3.6-27B (April 2026) offers a newer hybrid DeltaNet-Attention architecture, its suitability for schema-constrained IE output is less validated; we plan to evaluate it if compute allows. Qwen3-8B serves as a development/ablation backbone for rapid iteration. Compute fallback plan: if any 32B GRPO run fails (each costing ~30h), we fall back to Qwen3-8B as the primary backbone (reducing per-run cost from ~30h to ~8h) and report 32B results only if compute budget remains. NER evidence evaluation strategy: since no established gold standard exists for NER disambiguating context windows (unlike DocRED which provides gold evidence sentences for RE), we adopt a three-tier evaluation approach: (a) automatic evaluation against silver-standard evidence spans derived via dependency-parse-guided context extraction on ACE05 and SciERC, reporting IoU and coverage metrics; (b) human evaluation on a 100-instance stratified sample per dataset, where annotators judge whether predicted NER evidence spans are sufficient and minimal for entity-type disambiguation (binary sufficiency + minimality ratings), establishing inter-annotator agreement; (c) intrinsic analysis of evidence span length distributions to detect degenerate patterns (e.g., full-sentence copying). We acknowledge that NER evidence evaluation is intrinsically harder than RE evidence evaluation where DocRED provides gold annotations, and frame our NER evidence metrics as a proposed evaluation protocol rather than a comparison against established gold. Expected performance: we hypothesize comparable or modestly improved extraction F1 (+1-2 points over ProUIE/R2GRPO baselines, accounting for our larger 32B backbone), with the primary contribution being the introduction of provenance-aware attribution metrics (evidence span IoU, attribution precision, attribution recall) that no existing UIE system reports. Specifically, we target: NER F1 ≥87 on ACE05 among LLM-based generative approaches (note: encoder-based span models such as BINDER achieve 90.0 F1 but are not directly comparable to our generative UIE setting), RE Evi F1 competitive with GEGA (55.89 test / 56.09 dev on DocRED) while using end-to-end GRPO training rather than GEGA's hand-crafted GCN+evidence retrieval pipeline — demonstrating that provenance fidelity as a verifiable reward can match supervised evidence retrieval approaches without task-specific architectural engineering, and attribution precision ≥80% (fraction of extractions with valid NLI-verified evidence). The key empirical question is whether the provenance reward improves or trades off extraction quality; even if extraction F1 is neutral, demonstrating high attribution metrics alongside competitive extraction would establish a new evaluative standard for trustworthy IE.

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$300-500 (~3000-5000 conversation turns for iterative experiment design, error recovery, ablation planning)', 'compute_fallback': 'If any 32B GRPO run fails (~30h each), fall back to Qwen3-8B as primary backbone (reducing per-run cost from ~30h to ~8h) and report 32B results only if compute budget remains.', 'estimated_gpu_cost': '$330-600 (at ~$2.00/hr H100 spot pricing)', 'gpu_hours': '~165-200 H100-hours (sweeps over provenance reward weight and NLI threshold with reduced grid — 3 NLI threshold values instead of 5; LoRA rank fixed at 64; backbone ablation on Qwen3-8B; ~30-50% overhead from DeBERTa-v3-large NLI scoring during GRPO rollouts)', 'gpu_utilization': '85-95% — agent runs 24/7 launching next experiment immediately after each completes', 'risk_note': 'Fully automated provenance reward engineering may converge on degenerate patterns (e.g., model copies entire input sentence as evidence to maximize overlap); mitigated by length-penalty term in provenance reward and periodic automated checks on evidence span length distribution. NLI scoring overhead (~30-50% additional compute) is the primary cost increase vs. standard GRPO. Budget is tight at ≤200h — one failed 32B GRPO run (~30h) would require reducing ablation scope.', 'speed_bottleneck': 'GPU count — need 4 concurrent H100s for the 10-15 day timeline; single-GPU extends to 5-7 weeks. Secondary: GRPO rollout generation throughput on 32B model with LoRA, compounded by DeBERTa-v3-large NLI scoring overhead per rollout', 'team': '0 (initial setup only: ~4 hours to configure codebase, datasets, and evaluation pipeline)', 'timeline': '10-15 days with 4 concurrent H100 GPUs'}
- **human_in_loop**: {'claude_api_cost': '$100-200 (~1000-2000 conversation turns at ~$0.10/turn)', 'compute_fallback': 'If any 32B GRPO run fails (~30h each), fall back to Qwen3-8B as primary backbone (reducing per-run cost from ~30h to ~8h) and report 32B results only if compute budget remains.', 'estimated_gpu_cost': '$350-600 (at ~$2.00/hr H100 spot pricing)', 'gpu_hours': '~175-200 H100-hours (hyperparameter sweeps on provenance reward weight and NLI threshold, with LoRA rank fixed at 64 to stay within budget; NLI overhead from DeBERTa-v3-large scoring during GRPO rollouts)', 'gpu_utilization': '50-65% — agent queues experiments, pauses at approval gates for reward design decisions and provenance annotation quality checks', 'risk_note': 'Provenance reward calibration requires human judgment — automated gold-label-to-source alignment may introduce noisy supervision that compounds during GRPO; human must verify annotation pipeline quality before RL phase. NER evidence human evaluation adds ~8 hours of annotation time.', 'team': '1 researcher, ~45min/day check-in for reward calibration and provenance annotation quality review; ~8 hours total for human evaluation of 100-instance NER evidence samples', 'timeline': '6-8 weeks'}
- **manual**: {'compute_fallback': 'If any 32B GRPO run fails (~30h each), fall back to Qwen3-8B as primary backbone (reducing per-run cost from ~30h to ~8h) and report 32B results only if compute budget remains.', 'estimated_gpu_cost': '$280-570 (at ~$2.00/hr H100 spot pricing, Q2 2026)', 'gpu_hours': '~140-190 H100-hours (SFT w/ LoRA ~25-35h, GRPO ~75-100h including ~30-40% NLI reward overhead, ablations on Qwen3-8B + eval ~40-55h)', 'gpu_utilization': '~20-25% effective utilization; GPUs idle during code development, debugging, result analysis', 'team': '1-2 researchers', 'timeline': '3-4 months'}

## Key References

- R2GRPO: Beyond Path Selection — Better LLMs for Scientific IE with MimicSFT and R²GRPO (arXiv 2505.22068, May 2025)
- R1-RE: Cross-Domain Relation Extraction with RLVR (arXiv 2507.04642, July 2025)
- EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models (arXiv 2603.19532, March 2026)
- ReasoningNER: A Reasoning Paradigm for Named Entity Recognition (arXiv 2511.11978, Nov 2025)
- ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based UIE (arXiv 2604.10633, April 2026)
- Extract-0: A Specialized Language Model for Document Information Extraction (arXiv 2509.22906, Sep 2025)
- GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)
- KnowCoder: Coding Structured Knowledge into LLMs for UIE (ACL 2024)
- DocRED: A Large-Scale Document-Level Relation Extraction Dataset (ACL 2019)
- DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction (EACL 2023)
- GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction (ICASSP 2025, arXiv 2407.21384)
- CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction (arXiv 2504.06529, April 2025)
- AEVS: Grounded KG Extraction via LLMs with Anchor-Constrained Provenance Tracking (Computers 2026)
- MR-UIE: Multi-Perspective Reasoning with RL for UIE (Vicinagearth 2025)
- PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction (EMNLP 2025)
- Faithful GRPO: Improving Visual Spatial Reasoning via Constrained Policy Optimization (arXiv 2026)
- LAQuer: Localized Attribution Queries in Content-grounded Generation (ACL 2025)
- DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models (arXiv 2024)
- FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding (arXiv 2026)
- LongRLVR: Long-Context Reinforcement Learning Requires Verifiable Context Rewards (ICLR 2026, arXiv 2603.02146)
- SafePassage: High-Fidelity Information Extraction with Black Box LLMs (arXiv 2510.00276, Oct 2025)
- TRACE: Towards Transparent RAG — Fostering Evidence Traceability in LLM Generation via Reinforcement Learning (arXiv 2505.13258, May 2025)
- EviOmni: Learning to Extract Rational Evidence via Reinforcement Learning for RAG (arXiv 2507.15586, July 2025)

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': "Exceptionally thorough competitor positioning against 10+ systems with honest differentiation. Approach is well-specified: three reward dimensions (structural F1, provenance fidelity via IoU+NLI+length penalty, format compliance), three-tier NER evidence evaluation protocol, and calibrated performance expectations (+1-2 F1 improvement with primary contribution being attribution metrics). The NER evidence definition as 'disambiguating context window' elegantly resolves the circularity concern.", 'score': 4}**/5
  - feasibility: **{'rationale': 'For AAAI 2027 primary target (~11-12 weeks), timeline is adequate. Budget fits within ≤200 H100-hours (manual 140-190h, auto 165-200h) with concrete fallback to Qwen3-8B. All building blocks are proven (GRPO for IE via ProUIE/R2GRPO, LoRA on 32B models, DeBERTa-v3-large NLI scoring). NLI reward overhead (~30-50%) is acknowledged and mitigated via batching/caching. EMNLP stretch goal is honestly aggressive but scoped down to ACE05+DocRED with Qwen3-8B.', 'score': 4}**/5
  - impact: **{'rationale': 'Introduces provenance-aware attribution metrics (evidence IoU, attribution precision/recall) as a new evaluation standard for UIE — no existing system reports these alongside extraction F1. If DocRED Evi F1 matches GEGA (~55.9) via end-to-end GRPO rather than hand-crafted GCN+evidence retrieval, it demonstrates that provenance fidelity as a learnable reward can replace task-specific architectural engineering. Theoretical backing from LongRLVR establishes the necessity of dense evidence-level rewards, giving the work strong foundational grounding.', 'score': 4}**/5
  - novelty: **{'rationale': "Genuinely novel integration: evidence-span co-prediction as structured output + provenance fidelity as a decomposed verifiable GRPO reward across the full UIE stack (NER+RE+EE). Individual components exist in adjacent domains (EvidenceRL for NLI rewards in QA, SafePassage for evidence co-prediction as pipeline, R2GRPO for relevancy reward in single-task RE), but no prior system combines them. Well-differentiated from 10+ competitors with honest positioning, and strongly motivated by LongRLVR's formal proof (ICLR 2026) that outcome-only rewards produce vanishing gradients for context grounding.", 'score': 4}**/5

## Human Review Note

## Agent 审核结果（完整三阶段 pipeline）

**Verdict**: KILL_triage

**入口三重共识 (X)**: 21.0%
**终审自评 (Y)**: N/A
**出口三重共识 (Z)**: N/A
**Z 区间**: N/A
**真实提升 (Z-X)**: N/A
**幻觉幅度 (Y-Z)**: N/A
**出口一致性**: N/A
**出口三次评估**: N/A

### 优化方案 / 拒绝详情
【阶段】: Meta Judge

【三次中位】: [25%, 17%, 24%]  std=3.6%

【共识维度】:
- **Feasibility: 强**（3/3 一致）—— 三位审稿人均认为这是 proposal 最突出的维度，计算预算合理、数据集公开、fallback 计划务实
- **Technical Soundness: 中**（3/3 一致，R3 略偏强）—— 方法论整体合理，SFT→GRPO pipeline 成熟，但 +1-2 F1 信号极弱引发有效性疑问
- **Novelty: 中至弱**（3/3 均指出核心贡献是已有组件的组合迁移）—— 三位均认定 ProvUIE 处于 ProUIE + LongRLVR/EvidenceRL/TRACE 的交叉覆盖区，positive result "I would have guessed this"
- **Significance: 弱-中**（3/3 均指出 +1-2 F1 marginal + attribution metrics 作为 primary contribution 说服力不足）
- **ProUIE 压缩 novelty 空间**（3/3 共识）—— 三位均将 ProUIE（2604.10633, 2026年4月）识别为最具威胁的竞争者
- **R2GRPO 引用不可验证**（3/3 共识）—— 三位均无法在公开文献中找到此论文
- **预期 F1 仅 +1-2 点处于噪声边缘**（3/3 共识）—— 核心经验贡献薄弱
- **Related Work: 中至弱**（R1=中, R2=弱, R3=中）—— 2/3 给中，共识偏中

【异常维度】:
- **R2 将 Novelty 评为「弱」**（R1、R3 均为「中」）—— R2 额外强调了 proposal 对 ProUIE 的描述构成"事实性错误"（称其仅用 prompt-level substring instructions，而 ProUIE 实际已使用 GRPO+SFR 分层奖励），认为这不仅是 novelty 问题更是 scholarship 可信度问题。R1 和 R3 也注意到了 ProUIE 描述的不准确性，但未将其升级为"事实性错误"级别。
- **R2 将 Related Work 评为「弱」**（R1、R3 均为「中」）—— 同样源于 ProUIE 误述 + R2GRPO 不可验证的双重打击。
- **R1 独有地指出遗漏了 EAPO**（Evidence-Augmented Policy Optimization, 2026年1月）；**R3 独有地指出遗漏了 Ground-GRPO、MR-UIE、MORE-R1、LAT** 等近期工作 —— 这些遗漏进一步印证 related work 覆盖不完整。

【最终概率】: [15% - 26%] 中位 21%

【一致性】: 中（std=3.6%，处于 3-7% 区间；R2 偏严但其核心论据被其他两位部分认可）

【综合理由】:

三位审稿人在核心判断上高度一致：ProvUIE 是一个**形式完善、执行方案扎实但内核薄弱**的 proposal。共识清晰地指向以下结论链：

1. **Novelty 是主要瓶颈**（3/3 共识）。ProvUIE 的贡献本质上是将已验证思路（evidence 作为 GRPO 可验证奖励）迁移到已有 GRPO+UIE 框架（ProUIE）中。三位均预判审稿人反应为 "I would have guessed this"。R2 额外指出 proposal 对 ProUIE 的差异化描述与事实不符——虽然 R1/R3 措辞较温和，但三位都注意到了这一问题。考虑到这是 novelty 立论的基石，即使不上升到"事实性错误"，描述不准确本身也会被审稿人追问并削弱差异化论证。

2. **Significance 受限于 marginal gains**（3/3 共识）。+1-2 F1 处于噪声边缘，primary contribution 转向 attribution metrics——但这些指标缺乏社区共识和金标验证。三位均认为这更接近 Findings/evaluation track 定位。

3. **Feasibility 无争议地强**（3/3 共识），但"能做"不能补偿"是否值得在 EMNLP main 发"。

R2 的概率估计（17%）低于 R1（25%）和 R3（24%），差距约 7-8pp。R2 的额外降分主要来自 ProUIE 误述的严重性判定。虽然 R2 是 outlier，但其论据（ProUIE 描述不准确→差异化论证基础不稳）在事实层面是成立的，且 R1/R3 也部分认可。按照"分歧时偏严"原则，最终中位从三位中位（24%）向下调整至 21%，反映以下权衡：
- ProUIE 差异化描述的不准确性确实会被审稿人 flag，但未必构成 paper-level 的"事实性错误"——可能通过修正描述部分缓解
- 即使修正描述后，residual novelty（evidence 维度的奖励 vs. ProUIE 的结构匹配奖励）仍然是增量式的
- 21% 位于"15-20% 形式完善但内核薄弱"锚点的上缘，反映了 proposal 的高形式完善度对概率的微弱提升

上界（26%）被 Novelty 和 Significance 双重限制：即使 ProUIE 描述问题被完美修正、遗漏的 related work 被补齐，核心 "组合迁移" 性质不变。下界（15%）反映了 R2 所指出的最坏情况：审稿人同时 flag ProUIE 误述 + R2GRPO 不可验证 + marginal gains。

【建议】: 边缘（中位 21% 接近 22% 入口阈值线；若进入迭代，需重点解决 ProUIE 差异化描述和 novelty 增强）

【实施评估】:
- **计算资源**: ≤200 H100-hours（三方一致）。Qwen3-32B 单次 SFT+GRPO 约 30h/run（含 DeBERTa NLI 推理的 ~30-50% overhead）；8B fallback 约 8h/run。需 4-8× H100 集群（或等效云计算）。含多轮 ablation 实验，总训练时长约 100-200 H100-hours。
- **数据需求**: ACE05（需 LDC 许可，学术界广泛可得）、SciERC（公开）、DocRED（公开，含 evidence annotations）。三者均为 IE 领域标准 benchmark，无获取障碍。无需新数据采集。
- **人工介入**: 100-instance human evaluation for NER evidence 质量评估。需 2-3 名标注员，预估 10-20 人时。需设计标注指南。规模可控但统计显著性可能被质疑（R1 指出 100 instances 偏小）。
- **训练需求**: 需要模型训练。两阶段：SFT（LoRA）+ GRPO。主方案 Qwen3-32B，fallback Qwen3-8B。含 ablation 实验（奖励组件消融、backbone 对比等），总训练投入显著。
- **新 Benchmark**: 不构建全新 benchmark，但需构建 NER evidence 三层评估协议（silver-standard auto-eval + 100-instance human eval + span-length analysis），需为 ACE05/SciERC 生成 silver NER evidence annotations（原数据集无金标 NER evidence）。有一定工程量。
- **预估周期**: 完整版（AAAI 2027 / ICLR 2027 target）约 3-4 个月从启动到可投稿。Stretch goal（ARR May 2026 → EMNLP 2026）14 天完成核心 pipeline，三方一致认为风险极高。合理估计 EMNLP 版最短需 3-4 周（R1 估计），完整版含 ablation + writing 需 10-14 周（R2 估计）。

