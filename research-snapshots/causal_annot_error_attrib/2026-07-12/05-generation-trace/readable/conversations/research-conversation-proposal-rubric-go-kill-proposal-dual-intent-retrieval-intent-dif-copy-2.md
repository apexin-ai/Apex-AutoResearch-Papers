# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Dual-Intent Retrieval: Intent-Dif

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/b8aff3a6-0b8d-43d9-9984-5455ff59a891.jsonl`
- **Structured JSON:** [`d1b654f0dfb7540646eb.json`](../../sessions/d1/d1b654f0dfb7540646eb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T01:48:41.481Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T01:48:41.481Z",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Dual-Intent Retrieval: Intent-Differentiated Query Formulation for Reasoning-Augmented RAG\n\n**状态**: 待审阅  \n**级别**: top-tier  \n**创建时间**: 2026-05-15T16:06:37.791174+00:00\n\n## 描述\nWe propose Dual-Intent Retrieval, a method that explicitly classifies each retrieval call within a reasoning model's chain-of-thought as either discovery-intent (seeking new evidence to advance reasoning) or verification-intent (seeking evidence to confirm or refute an intermediate claim), then applies structurally different query construction and retrieval strategies for each. Discovery queries use standard BM25 retrieval, matching its strength at keyword-rich information-seeking queries. Verification queries use a hybrid BM25+dense retrieval pipeline with NLI-based contrastive reranking: given an intermediate claim, the model generates contrastive queries (seeded by templates during SFT, refined through RL), retrieves via both BM25 and E5-base-v2 dense retrieval, and re-ranks by evidential discriminativeness using DeBERTa-v3-base NLI scoring, surfacing documents that most clearly support or refute the claim.\n\nThis operationalizes an insight that ReaLM-Retrieve empirically observed but did not act upon: its behavioral analysis (Section 6.9) identifies 'verification retrievals' as a distinct pattern in 31% of cases that reduces backtracking by 18%, while its failure analysis finds that over-retrieval during exploration accounts for 31% of failures. Despite observing that retrieval intent varies structurally, ReaLM-Retrieve's QueryGen maps all retrieval calls through the same learned embedding space without differentiating strategy. Even Veri-R1 (Oct 2025), which trains verification-specific RL policies via GRPO with a multi-component reward (label + evidence IoU + format + validity), uses uniform query construction across all search turns. We make this insight actionable.\n\nThe approach addresses a broader gap: ReaLM-Retrieve adapts queries implicitly without distinguishing purpose; CoRAG (NeurIPS 2025) reformulates queries iteratively but uniformly; DeepControl (ICLR 2026 Workshop) controls retrieval volume, not query strategy; AutoRefine (NeurIPS 2025) refines evidence post-retrieval; RAG-Star (NAACL 2025) verifies answers in MCTS with uniform retrieval; Veri-R1 (Oct 2025) trains verification-specific RL but uses uniform query construction; RAFTS (ACL 2024) demonstrates contrastive argument synthesis for fact-checking but operates standalone; Reason and Verify (Mar 2026) structures verification taxonomies for biomedical RAG but applies uniform retrieval. None classify intent and differentiate query construction within RL-trained sequential reasoning.\n\nThe contribution is dual: (1) explicit intent classification with structurally differentiated retrieval pipelines, and (2) RL-discovered verification query strategies that emerge from the &lt;verify>claim ||| query&lt;/verify> format. The latter is a co-equal contribution: the structured format creates a rich action space for GRPO to discover sophisticated verification strategies (e.g., negation patterns, contrastive framing, claim-type-specific formulations) that humans might not manually design — and the query evolution analysis in Phase 3 is positioned as a key expected finding.\n\nBuilt atop Search-R1's open-source RL framework using Qwen2.5-7B (chosen over Qwen3-8B to avoid a known 10-20× GRPO training speed regression in veRL), we introduce intent tokens (&lt;discover>/&lt;verify>) and train via GRPO with a composite reward combining answer correctness and faithfulness. A critical design choice: we use different NLI model families for verification reranking (DeBERTa-v3-base, 184M params) vs. faithfulness reward (RoBERTa-large-NLI, 355M params) to prevent circular optimization where the policy learns to game its own reward signal. Intent labels are bootstrapped via heuristic rules for SFT cold start, then refined through RL. The &lt;verify>claim ||| query&lt;/verify> format allows RL to learn sophisticated query formulations beyond initial templates, following RAFTS's insight that LLM-generated contrastive formulations outperform fixed templates. We evaluate on six benchmarks — MuSiQue, HotpotQA, 2WikiMultiHopQA, StrategyQA, FEVER, and HOVER — against Search-R1, IRCoT, AutoRefine, RAG-Star, and Veri-R1 baselines (with model-scale caveats for Veri-R1's 3B models and ReaLM-Retrieve's 32B). StrategyQA tests implicit multi-hop reasoning where the model must infer what type of evidence to seek; FEVER is the canonical claim verification benchmark directly comparable with Veri-R1's evaluation; HOVER tests multi-hop verification — together providing comprehensive coverage of both the discovery and verification aspects of our contribution. A mandatory pilot validates that discovery/verification intent is distinguishable — well-motivated given ReaLM-Retrieve's 31% verification rate.\n\n**Compute budget with verified arithmetic:** The entire pipeline fits within ~202 H100-hours (hard cap ≤210). Phase 2 (the dominant cost) runs 2 GRPO training configurations × 500 steps each on 8×H100. Per-step time is ~75 sec (range: 65-90 sec; calibrated from veRL benchmarks showing 60-70 sec/step for Qwen2.5-7B on 8×A800, ms-swift issue #3302, with Search-R1 retrieval overhead partially offset by H100 throughput). Per run: 500 steps × 75 sec = 10.4 wall-hours × 8 GPUs = ~83 H100-hours. Two runs = ~166 H100-hours. Plus overhead (pilot 5h, SFT 5h, NLI 8h, eval 18h) = ~202 H100-hours. 500 steps matches Search-R1's own protocol and exceeds AutoRefine's 300-step convergence; GRPO risks reward collapse beyond 500 steps, making this a well-calibrated choice. Contingency: reduce to 400 steps if per-step exceeds 90 sec, giving ~196h total.\n\nPrimary target: AAAI 2027 (abstract ~July 21, full paper ~July 28, 2026), providing a comfortable ~10-week window. The May 25, 2026 ARR cycle — the last eligible for EMNLP 2026 (commitment deadline August 2, 2026; note: there is no June ARR cycle, as ARR switched to 10-week review cycles) — is a stretch goal only. ICLR 2027 (~October 2026) serves as a fallback for extended experiments.\n\n## 核心问题\nCurrent reasoning-augmented retrieval systems optimize various aspects of the retrieval-reasoning interface — when to retrieve (ReaLM-Retrieve), how much to retrieve (DeepControl), how to refine retrieved evidence (AutoRefine), and how to coordinate retrieval with reasoning structure (DualRAG, HARIS) — yet all treat query construction as a single undifferentiated process. ReaLM-Retrieve's learned QueryGen module generates context-adaptive query representations via cross-attention to reasoning step embeddings, adapting queries implicitly through learned representations. Critically, ReaLM-Retrieve's own behavioral analysis (Section 6.9) empirically identifies 'verification retrievals' as a distinct pattern in 31% of cases — reducing backtracking by 18% — and its failure analysis finds that 'over-retrieval during exploration' accounts for 31% of failures (Section 7.3). These observations directly evidence that retrieval intent varies structurally within reasoning chains and that intent-mismatched retrieval actively degrades performance. Yet ReaLM-Retrieve does not operationalize this insight: its QueryGen maps all retrieval calls through the same continuous embedding space, conflating exploratory and confirmatory information needs. No system explicitly classifies the purpose of each retrieval call within a reasoning chain and applies structurally different query construction strategies accordingly. Even Veri-R1 (Oct 2025), which specifically trains models for claim verification via GRPO with iterative retrieval across up to 3 search turns, applies the same uniform query construction strategy across all retrieval calls — further evidencing that the discovery/verification distinction is not operationalized even in verification-specialized systems. Within a reasoning chain, a retrieval call seeking new evidence to explore an unknown sub-question (discovery) requires broad, recall-oriented queries, while one checking whether a specific intermediate claim holds (verification) requires targeted, claim-contrastive queries that seek both supporting and refuting evidence. Implicit query adaptation via learned representations cannot capture this structural distinction because a verification query should actively seek disconfirming evidence, which is anti-correlated with the topical relevance signal that learned query generators optimize for. This intent-blind retrieval means verification-stage retrievals return topically relevant but evidentially uninformative documents, degrading reasoning faithfulness. The problem is compounded by evidence that retrieval can actively hurt reasoning when poorly matched to reasoning needs — Shakya et al. (2026) show that traces including retrieval perform slightly worse than CoT without retrieval, but that adaptive retrieval (choosing when to retrieve) improves overall performance, suggesting that retrieval quality and intent matching — not just retrieval timing or volume — is a critical bottleneck.\n\n## 机遇 / Why Now\nReaLM-Retrieve empirically observed that retrieval intent varies within reasoning chains — identifying verification retrievals (31% of cases) as a distinct beneficial pattern and over-retrieval during exploration (31% of failures) as a primary failure mode — but did not operationalize this insight. We make it actionable via explicit intent classification and structurally differentiated query construction.\n\nReasoning models now produce long CoT traces with explicit intermediate claims that create a structurally exploitable retrieval signal: 'retrieve evidence to check claim X' is functionally distinct from 'retrieve evidence to answer question Y,' and these two modes demand different query construction strategies — yet no existing system makes this distinction explicit and operationalizes it at query construction time.\n\nRecent work has advanced adjacent aspects of this space without addressing this core gap. On implicit query adaptation: ReaLM-Retrieve (Apr 2026) uses a learned single-layer transformer decoder QueryGen that generates context-adaptive 768-dim query embeddings via cross-attention to reasoning step representations, achieving 71.2% F1 on MuSiQue (+11.8% over standard RAG) with only 1.8 retrieval calls — but its learned representations adapt queries implicitly without distinguishing retrieval purpose, and its own error analysis reveals this as a limitation. On retrieval-verification in tree search: RAG-Star (NAACL 2025) uses retrieval-augmented verification within MCTS, scoring answer-document consistency to guide tree search backpropagation, but applies uniform retrieval for every sub-query and operates in tree-structured (not sequential) reasoning. On iterative query reformulation: CoRAG (NeurIPS 2025) dynamically reformulates queries based on evolving reasoning state via rejection sampling, achieving SOTA on KILT, but applies the same reformulation strategy regardless of whether the model needs exploration or confirmation. On retrieval control: DeepControl (ICLR 2026 Workshop) measures marginal information utility to control retrieval continuation and granularity (+9.4% over Search-R1 on Qwen2.5-7B), but controls how much to retrieve, not how to construct purpose-differentiated queries. On evidence refinement: AutoRefine (NeurIPS 2025) introduces a &lt;refine> step between search calls with retrieval-specific rewards via GRPO, dramatically improving multi-hop QA, but refines evidence post-retrieval without differentiating query construction. On reasoning-aware retrieval embeddings: AgentIR (Mar 2026) encodes reasoning traces into retrieval embeddings for intent-aware retrieval but treats all retrieval calls uniformly without intent classification. On RL-trained claim verification: Veri-R1 (Oct 2025) trains Qwen2.5-3B-Instruct via GRPO for iterative claim verification on FEVEROUS/FEVER/HOVER/SciFACT, improving joint accuracy by 30% and doubling evidence scores — but applies the same query strategy across all search turns despite being verification-specialized. On domain-specific structured verification: Reason and Verify (Mar 2026) integrates explicit sub-claim grounding with an eight-category verification taxonomy for biomedical RAG, achieving 89.1% on BioASQ-Y/N — but applies uniform retrieval without intent classification and is not RL-trained.\n\nThe precise gap: existing systems adapt query representations implicitly through learned embeddings (ReaLM-Retrieve, CoRAG, AgentIR), reformulate queries iteratively (CoRAG), control retrieval volume (DeepControl), refine evidence post-retrieval (AutoRefine, SURE-RAG, Entropic Claim Resolution), verify answers in tree search (RAG-Star), train verification-specific RL policies with uniform retrieval (Veri-R1), or structure verification taxonomies in domain-specific settings (Reason and Verify) — but none explicitly classifies retrieval intent as discovery vs. verification and applies structurally different query construction strategies for each, particularly claim-contrastive retrieval that actively seeks disconfirming evidence for verification-intent calls. ReaLM-Retrieve's own analysis shows this distinction exists and matters; Veri-R1's uniform approach to verification-specific retrieval confirms it remains unaddressed even in the most targeted systems. We operationalize it.\n\n## 方法思路\nWe build a dual-intent retrieval module on top of the open-source Search-R1 framework that introduces explicit intent-differentiated query formulation into reasoning-augmented retrieval. The approach has four phases designed to fit within ~200 H100-hours and ~11 days.\n\n**Model choice: Qwen2.5-7B.** We use Qwen2.5-7B as the primary model, not Qwen3-8B. This is a deliberate choice motivated by a known, unresolved training speed regression: Qwen3-8B exhibits 10-20× slower generation during veRL GRPO training compared to Qwen2.5-7B (veRL GitHub issues #1580, #3816), with each step taking ~1 hour instead of minutes. The root cause appears to be Qwen3's thinking mode generating excessively long outputs (~7000 tokens vs ~1000 tokens), and this affects even non-thinking configurations due to architectural differences in how vLLM handles Qwen3. Qwen2.5-7B is the backbone Search-R1 was originally validated on, with proven GRPO training efficiency and 24% average relative improvement on QA benchmarks. We use Qwen2.5-7B-Base for the primary experiments, consistent with Search-R1's original evaluation.\n\n**Phase 0 — Pilot Feasibility (Day 1, ~5 H100-hours):** Generate reasoning traces on 500 MuSiQue training examples using standard Search-R1 with Qwen2.5-7B. Apply heuristic rules to classify each &lt;search> call: if the preceding reasoning contains an explicit claim or assertion ('X is Y', 'therefore', 'this means') followed by retrieval, label it VERIFY; if it contains a question decomposition or information-seeking pattern ('I need to find', 'what is', sub-question form), label it DISCOVER. Manually inspect 100 labeled examples and compute distribution statistics. Go/no-go: proceed only if both categories appear with ≥15% frequency and heuristic accuracy ≥75%. This threshold is well-motivated: ReaLM-Retrieve's analysis found verification retrievals comprise 31% of cases, suggesting ≥15% is easily achievable.\n\n**Phase 1 — Implementation (Days 2-4):** Extend the Search-R1 token format: replace the single &lt;search>query&lt;/search> with two intent-tagged variants: &lt;discover>query&lt;/discover> and &lt;verify>claim ||| query&lt;/verify>. The verify format includes both the claim and an optional model-generated query, enabling RL to learn sophisticated query formulations beyond templates. This dual-format design serves a deeper purpose beyond mere classification: by structuring verification retrieval as explicit claim ||| query pairs, we give the RL optimization a rich action space in which to develop intent-specific query patterns. The model must learn not just what to search for, but how to construct queries that surface evidence specifically relevant to confirming or refuting its tentative claim — a fundamentally different skill from exploratory information-seeking. Implement differentiated query processing in the search environment:\n\n(a) Discovery mode — pass the query to BM25, return top-3 results (same as baseline). BM25 is appropriate for discovery queries because they tend to be keyword-rich and information-seeking, matching BM25's lexical matching strength.\n\n(b) Verification mode — uses a hybrid retrieval pipeline to address the limitation that BM25 performs poorly on semantically-oriented contrastive queries. Extract the claim and the model-generated query (or, during SFT cold-start, generate a contrastive query pair via templates: 'evidence supporting [claim]' / 'evidence contradicting [claim]'). Retrieve top-3 via BM25 (lexical match on claim content) and top-3 via dense retrieval (E5-base-v2, which Search-R1 already supports as a retrieval backend) using the contrastive queries. Pool the 6 results, re-rank by evidential discriminativeness using an NLI cross-encoder (cross-encoder/nli-deberta-v3-base, 184M params) to score entailment and contradiction, returning the top-3 documents ranked by |entailment − contradiction| score (most discriminative first). The hybrid BM25+dense approach is motivated by evidence that hybrid retrieval improves recall by 15-30% over either method alone, and dense retrieval is critical for semantic matching on contrastive queries where keywords like 'supporting'/'contradicting' are uninformative for BM25. Note: Search-R1 provides pre-built E5-base-v2 FAISS indexes for its Wikipedia corpus, eliminating index-building overhead.\n\n**Template limitation and RL-learned query refinement (co-equal contribution):** We acknowledge that template-based contrastive queries ('evidence supporting/contradicting [claim]') are simplistic — real verification needs are more nuanced (causal claims require different evidence patterns than factual or temporal claims). The &lt;verify>claim ||| query&lt;/verify> format is specifically designed to allow the model to learn more sophisticated query formulations through RL. During SFT cold-start, templates provide the initial format. During GRPO training, the model is free to generate arbitrary text in the query field, learning from outcome rewards which query formulations yield the most useful evidence. This follows RAFTS's (ACL 2024) insight that LLM-generated contrastive arguments outperform fixed templates, but integrates the learning directly into the RL loop rather than requiring a separate generation step. We position the RL-discovered verification query strategies as a co-equal contribution alongside the intent taxonomy itself: if the model learns to use negation patterns, hedge framing, contrastive structures, or claim-type-specific formulations that humans would not manually design, this constitutes a compelling finding about how structured action spaces enable emergent strategy discovery through reward optimization.\n\nSFT cold start: relabel heuristically-classified Search-R1 traces with intent tokens and fine-tune Qwen2.5-7B-Base for ~100 steps to learn the new format.\n\nNote on Search-R1 RL algorithm: Search-R1 supports both PPO and GRPO via separate training scripts (train_ppo.sh and train_grpo.sh) built on the veRL framework. We use the GRPO configuration for training efficiency and stability, consistent with recent work (AutoRefine, DeepControl, Veri-R1) that also builds on Search-R1 with GRPO.\n\n**NLI model separation to avoid reward circularity:** A critical design decision is using different NLI models for verification reranking vs. faithfulness reward computation, to prevent a circular optimization where the model learns to game its own reward signal. During verification-intent retrieval, documents are reranked by |entailment − contradiction| via cross-encoder/nli-deberta-v3-base (DeBERTa architecture, 184M params). The faithfulness reward component uses a different model family: ynie/roberta-large-snli_mnli_fever_anli_R1_R2_R3-nli (RoBERTa-large architecture, 355M params, trained on SNLI+MNLI+FEVER+ANLI). Using different architectures (DeBERTa disentangled attention vs. RoBERTa standard attention) and different training data distributions ensures the models have different decision boundaries, preventing the policy from learning to select documents that trivially satisfy the reward without genuinely improving evidential quality. The circularity concern is real: if the same model ranks documents and scores faithfulness, the optimization target reduces to 'retrieve documents that this specific model scores highly on' rather than 'retrieve genuinely informative evidence.' Different models with different inductive biases prevent this collapse.\n\n**NLI reranking cost analysis:** DeBERTa-v3-base (184M params) processes ~800-1200 sentence pairs/sec on a single H100. During GRPO training with global batch size B=256, average R=2.5 retrieval calls per sample, and estimated verification fraction V=0.4, total NLI pairs per step = B × R × V × 6 = 256 × 2.5 × 0.4 × 6 ≈ 1,536 pairs. At 1,000 pairs/sec, this adds ~1.5 seconds per step. The RoBERTa-large reward model (355M params) processes ~400-600 pairs/sec; with ~3 claims per trace × 256 samples = ~768 pairs, adding ~1.5 seconds per step. Combined NLI overhead is ~3 seconds per step. Compared to the LLM forward/backward pass on 8×H100 with Qwen2.5-7B, total NLI overhead is ~5-10% — manageable without dedicated hardware. To minimize memory contention, we run NLI inference on CPU (adding ~10-15 sec per step, still <25% overhead) or allocate a fraction of one GPU's memory. We budget an additional ~8 H100-hours for NLI overhead across all training runs.\n\n**Phase 2 — RL Training (Days 5-8, ~166 H100-hours on 8×H100):** Train with GRPO using a composite reward: R = α·EM(answer) + (1−α)·faithfulness, where faithfulness is the fraction of intermediate claims in the reasoning trace that are supported (entailment > 0.5) by at least one retrieved document, scored by the RoBERTa-large NLI model (distinct from the DeBERTa reranker). Set α = 0.7 (tunable). Run two configurations: (1) full dual-intent with hybrid contrastive verification retrieval (primary), (2) standard Search-R1 baseline with GRPO (ablation: no intent). The BM25-only ablation (dual-intent tokens with standard retrieval for both modes) is deferred to save compute; it can be added as a reduced-scale 250-step run (~28 H100-hours) if the primary runs finish under budget.\n\n**Per-run compute arithmetic:** Each run uses 500 training steps on 8×H100, matching Search-R1's own training protocol (the original Search-R1 paper trains for exactly 500 steps with checkpoints every 100 steps). Per-step time estimate: the veRL GRPO benchmark shows 60-70 sec/step for Qwen2.5-7B full-parameter GRPO on 8×A800 with NuminaMath-TIR (ms-swift issue #3302). Search-R1's multi-turn retrieval adds overhead from search engine calls during rollout generation (~2-4 search calls per trajectory with BM25 latency <50ms each) and longer context sequences (max_prompt_length=4096 vs ~2048 for math). H100's ~1.3× throughput advantage over A800 partially offsets this overhead. We estimate ~75 sec/step (range: 65-90 sec), yielding: 500 steps × 75 sec = 37,500 sec ≈ 10.4 wall-hours per run. Per-run GPU-hours: 10.4 wall-hours × 8 GPUs = **~83 H100-hours**. Two runs total: **~166 H100-hours**. **Contingency:** if per-step time exceeds 90 sec, reduce to 400 steps per run — still above AutoRefine's 300-step convergence point — giving 400 × 90 sec ≈ 10.0 wall-hours × 8 GPUs ≈ 80 H100-hours per run, ~160 H100-hours total for Phase 2.\n\n**Convergence justification for 500 steps:** 500 steps matches Search-R1's own training protocol, where the original paper uses exactly 500 steps for both Qwen2.5-3B and Qwen2.5-7B with GRPO. AutoRefine (NeurIPS 2025), built on the same Search-R1/veRL/GRPO stack, trains for only 300 steps and achieves its reported gains (HotpotQA: 0.405 F1, MuSiQue: 0.157 F1). GRPO-LEAD converges in ~200 steps with top-performing checkpoints selected via validation. Empirical GRPO training dynamics show gradient norms stabilize by step 40, with most accuracy gains in the first 200-300 steps. Additionally, GRPO is known to risk reward collapse when trained for too many steps, further motivating 500 steps as a well-calibrated choice rather than a compromise.\n\n**Phase 3 — Evaluation & Analysis (Days 9-11, ~18 H100-hours):** Evaluate on MuSiQue, HotpotQA, 2WikiMultiHopQA, StrategyQA, FEVER, and HOVER (6 benchmarks). MuSiQue, HotpotQA, and 2WikiMultiHopQA are standard multi-hop QA benchmarks requiring compositional reasoning with explicit decomposition. StrategyQA requires implicit multi-hop reasoning where the decomposition strategy is not given — the model must infer what type of evidence to seek, making it an ideal showcase for intent-differentiated retrieval since the discovery/verification transition is not signaled by the question structure but must emerge from the model's reasoning process. FEVER is the canonical fact verification benchmark (185K claims, supported/refuted/NEI) — essential for a method whose core contribution involves verification-intent retrieval, and directly comparable with Veri-R1's evaluation on the same benchmark. HOVER is a multi-hop claim verification benchmark requiring evidence from 2-4 Wikipedia articles, testing both discovery (finding relevant articles across hops) and verification (confirming multi-hop claims against aggregated evidence). Metrics: answer F1/EM, faithfulness (claim-support rate), retrieval precision/recall on supporting evidence. Baselines: Search-R1 (reproduced with GRPO), IRCoT, and ReaLM-Retrieve (reported numbers with model-scale caveats, as their best results use DeepSeek-R1-Distill-Qwen-32B). Additional comparisons: AutoRefine (reported numbers, NeurIPS 2025), RAG-Star (reported numbers from Llama-3.1-8B-Instruct), Veri-R1 (reported numbers on HOVER and FEVER, with model-scale caveats since Veri-R1 uses Qwen2.5-3B-Instruct and Llama3.2-3B-Instruct while we use 7B; we will report per-parameter efficiency where feasible to enable fair comparison). Analysis: (a) intent distribution — what fraction of retrievals are classified as discovery vs. verification across all six benchmarks, and how this compares to ReaLM-Retrieve's observed 31% verification rate, (b) per-intent retrieval quality — does verification mode retrieve more evidentially discriminative documents (measured by |entailment − contradiction| spread), (c) comparison with implicit adaptation — does explicit intent classification outperform ReaLM-Retrieve's learned QueryGen on verification-heavy reasoning chains, (d) NLI model separation analysis — compare performance with same-model vs. different-model reranking/reward to quantify circularity effects, (e) **query evolution analysis (key expected finding)** — do RL-learned verification queries diverge from initial templates, and what patterns emerge (claim-type-specific formulations, negation patterns, contrastive framing, hedge structures, etc.)? This analysis is positioned as a key finding, not merely a diagnostic: if RL discovers intent-specific query patterns that humans wouldn't write — e.g., systematically different query structures for causal vs. factual vs. temporal claims — that constitutes a compelling result in its own right, demonstrating that the structured &lt;verify>claim ||| query&lt;/verify> format enables emergent strategy discovery through reward optimization, (f) error analysis — when does intent misclassification degrade performance, (g) case studies showing how contrastive verification queries surface disconfirming evidence that standard and implicitly-adapted queries miss, (h) StrategyQA-specific analysis — does intent-differentiated retrieval show disproportionate gains on implicit decomposition tasks where the model must infer retrieval intent without explicit question structure?\n\n**Design justifications:** The binary discovery/verification taxonomy is the minimal distinction that captures the most variance in retrieval intent within reasoning chains. This choice is now directly grounded in ReaLM-Retrieve's empirical findings: their three behavioral patterns (early resolution 42%, verification 31%, failed retrieval 12%) naturally collapse into our binary taxonomy — early resolution and failed retrieval are both discovery-intent (information-seeking), while verification retrievals map directly to our verification-intent. The choice is further motivated by Shakya et al.'s (2026) finding that retrieval during exploration can hurt reasoning while adaptive retrieval helps — suggesting that the exploration/confirmation axis is the primary dimension along which retrieval intent varies. Finer categories (clarification, disambiguation, quantitative validation) are subsumed: clarification and disambiguation are discovery subtypes, quantitative/causal verification are verification subtypes. Binary classification is also more robust with limited RL training budget and avoids the need for multi-class intent supervision. The framework is extensible to additional intent types via new tokens.\n\nThe key distinction from related approaches: ReaLM-Retrieve's QueryGen learns a continuous mapping from reasoning states to query embeddings, and its own analysis reveals that verification retrievals are a distinct beneficial pattern — but it does not operationalize this insight by applying different retrieval pipelines. Veri-R1 trains verification-specific RL policies with a multi-component reward (label + evidence IoU + format + validity) but uses the same uniform query strategy across all search turns — even its emergent 'fine-grained subclaim-level decomposition' is not structurally supported by differentiated retrieval. Our approach makes intent classification explicit and applies structurally different retrieval pipelines — critically, verification queries use hybrid BM25+dense retrieval with NLI-based contrastive reranking to actively seek disconfirming evidence, which is anti-correlated with topical relevance maximization. RAG-Star uses retrieval for verification within MCTS but verifies candidate answers at tree nodes with uniform relevance-based retrieval, not intermediate claims with contrastive queries. AutoRefine's &lt;refine> step distills evidence post-retrieval but doesn't change how queries are constructed. CoRAG reformulates queries iteratively but applies the same reformulation strategy regardless of intent. DeepControl controls retrieval volume and timing but not query construction strategy. RAFTS (ACL 2024) demonstrates that contrastive argument synthesis improves fact verification, but operates as a standalone pipeline — we integrate contrastive retrieval directly into the RL-trained reasoning loop. Reason and Verify (Mar 2026) structures verification with an eight-category taxonomy for biomedical RAG but applies uniform retrieval — we address a different dimension (retrieval pipeline differentiation) in a domain-general RL-trained setting.\n\nThe contribution is dual: (1) explicit intent classification with structurally differentiated retrieval pipelines, and (2) RL-discovered verification query strategies that emerge from the &lt;verify>claim ||| query&lt;/verify> format — the latter being a co-equal contribution that may yield insights about how structured action spaces enable emergent retrieval strategies.\n\nFallback: if claim extraction quality is poor in the reasoning trace (e.g., no clear propositional claim before a retrieval call), default to discovery mode — this is safe because discovery mode is equivalent to the baseline.\n\n## 研究现状\nThe reasoning-augmented retrieval landscape in 2025-2026 has advanced along five axes — implicit query adaptation, retrieval timing/volume control, retrieval-reasoning coordination, post-retrieval evidence quality, and reasoning-stage verification — creating a rich but precisely gapped design space.\n\n**Implicit query adaptation.** ReaLM-Retrieve achieves 71.2% F1 on MuSiQue with 1.8 retrieval calls by combining step-level uncertainty-based retrieval timing with a learned QueryGen module (single-layer transformer decoder, 512 hidden dim, 8 attention heads) that cross-attends to current reasoning step embeddings, producing context-adaptive 768-dim query representations for ColBERTv2 dense retrieval. The +11.8% F1 improvement on MuSiQue (+10.1% average across three benchmarks) demonstrates that adaptive query generation substantially outperforms static queries. Crucially, ReaLM-Retrieve's own behavioral analysis (Section 6.9) identifies three dominant retrieval patterns: 'early resolution' (42% of cases, yielding 23% shorter reasoning chains), 'verification retrievals' (31%, reducing backtracking by 18%), and 'failed retrievals' (12%, extending chains by 8%). Its failure analysis (Section 7.3) finds that over-retrieval during exploratory reasoning phases accounts for 31% of failures by 'disrupting productive chains by prematurely committing to hypotheses.' These observations directly evidence that retrieval intent varies structurally and that intent-mismatched retrieval degrades performance — yet QueryGen's cross-attention mechanism learns a single continuous mapping from reasoning states to query embeddings, conflating exploratory and confirmatory needs into the same representation space. CoRAG (NeurIPS 2025) dynamically reformulates queries based on evolving reasoning state via rejection sampling training, establishing SOTA on KILT with >10-point EM improvements on multi-hop QA, but applies uniform reformulation strategy regardless of retrieval purpose. AgentIR (Mar 2026) encodes reasoning traces into retrieval embeddings for intent-aware retrieval but treats all retrieval calls uniformly without intent classification.\n\n**Retrieval timing and volume control.** DeepControl (ICLR 2026 Workshop) formalizes information utility as U(e) = ρ·Novelty + (1−ρ)·Effectiveness, using an annealed control-forcing curriculum to train retrieval continuation and granularity control, achieving +9.4% on Qwen2.5-7B over RL baselines across seven benchmarks. R1-Searcher++ trains models to decide whether to use internal knowledge or external search. Shakya et al. (Feb 2026) find that 'traces including retrieval actually perform worse compared to CoT' while the model's decision to adaptively avoid retrieval improves overall performance — suggesting that retrieval quality and intent matching matters more than retrieval quantity.\n\n**Retrieval-reasoning coordination.** Search-R1 trains LLMs via RL (supporting both PPO and GRPO) to issue search queries within reasoning, achieving +41%/+20% on QA benchmarks for 7B/3B models, with Qwen2.5-7B as the primary validated backbone. AutoRefine (NeurIPS 2025) introduces a &lt;refine> step between search calls that distills evidence from ~600 to ~100-200 tokens, trained with GRPO using dual rewards (answer correctness + retrieval quality), achieving major gains on multi-hop QA (HotpotQA: 0.405 vs 0.297 Search-R1; MuSiQue: 0.157 vs 0.066). DualRAG (ACL 2025) coordinates reasoning-augmented querying with progressive knowledge aggregation. HARIS (arXiv 2506.07528, Jun 2025) uses a hierarchical two-agent architecture (reasoning + search) with GRPO training on Qwen3-4B, evaluating on EX-FEVER (80.12% F1 on 2-hop) and HOVER (61.00% accuracy on 4-hop) for claim verification — but with uniform search strategy across all retrieval calls. IRCoT interleaves retrieval at fixed intervals.\n\n**Post-retrieval evidence quality.** SURE-RAG (May 2026) scores claim-evidence pairs for sufficiency. Entropic Claim Resolution (Mar 2026) selects discriminative evidence via entropy minimization. RAFTS (ACL 2024) synthesizes contrastive supporting/refuting arguments from retrieved passages via LLM-based generation with a two-stage BM25+dense retrieval pipeline for standalone fact verification — demonstrating that contrastive evidence framing improves verification accuracy, but operating as a standalone fact-checking system rather than integrated in reasoning RL loops. Reason and Verify (arXiv 2603.10143, Mar 2026) integrates explicit sub-claim grounding with an eight-category verification taxonomy for biomedical RAG, achieving 89.1% on BioASQ-Y/N with Llama-3-8B-Instruct. Though domain-specific (biomedical) and not RL-trained, it demonstrates concurrent interest in structured verification within RAG, using BGE cross-encoder reranking and rationale grounding — but applies uniform retrieval without intent classification. REPAIR (Jan 2026) uses reasoning plans for mid-course correction during reranking. All operate downstream of query construction.\n\n**Reasoning-stage verification.** RAG-Star (NAACL 2025) uses MCTS for deliberative reasoning with retrieval-augmented verification: for each MCTS node, retrieval checks answer-document consistency (scoring 1=unverifiable, 2=conflict, 3=aligned) with query- and answer-aware reward modeling. However, RAG-Star verifies candidate answers at MCTS tree nodes using uniform retrieval, not intermediate claims within sequential reasoning chains, and does not use contrastive queries to actively seek disconfirming evidence. Veri-R1 (arXiv 2510.01932, Oct 2025) is the most directly comparable RL-based verification system: it trains Qwen2.5-3B-Instruct and Llama3.2-3B-Instruct via GRPO for iterative claim verification with up to 3 search turns, using a 4-component reward (label correctness +2, evidence IoU, format compliance, validity weight). Evaluated on FEVEROUS, EX-FEVER, FEVER, SciFACT, and HOVER, Veri-R1 improves joint accuracy by up to 30% and doubles evidence scores vs baselines. Open-source and built on Search-R1/veRL. Critically, despite being designed specifically for claim verification, Veri-R1 does NOT differentiate retrieval intent — all search queries use the same uniform strategy, whether the model is exploring for initial evidence or confirming a tentative conclusion. Its case analysis shows Online RL naturally develops 'fine-grained subclaim-level decomposition,' but this emergent behavior is not structurally supported by differentiated retrieval pipelines. FIRE (NAACL Findings 2025) uses confidence-based iterative retrieval for fact-checking with 7.6× cost reduction but applies the same query strategy per iteration. 'Don't Let It Hallucinate' (NeurIPS 2025) transforms queries into logical premises for pre-generation verification, operating before reasoning chains begin. VERITAS rewards faithful reasoning but doesn't modify retrieval.\n\n**The gap.** All existing systems either (a) adapt query representations implicitly through learned embeddings without distinguishing retrieval purpose — even when their own analysis shows the distinction exists and matters (ReaLM-Retrieve, CoRAG, AgentIR), (b) control retrieval timing/volume without differentiating query construction (DeepControl, R1-Searcher++), (c) refine evidence post-retrieval without improving the upstream query (AutoRefine, SURE-RAG, ECR, RAFTS), (d) verify answers in tree search or pre-generation without contrastive query construction within sequential reasoning (RAG-Star, FIRE, Don't Let It Hallucinate), (e) train verification-specific RL policies but still use uniform query construction across all search turns (Veri-R1), or (f) structure verification taxonomies in domain-specific settings without intent-differentiated retrieval (Reason and Verify). No system explicitly classifies retrieval intent as discovery vs. verification within sequential reasoning chains and applies structurally different query construction strategies for each — particularly claim-contrastive retrieval that actively seeks disconfirming evidence during verification.\n\n## 目标 Venue\n- AAAI 2027 (abstract ~July 21, 2026; full paper ~July 28, 2026 — primary target with comfortable ~10-week window for experiments, analysis, and paper writing)\n- ARR May 25, 2026 → EMNLP 2026 (commitment deadline August 2, 2026) — stretch goal only, requires aggressive 10-day execution with pre-existing Search-R1/veRL familiarity; note: this is the last eligible ARR cycle for EMNLP 2026, as the next ARR cycle (August 3, 2026) falls after the EMNLP commitment deadline; no June ARR cycle exists due to ARR's switch to 10-week review cycles\n- ICLR 2027 (expected ~October 2026 — fallback allowing additional model scales, extended ablations, or supplementary benchmarks)\n\n## 关键参考\n- Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning (arXiv 2503.09516, Mar 2025) — base framework; supports PPO and GRPO via veRL, &lt;search> token format; validated on Qwen2.5-7B with 24% average relative improvement; trains for 500 GRPO steps with checkpoints every 100 steps; provides pre-built BM25 and E5 FAISS indexes for Wikipedia corpus\n- When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models [ReaLM-Retrieve] (arXiv 2604.26649, Apr 2026) — learned QueryGen module (single-layer transformer decoder, cross-attention to reasoning step embeddings, 768-dim adaptive query representations); +11.8% F1 on MuSiQue (71.2%), +10.1% average across 3 benchmarks; Section 6.9 identifies verification retrievals (31% of cases) as a distinct pattern reducing backtracking by 18%; Section 7.3 identifies over-retrieval during exploration as 31% of failures; implicitly adaptive but not intent-differentiated despite observing the need\n- RAG-Star: Enhancing Deliberative Reasoning with Retrieval Augmented Verification and Refinement (NAACL 2025, Jiang et al.) — MCTS-based reasoning with retrieval-augmented verification at tree nodes (answer-document consistency scoring), query- and answer-aware reward modeling; verifies candidate answers in tree search with uniform retrieval, not intermediate claims with contrastive queries\n- Chain-of-Retrieval Augmented Generation [CoRAG] (NeurIPS 2025, arXiv 2501.14342) — dynamic query reformulation via rejection sampling training, SOTA on KILT, >10-point EM on multi-hop QA; reformulates queries based on evolving state but without intent differentiation\n- Scaling Search-Augmented LLM Reasoning via Adaptive Information Control [DeepControl] (arXiv 2602.01672, ICLR 2026 Workshop SPOT) — information utility = ρ·Novelty + (1−ρ)·Effectiveness, retrieval continuation and granularity control with annealed curriculum; +9.4% on Qwen2.5-7B over RL baselines; controls retrieval volume, not query construction strategy\n- Search and Refine During Think [AutoRefine] (NeurIPS 2025, arXiv 2505.11277) — &lt;refine> step distilling evidence between search calls, GRPO with dual rewards (answer + retrieval quality); trains for 300 steps on Search-R1/veRL/GRPO stack and achieves convergence; HotpotQA: 0.405 vs 0.297 Search-R1, MuSiQue: 0.157 vs 0.066; refines evidence post-retrieval without intent-differentiated query construction\n- Retrieval Augmented Fact Verification by Synthesizing Contrastive Arguments [RAFTS] (ACL 2024) — LLM-based contrastive supporting/refuting argument synthesis with two-stage BM25+dense retrieval pipeline; demonstrates contrastive evidence framing improves verification; standalone system, not integrated in reasoning RL\n- Veri-R1: Toward Precise and Faithful Claim Verification via Online Reinforcement Learning (arXiv 2510.01932, Oct 2025) — GRPO-trained iterative claim verification with Qwen2.5-3B-Instruct and Llama3.2-3B-Instruct on FEVEROUS/EX-FEVER/FEVER/SciFACT/HOVER; 4-component reward (label correctness + evidence IoU + format compliance + validity weight); improves joint accuracy by 30%, doubles evidence scores; does NOT differentiate retrieval intent despite being verification-focused; open-source on Search-R1/veRL; most directly comparable RL-based verification baseline\n- HARIS: Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification (arXiv 2506.07528, Jun 2025) — hierarchical two-agent architecture (reasoning + search) with GRPO training on Qwen3-4B; evaluates on EX-FEVER (80.12% F1 on 2-hop) and HOVER (61.00% accuracy on 4-hop); uniform search strategy without intent differentiation\n- Reason and Verify: A Framework for Faithful Retrieval-Augmented Generation (arXiv 2603.10143, Mar 2026) — biomedical RAG with eight-category verification taxonomy, explicit sub-claim grounding, BGE cross-encoder reranking; 89.1% on BioASQ-Y/N with Llama-3-8B-Instruct; domain-specific but demonstrates concurrent interest in structured verification within RAG; uniform retrieval without intent classification\n- R1-Searcher++: Incentivizing Dynamic Knowledge Acquisition of LLMs via RL (arXiv 2505.17005, May 2025) — internal vs. external knowledge distinction, not intent within external retrieval\n- REPAIR: Adaptive Retrieval for Reasoning-Intensive Retrieval (arXiv 2601.04618, Jan 2026) — reasoning plans for reranking; operates post-retrieval, not at query construction\n- FIRE: Fact-checking with Iterative Retrieval and Verification (NAACL Findings 2025) — confidence-based iterative retrieval; 7.6× cost reduction but same query strategy per iteration\n- Don't Let It Hallucinate: Premise Verification via Retrieval-Augmented Logical Reasoning (NeurIPS 2025) — pre-generation premise verification, not during reasoning chain\n- Adaptive Retrieval helps Reasoning in LLMs — but mostly if it's not used (arXiv 2602.07213, Shakya et al., Feb 2026) — traces with retrieval perform slightly worse than CoT; adaptive retrieval (choosing when to retrieve) improves overall performance; directly motivates that retrieval quality and intent matching matters more than retrieval volume\n- DualRAG: A Dual-Process Approach to Integrate Reasoning and Retrieval for Multi-Hop QA (ACL 2025) — dual reasoning-retrieval processes but uniform retrieval strategy\n- AgentIR: Reasoning-Aware Retrieval for Deep Research Agents (arXiv 2603.04384, Mar 2026) — encodes reasoning traces in embeddings but uniform intent across all retrieval calls\n- SURE-RAG: Sufficiency and Uncertainty-Aware Evidence Verification for Selective RAG (arXiv, May 2026) — post-retrieval claim-evidence scoring\n- Entropic Claim Resolution: Uncertainty-Driven Evidence Selection for RAG (arXiv, Mar 2026) — post-retrieval evidence selection via entropy minimization\n- Beyond Correctness: Rewarding Faithful Reasoning in RAG [VERITAS] (arXiv, Oct 2025) — faithfulness reward for generators, not retrieval modification\n- Interleaving Retrieval with Chain-of-Thought Reasoning [IRCoT] (ACL 2023) — fixed-interval retrieval baseline\n- Adaptive-RAG: Learning to Adapt Retrieval-Augmented LLMs through Question Complexity (NAACL 2024)\n- veRL GitHub issues #1580, #3816 — Qwen3-8B GRPO training 10-20× slower than Qwen2.5-7B due to generation speed regression; motivates our model choice\n- ms-swift GitHub issue #3302 — GRPO training speed benchmark: 60-70 sec/step for Qwen2.5-7B full-parameter GRPO on 8×A800 with veRL; calibrates our per-step compute estimate\n\n## 资源估算\n### auto_research\n- **claude_api_cost**: $200-400 (est. 2000-4000 turns for autonomous experiment design and paper drafting)\n- **estimated_gpu_cost**: ~$630 (210h × ~$3.00/hr)\n- **gpu_hours**: ≤210 H100-hours (hard budget cap). Agent must track cumulative GPU-hours (wall-time × GPUs, not wall-time alone) and prioritize: primary dual-intent run (~83h) and baseline run (~83h) are mandatory; BM25-only ablation at 250 steps (~42h) is included only if cumulative spend remains ≤168h after the two primary runs. If approaching cap, agent reduces ablation steps or skips lowest-priority analysis.\n- **gpu_utilization**: ~85-95% utilization; agent pipelines experiments continuously\n- **risk_note**: Agent should implement early stopping on reward plateau detection (GRPO risks reward collapse beyond ~500 steps); if pilot feasibility fails (intent categories not distinguishable), agent should pivot to testing contrastive verification queries without intent classification\n- **speed_bottleneck**: Primary bottleneck is sequential GRPO runs on 8 GPUs (~10.4 wall-hours each at 75 sec/step); BM25 index pre-built, E5 FAISS index downloadable from Search-R1; NLI inference adds ~5-10% per-step overhead\n- **team**: 0 (initial setup and final review only)\n- **timeline**: 6-9 days with 8×H100 available\n\n### human_in_loop\n- **claude_api_cost**: $100-200 (est. 1000-2000 turns for code generation and experiment analysis)\n- **estimated_gpu_cost**: ~$606-630 (202-210h × ~$3.00/hr)\n- **gpu_hours**: ~202-210 H100-hours. Base plan (~202h) plus agent-proposed extensions with human approval: reduced-scale BM25-only ablation (250 steps on 8×H100 = 250 × 75 sec ≈ 5.2 wall-hours × 8 GPUs ≈ ~42h), reward weighting variants, or heuristic threshold tuning. Extensions prioritized by expected information value within remaining budget.\n- **gpu_utilization**: ~55-70% utilization; agent queues experiments while human reviews\n- **risk_note**: Composite faithfulness+correctness reward may need human judgment on α weighting if RL training shows reward hacking on the faithfulness component; if per-step time exceeds 90 sec, human approves step-count reduction to 400\n- **team**: 1 researcher, ~20-30min/day reviewing proposals and results\n- **timeline**: 2-3 weeks\n\n### manual\n- **estimated_gpu_cost**: ~$606 (202h × ~$3.00/hr H100 spot pricing)\n- **gpu_hours**: ~202 H100-hours total (range: 183-215 depending on per-step training speed). Breakdown with explicit wall-time × GPU arithmetic: Phase 0 pilot: ~5h (generation only, 1-2 GPUs); Phase 1 SFT cold start: ~5h (100 SFT steps); Phase 2 GRPO training: 2 runs × 500 steps × ~75 sec/step = 2 × (10.4 wall-hours × 8 GPUs) = ~166h; NLI overhead during training: ~8h; Phase 3 evaluation on 6 benchmarks: ~18h. Dense index building: ~0h (Search-R1 provides pre-built E5-base-v2 FAISS indexes). Per-step calibration: veRL GRPO benchmarks show 60-70 sec/step for Qwen2.5-7B on 8×A800 (ms-swift issue #3302); we estimate ~75 sec/step for Search-R1 on 8×H100, accounting for retrieval overhead partially offset by H100 throughput advantage. Contingency: if per-step exceeds 90 sec, reduce to 400 steps/run (above AutoRefine's 300-step convergence), giving 2 × (10.0 wall-hours × 8 GPUs) = ~160h for Phase 2, ~196h total.\n- **gpu_utilization**: ~40-50% effective utilization; GPUs idle during implementation, debugging, and analysis phases\n- **team**: 1 researcher with RL and retrieval experience\n- **timeline**: 10-12 days (10 days with 8×H100 and familiarity with Search-R1/veRL codebase; 12 days otherwise)\n\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T01:48:41.487Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T01:48:41.487Z",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891"
}
```

---

## Round 1

39 recorded events

### User

_source line 3 · 2026-05-16T01:48:41.522Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Dual-Intent Retrieval: Intent-Differentiated Query Formulation for Reasoning-Augmented RAG

**状态**: 待审阅  
**级别**: top-tier  
**创建时间**: 2026-05-15T16:06:37.791174+00:00

## 描述
We propose Dual-Intent Retrieval, a method that explicitly classifies each retrieval call within a reasoning model's chain-of-thought as either discovery-intent (seeking new evidence to advance reasoning) or verification-intent (seeking evidence to confirm or refute an intermediate claim), then applies structurally different query construction and retrieval strategies for each. Discovery queries use standard BM25 retrieval, matching its strength at keyword-rich information-seeking queries. Verification queries use a hybrid BM25+dense retrieval pipeline with NLI-based contrastive reranking: given an intermediate claim, the model generates contrastive queries (seeded by templates during SFT, refined through RL), retrieves via both BM25 and E5-base-v2 dense retrieval, and re-ranks by evidential discriminativeness using DeBERTa-v3-base NLI scoring, surfacing documents that most clearly support or refute the claim.

This operationalizes an insight that ReaLM-Retrieve empirically observed but did not act upon: its behavioral analysis (Section 6.9) identifies 'verification retrievals' as a distinct pattern in 31% of cases that reduces backtracking by 18%, while its failure analysis finds that over-retrieval during exploration accounts for 31% of failures. Despite observing that retrieval intent varies structurally, ReaLM-Retrieve's QueryGen maps all retrieval calls through the same learned embedding space without differentiating strategy. Even Veri-R1 (Oct 2025), which trains verification-specific RL policies via GRPO with a multi-component reward (label + evidence IoU + format + validity), uses uniform query construction across all search turns. We make this insight actionable.

The approach addresses a broader gap: ReaLM-Retrieve adapts queries implicitly without distinguishing purpose; CoRAG (NeurIPS 2025) reformulates queries iteratively but uniformly; DeepControl (ICLR 2026 Workshop) controls retrieval volume, not query strategy; AutoRefine (NeurIPS 2025) refines evidence post-retrieval; RAG-Star (NAACL 2025) verifies answers in MCTS with uniform retrieval; Veri-R1 (Oct 2025) trains verification-specific RL but uses uniform query construction; RAFTS (ACL 2024) demonstrates contrastive argument synthesis for fact-checking but operates standalone; Reason and Verify (Mar 2026) structures verification taxonomies for biomedical RAG but applies uniform retrieval. None classify intent and differentiate query construction within RL-trained sequential reasoning.

The contribution is dual: (1) explicit intent classification with structurally differentiated retrieval pipelines, and (2) RL-discovered verification query strategies that emerge from the &lt;verify>claim ||| query&lt;/verify> format. The latter is a co-equal contribution: the structured format creates a rich action space for GRPO to discover sophisticated verification strategies (e.g., negation patterns, contrastive framing, claim-type-specific formulations) that humans might not manually design — and the query evolution analysis in Phase 3 is positioned as a key expected finding.

Built atop Search-R1's open-source RL framework using Qwen2.5-7B (chosen over Qwen3-8B to avoid a known 10-20× GRPO training speed regression in veRL), we introduce intent tokens (&lt;discover>/&lt;verify>) and train via GRPO with a composite reward combining answer correctness and faithfulness. A critical design choice: we use different NLI model families for verification reranking (DeBERTa-v3-base, 184M params) vs. faithfulness reward (RoBERTa-large-NLI, 355M params) to prevent circular optimization where the policy learns to game its own reward signal. Intent labels are bootstrapped via heuristic rules for SFT cold start, then refined through RL. The &lt;verify>claim ||| query&lt;/verify> format allows RL to learn sophisticated query formulations beyond initial templates, following RAFTS's insight that LLM-generated contrastive formulations outperform fixed templates. We evaluate on six benchmarks — MuSiQue, HotpotQA, 2WikiMultiHopQA, StrategyQA, FEVER, and HOVER — against Search-R1, IRCoT, AutoRefine, RAG-Star, and Veri-R1 baselines (with model-scale caveats for Veri-R1's 3B models and ReaLM-Retrieve's 32B). StrategyQA tests implicit multi-hop reasoning where the model must infer what type of evidence to seek; FEVER is the canonical claim verification benchmark directly comparable with Veri-R1's evaluation; HOVER tests multi-hop verification — together providing comprehensive coverage of both the discovery and verification aspects of our contribution. A mandatory pilot validates that discovery/verification intent is distinguishable — well-motivated given ReaLM-Retrieve's 31% verification rate.

**Compute budget with verified arithmetic:** The entire pipeline fits within ~202 H100-hours (hard cap ≤210). Phase 2 (the dominant cost) runs 2 GRPO training configurations × 500 steps each on 8×H100. Per-step time is ~75 sec (range: 65-90 sec; calibrated from veRL benchmarks showing 60-70 sec/step for Qwen2.5-7B on 8×A800, ms-swift issue #3302, with Search-R1 retrieval overhead partially offset by H100 throughput). Per run: 500 steps × 75 sec = 10.4 wall-hours × 8 GPUs = ~83 H100-hours. Two runs = ~166 H100-hours. Plus overhead (pilot 5h, SFT 5h, NLI 8h, eval 18h) = ~202 H100-hours. 500 steps matches Search-R1's own protocol and exceeds AutoRefine's 300-step convergence; GRPO risks reward collapse beyond 500 steps, making this a well-calibrated choice. Contingency: reduce to 400 steps if per-step exceeds 90 sec, giving ~196h total.

Primary target: AAAI 2027 (abstract ~July 21, full paper ~July 28, 2026), providing a comfortable ~10-week window. The May 25, 2026 ARR cycle — the last eligible for EMNLP 2026 (commitment deadline August 2, 2026; note: there is no June ARR cycle, as ARR switched to 10-week review cycles) — is a stretch goal only. ICLR 2027 (~October 2026) serves as a fallback for extended experiments.

## 核心问题
Current reasoning-augmented retrieval systems optimize various aspects of the retrieval-reasoning interface — when to retrieve (ReaLM-Retrieve), how much to retrieve (DeepControl), how to refine retrieved evidence (AutoRefine), and how to coordinate retrieval with reasoning structure (DualRAG, HARIS) — yet all treat query construction as a single undifferentiated process. ReaLM-Retrieve's learned QueryGen module generates context-adaptive query representations via cross-attention to reasoning step embeddings, adapting queries implicitly through learned representations. Critically, ReaLM-Retrieve's own behavioral analysis (Section 6.9) empirically identifies 'verification retrievals' as a distinct pattern in 31% of cases — reducing backtracking by 18% — and its failure analysis finds that 'over-retrieval during exploration' accounts for 31% of failures (Section 7.3). These observations directly evidence that retrieval intent varies structurally within reasoning chains and that intent-mismatched retrieval actively degrades performance. Yet ReaLM-Retrieve does not operationalize this insight: its QueryGen maps all retrieval calls through the same continuous embedding space, conflating exploratory and confirmatory information needs. No system explicitly classifies the purpose of each retrieval call within a reasoning chain and applies structurally different query construction strategies accordingly. Even Veri-R1 (Oct 2025), which specifically trains models for claim verification via GRPO with iterative retrieval across up to 3 search turns, applies the same uniform query construction strategy across all retrieval calls — further evidencing that the discovery/verification distinction is not operationalized even in verification-specialized systems. Within a reasoning chain, a retrieval call seeking new evidence to explore an unknown sub-question (discovery) requires broad, recall-oriented queries, while one checking whether a specific intermediate claim holds (verification) requires targeted, claim-contrastive queries that seek both supporting and refuting evidence. Implicit query adaptation via learned representations cannot capture this structural distinction because a verification query should actively seek disconfirming evidence, which is anti-correlated with the topical relevance signal that learned query generators optimize for. This intent-blind retrieval means verification-stage retrievals return topically relevant but evidentially uninformative documents, degrading reasoning faithfulness. The problem is compounded by evidence that retrieval can actively hurt reasoning when poorly matched to reasoning needs — Shakya et al. (2026) show that traces including retrieval perform slightly worse than CoT without retrieval, but that adaptive retrieval (choosing when to retrieve) improves overall performance, suggesting that retrieval quality and intent matching — not just retrieval timing or volume — is a critical bottleneck.

## 机遇 / Why Now
ReaLM-Retrieve empirically observed that retrieval intent varies within reasoning chains — identifying verification retrievals (31% of cases) as a distinct beneficial pattern and over-retrieval during exploration (31% of failures) as a primary failure mode — but did not operationalize this insight. We make it actionable via explicit intent classification and structurally differentiated query construction.

Reasoning models now produce long CoT traces with explicit intermediate claims that create a structurally exploitable retrieval signal: 'retrieve evidence to check claim X' is functionally distinct from 'retrieve evidence to answer question Y,' and these two modes demand different query construction strategies — yet no existing system makes this distinction explicit and operationalizes it at query construction time.

Recent work has advanced adjacent aspects of this space without addressing this core gap. On implicit query adaptation: ReaLM-Retrieve (Apr 2026) uses a learned single-layer transformer decoder QueryGen that generates context-adaptive 768-dim query embeddings via cross-attention to reasoning step representations, achieving 71.2% F1 on MuSiQue (+11.8% over standard RAG) with only 1.8 retrieval calls — but its learned representations adapt queries implicitly without distinguishing retrieval purpose, and its own error analysis reveals this as a limitation. On retrieval-verification in tree search: RAG-Star (NAACL 2025) uses retrieval-augmented verification within MCTS, scoring answer-document consistency to guide tree search backpropagation, but applies uniform retrieval for every sub-query and operates in tree-structured (not sequential) reasoning. On iterative query reformulation: CoRAG (NeurIPS 2025) dynamically reformulates queries based on evolving reasoning state via rejection sampling, achieving SOTA on KILT, but applies the same reformulation strategy regardless of whether the model needs exploration or confirmation. On retrieval control: DeepControl (ICLR 2026 Workshop) measures marginal information utility to control retrieval continuation and granularity (+9.4% over Search-R1 on Qwen2.5-7B), but controls how much to retrieve, not how to construct purpose-differentiated queries. On evidence refinement: AutoRefine (NeurIPS 2025) introduces a &lt;refine> step between search calls with retrieval-specific rewards via GRPO, dramatically improving multi-hop QA, but refines evidence post-retrieval without differentiating query construction. On reasoning-aware retrieval embeddings: AgentIR (Mar 2026) encodes reasoning traces into retrieval embeddings for intent-aware retrieval but treats all retrieval calls uniformly without intent classification. On RL-trained claim verification: Veri-R1 (Oct 2025) trains Qwen2.5-3B-Instruct via GRPO for iterative claim verification on FEVEROUS/FEVER/HOVER/SciFACT, improving joint accuracy by 30% and doubling evidence scores — but applies the same query strategy across all search turns despite being verification-specialized. On domain-specific structured verification: Reason and Verify (Mar 2026) integrates explicit sub-claim grounding with an eight-category verification taxonomy for biomedical RAG, achieving 89.1% on BioASQ-Y/N — but applies uniform retrieval without intent classification and is not RL-trained.

The precise gap: existing systems adapt query representations implicitly through learned embeddings (ReaLM-Retrieve, CoRAG, AgentIR), reformulate queries iteratively (CoRAG), control retrieval volume (DeepControl), refine evidence post-retrieval (AutoRefine, SURE-RAG, Entropic Claim Resolution), verify answers in tree search (RAG-Star), train verification-specific RL policies with uniform retrieval (Veri-R1), or structure verification taxonomies in domain-specific settings (Reason and Verify) — but none explicitly classifies retrieval intent as discovery vs. verification and applies structurally different query construction strategies for each, particularly claim-contrastive retrieval that actively seeks disconfirming evidence for verification-intent calls. ReaLM-Retrieve's own analysis shows this distinction exists and matters; Veri-R1's uniform approach to verification-specific retrieval confirms it remains unaddressed even in the most targeted systems. We operationalize it.

## 方法思路
We build a dual-intent retrieval module on top of the open-source Search-R1 framework that introduces explicit intent-differentiated query formulation into reasoning-augmented retrieval. The approach has four phases designed to fit within ~200 H100-hours and ~11 days.

**Model choice: Qwen2.5-7B.** We use Qwen2.5-7B as the primary model, not Qwen3-8B. This is a deliberate choice motivated by a known, unresolved training speed regression: Qwen3-8B exhibits 10-20× slower generation during veRL GRPO training compared to Qwen2.5-7B (veRL GitHub issues #1580, #3816), with each step taking ~1 hour instead of minutes. The root cause appears to be Qwen3's thinking mode generating excessively long outputs (~7000 tokens vs ~1000 tokens), and this affects even non-thinking configurations due to architectural differences in how vLLM handles Qwen3. Qwen2.5-7B is the backbone Search-R1 was originally validated on, with proven GRPO training efficiency and 24% average relative improvement on QA benchmarks. We use Qwen2.5-7B-Base for the primary experiments, consistent with Search-R1's original evaluation.

**Phase 0 — Pilot Feasibility (Day 1, ~5 H100-hours):** Generate reasoning traces on 500 MuSiQue training examples using standard Search-R1 with Qwen2.5-7B. Apply heuristic rules to classify each &lt;search> call: if the preceding reasoning contains an explicit claim or assertion ('X is Y', 'therefore', 'this means') followed by retrieval, label it VERIFY; if it contains a question decomposition or information-seeking pattern ('I need to find', 'what is', sub-question form), label it DISCOVER. Manually inspect 100 labeled examples and compute distribution statistics. Go/no-go: proceed only if both categories appear with ≥15% frequency and heuristic accuracy ≥75%. This threshold is well-motivated: ReaLM-Retrieve's analysis found verification retrievals comprise 31% of cases, suggesting ≥15% is easily achievable.

**Phase 1 — Implementation (Days 2-4):** Extend the Search-R1 token format: replace the single &lt;search>query&lt;/search> with two intent-tagged variants: &lt;discover>query&lt;/discover> and &lt;verify>claim ||| query&lt;/verify>. The verify format includes both the claim and an optional model-generated query, enabling RL to learn sophisticated query formulations beyond templates. This dual-format design serves a deeper purpose beyond mere classification: by structuring verification retrieval as explicit claim ||| query pairs, we give the RL optimization a rich action space in which to develop intent-specific query patterns. The model must learn not just what to search for, but how to construct queries that surface evidence specifically relevant to confirming or refuting its tentative claim — a fundamentally different skill from exploratory information-seeking. Implement differentiated query processing in the search environment:

(a) Discovery mode — pass the query to BM25, return top-3 results (same as baseline). BM25 is appropriate for discovery queries because they tend to be keyword-rich and information-seeking, matching BM25's lexical matching strength.

(b) Verification mode — uses a hybrid retrieval pipeline to address the limitation that BM25 performs poorly on semantically-oriented contrastive queries. Extract the claim and the model-generated query (or, during SFT cold-start, generate a contrastive query pair via templates: 'evidence supporting [claim]' / 'evidence contradicting [claim]'). Retrieve top-3 via BM25 (lexical match on claim content) and top-3 via dense retrieval (E5-base-v2, which Search-R1 already supports as a retrieval backend) using the contrastive queries. Pool the 6 results, re-rank by evidential discriminativeness using an NLI cross-encoder (cross-encoder/nli-deberta-v3-base, 184M params) to score entailment and contradiction, returning the top-3 documents ranked by |entailment − contradiction| score (most discriminative first). The hybrid BM25+dense approach is motivated by evidence that hybrid retrieval improves recall by 15-30% over either method alone, and dense retrieval is critical for semantic matching on contrastive queries where keywords like 'supporting'/'contradicting' are uninformative for BM25. Note: Search-R1 provides pre-built E5-base-v2 FAISS indexes for its Wikipedia corpus, eliminating index-building overhead.

**Template limitation and RL-learned query refinement (co-equal contribution):** We acknowledge that template-based contrastive queries ('evidence supporting/contradicting [claim]') are simplistic — real verification needs are more nuanced (causal claims require different evidence patterns than factual or temporal claims). The &lt;verify>claim ||| query&lt;/verify> format is specifically designed to allow the model to learn more sophisticated query formulations through RL. During SFT cold-start, templates provide the initial format. During GRPO training, the model is free to generate arbitrary text in the query field, learning from outcome rewards which query formulations yield the most useful evidence. This follows RAFTS's (ACL 2024) insight that LLM-generated contrastive arguments outperform fixed templates, but integrates the learning directly into the RL loop rather than requiring a separate generation step. We position the RL-discovered verification query strategies as a co-equal contribution alongside the intent taxonomy itself: if the model learns to use negation patterns, hedge framing, contrastive structures, or claim-type-specific formulations that humans would not manually design, this constitutes a compelling finding about how structured action spaces enable emergent strategy discovery through reward optimization.

SFT cold start: relabel heuristically-classified Search-R1 traces with intent tokens and fine-tune Qwen2.5-7B-Base for ~100 steps to learn the new format.

Note on Search-R1 RL algorithm: Search-R1 supports both PPO and GRPO via separate training scripts (train_ppo.sh and train_grpo.sh) built on the veRL framework. We use the GRPO configuration for training efficiency and stability, consistent with recent work (AutoRefine, DeepControl, Veri-R1) that also builds on Search-R1 with GRPO.

**NLI model separation to avoid reward circularity:** A critical design decision is using different NLI models for verification reranking vs. faithfulness reward computation, to prevent a circular optimization where the model learns to game its own reward signal. During verification-intent retrieval, documents are reranked by |entailment − contradiction| via cross-encoder/nli-deberta-v3-base (DeBERTa architecture, 184M params). The faithfulness reward component uses a different model family: ynie/roberta-large-snli_mnli_fever_anli_R1_R2_R3-nli (RoBERTa-large architecture, 355M params, trained on SNLI+MNLI+FEVER+ANLI). Using different architectures (DeBERTa disentangled attention vs. RoBERTa standard attention) and different training data distributions ensures the models have different decision boundaries, preventing the policy from learning to select documents that trivially satisfy the reward without genuinely improving evidential quality. The circularity concern is real: if the same model ranks documents and scores faithfulness, the optimization target reduces to 'retrieve documents that this specific model scores highly on' rather than 'retrieve genuinely informative evidence.' Different models with different inductive biases prevent this collapse.

**NLI reranking cost analysis:** DeBERTa-v3-base (184M params) processes ~800-1200 sentence pairs/sec on a single H100. During GRPO training with global batch size B=256, average R=2.5 retrieval calls per sample, and estimated verification fraction V=0.4, total NLI pairs per step = B × R × V × 6 = 256 × 2.5 × 0.4 × 6 ≈ 1,536 pairs. At 1,000 pairs/sec, this adds ~1.5 seconds per step. The RoBERTa-large reward model (355M params) processes ~400-600 pairs/sec; with ~3 claims per trace × 256 samples = ~768 pairs, adding ~1.5 seconds per step. Combined NLI overhead is ~3 seconds per step. Compared to the LLM forward/backward pass on 8×H100 with Qwen2.5-7B, total NLI overhead is ~5-10% — manageable without dedicated hardware. To minimize memory contention, we run NLI inference on CPU (adding ~10-15 sec per step, still <25% overhead) or allocate a fraction of one GPU's memory. We budget an additional ~8 H100-hours for NLI overhead across all training runs.

**Phase 2 — RL Training (Days 5-8, ~166 H100-hours on 8×H100):** Train with GRPO using a composite reward: R = α·EM(answer) + (1−α)·faithfulness, where faithfulness is the fraction of intermediate claims in the reasoning trace that are supported (entailment > 0.5) by at least one retrieved document, scored by the RoBERTa-large NLI model (distinct from the DeBERTa reranker). Set α = 0.7 (tunable). Run two configurations: (1) full dual-intent with hybrid contrastive verification retrieval (primary), (2) standard Search-R1 baseline with GRPO (ablation: no intent). The BM25-only ablation (dual-intent tokens with standard retrieval for both modes) is deferred to save compute; it can be added as a reduced-scale 250-step run (~28 H100-hours) if the primary runs finish under budget.

**Per-run compute arithmetic:** Each run uses 500 training steps on 8×H100, matching Search-R1's own training protocol (the original Search-R1 paper trains for exactly 500 steps with checkpoints every 100 steps). Per-step time estimate: the veRL GRPO benchmark shows 60-70 sec/step for Qwen2.5-7B full-parameter GRPO on 8×A800 with NuminaMath-TIR (ms-swift issue #3302). Search-R1's multi-turn retrieval adds overhead from search engine calls during rollout generation (~2-4 search calls per trajectory with BM25 latency <50ms each) and longer context sequences (max_prompt_length=4096 vs ~2048 for math). H100's ~1.3× throughput advantage over A800 partially offsets this overhead. We estimate ~75 sec/step (range: 65-90 sec), yielding: 500 steps × 75 sec = 37,500 sec ≈ 10.4 wall-hours per run. Per-run GPU-hours: 10.4 wall-hours × 8 GPUs = **~83 H100-hours**. Two runs total: **~166 H100-hours**. **Contingency:** if per-step time exceeds 90 sec, reduce to 400 steps per run — still above AutoRefine's 300-step convergence point — giving 400 × 90 sec ≈ 10.0 wall-hours × 8 GPUs ≈ 80 H100-hours per run, ~160 H100-hours total for Phase 2.

**Convergence justification for 500 steps:** 500 steps matches Search-R1's own training protocol, where the original paper uses exactly 500 steps for both Qwen2.5-3B and Qwen2.5-7B with GRPO. AutoRefine (NeurIPS 2025), built on the same Search-R1/veRL/GRPO stack, trains for only 300 steps and achieves its reported gains (HotpotQA: 0.405 F1, MuSiQue: 0.157 F1). GRPO-LEAD converges in ~200 steps with top-performing checkpoints selected via validation. Empirical GRPO training dynamics show gradient norms stabilize by step 40, with most accuracy gains in the first 200-300 steps. Additionally, GRPO is known to risk reward collapse when trained for too many steps, further motivating 500 steps as a well-calibrated choice rather than a compromise.

**Phase 3 — Evaluation & Analysis (Days 9-11, ~18 H100-hours):** Evaluate on MuSiQue, HotpotQA, 2WikiMultiHopQA, StrategyQA, FEVER, and HOVER (6 benchmarks). MuSiQue, HotpotQA, and 2WikiMultiHopQA are standard multi-hop QA benchmarks requiring compositional reasoning with explicit decomposition. StrategyQA requires implicit multi-hop reasoning where the decomposition strategy is not given — the model must infer what type of evidence to seek, making it an ideal showcase for intent-differentiated retrieval since the discovery/verification transition is not signaled by the question structure but must emerge from the model's reasoning process. FEVER is the canonical fact verification benchmark (185K claims, supported/refuted/NEI) — essential for a method whose core contribution involves verification-intent retrieval, and directly comparable with Veri-R1's evaluation on the same benchmark. HOVER is a multi-hop claim verification benchmark requiring evidence from 2-4 Wikipedia articles, testing both discovery (finding relevant articles across hops) and verification (confirming multi-hop claims against aggregated evidence). Metrics: answer F1/EM, faithfulness (claim-support rate), retrieval precision/recall on supporting evidence. Baselines: Search-R1 (reproduced with GRPO), IRCoT, and ReaLM-Retrieve (reported numbers with model-scale caveats, as their best results use DeepSeek-R1-Distill-Qwen-32B). Additional comparisons: AutoRefine (reported numbers, NeurIPS 2025), RAG-Star (reported numbers from Llama-3.1-8B-Instruct), Veri-R1 (reported numbers on HOVER and FEVER, with model-scale caveats since Veri-R1 uses Qwen2.5-3B-Instruct and Llama3.2-3B-Instruct while we use 7B; we will report per-parameter efficiency where feasible to enable fair comparison). Analysis: (a) intent distribution — what fraction of retrievals are classified as discovery vs. verification across all six benchmarks, and how this compares to ReaLM-Retrieve's observed 31% verification rate, (b) per-intent retrieval quality — does verification mode retrieve more evidentially discriminative documents (measured by |entailment − contradiction| spread), (c) comparison with implicit adaptation — does explicit intent classification outperform ReaLM-Retrieve's learned QueryGen on verification-heavy reasoning chains, (d) NLI model separation analysis — compare performance with same-model vs. different-model reranking/reward to quantify circularity effects, (e) **query evolution analysis (key expected finding)** — do RL-learned verification queries diverge from initial templates, and what patterns emerge (claim-type-specific formulations, negation patterns, contrastive framing, hedge structures, etc.)? This analysis is positioned as a key finding, not merely a diagnostic: if RL discovers intent-specific query patterns that humans wouldn't write — e.g., systematically different query structures for causal vs. factual vs. temporal claims — that constitutes a compelling result in its own right, demonstrating that the structured &lt;verify>claim ||| query&lt;/verify> format enables emergent strategy discovery through reward optimization, (f) error analysis — when does intent misclassification degrade performance, (g) case studies showing how contrastive verification queries surface disconfirming evidence that standard and implicitly-adapted queries miss, (h) StrategyQA-specific analysis — does intent-differentiated retrieval show disproportionate gains on implicit decomposition tasks where the model must infer retrieval intent without explicit question structure?

**Design justifications:** The binary discovery/verification taxonomy is the minimal distinction that captures the most variance in retrieval intent within reasoning chains. This choice is now directly grounded in ReaLM-Retrieve's empirical findings: their three behavioral patterns (early resolution 42%, verification 31%, failed retrieval 12%) naturally collapse into our binary taxonomy — early resolution and failed retrieval are both discovery-intent (information-seeking), while verification retrievals map directly to our verification-intent. The choice is further motivated by Shakya et al.'s (2026) finding that retrieval during exploration can hurt reasoning while adaptive retrieval helps — suggesting that the exploration/confirmation axis is the primary dimension along which retrieval intent varies. Finer categories (clarification, disambiguation, quantitative validation) are subsumed: clarification and disambiguation are discovery subtypes, quantitative/causal verification are verification subtypes. Binary classification is also more robust with limited RL training budget and avoids the need for multi-class intent supervision. The framework is extensible to additional intent types via new tokens.

The key distinction from related approaches: ReaLM-Retrieve's QueryGen learns a continuous mapping from reasoning states to query embeddings, and its own analysis reveals that verification retrievals are a distinct beneficial pattern — but it does not operationalize this insight by applying different retrieval pipelines. Veri-R1 trains verification-specific RL policies with a multi-component reward (label + evidence IoU + format + validity) but uses the same uniform query strategy across all search turns — even its emergent 'fine-grained subclaim-level decomposition' is not structurally supported by differentiated retrieval. Our approach makes intent classification explicit and applies structurally different retrieval pipelines — critically, verification queries use hybrid BM25+dense retrieval with NLI-based contrastive reranking to actively seek disconfirming evidence, which is anti-correlated with topical relevance maximization. RAG-Star uses retrieval for verification within MCTS but verifies candidate answers at tree nodes with uniform relevance-based retrieval, not intermediate claims with contrastive queries. AutoRefine's &lt;refine> step distills evidence post-retrieval but doesn't change how queries are constructed. CoRAG reformulates queries iteratively but applies the same reformulation strategy regardless of intent. DeepControl controls retrieval volume and timing but not query construction strategy. RAFTS (ACL 2024) demonstrates that contrastive argument synthesis improves fact verification, but operates as a standalone pipeline — we integrate contrastive retrieval directly into the RL-trained reasoning loop. Reason and Verify (Mar 2026) structures verification with an eight-category taxonomy for biomedical RAG but applies uniform retrieval — we address a different dimension (retrieval pipeline differentiation) in a domain-general RL-trained setting.

The contribution is dual: (1) explicit intent classification with structurally differentiated retrieval pipelines, and (2) RL-discovered verification query strategies that emerge from the &lt;verify>claim ||| query&lt;/verify> format — the latter being a co-equal contribution that may yield insights about how structured action spaces enable emergent retrieval strategies.

Fallback: if claim extraction quality is poor in the reasoning trace (e.g., no clear propositional claim before a retrieval call), default to discovery mode — this is safe because discovery mode is equivalent to the baseline.

## 研究现状
The reasoning-augmented retrieval landscape in 2025-2026 has advanced along five axes — implicit query adaptation, retrieval timing/volume control, retrieval-reasoning coordination, post-retrieval evidence quality, and reasoning-stage verification — creating a rich but precisely gapped design space.

**Implicit query adaptation.** ReaLM-Retrieve achieves 71.2% F1 on MuSiQue with 1.8 retrieval calls by combining step-level uncertainty-based retrieval timing with a learned QueryGen module (single-layer transformer decoder, 512 hidden dim, 8 attention heads) that cross-attends to current reasoning step embeddings, producing context-adaptive 768-dim query representations for ColBERTv2 dense retrieval. The +11.8% F1 improvement on MuSiQue (+10.1% average across three benchmarks) demonstrates that adaptive query generation substantially outperforms static queries. Crucially, ReaLM-Retrieve's own behavioral analysis (Section 6.9) identifies three dominant retrieval patterns: 'early resolution' (42% of cases, yielding 23% shorter reasoning chains), 'verification retrievals' (31%, reducing backtracking by 18%), and 'failed retrievals' (12%, extending chains by 8%). Its failure analysis (Section 7.3) finds that over-retrieval during exploratory reasoning phases accounts for 31% of failures by 'disrupting productive chains by prematurely committing to hypotheses.' These observations directly evidence that retrieval intent varies structurally and that intent-mismatched retrieval degrades performance — yet QueryGen's cross-attention mechanism learns a single continuous mapping from reasoning states to query embeddings, conflating exploratory and confirmatory needs into the same representation space. CoRAG (NeurIPS 2025) dynamically reformulates queries based on evolving reasoning state via rejection sampling training, establishing SOTA on KILT with >10-point EM improvements on multi-hop QA, but applies uniform reformulation strategy regardless of retrieval purpose. AgentIR (Mar 2026) encodes reasoning traces into retrieval embeddings for intent-aware retrieval but treats all retrieval calls uniformly without intent classification.

**Retrieval timing and volume control.** DeepControl (ICLR 2026 Workshop) formalizes information utility as U(e) = ρ·Novelty + (1−ρ)·Effectiveness, using an annealed control-forcing curriculum to train retrieval continuation and granularity control, achieving +9.4% on Qwen2.5-7B over RL baselines across seven benchmarks. R1-Searcher++ trains models to decide whether to use internal knowledge or external search. Shakya et al. (Feb 2026) find that 'traces including retrieval actually perform worse compared to CoT' while the model's decision to adaptively avoid retrieval improves overall performance — suggesting that retrieval quality and intent matching matters more than retrieval quantity.

**Retrieval-reasoning coordination.** Search-R1 trains LLMs via RL (supporting both PPO and GRPO) to issue search queries within reasoning, achieving +41%/+20% on QA benchmarks for 7B/3B models, with Qwen2.5-7B as the primary validated backbone. AutoRefine (NeurIPS 2025) introduces a &lt;refine> step between search calls that distills evidence from ~600 to ~100-200 tokens, trained with GRPO using dual rewards (answer correctness + retrieval quality), achieving major gains on multi-hop QA (HotpotQA: 0.405 vs 0.297 Search-R1; MuSiQue: 0.157 vs 0.066). DualRAG (ACL 2025) coordinates reasoning-augmented querying with progressive knowledge aggregation. HARIS (arXiv 2506.07528, Jun 2025) uses a hierarchical two-agent architecture (reasoning + search) with GRPO training on Qwen3-4B, evaluating on EX-FEVER (80.12% F1 on 2-hop) and HOVER (61.00% accuracy on 4-hop) for claim verification — but with uniform search strategy across all retrieval calls. IRCoT interleaves retrieval at fixed intervals.

**Post-retrieval evidence quality.** SURE-RAG (May 2026) scores claim-evidence pairs for sufficiency. Entropic Claim Resolution (Mar 2026) selects discriminative evidence via entropy minimization. RAFTS (ACL 2024) synthesizes contrastive supporting/refuting arguments from retrieved passages via LLM-based generation with a two-stage BM25+dense retrieval pipeline for standalone fact verification — demonstrating that contrastive evidence framing improves verification accuracy, but operating as a standalone fact-checking system rather than integrated in reasoning RL loops. Reason and Verify (arXiv 2603.10143, Mar 2026) integrates explicit sub-claim grounding with an eight-category verification taxonomy for biomedical RAG, achieving 89.1% on BioASQ-Y/N with Llama-3-8B-Instruct. Though domain-specific (biomedical) and not RL-trained, it demonstrates concurrent interest in structured verification within RAG, using BGE cross-encoder reranking and rationale grounding — but applies uniform retrieval without intent classification. REPAIR (Jan 2026) uses reasoning plans for mid-course correction during reranking. All operate downstream of query construction.

**Reasoning-stage verification.** RAG-Star (NAACL 2025) uses MCTS for deliberative reasoning with retrieval-augmented verification: for each MCTS node, retrieval checks answer-document consistency (scoring 1=unverifiable, 2=conflict, 3=aligned) with query- and answer-aware reward modeling. However, RAG-Star verifies candidate answers at MCTS tree nodes using uniform retrieval, not intermediate claims within sequential reasoning chains, and does not use contrastive queries to actively seek disconfirming evidence. Veri-R1 (arXiv 2510.01932, Oct 2025) is the most directly comparable RL-based verification system: it trains Qwen2.5-3B-Instruct and Llama3.2-3B-Instruct via GRPO for iterative claim verification with up to 3 search turns, using a 4-component reward (label correctness +2, evidence IoU, format compliance, validity weight). Evaluated on FEVEROUS, EX-FEVER, FEVER, SciFACT, and HOVER, Veri-R1 improves joint accuracy by up to 30% and doubles evidence scores vs baselines. Open-source and built on Search-R1/veRL. Critically, despite being designed specifically for claim verification, Veri-R1 does NOT differentiate retrieval intent — all search queries use the same uniform strategy, whether the model is exploring for initial evidence or confirming a tentative conclusion. Its case analysis shows Online RL naturally develops 'fine-grained subclaim-level decomposition,' but this emergent behavior is not structurally supported by differentiated retrieval pipelines. FIRE (NAACL Findings 2025) uses confidence-based iterative retrieval for fact-checking with 7.6× cost reduction but applies the same query strategy per iteration. 'Don't Let It Hallucinate' (NeurIPS 2025) transforms queries into logical premises for pre-generation verification, operating before reasoning chains begin. VERITAS rewards faithful reasoning but doesn't modify retrieval.

**The gap.** All existing systems either (a) adapt query representations implicitly through learned embeddings without distinguishing retrieval purpose — even when their own analysis shows the distinction exists and matters (ReaLM-Retrieve, CoRAG, AgentIR), (b) control retrieval timing/volume without differentiating query construction (DeepControl, R1-Searcher++), (c) refine evidence post-retrieval without improving the upstream query (AutoRefine, SURE-RAG, ECR, RAFTS), (d) verify answers in tree search or pre-generation without contrastive query construction within sequential reasoning (RAG-Star, FIRE, Don't Let It Hallucinate), (e) train verification-specific RL policies but still use uniform query construction across all search turns (Veri-R1), or (f) structure verification taxonomies in domain-specific settings without intent-differentiated retrieval (Reason and Verify). No system explicitly classifies retrieval intent as discovery vs. verification within sequential reasoning chains and applies structurally different query construction strategies for each — particularly claim-contrastive retrieval that actively seeks disconfirming evidence during verification.

## 目标 Venue
- AAAI 2027 (abstract ~July 21, 2026; full paper ~July 28, 2026 — primary target with comfortable ~10-week window for experiments, analysis, and paper writing)
- ARR May 25, 2026 → EMNLP 2026 (commitment deadline August 2, 2026) — stretch goal only, requires aggressive 10-day execution with pre-existing Search-R1/veRL familiarity; note: this is the last eligible ARR cycle for EMNLP 2026, as the next ARR cycle (August 3, 2026) falls after the EMNLP commitment deadline; no June ARR cycle exists due to ARR's switch to 10-week review cycles
- ICLR 2027 (expected ~October 2026 — fallback allowing additional model scales, extended ablations, or supplementary benchmarks)

## 关键参考
- Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning (arXiv 2503.09516, Mar 2025) — base framework; supports PPO and GRPO via veRL, &lt;search> token format; validated on Qwen2.5-7B with 24% average relative improvement; trains for 500 GRPO steps with checkpoints every 100 steps; provides pre-built BM25 and E5 FAISS indexes for Wikipedia corpus
- When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models [ReaLM-Retrieve] (arXiv 2604.26649, Apr 2026) — learned QueryGen module (single-layer transformer decoder, cross-attention to reasoning step embeddings, 768-dim adaptive query representations); +11.8% F1 on MuSiQue (71.2%), +10.1% average across 3 benchmarks; Section 6.9 identifies verification retrievals (31% of cases) as a distinct pattern reducing backtracking by 18%; Section 7.3 identifies over-retrieval during exploration as 31% of failures; implicitly adaptive but not intent-differentiated despite observing the need
- RAG-Star: Enhancing Deliberative Reasoning with Retrieval Augmented Verification and Refinement (NAACL 2025, Jiang et al.) — MCTS-based reasoning with retrieval-augmented verification at tree nodes (answer-document consistency scoring), query- and answer-aware reward modeling; verifies candidate answers in tree search with uniform retrieval, not intermediate claims with contrastive queries
- Chain-of-Retrieval Augmented Generation [CoRAG] (NeurIPS 2025, arXiv 2501.14342) — dynamic query reformulation via rejection sampling training, SOTA on KILT, >10-point EM on multi-hop QA; reformulates queries based on evolving state but without intent differentiation
- Scaling Search-Augmented LLM Reasoning via Adaptive Information Control [DeepControl] (arXiv 2602.01672, ICLR 2026 Workshop SPOT) — information utility = ρ·Novelty + (1−ρ)·Effectiveness, retrieval continuation and granularity control with annealed curriculum; +9.4% on Qwen2.5-7B over RL baselines; controls retrieval volume, not query construction strategy
- Search and Refine During Think [AutoRefine] (NeurIPS 2025, arXiv 2505.11277) — &lt;refine> step distilling evidence between search calls, GRPO with dual rewards (answer + retrieval quality); trains for 300 steps on Search-R1/veRL/GRPO stack and achieves convergence; HotpotQA: 0.405 vs 0.297 Search-R1, MuSiQue: 0.157 vs 0.066; refines evidence post-retrieval without intent-differentiated query construction
- Retrieval Augmented Fact Verification by Synthesizing Contrastive Arguments [RAFTS] (ACL 2024) — LLM-based contrastive supporting/refuting argument synthesis with two-stage BM25+dense retrieval pipeline; demonstrates contrastive evidence framing improves verification; standalone system, not integrated in reasoning RL
- Veri-R1: Toward Precise and Faithful Claim Verification via Online Reinforcement Learning (arXiv 2510.01932, Oct 2025) — GRPO-trained iterative claim verification with Qwen2.5-3B-Instruct and Llama3.2-3B-Instruct on FEVEROUS/EX-FEVER/FEVER/SciFACT/HOVER; 4-component reward (label correctness + evidence IoU + format compliance + validity weight); improves joint accuracy by 30%, doubles evidence scores; does NOT differentiate retrieval intent despite being verification-focused; open-source on Search-R1/veRL; most directly comparable RL-based verification baseline
- HARIS: Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification (arXiv 2506.07528, Jun 2025) — hierarchical two-agent architecture (reasoning + search) with GRPO training on Qwen3-4B; evaluates on EX-FEVER (80.12% F1 on 2-hop) and HOVER (61.00% accuracy on 4-hop); uniform search strategy without intent differentiation
- Reason and Verify: A Framework for Faithful Retrieval-Augmented Generation (arXiv 2603.10143, Mar 2026) — biomedical RAG with eight-category verification taxonomy, explicit sub-claim grounding, BGE cross-encoder reranking; 89.1% on BioASQ-Y/N with Llama-3-8B-Instruct; domain-specific but demonstrates concurrent interest in structured verification within RAG; uniform retrieval without intent classification
- R1-Searcher++: Incentivizing Dynamic Knowledge Acquisition of LLMs via RL (arXiv 2505.17005, May 2025) — internal vs. external knowledge distinction, not intent within external retrieval
- REPAIR: Adaptive Retrieval for Reasoning-Intensive Retrieval (arXiv 2601.04618, Jan 2026) — reasoning plans for reranking; operates post-retrieval, not at query construction
- FIRE: Fact-checking with Iterative Retrieval and Verification (NAACL Findings 2025) — confidence-based iterative retrieval; 7.6× cost reduction but same query strategy per iteration
- Don't Let It Hallucinate: Premise Verification via Retrieval-Augmented Logical Reasoning (NeurIPS 2025) — pre-generation premise verification, not during reasoning chain
- Adaptive Retrieval helps Reasoning in LLMs — but mostly if it's not used (arXiv 2602.07213, Shakya et al., Feb 2026) — traces with retrieval perform slightly worse than CoT; adaptive retrieval (choosing when to retrieve) improves overall performance; directly motivates that retrieval quality and intent matching matters more than retrieval volume
- DualRAG: A Dual-Process Approach to Integrate Reasoning and Retrieval for Multi-Hop QA (ACL 2025) — dual reasoning-retrieval processes but uniform retrieval strategy
- AgentIR: Reasoning-Aware Retrieval for Deep Research Agents (arXiv 2603.04384, Mar 2026) — encodes reasoning traces in embeddings but uniform intent across all retrieval calls
- SURE-RAG: Sufficiency and Uncertainty-Aware Evidence Verification for Selective RAG (arXiv, May 2026) — post-retrieval claim-evidence scoring
- Entropic Claim Resolution: Uncertainty-Driven Evidence Selection for RAG (arXiv, Mar 2026) — post-retrieval evidence selection via entropy minimization
- Beyond Correctness: Rewarding Faithful Reasoning in RAG [VERITAS] (arXiv, Oct 2025) — faithfulness reward for generators, not retrieval modification
- Interleaving Retrieval with Chain-of-Thought Reasoning [IRCoT] (ACL 2023) — fixed-interval retrieval baseline
- Adaptive-RAG: Learning to Adapt Retrieval-Augmented LLMs through Question Complexity (NAACL 2024)
- veRL GitHub issues #1580, #3816 — Qwen3-8B GRPO training 10-20× slower than Qwen2.5-7B due to generation speed regression; motivates our model choice
- ms-swift GitHub issue #3302 — GRPO training speed benchmark: 60-70 sec/step for Qwen2.5-7B full-parameter GRPO on 8×A800 with veRL; calibrates our per-step compute estimate

## 资源估算
### auto_research
- **claude_api_cost**: $200-400 (est. 2000-4000 turns for autonomous experiment design and paper drafting)
- **estimated_gpu_cost**: ~$630 (210h × ~$3.00/hr)
- **gpu_hours**: ≤210 H100-hours (hard budget cap). Agent must track cumulative GPU-hours (wall-time × GPUs, not wall-time alone) and prioritize: primary dual-intent run (~83h) and baseline run (~83h) are mandatory; BM25-only ablation at 250 steps (~42h) is included only if cumulative spend remains ≤168h after the two primary runs. If approaching cap, agent reduces ablation steps or skips lowest-priority analysis.
- **gpu_utilization**: ~85-95% utilization; agent pipelines experiments continuously
- **risk_note**: Agent should implement early stopping on reward plateau detection (GRPO risks reward collapse beyond ~500 steps); if pilot feasibility fails (intent categories not distinguishable), agent should pivot to testing contrastive verification queries without intent classification
- **speed_bottleneck**: Primary bottleneck is sequential GRPO runs on 8 GPUs (~10.4 wall-hours each at 75 sec/step); BM25 index pre-built, E5 FAISS index downloadable from Search-R1; NLI inference adds ~5-10% per-step overhead
- **team**: 0 (initial setup and final review only)
- **timeline**: 6-9 days with 8×H100 available

### human_in_loop
- **claude_api_cost**: $100-200 (est. 1000-2000 turns for code generation and experiment analysis)
- **estimated_gpu_cost**: ~$606-630 (202-210h × ~$3.00/hr)
- **gpu_hours**: ~202-210 H100-hours. Base plan (~202h) plus agent-proposed extensions with human approval: reduced-scale BM25-only ablation (250 steps on 8×H100 = 250 × 75 sec ≈ 5.2 wall-hours × 8 GPUs ≈ ~42h), reward weighting variants, or heuristic threshold tuning. Extensions prioritized by expected information value within remaining budget.
- **gpu_utilization**: ~55-70% utilization; agent queues experiments while human reviews
- **risk_note**: Composite faithfulness+correctness reward may need human judgment on α weighting if RL training shows reward hacking on the faithfulness component; if per-step time exceeds 90 sec, human approves step-count reduction to 400
- **team**: 1 researcher, ~20-30min/day reviewing proposals and results
- **timeline**: 2-3 weeks

### manual
- **estimated_gpu_cost**: ~$606 (202h × ~$3.00/hr H100 spot pricing)
- **gpu_hours**: ~202 H100-hours total (range: 183-215 depending on per-step training speed). Breakdown with explicit wall-time × GPU arithmetic: Phase 0 pilot: ~5h (generation only, 1-2 GPUs); Phase 1 SFT cold start: ~5h (100 SFT steps); Phase 2 GRPO training: 2 runs × 500 steps × ~75 sec/step = 2 × (10.4 wall-hours × 8 GPUs) = ~166h; NLI overhead during training: ~8h; Phase 3 evaluation on 6 benchmarks: ~18h. Dense index building: ~0h (Search-R1 provides pre-built E5-base-v2 FAISS indexes). Per-step calibration: veRL GRPO benchmarks show 60-70 sec/step for Qwen2.5-7B on 8×A800 (ms-swift issue #3302); we estimate ~75 sec/step for Search-R1 on 8×H100, accounting for retrieval overhead partially offset by H100 throughput advantage. Contingency: if per-step exceeds 90 sec, reduce to 400 steps/run (above AutoRefine's 300-step convergence), giving 2 × (10.0 wall-hours × 8 GPUs) = ~160h for Phase 2, ~196h total.
- **gpu_utilization**: ~40-50% effective utilization; GPUs idle during implementation, debugging, and analysis phases
- **team**: 1 researcher with RL and retrieval experience
- **timeline**: 10-12 days (10 days with 8×H100 and familiarity with Search-R1/veRL codebase; 12 days otherwise)



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "afc6e2fe-4901-4946-8533-77cf3ebefba5",
  "type": "user",
  "uuid": "a512bfe7-dae3-45ea-ae92-6bc889914eab",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T01:48:41.520Z_

```json
{
  "parentUuid": "a512bfe7-dae3-45ea-ae92-6bc889914eab",
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
  "uuid": "1c45c3fa-6106-4155-84f0-8dcf9d013f9c",
  "timestamp": "2026-05-16T01:48:41.520Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T01:48:41.520Z_

```json
{
  "parentUuid": "1c45c3fa-6106-4155-84f0-8dcf9d013f9c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "16eeedb1-d547-4750-a0e4-c0bcefacf7e7",
  "timestamp": "2026-05-16T01:48:41.520Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Dual-Intent Retrieval: Intent-Differentiated Query Formulation for Reasoning-Augmented RAG  **状态**: 待审阅   **级别**…",
  "leafUuid": "16eeedb1-d547-4750-a0e4-c0bcefacf7e7",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate dual-intent retrieval proposal",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891"
}
```

---

### Assistant

_source line 8 · 2026-05-16T01:49:26.530Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal for EMNLP 2026 main conference submission. I need to evaluate the idea quality — core claim logic, novelty, significance — without assessing execution/experiments.

Let me first understand the core idea:

The proposal introduces "Dual-Intent Retrieval" — explicitly classifying each retrieval call in a reasoning model's chain-of-thought as either "discovery-intent" (seeking new evidence) or "verification-intent" (seeking to confirm/refute a claim), then applying structurally different query construction and retrieval strategies for each type.

Key claims:
1. Retrieval intent within reasoning chains is structurally bimodal (discovery vs. verification)


2. Current systems treat all retrieval uniformly despite evidence this distinction matters
3. Differentiating query construction strategy by intent will improve reasoning performance
4. RL can discover sophisticated verification query strategies through a structured action space

Now I'm checking whether the trivial alternative — just applying the same hybrid retrieval approach (BM25 + dense + NLI reranking) to all queries regardless of intent classification — would be sufficient. The proposal suggests intent classification adds value beyond just using better retrieval uniformly, though this needs careful examination.

Another simpler alternative would be to add NLI-based reranking to everything without intent classification at all, since the entailment-contradiction ranking signal might just be universally better. There's also a planned ablation comparing dual-intent tokens with standard retrieval across both modes to isolate whether intent classification itself matters versus just having a better retrieval pipeline.

For the premise check, the core assumption that retrieval intent splits cleanly into discovery versus verification comes from ReaLM-Retrieve's analysis, but that work actually identified three patterns — early resolution at 42%, verification at 31%, and then a third category that wasn't fully captured by the bimodal framing.

The claim that verification queries should actively seek disconfirming evidence, which would be anti-correlated with topical relevance, is somewhat hand-wavy. In practice, documents containing disconfirming evidence are often topically relevant too, so that anti-correlation needs stronger justification. There's also the untested assumption that heuristic rules can reliably classify intent from reasoning traces — the 75% accuracy threshold is set, but noisy classification could make the differentiation worse than just treating everything uniformly. And the expectation that RL will discover sophisticated verification strategies from the structured format is aspirational; 500 GRPO steps might not be enough to learn nuanced query formulation patterns.

The core novelty boils down to explicit intent classification paired with structured retrieval approaches, though that's where the assumptions start to accumulate.

Looking at the actual novelty here, the observation that retrieval intent varies isn't new — ReaLM-Retrieve already identified it, and it's fairly intuitive. The binary discovery/verification taxonomy is reasonable but obvious, and using different retrieval strategies for different query types is well-established in information retrieval. The specific combination of BM25 for discovery plus hybrid BM25+dense+NLI for verification is engineering rather than fundamental insight. The RL-discovered query strategies contribution is speculative and hinges on what RL actually learns. This feels more like systems integration — taking an observed distinction, making it explicit, and applying different pipelines — which is solid engineering but intellectually modest compared to the core claims.

Comparing against the most relevant work, the deltas are all incremental: ReaLM-Retrieve observed the distinction but didn't act on it; Veri-R1 did verification-specific RL but with uniform queries; RAFTS developed contrastive retrieval for fact-checking; AutoRefine tackled post-retrieval refinement. The novelty here is connecting existing observations with existing techniques rather than introducing fundamentally new ideas. The RL-discovered strategies could add something, but that's still speculative.

The problem itself is important and timely, but the specific approach of binary intent classification feels narrow and unlikely to surprise reviewers—most would probably expect that differentiating retrieval strategies helps, so the real question is just whether the gains are meaningful. The research angle is fairly constrained to one aspect of one type of system, which limits potential impact if the results are only modest.

The related work section covers the landscape well, positioning clearly against ReaLM-Retrieve, Veri-R1, RAFTS, CoRAG, DeepControl, AutoRefine, and RAG-Star.

I should verify whether recent work has already tackled this gap more directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16eeedb1-d547-4750-a0e4-c0bcefacf7e7",
  "isSidechain": false,
  "requestId": "req_011Cb5QYc8uHSLTXh9EEqbk3",
  "type": "assistant",
  "uuid": "b08a10a0-3afc-46f5-add3-203ee9f50606",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwdNfw91qmCpCPNgJyi7z9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28111,
      "cache_read_input_tokens": 0,
      "output_tokens": 1508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28111,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1508,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 28111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28111
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

_source line 9 · 2026-05-16T01:49:26.966Z_

I need to verify the novelty claims against recent literature before scoring. Let me search for potentially overlapping work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b08a10a0-3afc-46f5-add3-203ee9f50606",
  "isSidechain": false,
  "requestId": "req_011Cb5QYc8uHSLTXh9EEqbk3",
  "type": "assistant",
  "uuid": "9e088afa-ba72-4333-87fd-92fa4ddb6366",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwdNfw91qmCpCPNgJyi7z9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28111,
      "cache_read_input_tokens": 0,
      "output_tokens": 1508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28111,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1508,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 28111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28111
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

_source line 10 · 2026-05-16T01:49:27.356Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016p3wjWkyfzjHtNua2KBdeZ`</summary>

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
  "parentUuid": "9e088afa-ba72-4333-87fd-92fa4ddb6366",
  "isSidechain": false,
  "requestId": "req_011Cb5QYc8uHSLTXh9EEqbk3",
  "type": "assistant",
  "uuid": "ec18354a-25e3-452e-a0d5-ab11ccf3b7de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwdNfw91qmCpCPNgJyi7z9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28111,
      "cache_read_input_tokens": 0,
      "output_tokens": 1508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28111,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1508,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 28111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28111
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

_source line 11 · 2026-05-16T01:49:27.364Z_

<details><summary>↩ Tool result · `toolu_016p3wjWkyfzjHtNua2KBdeZ`</summary>

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
  "parentUuid": "ec18354a-25e3-452e-a0d5-ab11ccf3b7de",
  "isSidechain": false,
  "promptId": "afc6e2fe-4901-4946-8533-77cf3ebefba5",
  "type": "user",
  "uuid": "18bdf602-5272-4383-a2a8-f8bd28c51640",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "ec18354a-25e3-452e-a0d5-ab11ccf3b7de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-16T01:49:29.690Z_

<details><summary>Logged reasoning block</summary>

```text
Let me search for recent work that might overlap with this proposal's core contribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18bdf602-5272-4383-a2a8-f8bd28c51640",
  "isSidechain": false,
  "requestId": "req_011Cb5QbtH6XA973gPcf1Rco",
  "type": "assistant",
  "uuid": "8567eb0a-4f29-49c4-bd7a-70611095a2e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pga16bmTeRwkvFgcgRjfar",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2030,
      "cache_read_input_tokens": 28111,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 28111,
          "cache_creation_input_tokens": 2030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2030
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

_source line 13 · 2026-05-16T01:49:30.679Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J5N49VYG9Xb2zLDH4Wm4yB`</summary>

```json
{
  "query": "intent-differentiated retrieval reasoning chain discovery verification query construction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8567eb0a-4f29-49c4-bd7a-70611095a2e0",
  "isSidechain": false,
  "requestId": "req_011Cb5QbtH6XA973gPcf1Rco",
  "type": "assistant",
  "uuid": "f5a644e1-dc63-478d-b15e-1a36d963f55a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pga16bmTeRwkvFgcgRjfar",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2030,
      "cache_read_input_tokens": 28111,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 28111,
          "cache_creation_input_tokens": 2030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2030
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

_source line 14 · 2026-05-16T01:49:31.631Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CFQmTPxbrQctDJB5D2UkpY`</summary>

```json
{
  "query": "contrastive query formulation claim verification retrieval augmented generation RL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5a644e1-dc63-478d-b15e-1a36d963f55a",
  "isSidechain": false,
  "requestId": "req_011Cb5QbtH6XA973gPcf1Rco",
  "type": "assistant",
  "uuid": "c625db91-4023-4314-a80b-ed8e49b42680",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pga16bmTeRwkvFgcgRjfar",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2030,
      "cache_read_input_tokens": 28111,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 28111,
          "cache_creation_input_tokens": 2030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2030
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

_source line 15 · 2026-05-16T01:49:32.279Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014R5vCCqj7f7nqYMFjvZ7gA`</summary>

```json
{
  "query": "dual intent retrieval RAG reasoning models query strategy differentiation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c625db91-4023-4314-a80b-ed8e49b42680",
  "isSidechain": false,
  "requestId": "req_011Cb5QbtH6XA973gPcf1Rco",
  "type": "assistant",
  "uuid": "73172a5e-c7e2-4166-bc10-de09bab5742d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pga16bmTeRwkvFgcgRjfar",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2030,
      "cache_read_input_tokens": 28111,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 28111,
          "cache_creation_input_tokens": 2030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2030
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

_source line 16 · 2026-05-16T01:49:38.309Z_

<details><summary>↩ Tool result · `toolu_01CFQmTPxbrQctDJB5D2UkpY`</summary>

```text
Web search results for query: "contrastive query formulation claim verification retrieval augmented generation RL 2026"

Links: [{"title":"Retrieval Augmented Fact Verification by Synthesizing Contrastive Arguments","url":"https://arxiv.org/html/2406.09815v1"},{"title":"Optimizing Retrieval for RAG via Reinforced Contrastive Learning","url":"https://arxiv.org/html/2510.24652v1"},{"title":"Contrastive Retrieval-Augmented Generation on Experience","url":"https://aclanthology.org/2025.findings-acl.1224.pdf"},{"title":"Retrieval-Augmented Generation for AI-Generated Content: A Survey | Data Science and Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s41019-025-00335-5"},{"title":"Reason and Verify: A Framework for Faithful Retrieval-Augmented Generation","url":"https://arxiv.org/html/2603.10143"},{"title":"Retrieval Augmented Fact Verification by Synthesizing Contrastive Arguments | Request PDF","url":"https://www.researchgate.net/publication/381471159_Retrieval_Augmented_Fact_Verification_by_Synthesizing_Contrastive_Arguments"},{"title":"Reinforced Informativeness Optimization for Long-Form Retrieval-Augmented Generation","url":"https://arxiv.org/html/2505.20825"},{"title":"Retrieval-Augmented Generation with Conflicting Evidence","url":"https://arxiv.org/html/2504.13079v2"},{"title":"GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.","url":"https://github.com/liunian-Jay/Awesome-RAG"},{"title":"Retrieval Augmented Fact Verification by Synthesizing Contrastive Arguments - Illinois Experts","url":"https://experts.illinois.edu/en/publications/retrieval-augmented-fact-verification-by-synthesizing-contrastive"}]

Based on the search results, here are the key findings related to your query about contrastive query formulation, claim verification, and retrieval-augmented generation with RL in 2026:

## Key Research Areas

**Contrastive Arguments in Fact Verification:**

RAFTS (Retrieval Augmented Fact Verification through the synthesis of contrastive arguments) effectively retrieves relevant documents and performs few-shot fact verification using pretrained LLMs. RAFTS forms contrastive arguments (i.e., supporting or refuting) conditioned on the retrieved evidence.

**Reinforced Contrastive Learning for RAG:**

R3 is a Retrieval framework optimized for RAG through trial-and-feedback Reinforced contrastive learning. During training, the retrieved results interact with the environment to produce contrastive signals that automatically guide the retriever's self-improvement.

**Recent RL Approaches (2025-2026):**

Recent progress has motivated RL for autonomous retrieval invocation within long reasoning chains by multiple researchers in 2025 and 2026. Recent work includes CTRL-RAG (Contrastive Likelihood Reward Based Reinforcement Learning for Context-Faithful RAG Models) and ProRAG (Process-Supervised Reinforcement Learning for Retrieval-Augmented Generation).

These developments show active research combining contrastive methods with reinforcement learning to improve both query formulation and claim verification in RAG systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c625db91-4023-4314-a80b-ed8e49b42680",
  "isSidechain": false,
  "promptId": "afc6e2fe-4901-4946-8533-77cf3ebefba5",
  "type": "user",
  "uuid": "c4a8b0af-6666-4838-93e6-b564e5eca66b",
  "toolUseResult": {
    "query": "contrastive query formulation claim verification retrieval augmented generation RL 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HWjeyZFR1zMa17edSAp8s9",
        "content": [
          {
            "title": "Retrieval Augmented Fact Verification by Synthesizing Contrastive Arguments",
            "url": "https://arxiv.org/html/2406.09815v1"
          },
          {
            "title": "Optimizing Retrieval for RAG via Reinforced Contrastive Learning",
            "url": "https://arxiv.org/html/2510.24652v1"
          },
          {
            "title": "Contrastive Retrieval-Augmented Generation on Experience",
            "url": "https://aclanthology.org/2025.findings-acl.1224.pdf"
          },
          {
            "title": "Retrieval-Augmented Generation for AI-Generated Content: A Survey | Data Science and Engineering | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s41019-025-00335-5"
          },
          {
            "title": "Reason and Verify: A Framework for Faithful Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2603.10143"
          },
          {
            "title": "Retrieval Augmented Fact Verification by Synthesizing Contrastive Arguments | Request PDF",
            "url": "https://www.researchgate.net/publication/381471159_Retrieval_Augmented_Fact_Verification_by_Synthesizing_Contrastive_Arguments"
          },
          {
            "title": "Reinforced Informativeness Optimization for Long-Form Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2505.20825"
          },
          {
            "title": "Retrieval-Augmented Generation with Conflicting Evidence",
            "url": "https://arxiv.org/html/2504.13079v2"
          },
          {
            "title": "GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.",
            "url": "https://github.com/liunian-Jay/Awesome-RAG"
          },
          {
            "title": "Retrieval Augmented Fact Verification by Synthesizing Contrastive Arguments - Illinois Experts",
            "url": "https://experts.illinois.edu/en/publications/retrieval-augmented-fact-verification-by-synthesizing-contrastive"
          }
        ]
      },
      "Based on the search results, here are the key findings related to your query about contrastive query formulation, claim verification, and retrieval-augmented generation with RL in 2026:\n\n## Key Research Areas\n\n**Contrastive Arguments in Fact Verification:**\n\nRAFTS (Retrieval Augmented Fact Verification through the synthesis of contrastive arguments) effectively retrieves relevant documents and performs few-shot fact verification using pretrained LLMs. RAFTS forms contrastive arguments (i.e., supporting or refuting) conditioned on the retrieved evidence.\n\n**Reinforced Contrastive Learning for RAG:**\n\nR3 is a Retrieval framework optimized for RAG through trial-and-feedback Reinforced contrastive learning. During training, the retrieved results interact with the environment to produce contrastive signals that automatically guide the retriever's self-improvement.\n\n**Recent RL Approaches (2025-2026):**\n\nRecent progress has motivated RL for autonomous retrieval invocation within long reasoning chains by multiple researchers in 2025 and 2026. Recent work includes CTRL-RAG (Contrastive Likelihood Reward Based Reinforcement Learning for Context-Faithful RAG Models) and ProRAG (Process-Supervised Reinforcement Learning for Retrieval-Augmented Generation).\n\nThese developments show active research combining contrastive methods with reinforcement learning to improve both query formulation and claim verification in RAG systems."
    ],
    "durationSeconds": 6.673629401999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c625db91-4023-4314-a80b-ed8e49b42680",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T01:49:38.416Z_

<details><summary>↩ Tool result · `toolu_01J5N49VYG9Xb2zLDH4Wm4yB`</summary>

```text
Web search results for query: "intent-differentiated retrieval reasoning chain discovery verification query construction 2025 2026"

Links: [{"title":"Intent-Aware Neural Query Reformulation for Behavior-Aligned Product Search","url":"https://arxiv.org/html/2507.22213"},{"title":"[2604.27252] Unified Data Discovery across Query Modalities and User Intents","url":"https://arxiv.org/abs/2604.27252"},{"title":"GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.","url":"https://github.com/liunian-Jay/Awesome-RAG"},{"title":"Example-driven semantic-similarity-aware query intent discovery: Empowering users to cross the SQL barrier through query by example - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0306437926000013"},{"title":"Published as a conference paper at ICLR 2025 CHAIN-OF-ACTION:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a0b1082fc7823c4c68abcab4fa850e9c-Paper-Conference.pdf"},{"title":"A Survey on Retrieval And Structuring Augmented Generation","url":"https://arxiv.org/pdf/2509.10697"},{"title":"Reasoning Processes for Multi-hop Question Answering","url":"https://arxiv.org/pdf/2601.00536"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"From Web Search towards Agentic Deep ReSearch: Incentivizing Search with Reasoning Agents","url":"https://arxiv.org/html/2506.18959v1"},{"title":"Retrieval Augmented Generation (RAG) for LLMs | Prompt Engineering Guide&lt;!-- -->","url":"https://www.promptingguide.ai/research/rag"}]

Based on the web search results, I found several relevant recent papers and research addressing the topics you're interested in. Here's what the search uncovered:

## Intent-Differentiated Retrieval and Query Reformulation

Recent research centers on developing an intent-aware modeling framework that tailors query rewriting strategies to distinct buyer intent categories, operationalizing buyer queries into canonical intent classes—transactional, navigational, and informational—and applying differentiated reformulation mechanisms optimized for each intent bucket.

## Data Discovery Across Query Modalities

Data discovery must support different query modalities, including natural language statements and tables, and accommodate diverse user intents ranging from open-ended enrichment to task-driven inference. A unified data discovery framework called UniDisc supports both NL statements and tables as queries and generalizes across diverse user intents without intent-specific representations or relevance modeling.

## Reasoning and Verification in Retrieval-Augmented Systems

Recent work argues that seeking external information should manifest as configurable 'Plug-and-Play' actions such as querying web text, encoding domain knowledge, and analyzing tabular and numerical data. A key feature is automatically soliciting external information that forms as tokens, vectors, or numbers for integration into model reasoning, with actions designed as dataset-agnostic modules that LLMs invoke selectively.

## Multi-hop Reasoning and Verification Processes

Most literature in this area focuses on architectural or training innovations and treats how retrieval and reasoning interact as an implementation detail, with the sequence of retrieval calls, intermediate hypotheses, and stopping decisions rarely made explicit.

The search results reveal an active research landscape in 2025-2026 focused on making retrieval systems more intent-aware, supporting diverse query types, and improving the integration of reasoning with retrieval processes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5a644e1-dc63-478d-b15e-1a36d963f55a",
  "isSidechain": false,
  "promptId": "afc6e2fe-4901-4946-8533-77cf3ebefba5",
  "type": "user",
  "uuid": "640975e4-29de-420f-abd3-d61c8956438f",
  "toolUseResult": {
    "query": "intent-differentiated retrieval reasoning chain discovery verification query construction 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AW5LHJP8y8zRxaLf6E8LDW",
        "content": [
          {
            "title": "Intent-Aware Neural Query Reformulation for Behavior-Aligned Product Search",
            "url": "https://arxiv.org/html/2507.22213"
          },
          {
            "title": "[2604.27252] Unified Data Discovery across Query Modalities and User Intents",
            "url": "https://arxiv.org/abs/2604.27252"
          },
          {
            "title": "GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.",
            "url": "https://github.com/liunian-Jay/Awesome-RAG"
          },
          {
            "title": "Example-driven semantic-similarity-aware query intent discovery: Empowering users to cross the SQL barrier through query by example - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0306437926000013"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 CHAIN-OF-ACTION:",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/a0b1082fc7823c4c68abcab4fa850e9c-Paper-Conference.pdf"
          },
          {
            "title": "A Survey on Retrieval And Structuring Augmented Generation",
            "url": "https://arxiv.org/pdf/2509.10697"
          },
          {
            "title": "Reasoning Processes for Multi-hop Question Answering",
            "url": "https://arxiv.org/pdf/2601.00536"
          },
          {
            "title": "Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches",
            "url": "https://arxiv.org/html/2510.04905v1"
          },
          {
            "title": "From Web Search towards Agentic Deep ReSearch: Incentivizing Search with Reasoning Agents",
            "url": "https://arxiv.org/html/2506.18959v1"
          },
          {
            "title": "Retrieval Augmented Generation (RAG) for LLMs | Prompt Engineering Guide&lt;!-- -->",
            "url": "https://www.promptingguide.ai/research/rag"
          }
        ]
      },
      "Based on the web search results, I found several relevant recent papers and research addressing the topics you're interested in. Here's what the search uncovered:\n\n## Intent-Differentiated Retrieval and Query Reformulation\n\nRecent research centers on developing an intent-aware modeling framework that tailors query rewriting strategies to distinct buyer intent categories, operationalizing buyer queries into canonical intent classes—transactional, navigational, and informational—and applying differentiated reformulation mechanisms optimized for each intent bucket.\n\n## Data Discovery Across Query Modalities\n\nData discovery must support different query modalities, including natural language statements and tables, and accommodate diverse user intents ranging from open-ended enrichment to task-driven inference. A unified data discovery framework called UniDisc supports both NL statements and tables as queries and generalizes across diverse user intents without intent-specific representations or relevance modeling.\n\n## Reasoning and Verification in Retrieval-Augmented Systems\n\nRecent work argues that seeking external information should manifest as configurable 'Plug-and-Play' actions such as querying web text, encoding domain knowledge, and analyzing tabular and numerical data. A key feature is automatically soliciting external information that forms as tokens, vectors, or numbers for integration into model reasoning, with actions designed as dataset-agnostic modules that LLMs invoke selectively.\n\n## Multi-hop Reasoning and Verification Processes\n\nMost literature in this area focuses on architectural or training innovations and treats how retrieval and reasoning interact as an implementation detail, with the sequence of retrieval calls, intermediate hypotheses, and stopping decisions rarely made explicit.\n\nThe search results reveal an active research landscape in 2025-2026 focused on making retrieval systems more intent-aware, supporting diverse query types, and improving the integration of reasoning with retrieval processes."
    ],
    "durationSeconds": 7.732499564999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f5a644e1-dc63-478d-b15e-1a36d963f55a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Dual-Intent Retrieval: Intent-Differentiated Query Formulation for Reasoning-Augmented RAG  **状态**: 待审阅   **级别**…",
  "leafUuid": "640975e4-29de-420f-abd3-d61c8956438f",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate dual-intent retrieval proposal",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891"
}
```

---

### Tool result

_source line 20 · 2026-05-16T01:49:40.432Z_

<details><summary>↩ Tool result · `toolu_014R5vCCqj7f7nqYMFjvZ7gA`</summary>

```text
Web search results for query: "dual intent retrieval RAG reasoning models query strategy differentiation 2025 2026"

Links: [{"title":"Advanced RAG: Techniques & Concepts | Data Science Collective","url":"https://medium.com/data-science-collective/advanced-rag-techniques-concepts-e0b67366c5cf"},{"title":"KA-RAG: Integrating Knowledge Graphs and Agentic Retrieval-Augmented Generation for an Intelligent Educational Question-Answering Model","url":"https://www.mdpi.com/2076-3417/15/23/12547"},{"title":"When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models","url":"https://arxiv.org/html/2604.26649"},{"title":"DualRAG: A Dual-Process Approach to Integrate Reasoning and Retrieval for Multi-Hop Question Answering","url":"https://arxiv.org/html/2504.18243"},{"title":"A Survey of RAG-Reasoning Systems in LLMs","url":"https://arxiv.org/pdf/2507.09477"},{"title":"From RAG to Context - A 2025 year-end review of RAG | RAGFlow","url":"https://ragflow.io/blog/rag-review-2025-from-rag-to-context"},{"title":"MIND-RAG: Multimodal Context-Aware and Intent-Aware ...","url":"https://openaccess.thecvf.com/content/ICCV2025W/MRR%202025/papers/Yu_MIND-RAG_Multimodal_Context-Aware_and_Intent-Aware_Retrieval-Augmented_Generation_for_Educational_Publications_ICCVW_2025_paper.pdf"},{"title":"Agentic RAG: a comprehensive guide to intelligent retrieval and reasoning","url":"https://www.kore.ai/blog/what-is-agentic-rag"},{"title":"[2504.18243] DualRAG: A Dual-Process Approach to Integrate Reasoning and Retrieval for Multi-Hop Question Answering","url":"https://arxiv.org/abs/2504.18243"},{"title":"DualGraphRAG: A Dual-View Graph-Enhanced Retrieval-Augmented Generation Framework for Reliable and Efficient Question Answering","url":"https://www.mdpi.com/2076-3417/16/5/2221"}]

Based on the search results, I've found several relevant research developments in the 2025-2026 timeframe related to dual intent retrieval, RAG reasoning models, and query strategy differentiation:

## Key Recent Developments

**Dual-Process Approaches to RAG:**
DualRAG is a synergistic dual-process framework that seamlessly integrates reasoning and retrieval, operating through two tightly coupled processes: Reasoning-augmented Querying (RaQ) and progressive Knowledge Aggregation (pKA). As RaQ navigates the reasoning path and generates targeted queries, pKA ensures that newly acquired knowledge is systematically integrated to support coherent reasoning.

**Adaptive Retrieval Timing for Reasoning Models:**
Recent research has focused on optimizing when to retrieve during reasoning. The central finding is that fewer, better-timed retrievals outperform frequent, fixed-interval retrievals, pointing toward a broader shift where retrieval systems will need to evolve from pre-generation context providers into dynamic reasoning partners.

**Intent-Aware Retrieval Strategies:**
Systems are combining symbolic graph reasoning with dense semantic retrieval through proposed dual-retrieval strategies that support interpretable, context-aware responses to queries. The AI agent evaluates the intent behind the request, determines the complexity of the task, and identifies whether it requires a straightforward factual response or a multi-step reasoning operation, ensuring that the query is fully understood before any retrieval begins.

**Graph-Enhanced Dual-View Retrieval:**
A dual-view strategy is being designed to jointly retrieve one-hop triples centered on each node and shortest paths between nodes, representing local context and global connectivity information in knowledge graph-enhanced RAG frameworks.

**Agentic RAG Evolution:**
RAG is undergoing its metamorphosis, evolving from the specific pattern of "Retrieval-Augmented Generation" into a "Context Engine" with "intelligent retrieval" as its core capability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73172a5e-c7e2-4166-bc10-de09bab5742d",
  "isSidechain": false,
  "promptId": "afc6e2fe-4901-4946-8533-77cf3ebefba5",
  "type": "user",
  "uuid": "ae9f927a-584f-441b-8fe2-c0ca2ca95df1",
  "toolUseResult": {
    "query": "dual intent retrieval RAG reasoning models query strategy differentiation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EDyBdbtPH3j6qxW9rJcT1m",
        "content": [
          {
            "title": "Advanced RAG: Techniques & Concepts | Data Science Collective",
            "url": "https://medium.com/data-science-collective/advanced-rag-techniques-concepts-e0b67366c5cf"
          },
          {
            "title": "KA-RAG: Integrating Knowledge Graphs and Agentic Retrieval-Augmented Generation for an Intelligent Educational Question-Answering Model",
            "url": "https://www.mdpi.com/2076-3417/15/23/12547"
          },
          {
            "title": "When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models",
            "url": "https://arxiv.org/html/2604.26649"
          },
          {
            "title": "DualRAG: A Dual-Process Approach to Integrate Reasoning and Retrieval for Multi-Hop Question Answering",
            "url": "https://arxiv.org/html/2504.18243"
          },
          {
            "title": "A Survey of RAG-Reasoning Systems in LLMs",
            "url": "https://arxiv.org/pdf/2507.09477"
          },
          {
            "title": "From RAG to Context - A 2025 year-end review of RAG | RAGFlow",
            "url": "https://ragflow.io/blog/rag-review-2025-from-rag-to-context"
          },
          {
            "title": "MIND-RAG: Multimodal Context-Aware and Intent-Aware ...",
            "url": "https://openaccess.thecvf.com/content/ICCV2025W/MRR%202025/papers/Yu_MIND-RAG_Multimodal_Context-Aware_and_Intent-Aware_Retrieval-Augmented_Generation_for_Educational_Publications_ICCVW_2025_paper.pdf"
          },
          {
            "title": "Agentic RAG: a comprehensive guide to intelligent retrieval and reasoning",
            "url": "https://www.kore.ai/blog/what-is-agentic-rag"
          },
          {
            "title": "[2504.18243] DualRAG: A Dual-Process Approach to Integrate Reasoning and Retrieval for Multi-Hop Question Answering",
            "url": "https://arxiv.org/abs/2504.18243"
          },
          {
            "title": "DualGraphRAG: A Dual-View Graph-Enhanced Retrieval-Augmented Generation Framework for Reliable and Efficient Question Answering",
            "url": "https://www.mdpi.com/2076-3417/16/5/2221"
          }
        ]
      },
      "Based on the search results, I've found several relevant research developments in the 2025-2026 timeframe related to dual intent retrieval, RAG reasoning models, and query strategy differentiation:\n\n## Key Recent Developments\n\n**Dual-Process Approaches to RAG:**\nDualRAG is a synergistic dual-process framework that seamlessly integrates reasoning and retrieval, operating through two tightly coupled processes: Reasoning-augmented Querying (RaQ) and progressive Knowledge Aggregation (pKA). As RaQ navigates the reasoning path and generates targeted queries, pKA ensures that newly acquired knowledge is systematically integrated to support coherent reasoning.\n\n**Adaptive Retrieval Timing for Reasoning Models:**\nRecent research has focused on optimizing when to retrieve during reasoning. The central finding is that fewer, better-timed retrievals outperform frequent, fixed-interval retrievals, pointing toward a broader shift where retrieval systems will need to evolve from pre-generation context providers into dynamic reasoning partners.\n\n**Intent-Aware Retrieval Strategies:**\nSystems are combining symbolic graph reasoning with dense semantic retrieval through proposed dual-retrieval strategies that support interpretable, context-aware responses to queries. The AI agent evaluates the intent behind the request, determines the complexity of the task, and identifies whether it requires a straightforward factual response or a multi-step reasoning operation, ensuring that the query is fully understood before any retrieval begins.\n\n**Graph-Enhanced Dual-View Retrieval:**\nA dual-view strategy is being designed to jointly retrieve one-hop triples centered on each node and shortest paths between nodes, representing local context and global connectivity information in knowledge graph-enhanced RAG frameworks.\n\n**Agentic RAG Evolution:**\nRAG is undergoing its metamorphosis, evolving from the specific pattern of \"Retrieval-Augmented Generation\" into a \"Context Engine\" with \"intelligent retrieval\" as its core capability."
    ],
    "durationSeconds": 8.150172002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "73172a5e-c7e2-4166-bc10-de09bab5742d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T01:49:44.917Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DrvZCQ3MMzRp1MH2GRhWmP`</summary>

```json
{
  "query": "ReaLM-Retrieve verification retrieval intent classification query differentiation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae9f927a-584f-441b-8fe2-c0ca2ca95df1",
  "isSidechain": false,
  "requestId": "req_011Cb5QcqqH9T8qnAMJbbPQu",
  "type": "assistant",
  "uuid": "5f93bc27-615d-48a8-9a42-21a4da36f8fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014n3A3bXqjHgNR4cJ35iugi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3158,
      "cache_read_input_tokens": 30141,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3158,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 30141,
          "cache_creation_input_tokens": 3158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3158
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

_source line 22 · 2026-05-16T01:49:45.562Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018nPsZ8xhDKxjUmmBfazZoX`</summary>

```json
{
  "query": "Search-R1 GRPO intent tokens retrieval strategy differentiation reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f93bc27-615d-48a8-9a42-21a4da36f8fc",
  "isSidechain": false,
  "requestId": "req_011Cb5QcqqH9T8qnAMJbbPQu",
  "type": "assistant",
  "uuid": "42fbf1db-3dd9-4eb9-bbc2-a6b2cfc8e09d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014n3A3bXqjHgNR4cJ35iugi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3158,
      "cache_read_input_tokens": 30141,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3158,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 30141,
          "cache_creation_input_tokens": 3158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3158
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

_source line 23 · 2026-05-16T01:49:51.418Z_

<details><summary>↩ Tool result · `toolu_01DrvZCQ3MMzRp1MH2GRhWmP`</summary>

```text
Web search results for query: "ReaLM-Retrieve verification retrieval intent classification query differentiation 2026"

Links: [{"title":"What Is Retrieval-augmented Language Model (REALM)? - Dataconomy","url":"https://dataconomy.com/2025/03/19/what-is-retrieval-augmented-language-model-realm/"},{"title":"Intent-Driven Natural Language Interface: A Hybrid LLM + Intent Classification Approach | by Anil Malkani | Data Science Collective | Medium","url":"https://medium.com/data-science-collective/intent-driven-natural-language-interface-a-hybrid-llm-intent-classification-approach-e1d96ad6f35d"},{"title":"Intent Classification and Resolution | nageoffer/ragent | DeepWiki","url":"https://deepwiki.com/nageoffer/ragent/4.4-intent-classification-and-resolution"},{"title":"A complete guide to RAG evaluation: metrics, testing and best practices","url":"https://www.evidentlyai.com/llm-guide/rag-evaluation"},{"title":"Using Large Language Models to Generate, Validate, and Apply User Intent Taxonomies | ACM Transactions on the Web","url":"https://dl.acm.org/doi/10.1145/3732294"},{"title":"How Intent Classification Works in RAG Systems | by H. Ali | Medium","url":"https://alixaprodev.medium.com/how-intent-classification-works-in-rag-systems-15054d0ec5ce"},{"title":"Thinking in LangGraph - Docs by LangChain","url":"https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph"},{"title":"Intent Classification: 2026 Techniques for NLP Models | Label Your Data","url":"https://labelyourdata.com/articles/machine-learning/intent-classification"},{"title":"REALM: Integrating Retrieval into Language Representation Models","url":"https://blog.research.google/2020/08/realm-integrating-retrieval-into.html?m=1"},{"title":"Adaptive RAG strategy with query classification & retrieval (Gemini & Qdrant) | n8n workflow template","url":"https://n8n.io/workflows/3459-adaptive-rag-strategy-with-query-classification-and-retrieval-gemini-and-qdrant/"}]

Based on the web search results, I found information related to retrieval-augmented systems and intent classification, though I did not find a specific system specifically branded as "ReaLM-Retrieve" with those exact specifications. Here's what I found:

## REALM (Retrieval-Augmented Language Model)

REALM is a retrieval-augmented language model that represents a significant advancement in artificial intelligence within natural language processing, enhancing the performance of language models by effectively integrating knowledge retrieval mechanisms, making them better equipped for question-answering tasks.

## Key Components

REALM's framework features a two-pronged approach, integrating both retrieval and language generation processes, with a knowledge retriever element responsible for identifying and fetching relevant documents that inform the model's responses.

## Intent Classification and Query Differentiation

The best way to retrieve information often depends on the type of question asked, so adaptive systems adapt their strategy based on the user's query intent instead of using a one-size-fits-all approach.

Intent classification helps differentiate between comparison, lookup, ranking, and exploratory tasks.

By focusing on semantics rather than mere keyword matching, retrieval-augmented systems can deliver responses that align closely with the intent behind a question.

The search results don't contain information about a specific "ReaLM-Retrieve" system with those exact specifications from 2026. If you're looking for more specific information about this particular system, you may want to provide additional context or clarification about the source.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f93bc27-615d-48a8-9a42-21a4da36f8fc",
  "isSidechain": false,
  "promptId": "afc6e2fe-4901-4946-8533-77cf3ebefba5",
  "type": "user",
  "uuid": "bc89f7a1-d4cf-428b-bca7-b4e3e9f3e286",
  "toolUseResult": {
    "query": "ReaLM-Retrieve verification retrieval intent classification query differentiation 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011KNpP5Bz6oRLdZ9EGAoEGi",
        "content": [
          {
            "title": "What Is Retrieval-augmented Language Model (REALM)? - Dataconomy",
            "url": "https://dataconomy.com/2025/03/19/what-is-retrieval-augmented-language-model-realm/"
          },
          {
            "title": "Intent-Driven Natural Language Interface: A Hybrid LLM + Intent Classification Approach | by Anil Malkani | Data Science Collective | Medium",
            "url": "https://medium.com/data-science-collective/intent-driven-natural-language-interface-a-hybrid-llm-intent-classification-approach-e1d96ad6f35d"
          },
          {
            "title": "Intent Classification and Resolution | nageoffer/ragent | DeepWiki",
            "url": "https://deepwiki.com/nageoffer/ragent/4.4-intent-classification-and-resolution"
          },
          {
            "title": "A complete guide to RAG evaluation: metrics, testing and best practices",
            "url": "https://www.evidentlyai.com/llm-guide/rag-evaluation"
          },
          {
            "title": "Using Large Language Models to Generate, Validate, and Apply User Intent Taxonomies | ACM Transactions on the Web",
            "url": "https://dl.acm.org/doi/10.1145/3732294"
          },
          {
            "title": "How Intent Classification Works in RAG Systems | by H. Ali | Medium",
            "url": "https://alixaprodev.medium.com/how-intent-classification-works-in-rag-systems-15054d0ec5ce"
          },
          {
            "title": "Thinking in LangGraph - Docs by LangChain",
            "url": "https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph"
          },
          {
            "title": "Intent Classification: 2026 Techniques for NLP Models | Label Your Data",
            "url": "https://labelyourdata.com/articles/machine-learning/intent-classification"
          },
          {
            "title": "REALM: Integrating Retrieval into Language Representation Models",
            "url": "https://blog.research.google/2020/08/realm-integrating-retrieval-into.html?m=1"
          },
          {
            "title": "Adaptive RAG strategy with query classification & retrieval (Gemini & Qdrant) | n8n workflow template",
            "url": "https://n8n.io/workflows/3459-adaptive-rag-strategy-with-query-classification-and-retrieval-gemini-and-qdrant/"
          }
        ]
      },
      "Based on the web search results, I found information related to retrieval-augmented systems and intent classification, though I did not find a specific system specifically branded as \"ReaLM-Retrieve\" with those exact specifications. Here's what I found:\n\n## REALM (Retrieval-Augmented Language Model)\n\nREALM is a retrieval-augmented language model that represents a significant advancement in artificial intelligence within natural language processing, enhancing the performance of language models by effectively integrating knowledge retrieval mechanisms, making them better equipped for question-answering tasks.\n\n## Key Components\n\nREALM's framework features a two-pronged approach, integrating both retrieval and language generation processes, with a knowledge retriever element responsible for identifying and fetching relevant documents that inform the model's responses.\n\n## Intent Classification and Query Differentiation\n\nThe best way to retrieve information often depends on the type of question asked, so adaptive systems adapt their strategy based on the user's query intent instead of using a one-size-fits-all approach.\n\nIntent classification helps differentiate between comparison, lookup, ranking, and exploratory tasks.\n\nBy focusing on semantics rather than mere keyword matching, retrieval-augmented systems can deliver responses that align closely with the intent behind a question.\n\nThe search results don't contain information about a specific \"ReaLM-Retrieve\" system with those exact specifications from 2026. If you're looking for more specific information about this particular system, you may want to provide additional context or clarification about the source."
    ],
    "durationSeconds": 6.494357936999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5f93bc27-615d-48a8-9a42-21a4da36f8fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T01:49:53.582Z_

<details><summary>↩ Tool result · `toolu_018nPsZ8xhDKxjUmmBfazZoX`</summary>

```text
Web search results for query: "Search-R1 GRPO intent tokens retrieval strategy differentiation reasoning 2026"

Links: [{"title":"Search-R1: Training LLMs to Reason and Leverage ...","url":"https://arxiv.org/pdf/2503.09516"},{"title":"Search-R1: RL-Enabled Retrieval for LLMs","url":"https://www.emergentmind.com/topics/search-r1"},{"title":"GitHub - PeterGriffinJin/Search-R1: Search-R1: An Efficient, Scalable RL Training Framework for Reasoning & Search Engine Calling interleaved LLM based on veRL · GitHub","url":"https://github.com/PeterGriffinJin/Search-R1"},{"title":"[2503.09516] Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning","url":"https://ar5iv.labs.arxiv.org/html/2503.09516"},{"title":"Search-R1: A Novel approach to reasoning and retrieval | by Rahul | Medium","url":"https://rahul-tawar.medium.com/search-r1-a-novel-approach-to-reasoning-and-retrieval-bcfcc2400351"},{"title":"GitHub - junfanz1/GRPO: Search-R1 fine-tunes LLMs to decide when to search and when to answer using reinforcement learning over multi-step trajectories. It employs Group Relative Policy Optimization (GRPO) for stable token-level updates without a critic. The model learns adaptive retrieval policies, dynamically integrating search results to construct context and improve r · GitHub","url":"https://github.com/junfanz1/GRPO"},{"title":"Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=Rwhi91ideu"},{"title":"SEARCH-R1: Reinforcement Learning for Search-Augmented LLMs -","url":"https://ajithp.com/2025/03/18/search-r1-reinforcement-learning-llm/"},{"title":"Beyond RAG: Search-R1 Teaches LLMs to Learn How to Search","url":"https://machinelearningatscale.substack.com/p/beyond-rag-search-r1-teaches-llms"},{"title":"R1-Searcher: Incentivizing the Search Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2503.05592v1"}]

Based on the search results, I found comprehensive information about Search-R1, GRPO, intent tokens, retrieval strategy, and differentiation in reasoning. Here are the key findings:

## Search-R1 Overview

Search-R1 is a reinforcement learning framework that dynamically interleaves LLM reasoning with live search queries to fetch external evidence during multi-turn interactions.

## GRPO vs PPO Differentiation

The research provides clear differentiation between these RL methods:

**GRPO Characteristics:**
- GRPO converges faster than PPO across all cases
- GRPO leads to reward collapse after training for many steps, whereas PPO remains stable
- Group Relative Policy Optimization (GRPO) samples multiple trajectories per input, uses their average reward as a baseline, and regularizes with a KL-term to a reference policy

**PPO Characteristics:**
- PPO demonstrates greater training stability
- PPO relies on a critic model, which requires several warm-up steps before effective training begins

## Retrieved Token Masking Strategy

A critical innovation for differentiation in reasoning is retrieved token masking to stabilize training by focusing updates only on LLM-generated tokens. While optimizing LLM-generated tokens enhances the model's ability to interact with the search engine and perform reasoning, applying the same optimization to retrieved tokens can lead to unintended learning dynamics. To address this, loss masking for retrieved tokens ensures that the policy gradient objective is computed only over LLM-generated tokens, while excluding retrieved content from the optimization process.

## Multi-Turn Interleaved Reasoning

Search-R1 supports multi-turn retrieval and reasoning, where search calls are explicitly triggered by search tokens, retrieved content is enclosed within information tokens, while LLM reasoning steps are wrapped within think tokens, with the final answer formatted using answer tokens, allowing for structured, iterative decision-making.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42fbf1db-3dd9-4eb9-bbc2-a6b2cfc8e09d",
  "isSidechain": false,
  "promptId": "afc6e2fe-4901-4946-8533-77cf3ebefba5",
  "type": "user",
  "uuid": "02832ee7-62c8-4401-b406-afb5badb2020",
  "toolUseResult": {
    "query": "Search-R1 GRPO intent tokens retrieval strategy differentiation reasoning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RjCDVJFChDHR9749gL6qCV",
        "content": [
          {
            "title": "Search-R1: Training LLMs to Reason and Leverage ...",
            "url": "https://arxiv.org/pdf/2503.09516"
          },
          {
            "title": "Search-R1: RL-Enabled Retrieval for LLMs",
            "url": "https://www.emergentmind.com/topics/search-r1"
          },
          {
            "title": "GitHub - PeterGriffinJin/Search-R1: Search-R1: An Efficient, Scalable RL Training Framework for Reasoning & Search Engine Calling interleaved LLM based on veRL · GitHub",
            "url": "https://github.com/PeterGriffinJin/Search-R1"
          },
          {
            "title": "[2503.09516] Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning",
            "url": "https://ar5iv.labs.arxiv.org/html/2503.09516"
          },
          {
            "title": "Search-R1: A Novel approach to reasoning and retrieval | by Rahul | Medium",
            "url": "https://rahul-tawar.medium.com/search-r1-a-novel-approach-to-reasoning-and-retrieval-bcfcc2400351"
          },
          {
            "title": "GitHub - junfanz1/GRPO: Search-R1 fine-tunes LLMs to decide when to search and when to answer using reinforcement learning over multi-step trajectories. It employs Group Relative Policy Optimization (GRPO) for stable token-level updates without a critic. The model learns adaptive retrieval policies, dynamically integrating search results to construct context and improve r · GitHub",
            "url": "https://github.com/junfanz1/GRPO"
          },
          {
            "title": "Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=Rwhi91ideu"
          },
          {
            "title": "SEARCH-R1: Reinforcement Learning for Search-Augmented LLMs -",
            "url": "https://ajithp.com/2025/03/18/search-r1-reinforcement-learning-llm/"
          },
          {
            "title": "Beyond RAG: Search-R1 Teaches LLMs to Learn How to Search",
            "url": "https://machinelearningatscale.substack.com/p/beyond-rag-search-r1-teaches-llms"
          },
          {
            "title": "R1-Searcher: Incentivizing the Search Capability in LLMs via Reinforcement Learning",
            "url": "https://arxiv.org/html/2503.05592v1"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about Search-R1, GRPO, intent tokens, retrieval strategy, and differentiation in reasoning. Here are the key findings:\n\n## Search-R1 Overview\n\nSearch-R1 is a reinforcement learning framework that dynamically interleaves LLM reasoning with live search queries to fetch external evidence during multi-turn interactions.\n\n## GRPO vs PPO Differentiation\n\nThe research provides clear differentiation between these RL methods:\n\n**GRPO Characteristics:**\n- GRPO converges faster than PPO across all cases\n- GRPO leads to reward collapse after training for many steps, whereas PPO remains stable\n- Group Relative Policy Optimization (GRPO) samples multiple trajectories per input, uses their average reward as a baseline, and regularizes with a KL-term to a reference policy\n\n**PPO Characteristics:**\n- PPO demonstrates greater training stability\n- PPO relies on a critic model, which requires several warm-up steps before effective training begins\n\n## Retrieved Token Masking Strategy\n\nA critical innovation for differentiation in reasoning is retrieved token masking to stabilize training by focusing updates only on LLM-generated tokens. While optimizing LLM-generated tokens enhances the model's ability to interact with the search engine and perform reasoning, applying the same optimization to retrieved tokens can lead to unintended learning dynamics. To address this, loss masking for retrieved tokens ensures that the policy gradient objective is computed only over LLM-generated tokens, while excluding retrieved content from the optimization process.\n\n## Multi-Turn Interleaved Reasoning\n\nSearch-R1 supports multi-turn retrieval and reasoning, where search calls are explicitly triggered by search tokens, retrieved content is enclosed within information tokens, while LLM reasoning steps are wrapped within think tokens, with the final answer formatted using answer tokens, allowing for structured, iterative decision-making."
    ],
    "durationSeconds": 8.013672514000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "42fbf1db-3dd9-4eb9-bbc2-a6b2cfc8e09d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-16T01:49:56.041Z_

<details><summary>Logged reasoning block</summary>

```text
Let me search more specifically for work that might already differentiate retrieval intent within reasoning chains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02832ee7-62c8-4401-b406-afb5badb2020",
  "isSidechain": false,
  "requestId": "req_011Cb5Qdp4eXXN7iuQqV6Fsw",
  "type": "assistant",
  "uuid": "5c4d0e37-d7a9-40b5-9095-d400b4d27ded",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pc4HjdFW3bN3bwHtmtwn9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2180,
      "cache_read_input_tokens": 33299,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2180,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 33299,
          "cache_creation_input_tokens": 2180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2180
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

_source line 26 · 2026-05-16T01:49:56.993Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MPA8Cr1wRvuAqQJGNogUXx`</summary>

```json
{
  "query": "\"retrieval intent\" \"verification\" \"exploration\" OR \"discovery\" reasoning chain differentiated pipeline arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c4d0e37-d7a9-40b5-9095-d400b4d27ded",
  "isSidechain": false,
  "requestId": "req_011Cb5Qdp4eXXN7iuQqV6Fsw",
  "type": "assistant",
  "uuid": "aecf9811-d8ab-47c1-a116-99852889797f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pc4HjdFW3bN3bwHtmtwn9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2180,
      "cache_read_input_tokens": 33299,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2180,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 33299,
          "cache_creation_input_tokens": 2180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2180
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

_source line 27 · 2026-05-16T01:49:57.856Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vz4zmy8WB15zMkRPmojiEm`</summary>

```json
{
  "query": "HARIS claim verification hierarchical agent GRPO search intent 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aecf9811-d8ab-47c1-a116-99852889797f",
  "isSidechain": false,
  "requestId": "req_011Cb5Qdp4eXXN7iuQqV6Fsw",
  "type": "assistant",
  "uuid": "4197f049-c35e-4833-92d5-db89a7fa04fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pc4HjdFW3bN3bwHtmtwn9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2180,
      "cache_read_input_tokens": 33299,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2180,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 33299,
          "cache_creation_input_tokens": 2180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2180
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

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Dual-Intent Retrieval: Intent-Differentiated Query Formulation for Reasoning-Augmented RAG  **状态**: 待审阅   **级别**…",
  "leafUuid": "4197f049-c35e-4833-92d5-db89a7fa04fd",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate dual-intent retrieval proposal",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891"
}
```

---

### Tool result

_source line 30 · 2026-05-16T01:50:03.729Z_

<details><summary>↩ Tool result · `toolu_01Vz4zmy8WB15zMkRPmojiEm`</summary>

```text
Web search results for query: "HARIS claim verification hierarchical agent GRPO search intent 2025"

Links: [{"title":"Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification","url":"https://arxiv.org/html/2506.07528v1"},{"title":"Example of HARIS's reasoning agent rollout. The reasoning and search... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Example-of-HARISs-reasoning-agent-rollout-The-reasoning-and-search-agents-coordinate_fig2_392529941"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"Autonomous-Agents/README.md at main · tmgthb/Autonomous-Agents","url":"https://github.com/tmgthb/Autonomous-Agents/blob/main/README.md"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf"},{"title":"Multi-LLM Agents Architecture for Claim Verification","url":"https://ceur-ws.org/Vol-3962/paper20.pdf"},{"title":"AI Agents for Claims Automation: A Complete Guide","url":"https://www.v7labs.com/blog/automated-claims-processing-for-insurance"},{"title":"The Missing Layer in Agentic AI","url":"https://www.oreilly.com/radar/the-missing-layer-in-agentic-ai/"},{"title":"VerifiedUser – Identity Verification Tool - HAR.com","url":"https://cms.har.com/verified-user/"},{"title":"[2602.22817] Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks","url":"https://arxiv.org/abs/2602.22817"}]

Based on the search results, I found relevant information about HARIS and its relationship to claim verification, hierarchical agents, and GRPO. Here's what I found:

## HARIS Framework

HARIS (Hierarchical Agent Reasoning and Information Search) is a hierarchical agent framework designed for complex multi-hop claim verification, explicitly modeling the coordinated process of reasoning-driven searching and search-informed reasoning.

## Key Components

The high-level reasoning agent in HARIS constructs the main claim verification chain, coordinating multi-step reasoning and generating factual questions for the search agent when additional information is needed. The reasoning agent constructs the verification chain and issues questions to the search agent, while the search agent performs iterative retrievals and reports relevant information back to the reasoning agent.

## Training with GRPO

HARIS is trained end-to-end via Group Relative Policy Optimization (GRPO) using outcome-based rewards, directly optimizing task performance without intermediate supervision.

## Performance

HARIS demonstrates strong performance on two challenging benchmarks, EX-FEVER and HOVER, validating its effectiveness in tackling multi-hop claim verification.

The framework represents an advance in claim verification by addressing the challenge of coordinating between reasoning and information search to handle complex, multi-hop claims where evidence is fragmented across multiple sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4197f049-c35e-4833-92d5-db89a7fa04fd",
  "isSidechain": false,
  "promptId": "afc6e2fe-4901-4946-8533-77cf3ebefba5",
  "type": "user",
  "uuid": "cfe09dd6-3dc3-4a9d-9612-361cc0cf9673",
  "toolUseResult": {
    "query": "HARIS claim verification hierarchical agent GRPO search intent 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01R4m8A1qi45JMm1AoqzvMVp",
        "content": [
          {
            "title": "Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification",
            "url": "https://arxiv.org/html/2506.07528v1"
          },
          {
            "title": "Example of HARIS's reasoning agent rollout. The reasoning and search... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/Example-of-HARISs-reasoning-agent-rollout-The-reasoning-and-search-agents-coordinate_fig2_392529941"
          },
          {
            "title": "GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub",
            "url": "https://github.com/tmgthb/Autonomous-Agents"
          },
          {
            "title": "Autonomous-Agents/README.md at main · tmgthb/Autonomous-Agents",
            "url": "https://github.com/tmgthb/Autonomous-Agents/blob/main/README.md"
          },
          {
            "title": "Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1",
            "url": "https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf"
          },
          {
            "title": "Multi-LLM Agents Architecture for Claim Verification",
            "url": "https://ceur-ws.org/Vol-3962/paper20.pdf"
          },
          {
            "title": "AI Agents for Claims Automation: A Complete Guide",
            "url": "https://www.v7labs.com/blog/automated-claims-processing-for-insurance"
          },
          {
            "title": "The Missing Layer in Agentic AI",
            "url": "https://www.oreilly.com/radar/the-missing-layer-in-agentic-ai/"
          },
          {
            "title": "VerifiedUser – Identity Verification Tool - HAR.com",
            "url": "https://cms.har.com/verified-user/"
          },
          {
            "title": "[2602.22817] Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks",
            "url": "https://arxiv.org/abs/2602.22817"
          }
        ]
      },
      "Based on the search results, I found relevant information about HARIS and its relationship to claim verification, hierarchical agents, and GRPO. Here's what I found:\n\n## HARIS Framework\n\nHARIS (Hierarchical Agent Reasoning and Information Search) is a hierarchical agent framework designed for complex multi-hop claim verification, explicitly modeling the coordinated process of reasoning-driven searching and search-informed reasoning.\n\n## Key Components\n\nThe high-level reasoning agent in HARIS constructs the main claim verification chain, coordinating multi-step reasoning and generating factual questions for the search agent when additional information is needed. The reasoning agent constructs the verification chain and issues questions to the search agent, while the search agent performs iterative retrievals and reports relevant information back to the reasoning agent.\n\n## Training with GRPO\n\nHARIS is trained end-to-end via Group Relative Policy Optimization (GRPO) using outcome-based rewards, directly optimizing task performance without intermediate supervision.\n\n## Performance\n\nHARIS demonstrates strong performance on two challenging benchmarks, EX-FEVER and HOVER, validating its effectiveness in tackling multi-hop claim verification.\n\nThe framework represents an advance in claim verification by addressing the challenge of coordinating between reasoning and information search to handle complex, multi-hop claims where evidence is fragmented across multiple sources."
    ],
    "durationSeconds": 5.869673043000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4197f049-c35e-4833-92d5-db89a7fa04fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-16T01:50:04.138Z_

<details><summary>↩ Tool result · `toolu_01MPA8Cr1wRvuAqQJGNogUXx`</summary>

```text
Web search results for query: ""retrieval intent" "verification" "exploration" OR "discovery" reasoning chain differentiated pipeline arxiv 2026"

Links: [{"title":"From Web Search towards Agentic Deep ReSearch: Incentivizing Search with Reasoning Agents","url":"https://arxiv.org/html/2506.18959v1"},{"title":"Reasoning by Exploration: A Unified Approach to Retrieval and Generation over Graphs","url":"https://arxiv.org/html/2510.07484"},{"title":"Reasoning in Trees: Improving Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2601.11255"},{"title":"AgentIR: Reasoning-Aware Retrieval for Deep Research Agents","url":"https://arxiv.org/html/2603.04384"},{"title":"A Survey on Retrieval And Structuring Augmented Generation","url":"https://arxiv.org/pdf/2509.10697"},{"title":"[2603.04384] AgentIR: Reasoning-Aware Retrieval for Deep Research Agents","url":"https://arxiv.org/abs/2603.04384"},{"title":"A Survey of RAG-Reasoning Systems in LLMs","url":"https://arxiv.org/pdf/2507.09477"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"Reason and Verify: A Framework for Faithful Retrieval-Augmented Generation","url":"https://arxiv.org/html/2603.10143"},{"title":"AgentIR: Reasoning-Aware Retrival for Deep Research Agents","url":"https://arxiv.org/html/2603.04384v1"}]

The search has returned several highly relevant papers from arXiv 2026 on retrieval, reasoning, and related topics. Here are the key findings:

## Main Results:

**1. AgentIR: Reasoning-Aware Retrieval for Deep Research Agents (2603.04384)**

Deep Research agents generate explicit natural language reasoning before each search, revealing rich intent and context that existing retrievers entirely ignore. The paper proposes Reasoning-Aware Retrieval, which jointly embeds the reasoning trace alongside the agent's query, learning a retriever that leverages the rich intent and contextual information expressed in agent reasoning.

**2. Reasoning by Exploration (RoE) (2510.07484)**

Unlike traditional two-stage GraphRAG pipelines where a retriever extracts a static subgraph before reasoning begins, RoE enables a single LLM to actively explore the entire knowledge graph step by step, formulating reasoning as an exploration process over a knowledge graph. The framework includes a reinforcement learning stage that allows the model to interact with the knowledge graph and refine its exploration strategy through feedback, promoting broader and more diverse exploration behaviors.

**3. Reason and Verify Framework (2603.10143)**

The paper proposes a domain-specific RAG framework that integrates explicit reasoning and faithfulness verification, with neural query rewriting, cross-encoder reranking, and a rationale generation module that grounds sub-claims in specific evidence spans.

These papers demonstrate recent advances in differentiating retrieval pipelines based on reasoning intent, incorporating verification mechanisms, and enabling more dynamic exploration strategies in retrieval-augmented generation systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aecf9811-d8ab-47c1-a116-99852889797f",
  "isSidechain": false,
  "promptId": "afc6e2fe-4901-4946-8533-77cf3ebefba5",
  "type": "user",
  "uuid": "38f799a0-41c3-438a-8f42-471e95d78660",
  "toolUseResult": {
    "query": "\"retrieval intent\" \"verification\" \"exploration\" OR \"discovery\" reasoning chain differentiated pipeline arxiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Gibs7wbdRamEzYXr6j3tVs",
        "content": [
          {
            "title": "From Web Search towards Agentic Deep ReSearch: Incentivizing Search with Reasoning Agents",
            "url": "https://arxiv.org/html/2506.18959v1"
          },
          {
            "title": "Reasoning by Exploration: A Unified Approach to Retrieval and Generation over Graphs",
            "url": "https://arxiv.org/html/2510.07484"
          },
          {
            "title": "Reasoning in Trees: Improving Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2601.11255"
          },
          {
            "title": "AgentIR: Reasoning-Aware Retrieval for Deep Research Agents",
            "url": "https://arxiv.org/html/2603.04384"
          },
          {
            "title": "A Survey on Retrieval And Structuring Augmented Generation",
            "url": "https://arxiv.org/pdf/2509.10697"
          },
          {
            "title": "[2603.04384] AgentIR: Reasoning-Aware Retrieval for Deep Research Agents",
            "url": "https://arxiv.org/abs/2603.04384"
          },
          {
            "title": "A Survey of RAG-Reasoning Systems in LLMs",
            "url": "https://arxiv.org/pdf/2507.09477"
          },
          {
            "title": "Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches",
            "url": "https://arxiv.org/html/2510.04905v1"
          },
          {
            "title": "Reason and Verify: A Framework for Faithful Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2603.10143"
          },
          {
            "title": "AgentIR: Reasoning-Aware Retrival for Deep Research Agents",
            "url": "https://arxiv.org/html/2603.04384v1"
          }
        ]
      },
      "The search has returned several highly relevant papers from arXiv 2026 on retrieval, reasoning, and related topics. Here are the key findings:\n\n## Main Results:\n\n**1. AgentIR: Reasoning-Aware Retrieval for Deep Research Agents (2603.04384)**\n\nDeep Research agents generate explicit natural language reasoning before each search, revealing rich intent and context that existing retrievers entirely ignore. The paper proposes Reasoning-Aware Retrieval, which jointly embeds the reasoning trace alongside the agent's query, learning a retriever that leverages the rich intent and contextual information expressed in agent reasoning.\n\n**2. Reasoning by Exploration (RoE) (2510.07484)**\n\nUnlike traditional two-stage GraphRAG pipelines where a retriever extracts a static subgraph before reasoning begins, RoE enables a single LLM to actively explore the entire knowledge graph step by step, formulating reasoning as an exploration process over a knowledge graph. The framework includes a reinforcement learning stage that allows the model to interact with the knowledge graph and refine its exploration strategy through feedback, promoting broader and more diverse exploration behaviors.\n\n**3. Reason and Verify Framework (2603.10143)**\n\nThe paper proposes a domain-specific RAG framework that integrates explicit reasoning and faithfulness verification, with neural query rewriting, cross-encoder reranking, and a rationale generation module that grounds sub-claims in specific evidence spans.\n\nThese papers demonstrate recent advances in differentiating retrieval pipelines based on reasoning intent, incorporating verification mechanisms, and enabling more dynamic exploration strategies in retrieval-augmented generation systems."
    ],
    "durationSeconds": 7.139722208999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "aecf9811-d8ab-47c1-a116-99852889797f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-16T01:50:07.373Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do one more search specifically for any work that has already done what this proposal proposes — classifying retrieval intent within reasoning chains and applying different retrieval strategies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38f799a0-41c3-438a-8f42-471e95d78660",
  "isSidechain": false,
  "requestId": "req_011Cb5QebCmCnUjaNLf7b8qW",
  "type": "assistant",
  "uuid": "1b898861-5319-47c4-a87b-875745ff9c3c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Sherr9iLExLSh1tJHvBUk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 848,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 35479,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1006,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 848,
          "output_tokens": 129,
          "cache_read_input_tokens": 35479,
          "cache_creation_input_tokens": 1006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1006
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

_source line 33 · 2026-05-16T01:50:08.439Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JvCzkEANjbfLmst1Wr79st`</summary>

```json
{
  "query": "adaptive query construction exploration confirmation retrieval augmented reasoning NLI reranking claim-contrastive 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b898861-5319-47c4-a87b-875745ff9c3c",
  "isSidechain": false,
  "requestId": "req_011Cb5QebCmCnUjaNLf7b8qW",
  "type": "assistant",
  "uuid": "548a59ee-f5d0-4f84-9b05-eeb6a61f020a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Sherr9iLExLSh1tJHvBUk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 848,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 35479,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1006,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 848,
          "output_tokens": 129,
          "cache_read_input_tokens": 35479,
          "cache_creation_input_tokens": 1006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1006
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

_source line 34 · 2026-05-16T01:50:14.862Z_

<details><summary>↩ Tool result · `toolu_01JvCzkEANjbfLmst1Wr79st`</summary>

```text
Web search results for query: "adaptive query construction exploration confirmation retrieval augmented reasoning NLI reranking claim-contrastive 2025 2026"

Links: [{"title":"FAIR-RAG: Faithful Adaptive Iterative Refinement for Retrieval-Augmented Generation","url":"https://arxiv.org/html/2510.22344v1"},{"title":"Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers","url":"https://arxiv.org/html/2506.00054v1"},{"title":"DS@GT at CheckThat! 2025: Evaluating Context and Tokenization Strategies for Numerical Fact Verification","url":"https://arxiv.org/html/2507.06195"},{"title":"Contrastive Retrieval-Augmented Generation on Experience","url":"https://aclanthology.org/2025.findings-acl.1224.pdf"},{"title":"Reinforced Informativeness Optimization for Long-Form Retrieval-Augmented Generation","url":"https://arxiv.org/html/2505.20825"},{"title":"Adaptive Retrieval for Reasoning-Intensive Retrieval","url":"https://arxiv.org/pdf/2601.04618"},{"title":"GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.","url":"https://github.com/liunian-Jay/Awesome-RAG"},{"title":"Retrieval-Augmented Generation for AI-Generated Content: A Survey | Data Science and Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s41019-025-00335-5"},{"title":"Reasoning in Trees: Improving Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2601.11255"},{"title":"Q-PRM: Adaptive Query Rewriting for Retrieval-Augmented ...","url":"https://aclanthology.org/2025.findings-emnlp.817.pdf"}]

I've completed a web search for that query. The results show several recent papers and research from 2025-2026 related to retrieval-augmented generation and related techniques:

## Key Findings:

**FAIR-RAG Framework (October 2025):** FAIR-RAG's adaptivity is dynamic and occurs within the iterative process, as it continually adapts its query generation strategy based on the evolving set of retrieved evidence.

**Comprehensive RAG Survey (May 2025):** The search returned a comprehensive RAG survey covering various retrieval-augmented generation architectures and enhancements, including discussions of R2AG (Retrieval information into RAG) which recursively reranks candidates during generation, dynamically prioritizing evidence based on the evolving answer state.

**Numerical Fact Verification (July 2025):** A CheckThat! 2025 submission describes a hybrid BM25 + transformer evidence retrieval-reranking pipeline, subsequently plugged into a ModernBERT Natural Language Inference (NLI) core.

**Contrastive Retrieval-Augmented Generation (July 2025):** A paper on CoRE (Contrastive Retrieval-Augmented Generation on Experience) was published at ACL 2025.

**Query Rewriting (November 2025):** A paper titled "Q-PRM: Adaptive Query Rewriting for Retrieval-Augmented Generation" was published in EMNLP 2025 Findings.

The search results indicate active research in adaptive query construction, reranking techniques, and the integration of NLI models within retrieval-augmented generation systems during 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "548a59ee-f5d0-4f84-9b05-eeb6a61f020a",
  "isSidechain": false,
  "promptId": "afc6e2fe-4901-4946-8533-77cf3ebefba5",
  "type": "user",
  "uuid": "40da37dc-9b33-4533-a372-076a7a4a10b9",
  "toolUseResult": {
    "query": "adaptive query construction exploration confirmation retrieval augmented reasoning NLI reranking claim-contrastive 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HatKb4oL8LicyH7u8XwWqp",
        "content": [
          {
            "title": "FAIR-RAG: Faithful Adaptive Iterative Refinement for Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2510.22344v1"
          },
          {
            "title": "Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers",
            "url": "https://arxiv.org/html/2506.00054v1"
          },
          {
            "title": "DS@GT at CheckThat! 2025: Evaluating Context and Tokenization Strategies for Numerical Fact Verification",
            "url": "https://arxiv.org/html/2507.06195"
          },
          {
            "title": "Contrastive Retrieval-Augmented Generation on Experience",
            "url": "https://aclanthology.org/2025.findings-acl.1224.pdf"
          },
          {
            "title": "Reinforced Informativeness Optimization for Long-Form Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2505.20825"
          },
          {
            "title": "Adaptive Retrieval for Reasoning-Intensive Retrieval",
            "url": "https://arxiv.org/pdf/2601.04618"
          },
          {
            "title": "GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.",
            "url": "https://github.com/liunian-Jay/Awesome-RAG"
          },
          {
            "title": "Retrieval-Augmented Generation for AI-Generated Content: A Survey | Data Science and Engineering | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s41019-025-00335-5"
          },
          {
            "title": "Reasoning in Trees: Improving Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2601.11255"
          },
          {
            "title": "Q-PRM: Adaptive Query Rewriting for Retrieval-Augmented ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.817.pdf"
          }
        ]
      },
      "I've completed a web search for that query. The results show several recent papers and research from 2025-2026 related to retrieval-augmented generation and related techniques:\n\n## Key Findings:\n\n**FAIR-RAG Framework (October 2025):** FAIR-RAG's adaptivity is dynamic and occurs within the iterative process, as it continually adapts its query generation strategy based on the evolving set of retrieved evidence.\n\n**Comprehensive RAG Survey (May 2025):** The search returned a comprehensive RAG survey covering various retrieval-augmented generation architectures and enhancements, including discussions of R2AG (Retrieval information into RAG) which recursively reranks candidates during generation, dynamically prioritizing evidence based on the evolving answer state.\n\n**Numerical Fact Verification (July 2025):** A CheckThat! 2025 submission describes a hybrid BM25 + transformer evidence retrieval-reranking pipeline, subsequently plugged into a ModernBERT Natural Language Inference (NLI) core.\n\n**Contrastive Retrieval-Augmented Generation (July 2025):** A paper on CoRE (Contrastive Retrieval-Augmented Generation on Experience) was published at ACL 2025.\n\n**Query Rewriting (November 2025):** A paper titled \"Q-PRM: Adaptive Query Rewriting for Retrieval-Augmented Generation\" was published in EMNLP 2025 Findings.\n\nThe search results indicate active research in adaptive query construction, reranking techniques, and the integration of NLI models within retrieval-augmented generation systems during 2025-2026."
    ],
    "durationSeconds": 6.417636473999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "548a59ee-f5d0-4f84-9b05-eeb6a61f020a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35 · 2026-05-16T01:50:14.869Z_

```json
{
  "parentUuid": "40da37dc-9b33-4533-a372-076a7a4a10b9",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "30d77cef-e0b7-493a-a36a-03b56196bfae",
  "timestamp": "2026-05-16T01:50:14.869Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 36 · 2026-05-16T01:51:00.218Z_

<details><summary>Logged reasoning block</summary>

```text
Based on my searches, I haven't found any work that directly pre-empts this proposal's core contribution. No existing system explicitly classifies retrieval intent as discovery vs. verification within reasoning chains AND applies structurally different query construction strategies. The closest work:

1. AgentIR encodes reasoning traces into retrieval but treats all calls uniformly
2. HARIS coordinates reasoning + search agents but uses uniform search
3. Veri-R1 trains verification-specific RL but uses uniform queries
4. ReaLM-Retrieve observes the distinction but doesn't operationalize it

So the novelty claim seems valid — no one has done exactly this. 

Now I need to dig into whether this novelty actually matters. The real risk is a trivial alternative: what if just applying a strong hybrid retrieval pipeline with NLI reranking to every call outperforms the intent-aware approach? That would make the classification step unnecessary. The proposal assumes NLI reranking helps verification but might hurt discovery by anchoring to existing claims, but this isn't validated. There's also the question of whether simpler baselines like AutoRefine already solve this problem.

Looking at the core assumptions: the bimodal split between discovery and verification queries comes from ReaLM-Retrieve's 31% finding, but whether heuristic rules can actually classify this reliably is untested. The claim that verification queries need disconfirming evidence that's anti-correlated with topical relevance is shaky—documents with disconfirming evidence are often topically relevant too, so the anti-correlation is really between evidential valence and relevance matching, which aren't necessarily opposed. And there's an open question about whether RL will actually discover sophisticated verification strategies within the training budget.

On novelty, this feels more like systems integration than a fundamental breakthrough—it's combining ReaLM-Retrieve's observation with existing techniques like contrastive retrieval and NLI reranking. The core idea that different retrieval intents deserve different treatment is intuitive. The RL-discovered query strategies could be genuinely novel if they surface surprising patterns, but that's speculative, and framing a hoped-for result as a major contribution before validation is premature.

For significance, the problem matters but the scope is narrow—it's one optimization within reasoning-augmented RAG, a specific niche. Reviewers would likely see this as a natural extension of prior work rather than a surprising finding. The related work section is thorough and well-positioned, though, and the execution planning is careful. Ultimately, this is a solid, well-engineered proposal, but the core contribution—classifying retrieval intent and applying different strategies—feels like the obvious next step rather than something unexpected.

I'm settling on around 25% for EMNLP main conference. The gap is real and no one's tackled this exact combination, but the insight itself isn't surprising, the trivial baseline of just using hybrid retrieval everywhere isn't addressed, and the RL-discovered strategies part remains speculative. The narrowness of the problem also limits how much impact this would have. ReaLM-Retrieve's observations and the proposed solution is elegant—the NLI model separation to avoid reward circularity shows deep thinking, and if RL discovers interesting query patterns, that would be genuinely novel. But the core contribution is operationalizing an existing observation, the binary intent taxonomy feels simplistic, and the key logical claim about verification needing disconfirming evidence is weakly argued. The trivial alternative threat goes unaddressed.

I'm settling on 20-28%, median 24%. The proposal actually has two layers: the intent classification with differentiated pipelines is clear but incremental, while the RL-discovered verification strategies are speculative but potentially interesting. Together they could work for ACL or EMNLP if results are strong, but evaluating the idea itself, this lands in "solid engineering, obvious next step" territory—and that's below the novelty bar for a top venue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30d77cef-e0b7-493a-a36a-03b56196bfae",
  "isSidechain": false,
  "requestId": "req_011Cb5QfP43i2Xndh2Pi3aEr",
  "type": "assistant",
  "uuid": "db1a4262-825a-4d60-8791-515ba80f2ba2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Eq4u94HJt1obvscToqXfQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2018,
      "cache_read_input_tokens": 36485,
      "output_tokens": 4880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2018,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4880,
          "cache_read_input_tokens": 36485,
          "cache_creation_input_tokens": 2018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2018
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

_source line 37 · 2026-05-16T01:52:15.791Z_

Now I have sufficient information to provide a thorough assessment. Here is my evaluation:

---

```
【阶段】: Triage

【Trivial Alternative 检验】:
存在一个严重的 trivial alternative 威胁，proposal 未充分回应：

**为什么不对所有 retrieval call 都使用 hybrid BM25+dense+NLI reranking？** 如果 NLI-based contrastive reranking 能提高 verification query 的质量，为什么它不会同时提高 discovery query 的质量？proposal 声称 BM25 适合 discovery 因为"keyword-rich"，但这是假设而非论证。一个不需要任何 intent classification 的 trivial baseline —— 统一使用更强的 hybrid pipeline —— 可能达到类似效果且更简单。如果这个 baseline 表现接近，那么 intent classification 的增量价值（也就是整篇论文的核心贡献）就被消解了。

Proposal 计划了 BM25-only ablation（dual-intent tokens + 标准 retrieval），但这测试的是 "intent tokens 本身有没有用"，而非 "intent classification vs. 统一用更强 pipeline"。真正致命的 ablation 是：**对所有 query 统一使用 hybrid+NLI，不做 intent classification**。这一组被遗漏。

第二个 trivial alternative：AutoRefine 的 &lt;refine> step 在 post-retrieval 阶段蒸馏证据，已经在 HotpotQA/MuSiQue 上取得了大幅提升。如果 post-retrieval refinement 能弥补 query construction 阶段的不足，upstream 的 intent differentiation 增量价值可能很小。

**增量价值辩护（proposal 可以但未能做到的）：** intent classification 的真正价值应该在于 verification mode 主动寻找 disconfirming evidence（通过 contrastive query），这是一种 structurally different 的检索意图，不能通过简单使用更强的 pipeline 来实现。但 proposal 对"为什么 disconfirming evidence 不能通过统一 pipeline 获取"的论证薄弱。


【前提假设检验】:
核心 claim 的逻辑链中有 3 个未经充分验证的假设：

1. **"Verification query 需要 disconfirming evidence，而这与 topical relevance 信号反相关"** —— 这是核心逻辑的关键环节，但论证不足。包含 refuting evidence 的文档往往也是高度 topically relevant 的（例如，反驳 "X 出生在纽约" 的文档通常也是关于 X 的）。真正反相关的是 evidential valence 和 retrieval signal，但 dense retrieval 的 semantic matching 本身并不只优化 topical relevance —— 它可以捕捉到 semantic 层面的 contrastive 关系。这个假设如果不成立，整个 "为什么需要 differentiated pipeline" 的论证就塌了。

2. **"Heuristic rules 可以可靠地从 reasoning traces 中分类 intent"** —— 虽然设置了 75% accuracy 的 go/no-go 门槛，但 heuristic classification 的噪声在 RL 训练中会被放大。如果 30% 的 intent labels 是错误的，RL 在错误 label 上训练的 query construction 策略可能比不分类更差。Proposal 假设 "默认 fallback 到 discovery 是安全的"，但如果 heuristic 把 discovery 错标为 verification（false positive），会在不需要 contrastive query 的地方强行使用 contrastive pipeline，可能降低性能。

3. **"500 GRPO steps 足以让 RL 发现 sophisticated verification query strategies"** —— 这被定位为 "co-equal contribution"，但 RL 在 500 steps 内是否能在 query formulation 这个 secondary action space 上学到 beyond-template 的策略是未经验证的。Proposal 引用 RAFTS 证明 "LLM-generated contrastive formulations outperform templates"，但 RAFTS 使用的是大模型 zero-shot generation，不是 7B 模型在 500 RL steps 内学习的结果。将一个希望性发现定位为 co-equal contribution 是有风险的。


【3 维度打分】:

1. Novelty: 【弱-中】
   
   核心贡献是 "operationalize an existing observation" —— 将 ReaLM-Retrieve Section 6.9 中已经识别出的 verification retrieval pattern 显式化，配以不同的检索 pipeline。这是一个 natural next step，而非 surprising insight。任何仔细阅读 ReaLM-Retrieve 的研究者都可能想到 "为什么不根据 intent 使用不同策略"。
   
   与最相关 5-10 篇近期工作比较后的真实 novelty delta：
   - vs. ReaLM-Retrieve: delta 是 "显式分类 + 不同 pipeline"，属于 operationalization
   - vs. Veri-R1: delta 是 "differentiated query construction"，但 Veri-R1 本身只用 3B 模型，场景不完全可比
   - vs. RAFTS: delta 是 "集成到 RL 循环"，属于 integration
   - vs. AutoRefine: delta 是 "pre-retrieval intent 分类 vs. post-retrieval refinement"，是互补而非替代
   - vs. HARIS: delta 是 "binary intent + differentiated pipeline vs. hierarchical agents"，不同设计但解决类似问题
   
   剔除 surface differences（不同的 token format、不同的 pipeline 组合）之后，核心 insight 只有一条：**retrieval intent 应该被显式分类并用不同策略处理**。这更接近 engineering contribution 而非 conceptual breakthrough。
   
   第二个贡献 "RL-discovered query strategies" 在实验之前只是一个希望，不能作为 novelty 评估的依据。

2. Significance: 【中】
   
   研究问题是重要的 —— reasoning-augmented retrieval 是当前 NLP 的热点方向，如何提升 retrieval 质量确实是关键瓶颈（Shakya et al. 2026 的发现强化了这一点）。
   
   但显著性受限于：
   - **结果预期方向的可预测性**：如果 differentiated retrieval 表现更好，审稿人大概率会说 "I would have guessed this" 而非 "surprising"。Binary intent classification 提升性能是直觉上合理的结果。
   - **问题的窄度**：这是 reasoning-augmented RAG 中 query construction 阶段的一个 specific 优化。影响面限于使用 RL-trained reasoning+retrieval 的系统。
   - **可推广性受限**：binary taxonomy（discovery/verification）是否是最优分类？框架声称可扩展，但论文只测试 binary。
   
   如果结果是 negative（differentiation 不帮助或帮助很小），论文的贡献更多是 empirical insight（"显式分类不如隐式学习"），这也有价值但 significance 更低。

3. Related Work: 【强】
   
   Related work 覆盖极为全面。我在 web search 中未找到 proposal 遗漏的重要近期工作。对每篇相关工作的差异化定位准确且清晰。特别值得肯定的是：
   - 对 ReaLM-Retrieve、Veri-R1、HARIS 等最近期工作的深入分析
   - 对 gap 的结构化总结（5 个轴向的系统化梳理）
   - 对每个相关方法"做了什么 + 没做什么"的精确定位
   
   这是整个 proposal 最强的部分。唯一微弱的遗漏：没有充分讨论 FAIR-RAG（adaptive iterative refinement）和 Q-PRM（adaptive query rewriting），但这些不直接威胁 novelty claim。


【概率估计】: [18% - 28%] 中位 22%

【估计理由】:
Related Work 维度强（不拉后腿），但 Novelty 弱-中 和 Significance 中 共同限制了上界。

核心问题在于：这篇论文的 intellectual contribution 是 "operationalize an existing observation with known techniques"。Binary intent classification 是 obvious next step；hybrid BM25+dense+NLI 是已知技术的组合；GRPO training 是在 Search-R1 框架上的增量修改。审稿人最可能的反应是 "reasonable engineering contribution, but the core idea is not surprising enough for main conference"。

概率没有落入 15-18% 区间是因为：(a) gap 确实存在且被充分论证，(b) related work 定位清晰，(c) 如果 RL-discovered query patterns 出现 surprising 结果，论文有上行空间。但这个上行空间依赖于实验结果，而非 idea 本身的质量。

概率没有达到 28%+ 是因为：(a) trivial alternative 威胁严重且未回应，(b) 核心 claim 的前提假设（disconfirming evidence 与 topical relevance 反相关）论证薄弱，(c) "RL-discovered strategies" 作为 co-equal contribution 在实验前是空洞的。

**限制上界的关键维度是 Novelty** —— 即使 significance 提升到"中-强"，idea 的 incremental nature（operationalize + integrate known techniques）在 top-tier 会议上是硬伤。

【主要风险】:
1. **Trivial alternative 被审稿人发现**：审稿人大概率会问 "为什么不对所有 query 统一使用你的 hybrid+NLI pipeline？如果统一使用更强 pipeline 效果接近，intent classification 的价值在哪？" 如果这组 ablation 结果不利，论文核心贡献被消解。
2. **"Operationalize an obvious observation" 被视为 incremental**：核心 insight 来自 ReaLM-Retrieve 的 Section 6.9，proposal 本质上是 "take their observation and act on it"。审稿人可能判定这是一个 well-executed follow-up study 而非独立的 main conference contribution，尤其在 novelty 维度给出 borderline-reject 分数。
```

Sources:
- [AgentIR: Reasoning-Aware Retrieval for Deep Research Agents](https://arxiv.org/abs/2603.04384)
- [HARIS: Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification](https://arxiv.org/html/2506.07528v1)
- [Reason and Verify: A Framework for Faithful Retrieval-Augmented Generation](https://arxiv.org/html/2603.10143)
- [Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](https://arxiv.org/pdf/2503.09516)
- [RAFTS: Retrieval Augmented Fact Verification by Synthesizing Contrastive Arguments](https://arxiv.org/html/2406.09815v1)
- [ReaLM-Retrieve: When to Retrieve During Reasoning](https://arxiv.org/html/2604.26649)
- [DualRAG: A Dual-Process Approach to Integrate Reasoning and Retrieval for Multi-Hop QA](https://arxiv.org/html/2504.18243)
- [FAIR-RAG: Faithful Adaptive Iterative Refinement for RAG](https://arxiv.org/html/2510.22344v1)
- [Q-PRM: Adaptive Query Rewriting for RAG](https://aclanthology.org/2025.findings-emnlp.817.pdf)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db1a4262-825a-4d60-8791-515ba80f2ba2",
  "isSidechain": false,
  "requestId": "req_011Cb5QfP43i2Xndh2Pi3aEr",
  "type": "assistant",
  "uuid": "e48e586a-cafa-4e38-afb2-9698af86d419",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Eq4u94HJt1obvscToqXfQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2018,
      "cache_read_input_tokens": 36485,
      "output_tokens": 4880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2018,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4880,
          "cache_read_input_tokens": 36485,
          "cache_creation_input_tokens": 2018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2018
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

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Dual-Intent Retrieval: Intent-Differentiated Query Formulation for Reasoning-Augmented RAG  **状态**: 待审阅   **级别**…",
  "leafUuid": "e48e586a-cafa-4e38-afb2-9698af86d419",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate dual-intent retrieval proposal",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Dual-Intent Retrieval: Intent-Differentiated Query Formulation for Reasoning-Augmented RAG  **状态**: 待审阅   **级别**…",
  "leafUuid": "e48e586a-cafa-4e38-afb2-9698af86d419",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate dual-intent retrieval proposal",
  "sessionId": "b8aff3a6-0b8d-43d9-9984-5455ff59a891"
}
```

---
